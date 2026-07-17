# Slides (extracted) — slides.pdf

## Slide 1

GRADIENT DESCENT AND GENERAL DL REMARKS
Sergey Nikolenko
Harbour Space University
June 10, 2026
Random facts:
• June 10 is the World Art Nouveau Day, celebrated on the anniversary of the death of Antoni
Gaudí and Ödön Lechner
• on June 10, 1692, Bridget Bishop was hanged at Gallows Hill near Salem, Massachusetts, for
"certaine Detestable Arts called Witchcraft and Sorceries"
• on June 10, 1829, the first boat race between the Universities of Oxford and Cambridge took
place on the Thames; Cambridge challenged Oxford to the race, but lost easily
• on June 10, 1935, surgeon Robert Smith drank his last drink, staying sober afterwards with
the help of another alcoholic, Bill Wilson; this date marks the birth of Alcoholics Anonymous
• on June 10, 1886, a government commission arrived at Neuschwanstein to formally
pronounce King Ludwig II of Bavaria insane and depose him
• on June 10, 1967, Israel and Syria agreed to a cease-fire, ending the Six-Day War
• on June 10, 1987, the June Democratic Struggle started in South Korea, and people protest
against the government; the demonstrations forced the military regime under president
Chun Doo-hwan to institute democratic reforms leading to the Sixth Republic
1

## Slide 2

GRADIENT DESCENT
AND COMPUTATIONAL GRAPHS

## Slide 3

GRADIENT DESCENT
• Gradient descent: take the gradient w.r.t. weights, move in that
direction.
• Formally: for an error function 𝐸, targets 𝑦, and model 𝑓with
parameters 𝜃,
𝐸(𝜃) =
∑
(x,𝑦)∈𝐷
𝐸(𝑓(x, 𝜃), 𝑦),
𝜃𝑡= 𝜃𝑡−1 −𝜂∇𝐸(𝜃𝑡−1) = 𝜃𝑡−1 −𝜂
∑
(x,𝑦)∈𝐷
∇𝐸(𝑓(x, 𝜃𝑡−1), 𝑦).
• So we need to sum over the entire dataset for every step?!..
3

## Slide 4

GRADIENT DESCENT
• Hence, stochastic gradient descent: after every training sample
update
𝜃𝑡= 𝜃𝑡−1 −𝜂∇𝐸(𝑓(x𝑡, 𝜃𝑡−1), 𝑦𝑡),
• In practice people usually use mini-batches, it’s easy to
parallelize and smoothes out excessive “stochasticity”.
• So far the only parameter is the learning rate 𝜂.
3

## Slide 5

GRADIENT DESCENT
• Lots of problems with 𝜂:
• We will get to them later, for now let’s concentrate on the
certainly required step: the derivatives.
3

## Slide 6

COMPUTATIONAL GRAPH, FROP AND BPROP
• Let us represent a function as a composition of simple functions
(“simple” means that we can take derivatives).
• Example – 𝑓(𝑥, 𝑦) = 𝑥2 + 𝑥𝑦+ (𝑥+ 𝑦)2:
4

## Slide 7

COMPUTATIONAL GRAPH, FROP AND BPROP
• This way we can take the gradient with the chain rule:
(𝑓∘𝑔)′(𝑥) = (𝑓(𝑔(𝑥)))′ = 𝑓′(𝑔(𝑥))𝑔′(𝑥).
• This simply means that an increment 𝛿𝑥results in
𝛿𝑓= 𝑓′(𝑔(𝑥))𝛿𝑔= 𝑓′(𝑔(𝑥))𝑔′(𝑥)𝛿𝑥.
• We only need to be able to take gradients, i.e., derivatives w.r.t.
vectors:
∇x𝑓= (
𝜕𝑓
𝜕𝑥1
⋮
𝜕𝑓
𝜕𝑥𝑛
) .
∇x(𝑓∘𝑔) = (
𝜕𝑓∘𝑔
𝜕𝑥1
⋮
𝜕𝑓∘𝑔
𝜕𝑥𝑛
) = (
𝜕𝑓
𝜕𝑔
𝜕𝑔
𝜕𝑥1
⋮
𝜕𝑓
𝜕𝑔
𝜕𝑔
𝜕𝑥𝑛
) = 𝜕𝑓
𝜕𝑔∇x𝑔.
4

## Slide 8

