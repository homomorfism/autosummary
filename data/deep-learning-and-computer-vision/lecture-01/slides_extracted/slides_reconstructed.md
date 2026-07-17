# Intro to Machine Learning

## Historical Background

### AI Timelines
We live in some very interesting times... And nobody predicted this (a book from 2018 illustrates the point). Let’s start from the beginning.

### Early Thoughts on Artificial Intelligence
- Hephaestus created android robots for himself, such as the giant humanoid robot Talos.
- Pygmalion brought Galatea to life.
- Jehovah and Allah—pieces of clay.
- Some particularly wise rabbis could create golems.
- Albertus Magnus crafted an artificial speaking head (greatly upsetting Thomas Aquinas).

### Mechanical Automata
Early automata were quite inventive: al-Jazari (12th century), Robert II d’Artois’ Hesdin Castle, Leonardo da Vinci’s mechanical knight... Automata by Jaquet-Droz (XVIII century) were also remarkable.

But these were purely mechanical; mathematical/logical AI remained rudimentary for a long time. A notable early attempt is the logical machine by Ramon Llull (late XIII–early XIV century).

Starting from Dr. Frankenstein, AI consistently appears in literature.

### The Turing Test
AI as a science began with the Turing test (1950). A computer should successfully impersonate a human in a (written) dialogue between a judge, a human, and a computer. Actually, the original formulation was somewhat subtler and more interesting...

It is already obvious how much is required to build AI:
- natural language processing;
- knowledge representation;
- reasoning from acquired knowledge;
- learning from experience (machine learning itself).

By the way, it required special efforts to try the Turing test with modern LLMs, so officially it was passed only very recently (Jones, Bergen, Mar 31, 2025).

### The Dartmouth Workshop and the Birth of AI
AI as a field emerged in 1956 at the Dartmouth workshop. It was organized by John McCarthy, Marvin Minsky, Claude Shannon, and Nathaniel Rochester. Probably the most ambitious grant proposal in computing history.

> We propose a 2-month study of artificial intelligence to be carried out by 10 people in the summer of 1956 at Dartmouth College in Hanover, New Hampshire.
> The study is based on the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can simulate it. We will attempt to find how to make machines use natural languages, form abstractions and concepts, solve problems now reserved for humans, and improve themselves. We think significant advancement in one or more of these problems is possible if a carefully selected group of scientists works on it for a summer.

### 1956–1960: High Expectations
Optimistic times. It seemed that just a bit more, just a little bit...
- Allen Newell, Herbert Simon: **Logic Theorist**. Successfully re‑proved most of *Principia Mathematica*, sometimes even more elegantly than Russell and Whitehead themselves.
- **General Problem Solver** – a program trying to think like a human.
- Many specialized programs performing limited tasks (microworlds):
  - *Analogy* (IQ tests for “pick the odd one out”);
  - *Student* (algebraic word problems);
  - *Blocks World* (manipulating 3D blocks).

### 1970s: Knowledge‑Based Systems
Core idea: accumulate a sufficiently large set of rules and domain knowledge, then draw conclusions.

First success: **MYCIN** – blood infection diagnosis:
- about 450 rules;
- performed as well as experienced physicians and significantly better than novices.

### 1980s: Commercial Applications; AI Industry
The first AI department was at DEC (Digital Equipment Corporation); reportedly saving DEC about $10 million annually by 1986.

The boom ended by the late 80s as many companies failed to meet overly high expectations.

### 1990–2010: Data Mining, Machine Learning
In recent decades, the main focus shifted to machine learning and discovering patterns in data, especially with the development of the Internet. Next we got to the deep learning revolution, and recently to the LLM revolution… but that is a very different story.

## What is Machine Learning?

> A computer program **learns** with accumulating experience regarding a class of tasks $T$ and a performance measure $P$, if its performance on these tasks (according to $P$) improves as it gains new experience.

This definition is very (too?) general. What specific examples can we provide?

We will consider various algorithms solving specific tasks, performing better with more initial (test) data. Today we’ll discuss the general theory of Bayesian inference, usually applicable to any machine learning algorithm. But first—a brief overview of basic ML tasks.

## Key ML Tasks and Concepts

### Supervised Learning
- Learning with a set of labeled examples.
- **Training set**: a set of examples, each consisting of features (attributes); examples have correct answers – a **response** variable we want to predict; it can be categorical, continuous, or ordinal.
- A model learns from this dataset (training phase, learning phase), then it can be applied to new examples (test set).
- Main goal – train a model that not only fits training data but also **generalizes** well to new data; otherwise – **overfitting**.
- Usually, we are given only the training set – how to check model generalization? **Cross‑validation** – splitting data into training and validation sets.
- Typically, **preprocessing** is performed before inputting data, extracting the most informative aspects (**feature extraction**).
- Two main supervised tasks:
  - **Classification**: there is a discrete set of categories (classes), and new examples must be assigned to a class. Examples: text classification by topics, spam filtering; face/object/text recognition.
  - **Regression**: there is an unknown function whose values we must predict for new examples. Examples: engineering applications (predicting temperature, robot position, etc.); finance – predicting stock prices; same plus temporal changes – e.g., speech recognition.

