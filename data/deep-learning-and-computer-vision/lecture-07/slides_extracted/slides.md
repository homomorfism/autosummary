# Slides (extracted) — slides.pdf

## Slide 1

VISION TRANSFORMERS AND OBJECT DETECTION
Sergey Nikolenko
Harbour Space University
June 22, 2026
Random facts:
• on June 22, 1633, the Roman Inquisition forced the 69-year-old Galileo Galilei to kneel and
formally recant his claim that the Earth moves around the Sun; an unconfirmed legend has
it that as he rose he muttered "E pur si muove" ("and yet it moves")
• on June 22, 1986, in a single World Cup quarter-final against England, Diego Maradona
scored both the "Hand of God" goal (illegal goal the referee missed) and, four minutes later,
the "Goal of the Century"
• on June 22, 1969, the Cuyahoga River in Cleveland was so clogged with oil and industrial
waste that it caught fire; the blaze lasted barely half an hour, but the public outrage it
caused helped bring about the U.S. Environmental Protection Agency
• on June 22, 1978, astronomer James Christy discovered Charon, Pluto's largest moon, after
noticing a strange recurring bump on photographs of Pluto; Charon is so large relative to
Pluto that the two bodies actually orbit a point in the empty space between them
• on June 22, 1948, the HMT Empire Windrush docked near London carrying some 800
passengers from the Caribbean, a voyage now remembered as the symbolic beginning of
modern multicultural Britain
1

## Slide 2

VISION TRANSFORMERS

## Slide 3

VISUAL BERT
• Images are not sequences, right? Well...
• Visual BERT: let’s model captions and images jointly
• Use a fixed pretrained object detection system such as Faster
R-CNN, cut the objects out, embed them into vectors via CNNs
and special positional embeddings, and feed into a single
Transformer with the caption
3

## Slide 4

VISUAL BERT
• Pretraining: masked language modeling + sentence-image
prediction (distinguish whether a given caption matches the
image)
• Sample attention heads show how words from the caption
actually do attend to the corresponding objects
3

## Slide 5

VISUAL TRANSFORMER (VIT)
• The most successful Transformer-based architecture for images:
Vision Transformer (ViT; Dosovitsky et al., 2020)
• ViT is again a straighforward modification of BERT, but now there
is no text at the input, only image-based tokens
4

## Slide 6

VISUAL TRANSFORMER (VIT)
• The input image is cut into small patches: an 𝐻× 𝑊image with
𝐶channels x ∈ℝ𝐻×𝑊×𝐶becomes a sequence of patches
x𝑝∈ℝ𝑁×𝑃2×𝐶, where 𝑁= 𝐻𝑊/𝑃2 is the number of 𝑃× 𝑃
patches that fit
4

## Slide 7

VISUAL TRANSFORMER (VIT)
• Patches are turned into embeddings via a simple linear
projection, and then the sequence is fed into a Transformer
encoder just like BERT
• Pretraining: masked patch modeling just like BERT, replacing
half of the input embeddings with the same learnable [mask]
embedding
4

## Slide 8

VISUAL TRANSFORMER (VIT)
• ViT uses positional encodings to add information about the
sequence; interestingly, it is the same positional encoding as in
the original Transformer even though the geometry is 2D now
• Dosovitsky et al. experimented with 2D encodings, and it did not
make any difference
4

## Slide 9

SWIN TRANSFORMERS
• Swin Transformer (Liu et al., 2021; shifted windows): similar to
ViT but in a hierarchical fashion
5

## Slide 10

SWIN TRANSFORMERS
• It processes image patches on several scales, computing
self-attention across patches in a convolutional-like architecture
• The windows shift between self-attention layers, providing
connections between parts of the image
5

## Slide 11

SWIN TRANSFORMERS
• The architecture itself goes on reducing the geometry, like
classical CNN backbones:
• Swin can scale up to larger input resolutions and can be used
for dense recognition tasks such as image segmentation
5

## Slide 12

SWIN TRANSFORMERS
• A later iteration, Swin Transformer v2 (Liu et al., 2022), scaled the
Swin Transformer up to 3 billion parameters and allowed for
training with images up to 1536 × 1536 pixels, further improving
state of the art in image processing problems across the board
5

## Slide 13

