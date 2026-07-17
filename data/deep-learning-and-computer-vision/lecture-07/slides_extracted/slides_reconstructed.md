# Vision Transformers and Object Detection

## Vision Transformers

### Visual BERT

- Images are not sequences, right? Well...
- Visual BERT models captions and images jointly.
- Uses a fixed pretrained object detection system such as Faster R-CNN to cut out objects, embed them into vectors via CNNs and special positional embeddings, and feed them along with the caption into a single Transformer.
- **Pretraining**: masked language modeling + sentence-image prediction (distinguishing whether a given caption matches the image).
- Sample attention heads show how words from the caption attend to the corresponding objects.

### Vision Transformer (ViT)

- The most successful Transformer-based architecture for images: Vision Transformer (ViT; Dosovitsky et al., 2020).
- ViT is a straightforward modification of BERT, but with no text at the input — only image-based tokens.
- The input image is cut into small patches: an $H \times W$ image with $C$ channels $x \in \mathbb{R}^{H \times W \times C}$ becomes a sequence of patches $x_p \in \mathbb{R}^{N \times P^2 \times C}$, where $N = HW/P^2$ is the number of $P \times P$ patches that fit.
- Patches are turned into embeddings via a simple linear projection, and the sequence is fed into a Transformer encoder just like BERT.
- **Pretraining**: masked patch modeling (replacing half of the input embeddings with a learnable `[mask]` embedding), analogous to masked language modeling.
- ViT uses positional encodings — the same absolute positional encoding as in the original Transformer, even though the geometry is now 2D. Experiments with 2D positional encodings showed no difference.

### Swin Transformers

- Swin Transformer (Liu et al., 2021; “shifted windows”) is similar to ViT but built in a hierarchical fashion.
- It processes image patches on several scales, computing self-attention across patches in a convolutional-like architecture.
- Windows shift between self-attention layers, providing connections between different parts of the image.
- The architecture progressively reduces the spatial geometry, like classical CNN backbones.
- Swin can scale up to larger input resolutions and is suitable for dense recognition tasks such as image segmentation.
- A later iteration, Swin Transformer v2 (Liu et al., 2022), scaled the model up to 3 billion parameters and allowed training with images up to $1536 \times 1536$ pixels, further improving state of the art across image processing tasks.

### Perceiver

- DeepMind’s Perceiver (Jaegle et al., 2021a) is a general-purpose architecture that can process numerous modalities without modality-specific encoders.
- The main idea is to avoid the quadratic bottleneck of self-attention by using lower-dimensional latent units as queries — a small vector of latents attends to large byte arrays for keys and values.
- Trained on images, point clouds, audio, and video with no change to the architecture; attention maps can go down to individual pixels.
- Perceiver IO (Jaegle et al., 2021b) extends this to high-dimensional outputs, handling tasks that require structured outputs:
  - multi-task language understanding,
  - dense visual tasks like optical flow,
  - hybrid dense/sparse multimodal tasks (video+audio+class autoencoding),
  - tasks with symbolic outputs such as StarCraft II.
- In Perceiver IO, output queries are constructed automatically by combining a set of vectors that describe properties of the current output (e.g., position coordinates).

## Object Detection

### Problem Setting

- Basic classification architectures are not sufficient for computer vision; we need to recognise objects in photographs.
- The problem of using CNNs to determine where objects are is exactly **object detection**.

### R-CNN

- R-CNN (Region-based ConvNet; Girshick et al., 2014) looks for bounding boxes with an external algorithm (e.g., selective search), then extracts CNN features (from a CNN pretrained on ImageNet and fine-tuned on the target dataset) and classifies each region.
- Visualising the result: images show regions of activation for a neuron from a high layer.
- Additionally, a bounding box regression localises objects using a linear regression on features from the last pooling layer.
- Excellent for its time, R-CNN won the ILSVRC 2013 detection challenge (200 classes).

### Fast R-CNN

