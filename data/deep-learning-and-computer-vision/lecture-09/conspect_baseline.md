# VAE and Diffusion Models

## Motivation: From Autoencoder to Generative Model *[00:02]*

An autoencoder maps an input $x$ (e.g., an image) through an **encoder** to a low‑dimensional latent code $z$, then through a **decoder** to a reconstruction $\hat{x}$. Training is straightforward: minimise a reconstruction loss between $x$ and $\hat{x}$, using only unlabelled data (each $x$ is its own target).  

Why can’t we simply use the decoder as a generative model?  
Even though the latent codes lie on a much simpler manifold than the original data space, they **do not cover the whole latent space**. A randomly sampled $z$ almost certainly falls outside the manifold of good latent codes, so the decoder produces a meaningless output.  

One solution is the **adversarial autoencoder** (regularise the latent space with a discriminator, like a GAN).  
The **variational autoencoder** (VAE) takes a different, ultimately more successful, approach.

## Variational Autoencoder: Distributions in Latent Space *[00:08]*

The core problem: every training point $x$ maps to a single $z$, causing dramatic overfitting of the latent manifold. Shift $z$ slightly and you fall off the manifold.  

**VAE key idea:** instead of a single point, the encoder outputs an entire **distribution** $p(z \mid x)$.  
For a given input, the encoder produces parameters of a Gaussian – a mean vector $\mu(x)$ and a diagonal covariance with vector $\sigma(x)$.  
Then we sample $z \sim \mathcal N\big(\mu(x), \operatorname{diag}(\sigma^2(x))\big)$ and feed it to the decoder; it must still reconstruct the original $x$.  

Intuition: cover the latent space with “wide enough” Gaussians that overlap, so any point sampled from a simple prior (e.g. $\mathcal N(0,I)$) lands in a region the decoder understands.

**The regularisation problem**  
If left unconstrained, the model will cheat:

- drive $\sigma \to 0$, collapsing to a standard autoencoder;  
- or push means far apart while fixing $\sigma$, effectively keeping points isolated.  

Therefore we must add a regulariser that keeps the encoder distributions close to a standard Gaussian $\mathcal N(0,I)$, preventing collapse and ensuring coverage.

Two questions arise:

1. How exactly should we choose the reconstruction loss and the regulariser?  
2. How can we backpropagate through a random sampling operation?

## Variational Approximation and the VAE Loss *[00:19]*

### Decomposition and the necessity of approximation

The model involves two variables: $x$ (data) and $z$ (latent). The joint distribution can be factorised in two ways:

$$
p(x,z) \;=\; p(z)\,p(x \mid z) \;=\; p(x)\,p(z \mid x).
$$

- $p(z \mid x)$ – the encoder distribution (complex, unknown);  
- $p(x \mid z)$ – the decoder distribution (we model as simple, e.g. Gaussian noise around $\hat{x}$);  
- $p(z)$ – the prior on latent codes (we fix to $\mathcal N(0,I)$);  
- $p(x)$ – the true data distribution (extremely complex, e.g. cat pictures).

If both $p(x \mid z)$ and $p(z \mid x)$ were simple (e.g. Gaussians), their product would be a Gaussian – but $p(x)$ is **not** a Gaussian. Hence they cannot both be simple.  
VAE chooses to keep the decoder simple (Gaussian noise) and to **approximate** the intractable true encoder $p(z \mid x)$ with a simple variational distribution $q(z) = \mathcal N(\mu(x), \operatorname{diag}(\sigma^2(x)))$.

### The variational lower bound (ELBO)

We want $q(z)$ close to $p(z \mid x)$, i.e. minimise $\mathrm{KL}(q \| p(z \mid x))$. But $p(z \mid x)$ is unknown.  
The following identity (holding for *any* $q$) lets us trade this intractable KL for a tractable objective.

