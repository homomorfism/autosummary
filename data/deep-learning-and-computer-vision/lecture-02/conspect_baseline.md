# Linear Models and Intro to Deep Learning *[00:11]*

## Bayesian Approach to Machine Learning *[00:11]*

The entire lecture builds on the Bayesian rule as the most important formula in machine learning.  
Given a hypothesis $\theta$ and evidence $D$, the posterior updates our prior beliefs:

$$p(\theta \mid D) = \frac{p(D \mid \theta)\,p(\theta)}{p(D)}.$$

- **Prior** $p(\theta)$ – what we believe before seeing data.
- **Likelihood** $p(D \mid \theta)$ – how probable the observed data is under a given hypothesis.
- **Posterior** $p(\theta \mid D)$ – our updated belief after seeing evidence.
- **Evidence (marginal likelihood)** $p(D)$ – a normalising constant.

Three optimisation problems follow from this identity:

1. **Maximum likelihood (ML):** $\theta_{\text{ML}} = \arg\max_{\theta} p(D\mid\theta)$ — purely frequentist, no prior.
2. **Maximum a posteriori (MAP):** $\theta_{\text{MAP}} = \arg\max_{\theta} p(\theta\mid D) \propto p(D\mid\theta)\,p(\theta)$ — incorporates a prior.
3. **Full posterior inference** and predictive distribution $p(x\mid D)$.

In deep learning practice, we almost always compose a loss function of the form  

$$-\bigl(\log p(D\mid\theta) + \log p(\theta)\bigr)$$  

and minimise it. The result is the MAP estimate $\theta_{\text{MAP}}$.  
**Key point:** $\theta_{\text{MAP}}$ is just a point estimate – the maximum of a whole distribution. The model’s uncertainty is captured by the full posterior, but for huge neural networks we are usually forced to settle for the point estimate.

### Probability as Degree of Belief *[00:21]*

Classical probability (frequency as limit of experiments) works for repeatable events, but in machine learning we often need to reason about unique events (Spain winning the 2026 World Cup, whether the Odyssey was written by a woman, AGI risk by 2030). Here probability functions as **degree of belief** – a representation of our uncertainty. Both interpretations follow the same mathematical rules.

> **Take‑away:** When we train a model we are not reaching a logical certainty; we are updating our beliefs. Even with vast data the result remains a distribution, and the best we get is a point estimate that should be interpreted cautiously.

### Bayesian Reasoning Examples *[00:36]*

Understanding which quantity is on which side of the conditioning bar is essential – many real‑world mistakes come from swapping them.

**1. Two children problem**  
A person has two children; each child is equally likely to be a boy or a girl independently.  

- *Question 1:* You ask “Do you have any boys?” and the answer is **yes**.  
  Sample space: BB, BG, GB, GG (all equal prior ¼). The answer eliminates GG, leaving three equally likely cases. Two of them contain a girl, so $P(\text{has a girl} \mid \text{has a boy}) = \frac{2}{3}$.  

- *Question 2:* You meet one of the children and it is a boy.  
  Now you have fixed one specific child, eliminating two cases (e.g., if the met child is the first, only BB and BG remain). $P(\text{other is girl}) = \frac{1}{2}$.  

This shows how the *nature* of the evidence changes the conditional probability even though both times you learn “there is a boy”.

**2. Blood type in a murder trial**  
A rare blood type (1 % prevalence) is found at the crime scene and the defendant also has it.  

- **Prosecutor’s fallacy:** “The chance of having this blood type if innocent is 1 %, therefore the defendant is guilty with probability 99 %.”  
  This equates $P(\text{blood type} \mid \text{innocent})$ with $P(\text{innocent} \mid \text{blood type})$ – a classic mistake.  
  The correct inference needs the prior probability of guilt, the base rate of the blood type, etc.  

- **Defence attorney’s error:** “A million people live in the city, so ≈10 000 have the same blood type; the evidence gives only a 0.01 % probability of guilt.”  
  The attorney implicitly assumes that among those 10 000 everyone is equally likely to be the killer, ignoring why the defendant is on trial.  

