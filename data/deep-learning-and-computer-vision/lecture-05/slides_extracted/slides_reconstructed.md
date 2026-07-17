# Convolutional Architectures and Beyond

## Important Convolutional Architectures

There is a huge number of different models based on the CNN idea. Most of them are accompanied by code, and many provide models pretrained on ImageNet or other large standard datasets. However, they are usually based on a few standard ideas, which we will now consider.

### AlexNet (Krizhevsky, Sutskever, Hinton, 2012)
The architecture that kick-started modern deep learning for computer vision. *(No additional textual details in the source.)*

### VGG
VGG (Oxford Visual Geometry Group) represents large convolutions as compositions of $3 \times 3$ convolutions. This reduces the number of weights and makes the network deeper. The VGG network was used in the ImageNet Large Scale Visual Recognition Competition (ILSVRC-2014). NVIDIA has been optimising GPUs especially for $3 \times 3$ convolutions.

### Inception (GoogLeNet)
Inception and GoogLeNet based on it use the “network in network” idea to reduce the number of weights even further. Another idea is to add additional classifiers (additional terms for the objective function).

#### Inception v2 and v3
In Inception v2 (Szegedy et al., 2015), $n \times n$ convolutions were replaced by $n \times 1$ and $1 \times n$ convolutions. Filter banks in Inception v2 became wide rather than deep. The same paper also introduced Inception v3, which uses RMSProp, factorised $7 \times 7$ convolutions, batch normalisation in the additional classifiers, and label smoothing.

#### Label Smoothing
In a regular classifier we train the softmax with a hard objective $q(k) = [k = y]$, i.e., the arguments of the softmax function “want” to grow unboundedly. As a result, the models overfit and become too certain. A possible solution is to optimise instead
$$q'(k) = (1 - \epsilon)[k = y] + \epsilon\, u(k)$$
for some prior distribution $u(k)$, for instance $u(k) = \frac{1}{K}$.

### ResNet
Residual learning: instead of learning a function directly, we train the differences (residues) between one layer and the next, so that gradients can flow with no obstacle. A function implemented by a residual unit looks like
$$y^{(k)} = F(x^{(k)}) + x^{(k)},$$
where $x^{(k)}$ is the input of layer $k$, $F$ is the function computed by the layer, and $y^{(k)}$ is the output that becomes $x^{(k+1)}$ for the next layer. The gradient can pass through and does not vanish when $F$ becomes saturated:
$$\frac{\partial y^{(k)}}{\partial x^{(k)}} = 1 + \frac{\partial F(x^{(k)})}{\partial x^{(k)}}.$$
This has allowed for very deep networks.

Another similar approach is highway networks by Jürgen Schmidhuber. There the output of layer $k$ is also represented as a combination of $x^{(k)}$ and $F(x^{(k)})$, but in a different way:
$$y^{(k)} = C(x^{(k)})\,x^{(k)} + T(x^{(k)})\,F(x^{(k)}),$$
where $C$ is the carry gate and $T$ is the transform gate; usually it is a convex combination, $C = 1 - T$. Practice shows that the residual connections should be as “straight” as possible.

ResNet variations and the revolution of depth (Kaiming He) further demonstrated the power of extremely deep convolutional networks.

### ResNeXt
ResNeXt (Xie et al., 2016) replaces ResNet units with “split-transform-merge” units, similar to Inception. The input is divided into blocks with respect to channels, and every block receives its own convolutions. This idea is reminiscent of group convolutions, already used in AlexNet for parallelisation; they yield a kind of specialisation in the resulting feature maps.

### Inception v4 and Inception‑ResNet
Another classic paper (Szegedy et al., 2016) introduced Inception v4 and Inception‑ResNet.

- **Inception v4** standardises everything and simplifies the units. First, a “stem” module is defined. Three basic blocks – A, B, and C – are used, together with special reduction blocks to reduce spatial dimensions.
- **Inception‑ResNet** adds residual connections to these Inception blocks. There is no pooling, but reduction blocks are still employed. The architecture becomes even simpler. Inception‑ResNet v2 is a refined version that performs very well in practice.

### SqueezeNet
SqueezeNet (Iandola et al., 2017) aims to drastically reduce the number of parameters:
- replace $3 \times 3$ filters with $1 \times 1$;
- reduce the number of input channels for the remaining $3 \times 3$ convolutions;
- delay downsampling as late as possible to keep activation maps large.

The key building block is the **fire module**:
- a *squeeze* convolutional layer (only $1 \times 1$ filters);
- an *expand* layer (a mix of $1 \times 1$ and $3 \times 3$ filters).

This yields about 50× fewer parameters than AlexNet, although there is a trade-off in accuracy.

### MobileNet
MobileNet (Howard et al., 2017) designs networks for mobile devices. It uses **depthwise separable convolutions**: decompose a standard convolution into a depthwise convolution (one filter per input channel) followed by a $1 \times 1$ convolution. The resulting layer has a more complex structure but far fewer weights. The overall architecture is not very deep. It saves many parameters at the price of a small decrease in quality.