$$
\begin{aligned}
\log p(x) &= \log p(x,z) - \log p(z \mid x) \\[2mm]
&= \mathbb E_{q(z)}\big[\log p(x,z)\big] - \mathbb E_{q(z)}\big[\log q(z)\big] \\
&\quad + \mathbb E_{q(z)}\big[\log q(z)\big] - \mathbb E_{q(z)}\big[\log p(z \mid x)\big] \\[2mm]
&= \underbrace{\int q(z)\log\frac{p(x,z)}{q(z)}\,dz}_{\mathcal L(q)} \;+\; \underbrace{\int q(z)\log\frac{q(z)}{p(z \mid x)}\,dz}_{\mathrm{KL}(q(z)\,\|\,p(z \mid x))}.
\end{aligned}
$$

Because $\log p(x)$ is constant with respect to $q$, **maximising $\mathcal L(q)$** is equivalent to **minimising $\mathrm{KL}(q\|p(z \mid x))$**.  
$\mathcal L(q)$ is called the **variational lower bound** (or evidence lower bound, ELBO).

Crucially, $\mathcal L(q)$ only requires the joint distribution $p(x,z)$ – which in the VAE factorises as $p(z)\,p(x \mid z)$, both Gaussians – and the approximating distribution $q$. It completely avoids $p(z \mid x)$.

### From ELBO to the VAE loss

Substitute $p(x,z) = p(z)\,p(x \mid z)$:

$$
\begin{aligned}
\mathcal L(q) &= \int q(z)\log\frac{p(z)\,p(x \mid z)}{q(z)}\,dz \\
&= \mathbb E_{q(z)}\big[\log p(x \mid z)\big] \;-\; \mathrm{KL}\big(q(z)\,\|\,p(z)\big).
\end{aligned}
$$

Now each term becomes explicit.

1. **Reconstruction term** – since $p(x \mid z) = \mathcal N\big(f_\theta(z), \sigma^2 I\big)$ with $f_\theta$ the decoder network:
   $$
   \mathbb E_{q(z)}\big[\log p(x \mid z)\big] \;=\; -\frac{1}{2c}\,\mathbb E_{q(z)}\big[\|x - f_\theta(z)\|^2\big] \;+\; \text{const}.
   $$
   In practice the expectation is approximated by averaging over a mini‑batch; this yields the classic least‑squares reconstruction loss.

2. **Regularisation term** – for $q(z) = \mathcal N(\mu,\Sigma)$ with diagonal $\Sigma$ and prior $p(z) = \mathcal N(0,I)$, the KL divergence has a closed form:
   $$
   \mathrm{KL}\big(q(z)\,\|\,p(z)\big) \;=\; \frac12 \sum_{j=1}^{d} \Big(\sigma^2_{x,j} + \mu^2_{x,j} - \log\sigma^2_{x,j} - 1\Big).
   $$
   This term penalises deviations from the standard Gaussian – exactly the regulariser we needed.

> **VAE loss (negative ELBO, to minimise):**
> $$
> \mathcal L_{\text{VAE}} = \frac{1}{2c}\,\mathbb E_{q(z)}\big[\|x - f_\theta(z)\|^2\big] \;+\; \frac12 \sum_{j=1}^{d} \big(\sigma^2_{x,j} + \mu^2_{x,j} - \log\sigma^2_{x,j} - 1\big).
> $$

Thus the variational approximation simultaneously **derives** both the reconstruction loss and the exact form of the regulariser, something that would otherwise be arbitrary.

## Reparametrization Trick *[00:54]*

Sampling $z \sim \mathcal N(\mu,\sigma^2)$ blocks gradient flow during backpropagation.  
The **reparametrization trick** circumvents this for Gaussians:

1. Sample auxiliary noise $u \sim \mathcal N(0,I)$, independent of $\mu,\sigma$.
2. Compute $z = \mu + \sigma \odot u$ (element‑wise product).

Now the randomness is “externalised” – $\mu$ and $\sigma$ are differentiable transformations of $u$, so gradients pass through normally. This trick is simple but essential for training VAEs end‑to‑end.