- **Real‑life case – O.J. Simpson.**  
  The defence argued that only 1 in 2500 women subjected to domestic violence is murdered, therefore domestic violence is irrelevant. This confuses $P(\text{murdered} \mid \text{history of violence})$ with the relevant $P(\text{husband is murderer} \mid \text{woman murdered AND history of violence})$. Using the same statistics, the correct estimate is around 7/8 – the husband is by far the most likely perpetrator. The court’s acceptance of the defence’s argument was a Bayesian mistake.

> **Habit:** Always ask yourself what is on the left and right of the conditioning bar – what exactly are you trying to estimate?

## Linear Regression *[02:29]*

A linear model assumes the target $y$ is a linear combination of input features:

$$y(\mathbf{x}, \mathbf{w}) = \mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x}),$$

where $\boldsymbol{\phi}(\mathbf{x})$ is a (possibly non‑linear) feature vector. By prepending a constant feature $\phi_0(\mathbf{x}) = 1$, the intercept is absorbed – a standard trick to keep formulas clean.

### From Likelihood to Least Squares

Given a training set $\{(\mathbf{x}_n, t_n)\}_{n=1}^N$, we want the “best” $\mathbf{w}$.  
The usual choice – minimising the **sum of squared errors (RSS)**  

$$\operatorname{RSS}(\mathbf{w}) = \sum_{n=1}^N \bigl(t_n - \mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x}_n)\bigr)^2$$

– is **not** arbitrary. It follows from a probabilistic model.

**Three assumptions (and a hidden fourth):**

1. The data points are conditionally independent given the parameters.
2. The centre of the noise distribution is the linear function itself: $\mathbb{E}[t_n] = \mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x}_n)$.
3. The noise is zero‑mean Gaussian with constant variance $\sigma^2$:
   $$p(t_n \mid \mathbf{x}_n, \mathbf{w}, \sigma^2) = \mathcal{N}\bigl(t_n \mid \mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x}_n),\; \sigma^2\bigr).$$
   The Gaussian is natural because of the **central limit theorem**: when many small, independent perturbations add up, the sum becomes approximately normal.
4. **Homoscedasticity** – the noise variance $\sigma^2$ is the same for all data points. This lets us pull $\sigma$ out of the sum. If the variance changes (data become more scattered in some region), the loss function must be modified – one reason to understand the assumptions.

**Maximum likelihood solution**  
The log‑likelihood is  

