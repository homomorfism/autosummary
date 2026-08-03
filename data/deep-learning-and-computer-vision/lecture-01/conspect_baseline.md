# INTRO TO MACHINE LEARNING

## AI Timelines and the Acceleration of Progress *[02:55]*

The field of artificial intelligence has a long history, but the recent pace of change is unprecedented.  
Until about 2022, AI looked like a regular scientific field with gradual, stepwise progress.  
The arrival of ChatGPT in late 2022, followed by the explosion of large language models (LLMs) in spring 2023, shattered that picture.  
On a single day—14 March 2023—Google announced LLM integration into its workspace, Anthropic unveiled its Claude models, and OpenAI announced GPT‑4.  
Three years ago it was still plausible that this was just a temporary breakthrough, but progress has not slowed; if anything, it is accelerating.  
Frontier labs now use their own models to improve their models, edging toward recursive self‑improvement.

How unexpected was this? A 2018 book surveyed prominent researchers about the timeline for human‑level AI.  
The most optimistic prediction, by Ray Kurzweil, was 2029; most placed it around 50 years away.  
We are living through a phase change that very few foresaw.

## Early Concepts of Artificial Intelligence *[12:29]*

The dream of creating artificial beings is ancient.  
Many religious traditions describe humans themselves as artificial intelligences fashioned by a deity from clay or other substances.  
Greek mythology includes Hephaestus’ android robots, most famously the giant bronze guardian Talos, who defended Crete by hurling rocks at enemy ships.  
The interesting lesson is that **throwing rocks with accuracy turned out to be much easier to automate than recognising enemy ships**—a quintessential computer vision problem that remains challenging.

Medieval and early‑modern automata, such as the programmable calligrapher and draftsman built by Pierre Jaquet‑Droz (18th century), were purely mechanical but showed early glimpses of programmability.  
The first real mathematical thinking about AI, however, started in the 20th century.

## The Turing Test *[21:11]*

Alan Turing’s 1950 essay *Computing Machinery and Intelligence* posed the question “Can machines think?” and introduced what we now call the **Turing test**.  
A human judge converses in writing with a human and a machine; the machine passes if the judge cannot reliably tell which is which.  
Crucially, the test is **probabilistic**: a single run is meaningless (the judge could just guess with 50 % success).  
The machine must make the judge’s recognition rate indistinguishable from random chance over repeated trials.

The Turing test has **survived the shifting goalposts** that plagued other AI milestones.  
When Deep Blue beat Kasparov at chess in 1997, the response was “chess doesn’t count—it’s just tree search.”  
When AlphaGo conquered Go, again the goalposts moved.  
But nobody ever dismissed the Turing test as trivial.  
Why? Because free‑form natural language conversation can cover *any* domain, including computer vision, 3D reasoning, and common sense.  
To predict the next token in a text—the core task of modern language models—a system must implicitly learn about the world, not just language.  
That is why LLMs continue to surprise us with emergent capabilities.

Formally, the Turing test was convincingly passed only in 2025, after a 75‑year reign.  
Turing’s original formulation was more subtle: the machine had to impersonate a woman while a man also tried to impersonate a woman, so that *every* participant had to pretend to be somebody else.

## The Dartmouth Workshop and the Birth of AI *[41:11]*

The positive, engineering‑oriented field of AI began in 1956 at the **Dartmouth Summer Research Project**, organised by John McCarthy, Marvin Minsky, Claude Shannon, and Nathaniel Rochester.  
The grant proposal was astonishingly ambitious:

> We propose a 2‑month study of artificial intelligence … The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can simulate it. We will attempt to find how to make machines use natural languages, form abstractions and concepts, solve problems now reserved for humans, and improve themselves.

They did not solve these problems in one summer, but the workshop established AI as a research field.  
Early successes included **Logic Theorist** (a theorem prover that re‑proved much of *Principia Mathematica*) and the **General Problem Solver**, fuelling high expectations.

## AI Winters and the Resurgence of Connectionism *[44:43]*

Optimism waned when projects such as machine translation failed to deliver.  
The 1970s became the **first AI winter**: funding dried up, and only a handful of researchers persisted, mostly on **expert systems** like MYCIN, which diagnosed blood infections using ~450 heuristic rules.  
The central challenge was combining rules that were fuzzy and overlapping; the field learned that pure logic was not enough.

