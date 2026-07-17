# Slides (extracted) — slides.pdf

## Slide 1

LINEAR MODELS AND INTRO TO DEEP LEARNING
Sergey Nikolenko
Harbour Space University
June 9, 2026
Random facts:
• on June 9, 411 BC, the democratic government in Athens was overthrown in the Athenian
coup and replaced by a short-lived oligarchy of the Four Hundred
• on June 9, 53, the Roman emperor Nero married Claudia Octavia, and on June 9, 68 he died
by suicide, thus ending the Julio-Claudian dynasty and starting a civil war known as the Year
of the Four Emperors
• on June 9, 721, Duke Odo of Aquitaine defeated the Moors (Umayyad Muslim) in the Battle of
Toulouse, one of the main battles that stopped the Muslim conquest of Europe
• on June 9, 1732, James Oglethorpe was granted a royal charter to establish a colony in the
modern state of Georgia, which he imagined as a place to send "the unemployed and the
unemployable"
• on June 9, 1928, Charles Kingsford Smith completed the first trans-Pacific flight in a Fokker
Trimotor monoplane, the Southern Cross
• on June 9, 1934, Donald Fauntleroy Duck first appeared on screen in The Wise Little Hen
1

## Slide 2

BAYESIAN APPROACH TO ML

## Slide 3

BASIC DEFINITIONS
• We won’t need mathematical definitions of sigma-algebras,
probability measures, Borel sets, etc.
• It suffices to understand discrete random variables
(probabilities summing to one) and continuous random
variables (integral of nonnegative density equals one)
3

## Slide 4

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
3

## Slide 5

DEFINITIONS
• Let us begin with the Bayes’ theorem:
𝑝(𝜃|𝐷) = 𝑝(𝜃)𝑝(𝐷|𝜃)
𝑝(𝐷)
.
• Here, 𝑝(𝜃) is the prior probability, 𝑝(𝐷|𝜃) is the likelihood, 𝑝(𝜃|𝐷)
is the posterior probability, and 𝑝(𝐷) = ∫𝑝(𝐷∣𝜃)𝑝(𝜃)d𝜃is the
evidence.
4

## Slide 6

ML VS. MAP
• In statistics, typically we look for the maximum likelihood
hypothesis:
𝜃𝑀𝐿= arg max𝜃𝑝(𝐷∣𝜃).
• Bayesian approaches seek the posterior distribution
𝑝(𝜃|𝐷) ∝𝑝(𝐷|𝜃)𝑝(𝜃)
and possibly the maximum a posteriori hypothesis:
𝜃𝑀𝐴𝑃= arg max𝜃𝑝(𝜃∣𝐷) = arg max𝜃𝑝(𝐷∣𝜃)𝑝(𝜃).
5

## Slide 7

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
6

## Slide 8

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
7

## Slide 9

PROBABILITY AS FREQUENCY
• Classical probability theory, originating from physical
experiments, usually views probability as the limit of the ratio of
occurrences of a particular experiment outcome to the total
number of experiments.
• Standard example: tossing a coin.
8

## Slide 10

PROBABILITY AS A DEGREE OF BELIEF
• But we might want to reason about the “probability” of:
• Spain winning the FIFA World Cup in 2026;
• the Odyssey having been written by a woman;
• AGI taking over control from humans by 2030;
• ...
• But “experiments repeated to infinity” are meaningless
here—there is exactly one experiment.
9

## Slide 11

PROBABILITY AS A DEGREE OF BELIEF
• Here, probabilities become degrees of belief. This is the
Bayesian interpretation of probability (as Thomas Bayes
originally saw it).
• Fortunately, both interpretations follow the same laws; results
show that natural axioms of probabilistic logic lead to a very
restricted class of functions (Cox, 19).
9

## Slide 12

EXAMPLES
1. A person has two kids. Let’s assume that every baby is born
either a boy or a girl independently with equal probabilities 1
2.
Two problem settings:
(1) I’ve asked if the guy has any boys, and he said yes; what’s the
probability that he has a girl?
(2) I’ve met one of his kids, and it’s a boy; what’s the probability that
the other is a girl?
10

## Slide 13

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
10

## Slide 14

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
10

## Slide 15

LINEAR REGRESSION

## Slide 16

LINEAR REGRESSION
• For example, linear regression.
• Linear model: consider a linear function
𝑦(x, w) = 𝑤0 +
𝑝
∑
𝑗=1
𝑥𝑗𝑤𝑗= x⊤w,
x = (1, 𝑥1, … , 𝑥𝑝).
• How can we find optimal parameterŝ w by training data of the
form (x𝑖, 𝑦𝑖)𝑁
𝑖=1?
12

