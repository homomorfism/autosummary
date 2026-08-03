# Convolutional Architectures and Beyond

## Important Convolutional Architectures *[12:08]*

### AlexNet and the Dawn of Model Parallelization
The first convolutional network to decisively beat classical computer vision methods on ImageNet was **AlexNet** (Krizhevsky, Sutskever, Hinton, 2012). It cut the error rate from about 22–23 % down to 13 %, a jump so large that the next year’s leaderboard consisted entirely of convolutional networks. Beyond the architecture itself, AlexNet introduced the first industrial-scale instance of **model parallelization**. Because the model was too large for a single GPU, it was split into two pipelines that exchanged information only at a couple of points. Today this is still the key idea when a network does not fit on one GPU: you place different weight tensors on different devices, and PyTorch handles the communication automatically. The alternative, **data parallelization**, simply distributes different mini-batch examples to different GPUs and averages their weight updates – it scales the mini-batch size without changing the model.

### VGG: Stacking Small Filters
The **VGG** (Visual Geometry Group) network established that a stack of several $3 \times 3$ convolutions can replace one large convolution. A $3 \times 3$ convolution looks at a small neighbourhood; stacking two such layers gives an effective receptive field of $5 \times 5$, and stacking three gives $7 \times 7$. The number of weights drops dramatically compared with a single large filter, and the extra depth acts as an additional structural regularisation: the network is forced to process the input in the same way across different locations. Modern specialised GPU primitives are heavily optimised for $3 \times 3$ convolutions, making this design even more practical.

### Inception and “Network in Network”
The **Inception** (GoogLeNet) family pushes the “network in network” idea: instead of relying on a single convolutional filter, an Inception unit runs several parallel threads—$1 \times 1$, $3 \times 3$, $5 \times 5$ convolutions, and even pooling—and concatenates their outputs. This treats each spatial tile with a small custom network rather than a mere linear filter. Later versions (Inception v2/v3) further factorise large filters: an $n \times n$ convolution is replaced by a sequence of $n \times 1$ and $1 \times n$ convolutions, saving even more parameters. Inception v3 also introduced **label smoothing**: instead of the hard one-hot target $q(k)=[k=y]$, the network is trained with

$$q'(k) = (1 - \epsilon)\,[k=y] + \epsilon\,u(k),$$

where $u(k)$ is a prior (usually uniform). This keeps the softmax arguments from growing unboundedly and reduces overconfidence.

### Residual Networks: The Revolution of Depth
A deep plain network suffers from vanishing gradients: when a layer saturates, its derivative becomes tiny and cuts off gradient flow to all earlier layers. **ResNet** solves this with a skip-connection that adds the input back to the output:

$$y^{(k)} = F(x^{(k)}) + x^{(k)}.$$

Now the gradient becomes

$$\frac{\partial y^{(k)}}{\partial x^{(k)}} = 1 + \frac{\partial F(x^{(k)})}{\partial x^{(k)}},$$

so even when $F$ saturates and its derivative approaches zero, the gradient still propagates through the identity term. This simple idea, which Kaiming He called the “revolution of depth”, immediately allowed networks with 150, 200, or even more layers to train reliably. In practice, ResNets stop improving beyond about 200 layers, but they never break.  

A closely related design is the **highway network**, where the output is a convex combination of the input and the transformed signal:

$$y^{(k)} = C(x^{(k)})\,x^{(k)} + T(x^{(k)})\,F(x^{(k)}),\qquad C = 1 - T.$$

Empirical evidence shows that keeping the residual path as “straight” as possible (i.e., just addition without gating) works best.

### Bottlenecks, Group Convolutions, and the Split‑Transform‑Merge Idea *[26:06]*
Even with convolutions, the weight tensor of a typical layer with $D$ input channels and $D'$ output channels can be large ($D \times W \times H \times D'$; e.g. $256 \times 3 \times 3 \times 256 \approx 590\,k$). A **bottleneck** tries to shrink this by first projecting to a much smaller number of channels with a $1 \times 1$ convolution, performing the expensive spatial convolution in the low‑dimensional space, and then projecting back with another $1 \times 1$ convolution.