In the 1980s, neural networks re‑emerged (convolutional nets, recurrent nets), but they were hamstrung by insufficient data and compute.  
The **deep learning revolution** ignited in the mid‑2000s when larger datasets (thanks to the internet), faster hardware, and the switch from CPUs to GPUs made training deep networks practical.  
Since then, neural methods have become the dominant paradigm across virtually all of machine learning.

## What is Machine Learning? *[52:31]*

A classical definition:

> A computer program **learns** with respect to a class of tasks $T$ and a performance measure $P$, if its performance on $T$, as measured by $P$, improves with experience.

While this seems almost tautological, it forces an essential point: **learning requires a numerical performance measure**—a *loss function*.  
Designing the right loss function is often half the battle in deep learning; minimising it should produce the behaviour you actually want.

## Key Machine Learning Tasks *[54:15]*

### Supervised Learning
Given a dataset of input‑output pairs $\{(x_i, y_i)\}$, learn the conditional distribution $p(y \mid x)$.  
Typical tasks:
- **Classification:** $y$ is a discrete label (e.g. cat vs dog).
- **Regression:** $y$ is a continuous value (e.g. temperature prediction).

The model must generalise beyond the training set, avoiding **overfitting**.  
Labelling data is often extremely expensive, especially for dense tasks like segmentation.

### Unsupervised Learning
No $y$ is provided; the dataset is just $\{x_i\}$.  
The goal is to find structure in $p(x)$ itself.  
Common forms:
- **Dimensionality reduction / representation learning:** Map a high‑dimensional input (e.g. a 1‑megapixel image $\approx 3\times10^6$ numbers) into a compact vector that preserves essential information.  
  A canonical deep‑learning approach is the **auto‑encoder**: an encoder compresses $x$ to a latent $z$, a decoder reconstructs $\hat{x}$ from $z$, and the loss is simply $\|\hat{x} - x\|^2$.  
  This forces $z$ to be a meaningful, low‑dimensional summary.
- **Clustering:** Partition data into groups so that within‑cluster similarity is high and between‑cluster similarity is low.  
  Clustering can be seen as the extreme of dimensionality reduction where the latent space is a finite set of labels.

### Reinforcement Learning
An agent interacts with an environment, receiving rewards, and learns a **policy** to maximise cumulative reward.  
No dataset exists upfront; the agent generates its own experience.  
Classic challenges include balancing exploration vs. exploitation and assigning credit to earlier actions when a reward arrives only at the end (credit assignment).  
Reinforcement learning is a separate world with its own techniques and will not be a focus of this course.

### Other Paradigms
- **Active learning:** the model chooses which data to label next.
- **Semi‑supervised learning:** part of the data is labelled.
- **Learning to rank:** produce an ordering (e.g. search results).
- **Bootstrapping:** a model improves itself using its own predictions.

## Probability Theory as the Bedrock of Machine Learning *[1:45:23]*

Machine learning, from its foundations to modern deep networks, is essentially applied probability theory.  
We will not need the heavy measure‑theoretic machinery (sigma‑algebras, Borel sets, etc.); only the core intuitions about random variables, densities, and basic rules.

### Basic Definitions
- **Discrete random variable:** probabilities of outcomes sum to $1$.
- **Continuous random variable:** characterised by a density $p(x) \ge 0$, $\int p(x) \, dx = 1$.
- **Joint probability:** $p(x, y)$ – the probability of two events occurring together.
- **Marginalisation:** $p(x) = \sum_y p(x, y)$ (or integral in the continuous case).
- **Conditional probability:** 
  $$p(x, y) = p(x \mid y)\, p(y) = p(y \mid x)\, p(x).$$
  Hence $p(x \mid y) = \frac{p(x, y)}{p(y)}$.
- **Bayes’ theorem:**
  $$p(y \mid x) = \frac{p(x \mid y)\, p(y)}{p(x)}.$$
- **Independence:** $x$ and $y$ are independent if $p(x, y) = p(x)\, p(y)$; then $p(y \mid x) = p(y)$.

The conditional probability $p(y \mid x)$ is the central object of supervised learning.

## Bayesian Inference: The Main Formula of Machine Learning *[1:57:11]*

In our new notation, let:
- $D$ = dataset (observed data),
- $\theta$ = model parameters (everything we want to learn – weights of a network, probability of heads, etc.).

Bayes’ theorem becomes

