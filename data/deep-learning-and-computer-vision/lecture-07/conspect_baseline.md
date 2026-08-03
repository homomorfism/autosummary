# Vision Transformers and Object Detection

## Visual BERT: Joint Captioning and Images *[03:48]*

**Visual BERT** was one of the first successful attempts to handle pictures with transformers. It was designed primarily for image captioning. The idea was to feed both text tokens and **object tokens** – vectors representing specific objects found on the picture – into a single Transformer. To obtain those object tokens, you first need to solve object detection, extract the bounding boxes of objects, embed them into vectors (e.g. via a CNN), and feed the resulting sequence alongside the caption. The Transformer then learns to attend across modalities: for instance, words in the caption attend to the corresponding image regions. The key insight is that a Transformer treats any sequence of vectors uniformly, regardless of whether those vectors came from text or images. This paved the way for applying Transformers to vision directly.

## Vision Transformer (ViT) *[06:04]*

The **Vision Transformer (ViT)** (Dosovitskiy et al., 2020) applies a standard Transformer encoder to images without any text input. The simplicity is striking:

- An image $x \in \mathbb{R}^{H \times W \times C}$ is split into $N = HW / P^2$ patches of size $P \times P$.
- Each patch is flattened and projected linearly into an embedding vector, forming a sequence $x_p \in \mathbb{R}^{N \times P^2 C}$.
- The sequence is fed into a Transformer encoder exactly like BERT, with **masked patch modeling** as the pretraining objective: half of the input embeddings are replaced by a learnable `[mask]` embedding, and the model must reconstruct the original patch content.
- Positional encodings are added to preserve spatial information. Remarkably, the original ViT uses the **same 1D positional encodings** as the text Transformer. The authors experimented with 2D encodings but found no improvement – treating the grid as a simple sequence works perfectly well.

ViT revolutionized computer vision because the Transformer extracts richer, more semantically meaningful features than convolutional networks. In many applications, one can simply replace a CNN backbone with ViT and get better results. Hundreds of papers after 2020 exploited this fact.

**The quadratic complexity problem.** Every Transformer has an attention matrix of size $L \times L$ where $L$ is the input length. For ViT, $L$ equals the number of patches, so the complexity grows quadratically with the number of patches. This forbids using very small patches (to capture fine details) because even a million-pixel input would require an infeasible $10^{12}$ attention weights. Therefore, ViT must use relatively large patches, which means small details – like a distant cat sitting entirely inside one patch – may be lost. There is no perfect patch size; too large loses detail, too small is computationally impossible.

## Swin Transformer: Hierarchical Vision with Shifted Windows *[13:08]*

The **Swin Transformer** (Liu et al., 2021) addresses the quadratic complexity while preserving the ability to capture fine details and global context. The name stands for **Shifted windows**.

**Hierarchical processing.** Instead of feeding the entire fine grid to a self-attention layer, the image is broken into smaller windows. Within each window, self-attention complexity is only quadratic in the window size, not the whole image. The network then proceeds in stages:
- Start with small windows on a fine grid → process locally.
- Merge features from neighbouring windows → process at a coarser scale.
- Repeat, finally processing the whole image at a coarse level.

At every scale, transformer layers only ever see a fixed, small number of tokens (e.g., $4 \times 4 = 16$). This reduces the overall complexity from $O(N^2)$ to roughly linear in the number of patches.

**Shifted windows for global context.** The downside of strict window partitioning is that features cannot communicate across windows, losing global context. Global context is essential: a small white blob on a highway is probably a car, but the same blob on water is a boat; you cannot classify it without seeing the surroundings. The Swin Transformer solves this with **window shifting**: between consecutive self-attention layers, the grid of windows is shifted by half a window size. A feature that belonged to one window in layer $\ell$ will belong to a different, overlapping window in layer $\ell+1$. Over several layers, the receptive field expands, allowing information to propagate across the whole image.

**Boundary handling.** Shifting creates incomplete windows at the image edges. The original implementation wraps the image around a torus, grouping leftover parts together. While conceptually neat, the border-handling code becomes extremely convoluted, especially in 3D versions. Nevertheless, Swin Transformer v2 (Liu et al., 2022) scaled the architecture to 3 billion parameters and input resolutions up to $1536 \times 1536$, achieving state-of-the-art results across many vision tasks.

Swin and ViT are the two dominant backbones for modern computer vision. A **backbone** is the part of the network that performs feature extraction; you can later attach task-specific heads (classification, detection, segmentation) on top.

---

## Object Detection: Problem Setting *[23:34]*

