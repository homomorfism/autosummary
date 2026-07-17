# Slides (extracted) — slides.pdf

## Slide 1

VAE AND DIFFUSION MODELS
Sergey Nikolenko
Harbour Space University
June 24, 2026
Random facts:
• on June 24, 1374, a "dancing plague" broke out in Aachen: crowds of people danced
uncontrollably through the streets for days, some until they collapsed, in one of several
genuinely documented outbreaks of compulsive dancing in medieval Europe
• on June 24, 1497, John Cabot, sailing under an English flag, reached the coast of
Newfoundland and became the first European on the North American mainland since the
Vikings; he was rewarded by King Henry VII with the grand sum of ten pounds
• on June 24, 1717, the first Masonic Grand Lodge in the world, the Premier Grand Lodge of
England, was founded in London
• on June 24, 1812, Napoleon led his Grande Armée of around 600,000 men across the Niemen
River into Russia; less than a tenth of them would return
• on June 24, 1947, the pilot Kenneth Arnold reported nine objects flying "like a saucer
skipping over water" near Mount Rainier; a newspaper turned his phrasing into "flying
saucer" and the modern UFO era was born
• on June 24, 2010, at Wimbledon, John Isner of the United States defeated Nicolas Mahut of
France in the longest match in professional tennis history, 70:68 in the final fifth set
1

## Slide 2

GENERATIVE MODELS
IN DEEP LEARNING

## Slide 3

DEEP GENERATIVE MODELS
3

## Slide 4

VARIATIONAL AUTOENCODERS

## Slide 5

IDEA AND MOTIVATION
• The main task is: how do we make an autoencoder into a
generative model?
5

## Slide 6

IDEA AND MOTIVATION
• It’s hard to find a good point even in a low-dimensional space:
5

## Slide 7

IDEA AND MOTIVATION
• The main idea of the variational autoencoder (Kingma et al.,
2013): let every point x map not to a single point z but to an
entire distribution 𝑝(x|z):
5

## Slide 8

IDEA AND MOTIVATION
• The intuition is that the decoder has to be stable to small
changes in z; this is, in a way, an improved version of a
denoising autoencoder
• We want to cover the space of latent codes with «wide enough»
distributions:
5

## Slide 9

IDEA AND MOTIVATION
• But there is a problem: if we just train an autoencoder, it will be
easier for it to decode «narrow» distributions, and we will
ultimately get to distributions with zero variance, i.e., to a
regular autoencoder that does not really help us
• How do we solve this problem?
5

## Slide 10

IDEA AND MOTIVATION
• We have to add a constraint on 𝑝(x|z), i.e., regularize it:
5

## Slide 11

IDEA AND MOTIVATION
• There are now two questions left:
• how do we choose the loss function and regularizer?
• how can we pass gradients through the sampling process?
• Let us answer both of these questions...
5

## Slide 12

VARIATIONAL APPROXIMATIONS IN THE VAE
• Let’s start from the beginning: we want to train an encoder to
find good latent codes z from images x and train a decoder that
turns z back into x.
• We can decompose the joint distribution 𝑝(x, z) differently:
𝑝(z) 𝑝(x|z) = 𝑝(x, z) = 𝑝(x) 𝑝(z|x)
6

## Slide 13

VARIATIONAL APPROXIMATIONS IN THE VAE
• Here:
• 𝑝(x) is the distribution of images,
• 𝑝(z) is the distribution of latent codes, i.e., a simple distribution
we can sample from;
• the other two we need to find, they are the encoder distribution
𝑝(z|x) and the decoder distribution 𝑝(x|z).
6

## Slide 14

VARIATIONAL APPROXIMATIONS IN THE VAE
• To get a generative model we need to train both 𝑝(x|z) and
𝑝(z|x).
• But we have a simple 𝑝(z) and a very complex 𝑝(x)!
• This means that we have to pick one:
• either we assume that 𝑝(x|z) is simple and then look for a
complex 𝑝(z|x);
• or, vice versa, assume that 𝑝(z|x) is simple and then look for a
complex 𝑝(x|z).
6

## Slide 15

