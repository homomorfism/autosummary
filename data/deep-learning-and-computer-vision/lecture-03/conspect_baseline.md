# Gradient Descent and General Deep Learning Remarks

Deep learning replaced the manual feature extraction of classical machine learning with a single end‑to‑end trainable model – the neural network. Inside every such network there is still a feature‑extraction part, followed by a final linear layer (linear regression or, much more often, logistic regression). Training any neural network amounts to minimizing a loss function with respect to its millions of weights. The only practical tool we have for that is gradient descent, and the key algorithmic ingredient that makes it possible is **backpropagation**.

---

## Activation Functions *[06:30]*

A single artificial neuron computes a linear combination of its inputs and then applies a non‑linear **activation function**. Composing many such simple units can approximate arbitrarily complex behaviour, but the activation must be chosen so that gradients can flow backwards through the network.

### From Threshold to Sigmoid

The original McCulloch–Pitts neuron and the Rosenblatt perceptron used a **threshold (Heaviside step)** function:

$$
\text{step}(x) = \begin{cases}
0, & \text{if } x < 0,\\
1, & \text{if } x \ge 0.
\end{cases}
$$

With a single perceptron this can work, but in a multi‑layer network the derivative is zero almost everywhere — the gradient would be identically zero and no learning can happen. The natural fix is a smooth approximation. For decades neural networks used **sigmoid** functions, monotonically increasing from a low horizontal asymptote to a high one. The most common choices were:

- **logistic sigmoid**  
  $$\sigma(x) = \frac{1}{1 + e^{-x}}$$
  (saturates at 0 and 1)  
- **hyperbolic tangent**  
  $$\tanh(x) = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$$
  (saturates at –1 and +1, symmetric around zero – preferred for hidden layers)

Both suffer from **saturation**: when the input to the neuron becomes large in absolute value, the derivative of the activation becomes very close to zero and the gradients effectively stop.

### ReLU and Its Benefits *[13:25]*

Around 2011–2012 a much simpler activation was tried and proved extremely effective: the **rectified linear unit (ReLU)**.

$$
\text{ReLU}(x) = \max(0, x) =
\begin{cases}
0, & \text{if } x < 0,\\
x, & \text{if } x \ge 0.
\end{cases}
$$

**Why ReLU works well:**

- On the negative side the gradient is zero – this introduces **sparsity**, which is often desirable (e.g. in convolutional networks where weights are reused across the input, having half of the activations zero is fine and even acts as a regularizer).
- On the positive side the function is **unbounded** and its derivative is constant (1). Unlike sigmoids, a neuron can distinguish between “activated” and “strongly activated”; there is no saturation on the right, so gradients never vanish just because the neuron is very sure.
- There is a nice mathematical intuition: $\text{ReLU}(x)$ can be seen as an infinite sum of shifted sigmoids $\sum_{i} \sigma(x + \frac{1}{2} - i)$ which, after smoothing, asymptotically approaches a straight line with slope 1.
- There is also a biological justification: the firing rate of real biological neurons as a function of input current looks like a black curve that first stays quiet, goes through a phase transition, and then becomes roughly linear – very similar to ReLU.

### Further Evolution: Leaky ReLU, Swish, Mish, ACON

- **Leaky ReLU** $\text{LReLU}(x) = \max(ax, x)$ with a small slope $a$ on the negative side (e.g. $a=0.01$) – prevents complete gradient loss on negative inputs.
- **Softplus** $\text{softplus}(x) = \ln(1+e^x)$ – a smooth approximation of ReLU.
- **Exponential Linear Unit (ELU)**: $\text{ELU}(x) = x$ for $x\ge0$, $\alpha(e^x-1)$ for $x<0$.

Around 2017, researchers at Google ran an **automated search** over the space of activation functions represented as computational graphs. The search was evolutionary (mutations and cross‑overs of graph structures) and purely empirical – it simply tried many candidate functions on a suite of architectures and datasets. The winner was **Swish**:

$$
\text{Swish}(x) = x\,\sigma(\beta x) = \frac{x}{1 + e^{-\beta x}}.
$$

Swish looks similar to ReLU on the right but has a non‑monotonic bump on the left (it dips below zero and then returns to zero). It consistently outperformed ReLU in many vision architectures. A later variant, **Mish**, $x\tanh(\text{softplus}(x))$, also became popular.

