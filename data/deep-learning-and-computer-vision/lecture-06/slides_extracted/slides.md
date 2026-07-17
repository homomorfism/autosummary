# Slides (extracted) — slides.pdf

## Slide 1

ATTENTION AND TRANSFORMERS
Sergey Nikolenko
Harbour Space University
June 17, 2026
Random facts:
• on June 17, 1631, Mumtaz Mahal died giving birth to her fourteenth child, and her
grief-stricken husband, the Mughal emperor Shah Jahan, spent the next two decades
building her tomb, the Taj Mahal
• on June 17, 1885, the Statue of Liberty arrived in New York Harbor from France, dismantled
into 350 pieces packed in 214 crates; it then sat boxed up for months while Joseph Pulitzer's
newspaper shamed the public into paying for the pedestal it was to stand on
• on June 17, 1972, five White House operatives were arrested for burgling the offices of the
Democratic National Committee during an attempt by members of the administration of
Richard Nixon to illegally wiretap the political opposition (the Watergate scandal)
• on June 17, 1939, France carried out its last public guillotining, of the murderer Eugen
Weidmann at Versailles; the crowd was so unruly and the smuggled film footage so
scandalous that all further executions were moved behind prison walls
• on June 17, 1972, five men were caught breaking into the Democratic National Committee
headquarters at the Watergate complex in Washington; what was first dismissed as a
``third-rate burglary'' would two years later force a sitting U.S. president to resign
1

## Slide 2

LSTM AND GRU

## Slide 3

LSTM
• Vanishing gradients: we have to multiply by 𝑊every time.
• This makes it impossible to have long-term memory.
• What do we do?..
3

## Slide 4

LSTM
• ...we have seen the basic idea in ResNet: we have to provide the
“constant error carousel”, a shortcut for the gradients.
• Idea from the mid-1990s (Schmidhuber): let’s construct RNNs
from a more complex unit that has the shortcut and controls
memory explicitly.
• LSTM (long short-term memory).
3

## Slide 5

LSTM
• “Vanilla” LSTM: c𝑡is the cell state, and h𝑡is the hidden state.
• Input gate and forget gate control whether we change c𝑡to the
new candidate cell state.
3

## Slide 6

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
3

## Slide 7

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
3

## Slide 8

LSTM
• ...so of course we add a few more weight matrices (peepholes).
3

## Slide 9

LSTM
• Formally:
i𝑡= 𝜎(𝑊𝑥𝑖x𝑡+ 𝑊ℎ𝑖h𝑡−1 + 𝑊𝑝𝑖c𝑡−1 + b𝑖)
f𝑡= 𝜎(𝑊𝑥𝑓x𝑡+ 𝑊ℎ𝑓h𝑡−1 + 𝑊𝑝𝑓c𝑡−1 + b𝑓)
o𝑡= 𝜎(𝑊𝑥𝑜x𝑡+ 𝑊ℎ𝑜h𝑡−1 + 𝑊𝑝𝑜c𝑡−1 + b𝑜)
• Huge number of LSTM variations: we can basically remove any
kind of gate, add or remove each peephole, add or remove
activation functions etc.
• How do we choose?
3

## Slide 10

LSTM
• «LSTM: a Search Space Odyssey» (Greff et al., 2015).
• Shows an experimental comparison of many variations.
• In particular, some significantly simpler architectures (with one
less gate!) did not lose to the vanilla LSTM much.
• This brings us to...
3

## Slide 11

GRU
• ...Gated Recurrent Units (GRU); developed in (Cho et al., 2014).
• Also implements the constant error carousel, but simpler than
LSTM.
4

## Slide 12

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
4

## Slide 13

GRU
• There are other variations too.
• (Józefowicz, Zaremba, Sutskever, 2015): huge experimental
comparison, with an evolutionary approach.
• Identified three interesting architectures.
4

## Slide 14

WHAT IS ATTENTION?

## Slide 15

ATTENTION
• You are paying attention to me now, right?
• What does it mean?..
• Images from the retina go through something like a CNN, but
then we pay attention to a part of it and don’t care about the
rest. What does it mean?
• Turns out it’s a pretty difficult question.
• A.R. Luria: attention, memory, and cognitive functions.
6

## Slide 16

