# Slides (extracted) — slides.pdf

## Slide 1

CONVOLUTIONAL ARCHITECTURES AND BEYOND
Sergey Nikolenko
Harbour Space University
June 16, 2026
Random facts:
• on June 16, 1884, LaMarcus Thompson's Switchback Railway opened at Coney Island as the
first purpose-built roller coaster; it ambled along at about six miles per hour for a nickel a
ride, yet proved profitable enough to spawn an entire industry
• on June 16, 1904, James Joyce set the whole action of Ulysses, all seven hundred-odd pages
of it, on this one ordinary Dublin day, because it was the date of his first walk out with Nora
Barnacle; readers now retrace it each ``Bloomsday'' in Edwardian dress
• on June 16, 1911, the Computing-Tabulating-Recording Company was incorporated in New
York, merging a scale maker, a time-clock maker, and Herman Hollerith's census
tabulating-machine business; the ungainly conglomerate was not renamed IBM until 1924
• on June 16, 1960, Alfred Hitchcock's Psycho premiered in New York under a strict ``no one
admitted after the start'' rule, enforced by Pinkerton guards and life-sized cardboard
cutouts of the director; that gimmick is why films have had fixed start times ever since
• on June 16, 1963, Valentina Tereshkova, a textile worker and amateur parachutist, became
the first woman in space aboard Vostok 6, circling the Earth 48 times in just under three
days; no other woman would reach orbit for another 19 years
1

## Slide 2

IMPORTANT CONVOLUTIONAL ARCHI-
TECTURES

## Slide 3

THE ZOO
• There is a huge number of different models based on the CNN
idea.
• Most of them are accompanied by code.
• Many provide models pretrained on the ImageNet or other large
standard datasets.
• But usually they are all based on a few standard ideas, and
that’s exactly what we are going to consider.
3

## Slide 4

(KRIZHEVSKY, SUTSKEVER, HINTON, 2012): ALEXNET
4

## Slide 5

(KRIZHEVSKY, SUTSKEVER, HINTON, 2012): ALEXNET
5

## Slide 6

VGG
• VGG (Oxford Visual Geometry Group): let’s represent large
convolutions as compositions of 3 × 3 convolutions.
• This reduces the number of weights and makes the network
deeper.
6

## Slide 7

VGG
• The VGG network used in ImageNet Large Scale Visual
Recognition Competition (ILSVRC-2014):
• NVIDIA has been optimizing GPUs especially for 3 × 3
convolutions.
6

## Slide 8

INCEPTION
• Inception and GoogLeNet based on it: let’s use the “network in
network” idea to reduce the number of weights even further.
• Another idea – additional classifiers (additional terms for the
objective function).
7

## Slide 9

INCEPTION
• In Inception v2 (Szegedy et al., 2015) 𝑛× 𝑛convolutions were
replaced by 𝑛× 1 and 1 × 𝑛convolutions:
7

## Slide 10

INCEPTION
• Filter banks in Inception v2 became wide rather than deep:
• The same paper also introduced Inception v3; same thing, but
with RMSProp, factorized 7 × 7 convolutions, batchnorm in
additional classifiers and...
7

## Slide 11

INCEPTION
• Label smoothing:
• in a regular classifier we train the softmax with hard objective
𝑞(𝑘) = [𝑘= 𝑦], i.e., arguments of the softmax function “want” to
grow unboundedly;
• as a result, the models overfit and become too certain;
• possible solution: let’s instead optimize
𝑞′(𝑘) = (1 −𝜖)[𝑘= 𝑦] + 𝜖𝑢(𝑘)
for some prior distribution 𝑢(𝑘), say 𝑢(𝑘) =
1
𝐾.
7

## Slide 12

RESNET
• Residual learning: let’s train the differences (residues) between
one layer and the next.
• Then the gradients will be able to flow with no obstacle.
• A function implemented by a residual unit looks like
y(𝑘) = 𝐹(x(𝑘)) + x(𝑘),
where x(𝑘) is the input vector of layer 𝑘, 𝐹(𝑥) is the function
computed by the layer, and y(𝑘) is the output of the residual
layer that will then become x(𝑘+1) for the next layer.
• Now the gradient can pass through and does not vanish when 𝐹
becomes saturated:
𝜕y(𝑘)
𝜕x(𝑘) = 1 + 𝜕𝐹(x(𝑘))
𝜕x(𝑘)
.
8