- R-CNN had several problems:
  - Multiple training stages (train CNN, then SVM on CNN features, then bounding box regressors).
  - Very long training because features had to be extracted for every region proposal and written to disk.
  - Slow recognition (~47 s per image even on a GPU) because a full CNN forward pass was needed for each proposal.
- Fast R-CNN (Girshick, 2014) addresses these with **RoI (Region of Interest) projection**: one pass of the main CNN over the whole image, then feature cropping and pooling for each region.
- The loss is a sum of classification error and bounding box regression error.
- Two orders of magnitude faster with no loss of quality; the region proposals still come from selective search (adding more candidates did not help much).

### Faster R-CNN

- The remaining bottleneck was selective search for generating proposals.
- Faster R-CNN (Ren et al., 2015) embeds proposal generation inside the network by adding a separate **Region Proposal Network (RPN)**.
- The RPN evaluates each possibility from a set of predefined anchor boxes.
- A very strong detector, best at the time across all evaluation metrics (Pascal VOC 2007, 2012) and still relevant today.

### YOLO

- You Only Look Once (YOLO; Redmon et al., 2016): look for both bounding boxes and object classes in a single pass.
- The image is split into an $S \times S$ grid.
- In each grid cell, the network predicts both bounding boxes and class probabilities; combined as $p(\text{class}_i \mid \text{obj}) \cdot p(\text{obj}) \cdot \text{IOU}_{\text{bbox}}$ (or simply $p(\text{class}_i) \cdot \text{IOU}$ after later refinements).
- The output is a tensor of size $S \times S \times (5B + C)$, where each of the $B$ bounding boxes consists of $(x, y, w, h)$ and a confidence score.
- Training is end-to-end with a single loss function, where $\mathbb{1}_{\text{obj}}^{ij} = 1$ iff the $j$-th bounding box predictor in cell $i$ is responsible for predicting an object that is actually present.
- Slightly lower accuracy than Faster R-CNN, but much faster and works out-of-the-box.

### From Hand-crafted Pipelines to Set Prediction

- Classical detectors — R-CNN, Faster R-CNN, YOLO, SSD — all rely on hand-designed components: a dense grid of anchor boxes, region proposals, and non-maximum suppression (NMS) to remove duplicate predictions.
- None of these pieces are learned end-to-end: anchors and NMS require careful manual tuning, and NMS is a non-differentiable post-processing step bolted on after the network.
- A fundamental question: can we treat detection as a direct **set prediction** problem, letting a Transformer predict the whole set of objects at once, with no anchors and no NMS?
- This is exactly the idea behind DETR, opening the door to Transformer-based detectors that dominate the field today.

## Object Detection with Transformers

### DETR and Its Extensions

#### DETR

- DETR (DEtection TRansformer; Carion et al., 2020) — a direct adaptation of Transformers for object detection.
- Object detection is a set prediction task; DETR uses a set-based global loss that enforces unique predictions through bipartite matching and an encoder-decoder Transformer architecture.
- It uses a conventional convolutional backbone (e.g., ResNet), flattens the features, adds positional encoding, and processes them with an encoder.
- The decoder receives a small fixed number of learnable **object queries** (positional embeddings) that attend to the encoder output.
- A small feedforward network on top of the decoder outputs class labels (including “no object”) and bounding boxes.
- **Loss function** based on Hungarian bipartite matching:
  - For a set of predictions $\hat{y} = \{\hat{y}_i\}_{i=1}^N$ and ground-truth objects $y = \{y_i\}_{i=1}^N$ (padded with $\varnothing$ to size $N$), find the permutation
    $$\sigma^* = \arg\min_\sigma \sum_{i=1}^N \mathcal{L}_{\text{match}}(y_i, \hat{y}_{\sigma(i)})$$
    via the Hungarian algorithm.
  - The matching cost is
    $$\mathcal{L}_{\text{match}}(y_i, \hat{y}_{\sigma(i)}) = -\mathbf{1}[c_i \neq \varnothing]\, \hat{p}_{\sigma(i)}(c_i) + \mathbf{1}[c_i \neq \varnothing]\, \ell_{\text{box}}(b_i, \hat{b}_{\sigma(i)}),$$
    where $c_i$ is the class label, $b_i \in \mathbb{R}^4$ the bounding box, and $\ell_{\text{box}}$ combines IoU and $L_1$ losses.
  - After matching, the training loss is
    $$\mathcal{L}_{\text{Hungarian}}(y, \hat{y}) = \sum_{i=1}^N \left( -\log \hat{p}_{\sigma^*(i)}(c_i) + \mathbf{1}[c_i \neq \varnothing]\, \ell_{\text{box}}(b_i, \hat{b}_{\sigma(i)}) \right);$$
    in practice, “no object” predictions are down-weighted.