ATTENTION
• In reality it’s mostly about the interaction with working memory
(Knudsen, 2007):
6

## Slide 17

ATTENTION
• How do we implement this in ANNs? Especially “conscious”
attention.
• But “unconscious” attention as well; e.g., with images we don’t
see much at any given moment of time.
• The fovea is small:
• Simons, Chabris, 1999: https://www.youtube.com/watch?v=vJG698U2Mvo
6

## Slide 18

ATTENTION
• Our eyes work in saccades, and this doesn’t always help either:
6

## Slide 19

FOVEAL GLIMPSES
• A neural network also might want to consciously understand
“what to look at”.
• One of the first works (Larochelle, Hinton, 2010):
• They model the positions of saccades and learn to do a
sequence of glimpses.
• A sequence means...
7

## Slide 20

RECURRENT VISUAL ATTENTION

## Slide 21

RECURRENT VISUAL ATTENTION
• It all really happened in (Mnih et al., 2014), “Recurrent Models of
Visual Attention”:
• from the previous vector h𝑡−1 and new “glimpse” location 𝑡the
funciton 𝑓𝑔makes g𝑡, the input for step 𝑡;
• from h𝑡−1 and g𝑡function 𝑓ℎobtains h𝑡;
• from it, the “action” 𝑎𝑡= 𝑓𝑎(h𝑡) and the next “glimpse” location
𝑡+1 = 𝑓𝑙(h𝑡).
9

## Slide 22

RECURRENT VISUAL ATTENTION
• This is where a lot of different ML ideas come together; formal
model:
g𝑡=𝑓𝑔(x𝑡, l𝑡−1; 𝜃𝑔),
h𝑡=𝑓ℎ(h𝑡−1, g𝑡; 𝜃ℎ),
l𝑡∼𝑝(⋅∣𝑓𝑙(h𝑡; 𝜃𝑙)),
𝑎𝑡∼𝑝(⋅∣𝑓𝑎(h𝑡; 𝜃𝑎)).
• After an action we get a new observation x𝑡+1 and reward 𝑟𝑡that
we’ll get at the end, for correct classification.
• What does it remind of?..
9

## Slide 23

RECURRENT VISUAL ATTENTION
• ...that’s right, reinforcement learning!
• We need to train a stochastic policy 𝜋((l𝑡, 𝑎𝑡) ∣s1∶𝑡; 𝜃) that would
output the next action by history.
• Here 𝜋is defined via an RNN, and we need to optimize
𝐽(𝜃) = 𝔼𝑝(s1∶𝑇;𝜃) [𝑅] = 𝔼𝑝(s1∶𝑇;𝜃) [
𝑇
∑
𝑡=1
𝑟𝑡] .
• We won’t go into details, but RL is all about optimizing these
seemingly very complicated functions; here we can use the
REINFORCE algorithm and other policy gradient approaches.
9

## Slide 24

RECURRENT VISUAL ATTENTION
• Results:
9

## Slide 25

RECURRENT VISUAL ATTENTION
• Results:
• Here is attention walking around the picture:
9

## Slide 26

RECURRENT VISUAL ATTENTION
• In the next work Ba et al. (2015) made a deep model:
• And trained it differently, with variational approximations
(definitely won’t go there now, but the point is it’s all used in DL
too).
9

## Slide 27

RECURRENT VISUAL ATTENTION
• Recognizing two numbers:
• Interestingly, addition works differently:
9

## Slide 28

RECURRENT VISUAL ATTENTION
• (Gregor et al., 2015): DRAW: A Recurrent Neural Network For
Image Generation.
• Next step in visual attention development, a variation of the
variational autoencoder:
9

## Slide 29

ENCODER-DECODER AND ATTENTION

## Slide 30

MACHINE TRANSLATION
• Machine translation is an excellent test problem
• In essence, it’s a sequence-to-sequence problem, so it’s natural
to use RNNs:
• RNN models the sequence 𝑋= (𝑥1, 𝑥2, … , 𝑥𝑇) as
𝑝(𝑥1), 𝑝(𝑥2 ∣𝑥1), … , 𝑝(𝑥𝑇∣𝑥<𝑇) = 𝑝(𝑥𝑇∣𝑥𝑇−1, … , 𝑥1),
and now 𝑝(𝑋) is just
𝑝(𝑋) = 𝑝(𝑥1)𝑝(𝑥2 ∣𝑥1) … 𝑝(𝑥𝑘∣𝑥<𝑘) … 𝑝(𝑥𝑇∣𝑥<𝑇);
• that’s how RNNs are used in language models: predict the next
word from the previous word and hidden state.
• How do we apply this idea to translation?
11