## Slide 13

RESNET
• This has allowed for very deep networks.
• Another similar approach – highway networks by Jürgen
Schmidhuber.
• We again represent y(𝑘), output of layer 𝑘, as a linear
combination of x(𝑘) and 𝐹(x(𝑘)), but in a different way:
y(𝑘) = 𝐶(x(𝑘))x(𝑘) + 𝑇(x(𝑘))𝐹(x(𝑘)),
where 𝐶is the carry gate, and 𝑇is the transform gate; usually
it’s a convex combination, 𝐶= 1 −𝑇.
• Practice shows that the residual connections should be as
“straight” as possible.
8

## Slide 14

RESNET: VARIATIONS
9

## Slide 15

REVOLUTION OF DEPTH (KAIMING HE)
10

## Slide 16

REVOLUTION OF DEPTH (KAIMING HE)
11

## Slide 17

REVOLUTION OF DEPTH (KAIMING HE)
12

## Slide 18

RESNEXT
• ResNeXt (Xie et al., 2016): let’s replace ResNet units with
“split-transform-merge” units, similar to Inception.
• The input is divided into blocks w.r.t. channels, and every block
gets its own convolutions.
13

## Slide 19

RESNEXT
• The idea is similar to group convolutions, used already in
AlexNet for parallelization:
• They do yield a kind of a specialization in the results:
13

## Slide 20

INCEPTION V4 AND INCEPTION RESNET
• Another classic paper (Szegedy et al., 2016) introduced Inception
v4 and Inception ResNet.
• Inception v4 – let’s standardize everything and simplify the
units. First, the “stem”:
14

## Slide 21

INCEPTION V4 AND INCEPTION RESNET
• Second, we now have three basic blocks A, B, and C:
14

## Slide 22

INCEPTION V4 AND INCEPTION RESNET
• And special reduction blocks to reduce the dimensions:
14

## Slide 23

INCEPTION V4 AND INCEPTION RESNET
• Inception ResNet adds residual connections to these blocks:
14

## Slide 24

INCEPTION V4 AND INCEPTION RESNET
• There is no pooling now but there are still reduction blocks:
14

## Slide 25

INCEPTION V4 AND INCEPTION RESNET
• As a result, the architecture has become even simpler; Inception
v4 (top), Inception ResNet (bottom):
14

## Slide 26

INCEPTION V4 AND INCEPTION RESNET
• Inception ResNet v2:
14

## Slide 27

INCEPTION V4 AND INCEPTION RESNET
• And it works quite well:
14

## Slide 28

SQUEEZENET
• SqueezeNet (Iandola et al., 2017) – how to reduce the number of
parameters:
• replace 3 × 3 filters with 1 × 1;
• reduce the number of inputs for 3 × 3 convolutions;
• delay downsampling as late as possible to increase the size of
activation maps.
15

## Slide 29

SQUEEZENET
• Fire module:
• squeeze convolutional layer (1 × 1 only);
• expand layer (1 × 1 and 3 × 3).
15

## Slide 30

SQUEEZENET
• General SqueezeNet architecture:
15

## Slide 31

SQUEEZENET
• We get 50x fewer parameters than AlexNet. But:
15

## Slide 32

MOBILENET
• MobileNet (Howard et al., 2017): networks for mobile devices.
• Depthwise separable convolutions: let’s decompose a
convolution into a depthwise convolution (one filter for each
channel) and a 1 × 1 convolution.
16

## Slide 33

MOBILENET
• Then the structure of a layer will be more complex (but with
fewer weights), and the overall architecture is not so deep:
16

## Slide 34

MOBILENET
• We see that we can save a lot of parameters at the price of a
small decrease in quality:
16

## Slide 35

EFFICIENTNET
• EfficientNet (Tan, Le, 2019): neural architecture search to design
state of the art networks at a fraction of the cost
17

## Slide 36

EFFICIENTNET
• Different kinds of scaling for the models:
17

## Slide 37

BATCH NORMALIZATION

## Slide 38

BATCH NORMALIZATION
• Important problem in deep neural networks: internal covariate
shift.
• When we change the weights of a layer, the distribution of its
outputs changes.
• This means that the next layer has to re-train almost from
scratch, it did not expect these outputs.
• Moreover, these neurons might have already reached saturation,
so they can’t re-train quickly.
• This seriously impedes learning.
19