- DETR provides good results and distributes object instances across attention heads; decoder attention for each object is localised to object boundaries.
- It likely separates instances via global attention in the encoder, leaving the decoder to handle class and boundary refinement.
- Limitations: struggles with small objects, and the quadratic complexity makes multi-scale detection difficult.

#### Deformable DETR

- Deformable DETR (Zhu et al., 2021) replaces standard self-attention with **deformable attention**, attending only to a few sampling points around a reference location, dramatically reducing complexity and enabling multi-scale feature processing.

#### DAB-DETR

- DAB-DETR (Dynamic Anchor Box DETR; Liu et al., 2022) reintroduces the idea of anchor boxes but makes them **learnable** and gradually refined from layer to layer in the decoder.
- The anchor box width and height are used to modulate cross-attention, leading to much better localised attention and faster training.

#### SMCA DETR

- SMCA DETR (Spatially Modulated Co-Attention DETR; Gao et al., 2021) modulates attention weights through spatial priors: nearby locations are given higher importance based on predicted offsets relative to reference points.

#### DN-DETR

- Optimal bipartite matching is unstable early in training (small weight changes can cause completely different assignments).
- DN-DETR (Li et al., 2022) adds a training objective: reconstruct **noisy ground truth boxes** fed via additional denoising queries.
- This improves offset prediction because denoising queries serve as “good anchors” for learning offsets, keeping anchors closer to their targets.

#### DINO

- DINO (DETR with Improved DeNoising Anchor Boxes; Zhang et al., 2022) builds on DN-DETR with several improvements:
  - **Negative examples**: anchors with large noise that have no nearby ground-truth objects are added, forcing the model to reject them.
  - **Mixed query selection**: positional queries are initialised from encoder proposals, while content queries remain learnable and independent.
  - **Two-step lookahead**: bounding box quality depends on the current anchor (positional query) and the current offset prediction. Deformable DETR blocked gradient backpropagation to stabilise training; DINO blocks gradients one step further, updating layer $i$ parameters based on auxiliary losses from boxes $b_i$ and $b_{i+1}$.
- Very good results with fast training (using a ResNet-50 backbone).

#### H-Deformable-DETR

- A simple idea (Jia et al., 2023): during training there are very few positive examples, so **copy them** by adding additional queries that predict the same ground truth boxes, with attention masks separating query groups.

#### UP-DETR

- UP-DETR (Dai et al., 2021) adds **unsupervised pretraining**: a random patch is taken and DETR must predict its position and reconstruct its features — preserving semantics without needing classification labels.

#### DETReg

- DETReg (Bar et al., 2022) uses objects or regions found by external algorithms (possibly even selective search) instead of random crops during self-supervised pretraining, and predicts embeddings for these pseudo-objects.

#### Co-DETR

- Co-DETR (Zong et al., 2023) attaches several auxiliary heads from other object detection models, introducing new positive examples through matching to improve training.

#### Overview

- A survey by Shehzadi et al. (2023) provides an overview of the rapidly evolving DETR family of methods.
