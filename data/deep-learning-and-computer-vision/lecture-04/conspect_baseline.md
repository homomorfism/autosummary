# Convolutional Neural Networks

## Biological Motivation: The Visual Cortex *[09:44]*

Convolutional neural networks (CNNs) are a cornerstone of the deep learning revolution, and their design was partly inspired by the structure of the mammalian visual cortex. The seminal work by **Hubel and Wiesel** (who received the Nobel Prize for these studies) revealed how the brain processes visual information through a hierarchy of simple feature detectors.

Their key experimental breakthrough was the ability to fabricate micro‑electrodes fine enough to record the activity of a single neuron in a living brain—often that of a cat. By doing so they discovered that neurons in the very first processing stage (the primary visual cortex, V1) do not see the whole image; each neuron has a small **receptive field** and responds only to extremely simple patterns inside that field. For instance, a neuron might fire intensely for a bright vertical line and become almost silent as the line is rotated.

This immediately suggests a hierarchical organisation:
- The first layer extracts local primitives (edges, orientations).
- A second layer would combine these primitives into more complex shapes (e.g., a corner from a horizontal and a vertical line).

Hubel and Wiesel did identify neurons in the second visual area (V2) that responded to such combinations. However, they wisely stopped there. The true structure of the visual cortex is immensely more complicated. While a simplified picture shows layers V1 → V2 → V3 → V4 → V5/V6, the reality is a dense mesh of feed‑forward, feedback and lateral connections. The biological brain is **not a clean feed‑forward network**.

> **Important biological limitation:** A single biological neuron has exactly one output (its axon). To perform gradient descent, every node in a computational graph must implement at least two functions: a forward computation and a backward gradient computation. This is fundamentally impossible for a single neuron. Therefore, the human brain **cannot** train itself by gradient descent; it must rely on massive feedback loops and a different, still unknown learning mechanism. The analogy between artificial and biological neurons stops at the connectionist principle—a large composition of simple units can yield complex behaviour—and at the layered hierarchical organisation.

Nevertheless, the observed hierarchy of simple‑to‑complex features in the visual cortex was the conceptual seed for convolutional networks.

## From Biology to Computers: The Neocognitron and LeNet *[24:12]*

Building on this inspiration, **Kunihiko Fukushima** proposed the **Neocognitron** in 1979. It was a deep, multi‑layer architecture that used fixed filters (convolutions) to extract features across an image. Remarkably, the Neocognitron employed activations very similar to modern ReLU (the hinge‑shaped activation) decades before they became standard. However, the Neocognitron lacked **learning**—its filters were hand‑designed, not trained.

Convolutional networks in their modern, trainable form were developed in the late 1980s by **Yann LeCun** and his group. LeCun’s key contribution was making the convolution kernels **learnable** via backpropagation, and his architectures (such as LeNet) demonstrated the power of this idea on practical tasks like handwritten digit recognition.

## The Core Idea of Convolutional Neural Networks *[26:02]*

The fundamental assumption behind CNNs is **translation invariance of feature detectors**: if you are looking for a specific pattern (e.g., a boy’s face, a digit, a corner), exactly the **same** detector should be applied everywhere across the image. The location of the pattern changes the input, but the function that detects it remains identical.

This leads to the following pipeline:

1. **Tiling**  
   The input (an image, or any multi‑dimensional array) is divided into small, overlapping windows (tiles). Typically odd‑sized tiles such as $3\times3$ or $5\times5$ are used.

2. **Local processing**  
   A **small neural network**—in practice just a single fully‑connected layer—is applied to every tile.  
   This network receives the tile’s pixel values (flattened into a vector) and outputs a vector of new **features**.

3. **Forming the next representation**  
   Because each tile yields a feature vector and the tiles themselves form a spatial grid, the output of a convolutional layer is a three‑dimensional tensor:  
   $\text{height} \times \text{width} \times \text{number of features}$  
   (often called *channels* or *feature maps*).  
   The spatial dimensions may shrink unless special measures are taken (see padding later).

