# Slides (extracted) — slides.pdf

## Slide 1

INTRO TO MACHINE LEARNING
Sergey Nikolenko
Harbour Space University
June 8, 2026
Random facts:
• on June 8, 793, "the ravaging of wretched heathen men destroyed God's church at
Lindisfarne" in Northumbria; thus began Viking activity on the British Isles
• on June 8, 1191, Richard Cœur de Lion arrived in Acre and began the Third Crusade; he
defeated Saladin at Arsuf and Jaffa, reaching a settlement in September 1192
• on June 8, 1794, Maximilien Robespierre opened the first celebration of the French
Revolution's new state religion, Culte de l'Être suprême (Cult of the Supreme Being); large
festivals were to be held all across France, with Jacques-Louis David organizing it in Paris;
when Robespierre was guillotined on July 28 (in two months) the religion immediately
disappeared and was officially banned by Napoleon in 1802
• on June 8, 1887, Herman Hollerith applied for US patent #395,781 for the "Art of Compiling
Statistics", which was his punched card calculator
• on June 8, 1959, USS Barbero and the US Postal Service attempted the delivery of mail via
Missile Mail, firing a cruise missile with nuclear warhead replaced by mail containers
1

## Slide 2

WHAT IS MACHINE LEARNING

## Slide 3

AI TIMELINES
• We live in some very interesting times...
3

## Slide 4

AI TIMELINES
• We live in some very interesting times...
3

## Slide 5

AI TIMELINES
• We live in some very interesting times...
3

## Slide 6

AI TIMELINES
• And nobody predicted this! This is a book from 2018:
• Let’s start from the beginning...
3

## Slide 7

EARLY THOUGHTS ON ARTIFICIAL INTELLIGENCE
• Hephaestus created android
robots for himself, such as the
giant humanoid robot Talos
• Pygmalion brought Galatea to life
• Jehovah and Allah—pieces of clay
• Some particularly wise rabbis
could create golems
• Albertus Magnus crafted an
artificial speaking head (greatly
upsetting Thomas Aquinas)
4

## Slide 8

MECHANICAL AUTOMATA
• Early automata were quite inventive: al-Jazari (12th century)
• Robert II d’Artois’ Hesdin Castle, Leonardo da Vinci’s mechanical
knight...
5

## Slide 9

MECHANICAL AUTOMATA
• Automata by Jaquet-Droz (XVIII century):
5

## Slide 10

MECHANICAL AUTOMATA
• But these were purely mechanical; mathematical/logical AI
remained rudimentary for a long time.
• Logical machine by Ramon Llull (late XIII–early XIV century):
• Starting from Dr. Frankenstein, AI consistently appears in
literature...
5

## Slide 11

THE TURING TEST
• AI as a science began with the Turing test (1950).
• A computer should successfully impersonate a human in a
(written) dialogue between a judge, a human, and a computer.
Actually, the original formulation was somewhat subtler and
more interesting...
6

## Slide 12

THE TURING TEST
• It is already obvious how much is required to build AI:
• natural language processing;
• knowledge representation;
• reasoning from acquired knowledge;
• learning from experience (machine learning itself).
6

## Slide 13

THE TURING TEST
• By the way, it required special efforts to try the Turing test with
modern LLMs, so officially it was passed only very recently
(Jones, Bergen, Mar 31, 2025):
6

## Slide 14

THE DARTMOUTH WORKSHOP
• AI as a field emerged in 1956 at the Dartmouth workshop.
• It was organized by John McCarthy, Marvin Minsky, Claude
Shannon, and Nathaniel Rochester.
• Probably the most ambitious grant proposal in computing
history.
7

## Slide 15

THE DARTMOUTH WORKSHOP
We propose a 2-month study of artificial intelligence to be carried
out by 10 people in the summer of 1956 at Dartmouth College in
Hanover, New Hampshire.
The study is based on the conjecture
that every aspect of learning or any other feature of intelligence
can in principle be so precisely described that a machine can sim-
ulate it. We will attempt to find how to make machines use natural
languages, form abstractions and concepts, solve problems now re-
served for humans, and improve themselves. We think significant
advancement in one or more of these problems is possible if a care-
fully selected group of scientists works on it for a summer.
7

## Slide 16

1956–1960: HIGH EXPECTATIONS
• Optimistic times. It seemed that just a bit more, just a little bit...
• Allen Newell, Herbert Simon: Logic Theorist. Successfully
re-proved most of Principia Mathematica, sometimes even more
elegantly than Russell and Whitehead themselves.
8

