# Generative Adversarial Networks

## Taxonomy of Deep Generative Models *[01:18]*

Generative models produce objects of high dimensionality and complex structure — images, text, music, video. In deep learning, the first major divide lies between **explicit density models** and **implicit density models**.

### Explicit Density Models
An explicit density model provides a formula for $p(x)$, the probability density of the data. Even though the true distribution of, say, cat photos in a multi-million-dimensional pixel space is impossibly complicated, we can build an explicit approximation.

- **Tractable density** — you can literally write down $p(x)$ as a closed‑form product of conditional distributions.  
  The classic example is an **autoregressive model**, which decomposes  
  $$p(x_1, x_2, \dots, x_n) = p(x_1) \, p(x_2 \mid x_1) \, p(x_3 \mid x_1, x_2) \cdots p(x_n \mid x_1, \dots, x_{n-1}).$$  
  This identity is always true, but to make it useful we introduce simplifying assumptions: a Markov chain, an RNN with a hidden state, or a Transformer that conditions each next token on the preceding context. All large language models (LLMs) live in this class — they generate text one token at a time. Pixel‑wise autoregressive models for images (e.g., PixelCNN) exist, but generating a million pixels a million times is prohibitively slow.

- **Approximate density** — instead of forcing $p(x)$ itself to be tractable, we approximate it with a simpler distribution $q(x)$ that is easy to handle.  
  The most important family here are **Variational Autoencoders (VAEs)**, which use variational inference to build a learnable lower bound on the log‑likelihood. VAEs are a cornerstone of generative modelling; even diffusion models typically operate in the latent space of a VAE.

- **Flow‑based models** — an alternative approach that composes many simple, invertible transformations $f_k \circ \dots \circ f_1(z)$ so that the density $p(x)$ can be computed by the change‑of‑variables formula. These also belong to explicit density models but are not covered today.

### Implicit Density Models
An implicit density model never gives you a formula for $p(x)$. It is just a sampler: you feed in random noise and get out a sample $\hat{x}$ that should look like it came from the data distribution. There is no way to read off a density from the trained network — you can only draw from it. The main (and almost only) example of this class is **Generative Adversarial Networks (GANs)**.

## Generative Adversarial Networks: Core Idea *[14:45]*

### The Generator’s Loss Function Problem
A generator $G$ maps a random noise vector $z \sim p_z(z)$ (e.g., standard Gaussian) to an output $\hat{x}$ that should resemble a real image. We have a dataset of real images, but there is no paired supervision — no “this $z$ should produce that particular $x$”. Hence, there is no obvious loss function that tells us how good a generated image is. This is the central challenge: how do you score the output?

The GAN solution: **learn the loss function itself**. Introduce a second network, the **discriminator** $D$, whose job is binary classification — did this image come from the real data distribution $p_{\text{data}}$ (output $1$) or from the generator $p_g$ (output $0$)? The generator and discriminator have opposing objectives: $D$ wants to tell real from fake; $G$ wants to fool $D$. This is **adversarial training**.

### Formal Minimax Game
Let $G(z; \theta_g): Z \to X$ and $D(x; \theta_d): X \to [0,1]$. The discriminator maximises the log‑likelihood of correct classification:

$$L_D = \mathbb{E}_{x \sim p_{\text{data}}(x)}[\log D(x)] + \mathbb{E}_{x \sim p_g(x)}[\log(1 - D(x))].$$

The generator wants to minimise the same quantity — it tries to push $D(G(z))$ towards $1$ (i.e., fool the discriminator). Combined, we have the **minimax game**

$$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))].$$

This is not ordinary optimisation; it is a zero‑sum game where two players are competing. In principle, finding an equilibrium in such a game is much harder than a simple minimisation. However, the structure of the problem makes it feasible.

### Theoretical Optimum
For a fixed generator, the optimal discriminator is the Bayesian posterior:

$$D^*_G(x) = \frac{p_{\text{data}}(x)}{p_{\text{data}}(x) + p_g(x)}.$$

Plugging $D^*_G$ into the value function yields the **Jensen–Shannon divergence** between $p_{\text{data}}$ and $p_g$:

$$\mathrm{JSD}(p_{\text{data}} \| p_g) = \frac{1}{2} \mathrm{KL}\!\left(p_{\text{data}} \;\middle\|\; \frac{p_{\text{data}}+p_g}{2}\right) + \frac{1}{2} \mathrm{KL}\!\left(p_g \;\middle\|\; \frac{p_{\text{data}}+p_g}{2}\right).$$

Thus, at the global minimum of the game we recover $p_g = p_{\text{data}}$.

### The Saturation Problem
Unfortunately, the theoretical loss $\mathbb{E}_z[\log(1 - D(G(z)))]$ is very poor for training the generator in practice. The problem is the sigmoid‑saturated cross‑entropy: when the discriminator becomes good at separating real from fake, it gives confident predictions ($D(G(z)) \approx 0$). The gradient of $\log(1-D)$ saturates, nearly vanishes, and backpropagation through $D$ provides almost no signal to $G$ — exactly when the generator needs to improve the most.

The practical fix is to use a **non‑saturating loss** for the generator:

$$\text{minimise } -\mathbb{E}_{z \sim p_z(z)}[\log D(G(z))],$$

i.e., maximise the probability that the discriminator makes a mistake, rather than minimising the probability of its correct answer. This keeps the gradient alive when the discriminator is strong.

### Training Procedure *[26:49 – 38:27]*
Training proceeds in alternation, much like an EM algorithm:
1. Fix $G$, update $D$ by improving the binary cross‑entropy on mini‑batches of real data and generated data.
2. Fix $D$, update $G$ using the non‑saturating loss.

In practice, the discriminator is often updated more frequently, or we carefully balance the two to avoid one overpowering the other too quickly.

## DCGAN and Latent Space Exploration *[39:45]*

The original GAN (2014) produced reasonable digits on MNIST but struggled with diverse, natural images. A major advance came with **Deep Convolutional GANs (DCGANs)**, which replaced fully‑connected layers with convolutional/deconvolutional architectures, used strided convolutions instead of pooling, added batch normalisation everywhere, and trained with the Adam optimiser.

After only a few epochs on a dataset like LSUN bedrooms, DCGAN could produce recognisable, though still tiny, images (64 × 64 or 128 × 128). These results were state‑of‑the‑art a decade ago and already hinted at the latent space structure.

### The Latent Walk: A Visual Sanity Check
How can you tell if a generator has learned a meaningful mapping, not just memorised a few training examples? The discriminator cannot answer this — its inability to distinguish merely says it is not powerful enough or not well trained. A widely used visual test is a **linear walk in the latent space**.

Think of the generator as a map from a simple latent distribution $Z$ (e.g., a standard Gaussian) to a point $X$ on the immensely complicated manifold of real images. To generate new images we need to be able to sample a random $z$ and land reliably on that manifold. If we take two latent vectors $z_1$, $z_2$ that both produce plausible images, and we interpolate linearly between them, *every* intermediate point should also produce a plausible image. If, instead, the images blur or morph unrealistically (as would happen if interpolation took place directly in pixel space), the manifold is not well flattened. Good DCGANs show smooth, realistic transitions during such walks, confirming that the latent space is well‑behaved and that sampling from the prior will yield reasonable outputs.

### Failure Modes
Early GANs, including DCGAN, exhibited characteristic failures that stem from the local receptive fields of convolution. The generator builds an image part by part with limited global context:
- **Counting problems** (e.g., three‑headed dogs, multiple eyes) — the model does not know how many of a repeated feature to produce because it only sees a small neighbourhood.
- **Perspective inconsistencies** — different halves of an object may be rendered from different viewpoints because the generator has no global 3D understanding.

These mistakes are easy for humans to spot, but they reflect how genuinely difficult it is to enforce global coherence with purely local operations.

## Progressive Growing GANs (ProGAN) *[54:56]*