$$
p(\theta \mid D) = \frac{p(D \mid \theta)\, p(\theta)}{p(D)},
$$

or, since the denominator $p(D)$ does not depend on $\theta$,

$$
p(\theta \mid D) \propto p(D \mid \theta)\, p(\theta).
$$

- **Likelihood** $p(D \mid \theta)$: how probable the observed data is given a particular setting of the parameters.  
  This is the part that the model definition directly gives us.
- **Prior** $p(\theta)$: our belief about the parameters *before* seeing any data.
- **Posterior** $p(\theta \mid D)$: our updated belief after incorporating the data.
- **Evidence** $p(D) = \int p(D \mid \theta) p(\theta) \, d\theta$: a normalising constant that makes the posterior integrate to $1$.

Two common inference tasks:

1. **Maximum Likelihood (ML):** $\theta_{\text{ML}} = \arg\max_\theta p(D \mid \theta)$.
2. **Maximum a Posteriori (MAP):** $\theta_{\text{MAP}} = \arg\max_\theta p(\theta \mid D) = \arg\max_\theta p(D \mid \theta)\, p(\theta)$.

The denominator $p(D)$ is irrelevant for maximisation, so we usually work with the numerator only.

### Direct and Inverse Problems

- **Direct problem:** given a fully specified probabilistic model, compute the probability of some event (e.g. “an urn contains 10 balls, 3 black – what is the chance of drawing a black ball?”).
- **Inverse problem (typical in ML):** observe outcomes and infer the hidden parameters (e.g. “I drew a black ball; which urn did it come from?”).  
  Inverse problems naturally require Bayes’ rule.

### Probability as Frequency vs. Degree of Belief

Classical probability interprets $p$ as a limiting frequency in infinitely repeated experiments (tossing a coin many times).  
But many real‑world questions – “will Spain win the 2026 World Cup?”, “will AGI take over by 2030?” – concern **unique, unrepeatable events**.  
The Bayesian interpretation treats probabilities as **degrees of belief**, and it obeys the same mathematical rules.  
Both viewpoints are valid, but Bayesian reasoning is often more natural for the kinds of problems machine learning actually solves.

## Example: Bayesian Inference for a Biased Coin  *[2:05:15]*

### Problem setup
We toss a coin with unknown probability of heads $\theta = p(\text{heads})$.  
The data $D$ is a sequence of $n$ heads and $m$ tails.  
Assuming **conditional independence** given $\theta$ (once you know $\theta$, different tosses are independent), the likelihood is

$$
p(D \mid \theta) = \theta^{\,n} (1-\theta)^{\,m}.
$$

### Maximum likelihood
Maximising $p(D \mid \theta)$ with respect to $\theta$ (derivative, set to zero) yields

$$
\theta_{\text{ML}} = \frac{n}{n+m}.
$$

This is the intuitive “number of heads divided by total tosses”.  
For large $n+m$, it converges to the true $\theta$.

### The problem with scarce data
Suppose we have tossed the coin only **once** and got tails.  
Then $p(D \mid \theta) = 1-\theta$, which has no interior maximum; $\theta_{\text{ML}}$ would be $-\infty$ unless we constrain $\theta \in [0,1]$.  
With the constraint, $\theta_{\text{ML}} = 0$.  
This would imply that the coin will *always* land tails – an absurd conclusion after a single trial.  
The mathematics is correct; what is missing is our **prior belief** about the coin.

### Adding a prior
A prior is a distribution over $\theta$ that reflects what we believed before any data.  
If we have no strong opinion, we might use a **uniform prior** $p(\theta) = 1$ on $[0,1]$.  
Then the posterior (up to normalisation) is $p(\theta \mid D) \propto (1-\theta)$.  
After normalising, $p(\theta \mid D) = 2(1-\theta)$ for $\theta \in [0,1]$.  
The **MAP estimate** is still $0$, because the prior is flat and does not shift the maximum.  
However, a crucial difference appears when we move from parameter estimates to **predictions**.

## The Predictive Distribution and Laplace’s Rule *[2:48:15]*

The ultimate goal of learning is not the parameters $\theta$ themselves, but making **predictions** about future data.  
For a new coin toss, we want $p(\text{heads} \mid D)$.  
This is computed by **averaging the likelihood over the posterior**:

$$
p(\text{heads} \mid D) = \int_0^1 p(\text{heads} \mid \theta)\, p(\theta \mid D)\, d\theta
= \int_0^1 \theta \; p(\theta \mid D)\, d\theta.
$$