## Slide 17

1956–1960: HIGH EXPECTATIONS
• Optimistic times. It seemed that just a bit more, just a little bit...
• General Problem Solver—a program trying to think like a human;
• Many specialized programs performing limited tasks
(microworlds):
• Analogy (IQ tests for “pick the odd one out”);
• Student (algebraic word problems);
• Blocks World (manipulating 3D blocks).
8

## Slide 18

1970S: KNOWLEDGE-BASED SYSTEMS
• Core idea: accumulate a sufficiently large set of rules and
domain knowledge, then draw conclusions.
• First success: MYCIN—blood infection diagnosis:
• about 450 rules;
• performed as well as experienced physicians and significantly
better than novices.
9

## Slide 19

1980S: COMMERCIAL APPLICATIONS; AI INDUSTRY
• The first AI department was at DEC (Digital Equipment
Corporation); reportedly saving DEC about $10 million annually
by 1986.
• The boom ended by the late 80s as many companies failed to
meet overly high expectations.
10

## Slide 20

1990–2010: DATA MINING, MACHINE LEARNING
• In recent decades, the main focus shifted to machine learning
and discovering patterns in data
• Especially with the development of the Internet
• Next we got to the deep learning revolution, and recently to the
LLM revolution... but that is a very different story
11

## Slide 21

DEFINITION
• What does a ”learning machine” mean? How to define
”learnability”?
12

## Slide 22

DEFINITION
• What does a ”learning machine” mean? How to define
”learnability”?
Definition
A computer program learns with accumulating experience regarding
a class of tasks 𝑇and a performance measure 𝑃, if its performance
on these tasks (according to 𝑃) improves as it gains new experience.
• This definition is very (too?) general.
• What specific examples can we provide?
12

## Slide 23

WHAT WE WILL COVER
• We will consider various algorithms solving specific tasks,
performing better with more initial (test) data
• Today we’ll discuss the general theory of Bayesian inference,
usually applicable to any machine learning algorithm
• But first—a brief overview of basic ML tasks
13

## Slide 24

KEY ML TASKS AND CONCEPTS
14

## Slide 25

KEY ML TASKS AND CONCEPTS
• Supervised learning – learning with a set of labeled examples:
• training set – a set of examples, each consisting of features
(attributes);
• examples have correct answers – a variable (response) we want to
predict; it can be categorical, continuous, or ordinal;
• a model learns from this dataset (training phase, learning phase),
then it can be applied to new examples (test set);
• main goal – train a model that not only fits training data but also
generalizes well to new data;
• otherwise – overfitting;
15

## Slide 26

KEY ML TASKS AND CONCEPTS
• Supervised learning – learning with a set of labeled examples:
• usually, we’re given only the training set – how can we check
model generalization?
• cross-validation – splitting data into training and validation sets;
• typically, preprocessing is performed before inputting data,
extracting the most informative aspects (feature extraction).
15

## Slide 27

KEY ML TASKS AND CONCEPTS
• Supervised learning – learning with a set of labeled examples:
• Classification: there is a discrete set of categories (classes), and
new examples must be assigned to a class;
• text classification by topics, spam filtering;
• face/object/text recognition;
• Regression: there is an unknown function whose values we must
predict for new examples:
• engineering applications (predicting temperature, robot position,
etc.);
• finance – predicting stock prices;
• same plus temporal changes – e.g., speech recognition
15

## Slide 28

KEY ML TASKS AND CONCEPTS
• Supervised learning – learning with a set of labeled examples:
• Unsupervised learning – learning without labeled data, only raw
data:
• clustering: partitioning data into unknown classes based on
similarity:
• identifying gene families from nucleotide sequences
• user clustering and personalization
• clustering mass spectrometry images into segments with different
compositions
15

## Slide 29

KEY ML TASKS AND CONCEPTS
• Supervised learning – learning with a set of labeled examples:
• Unsupervised learning – learning without labeled data, only raw
data:
• dimensionality reduction: data has huge dimensionality (many
features), and we need to reduce it by selecting the most
informative features so algorithms can run effectively;
• matrix completion: given a sparse matrix, predict missing values;
• often some data has labeled examples – semi-supervised learning.
15

## Slide 30