VARIATIONAL APPROXIMATIONS IN THE VAE
• VAE chooses the first option: suppose that
𝑝(x|z) = 𝑁(x|𝑓(z), 𝑐I) ,
where
𝑓(z) = Decoder(z)
• On the left we have 𝑝(z|x) times 𝑝(z) = 𝑁(z|0, I), i.e., a
Gaussian again.
6

## Slide 16

VARIATIONAL APPROXIMATIONS IN THE VAE
• On the right, we will be looking for an approximation
𝑞(z) ≈𝑝(z|x):
• Namely a variational approximation...
6

## Slide 17

VARIATIONAL APPROXIMATIONS IN THE VAE
• Let us derive the variational approximation from first principles:
𝑝(x, z) = 𝑝(x) 𝑝(z|x) ,
log 𝑝(x) = log 𝑝(x, z) −log 𝑝(z|x) ,
take the expectation over 𝑞(z):
𝔼𝑞(z) [log 𝑝(x)] = 𝔼𝑞(z) [log 𝑝(x, z)] −𝔼𝑞(z) [log 𝑝(z|x)] ,
and then do standard transformations:
log 𝑝(x) =𝔼𝑞(z) [log 𝑝(x, z)] −𝔼𝑞(z) [log 𝑞(z)] +
+ 𝔼𝑞(z) [log 𝑞(z)] −𝔼𝑞(z) [log 𝑝(z|x)] ,
log 𝑝(x) = ∫𝑞(z)log 𝑝(x, z)
𝑞(z) dz + ∫𝑞(z)log 𝑞(z)
𝑝(z|x)dz.
6

## Slide 18

VARIATIONAL APPROXIMATIONS IN THE VAE
• We get that
log 𝑝(x) = 𝐿(𝑞) + KL (𝑞(𝑧) ‖𝑝(z|x)) ,
where
𝐿(𝑞) = ∫𝑞(z)log 𝑝(x, z)
𝑞(z) dz.
6

## Slide 19

VARIATIONAL APPROXIMATIONS IN THE VAE
• Thus, we can approximate 𝑝(z|x) with 𝑞(z) by maximizing 𝐿(𝑞).
In the case of VAE it is easy to find:
𝐿(𝑞) = ∫𝑞(z)log 𝑝(x, z)
𝑞(z) dz = ∫𝑞(z)log 𝑝(z) 𝑝(x|z)
𝑞(z)
dz
= ∫𝑞(z)log 𝑝(x|z)dz + ∫𝑞(z)log 𝑝(z)
𝑞(z)dz
= ∫𝑞(z)log 𝑁(x|𝑓(z), 𝑐I)dz −KL (𝑞(z) ‖𝑝(z))
= −1
2𝑐𝔼𝑞(z) [‖x −𝑓(z)‖
2] −KL (𝑞(z) ‖𝑝(z)) .
6

## Slide 20

VARIATIONAL APPROXIMATIONS IN THE VAE
• And thus we have arrived at exactly what our intuition predicted:
6

## Slide 21

VARIATIONAL APPROXIMATIONS IN THE VAE
• But now we know exactly what 𝐿rec looks like, and it is also easy
to find the KL divergence between two Gaussians:
KL (𝑞(z) ‖𝑝(z)) = 1
2
𝑑
∑
𝑗=1
(𝜎2
x,𝑗+ 𝜇2
x,𝑗−log 𝜎2
x,𝑗−1) .
• This leads to the final loss function for the variational
autoencoder:
𝐿(𝑞) = −1
2𝑐𝔼𝑞(z) [‖x −𝑓(z)‖
2]−1
2
𝑑
∑
𝑗=1
(𝜎2
x,𝑗+ 𝜇2
x,𝑗−log 𝜎2
x,𝑗−1) .
• It only remains to solve the sampling problem...
6

## Slide 22

REPARAMETRIZATION TRICK
• To train the model, we need to pass the gradients through z
back to the encoder, but we can’t go through sampling
• Reparametrization trick: let us first sample and then transform
the result
7

## Slide 23

REPARAMETRIZATION TRICK
• Now we have all components firmly in place: we sample a
mini-batch of u for an input mini-batch of x and use it for
training
7