## Slide 31

ENCODER-DECODER ARCHITECTURES
• Encoder-decoder architectures (Sutskever et al., 2014; Cho et al.,
2014):
• First encode, then decode back.
12

## Slide 32

ENCODER-DECODER ARCHITECTURES
• The same can work with machine translation:
• Problem: we need to compress everything down to a single
vector.
• It won’t work with long sequences, even long-ish individual
sentences.
12

## Slide 33

ATTENTION IN NEURAL NETWORKS
• Solution: let’s train special weights that show how important a
given part of the input is for the current output.
• Direct application of the idea – bidirectional LSTM plus attention
(Bahdanau et al. 2014):
13

## Slide 34

ATTENTION IN NEURAL NETWORKS
• Soft attention (Luong et al. 2015a; 2015b; Jean et al. 2015):
• encoder is a bidirectional RNN, with both contexts;
• the attention network estimates relevance – do we need to
translate this word right now?
13

## Slide 35

ATTENTION IN NEURAL NETWORKS
• Formally it’s very simple: compute attention weights 𝛼𝑡𝑗and
re-weigh context vectors:
𝑒𝑡𝑗= 𝑎(𝑧𝑡−1, 𝑗),
𝛼𝑡𝑗= softmax(𝑒𝑡𝑗; 𝑒𝑡∗),
𝑐𝑡= ∑
𝑗
𝛼𝑡𝑗ℎ𝑗, and now 𝑧𝑡= 𝑓(𝑠𝑡−1, 𝑦𝑡−1, 𝑐𝑖).
13

## Slide 36

ATTENTION IN NEURAL NETWORKS
• We can visualize what the network is looking at:
13

## Slide 37

ATTENTION IN NEURAL NETWORKS
• And we get a much better word order:
13

## Slide 38

ATTENTION IN NEURAL NETWORKS
• One unusual application – “Grammar as a Foreign Language”
(Vinyals et al., 2015)
13

## Slide 39

GOOGLE TRANSLATE
• (Wu et al., 2016): Google’s Neural Machine Translation System:
Bridging the Gap between Human and Machine Translation:
• the basic architecture of Google Translate was the same: encoder,
decoder, attention;
• RNNs are much deeper, 8 layers in both encoder and decoder:
14

## Slide 40

GOOGLE TRANSLATE
• (Wu et al., 2016): Google’s Neural Machine Translation System:
Bridging the Gap between Human and Machine Translation:
• stacked LSTM stop working beyond 4-5 layers;
• so they add residual connections, like ResNet:
14

## Slide 41

GOOGLE TRANSLATE
• (Wu et al., 2016): Google’s Neural Machine Translation System:
Bridging the Gap between Human and Machine Translation:
• the bottom layer is bidirectional:
14

## Slide 42

SHOW, ATTEND, AND TELL
• Now let’s get back to images and try to generate subtitles for
them.
• First work – “Show and Tell” (Vinyals et al., 2015):
15

## Slide 43

SHOW, ATTEND, AND TELL
• Straightforward architecture:
• objective function is just ∑(𝐼,𝑆) log 𝑝(𝑆∣𝐼; 𝜃), where 𝐼is the image
and 𝑆is the description;
• decompose and model 𝑝(𝑆𝑡∣𝐼, 𝑆0, … , 𝑆𝑡−1) with an LSTM-based
RNN;
• and use a CNN to extract image features.
15

## Slide 44

SHOW, ATTEND, AND TELL
• It was reasonable but not very good:
15

## Slide 45

SHOW, ATTEND, AND TELL
• “Show, Attend, and Tell” (Xu et al., 2015):
15

## Slide 46

SHOW, ATTEND, AND TELL
• Soft attention vs. hard attention:
• Soft attention – create an annotation with weights
𝜙({a}𝑖, {𝛼𝑖}) =
𝐿
∑
𝑖=1
𝛼𝑡,𝑖a𝑖.
15