KEY ML TASKS AND CONCEPTS
• Reinforcement learning – learning where an agent learns from
its own trials and errors:
• multi-armed bandits: choosing from several actions, each leading
to random outcomes; goal is to maximize rewards;
• exploration vs. exploitation: deciding when to explore new options
versus exploiting known ones;
• credit assignment: reward is given at the end (winning a game),
and we must assign credit to each action leading to success.
15

## Slide 31

KEY ML TASKS AND CONCEPTS
• Active learning – choosing the next (relatively expensive) test;
• Learning to rank – ordinal regression to produce ordered lists
(internet search);
• Bootstrapping – reusing the results of a model to improve itself;
• Model selection – finding the balance between models with
many or few parameters.
15

## Slide 32

PROBABILITY IN MACHINE LEARNING
• All methods and approaches benefit from methods that not only
give answers but also estimate model confidence, data
description quality, and anticipate how these measures change
with further experiments.
• Probability theory thus plays a central role in machine learning,
and we will actively use it.
16

## Slide 33

BAYESIAN APPROACH TO ML

## Slide 34

BASIC DEFINITIONS
• We won’t need mathematical definitions of sigma-algebras,
probability measures, Borel sets, etc.
• It suffices to understand discrete random variables
(probabilities summing to one) and continuous random
variables (integral of nonnegative density equals one)
18

## Slide 35

BASIC DEFINITIONS
• Joint probability – probability of two events occurring
simultaneously, 𝑝(𝑥, 𝑦); marginalization:
𝑝(𝑥) = ∑
𝑦
𝑝(𝑥, 𝑦).
• Conditional probability – probability of one event given another
occurred, 𝑝(𝑥∣𝑦):
𝑝(𝑥, 𝑦) = 𝑝(𝑥∣𝑦)𝑝(𝑦) = 𝑝(𝑦∣𝑥)𝑝(𝑥).
• Bayes’ theorem – from above:
𝑝(𝑦|𝑥) = 𝑝(𝑥|𝑦)𝑝(𝑦)
𝑝(𝑥)
=
𝑝(𝑥|𝑦)𝑝(𝑦)
∑𝑦′ 𝑝(𝑥|𝑦′)𝑝(𝑦′).
• Independence: 𝑥and 𝑦are independent if
𝑝(𝑥, 𝑦) = 𝑝(𝑥)𝑝(𝑦).
18

## Slide 36

DEFINITIONS
• Let us begin with the Bayes’ theorem:
𝑝(𝜃|𝐷) = 𝑝(𝜃)𝑝(𝐷|𝜃)
𝑝(𝐷)
.
• Here, 𝑝(𝜃) is the prior probability, 𝑝(𝐷|𝜃) is the likelihood, 𝑝(𝜃|𝐷)
is the posterior probability, and 𝑝(𝐷) = ∫𝑝(𝐷∣𝜃)𝑝(𝜃)d𝜃is the
evidence.
19

## Slide 37

ML VS. MAP
• In statistics, typically we look for the maximum likelihood
hypothesis:
𝜃𝑀𝐿= arg max𝜃𝑝(𝐷∣𝜃).
• Bayesian approaches seek the posterior distribution
𝑝(𝜃|𝐷) ∝𝑝(𝐷|𝜃)𝑝(𝜃)
and possibly the maximum a posteriori hypothesis:
𝜃𝑀𝐴𝑃= arg max𝜃𝑝(𝜃∣𝐷) = arg max𝜃𝑝(𝐷∣𝜃)𝑝(𝜃).
20

## Slide 38

DIRECT AND INVERSE PROBLEMS
• Direct problem: an urn contains 10 balls, 3 of which are black.
What is the probability of drawing a black ball?
• Or: an urn contains 10 balls numbered from 1 to 10. What’s the
probability that the sum of numbers on three consecutively
drawn balls is 12?
• Inverse problem: two urns each contain 10 balls; one has 3 black
balls, the other 6. Someone took a ball from one urn, and it was
black. What’s the probability that it was taken from the first urn?
• Notice that in the inverse problem, probabilities immediately
become Bayesian (although it can also be reformulated through
frequencies).
21

## Slide 39

DIRECT AND INVERSE PROBLEMS
• In other words, direct probability problems describe a
probabilistic process or model and ask to calculate a specific
probability (i.e., predict behavior based on the model).
• Inverse problems contain hidden variables (in the example—the
number of the urn from which the ball was drawn). They often
require building a probabilistic model based on observed
behavior.
• Machine learning problems typically belong to the second
category.
22

