# Attention and Transformers

## LSTM and GRU

### LSTM

Recurrent neural networks suffer from vanishing gradients because the weight matrix \(W\) is multiplied at each time step, making it impossible to retain long-term memory. The basic idea for a solution had already appeared in ResNet: provide a “constant error carousel”, a shortcut for the gradients. This led (Schmidhuber, mid-1990s) to a more complex recurrent unit that explicitly controls memory: **Long Short-Term Memory (LSTM)** (Hochreiter & Schmidhuber, 1995; 1997; modern form by Gers & Schmidhuber, 2000).

The LSTM cell maintains a **cell state** \(c_t\) and a **hidden state** \(h_t\). Three gates—input, forget, and output—regulate information flow. The formal definition is:

\[
\begin{aligned}
c'_t &= \tanh(W_{xc} x_t + W_{hc} h_{t-1} + b_{c'}) \quad &\text{(candidate cell state)} \\[2pt]
i_t  &= \sigma(W_{xi} x_t + W_{hi} h_{t-1} + b_i) \quad &\text{(input gate)} \\[2pt]
f_t  &= \sigma(W_{xf} x_t + W_{hf} h_{t-1} + b_f) \quad &\text{(forget gate)} \\[2pt]
o_t  &= \sigma(W_{xo} x_t + W_{ho} h_{t-1} + b_o) \quad &\text{(output gate)} \\[2pt]
c_t  &= f_t \odot c_{t-1} + i_t \odot c'_t \quad &\text{(cell state)} \\[2pt]
h_t  &= o_t \odot \tanh(c_t) \quad &\text{(block output)}
\end{aligned}
\]