A single bottleneck, however, is problematic: compressing a rich vector of (say) $256$ features down to $32$ loses information, and the final expansion cannot recover it. If one were content with only $32$ features, the previous layer could simply produce $32$ channels directly. The bottleneck therefore makes sense only when it is replicated several times in parallel. This is the **split‑transform‑merge** paradigm:

- **Split** the input channels into several groups, each processed by its own bottleneck.
- **Transform** each group independently—possibly with different learned weights.
- **Merge** the results, typically by concatenation.

For instance, taking $D=256$ and reducing to $32$ channels inside each of eight parallel pathways, and then concatenating the outputs back to $256$, replaces the large weight tensor with eight small ones. The weight saving is no longer $25\times$ (as with a single bottleneck) but roughly $4\times$, which is still substantial. More importantly, each pathway learns a **different projection** onto a low‑dimensional subspace. The network effectively captures several distinct “views” of the high‑dimensional feature space. This is not a mere compression trick—learning multiple complementary projections often works better than processing the whole feature vector directly, and even random projections can be helpful; here the projections are learned and task‑driven.

The split‑transform‑merge pattern appears explicitly in **ResNeXt**, where a ResNet block is replaced by a set of parallel convolutional paths (group convolutions) whose outputs are summed. It is also a direct descendant of the Inception unit and is closely related to **group convolutions**, first used in AlexNet for parallelisation across GPUs; groups naturally tend to specialise in different types of features.

### Inception v4 and Inception‑ResNet *[42:47]*
The later Inception networks further simplified and standardised the building blocks. **Inception v4** introduced a uniform “stem” and three basic block types (A, B, C), together with dedicated **reduction blocks** that use strided convolutions (and occasionally pooling) to halve the spatial dimensions. Instead of a fixed pooling layer, these reduction blocks learn how best to downsample. **Inception‑ResNet** then added residual connections directly inside the Inception blocks, yielding a family of backbones that were state‑of‑the‑art around 2016. Inception‑ResNet-v2 was especially influential. For downstream tasks (object detection, segmentation) where labelled data is scarce, the standard recipe is to take a network pre‑trained on ImageNet, remove its classification head, and use the remainder as a fixed or fine‑tuned **feature extractor** (a **backbone**). Inception‑ResNet models served as highly effective backbones for years.

### Towards Efficient Networks: SqueezeNet, MobileNet, EfficientNet *[46:59]*
Two different resources matter for practical deployment:

- **Memory** – the total number of parameters (weights). A smaller footprint is essential for mobile or embedded devices.
- **Latency** – the time a forward pass takes, which depends primarily on the *number of layers* (sequential steps) and secondarily on the layer sizes, once the model fits on the accelerator.

**SqueezeNet** targets memory with **fire modules**: a *squeeze* layer of $1 \times 1$ convolutions reduces the channel count, followed by an *expand* layer mixing $1 \times 1$ and $3 \times 3$ convolutions. Delaying spatial downsampling as long as possible keeps activation maps large, which helps accuracy despite the parameter reduction. SqueezeNet achieves 50× fewer parameters than AlexNet at comparable accuracy.

**MobileNet** focuses on latency‑sensitive mobile applications. It uses **depthwise separable convolutions**: a standard convolution is factorised into a *depthwise* convolution (one independent filter per input channel) and a pointwise $1 \times 1$ convolution. The saving in both parameters and FLOPs is enormous, with only a small drop in accuracy.