COMPUTATIONAL GRAPH, FROP AND BPROP
• Or, if 𝑓depends on 𝑥in several different ways,
𝑓= 𝑓(𝑔1(𝑥), 𝑔2(𝑥), … , 𝑔𝑘(𝑥)), the increment 𝛿𝑥now comes into
play several times:
𝜕𝑓
𝜕𝑥= 𝜕𝑓
𝜕𝑔1
𝜕𝑔1
𝜕𝑥+ … + 𝜕𝑓
𝜕𝑔𝑘
𝜕𝑔𝑘
𝜕𝑥=
𝑘
∑
𝑖=1
𝜕𝑓
𝜕𝑔𝑖
𝜕𝑔𝑖
𝜕𝑥.
∇x𝑓= 𝜕𝑓
𝜕𝑔1
∇x𝑔1 + … + 𝜕𝑓
𝜕𝑔𝑘
∇x𝑔𝑘=
𝑘
∑
𝑖=1
𝜕𝑓
𝜕𝑔𝑖
∇x𝑔𝑖.
• Note that we got matrix multiplication for the Jacobi matrix:
∇x𝑓= ∇xg∇g𝑓, where ∇xg = ⎛
⎜
⎜
⎜
⎝
𝜕𝑔1
𝜕𝑥1
…
𝜕𝑔𝑘
𝜕𝑥1
⋮
⋮
𝜕𝑔1
𝜕𝑥𝑛
…
𝜕𝑔𝑘
𝜕𝑥𝑛
⎞
⎟
⎟
⎟
⎠
.
4

## Slide 9

COMPUTATIONAL GRAPH, FROP AND BPROP
• Let’s now go back to the example:
4

## Slide 10

COMPUTATIONAL GRAPH, FROP AND BPROP
• Forward propagation: we compute 𝜕𝑓
𝜕𝑥by the chain rule.
4

## Slide 11

COMPUTATIONAL GRAPH, FROP AND BPROP
• Backpropagation: starting from the end node, go back as
𝜕𝑓
𝜕𝑔= ∑𝑔′∈Children(𝑔)
𝜕𝑓
𝜕𝑔′
𝜕𝑔′
𝜕𝑔.
4

## Slide 12

COMPUTATIONAL GRAPH, FROP AND BPROP
• Backprop is much better: we get all derivatives in a single pass
through the graph.
• Aaaand... that’s it! We can now take the gradients of any
complicated composition of simple functions.
• Which is all we need to apply gradient descent!
• The libraries – PyTorch, TensorFlow, theano – are actually
automatic differentiation libraries. This is their main function.
• So you can implement lots of “classical” models in TensorFlow
and train them by gradient descent.
• And live neurons can’t do that because you need two different
outputs to compute the value and the derivative.
4

## Slide 13

ACTIVATION FUNCTIONS

## Slide 14

ACTIVATION FUNCTIONS
• There are many different nonlinearities; let’s do a brief survey.
• Logistic sigmoid:
𝜎(𝑥) =
1
1 + 𝑒−𝑥.
6

## Slide 15

ACTIVATION FUNCTIONS
• Hyperbolic tangent:
tanh(𝑥) = 𝑒𝑥−𝑒−𝑥
𝑒𝑥+ 𝑒−𝑥
• Very similar, but zero is not a saturation point.
6

## Slide 16