## Slide 39

BATCH NORMALIZATION
• A characteristic example; note how different the distributions
are:
• What can we do?
19

## Slide 40

BATCH NORMALIZATION
• We could try to normalize (whiten) after every layer.
• Does not work: consider a layer that simply adds a bias 𝑏to its
inputs u:̂
x = x −𝔼[x] , where x = u + 𝑏.
• On the next gradient descent step, we’ll have 𝑏∶= 𝑏+ Δ𝑏...
• ...but̂ x will not change:
u + 𝑏+ Δ𝑏−𝔼[u + 𝑏+ Δ𝑏] = u + 𝑏−𝔼[u + 𝑏] .
• So the biases will simply increase unboundedly, and that’s all
the training we’ll get; not a good thing.
19

## Slide 41

BATCH NORMALIZATION
• We can try to add normalization as a layer:̂
x = Norm(x, 𝑋).
• But note that the entire dataset 𝑋is required here.
• So on the gradient descent step we’ll need to compute 𝜕Norm
𝜕x
and 𝜕Norm
𝜕𝑋, and also the covariance matrix
Cov[x] = 𝔼x∈𝑋[xx⊤] −𝔼[x] 𝔼[x]
⊤.
• Definitely won’t work.
19

## Slide 42

BATCH NORMALIZATION
• The solution is to normalize each component separately, and
not over the whole dataset but over the current mini-batch;
hence batch normalization.
• After batch normalization we get̂
𝑥𝑘= 𝑥𝑘−𝔼[𝑥𝑘]
√Var [𝑥𝑘]
,
where the statistics are computed over the current mini-batch.
• However, one more problem: now nonlinearities disappear!
• E.g., we will almost always get into the region where 𝜎is very
close to linear.
19

## Slide 43

BATCH NORMALIZATION
• To fix this, we have to allow the batchnorm layer enough
flexibility to sometimes do nothing with the inputs.
• So we introduce additional shift and scale parameters:
𝑦𝑘= 𝛾𝑘̂𝑥𝑘+ 𝛽𝑘= 𝛾𝑘
𝑥𝑘−𝔼[𝑥𝑘]
√Var[𝑥𝑘]
+ 𝛽𝑘.
• 𝛾𝑘and 𝛽𝑘are new variables and will be trained just like the
weights.
19

## Slide 44

BATCH NORMALIZATION
• Final scheme:
19

## Slide 45

WHAT BN ACTUALLY DOES
• The original idea was to reduce internal covariate shift.
• But it turned out that BN’s effectiveness does not really depend
on this; still, BN helps with regularization, makes dropout
unnecessary, and so on. Possible reasons:
• BN smooths the gradients, reducing the Lipschitz constant
(Santurkar et al., 2019);
• BN decouples the learning of the direction and the length of the
weight vectors, which improves training;
• there are results showing that BN helps achieve linear
convergence in ordinary gradient descent.
20

## Slide 46

VARIANTS
• Mini-batch normalization has by now become essentially the
standard.
• Yet another very cool story, much like dropout.
• But the idea goes further:
• (Laurent et al., 2016): BN does not help recurrent networks;
• (Cooijmans et al., 2016): recurrent batch normalization;
• (Salimans and Kingma, 2016): weight normalization to improve
training — let us add the weights as
h𝑖= 𝑓(
𝛾
‖w𝑖‖w⊤
𝑖x + 𝑏𝑖) ;
then we rescale the gradient, stabilize its norm, and bring its
covariance matrix closer to the identity, which improves training.
• Let us make sense of the landscape of normalization methods
21

## Slide 47

VARIANTS
• In general, all these methods use the same operations:
21

## Slide 48

VARIANTS
• and differ in the set of operations and in which dimensions they
are applied over:
21

## Slide 49

VARIANTS
• Batch norm – over the mini-batch (often used for images):
21

## Slide 50

VARIANTS
• Layer norm – over the channels and spatial dimensions, i.e.,
over all outputs of a layer (used mostly for vectors, in particular
in transformers):
21

## Slide 51

VARIANTS
• Instance norm – only over the spatial dimensions, i.e., we drop
the channels (used, e.g., in AdaIN for style transfer):
21

## Slide 52

VARIANTS
• Group norm – we can split the channels into groups:
21

## Slide 53

