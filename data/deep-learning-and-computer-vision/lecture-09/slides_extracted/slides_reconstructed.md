# VAE and Diffusion Models

## Variational Autoencoders

### Idea and Motivation

The main task is to turn an autoencoder into a generative model.

A straightforward autoencoder maps each input point \(x\) to a single latent code \(z\); sampling new points in that latent space is difficult because the code space is not densely populated (even in low dimensions it is hard to find a “good” point).

The core idea of the **variational autoencoder** (Kingma et al., 2013) is to let every input \(x\) map not to a single latent code but to an entire distribution \(q(z|x)\).  
Intuitively, the decoder must be stable to small changes in \(z\); this can be seen as an improved version of a denoising autoencoder. We want to cover the latent space with “wide enough” distributions.

However, if we simply train an autoencoder, it will prefer to decode from extremely narrow distributions, eventually collapsing to a zero‑variance distribution – back to a regular autoencoder that does not help for generation.  
Therefore we must add a constraint (regularizer) on \(q(z|x)\) to enforce that it stays close to a simple prior (e.g., a standard Gaussian).

Two questions remain:

1. How do we choose the loss function and the regularizer?
2. How can we backpropagate gradients through the sampling process?

### Variational Approximations in the VAE

We want to train an encoder that maps images \(x\) to latent codes \(z\) (i.e., \(q(z|x)\)) and a decoder that reconstructs images from \(z\) (\(p(x|z)\)).  
The joint distribution \(p(x,z)\) factorises in two ways:

\[
p(z)\,p(x|z) = p(x,z) = p(x)\,p(z|x)
\]

Here:

- \(p(x)\) is the (complex, unknown) distribution of images,
- \(p(z)\) is a simple prior we can sample from, e.g. \(\mathcal{N}(0,I)\);
- \(p(z|x)\) is the encoder distribution,
- \(p(x|z)\) is the decoder distribution.

To obtain a generative model we must learn both \(p(x|z)\) and \(p(z|x)\).  
Because \(p(x)\) is very complex, we must pick one of the two distributions to be simple and the other to be complex.  
The VAE chooses the first option: assume that \(p(z|x)\) is simple and let \(p(x|z)\) be complex. More precisely, we assume

\[
p(x|z) = \mathcal{N}(x \mid f(z), cI) ,
\]

where \(f(z) = \text{Decoder}(z)\).  
The prior is \(p(z) = \mathcal{N}(z \mid 0, I)\).

We will look for a variational approximation \(q(z) \approx p(z|x)\); that is, we parametrise the encoder with a distribution \(q(z)\) (also Gaussian) and maximise a lower bound on the log‑likelihood.

#### Derivation of the variational lower bound

Start from the joint:

\[
p(x,z) = p(x)\,p(z|x) \quad\Rightarrow\quad \log p(x) = \log p(x,z) - \log p(z|x).
\]

Take the expectation over \(q(z)\):

\[
\mathbb{E}_{q(z)}[\log p(x)] = \mathbb{E}_{q(z)}[\log p(x,z)] - \mathbb{E}_{q(z)}[\log p(z|x)] .
\]

Standard manipulations yield:

\[
\begin{aligned}
\log p(x) &= \mathbb{E}_{q(z)}[\log p(x,z)] - \mathbb{E}_{q(z)}[\log q(z)] \\
&\quad + \mathbb{E}_{q(z)}[\log q(z)] - \mathbb{E}_{q(z)}[\log p(z|x)] \\[4pt]
&= \int q(z) \log \frac{p(x,z)}{q(z)}\,dz + \int q(z) \log \frac{q(z)}{p(z|x)}\,dz .
\end{aligned}
\]

Thus

\[
\log p(x) = \mathcal{L}(q) + \operatorname{KL}\bigl(q(z)\,\|\,p(z|x)\bigr),
\]

where the **evidence lower bound (ELBO)** is

\[
\mathcal{L}(q) = \int q(z) \log \frac{p(x,z)}{q(z)}\,dz .
\]

Hence, maximising \(\mathcal{L}(q)\) w.r.t. \(q\) minimises the KL divergence, making \(q(z)\) a good approximation to \(p(z|x)\). For the VAE the ELBO becomes:

\[
\begin{aligned}
\mathcal{L}(q) &= \int q(z) \log \frac{p(z)p(x|z)}{q(z)}\,dz \\[4pt]
&= \int q(z) \log p(x|z)\,dz + \int q(z) \log \frac{p(z)}{q(z)}\,dz \\[4pt]
&= \int q(z) \log \mathcal{N}(x \mid f(z), cI)\,dz - \operatorname{KL}\bigl(q(z)\,\|\,p(z)\bigr) \\[4pt]
&= -\frac{1}{2c}\,\mathbb{E}_{q(z)}\!\left[\|x - f(z)\|^2\right] - \operatorname{KL}\bigl(q(z)\,\|\,p(z)\bigr) .
\end{aligned}
\]

The first term is the reconstruction loss, the second term is the regulariser that pushes \(q(z)\) towards the prior \(p(z) = \mathcal{N}(0,I)\).

For a Gaussian encoder \(q(z|x) = \mathcal{N}\!\bigl(z \mid \mu_{x}, \operatorname{diag}(\sigma^2_{x})\bigr)\), the KL divergence between two Gaussians has a closed form:

\[
\operatorname{KL}\bigl(q(z)\,\|\,p(z)\bigr) = \frac{1}{2} \sum_{j=1}^{d} \bigl(\sigma^2_{x,j} + \mu^2_{x,j} - \log\sigma^2_{x,j} - 1\bigr) .
\]

Consequently, the final VAE loss function is

\[
\mathcal{L}(q) = -\frac{1}{2c}\,\mathbb{E}_{q(z)}\!\left[\|x - f(z)\|^2\right] - \frac{1}{2} \sum_{j=1}^{d} \bigl(\sigma^2_{x,j} + \mu^2_{x,j} - \log\sigma^2_{x,j} - 1\bigr) .
\]

### Reparametrization Trick

To train the model we must backpropagate gradients through the sampling of \(z\); direct sampling is not differentiable.  
**Reparametrization trick**: first sample an auxiliary noise variable \(u \sim \mathcal{N}(0,I)\), then transform it:

\[
z = \mu_x + \sigma_x \odot u .
\]

Now the randomness goes through \(u\), and the parameters \(\mu_x, \sigma_x\) receive gradients. During training, for each mini‑batch of images \(x\) we sample a matching mini‑batch of \(u\) and use them together.

---

## Diffusion Models

### Introduction

(Sohl‑Dickstein et al., 2015) proposed an idea from non‑equilibrium thermodynamics: train a Markov chain that gradually turns random noise into the desired data distribution.  
To do this, we first define a **forward** chain that progressively destroys the data by adding noise. Then we learn to **reverse** each step; if successful, we can start from pure noise and generate samples by moving backwards along the chain.

### Forward Diffusion Process

Let the data be \(x_0 \sim p(x_0)\). Forward diffusion adds Gaussian noise at each step \(t\):

\[
q(x_t \mid x_{t-1}) = \mathcal{N}\!\bigl(x_t \mid \sqrt{1-\beta_t}\,x_{t-1},\; \beta_t I\bigr),
\]

where \(\beta_t\) is a noise schedule. Over \(T\) steps,

\[
q(x_{1:T} \mid x_0) = \prod_{t=1}^{T} q(x_t \mid x_{t-1}) .
\]

Thanks to the reparametrization trick, we can sample \(x_t\) directly in closed form. Define \(\alpha_t = 1 - \beta_t\) and \(A_t = \prod_{i=1}^{t} \alpha_i\). Then, with \(\epsilon \sim \mathcal{N}(0,I)\),

\[
x_t = \sqrt{\alpha_t}\,x_{t-1} + \sqrt{1-\alpha_t}\,\epsilon
     = \sqrt{\alpha_t\alpha_{t-1}}\,x_{t-2} + \sqrt{1-\alpha_t\alpha_{t-1}}\,\epsilon
     = \dots = \sqrt{A_t}\,x_0 + \sqrt{1-A_t}\,\epsilon .
\]

Thus

\[
q(x_t \mid x_0) = \mathcal{N}\!\bigl(x_t \mid \sqrt{A_t}\,x_0,\; (1-A_t)I\bigr).
\]