## Slide 24

DIFFUSION MODELS

## Slide 25

DIFFUSION MODELS
• (Sohl-Dickstein et al., 2015): Deep Unsupervised Learning using
Nonequilibrium Thermodynamics
• An idea from statistical physics: let us train a Markov chain that
will gradually turn random noise into the distribution we want
• To do that, let us start with a chain that turns the distribution
we want into random noise:
9

## Slide 26

DIFFUSION MODELS
• And then let us try to reverse each step:
• If we succeed, then later we can start from random noise and
move backwards:
9

## Slide 27

DIFFUSION MODELS
• Forward diffusion: let us start with 𝑝(x0) and add Gaussian
noise:
𝑞(x𝑡∣x𝑡−1) = 𝑁(x𝑡∣√1 −𝛽𝑡x𝑡−1, 𝛽𝑡I) .
• Then x0 gradually turns into noise, say, in 𝑇steps:
𝑞(x1∶𝑇∣x0) =
𝑇
∏
𝑡=1
𝑞(x𝑡∣x𝑡−1) .
9

## Slide 28

DIFFUSION MODELS
• And for each 𝑡we can sample x𝑡in closed form via the
reparametrization trick: let 𝜖∼𝑁(0, I) and denote 𝛼𝑡= 1 −𝛽𝑡,
𝐴𝑡= ∏
𝑇
𝑖=1 𝛼𝑖; then
x𝑡= √𝛼𝑡x𝑡−1 + √1 −𝛼𝑡𝜖= √𝛼𝑡𝛼𝑡−1x𝑡−2 + √1 −𝛼𝑡𝛼𝑡−1𝜖= …
… = √𝐴𝑡x0+√1 −𝐴𝑡𝜖, that is 𝑞(x𝑡∣x0) = 𝑁(x𝑡∣√𝐴𝑡x0, (1 −𝐴𝑡) I) ,
because when we add two Gaussians 𝑁(0, 𝜎2
1I) and 𝑁(0, 𝜎2
1I),
we get a Gaussian 𝑁(0, (𝜎2
1 + 𝜎2
2) I), and in our case this is
(1 −𝛼𝑡) + 𝛼𝑡(1 −𝛼𝑡) = 1 −𝛼𝑡𝛼𝑡−1.
9

## Slide 29

DIFFUSION MODELS
• And now the task, it would seem, is to reverse this process, to
learn how to sample from 𝑞(x𝑡−1 ∣x𝑡)
9

## Slide 30

DIFFUSION MODELS
• For small 𝛽𝑡the reverse distributions will also be Gaussian, but
their parameters now depend on the data points.
• Reverse diffusion: now we need to train the distributions
𝑝𝜃(x0∶𝑇) = 𝑝𝜃(x𝑇)
𝑇
∏
𝑡=1
𝑝𝜃(x𝑡−1 ∣x𝑡) ,
where
𝑝𝜃(x𝑡−1 ∣x𝑡) = 𝑁(x𝑡−1∣𝜇𝜃(x𝑡, 𝑡), Σ𝜃(x𝑡, 𝑡)) .
9

## Slide 31

DIFFUSION MODELS
• If we knew x0, we could reverse it analytically, by the way:
𝑞(x𝑡−1 ∣x𝑡, x0) = 𝑞(x𝑡∣x𝑡−1, x0) 𝑞(x𝑡−1 ∣x0)
𝑞(x𝑡∣x0)
∝
∝𝑒
−1
2 ( (x𝑡−√𝛼𝑡x𝑡−1)2
𝛽𝑡
+ (x𝑡−1−√𝐴𝑡−1x0)2
1−𝐴𝑡−1
+ (x𝑡−√𝐴𝑡x0)2
1−𝐴𝑡
),
and in this formula we now need to complete the square in
x𝑡−1...
9

## Slide 32