## Diffusion Models *[1:08]*

### Basic idea – forward and reverse diffusion

The core concept comes from non‑equilibrium statistical physics, but reduces to a Markov chain insight:

- **Forward process (noising):** start with a clean image $x_0$ and repeatedly add small amounts of Gaussian noise:
  $$
  q(x_t \mid x_{t-1}) = \mathcal N\big(x_t \mid \sqrt{1-\beta_t}\,x_{t-1},\; \beta_t I\big),
  $$
  with $0 < \beta_t \ll 1$. After $T$ steps (typically hundreds), the image becomes indistinguishable from pure noise $\mathcal N(0,I)$.

- **Reverse process (denoising):** learn a Markov chain that gradually removes noise:
  $$
  p_\theta(x_{t-1} \mid x_t) = \mathcal N\big(x_{t-1} \mid \mu_\theta(x_t,t),\; \Sigma_\theta(x_t,t)\big).
  $$
  Then a generative model is obtained by sampling $x_T \sim \mathcal N(0,I)$ and running the reverse chain.

### Closed‑form forward sampling and conditional reversal

Let $\alpha_t = 1-\beta_t$ and $\bar A_t = \prod_{i=1}^t \alpha_i$.  
By iterating the forward step we obtain a direct closed‑form expression for $x_t$ given $x_0$:

$$
q(x_t \mid x_0) = \mathcal N\big(x_t \mid \sqrt{\bar A_t}\,x_0,\; (1-\bar A_t)I\big),
\quad\text{i.e.}\quad x_t = \sqrt{\bar A_t}\,x_0 + \sqrt{1-\bar A_t}\,\epsilon,\;\; \epsilon\sim\mathcal N(0,I).
$$

If we knew both $x_t$ and $x_0$, the reverse step is analytically solvable:

$$
q(x_{t-1} \mid x_t, x_0) = \mathcal N\big(x_{t-1} \mid \tilde\mu(x_t,x_0),\; \tilde\beta_t I\big),
$$

with known formulas for $\tilde\mu$ and $\tilde\beta_t$. In particular, $\tilde\mu$ can be expressed in terms of the noise $\epsilon_t$ that would take $x_0$ to $x_t$, showing that predicting the added noise is the key task.

### Variational bound for diffusion

The training objective is again a variational lower bound (ELBO), now applied to the whole trajectory of $T$ steps. Minimising this bound yields a loss that decomposes into per‑step KL divergences between the true reverse conditional $q(x_{t-1}\mid x_t,x_0)$ (tractable) and the model $p_\theta(x_{t-1}\mid x_t)$.  
In practice the model is often parametrised to predict the noise $\epsilon_\theta(x_t,t)$, leading to a simple mean‑squared error:

$$
L_t = \mathbb E_{x_0,\epsilon}\Big[\big\|\epsilon - \epsilon_\theta(\sqrt{\bar A_t}\,x_0 + \sqrt{1-\bar A_t}\,\epsilon,\;t)\big\|^2\Big].
$$

### DDPM – Denoising Diffusion Probabilistic Models *[1:17]*

Ho et al. (2020) introduced practical improvements that made diffusion competitive with GANs:

- Fixed, pre‑defined $\beta_t$ schedule (no training of the forward process).
- Fixed variance $\Sigma_\theta$ for the reverse steps; only the mean (i.e., the noise prediction) is learned.
- A special discrete likelihood model at the final step $p_\theta(x_0\mid x_1)$ that handles the discretised image intensities (e.g., $[-1,1]$ scaled from $\{0,\dots,255\}$).

The result: excellent image quality, but **extremely slow** – generating one image required hundreds of sequential neural‑network passes.

### DDIM – Denoising Diffusion Implicit Models *[1:19]*