Object detection is the task of localising and classifying multiple objects in an image. Formally, for each object of interest we must predict:

- A **bounding box** defined by four numbers: $(x, y, w, h)$ — the coordinates of one corner and the width and height.
- A **class label**, given as a probability distribution over known classes.

**Fixed number of outputs.** Neural networks require a fixed output size, but an image can contain a varying number of objects. The standard solution is to fix a maximum number of objects $K$ that the network will output. Each of the $K$ “slots” predicts:

- A **confidence** score (probability that a real object exists in that slot).
- A **class distribution** (only meaningful if an object is present).
- A **bounding box**.

During training, most slots will be empty, so their confidence is driven to zero.

**Training requires matching.** The ground truth also consists of a set of objects (class + box). The network’s output slots do **not** have a predefined order (there is no reason slot 1 must correspond to the cat and slot 2 to the dog). We therefore need to solve an **assignment problem**: find the optimal one-to-one matching between ground-truth objects and predicted slots that minimises a total cost. The cost for matching a ground-truth object $y_i = (c_i, b_i)$ to a prediction $\hat{y}_{\sigma(i)}$ combines classification error and bounding box error. The matching is typically done with the **Hungarian algorithm**, which yields a bipartite matching.

**Loss function.** Once the optimal matching $\sigma^*$ is found, the actual training loss is computed only for the matched pairs:

1. **Confidence loss**: for matched real objects the confidence should be $1$; for unmatched slots it should be $0$. This is often a binary cross-entropy (log-confidence).
2. **Classification loss**: for matched objects, a cross-entropy between the predicted class distribution and the true class.
3. **Bounding box regression loss**: for matched objects, the predicted box $(x, y, w, h)$ must match the ground-truth box.

The overall loss can be written as:

$$
\mathcal{L}_{\text{Hungarian}}(y, \hat{y}) = \sum_{i=1}^{N} \Big[ -\log \hat{p}_{\sigma^*(i)}(c_i) + \mathbb{1}_{\{c_i \neq \emptyset\}} \, \mathcal{L}_{\text{box}}(b_i, \hat{b}_{\sigma^*(i)}) \Big],
$$

where empty objects get a smaller weight in practice.

**Intersection over Union (IoU) for bounding boxes.** A simple coordinate-wise $L_1$ or $L_2$ loss has a problem: the same numerical error in $x$ or $w$ matters much more for small objects than for large ones. A small shift may cause zero overlap for a tiny box, while it barely affects a large box. The standard metric is **IoU**:

$$
\text{IoU}(B_1, B_2) = \frac{\text{area}(B_1 \cap B_2)}{\text{area}(B_1 \cup B_2)}.
$$

IoU naturally scales between $0$ and $1$, and it is differentiable *provided the boxes overlap*. However, when boxes do **not** overlap, IoU is exactly $0$ and its gradient is zero, giving the network no signal about the direction to move. This led to extensions such as **Generalized IoU (GIoU)**, which also considers the smallest enclosing box and penalises distance between non-overlapping boxes, providing a meaningful gradient even when IoU is zero.

**IoU threshold during training.** When computing the assignment, a predicted box is only allowed to match a ground-truth box if its IoU exceeds a threshold (e.g., $0.5$). Otherwise it is treated as background (confidence driven to $0$). This prevents far-away boxes from being incorrectly assigned to an object.

**Non‑maximum suppression (NMS) at inference.** At test time, the network often produces many overlapping high-confidence boxes around the same object. To obtain a clean output, a post‑processing step called **non-maximum suppression** is applied: boxes with the highest confidence are kept, and lower-confidence boxes with high IoU overlap are suppressed. NMS is a non‑differentiable handcrafted step used only at inference; during training, the matching already handles duplicates implicitly.

---

## Classical Object Detection Architectures *[52:20]*

### R‑CNN: Region‑based CNN *[52:56]*

The first successful deep‑learning detector was **R‑CNN** (Girshick et al., 2014). It follows a **two‑stage** approach:

1. **Region proposal:** an external algorithm, **selective search**, generates around $2000$ candidate bounding boxes that may contain objects (regardless of class).
2. **Per‑region classification:** each candidate box is warped to a fixed square size (e.g., $224 \times 224$) and passed through a CNN pretrained on ImageNet to extract features. Those features are then classified by a separate SVM to determine the object class. An additional linear regressor refines the bounding box coordinates.

R‑CNN was a breakthrough but suffered from three severe problems:

- Multi‑stage training: CNN fine‑tuning, SVM training, and bounding‑box regressor training were separate.
- Extremely slow: each of the $2000$ regions required a full CNN forward pass, taking about $47$ seconds per image on a GPU.
- The external region proposal is a bottleneck and not trainable.

### Fast R‑CNN *[1:00:14]*

**Fast R‑CNN** (Girshick, 2014) kept the two‑stage philosophy but made two crucial improvements:

- The entire image is passed through a convolutional backbone **only once**, producing a **feature map**.
- For each region proposal, the corresponding part of the feature map is cropped via **RoI (Region of Interest) projection**. Since the feature map retains some spatial geometry, each proposal maps to a fixed‑size feature block through **RoI pooling**: the block is divided into a fixed grid (e.g., $2 \times 2$) and max‑pooled, yielding a constant‑size representation regardless of the original proposal size.
- A single small detection head (classifier + bounding‑box regressor) processes each pooled feature.

This made Fast R‑CNN two orders of magnitude faster than R‑CNN with no loss in accuracy. However, region proposals still came from an external, non‑learned algorithm (selective search).

### Faster R‑CNN *[1:07:07]*

**Faster R‑CNN** (Ren et al., 2015) removed the last non‑learned component. It introduced a **Region Proposal Network (RPN)** that operates on the same feature map. The RPN slides a small network over the feature map and, at each location, evaluates a set of predefined **anchor boxes** (various scales and aspect ratios) and outputs two things: an objectness score and a box refinement. The top‑scoring proposals are then fed to the same RoI pooling + detection head as in Fast R‑CNN.

Faster R‑CNN became the standard detector for several years: it was completely end‑to‑end trainable and could be used with any convolutional backbone (VGG, ResNet, EfficientNet, etc.). All subsequent improvements in backbones automatically translated into better detection, a hallmark of **meta‑architectures**: the detection head and proposal mechanism are fixed, and you only swap the feature extractor.

### One‑stage detection and YOLO *[1:10:54]*

Faster R‑CNN is a **two‑stage** detector: it first proposes regions, then classifies and refines them. In contrast, **one‑stage** detectors skip the proposal step and directly predict class and box for a dense set of candidate locations in a single pass.

The most famous one‑stage family is **YOLO** (You Only Look Once; Redmon et al., 2016). The image is divided into an $S \times S$ grid. Each grid cell predicts:

- $B$ bounding boxes (each with $x, y, w, h$ and a confidence score).
- Class probabilities for the cell (conditioned on an object being present).

The output is a tensor of shape $S \times S \times (5B + C)$. Everything is trained end‑to‑end with a single, unified loss. YOLO trades a slight drop in accuracy for dramatically faster inference, making it suitable for real‑time applications. Subsequent versions (YOLOv2, YOLOv3, etc.) refined the architecture through many small improvements (better backbones, anchor boxes, multi‑scale training, hierarchical softmax for large class sets), each adding a few percentage points to the mean Average Precision.

### The small‑object problem and Feature Pyramid Networks *[1:15:07]*

Across all detectors, the hardest challenge is **detecting small objects**. A large object occupying a quarter of the image is easy; a tiny distant object may only cover a few pixels. In a CNN backbone, as we go deeper we **lose spatial resolution** – the feature map becomes coarser. A small object will eventually fit entirely inside one feature vector, and its identity is lost. If we instead stop the backbone early to keep a fine grid, the features are not semantically rich enough and processing all fine‑grid locations becomes computationally prohibitive.

The solution is **multi‑scale detection**. Instead of a single feature map, we attach detection heads (or region proposal networks) at **multiple stages** of the backbone, where the grid is still fine (for small objects) or coarse (for large objects). However, fine‑scale features lack global context, which is often crucial for recognising small objects (a few pixels of an animal can be a car or a boat depending on surroundings).

The **Feature Pyramid Network (FPN)** addresses this by adding **top‑down pathways**: high‑level, semantically strong features from deeper, coarser layers are upsampled and merged with the fine‑scale features via lateral connections. The resulting feature pyramid gives every scale access to rich semantic information. FPN was a very influential idea and remains a staple in modern detectors. Architectures like EfficientDet used neural architecture search to automatically design the optimal FPN connections.

---

## Object Detection with Transformers *[1:23:06]*

Classical detectors all rely on hand‑crafted components: anchor boxes, region proposals, and non‑maximum suppression. These are tuned manually and, in the case of NMS, are non‑differentiable post‑processing. The transformer philosophy suggests a different route: treat detection as a **set prediction problem** – let the transformer directly output the set of objects, with no anchors and no NMS.