## Slide 40

PROBABILITY AS FREQUENCY
• Classical probability theory, originating from physical
experiments, usually views probability as the limit of the ratio of
occurrences of a particular experiment outcome to the total
number of experiments.
• Standard example: tossing a coin.
23

## Slide 41

PROBABILITY AS A DEGREE OF BELIEF
• But we might want to reason about the “probability” of:
• Spain winning the FIFA World Cup in 2026;
• the Odyssey having been written by a woman;
• AGI taking over control from humans by 2030;
• ...
• But “experiments repeated to infinity” are meaningless
here—there is exactly one experiment.
24

## Slide 42

PROBABILITY AS A DEGREE OF BELIEF
• Here, probabilities become degrees of belief. This is the
Bayesian interpretation of probability (as Thomas Bayes
originally saw it).
• Fortunately, both interpretations follow the same laws; results
show that natural axioms of probabilistic logic lead to a very
restricted class of functions (Cox, 19).
24

## Slide 43

EXAMPLES
1. A person has two kids. Let’s assume that every baby is born
either a boy or a girl independently with equal probabilities 1
2.
Two problem settings:
(1) I’ve asked if the guy has any boys, and he said yes; what’s the
probability that he has a girl?
(2) I’ve met one of his kids, and it’s a boy; what’s the probability that
the other is a girl?
25

## Slide 44

EXAMPLES
2. A murder has happened. Blood at the crime scene is certain to
be the killer’s, and it’s a rare blood type with 1% prevalence...
including the defendant.
(1) Prosecutor says: «The chance that the defendant would have this
blood type if he was innocent is only 1%, so with probability 99%
he is guilty». What’s the prosecutor’s mistake?
(2) Defense attorney says: «A million people live in the city, so about
10000 of them have the same blood type. So all that the blood
tells us is that the defendant is guilty with probability 0.01%; that’s
no proof, please strike that». What is the attorney’s mistake?
25

## Slide 45

EXAMPLES
3. Real cases.
(1) The prosecutor said that O.J. Simpson already had a history of
domestic violence with his wife. The attorney pointed out: «That’s
awful but only one out of 2500 women subject to domestic
violence actually get killed, so this is irrelevant for the murder».
The court agreed with the defense; is this correct inference?
(2) Two babies of the same mother, Sally Clark, died from SIDS; the
prosecutor said that the combined probability of two SIDS cases in
a row (obtained from single-case statistic) was about 1 in 73
million; is he right?
25

## Slide 46

BAYESIAN INFERENCE
FOR A COIN

## Slide 47

PROBLEM STATEMENT
• Simple inference problem: an unfair coin is flipped 𝑁times,
producing a sequence of results. We must determine its
”unfairness” and predict the next outcome.
27

## Slide 48

PROBLEM STATEMENT
• If we have a probability 𝑝ℎ= 𝜃for heads (and thus tails
probability 𝑝𝑡= 1 −𝜃), the probability of a sequence 𝑠with 𝑛
heads and 𝑚tails is
𝑝(𝑠|𝑝ℎ= 𝜃) = 𝜃𝑛(1 −𝜃)𝑚.
• Assume a uniform prior for coin probability before the
experiments, meaning no initial preference about 𝜃.
• We now use Bayes’ theorem to infer the hidden parameters.
27

## Slide 49

EXAMPLE OF BAYESIAN INFERENCE
• Likelihood: 𝑝(𝜃|𝑠) = 𝑝(𝑠|𝜃)𝑝(𝜃)
𝑝(𝑠)
.
• Here, 𝑝(𝜃) should be understood as a continuous random
variable defined on the interval [0, 1], which it indeed is. Our
assumption of a uniform distribution in this case means the
prior probability 𝑝(𝜃) = 1, 𝜃∈[0, 1] (i.e., we have no prior
preference about the coin’s fairness, assuming all outcomes
equally likely). We already know 𝑝(𝑠|𝜃).
• Thus, we have:
𝑝(𝜃|𝑠) = 𝜃𝑛(1 −𝜃)𝑚
𝑝(𝑠)
.
28

## Slide 50