VARIANTS
• Weight standardization – we standardize the weights rather than
the activations, separately for each channel, i.e., we also
normalize the gradients during backpropagation (group norm +
weight standardization were used in BiT – Big Transfer):
21

## Slide 54

VARIANTS
• In summary:
21

## Slide 55

VARIANTS
• But in general this is, as always, a big science (Huang et al., 2020):
21

## Slide 56

VARIANTS
• And really big it is:
21

## Slide 57

WORKING WITH SEQUENCES

## Slide 58

SEQUENCES
• Sequences: financial time series, language, sound...
• Different kinds of sequence-based problems:
23

## Slide 59

SEQUENCES
• How to we apply a neural network to a sequence-based
problem?
• We can try to use a sliding window:
23

## Slide 60

SEQUENCES
• ...but it would be better to have a hidden state and update it.
• This is the whole idea of recurrent neural networks (RNN).
• But how do we do backprop? Doesn’t the computational graph
have cycles now that
𝑠𝑖= ℎ(𝑥𝑖, 𝑥𝑖+1, 𝑥𝑖+2, 𝑠𝑖−1)?
23

## Slide 61

SEQUENCES
• ...not really. We can “unroll” it back:
𝑦6 = 𝑓(𝑥3, 𝑥4, 𝑥5, 𝑠2) = 𝑓(𝑥3, 𝑥4, 𝑥5, ℎ(𝑥2, 𝑥3, 𝑥4, 𝑠1)) =
= 𝑓(𝑥3, 𝑥4, 𝑥5, ℎ(𝑥2, 𝑥3, 𝑥4, ℎ(𝑥1, 𝑥2, 𝑥3, 𝑠0))).
• So formally there is no problem.
• But, of course, lots of practical issues – it’s a very deep network
with lots of shared weights...
23

## Slide 62

RECURRENT NEURAL NETWORKS

## Slide 63

SIMPLE RNN
• “Simple” RNN:
25

## Slide 64

SIMPLE RNN
• Formally:
a𝑡= b + 𝑊s𝑡−1 + 𝑈x𝑡,
s𝑡= 𝑓(a𝑡),
o𝑡= c + 𝑉s𝑡,
y𝑡= ℎ(o𝑡),
where 𝑓is the recurrent nonlinearity, and ℎis the output
function.
• Two problems:
• exploding gradients;
• vanishing gradients.
25

## Slide 65

EXPLODING GRADIENTS
• We multiply by the same 𝑊, and the norm of the gradient grows
or decreases exponentially.
• What do we do when it explodes?
26

## Slide 66

EXPLODING GRADIENTS
• We can simply bound the gradients from above!
• Two versions — bound either the norm or every value:
• sgd = optimizers.SGD(lr=0.01, clipnorm=1.)
• sgd = optimizers.SGD(lr=0.01, clipvalue=.05)
26

## Slide 67

EXPLODING GRADIENTS
• (Pascanu et al., 2013) – nice pictures about it:
26

## Slide 68

EXPLODING GRADIENTS
• Also explains where such gaps come from – RNNs have
“bifurcation points”:
26

## Slide 69

BIDIRECTIONAL RNN
• Sometimes we need context from both directions:
27

## Slide 70

BIDIRECTIONAL RNN
• Formally:
s𝑡= 𝜎(b + 𝑊s𝑡−1 + 𝑈x𝑡) ,
s′
𝑡= 𝜎(b′ + 𝑊′s′
𝑡+1 + 𝑈′x𝑡) ,
o𝑡= c + 𝑉s𝑡+ 𝑉′s′
𝑡,
y𝑡= ℎ(o𝑡) .
• This, of course, generalizes to any other sort of constructions.
27

## Slide 71

LSTM AND GRU

## Slide 72

LSTM
• Vanishing gradients: we have to multiply by 𝑊every time.
• This makes it impossible to have long-term memory.
• What do we do?..
29

## Slide 73

LSTM
• ...we have seen the basic idea in ResNet: we have to provide the
“constant error carousel”, a shortcut for the gradients.
• Idea from the mid-1990s (Schmidhuber): let’s construct RNNs
from a more complex unit that has the shortcut and controls
memory explicitly.
• LSTM (long short-term memory).
29

## Slide 74

LSTM
• “Vanilla” LSTM: c𝑡is the cell state, and h𝑡is the hidden state.
• Input gate and forget gate control whether we change c𝑡to the
new candidate cell state.
29