### Unsupervised Learning
- Learning without labeled data, only raw data.
- **Clustering**: partitioning data into unknown classes based on similarity. Examples: identifying gene families from nucleotide sequences; user clustering and personalization; clustering mass spectrometry images into segments with different compositions.
- **Dimensionality reduction**: data has huge dimensionality (many features), and we need to reduce it by selecting the most informative features so algorithms can run effectively.
- **Matrix completion**: given a sparse matrix, predict missing values.
- Often some data has labeled examples – **semi‑supervised learning**.

### Reinforcement Learning
- Learning where an agent learns from its own trials and errors.
- **Multi‑armed bandits**: choosing from several actions, each leading to random outcomes; goal is to maximize rewards.
- **Exploration vs. exploitation**: deciding when to explore new options versus exploiting known ones.
- **Credit assignment**: reward is given at the end (winning a game), and we must assign credit to each action leading to success.

### Other Learning Paradigms
- **Active learning** – choosing the next (relatively expensive) test.
- **Learning to rank** – ordinal regression to produce ordered lists (internet search).
- **Bootstrapping** – reusing the results of a model to improve itself.
- **Model selection** – finding the balance between models with many or few parameters.

## Probability in Machine Learning
All methods and approaches benefit from methods that not only give answers but also estimate model confidence, data description quality, and anticipate how these measures change with further experiments. Probability theory thus plays a central role in machine learning, and we will actively use it.

## Bayesian Approach to Machine Learning

### Basic Probability Definitions
We won’t need mathematical definitions of sigma‑algebras, probability measures, Borel sets, etc. It suffices to understand discrete random variables (probabilities summing to one) and continuous random variables (integral of non‑negative density equals one).

- **Joint probability** – probability of two events occurring simultaneously, $p(x, y)$; **marginalization**:
  $$p(x) = \sum_y p(x, y).$$
- **Conditional probability** – probability of one event given another occurred, $p(x \mid y)$:
  $$p(x, y) = p(x \mid y)p(y) = p(y \mid x)p(x).$$