### DETR: Detection Transformer *[1:25:12]*

**DETR** (Carion et al., 2020) is the first detector to fully embrace this idea. The architecture is a straightforward **encoder‑decoder Transformer** applied to image features:

- A standard CNN backbone (e.g., ResNet) extracts a feature map from the image.
- The feature map is flattened into a sequence of tokens, and positional encodings are added.
- The **Transformer encoder** processes this sequence, mixing global context. It does not perform detection itself; it refines the features to be suitable for detection.
- The **Transformer decoder** takes a fixed set of **object queries** – learned positional embeddings that are independent of the image. Each query is a “slot” for one potential object. The decoder uses cross‑attention to gather information from the encoder output (the image), and self‑attention to coordinate among queries (so they do not duplicate the same object).
- The output of each query passes through a small feed‑forward **detection head** that predicts the class and bounding box (or “no object”).

The number of objects detected equals the number of object queries (typically $N=100$). Because the queries exchange information through self‑attention, they **specialise**: different queries learn to focus on different spatial locations and object sizes. Consequently, DETR does not need non‑maximum suppression – multiple queries will not all converge to the same object.

**Training with bipartite matching.** DETR inherits the set prediction loss described earlier. For a set of $N$ predictions $\hat{y} = \{\hat{y}_i\}$ and ground truth objects $y$ (padded with $\emptyset$ to size $N$), it finds the optimal permutation $\sigma^*$ via the Hungarian algorithm that minimizes the matching cost:

$$
\mathcal{L}_{\text{match}}(y_i, \hat{y}_{\sigma(i)}) = -\mathbb{1}_{\{c_i \neq \emptyset\}} \hat{p}_{\sigma(i)}(c_i) + \mathbb{1}_{\{c_i \neq \emptyset\}} \mathcal{L}_{\text{box}}(b_i, \hat{b}_{\sigma(i)}),
$$

where $\mathcal{L}_{\text{box}}$ combines $L_1$ loss and GIoU loss. After matching, the actual training loss sums negative log‑likelihood for the matched classes and the bounding box loss for non‑empty objects. Empty objects are down‑weighted.

**Scale limitation.** The original DETR processes features at a single scale, making it weak on small objects. Visualizing decoder attention shows that attention weights concentrate on object boundaries, which is enough for classification and box refinement once objects have been separated by the encoder. However, the quadratic complexity of standard self‑attention prevents simply running DETR on a fine multi‑scale grid.

### Deformable DETR *[1:32:41]*

**Deformable DETR** (Zhu et al., 2021) solves the scale problem by using **deformable attention**. Instead of attending to all tokens, each attention head attends to only a small, learned set of sampling points around a reference point. This reduces the complexity from $O(L^2)$ to $O(L K)$ where $K \ll L$ is the number of sampled points. With this efficiency, Deformable DETR can process multi‑scale feature maps (obtained from different backbone layers) without blowing up computation. It thus detects small objects much better while keeping the end‑to‑end, NMS‑free philosophy.

### Improving object queries: DAB‑DETR, DN‑DETR, DINO *[1:36:21]*

One weakness of DETR is that object queries – abstract vectors – learn to specialise very slowly. A sequence of works re‑interpreted queries as **anchor boxes** and introduced mechanisms to speed up training and improve detection:

- **DAB‑DETR** (Dynamic Anchor Box DETR; Liu et al., 2022) makes each query an explicit 4‑tuple $(x, y, w, h)$, an anchor box that is refined layer by layer in the decoder. The width and height are used to modulate cross‑attention, making attention better localised around the box. This gives clear semantics and faster convergence.

- **DN‑DETR** (Denoising DETR; Li et al., 2022) tackles the instability of the Hungarian matching during early training. It adds a denoising objective: extra queries are fed noisy versions of ground truth boxes, and the network must reconstruct the original, clean box. This “good anchor” signal stabilises offset prediction and keeps queries close to their targets.

- **DINO** (DETR with Improved DeNoising anchor boxes; Zhang et al., 2022) further improves DN‑DETR by introducing negative examples (bad anchors that should be rejected) and by using a **mixed query selection** strategy where positional queries are initialised from encoder proposals while content queries remain learned. A look‑ahead training scheme (two‑step gradient blocking) also improves box quality. DINO achieves state‑of‑the‑art results with much faster training.

These detectors all share the core DETR idea: **object queries are slots that a transformer decoder fills with content by attending to the image**. The entire detection pipeline becomes a learned set‑prediction machine, eliminating hand‑crafted anchors and NMS while offering excellent performance.