DIFFUSION MODELS
• This yields
𝑞(x𝑡−1 ∣x𝑡, x0) = 𝑁(x𝑡−1∣̃𝜇(x𝑡, x0) ,̃ 𝛽𝑡I) ,
wherẽ
𝛽𝑡= 1 −𝐴𝑡−1
1 −𝐴𝑡
⋅𝛽𝑡,̃
𝜇(x𝑡, x0) =
√𝛼𝑡(1 −𝐴𝑡−1)
1 −𝐴𝑡
x𝑡+ √𝐴𝑡−1𝛽𝑡
1 −𝐴𝑡
x0,
and since we know that x𝑡= √𝐴𝑡x0 + √1 −𝐴𝑡𝜖,̃
𝜇(x𝑡, x0) =
1
√𝐴𝑡
(x𝑡−
1 −𝛼𝑡
√1 −𝐴𝑡
𝜖𝑡) .
9

## Slide 33

DIFFUSION MODELS
• Ultimately we want the reverse diffusion to reconstruct 𝑞(x0)
from a standard input into x𝑛; roughly like this:
9

## Slide 34

DIFFUSION MODELS
• What should we do? As always in Bayesian inference,
approximate!
• At each step the model should become a good approximation to
𝑞(x𝑡∣x𝑡−1), without conditioning on the unknown x0:
9

## Slide 35

DIFFUSION MODELS
• To obtain this approximation, we need a variational lower
bound, similar to the one we had in VAE and DALL-E
• We start with a bound on the global distribution
𝑞(x1∶𝑇∣x0) = 𝑞(x1, … , x𝑇∣x0):
• And then it will decompose into bounds for the individual steps
of the diffusion process
9

## Slide 36

DIFFUSION MODELS
• Let us recall the idea of variational approximations:
𝑝(x, z) = 𝑝(x) 𝑝(z|x) ,
log 𝑝(x) = log 𝑝(x, z) −log 𝑝(z|x) ,
let us take the expectation over 𝑞(z):
𝔼𝑞(z) [log 𝑝(x)] = 𝔼𝑞(z) [log 𝑝(x, z)] −𝔼𝑞(z) [log 𝑝(z|x)] ,
and then do the standard manipulations:
log 𝑝(x) =𝔼𝑞(z) [log 𝑝(x, z)] −𝔼𝑞(z) [log 𝑞(z)] +
+ 𝔼𝑞(z) [log 𝑞(z)] −𝔼𝑞(z) [log 𝑝(z|x)] ,
log 𝑝(x) = ∫𝑞(z)log 𝑝(x, z)
𝑞(z) dz + ∫𝑞(z)log 𝑞(z)
𝑝(z|x)dz.
9

## Slide 37

DIFFUSION MODELS
• In the end it turns out that
log 𝑝(x) = 𝐿(𝑞) + KL (𝑞(z) ‖𝑝(z|x)) ,
where
𝐿(𝑞) = ∫𝑞(z)log 𝑝(x, z)
𝑞(z) dz.
9

## Slide 38

DIFFUSION MODELS
• Let us derive the variational bound for the diffusion model
again from first principles:
log 𝑝𝜃(x0) = log 𝑝𝜃(x0, … , x𝑇) −log 𝑝𝜃(x1, … , x𝑇∣x0) ,
𝔼𝑞(x0) [log 𝑝𝜃(x0)] = 𝔼𝑞(x0∶𝑇) [log 𝑝𝜃(x0∶𝑇)]−𝔼𝑞(x0∶𝑇) [log 𝑝𝜃(x1∶𝑇∣x0)] =
= 𝔼𝑞(x0∶𝑇) [log
𝑝𝜃(x0∶𝑇)
𝑞(x1∶𝑇∣x0)] + 𝔼𝑞(x0∶𝑇) [log 𝑞(x1∶𝑇∣x0)
𝑝𝜃(x1∶𝑇∣x0)] .
• Here the second term is the KL divergence, and we get the loss
function as minus the variational lower bound:
𝐿= 𝔼𝑞(x0∶𝑇) [log 𝑞(x1∶𝑇∣x0)
𝑝𝜃(x0∶𝑇)
] ≥−𝔼𝑞(x0) [log 𝑝𝜃(x0)] .
9

## Slide 39