## Slide 47

SHOW, ATTEND, AND TELL
• Hard attention is trained by maximizing the variational lower
bound
𝐿𝑠= ∑
𝑠
𝑝(𝑠∣a) log 𝑝(y ∣𝑠, a) ≤log ∑
𝑠
𝑝(𝑠∣a)𝑝(y ∣𝑠, a) = log 𝑝(y ∣a).
• We can take derivatives of 𝐿𝑠:
𝜕𝐿𝑠
𝜕𝑊= ∑
𝑠
𝑝(𝑠∣a) [𝜕log 𝑝(y ∣𝑠, a)
𝜕𝑊
+ log 𝑝(y ∣𝑠, a)𝜕log 𝑝(𝑠∣a)
𝜕𝑊
] .
• And then sample 𝑠𝑡with probabilities 𝛼𝑖and approximate the
expectation with a sample.
15

## Slide 48

SHOW, ATTEND, AND TELL
• Show, Attend, and Tell is often very good:
• And when it fails we can try to see why.
15

## Slide 49

SHOW, ATTEND, AND TELL
• Examples – hard attention:
15

## Slide 50

SHOW, ATTEND, AND TELL
• Examples – soft attention:
15

## Slide 51

SHOW, ATTEND, AND TELL
• Examples – hard attention:
15

## Slide 52

SHOW, ATTEND, AND TELL
• Examples – soft attention:
15

## Slide 53

SHOW, ATTEND, AND TELL
• Examples – hard attention:
15

## Slide 54

SHOW, ATTEND, AND TELL
• Examples – soft attention:
15

## Slide 55

TRANSFORMERS ARE ALL YOU NEED

## Slide 56

TRANSFORMER
• In 2017, it turned out that attention-based encoder-decoder
architectures can be both easier and more interesting
• Attention is all you need (Vaswani et al., 2017)
• The main idea, self-attention, turns out to be very fruitful for
various seq2seq problems
• The primary motivation is to try and avoid encoding sequences
with a fixed size vector
17

## Slide 57

TRANSFORMER
• General flowchart:
• Now in more detail...
17

## Slide 58

TRANSFORMER
• The essence is, again, an encoder-decoder architecture:
17

## Slide 59

TRANSFORMER
• Each block consists of a self-attention layer followed by a
feedforward layer that is applied independently to each input
position:
17

## Slide 60

TRANSFORMER
• Words are represented by vectors, and the feedforward layer
does everything in parallel:
17

## Slide 61

TRANSFORMER
• Overall more detailed picture:
• But what is self-attention?
17

## Slide 62

SELF-ATTENTION
• To understand self-attention, let us begin with information
retrieval.
18

## Slide 63

SELF-ATTENTION
• Both queries and documents share the same latent space,
although the ways of encoding them into this latent space may
be different (after all, even if both queries and documents are
texts they have very different properties)
• A search query is put through a query encoder to get to the
latent space
• Documents (represented by images in the figure) are also
represented in the same latent space via a different encoder
• To find the most relevant documents, we simply find the nearest
neighbors for the query in the latent space among the
documents; one often assumes that the latent space is linear
and the distance metric there is just the scalar product of
vectors, dist(𝑞, 𝑑) = Enc𝑞(𝑞)⊤Enc𝑑(𝑑).
18

## Slide 64

SELF-ATTENTION
• In self-attention, this intuition comes alive very abstractly. The
layer receives as input a sequence of vectors x1, x2, … , x𝐿, i.e., a
matrix 𝑋∈ℝ𝑑×𝐿.
• Queries, keys, and documents come from x𝑖themselves:
• multiplying x1 by a weight matrix 𝑊𝑄, we get the query vector
q1 = 𝑊𝑄x1; note that the dimension 𝑞of the query vectors,
q𝑖∈ℝ𝑞, may be different from (usually lower than) the input
dimension 𝑑, x𝑖∈ℝ𝑑;
• multiplying x𝑖by a weight matrix 𝑊𝐾, we get the key vectors
k𝑖= 𝑊𝐾x𝑖for 𝑖= 1, … , 𝐿; since we want queries and keys to
inhabit the same latent space, we have the keys with the same
dimension as queries, k𝑖∈ℝ𝑞, so 𝑊𝑉∈ℝ𝑞×𝑑;
• the third weight matrix 𝑊𝑉gets us value vectors v𝑖= 𝑊𝑉x𝑖for
𝑖= 1, … , 𝐿; these are the documents that we will “retrieve” by
their keys k𝑖; formally we have a different dimension 𝑣for the
values, v𝑖∈ℝ𝑣and 𝑊𝑉∈ℝ𝑣×𝑑; in practice usually 𝑣= 𝑞.
18

