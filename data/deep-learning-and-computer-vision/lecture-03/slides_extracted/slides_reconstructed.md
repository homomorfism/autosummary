# Gradient Descent and General DL Remarks

## Gradient Descent and Computational Graphs

### Gradient Descent

**Gradient descent** updates weights by moving in the direction of the negative gradient of an error function. For an error function $E$, targets $y$, and a model $f$ with parameters $\theta$,

$$
E(\theta) = \sum_{(x,y) \in D} E(f(x, \theta), y),
$$

$$
\theta_t = \theta_{t-1} - \eta \nabla E(\theta_{t-1}) = \theta_{t-1} - \eta \sum_{(x,y) \in D} \nabla E(f(x, \theta_{t-1}), y).
$$

Summing over the entire dataset at every step is impractical, so **stochastic gradient descent (SGD)** uses a single sample (or a mini‑batch):

$$
\theta_t = \theta_{t-1} - \eta \nabla E(f(x_t, \theta_{t-1}), y_t).
$$

Mini‑batches are easy to parallelise and smooth out excessive stochasticity. The only parameter is the learning rate $\eta$; many problems later, but first we must compute derivatives efficiently.

### Computational Graphs, Forward and Backward Propagation

Represent a function as a composition of simple functions for which derivatives are known.  
Example: $f(x, y) = x^2 + xy + (x+y)^2$ can be decomposed into a computational graph.  
(The graph is shown as a figure – a sequence of elementary operations.)

The **chain rule** gives the derivative of a composition:

$$
(f \circ g)'(x) = f'(g(x)) \, g'(x).
$$

For vector-valued functions, the gradient $\nabla_{\!x} f = \left( \frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n} \right)^\top$ obeys

$$
\nabla_{\!x} (f \circ g) = \frac{\partial f}{\partial g} \nabla_{\!x} g.
$$

When $f$ depends on $x$ in several ways, $f = f(g_1(x), g_2(x), \dots, g_k(x))$, the derivative sums over all paths:

$$
\frac{\partial f}{\partial x} = \sum_{i=1}^{k} \frac{\partial f}{\partial g_i} \frac{\partial g_i}{\partial x},
\qquad
\nabla_{\!x} f = \sum_{i=1}^{k} \frac{\partial f}{\partial g_i} \nabla_{\!x} g_i.
$$

In matrix form, $\nabla_{\!x} f = \nabla_{\!x} \mathbf{g} \; \nabla_{\!\mathbf{g}} f$, where the Jacobian

$$
\nabla_{\!x} \mathbf{g} =
\begin{pmatrix}
\frac{\partial g_1}{\partial x_1} & \dots & \frac{\partial g_k}{\partial x_1} \\
\vdots & & \vdots \\
\frac{\partial g_1}{\partial x_n} & \dots & \frac{\partial g_k}{\partial x_n}
\end{pmatrix}.
$$

**Forward propagation** computes $\frac{\partial f}{\partial x}$ by traversing the graph from inputs to the output.  
**Backpropagation** starts from the output and works backward:

$$
\frac{\partial f}{\partial g} = \sum_{g' \in \text{Children}(g)} \frac{\partial f}{\partial g'} \frac{\partial g'}{\partial g}.
$$

Backprop obtains all derivatives in a single pass through the graph. This is exactly the core of modern deep learning frameworks – PyTorch, TensorFlow, Theano are essentially automatic differentiation libraries.  
(Incidentally, biological neurons cannot do this because they would need separate outputs to compute the value and the derivative.)

---

## Activation Functions

### Survey of Activation Functions

- **Logistic sigmoid:** $\displaystyle \sigma(x) = \frac{1}{1+e^{-x}}$.
- **Hyperbolic tangent:** $\displaystyle \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$. (Similar to sigmoid but zero is not a saturation point.)

- **Heaviside step function:**
  $$ \text{step}(x) = \begin{cases}
  0, & \text{if } x < 0, \\
  1, & \text{if } x > 0.
  \end{cases} $$

- **Rectified Linear Unit (ReLU):**
  $$ \text{ReLU}(x) = \begin{cases}
  0, & \text{if } x < 0, \\
  x, & \text{if } x \ge 0.
  \end{cases} $$

  - **Mathematical motivation:** a sum of shifted sigmoids approximates a soft ReLU:
    $$ \sigma\!\left(x+\tfrac{1}{2}\right) + \sigma\!\left(x-\tfrac{1}{2}\right) + \sigma\!\left(x-\tfrac{3}{2}\right) + \dots $$

  - **Biological motivation:** a simple integrate‑and‑fire neuron with a refractory period yields a response
    $$ f(I) = \begin{cases}
    \left( \tau \log \frac{E+RI - V_{\text{reset}}}{E+RI - V_{th}} \right)^{-1}, & \text{if } E+RI > V_{th}, \\
    0, & \text{if } E+RI \le V_{th}.
    \end{cases} $$

- **ReLU variants:**
  - **Softplus:** $\text{softplus}(x) = \ln(1+e^x)$.
  - **Leaky ReLU:** $\displaystyle \text{LReLU}(x) = \begin{cases} a x, & x<0,\\ x, & x>0. \end{cases}$
  - **Exponential Linear Unit (ELU):** $\displaystyle \text{ELU}(x) = \begin{cases} \alpha(e^x-1), & x<0,\\ x, & x\ge 0. \end{cases}$

- **Swish** (found by automatic search, Ramachandran et al. 2017):
  $$ \text{Swish}(x) = x\,\sigma(\beta x) = \frac{x}{1+e^{-\beta x}}. $$

- **Mish** (Misra 2019):
  $$ \text{Mish}(x) = x \tanh\!\bigl(\text{softplus}(x)\bigr) = x \tanh\!\bigl(\ln(1+e^x)\bigr). $$

### ACON: A General Framework

A smooth generalisation of the maximum (Ma et al. 2020):

$$
S_\beta(x_1, \dots, x_n) = \frac{\sum_{i=1}^n x_i e^{\beta x_i}}{\sum_{i=1}^n e^{\beta x_i}}.
$$

Taking two functions $g(x), h(x)$ and using the identity $\frac{e^{\beta g}}{e^{\beta g}+e^{\beta h}} = \sigma(\beta(g-h))$, we obtain

$$
\begin{aligned}
S_\beta(g(x), h(x)) &= g(x)\frac{e^{\beta g(x)}}{e^{\beta g(x)}+e^{\beta h(x)}} + h(x)\frac{e^{\beta h(x)}}{e^{\beta g(x)}+e^{\beta h(x)}} \\
&= g(x)\sigma(\beta(g(x)-h(x))) + h(x)\sigma(\beta(h(x)-g(x))) \\
&= (g(x)-h(x))\,\sigma(\beta(g(x)-h(x))) + h(x).
\end{aligned}
$$

This construction, called **ACON** (ActivateOrNot), encompasses many activation functions:

- **ACON‑A:** set $g(x)=x,\; h(x)=0$. The hard maximum is $\max(x,0)=\text{ReLU}$, and the soft maximum gives $\text{Swish}(x) = x\,\sigma(\beta x)$.

- **ACON‑B:** $g(x)=x,\; h(x)=a x$ ($a<1$). The hard maximum is $\max(x, a x) = \text{LReLU}(x)$, and the soft version is
  $$ f_{\text{ACON-B}} = (1-a)\,x\,\sigma(\beta(1-a)x) + a x. $$

- **ACON‑C:** generalise to $g(x)=a_1 x$, $h(x)=a_2 x$:
  $$ f_{\text{ACON-C}} = (a_1-a_2)\,x\,\sigma(\beta(a_1-a_2)x) + a_2 x. $$
  Here $a_1, a_2$ are learnable parameters; intuitively they are the asymptotic slopes:
  $$ \lim_{x\to\infty} \frac{d f_{\text{ACON-C}}}{dx} = a_1,\qquad \lim_{x\to-\infty} \frac{d f_{\text{ACON-C}}}{dx} = a_2. $$
  (A plot of ACON‑C for various parameter values is shown.)

Ma et al. demonstrate that tuning these parameters yields improvements even on standard tasks. While ACON‑C is not yet widely adopted, it illustrates the unexplored design space even in elementary activation functions.

---

## Variations of Gradient Descent

### Vanilla Gradient Descent and Learning Rate Schedules

The plain gradient descent update:
$$ \mathbf{x}_k = \mathbf{x}_{k-1} - \alpha \nabla f(\mathbf{x}_k). $$

The learning rate $\alpha$ is crucial. Two basic schedules:
- **Linear decay:** $\displaystyle \alpha = \alpha_0\left(1 - \frac{t}{T}\right)$.
- **Exponential decay:** $\displaystyle \alpha = \alpha_0 e^{-t/T}$.

### Wolfe Conditions and Step Size Selection

When searching along a descent direction $\mathbf{p}_k$ (e.g., $\mathbf{p}_k = \nabla_{\!x} f(\mathbf{x}_k)$), define $\phi_k(\alpha) = f(\mathbf{x}_k + \alpha \mathbf{p}_k)$. Then $\phi'_k(\alpha) = \nabla f(\mathbf{x}_k + \alpha \mathbf{p}_k)^\top \mathbf{p}_k$, and $\phi'_k(0) < 0$ if $\mathbf{p}_k$ is a descent direction. The step size $\alpha$ should satisfy:

- **Armijo rule:** $\phi_k(\alpha) \le \phi_k(0) + c_1 \alpha \phi'_k(0)$ for some $c_1 \in (0, \tfrac12)$.
- **Wolfe conditions (stronger):** Armijo rule **plus** $|\phi'_k(\alpha)| \le c_2 |\phi'_k(0)|$, i.e., the gradient projection is sufficiently decreased.

Stopping criterion: $\|\nabla f(\mathbf{x}_k)\|_2 \le \epsilon$ or $\|\nabla f(\mathbf{x}_k)\|_2 \le \epsilon \|\nabla f(\mathbf{x}_0)\|_2$.

### Newton’s Method and L‑BFGS

When variables differ in scale, e.g. $f(x,y) = \frac12 x^2 + \frac{\rho}{2} y^2$ with $\rho \gg 1$, gradient descent zig‑zags slowly.  
**Newton’s method** scales the step by the inverse Hessian:

$$
\mathbf{g}_k = \nabla_{\!x} f(\mathbf{x}_k),\quad \mathbf{H}_k = \nabla^2_{\!x} f(\mathbf{x}_k),\qquad
\mathbf{x}_{k+1} = \mathbf{x}_k - \alpha_k \mathbf{H}_k^{-1} \mathbf{g}_k.
$$

The Armijo rule applies to Newton steps:
$$ \alpha_k :\; f(\mathbf{x}_{k+1}) \le f(\mathbf{x}_k) - c_1 \alpha_k \mathbf{g}_k^\top \mathbf{H}_k^{-1} \mathbf{g}_k,\quad c_1 \approx 10^{-4}. $$

Computing $\mathbf{H}_k$ is prohibitive for large networks. Quasi‑Newton methods such as **L‑BFGS** build an approximation of $\mathbf{H}^{-1}$ from stored history of argument updates. An open question is whether L‑BFGS or similar can be made practical for deep learning; currently they do not work well, partly because the gradient itself is only an estimate.

---

## Stochastic Gradient Descent (SGD)

### Formalisation and Mini‑Batches

In practice we use stochastic gradient descent:

$$
\mathbf{x}_t = \mathbf{x}_{t-1} - \alpha \nabla f(\mathbf{x}_{t-1}, y_t)
$$
(and its mini‑batch variant). This arises from **stochastic optimisation**:

$$
F(\mathbf{x}) = \mathbb{E}_{q(\mathbf{y})} f(\mathbf{x}, \mathbf{y}) \to \min_{\mathbf{x}},
$$

where, for example, $F(\mathbf{x}) = \frac{1}{N} \sum_{i=1}^N f_i(\mathbf{x}) = \mathbb{E}_{i \sim \mathcal{U}(1,\dots,N)} f_i(\mathbf{x})$ (empirical risk minimisation).  

A mini‑batch of size $m$ yields unbiased estimates:

$$
\hat{F}(\mathbf{x}) = \frac{1}{m} \sum_{i=1}^m f(\mathbf{x}, \mathbf{y}_i),\qquad
\hat{\mathbf{g}}(\mathbf{x}) = \frac{1}{m} \sum_{i=1}^m \nabla_{\!x} f(\mathbf{x}, \mathbf{y}_i).
$$

### Problems of SGD

- It never moves in exactly the right direction;
- Even at the exact optimum of $F$, the stochastic gradient step is non‑zero, so convergence with constant step size is impossible;
- We do not know $F$ or $\nabla F$, so the Armijo and Wolfe rules cannot be applied.

### Convergence Analysis

Assume $F(\mathbf{x}) = \mathbb{E}_{q(\mathbf{y})} f(\mathbf{x}, \mathbf{y})$ and consider the iteration

$$
\mathbf{x}_{k+1} = \mathbf{x}_k - \alpha_k \hat{\mathbf{g}}_k,\qquad \mathbb{E}\,\hat{\mathbf{g}}_k = \mathbf{g}_k = \nabla F(\mathbf{x}_k).
$$

Expanding the squared distance to the optimum $\mathbf{x}_{\text{opt}}$:

$$
\begin{aligned}
\|\mathbf{x}_{k+1} - \mathbf{x}_{\text{opt}}\|^2
&= \|\mathbf{x}_k - \alpha_k \hat{\mathbf{g}}_k - \mathbf{x}_{\text{opt}}\|^2 \\
&= \|\mathbf{x}_k - \mathbf{x}_{\text{opt}}\|^2 - 2\alpha_k \hat{\mathbf{g}}_k^\top (\mathbf{x}_k - \mathbf{x}_{\text{opt}}) + \alpha_k^2 \|\hat{\mathbf{g}}_k\|^2.
\end{aligned}
$$

Taking expectation w.r.t. the data at step $k$:

$$
\mathbb{E}\|\mathbf{x}_{k+1} - \mathbf{x}_{\text{opt}}\|^2 = \|\mathbf{x}_k - \mathbf{x}_{\text{opt}}\|^2 - 2\alpha_k \mathbf{g}_k^\top (\mathbf{x}_k - \mathbf{x}_{\text{opt}}) + \alpha_k^2 \mathbb{E}\|\hat{\mathbf{g}}_k\|^2.
$$

If $F$ is convex, $F(\mathbf{x}_{\text{opt}}) \ge F(\mathbf{x}_k) + \mathbf{g}_k^\top (\mathbf{x}_k - \mathbf{x}_{\text{opt}})$. Substituting,

$$
\alpha_k \bigl(F(\mathbf{x}_k) - F(\mathbf{x}_{\text{opt}})\bigr) \le
\frac12 \|\mathbf{x}_k - \mathbf{x}_{\text{opt}}\|^2 + \frac12 \alpha_k^2 \mathbb{E}\|\hat{\mathbf{g}}_k\|^2 - \frac12 \mathbb{E}\|\mathbf{x}_{k+1} - \mathbf{x}_{\text{opt}}\|^2.
$$

Summing from $i=0$ to $k$ and telescoping:

$$
\sum_{i=0}^k \alpha_i \bigl(\mathbb{E} F(\mathbf{x}_i) - F(\mathbf{x}_{\text{opt}})\bigr)
\le \frac12 \|\mathbf{x}_0 - \mathbf{x}_{\text{opt}}\|^2 + \frac12 \sum_{i=0}^k \alpha_i^2 \mathbb{E}\|\hat{\mathbf{g}}_i\|^2.
$$

By convexity, the weighted average $\hat{\mathbf{x}}_k = \frac{\sum \alpha_i \mathbf{x}_i}{\sum \alpha_i}$ satisfies

$$
\mathbb{E} F(\hat{\mathbf{x}}_k) - F(\mathbf{x}_{\text{opt}}) \le
\frac{\|\mathbf{x}_0 - \mathbf{x}_{\text{opt}}\|^2 + \sum_{i=0}^k \alpha_i^2 \mathbb{E}\|\hat{\mathbf{g}}_i\|^2}{2\sum_{i=0}^k \alpha_i}.
$$

Assuming $\|\mathbf{x}_0 - \mathbf{x}_{\text{opt}}\| \le R$ and $\mathbb{E}\|\hat{\mathbf{g}}_k\|^2 \le G^2$,

$$
\mathbb{E} F(\hat{\mathbf{x}}_k) - F(\mathbf{x}_{\text{opt}}) \le \frac{R^2 + G^2 \sum_{i=0}^k \alpha_i^2}{2\sum_{i=0}^k \alpha_i}.
$$

**Key consequences:**

- For constant step size $\alpha_i = h$,
  $$ \mathbb{E} F(\hat{\mathbf{x}}_k) - F(\mathbf{x}_{\text{opt}}) \le \frac{R^2}{2h(k+1)} + \frac{G^2 h}{2} \xrightarrow{k\to\infty} \frac{G^2 h}{2}. $$
  SGD converges to an “uncertainty region” of radius proportional to the step size.
- Larger $h$ gives faster initial progress but a larger final uncertainty region; we must decrease the learning rate over time.
- SGD convergence is slow: full GD achieves $O(1/k)$ for convex functions, while SGD gives $O(1/\sqrt{k})$ because of the variance term.
- Far from the uncertainty region the rate is still $O(1/k)$, so slowdown only occurs near the optimum.
- The bound depends on the variance $G^2$ – crucial for neuro‑Bayesian approaches.

---

## SGD with Momentum

### Classical Momentum

To maintain velocity and damp oscillations, we keep a fraction $\gamma$ of the previous update:

$$
\mathbf{u}_t = \gamma \mathbf{u}_{t-1} + \eta \nabla_{\!x} F(\mathbf{x}),\qquad
\mathbf{x} = \mathbf{x} - \mathbf{u}_t.
$$

### Nesterov’s Momentum

We know the intermediate point $\gamma \mathbf{u}_{t-1}$ where the parameters are heading; let’s evaluate the gradient there:

$$
\mathbf{u}_t = \gamma \mathbf{u}_{t-1} + \eta \nabla_{\!x} F(\mathbf{x} - \gamma \mathbf{u}_{t-1}).
$$

Problems remain – can we do even better?

---

## Adaptive Gradient Descent

### Motivation and Adagrad

Instead of a single global learning rate, adapt the rate per parameter: move faster along dimensions with small, consistent gradients and slower along rapidly changing ones.

**Adagrad** maintains a diagonal matrix $\mathbf{G}_t$ that accumulates squared gradients:

$$
G_{t,ii} = G_{t-1,ii} + g_{t,i}^2,\qquad
g_{t,i} = \frac{\partial L}{\partial w_i}.
$$

The update:
$$ w_{t+1,i} = w_{t,i} - \frac{\eta}{\sqrt{G_{t,ii} + \epsilon}} \; g_{t,i}. $$

Because $G_{t,ii}$ always grows, the learning rate decays monotonically and never rebounds – undesirable for non‑stationary problems.

### Adadelta

**Adadelta** (Zeiler 2012) mitigates the monotonic decay in two ways:

1. **Exponential moving average** of squared gradients:
   $$ G_{t,ii} = \rho G_{t-1,ii} + (1-\rho) g_{t,i}^2. $$
   Update: $\displaystyle \mathbf{u}_t = -\frac{\eta}{\sqrt{\mathbf{G}_{t-1} + \epsilon}} \,\mathbf{g}_{t-1}$.

2. **Units matching:** In plain SGD or momentum, the update $\Delta w$ has the units of the gradient (e.g., m/s for weights in seconds), which is dimensionally inconsistent. Second‑order methods fix this because $\Delta w \propto \mathbf{H}^{-1} \nabla f$ automatically carries the dimension of $w$. Adadelta approximates the RMS of parameter updates with another exponential average:
   $$ \mathbb{E}[\Delta w^2]_t = \rho \mathbb{E}[\Delta w^2]_{t-1} + (1-\rho) \Delta w_t^2, $$
   and then
   $$ \mathbf{u}_t = - \frac{\sqrt{\mathbb{E}[\Delta w^2]_{t-1} + \epsilon}}{\sqrt{\mathbf{G}_{t-1} + \epsilon}} \; \mathbf{g}_{t-1}. $$

### RMSprop

**RMSprop** (from Hinton’s lectures) is essentially Adadelta without the units‑matching correction:

$$ \mathbf{u}_t = - \frac{\eta}{\sqrt{\mathbf{G}_{t-1} + \epsilon}} \; \mathbf{g}_{t-1}. $$

### Adam

**Adam** (Kingma & Ba 2014) combines momentum with adaptive scaling, using bias‑corrected exponential moving averages of the gradient and its square:

$$
\begin{aligned}
\mathbf{m}_t &= \beta_1 \mathbf{m}_{t-1} + (1-\beta_1) \mathbf{g}_t, \\
\mathbf{v}_t &= \beta_2 \mathbf{v}_{t-1} + (1-\beta_2) \mathbf{g}_t^2, \\
\mathbf{u}_t &= \frac{\eta}{\sqrt{\mathbf{v}_t} + \epsilon} \mathbf{m}_t.
\end{aligned}
$$

Recommended defaults: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$. Adam is widely used because it usually requires little tuning.

### Nadam

**Nadam** (Dozat 2016) incorporates Nesterov’s momentum into Adam.

### General Formulation

Adaptive methods can be seen as a unified framework:

- **Vanilla SGD:**
  $\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha_k \tilde{\nabla} f(\mathbf{w}_k)$,
  where $\tilde{\nabla} f(\mathbf{w}_k) = \nabla f(\mathbf{w}_k; x_{i_k})$.

- **SGD with momentum:**
  $\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha_k \tilde{\nabla} f\bigl(\mathbf{w}_k + \gamma_k (\mathbf{w}_k - \mathbf{w}_{k-1})\bigr) + \beta_k (\mathbf{w}_k - \mathbf{w}_{k-1})$.

- **Adaptive SGD:**
  $\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha_k \mathbf{H}_k^{-1} \tilde{\nabla} f\bigl(\mathbf{w}_k + \gamma_k (\mathbf{w}_k - \mathbf{w}_{k-1})\bigr) + \beta_k \mathbf{H}_k^{-1} \mathbf{H}_{k-1} (\mathbf{w}_k - \mathbf{w}_{k-1})$,
  where $\mathbf{H}_k = \operatorname{diag}\!\bigl( [\sum_{i=1}^k \eta_i \mathbf{g}_i \circ \mathbf{g}_i]^{1/2} \bigr)$, i.e. a diagonal matrix of the square roots of weighted sums of past squared gradients (with $\mathbf{g}_k = \tilde{\nabla} f$). Basic SGD corresponds to $\mathbf{H}_k = \mathbf{I}$ (standard $L_2$ geometry).

---

## Adam, AdamW, and Other Modifications

### Poor Generalisation of Adaptive Methods

Adam was initially celebrated, but researchers later reverted to plain SGD in many tasks. **Wilson et al. (2017)** showed that adaptive methods can converge to different, often worse‑generalising minima (overfitting). This is not only a worst‑case concern but appears in practice. Because Adam is sometimes superior in early training, switching from Adam to SGD mid‑training was proposed (Keskar & Socher 2017).

### Weight Decay and AdamW

**Weight decay** (Hanson & Pratt 1988) originally meant

$$
\mathbf{x}_{t+1} = (1 - w) \mathbf{x}_t - \eta \nabla f_t(\mathbf{x}_t).
$$

It is equivalent to adding an $L_2$ regulariser: $f_t^{\text{reg}}(\mathbf{x}_t) = f_t(\mathbf{x}_t) + \frac{w}{2} \|\mathbf{x}_t\|_2^2$, i.e. $\nabla f_t^{\text{reg}} = \nabla f_t + w \mathbf{x}_t$.  
However, with momentum or adaptive methods this equivalence breaks: in momentum, $\mathbf{x}_t$ decays by $\alpha w \mathbf{x}_{t-1}$ instead of $w \mathbf{x}_{t-1}$, coupling the weight decay hyperparameter with the learning rate. The simple fix is to apply decay directly to the parameter update after scaling.

**AdamW** (Loshchilov & Hutter 2018) decouples weight decay from the adaptive step:

$$
\begin{aligned}
\text{(Standard AdamL2)} &\quad \mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1-\beta_1)(\mathbf{g}_t + w \mathbf{w}_{t-1}), \\
\text{(AdamW)} &\quad \mathbf{w}_t = \mathbf{w}_{t-1} - \eta \left( \frac{1}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon} \hat{\mathbf{m}}_t + w \mathbf{w}_{t-1} \right).
\end{aligned}
$$

In AdamW, the weight decay is applied separately, restoring the original behaviour and decoupling hyperparameters. Both the hyperparameter landscape and generalisation improve compared to standard Adam.

---

## Super‑Convergence and AMSGrad

- **Super‑Convergence** (Smith & Topin 2017): cyclically varying the learning rate (a combination of curriculum learning and simulated annealing) can drastically accelerate training. However, this does not reproduce stably across tasks.

- **AMSGrad** (Reddi et al. 2018): the exponential moving average in Adam/RMSprop can harm convergence; the original proof of Adam’s convergence was incorrect. AMSGrad keeps the maximum of past gradient squares instead of the exponential average, which fixes the convergence proof. In practice, however, the benefit is not always confirmed.
