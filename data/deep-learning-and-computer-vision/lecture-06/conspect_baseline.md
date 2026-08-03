# Attention and Transformers

## Recurrent Networks and the Vanishing Gradient Problem *[00:01]*

Any recurrent neural network (RNN) is effectively a very deep network – its depth equals the input sequence length. As activations and gradients propagate through time, we repeatedly multiply by the same weight matrix \(W\). If the spectral radius of \(W\) is less than 1, the gradients shrink exponentially (**vanishing gradients**); if it is greater than 1, they explode. Exploding gradients cause numerical overflows and obvious failure, but vanishing gradients are far more dangerous: the loss still decreases, gradients w.r.t. \(W\) do not vanish because \(W\) participates in the most recent steps. The network still trains, yet it makes its decisions based only on the last few elements of the sequence – it **loses the ability to have long‑term memory**.

## LSTM — Long Short‑Term Memory *[09:08]*

To give the gradient a shortcut past the repeated multiplications, we introduce a **constant error carousel**, exactly the same idea as residual connections in ResNet. This was pioneered in the 1990s (Hochreiter & Schmidhuber, 1995/1997; Gers & Schmidhuber, 2000) and gave rise to the most important recurrent unit.

An LSTM maintains two separate vectors: the **cell state** \(c_t\) (the “highway” for long‑term memory) and the **hidden state** \(h_t\) (the normal working memory). The whole cell is organized around **gates** – tiny linear classifiers that output a vector of values in \((0,1)\) via a sigmoid and act as a **control signal**, deciding what to erase, write, or read.

### The LSTM Cell