## Slide 65

SELF-ATTENTION
• Then we do the retrieval part, computing attention scores as
scalar products between queries and documents.
• We need to rescale q⊤
𝑖v𝑗, dividing it by √𝑞, and get the scores
through softmax to turn them into probabilities:
𝛼𝑖𝑗= softmax ( 1
√𝑞q𝑖𝐾⊤)
𝑗
,
where 𝐾∈ℝ𝑞×𝐿are all the keys combined in a matrix,
𝐾= 𝑊𝐾𝑋.
• Then we use the result as coefficients for a convex combination
of values v𝑗:
z𝑖= softmax ( 1
√𝑞q𝑖𝐾⊤) 𝑉,
where 𝑉∈ℝ𝑞×𝐿are the values, 𝑉= 𝑊𝑉𝑋.
18

## Slide 66

SELF-ATTENTION
• Overall structure of a self-attention layer:
18

## Slide 67

SELF-ATTENTION
• And that’s it for the intuition! We can combine the computation
of each z𝑖into a single formula in matrix form:
𝑍= softmax ( 1
√𝑞𝑄𝐾⊤) 𝑉.
• But this is only one way to “look at” the input vectors! What we
have defined now is not the full self-attention layer but only a
single self-attention head.
• We parallelize these computations along 𝐻different heads,
using different weight matrices 𝑊𝑄
1 , … 𝑊𝑄
𝐻, 𝑊𝐾
1 , … 𝑊𝐾
𝐻, and
𝑊𝑉
1 , … 𝑊𝑉
𝐻. This is known as multi-head attention.
18

## Slide 68

SELF-ATTENTION
• After 𝐻parallel heads we get 𝑣× 𝐿output matrices
𝑍1, 𝑍2, … , 𝑍𝐻, concatenate them all into 𝑍concat ∈ℝ𝐿×𝐻𝑣, and
add another weight matrix 𝑊𝑂∈ℝ𝐻𝑣×𝑑to compress the result
back to the necessary dimension:
𝑍= (𝑍concat𝑊𝑂)
⊤.
• With 𝑊𝑂, the self-attention layer can mix up representations
obtained from different attention heads; this is also an
important way to add more flexibility and expressiveness to the
architecture.
18

## Slide 69

SELF-ATTENTION
• Multi-head attention:
• This is the most important part, but we are not yet done.
18

## Slide 70

THE DECODER SIDE
• The decoder part has two more layer types: masked
self-attention and encoder-decoder attention.
• Masked attention basically means that since the decoder works
autoregressively, it should not peek at the tokens that it has not
produced yet.
• To do that, it’s easier to just input the whole sequence and mask
future positions inside self-attention layers themselves.
• Formally this means that we set the softmax arguments to −∞
for future tokens, which means that their attention weights will
always be zero.
19

## Slide 71

THE DECODER SIDE
• Encoder-decoder attention is a variation on the self-attention
mechanism that conditions itself on the results of the encoder.
• Sounds difficult... but in fact it’s an almost trivial modification!
We have the exact same self-attention layer but use different
vectors as input:
• to create the queries, we use vectors from the previous layer, i.e.,
current representations of already generated output tokens;
• but for the “documents” in our “retrieval” task, i.e., for the key and
value vectors, we use the vectors from the decoder.
• Informally, this means that we are doing “retrieval” on the
encoder’s output with queries made of already produced tokens.
• Formally, all dimensions match nicely: there are 𝐿terms in the
softmax argument for each vector, but the number of queries
and hence number of outputs matches the number of inputs.
19

## Slide 72