## Slide 17

LINEAR REGRESSION
• How can we find optimal parameterŝ w by training data of the
form (x𝑖, 𝑦𝑖)𝑁
𝑖=1?
• Least squares estimation: we will minimize
RSS(w) =
𝑁
∑
𝑖=1
(𝑦𝑖−x⊤
𝑖w)2.
• There is even an exact solution, but that’s not important right
now.
12

## Slide 18

LINEAR REGRESSION
• What is important: suppose that noise (error in the data) has a
normal distribution, i.e., observed variable 𝑡is
𝑡= 𝑦(x, w) + 𝜖,
𝜖∼𝑁(0, 𝜎2), that is
𝑝(𝑡∣x, w, 𝜎2) = 𝑁(𝑡∣𝑦(x, w), 𝜎2).
12

## Slide 19

LINEAR REGRESSION
• Aside – normal distribution:
𝑝(𝑥) =
1
𝜎
√
2𝜋
𝑒−(𝑥−𝜇)2
2𝜎2 .
• Why is it so important?
12

## Slide 20

LINEAR REGRESSION
• Consider a dataset X = {x1, … , x𝑁} with correct answers
t = {𝑡1, … , 𝑡𝑁}.
• We assume that the data points are independent identically
distributed:
𝑝(t ∣X, w, 𝜎2) =
𝑁
∏
𝑛=1
𝑁(𝑡𝑛∣w⊤𝜙(x𝑛), 𝜎2) .
• We take the logarithm (we omit X below for brevity):
ln 𝑝(t ∣w, 𝜎2) = −𝑁
2 ln(2𝜋𝜎2) −
1
2𝜎2
𝑁
∑
𝑛=1
(𝑡𝑛−w⊤𝜙(x𝑛))
2 .
12

## Slide 21

LINEAR REGRESSION
• And we see that to maximize the likelihood w.r.t. w we need to
minimize the mean squared error!
∇w ln 𝑝(t ∣w, 𝜎2) = 1
𝜎2
𝑁
∑
𝑛=1
(𝑡𝑛−w⊤𝜙(x𝑛)) 𝜙(x𝑛).
• We can also get a posterior distribution, introducing prior
distributions (also normal).
• And then the predictive distribution
𝑝(𝑦∣x, 𝐷) = ∫
w
𝑝(𝑦∣x, w)𝑝(w ∣𝐷)dw
...but that’s beside the point right now.
• Main conclusion: in many regression problems it makes sense to
minimize the sum of squared deviations, this corresponds to
normally distributed noise.
12

## Slide 22

BAYESIAN REGULARIZATION

## Slide 23

BAYESIAN REGULARIZATION
• And now let us look at regression from the pure Bayesian
perspective.
• Recall that in Bayesian inference, we
(1) find the posterior distribution on the hypotheses/parameters:
𝑝(𝜃∣𝐷) ∝𝑝(𝐷|𝜃)𝑝(𝜃)
(and/or find the maximal a posteriori hypothesis
arg max𝜃𝑝(𝜃∣𝐷));
(2) find the predictive distribution:
𝑝(𝑥∣𝐷) ∝∫
𝜃∈Θ
𝑝(𝑥∣𝜃)𝑝(𝐷|𝜃)𝑝(𝜃)d𝜃.
14

## Slide 24

BAYESIAN REGULARIZATION
• We have not yet had any priors in our study of linear regression.
• Let us introduce a prior; e.g., the normal distribution:
𝑝(w) = 𝑁(w ∣𝜇0, Σ0).
• Consider a dataset X = {x1, … , x𝑁} with values t = {𝑡1, … , 𝑡𝑁};
we again assume that they are independent and identically
distributed:
𝑝(t ∣X, w, 𝜎2) =
𝑁
∏
𝑛=1
𝑁(𝑡𝑛∣w⊤𝜙(x𝑛), 𝜎2) .
14

## Slide 25

BAYESIAN REGULARIZATION
• Then the problem is to compute
𝑝(w ∣t) ∝𝑝(t ∣X, w, 𝜎2)𝑝(w)
= 𝑁(w ∣𝜇0, Σ0)
𝑁
∏
𝑛=1
𝑁(𝑡𝑛∣w⊤𝜙(x𝑛), 𝜎2) .
• Let us compute!
14