DIFFUSION MODELS
• This bound can be computed as a sum:
𝐿=𝔼𝑞[log 𝑞(x1∶𝑇∣x0)
𝑝𝜃(x0∶𝑇)
] = 𝔼𝑞[log
∏𝑇
𝑡=1 𝑞(x𝑡∣x𝑡−1)
𝑝𝜃(x𝑇) ∏𝑇
𝑡=1 𝑝𝜃(x𝑡−1 ∣x𝑡)
]
=𝔼𝑞[−log 𝑝𝜃(x𝑇) +
𝑇
∑
𝑡=1
log 𝑞(x𝑡∣x𝑡−1)
𝑝𝜃(x𝑡−1 ∣x𝑡) ]
=𝔼𝑞[−log 𝑝𝜃(x𝑇) +
𝑇
∑
𝑡=2
log 𝑞(x𝑡∣x𝑡−1)
𝑝𝜃(x𝑡−1 ∣x𝑡) + log 𝑞(x1 ∣x0)
𝑝𝜃(x0 ∣x1) ]
=𝔼𝑞[−log 𝑝𝜃(x𝑇) +
𝑇
∑
𝑡=2
log (𝑞(x𝑡∣x𝑡−1, x0)
𝑝𝜃(x𝑡−1 ∣x𝑡)
𝑞(x𝑡∣x0)
𝑞(x𝑡−1 ∣x0) ) + log 𝑞(x1 ∣x0)
𝑝𝜃(x0 ∣x1)]
=𝔼𝑞[−log 𝑝𝜃(x𝑇) +
𝑇
∑
𝑡=2
log 𝑞(x𝑡∣x𝑡−1, x0)
𝑝𝜃(x𝑡−1 ∣x𝑡)
+ log 𝑞(x𝑇∣x0)
𝑞(x1 ∣x0) + log 𝑞(x1 ∣x0)
𝑝𝜃(x0 ∣x1)]
=𝔼𝑞[log 𝑞(x𝑇∣x0)
𝑝𝜃(x𝑇)
+
𝑇
∑
𝑡=2
log 𝑞(x𝑡∣x𝑡−1, x0)
𝑝𝜃(x𝑡−1 ∣x𝑡)
−log 𝑝𝜃(x0 ∣x1)] .
9

## Slide 40

DIFFUSION MODELS
• In the end we obtain
𝐿=𝐿𝑇+ 𝐿𝑇−1 + … + 𝐿0,
where
𝐿𝑇=KL (𝑞(x𝑇∣x0) ‖𝑝𝜃(x𝑇)) ,
𝐿𝑡=KL (𝑞(x𝑡∣x𝑡+1, x0) ‖𝑝𝜃(x𝑡∣x𝑡+1)) ,
𝑡= 1, … , 𝑇−1,
𝐿0 = −log 𝑝𝜃(x0 ∣x1) .
9

## Slide 41

DIFFUSION MODELS
• These are all KL divergences between Gaussians, which can be
computed and substituted into the loss function
• For example, in 𝐿𝑡we use the Gaussian parametrization
𝑝𝜃(x𝑡−1 ∣x𝑡) = 𝑁(x𝑡−1∣𝜇𝜃(x𝑡, 𝑡), Σ𝜃(x𝑡, 𝑡))
and try to match its parameters with 𝑞(x𝑡∣x𝑡−1, x0). For the
mean, for example,
𝜇𝜃(x𝑡, 𝑡) ≈̃ 𝜇𝑡(x𝑡, x0) =
1
√𝐴𝑡
(x𝑡−
1 −𝛼𝑡
√1 −𝐴𝑡
𝜖𝑡) ,
and since we know x𝑡during training, we can parametrize the
noise directly:
𝑝𝜃(x𝑡−1 ∣x𝑡) = 𝑁(x𝑡−1∣1
√𝛼𝑡
(x𝑡−
1 −𝛼𝑡
√1 −𝐴𝑡
𝜖𝜃(x𝑡, 𝑡)) , Σ𝜃(x𝑡, 𝑡)) .
9

## Slide 42

DIFFUSION MODELS
• (Sohl-Dickstein et al., 2015) on its own did not work too well,
except perhaps on CIFAR:
9

## Slide 43