$$
\ln p(\mathbf{t}\mid\mathbf{X},\mathbf{w},\sigma^2) = -\frac{N}{2}\ln(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{n=1}^N \bigl(t_n - \mathbf{w}^\top\boldsymbol{\phi}_n\bigr)^2 .
$$

Maximising this w.r.t. $\mathbf{w}$ is equivalent to minimising the RSS – the square error directly reflects the Gaussian noise assumption.

### Polynomial Regression and Overfitting *[02:56]*

To illustrate, consider a one‑dimensional input $x$ and true function a sine wave.  
- **Degree 1** (straight line) under‑fits.  
- **Degree 3** already captures the sine’s single bump well.  
- **Degree 10** with only 11 points passes through every training point exactly (RSS = 0) but oscillates wildly between points – the classic picture of **overfitting**.  

In high dimensions overfitting arises naturally when you expand features.  
Going from $D$ original features to quadratic features gives $\approx D^2/2$ new features (cross‑terms $x_i x_j$). If $D=100$, you jump to ≈5000 features – many are irrelevant, but you don’t know which ones *a priori*, so you must include them all. Overfitting is then almost inevitable.

**Symptoms**  
- Validation / test error grows while training error stays tiny.  
- The coefficients explode (e.g., $\pm 50$ for a problem where $x,y$ are $\mathcal{O}(1)$).  

This explosion is a sign that the model is using unreasonable parameter values to exactly fit noise.  
Intuitively, in a high‑dimensional weight space the model has too much “variety”; constraining the weights toward zero reduces the effective complexity.

## Bayesian Regularization *[03:00]*

> **Regularization = placing a prior on the parameters.**  

We want $p(\mathbf{w})$, concentrated near zero, to express our prior belief that extremely large weights are unlikely. A natural choice is again a Gaussian:

$$p(\mathbf{w}) = \mathcal{N}(\mathbf{w} \mid \mathbf{0}, \tfrac{1}{\alpha}\mathbf{I}).$$

Adding the log‑prior to the log‑likelihood gives the MAP objective:

$$-\frac{1}{2\sigma^2}\sum_{n=1}^N(t_n - \mathbf{w}^\top\boldsymbol{\phi}_n)^2 \;-\; \frac{\alpha}{2}\mathbf{w}^\top\mathbf{w} + \text{const}.$$

This is exactly **ridge regression** (L2 regularization). The hyperparameter $\alpha$ trades off data fit against weight size.

- Adding an L2 regularizer does **not** change the model structure (the number of parameters stays the same); it “pulls” the solution toward the origin inside the fixed‑dimensional weight space.
- A different prior yields a different regularizer. Using a Laplace prior $p(w_j) \propto e^{-\alpha|w_j|}$ gives the **L1 (LASSO) regularizer** $\sum |w_j|$.  
  LASSO drives many coefficients exactly to zero, producing **sparse** models – useful when you want automatic feature selection from a large pool of candidates.

This probabilistic view explains why loss functions in any model (including deep neural networks) can be seen as derived from likelihood + prior. The “regularizer” is simply the part that does **not** depend on data.

> **Important distinction:** Regularization works **inside** a fixed model (fixed set of parameters); **model selection** (AIC, BIC, etc.) chooses between models of different complexity by approximating the evidence $p(D \mid \mathcal{M}_k)$. The two levels are separate.

## Classification and Logistic Regression *[02:04]*

### Why classification cannot use raw discrete outputs

A classifier that directly outputs class labels (e.g., 0/1 threshold) has zero gradient almost everywhere – it provides no learning signal for earlier layers. Moreover, we want a **probability distribution** over classes to express uncertainty.

### Binary classification and the logistic sigmoid

Model $p(C_1\mid\mathbf{x})$ in a way that allows a linear relationship somewhere.  
Start from Bayes’ theorem:

$$p(C_1\mid\mathbf{x}) = \frac{p(\mathbf{x}\mid C_1)\,p(C_1)}{p(\mathbf{x}\mid C_1)\,p(C_1) + p(\mathbf{x}\mid C_2)\,p(C_2)}.$$

Define the **odds** $p(C_1)/p(C_2)$ and then the **log‑odds (logit)**:

$$a = \ln\frac{p(\mathbf{x}\mid C_1)\,p(C_1)}{p(\mathbf{x}\mid C_2)\,p(C_2)}.$$

Now $a \in (-\infty,\infty)$ can naturally be modelled as a linear function $a = \mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})$.  
Inverting the transformation gives the **logistic sigmoid**:

$$p(C_1\mid\mathbf{x}) = \sigma(a) = \frac{1}{1 + e^{-a}}.$$

The function $\sigma$ is S‑shaped: it saturates at 0 and 1 and passes through 0.5 at $a=0$, providing a smooth interpolation that can be differentiated anywhere.

**Loss function** – For a dataset $\{(\boldsymbol{\phi}_n, t_n)\}$ with $t_n\in\{0,1\}$, the likelihood is

$$p(\mathbf{t}\mid\mathbf{w}) = \prod_{n=1}^N y_n^{\,t_n}(1-y_n)^{1-t_n},\qquad y_n = \sigma(\mathbf{w}^\top\boldsymbol{\phi}_n).$$

Taking negative log gives the **cross‑entropy** error:

$$E(\mathbf{w}) = -\sum_{n=1}^N \bigl[\,t_n\ln y_n + (1-t_n)\ln(1-y_n)\,\bigr].$$

Minimising this fits the logistic regression model; the optimum can be found by gradient descent.

### Multi‑class classification: softmax *[02:20]*

For $K$ classes, the natural generalisation uses a vector of **scores** $a_k = \mathbf{w}_k^\top\mathbf{x}$ and normalises with the **softmax function**:

$$p(C_k\mid\mathbf{x}) = \frac{e^{a_k}}{\sum_{j=1}^K e^{a_j}}.$$

- The name “softmax” reflects that it softly picks the maximum score – when one $a_k$ dominates, the output is nearly a one‑hot vector.
- The scores can be any real numbers; because of the exponential, adding a constant to all $a_k$ leaves the probabilities unchanged, so negative values are harmless.
- For a one‑hot target vector, the loss reduces to the negative log‑probability of the correct class.

### Connection to neural networks