## Slide 26

BAYESIAN REGULARIZATION
• We get
𝑝(w ∣t) = 𝑁(w ∣𝜇𝑁, Σ𝑁),
𝜇𝑁= Σ𝑁(Σ−1
0 𝜇0 + 1
𝜎2 Φ⊤t) ,
Σ𝑁= (Σ−1
0
+ 1
𝜎2 Φ⊤Φ)
−1
.
• And now the log likelihood.
14

## Slide 27

BAYESIAN REGULARIZATION
• If we take the prior distribution around zero:
𝑝(w) = 𝑁(w ∣0, 1
𝛼I),
we get the log likelihood as
ln 𝑝(w ∣t) = −1
2𝜎2
𝑁
∑
𝑛=1
(𝑡𝑛−w⊤𝜙(x𝑛))
2 −𝛼
2 w⊤w + const,
i.e., precisely ridge regression!
14

## Slide 28

EXAMPLE
15

## Slide 29

EXAMPLE
16

## Slide 30

EXAMPLE
17

## Slide 31

EXAMPLE
18

## Slide 32

GENERALIZATION
• A slight generalization – a more general prior distribution:
𝑝(w ∣𝛼) = [𝑞
2 (𝛼
2 )
1/𝑞
1
Γ(1/𝑞)]
𝑀
𝑒−𝛼
2 ∑𝑀
𝑗=1∣𝑤𝑗∣
𝑞
.
Exercise. Compute the log likelihood.
19

## Slide 33

CLASSIFICATION

## Slide 34

CLASSIFICATION PROBLEMS
• For classification problems it is even more clear: we want to
classify a vector x to one of 𝐾classes 𝐶𝑘.
• Suppose that class 𝐶𝑘has density 𝑝(x ∣𝐶𝑘), find prior
distributions 𝑝(𝐶𝑘), and then compute 𝑝(𝐶𝑘∣x) by Bayes’
theorem.
• For two classes:
𝑝(𝐶1 ∣x) =
𝑝(x ∣𝐶1)𝑝(𝐶1)
𝑝(x ∣𝐶1)𝑝(𝐶1) + 𝑝(x ∣𝐶2)𝑝(𝐶2).
21

## Slide 35

CLASSIFICATION PROBLEMS
• We rewrite:
𝑝(𝐶1 ∣x) =
𝑝(x ∣𝐶1)𝑝(𝐶1)
𝑝(x ∣𝐶1)𝑝(𝐶1) + 𝑝(x ∣𝐶2)𝑝(𝐶2) =
1
1 + 𝑒−𝑎= 𝜎(𝑎),
where
𝑎= ln 𝑝(x ∣𝐶1)𝑝(𝐶1)
𝑝(x ∣𝐶2)𝑝(𝐶2),
𝜎(𝑎) =
1
1 + 𝑒−𝑎.
21

## Slide 36

CLASSIFICATION PROBLEMS
• 𝜎(𝑎) is the logistic sigmoid:
𝜎(𝑎) =
1
1 + 𝑒−𝑎
• 𝜎(−𝑎) = 1 −𝜎(𝑎).
• 𝑎= ln (
𝜎
1−𝜎) – logit function.
21

## Slide 37

CLASSIFICATION PROBLEMS
• This, in particular, leads to logistic regression: we optimize w
directly.
• For a dataset {𝜙𝑛, 𝑡𝑛}, 𝑡𝑛∈{0, 1}, 𝜙𝑛= 𝜙(x𝑛):
𝑝(t ∣w) =
𝑁
∏
𝑛=1
𝑦𝑡𝑛
𝑛(1 −𝑦𝑛)1−𝑡𝑛,
𝑦𝑛= 𝑝(𝐶1 ∣𝜙𝑛).
• We find maximal likelihood parameters, minimizing −ln 𝑝(t ∣w):
𝐸(w) = −ln 𝑝(t ∣w) = −
𝑁
∑
𝑛=1
[𝑡𝑛ln 𝑦𝑛+ (1 −𝑡𝑛) ln(1 −𝑦𝑛)] .
21

## Slide 38

CLASSIFICATION PROBLEMS
• And we get a sigmoid that optimally separates the data and that
even tries to model probabilities:
21

## Slide 39