**EfficientNet** (Tan & Le, 2019) was discovered by **neural architecture search**. The key insight is **compound scaling**: a convolutional network can be scaled along three dimensions—depth (number of layers), width (channel count), and resolution (input pixel count). If the depth grows by factor $\alpha^\phi$, the width by $\beta^\phi$, and the resolution by $\gamma^\phi$, the total parameter count scales roughly as $(\alpha \cdot \beta \cdot \gamma)^\phi$. EfficientNet uses an evolutionary search to find the optimal balance $\alpha, \beta, \gamma$ for a base model, then scales it up with a single compound coefficient $\phi$. The resulting family defines the **Pareto frontier** on an accuracy‑vs‑parameter plot: for every given size it gives the best accuracy, and for every target accuracy it gives the smallest network. EfficientNet remains the dominant CNN backbone for many tasks, even as transformers have taken over elsewhere.

---

## Batch Normalization and Normalization Variants *[56:14]*

### Internal Covariate Shift and Batch Normalization
During training, each layer’s weight update changes the distribution of its outputs, which in turn forces the next layer to re‑adapt. This **internal covariate shift** slows down learning and can drive neurons into saturated regimes. Normalising the outputs of each layer seems desirable, but naive normalisation with the full dataset or with full whitening is computationally prohibitive and interferes with gradient updates (e.g. biasing can diverge).

**Batch normalisation** (BN) solves this by normalising each feature over the current mini‑batch:

$$\hat{x}_k = \frac{x_k - \mathbb{E}[x_k]}{\sqrt{\mathrm{Var}[x_k]}},$$

where the statistics are computed on the mini‑batch. To prevent the transformation from removing all non‑linearity (sigmoids would become almost linear near zero), learnable scale and shift parameters $\gamma_k$, $\beta_k$ are introduced:

$$y_k = \gamma_k \hat{x}_k + \beta_k.$$

When $\gamma_k = \sqrt{\mathrm{Var}[x_k]}$ and $\beta_k = \mathbb{E}[x_k]$, the BN layer can simply pass the input unchanged.

### Why Batch Norm Works
Although BN was originally motivated by reducing internal covariate shift, later studies showed that its benefits do not really come from that. BN smooths the loss landscape (reducing the Lipschitz constant), decouples the direction and length of weight vectors, and often leads to linear convergence of gradient descent. In practice it acts as a regulariser, making dropout unnecessary.

### A Zoo of Normalization Schemes
All modern normalisation methods share the same core operations but differ in the dimensions over which the statistics are computed. For a feature tensor with shape $N \times C \times H \times W$ (batch, channels, spatial):

- **Batch Norm** – over $(N, H, W)$, i.e. per channel across the mini‑batch and spatial locations. Standard for CNNs.
- **Layer Norm** – over $(C, H, W)$, i.e. over the whole feature vector of one sample. No dependency on the mini‑batch; used extensively in transformers (where batch size is often small).
- **Instance Norm** – over $(H, W)$ only, per sample and per channel. Used in style transfer (AdaIN).
- **Group Norm** – splits channels into groups and normalises over each group’s spatial dimensions. Paired with weight standardisation in Big Transfer (BiT).
- **Weight Standardisation** – normalises the weights themselves rather than the activations, channel‑wise, smoothing gradients during backpropagation.

The choice is largely dictated by the architecture and the effective batch size that can be used.

---

## Recurrent Neural Networks *[58:53]*

### Sequence Data and Problem Types
Many real‑world inputs are inherently sequential: financial time series, sound (a sequence of amplitude samples or spectral frames), video (a sequence of images), and especially text (a sequence of tokens). Different problem formulations arise:

- **Many‑to‑one** – a sequence input and a single output (e.g. text classification, sentiment analysis).
- **One‑to‑many** – a single input produces a sequence (e.g. image captioning).
- **Sequence‑to‑sequence** – input and output are both sequences, possibly of different lengths (e.g. machine translation).
- **Sequence labelling** – input and output are aligned sequences of the same length (e.g. part‑of‑speech tagging, frame‑wise video annotation).