## Slide 75

LSTM
• Formally:
c′
𝑡
= tanh (𝑊𝑥𝑐x𝑡+ 𝑊ℎ𝑐h𝑡−1 + b𝑐′)
candidate cell state
i𝑡
= 𝜎(𝑊𝑥𝑖x𝑡+ 𝑊ℎ𝑖h𝑡−1 + b𝑖)
input gate
f𝑡
= 𝜎(𝑊𝑥𝑓x𝑡+ 𝑊ℎ𝑓h𝑡−1 + b𝑓)
forget gate
o𝑡
= 𝜎(𝑊𝑥𝑜x𝑡+ 𝑊ℎ𝑜h𝑡−1 + b𝑜)
output gate
c𝑡
= f𝑡⊙c𝑡−1 + i𝑡⊙c′
𝑡,
cell state
h𝑡
= o𝑡⊙tanh(c𝑡)
block output
• So the LSTM cell is able to control the cell state with the hidden
state and weights.
• Very flexible, and if the forget gate is closed (f𝑡= 1), we have
c𝑡= c𝑡−1 + i𝑡⊙c′
𝑡, so
𝜕c𝑡
𝜕c𝑡−1
= 1.
• The constant error carousel!
29

## Slide 76

LSTM
• LSTM was developed in mid-1990s (Hochreiter and Schmidhuber,
1995; 1997).
• Completely in its modern form in (Gers, Schmidhuber, 2000).
• One problem: we want to control c, but it’s unavailable for the
gates! They only see h𝑡−1, which is
h𝑡−1 = o𝑡−1 ⊙tanh(c𝑡−1).
• So if the output gate is closed the behaviour of LSTM does not
depend on cell state at all.
• This is not good...
29

## Slide 77

LSTM
• ...so of course we add a few more weight matrices (peepholes).
29

## Slide 78

LSTM
• Formally:
i𝑡= 𝜎(𝑊𝑥𝑖x𝑡+ 𝑊ℎ𝑖h𝑡−1 + 𝑊𝑝𝑖c𝑡−1 + b𝑖)
f𝑡= 𝜎(𝑊𝑥𝑓x𝑡+ 𝑊ℎ𝑓h𝑡−1 + 𝑊𝑝𝑓c𝑡−1 + b𝑓)
o𝑡= 𝜎(𝑊𝑥𝑜x𝑡+ 𝑊ℎ𝑜h𝑡−1 + 𝑊𝑝𝑜c𝑡−1 + b𝑜)
• Huge number of LSTM variations: we can basically remove any
kind of gate, add or remove each peephole, add or remove
activation functions etc.
• How do we choose?
29

## Slide 79

LSTM
• «LSTM: a Search Space Odyssey» (Greff et al., 2015).
• Shows an experimental comparison of many variations.
• In particular, some significantly simpler architectures (with one
less gate!) did not lose to the vanilla LSTM much.
• This brings us to...
29

## Slide 80

GRU
• ...Gated Recurrent Units (GRU); developed in (Cho et al., 2014).
• Also implements the constant error carousel, but simpler than
LSTM.
30

## Slide 81

GRU
• Formally:
u𝑡= 𝜎(𝑊𝑥𝑢x𝑡+ 𝑊ℎ𝑢h𝑡−1 + b𝑢)
r𝑡= 𝜎(𝑊𝑥𝑟x𝑡+ 𝑊ℎ𝑟h𝑡−1 + b𝑟)
h′
𝑡= tanh(𝑊𝑥ℎ′x𝑡+ 𝑊ℎℎ′(r𝑡⊙h𝑡−1))
h𝑡= (1 −u𝑡) ⊙h′
𝑡+ u𝑡⊙h𝑡−1
• Update gate and reset gate; there is no distinction between c𝑡
and h𝑡.
• Fewer matrices (6 vs. 8 or 11 with peepholes), fewer weights, but
only very slightly worse than LSTM.
• So you can fit more GRUs and have better networks on a given
computational budget.
30

## Slide 82

GRU
• There are other variations too.
• (Józefowicz, Zaremba, Sutskever, 2015): huge experimental
comparison, with an evolutionary approach.
• Identified three interesting architectures.
30

## Slide 83

THANK YOU!
Thank you for your attention!
31