SEVERAL CLASSES
• In case of several classes we get
𝑝(𝐶𝑘∣x) =
𝑝(x ∣𝐶𝑘)𝑝(𝐶𝑘)
∑𝑗𝑝(x ∣𝐶𝑗)𝑝(𝐶𝑗) =
𝑒𝑎𝑘
∑𝑗𝑒𝑎𝑗.
• Here 𝑎𝑘= ln 𝑝(x ∣𝐶𝑘)𝑝(𝐶𝑘).
•
𝑒𝑎𝑘
∑𝑗𝑒𝑎𝑗is the normalized exponent (softmax).
• Conclusion: for a classification problem it makes sense to
minimize the cross-entropy ∑
𝑁
𝑛=1 [𝑡𝑛ln 𝑦𝑛+ (1 −𝑡𝑛) ln(1 −𝑦𝑛)]
and softmax (rather than classification error, which is
problematic).
• One question remains: how do we optimize all this?
• How do we optimize complicated functions in general?
22

## Slide 40

GRADIENT DESCENT
• Gradient descent: virtually the only way to optimize complicated
non-convex functions.
• Take the gradient ∇𝐸(w) w.r.t. weights, move in that direction.
23

## Slide 41

GRADIENT DESCENT
• E.g., for logistic regression we can optimize
𝐸(w) = −ln 𝑝(t ∣w) = −
𝑁
∑
𝑛=1
[𝑡𝑛ln 𝑦𝑛+ (1 −𝑡𝑛) ln(1 −𝑦𝑛)] .
• We use the fact that 𝜎′ = 𝜎(1 −𝜎).
• Take the gradient:
∇𝐸(w) =
𝑁
∑
𝑛=1
(𝑦𝑛−𝑡𝑛)𝜙𝑛.
• And then we can simply use gradient descent (or do even better
with IRLS).
23

## Slide 42

GRADIENT DESCENT
• Gradient descent is a local optimization procedure.
• But there are no global ones... we will only talk of local
improvements of gradient descent, but there will never be a
guarantee with these methods.
23

## Slide 43

THE BRAIN AND ANN HISTORY

## Slide 44

HUMAN BRAIN AS A COMPUTER
• The human brain is a pretty slow computer, but it can do some
pretty amazing things.
• How does it do it?
• Lots of neurons: 1011 neurons, about 7000 synapses each, so in
total about 1014–1015 connections (synapses).
25

## Slide 45

HUMAN BRAIN AS A COMPUTER
• Each neuron:
• gets a signal through the dendrites from other neurons;
• sends signals from time to time through the axon;
• synapses are connections between one neuron’s axon and other
neurons’ dendrites attached to it.
25

## Slide 46

HUMAN BRAIN AS A COMPUTER
• A neuron produces spikes stochastically.
• The firing rate is only 10 to 200 Hz.
• But we can recognize a face in a couple hundred milliseconds.
• This means that sequential computations are very short.
• But the brain is heavily parallelized.
26

## Slide 47

HUMAN BRAIN AS A COMPUTER
• Here is how we process visual input:
27

## Slide 48

FEATURE LEARNING
• Another part of the story: feature learning.
• The brain can train very well on a very small data sample.
• And it can adapt to new data sources.
• How does it do it? Can we do the same?
28

## Slide 49

FEATURE LEARNING
• Systems for processing unstructured data look like
input →features →classifier
• For a long time good features had to be handmade:
• MFCC for speech recognition;
• SIFT for image processing;
• ...
• Feature engineering: can we learn good features automatically?
28

## Slide 50

PLASTICITY
• Third point: neuroplasticity.
• It appears that there is a single learning algorithm (“The Master
Algorithm”) that can be applied to very different situations.
29

## Slide 51

THE MATHEMATICAL ESSENCE
• Generally speaking, all we do in machine learning is
approximation and optimization of various functions.
• For example:
• a function from a picture to what it shows;
• even simpler: binary function from an image’s pixels to “is it a cat
or not”;
• it’s a rather complicated function, and it’s defined as a dataset
(values at a few points);
• how do we approximate it?
30

## Slide 52

THE MATHEMATICAL ESSENCE
• Common approach in machine learning:
• construct a class of models, usually parametric;
• tune the parameters so that the model fits the data well;
• i.e., we optimize a certain error function or quality metric.
• Neural networks are basically universal approximators, a very
wide and flexible parametric class of functions.
• The problem is how to train them well.
30

## Slide 53

ANN HISTORY
• Let’s try to mimic nature: get a large highly connected thing of
small simple things.
• The idea of modeling neurons with simple functions is very-very
old (McCulloch, Pitts, 1943).
• Artificial neural networks (even with several layers) were
proposed, among others, by Turing (1948).
• Rosenblatt, 1958: perceptron (one artificial neuron, will see in a
minute): a linear separating surface.
• Training by gradient descent also appeared at the same time.
31