### EfficientNet
EfficientNet (Tan, Le, 2019) applies neural architecture search to design state‑of‑the‑art networks at a fraction of the cost. A key insight is compound scaling: simultaneously scaling network width, depth, and input resolution yields better performance than scaling a single dimension.

---

## Batch Normalization

### The Internal Covariate Shift Problem
In deep networks, when we change the weights of a layer, the distribution of its outputs changes. The next layer then has to re‑train almost from scratch, because it did not expect these new outputs. Moreover, neurons may already have reached saturation, slowing down re‑training. This phenomenon – internal covariate shift – seriously impedes learning.

### Why Naïve Solutions Fail
- **Whitening after every layer**: consider a layer that simply adds a bias $b$ to its input $u$, producing $x = u + b$. If we normalise by subtracting the mean, $\hat{x} = x - \mathbb{E}[x]$, and then update $b := b + \Delta b$, the normalised output does not change:
$$u + b + \Delta b - \mathbb{E}[u + b + \Delta b] = u + b - \mathbb{E}[u + b].$$
The biases will grow unboundedly without affecting the normalised output, so training fails.
- **Normalisation as a layer**: $\hat{x} = \text{Norm}(x, X)$ requires the entire dataset $X$ to compute gradients $\frac{\partial \text{Norm}}{\partial x}$, $\frac{\partial \text{Norm}}{\partial X}$, and the covariance matrix $\text{Cov}[x] = \mathbb{E}_{x \in X}[xx^\top] - \mathbb{E}[x]\mathbb{E}[x]^\top$. This is computationally prohibitive.

### Batch Normalization (BN)
The solution is to normalise each component separately, not over the whole dataset but over the current mini‑batch – hence **batch normalisation**. For a component $x_k$,
$$\hat{x}_k = \frac{x_k - \mathbb{E}[x_k]}{\sqrt{\text{Var}[x_k]}},$$
where the statistics are computed over the current mini‑batch.

A new problem arises: nonlinearities can disappear because the normalised values almost always fall into the linear region of activation functions (e.g., sigmoid). To fix this, we introduce learnable shift and scale parameters:
$$y_k = \gamma_k \hat{x}_k + \beta_k = \gamma_k \frac{x_k - \mathbb{E}[x_k]}{\sqrt{\text{Var}[x_k]}} + \beta_k.$$
The parameters $\gamma_k$, $\beta_k$ are trained jointly with the network weights.

### What BN Actually Does
Although originally motivated by reducing internal covariate shift, subsequent research showed that BN’s effectiveness does not really depend on this. Nevertheless, BN helps with regularisation, makes dropout unnecessary, and improves training. Possible explanations include:
- BN smooths the gradients, reducing the Lipschitz constant (Santurkar et al., 2019);
- BN decouples the learning of the direction and length of weight vectors, which improves training;
- there are results showing that BN helps achieve linear convergence in ordinary gradient descent.

### Variants of Normalization
Many normalisation methods share the same general operations: compute statistics over some set, normalise, then transform with learned scale and shift parameters. They differ in *which dimensions* the statistics are computed over.

#### General Formulation
All methods compute mean and variance over a specified set of axes, normalise, and then apply an affine transformation $\gamma$, $\beta$.

- **Batch Normalization** – over the mini‑batch dimension ($N$). Commonly used for images.
- **Layer Normalization** – over all channels and spatial dimensions of a layer (i.e., over all features of a sample). Used mostly for vectors, in particular in transformers.
- **Instance Normalization** – over the spatial dimensions only ($H, W$), separately for each sample and channel. Used, e.g., in AdaIN for style transfer.
- **Group Normalization** – split channels into groups, then normalise over each group together with the spatial dimensions.
- **Weight Standardization** – instead of normalising activations, standardise the weights (per output channel). It effectively normalises the gradients during backpropagation. Group norm + weight standardisation were used in BiT (Big Transfer).

#### Summary and Further Developments
- Batch normalisation is not effective for recurrent networks (Laurent et al., 2016); recurrent batch normalisation was proposed (Cooijmans et al., 2016).
- Weight normalisation (Salimans and Kingma, 2016) transforms weights as $h_i = f\!\left(\frac{\gamma}{\|w_i\|} w_i^\top x + b_i\right)$, which rescales the gradient, stabilises its norm, and brings the covariance matrix closer to the identity.
- The landscape of normalisation methods is extensive and remains an active area of research (Huang et al., 2020).

---

## Working with Sequences

Sequences – financial time series, language, sound – give rise to various problems (sequence classification, sequence labelling, sequence generation, etc.).

A simple approach is to use a sliding window over the sequence. A more powerful idea is to maintain a hidden state that is updated as the network processes the sequence – this leads to *recurrent neural networks* (RNNs).

Although the computational graph appears to have cycles ($s_i = h(x_i, x_{i+1}, x_{i+2}, s_{i-1})$), backpropagation is possible by “unrolling” the recurrence in time:
$$y_6 = f(x_3, x_4, x_5, s_2) = f(x_3, x_4, x_5, h(x_2, x_3, x_4, s_1)) = f(x_3, x_4, x_5, h(x_2, x_3, x_4, h(x_1, x_2, x_3, s_0))).$$
Formally there is no problem, but practically we are dealing with a very deep network with many shared weights, which causes notorious training difficulties.

