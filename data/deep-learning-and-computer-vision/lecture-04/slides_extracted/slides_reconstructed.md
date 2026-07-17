# Convolutional Neural Networks

## Visual Cortex

Convolutional neural networks (CNNs) are an important part of the deep learning revolution. Their design is partly motivated by the visual cortex.

Hubel and Wiesel’s famous studies showed that first-level neurons activate for simple shapes, second‑level neurons activate for combinations of these simple shapes, third‑level… nope, they wisely didn’t go there.

Information from the retina goes to the lateral geniculate nucleus (LGN), then to the visual cortex. It is neatly organised into layers, from V1 to V4 and then either to V5 or to V6. Although the brain is very complicated, some kind of layered organisation is indeed present:

- **V1** – local features;
- **V2** – more local features, binocular vision;
- **V3** – colour, texture, first results of segmentation;
- **V4** – geometric shapes, silhouettes; the most important layer for attention;
- **V5** – recognises motion of objects segmented in V4;
- **V6** – generalises data from the whole image; wide‑field stimulation; processes changes due to our own movement;
- **V7** (controversial) – recognition of complex objects, e.g., human faces.

**What pathway**: V2 → V4, recognition of shapes and objects.  
**Where pathway**: V2 → V5 and V6, motion recognition, control over eyes and hands.

## Convolutional Neural Networks: Idea

These biological ideas are reflected in artificial neural networks as convolutional networks. Convolutions first appeared in the Neocognitron (Fukushima, 1979; 1980) and in their modern form in LeCun’s group in the late 1980s.

The main idea: we would like to apply the same operation to every part of the image.

1. **Break the picture into windows.**
2. **Apply a small neural network to every window.**
3. **Compress the image by max‑pooling over small windows.**
4. **Predict with a fully connected network.**

Adding new layers improves generalisation. Moreover, we can see where exactly in the picture individual neurons activate.

## CNNs Formally

Formally, we have a single small matrix (weight kernel) and apply it to every window. Let $x^{(l)}$ be the feature map in layer $l$. A two‑dimensional convolution with a kernel of size $(2d+1)\times(2d+1)$ and weight matrix $W$ is defined as

$$
y^{(l)}_{i,j} = \sum_{-d \le a,b \le d} W_{a,b}\; x^{(l)}_{i+a,\,j+b}.
$$

This is usually followed by a nonlinearity $h$:

$$
z^{(l)}_{i,j} = h\!\left(y^{(l)}_{i,j}\right),
$$

almost always ReLU in modern networks: $z^{(l)}_{i,j} = \max(0, \, y^{(l)}_{i,j})$.

Then max‑pooling (sometimes average‑pooling, but usually max) is applied:

$$
x^{(l+1)}_{i,j} = \max_{-d \le a,b \le d} z^{(l)}_{i+a,\,j+b}.
$$

This constitutes one convolutional layer. The classical **LeNet** architecture is an early example. Modern CNNs can become very deep thanks to a number of architectural tricks and advances.