> **Constant error carousel.** If the forget gate is fully open (\(f_t = 1\)), then \(c_t = c_{t-1} + i_t \odot c'_t\) and consequently \(\frac{\partial c_t}{\partial c_{t-1}} = 1\), allowing gradients to flow unchanged.

One problem remains: the gates only see the hidden state \(h_{t-1} = o_{t-1} \odot \tanh(c_{t-1})\). If the output gate is closed, the LSTM’s behaviour becomes independent of the cell state. This is remedied by adding **peephole connections**—extra weight matrices that give the gates direct access to \(c_{t-1}\):

\[
\begin{aligned}
i_t &= \sigma(W_{xi} x_t + W_{hi} h_{t-1} + W_{pi} c_{t-1} + b_i) \\
f_t &= \sigma(W_{xf} x_t + W_{hf} h_{t-1} + W_{pf} c_{t-1} + b_f) \\
o_t &= \sigma(W_{xo} x_t + W_{ho} h_{t-1} + W_{po} c_{t-1} + b_o)
\end{aligned}
\]

A huge number of LSTM variations exist—any gate can be removed, peepholes can be added or omitted, activation functions altered, etc. Greff et al. (2015) (“LSTM: a Search Space Odyssey”) experimentally compared many variants and found that some significantly simpler architectures (with one fewer gate) performed nearly as well as vanilla LSTM.

### GRU

**Gated Recurrent Units (GRU)**, introduced by Cho et al. (2014), also implement the constant error carousel but with a simpler design. The GRU merges cell state and hidden state into a single vector \(h_t\) and uses only two gates:

\[
\begin{aligned}
u_t   &= \sigma(W_{xu} x_t + W_{hu} h_{t-1} + b_u) \quad &\text{(update gate)} \\
r_t   &= \sigma(W_{xr} x_t + W_{hr} h_{t-1} + b_r) \quad &\text{(reset gate)} \\[2pt]
h'_t  &= \tanh(W_{xh'} x_t + W_{hh'} (r_t \odot h_{t-1})) \quad &\text{(candidate state)} \\[2pt]
h_t   &= (1 - u_t) \odot h'_t + u_t \odot h_{t-1}
\end{aligned}
\]

Compared to LSTM, GRU has fewer weight matrices (6 vs. 8, or 11 with peepholes), fewer parameters, and is only slightly worse in performance. For a fixed computational budget one can therefore use more GRU units and obtain better networks. Other variations have been explored; Józefowicz et al. (2015) conducted a huge experimental comparison with an evolutionary approach and identified three particularly interesting architectures.

## What is Attention?

### Biological Attention and Saccades

Attention is in large part the interaction with working memory (Knudsen, 2007). In vision, the human fovea is very small—we only perceive a tiny high-resolution patch at any moment. The eyes move in rapid saccades, sequentially fixating on different parts of the scene. This can be both conscious and unconscious. A famous illustration is the Invisible Gorilla experiment (Simons & Chabris, 1999), where observers concentrating on a ball-passing task completely miss a person in a gorilla suit walking through the frame.

### Foveal Glimpses: Early Models

A neural network might also benefit from consciously deciding “what to look at”. One of the first works (Larochelle & Hinton, 2010) modelled the positions of saccades and learned a sequence of **glimpses**.

### Recurrent Models of Visual Attention

The idea was fully realized in “Recurrent Models of Visual Attention” (Mnih et al., 2014). At each time step, a recurrent network receives a glimpse \(g_t\) from the current observation and the previous location, updates its hidden state \(h_t\), and outputs a new location \(l_t\) and action \(a_t\):

\[
\begin{aligned}
g_t &= f_g(x_t, l_{t-1}; \theta_g), \\
h_t &= f_h(h_{t-1}, g_t; \theta_h), \\
l_t &\sim p(\cdot \mid f_l(h_t; \theta_l)), \\
a_t &\sim p(\cdot \mid f_a(h_t; \theta_a)).
\end{aligned}
\]

A reward \(r_t\) is received after the action, with the goal of correct final classification. This defines a stochastic policy \(\pi((l_t,a_t)\mid s_{1:t};\theta)\) implemented by an RNN, and the objective is to maximise expected total reward:

\[
J(\theta) = \mathbb{E}_{p(s_{1:T};\theta)}[R] = \mathbb{E}_{p(s_{1:T};\theta)}\!\left[\sum_{t=1}^T r_t\right].
\]

This is a reinforcement learning problem; the REINFORCE algorithm and other policy gradient methods can be used to optimise it.

*(Figures show attention trajectories walking around an image, focusing on the relevant object.)*

Subsequent work by Ba et al. (2015) extended the approach to deep models trained with variational approximations. Gregor et al. (2015) proposed **DRAW: A Recurrent Neural Network For Image Generation**, a recurrent attention-based variational autoencoder.

## Encoder-Decoder Architectures and Attention

### Machine Translation with Encoder-Decoder RNNs

Machine translation is a canonical sequence-to-sequence problem. An RNN language model factors a sequence \(X = (x_1,\dots,x_T)\) as  

\[
p(X) = p(x_1) p(x_2 \mid x_1) \cdots p(x_T \mid x_{<T}).
\]

For translation, one can use an **encoder-decoder architecture** (Sutskever et al., 2014; Cho et al., 2014): an RNN encoder compresses the source sentence into a fixed-size vector, and an RNN decoder generates the target sentence from that vector. The critical limitation is that everything must be squeezed through a single fixed-size vector; performance degrades on long sequences.

### Attention Mechanism

The solution is to let the decoder *attend* to all encoder hidden states, weighted by relevance. Bahdanau et al. (2014) combined a bidirectional LSTM encoder with an attention mechanism. Soft attention (Luong et al., 2015a,b; Jean et al., 2015) computes attention weights \(\alpha_{tj}\) as follows:

\[
e_{tj} = a(z_{t-1}, j), \qquad 
\alpha_{tj} = \operatorname{softmax}(e_{tj}), \qquad 
c_t = \sum_j \alpha_{tj} h_j,
\]

and the decoder state is updated as \(z_t = f(s_{t-1}, y_{t-1}, c_t)\). Visualisations of the attention weights show clear word alignments and much better target word order. Vinyals et al. (2015) applied the same idea to parsing, treating “Grammar as a Foreign Language”.

### Google’s Neural Machine Translation System

Wu et al. (2016) (“Google’s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation”) scaled the architecture to very deep stacks: 8 encoder layers and 8 decoder layers of LSTMs. Stacked LSTMs stop working beyond 4–5 layers, so they added residual connections (like ResNet). The bottom layer of the encoder is bidirectional. This system powered Google Translate for several years.

## Show, Attend, and Tell: Image Captioning with Attention

**Show and Tell** (Vinyals et al., 2015) used a CNN to extract a fixed image feature vector, then fed it to an LSTM decoder that generated a caption word by word, maximising \(\sum_{(I,S)} \log p(S \mid I; \theta)\). It worked reasonably well but lacked fine-grained alignment.

**Show, Attend, and Tell** (Xu et al., 2015) introduced spatial attention over CNN feature vectors \(\{a_i\}_{i=1}^L\). At each step, a context vector is formed as \(\phi(\{a_i\},\{\alpha_{t,i}\}) = \sum_{i=1}^L \alpha_{t,i} a_i\). Two variants were studied:

- **Soft attention**: a deterministic weighted sum, differentiable and trained end-to-end.
- **Hard attention**: stochastic, trained by maximising a variational lower bound:

\[
L_s = \sum_s p(s \mid a) \log p(y \mid s, a) \;\leq\; \log \sum_s p(s \mid a) p(y \mid s, a) = \log p(y \mid a).
\]

The gradient is

\[
\frac{\partial L_s}{\partial W} = \sum_s p(s \mid a) \!\left[ \frac{\partial \log p(y \mid s, a)}{\partial W} + \log p(y \mid s, a) \frac{\partial \log p(s \mid a)}{\partial W} \right],
\]

and one approximates the expectation by sampling \(s\) from the attention distribution \(\alpha_i\).

*(Figures demonstrate generated captions with both hard and soft attention, highlighting the attended regions; failures can be analysed by inspecting attention.)*

## Transformers

### Overview

The **Transformer** (Vaswani et al., 2017) abandons recurrence entirely, using only attention. The architecture follows the encoder-decoder pattern. Each encoder block consists of a **self-attention** layer followed by a position-wise feedforward network; the decoder adds **masked self-attention** and **encoder-decoder attention**. Because all tokens are processed in parallel, training is orders of magnitude faster than with RNNs.

### Self-Attention Mechanism

Self-attention is inspired by information retrieval. An input sequence of vectors \(X \in \mathbb{R}^{d \times L}\) is transformed into **queries** \(Q = W_Q X\), **keys** \(K = W_K X\), and **values** \(V = W_V X\), with \(W_Q, W_K \in \mathbb{R}^{q \times d}\) and \(W_V \in \mathbb{R}^{v \times d}\) (usually \(v = q\)). The attention scores are scaled dot-products:

\[
\operatorname{Attention}(Q, K, V) = \operatorname{softmax}\!\left( \frac{1}{\sqrt{q}} Q K^{\top} \right) V .
\]

Scaling by \(1/\sqrt{q}\) prevents extremely small gradients. The output is an \(L \times v\) matrix.

### Multi-Head Attention

A single attention head only captures one type of relationship. To enrich the representation, the Transformer uses **multi-head attention**: \(H\) different sets of weight matrices produce \(H\) independent outputs \(Z^1,\dots,Z^H\). These are concatenated into \(Z_{\text{concat}} \in \mathbb{R}^{L \times Hv}\) and projected back to dimension \(d\):

\[
Z = \bigl(Z_{\text{concat}} W_O\bigr)^{\top}, \qquad W_O \in \mathbb{R}^{Hv \times d}.
\]

This allows the layer to mix information from different representation subspaces.

### Decoder: Masked Attention and Encoder-Decoder Attention

Because the decoder generates tokens autoregressively, it must not attend to future positions. **Masked self-attention** sets the pre-softmax values for future tokens to \(-\infty\), forcing their attention weights to zero.

**Encoder-decoder attention** is essentially the same attention mechanism, but the queries come from the previous decoder layer (the partially generated output), while keys and values come from the encoder’s final layer. Thus the decoder performs “retrieval” over the encoder’s output, conditioned on the tokens already produced.

### Tokenization: Byte-Pair Encoding

Transformers use subword tokenization, most commonly **Byte-Pair Encoding (BPE)**. Starting from vocabulary counts:

\[
\{\text{cat}:10,\; \text{pet}:12,\; \text{mat}:5,\; \text{rat}:8,\; \text{eats}:4\},
\]

split into characters and count pairs:

\[
\begin{aligned}
\text{characters}&: \{c:10, a:27, t:39, p:12, e:16, m:5, r:8, s:4\}, \\
\text{pairs}&: \{ca:10, at:27, pe:12, et:12, ma:5, ra:8, ea:4, ts:4\}.
\end{aligned}
\]

The most frequent pair “at” (frequency 27) is replaced by a new symbol \(Z\):

\[
\{cZ:10,\; pet:12,\; mZ:5,\; rZ:8,\; eZs:4\}.
\]

This process is repeated—next replacing “pe” or “et” with \(Y\)—until the desired vocabulary size is reached. BPE efficiently handles rare words by encoding frequent subword units.

### Positional Encoding

Self-attention is completely invariant to token order. To inject sequence information, the Transformer adds **positional encodings** to the input embeddings. The encodings use sine and cosine functions of different frequencies:

\[
\begin{aligned}
PE_{(pos, 2i)}   &= \sin\!\left(\frac{pos}{10000^{2i/d}}\right), \\
PE_{(pos, 2i+1)} &= \cos\!\left(\frac{pos}{10000^{2i/d}}\right),
\end{aligned}
\]

where \(pos\) is the token position and \(d\) the embedding dimension. This scheme allows the model to extrapolate to longer sequences than seen during training, and relative distances can be inferred from phase differences.

### Results

The Transformer trains 100× faster than comparable recurrent models and achieves superior translation quality. Self-attention drastically shortens the path length between any two positions, facilitating long-range dependencies. The attention weights themselves offer a degree of interpretability—one can visualise which tokens the model is attending to at each layer. *(Figures show example attention weight matrices, revealing syntactic and semantic relations.)*
