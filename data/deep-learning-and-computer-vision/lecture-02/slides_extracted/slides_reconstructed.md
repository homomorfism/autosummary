# Linear Models and Intro to Deep Learning

## Bayesian Approach to Machine Learning

### Basic Probability Definitions

The discussion assumes familiarity with discrete random variables (probabilities summing to one) and continuous random variables (nonnegative density integrating to one). Formal measure-theoretic concepts (sigma-algebras, Borel sets, etc.) are not required.

- **Joint probability** – probability of two events occurring simultaneously: \(p(x, y)\).
- **Marginalization:** \(p(x) = \sum_y p(x, y)\).
- **Conditional probability** – probability of one event given another occurred: \(p(x\mid y)\).  
  The chain rule: \(p(x, y) = p(x\mid y)\,p(y) = p(y\mid x)\,p(x)\).
- **Bayes’ theorem:**  
  \[
  p(y\mid x) = \frac{p(x\mid y)\,p(y)}{p(x)} 
              = \frac{p(x\mid y)\,p(y)}{\sum_{y'} p(x\mid y')\,p(y')}.
  \]
- **Independence:** \(x\) and \(y\) are independent if \(p(x,y)=p(x)\,p(y)\).

> **Bayes’ theorem for parameters and data:**  
> \[
> p(\theta\mid D) = \frac{p(\theta)\,p(D\mid\theta)}{p(D)},
> \]
> where  
> * \(p(\theta)\) – prior probability,  
> * \(p(D\mid\theta)\) – likelihood,  
> * \(p(\theta\mid D)\) – posterior probability,  
> * \(p(D) = \int p(D\mid\theta)\,p(\theta)\,d\theta\) – evidence (marginal likelihood).

**Maximum Likelihood vs. Maximum a Posteriori**

- Maximum likelihood (ML) hypothesis: \(\theta_{\text{ML}} = \arg\max_\theta p(D\mid\theta)\).
- Bayesian approaches work with the full posterior \(p(\theta\mid D) \propto p(D\mid\theta)\,p(\theta)\) and often extract the maximum a posteriori (MAP) hypothesis:  
  \(\theta_{\text{MAP}} = \arg\max_\theta p(\theta\mid D) = \arg\max_\theta p(D\mid\theta)\,p(\theta)\).

### Direct and Inverse Problems

- **Direct problem (prediction):** given a probabilistic model, compute a specific probability.  
  *Example:* an urn contains 10 balls, 3 black; what is the probability of drawing a black ball? Or 10 balls numbered 1–10; what is the probability that the sum of three consecutively drawn balls equals 12?
- **Inverse problem (inference):** hidden variables must be inferred from observed behaviour.  
  *Example:* two urns each have 10 balls; one has 3 black, the other 6. A ball drawn from one urn is black. What is the probability it came from the first urn?  
  Such problems naturally lead to Bayesian reasoning, though they can be rephrased through frequencies.

Machine learning problems are predominantly of the inverse type: building probabilistic models from observations.

### Frequentist vs. Bayesian Interpretations of Probability

- **Classical (frequentist) view:** probability is the limiting frequency of an outcome in an infinite sequence of identical trials (e.g., tossing a coin).
- **Bayesian view:** probability quantifies a *degree of belief*. This applies to unique, non-repeatable events:  
  * Spain winning the FIFA World Cup in 2026  
  * the *Odyssey* having been written by a woman  
  * AGI taking control by 2030  

  Here “repeated experiments” are meaningless; there is exactly one experiment.

In the Bayesian interpretation (as originally envisioned by Thomas Bayes), probabilities become subjective beliefs. Both interpretations follow the same mathematical laws; Cox’s theorem shows that natural axioms of plausible reasoning lead to a very restricted class of functions.

### Examples

1. **Two children** – assume each child is boy or girl independently with equal probability \(\frac12\).  
   (a) After asking whether the person has any boys, he answers “yes”. What is the probability he has a girl?  
   (b) I meet one of his children, and it is a boy. What is the probability the other is a girl?

2. **Murder trial** – blood at the scene matches the defendant’s rare blood type (population frequency 1%).  
   (1) Prosecutor: “The chance the defendant would have this blood type if innocent is 1%, therefore he is guilty with probability 99%.” What is the mistake?  
   (2) Defence attorney: “A million people live in the city, so about 10 000 share the blood type. The blood evidence gives only a 0.01% probability of guilt – that is no proof.” What is the attorney’s mistake?

3. **Real cases**  
   - O.J. Simpson: the prosecutor cited a history of domestic violence. The defence argued that only 1 out of 2500 women subject to domestic violence is killed, so it is irrelevant. The court agreed; is this correct inference?  
   - Sally Clark: two babies died of SIDS; the prosecutor calculated the combined probability of two SIDS deaths (from the single-case statistic) to be about 1 in 73 million. Is this reasoning correct?

---

## Linear Regression

### Least Squares and Maximum Likelihood

**Linear model:**  
\[
y(\mathbf{x},\mathbf{w}) = w_0 + \sum_{j=1}^p x_j w_j = \mathbf{x}^\top \mathbf{w},
\qquad \mathbf{x} = (1, x_1, \dots, x_p).
\]

Given training data \(\{(\mathbf{x}_i, y_i)\}_{i=1}^N\), we find optimal parameters \(\hat{\mathbf{w}}\) by minimising the **residual sum of squares** (least squares):
\[
\text{RSS}(\mathbf{w}) = \sum_{i=1}^N \bigl(y_i - \mathbf{x}_i^\top \mathbf{w}\bigr)^2.
\]
An exact closed-form solution exists, but the derivation via probability is more instructive.

**Noise assumption:** The observed target \(t\) is the model output plus Gaussian noise:  
\[
t = y(\mathbf{x},\mathbf{w}) + \epsilon,\quad \epsilon \sim \mathcal{N}(0,\sigma^2),
\]
so that
\[
p(t\mid\mathbf{x},\mathbf{w},\sigma^2) = \mathcal{N}\bigl(t\mid y(\mathbf{x},\mathbf{w}), \sigma^2\bigr).
\]

*Aside – normal distribution:*
\[
p(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).
\]

**Maximum likelihood estimation.** Assume the data are i.i.d.:
\[
p(\mathbf{t}\mid X,\mathbf{w},\sigma^2) = \prod_{n=1}^N \mathcal{N}\bigl(t_n\mid \mathbf{w}^\top\phi(\mathbf{x}_n), \sigma^2\bigr).
\]
Taking the logarithm,
\[
\ln p(\mathbf{t}\mid\mathbf{w},\sigma^2)
= -\frac{N}{2}\ln(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{n=1}^N \bigl(t_n - \mathbf{w}^\top\phi(\mathbf{x}_n)\bigr)^2.
\]

Maximising this w.r.t. \(\mathbf{w}\) is equivalent to minimising the sum of squared errors. The gradient is:
\[
\nabla_{\mathbf{w}} \ln p(\mathbf{t}\mid\mathbf{w},\sigma^2)
= \frac{1}{\sigma^2} \sum_{n=1}^N \bigl(t_n - \mathbf{w}^\top\phi(\mathbf{x}_n)\bigr)\,\phi(\mathbf{x}_n).
\]

One can also obtain a full posterior distribution by introducing a prior (also normal) and then compute the predictive distribution \(p(y\mid\mathbf{x},\mathcal{D}) = \int p(y\mid\mathbf{x},\mathbf{w})\,p(\mathbf{w}\mid\mathcal{D})\,d\mathbf{w}\).

**Key conclusion:** In many regression problems, minimising the sum of squared deviations is the natural choice because it corresponds to assuming normally distributed noise.

---

## Bayesian Regularization

### Ridge Regression as MAP Estimation

Bayesian inference proceeds by:
1. Finding the posterior \(p(\theta\mid D) \propto p(D\mid\theta)\,p(\theta)\) (or the MAP hypothesis \(\arg\max_\theta p(\theta\mid D)\)).
2. Finding the predictive distribution \(p(x\mid D) \propto \int p(x\mid\theta)\,p(D\mid\theta)\,p(\theta)\,d\theta\).

Introduce a prior on the weights; e.g., a normal distribution:
\[
p(\mathbf{w}) = \mathcal{N}(\mathbf{w}\mid \boldsymbol{\mu}_0, \boldsymbol{\Sigma}_0).
\]

Again assume i.i.d. normal likelihood:
\[
p(\mathbf{t}\mid X,\mathbf{w},\sigma^2) = \prod_{n=1}^N \mathcal{N}\bigl(t_n\mid \mathbf{w}^\top\phi(\mathbf{x}_n), \sigma^2\bigr).
\]

The posterior is proportional to
\[
p(\mathbf{w}\mid\mathbf{t}) \propto \mathcal{N}(\mathbf{w}\mid \boldsymbol{\mu}_0, \boldsymbol{\Sigma}_0)
   \prod_{n=1}^N \mathcal{N}\bigl(t_n\mid \mathbf{w}^\top\phi(\mathbf{x}_n), \sigma^2\bigr).
\]

Computing the product yields a Gaussian posterior:
\[
p(\mathbf{w}\mid\mathbf{t}) = \mathcal{N}(\mathbf{w}\mid \boldsymbol{\mu}_N, \boldsymbol{\Sigma}_N),
\]
where
\[
\boldsymbol{\mu}_N = \boldsymbol{\Sigma}_N\Bigl(\boldsymbol{\Sigma}_0^{-1}\boldsymbol{\mu}_0
   + \frac{1}{\sigma^2}\Phi^\top \mathbf{t}\Bigr),\qquad
\boldsymbol{\Sigma}_N = \Bigl(\boldsymbol{\Sigma}_0^{-1}
   + \frac{1}{\sigma^2}\Phi^\top\Phi\Bigr)^{-1},
\]
and \(\Phi\) is the design matrix with rows \(\phi(\mathbf{x}_n)^\top\).

If the prior is zero‑mean isotropic,
\[
p(\mathbf{w}) = \mathcal{N}\!\left(\mathbf{w}\mid 0, \tfrac{1}{\alpha}I\right),
\]
the log‑posterior becomes
\[
\ln p(\mathbf{w}\mid\mathbf{t}) = 
-\frac{1}{2\sigma^2}\sum_{n=1}^N \bigl(t_n - \mathbf{w}^\top\phi(\mathbf{x}_n)\bigr)^2
- \frac{\alpha}{2}\mathbf{w}^\top\mathbf{w} + \text{const}.
\]
This is precisely the **ridge regression** objective: penalised least squares with an \(\ell_2\) regulariser. Thus, ridge regression is the MAP estimate under a Gaussian prior. Examples are shown in the figures.

### Generalization to \(\ell_q\) Priors

A more general prior can be chosen:
\[
p(\mathbf{w}\mid\alpha) = 
\left[\frac{q}{2}\left(\frac{\alpha}{2}\right)^{1/q} \frac{1}{\Gamma(1/q)}\right]^M
\exp\!\left(-\frac{\alpha}{2} \sum_{j=1}^M |w_j|^q\right).
\]
The resulting log‑posterior contains a regulariser proportional to \(\|\mathbf{w}\|_q^q\) (exercise: derive the MAP objective). This subsumes ridge (\(q=2\)) and Laplace (LASSO, \(q=1\)) priors.

---

## Classification

### Logistic Regression and Softmax

In a classification problem we assign an input \(\mathbf{x}\) to one of \(K\) classes \(C_k\).

- Assume each class has a density \(p(\mathbf{x}\mid C_k)\) and a prior \(p(C_k)\).
- Bayes’ theorem gives the posterior \(p(C_k\mid\mathbf{x})\).

For two classes:
\[
p(C_1\mid\mathbf{x}) = 
\frac{p(\mathbf{x}\mid C_1)\,p(C_1)}
     {p(\mathbf{x}\mid C_1)\,p(C_1) + p(\mathbf{x}\mid C_2)\,p(C_2)}
   = \frac{1}{1 + e^{-a}} = \sigma(a),
\]
where
\[
a = \ln\frac{p(\mathbf{x}\mid C_1)\,p(C_1)}{p(\mathbf{x}\mid C_2)\,p(C_2)},
\qquad
\sigma(a) = \frac{1}{1+e^{-a}}.
\]

- \(\sigma(a)\) is the **logistic sigmoid**; \(\sigma(-a)=1-\sigma(a)\).
- The inverse is the **logit** function: \(a = \ln\bigl(\frac{\sigma}{1-\sigma}\bigr)\).

**Logistic regression** models the decision boundary directly:
\[
y_n = p(C_1\mid\phi_n) = \sigma(\mathbf{w}^\top\phi_n).
\]

For a dataset \(\{\phi_n, t_n\}\), \(t_n\in\{0,1\}\), the likelihood is
\[
p(\mathbf{t}\mid\mathbf{w}) = \prod_{n=1}^N y_n^{t_n} (1-y_n)^{1-t_n}.
\]

The negative log‑likelihood gives the **cross‑entropy** error function:
\[
E(\mathbf{w}) = -\ln p(\mathbf{t}\mid\mathbf{w}) 
= - \sum_{n=1}^N \bigl[ t_n \ln y_n + (1-t_n)\ln(1-y_n) \bigr].
\]

Minimising this yields a sigmoid that optimally separates the data and even attempts to model probabilities.

**Multiple classes:**  
\[
p(C_k\mid\mathbf{x}) = \frac{p(\mathbf{x}\mid C_k)\,p(C_k)}
   {\sum_j p(\mathbf{x}\mid C_j)\,p(C_j)}
   = \frac{e^{a_k}}{\sum_j e^{a_j}},
\quad a_k = \ln p(\mathbf{x}\mid C_k)\,p(C_k).
\]
The function \(\frac{e^{a_k}}{\sum_j e^{a_j}}\) is the **softmax** (normalized exponential).

**Conclusion:** For classification it makes sense to minimise the cross‑entropy (with softmax outputs) rather than the raw classification error, which is problematic.

---

## Gradient Descent

Gradient descent is the fundamental method for optimising complicated, non‑convex functions.

- Update rule: \(\mathbf{w}^{(\tau+1)} = \mathbf{w}^{(\tau)} - \eta \nabla E(\mathbf{w})\).

For logistic regression we minimise
\[
E(\mathbf{w}) = -\sum_{n=1}^N \bigl[ t_n \ln y_n + (1-t_n)\ln(1-y_n) \bigr],
\qquad y_n = \sigma(\mathbf{w}^\top\phi_n).
\]
Using \(\sigma'(a) = \sigma(a)(1-\sigma(a))\), the gradient is
\[
\nabla E(\mathbf{w}) = \sum_{n=1}^N (y_n - t_n)\,\phi_n.
\]

Gradient descent proceeds by iterative updates in the direction opposite the gradient.

- Gradient descent is a **local** optimisation procedure; no global convergence guarantees exist.
- All improvements discussed in the sequel will be local – global guarantees are not available with these methods.

---

## The Brain and the History of Artificial Neural Networks

### Human Brain as a Parallel Computer

- The human brain contains \(\sim 10^{11}\) neurons, each with about \(7\,000\) synapses, leading to \(10^{14}\)–\(10^{15}\) connections.
- **Neuron structure:** dendrites receive signals; the axon transmits spikes; synapses connect one neuron’s axon to other neurons’ dendrites.
- Neurons produce spikes stochastically, with firing rates of only 10–200 Hz.
- Yet we can recognise a face in a few hundred milliseconds, implying that sequential computations are very short. The brain achieves this by massive parallelism.
- Visual processing follows a hierarchical pathway (see figure).

### Feature Learning and Plasticity

- Traditional systems for unstructured data rely on hand‑crafted features: input → features → classifier.  
  *Examples:* MFCC for speech, SIFT for images.
- **Feature learning** asks: can we learn good features automatically? The brain succeeds at learning from very small data samples and can adapt to new data sources.
- **Neuroplasticity** suggests a single learning algorithm (the “Master Algorithm”) might be at work across very different sensory modalities.

### The Mathematical Essence of Neural Networks

Machine learning is essentially function approximation and optimisation. For example:
- A function from an image’s pixels to “cat or not” is extremely complicated.
- It is defined only at the points provided by a dataset.

The common approach:
1. Construct a parametric class of models (functions).
2. Tune the parameters to fit the data well, i.e., optimise a chosen error function or quality metric.

**Neural networks** are universal approximators – a very wide and flexible parametric class. The challenge is how to train them effectively.

### Historical Development of Artificial Neural Networks

- Early ideas: modelling neurons with simple functions (McCulloch & Pitts, 1943). Artificial neural networks with multiple layers were proposed by Turing (1948).
- **Perceptron** (Rosenblatt, 1958): a single artificial neuron implementing a linear separating surface.  
  A single neuron combines inputs linearly and passes the result through a nonlinear activation function:
  \[
  y = h(\mathbf{w}^\top\mathbf{x}) = h\!\left(\sum_i w_i x_i\right).
  \]
- Training the original Rosenblatt perceptron (\(h\) = identity):
  \[
  E_P(\mathbf{w}) = -\sum_{\mathbf{x}\in\mathcal{M}} y(\mathbf{x})\,(\mathbf{w}^\top\mathbf{x}),\qquad
  \mathbf{w}^{(\tau+1)} = \mathbf{w}^{(\tau)} - \eta \nabla E_P(\mathbf{w}) = \mathbf{w}^{(\tau)} + \eta\, t_n \mathbf{x}_n.
  \]
- For binary classification one can also use the logistic sigmoid activation, yielding the cross‑entropy error as above – essentially logistic regression.

The first perceptron learned to recognise letters (see figure) and was hailed as a major success.

- **Minsky’s critique:** even with a nonlinearity, a single perceptron can only produce a linear separating surface. This necessitates a network of perceptrons.
- 1960s: Minsky & Papert (1969) showed that XOR cannot be modelled by a perceptron – a fact that was regarded as a serious obstacle.
- **Backpropagation** was invented by Brison & Hoback (1969) and rediscovered by Hinton (1974), who popularised it.
- Multilayer ANNs essentially in their modern form appeared in the late 1970s; deep models existed in the early 1980s. The idea of depth is old.
- By the early 1990s, neural networks failed to live up to the hype (partly for technical reasons). John Denker (1994): “Neural networks are the second best way of doing just about anything.”
- In the 1990s, neural networks were largely forgotten, except for image processing (Yann LeCun) and a few groups (Geoffrey Hinton, Yoshua Bengio).
- **Deep learning revolution (2006):** Hinton’s group trained Deep Belief Networks (DBNs) using unsupervised pretraining. Additional enablers: more powerful computers, GPU computations, much larger datasets, and new regularisation/optimisation techniques. Pretraining later became unnecessary. Together with architectural innovations, these are the key ingredients of the deep learning revolution.

### Real Neurons and Hebbian Learning

- Real neurons most likely do not perform gradient descent (backpropagation would be difficult to implement biologically).
- **Hebbian learning:** increase the weight between neurons that fire together: \(\Delta w_i = \eta\, x_i x_j\). This principle led to Hopfield networks for associative memory.
- Current research focuses on spike‑timing‑dependent plasticity, where the weight change depends on the precise temporal relationship between spikes.

### Combining Perceptrons into Networks

- A network (multilayer perceptron) connects perceptrons so that outputs of one layer become inputs to the next.
- Hornik (1990): a two‑layer neural network can approximate any function (universal approximation theorem). In practice, deep networks exploit distributed representations and are significantly more expressive (see figure).
- Networks are typically organised in layers, which naturally suggests easy parallelisation.
- Thus, we approximate a very complicated function by a large composition of simple functions.
- **Training:** the standard answer is gradient descent, but there are complications that will be addressed later.