### Reverse Diffusion and Variational Lower Bound

If \(\beta_t\) is small, the reverse distributions \(q(x_{t-1} \mid x_t)\) are also Gaussian, but their parameters depend on the whole data distribution.  
We define the reverse process with learnt parameters \(\theta\):

\[
p_\theta(x_{0:T}) = p_\theta(x_T) \prod_{t=1}^{T} p_\theta(x_{t-1} \mid x_t),
\]
\[
p_\theta(x_{t-1} \mid x_t) = \mathcal{N}\!\bigl(x_{t-1} \mid \mu_\theta(x_t,t),\; \Sigma_\theta(x_t,t)\bigr).
\]

If we knew \(x_0\), the reverse step could be computed analytically. Conditioning on \(x_0\),

\[
q(x_{t-1} \mid x_t, x_0) = \frac{q(x_t \mid x_{t-1}, x_0)\,q(x_{t-1} \mid x_0)}{q(x_t \mid x_0)} .
\]

Completing the square in \(x_{t-1}\) gives

\[
q(x_{t-1} \mid x_t, x_0) = \mathcal{N}\!\bigl(x_{t-1} \mid \tilde{\mu}(x_t,x_0),\; \tilde{\beta}_t I\bigr),
\]

with

\[
\tilde{\beta}_t = \frac{1-A_{t-1}}{1-A_t}\,\beta_t,
\qquad
\tilde{\mu}(x_t,x_0) = \frac{\sqrt{\alpha_t}(1-A_{t-1})}{1-A_t}\,x_t + \frac{\sqrt{A_{t-1}}\beta_t}{1-A_t}\,x_0 .
\]

Using \(x_t = \sqrt{A_t}\,x_0 + \sqrt{1-A_t}\,\epsilon_t\), we can rewrite

\[
\tilde{\mu}(x_t,x_0) = \frac{1}{\sqrt{\alpha_t}}\Bigl(x_t - \frac{1-\alpha_t}{\sqrt{1-A_t}}\,\epsilon_t\Bigr).
\]

The goal of training is to approximate the true reverse step without conditioning on the unknown \(x_0\); we do so by minimising a variational bound analogous to that of the VAE.

Starting again from first principles,

\[
\log p_\theta(x_0) = \log p_\theta(x_{0:T}) - \log p_\theta(x_{1:T} \mid x_0) .
\]

Taking the expectation over the forward process \(q(x_{0:T})\),

\[
\begin{aligned}
\mathbb{E}_{q(x_0)}[\log p_\theta(x_0)]
&= \mathbb{E}_{q(x_{0:T})}[\log p_\theta(x_{0:T})]
   - \mathbb{E}_{q(x_{0:T})}[\log p_\theta(x_{1:T} \mid x_0)] \\
&= \mathbb{E}_{q(x_{0:T})}\!\left[\log\frac{p_\theta(x_{0:T})}{q(x_{1:T} \mid x_0)}\right]
   + \mathbb{E}_{q(x_{0:T})}\!\left[\log\frac{q(x_{1:T} \mid x_0)}{p_\theta(x_{1:T} \mid x_0)}\right].
\end{aligned}
\]

The second term is a KL divergence (non‑negative), so we obtain the variational lower bound or, up to a sign, the loss function:

\[
L = \mathbb{E}_{q(x_{0:T})}\!\left[\log\frac{q(x_{1:T} \mid x_0)}{p_\theta(x_{0:T})}\right]
\geq -\mathbb{E}_{q(x_0)}[\log p_\theta(x_0)] .
\]

Expanding the ratio breaks the loss into a sum of step‑wise terms:

\[
\begin{aligned}
L &= \mathbb{E}_q\!\left[-\log p_\theta(x_T) + \sum_{t=1}^T \log\frac{q(x_t \mid x_{t-1})}{p_\theta(x_{t-1} \mid x_t)}\right] \\
  &= \mathbb{E}_q\!\left[-\log p_\theta(x_T) + \sum_{t=2}^T \log\frac{q(x_t \mid x_{t-1})}{p_\theta(x_{t-1} \mid x_t)} + \log\frac{q(x_1 \mid x_0)}{p_\theta(x_0 \mid x_1)}\right] \\
  &\;\vdots \\
  &= \mathbb{E}_q\!\left[\log\frac{q(x_T \mid x_0)}{p_\theta(x_T)} + \sum_{t=2}^T \log\frac{q(x_t \mid x_{t-1}, x_0)}{p_\theta(x_{t-1} \mid x_t)} - \log p_\theta(x_0 \mid x_1)\right].
\end{aligned}
\]