In 2020, Ma et al. introduced **ACON (ActivateOrNot)**, a family that generalizes many activations through a smooth maximum operator:

$$
S_\beta(x_1,\dots,x_n) = \frac{\sum_{i=1}^n x_i e^{\beta x_i}}{\sum_{i=1}^n e^{\beta x_i}}.
$$

By setting $g(x)$ and $h(x)$ as two functions of $x$, the soft maximum

$$
f_{\text{ACON}} = S_\beta(g(x), h(x)) = (g(x)-h(x))\,\sigma(\beta(g(x)-h(x))) + h(x)
$$

recovers Swish when $g(x)=x,\; h(x)=0$, Leaky ReLU variants when $g(x)=x,\; h(x)=ax$, and a learnable $a_1,a_2$ in **ACON‑C**. Despite interesting properties, ACON is rarely seen in practice.

Modern large language models often use the **Gaussian Error Linear Unit (GELU)**, $x\,\Phi(x)$ (with the CDF of a standard Gaussian), which also resembles a smooth Swish.

**Practical recommendation:** start with ReLU, try Swish or GELU, and perhaps a Leaky ReLU variant as a fallback.

---

## Backpropagation and Computational Graphs *[30:44]*

### The Training Objective

The network computes a scalar loss $l(\mathbf{x}, y, \mathbf{w})$ for one training sample. The total loss for the whole dataset is the average (or sum)

$$
L(\mathbf{w}) = \frac{1}{N}\sum_{n=1}^{N} l(\mathbf{x}_n, y_n, \mathbf{w}).
$$

Training means finding $\mathbf{w}$ that minimizes $L(\mathbf{w})$. The network is a massive composition of simple operations — a **computational graph** — so the only realistic way to obtain the gradient $\nabla_{\mathbf{w}} L$ is to differentiate through that graph automatically.

### Computational Graph and Chain Rule

Any formula can be drawn as a directed acyclic graph whose nodes are elementary operations (addition, multiplication, exponentiation, etc.). For a concrete example we will use

$$
f(x,y) = (x+y)^2 (x-y) + y^3.
$$

The graph is:

```
    x   y
   / \ / \
  a=(x+y)  b=(x-y)  c=y^3
    |
    d = a²
     \
      e = d · b
       \
        f = e + c
```

Intermediate nodes: $a=x+y$, $b=x-y$, $c=y^3$, $d=a^2$, $e=d\cdot b$, $f=e+c$.

### Forward Propagation as Derivative Computation

If we go bottom‑up we can compute not only the function values but also, say, $\frac{\partial f}{\partial x}$ by tracing how a small change in $x$ propagates. With $x=2, y=-1$:

- $a=1,\; b=3,\; c=-1,\; d=1,\; e=3,\; f=2$.
- $\frac{\partial f}{\partial x} = \frac{\partial e}{\partial x} + \frac{\partial c}{\partial x}$. $\frac{\partial c}{\partial x}=0$, $\frac{\partial e}{\partial x} = \frac{\partial d}{\partial x}\,b + d\,\frac{\partial b}{\partial x} = (2a\cdot1)\cdot b + 1\cdot d = 2ab + d = 2\cdot 1\cdot 3 + 1 = 7$.

We obtain both $f$ and $\frac{\partial f}{\partial x}$ in one single forward pass. To get $\frac{\partial f}{\partial y}$ we could either make a second pass or compute all derivatives simultaneously.

### Why Forward Propagation is Not Enough

In a real network the number of learnable weights $|\mathbf{w}|$ is in the millions (or billions). Forward‑propagating derivatives with respect to **every** weight would require either:

- $|\mathbf{w}|$ separate passes through the graph (completely infeasible time‑wise), or
- a single pass that carries a vector of size $|\mathbf{w}|$ on every edge, causing a memory blow‑up (a million copies of the network).

Neither approach is practical.

### Backpropagation: Computing $\frac{\partial f}{\partial \text{everything}}$

The solution is **backpropagation**. Instead of starting from the inputs and computing $\frac{\partial \text{everything}}{\partial x}$, we start from the output and compute $\frac{\partial f}{\partial \text{everything}}$ moving top‑down.

In the example:

- $\frac{\partial f}{\partial f} = 1$ (base case).
- $\frac{\partial f}{\partial e} = 1$, $\frac{\partial f}{\partial c} = 1$.
- $\frac{\partial f}{\partial d} = \frac{\partial f}{\partial e}\,\frac{\partial e}{\partial d} = 1 \cdot b = 3$.
- $\frac{\partial f}{\partial b} = \frac{\partial f}{\partial e}\,\frac{\partial e}{\partial b} = 1 \cdot d = 1$.
- $\frac{\partial f}{\partial a} = \frac{\partial f}{\partial d}\,\frac{\partial d}{\partial a} = 3 \cdot 2a = 6$.

Now, when a node has multiple outgoing edges (like $x$ feeding into $a$ and $b$) we sum the contributions:

$$
\frac{\partial f}{\partial x} = \frac{\partial f}{\partial a}\,\frac{\partial a}{\partial x} + \frac{\partial f}{\partial b}\,\frac{\partial b}{\partial x} = 6\cdot 1 + 1\cdot 1 = 7,
$$

$$
\frac{\partial f}{\partial y} = \frac{\partial f}{\partial a}\,\frac{\partial a}{\partial y} + \frac{\partial f}{\partial b}\,\frac{\partial b}{\partial y} + \frac{\partial f}{\partial c}\,\frac{\partial c}{\partial y} = 6\cdot 1 + 1\cdot (-1) + 1\cdot 3y^2 = 6 - 1 + 3 = 8.
$$

The crucial advantage: we obtained **all partial derivatives in a single backward pass** without recomputing shared sub‑expressions. Neural networks always have one scalar loss and many inputs (weights); backpropagation is perfectly suited to that asymmetry.

### Two Passes: Forward and Backward

In practice backpropagation requires two passes:

1. **Forward pass** – compute and store the numerical values of every intermediate node (because the local derivatives depend on those values).
2. **Backward pass** – starting from the output, recursively compute $\frac{\partial f}{\partial \text{everything}}$ using the chain rule and the stored values.

### Automatic Differentiation Libraries

Modern frameworks (PyTorch, TensorFlow, JAX) are, at their core, **automatic differentiation engines**. Their most performance‑critical job is to run forward and backward passes efficiently. All the layers, modules and high‑level APIs are syntactic sugar built on top of that graph‑tracing machinery. The weights are just a special kind of input to this graph – we differentiate with respect to them during training.

---

## Gradient Descent and Stochastic Gradient Descent *[01:17:21]*

### First‑order vs Second‑order Optimization

Gradient descent updates weights using the first‑order Taylor expansion:

$$
L(\mathbf{w}) \approx L(\mathbf{w}_k) + (\mathbf{w} - \mathbf{w}_k)^\top \nabla L(\mathbf{w}_k),
$$

and moves in the negative gradient direction:

$$
\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha \nabla L(\mathbf{w}_k).
$$

This is a “stupid” algorithm in the sense that it only tells you a direction, not how far to go – the step size $\alpha$ (the **learning rate**) must be chosen externally.

Centuries of optimisation theory have produced better techniques. The most natural is **Newton’s method**, which uses a quadratic approximation:

$$
L(\mathbf{w}) \approx L(\mathbf{w}_k) + (\mathbf{w}-\mathbf{w}_k)^\top \mathbf{g}_k + \frac{1}{2} (\mathbf{w}-\mathbf{w}_k)^\top \mathbf{H}_k (\mathbf{w}-\mathbf{w}_k),
$$

where $\mathbf{g}_k = \nabla L(\mathbf{w}_k)$ and $\mathbf{H}_k = \nabla^2 L(\mathbf{w}_k)$ (the Hessian). Setting the gradient to zero gives

$$
\mathbf{w}_{k+1} = \mathbf{w}_k - \mathbf{H}_k^{-1} \mathbf{g}_k.
$$

Newton’s method automatically determines the step size, is far more robust, and converges in fewer iterations. The obvious problem is computational: for $10^6$ parameters the Hessian is a $10^6 \times 10^6$ matrix that must be stored and inverted – impossible. Even quasi‑Newton methods that keep a low‑rank approximation (**L‑BFGS**) fail in deep learning because they rely on accurate gradient evaluations.

### The True Loss is an Expectation

The actual loss $L(\mathbf{w}) = \frac{1}{N}\sum_{n=1}^N l(\mathbf{x}_n, y_n, \mathbf{w})$ is an average over the whole training set. Computing the true gradient $\nabla L$ would require a full pass over the entire dataset on every single optimisation step, which is prohibitively expensive.

### Stochastic Gradient Descent