4. **Stacking**  
   This process can be repeated: the output tensor of one layer becomes the input of the next, which again is tiled, processed with a (new) small network, and so on. In this way the network builds a hierarchy of features, from simple edges to complex shapes.

The crucial gain is **weight sharing**. The *same* small weight matrix is reused for *every* tile. This means the number of trainable parameters does **not** depend on the size of the input image, only on the tile (kernel) size and the number of input/output channels. This drastically reduces the number of parameters compared to a fully‑connected layer and acts as a powerful **structural regulariser**: we are explicitly imposing that the same operation must be performed everywhere, which encodes the prior knowledge of translation invariance.

## Pooling Layers *[33:25]*

A drawback of stacking only convolutional layers is that the receptive field grows very slowly. With $3\times3$ kernels, each layer adds only **2** pixels to the effective field of view. To reach a receptive field covering a $256\times256$ image you would need about 130 layers, which is impractical. Therefore, classical CNNs introduce **pooling layers** to aggressively reduce the spatial dimensions.

A pooling layer operates on the output of a convolutional layer:
- It partitions the feature maps into small, **non‑overlapping** windows (almost always $2\times2$).
- For each window, it replaces the four values with a single summary statistic:
  - **Max‑pooling:** take the maximum.
  - **Average‑pooling:** take the mean.

Max‑pooling is overwhelmingly the standard choice. The intuitive justification is that for “presence” features (is a face, a corner, an edge present?), the maximum is the correct composition: if any tile in the window detected the object, the whole window should report its presence. Average‑pooling tends to dilute such strong signals. Features that measure continuous quantities (e.g., colour saturation) may benefit from averaging, but object‑oriented features obey the max law. Empirically, max‑pooling just works better.

With $2\times2$ pooling, the width and height are halved, reducing the number of features by a factor of four. Pooling layers have **zero trainable parameters**—they are deterministic down‑sampling operations.

## Formal Definition of Convolution and Pooling *[43:18]*

Let $x^l$ be the input feature map at layer $l$, with spatial dimensions and depth $D$.

**Convolution**  
A two‑dimensional convolution uses a kernel of size $(2d+1)\times(2d+1)$ and a weight tensor $W$ (also of shape $(2d+1)\times(2d+1)\times D \times D'$, where $D'$ is the desired number of output features). Concretely, for each output position $(i,j)$ and each output channel $c'$, the operation is:

$$
y^l_{i,j,c'} = \sum_{c=1}^{D} \;\sum_{-d \le a,b \le d} W_{a,b,c,c'} \; x^l_{i+a,\,j+b,\,c}
$$

In slides and simpler notation one often writes the per‑channel version as:

$$
y^l_{i,j} = \sum_{-d \le a,b \le d} W_{a,b} \; x^l_{i+a,\,j+b}
$$

(implicitly summing over input channels and using a separate kernel for each output channel).

A **nonlinearity** is then applied element‑wise:

$$
z^l_{i,j} = h(y^l_{i,j})
$$

In almost all modern CNNs, $h$ is the **ReLU** function: $h(u) = \max(0,u)$.

**Pooling**  
Max‑pooling (over a $(2d+1)\times(2d+1)$ window) is defined as:

$$
x^{l+1}_{i,j} = \max_{-d \le a,b \le d} \; z^l_{i+a,\,j+b}
$$

(Average‑pooling replaces $\max$ with the arithmetic mean.)

After several convolution‑pooling blocks the spatial dimensions become small enough that the whole tensor can be flattened and fed into one or more **fully‑connected layers** (the *classification head*).

## The Power of Weight Sharing: A LeNet Example *[52:45]*

To appreciate the parameter savings, consider a classical LeNet‑style network for grayscale $32\times32$ input (depth $1$). The architecture (depicted in many textbooks) proceeds as follows:

1. **Input:** $1 \times 32 \times 32$
2. **Conv1:** $5\times5$ kernel, 6 output features → output $6 \times 28 \times 28$  
   *Weights:* $1 \times 5 \times 5 \times 6 = 150$
3. **Max‑pooling1:** $2\times2$ → output $6 \times 14 \times 14$  
   *Weights:* **0** (deterministic)
4. **Conv2:** $5\times5$ kernel, 16 output features → output $16 \times 10 \times 10$  
   *Weights:* $6 \times 5 \times 5 \times 16 = 2400$
5. **Max‑pooling2:** $2\times2$ → output $16 \times 5 \times 5$  
   *Weights:* 0
6. **Fully‑connected 1:** The $16\times5\times5 = 400$ values are flattened and mapped to 120 neurons.  
   *Weights:* $400 \times 120 = 48\,000$ (plus biases)
7. **Fully‑connected 2:** 120 → 84  
   *Weights:* $120 \times 84 = 10\,080$
8. **Output (softmax):** 84 → 10  
   *Weights:* $84 \times 10 = 840$

Total trainable parameters ≈ $150 + 2400 + 48\,000 + 10\,080 + 840 \approx 61\,470$. Of these, only about $2550$ (roughly 4%) belong to the convolutional layers. Had the first layer been a naive fully‑connected transformation from $32\times32 = 1024$ pixels to a $28\times28\times6$ output, it would have required around **five million** weights. The convolutional structure slashes this to 150, directly encoding the intuition that a feature detector should be location independent. This is **structural regularisation**—hard‑coding equality constraints on weights—and it is the primary reason CNNs can scale to high‑resolution images.

## Backpropagation in CNNs and the Role of ReLU *[1:13:00]*

In a CNN, every weight in the kernel is reused across every spatial tile. In the backward pass, the gradient for that weight is the sum (by the chain rule) of all the individual gradients from each tile in which it participates. Thus a single weight receives gradient information from the **entire** image, which makes optimisation extremely stable.

This abundance of signal points makes **sparsity** desirable. With ReLU activations, many neurons output exactly zero for a given window. A zero activation stops gradient flow through that part of the graph for that tile, but the weight still receives updates from all the other tiles where the activation was positive. Sparsity therefore accelerates computation without harming learning—in fact, it acts as a mild regulariser. ReLU and convolutional weight sharing are an exceptionally well‑matched pair.

## Practical Techniques: Padding and Stride *[1:17:10]*

**Padding**  
Applying a $K \times K$ convolution reduces the spatial dimensions by $K-1$ (since border pixels cannot serve as the centre of a full window). To preserve the spatial size—often desired when stacking many layers—we can **pad** the input with extra values before the convolution. The two most common strategies:
- **Zero padding:** fill the out‑of‑bounds values with 0.
- **Mirror padding:** reflect the border pixels outward.

Zero padding sometimes creates artefacts near the border because windows there see many zeros. Mirror padding mitigates this but is slightly more expensive. The main goal is to let every original pixel be the centre of a window, so the output has the same height and width as the input.

**Stride**  
Instead of a pooling layer, one can reduce spatial dimensions by skipping pixels when placing windows. If windows are centred only on **every second pixel** (stride 2), the number of tiles is halved in each direction, and the output becomes roughly $W/2 \times H/2$. Crucially, no information is lost: every pixel is still covered by at least one window (often by two). This gives the same geometric down‑sampling as a $2\times2$ pooling layer, but without an explicit separate operation. The stride can be set independently for height and width (a pair of numbers), though it is usually the same in both directions.

## Trends: Moving Away from Pooling *[1:26:28]*

While pooling was standard in early CNNs, it has undesirable side‑effects: it eliminates many computational paths and can distort gradients. Modern architectures (e.g., Inception, ResNet) tend to replace explicit pooling with **strided convolutions** or small sub‑networks that accomplish spatial reduction while learning the best way to combine features. Pooling is far from obsolete, but the trend is to let the network learn its own down‑sampling rather than imposing a fixed max or average operation.