Thus

\[
L = L_T + L_{T-1} + \dots + L_0,
\]

where

\[
\begin{aligned}
L_T &= \operatorname{KL}\!\bigl(q(x_T \mid x_0)\,\|\,p_\theta(x_T)\bigr), \\[2pt]
L_t &= \operatorname{KL}\!\bigl(q(x_t \mid x_{t+1},x_0)\,\|\,p_\theta(x_t \mid x_{t+1})\bigr), \quad t=1,\dots,T-1, \\[2pt]
L_0 &= -\log p_\theta(x_0 \mid x_1).
\end{aligned}
\]

All these terms are KL divergences between Gaussians, so they can be computed analytically. For the intermediate steps we use the parametrisation

\[
p_\theta(x_{t-1} \mid x_t) = \mathcal{N}\!\bigl(x_{t-1} \mid \mu_\theta(x_t,t),\; \Sigma_\theta(x_t,t)\bigr)
\]

and try to match the reverse conditional mean:

\[
\mu_\theta(x_t,t) \approx \tilde{\mu}(x_t,x_0) = \frac{1}{\sqrt{\alpha_t}}\Bigl(x_t - \frac{1-\alpha_t}{\sqrt{1-A_t}}\,\epsilon_t\Bigr).
\]

Since \(x_t\) is known during training, we can parametrise the noise directly:

\[
p_\theta(x_{t-1} \mid x_t) = \mathcal{N}\!\left(x_{t-1} \,\Bigg|\, \frac{1}{\sqrt{\alpha_t}}\Bigl(x_t - \frac{1-\alpha_t}{\sqrt{1-A_t}}\,\epsilon_\theta(x_t,t)\Bigr),\; \Sigma_\theta(x_t,t)\right).
\]

### DDPM (Denoising Diffusion Probabilistic Models)

(Ho et al., 2020) refine the earlier framework with the same basic structure of the loss. The key observations are:

- The forward diffusion variances \(\beta_t\) are fixed hyperparameters → all \(q\)‑distributions are untrained. Since \(p_\theta(x_T)\) is a fixed prior, \(L_T\) is a constant.
- For the intermediate steps the variances in \(p_\theta(x_t \mid x_{t+1})\) are also not trained; a simple closed form for \(L_t\) is available.
- For \(L_0\) (the final decoding step) a separate discrete decoder is introduced. If the data are integers in \(\{0,\dots,255\}\) rescaled to \([-1,1]\) (the natural image representation), DDPM models

\[
p_\theta(x_0 \mid x_1) = \prod_{i=1}^{D} \int_{\delta_-(x_{0,i})}^{\delta_+(x_{0,i})} \mathcal{N}\!\bigl(x \mid \mu_{\theta,i}(x_1),\; \sigma^2_1\bigr)\,dx,
\]

where \(i\) runs over pixels, \(\mu_\theta(x_1)\) is the decoder, and the integration limits extend \(\frac{1}{255}\) on each side of \(x_{0,i}\). At sampling time one can use \(\mu_\theta(x_1)\) without noise.

DDPM already gave excellent generation, comparable to the best GANs of the time. (The earlier Sohl‑Dickstein et al. 2015 results had worked well only on small datasets like CIFAR.)

### DDIM (Denoising Diffusion Implicit Models)

(Song et al., 2020) address a major drawback: all diffusion models up to that point are very slow at generation because they must run sequentially through thousands of steps. Sampling from a trained GAN is about 1000× faster than from DDPM for the same image size.

The key insight is that the loss \(L\) depends only on the marginals \(q(x_t \mid x_0)\), not on the full joint \(q(x_{1:T} \mid x_0)\). Hence we can define a **different** forward joint distribution with the same marginals and reuse the same loss function. In particular, we can generalise to **non‑Markovian** forward processes, as long as a reverse Markov chain exists.