PERCEIVER
• DeepMind’s Perceiver (Jaegle et al., 2021a) is a general-purpose
architecture that can process numerous different modalities
• The main idea is to avoid the quadratic bottleneck of
self-attention by using lower-dimensional latent units
• It’s quadratic in the number of queries, so we use a small vector
of latents for queries and add large byte arrays for 𝐾and 𝑉
6

## Slide 14

PERCEIVER
• Trained on images, point clouds, audio, and video, with no
modality-specific encoders and no change to the architecture!
6

## Slide 15

PERCEIVER
• Attention maps go down to individual pixels:
6

## Slide 16

PERCEIVER
• Perceiver IO (Jaegle et al., 2021b), the next version that
concentrates on high-dimensional outputs as well
• Can process even more various structured data: multi-task
language understanding, dense visual tasks like optical flow,
hybrid dense/sparse multimodal tasks such as
video+audio+class autoencoding, and tasks with symbolic
outputs like StarCraft II
6

## Slide 17

PERCEIVER
• Perceiver IO architecture:
• The actual output queries are constructed automatically by
combining a set of vectors that describe properties of the
current output such as position coordinates
6

## Slide 18

OBJECT DETECTION

## Slide 19

PROBLEM SETTING
• We have already discussed basic classification architectures.
• But for computer vision, classification is not enough; we need to
recognize objects on photographs.
• How do we use CNNs to understand where the objects are?
• This is exactly the object detection problem.
8

## Slide 20

R-CNN
• R-CNN: Region-based ConvNet (Girshick et al., 2014).
• Basic idea: look for bounding boxes with some external
algorithm (e.g., selective search).
• Then extract CNN features (from a CNN trained on ImageNet and
fine-tuned on the necessary dataset) and classify.
9

## Slide 21

R-CNN
• Visualizing the result: the image shows regions of activation for
a neuron from a high layer.
9

## Slide 22

R-CNN
• Visualizing the result: the image shows regions of activation for
a neuron from a high layer.
9

## Slide 23

R-CNN
• Plus a bounding box regression: we localize with a linear
regression on the features from the last pooling layer.
• Excellent for its time, R-CNN won ILSVRC2013 (200 classes).
9

## Slide 24

FAST R-CNN
• R-CNN was still the best at its time.
• But R-CNN has many problems:
• we have to train it in several steps (first CNN, then SVM on CNN
features, then bounding box regressors)
• it is very long to train, for technical reasons (we need to extract
features from each box in the training set and write it to disk to
train SVM and regressors);
• recognition is very slow (47s per image even on a GPU).
• The main reason is that we need to make a pass through the
CNN for every region.
10

## Slide 25

FAST R-CNN
• Hence, Fast R-CNN (Girshick, 2014).
• RoI (region of interest) projection collects features from a region.
• One pass of the main CNN for the whole image.
• Loss = classification error + bounding box regression error.
• Two orders of magnitude faster, no loss of quality.
10

## Slide 26

FAST R-CNN
• The candidates themselves still come from selective search.
• It turned out that it does not help much to add more candidates.
10

## Slide 27

FASTER R-CNN
• One more bottleneck left: selective search to choose bounding
boxes.
• It turns out that this can also be embedded into the network!
• Faster R-CNN (Ren et al., 2015) adds a separate Region Proposal
Network:
11

## Slide 28

FASTER R-CNN
• It evaluates each individual possibility from a set of predefined
anchor boxes:
11

## Slide 29

FASTER R-CNN
• A very good detector, best at the time for all evaluation metrics
and still relevant.
• Pascal VOC 2007:
• Pascal VOC 2012:
11

## Slide 30

YOLO
• You only look once (YOLO; Redmon et al., 2016).
• Look for both bounding boxes and the objects themselves in a
single pass.
12

## Slide 31

YOLO
• Idea: split the image into an 𝑆× 𝑆grid.
• In each cell, predict both bounding boxes and class
probabilities; then simply 𝑝(class𝑖∣obj)𝑝(obj)𝑝(bbox).
• The network’s output is a tensor of size 𝑆× 𝑆× (5𝐵+ 𝐶), where
each bbox consists of (𝑥, 𝑦, 𝑤, ℎ) and certainty.
12

## Slide 32

YOLO
• YOLO architecture:
12

## Slide 33