A sliding‑window convolutional approach can handle sequences to some extent, but it fundamentally lacks a mechanism to remember tokens that occurred long before the current window. Understanding a paragraph requires holding information from its beginning.

### The Recurrent Core: Hidden State and Weight Sharing
An **RNN** processes a sequence $x_1, x_2, \dots, x_T$ one element at a time while maintaining a **hidden state** vector $h_t$. The state is updated recursively:

$$h_t = f(x_t, h_{t-1}) .$$

The same function $f$ (and therefore the same weight matrices) is re‑used for every time step. This weight sharing means:

- The network can handle sequences of arbitrary length.
- Every example in the sequence contributes to the gradient of the shared weights, just as a convolutional filter receives gradients from every spatial position.

The simplest recurrent cell is a linear map followed by a non‑linearity:

$$a_t = b + W h_{t-1} + U x_t, \quad h_t = \phi(a_t),$$

with $\phi$ typically $\tanh$ or a similar saturating activation. An output $y_t$ can be produced at every step or only after the last hidden state, depending on the task.

### Bidirectional RNNs
A single‑direction RNN only sees the past context. For tasks such as sequence labelling, the prediction at position $t$ should ideally use both left and right context. A **bidirectional RNN** runs two independent networks—one left‑to‑right, one right‑to‑left—and concatenates (or otherwise merges) their hidden states at each step. This gives the predictor access to the full surrounding context. The exception is tasks where future information is genuinely unavailable, for example **language modelling** (predicting the next word) or **online object tracking**, which must process a live stream without look‑ahead.

### Training RNNs: Backpropagation Through Time
Training an RNN means computing the gradient of a loss $L$ (defined on the final output or on each step) with respect to the shared weight matrices. The computational graph is a **unrolled** chain: at each step the same $W$ participates both in the forward computation and in the loss. Consequently, the total gradient is a sum over all times:

$$\frac{\partial L}{\partial W} = \sum_{t=1}^{T} \frac{\partial L}{\partial h_t} \frac{\partial h_t}{\partial W}.$$

This is the same effect that makes weight sharing so effective—every time step provides a signal—but it also introduces a serious difficulty.

### Exploding and Vanishing Gradients
Consider a drastically simplified recurrence where $h_t = W h_{t-1}$ (ignoring inputs and non‑linearities). Then $h_T = W^{\,T} h_0$. The norm of $h_T$ behaves like $(\rho)^T \|h_0\|$, where $\rho$ is the **spectral radius** of $W$ (roughly, the factor by which multiplying by $W$ scales a vector). The same repeated multiplication occurs during the backward pass, because gradients flow through the transpose.

- If $\rho > 1$, the activations and gradients **explode** exponentially. This leads to numerical overflow, chaotic loss surfaces, and non‑sensical updates.
- If $\rho < 1$, the signals **vanish** exponentially. The network becomes unable to learn long‑range dependencies: the influence of early tokens on the loss quickly approaches zero.

Both regimes are common in practice, because it is very difficult to keep $\rho$ precisely at $1$ throughout training.

### Gradient Clipping
The exploding gradient problem has an elegantly simple solution: **gradient clipping**. Whenever the norm of a gradient exceeds a predefined threshold, the vector is rescaled to that threshold. There are two common variants:

```python
# Keras-style
sgd = optimizers.SGD(lr=0.01, clipnorm=1.)    # clip by norm
sgd = optimizers.SGD(lr=0.01, clipvalue=.05)  # clip every component
```

Geometrically, exploding gradients correspond to a near‑vertical “wall” in the loss landscape. Without clipping, an optimiser would bounce off the wall and fly far away. Clipping simply projects the step back, keeping the search in the well‑behaved region and preserving the general direction of the update. It is a standard, harmless component of RNN training.

Solving the *vanishing* gradient problem is more subtle and requires carefully designed recurrent units with built‑in gradient highways—a topic that leads directly to **LSTM** and **GRU** architectures, to be discussed next.