TOKENIZATION
• We use an embedding layer but how do we split text into tokens?
• Byte-pair encoding: an interesting idea based on Huffman
coding.
• Let’s begin by building a vocabulary:
{cat ∶10, pet ∶12, mat ∶5, rat ∶8, eats ∶4}.
20

## Slide 73

TOKENIZATION
• Then split it into symbols and count pairs of symbols:
{cat ∶10, pet ∶12, mat ∶5, rat ∶8, eats ∶4},
{𝑐∶10, 𝑎∶27, 𝑡∶39, 𝑝∶12, 𝑒∶16, 𝑚∶5, 𝑟∶8, 𝑠∶4},
{𝑐𝑎∶10, 𝑎𝑡∶27, 𝑝𝑒∶12, 𝑒𝑡∶12, 𝑚𝑎∶5, 𝑟𝑎∶8, 𝑒𝑎∶4, 𝑡𝑠∶4}.
20

## Slide 74

TOKENIZATION
• Now take the most frequent pair (“at”) and re-encode it with a
single new symbol (Z) that is added to the vocabulary:
{cZ ∶10, pet ∶12, mZ ∶5, rZ ∶8, eZs ∶4},
{𝑐∶10, 𝑍∶27, 𝑡∶12, 𝑝∶12, 𝑒∶16, 𝑚∶5, 𝑟∶8, 𝑠∶4},
{𝑐𝑍∶10, 𝑝𝑒∶12, 𝑒𝑡∶12, 𝑚𝑍∶5, 𝑟𝑍∶8, 𝑒𝑍∶4, 𝑍𝑠∶4}.
20

## Slide 75

TOKENIZATION
• Now we can choose the new most frequent pair—in this case pe
or et—and replace it with another new symbol, say Y:
{cZ ∶10, Yt ∶12, mZ ∶5, rZ ∶8, eZs ∶4},
{𝑐∶10, 𝑍∶27, 𝑌∶12, 𝑡∶12, 𝑒∶4, 𝑚∶5, 𝑟∶8, 𝑠∶4},
{𝑐𝑍∶10, 𝑌𝑡∶12, 𝑚𝑍∶5, 𝑟𝑍∶8, 𝑒𝑍∶4, 𝑍𝑠∶4}.
• And so on, until we reach the necessary vocabulary size.
20

## Slide 76

POSITIONAL ENCODING
• In the Transformer, every input token can “look at” any other
input token directly, with no regard for the distance between
them in the input sequence.
• This is great compared to RNNs!
• But it means that we have a fixed bounded context window and,
moreover, since attention weights cover all tokens uniformly, we
lose the sequence: a self-attention layer does not know that
some tokens are “next to each other” or “closer in the input
sequence”.
• We need to give the Transformer an idea of the input sequence
artificially; this is done via positional encodings.
21

## Slide 77

POSITIONAL ENCODING
• Positional encodings are vectors added to the embedding that
reflect where in the sequence the current token is.
• How could we encode the position? We could have a number
that is increasing with the position but it is hard to get right:
• if we use an increasing sequence like 1, 2, 3, …, it will not
generalize to sequences longer than the usual length in the
training set, and the network’s behaviour would be much less well
defined for large values;
• if we use a given interval, say [0, 1], and break it down into the
necessary number of pieces, then the positional encoding would
have no idea how many words are actually there between two
tokens: the distance from 0 to 1
2 could be 1 token or 100.
21

## Slide 78

POSITIONAL ENCODING
• So we use something like positional numbers (where each digit
forms a periodic function with different periods), but with
continuous periodic functions, sine waves:
PE (pos, 2𝑖) = sin (
pos
100002𝑖/𝑑) ,
PE (pos, 2𝑖+ 1) = cos (
pos
100002𝑖/𝑑) ,
where pos is the token position, 𝑑is the embedding dimension.
21

## Slide 79

TRANSFORMER RESULTS
• As a result, the Transformer trains weights for how other words
participate in processing the current word:
22

## Slide 80

TRANSFORMER RESULTS
• Self-attention is important: first, computationally; second, it
reduces path lengths between words; third, potentially adds
interpretability:
22

## Slide 81

TRANSFORMER RESULTS
• Works better, trains 100x faster:
22

## Slide 82

THANK YOU!
Thank you for your attention!
23