- **Bayes’ theorem** – from above:
  $$p(y \mid x) = \frac{p(x \mid y)p(y)}{p(x)} = \frac{p(x \mid y)p(y)}{\sum_{y'} p(x \mid y')p(y')}.$$
- **Independence**: $x$ and $y$ are independent if $p(x, y) = p(x)p(y)$.

### Bayesian Inference for Parameters
Let us begin with the Bayes’ theorem for parameter estimation:
$$p(\theta \mid D) = \frac{p(\theta)p(D \mid \theta)}{p(D)}.$$
Here, $p(\theta)$ is the **prior** probability, $p(D \mid \theta)$ is the **likelihood**, $p(\theta \mid D)$ is the **posterior** probability, and $p(D) = \int p(D \mid \theta)p(\theta)\,\mathrm{d}\theta$ is the **evidence**.

### Maximum Likelihood vs. Maximum a Posteriori
In statistics, typically we look for the maximum likelihood hypothesis:
$$\theta_{\text{ML}} = \arg\max_\theta p(D \mid \theta).$$
Bayesian approaches seek the posterior distribution $p(\theta \mid D) \propto p(D \mid \theta)p(\theta)$ and possibly the maximum a posteriori hypothesis:
$$\theta_{\text{MAP}} = \arg\max_\theta p(\theta \mid D) = \arg\max_\theta p(D \mid \theta)p(\theta).$$

### Direct and Inverse Problems
- **Direct problem**: an urn contains 10 balls, 3 of which are black. What is the probability of drawing a black ball? Or: an urn contains 10 balls numbered from 1 to 10. What’s the probability that the sum of numbers on three consecutively drawn balls is 12?
- **Inverse problem**: two urns each contain 10 balls; one has 3 black balls, the other 6. Someone took a ball from one urn, and it was black. What’s the probability that it was taken from the first urn?

Notice that in the inverse problem, probabilities immediately become Bayesian (although it can also be reformulated through frequencies). In other words, direct probability problems describe a probabilistic process or model and ask to calculate a specific probability (i.e., predict behaviour based on the model). Inverse problems contain hidden variables and often require building a probabilistic model based on observed behaviour. Machine learning problems typically belong to the second category.

### Probability as Frequency vs. Degree of Belief
Classical probability theory, originating from physical experiments, usually views probability as the limit of the ratio of occurrences of a particular experiment outcome to the total number of experiments (e.g., tossing a coin).

But we might want to reason about the “probability” of:
- Spain winning the FIFA World Cup in 2026;
- the *Odyssey* having been written by a woman;
- AGI taking over control from humans by 2030;
- ...

Here, “experiments repeated to infinity” are meaningless—there is exactly one experiment. In such cases, probabilities become **degrees of belief**. This is the Bayesian interpretation of probability (as Thomas Bayes originally saw it). Fortunately, both interpretations follow the same laws; results show that natural axioms of probabilistic logic lead to a very restricted class of functions (Cox, 19).

### Examples

1. **Two children problem.** A person has two kids. Assume that every baby is born either a boy or a girl independently with equal probabilities $\frac{1}{2}$.
   - (1) I’ve asked if the guy has any boys, and he said yes; what’s the probability that he has a girl?
   - (2) I’ve met one of his kids, and it’s a boy; what’s the probability that the other is a girl?

2. **Prosecutor’s fallacy.** A murder has happened. Blood at the crime scene is certain to be the killer’s, and it’s a rare blood type with 1 % prevalence… including the defendant.
   - (1) Prosecutor says: “The chance that the defendant would have this blood type if he was innocent is only 1 %, so with probability 99 % he is guilty”. What’s the prosecutor’s mistake?
   - (2) Defense attorney says: “A million people live in the city, so about 10000 of them have the same blood type. So all that the blood tells us is that the defendant is guilty with probability 0.01 %; that’s no proof, please strike that”. What is the attorney’s mistake?

3. **Real cases.**
   - (1) The prosecutor said that O.J. Simpson already had a history of domestic violence with his wife. The attorney pointed out: “That’s awful but only one out of 2500 women subject to domestic violence actually get killed, so this is irrelevant for the murder”. The court agreed with the defense; is this correct inference?
   - (2) Two babies of the same mother, Sally Clark, died from SIDS; the prosecutor said that the combined probability of two SIDS cases in a row (obtained from single‑case statistic) was about 1 in 73 million; is he right?

## Bayesian Inference for a Coin

### Problem Statement
Simple inference problem: an unfair coin is flipped $N$ times, producing a sequence of results. We must determine its “unfairness” and predict the next outcome.

If we have a probability $p_h = \theta$ for heads (and thus tails probability $p_t = 1 - \theta$), the probability of a sequence $s$ with $n$ heads and $m$ tails is
$$p(s \mid p_h = \theta) = \theta^n (1 - \theta)^m.$$
Assume a uniform prior for coin probability before the experiments, meaning no initial preference about $\theta$. We now use Bayes’ theorem to infer the hidden parameters.

### Example of Bayesian Inference
Likelihood: $p(\theta \mid s) = \frac{p(s \mid \theta)p(\theta)}{p(s)}$.
Here, $p(\theta)$ should be understood as a continuous random variable defined on $[0,1]$; our uniform prior means $p(\theta) = 1$, $\theta \in [0,1]$. We already know $p(s \mid \theta)$.

Thus,
$$p(\theta \mid s) = \frac{\theta^n (1 - \theta)^m}{p(s)}.$$
The evidence $p(s)$ can be calculated as
$$p(s) = \int_0^1 \theta^n (1 - \theta)^m \, \mathrm{d}\theta = \frac{\Gamma(n+1)\Gamma(m+1)}{\Gamma(n+m+2)} = \frac{n!\,m!}{(n+m+1)!},$$
but $\arg\max_\theta p(\theta \mid s) = \frac{n}{n+m}$ can be found without this integral.

To predict the next outcome, we calculate $p(\text{heads} \mid s)$:
$$
\begin{aligned}
p(\text{heads} \mid s) &= \int_0^1 p(\text{heads} \mid \theta) \, p(\theta \mid s) \, \mathrm{d}\theta \\
&= \int_0^1 \frac{\theta^{n+1} (1 - \theta)^m}{p(s)} \, \mathrm{d}\theta \\
&= \frac{(n+1)!\,m!}{(n+m+2)!} \cdot \frac{(n+m+1)!}{n!\,m!} = \frac{n+1}{n+m+2}.
\end{aligned}
$$
We have obtained **Laplace’s rule**.

This illustrates two main tasks in Bayesian inference:
1. Finding the posterior distribution over hypotheses/parameters: $p(\theta \mid D) \propto p(D \mid \theta)p(\theta)$ and/or the maximum a posteriori hypothesis $\theta_{\text{MAP}} = \arg\max_\theta p(\theta \mid D)$.
2. Finding the predictive distribution for outcomes of future experiments: $p(x \mid D) \propto \int_{\theta \in \Theta} p(x \mid \theta) \, p(D \mid \theta) \, p(\theta) \, \mathrm{d}\theta$.

## Conjugate Priors

### A Reminder
Bayesian inference involves:
- $p(x \mid \theta)$ – the likelihood of the data;
- $p(\theta)$ – the prior distribution;
- $p(x) = \int_\Theta p(x \mid \theta) p(\theta) \, \mathrm{d}\theta$ – the marginal likelihood;
- $p(\theta \mid x) = \frac{p(x \mid \theta) p(\theta)}{p(x)}$ – the posterior distribution;
- $p(x' \mid x) = \int_\Theta p(x' \mid \theta) p(\theta \mid x) \, \mathrm{d}\theta$ – the prediction for a new $x'$.

The task is usually to find $p(\theta \mid x)$ and/or $p(x' \mid x)$.

### Prior Distributions
When doing Bayesian inference, besides the likelihood we must also have a prior distribution over all possible values of the parameters. The choice of prior is very important. To compute $p(\theta \mid x)$ and/or $p(x' \mid x)$, we first have to choose $p(\theta)$. How should we choose prior distributions?

### Conjugate Priors
A reasonable goal: let us choose distributions that keep the same form a posteriori. Before inference we have a prior $p(\theta)$. After data, we have a posterior $p(\theta \mid x)$. We want $p(\theta \mid x)$ to have the same form as $p(\theta)$, just with different parameters.

A (not too formal) definition: a family of distributions $p(\theta \mid \alpha)$ is called a family of **conjugate priors** for a family of likelihoods $p(x \mid \theta)$ if, after multiplying by the likelihood, the posterior stays in the same family: $p(\theta \mid x, \alpha) = p(\theta \mid \alpha')$. The $\alpha$ are called **hyperparameters** – the “parameters of the distribution of the parameters”. (Trivial example: the family of all distributions is conjugate to anything, but that is not very interesting.)

The form of a good prior depends on the form of the data distribution itself, $p(x \mid \theta)$. Conjugate priors have been computed for many distributions; we will give a few examples.

### Bernoulli Trials (Beta Prior)
What is the conjugate prior for tossing an unfair coin (Bernoulli trials)? The answer: the **Beta distribution**. The density of the coin’s bias $\theta$ is
$$p(\theta \mid \alpha, \beta) = \frac{\theta^{\alpha-1}(1-\theta)^{\beta-1}}{B(\alpha, \beta)}.$$
If we sample the coin and obtain $s$ heads and $f$ tails, then
$$p(s, f \mid \theta) = \binom{s+f}{s} \theta^s (1-\theta)^f,$$
and the posterior becomes
$$p(\theta \mid s, f) = \frac{\binom{s+f}{s} \theta^{s+\alpha-1}(1-\theta)^{f+\beta-1} / B(\alpha, \beta)}{\int_0^1 \binom{s+f}{s} x^{s+\alpha-1}(1-x)^{f+\beta-1} / B(\alpha, \beta) \, \mathrm{d}x} = \frac{\theta^{s+\alpha-1}(1-\theta)^{f+\beta-1}}{B(s+\alpha, f+\beta)}.$$
Thus, the conjugate prior is $p(\theta \mid \alpha, \beta) \propto \theta^{\alpha-1}(1-\theta)^{\beta-1}$. After receiving new data with $s$ heads and $f$ tails, the hyperparameters update to $s+\alpha$, $f+\beta$:
$$p(\theta \mid s+\alpha, f+\beta) \propto \theta^{s+\alpha-1}(1-\theta)^{f+\beta-1}.$$
At this point you can forget the complicated formulas—a very simple learning rule emerges (where “learning” now means updating the hyperparameters).

### The Beta Distribution
*(figure: Beta distribution)*

### Multinomial Distribution (Dirichlet Prior)
A simple generalization: consider a **multinomial distribution** with $n$ trials and $k$ categories, where $x_i$ of the experiments fell into category $i$. The parameters $\theta_i$ are the probabilities of falling into category $i$:
$$p(x \mid \theta) = \binom{n}{x_1, \dots, x_k} \theta_1^{x_1} \theta_2^{x_2} \dots \theta_k^{x_k}.$$
The conjugate prior is the **Dirichlet distribution**:
$$p(\theta \mid \alpha) \propto \theta_1^{\alpha_1-1} \theta_2^{\alpha_2-1} \dots \theta_k^{\alpha_k-1}.$$
**Exercise.** Show that upon receiving data $x_1, \dots, x_k$ the hyperparameters update to
$$p(\theta \mid x, \alpha) = p(\theta \mid x + \alpha) \propto \theta_1^{x_1+\alpha_1-1} \theta_2^{x_2+\alpha_2-1} \dots \theta_k^{x_k+\alpha_k-1}.$$

### The Dirichlet Distribution
*(figure: Dirichlet distribution)*