With the uniform prior and $D$ consisting of a single tail, this integral gives $\frac{1}{3}$, not $0$.  
More generally, after $n$ heads and $m$ tails under a uniform prior, one obtains

$$
p(\text{heads} \mid D) = \frac{n+1}{n+m+2},
$$

known as **Laplace’s rule of succession**.  
This formula is less extreme than the ML estimate when data is scarce, and both converge as the number of observations grows.

Thus, full Bayesian inference – keeping the entire posterior distribution and averaging over it – yields **smoothed, more cautious predictions** that automatically account for uncertainty in the parameters.

## Conjugate Priors: Convenience Meets Intuition *[3:06:00]*

For a real coin, our intuition is not a uniform prior; we expect it to be approximately fair (a bell‑shaped curve around $0.5$).  
If we used a truncated normal distribution, the posterior would be a product of an exponential and a polynomial – messy to work with analytically.  
The key idea is to **choose a prior whose functional form looks like the likelihood**, so that multiplication is easy and the posterior stays in the same family.  
Such priors are called **conjugate priors**.

For Bernoulli trials (coin tosses), the conjugate family is the **Beta distribution**:

$$
p(\theta \mid \alpha, \beta) = \frac{\theta^{\,\alpha-1} (1-\theta)^{\,\beta-1}}{B(\alpha,\beta)},
\qquad \theta \in [0,1].
$$

- $\alpha$ and $\beta$ are *hyperparameters* that encode our prior belief.  
  - $\alpha = 1, \beta = 1$ gives the uniform distribution.  
  - Larger equal values (e.g. $\alpha = \beta = 10$) produce a peak at $\theta = 0.5$, reflecting strong belief in fairness.

If we then observe $n$ heads and $m$ tails, the posterior is also a Beta:

$$
p(\theta \mid D) = \operatorname{Beta}(\theta \mid \alpha + n,\, \beta + m).
$$

The update rule is simply **add the counts** to the hyperparameters.

This makes Bayesian updating trivially easy:  
- Start with prior $\operatorname{Beta}(\alpha, \beta)$.  
- After seeing data, the posterior becomes $\operatorname{Beta}(\alpha + n, \beta + m)$.  
- To incorporate further data $D'$, just use this posterior as the new prior and add the new counts.

Moreover, the conjugate prior framework naturally connects to **regularisation** in loss functions:  
taking logs, $\log p(\theta \mid D) = \log p(D \mid \theta) + \log p(\theta) + \text{const}$.  
The log‑prior acts as a regulariser on the parameters.

### Extension: Multinomial and Dirichlet
If we have $k$ categories instead of two (a multinomial distribution with parameters $\theta_1, \dots, \theta_k$), the conjugate prior is the **Dirichlet distribution**:

$$
p(\theta \mid \alpha) \propto \theta_1^{\alpha_1-1} \theta_2^{\alpha_2-1} \cdots \theta_k^{\alpha_k-1}.
$$

The update is again simple: $p(\theta \mid x, \alpha) = \operatorname{Dirichlet}(\theta \mid \alpha_1 + x_1, \dots, \alpha_k + x_k)$.

## Summary *[3:18:44]*

- Machine learning is, at its core, probabilistic inference: we update our beliefs about model parameters $\theta$ given data $D$ using **Bayes’ theorem**.
- The main objects are the **likelihood** $p(D \mid \theta)$ (the model), the **prior** $p(\theta)$ (our initial belief), and the **posterior** $p(\theta \mid D)$ (the updated belief).
- The two standard point estimates are **maximum likelihood** ($\theta_{\text{ML}}$) and **maximum a posteriori** ($\theta_{\text{MAP}}$).
- In practice we rarely have infinite data, so the prior matters.  
  The rational way to make predictions is to **average over the posterior**, yielding the **predictive distribution** $p(x \mid D) = \int p(x \mid \theta) p(\theta \mid D) d\theta$.
- Choosing a prior from a **conjugate family** (like Beta for a coin, Dirichlet for multinomial) makes computation trivial: the posterior has the same form as the prior, with hyperparameters updated by simple addition.
- These ideas are the foundation of all machine learning; even when we later train neural networks with gradient descent, the loss functions we minimise are essentially negative log‑posteriors, and regularisation terms are implicit priors.