---

## Recurrent Neural Networks

### Simple RNN
Formally, a simple RNN step is:
$$a_t = b + W s_{t-1} + U x_t, \quad s_t = f(a_t),$$
$$o_t = c + V s_t, \quad y_t = h(o_t),$$
where $f$ is the recurrent nonlinearity and $h$ the output function.

Two major problems arise:
- **exploding gradients**,
- **vanishing gradients**.

### Exploding Gradients and Gradient Clipping
Because we repeatedly multiply by the same weight matrix $W$, the norm of the gradient grows or shrinks exponentially. When it explodes, we can simply bound the gradients from above:
- clip by norm: `clipnorm=1.`
- clip by value: `clipvalue=0.05`

This prevents extreme updates. Pascanu et al. (2013) illustrated this and showed that RNNs have “bifurcation points” where such instabilities originate.

### Bidirectional RNN
Sometimes context from both past and future is needed. A bidirectional RNN computes:
$$s_t = \sigma(b + W s_{t-1} + U x_t),$$
$$s'_t = \sigma(b' + W' s'_{t+1} + U' x_t),$$
$$o_t = c + V s_t + V' s'_t, \quad y_t = h(o_t).$$
This principle generalises to any recurrent architecture.

---

## LSTM and GRU

### LSTM (Long Short-Term Memory)

Vanishing gradients occur because the gradient must repeatedly pass through multiplication by $W$. To provide long‑term memory, the “constant error carousel” – a shortcut for gradients – is needed, very much like the residual connections in ResNet.

LSTM, developed in the mid‑1990s (Hochreiter & Schmidhuber, 1995, 1997; modern form by Gers & Schmidhuber, 2000), constructs a more complex unit that explicitly controls memory.

#### Vanilla LSTM
The LSTM cell maintains a **cell state** $c_t$ and a **hidden state** $h_t$. Gates control information flow:
- **candidate cell state**:
  $$c'_t = \tanh(W_{xc} x_t + W_{hc} h_{t-1} + b_{c'})$$
- **input gate** $i_t$, **forget gate** $f_t$, **output gate** $o_t$:
  $$i_t = \sigma(W_{xi} x_t + W_{hi} h_{t-1} + b_i)$$
  $$f_t = \sigma(W_{xf} x_t + W_{hf} h_{t-1} + b_f)$$
  $$o_t = \sigma(W_{xo} x_t + W_{ho} h_{t-1} + b_o)$$
- **cell state update**:
  $$c_t = f_t \odot c_{t-1} + i_t \odot c'_t$$
- **hidden state**:
  $$h_t = o_t \odot \tanh(c_t)$$

If the forget gate is fully open ($f_t = 1$), we have $c_t = c_{t-1} + i_t \odot c'_t$, so $\frac{\partial c_t}{\partial c_{t-1}} = 1$ – the constant error carousel.

#### Peephole Connections
A problem: the gates only see $h_{t-1}$, which is $o_{t-1} \odot \tanh(c_{t-1})$. If the output gate is closed, the LSTM behaviour becomes independent of the cell state. Peephole connections add the cell state directly to the gate computations:
$$i_t = \sigma(W_{xi} x_t + W_{hi} h_{t-1} + W_{pi} c_{t-1} + b_i)$$
$$f_t = \sigma(W_{xf} x_t + W_{hf} h_{t-1} + W_{pf} c_{t-1} + b_f)$$
$$o_t = \sigma(W_{xo} x_t + W_{ho} h_{t-1} + W_{po} c_{t-1} + b_o)$$

There are numerous LSTM variations; one can remove or add gates, peepholes, activation functions, etc. The extensive experimental comparison “LSTM: A Search Space Odyssey” (Greff et al., 2015) showed that some significantly simpler architectures (with one gate fewer) perform nearly as well as the vanilla LSTM.

### GRU (Gated Recurrent Unit)

Developed by Cho et al. (2014), GRU also implements the constant error carousel but is simpler than LSTM. It merges cell state and hidden state and uses two gates:

- **update gate** $u_t$ and **reset gate** $r_t$:
  $$u_t = \sigma(W_{xu} x_t + W_{hu} h_{t-1} + b_u)$$
  $$r_t = \sigma(W_{xr} x_t + W_{hr} h_{t-1} + b_r)$$
- **candidate hidden state**:
  $$h'_t = \tanh(W_{xh'} x_t + W_{hh'} (r_t \odot h_{t-1}))$$
- **hidden state update**:
  $$h_t = (1 - u_t) \odot h'_t + u_t \odot h_{t-1}$$

GRU uses fewer weight matrices (6 vs. 8 or 11 with peepholes) and fewer parameters, but is only slightly worse than LSTM. Thus, more GRUs can be fit under a given computational budget.

Other variations exist; Józefowicz, Zaremba, and Sutskever (2015) performed a huge evolutionary search over RNN architectures and identified several interesting alternative structures.