(Song et al., 2020)  
Observation: the ELBO depends only on the marginal distributions $q(x_t \mid x_0)$, not on the full joint $q(x_{1:T}\mid x_0)$. Hence we can choose a different forward process that shares the same marginals, opening the door to **non‑Markovian** and **implicit** formulations.

Key idea: instead of approximating the direction to the previous step $x_{t-1}$, at every step the model **directly predicts the direction to the original $x_0$**.  
This decoupling means we can take larger “jumps” – skip intermediate steps – accelerating generation by **10×–100×** with no quality loss.

Additional properties:

- The reverse process can be made **deterministic** (zero variance), making the model a true implicit model where each noise $x_T$ maps to exactly one image.  
- DDIMs provide a smoothly structured latent space, enabling **interpolations** that were impossible with standard DDPMs.

### Latent Diffusion Models (Stable Diffusion) *[1:23]*

A further breakthrough: run the diffusion process in the **latent space** of a pretrained autoencoder rather than on raw pixels.  

- A modern VAE (often a VQ‑VAE with adversarial patch‑based losses) compresses images into a compact latent representation.  
- A diffusion model then operates on these latent codes, making training and sampling far more efficient.

**Stable Diffusion** (Rombach, Blattmann et al., 2022) popularised this architecture. Crucially, **conditioning** (e.g., text prompts) is injected at every denoising step, typically via cross‑attention with a transformer‑encoded text vector. The reversed latent code is finally decoded back to an image by the VAE decoder.

### DALL‑E 2 and Midjourney

- **DALL‑E 2** (unCLIP) uses a CLIP joint text–image embedding space: a prior model generates a CLIP image embedding from text, and a diffusion decoder turns that embedding into an image. Diffusion again happens in a semantic latent space.  
- **Midjourney** (proprietary) is believed to follow a similar latent‑diffusion design.

### Diffusion Transformers (DiT) *[1:28]*

Peebles & Xie (2022) replaced the U‑Net backbone of latent diffusion with a **transformer**.  
The input latent feature map is “patchified” into a sequence, processed by transformer blocks, and conditioned on time and (optionally) class/text via adaptive layer normalisation.  
DiTs show strong correlation between compute (GFLOPs) and generation quality, scaling more efficiently than earlier architectures.

### Flux and Beyond

**Flux** (successor to Stable Diffusion, by the same team) further refined the architecture and produced state‑of‑the‑art local text‑to‑image generation at its time.  
Since then, the frontier has moved to closed, large‑scale models (GPT‑image, Gemini), but the underlying principles remain latent diffusion with transformer backbones.

### Speeding up sampling: ODE solvers and flow matching

- **DPM‑Solver++** frames DDIM as a first‑order ODE solver and replaces it with higher‑order multi‑step schemes, reducing the required sampling steps even further with greater stability.  
- **UniPC** introduces a predictor–corrector framework that universally increases the accuracy order without extra model evaluations.  
- **Flow matching** generalises diffusion and has become the foundation of many modern generative models.

## A Taxonomy of Deep Generative Models *[1:32]*

| Category | Examples | Core idea |
|---|---|---|
| **Implicit density** | GANs | Compete generator vs. discriminator; no explicit likelihood. |
| **Explicit – autoregressive** | WaveNet, LLMs | Factorise $p(x)=\prod_t p(x_t\mid x_{<t})$ and generate sequentially. |
| **Explicit – flow‑based** | RealNVP, Glow | Invertible transforms from a simple base density. |
| **Explicit – approximate density (variational)** | VAE, diffusion models | Optimise a bound (ELBO) by approximating an intractable posterior. |

VAEs and diffusion models belong to the approximate density branch. They do not assume the true reverse/encoder distribution is simple; instead they **approximate** it and make assumptions only on the approximating distribution, with the variational lower bound providing a principled objective.  

This variational principle, first encountered in the simplest form in VAEs, recurs in ever more elaborate forms throughout generative modelling – it is one of the truly fundamental ideas in machine learning.