EXAMPLE OF BAYESIAN INFERENCE
• Thus, we have:
𝑝(𝜃|𝑠) = 𝜃𝑛(1 −𝜃)𝑚
𝑝(𝑠)
.
• 𝑝(𝑠) can be calculated as
𝑝(𝑠) = ∫
1
0
𝜃𝑛(1 −𝜃)𝑚𝑑𝜃=
= Γ(𝑛+ 1)Γ(𝑚+ 1)
Γ(𝑛+ 𝑚+ 2)
=
𝑛!𝑚!
(𝑛+ 𝑚+ 1)!,
but arg max𝜃𝑝(𝜃∣𝑠) =
𝑛
𝑛+𝑚can be found without this integral.
28

## Slide 51

EXAMPLE OF BAYESIAN INFERENCE
• Thus, we have:
𝑝(𝜃|𝑠) = 𝜃𝑛(1 −𝜃)𝑚
𝑝(𝑠)
.
• But that’s not all. To predict the next outcome, we calculate
𝑝(heads|𝑠):
𝑝(heads|𝑠) = ∫
1
0
𝑝(heads|𝜃)𝑝(𝜃|𝑠)𝑑𝜃=
= ∫
1
0
𝜃𝑛+1(1 −𝜃)𝑚
𝑝(𝑠)
𝑑𝜃=
=
(𝑛+ 1)!𝑚!
(𝑛+ 𝑚+ 2)! ⋅(𝑛+ 𝑚+ 1)!
𝑛!𝑚!
=
𝑛+ 1
𝑛+ 𝑚+ 2.
• We have obtained Laplace’s rule.
28

## Slide 52

EXAMPLE OF BAYESIAN INFERENCE
• Thus, we have:
𝑝(𝜃|𝑠) = 𝜃𝑛(1 −𝜃)𝑚
𝑝(𝑠)
.
• This was an illustration of two main tasks in Bayesian inference:
(1) finding the posterior distribution over hypotheses/parameters:
𝑝(𝜃∣𝐷) ∝𝑝(𝐷|𝜃)𝑝(𝜃)
and/or finding the maximum a posteriori hypothesis
𝜃MAP = arg max𝜃𝑝(𝜃∣𝐷);
(2) finding the predictive distribution for outcomes of future
experiments:
𝑝(𝑥∣𝐷) ∝∫
𝜃∈Θ
𝑝(𝑥∣𝜃)𝑝(𝐷|𝜃)𝑝(𝜃)d𝜃.
28

## Slide 53

CONJUGATE PRIORS

## Slide 54

A REMINDER
• Recall that our main task is to learn the parameters of a
distribution and/or to predict its next points from the available
data.
• Bayesian inference involves:
• 𝑝(𝑥∣𝜃) – the likelihood of the data;
• 𝑝(𝜃) – the prior distribution;
• 𝑝(𝑥) = ∫Θ 𝑝(𝑥∣𝜃)𝑝(𝜃)𝑑𝜃– the marginal likelihood;
• 𝑝(𝜃∣𝑥) = 𝑝(𝑥∣𝜃)𝑝(𝜃)
𝑝(𝑥)
– the posterior distribution;
• 𝑝(𝑥′ ∣𝑥) = ∫Θ 𝑝(𝑥′ ∣𝜃)𝑝(𝜃∣𝑥)𝑑𝜃– the prediction for a new 𝑥′.
• The task is usually to find 𝑝(𝜃∣𝑥) and/or 𝑝(𝑥′ ∣𝑥).
30

## Slide 55

PRIOR DISTRIBUTIONS
• When we do Bayesian inference, besides the likelihood we must
also have a prior distribution over all possible values of the
parameters.
• We have not paid special attention to them before, but they are
very important.
• The task of Bayesian inference is to compute 𝑝(𝜃∣𝑥) and/or
𝑝(𝑥′ ∣𝑥).
• But to do that, we first have to choose 𝑝(𝜃). How should we
choose prior distributions?
31

## Slide 56

CONJUGATE PRIORS
• A reasonable goal: let us choose the distributions so that they
keep the same form a posteriori.
• Before inference we have a prior distribution 𝑝(𝜃).
• After it we have some new posterior distribution 𝑝(𝜃∣𝑥).
• I want 𝑝(𝜃∣𝑥) to have the same form as 𝑝(𝜃), just with different
parameters.
32

## Slide 57

CONJUGATE PRIORS
• A (not too formal) definition: a family of distributions 𝑝(𝜃∣𝛼) is
called a family of conjugate priors for a family of likelihoods
𝑝(𝑥∣𝜃) if, after multiplying by the likelihood, the posterior
𝑝(𝜃∣𝑥, 𝛼) stays in the same family: 𝑝(𝜃∣𝑥, 𝛼) = 𝑝(𝜃∣𝛼′).
• 𝛼are called hyperparameters – the “parameters of the
distribution of the parameters”.
• Trivial example: the family of all distributions is conjugate to
anything, but that is not very interesting.
32