In a deep neural network for classification, the main body extracts features $\mathbf{z}$ of dimension $D$. The **last layer** is often a linear transformation $\mathbf{W}\mathbf{z}$ (a $K\times D$ matrix) giving scores, followed by softmax to produce a probability vector. Thus the final stage is exactly logistic regression **on the learned features** – all previous layers are doing feature extraction for this linear classifier.  
For regression tasks, the last layer is analogously a linear layer (no softmax) on top of the extracted features.

## Introduction to Deep Learning *[02:33]*

### Biological Inspiration

The human brain contains roughly $10^{11}$ neurons, each making ≈7000 synaptic connections (≈ $10^{14}$–$10^{15}$ parameters).  
Computationally, a neuron:

- receives inputs through **dendrites** (thousands per neuron),
- integrates the inputs (via weighted connections at **synapses**),
- sends out a **spike** along the **axon** when sufficiently excited.

**Spikes** are all‑or‑nothing events; information is coded in the **firing rate** (10–200 Hz).  
This means the brain is a **massively parallel but shallow** computer: it can perform a huge number of operations simultaneously, yet a single “pass” through the whole visual system takes only 200–300 ms – just a few tens of sequential steps. Deep artificial networks mirror this: they are wide and use relatively few (hundreds, not thousands) of layer‑wise transformations.

**Neuroplasticity** – the brain adapts to completely new sensory modalities (e.g., seeing via a tongue electrode grid). This suggests a **single, general learning algorithm** at work. The same idea motivates neural networks: a large composition of simple, identical units can learn a vast variety of functions.

### History of Artificial Neural Networks

- **1943:** McCulloch & Pitts propose a mathematical model of a neuron as a weighted sum followed by a threshold – essentially the modern artificial neuron.
- **1948:** Alan Turing already sketches the idea of multilayer networks.
- **1958:** Rosenblatt builds the **Perceptron**, a single neuron trained by gradient descent. It could recognise letters and was hailed in the press as the first step to general AI.
- **1969:** Minsky & Papert show that a single perceptron cannot solve the XOR problem (classes not linearly separable).  
  *Critically, this only proves that* one *neuron is insufficient; a network of perceptrons can easily solve XOR. Yet the result contributed to the first “AI winter”.*
- **1970s–80s:** **Backpropagation** (chain rule through the network) is independently rediscovered multiple times, making it possible to train multilayer perceptrons. Deep networks appear in the 1980s (convolutional nets, recurrent nets).
- **1990s:** Neural networks fall out of favour again because they underperformed specialised models on small datasets and limited hardware. The slogan: “neural networks are the second best way of doing just about anything.”
- **2006:** Hinton’s group revives deep learning with unsupervised pretraining and **GPU acceleration**. GPUs provided a 10–20× speedup, moving computations from “not working” to “working”.
- **2010s:** Deep nets revolutionise speech recognition (Siri), computer vision (AlexNet, 2012), and NLP. By **2017** the **Transformer** architecture arrives, reshaping the whole field again.

### The Artificial Neuron and Deep Networks

The basic unit is an **artificial neuron**:

$$y = h\!\left(\sum_i w_i x_i\right) = h(\mathbf{w}^\top\mathbf{x}).$$

- **Weights** $\mathbf{w}$ are the learnable parameters.
- **Activation function** $h$ must be **non‑linear**; otherwise a composition of linear transforms remains linear and a deep network collapses to a single linear layer. Any non‑linearity suffices to achieve universal approximation.
- Typically neurons are arranged in **layers**; the output of one layer becomes the input to the next.

> **Connectionism:** A huge composition of extremely simple units yields an extraordinarily complex function – the core idea of deep learning.

The **key challenge** is training – finding all weights via gradient descent. This requires computing gradients through the whole computational graph, which is exactly what backpropagation does. We will study gradient descent variants and backpropagation in the next lecture.

### Gradient Descent (Preview) *[02:30]*

For complicated non‑convex functions, the only feasible optimisation method is **gradient descent**: repeatedly move a small step opposite to the gradient $\nabla_\mathbf{w} E(\mathbf{w})$.  
It finds a **local** minimum; there is never a guarantee of globality. Even for logistic regression, a closed‑form solution does not exist, so iterative gradient methods are mandatory – the same holds for all neural networks.