We therefore view $L$ as an expectation over the data distribution and approximate it with a small random subset – a **mini‑batch** of size $m$:

$$
\hat{\mathbf{g}}_k = \frac{1}{m} \sum_{i=1}^{m} \nabla_{\mathbf{w}}\, l(\mathbf{x}_{i_k}, y_{i_k}, \mathbf{w}_k).
$$

This is an unbiased Monte‑Carlo estimate of the true gradient. The update becomes

$$
\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha_k \,\hat{\mathbf{g}}_k.
$$

Mini‑batch sizes are usually small (4, 8, 16, …) because the network must fit into GPU memory. The variance of the gradient estimate is substantial, but it is the best approximation we can afford. This variance is the reason why second‑order methods break down – they need reliable gradient values, and stochastic samples with high variance destroy the delicate quasi‑Newton approximations.

### Theoretical Behaviour of SGD

A standard analysis (assuming convex $F$) yields the bound

$$
\mathbb{E}F(\hat{\mathbf{w}}_k) - F(\mathbf{w}_{\text{opt}}) \le \frac{R^2 + G^2 \sum_{i=0}^k \alpha_i^2}{2 \sum_{i=0}^k \alpha_i},
$$

where $R$ bounds the initial distance to the optimum and $G$ bounds the expected squared norm of the stochastic gradients. For a constant step size $h$,

$$
\mathbb{E}F(\hat{\mathbf{w}}_k) - F(\mathbf{w}_{\text{opt}}) \le \frac{R^2}{2h(k+1)} + \frac{G^2 h}{2} \;\xrightarrow{k\to\infty}\; \frac{G^2 h}{2}.
$$

**Key takeaways:**

- SGD quickly reaches a neighbourhood of the optimum, but with a constant learning rate it **never converges exactly**; it oscillates inside a “noisy ball” whose radius is proportional to $G^2 h$.
- To converge to the true optimum you must let the step sizes go to zero, e.g. $\alpha_k \sim 1/k$, so that $\sum \alpha_k = \infty$ but $\sum \alpha_k^2 < \infty$.
- Far from the neighbourhood the convergence can still be $O(1/k)$; the slowdown only occurs near the optimum.

### The Problem of Scales

Even for a trivial quadratic $f(\mathbf{w}) = \frac{1}{2} x^2 + \frac{\rho}{2} y^2$, gradient descent suffers when the coordinates have very different scales ($\rho \ll 1$). The learning rate cannot be increased beyond the limit set by the fastest‑changing coordinate (here $x$) without causing divergence, so progress along the slow axis ($y$) becomes excruciatingly slow. This motivates **adaptive** and **momentum‑based** methods.

---

## SGD Improvements *[2:01:16]*

### Momentum

Momentum draws on the physical intuition of a ball rolling down a slope – it accumulates velocity in directions where the gradient consistently points:

$$
\mathbf{u}_k = \gamma \mathbf{u}_{k-1} - \alpha \,\hat{\mathbf{g}}_k, \qquad
\mathbf{w}_{k+1} = \mathbf{w}_k + \mathbf{u}_k.
$$

Typically $\gamma \approx 0.95$–$0.99$. The method speeds up movement along shallow but consistent slopes and dampens oscillations across steep ravines.

### Nesterov Accelerated Gradient (NAG)

Nesterov (1983) proposed a “look‑ahead” variant: since we already know that the momentum will carry us to $\mathbf{w}_k + \gamma \mathbf{u}_{k-1}$, why not compute the gradient **there** instead of at the current point?

$$
\mathbf{u}_k = \gamma \mathbf{u}_{k-1} - \alpha \,\nabla L(\mathbf{w}_k + \gamma \mathbf{u}_{k-1}), \qquad
\mathbf{w}_{k+1} = \mathbf{w}_k + \mathbf{u}_k.
$$

This anticipates the upcoming slope and naturally slows down before hitting a wall, reducing oscillations even further. NAG often converges asymptotically faster than plain momentum.

### Adaptive Methods: Motivation

All previous methods treat every coordinate equally. In a high‑dimensional space different weights may need very different effective learning rates. **Adaptive** algorithms scale the learning rate per‑parameter based on the history of gradients.

#### Adagrad

Adagrad maintains a running sum of squared gradients per parameter:

$$
G_{k,i} = G_{k-1,i} + g_{k,i}^2, \qquad
w_{k+1,i} = w_{k,i} - \frac{\eta}{\sqrt{G_{k,i} + \epsilon}}\, g_{k,i}.
$$

Parameters that experienced large gradients see their effective learning rate shrink quickly; parameters with small gradients keep a higher rate. The drawback: $G_{k,i}$ only grows, so the learning rate can never rebound after passing through a steep region – it eventually becomes too small.

#### RMSprop

The fix is to replace the sum with an **exponential moving average**:

$$
G_{k,i} = \rho G_{k-1,i} + (1-\rho) g_{k,i}^2,
$$

and then update with $\displaystyle w_{k+1,i} = w_{k,i} - \frac{\eta}{\sqrt{G_{k,i} + \epsilon}}\, g_{k,i}$. This forgets old gradients and allows the learning rate to grow again when gradients become small. RMSprop was popularised by Hinton and is essentially Adagrad with an exponential moving average.

#### Adadelta

Adadelta adds a second idea: correcting the **units of measurement**. In plain SGD one subtracts a quantity with units of $\partial L/\partial w$ (velocity‑like) from $w$ (position‑like) – the dimensions do not match, which reflects the scale‑mismatch problem. Second‑order methods ($\mathbf{H}^{-1}\mathbf{g}$) have correct dimensions. Adadelta approximates this by keeping an exponential moving average of the squared parameter updates $\mathbb{E}[\Delta w^2]_t$ and scaling the gradient accordingly:

$$
w_{k+1,i} = w_{k,i} - \frac{\sqrt{\mathbb{E}[\Delta w^2]_{k-1} + \epsilon}}{\sqrt{G_{k,i} + \epsilon}}\, g_{k,i}.
$$

Adadelta removes the need to manually set a learning rate, but in practice it is less common than Adam.

### Adam

Adam (Kingma & Ba, 2014) combines the exponential moving average of **squared** gradients (like RMSprop) with an exponential moving average of the gradients **themselves** (like momentum with friction). The update for a single parameter weight $w_i$ is:

$$
m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t, \qquad
v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2,
$$

$$
w_{t+1,i} = w_{t,i} - \frac{\eta}{\sqrt{v_t + \epsilon}}\, m_t.
$$

Typical hyperparameters: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$. Adam is extremely robust – these default values work well across a wide range of problems, so it became the most popular optimisation algorithm in deep learning.

Smoothing the gradient itself (via $m_t$) significantly reduces the variance of the noisy mini‑batch estimates, which is a major reason for Adam’s good performance.

### AdamW: Fixing Weight Decay

In classical neural networks, **weight decay** was implemented by shrinking the weights before the gradient step:

$$
\mathbf{w}_{k+1} = (1 - \lambda)\mathbf{w}_k - \alpha \mathbf{g}_k.
$$

In vanilla SGD this is exactly equivalent to $L_2$ regularisation (just rearranging terms). However, with adaptive methods like Adam the equivalence breaks because the adaptively scaled update does not correspond to a simple $\lambda \mathbf{w}$ term in the loss. Without care, weights with large gradients decay less, leading to suboptimal regularisation.

**AdamW** (Loshchilov & Hutter, 2018) re‑introduces weight decay directly in the update, decoupling it from the adaptive scaling. The result is better generalisation and more interpretable hyperparameters. AdamW is now a standard choice alongside plain Adam.

### A Cautionary Tale: Super‑Convergence and AMSGrad

- **Super‑convergence** (Smith & Topin, 2017) proposed **cyclic learning rates** – periodically raising the learning rate after decaying it. Experiments showed dramatically faster convergence (10×–20×) while reaching similar final accuracy. Despite the initial excitement, cyclic schedules are not universally adopted; they can be unstable and are rarely used in practice today.
- **AMSGrad** (Reddi et al., 2018) identified a flaw in the original convergence proof of Adam and provided a counterexample where Adam can diverge. The fix replaces the exponential moving average $v_t$ with a **maximum** over past values. The resulting algorithm has a correct convergence proof and won the ICLR 2018 Best Paper award. Yet, after eight years, nobody actually uses it – empirically it performs no better than Adam and sometimes worse.

Both stories illustrate the same lesson: deep learning is an intensely empirical field. Even a theorem‑backed improvement does not guarantee adoption if it does not win on the practical benchmarks. Adam (and AdamW) remain the workhorses, while plain SGD with momentum is still a solid, widely used baseline.