## Slide 58

CONJUGATE PRIORS
• Of course, the form of a good prior depends on the form of the
data distribution itself, 𝑝(𝑥∣𝜃).
• Conjugate priors have been computed for many distributions;
we will give a few examples.
32

## Slide 59

BERNOULLI TRIALS
• What is the conjugate prior for tossing an unfair coin (Bernoulli
trials)?
• The answer: it is the Beta distribution; the density of the coin’s
bias 𝜃is
𝑝(𝜃∣𝛼, 𝛽) = 𝜃𝛼−1(1 −𝜃)𝛽−1
𝐵(𝛼, 𝛽)
.
33

## Slide 60

BERNOULLI TRIALS
• The density of the coin’s bias 𝜃:
𝑝(𝜃∣𝛼, 𝛽) = 𝜃𝛼−1(1 −𝜃)𝛽−1
𝐵(𝛼, 𝛽)
.
• Then, if we sample the coin and obtain 𝑠heads and 𝑓tails, we
get
𝑝(𝑠, 𝑓∣𝜃) = (𝑠+ 𝑓
𝑠
)𝜃𝑠(1 −𝜃)𝑓, and
𝑝(𝜃|𝑠, 𝑓) =
(𝑠+𝑓
𝑠)𝜃𝑠+𝛼−1(1 −𝜃)𝑓+𝛽−1/𝐵(𝛼, 𝛽)
∫
1
0 (𝑠+𝑓
𝑠)𝑥𝑠+𝛼−1(1 −𝑥)𝑓+𝛽−1/𝐵(𝛼, 𝛽)𝑑𝑥
=
= 𝜃𝑠+𝛼−1(1 −𝜃)𝑓+𝛽−1
𝐵(𝑠+ 𝛼, 𝑓+ 𝛽)
.
33

## Slide 61

BERNOULLI TRIALS
• So it turns out that the conjugate prior for the bias 𝜃of an unfair
coin is
𝑝(𝜃∣𝛼, 𝛽) ∝𝜃𝛼−1(1 −𝜃)𝛽−1.
• After receiving new data with 𝑠heads and 𝑓tails, the
hyperparameters change to
𝑝(𝜃∣𝑠+ 𝛼, 𝑓+ 𝛽) ∝𝜃𝑠+𝛼−1(1 −𝜃)𝑓+𝛽−1.
• At this point you can forget the complicated formulas and
derivations – we got a very simple learning rule (where
“learning” now means updating the hyperparameters).
33

## Slide 62

THE BETA DISTRIBUTION
34

## Slide 63

MULTINOMIAL DISTRIBUTION
• A simple generalization: consider a multinomial distribution
with 𝑛trials and 𝑘categories, where 𝑥𝑖of the experiments fell
into category 𝑖.
• The parameters 𝜃𝑖are the probabilities of falling into category 𝑖:
𝑝(𝑥∣𝜃) = (
𝑛
𝑥1, … , 𝑥𝑛
)𝜃𝑥1
1 𝜃𝑥2
2 … 𝜃𝑥𝑘
𝑘.
• The conjugate prior is the Dirichlet distribution:
𝑝(𝜃∣𝛼) ∝𝜃𝛼1−1
1
𝜃𝛼2−1
2
… 𝜃𝛼𝑘−1
𝑘
.
35

## Slide 64

MULTINOMIAL DISTRIBUTION
• The conjugate prior is the Dirichlet distribution:
𝑝(𝜃∣𝛼) ∝𝜃𝛼1−1
1
𝜃𝛼2−1
2
… 𝜃𝛼𝑘−1
𝑘
.
Exercise. Show that upon receiving data 𝑥1, … , 𝑥𝑘the hyperparameters change to
𝑝(𝜃∣𝑥, 𝛼) = 𝑝(𝜃∣𝑥+ 𝛼) ∝𝜃𝑥1+𝛼1−1
1
𝜃𝑥2+𝛼2−1
2
… 𝜃𝑥𝑘+𝛼𝑘−1
𝑘
.
35

## Slide 65

THE DIRICHLET DISTRIBUTION
36

## Slide 66

THANK YOU!
Thank you for your attention!
37