ACTIVATION FUNCTIONS
• Heaviside step function:
step(𝑥) = {0,
if 𝑥< 0,
1,
if 𝑥> 0.
6

## Slide 17

ACTIVATION FUNCTIONS
• Rectified linear unit (ReLU):
ReLU(𝑥) = {0,
if 𝑥< 0,
𝑥,
if 𝑥≥0.
6

## Slide 18

ACTIVATION FUNCTIONS
• Mathematical motivation for ReLU:
𝜎(𝑥+ 1
2) + 𝜎(𝑥−1
2) + 𝜎(𝑥−3
2) + 𝜎(𝑥−5
2) + … .
6

## Slide 19

ACTIVATION FUNCTIONS
• Biological motivation for ReLU:
𝑓(𝐼) =
⎧
{
⎨
{
⎩
(𝜏log 𝐸+𝑅𝐼−𝑉reset
𝐸+𝑅𝐼−𝑉𝑡ℎ)
−1 ,
if 𝐸+ 𝑅𝐼> 𝑉𝑡ℎ,
0,
if 𝐸+ 𝑅𝐼≤𝑉𝑡ℎ,
6

## Slide 20

ACTIVATION FUNCTIONS
• There are several ReLU variations: softplus(𝑥) = ln (1 + 𝑒𝑥) ,
LReLU(𝑥) = {𝑎𝑥,
if 𝑥< 0,
𝑥,
if 𝑥> 0;
ELU(𝑥) = {𝛼(𝑒𝑥−1) ,
𝑥< 0,
𝑥,
𝑥≥0.
−5
−4
−3
−2
−1
0
1
−1.00
−0.75
−0.50
−0.25
0.00
0.25
0.50
0.75
1.00
ReLU activation
Softplus
Leaky ReLU, a = 1
5
Leaky ReLU, a =
1
20
Exponential linear unit, α = 1.0
Exponential linear unit, α = 1
5
6

## Slide 21

ACTIVATION FUNCTIONS
• But that’s only the beginning. Ramachandran et al. (2017) did an
automated search over the function space and found Swish:
Swish(𝑥) = 𝑥𝜎(𝛽𝑥) =
𝑥
1 + 𝑒−𝛽𝑥
• (Misra, 2019): Mish(𝑥) = 𝑥tanh (softplus(𝑥)) = 𝑥tanh (ln (1 + 𝑒𝑥))
−0 5
0.0
0.5
1.0
1.5
2.0
ReLU activation
Swish activation, β = 1
Swish activation, β = 5
Mish activation
6

## Slide 22

ACTIVATION FUNCTIONS
• But the most interesting development happened in 2020...
• (Ma et al., 2020): let’s consider a smooth generalization of the
maximum
𝑆𝛽(𝑥1, … , 𝑥𝑛) = ∑
𝑛
𝑖=1 𝑥𝑖𝑒𝛽𝑥𝑖
∑
𝑛
𝑖=1 𝑒𝛽𝑥𝑖.
• And let’s substitute two functions of 𝑥in there, i.e., hard
maximum max (𝑔(𝑥), ℎ(𝑥)) will correspond to
𝑆𝛽(𝑔(𝑥), ℎ(𝑥)) = 𝑔(𝑥)
𝑒𝛽𝑔(𝑥)
𝑒𝛽𝑔(𝑥) + 𝑒𝛽ℎ(𝑥) + ℎ(𝑥)
𝑒𝛽ℎ(𝑥)
𝑒𝛽𝑔(𝑥) + 𝑒𝛽ℎ(𝑥) =
= 𝑔(𝑥)𝜎(𝛽(𝑔(𝑥) −ℎ(𝑥))) + ℎ(𝑥)𝜎(𝛽(ℎ(𝑥) −𝑔(𝑥))) =
= (𝑔(𝑥) −ℎ(𝑥)) 𝜎(𝛽(𝑔(𝑥) −ℎ(𝑥))) + ℎ(𝑥).
6

## Slide 23

ACTIVATION FUNCTIONS
• Ma et al. called it ActivateOrNot (ACON). Now this construction
generalizes everything:
• for 𝑔(𝑥) = 𝑥and ℎ(𝑥) = 0 the hard maximum is
ReLU(𝑥) = max(𝑥, 0), and the soft maximum is
𝑓𝐴𝐶𝑂𝑁−𝐴(𝑥, 0) = 𝑆𝛽(𝑥, 0) = 𝑥𝜎(𝛽𝑥) ,
i.e., precisely Swish!
• for 𝑔(𝑥) = 𝑥and ℎ(𝑥) = 𝑎𝑥for some 𝑎< 1, the hard maximum is
LReLU(𝑥) = max(𝑥, 𝑝𝑥), and the soft maximum is
𝑓𝐴𝐶𝑂𝑁−𝐵= 𝑆𝛽(𝑥, 𝑎𝑥) = (1 −𝑎) 𝑥𝜎(𝛽(1 −𝑎)𝑥) + 𝑎𝑥;
6

## Slide 24

ACTIVATION FUNCTIONS
• Ma et al. called it ActivateOrNot (ACON). Now this construction
generalizes everything:
• and this can be straightforwardly generalized to
𝑓𝐴𝐶𝑂𝑁−𝐶= 𝑆𝛽(𝑎1𝑥, 𝑎2𝑥) = (𝑎1 −𝑎2) 𝑥𝜎(𝛽(𝑎1 −𝑎2)𝑥) + 𝑎2𝑥;
now 𝑎1 and 𝑎2 can be learnable parameters, and intuitively it’s just
the limits of the derivative on both sides:
lim
𝑥→∞
d𝑓𝐴𝐶𝑂𝑁−𝐶
d𝑥
= 𝑎1,
lim
𝑥→−∞
d𝑓𝐴𝐶𝑂𝑁−𝐶
d𝑥
= 𝑎2.
6

## Slide 25

ACTIVATION FUNCTIONS
• Here is ACON-C for different parameter values:
−4
−3
−2
−1
0
1
2
3
4
−0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
ACON-C, a1 = 1, a2 = 0, β = 1
ACON-C, a1 = 1.2, a2 = −0.1, β = 1
ACON-C, a1 = 1, a2 = −0.8, β = 1
ACON-C, a1 = 1, a2 = −0.8, β = 0.1
ACON-C, a1 = 1, a2 = −0.8, β = 0.01
6

## Slide 26

ACTIVATION FUNCTIONS
• Ma et al. show that by tuning the parameters one can win a lot
even in bog-standard tasks:
• I haven’t seen much of ACON-C in actual practice, but this just
goes to show that deep learning has a lot of not-very-hidden
depths even in the simplest things.
6

## Slide 27

VARIATIONS OF
GRADIENT DESCENT

## Slide 28

GRADIENT DESCENT
• “Vanilla” gradient descent:
x𝑘= x𝑘−1 −𝛼∇𝑓(x𝑘).
• So much depends on the learning rate 𝛼.
• First idea — let 𝛼decrease with time:
• linear decay:
𝛼= 𝛼0 (1 −𝑡
𝑇) ;
• exponential decay:
𝛼= 𝛼0𝑒−𝑡
𝑇.
8

## Slide 29

GRADIENT DESCENT
• There’re a lot of results here. Wolfe conditions: if we are solving
minx 𝑓(x), and on step 𝑘we already know the direction p𝑘
where to go (e.g., p𝑘= ∇x𝑓(x𝑘)), i.e., we need to solve
min𝛼𝑓(x𝑘+ 𝛼p𝑘), then:
• for 𝜙𝑘(𝛼) = 𝑓(x𝑘+ 𝛼p𝑘) we have 𝜙′
𝑘(𝛼) = ∇𝑓(x𝑘+ 𝛼p𝑘)⊤p𝑘, and if
p𝑘is the descent direction then 𝜙′
𝑘(0) < 0;
• the step size 𝛼must satisfy the Armijo rule:
𝜙𝑘(𝛼) ≤𝜙𝑘(0) + 𝑐1𝛼𝜙′
𝑘(0) for some 𝑐1 ∈(0, 1
2);
• or even stronger Wolfe’s rule: Armijo rule plus
|𝜙′
𝑘(𝛼)| ≤𝑐2|𝜙′
𝑘(0)|,
i.e., we’d like to decrease the projection of the gradient.
• We stop the process when ‖∇x𝑓(x𝑘)‖2 ≤𝜖or
‖∇x𝑓(x𝑘)‖2 ≤𝜖‖∇x𝑓(x0)‖2 (why square, btw?).
8

## Slide 30

GRADIENT DESCENT
• Let’s see what happens if the scale is different: for a function
𝑓(𝑥, 𝑦) = 1
2𝑥2 + 𝜌
2𝑦2 →min𝑥,𝑦
• For elongated “valleys” (variables with different scale) we get a
lot of superfluous iterations, everything is very slow.
• Much better to be adaptive; but how?
8

## Slide 31

GRADIENT DESCENT
• The best thing in life is, of course, Newton’s method: let’s scale
back with the Hessian
g𝑘= ∇x𝑓(x𝑘), 𝐻𝑘= ∇2
x𝑓(x𝑘), and x𝑘+1 = x𝑘−𝛼𝑘𝐻−1
𝑘g𝑘.
• Armijo rule is applicable here as well:
𝛼𝑘∶
𝑓(x𝑘+1) ≤𝑓(x𝑘) −𝑐1𝛼𝑘𝑔⊤
𝑘𝐻−1
𝑘g𝑘, 𝑐1 ≈10−4.
• Would be very nice but, alas, you can’t just compute 𝐻𝑘.
8

## Slide 32

GRADIENT DESCENT
• There are approximations.
• Conjugate gradients, quasi-Newtonian methods...
• L-BFGS (limited memory Broyden–Fletcher–Goldfarb–Shanno):
• construct an approximation to 𝐻−1;
• to do that, save updates of the arguments and then express 𝐻−1
through them.
• Important open question: can we make L-BFGS or something
similar work for deep learning?
• Doesn’t work so far, mostly because you do need to be able to
compute the gradient.
• And we aren’t. Wait, what?..
8

## Slide 33

STOCHASTIC GRADIENT DESCENT
• We are usually dealing with stochastic gradient descent:
x𝑡= x𝑡−1 −𝛼∇𝑓(x𝑡, x𝑡−1, 𝑦𝑡).
• With mini-batches, too. How do we understand this formally?
• We are usually dealing with stochastic optimization problems:
𝐹(x) = 𝔼𝑞(y)𝑓(x, y) →min
x
∶
• empirical risk minimization:
𝐹(x) = 1
𝑁
𝑁
∑
𝑖=1
𝑓𝑖(x) = 𝔼𝑖∼U(1,…,𝑁)𝑓𝑖(x) →min
x ;
• variational lower bound (ELBO) minimization... but later about that
(if ever).
• So what are mini-batches, then?
9

## Slide 34

STOCHASTIC GRADIENT DESCENT
• Simply empirical estimates of a random function from a sample:̂
𝐹(x) = 1
𝑚
𝑚
∑
𝑖=1
𝑓(x, y𝑖),̂
g(x) = 1
𝑚
𝑚
∑
𝑖=1
∇x𝑓(x, y𝑖).
• Very good estimates: unbiased, converging (albeit slowly), easy
to compute.
• In general, that’s how you motivate stochastic gradient descent
(SGD), it’s a Monte-Carlo approach. But there are problems...
9

## Slide 35

STOCHASTIC GRADIENT DESCENT
• SGD problems:
• never goes in the right direction,
• even at the exact optimum of 𝐹(x) the step is nonzero, i.e., it
cannot converge with a constant step size,
• we know neither 𝐹(x) nor ∇𝐹(x), i.e., we cannot use Armijo and
Wolfe’s rules.
9

## Slide 36

STOCHASTIC GRADIENT DESCENT
• Nevertheless, we can try to analyze an SGD iteration for
𝐹(x) = 𝔼𝑞(y)𝑓(x, y) →minx:
x𝑘+1 = x𝑘−𝛼𝑘̂g𝑘,
𝔼̂g𝑘= g𝑘= ∇𝐹(x𝑘).
• Let’s estimate the residue of a point on some iteration:
‖x𝑘+1 −xopt‖2 = ‖x𝑘−𝛼𝑘̂g𝑘−xopt‖2 =
= ‖x𝑘−xopt‖2 −2𝛼𝑘̂g⊤
𝑘(x𝑘−xopt) + 𝛼2
𝑘‖̂g𝑘‖2.
• Take expectation with respect to 𝑞(y) at time moment 𝑘:
𝔼‖x𝑘+1 −xopt‖2 = ‖x𝑘−xopt‖2 −2𝛼𝑘g⊤
𝑘(x𝑘−xopt) + 𝛼2
𝑘𝔼‖̂g𝑘‖2.
9

## Slide 37

STOCHASTIC GRADIENT DESCENT
• Assume for simplicity that 𝐹is convex:
𝐹(xopt) ≥𝐹(x𝑘) + g⊤
𝑘(x𝑘−xopt)
9

## Slide 38

STOCHASTIC GRADIENT DESCENT
• We had
𝔼‖x𝑘+1 −xopt‖2 = ‖x𝑘−xopt‖2 −2𝛼𝑘g⊤
𝑘(x𝑘−xopt) + 𝛼2
𝑘𝔼‖̂g𝑘‖2,
𝐹(xopt) ≥𝐹(x𝑘) + g⊤
𝑘(x𝑘−xopt).
• Therefore,
𝛼𝑘(𝐹(x𝑘) −𝐹(xopt)) ≤𝛼𝑘g⊤
𝑘(x𝑘−xopt) =
= 1
2‖x𝑘−xopt‖2 + 1
2𝛼2
𝑘𝔼‖̂g𝑘‖2 −1
2𝔼‖x𝑘+1 −xopt‖2.
9

## Slide 39

STOCHASTIC GRADIENT DESCENT
• Take the expectation of the left-hand side and sum up:
𝑘
∑
𝑖=0
𝛼𝑖(𝔼𝐹(x𝑖) −𝐹(xopt)) ≤
≤1
2‖x0 −xopt‖2 + 1
2
𝑘
∑
𝑖=0
𝛼2
𝑖𝔼‖̂g𝑖‖2 −1
2𝔼‖x𝑘+1 −xopt‖2 ≤
≤1
2‖x0 −xopt‖2 + 1
2
𝑘
∑
𝑖=0
𝛼2
𝑖𝔼‖̂g𝑖‖2.
• We got the sum of function values at different points with
weights 𝛼𝑖. What do we do now?
9

## Slide 40

STOCHASTIC GRADIENT DESCENT
• Use convexity:
𝔼𝐹(∑𝑖𝛼𝑖x𝑖
∑𝑖𝛼𝑖
) −𝐹(xopt) ≤
≤∑𝑖𝛼𝑖(𝔼𝐹(x𝑖) −𝐹(xopt)
∑𝑖𝛼𝑖
≤
1
2‖x0 −xopt‖2 + 1
2 ∑
𝑘
𝑖=0 𝛼2
𝑖𝔼‖̂g𝑖‖2
∑𝑖𝛼𝑖
.
• The estimate is on the value in a linear combination of points
(in practice there is no difference or it’s even better to take the
last point).
• If ‖x0 −xopt‖ ≤𝑅and 𝔼‖̂g𝑘‖2 ≤𝐺2 then
𝔼𝐹(̂x𝑘) −𝐹(xopt) ≤𝑅2 + 𝐺2 ∑
𝑘
𝑖=0 𝛼2
𝑖
2 ∑
𝑘
𝑖=0 𝛼𝑖
.
9

## Slide 41

STOCHASTIC GRADIENT DESCENT
• The main bound regarding SGD:
𝔼𝐹(̂x𝑘) −𝐹(xopt) ≤𝑅2 + 𝐺2 ∑
𝑘
𝑖=0 𝛼2
𝑖
2 ∑
𝑘
𝑖=0 𝛼𝑖
.
• 𝑅is an estimate for the initial residue, and 𝐺is an estimate of
something like the variance of the stochastic gradient.
• For instance, for constant step size 𝛼𝑖= ℎ
𝔼𝐹(̂x𝑘) −𝐹(xopt) ≤
𝑅2
2ℎ(𝑘+ 1) + 𝐺2ℎ
2
→𝑘→∞
𝐺2ℎ
2 .
9

## Slide 42

STOCHASTIC GRADIENT DESCENT
• SGD summary:
• SGD comes to an “uncertainty region” of radius 1
2𝐺2ℎ, and it is
proportional to step size;
• the faster we go, the faster we arrive there but the larger the
uncertainty region will be, i.e., we need to reduce the learning rate
with time;
• SGD converges slowly: full GD for convex functions has residue
𝑂(1/𝑘), while SGD has only 𝑂(1/
√
𝑘);
• but far from the uncertainty region we still have 𝑂(1/𝑘) residue for
constant learning rate, i.e., it slows down only near the optimum,
and generally our goal is to reach the uncertainty region;
• but it still depends on 𝐺, and this will be especially important for
neurobayesian approaches.
9

## Slide 43

SGD WITH MOMENTUM
• We need some improvements, need to do something with the
learning rate.
• Better not decrease it too quickly.
• But this does not take into account 𝐹itself, anyway.
10

## Slide 44

SGD WITH MOMENTUM
• SGD with momentum: let’s keep part of the velocity, like inertia
in physics.
• We get
𝑢𝑡= 𝛾𝑢𝑡−1 + 𝜂∇x𝐹(x),
x = x −𝑢𝑡.
• We preserve 𝛾𝑢𝑡−1 from the previous step.
10

## Slide 45

SGD WITH MOMENTUM
• But we already know we will get to the intermediate point 𝛾𝑢𝑡−1.
• Let’s compute the gradient right there!
10

## Slide 46

SGD WITH MOMENTUM
• Nesterov’s momentum:
𝑢𝑡= 𝛾𝑢𝑡−1 + 𝜂∇x𝐹(x −𝛾𝑢𝑡−1)
10

## Slide 47

SGD WITH MOMENTUM
• The problems are still there, of course:
• Can we do even better?..
10

## Slide 48

ADAPTIVE GRADIENT DESCENT
• Previously, we had the same learning rate in all directions.
• Idea: let’s move faster along the axes that do not change much
and slower along the faster changing parameters.
11

## Slide 49

ADAPTIVE GRADIENT DESCENT
• Adagrad: let’s take into account the history of updates.
• Denoting 𝑔𝑡,𝑖= ∇w𝑖𝐿(w), we get
w𝑡+1,𝑖= w𝑡,𝑖−
𝜂
√𝐺𝑡,𝑖𝑖+ 𝜖⋅𝑔𝑡,𝑖,
where 𝐺𝑡is a diagonal matrix with 𝐺𝑡,𝑖𝑖= 𝐺𝑡−1,𝑖𝑖+ 𝑔2
𝑡,𝑖that
stores the total value of the gradient along the entire learning
history.
• Thus, learning rate keeps decreasing but at different rates for
different w𝑖.
• What’s the problem with Adagrad?
11

## Slide 50

ADAPTIVE GRADIENT DESCENT
• Problem: 𝐺keeps increasing, and the learning rate will never
rebound.
• Adadelta (Zeiler, 2012) – same idea with two modifications.
• First, we store an exponential average of the history:
𝐺𝑡,𝑖𝑖= 𝜌𝐺𝑡−1,𝑖𝑖+ (1 −𝜌)𝑔2
𝑡,𝑖.
• And then do the same kind of update:
u𝑡= −
𝜂
√𝐺𝑡−1 + 𝜖
g𝑡−1.
11

## Slide 51

ADAPTIVE GRADIENT DESCENT
• Second, we need to take “units of measurement” into account.
• There was a problem in previous approaches:
• in regular gradient descent or with momentum the “units” of
parameter updates Δw are the units of gradient, i.e., if the weights
are in seconds and objective function is in meters the gradient will
be measures in meters per second, and we are subtracting meters
per second from seconds; they might have completely different
scales;
• in Adagrad the values of Δw resulted from ratios of gradients, so
the updates were dimensionless; not so good as well.
11

## Slide 52

ADAPTIVE GRADIENT DESCENT
• Tnis problem does not arise in second order optimization:
parameter update Δw is proportional to 𝐻−1∇w𝑓, i.e.,
Δw ∝𝐻−1∇w𝑓∝
𝜕𝑓
𝜕w
𝜕2𝑓
𝜕w2
∝dimension of w.
• To fix Adadelta, let’s use another exponential average, now of
the squares of parameter updates.
• We approximate it with previous steps:
𝔼[Δw2]𝑡= 𝜌𝔼[Δw2]𝑡−1 + (1 −𝜌)Δw2, where
𝑢𝑡= −
√𝔼[Δw2]𝑡−1 + 𝜖
√𝐺𝑡−1 + 𝜖
⋅𝑔𝑡−1.
11

## Slide 53

ADAPTIVE GRADIENT DESCENT
• Sometimes you also hear about RMSprop (no real reference,
Hinton’s lectures).
• It’s basically the same as Adadelta, but RMSprop does not use
the second idea with changing measurement units:
𝑢𝑡= −
𝜂
√𝐺𝑡−1 + 𝜖
⋅𝑔𝑡−1.
11

## Slide 54

ADAPTIVE GRADIENT DESCENT
• Finally, Adam (Kingma, Ba, 2014) arrived.
• A modification of Adagrad with smoothed versions of mean and
mean squared gradients:
𝑚𝑡= 𝛽1𝑚𝑡−1 + (1 −𝛽1)𝑔𝑡,
𝑣𝑡= 𝛽2𝑣𝑡−1 + (1 −𝛽2)𝑔2
𝑡,
𝑢𝑡=
𝜂
√𝑣+ 𝜖𝑚𝑡.
• (Kingma, Ba, 2014) recommend 𝛽1 = 0.9, 𝛽2 = 0.999, 𝜖= 10−8.
• Adam virtually does not need tuning and is very often used in
practice.
• ...[http://ruder.io/optimizing-gradient-descent/]...
11

## Slide 55

ADAPTIVE GRADIENT DESCENT
• Nadam (Dozat, 2016), a combination of Adam and Nesterov’s
momentum:
11

## Slide 56

ADAPTIVE GRADIENT DESCENT
• A slightly more general view – all of this looks as follows:
• vanilla stochastic gradient descent:
w𝑘+1 = w𝑘−𝛼𝑘̃∇𝑓(w𝑘), wherẽ ∇𝑓(w𝑘) = ∇𝑓(w𝑘; x𝑖𝑘);
• SGD with momentum:
w𝑘+1 = w𝑘−𝛼𝑘̃∇𝑓(w𝑘+ 𝛾𝑘(w𝑘−w𝑘−1)) + 𝛽𝑘(w𝑘−w𝑘−1) ;
• adaptive SGD:
w𝑘+1 = w𝑘−𝛼𝑘𝐻−1
𝑘̃ ∇𝑓(w𝑘+ 𝛾𝑘(w𝑘−w𝑘−1))+𝛽𝑘𝐻−1
𝑘𝐻𝑘−1 (w𝑘−w𝑘−1) ,
where usually 𝐻𝑘= diag ([∑
𝑘
𝑖=1 𝜂𝑖g𝑖∘g𝑖]
1/2
), where
g𝑘=̃ ∇𝑓(w𝑘+ 𝛾𝑘(w𝑘−w𝑘−1)) (i.e., 𝐻𝑘is a diagonal matrix whose
elements are square roots of linear combinations of squares of
the previous gradients).
• Adaptive methods are trying to adapt to the data space
geometry, while basic SGD uses the standard 𝐿2-geometry with
𝐻𝑘= I.
11

## Slide 57

ADAM, ADAMW, AND OTHER ANIMALS
• When Adam appeared, it was all the buzz:
• But then people realized it’s not that simple. Researchers often
used plain vanilla SGD instead. Why?
12

## Slide 58

ADAM, ADAMW, AND OTHER ANIMALS
• The Marginal Value of Adaptive Gradient Methods in Machine
Learning (Wilson et al., 2017)
• Basic conclusions:
• when the problem has several global minima, different algorithms
can find different solutions from the same initial point;
• in particular, adaptive methods can lead to overfitting, i.e., local
solutions that generalize poorly;
• and this is not just the theoretical worst case but also happens in
practice.
12

## Slide 59

ADAM, ADAMW, AND OTHER ANIMALS
• The Marginal Value of Adaptive Gradient Methods in Machine
Learning (Wilson et al., May 2017)
12

## Slide 60

ADAM, ADAMW, AND OTHER ANIMALS
• But Adam is still great at the beginning.
• That’s why people suggested to, e.g., switch from Adam to SGD at
the right time (Keskar, Socher, Dec 2017)
• But this is not the whole story either...
12

## Slide 61

ADAM, ADAMW, AND OTHER ANIMALS
• Fixing Weight Decay Regularization in Adam (Loshchilov, Hutter,
Feb 2018):
• weight decay is usually assumed to be the same as
𝐿2-regularization;
• but it turns out that’s not quite true for adaptive methods;
• let’s dig a little deeper...
12

## Slide 62

ADAM, ADAMW, AND OTHER ANIMALS
• Original weight decay (Hanson, Pratt, 1988):
x𝑡+1 = (1 −𝑤)x𝑡−𝜂∇𝑓𝑡(x𝑡),
where 𝑤is the weight decay rate, 𝜂is the learning rate.
• It is obviously equivalent to changing 𝑓:
𝑓reg
𝑡
(x𝑡) = 𝑓𝑡(x𝑡) + 𝑤
2 ‖x𝑡‖2
2.
• Or, easier still, changing the gradient:
∇𝑓reg
𝑡
(x𝑡) = ∇𝑓𝑡(x𝑡) + 𝑤x𝑡.
• That’s all true but...
12

## Slide 63

ADAM, ADAMW, AND OTHER ANIMALS
• ...but doesn’t work already even with momentum:
• We see that x𝑡decays by 𝛼𝑤x𝑡−1, not by 𝑤x𝑡−1; to get the same
behaviour we need to set 𝑤𝑡= 𝛼
𝛼′ 𝛿, and now hyperparameters 𝛼
and 𝑤are connected.
• Easy solution: let’s move decay to the change of x𝑡itsefl (line 9)
and add scaling to 𝜂𝑡.
12

## Slide 64

ADAM, ADAMW, AND OTHER ANIMALS
• The same happens with Adam:
• In basic Adam, weights with large gradients decay less, which is
not always a good idea.
• AdamW restores the original behaviour.
12

## Slide 65

ADAM, ADAMW, AND OTHER ANIMALS
• And now the hyperparameters disentangle much better:
12

## Slide 66

ADAM, ADAMW, AND OTHER ANIMALS
• And the generalization is better too:
12

## Slide 67

SUPER-CONVERGENCE AND AMSGRAD
• Two more interesting ideas.
• Super-Convergence (Smith, Topin, 2017): let’s change the
learning rate cyclically.
• A combination of curriculum learning (Bengio et al., 2009) and
classical simulated annealing.
• But this does not reproduce in a stable way.
13

## Slide 68

SUPER-CONVERGENCE AND AMSGRAD
• Another idea with a similar destiny – amsgrad (Reddi et al.,
2018), ICLR 2018 best paper!
• Idea:
• exponential average in Adam/RMSprop can hurt convergence;
• in particular, the proof of Adam’s convergence was wrong;
• while AMSGrad keeps the maximal gradient size, and that’s better.
• But this is not really confirmed in practice either...
13

## Slide 69

THANK YOU!
Thank you for your attention!
14