YOLO
• And all this is trained end-to-end, with a single loss function:
where 𝟙obj
𝑖𝑗
= 1 iff the 𝑗th bbox predictor in cell 𝑖is responsible
for predicting an object which is really there.
12

## Slide 34

YOLO
• We get slightly worse results than Faster R-CNN but much faster
and out of the box:
12

## Slide 35

FROM HAND-CRAFTED PIPELINES TO SET PREDICTION
• Classical detectors – R-CNN, Faster R-CNN, YOLO, SSD – all rely
on hand-designed components: a dense grid of anchor boxes,
region proposals, and non-maximum suppression (NMS) to
remove duplicate predictions.
• None of these pieces are learned end-to-end: anchors and NMS
need careful manual tuning, and NMS is a non-differentiable
post-processing step bolted on after the network.
• Can we instead treat detection as a direct set prediction
problem – let a Transformer predict the whole set of objects at
once, with no anchors and no NMS?
• This is exactly the idea behind DETR, and it opens the door to
the transformer-based detectors that dominate the field today.
13

## Slide 36

OBJECT DETECTION
WITH TRANSFORMERS

## Slide 37

DETR AND ITS EXTENSIONS
• DETR (DEtection TRansformer; Carion et al., 2020) — a direct
adaptation of transformers
• Object detection is a set prediction task; DETR adds a set-based
global loss function that gives unique predictions through
bipartite matching, and an encoder-decoder architecture based
on a transformer
15

## Slide 38

DETR AND ITS EXTENSIONS
• DETR uses a traditional convolutional backbone (ResNet in
Carion et al., but you can use anything)
• Then DETR flattens the features, adds positional encoding, and
mixes the features using an encoder
• The decoder takes as input a small number of object queries,
learnable positional embeddings, with attention to the encoder
output
• The output passes through a small feedforward network that
predicts the class and bbox (or ”no object”)
15

## Slide 39