A crucial technical idea for scaling up resolution is to not generate the whole image at once. **Progressive Growing GAN (ProGAN)** trains a GAN in stages, starting from $4 \times 4$ pixels and progressively adding layers that quadruple the resolution up to $1024 \times 1024$. At each stage, new convolutional layers are added smoothly to both the generator and the discriminator. This way, the model first learns large‑scale structure, then refines it, and training time is saved because the early stages see many more lower‑resolution images. After about two weeks of training on powerful hardware, ProGAN produced the first high‑resolution, photo‑realistic human faces — known from the website “ThisPersonDoesNotExist”.

At the time, ProGAN already incorporated improved loss functions. One of them was the **Least Squares GAN (LSGAN)**, which replaces the sigmoid cross‑entropy with a squared‑deviation target:

$$\min_D \frac{1}{2}\,\mathbb{E}_{p_{\text{data}}}\bigl[(D(x)-b)^2\bigr] + \frac{1}{2}\,\mathbb{E}_{p_z}\bigl[(D(G(z))-a)^2\bigr],$$

$$\min_G \frac{1}{2}\,\mathbb{E}_{p_z}\bigl[(D(G(z))-c)^2\bigr],$$

with typical choices $a=0$, $b=c=1$. Because the loss penalises overshooting, nothing explodes to infinity, and gradients remain useful.

## Wasserstein GAN (WGAN) *[1:00:28]*

### The Manifold Mismatch Problem
The deeper reason why standard divergences cause trouble in generative modelling is that $p_{\text{data}}$ and $p_g$ are concentrated on low‑dimensional manifolds inside the high‑dimensional pixel space. The support of a realistic cat photo set is a tiny, intricate surface in $\mathbb{R}^{3\mathrm{M}}$. The generator, by construction, maps a low‑dimensional noise vector to an image, so its distribution $p_g$ also lies on some low‑dimensional manifold. In the beginning, these two manifolds almost surely do **not** intersect; their overlap has measure zero.

Now consider the Kullback–Leibler divergence $\mathrm{KL}(p_{\text{data}} \| p_g) = \int p_{\text{data}}(x) \log \frac{p_{\text{data}}(x)}{p_g(x)}\,dx$. Where $p_{\text{data}}(x) > 0$, we typically have $p_g(x) = 0$, making the logarithm infinite. The divergence is undefined (or infinite) and yields no useful gradient to move $p_g$ towards $p_{\text{data}}$. Classical machine learning avoids this by adding Gaussian noise to the model, smoothing its support everywhere. But in implicit generative models we cannot remove that noise during generation — adding noise blurs the images and defeats the purpose.

### Earth Mover (Wasserstein‑1) Distance
The **Earth Mover distance** (Wasserstein‑1) provides a solution. Intuitively, think of the two probability distributions as piles of earth of total volume 1. The Wasserstein distance is the *minimum amount of work* needed to turn one pile into the other — work $\approx$ mass $\times$ distance moved. Formally,

$$W(p_{\text{data}}, p_g) = \inf_{\gamma \in \Pi(p_{\text{data}}, p_g)} \mathbb{E}_{(x,y) \sim \gamma}\bigl[\|x - y\|\bigr],$$

where $\Pi$ is the set of joint distributions whose marginals are $p_{\text{data}}$ and $p_g$.

Crucially, this distance remains continuous and provides meaningful gradients even when the supports are disjoint. Moving a distribution a little bit closer always reduces the Earth Mover distance, whereas the KL divergence would still be infinite.

### Kantorovich–Rubinstein Duality and the Critic
Computing the infimum over joint distributions seems intractable, but the Kantorovich–Rubinstein duality transforms it into a supremum over 1‑Lipschitz functions:

$$W(p_{\text{data}}, p_g) = \sup_{\|f\|_L \le 1} \Bigl( \mathbb{E}_{x \sim p_{\text{data}}}[f(x)] - \mathbb{E}_{x \sim p_g}[f(x)] \Bigr).$$

We can parametrise $f$ with a neural network $f_w$ (called the **critic** instead of a discriminator, because it no longer does binary classification) and enforce the Lipschitz constraint, originally by weight clipping to a small range. The training procedure is:
1. For a fixed generator, train the critic to maximise the difference of expectations — this approximates $W(p_{\text{data}}, p_g)$.
2. For a fixed critic, compute the gradient of the generator as $-\mathbb{E}_{z}[\nabla_\theta f_w(G_\theta(z))]$ and update $G$.