DDPM
• The next step: “Denoising Diffusion Probabilistic Models” (DDPM;
Ho et al., 2020)
• The same basic idea, the same structure of the loss function:
10

## Slide 44

DDPM
• But then DDPM makes the following observations:
• the variances of forward diffusion 𝛽𝑡are constant
hyperparameters, they are not trained, so all of the 𝑞’s are not
trained; since 𝑝𝜃(x𝑇) is a fixed distribution from which we will
sample, 𝐿𝑇is a constant;
• for the intermediate steps the variances in 𝑝𝜃(x𝑡∣x𝑡+1) are also
not trained, and one can find a simple closed form for 𝐿𝑡;
• most importantly, let us introduce a separate discrete decoder for
𝐿0; if the data consists of integers from 0 to 255, rescaled to [−1, 1]
(this is the natural representation for images), DDPM models
𝑝𝜃(x0 ∣x1) =
𝐷
∏
𝑖=1
∫
𝛿+(𝑥0,𝑖)
𝛿−(𝑥0,𝑖)
𝑁(𝑥∣𝜇𝜃,𝑖(x1) , 𝜎2
1) d𝑥,
where 𝑖runs over the pixels, 𝜇𝜃(x1) is the decoder, and the
integration limits are
1
255 on each side of 𝑥0,𝑖
• That is, one can substitute a different model at the last step and
use 𝜇𝜃(x1) without noise during sampling
10

## Slide 45

DDPM
• DDPM already gave excellent generation, comparable to the best
GANs of that time:
10

## Slide 46

DDIM
• The next step came very soon: “Denoising Diffusion Implicit
Models” (DDIM; Song et al., 2020)
• An important drawback of all diffusion models so far is that they
are very slow
• Generation has to go through all the diffusion steps, and there
are literally thousands of them, and they run sequentially, they
do not parallelize
• Song et al. mention that sampling from a trained GAN is about
1000 times faster than sampling from DDPM for the same image
size
11

## Slide 47

DDIM
• How can we speed up diffusion models?
• Song et al. generalize diffusion models and in particular DDPM
• The loss function 𝐿does not depend directly on the joint
distribution 𝑞(x1∶𝑇∣x0), only on the marginals 𝑞(x𝑡∣x0)
• This means that we can reuse the same loss function for a
different joint distribution, as long as it has the same marginals
• In particular, we can even generalize to non-Markovian diffusion
processes, provided that we can find a reverse Markov chain for
them:
11

## Slide 48

DDIM
• For DDIM we will define the diffusion process in terms of its
reverse form:
𝑞𝜎(x1∶𝑇∣x0) = 𝑞𝜎(x𝑇∣x0)
𝑇
∏
𝑡=2
𝑞𝜎(x𝑡−1 ∣x𝑡, x0) .
• Now we can express the forward diffusion distributions by
Bayes’ theorem:
𝑞𝜎(x𝑡∣x𝑡−1, x0) = 𝑞𝜎(x𝑡−1 ∣x𝑡, x0) 𝑞𝜎(x𝑡∣x0)
𝑞𝜎(x𝑡−1 ∣x0)
.
11

## Slide 49

DDIM
• And now we can show that the resulting process has exactly the
same marginals, so the reverse diffusion can be trained with the
same loss function, and it will be a Markov chain:
11

## Slide 50

DDIM
• So far this does not help much: we have extended the class of
distributions for forward diffusion, but sampling a new image
still has to go through all the steps of reverse diffusion
• But now, instead of approximating the random noise 𝜖𝑡that
leads from x𝑡to x𝑡+1, we can approximate the random noise 𝜖𝑡
that will lead directly from x0 to x𝑡+1!
• And when we move in the reverse direction, we approximate the
direction not toward x𝑡, but directly toward x0, and we can move
in that direction faster
11

## Slide 51

DDIM
• An illustration:
• It is hard to say which approximation is better, but now we have
separated the dependence of 𝜖𝑡on x0, and we can jump several
steps at once, moving from x𝑡to x𝑡+𝑘in one step with an
increased 𝜖!
11

## Slide 52

DDIM
• This led to a 10x–100x speedup compared to DDPM without loss
of quality:
11