DETR AND ITS EXTENSIONS
• The loss function comes from bipartite matching:
• for a set of predictionŝ 𝑦= {̂𝑦𝑖}𝑁
𝑖=1 and ground truth objects
y = {𝑦𝑖}𝑁
𝑖=1 (plus ∅, since 𝑁must be large), we find a permutation
𝜎∗= arg min𝜎∑
𝑁
𝑖=1 𝑙match(𝑦𝑖,̂ 𝑦𝜎(𝑖)) using the Hungarian algorithm,
where 𝑙match is the matching cost;
• 𝑙match combines prediction accuracy for 𝑦𝑖= (𝑐𝑖, 𝑏𝑖), where 𝑐𝑖is the
class label (possibly ∅), and 𝑏𝑖∈ℝ4 is the bbox:
𝑙match(𝑦𝑖,̂ 𝑦𝜎(𝑖)) = −[𝑐𝑖≠∅]̂𝑝𝜎(𝑖)(𝑐𝑖) + [𝑐𝑖≠∅]𝑙box(𝑏𝑖,̂ 𝑏𝜎(𝑖));
here 𝑙box is a combination of IoU and 𝐿1 loss functions;
• after matching, the actual loss function is
𝑙Hungarian(y,̂ 𝑦) =
𝑁
∑
𝑖=1
(−loĝ 𝑝𝜎∗(𝑖)(𝑐𝑖) + [𝑐𝑖≠∅]𝑙box(𝑏𝑖,̂ 𝑏𝜎(𝑖)) ;
now we also predict 𝑐𝑖= ∅, but in practice they get lower weight.
15

## Slide 40

DETR AND ITS EXTENSIONS
• Good results, and DETR is able to distribute object instances
across attention heads:
15

## Slide 41

DETR AND ITS EXTENSIONS
• Decoder attention for each object is localized on boundaries
• Most likely, DETR separates instances with global attention in
the encoder, and the decoder only needs to figure out classes
and object boundaries
15

## Slide 42

DETR AND ITS EXTENSIONS
• DETR works well, but not very well on small objects, and
quadratic complexity makes multi-scale detection a very
difficult task
• Deformable DETR (Zhu et al., 2021): let’s use deformable
attention and attend only to a few pixels
15

## Slide 43

DETR AND ITS EXTENSIONS
• General architecture:
15

## Slide 44

DETR AND ITS EXTENSIONS
• DETR’s positional queries are essentially flexible learnable
anchors for bounding boxes; they are trained globally and do
not depend on the current image
• Learning spatial queries from data (without any fixed anchor
boxes) is an important part of DETR, but DETR trains very, very
slowly, and spatial queries are a big factor in this
• How can we improve this?
15

## Slide 45

DETR AND ITS EXTENSIONS
• DAB-DETR (Dynamic Anchor Box DETR; Liu et al., 2022): let’s
return to the idea of anchor boxes
• Learnable anchors are gradually refined from layer to layer in
the decoder, and now they have specific semantics:
15

## Slide 46

DETR AND ITS EXTENSIONS
• The width and height of the anchor box are used to modulate
cross-attention, so attention becomes much better localized,
and this helps speed up training
15

## Slide 47

DETR AND ITS EXTENSIONS
• Overview:
15

## Slide 48

DETR AND ITS EXTENSIONS
• SMCA DETR (Spatially Modulated Co-Attention DETR; Gao et al.,
2021) modulates attention weights through spatial priors; what’s
nearby is more important: spatial weights based on predicted
offsets relative to reference points
15

## Slide 49

DETR AND ITS EXTENSIONS
• Another problem comes from optimal matching: a small change
in weights can lead to a completely different result, predictions
are unstable, especially at the beginning of training
• DN-DETR (Li et al., 2022): let’s add another training objective —
reconstruction of noisy ground truth boxes that are fed with
additional queries
15

## Slide 50

DETR AND ITS EXTENSIONS
• This improves offset prediction: each query has to predict very
different offsets due to matching instability, and denoising
queries serve as ”good anchors” for offset prediction
• As a result, anchors are located closer to their targets (DAB-DETR
on the left, DN-DETR on the right):
15

## Slide 51

DETR AND ITS EXTENSIONS
• DINO (DETR with Improved DeNoising Anchor Boxes; Zhang et al.,
2022): a modification of DETR based on the DN-DETR idea
• The basic structure is more or less the same:
15

## Slide 52

DETR AND ITS EXTENSIONS
• DN-DETR needs good anchors to improve offset learning; but
what about bad anchors that have no nearby ground truth
objects?
• DINO adds negative examples to mitigate this; part of the inputs
are anchors with large noise that should be rejected
15

## Slide 53

DETR AND ITS EXTENSIONS
• Mixed query selection: positional queries are initialized from
encoder proposals, while content queries remain independent
15

## Slide 54

DETR AND ITS EXTENSIONS
• Two-step lookahead: bounding box quality depends on the
current anchor (positional query) and the current offset
prediction
• Deformable DETR blocked gradient backpropagation to stabilize
training: layer 𝑖parameters are updated based on the auxiliary
loss from boxes 𝑏𝑖
• DINO blocks gradients one more step further, so layer 𝑖
parameters are updated based on the auxiliary loss from boxes
𝑏𝑖and 𝑏𝑖+1
15

## Slide 55

DETR AND ITS EXTENSIONS
• Very good results, fast training (left with ResNet-50 backbone)
15

## Slide 56

DETR AND ITS EXTENSIONS
• H-Deformable-DETR (Jia et al., 2023) — a very simple and
interesting idea
• We have very few positive examples, so let’s copy them!
• During training we add additional queries that should predict
the same ground truth boxes, with attention masks that
separate query groups
15

## Slide 57

DETR AND ITS EXTENSIONS
• How else can we fix DETR’s long training time?
• UP-DETR (Dai et al., 2021) — let’s add unsupervised,
self-supervised pretraining; we take a random patch and ask
DETR to predict its position and reconstruct its features (this is
needed because we don’t have classification labels, but we need
to preserve semantics):
15

## Slide 58

DETR AND ITS EXTENSIONS
• DETReg (Bar et al., 2022) — instead of random crops let’s use
objects or regions found by other algorithms, possibly even
selective search
• We can also predict embeddings for these pseudo-objects
15

## Slide 59

DETR AND ITS EXTENSIONS
• Co-DETR (Zong et al., 2023) adds several auxiliary heads from
other object detection models; new positive examples through
matching
15

## Slide 60

DETR AND ITS EXTENSIONS
• Graph for ResNet-50 backbone:
15

## Slide 61

DETR AND ITS EXTENSIONS
• Overview from an (old) survey (Shehzadi et al., 2023):
15

## Slide 62

THANK YOU!
Thank you for your attention!
16