| Gate / candidate | Formula |
|------------------|---------|
| Candidate cell state | \(c'_t = \tanh(W_{xc}x_t + W_{hc}h_{t-1} + b_{c'})\) |
| Input gate | \(i_t = \sigma(W_{xi}x_t + W_{hi}h_{t-1} + b_i)\) |
| Forget gate | \(f_t = \sigma(W_{xf}x_t + W_{hf}h_{t-1} + b_f)\) |
| Output gate | \(o_t = \sigma(W_{xo}x_t + W_{ho}h_{t-1} + b_o)\) |
| New cell state | \(c_t = f_t \odot c_{t-1} + i_t \odot c'_t\) |
| New hidden state | \(h_t = o_t \odot \tanh(c_t)\) |

**Intuition**  
- The **forget gate** \(f_t\) multiplies the old cell state element‑wise: values near 1 “keep”, near 0 “erase”.  
- The **candidate** \(c'_t\) proposes new numbers to write.  
- The **input gate** \(i_t\) selects which parts of \(c'_t\) are actually written. Because the forget gate already erased the corresponding cells, writing is simply **addition**.  
- The **output gate** \(o_t\) decides which parts of the updated cell state should be exposed to the next hidden state (and used by the rest of the network).

Crucially, when the forget gate is fully open (\(f_t \to 1\)), we obtain

\[
c_t = c_{t-1} + i_t \odot c'_t \quad\Longrightarrow\quad \frac{\partial c_t}{\partial c_{t-1}} = 1,
\]

which provides the **constant error carousel** – a highway for gradients that is only interrupted when we explicitly choose to erase.

LSTM has many weight matrices (eight in the vanilla version, up to eleven with peepholes) and requires large memory sizes (\(d \ge 256\) typically), so it is expensive to train. Only around 2015 did sufficient compute become available to train huge LSTMs. Yet it **still stands** – modern recurrent systems (e.g. AlphaStar) consistently prefer LSTM over other recurrent units.

### Peephole Connections

A known issue: the gates only see \(h_{t-1}\), which is \(o_{t-1} \odot \tanh(c_{t-1})\). If the output gate is closed, the gates have no direct information about the cell state. The fix is to add direct **peepholes** – extra weight matrices that multiply \(c_{t-1}\) in the gate equations:

\[
i_t = \sigma(W_{xi}x_t + W_{hi}h_{t-1} + W_{pi}c_{t-1} + b_i),\quad
f_t = \sigma(\dots + W_{pf}c_{t-1} + \dots),\quad
o_t = \sigma(\dots + W_{po}c_{t-1} + \dots).
\]

Many LSTM variations exist. The survey “LSTM: A Search Space Odyssey” (Greff et al., 2015) showed that you can even remove an entire gate without much performance loss.

## GRU — Gated Recurrent Unit *[30:53]*

Developed by Cho et al. (2014), the GRU simplifies LSTM while preserving the error carousel.

- There is **no separate cell state**; everything is in the hidden state \(h_t\).
- Instead of separate forget and input gates, a single **update gate** \(u_t\) produces a convex combination of the old state and a candidate:

\[
\begin{aligned}
u_t &= \sigma(W_{xu}x_t + W_{hu}h_{t-1} + b_u) \\
r_t &= \sigma(W_{xr}x_t + W_{hr}h_{t-1} + b_r) \\
h'_t &= \tanh(W_{xh'}x_t + W_{hh'}(r_t \odot h_{t-1})) \\
h_t &= (1 - u_t) \odot h'_t + u_t \odot h_{t-1}
\end{aligned}
\]

- \(u_t\) close to 1 keeps the old memory; \(u_t\) close to 0 replaces it with the candidate.  
- The **reset gate** \(r_t\) selects which parts of the previous state to use when computing the candidate.

GRU has only 6 weight matrices (vs. 8 for vanilla LSTM, 11 with peepholes). In 2015–2016 NLP papers almost universally adopted GRU because it is more efficient. Today, however, large‑scale practice has **switched back to LSTM** for reasons that are mostly empirical: LSTM seems to scale better to truly hard problems.

> **Take‑away:** Both LSTM and GRU implement the constant error carousel, enabling gradient flow through arbitrarily long sequences. LSTM remains the gold standard for large recurrent networks.

---

## What is Attention? *[41:48]*

Neurobiologically, attention is as fundamental as memory and cognition (A.R. Luria). It acts as a **filter** between a very short‑term working memory (a few seconds) and further processing. Crucially, unlike a convolutional network that processes every pixel equally, humans can **completely miss** objects in their field of view if attention is directed elsewhere (the famous “invisible gorilla” experiment).

Our vision itself is structured around **foveal glimpses** – high resolution only at the centre of gaze, with the rest blurry – and the brain stitches these glimpses together by rapid **saccadic** eye movements. The original motivation for attention in neural networks was to mimic this efficiency: look at a few small, high‑resolution patches of a large image, choose where to look next, and make a decision, thus drastically reducing input size.

### Recurrent Visual Attention (early models) *[54:26]*

Early works (Mnih et al., 2014; Ba et al., 2015) used an RNN to select a sequence of glimpse locations. At each step:

\[
g_t = f_g(\mathbf{x}_t, l_{t-1}),\quad
h_t = f_h(h_{t-1}, g_t),\quad
l_t \sim p(\cdot \mid f_l(h_t)),\quad
a_t \sim p(\cdot \mid f_a(h_t))
\]

The network received a reward only at the end (e.g. correct classification), so training was done with reinforcement learning (e.g. REINFORCE). Later models like DRAW used variational inference. These models are now **outdated**, but they established the principle of looking at parts of the input sequentially.

---

## Encoder–Decoder and Attention *[55:27]*

The real breakthrough came by applying attention to **encoder–decoder** sequence‑to‑sequence models.

**The bottleneck problem**  
A standard RNN encoder compresses the entire input sentence into a **single vector** \(z\). For short sentences this works, but:

- If \(z\) is too small, it cannot hold enough information for long inputs.
- If \(z\) is made very large, the decoder LSTM becomes gigantic, requiring quadratic numbers of weights that cannot be trained.

As a result, quality is good for short sentences and **collapses for long ones**.

### Attention as a soft lookup *[1:03:14]*

The solution is to produce a representation for **every input token** and let the decoder **reweigh** them at each step. Concretely:

1. A **bidirectional encoder** produces a vector \(z_i\) for every input token \(i\).
2. At decoder step \(t\) (hidden state \(s_{t-1}\)), an **attention network** \(a\) scores each input position:

\[
e_{t j} = a(s_{t-1}, z_j)
\]

3. Softmax turns the scores into a convex combination:

\[
\alpha_{t j} = \operatorname{softmax}(e_{t1}, e_{t2}, \dots)
\]

4. The context vector is the weighted sum:

\[
c_t = \sum_j \alpha_{t j} z_j
\]

5. The decoder now uses \(c_t\) along with the previous output \(y_{t-1}\) and its hidden state to produce the next token.

The attention network is **tiny** – typically around 2 % of the total parameters – yet it **drives the results**. It is **never explicitly supervised** (we don’t know which source word aligns to which target word). The whole model is trained end‑to‑end on parallel sentences, and the attention weights **emerge** as meaningful alignments.

Interpretable attention matrices are a hallmark of this approach: for translation, they usually form a diagonal, with off‑diagonal spikes for reordered words or multi‑word phrases (e.g. French “la destruction” → English “destruction”).

**Practical effect**  
Around 2015‑2016, Google Translate switched to such an architecture and experienced a **phase transition** in quality – it became good enough that post‑editing was faster than translating from scratch.

### Beyond text: image captioning with attention

The same idea works for images: instead of compressing a CNN’s output into a single vector, we keep a \(14 \times 14\) feature map and compute attention over these spatial locations. The caption generator can then **look at different parts** of the image while generating each word (e.g. “woman”, “throwing”, “frisbee”). Hard attention (sampling a single location) and soft attention (convex combination) were both explored (Xu et al., 2015).

---

## Transformers — Attention Is All You Need *[1:46:31]*

Vaswani et al. (2017) proposed an architecture built entirely on attention, discarding recurrence. The original paper modestly aimed for comparable performance with higher efficiency, but the transformer turned out to be **extremely general and scalable** – it now underlies nearly all state‑of‑the‑art models.

### High‑level structure

The transformer is an **encoder–decoder** design for machine translation:

- **Encoder**: 6 identical layers, each containing a self‑attention sublayer and a feed‑forward sublayer, with residual connections and layer normalization.
- **Decoder**: 6 identical layers, each containing a **masked** self‑attention, an **encoder–decoder attention**, and a feed‑forward sublayer (again with residuals and layer norm).
- Input tokens are first passed through a learned **embedding** layer, becoming vectors. The whole transformer operates on sequences of vectors, rewriting them context‑aware representations.

The decoder is autoregressive: it generates one token at a time, and a final linear + softmax layer produces output token probabilities.

### Self‑Attention – the core *[2:02:20]*

**Information retrieval intuition**  
In neural search, documents and queries are encoded into a shared latent space, and relevance is measured by the dot product. Self‑attention applies this idea to **the same set of vectors**: each input vector is simultaneously the query and a “document”.

From an input sequence \(X = [x_1, \dots, x_L]\) (each \(x_i \in \mathbb{R}^D\)) we compute three projections:

\[
Q = X W_Q \quad (W_Q \in \mathbb{R}^{D \times d_k}),\qquad
K = X W_K \quad (W_K \in \mathbb{R}^{D \times d_k}),\qquad
V = X W_V \quad (W_V \in \mathbb{R}^{D \times d_v})
\]

- **Queries** \(Q\) and **keys** \(K\) live in the same space (dimension \(d_k\)); **values** \(V\) can have a different dimension \(d_v\) (often \(d_v = d_k\)).

The **attention weights** are computed as scaled dot‑products:

\[
\operatorname{Attention}(Q, K, V) = \operatorname{softmax}\!\left(\frac{Q K^T}{\sqrt{d_k}}\right) V
\]

- Dot products \(Q K^T\) yield a matrix of raw affinities between every query and every key.
- **Scaling by \(\sqrt{d_k}\)** prevents the dot products from growing too large: with random vectors, the variance of the dot product is \(\approx d_k\); without scaling the softmax would saturate into one‑hot vectors, losing gradient signal.
- Softmax converts each row into a convex combination.
- Multiplying by \(V\) produces the output as a weighted sum of the value vectors.

Every output position is directly connected to **every input position** in a single step – the **path length is 1**, regardless of distance in the sequence. This is a huge advantage over RNNs, but the cost is a **quadratic complexity** \(O(L^2)\) in the sequence length, which is the central computational challenge of transformers.

### Multi‑Head Attention *[2:36:00]*

A single attention head projects the input into a small space (\(d_k \approx 64\)), which is too small to capture all relevant relationships. Instead, we run \(H\) independent heads in parallel, each with its own \(W_Q^{(h)}, W_K^{(h)}, W_V^{(h)}\):

\[
\operatorname{MultiHead}(Q, K, V) = \operatorname{Concat}(\text{head}_1, \dots, \text{head}_H) W_O
\]

where \(\text{head}_h = \operatorname{Attention}(X W_Q^{(h)}, X W_K^{(h)}, X W_V^{(h)})\) and \(W_O \in \mathbb{R}^{H d_v \times D}\) projects the concatenated result back to the model dimension \(D\). This gives the model multiple “ways of looking” at the data and mixes the different perspectives.

### Decoder‑specific attention layers

**Masked Self‑Attention**  
The decoder is trained to predict the next token given the prefix. For efficiency, the whole output sequence is fed at once, but future tokens must not influence the prediction. **Causal masking** zeros out the softmax inputs for future positions, setting those attention weights to zero.

**Encoder–Decoder Attention**  
This is a **cross‑attention** layer:  
- **Queries** come from the decoder’s previous layer (the tokens produced so far).  
- **Keys** and **values** come from the encoder’s output (the full source representation).  

It is essentially the same self‑attention mechanism, but with \(Q, K, V\) originating from two different sequences. The resulting attention matrix is **not square**, and it gives the decoder a direct window into the source.

### Tokenization with Byte‑Pair Encoding *[2:54:48]*

Using full words as tokens would require a vocabulary of millions (including typos, inflected forms, etc.); using characters would make sequences too long. **BPE** is a deterministic Huffman‑coding procedure that builds a subword vocabulary:

1. Start with individual characters as the initial vocabulary.
2. Count all adjacent pairs of tokens in the corpus.
3. Replace the most frequent pair with a new token (e.g. ‘a’ + ‘t’ → ‘Z’).
4. Repeat until the desired vocabulary size is reached.

Common morphemes like “‑ed”, “‑tion” become single tokens; rare words stay as multiple subword tokens.

### Positional Encodings *[3:02:30]*

Because the self‑attention layer treats the input as an unordered set, we must inject **position information**. Two principal approaches exist:

**Sinusoidal positional encodings (original transformer)**  
For position \(pos\) and dimension index \(i\):

\[
PE_{(pos, 2i)} = \sin\!\left(\frac{pos}{10000^{2i/d}}\right), \quad
PE_{(pos, 2i+1)} = \cos\!\left(\frac{pos}{10000^{2i/d}}\right)
\]

Different dimensions oscillate at different frequencies, mimicking a positional numeral system in a continuous way. The dot product of two encodings depends only on their relative distance \(i-j\).

**Rotary Positional Encodings (RoPE)** – the modern choice  
Treat the embedding vector in pairs \((x_{2k}, x_{2k+1})\) as 2D vectors. Apply a rotation through an angle that grows linearly with position:

\[
\begin{pmatrix} x'_{2k} \\ x'_{2k+1} \end{pmatrix} =
\begin{pmatrix}
\cos(k\theta) & -\sin(k\theta) \\
\sin(k\theta) & \cos(k\theta)
\end{pmatrix}
\begin{pmatrix} x_{2k} \\ x_{2k+1} \end{pmatrix}
\]

Because rotations add (\(k\theta + l\theta = (k+l)\theta\)), the dot product between two RoPE‑encoded vectors depends only on the offset \(k-l\), giving a perfect distance‑preserving arithmetic.

> **Summary**  
> Transformers replace recurrence with **self‑attention**, achieving direct connections between all positions and enabling massive parallelisation. They scale far better than LSTMs – doubling the number of parameters reliably improves performance – which is why they underlie modern LLMs with trillions of parameters. Their main weakness is the **quadratic \(O(L^2)\) complexity** in sequence length, motivating an entire field of efficient attention variants.