For DDIM, the forward process is defined implicitly through its reverse form:

\[
q_\sigma(x_{1:T} \mid x_0) = q_\sigma(x_T \mid x_0) \prod_{t=2}^{T} q_\sigma(x_{t-1} \mid x_t, x_0).
\]

The corresponding forward conditional is obtained by Bayes’ theorem:

\[
q_\sigma(x_t \mid x_{t-1}, x_0) = \frac{q_\sigma(x_{t-1} \mid x_t, x_0)\,q_\sigma(x_t \mid x_0)}{q_\sigma(x_{t-1} \mid x_0)} .
\]

It can be shown that the marginals remain unchanged, so the reverse diffusion can be trained with the same ELBO, and it yields a Markov chain.

So far the number of sampling steps is still large. However, the reparametrisation now allows us to approximate the noise \(\epsilon_t\) that would lead directly from \(x_0\) to \(x_t\), rather than from \(x_t\) to \(x_{t+1}\). In the reverse direction we estimate the direction toward \(x_0\) and can take larger jumps, moving from \(x_t\) to \(x_{t+k}\) in a single step by inflating \(\epsilon\) appropriately. This gives a 10×–100× speedup over DDPM without loss of quality.

Additionally, generation in DDIM need not be stochastic: we can set the reverse variance to zero, making the mapping deterministic. Then each latent code in \(x_T\) corresponds to exactly one image, and DDIM becomes a good model for latent representations – e.g., interpolations in the latent space are smooth (something DDPM could not do because of its high noise).

### Stable Diffusion

A further breakthrough came when the diffusion process was moved into a lower‑dimensional latent space.

**Stable Diffusion** (Rombach, Blattmann et al., 2022) trains a diffusion model on latent codes obtained from a pretrained autoencoder. This dramatically reduces computational cost while preserving high quality.

### DALL‑E 2 (unCLIP)

**unCLIP**, also known as DALL‑E 2 (Ramesh et al., 2022), factorises the conditional image generation as

\[
p(x \mid y) = p(x \mid c, y)\,p(c \mid y),
\]

where:

- a prior model \(p(c \mid y)\) produces a CLIP embedding \(c\) from a text description \(y\);
- the decoder \(p(x \mid c, y)\) first generates a “noise” (prior) for the image, then uses a diffusion model to draw the image conditioned on both \(c\) and \(y\).

### Midjourney

Midjourney is another diffusion‑based image generation model; its architecture and training details are not elaborated in this lecture.

### Diffusion Transformers (DiT)

A fully modern architecture, **DiT** (Peebles, Xie, 2022), is a latent diffusion model that replaces the U‑Net backbone with a transformer.

The input is an \(I \times I \times C\) tensor, “patchified” into a sequence of \(p \times p\) patches, giving sequence length \(T = (I/p)^2\) (the patch size \(p\) quadratically influences complexity). These tokens are processed by DiT blocks that use **adaptive layer normalisation**, where the normalisation parameters come from a conditioning signal (e.g., a time embedding).

DiTs are much more computationally efficient: Transformer GFLOPs correlate strongly with generation quality, and large DiT models use computation more efficiently than U‑Net–based counterparts.

### Flux

Flux is a later diffusion‑based model; no further details are provided in this lecture.

### Recent Developments

#### DPM‑Solver++

(Lu et al., 2022) observe that DDIM corresponds to a first‑order integration of an underlying ordinary differential equation (ODE). By employing higher‑order (e.g., multistep second‑ or third‑order) ODE solvers, one can reduce the local error and take even larger steps, so even fewer reverse steps are required. DPM‑Solver++ proves more stable and efficient than previous approaches.

#### UniPC

(Zhao et al., 2023) propose a “predictor‑corrector” framework. They derive a universal correcting step (UniC) that can be added after any base predictor to increase the order of accuracy without additional model evaluations; the matching UniP predictor is derived accordingly.

#### Flow Matching

The most significant recent direction is **flow matching**. Many modern generative models are now based on this approach. Details of flow matching are beyond the scope of this lecture.