## Slide 53

DDIM
• Generation in DDIMs does not have to be stochastic either; one
can set the variance of reverse diffusion to zero during
generation
• And now the latent code in the space x𝑇corresponds to exactly
one image, and DDIM is a good model for latent representations;
here, for example, are interpolations in the latent space:
• DDPM could not interpolate, because a great deal of noise is
dd d
h
d
l
h
11

## Slide 54

STABLE DIFFUSION

## Slide 55

STABLE DIFFUSION
• Another breakthrough came when this diffusion process started
to be used in latent space
• Stable Diffusion (Rombach, Blattmann et al., 2022):
13

## Slide 56

STABLE DIFFUSION
• Stable Diffusion (Rombach, Blattmann et al., 2022):
13

## Slide 57

STABLE DIFFUSION
• unCLIP, also known as DALL-E 2 (Ramesh et al., 2022), trains
𝑝(x|𝑦) = 𝑝(x|c, 𝑦) 𝑝(c|𝑦) ,
where the prior model 𝑝(c|𝑦) builds a CLIP embedding from text,
and in 𝑝(x|c, 𝑦) first a “noise” (prior) for the image is generated,
and then a diffusion model draws the image
13

## Slide 58

DALL-E 2
14

## Slide 59

MIDJOURNEY
15

## Slide 60

DIFFUSION TRANSFORMERS

## Slide 61

DIFFUSION TRANSFORMERS
• A fully modern architecture by now – DiT (Peebles, Xie, 2022)
• This is a latent diffusion model, but instead of a U-Net-like
architecture for the latent codes it uses a transformer
• The transformer input is an 𝐼× 𝐼× 𝐶tensor, ”patchified” into a
sequence of 𝑝× 𝑝patches of length 𝑇= (𝐼/𝑝)2; 𝑝is a
hyperparameter that affects complexity quadratically
17

## Slide 62

DIFFUSION TRANSFORMERS
• Then it is processed by DiT blocks; the interesting part here is
adaptive layer norm with parameters taken from the condition
17

## Slide 63

DIFFUSION TRANSFORMERS
• It turns out that DiTs are much more computationally efficient:
17

## Slide 64

DIFFUSION TRANSFORMERS
• Transformer GFlops are strongly correlated with quality, and
large DiT models use computation more efficiently:
17

## Slide 65

DIFFUSION TRANSFORMERS
• Good samples:
17

## Slide 66

FLUX
18

## Slide 67

FLUX
19

## Slide 68

FLUX
20

## Slide 69

FLUX
21

## Slide 70

FLUX
22

## Slide 71

FLUX
23

## Slide 72

FLUX
24

## Slide 73

FLUX
25

## Slide 74

FLUX
26

## Slide 75

WHAT'S NEXT?

## Slide 76

RECENT NEWS IN DIFFUSION MODELS
• What happened after DiT in diffusion models?
• DPM-Solver++ (Lu et al., 2022): how to speed up DDIM further?
• As we saw above, DDIM is a first-order step for integrating a
certain ODE
• But there is a whole science of how to solve ODEs better!
• Let us pick some multistep second- or third-order scheme; it
will reduce the local error, and in the end we will be able to take
even wider steps, and even fewer steps will be needed
28

## Slide 77

RECENT NEWS IN DIFFUSION MODELS
• For example, DPM-Solver++ is indeed more stable and works
better than other variants (which we will not discuss):
28

## Slide 78

RECENT NEWS IN DIFFUSION MODELS
• UniPC (Zhao et al., 2023): a “predictor-corrector”-type method
• They derive a universal correcting step (UniC) that can be added
after any base predictor to increase the order of accuracy
without additional model calls, and they derive the matching
UniP predictor
28

## Slide 79

RECENT NEWS IN DIFFUSION MODELS
• And the most interesting further development is, of course, flow
matching:
28

## Slide 80

RECENT NEWS IN DIFFUSION MODELS
• Many modern generative models are based on it:
• But that’s a different story...
28

## Slide 81

DEEP GENERATIVE MODELS
29

## Slide 82

THANK YOU!
Thank you for your attention!
30