## Slide 54

ANN HISTORY
• One neuron is modeled as follows:
• Linear combination of inputs follows by a nonlinear activation
function:
𝑦= ℎ(w⊤x) = ℎ(∑
𝑖
𝑤𝑖𝑥𝑖) .
• How can you train a perceptron and what will be the result?
31

## Slide 55

ANN HISTORY
• Training by gradient descent.
• Original Rosenblatt’s perceptron (ℎ= id):
𝐸𝑃(w) = −∑
x∈ℳ
𝑦(x) (w⊤x) ,
w(𝜏+1) = w(𝜏) −𝜂∇w𝐸𝑃(w) = w(𝜏) + 𝜂𝑡𝑛x𝑛.
• Or, e.g., we can do binary classification by plugging in logistic
sigmoid as the activation function ℎ(𝑥) = 𝜎(𝑥) =
1
1+𝑒−𝑥:
𝐸(w) = −1
𝑁
𝑁
∑
𝑖=1
(𝑦𝑖log 𝜎(w⊤x𝑖) + (1 −𝑦𝑖) log (1 −𝜎(w⊤x𝑖))) .
• Basically logistic regression.
31

## Slide 56

ANN HISTORY
• The first perceptron (Rosenblatt, 1958) learned to recognize
letters.
31

## Slide 57

ANN HISTORY
• Hailed as a huge success:
31

## Slide 58

ANN HISTORY
• Minsky’s critique: even with a nonlinearity, one perceptron can
only have a linear separating surface.
31

## Slide 59

ANN HISTORY
• Well, sure! You need to make a network of perceptrons:
• More about that later (actually, the whole course is about that).
• But first let’s see what people do with a single perceptron.
31

## Slide 60

ANN HISTORY
• 1960s: studies of the perceptron.
• (Minsky, Papert, 1969): XOR cannot be modeled by a perceptron.
• For some reason, this was thought to be a big problem.
• (Brison, Hoback, 1969): backpropagation.
• (Hinton, 1974): rediscovered backpropagation and popularized it.
• Second half of the 1970s – multilayer ANN, basically in the
modern form.
• Deep models appeared in early 1980s! It’s not much of an idea.
31

## Slide 61

ANN HISTORY
• But by the early 1990s neural networks did not live up to the
hype (in part for technical reasons).
• John Denker, 1994: «neural networks are the second best way of
doing just about anything».
• So in the 1990s, neural networks were all but forgotten again.
• Except for image processing (Yann LeCun) and a few more
groups (Geoffrey Hinton, Yoshua Bengio).
31

## Slide 62

ANN HISTORY
• Deep learning revolution begins in 2006: Geoffrey Hinton’s
group learned how to train Deep Belief Networks (DBN).
• Main idea: unsupervised pretraining.
• Next component: more powerful computers, computations on
GPUs.
• And much larger datasets.
• Then we got new regularization and optimization techniques
(we’ll talk about those), and pretraining by now is not really
necessary.
• These, together with the architectures, are the main components
of the deep learning revolution.
31

## Slide 63

REAL NEURONS
• Do actual neurons do gradient descent?
• Probably not (we’ll see that backprop would be hard to do).
• Although Geoffrey Hinton had an interesting talk about it. But
still, no.
• Hebbian learning – increase the weight between neurons that
fire together:
Δ𝑤𝑖= 𝜂𝑥𝑖𝑥𝑗.
• Led to Hopfield networks that kinda do associative memory.
• Current research: spike-timing-dependent plasticity; i.e., the
increase depends on the actual temporal properties of signals.
32

## Slide 64

COMBINING PERCEPTRONS INTO A NETWORK
• A network of perceptrons; outputs of one are inputs of another.
• Hornik, 1990: a two-layer ANN can approximate any function.
• This is just theory, but in practice, deep networks are indeed
more expressive – distributed representations:
33

## Slide 65

COMBINING PERCEPTRONS INTO A NETWORK
• Note also how they NNs are usually organized in layers.
• This is natural and suggests easy parallelization.
33

## Slide 66

COMBINING PERCEPTRONS INTO A NETWORK
• So we approximate a very complicated function with a large
composition of simple functions.
• How do we train it?
• Simple answer: gradient descent. But there are complications
here.
33

## Slide 67

THANK YOU!
Thank you for your attention!
34