The WGAN loss correlates much better with image quality and allows the critic to be trained to convergence, unlike the discriminator in a standard GAN.

### Improved WGAN (WGAN‑GP)
Weight clipping can cause the critic to learn over‑simplified functions and may lead to exploding or vanishing gradients. An **Improved WGAN** replaces the hard clipping with a soft gradient penalty:

$$\lambda \; \mathbb{E}_{\hat{x} \sim P_{\hat{x}}}\bigl[(\|\nabla_{\hat{x}} D(\hat{x})\|_2 - 1)^2\bigr],$$

where $\hat{x}$ is sampled uniformly along straight lines between real and generated samples. This encourages the critic’s gradient norm to stay close to 1 everywhere, enforcing the Lipschitz condition in a much gentler way and yielding more stable training.

## SAGAN, BigGAN and Image Quality *[1:31:23]*

Further improvements addressed the locality of convolutions and scaled up the models:
- **Self‑Attention GAN (SAGAN)** adds a Transformer‑like self‑attention mechanism over image features, letting the generator capture long‑range dependencies. The attention maps show that the network indeed looks far across the image when synthesising fine details.
- **BigGAN** combined self‑attention with very large architectures and careful regularisation, improving the Inception score threefold and producing high‑fidelity interpolations (e.g., smoothly morphing a bird into a dog with plausible intermediate hybrids).

Evaluating image quality itself is non‑trivial. The **Inception score** is a commonly used metric: take a generated image $x$, run a pre‑trained Inception classifier to get $p(y \mid x)$, and compute
$$\mathrm{IS} = \exp\!\Bigl( \mathbb{E}_x \,\mathrm{KL}\bigl(p(y \mid x) \,\|\, p(y)\bigr) \Bigr), \quad p(y) = \int p(y \mid G(z))\, dz.$$
This rewards images that are confidently classified as a particular class (low entropy in $p(y \mid x)$) while the generated set as a whole is diverse across classes (high entropy in $p(y)$).

## Adversarial Autoencoders (AAE) *[1:32:11]*

A natural way to obtain a loss function for generation is to train an **autoencoder**: an encoder maps an image $x$ to a latent code $z$, a decoder maps $z$ back to a reconstruction $\hat{x}$, and we minimise $\|x - \hat{x}\|^2$. After training, the decoder alone looks like a generator — feed it a latent code $z$, get an image. The problem is that the aggregated posterior distribution of latent codes produced by the encoder on real data is complicated and not easy to sample from. Simply drawing $z$ from a standard Gaussian and feeding it to the decoder will almost certainly miss the correct manifold, producing garbage.

An **Adversarial Autoencoder** solves this by adding a discriminator *in the latent space*. The discriminator learns to distinguish between latent codes produced by the encoder (from real data) and samples drawn from a simple prior (e.g., a standard Gaussian). The encoder is simultaneously trained to fool this discriminator, so its output distribution is pushed to match the prior. Once trained, sampling a $z$ from the Gaussian and passing it through the decoder yields plausible images. AAEs can be extended to conditional generation (by providing a label to the encoder and decoder) and to semi‑supervised learning. While VAEs offer a cleaner probabilistic regularisation, AAEs are a direct, adversarial alternative that still sees use.

### Other GAN Architectures
- **Conditional GANs** — $G$ receives both a noise vector and a conditioning input (e.g., a class label, a low‑resolution image, or an age descriptor). This enables tasks like face ageing and super‑resolution (e.g., ESRGAN).
- **Stacked GANs (SGAN)** — a chain of GANs where later stages condition on the output of earlier ones, progressively refining the representation through a hierarchy.

## Conclusion *[1:41:14]*

GANs were the state‑of‑the‑art for unconditional image generation until around 2020. They remain strong in specific niches — super‑resolution, style transfer, and any domain where an explicit density is not needed. For text‑to‑image generation and large‑scale prompted image synthesis, diffusion models have taken over, but the principle of adversarial training is still embedded in many modern pipelines. The next lecture will introduce diffusion models and show how they connect to the ideas discussed today.
