# Transcript — whisper_cpp

- **Provider:** whisper_cpp
- **Language:** en
- **Audio duration:** 3:15:11
- **Segments:** 5593
- **model:** ggml-large-v3-turbo.bin
- **vad:** True
- **beam_size:** 5
- **entropy_thold:** 2.8
- **latency_sec:** 1438.57

## Segments

**[00:12 – 00:25]** Good morning, everyone. We continue our investigations of machine learning and yesterday we finally got to neural networks.

**[00:25 – 00:34]** We got to our main topic of the class and we will be discussing neural networks for the rest of our time.

**[00:35 – 00:42]** But still, I'm glad that we went over some fundamentals and I hope they have been interesting and instructive for you.

**[00:43 – 00:52]** So maybe just as a quick recap first, what we did yesterday and where we are right now.

**[00:53 – 01:16]** So we discussed, yesterday we discussed things like linear models, but basically linear models or more complicated classical machine learning models like, I don't know, regression tree boosting or Gaussian processes or

**[01:16 – 01:33]** some probabilistic models with some, I don't know, variational clustering or whatever, all of these models followed classically the same pattern, followed the same structure.

**[01:33 – 01:46]** So you have your high dimensional input, like images, sound, videos, whatever, then you do feature extraction, right?

**[01:46 – 01:59]** We discussed that yesterday, then you get something like a vector of features and then you do your ML model, right?

**[01:59 – 02:05]** And the whole point and the ML model now gives you the output which you need.

**[02:06 – 02:08]** This is the Y and this is the X.

**[02:09 – 02:19]** So classical models, in classical machine learning, what people would do, they would think and do feature extraction manually.

**[02:19 – 02:50]** And the main advantage of deep learning when it came on, and by now we have many more advantages, but the main revolution, like the contents of the deep learning revolution of the late 2000s or early 2010s, was that this manual feature extraction switched to end-to-end learning of a single model, which was the neural network, right?

**[02:50 – 02:58]** So now in deep learning, mostly this is all a big neural network, right?

**[02:59 – 03:21]** And when we implement it, when we run it, it's just a single thing that we don't need to distinguish, but inside, of course, there is the first part, the main part, that still does the feature extraction, and then it produces the semantically relevant features,

**[03:21 – 03:49]** the features that are, by virtue of training, the most meaningful features for the output that we want, and then we do the final layer, which is, again, one of these linear models usually, either linear regression if we predict a number, or logistic regression if we do classification, as we actually usually do.

**[03:51 – 03:58]** It's rare to have numbers as outputs. We will have examples like that, but it's not really common.

**[03:58 – 04:18]** So then, what else we did yesterday? We started talking about the structure of neural networks, but we only started talking about individual perceptrons, individual artificial neurons.

**[04:18 – 04:40]** And this was, I think, where we stopped. We discussed that a common structure of a single unit in the neural network of the perceptron is a linear combination of the inputs followed by a non-linearity.

**[04:40 – 05:04]** And I think we didn't do, yesterday we didn't do a real survey of these functions, of activation functions, but it's a pretty short topic and let's just get it out of the way now.

**[05:04 – 05:26]** So what kinds of activation functions can be used in neurons? So again, we discussed yesterday that the whole point of neural networks is to take structures like this, to take small elementary functions like this, and then do like a computational graph based on them.

**[05:26 – 05:59]** And when you do a computational graph based on elementary functions that you understand, elementary functions that are easy, when you do compositions of easy things, like we discussed with this connectionism principle, which is basically just true, when you compose a lot of simple things, you can get some very complicated results.

**[05:59 – 06:28]** Of course, the question is, how do you tweak your composition in such a way that the result is what you want? And this is the whole point of deep learning, right? Training such big compositions, finding their weights, learning their weights. But at least theoretically, as soon as you have any kind of non-linearity here, you can more or less approximate anything you want.

**[06:30 – 06:51]** So our first topic for today, a brief one, will be what are the non-linearities that people actually use? And it's an interesting question, actually. It's a bit more interesting, maybe, than you would expect.

**[06:52 – 07:07]** So originally, in, I don't know, in 1943, in the original McCulloch-Pitts paper, and in 1958, in Frank Rosenblatt's Perceptron, people used threshold functions.

**[07:07 – 07:26]** So, the activation would be a threshold, have a side-step function, call it what you want, but basically there would be an A, and the rule would be if W times X is over A, then 1, else 0, right?

**[07:26 – 07:45]** This is a fine function if all you have is a single perceptron, then it's okay, you can do learning on this and everything more or less works, and that's how the original perceptron worked.

**[07:45 – 07:50]** But you can't really do networks of these guys, right?

**[07:50 – 08:00]** So I told you yesterday that you can't do networks of linear perceptrons because if the perceptrons are linear, then it doesn't make any sense to do a network.

**[08:00 – 08:08]** A composition of linear functions is linear again, so you just get your whole network equivalent to a single perceptron.

**[08:08 – 08:11]** Well, with these guys, it's not true.

**[08:11 – 08:15]** With these guys, there are universal approximation theorems.

**[08:15 – 08:22]** You can definitely approximate whatever you want, but you can't find this approximation, unfortunately,

**[08:22 – 08:29]** because the only way we have to train such big compositions--

**[08:29 – 08:32]** and that will be our main topic for today, actually--

**[08:32 – 08:37]** the only way to train such compositions is gradient descent and other techniques

**[08:37 – 08:46]** that are based on local movements of the weights, on local properties of the loss function.

**[08:46 – 08:55]** And when you have a piecewise constant activation function, gradients don't work.

**[08:55 – 08:59]** I mean, formally, they work, but they're just equal to zeros, right?

**[08:59 – 09:04]** The f' is equal to zero here, f' is equal to zero here.

**[09:04 – 09:14]** And when you sit over here with your w times x and you move to your w slightly,

**[09:14 – 09:19]** maybe you go here, maybe you go here, but the answer doesn't change.

**[09:19 – 09:23]** And the derivative is always zero and we don't know where to go, right?

**[09:23 – 09:29]** So these guys definitely don't work for networks.

**[09:29 – 09:33]** So what did people do?

**[09:33 – 09:37]** People looked at these threshold activations.

**[09:37 – 09:46]** They still had this idea that a threshold activation is supposed to be good.

**[09:46 – 09:52]** A threshold activation is like what we are actually trying to achieve.

**[09:52 – 09:55]** Like a neuron is either activated or not.

**[09:55 – 10:00]** And we want to have a big composition of neurons

**[10:00 – 10:04]** that are in various states of activated or not activated.

**[10:04 – 10:08]** But we cannot have this strict jump.

**[10:08 – 10:12]** So let's have a soft approximation to it.

**[10:12 – 10:18]** So for quite a while, throughout all of this classical phase

**[10:18 – 10:24]** of early neural networks up until 2011 or 12, I think,

**[10:24 – 10:30]** mostly people used sigmoid activation functions.

**[10:30 – 10:37]** And so when people say a sigmoid function,

**[10:37 – 10:47]** what they actually mean is that there is a horizontal asymptote on the left,

**[10:47 – 10:50]** there is a horizontal asymptote on the right,

**[10:50 – 10:54]** and the function monotonically goes like this

**[10:54 – 10:58]** from negative infinity to positive infinity.

**[10:58 – 11:03]** So the proverbial example, the archetypal example of a sigmoid

**[11:03 – 11:06]** is the logistic sigmoid, which we discussed yesterday.

**[11:06 – 11:12]** So sigma of a is one over one plus e to the power of minus a.

**[11:12 – 11:14]** It goes from zero to one.

**[11:14 – 11:16]** It's symmetrical.

**[11:16 – 11:22]** It doesn't have zero derivatives anywhere, et cetera, et cetera.

**[11:22 – 11:28]** And so there have been, there was a lot of,

**[11:28 – 11:32]** there were a lot of neural networks in the 1990s, 1980s, 2000s

**[11:32 – 11:38]** with activation functions like this and also with other sigmoids.

**[11:38 – 11:41]** So I won't go into details. It doesn't matter for us now.

**[11:41 – 11:48]** But for technical reasons, it's not really good that your sigmoid saturates at zero.

**[11:48 – 11:55]** So it's a separate technical problem that you don't really want to approximate zero.

**[11:55 – 12:03]** So a better sigmoid for at least internal layers would be something that goes from one to, say, minus one.

**[12:03 – 12:10]** And then it would be symmetrical around zero, actually.

**[12:10 – 12:20]** And actually, a more common sigmoid function for neural networks was the hyperbolic tangent.

**[12:20 – 12:24]** And I always forget where the minuses are.

**[12:24 – 12:32]** a to the power minus a minus, plus, plus, minus, I guess like this.

**[12:32 – 12:37]** I guess it's like this, yeah.

**[12:37 – 12:41]** So it goes to one on positive infinity.

**[12:41 – 12:45]** It goes to minus, yeah, right, it goes to minus one on negative infinity.

**[12:45 – 12:51]** And again, it's symmetrical, blah, blah, blah, same kind of thing.

**[12:51 – 12:57]** So people were using these sigmoid functions all the way through about,

**[12:57 – 13:06]** I don't remember the exact year, but about 2011 or 2012.

**[13:06 – 13:13]** And in 2011, 2012, there was a very influential paper,

**[13:13 – 13:16]** a very important remark,

**[13:16 – 13:20]** that where people tried a completely different activation function,

**[13:20 – 13:25]** a very, very simple one, and it turned out to work extremely well.

**[13:25 – 13:30]** So the function that they tried is called ReLU,

**[13:30 – 13:38]** which stands for Rectified Linear Unit and Linear Unit.

**[13:38 – 13:46]** And it basically goes like this.

**[13:46 – 13:52]** So on the negative part of the inputs over here,

**[13:52 – 13:54]** it's just zero.

**[13:54 – 13:58]** And on the positive part, it's just x.

**[13:58 – 14:00]** It equals to the input.

**[14:00 – 14:05]** So ReLU of A is...

**[14:05 – 14:09]** Formally, you can write it like max of zero and A,

**[14:09 – 14:13]** or you can write it with one Boolean operator.

**[14:13 – 14:19]** So 1 if A greater than zero, L is zero.

**[14:19 – 14:22]** That's it. Sorry, not 1, A.

**[14:22 – 14:28]** If A greater than zero, L is zero.

**[14:28 – 14:29]** That's it.

**[14:29 – 14:37]** And it proved to be a very cool, very nice activation function.

**[14:37 – 14:42]** So what were the benefits?

**[14:42 – 14:45]** Well, first of all, I just told you

**[14:45 – 14:51]** that it's now good to have piecewise constant activation functions

**[14:51 – 14:53]** because the gradients are zero.

**[14:53 – 14:58]** And indeed, if you go through a ReLU,

**[14:58 – 15:02]** if you go through a neuron,

**[15:02 – 15:05]** through a unit with ReLU activation,

**[15:05 – 15:10]** and you have a negative argument for ReLU.

**[15:10 – 15:14]** So if your W times A falls over here,

**[15:14 – 15:17]** or W times X falls over here,

**[15:17 – 15:19]** then you don't learn anything.

**[15:19 – 15:22]** So it's just straight zero,

**[15:22 – 15:24]** it propagates as zero,

**[15:24 – 15:26]** and when you go back, your gradients stop there.

**[15:26 – 15:28]** We don't yet know what it means to go back,

**[15:28 – 15:32]** but we'll understand it just now, just today.

**[15:32 – 15:37]** But in this case, it's okay.

**[15:37 – 15:40]** In many architectures,

**[15:40 – 15:42]** it's okay to have this kind of sparsity,

**[15:42 – 15:45]** and it's even a good thing to have this kind of sparsity.

**[15:45 – 15:48]** So in, for example, convolutional architectures,

**[15:48 – 15:52]** which we will discuss, I suppose, in our next lectures,

**[15:52 – 15:54]** in convolutional architectures,

**[15:54 – 15:58]** you have the same weights reused a lot of times

**[15:58 – 16:01]** all across the input.

**[16:01 – 16:05]** And when you have the same weights reused all across the input,

**[16:05 – 16:07]** it's fine and it's even desirable

**[16:07 – 16:10]** to have like half of them just zeroed out.

**[16:10 – 16:14]** So that's not really a problem.

**[16:14 – 16:19]** And it turned out that it's really a good property

**[16:19 – 16:22]** to have unbounded activations like this.

**[16:22 – 16:27]** So with any kind of sigmoids,

**[16:27 – 16:29]** you have this problem of saturation.

**[16:29 – 16:34]** You have the derivatives of your activation function

**[16:34 – 16:38]** go to zero on the left and on the right.

**[16:38 – 16:40]** Here the S will go to zero on the left immediately,

**[16:40 – 16:42]** but on the right they don't.

**[16:42 – 16:46]** And this means that this sigmoid, no sigmoid can distinguish

**[16:46 – 16:51]** between activated, really activated, and super-duper activated.

**[16:51 – 16:54]** It just activated.

**[16:54 – 16:58]** And what's even worse, when you go to this regime,

**[16:58 – 17:01]** when your input, when your sigmoid becomes,

**[17:01 – 17:04]** when your neuron becomes very sure in what it does,

**[17:04 – 17:08]** when the arguments to the sigmoid become large in absolute value,

**[17:08 – 17:10]** you stop hearing.

**[17:10 – 17:15]** So your derivatives are very close to zero, and the gradients just stop.

**[17:15 – 17:19]** Here, you explicitly stop on the negative side,

**[17:19 – 17:21]** but on the positive side, you never stop.

**[17:21 – 17:25]** You just keep learning, which is also great.

**[17:25 – 17:28]** So in a way, it's...

**[17:28 – 17:31]** And there is even a mathematical result about this.

**[17:31 – 17:34]** I don't remember if I have it on the slides.

**[17:34 – 17:36]** Maybe I do.

**[17:36 – 17:39]** Let me skip this, activation functions.

**[17:39 – 17:43]** Yeah, and there is even a mathematical result that says,

**[17:43 – 17:47]** well, if you take a few sigmoids and you stack them together,

**[17:47 – 17:51]** like an infinite series of sigmoids and you stack them together,

**[17:51 – 17:56]** what you get is more or less the real.

**[17:56 – 18:02]** So if you add up this series, of course, you don't get this exact kink at zero.

**[18:02 – 18:04]** Of course, it will be smooth.

**[18:04 – 18:10]** But then it will very soon asymptotically be just y equals x.

**[18:10 – 18:14]** It will go to a straight line and it will stay being a straight line.

**[18:14 – 18:20]** So in a way, the real activation is like staking a lot of sigmoids

**[18:20 – 18:27]** and looking how many of them actually activate, which is, of course, more information.

**[18:27 – 18:32]** So this is a good thing.

**[18:32 – 18:35]** What else do I want to say here?

**[18:35 – 18:38]** Oh, and there is...

**[18:38 – 18:43]** Yeah, sorry about the Russian on the picture, but there is also a very interesting remark here

**[18:43 – 18:47]** that connects back to what we discussed yesterday about the brains.

**[18:47 – 18:52]** Actually, if you look at how our biological neurons activate,

**[18:52 – 18:56]** it does look like a real activation function.

**[18:56 – 19:04]** So this is like a good model or whatever of the firing rates of neurons,

**[19:04 – 19:10]** basically of their activation strength, how much they're excited.

**[19:10 – 19:14]** And it looks like this black curve over here.

**[19:14 – 19:18]** So at first it doesn't go negative, of course.

**[19:18 – 19:25]** But then from zero for a while it just stays non-inactive, not activated at all.

**[19:25 – 19:29]** Then there is this complicated phase transition.

**[19:29 – 19:33]** But after the complicated phase transition, we basically get a straight line,

**[19:33 – 19:37]** which is pretty cool.

**[19:37 – 19:43]** I mean, it's pretty interesting and unexpected that it would be actually a straight line,

**[19:43 – 19:45]** but it looks like it is.

**[19:45 – 19:48]** Of course, it doesn't go to infinity.

**[19:48 – 19:51]** Please do not experiment with that.

**[19:51 – 19:56]** No, if you apply a thousand volts to your brain, you will not think faster and better.

**[19:56 – 19:59]** This will not end well. Do not do that.

**[19:59 – 20:03]** Of course, it saturates in real life and biology.

**[20:03 – 20:15]** But in a computer, it doesn't have to saturate, or at least we can stretch the straight line however far we want.

**[20:15 – 20:22]** Of course, these are just additional considerations.

**[20:22 – 20:26]** These are just some interesting facts about the real...

**[20:26 – 20:30]** Of course, the real bonus was that it worked very well.

**[20:30 – 20:38]** So in practice, as soon as people... it wasn't a new idea, real activations existed since the 1970s or something.

**[20:38 – 20:47]** But as soon as people tried them with real networks, with convolutional networks especially,

**[20:47 – 20:57]** and they saw the results in about 2011-2012, mostly everyone switched to realos.

**[20:57 – 20:59]** Of course, it did not stop there.

**[20:59 – 21:03]** So there has been a lot of further research on activation functions.

**[21:03 – 21:06]** There have been interesting results.

**[21:06 – 21:11]** So what was the next step?

**[21:11 – 21:18]** Well, the first next step was kind of straightforward.

**[21:18 – 21:29]** So I said that in some situations it is desirable to have this sparse UTM.

**[21:29 – 21:40]** In some situations it is a good thing to zero out some of the activations over here.

**[21:40 – 21:43]** But in other situations it's not.

**[21:43 – 21:48]** And when you don't want to lose the gradient flow through your network,

**[21:48 – 21:56]** when you don't want to be sparse, then of course you'd want something non-zero on the left.

**[21:56 – 22:02]** So the immediate modification was what we call a leaky relo.

**[22:02 – 22:06]** Basically the same thing, but on the left you also have a straight line,

**[22:06 – 22:14]** but it's a straight line which has a smaller slope than on the right.

**[22:14 – 22:21]** So it's still just a single hinge, a connection of two straight lines at zero,

**[22:21 – 22:26]** but now it's non-zero on the left.

**[22:26 – 22:34]** And then what people did at around 2017, I think,

**[22:34 – 22:43]** was they ran an automated search for the best possible activation function.

**[22:43 – 22:50]** And I do want to discuss this a little bit because we will see examples like that later also.

**[22:50 – 22:57]** So if you look at your activation functions, what are they?

**[22:57 – 23:03]** Like, what is their nature? They are just straightforward mathematical functions of one variable, right?

**[23:03 – 23:06]** Just a function in the high school sense of the word.

**[23:06 – 23:13]** And what is the representation of this? How do you represent functions?

**[23:13 – 23:16]** What is the structure of these guys?

**[23:16 – 23:21]** Well, they're defined by formulas, right? And what is a formula?

**[23:21 – 23:28]** A formula is a computational graph. So for example, how does ReLU look?

**[23:28 – 23:35]** What does ReLU look like? Well, you have your input, x, you have a constant zero,

**[23:35 – 23:40]** and then you have a maximum, and you have your output.

**[23:40 – 23:46]** Okay, very simple computational graph. Two inputs, one of them, a constant, and that's it.

**[23:46 – 23:57]** What about the logistic sigmo? Well, you have x, you have 1, you have, for example...

**[23:57 – 24:01]** I mean, I'm just making an example. You can define functions in a different way.

**[24:01 – 24:08]** But, for example, here, there is a unary function e to the power minus argument.

**[24:08 – 24:14]** And then there is plus 1. And then there is the inverse, right? Go 1 over.

**[24:14 – 24:17]** And as a result, you get sigma of x.

**[24:17 – 24:26]** For a hyperbolic tangent, you have x, you have e to the power, you have e to the negative power.

**[24:26 – 24:37]** And then you subtract, and then you add, and then you divide, and you get your hyperbolic tangent, right?

**[24:37 – 24:38]** And so on.

**[24:38 – 24:46]** So a function, if you write it as a formula, what the formula actually is, what is a formula is a mathematical object.

**[24:46 – 24:47]** It's a graph.

**[24:47 – 24:54]** It's a graph composed of elementary functions of operations that constitute this formula.

**[24:54 – 25:00]** And which means that you can sweep over these graphs, right?

**[25:00 – 25:02]** You can search through these graphs.

**[25:02 – 25:05]** I won't go into details on how exactly people do it.

**[25:05 – 25:07]** It doesn't matter for our class.

**[25:07 – 25:18]** But basically, at some point, they ran a very expensive search over a lot of graphs, a lot of activation functions like this.

**[25:18 – 25:22]** Of course, when you do a search like that, you cannot actually prove anything.

**[25:22 – 25:25]** There is no mathematical statement. It's all empirical, right?

**[25:25 – 25:39]** So you just try different stuff, you see what works better on the set of data sets, set of architectures that you set up,

**[25:39 – 25:43]** and then you just see what works better, right?

**[25:43 – 25:53]** And you see what works better, and you progress by mutating the graphs a little bit.

**[25:53 – 25:59]** It's basically an evolutionary thing usually because you can't take a gradient on the graph structure.

**[25:59 – 26:07]** So you need to do like crossover, like copying parts of one graph to the other, or small mutations, like change around things,

**[26:07 – 26:12]** see what works, go to the population of things that work, et cetera, et cetera.

**[26:12 – 26:15]** It's an evolutionary algorithm.

**[26:15 – 26:24]** And as a result, at that point, they came up with something called the switch activation function.

**[26:24 – 26:27]** Yeah, 2017, it was done by Google.

**[26:27 – 26:31]** Of course, who else would have all of that compute back in 2017?

**[26:31 – 26:37]** And the switch activation function, I mean, I cannot explain to you why it is better.

**[26:37 – 26:41]** I can only show it to you and say that, yeah, empirically it's better.

**[26:41 – 26:47]** So it looks kind of like a leaky ReLU, so it's very similar to ReLU on the right,

**[26:47 – 26:50]** and they are all very similar to ReLU on the right.

**[26:50 – 26:54]** And on the left, it at first goes like this, but then it goes back to zero.

**[26:54 – 26:59]** So it's not monotone, interestingly.

**[26:59 – 27:05]** And yeah, it proved to work better for some reason.

**[27:05 – 27:11]** And a lot of standard architectures, especially in computer vision, actually,

**[27:11 – 27:17]** you will see if you go inside, we won't go to that level of detail thinking class,

**[27:17 – 27:22]** but if you go inside, you will see that a lot of standard architectures actually use Swish activations.

**[27:22 – 27:27]** And of course, that is also not the end of the story.

**[27:27 – 27:37]** So let me, maybe, I don't want to spend too much time on that, but people keep doing that.

**[27:37 – 27:42]** These are experiments for yesterday.

**[27:42 – 27:47]** So I will publish this notebook as usual.

**[27:47 – 27:54]** These are the standard activations like threshold, logistics, sigmoid, hyperbolic tangent, and the ReLU.

**[27:54 – 27:59]** And then you have different leaky ReLUs, which are all the same on the right.

**[27:59 – 28:08]** You have exponential linear units, which is basically, again, a straight line on the right.

**[28:08 – 28:14]** And on the left is asymptotically going to somewhere curve.

**[28:14 – 28:21]** Then you have swishes, you have mish, which is a variant of swish, whatever, doesn't matter.

**[28:21 – 28:23]** And then, okay, let me skip that.

**[28:23 – 28:28]** And then you have this also pretty interesting function called the GLU,

**[28:28 – 28:31]** where G stands for Gaussian.

**[28:31 – 28:41]** And the Gaussian function is based on the cumulative distribution function of a standard Gaussian.

**[28:41 – 28:52]** So it also looks pretty much like a swish, but it's a little bit different.

**[28:52 – 28:56]** And again, so you can see the formula here.

**[28:56 – 29:02]** It's basically just the CDF of a Gaussian.

**[29:02 – 29:09]** And it's CDF of a Gaussian times X.

**[29:09 – 29:18]** And for some reason, it works better in many modern architectures.

**[29:18 – 29:23]** So I guess modern LLMs mostly use Chilo activations.

**[29:23 – 29:28]** Maybe there is a deep science behind it, but I'm just not an expert in that.

**[29:28 – 29:33]** I just wanted to mention that people are still working on ideas like this.

**[29:33 – 29:40]** But all of this is just...

**[29:40 – 29:47]** In a way, in this part, I just want to show you how all rabbit holes go deep.

**[29:47 – 29:53]** So wherever you look, you can find a long series of works.

**[29:53 – 29:56]** You can find a lot of different ideas.

**[29:56 – 30:03]** And for every idea, you will see some confirming experiments, of course, otherwise it wouldn't be published.

**[30:03 – 30:07]** Some may be even theoretical reasoning of why this idea is good.

**[30:07 – 30:11]** But then, you know, some ideas work out, some ideas disappear.

**[30:11 – 30:19]** And over here for activation functions, there was this like a different color.

**[30:19 – 30:27]** There was, I guess, the sequence of activations that you actually want to try is like ReLU, then Swish,

**[30:27 – 30:36]** then maybe GLU with the Gaussian linear unit, and maybe a Leaky ReLU as a variation.

**[30:36 – 30:44]** So that's where the field stands. Okay, don't want to spend more time on that.

**[30:44 – 30:52]** What I do want to spend a little bit more time on is, of course, backpropagation.

**[30:52 – 30:59]** So let me first motivate what we are going to talk about.

**[30:59 – 31:09]** And I know backpropagation is pretty simple, it's pretty straightforward, especially compared to what we've been talking about yesterday and the day before.

**[31:09 – 31:19]** But I still want to discuss it at least very quickly, because there is one or two points that I want to make in there.

**[31:19 – 31:28]** And also, well, I think it's worth reminding you about backpropagation.

**[31:28 – 31:37]** So, first of all, what problem are we solving? Where does backpropagation come from?

**[31:37 – 31:52]** Well, as we already discussed, a neural network is basically this huge function.

**[31:52 – 32:05]** So far, it's a small f, but this huge function, which computes, actually not even the output, but the function that computes the loss function for some input.

**[32:05 – 32:13]** So there are weights of the neural network. They constitute part of the inputs.

**[32:13 – 32:22]** There are inputs like the picture that we are classifying or whatever.

**[32:22 – 32:26]** This is x, and there is the correct answer, which is y.

**[32:26 – 32:32]** And the final output of a neural network on that would be the value of the loss function.

**[32:32 – 32:36]** So here it's still small l.

**[32:36 – 32:41]** Small l on x, y, and w, right?

**[32:41 – 32:48]** So, for example, if you are distinguishing between cats and dogs,

**[32:48 – 32:54]** what you actually do is this is your x, y is the cat class.

**[32:54 – 33:00]** So formally it's like, well, okay, since there are only two classes,

**[33:00 – 33:04]** let me just say it's one, as opposed to zero.

**[33:04 – 33:07]** If it was a dog, it would be zero.

**[33:07 – 33:12]** And then your picture, your input image goes through a very complicated neural network,

**[33:12 – 33:17]** and this very complicated neural network gives you, like, y hat, its prediction.

**[33:17 – 33:22]** And probably there was a logistic sigmoid at the end, as we discussed yesterday.

**[33:22 – 33:29]** But anyway, the output is y hat, which is like the estimated probability

**[33:29 – 33:31]** of the cat class, right?

**[33:31 – 33:37]** And then you can't take the gradient of that because you don't know where to go.

**[33:37 – 33:43]** To know where to go, you need to also combine it with the correct answer.

**[33:43 – 33:50]** And then here you compute the loss based on the prediction of your network

**[33:50 – 33:56]** and based on the correct answer.

**[33:56 – 34:03]** And the output in this case would be something like minus log y hat,

**[34:03 – 34:13]** which we are supposed to minimize so that y hat would grow and would be closer to 1.

**[34:13 – 34:18]** Minimize with respect to what? Minimize with respect to the weights.

**[34:18 – 34:22]** So this neural network has weights inside, the loss function probably doesn't have weights inside,

**[34:22 – 34:28]** but the neural network does have weights and we want to minimize it with respect to double.

**[34:28 – 34:30]** That's also not the end of the story, right?

**[34:30 – 34:32]** In machine learning, we don't have only one data point.

**[34:32 – 34:35]** We have lots of data points.

**[34:35 – 34:37]** We have a whole data set.

**[34:37 – 34:42]** So the actual loss function, capital L of W,

**[34:42 – 34:45]** now it's just of W, not of X and Y specifically,

**[34:45 – 34:47]** is something like the sum or the average.

**[34:47 – 34:48]** It doesn't matter, of course.

**[34:48 – 34:50]** We are just maximizing or minimizing.

**[34:50 – 34:55]** So it's the sum or the average of these small loss functions

**[34:55 – 35:03]** for every element in the dataset, right?

**[35:03 – 35:13]** So when we train, we are minimizing the average loss function on the dataset.

**[35:13 – 35:15]** Kind of makes sense.

**[35:15 – 35:17]** Maybe we have some weights inside.

**[35:17 – 35:18]** Maybe it's a bit more complicated.

**[35:18 – 35:22]** Maybe some samples are more important than others, whatever.

**[35:22 – 35:24]** For now, let's just stay simple.

**[35:24 – 35:28]** We want to minimize the total loss over the whole dataset.

**[35:28 – 35:33]** So we are minimizing this with respect to W.

**[35:33 – 35:36]** How do we do that?

**[35:36 – 35:42]** So I hope by now I've convinced you that this loss function

**[35:42 – 35:45]** is a very, very complicated function of W.

**[35:45 – 35:49]** I mean, we didn't even go into any architectures yet,

**[35:49 – 35:54]** but every architecture is also a huge composition of different stuff.

**[35:54 – 36:00]** But even in this formula, you can see that it's like a sum over the dataset.

**[36:00 – 36:07]** So it's a sum of a million terms, and every term is a pretty complicated function.

**[36:07 – 36:13]** So L of W is very complex.

**[36:13 – 36:16]** In practice, there are a lot of Ws.

**[36:16 – 36:20]** The length of the W vector is big.

**[36:20 – 36:25]** We are operating in high dimensions, almost inevitably.

**[36:25 – 36:57]** And L of W is hopelessly non-convex, is hopelessly complicated, and we definitely cannot hope to enumerate all possible Ws and look for the minimum or to do some complicated procedure here.

**[36:57 – 37:06]** Basically, almost all that we can do is to do some form of gradient descent.

**[37:06 – 37:13]** I will tell you later today why even slightly more complicated things fail.

**[37:13 – 37:28]** But basically, the only thing that works is to do gradient descent, which means update the weights locally with a rule like this one.

**[37:28 – 37:35]** So I want to make capital L smaller.

**[37:35 – 37:40]** So I am at point WK.

**[37:40 – 37:46]** On iteration K, I have the current checkpoint of the model and its weights are WK.

**[37:46 – 37:59]** So to get the next value of the weights, to get the next checkpoint, I subtract, I go in the direction opposite to the gradient.

**[37:59 – 38:03]** In the direction where the loss function decreases the quickest.

**[38:03 – 38:07]** I hope you know that already, right?

**[38:07 – 38:12]** So I want to go over here.

**[38:12 – 38:16]** I compute the gradient at point WK.

**[38:16 – 38:26]** And then I go slightly in the direction of this largest, of this most steepest slope downwards.

**[38:26 – 38:29]** This is the idea of gradient descent.

**[38:29 – 38:34]** We will see how it has evolved and where we are with gradient descent today.

**[38:34 – 38:37]** But the basic idea is still this.

**[38:37 – 38:45]** And what do we need to do to implement an iterative procedure like this to implement actual gradient descent?

**[38:45 – 38:53]** Well, if you look at the formula, you will see that the only thing that we really need to do is we need to be able to compute the gradient.

**[38:53 – 38:57]** That's it, right? After it's easy.

**[38:57 – 39:07]** So we need some kind of algorithm, we need some kind of procedure to compute gradients of big complicated functions.

**[39:07 – 39:18]** Well, we can't have a generic procedure for any function with however it is defined, but how is L defined?

**[39:18 – 39:23]** What do I mean actually physically when I say a big complicated function?

**[39:23 – 39:34]** Well, in neural networks, in deep learning, a complicated function is defined also as a computational graph, right?

**[39:34 – 39:48]** So what I actually have here is some kind of, so I have X, all of these different axes from the data set and the Ys and whatever.

**[39:48 – 40:00]** And they go into this impossibly complicated graph, but it's a directed acyclic graph that just does the computation from left to right.

**[40:00 – 40:05]** And we go through it and we can compute stuff.

**[40:05 – 40:09]** And then L falls out, right?

**[40:09 – 40:22]** So the assumption here is that this is a very big composition, but every element of this composition, every node in the graph is simple.

**[40:22 – 40:33]** It's simple enough that I can compute its values, compute all of the derivatives locally in this node, do anything I want inside this single node.

**[40:33 – 40:44]** Okay? So the single node is some kind of an elementary function. For example, this is a node, right?

**[40:44 – 40:53]** So it's just doing this dot product between two vectors. Very simple function. I definitely understand what the derivatives are, what the value is, blah, blah, blah.

**[40:53 – 41:01]** Or here is a node, an activation function, which is a fixed, known function of one variable, and of course I know it's derivative two.

**[41:01 – 41:10]** So I assume that my very complex function is computed through a computational graph of simple functions.

**[41:10 – 41:18]** And my task is, let's compute the gradient of this guy with respect to a part of the inputs.

**[41:18 – 41:24]** I didn't actually put the weights here, but they are also somewhere over here.

**[41:24 – 41:29]** And they're also part of the inputs for this computational graph.

**[41:29 – 41:34]** And I want to compute this at some specific point.

**[41:34 – 41:39]** So backpropagation is a way to do that.

**[41:39 – 41:40]** That's basically it.

**[41:40 – 41:48]** And to explain backpropagation, I think it's best to just go for an example.

**[41:48 – 41:56]** So let's, I don't know, you can give me some kind of polynomial of two variables.

**[41:56 – 41:57]** Usually that's enough.

**[41:57 – 42:01]** They give me an f of x and y.

**[42:01 – 42:13]** I don't know, some relatively complicated composition of simple things like pluses, squares, multiplications.

**[42:13 – 42:22]** I guess I'm not making myself clear what I want to see here, but something like, I don't know.

**[42:22 – 42:43]** Let's pull something out of x plus y squared times x squared plus y, plus xy maybe, something like this.

**[42:43 – 43:02]** It doesn't work too well. x plus y squared times x, okay, times x minus y plus y cubed or whatever.

**[43:02 – 43:05]** Let's put it this way. It doesn't really matter.

**[43:05 – 43:09]** So we have this kind of, okay, so for our example, we have this kind of function.

**[43:09 – 43:12]** And I write it as a formula, which means that I write it as a graph.

**[43:12 – 43:21]** Like we just discussed, it's a computational graph with elementary functions like plus, minus, squared, etc.

**[43:21 – 43:25]** So let me draw this graph.

**[43:25 – 43:35]** My question will be, I want to compute the gradient of f, so I want to compute df over dx and df over dy.

**[43:35 – 43:39]** That's the question.

**[43:39 – 43:43]** Let me draw the graph for you.

**[43:43 – 43:48]** I'm used to drawing it bottoms up, so here I have x and y.

**[43:48 – 43:50]** What do I do?

**[43:50 – 43:52]** I do a plus over here.

**[43:52 – 43:55]** I do a minus over here.

**[43:55 – 43:59]** x minus y, right?

**[43:59 – 44:03]** I do a cube over here.

**[44:03 – 44:07]** Then I do a square over here.

**[44:07 – 44:10]** Multiplication with the minus.

**[44:10 – 44:13]** And then I add the cube.

**[44:13 – 44:20]** Okay, so let me maybe go through this graph

**[44:20 – 44:22]** and put some letters here.

**[44:22 – 44:27]** So like, let's say a is x plus y.

**[44:27 – 44:29]** I want to denote the intermediate nodes here,

**[44:29 – 44:31]** the outputs of intermediate nodes.

**[44:31 – 44:34]** So b is x minus y.

**[44:34 – 44:37]** c is y cubed.

**[44:37 – 44:41]** d is a squared.

**[44:41 – 44:42]** Oh, perfect.

**[44:42 – 44:47]** e is d times b.

**[44:47 – 44:52]** And f, just like f, is e plus c.

**[44:52 – 44:56]** Okay, so notice what we've done.

**[44:56 – 44:59]** We've represented this function as a graph,

**[44:59 – 45:01]** which is exactly the same as a formula.

**[45:01 – 45:02]** When you write down a formula,

**[45:02 – 45:06]** you are actually writing down a graph like this one.

**[45:06 – 45:12]** And every single function in this graph is very, very simple.

**[45:12 – 45:17]** We know everything about taking the cube.

**[45:17 – 45:19]** We know what the derivative is.

**[45:19 – 45:21]** We know what the result is.

**[45:21 – 45:23]** Every function is simple.

**[45:23 – 45:25]** But we don't yet know, let's say,

**[45:25 – 45:30]** what is the global result of f.

**[45:30 – 45:33]** So what can we do with this graph?

**[45:33 – 45:37]** Well, first of all, we can use it to actually compute stuff.

**[45:37 – 45:43]** So we can, for example, let's say x is equal to 1,

**[45:43 – 45:47]** y is equal to, I don't know, minus 1.

**[45:47 – 45:52]** What will be the value of f?

**[45:52 – 45:54]** And we can go through this graph bottom-up,

**[45:54 – 45:56]** and compute every node, and we compute f,

**[45:56 – 45:58]** just like we would go through the formula, right?

**[45:58 – 46:08]** So in this case, a will be 0, b will be 2, c will be minus 1, d will be 0,

**[46:08 – 46:12]** oh, okay, it's too easy, but still, okay, e will be also 0,

**[46:12 – 46:17]** and f will be minus 1, okay.

**[46:17 – 46:18]** What else can we do?

**[46:18 – 46:23]** And this procedure, when we go bottom-up from the inputs to the output,

**[46:23 – 46:28]** this procedure is called forward propagation.

**[46:28 – 46:40]** So forward propagation or fprop is when you go from the inputs to the output, right?

**[46:40 – 46:43]** Bottom-up in this graph.

**[46:43 – 46:46]** And with forward propagation, of course, you can compute the value of the function.

**[46:46 – 46:49]** That's very straightforward.

**[46:49 – 46:55]** Interestingly, you can also compute derivatives with forward propagation.

**[46:55 – 46:56]** Isn't that right?

**[46:56 – 47:03]** So for example, let's say I want to compute df over dx.

**[47:03 – 47:09]** How do I compute df over dx while going bottoms up on this graph?

**[47:09 – 47:12]** Well, by induction, right?

**[47:12 – 47:21]** So I have the base of the induction which says dx over dx is 1, dy over dx is 0.

**[47:21 – 47:27]** Okay, now I go here and I say, oh, what is dA over dx?

**[47:27 – 47:34]** Well, since this is a plus, then dA over dx is dx over dx plus dy over dx.

**[47:34 – 47:38]** So it's 1 plus 0, it's 1.

**[47:38 – 47:44]** And so on. dB over dx will be 1 minus 0 will be 1.

**[47:44 – 47:51]** dC over dx will be 3 times y squared.

**[47:51 – 47:56]** Oh, sorry, I'm doing dx, it will be 0.

**[47:56 – 48:02]** I apologize. dC over dx will be 3y squared times dy over dx.

**[48:02 – 48:05]** And dy over dx is 0, so that will be 0.

**[48:05 – 48:18]** Now dD over dx is 2a times da over dx, right?

**[48:18 – 48:22]** And, okay, so let me maybe, sorry, let me change this example

**[48:22 – 48:27]** because all of these zeros will not be really interesting.

**[48:27 – 48:36]** So maybe let's say x is 2 and y is minus 1.

**[48:36 – 48:41]** So now here we have minus 1, here we have 3, here we have 9,

**[48:41 – 48:45]** here we have, oh sorry, here we have 1.

**[48:45 – 48:49]** I'm bad at arithmetic.

**[48:49 – 48:54]** Here we have 1, here we have 3, 1 times 3 is 3, and 3 minus 1 is 2.

**[48:54 – 48:57]** So we don't have a graph full of zeros.

**[48:57 – 49:02]** Okay, so dd over dx is 2a times da over dx,

**[49:02 – 49:05]** and da over dx is 1, so it's like 2a.

**[49:05 – 49:11]** So it's 2 times x plus y if you write down the formula.

**[49:11 – 49:19]** Then de, okay, so de over dx, let me write it down here, de over dx.

**[49:19 – 49:25]** E is a product, so how do you differentiate the product?

**[49:25 – 49:32]** It's d over dx times b plus db over dx times d, right?

**[49:32 – 49:43]** So that will be dd over dx is 2 times x plus y times b, which is x minus y, right?

**[49:43 – 49:53]** Plus db over dx is 1 times d, which is x plus y squared, okay?

**[49:53 – 49:56]** So this is going to be de over dx.

**[49:56 – 50:09]** Now df over dx finally, df over dx is just de over dx plus dc over dx, right?

**[50:09 – 50:16]** And we know all of these guys, so dc over dx is 0 and de over dx is this.

**[50:16 – 50:25]** So the answer is x plus y squared plus 2 times x plus y times x minus y.

**[50:25 – 50:32]** You can open the brackets, doesn't matter for us. Sounds about right.

**[50:32 – 50:38]** So if you just look at the formula and you do it in your head, it looks correct.

**[50:38 – 50:44]** Of course, in practice, you wouldn't be able to drag the formulas with you.

**[50:44 – 50:51]** So in practice, what you would actually do is you would compute the numerical values of these derivatives.

**[50:51 – 51:01]** So you would start with 1 and 0, and then here it's also 0.

**[51:01 – 51:04]** Okay, so here the formula and the value is the same.

**[51:04 – 51:08]** Here also 1 is both the formula and the value, and here also.

**[51:08 – 51:14]** But here you would not have a formula like 2 times x plus y, you would just have the numerical value.

**[51:14 – 51:20]** And actually what you would do if you were implementing it as an algorithm,

**[51:20 – 51:24]** you don't know x and y when you are inside this node.

**[51:24 – 51:34]** What you do know is a. You know this input that went here from a, and a was equal to 1.

**[51:34 – 51:40]** So we can just stop at this point and say that the derivative here is equal to 2.

**[51:40 – 51:52]** And similarly here, what we actually are computing is dd over dx, which is 2, times b, the value of b, which is 3.

**[51:52 – 51:55]** It goes here.

**[51:55 – 52:02]** Plus db over dx, which is 1, times the value of d, which is 1.

**[52:02 – 52:05]** So we'll get something like 7 here.

**[52:05 – 52:10]** And then we would add 7 and 0 and get 7, and I suppose that's correct.

**[52:10 – 52:17]** If I substitute 2 and minus 1, I get 6 plus 1, 7.

**[52:17 – 52:22]** So what have we done now?

**[52:22 – 52:31]** We have gone through the graph bottom-up, and we have only done it once.

**[52:31 – 52:35]** We don't need several passes, we just need one single pass.

**[52:35 – 52:38]** Yes, we do both when we go through the graph.

**[52:38 – 52:41]** We do both computing the functions

**[52:41 – 52:46]** and computing the derivative, everything over dx, right?

**[52:46 – 52:49]** But it's okay.

**[52:49 – 52:51]** We go through the graph, we compute these two things,

**[52:51 – 52:53]** and when we arrive at the end,

**[52:53 – 53:00]** we have both the value of f and the value of df over dx.

**[53:00 – 53:03]** So here is a question for you.

**[53:03 – 53:05]** I hope somebody is still with me,

**[53:05 – 53:08]** because I know this probably was boring.

**[53:08 – 53:10]** But here is a question for you.

**[53:10 – 53:13]** Why is that not enough?

**[53:13 – 53:18]** I just did a single pass through the graph and I got the derivative.

**[53:18 – 53:21]** Why can't I just use this algorithm?

**[53:21 – 53:23]** Why do I need backpropagation?

**[53:23 – 53:29]** What's the catch? What's wrong here?

**[53:29 – 53:31]** All the formulas are right.

**[53:31 – 53:34]** We did indeed get the derivative.

**[53:34 – 53:36]** But why can't we just use this approach?

**[53:36 – 53:51]** While you're thinking, I'll copy the graph

**[53:51 – 53:54]** because then we'll go to actually backpropagation.

**[53:54 – 53:58]** But why can't we just use forward propagation

**[53:58 – 54:01]** and be content with forward propagation?

**[54:01 – 54:39]** Okay, so we need gradients and we just got df over dx.

**[54:39 – 54:42]** We can do df over dy in the same way.

**[54:42 – 54:49]** What's the catch?

**[54:49 – 55:00]** I see.

**[55:00 – 55:02]** I knew that we need to repeat this

**[55:02 – 55:06]** even though we probably know backpropagation already.

**[55:06 – 55:11]** What's the catch?

**[55:11 – 55:12]** Why can't I just use this?

**[55:12 – 55:15]** Why do I need to invent anything else?

**[55:15 – 55:18]** Now I will proceed to backprop.

**[55:18 – 55:22]** I will tell you how to go from the end to the beginning of this graph.

**[55:22 – 55:24]** It will be slightly different.

**[55:24 – 55:26]** But why can't I use this?

**[55:26 – 55:53]** What's wrong with this?

**[55:53 – 56:03]** Theoretically, formally, we can, right?

**[56:03 – 56:04]** Everything is correct.

**[56:04 – 56:06]** We did get df over dx.

**[56:06 – 56:10]** And sure enough, we can do the same thing and get df over dy.

**[56:10 – 56:11]** No problem.

**[56:11 – 56:18]** So what is the problem if it's not in the formal correctness?

**[56:18 – 57:04]** How would we apply this algorithm to an actual neural network?

**[57:04 – 58:31]** What would be the procedure?

**[58:31 – 58:42]** So how would we apply this algorithm, this forward propagation derivative computing algorithm,

**[58:42 – 58:47]** to a real neural network or actually to any function?

**[58:47 – 58:57]** As you said, but for some reason didn't elaborate on it, we need the whole gradient as a result.

**[58:57 – 59:02]** In this case, we need both df over dx and df over dy.

**[59:02 – 59:10]** So this procedure, the one that I wrote down, gives you df over dx.

**[59:10 – 59:12]** How do I get df over dy?

**[59:12 – 59:16]** Well, I can go through the graph again, but this time I will compute.

**[59:16 – 59:21]** I will start with dx over dy, which is zero, dy over dy, which is one,

**[59:21 – 59:26]** and again go through the graph and get to f.

**[59:26 – 59:28]** And I will get df over dy, sure.

**[59:28 – 59:34]** Or alternatively, what I could do, I could compute this all in parallel.

**[59:34 – 59:40]** So as I go through the graph, I am doing everything at once.

**[59:40 – 59:45]** I am doing the values, I am doing dx, so d everything over dx,

**[59:45 – 59:48]** and I am also doing d everything over dy.

**[59:48 – 59:52]** That's also possible.

**[59:52 – 59:56]** Then I will only need one path, and during this one path,

**[59:56 – 59:57]** I will compute everything.

**[59:57 – 1:00:04]** But both of these approaches are completely impractical, you see.

**[1:00:04 – 1:00:08]** In a real neural network, how do we want to scale this up?

**[1:00:08 – 1:00:10]** For a function of two variables, it's fine.

**[1:00:10 – 1:00:13]** But how do we scale this up?

**[1:00:13 – 1:00:16]** When you scale it up to a real neural network,

**[1:00:16 – 1:00:20]** as I said, the length of the vector of the gradient is large.

**[1:00:20 – 1:00:25]** So modern neural networks may have billions of weights,

**[1:00:25 – 1:00:29]** at least millions for sure, right?

**[1:00:29 – 1:00:36]** So what does it mean to apply this algorithm

**[1:00:36 – 1:00:40]** to get a gradient over a million variables?

**[1:00:40 – 1:00:46]** It means we either need to go over the graph a million times,

**[1:00:46 – 1:00:51]** it doesn't sound good, or we go over the graph once,

**[1:00:51 – 1:00:57]** but in every node of the graph, we need a vector of size a million,

**[1:00:57 – 1:01:02]** because we actually do need all of these values when we go,

**[1:01:02 – 1:01:07]** and basically we need a huge amount of memory,

**[1:01:07 – 1:01:10]** we need a million times the size of the graph of memory

**[1:01:10 – 1:01:14]** to actually do this one over class.

**[1:01:14 – 1:01:18]** So neither of these actually works, right?

**[1:01:18 – 1:01:22]** As you probably understand, the networks are,

**[1:01:22 – 1:01:26]** the practical networks will be so large that they,

**[1:01:26 – 1:01:30]** maybe just one copy of them barely fits into your GPU, right?

**[1:01:30 – 1:01:35]** So, of course, you cannot fit a million copies

**[1:01:35 – 1:01:39]** of the neural network into memory to do this.

**[1:01:39 – 1:01:44]** And, of course, you can do a million passes over the network,

**[1:01:44 – 1:01:46]** but then it would take forever, right?

**[1:01:46 – 1:01:49]** So either the time doesn't work

**[1:01:49 – 1:01:53]** or the space doesn't work in this case.

**[1:01:53 – 1:01:58]** Fortunately, we can do it in a much better way.

**[1:01:58 – 1:02:02]** And that's what backpropagation is about.

**[1:02:02 – 1:02:15]** So backpropagation, Bprop, switches the question,

**[1:02:15 – 1:02:18]** switches, goes to the dual, I don't know,

**[1:02:18 – 1:02:24]** to the converse way of viewing this graph

**[1:02:24 – 1:02:28]** and to the inverse way of moving through this graph.

**[1:02:28 – 1:02:32]** So what did we do here in the straightforward approach

**[1:02:32 – 1:02:35]** when we go bottom-up?

**[1:02:35 – 1:02:40]** When we go bottom-up, we compute d everything over dx.

**[1:02:40 – 1:02:43]** So we get this sequence when we go through the graph

**[1:02:43 – 1:02:46]** of d every node over dx.

**[1:02:46 – 1:02:50]** And finally we get to df over dx.

**[1:02:50 – 1:02:56]** When you do it like this, obviously you need to do as much

**[1:02:56 – 1:03:00]** to get df over dy and so on.

**[1:03:00 – 1:03:06]** But what if, instead of starting from the inputs

**[1:03:06 – 1:03:11]** and doing d everything over dx, what if we did it the opposite?

**[1:03:11 – 1:03:19]** What if we start from top and we do df over d everything, you see?

**[1:03:19 – 1:03:24]** So we go, now the base of our induction is df over df, which is 1.

**[1:03:24 – 1:03:33]** And then what do we, for example, do here when we go to e?

**[1:03:33 – 1:03:36]** We say, all right, so what is df over de?

**[1:03:36 – 1:03:40]** Well, we only need to know locally how f is computed.

**[1:03:40 – 1:03:45]** So f is e plus c, so df over de is 1.

**[1:03:45 – 1:03:46]** Very easy.

**[1:03:46 – 1:03:48]** Here also df over dc is 1.

**[1:03:48 – 1:03:51]** Then it becomes a bit more interesting.

**[1:03:51 – 1:03:56]** So now what is, let's say, df?

**[1:03:56 – 1:04:00]** Okay, so here I want to put df over dd over here, right?

**[1:04:00 – 1:04:04]** And I write it separately, won't fit there.

**[1:04:04 – 1:04:06]** What is df over dd?

**[1:04:06 – 1:04:11]** Well, d goes to f only through e, right?

**[1:04:11 – 1:04:20]** So by the chain rule, as usual, df over dd is df over dd times d e over dd.

**[1:04:20 – 1:04:26]** So df over d is 1 and d e over dd is b.

**[1:04:26 – 1:04:31]** So it's 1 times b, right?

**[1:04:31 – 1:04:37]** And so on. So for example, so here I get b.

**[1:04:37 – 1:04:44]** Now let's say d, okay, what else?

**[1:04:44 – 1:04:49]** DF over DE, yeah, DF over DB is the next step, right?

**[1:04:49 – 1:04:54]** DF over DB is, again, B goes only through E,

**[1:04:54 – 1:04:59]** so it's DF over DE times DE over DB, and it's D, okay?

**[1:05:01 – 1:05:06]** DF over DA, again, A goes only through D,

**[1:05:06 – 1:05:09]** so it's D, okay, let me put it here,

**[1:05:09 – 1:05:14]** DF over DA is DF over DD times DD over DA,

**[1:05:15 – 1:05:25]** and it's, it's what, it's 2A times B, okay?

**[1:05:25 – 1:05:33]** So 2AB, and now comes the interesting part.

**[1:05:33 – 1:05:39]** So now I have DF over DA, DF over DB, and DF over DC,

**[1:05:39 – 1:05:44]** and now I need to compute, let's say, DF over DX,

**[1:05:44 – 1:05:49]** and X goes in two different things, right?

**[1:05:49 – 1:05:51]** So there are two outgoing edges here,

**[1:05:51 – 1:05:56]** which means that X is a part of A,

**[1:05:56 – 1:05:57]** which is then a part of F,

**[1:05:57 – 1:06:01]** and X is a part of B, which is then a part of F.

**[1:06:01 – 1:06:05]** So again, by the chain rule, it's really straightforward.

**[1:06:05 – 1:06:08]** I just need to add up the contributions, right?

**[1:06:08 – 1:06:13]** So DF over DA times DA over DX,

**[1:06:13 – 1:06:18]** plus DF over DB times DB over DX, that's it.

**[1:06:18 – 1:06:21]** So I know DF over DA, which is 2AB.

**[1:06:21 – 1:06:24]** DA over DX is one, right?

**[1:06:24 – 1:06:26]** This is straightforward.

**[1:06:26 – 1:06:29]** Plus DF over DB, which is B,

**[1:06:29 – 1:06:33]** times DB over DX, which is also one.

**[1:06:33 – 1:06:35]** So we got 2AB plus D.

**[1:06:35 – 1:06:41]** So this is 2 times X plus Y times X minus Y

**[1:06:41 – 1:06:48]** plus X plus Y squared, which is, I guess, correct.

**[1:06:48 – 1:06:53]** So we got the same result as before, right?

**[1:06:53 – 1:06:54]** DF over DX.

**[1:06:54 – 1:07:00]** But the beautiful part here is that without starting over,

**[1:07:00 – 1:07:04]** without re-computing everything that was happening above,

**[1:07:04 – 1:07:09]** we also can immediately get DF over DY over here, right?

**[1:07:09 – 1:07:12]** So now Y goes to three different things.

**[1:07:12 – 1:07:15]** Okay, let me, since you were not very quick

**[1:07:15 – 1:07:16]** to answer my questions,

**[1:07:16 – 1:07:20]** then let me write it down in a bit more detail.

**[1:07:20 – 1:07:23]** So DF over DA times DA over DY, right?

**[1:07:23 – 1:07:27]** Plus DF over DB times DB over DY,

**[1:07:27 – 1:07:32]** plus DF over DC times DC over DY.

**[1:07:32 – 1:07:34]** And what we get here?

**[1:07:34 – 1:07:40]** Well, DF over DA is two AB times one.

**[1:07:40 – 1:07:44]** DF over DB is D times minus one, right?

**[1:07:44 – 1:07:49]** DF DB over DY is minus one, so minus D.

**[1:07:49 – 1:07:51]** And DF over DC is one,

**[1:07:51 – 1:07:55]** but then we need to multiply by DC over DY,

**[1:07:55 – 1:07:59]** which is three Y squared.

**[1:07:59 – 1:08:04]** So we get like two times X plus Y time X minus Y

**[1:08:04 – 1:08:10]** minus X plus Y squared plus three Y squared.

**[1:08:10 – 1:08:12]** And I suppose that's also correct, right?

**[1:08:12 – 1:08:14]** If you go and look at this, yeah,

**[1:08:14 – 1:08:17]** obviously that's also correct.

**[1:08:17 – 1:08:22]** So notice the difference, right?

**[1:08:22 – 1:08:26]** Instead of going bottom up and computing D everything over DX

**[1:08:26 – 1:08:31]** and then, or in parallel, D everything over DY,

**[1:08:31 – 1:08:35]** thus doing a lot of unnecessary computations,

**[1:08:36 – 1:08:39]** we are going from top to the bottom

**[1:08:39 – 1:08:42]** and we are computing DF over D everything.

**[1:08:42 – 1:08:46]** And of course, these are two symmetrical approaches.

**[1:08:46 – 1:08:48]** They are dual to each other.

**[1:08:48 – 1:08:52]** They, it's, you can argue that it's basically the same,

**[1:08:52 – 1:08:56]** but neural networks are not symmetrical, right?

**[1:08:56 – 1:09:02]** You always have only one output because you want to,

**[1:09:02 – 1:09:04]** for example, minimize your output, right?

**[1:09:04 – 1:09:07]** You need to have a single function that you minimize.

**[1:09:07 – 1:09:09]** You cannot minimize several functions at once

**[1:09:09 – 1:09:11]** or a million functions at once.

**[1:09:11 – 1:09:12]** That doesn't work.

**[1:09:12 – 1:09:14]** If you have a million functions that you need to minimize,

**[1:09:14 – 1:09:20]** first, you need to compose them into a single function.

**[1:09:20 – 1:09:25]** So you always have only one output at the end

**[1:09:25 – 1:09:28]** and you have millions of inputs.

**[1:09:28 – 1:09:31]** So this approach scales well

**[1:09:31 – 1:09:35]** if you have lots of outputs and few inputs,

**[1:09:35 – 1:09:37]** then this is the proper way.

**[1:09:37 – 1:09:40]** But our situation is the opposite.

**[1:09:40 – 1:09:41]** In real neural networks,

**[1:09:41 – 1:09:44]** we have lots of inputs and one output.

**[1:09:44 – 1:09:48]** So we use backpropagation.

**[1:09:48 – 1:09:52]** Notice how, in this case,

**[1:09:52 – 1:09:58]** like what did we need to do these computations?

**[1:09:58 – 1:10:00]** I wrote down formulas because they are easier

**[1:10:00 – 1:10:03]** to follow than just numbers,

**[1:10:03 – 1:10:05]** because numbers don't mean anything.

**[1:10:05 – 1:10:09]** But in practice, of course, in actual computation,

**[1:10:09 – 1:10:11]** they would be numbers, right?

**[1:10:11 – 1:10:14]** This would be numerical values of these things.

**[1:10:14 – 1:10:19]** And so when you start out with df over df,

**[1:10:19 – 1:10:21]** of course, it's always one.

**[1:10:21 – 1:10:25]** But then, as we progressed through the graph backwards

**[1:10:25 – 1:10:30]** to compute, for example, df over dd,

**[1:10:30 – 1:10:31]** so what's happening?

**[1:10:31 – 1:10:34]** What gets transmitted on this edge?

**[1:10:34 – 1:10:39]** What gets transmitted from e to d?

**[1:10:39 – 1:10:44]** We needed not only df over d, which we got from above,

**[1:10:44 – 1:10:47]** but we also needed d over dd.

**[1:10:47 – 1:10:52]** And to compute d over dd, we needed the value of b.

**[1:10:52 – 1:10:58]** So we needed to know the values of these intermediate nodes.

**[1:10:58 – 1:10:59]** Again, it's all local.

**[1:10:59 – 1:11:05]** To compute this, I only need the nodes that go inside e.

**[1:11:05 – 1:11:11]** But I do need to know the values too, not only the derivatives.

**[1:11:11 – 1:11:14]** Because to compute the derivatives, I need to know the values.

**[1:11:14 – 1:11:20]** So in practice, backpropagation is not one pass through the graph.

**[1:11:20 – 1:11:22]** It's two passes.

**[1:11:22 – 1:11:26]** So how the algorithm actually works.

**[1:11:26 – 1:11:35]** First, you do forward propagation to compute values of intermediate nodes.

**[1:11:35 – 1:11:37]** And yes, you need to store them.

**[1:11:37 – 1:11:45]** So it's kind of like you need to store two numbers on every edge of this graph.

**[1:11:45 – 1:11:56]** And then backprop to compute df over d everything for every intermediate node.

**[1:11:56 – 1:11:59]** So that's backpropagation.

**[1:11:59 – 1:12:10]** And this is a very efficient and actually pretty straightforward way to compute gradients.

**[1:12:10 – 1:12:23]** And actually, if you look at any deep learning library like PyTorch that you will probably be using in practice in our class,

**[1:12:23 – 1:12:31]** if you look at any deep learning library, what you see is its basic operation,

**[1:12:32 – 1:12:40]** what it actually is supposed to do really, really well, its main job, is to do these two passes to the graph.

**[1:12:41 – 1:12:52]** So these are the key procedures, the key functions that the library needs to implement,

**[1:12:52 – 1:12:58]** and everything else is basically just syntactic sugar on top of that.

**[1:12:58 – 1:13:04]** So if you, I don't know, if you program in PyTorch,

**[1:13:04 – 1:13:11]** if you do the practical sessions of this class and you implement a new neural network,

**[1:13:11 – 1:13:17]** sure, you will see that PyTorch has thousands of classes with different layers,

**[1:13:17 – 1:13:22]** different kinds of components,

**[1:13:22 – 1:13:26]** and all of these components are only there,

**[1:13:26 – 1:13:29]** they are only needed to set up this graph.

**[1:13:29 – 1:13:34]** And these components can be relatively inefficient, it doesn't really matter.

**[1:13:34 – 1:13:40]** They are only run once and they don't do much, to be honest.

**[1:13:40 – 1:13:45]** What actually has to be efficient, what is the meat of everything,

**[1:13:45 – 1:13:49]** is computing the gradient along the graph.

**[1:13:49 – 1:13:56]** So I like to say that PyTorch and TensorFlow and whatever else,

**[1:13:56 – 1:14:01]** what they actually are, are automatic differentiation libraries.

**[1:14:01 – 1:14:05]** They are not... I mean, the deep learning is an afterthought.

**[1:14:05 – 1:14:10]** What actually has to be extremely efficient

**[1:14:10 – 1:14:13]** is the forward propagation and the backward propagation procedure.

**[1:14:13 – 1:14:20]** The rest can be done in any way.

**[1:14:20 – 1:14:24]** OK, what else do I want to say here?

**[1:14:24 – 1:14:26]** What else do I want to say?

**[1:14:26 – 1:14:32]** OK, forward propagation, backward propagation, example.

**[1:14:32 – 1:14:35]** OK, so while I'm thinking what else I missed,

**[1:14:35 – 1:14:39]** let me show you what I will also make available.

**[1:14:39 – 1:14:44]** I have some examples over here.

**[1:14:44 – 1:14:49]** So it's a different function, but something like what I just did on the board.

**[1:14:49 – 1:14:50]** And you can play with it.

**[1:14:50 – 1:14:53]** You can define a different computational graph

**[1:14:53 – 1:15:00]** and see how the values propagate through a network like this one, right?

**[1:15:00 – 1:15:01]** Oh, yeah.

**[1:15:01 – 1:15:08]** And also, just to circle back to how it actually applies to neural networks,

**[1:15:08 – 1:15:14]** notice that when you say,

**[1:15:14 – 1:15:17]** what is the input to a neural network?

**[1:15:20 – 1:15:23]** Your intuition, your default answer would be

**[1:15:23 – 1:15:26]** the input is X and Y, or actually only X.

**[1:15:26 – 1:15:30]** So if you ask what is the input of the neural network

**[1:15:30 – 1:15:32]** that distinguishes cats from dogs, well, that's an image.

**[1:15:32 – 1:15:34]** And that's true, right?

**[1:15:34 – 1:15:38]** So the default way to think of inputs is this.

**[1:15:39 – 1:15:43]** But if you think of the network as a computational graph,

**[1:15:43 – 1:15:46]** it has two different sorts of inputs.

**[1:15:46 – 1:15:48]** I think I already said that, right?

**[1:15:48 – 1:15:51]** So it has inputs that are fixed, that are always fixed,

**[1:15:51 – 1:15:52]** that we do not optimize.

**[1:15:52 – 1:15:58]** And these are like images, correct answers to the images and so on.

**[1:15:58 – 1:16:00]** These are the x's and the y's.

**[1:16:00 – 1:16:03]** And also there are the weights.

**[1:16:03 – 1:16:08]** And the weights, they are also inputs to the computational graph.

**[1:16:08 – 1:16:10]** They are not computed from anywhere.

**[1:16:10 – 1:16:15]** They are variables that appear in this huge, huge formula.

**[1:16:15 – 1:16:19]** And when we are doing training,

**[1:16:19 – 1:16:24]** when we learn, when we are doing training of neural networks,

**[1:16:24 – 1:16:30]** we are actually interested in gradients with respect to the weights.

**[1:16:30 – 1:16:35]** And so, yeah, if anybody asks,

**[1:16:35 – 1:16:38]** there are different kinds of inputs to a neural network,

**[1:16:38 – 1:16:41]** and the weights are also inputs.

**[1:16:41 – 1:16:47]** And when I was doing this example, there was no fixed input here.

**[1:16:47 – 1:16:50]** So I could have added a constant or something, but I mean,

**[1:16:50 – 1:16:52]** it wouldn't serve any purpose.

**[1:16:52 – 1:16:55]** Like x and y in this example are both weights,

**[1:16:55 – 1:17:02]** and we need to have a gradient with respect to x and y.

**[1:17:02 – 1:17:07]** All right, has this been clear?

**[1:17:07 – 1:17:15]** Did you already know this?

**[1:17:15 – 1:17:21]** Okay, so before the break,

**[1:17:21 – 1:17:24]** I guess I don't have too much time,

**[1:17:24 – 1:17:31]** so let me just maybe do a part of what I wanted to say

**[1:17:31 – 1:17:35]** about gradient descent.

**[1:17:35 – 1:17:40]** Specifically, let me motivate stochastic gradient descent

**[1:17:40 – 1:17:43]** and actually introduce it.

**[1:17:43 – 1:17:44]** And then after the break,

**[1:17:44 – 1:17:47]** we will discuss the actual algorithms

**[1:17:47 – 1:17:49]** of stochastic gradient descent.

**[1:17:49 – 1:17:57]** So here is a question.

**[1:17:57 – 1:18:00]** There are a lot of problems in deep learning,

**[1:18:00 – 1:18:02]** in practical deep learning,

**[1:18:02 – 1:18:06]** that come from the fact that we are using gradient descent.

**[1:18:06 – 1:18:09]** And we will discuss some of these problems in class.

**[1:18:09 – 1:18:11]** Of course, we don't yet see them.

**[1:18:11 – 1:18:13]** We are just on the beginning to look at this stuff.

**[1:18:13 – 1:18:18]** But basically, gradient descent is a pretty stupid algorithm.

**[1:18:18 – 1:18:20]** It's a first order algorithm.

**[1:18:20 – 1:18:26]** So gradient descent is a first order--

**[1:18:26 – 1:18:30]** comes from the first order approximation to the loss.

**[1:18:30 – 1:18:38]** So I take L of W, and I say, well, OK, so right now,

**[1:18:38 – 1:18:40]** I am at point W_k.

**[1:18:40 – 1:18:45]** Let me do a Taylor series of L of W at point W_k.

**[1:18:45 – 1:18:54]** So I say, well, it's L of W_k plus W minus W_k times

**[1:18:54 – 1:19:02]** the gradient of L at point W_k.

**[1:19:02 – 1:19:05]** And gradient descent basically stops here.

**[1:19:05 – 1:19:06]** It just looks at this.

**[1:19:06 – 1:19:11]** It says, all right, so the gradient is the direction of steepest

**[1:19:11 – 1:19:16]** increase, therefore the opposite direction is the steepest decrease.

**[1:19:16 – 1:19:20]** Let's go there if you want to minimize.

**[1:19:20 – 1:19:26]** But we've had hundreds of years of optimization theory, right?

**[1:19:26 – 1:19:33]** So gradient descent could be done by, I don't know, Newton and Leibniz.

**[1:19:33 – 1:19:40]** And since then, we've had quite a lot of more involved

**[1:19:40 – 1:19:43]** but better optimization techniques, right?

**[1:19:43 – 1:19:48]** And the most straightforward idea, when you look at gradient descent like this,

**[1:19:48 – 1:19:53]** would be, well, what if we go one step further in the Taylor series?

**[1:19:53 – 1:19:55]** Why not?

**[1:19:55 – 1:20:03]** What if we also go to the second derivatives, w minus wk,

**[1:20:03 – 1:20:06]** that now there is a quadratic form in here, right?

**[1:20:06 – 1:20:11]** Times h inverse, not inverse, sorry, just h,

**[1:20:11 – 1:20:18]** times W minus WK plus something smaller.

**[1:20:20 – 1:20:29]** So now we are approximating, not by a surface, not by a linear surface,

**[1:20:29 – 1:20:33]** which, to be honest, is a pretty stupid idea for optimization.

**[1:20:34 – 1:20:37]** Well, I mean, it's not stupid in the sense that it can work,

**[1:20:37 – 1:20:40]** but it's stupid in the sense that it's naive.

**[1:20:40 – 1:20:46]** So if I'm looking at a complicated function

**[1:20:46 – 1:20:54]** and I'm trying to see, like, what is the derivative here, where to go,

**[1:20:54 – 1:21:00]** then all that the derivative tells me is that, well, you need to go here

**[1:21:00 – 1:21:04]** or you need to go here if we are in dimension one, right?

**[1:21:04 – 1:21:07]** And it doesn't tell you anything about how far you should go.

**[1:21:07 – 1:21:10]** And this is actually the main problem of gradient descent.

**[1:21:10 – 1:21:14]** This is what optimization theory to a large extent was about.

**[1:21:14 – 1:21:15]** It's a big topic.

**[1:21:17 – 1:21:19]** Like the gradient gives you the direction,

**[1:21:19 – 1:21:21]** but how far should you go along this direction?

**[1:21:21 – 1:21:22]** What should be the learning rate?

**[1:21:22 – 1:21:24]** What should be the step size?

**[1:21:25 – 1:21:29]** But if you go one step further,

**[1:21:29 – 1:21:32]** then what you are doing is you are approximating

**[1:21:32 – 1:21:40]** your difficult function locally with a quadratic surface.

**[1:21:40 – 1:21:46]** On here it would be a parabola, but with a quadratic surface.

**[1:21:47 – 1:21:50]** And now there are no equations anymore.

**[1:21:51 – 1:21:52]** You know where to go.

**[1:21:52 – 1:21:55]** You can go immediately to the minimum of this parabola,

**[1:21:56 – 1:21:57]** to the minimum of this quadratic surface.

**[1:21:58 – 1:22:01]** And it's a very simple formula, right?

**[1:22:01 – 1:22:02]** You look at this and you say,

**[1:22:02 – 1:22:04]** okay, I want to minimize this guy.

**[1:22:04 – 1:22:05]** So how do you minimize?

**[1:22:05 – 1:22:07]** Well, you take the gradient with respect to W.

**[1:22:08 – 1:22:12]** Okay, so what is going to be the gradient with respect to W?

**[1:22:12 – 1:22:15]** Let's say that, let me call this vector G,

**[1:22:16 – 1:22:19]** the gradient GK, the gradient at step K.

**[1:22:20 – 1:22:21]** And this is HK.

**[1:22:22 – 1:22:24]** This is the matrix of the second derivatives H

**[1:22:24 – 1:22:26]** because it's called the Hessian.

**[1:22:28 – 1:22:32]** And I take the gradient of the first part.

**[1:22:32 – 1:22:33]** This disappears.

**[1:22:33 – 1:22:34]** This disappears.

**[1:22:34 – 1:22:36]** There is just GK, right?

**[1:22:36 – 1:22:39]** And then I take the gradient of the second part.

**[1:22:39 – 1:22:41]** The two cancels out.

**[1:22:41 – 1:22:46]** And we get GK plus HK times W.

**[1:22:47 – 1:22:50]** And that's the gradient of this quadratic function.

**[1:22:50 – 1:22:52]** So it should be equal to zero.

**[1:22:55 – 1:22:57]** And I guess that's...

**[1:22:57 – 1:22:59]** Sorry, that's not it, of course.

**[1:22:59 – 1:23:02]** I forgot the first...

**[1:23:02 – 1:23:07]** I forgot HK times W minus WK, of course.

**[1:23:07 – 1:23:10]** And that should be equal to zero.

**[1:23:10 – 1:23:21]** So basically W is WK minus HK inverse times GK.

**[1:23:22 – 1:23:22]** That's it.

**[1:23:23 – 1:23:26]** And you can say that this is your next W.

**[1:23:26 – 1:23:28]** And you have no problem with the step size.

**[1:23:29 – 1:23:33]** And this procedure is far, far, far more robust, more stable.

**[1:23:34 – 1:23:41]** You will never or almost never go to some bad part of the search space.

**[1:23:42 – 1:23:45]** You will converge in far fewer iterations.

**[1:23:46 – 1:23:47]** Basically, it's better all around.

**[1:23:50 – 1:23:52]** And this is called Newton's method, by the way.

**[1:23:53 – 1:24:01]** Newton's method or second order optimization or second order optimization or whatever.

**[1:24:02 – 1:24:06]** So why can't we use Newton's method for gradient descent?

**[1:24:08 – 1:24:13]** Well, for Newton's method itself, the answer is kind of obvious.

**[1:24:13 – 1:24:18]** Because we cannot afford to do this computation, right?

**[1:24:19 – 1:24:26]** So, again, remember that w is a very, very long vector, right?

**[1:24:26 – 1:24:29]** It's like a million of numbers.

**[1:24:29 – 1:24:31]** It's a vector of size a million.

**[1:24:32 – 1:24:37]** So hk, the matrix of second derivatives, right?

**[1:24:37 – 1:24:45]** dL over dWi dWj is a matrix of size a million times a million.

**[1:24:46 – 1:24:48]** And we are supposed to compute this matrix,

**[1:24:48 – 1:24:50]** but more than compute, we're supposed to invert it.

**[1:24:51 – 1:24:53]** So of course, it's not going to work computationally, right?

**[1:24:54 – 1:24:55]** No question about this.

**[1:24:57 – 1:25:03]** But a more interesting question is, in optimization theory,

**[1:25:04 – 1:25:09]** in classical optimization theory, like in the 1960s, 1970s, 1980s,

**[1:25:10 – 1:25:13]** people also were thinking about this.

**[1:25:14 – 1:25:17]** There were no huge neural networks at the time,

**[1:25:17 – 1:25:18]** but there were functions to optimize,

**[1:25:19 – 1:25:20]** and there were difficult functions to optimize,

**[1:25:20 – 1:25:23]** and there were cases when second-order techniques

**[1:25:23 – 1:25:26]** were too difficult computationally.

**[1:25:26 – 1:25:29]** So there is this whole field

**[1:25:29 – 1:25:33]** of what is called quasi-Newton algorithms,

**[1:25:35 – 1:25:37]** quasi-Newton algorithms,

**[1:25:40 – 1:25:42]** and there are basically approximations to this.

**[1:25:43 – 1:25:47]** So the most famous such algorithm is called LBFGS,

**[1:25:48 – 1:25:50]** where L stands for limited memory,

**[1:25:50 – 1:25:53]** and BFGS are four last names,

**[1:25:53 – 1:25:56]** Fletcher, Boyden, Goldfarb,

**[1:25:56 – 1:25:57]** something like this.

**[1:25:58 – 1:26:00]** So it's a very famous algorithm.

**[1:26:00 – 1:26:02]** I won't go into details on how it works.

**[1:26:02 – 1:26:04]** It's definitely not relevant for us.

**[1:26:04 – 1:26:06]** But basically what it does is

**[1:26:06 – 1:26:13]** keeps an approximation to this kind of update

**[1:26:13 – 1:26:16]** and a very good approximation

**[1:26:16 – 1:26:20]** by only looking at the Ws themselves,

**[1:26:21 – 1:26:23]** W1, W2, and so on,

**[1:26:24 – 1:26:25]** and the gradient vectors.

**[1:26:27 – 1:26:30]** So like when you go from K to K plus 1,

**[1:26:30 – 1:26:33]** there is a procedure to update

**[1:26:33 – 1:26:36]** this approximate Hessean,

**[1:26:36 – 1:26:37]** approximate inverse Hessean.

**[1:26:38 – 1:26:40]** And this procedure is quick

**[1:26:40 – 1:26:43]** and it never deals with

**[1:26:43 – 1:26:45]** a million times a million matrices.

**[1:26:46 – 1:26:47]** Basically, it's a low-rank approximation,

**[1:26:48 – 1:26:49]** but let's not go there.

**[1:26:50 – 1:26:53]** So there are good ways

**[1:26:53 – 1:26:56]** to do something like the second-order technique

**[1:26:56 – 1:27:00]** without going actually to the second-order

**[1:27:00 – 1:27:04]** while only staying at the level of gradients

**[1:27:04 – 1:27:06]** and gradient vectors,

**[1:27:07 – 1:27:11]** and doing it in relatively low complexity.

**[1:27:13 – 1:27:16]** So why don't we do that in deep learning?

**[1:27:18 – 1:27:20]** And the answer is, again,

**[1:27:20 – 1:27:22]** we would be very happy to,

**[1:27:23 – 1:27:25]** and just as we would be very happy

**[1:27:25 – 1:27:26]** to use Newton's method,

**[1:27:26 – 1:27:27]** we would be very happy

**[1:27:27 – 1:27:29]** to do the second-order optimization,

**[1:27:30 – 1:27:32]** and we would be nearly as happy

**[1:27:32 – 1:27:36]** to do LBFGS for a neural network,

**[1:27:36 – 1:27:38]** but we can't.

**[1:27:39 – 1:27:41]** And here comes the interesting part.

**[1:27:41 – 1:27:43]** So why am I building up to this?

**[1:27:43 – 1:27:44]** So first, I wanted to mention

**[1:27:44 – 1:27:45]** second-order optimization,

**[1:27:46 – 1:27:50]** but also why doesn't an algorithm

**[1:27:50 – 1:27:51]** like this work?

**[1:27:52 – 1:27:54]** I didn't tell you what the algorithm is,

**[1:27:54 – 1:27:55]** but trust me,

**[1:27:55 – 1:27:58]** it only requires to know gradients

**[1:27:58 – 1:27:59]** at individual points,

**[1:27:59 – 1:28:00]** values at these points,

**[1:28:01 – 1:28:02]** and that's it in Europe.

**[1:28:03 – 1:28:05]** And the answer is,

**[1:28:06 – 1:28:07]** in deep learning,

**[1:28:08 – 1:28:09]** unfortunately,

**[1:28:10 – 1:28:13]** we cannot even apply gradient descent

**[1:28:13 – 1:28:17]** because we cannot even compute the gradient.

**[1:28:20 – 1:28:20]** Or, I mean,

**[1:28:20 – 1:28:22]** we can only compute it like once

**[1:28:22 – 1:28:24]** and not in every step.

**[1:28:26 – 1:28:27]** Why so?

**[1:28:27 – 1:28:30]** Well, for a very straightforward reason,

**[1:28:30 – 1:28:32]** and I actually already mentioned this reason.

**[1:28:32 – 1:28:34]** Where did I do that?

**[1:28:34 – 1:28:35]** I did it somewhere.

**[1:28:37 – 1:28:37]** Where did I mean?

**[1:28:38 – 1:28:39]** Yeah, here, right?

**[1:28:39 – 1:28:41]** So what is the function

**[1:28:41 – 1:28:43]** that we are actually minimizing

**[1:28:43 – 1:28:43]** in machine learning?

**[1:28:43 – 1:28:47]** The function L of W

**[1:28:47 – 1:28:50]** is like a huge average

**[1:28:50 – 1:28:53]** or a huge sum

**[1:28:53 – 1:28:54]** same thing

**[1:28:54 – 1:28:58]** of loss functions

**[1:28:58 – 1:29:01]** across the whole data set

**[1:29:01 – 1:29:04]** L of X, N

**[1:29:04 – 1:29:06]** Y, N, W

**[1:29:06 – 1:29:09]** You can think of it, by the way,

**[1:29:09 – 1:29:11]** usually as something like

**[1:29:11 – 1:29:13]** the negative log likelihood

**[1:29:13 – 1:29:16]** log P of

**[1:29:16 – 1:29:18]** or log posterior

**[1:29:18 – 1:29:20]** log P of W

**[1:29:20 – 1:29:22]** given X, N, Y, N

**[1:29:22 – 1:29:24]** to connect it to

**[1:29:24 – 1:29:26]** what we discussed

**[1:29:26 – 1:29:27]** yesterday and the day before

**[1:29:27 – 1:29:29]** but in any case

**[1:29:29 – 1:29:32]** your complicated neural network

**[1:29:32 – 1:29:33]** with a million weights

**[1:29:33 – 1:29:35]** leaves over here

**[1:29:35 – 1:29:39]** it computes the loss

**[1:29:39 – 1:29:41]** yes, but it computes the loss

**[1:29:41 – 1:29:44]** only on one training sample

**[1:29:44 – 1:29:46]** and to get the function

**[1:29:46 – 1:29:47]** that you minimize

**[1:29:47 – 1:29:49]** you need to go over

**[1:29:49 – 1:29:49]** the whole dataset

**[1:29:49 – 1:29:53]** so the actual

**[1:29:53 – 1:29:55]** honest-to-God gradient

**[1:29:55 – 1:29:58]** the actual GK

**[1:29:58 – 1:30:01]** would be a huge average

**[1:30:01 – 1:30:05]** of gradients

**[1:30:05 – 1:30:07]** of this loss function

**[1:30:07 – 1:30:11]** loss functions

**[1:30:11 – 1:30:12]** at point WK

**[1:30:12 – 1:30:13]** right

**[1:30:13 – 1:30:15]** and yes

**[1:30:15 – 1:30:15]** we can obviously

**[1:30:15 – 1:30:17]** compute every one of them

**[1:30:17 – 1:30:17]** but

**[1:30:17 – 1:30:21]** if I wanted to compute

**[1:30:21 – 1:30:23]** the true value

**[1:30:23 – 1:30:24]** of the gradient vector

**[1:30:24 – 1:30:25]** I would need to go

**[1:30:25 – 1:30:27]** over the whole dataset

**[1:30:27 – 1:30:29]** on every step

**[1:30:29 – 1:30:31]** which is

**[1:30:31 – 1:30:33]** kind of obviously impractical

**[1:30:33 – 1:30:33]** so yeah

**[1:30:33 – 1:30:34]** we will go over

**[1:30:34 – 1:30:35]** the whole dataset

**[1:30:35 – 1:30:36]** but maybe like

**[1:30:36 – 1:30:36]** once or twice

**[1:30:36 – 1:30:38]** not on every step

**[1:30:38 – 1:30:40]** of our optimization procedure

**[1:30:40 – 1:30:41]** that's not going to work

**[1:30:41 – 1:30:48]** so what is the actual setting

**[1:30:48 – 1:30:49]** how

**[1:30:49 – 1:30:51]** what is the problem

**[1:30:51 – 1:30:51]** that we are solving

**[1:30:51 – 1:30:53]** if I am telling you

**[1:30:53 – 1:30:54]** that we cannot even

**[1:30:54 – 1:30:55]** compute the function

**[1:30:55 – 1:30:56]** that we are optimizing

**[1:30:56 – 1:30:57]** right

**[1:30:57 – 1:30:58]** it's the same thing

**[1:30:58 – 1:30:58]** right

**[1:30:58 – 1:30:59]** we can compute the gradient

**[1:30:59 – 1:31:00]** because it's a huge sum

**[1:31:00 – 1:31:01]** and therefore

**[1:31:01 – 1:31:02]** we can't even compute

**[1:31:02 – 1:31:03]** the function itself

**[1:31:03 – 1:31:05]** because it's the same huge sum

**[1:31:05 – 1:31:09]** then what are we even doing

**[1:31:09 – 1:31:11]** well

**[1:31:11 – 1:31:12]** the answer is

**[1:31:12 – 1:31:14]** we are doing

**[1:31:14 – 1:31:15]** what is known as

**[1:31:15 – 1:31:16]** stochastic gradient descent

**[1:31:16 – 1:31:25]** I wrote

**[1:31:25 – 1:31:26]** I wrote all of these functions

**[1:31:26 – 1:31:27]** not as sums

**[1:31:27 – 1:31:28]** but as averages

**[1:31:28 – 1:31:30]** it doesn't matter for optimization

**[1:31:30 – 1:31:31]** but I wrote them

**[1:31:31 – 1:31:32]** as averages

**[1:31:32 – 1:31:35]** to make the following point

**[1:31:35 – 1:31:37]** you can view this loss function

**[1:31:37 – 1:31:38]** you can view the function

**[1:31:38 – 1:31:39]** that we are optimizing

**[1:31:39 – 1:31:42]** as an expectation

**[1:31:42 – 1:31:46]** over the data set

**[1:31:46 – 1:31:49]** over the uniform distribution

**[1:31:49 – 1:31:50]** over the data set

**[1:31:50 – 1:31:53]** of this

**[1:31:53 – 1:31:57]** small loss function

**[1:31:57 – 1:31:59]** so x and y

**[1:31:59 – 1:32:01]** here x and y

**[1:32:01 – 1:32:03]** are taken just uniformly

**[1:32:03 – 1:32:05]** at random from the data set

**[1:32:05 – 1:32:06]** right

**[1:32:06 – 1:32:07]** because

**[1:32:07 – 1:32:09]** well what is the expectation

**[1:32:09 – 1:32:10]** the expectation is the average

**[1:32:10 – 1:32:12]** weight with probabilities

**[1:32:12 – 1:32:13]** so if I take everything

**[1:32:13 – 1:32:14]** with equal probabilities

**[1:32:14 – 1:32:15]** I get just the average

**[1:32:15 – 1:32:19]** so our function

**[1:32:19 – 1:32:22]** is actually

**[1:32:22 – 1:32:24]** an expectation

**[1:32:24 – 1:32:26]** of a different function

**[1:32:26 – 1:32:28]** with respect to some of the variables

**[1:32:28 – 1:32:29]** with respect to x and y

**[1:32:29 – 1:32:31]** and I want to minimize it

**[1:32:31 – 1:32:33]** with respect to the other variables

**[1:32:33 – 1:32:34]** with respect to w

**[1:32:34 – 1:32:38]** when you have a problem like this

**[1:32:38 – 1:32:39]** this is what's called

**[1:32:39 – 1:32:40]** stochastic optimization

**[1:32:40 – 1:32:48]** and what is

**[1:32:48 – 1:32:50]** how can we do it

**[1:32:50 – 1:32:51]** if we cannot compute

**[1:32:51 – 1:32:54]** this expectation directly

**[1:32:54 – 1:32:58]** well there is basically always

**[1:32:58 – 1:33:00]** exactly one true way

**[1:33:00 – 1:33:01]** to approximate the expectation

**[1:33:01 – 1:33:02]** you take a sample

**[1:33:02 – 1:33:03]** and that's it

**[1:33:03 – 1:33:07]** so what we are actually doing

**[1:33:07 – 1:33:09]** in practice

**[1:33:09 – 1:33:12]** is on every step along the way

**[1:33:12 – 1:33:15]** we are taking

**[1:33:15 – 1:33:17]** not the gradient

**[1:33:17 – 1:33:18]** gk

**[1:33:18 – 1:33:20]** which is

**[1:33:20 – 1:33:22]** I mean the expectation is linear

**[1:33:22 – 1:33:23]** so it's the same thing

**[1:33:23 – 1:33:24]** it's the expectation

**[1:33:24 – 1:33:26]** of the gradients of l

**[1:33:26 – 1:33:28]** right

**[1:33:28 – 1:33:32]** but we are approximating

**[1:33:32 – 1:33:33]** the true gradient

**[1:33:33 – 1:33:34]** with

**[1:33:34 – 1:33:36]** let's say

**[1:33:36 – 1:33:37]** g hat

**[1:33:37 – 1:33:38]** k

**[1:33:38 – 1:33:40]** which is just

**[1:33:40 – 1:33:42]** the average over a small

**[1:33:42 – 1:33:43]** subsample of this

**[1:33:43 – 1:33:46]** 1 over let's say m

**[1:33:46 – 1:33:48]** times the sum

**[1:33:48 – 1:33:51]** gradient

**[1:33:51 – 1:33:54]** l of x

**[1:33:54 – 1:33:54]** i

**[1:33:54 – 1:33:55]** y i

**[1:33:55 – 1:33:57]** w

**[1:33:57 – 1:33:59]** so

**[1:33:59 – 1:34:01]** on every step

**[1:34:01 – 1:34:02]** along the way

**[1:34:02 – 1:34:05]** what we are actually doing

**[1:34:05 – 1:34:06]** and you probably already know this

**[1:34:06 – 1:34:07]** you just

**[1:34:07 – 1:34:08]** I just kind of think

**[1:34:08 – 1:34:09]** you never thought of it

**[1:34:09 – 1:34:10]** from this direction

**[1:34:10 – 1:34:11]** from this angle

**[1:34:11 – 1:34:12]** but the result

**[1:34:12 – 1:34:13]** you probably already know

**[1:34:13 – 1:34:14]** what we actually do

**[1:34:14 – 1:34:14]** when we train

**[1:34:14 – 1:34:15]** difficult

**[1:34:15 – 1:34:17]** complicated machine learning models

**[1:34:17 – 1:34:18]** we

**[1:34:18 – 1:34:20]** don't

**[1:34:20 – 1:34:22]** go over the whole data set

**[1:34:22 – 1:34:23]** to compute the loss

**[1:34:23 – 1:34:24]** we go

**[1:34:24 – 1:34:26]** through mini batches

**[1:34:26 – 1:34:27]** right

**[1:34:27 – 1:34:28]** and

**[1:34:28 – 1:34:29]** this mini batch

**[1:34:29 – 1:34:32]** formally

**[1:34:32 – 1:34:33]** it's a sample

**[1:34:33 – 1:34:34]** from the data set

**[1:34:34 – 1:34:35]** so

**[1:34:35 – 1:34:37]** what we are actually doing

**[1:34:37 – 1:34:38]** like mathematically

**[1:34:38 – 1:34:40]** what the meaning of what we are doing

**[1:34:40 – 1:34:41]** in stochastic gradient descent

**[1:34:41 – 1:34:42]** is

**[1:34:42 – 1:34:44]** we are approximating

**[1:34:44 – 1:34:45]** the true value of the gradient

**[1:34:45 – 1:34:46]** which is

**[1:34:46 – 1:34:47]** big and difficult

**[1:34:47 – 1:34:48]** with

**[1:34:48 – 1:34:49]** a

**[1:34:49 – 1:34:50]** sample

**[1:34:50 – 1:34:53]** sampled value of the gradient

**[1:34:53 – 1:34:54]** so

**[1:34:54 – 1:34:55]** on average

**[1:34:55 – 1:34:57]** if you take the average of this

**[1:34:57 – 1:34:58]** over the whole data set

**[1:34:58 – 1:34:59]** obviously you get the same thing

**[1:34:59 – 1:34:59]** so the

**[1:34:59 – 1:35:00]** the mean

**[1:35:00 – 1:35:01]** is correct

**[1:35:01 – 1:35:02]** and

**[1:35:02 – 1:35:03]** to be honest

**[1:35:03 – 1:35:06]** approximating the

**[1:35:06 – 1:35:08]** expectation with a sample

**[1:35:08 – 1:35:10]** is like one of the best things

**[1:35:10 – 1:35:12]** one of the best approximations ever

**[1:35:12 – 1:35:14]** it has all of the nice properties

**[1:35:14 – 1:35:15]** it converges

**[1:35:15 – 1:35:17]** it has

**[1:35:17 – 1:35:20]** it's unbiased

**[1:35:20 – 1:35:20]** it has

**[1:35:20 – 1:35:22]** lots of

**[1:35:22 – 1:35:23]** results known about it

**[1:35:23 – 1:35:24]** so

**[1:35:24 – 1:35:25]** it's as good an approximation

**[1:35:25 – 1:35:26]** as we can hope for

**[1:35:26 – 1:35:29]** and what we actually do in practice

**[1:35:29 – 1:35:30]** is we go

**[1:35:30 – 1:35:33]** on every step

**[1:35:33 – 1:35:35]** of gradient descent

**[1:35:35 – 1:35:36]** we sample a mini batch

**[1:35:36 – 1:35:37]** we take a small subset

**[1:35:37 – 1:35:38]** from

**[1:35:38 – 1:35:39]** the data set

**[1:35:39 – 1:35:40]** we compute the gradients

**[1:35:40 – 1:35:41]** on the subset

**[1:35:41 – 1:35:42]** and then

**[1:35:42 – 1:35:44]** we see what happens next

**[1:35:44 – 1:35:46]** and then we update the weights

**[1:35:46 – 1:35:48]** according only to the gradients

**[1:35:48 – 1:35:48]** on this subset

**[1:35:48 – 1:35:50]** you probably know this

**[1:35:50 – 1:35:51]** but now

**[1:35:51 – 1:35:51]** you can

**[1:35:51 – 1:35:53]** you can see what it actually means

**[1:35:53 – 1:35:56]** but

**[1:35:56 – 1:35:58]** even though

**[1:35:58 – 1:35:59]** this is a good approximation

**[1:35:59 – 1:36:01]** and even though

**[1:36:01 – 1:36:02]** indeed we will go to

**[1:36:02 – 1:36:05]** when we do stochastic gradient descent

**[1:36:05 – 1:36:06]** we do

**[1:36:06 – 1:36:10]** arrive at a good

**[1:36:10 – 1:36:13]** at the neighborhood of minimum

**[1:36:13 – 1:36:14]** etc etc

**[1:36:14 – 1:36:15]** we'll discuss it after the break

**[1:36:15 – 1:36:16]** what we actually get

**[1:36:16 – 1:36:18]** from SGD

**[1:36:18 – 1:36:19]** but

**[1:36:19 – 1:36:22]** it's still an approximation

**[1:36:22 – 1:36:23]** and

**[1:36:23 – 1:36:25]** in practice

**[1:36:25 – 1:36:26]** it's a pretty bad one

**[1:36:26 – 1:36:27]** I mean

**[1:36:27 – 1:36:28]** it's good theoretically

**[1:36:28 – 1:36:29]** but

**[1:36:29 – 1:36:31]** the specific numbers

**[1:36:31 – 1:36:32]** are like

**[1:36:32 – 1:36:34]** the size of the data set

**[1:36:34 – 1:36:35]** is in millions

**[1:36:35 – 1:36:36]** or more

**[1:36:36 – 1:36:37]** and

**[1:36:37 – 1:36:38]** the actual

**[1:36:38 – 1:36:39]** mini-batch size

**[1:36:39 – 1:36:39]** is like

**[1:36:39 – 1:36:40]** 4

**[1:36:40 – 1:36:43]** or 8

**[1:36:43 – 1:36:43]** maybe

**[1:36:43 – 1:36:45]** so the mini-batch size

**[1:36:45 – 1:36:46]** should be

**[1:36:46 – 1:36:47]** such that

**[1:36:47 – 1:36:48]** this many copies

**[1:36:48 – 1:36:49]** of the network

**[1:36:49 – 1:36:50]** would fit into your

**[1:36:50 – 1:36:51]** GPU memory

**[1:36:51 – 1:36:52]** and

**[1:36:52 – 1:36:53]** it's a small number

**[1:36:53 – 1:36:54]** the

**[1:36:54 – 1:36:55]** the data set

**[1:36:55 – 1:36:56]** is of course

**[1:36:56 – 1:36:57]** large

**[1:36:57 – 1:36:57]** so

**[1:36:57 – 1:36:59]** we are approximating

**[1:36:59 – 1:36:59]** the average

**[1:36:59 – 1:37:01]** of a million numbers

**[1:37:01 – 1:37:02]** by taking

**[1:37:02 – 1:37:03]** like 4

**[1:37:03 – 1:37:04]** or 8

**[1:37:04 – 1:37:05]** or even 1

**[1:37:05 – 1:37:06]** number at random

**[1:37:06 – 1:37:08]** so of course

**[1:37:08 – 1:37:09]** mathematically

**[1:37:09 – 1:37:09]** it's the best

**[1:37:09 – 1:37:10]** we can do

**[1:37:10 – 1:37:11]** but it's still

**[1:37:11 – 1:37:12]** a pretty bad approximation

**[1:37:12 – 1:37:13]** it still has

**[1:37:13 – 1:37:14]** a pretty big variance

**[1:37:14 – 1:37:16]** and unfortunately

**[1:37:16 – 1:37:17]** this variance

**[1:37:17 – 1:37:18]** kills

**[1:37:18 – 1:37:19]** algorithms

**[1:37:19 – 1:37:20]** like LBFGS

**[1:37:20 – 1:37:21]** so

**[1:37:21 – 1:37:23]** since

**[1:37:23 – 1:37:24]** they are also

**[1:37:24 – 1:37:25]** doing approximations

**[1:37:25 – 1:37:26]** in order

**[1:37:26 – 1:37:27]** for those

**[1:37:27 – 1:37:29]** I can't explain

**[1:37:29 – 1:37:30]** without this

**[1:37:30 – 1:37:31]** whole separate lecture

**[1:37:31 – 1:37:31]** why

**[1:37:31 – 1:37:32]** but trust me

**[1:37:32 – 1:37:36]** since

**[1:37:36 – 1:37:36]** we are also

**[1:37:36 – 1:37:37]** doing approximations

**[1:37:37 – 1:37:38]** here

**[1:37:38 – 1:37:38]** in order

**[1:37:38 – 1:37:39]** for those

**[1:37:39 – 1:37:40]** approximations

**[1:37:40 – 1:37:41]** to actually work

**[1:37:41 – 1:37:42]** we need

**[1:37:42 – 1:37:43]** to have

**[1:37:43 – 1:37:44]** very good values

**[1:37:44 – 1:37:45]** of the actual gradients

**[1:37:45 – 1:37:46]** like true values

**[1:37:46 – 1:37:47]** or at least

**[1:37:47 – 1:37:48]** very good approximations

**[1:37:48 – 1:37:49]** we cannot just

**[1:37:49 – 1:37:50]** replace these

**[1:37:50 – 1:37:51]** GIs

**[1:37:51 – 1:37:51]** with

**[1:37:51 – 1:37:53]** sampled versions

**[1:37:53 – 1:37:54]** with huge variances

**[1:37:54 – 1:37:55]** and hope for the best

**[1:37:55 – 1:37:56]** the best will not come

**[1:37:56 – 1:37:57]** so

**[1:37:57 – 1:37:58]** it's

**[1:37:58 – 1:37:59]** it's an interesting

**[1:37:59 – 1:38:00]** and

**[1:38:00 – 1:38:01]** a very

**[1:38:01 – 1:38:02]** practical

**[1:38:02 – 1:38:03]** actually

**[1:38:03 – 1:38:04]** open problem

**[1:38:04 – 1:38:05]** for deep learning

**[1:38:05 – 1:38:06]** like can we do

**[1:38:06 – 1:38:06]** better

**[1:38:06 – 1:38:07]** can we

**[1:38:07 – 1:38:09]** can we maybe modify

**[1:38:09 – 1:38:10]** quasi-newton algorithms

**[1:38:10 – 1:38:11]** so that

**[1:38:11 – 1:38:12]** they are

**[1:38:12 – 1:38:14]** they will start working

**[1:38:14 – 1:38:15]** so that

**[1:38:15 – 1:38:16]** we can

**[1:38:16 – 1:38:17]** for example

**[1:38:17 – 1:38:19]** use stochastic gradients

**[1:38:19 – 1:38:21]** this sample estimates

**[1:38:21 – 1:38:22]** instead of true gradients

**[1:38:22 – 1:38:22]** and

**[1:38:22 – 1:38:23]** still

**[1:38:23 – 1:38:25]** go where we want to go

**[1:38:25 – 1:38:27]** this is unknown

**[1:38:27 – 1:38:28]** and

**[1:38:28 – 1:38:29]** probably we can't

**[1:38:29 – 1:38:29]** because

**[1:38:29 – 1:38:31]** lots of smart people

**[1:38:31 – 1:38:32]** have already thought about this

**[1:38:32 – 1:38:33]** and

**[1:38:33 – 1:38:34]** unfortunately

**[1:38:34 – 1:38:37]** no solution has come

**[1:38:37 – 1:38:40]** but

**[1:38:40 – 1:38:43]** of course

**[1:38:43 – 1:38:44]** stochastic gradient descent

**[1:38:44 – 1:38:46]** so

**[1:38:46 – 1:38:47]** now

**[1:38:47 – 1:38:47]** okay

**[1:38:47 – 1:38:47]** so now

**[1:38:47 – 1:38:48]** the actual

**[1:38:48 – 1:38:50]** formula of the update

**[1:38:50 – 1:38:50]** is this

**[1:38:50 – 1:38:52]** wk plus 1

**[1:38:52 – 1:38:54]** is wk

**[1:38:54 – 1:38:55]** minus

**[1:38:55 – 1:38:56]** some learning rate

**[1:38:56 – 1:38:58]** times

**[1:38:58 – 1:39:01]** okay let me just

**[1:39:01 – 1:39:01]** call it

**[1:39:01 – 1:39:02]** times

**[1:39:02 – 1:39:03]** gk hat

**[1:39:03 – 1:39:04]** so times this

**[1:39:04 – 1:39:06]** sampled gradient

**[1:39:06 – 1:39:08]** I will call it

**[1:39:08 – 1:39:09]** sgd

**[1:39:09 – 1:39:10]** stochastic gradient descent

**[1:39:10 – 1:39:11]** and of course

**[1:39:11 – 1:39:12]** this is also not

**[1:39:12 – 1:39:13]** the end of the story

**[1:39:13 – 1:39:13]** this is

**[1:39:13 – 1:39:15]** the first natural

**[1:39:15 – 1:39:16]** step

**[1:39:16 – 1:39:17]** the simplest possible

**[1:39:17 – 1:39:17]** algorithm

**[1:39:17 – 1:39:19]** and of course

**[1:39:19 – 1:39:20]** there have been

**[1:39:20 – 1:39:21]** lots and lots

**[1:39:21 – 1:39:21]** of modifications

**[1:39:21 – 1:39:22]** and improvements

**[1:39:22 – 1:39:23]** of this idea

**[1:39:23 – 1:39:24]** so after the break

**[1:39:24 – 1:39:25]** we'll discuss those

**[1:39:25 – 1:39:26]** they also lie

**[1:39:26 – 1:39:27]** at the very heart

**[1:39:27 – 1:39:28]** of deep learning

**[1:39:28 – 1:39:30]** and for now

**[1:39:30 – 1:39:31]** are there any questions

**[1:39:31 – 1:39:33]** about sgd

**[1:39:33 – 1:39:34]** backprop

**[1:39:34 – 1:39:41]** okay

**[1:39:41 – 1:39:42]** if no questions

**[1:39:42 – 1:39:44]** then let's have a break

**[1:39:44 – 1:39:46]** and when we reconvene

**[1:39:46 – 1:39:47]** we go to

**[1:39:47 – 1:39:48]** sgd variations

**[1:39:48 – 1:39:49]** and algorithms

**[1:39:49 – 1:39:50]** that people actually use

**[1:39:50 – 1:39:51]** to train neural networks

**[1:39:51 – 1:39:52]** break

**[1:39:54 – 2:01:16]** let's

**[2:01:16 – 2:01:17]** let's continue

**[2:01:17 – 2:01:19]** so

**[2:01:19 – 2:01:22]** we stopped

**[2:01:22 – 2:01:22]** at the notion

**[2:01:22 – 2:01:23]** of

**[2:01:23 – 2:01:25]** stochastic gradient descent

**[2:01:25 – 2:01:27]** and I actually

**[2:01:27 – 2:01:28]** before

**[2:01:28 – 2:01:30]** I don't want to

**[2:01:30 – 2:01:31]** delve too deep

**[2:01:31 – 2:01:32]** into the theory

**[2:01:32 – 2:01:33]** of this stuff

**[2:01:33 – 2:01:35]** but I want to show you

**[2:01:35 – 2:01:36]** a couple of

**[2:01:36 – 2:01:38]** pictures and results

**[2:01:38 – 2:01:38]** about it

**[2:01:38 – 2:01:40]** before we actually

**[2:01:40 – 2:01:42]** proceed to

**[2:01:42 – 2:01:47]** to the new algorithms

**[2:01:47 – 2:01:48]** to

**[2:01:48 – 2:01:49]** variations of

**[2:01:49 – 2:01:50]** stochastic gradient descent

**[2:01:50 – 2:01:51]** so

**[2:01:51 – 2:01:56]** what actually happens

**[2:01:56 – 2:01:58]** in stochastic gradient descent

**[2:01:58 – 2:01:59]** you can actually

**[2:01:59 – 2:02:00]** analyze it

**[2:02:00 – 2:02:01]** and classical

**[2:02:01 – 2:02:03]** optimization theory

**[2:02:03 – 2:02:03]** has analyzed it

**[2:02:03 – 2:02:04]** in great detail

**[2:02:04 – 2:02:06]** and

**[2:02:06 – 2:02:08]** what actually happens

**[2:02:08 – 2:02:10]** like what is the

**[2:02:10 – 2:02:13]** correct

**[2:02:13 – 2:02:15]** way of looking at it

**[2:02:15 – 2:02:15]** so to speak

**[2:02:15 – 2:02:16]** well

**[2:02:16 – 2:02:17]** basically

**[2:02:17 – 2:02:21]** a lot of optimization theory

**[2:02:21 – 2:02:24]** was centered around

**[2:02:24 – 2:02:25]** this question

**[2:02:25 – 2:02:26]** so

**[2:02:26 – 2:02:28]** suppose that

**[2:02:28 – 2:02:30]** we are standing over here

**[2:02:30 – 2:02:31]** this is our

**[2:02:31 – 2:02:32]** wk

**[2:02:32 – 2:02:34]** and

**[2:02:34 – 2:02:36]** what does the

**[2:02:36 – 2:02:38]** gradient descent tell us

**[2:02:38 – 2:02:39]** well it tells us

**[2:02:39 – 2:02:42]** the direction where we are supposed to go

**[2:02:42 – 2:02:42]** right

**[2:02:42 – 2:02:44]** so we know that we are supposed to go

**[2:02:44 – 2:02:45]** in the direction of gk

**[2:02:45 – 2:02:48]** but we don't know how far we should go

**[2:02:48 – 2:02:50]** like do we stop here

**[2:02:50 – 2:02:51]** do we go all the way here

**[2:02:51 – 2:02:52]** or here

**[2:02:52 – 2:02:53]** we don't know

**[2:02:53 – 2:02:55]** it's only the direction

**[2:02:55 – 2:02:56]** not the end point

**[2:02:56 – 2:02:59]** so a lot of optimization

**[2:02:59 – 2:03:00]** actually

**[2:03:00 – 2:03:02]** a lot of optimization theory

**[2:03:02 – 2:03:03]** if you

**[2:03:03 – 2:03:07]** if you ever had a class on it

**[2:03:07 – 2:03:09]** or if you will have a class on it

**[2:03:09 – 2:03:11]** a lot of it centers on

**[2:03:11 – 2:03:13]** this one-dimensional optimization problem

**[2:03:13 – 2:03:16]** like we already know the direction

**[2:03:16 – 2:03:19]** and we are optimizing f of x

**[2:03:19 – 2:03:21]** we are let's say minimizing

**[2:03:21 – 2:03:23]** and at this point

**[2:03:23 – 2:03:28]** we already know that I want to go from x

**[2:03:28 – 2:03:31]** to the direction g

**[2:03:31 – 2:03:32]** right

**[2:03:32 – 2:03:37]** but I still don't know how far I want to go

**[2:03:37 – 2:03:40]** so let me treat this as a function of one variable

**[2:03:40 – 2:03:44]** and let me try to actually find the optimal step size

**[2:03:44 – 2:03:48]** let me actually try to find out

**[2:03:48 – 2:03:49]** how far I should go in this direction

**[2:03:49 – 2:03:53]** so it will still be an iterative procedure

**[2:03:53 – 2:03:55]** but hopefully we can say something about

**[2:03:55 – 2:03:56]** how far we should go

**[2:03:56 – 2:04:00]** so a lot of classical results

**[2:04:00 – 2:04:02]** like Wolff's rule or Micho's rule etc. etc.

**[2:04:02 – 2:04:05]** they are all about this kind of problem

**[2:04:05 – 2:04:07]** and we don't care about these results

**[2:04:07 – 2:04:09]** because they don't carry over

**[2:04:09 – 2:04:11]** to stochastic gradient descent that easily

**[2:04:11 – 2:04:15]** what does carry over?

**[2:04:15 – 2:04:21]** so what does classical optimization theory say about

**[2:04:21 – 2:04:22]** okay we discussed this

**[2:04:22 – 2:04:25]** so what does classical optimization theory say

**[2:04:25 – 2:04:27]** about stochastic gradient descent specifically?

**[2:04:28 – 2:04:33]** well SGD if you look at its trajectory

**[2:04:33 – 2:04:35]** if you look at how it works

**[2:04:35 – 2:04:37]** it actually works like this

**[2:04:37 – 2:04:39]** and I will make it precise in a moment

**[2:04:39 – 2:04:42]** but the picture is like this

**[2:04:42 – 2:04:44]** if you are optimizing a function

**[2:04:44 – 2:04:51]** you first go to the neighborhood of the minimum

**[2:04:51 – 2:04:53]** to the neighborhood of the optimum

**[2:04:53 – 2:04:56]** well it's a local optimum in general

**[2:04:56 – 2:04:57]** but this example is global doesn't matter

**[2:04:57 – 2:05:01]** so you go to the neighborhood of a n optimum

**[2:05:01 – 2:05:06]** quite quickly at first

**[2:05:06 – 2:05:09]** this is the initial part of these trajectories

**[2:05:09 – 2:05:10]** as you can see

**[2:05:10 – 2:05:11]** you go basically in the correct direction

**[2:05:11 – 2:05:12]** for a long time

**[2:05:12 – 2:05:16]** but then when you arrive

**[2:05:16 – 2:05:17]** you can't stop

**[2:05:17 – 2:05:19]** you can't converge

**[2:05:19 – 2:05:21]** or at least you can't converge by default

**[2:05:21 – 2:05:24]** so if you have a constant step size

**[2:05:24 – 2:05:26]** in gradient descent

**[2:05:26 – 2:05:29]** if you don't have a schedule

**[2:05:29 – 2:05:32]** of decaying atas down to zero

**[2:05:32 – 2:05:35]** then what's going to happen

**[2:05:35 – 2:05:36]** with stochastic gradient descent

**[2:05:36 – 2:05:39]** is it will go to the neighborhood

**[2:05:39 – 2:05:40]** of the optimum

**[2:05:40 – 2:05:42]** and it will then oscillate there back and forth

**[2:05:42 – 2:05:46]** because it cannot even recognize

**[2:05:46 – 2:05:47]** when it goes to the optimum itself

**[2:05:47 – 2:05:49]** because in the optimum the gradient is zero

**[2:05:49 – 2:05:50]** yes but we don't know the gradient

**[2:05:50 – 2:05:53]** we get a random sample of the gradient

**[2:05:53 – 2:05:54]** which will not be zero

**[2:05:54 – 2:05:57]** and then we will go out of the optimum

**[2:05:57 – 2:05:58]** and somewhere else

**[2:05:58 – 2:06:01]** so we can never know where exactly the optimum is

**[2:06:01 – 2:06:03]** but we can get to a neighborhood of it

**[2:06:03 – 2:06:05]** and then just go around this neighborhood

**[2:06:05 – 2:06:08]** due to our random sampling

**[2:06:08 – 2:06:11]** sounds pretty reasonable

**[2:06:11 – 2:06:14]** and if you do a little bit of math

**[2:06:14 – 2:06:15]** which I think I will skip

**[2:06:15 – 2:06:16]** it's not hard

**[2:06:16 – 2:06:19]** but just I don't think there is any point

**[2:06:19 – 2:06:20]** in us going through this

**[2:06:20 – 2:06:22]** if you do a little bit of math

**[2:06:22 – 2:06:27]** you arrive at an interesting estimate

**[2:06:27 – 2:06:30]** for like how long it's going to take

**[2:06:30 – 2:06:34]** and how stochastic gradient descent converges

**[2:06:34 – 2:06:39]** so this is the result

**[2:06:39 – 2:06:43]** the expected value of the function

**[2:06:43 – 2:06:44]** that we are optimizing

**[2:06:44 – 2:06:48]** at well not quite at xk

**[2:06:48 – 2:06:50]** this is xk head

**[2:06:50 – 2:06:51]** which is an intermediate point

**[2:06:51 – 2:06:52]** let's forget about the details

**[2:06:52 – 2:06:54]** basically after k iterations

**[2:06:54 – 2:06:58]** what we expect the function value to be

**[2:06:58 – 2:07:01]** what is its residue

**[2:07:01 – 2:07:02]** what is its difference

**[2:07:02 – 2:07:03]** with the optimal function value

**[2:07:03 – 2:07:04]** so we are minimizing

**[2:07:05 – 2:07:07]** the optimal value is lower

**[2:07:07 – 2:07:09]** but after k iterations

**[2:07:09 – 2:07:12]** we can expect to be pretty close to the optimum

**[2:07:12 – 2:07:13]** how close

**[2:07:13 – 2:07:14]** there is actually an answer

**[2:07:14 – 2:07:16]** there is a bound like this one

**[2:07:16 – 2:07:19]** so it's less than or equal to

**[2:07:19 – 2:07:22]** actually a previous slide should say

**[2:07:22 – 2:07:23]** less than or equal to

**[2:07:23 – 2:07:24]** r squared

**[2:07:24 – 2:07:26]** r squared is this guy

**[2:07:26 – 2:07:29]** it's the original residue

**[2:07:29 – 2:07:31]** it's how far we were from the optimum in the beginning

**[2:07:31 – 2:07:33]** so this is a constant basically

**[2:07:33 – 2:07:36]** it's fixed at the beginning of our optimization process

**[2:07:36 – 2:07:40]** and then there is this part

**[2:07:40 – 2:07:41]** which is more interesting

**[2:07:41 – 2:07:44]** so alpha i's are the step sizes

**[2:07:44 – 2:07:45]** right

**[2:07:45 – 2:07:47]** so on step size i

**[2:07:47 – 2:07:50]** we go to alpha i times g i

**[2:07:50 – 2:07:52]** we add this vector to alpha i times g i

**[2:07:52 – 2:07:55]** and here in the numerator

**[2:07:55 – 2:07:58]** we get the sum of the norms

**[2:07:58 – 2:08:00]** of this stochastic gradient squared

**[2:08:00 – 2:08:03]** times alpha i squared

**[2:08:03 – 2:08:06]** and in the denominator down here

**[2:08:06 – 2:08:08]** we get just the sum of alphas

**[2:08:08 – 2:08:12]** so if our stochastic gradients are bounded

**[2:08:12 – 2:08:15]** and probably they are

**[2:08:15 – 2:08:17]** even though they are stochastic

**[2:08:17 – 2:08:20]** then we can just plug in this bound

**[2:08:20 – 2:08:21]** whatever it is

**[2:08:21 – 2:08:24]** and we get this general form of the formula

**[2:08:24 – 2:08:28]** so this is exactly what explains

**[2:08:28 – 2:08:31]** the behavior of stochastic gradient descent

**[2:08:31 – 2:08:32]** because look

**[2:08:32 – 2:08:35]** suppose you have constant step size

**[2:08:35 – 2:08:36]** like we just did

**[2:08:36 – 2:08:38]** if we had constant step size

**[2:08:38 – 2:08:40]** let's say all alpha i's are equal to h

**[2:08:40 – 2:08:45]** then this splits into two terms

**[2:08:45 – 2:08:48]** and the first term is r squared over h

**[2:08:48 – 2:08:51]** which is basically over h times k

**[2:08:51 – 2:08:54]** which basically just goes to 0

**[2:08:54 – 2:08:57]** pretty quickly as k grows

**[2:08:57 – 2:08:59]** we go from iteration to iteration

**[2:08:59 – 2:09:00]** k increases

**[2:09:00 – 2:09:02]** so k increases to infinity

**[2:09:02 – 2:09:04]** and the rest is constant

**[2:09:04 – 2:09:05]** so it goes to 0

**[2:09:05 – 2:09:07]** and the second part is just constant

**[2:09:07 – 2:09:11]** so the first part depends on how far we were

**[2:09:11 – 2:09:12]** in the beginning

**[2:09:12 – 2:09:14]** and it goes to 0

**[2:09:14 – 2:09:16]** which means that however far we were

**[2:09:16 – 2:09:19]** we will go close to the correct option

**[2:09:19 – 2:09:20]** on the other hand

**[2:09:20 – 2:09:22]** when we get there

**[2:09:22 – 2:09:25]** even when this part goes to 0

**[2:09:25 – 2:09:27]** there is still the constant part over here

**[2:09:27 – 2:09:29]** which doesn't have k inside

**[2:09:29 – 2:09:33]** so it will remain a constant

**[2:09:33 – 2:09:39]** but of course this formula tells us more than that

**[2:09:39 – 2:09:42]** this is just a special case for the constant step size

**[2:09:42 – 2:09:44]** and this formula also tells us

**[2:09:44 – 2:09:46]** how do we choose alphas

**[2:09:46 – 2:09:49]** so that stochastic gradient descent converges

**[2:09:49 – 2:09:51]** and the answer is

**[2:09:51 – 2:09:53]** well if you want this guy to go to zero

**[2:09:53 – 2:09:56]** what is the easiest way to do it

**[2:09:56 – 2:09:58]** you want your denominator

**[2:09:58 – 2:10:02]** the sum of alphas to go to infinity

**[2:10:02 – 2:10:04]** and at the same time

**[2:10:04 – 2:10:05]** you want your numerator

**[2:10:05 – 2:10:07]** the sum of alpha squared

**[2:10:07 – 2:10:08]** to not go to infinity

**[2:10:08 – 2:10:14]** so the practical conclusion

**[2:10:14 – 2:10:17]** one practical conclusion from this formula

**[2:10:17 – 2:10:19]** is that if you want your

**[2:10:19 – 2:10:21]** stochastic gradient descent to converge

**[2:10:21 – 2:10:25]** and if you want it to converge to an optimum

**[2:10:25 – 2:10:29]** then probably you need to take alphas

**[2:10:29 – 2:10:30]** the step sizes

**[2:10:30 – 2:10:32]** you want to reduce them obviously

**[2:10:32 – 2:10:33]** otherwise you will never converge

**[2:10:33 – 2:10:35]** but how fast do you reduce them?

**[2:10:35 – 2:10:37]** what is the schedule of reducing them?

**[2:10:37 – 2:10:39]** well this formula gives you the answers

**[2:10:39 – 2:10:42]** you want to reduce them in such a way

**[2:10:42 – 2:10:45]** that the sum of alphas goes to infinity

**[2:10:45 – 2:10:46]** diverges

**[2:10:46 – 2:10:48]** but the sum of alpha squares

**[2:10:48 – 2:10:49]** does not go to infinity

**[2:10:49 – 2:10:50]** converges, right?

**[2:10:51 – 2:10:55]** so what would be the easiest example?

**[2:10:55 – 2:10:56]** the easiest example would be just

**[2:10:56 – 2:10:58]** alpha i

**[2:10:58 – 2:11:01]** if we go

**[2:11:01 – 2:11:03]** if we go back in our notation

**[2:11:03 – 2:11:04]** like eta k

**[2:11:04 – 2:11:07]** and we ask a question of

**[2:11:07 – 2:11:09]** how fast should eta k go to 0

**[2:11:09 – 2:11:14]** then this formula gives you

**[2:11:14 – 2:11:15]** a possible answer like this

**[2:11:15 – 2:11:17]** I can do like

**[2:11:17 – 2:11:20]** eta k is something like 1 over k

**[2:11:20 – 2:11:23]** then the sum of eta k goes to infinity

**[2:11:23 – 2:11:26]** but the sum of eta k squared

**[2:11:26 – 2:11:27]** does not go to infinity

**[2:11:27 – 2:11:30]** and therefore stochastic gradient descent

**[2:11:30 – 2:11:31]** converges

**[2:11:31 – 2:11:35]** so it's just one possible answer

**[2:11:35 – 2:11:36]** and to be honest

**[2:11:36 – 2:11:38]** in practice this formula doesn't tell you much

**[2:11:38 – 2:11:41]** so it tells you this general convergence behavior

**[2:11:41 – 2:11:44]** but it doesn't really translate to

**[2:11:44 – 2:11:46]** like real, I don't know

**[2:11:46 – 2:11:48]** estimates on the size of this neighborhood

**[2:11:48 – 2:11:49]** for example

**[2:11:49 – 2:11:52]** because it always includes this g-squared

**[2:11:52 – 2:11:54]** and you can never know g-squared in practice

**[2:11:54 – 2:11:57]** it's bound on your sampled gradients

**[2:11:57 – 2:11:59]** so on like a sample

**[2:11:59 – 2:12:01]** of subsample of your data set

**[2:12:01 – 2:12:02]** which probably has a lot of variance

**[2:12:02 – 2:12:04]** so you don't know g-squared in practice

**[2:12:04 – 2:12:06]** but anyway

**[2:12:06 – 2:12:08]** it does tell you something useful

**[2:12:08 – 2:12:09]** about stochastic gradient descent

**[2:12:09 – 2:12:15]** but this is not really

**[2:12:15 – 2:12:16]** what I will be talking to you about

**[2:12:16 – 2:12:19]** now in the second part of our class

**[2:12:19 – 2:12:22]** what I am going to be talking to you about

**[2:12:22 – 2:12:25]** is a very different problem

**[2:12:25 – 2:12:27]** of stochastic gradient descent

**[2:12:27 – 2:12:31]** one second, sorry

**[2:12:31 – 2:12:47]** yeah, sorry

**[2:12:47 – 2:12:51]** so what I will be talking to you about

**[2:12:51 – 2:12:52]** is a different problem

**[2:12:52 – 2:12:53]** of stochastic gradient descent

**[2:12:53 – 2:12:56]** so let me show you

**[2:12:56 – 2:12:57]** what the problem actually is

**[2:12:57 – 2:12:59]** it's over here

**[2:12:59 – 2:13:01]** yeah

**[2:13:01 – 2:13:05]** so let me

**[2:13:05 – 2:13:07]** just let me first

**[2:13:07 – 2:13:09]** write down a very simple formula

**[2:13:09 – 2:13:10]** this

**[2:13:10 – 2:13:12]** okay, so we discussed

**[2:13:12 – 2:13:13]** SGD

**[2:13:13 – 2:13:14]** now let's say

**[2:13:14 – 2:13:16]** point number five

**[2:13:16 – 2:13:19]** is SGD

**[2:13:19 – 2:13:20]** improvements

**[2:13:20 – 2:13:23]** improvements

**[2:13:23 – 2:13:25]** and variations

**[2:13:25 – 2:13:30]** so what is the problem

**[2:13:30 – 2:13:31]** that we are solving

**[2:13:31 – 2:13:31]** what is

**[2:13:31 – 2:13:32]** an important

**[2:13:32 – 2:13:34]** problem

**[2:13:34 – 2:13:35]** of all of this

**[2:13:35 – 2:13:38]** of stochastic gradient descent

**[2:13:38 – 2:13:40]** let's consider

**[2:13:40 – 2:13:42]** the following example

**[2:13:42 – 2:13:44]** it's as simple

**[2:13:44 – 2:13:46]** as they come

**[2:13:46 – 2:13:47]** it's probably like

**[2:13:47 – 2:13:48]** the easiest

**[2:13:48 – 2:13:49]** optimization problem

**[2:13:49 – 2:13:50]** possible

**[2:13:50 – 2:13:52]** I will have

**[2:13:52 – 2:13:54]** a function

**[2:13:54 – 2:13:56]** of two variables

**[2:13:56 – 2:13:57]** x and y

**[2:13:57 – 2:13:59]** and it will look like

**[2:13:59 – 2:14:00]** this x squared

**[2:14:00 – 2:14:01]** plus a constant

**[2:14:01 – 2:14:03]** times y squared

**[2:14:03 – 2:14:04]** okay

**[2:14:04 – 2:14:06]** and I want to minimize it

**[2:14:06 – 2:14:07]** with respect to x and y

**[2:14:07 – 2:14:09]** so here

**[2:14:09 – 2:14:10]** sorry

**[2:14:10 – 2:14:12]** here is the function

**[2:14:12 – 2:14:12]** right

**[2:14:12 – 2:14:13]** the

**[2:14:13 – 2:14:13]** the

**[2:14:13 – 2:14:14]** contour plot

**[2:14:14 – 2:14:15]** of the function

**[2:14:15 – 2:14:17]** it's

**[2:14:17 – 2:14:18]** the very

**[2:14:18 – 2:14:19]** easiest

**[2:14:19 – 2:14:19]** problem

**[2:14:19 – 2:14:20]** the very easiest

**[2:14:20 – 2:14:21]** optimization problem

**[2:14:21 – 2:14:22]** possible right

**[2:14:22 – 2:14:22]** it's quadratic

**[2:14:22 – 2:14:24]** the minimum

**[2:14:24 – 2:14:25]** is at zero

**[2:14:25 – 2:14:26]** we immediately

**[2:14:26 – 2:14:27]** see that the

**[2:14:27 – 2:14:28]** minimum is at zero

**[2:14:28 – 2:14:30]** it's convex

**[2:14:30 – 2:14:31]** it goes to zero

**[2:14:31 – 2:14:32]** everything is great

**[2:14:32 – 2:14:33]** everything is fine

**[2:14:33 – 2:14:34]** right

**[2:14:34 – 2:14:35]** so very very

**[2:14:35 – 2:14:36]** simple problem

**[2:14:36 – 2:14:37]** however you want

**[2:14:37 – 2:14:38]** to look at it

**[2:14:38 – 2:14:39]** for example

**[2:14:39 – 2:14:40]** if you want to use

**[2:14:40 – 2:14:41]** Newton's method

**[2:14:41 – 2:14:41]** if you want to use

**[2:14:41 – 2:14:42]** the second order method

**[2:14:42 – 2:14:44]** you go to zero

**[2:14:44 – 2:14:44]** in one step

**[2:14:44 – 2:14:45]** because there is

**[2:14:45 – 2:14:46]** no approximation now

**[2:14:46 – 2:14:47]** the second order

**[2:14:47 – 2:14:49]** is just the function f

**[2:14:49 – 2:14:51]** but

**[2:14:51 – 2:14:52]** what does

**[2:14:52 – 2:14:54]** first order

**[2:14:54 – 2:14:56]** what do first order

**[2:14:56 – 2:14:56]** methods do

**[2:14:56 – 2:14:58]** how does gradient descent

**[2:14:58 – 2:14:59]** tackle this

**[2:14:59 – 2:15:00]** well

**[2:15:00 – 2:15:02]** it turns out

**[2:15:02 – 2:15:04]** that it depends a lot

**[2:15:04 – 2:15:05]** on the constant

**[2:15:05 – 2:15:07]** we shouldn't matter

**[2:15:07 – 2:15:07]** right

**[2:15:07 – 2:15:08]** but it does

**[2:15:08 – 2:15:09]** depend a lot

**[2:15:09 – 2:15:10]** on the constant

**[2:15:10 – 2:15:12]** so here I start

**[2:15:12 – 2:15:12]** with this constant

**[2:15:12 – 2:15:13]** so you can see

**[2:15:13 – 2:15:15]** that this is the function

**[2:15:15 – 2:15:15]** x squared

**[2:15:15 – 2:15:16]** plus rho

**[2:15:16 – 2:15:17]** times y squared

**[2:15:17 – 2:15:18]** and you can see

**[2:15:18 – 2:15:19]** that I begin with

**[2:15:19 – 2:15:20]** rho equal to

**[2:15:20 – 2:15:21]** one half

**[2:15:21 – 2:15:22]** so it's almost

**[2:15:22 – 2:15:24]** a circle

**[2:15:24 – 2:15:25]** it's like slightly

**[2:15:25 – 2:15:26]** elongated ellipse

**[2:15:26 – 2:15:28]** when it's almost a circle

**[2:15:28 – 2:15:28]** everything works

**[2:15:28 – 2:15:29]** works beautifully

**[2:15:29 – 2:15:30]** right

**[2:15:30 – 2:15:31]** so I tried a few

**[2:15:31 – 2:15:32]** learning rates

**[2:15:32 – 2:15:34]** and one

**[2:15:34 – 2:15:34]** okay so

**[2:15:34 – 2:15:35]** one over a hundred

**[2:15:35 – 2:15:37]** was a bit too slow

**[2:15:37 – 2:15:38]** and it didn't go

**[2:15:38 – 2:15:39]** all the way to zero

**[2:15:39 – 2:15:40]** that's fine

**[2:15:40 – 2:15:41]** of course I can choose

**[2:15:41 – 2:15:41]** a learning rate

**[2:15:41 – 2:15:42]** which is too slow

**[2:15:42 – 2:15:43]** that's in my hands

**[2:15:43 – 2:15:45]** but larger learning rates

**[2:15:45 – 2:15:47]** just went straight to zero

**[2:15:47 – 2:15:48]** it was all fine

**[2:15:48 – 2:15:49]** so there is absolutely

**[2:15:49 – 2:15:51]** no problem in

**[2:15:51 – 2:15:53]** actually sorry

**[2:15:53 – 2:15:55]** it shouldn't be SGD here

**[2:15:55 – 2:15:55]** it's just

**[2:15:55 – 2:15:57]** it's just gradient descent

**[2:15:57 – 2:15:57]** right

**[2:15:57 – 2:15:58]** there is no

**[2:15:58 – 2:16:00]** mini batch

**[2:16:00 – 2:16:01]** there are no mini batches

**[2:16:01 – 2:16:02]** nothing is stochastic here

**[2:16:02 – 2:16:05]** so let me fix that

**[2:16:05 – 2:16:07]** yeah

**[2:16:07 – 2:16:08]** so just regular gradient descent

**[2:16:08 – 2:16:10]** it goes straight to zero

**[2:16:10 – 2:16:10]** everything works fine

**[2:16:10 – 2:16:13]** but what if I

**[2:16:13 – 2:16:16]** start reducing row further

**[2:16:16 – 2:16:17]** what if it's now

**[2:16:17 – 2:16:18]** not 1 over 2

**[2:16:18 – 2:16:19]** but 1 over 20

**[2:16:19 – 2:16:21]** well

**[2:16:21 – 2:16:22]** what happens

**[2:16:22 – 2:16:23]** as I reduce row

**[2:16:23 – 2:16:26]** the coordinates

**[2:16:26 – 2:16:29]** become more

**[2:16:29 – 2:16:30]** like their scale

**[2:16:30 – 2:16:31]** becomes more different

**[2:16:31 – 2:16:32]** the coordinates

**[2:16:32 – 2:16:33]** become more

**[2:16:33 – 2:16:35]** imbalanced

**[2:16:35 – 2:16:36]** so

**[2:16:36 – 2:16:39]** for example

**[2:16:39 – 2:16:40]** here

**[2:16:40 – 2:16:41]** row is

**[2:16:41 – 2:16:42]** y

**[2:16:42 – 2:16:44]** changes

**[2:16:44 – 2:16:45]** 50 times slower

**[2:16:45 – 2:16:46]** than x

**[2:16:46 – 2:16:48]** so what does it mean

**[2:16:48 – 2:16:49]** for gradient descent

**[2:16:49 – 2:16:50]** it means that

**[2:16:50 – 2:16:51]** horizontally

**[2:16:51 – 2:16:52]** in terms of x

**[2:16:52 – 2:16:53]** it's exactly the same

**[2:16:53 – 2:16:54]** we go to 0

**[2:16:54 – 2:16:55]** and we stay there

**[2:16:55 – 2:16:56]** no problem

**[2:16:56 – 2:16:58]** but in terms of y

**[2:16:58 – 2:17:01]** well now it takes

**[2:17:01 – 2:17:02]** a longer time

**[2:17:02 – 2:17:03]** to go to 0

**[2:17:03 – 2:17:03]** right

**[2:17:03 – 2:17:06]** but while I am at the level

**[2:17:06 – 2:17:07]** of 0.05

**[2:17:07 – 2:17:09]** it's still quite possible

**[2:17:09 – 2:17:09]** so

**[2:17:09 – 2:17:10]** but notice that

**[2:17:10 – 2:17:11]** like the

**[2:17:11 – 2:17:13]** the range of good

**[2:17:13 – 2:17:14]** learning rates

**[2:17:14 – 2:17:14]** begins to shrink

**[2:17:14 – 2:17:15]** right

**[2:17:15 – 2:17:16]** so before that

**[2:17:16 – 2:17:19]** for a more or less

**[2:17:19 – 2:17:19]** a circle

**[2:17:19 – 2:17:20]** it was fine

**[2:17:20 – 2:17:21]** unless I chose

**[2:17:21 – 2:17:22]** the learning rate

**[2:17:22 – 2:17:23]** like actively too low

**[2:17:23 – 2:17:25]** but now

**[2:17:25 – 2:17:26]** 0.1

**[2:17:26 – 2:17:27]** is also kind of too low

**[2:17:27 – 2:17:29]** only 0.5

**[2:17:29 – 2:17:30]** gets to 0

**[2:17:30 – 2:17:31]** in 200 iterations

**[2:17:31 – 2:17:32]** which is quite a lot

**[2:17:32 – 2:17:33]** for such a simple function

**[2:17:33 – 2:17:34]** right

**[2:17:34 – 2:17:38]** and if I continue

**[2:17:38 – 2:17:39]** in this way

**[2:17:39 – 2:17:41]** then pretty soon

**[2:17:41 – 2:17:43]** everything will be too slow

**[2:17:43 – 2:17:46]** and here is the catch

**[2:17:46 – 2:17:47]** so you could say

**[2:17:47 – 2:17:48]** oh but why don't you

**[2:17:48 – 2:17:49]** just increase the learning rate

**[2:17:49 – 2:17:50]** of course

**[2:17:50 – 2:17:51]** for this function

**[2:17:51 – 2:17:52]** you should go faster

**[2:17:52 – 2:17:54]** but the point

**[2:17:54 – 2:17:55]** the problem is

**[2:17:55 – 2:17:56]** I really can't

**[2:17:56 – 2:17:57]** because

**[2:17:57 – 2:17:58]** okay

**[2:17:58 – 2:17:59]** I can go from

**[2:17:59 – 2:18:01]** 0.5

**[2:18:01 – 2:18:02]** to 0.9

**[2:18:02 – 2:18:04]** or even 0.99

**[2:18:04 – 2:18:05]** and

**[2:18:05 – 2:18:06]** yeah

**[2:18:06 – 2:18:07]** it will get me

**[2:18:07 – 2:18:08]** a little bit closer

**[2:18:08 – 2:18:09]** to zero

**[2:18:09 – 2:18:10]** but

**[2:18:10 – 2:18:12]** I cannot go over one

**[2:18:12 – 2:18:13]** because

**[2:18:13 – 2:18:15]** if I go over one

**[2:18:15 – 2:18:16]** even a little bit

**[2:18:16 – 2:18:17]** then

**[2:18:17 – 2:18:18]** the x coordinate

**[2:18:18 – 2:18:19]** starts to diverge

**[2:18:19 – 2:18:20]** right

**[2:18:20 – 2:18:21]** because

**[2:18:21 – 2:18:22]** along the x coordinate

**[2:18:22 – 2:18:25]** the coefficient

**[2:18:25 – 2:18:26]** is still one

**[2:18:26 – 2:18:27]** so

**[2:18:27 – 2:18:27]** of course

**[2:18:27 – 2:18:29]** the problem is not that

**[2:18:29 – 2:18:30]** y changes slowly

**[2:18:30 – 2:18:33]** in absolute values

**[2:18:33 – 2:18:34]** that wouldn't be a problem

**[2:18:34 – 2:18:34]** of course

**[2:18:34 – 2:18:35]** the problem is that

**[2:18:35 – 2:18:36]** x and y

**[2:18:36 – 2:18:36]** are changing

**[2:18:36 – 2:18:38]** at very different rates

**[2:18:38 – 2:18:39]** x and y

**[2:18:39 – 2:18:41]** have very different scales

**[2:18:41 – 2:18:42]** and

**[2:18:42 – 2:18:43]** at this point

**[2:18:43 – 2:18:44]** even for

**[2:18:44 – 2:18:45]** something like

**[2:18:45 – 2:18:49]** 500-200 fold difference

**[2:18:49 – 2:18:50]** between them

**[2:18:50 – 2:18:52]** there's already

**[2:18:52 – 2:18:54]** no good learning rate

**[2:18:54 – 2:18:55]** for gradient descent

**[2:18:55 – 2:18:56]** even though

**[2:18:56 – 2:18:57]** it's

**[2:18:57 – 2:18:59]** so it either diverges

**[2:18:59 – 2:19:00]** or it just

**[2:19:00 – 2:19:01]** takes hopelessly long

**[2:19:01 – 2:19:03]** to go anywhere

**[2:19:03 – 2:19:03]** right

**[2:19:03 – 2:19:04]** so we can do

**[2:19:04 – 2:19:05]** 2,000 iterations

**[2:19:05 – 2:19:06]** then we will probably

**[2:19:06 – 2:19:07]** get there

**[2:19:07 – 2:19:08]** yeah okay

**[2:19:08 – 2:19:09]** with 2,000 iterations

**[2:19:09 – 2:19:10]** we will get there

**[2:19:10 – 2:19:10]** but

**[2:19:10 – 2:19:12]** 2,000 iterations

**[2:19:12 – 2:19:14]** of gradient descent

**[2:19:14 – 2:19:16]** for a quadratic function

**[2:19:16 – 2:19:17]** starting from

**[2:19:17 – 2:19:19]** 0.1 and 3 halves

**[2:19:19 – 2:19:20]** and going to 0

**[2:19:20 – 2:19:22]** it doesn't make any sense

**[2:19:22 – 2:19:22]** right

**[2:19:22 – 2:19:25]** so

**[2:19:25 – 2:19:27]** here is the problem

**[2:19:27 – 2:19:27]** right

**[2:19:27 – 2:19:29]** when

**[2:19:29 – 2:19:33]** even

**[2:19:33 – 2:19:35]** even in very simple cases

**[2:19:35 – 2:19:36]** when

**[2:19:36 – 2:19:38]** the different variables

**[2:19:38 – 2:19:39]** in

**[2:19:39 – 2:19:41]** your optimization function

**[2:19:41 – 2:19:43]** in your

**[2:19:43 – 2:19:45]** set of variables

**[2:19:45 – 2:19:46]** when different variables

**[2:19:46 – 2:19:49]** begin to differ in scale

**[2:19:49 – 2:19:50]** when they begin

**[2:19:50 – 2:19:51]** to have

**[2:19:51 – 2:19:54]** different rates

**[2:19:54 – 2:19:55]** at which we should move

**[2:19:55 – 2:19:55]** along them

**[2:19:55 – 2:19:58]** everything kind of fails

**[2:19:58 – 2:19:59]** gradient descent

**[2:19:59 – 2:20:00]** cannot

**[2:20:00 – 2:20:01]** have a unified

**[2:20:01 – 2:20:02]** rate

**[2:20:02 – 2:20:03]** that we should do

**[2:20:03 – 2:20:05]** and I think

**[2:20:05 – 2:20:07]** yeah

**[2:20:07 – 2:20:07]** sorry

**[2:20:07 – 2:20:09]** this is the next step

**[2:20:09 – 2:20:10]** so

**[2:20:10 – 2:20:12]** this is the

**[2:20:12 – 2:20:12]** mostly

**[2:20:12 – 2:20:14]** this is the problem

**[2:20:14 – 2:20:14]** that we are solving

**[2:20:14 – 2:20:15]** and

**[2:20:15 – 2:20:16]** we will go through

**[2:20:16 – 2:20:17]** several different

**[2:20:17 – 2:20:20]** ideas

**[2:20:20 – 2:20:21]** that people had

**[2:20:21 – 2:20:22]** while solving it

**[2:20:22 – 2:20:22]** I

**[2:20:22 – 2:20:24]** will not

**[2:20:24 – 2:20:26]** this is not

**[2:20:26 – 2:20:27]** a historical lesson

**[2:20:27 – 2:20:28]** the ideas that we

**[2:20:28 – 2:20:29]** discuss are still

**[2:20:29 – 2:20:30]** real and

**[2:20:30 – 2:20:30]** useful

**[2:20:30 – 2:20:30]** so

**[2:20:30 – 2:20:33]** let's go through

**[2:20:33 – 2:20:33]** these ideas

**[2:20:33 – 2:20:35]** the first step

**[2:20:35 – 2:20:37]** the first idea

**[2:20:37 – 2:20:39]** okay so let me

**[2:20:39 – 2:20:39]** maybe

**[2:20:39 – 2:20:40]** maybe let's start

**[2:20:40 – 2:20:41]** with step zero

**[2:20:41 – 2:20:42]** I will set up

**[2:20:42 – 2:20:43]** the notation first

**[2:20:43 – 2:20:44]** because I will

**[2:20:44 – 2:20:45]** reuse it

**[2:20:45 – 2:20:46]** all the time

**[2:20:46 – 2:20:47]** so the notation

**[2:20:47 – 2:20:47]** is

**[2:20:47 – 2:20:51]** I go

**[2:20:51 – 2:20:51]** from

**[2:20:51 – 2:20:53]** x

**[2:20:53 – 2:20:54]** k minus

**[2:20:54 – 2:20:54]** 1

**[2:20:54 – 2:20:56]** to

**[2:20:56 – 2:20:57]** x

**[2:20:57 – 2:20:57]** k

**[2:20:57 – 2:20:58]** okay

**[2:20:58 – 2:20:59]** so I'm

**[2:20:59 – 2:21:00]** optimizing something

**[2:21:00 – 2:21:00]** like f

**[2:21:00 – 2:21:01]** of x

**[2:21:01 – 2:21:03]** I have

**[2:21:03 – 2:21:04]** the vector

**[2:21:04 – 2:21:05]** x of variables

**[2:21:05 – 2:21:06]** and

**[2:21:06 – 2:21:07]** recently

**[2:21:07 – 2:21:08]** I went from

**[2:21:08 – 2:21:09]** x k minus

**[2:21:09 – 2:21:09]** 1 to

**[2:21:09 – 2:21:10]** x k

**[2:21:10 – 2:21:11]** I call this

**[2:21:11 – 2:21:12]** vector

**[2:21:12 – 2:21:12]** u k

**[2:21:12 – 2:21:14]** or u k

**[2:21:14 – 2:21:15]** u k minus

**[2:21:15 – 2:21:15]** 1

**[2:21:15 – 2:21:15]** I think

**[2:21:15 – 2:21:16]** yeah

**[2:21:16 – 2:21:17]** so for the word

**[2:21:17 – 2:21:17]** update

**[2:21:17 – 2:21:18]** so u k minus

**[2:21:18 – 2:21:19]** 1 is

**[2:21:19 – 2:21:21]** x k minus

**[2:21:21 – 2:21:21]** x k minus

**[2:21:21 – 2:21:22]** 1

**[2:21:22 – 2:21:22]** it's my last

**[2:21:22 – 2:21:23]** update

**[2:21:23 – 2:21:24]** and now

**[2:21:24 – 2:21:25]** I am at

**[2:21:25 – 2:21:25]** point x k

**[2:21:25 – 2:21:27]** and

**[2:21:27 – 2:21:28]** let's say

**[2:21:28 – 2:21:29]** I have a gradient

**[2:21:29 – 2:21:31]** g k

**[2:21:31 – 2:21:31]** here

**[2:21:31 – 2:21:32]** so

**[2:21:32 – 2:21:34]** at this point

**[2:21:34 – 2:21:37]** let's just assume

**[2:21:37 – 2:21:37]** that we are

**[2:21:37 – 2:21:38]** talking about

**[2:21:38 – 2:21:39]** stochastic gradient

**[2:21:39 – 2:21:40]** and this is not

**[2:21:40 – 2:21:40]** the true gradient

**[2:21:40 – 2:21:42]** this is the

**[2:21:42 – 2:21:43]** stochastic estimate

**[2:21:43 – 2:21:44]** or it could be

**[2:21:44 – 2:21:45]** a true gradient

**[2:21:45 – 2:21:46]** for what I'm going

**[2:21:46 – 2:21:46]** to tell you now

**[2:21:46 – 2:21:47]** it doesn't matter

**[2:21:47 – 2:21:48]** so

**[2:21:48 – 2:21:49]** there is

**[2:21:49 – 2:21:50]** a direction

**[2:21:50 – 2:21:51]** that the gradient

**[2:21:51 – 2:21:51]** tells you

**[2:21:51 – 2:21:53]** maybe it's a sample

**[2:21:53 – 2:21:54]** maybe it's the true one

**[2:21:54 – 2:21:55]** for what I'm about

**[2:21:55 – 2:21:56]** to say

**[2:21:56 – 2:21:56]** it doesn't matter

**[2:21:56 – 2:21:58]** but there is a gradient

**[2:21:58 – 2:22:00]** direction over here

**[2:22:00 – 2:22:03]** so classical

**[2:22:03 – 2:22:03]** SGD

**[2:22:03 – 2:22:06]** or GD

**[2:22:06 – 2:22:06]** or whatever

**[2:22:06 – 2:22:08]** would do it

**[2:22:08 – 2:22:08]** this way

**[2:22:08 – 2:22:10]** XK plus 1

**[2:22:10 – 2:22:11]** would be

**[2:22:11 – 2:22:12]** XK

**[2:22:12 – 2:22:13]** plus

**[2:22:13 – 2:22:14]** some

**[2:22:14 – 2:22:15]** alpha

**[2:22:15 – 2:22:16]** times

**[2:22:16 – 2:22:17]** GK

**[2:22:17 – 2:22:17]** right

**[2:22:17 – 2:22:18]** so let me say

**[2:22:18 – 2:22:19]** that this is

**[2:22:19 – 2:22:20]** oh sorry

**[2:22:20 – 2:22:21]** minus

**[2:22:21 – 2:22:21]** right

**[2:22:21 – 2:22:22]** we are minimizing

**[2:22:22 – 2:22:23]** some minus

**[2:22:23 – 2:22:24]** so let me say

**[2:22:24 – 2:22:25]** that this is already

**[2:22:25 – 2:22:26]** minus alpha

**[2:22:26 – 2:22:27]** times GK

**[2:22:27 – 2:22:29]** minus alpha

**[2:22:29 – 2:22:30]** times GK

**[2:22:30 – 2:22:31]** and

**[2:22:31 – 2:22:32]** in the simplest

**[2:22:32 – 2:22:34]** example of SGD

**[2:22:34 – 2:22:35]** this is

**[2:22:35 – 2:22:36]** X plus 1

**[2:22:36 – 2:22:37]** this is

**[2:22:37 – 2:22:38]** XK plus 1

**[2:22:38 – 2:22:39]** and

**[2:22:39 – 2:22:40]** UK

**[2:22:40 – 2:22:41]** is just

**[2:22:41 – 2:22:43]** minus alpha

**[2:22:43 – 2:22:43]** times GK

**[2:22:43 – 2:22:44]** that's it

**[2:22:44 – 2:22:48]** so

**[2:22:48 – 2:22:50]** idea number 1

**[2:22:50 – 2:22:52]** let's go over the ideas

**[2:22:52 – 2:22:54]** idea number 1

**[2:22:54 – 2:22:55]** is called

**[2:22:55 – 2:22:57]** momentum

**[2:22:57 – 2:23:01]** momentum

**[2:23:01 – 2:23:02]** like

**[2:23:02 – 2:23:04]** like in school

**[2:23:04 – 2:23:05]** in high school physics

**[2:23:05 – 2:23:06]** right

**[2:23:06 – 2:23:07]** the impulse

**[2:23:07 – 2:23:08]** the momentum

**[2:23:08 – 2:23:10]** of motion

**[2:23:10 – 2:23:11]** what's the English word

**[2:23:11 – 2:23:11]** for that

**[2:23:11 – 2:23:12]** whatever

**[2:23:12 – 2:23:13]** okay

**[2:23:13 – 2:23:14]** so the

**[2:23:14 – 2:23:14]** the momentum

**[2:23:14 – 2:23:15]** which is like

**[2:23:15 – 2:23:16]** m times v

**[2:23:16 – 2:23:17]** in high school physics

**[2:23:17 – 2:23:19]** what

**[2:23:19 – 2:23:21]** how does it appear here

**[2:23:21 – 2:23:22]** well

**[2:23:22 – 2:23:23]** let's go back

**[2:23:23 – 2:23:23]** to our

**[2:23:23 – 2:23:24]** picture

**[2:23:24 – 2:23:25]** we had

**[2:23:25 – 2:23:26]** xk minus 1

**[2:23:26 – 2:23:28]** and we just

**[2:23:28 – 2:23:29]** went to

**[2:23:29 – 2:23:30]** xk

**[2:23:30 – 2:23:31]** through a vector

**[2:23:31 – 2:23:31]** called

**[2:23:31 – 2:23:32]** uk minus 1

**[2:23:32 – 2:23:34]** and there is

**[2:23:34 – 2:23:35]** a direction

**[2:23:35 – 2:23:36]** that the gradient

**[2:23:36 – 2:23:37]** wants us to go

**[2:23:37 – 2:23:38]** minus alpha

**[2:23:38 – 2:23:39]** times jk

**[2:23:39 – 2:23:43]** so the

**[2:23:43 – 2:23:44]** momentum

**[2:23:44 – 2:23:45]** method

**[2:23:45 – 2:23:46]** says

**[2:23:46 – 2:23:46]** well

**[2:23:46 – 2:23:48]** what are we really

**[2:23:48 – 2:23:49]** doing

**[2:23:49 – 2:23:50]** like what's the

**[2:23:50 – 2:23:51]** physical view

**[2:23:51 – 2:23:51]** of this

**[2:23:51 – 2:23:54]** what does it

**[2:23:54 – 2:23:54]** all mean

**[2:23:54 – 2:23:56]** well it looks like

**[2:23:56 – 2:23:56]** gradient descent

**[2:23:56 – 2:23:57]** looks like

**[2:23:57 – 2:23:59]** a bow

**[2:23:59 – 2:24:00]** rolling down

**[2:24:00 – 2:24:00]** some kind

**[2:24:00 – 2:24:01]** of a slope

**[2:24:01 – 2:24:02]** right

**[2:24:02 – 2:24:03]** it's like a

**[2:24:03 – 2:24:04]** material point

**[2:24:04 – 2:24:05]** and it's

**[2:24:05 – 2:24:06]** on a slope

**[2:24:06 – 2:24:07]** so it rolls

**[2:24:07 – 2:24:07]** down the

**[2:24:07 – 2:24:08]** direction

**[2:24:08 – 2:24:08]** where

**[2:24:08 – 2:24:09]** the gradient

**[2:24:09 – 2:24:10]** tells it to

**[2:24:10 – 2:24:10]** go

**[2:24:10 – 2:24:11]** in the

**[2:24:11 – 2:24:12]** steepest

**[2:24:12 – 2:24:12]** descent

**[2:24:12 – 2:24:13]** direction

**[2:24:13 – 2:24:13]** so

**[2:24:13 – 2:24:16]** so why

**[2:24:16 – 2:24:16]** don't we

**[2:24:16 – 2:24:17]** take this

**[2:24:17 – 2:24:17]** hint

**[2:24:17 – 2:24:19]** from regular

**[2:24:19 – 2:24:19]** Newtonian

**[2:24:19 – 2:24:20]** physics

**[2:24:20 – 2:24:21]** and why

**[2:24:21 – 2:24:21]** don't we

**[2:24:21 – 2:24:22]** actually

**[2:24:22 – 2:24:24]** apply it

**[2:24:24 – 2:24:24]** to

**[2:24:24 – 2:24:26]** how to say

**[2:24:26 – 2:24:29]** why don't

**[2:24:29 – 2:24:29]** we also

**[2:24:29 – 2:24:30]** add another

**[2:24:30 – 2:24:30]** physical

**[2:24:30 – 2:24:32]** thing from

**[2:24:32 – 2:24:32]** there

**[2:24:32 – 2:24:33]** inertia

**[2:24:33 – 2:24:34]** why don't

**[2:24:34 – 2:24:35]** we add

**[2:24:35 – 2:24:35]** this

**[2:24:35 – 2:24:36]** conservation

**[2:24:36 – 2:24:37]** of momentum

**[2:24:37 – 2:24:37]** here

**[2:24:37 – 2:24:38]** basically

**[2:24:38 – 2:24:39]** what this

**[2:24:39 – 2:24:39]** means is

**[2:24:39 – 2:24:40]** if your

**[2:24:40 – 2:24:41]** ball goes

**[2:24:41 – 2:24:41]** down the

**[2:24:41 – 2:24:42]** slope

**[2:24:42 – 2:24:43]** and the

**[2:24:43 – 2:24:43]** slope

**[2:24:43 – 2:24:43]** suddenly

**[2:24:43 – 2:24:44]** changes

**[2:24:44 – 2:24:45]** then for

**[2:24:45 – 2:24:45]** a while

**[2:24:45 – 2:24:46]** the ball

**[2:24:46 – 2:24:46]** will follow

**[2:24:46 – 2:24:47]** its current

**[2:24:47 – 2:24:47]** velocity

**[2:24:47 – 2:24:48]** right

**[2:24:48 – 2:24:48]** so it's

**[2:24:48 – 2:24:49]** going to

**[2:24:49 – 2:24:50]** have some

**[2:24:50 – 2:24:51]** momentum

**[2:24:51 – 2:24:54]** formally

**[2:24:54 – 2:24:54]** what it

**[2:24:54 – 2:24:55]** means is

**[2:24:55 – 2:24:56]** when I

**[2:24:56 – 2:24:57]** am here

**[2:24:57 – 2:24:59]** and I

**[2:24:59 – 2:24:59]** have come

**[2:24:59 – 2:25:00]** from here

**[2:25:00 – 2:25:01]** that's why

**[2:25:01 – 2:25:02]** I was

**[2:25:02 – 2:25:03]** drawing the

**[2:25:03 – 2:25:03]** previous

**[2:25:03 – 2:25:04]** update too

**[2:25:04 – 2:25:06]** I not

**[2:25:06 – 2:25:07]** only move

**[2:25:07 – 2:25:07]** along the

**[2:25:07 – 2:25:08]** gradient

**[2:25:08 – 2:25:09]** but I

**[2:25:09 – 2:25:10]** also

**[2:25:10 – 2:25:11]** conserve

**[2:25:11 – 2:25:13]** a bit

**[2:25:13 – 2:25:14]** of the

**[2:25:14 – 2:25:14]** previous

**[2:25:14 – 2:25:15]** update

**[2:25:15 – 2:25:16]** so I

**[2:25:16 – 2:25:17]** also

**[2:25:17 – 2:25:18]** add some

**[2:25:18 – 2:25:19]** gamma times

**[2:25:19 – 2:25:20]** u k

**[2:25:20 – 2:25:20]** minus one

**[2:25:20 – 2:25:21]** so this

**[2:25:21 – 2:25:21]** is the

**[2:25:21 – 2:25:22]** inertial

**[2:25:22 – 2:25:23]** motion

**[2:25:23 – 2:25:23]** I follow

**[2:25:23 – 2:25:24]** the already

**[2:25:24 – 2:25:25]** existing

**[2:25:25 – 2:25:25]** momentum

**[2:25:25 – 2:25:28]** and then

**[2:25:28 – 2:25:30]** so my

**[2:25:30 – 2:25:31]** final update

**[2:25:31 – 2:25:32]** will be the

**[2:25:32 – 2:25:32]** sum of

**[2:25:32 – 2:25:33]** these guys

**[2:25:33 – 2:25:33]** right

**[2:25:33 – 2:25:35]** so then

**[2:25:35 – 2:25:36]** I will go

**[2:25:36 – 2:25:36]** over here

**[2:25:36 – 2:25:37]** this will be

**[2:25:37 – 2:25:38]** x k

**[2:25:38 – 2:25:38]** plus one

**[2:25:38 – 2:25:40]** so now

**[2:25:40 – 2:25:42]** x k

**[2:25:42 – 2:25:43]** plus one

**[2:25:43 – 2:25:44]** is x k

**[2:25:44 – 2:25:45]** plus

**[2:25:45 – 2:25:46]** gamma

**[2:25:46 – 2:25:47]** times u

**[2:25:47 – 2:25:48]** k minus

**[2:25:48 – 2:25:48]** one

**[2:25:48 – 2:25:49]** we carry over

**[2:25:49 – 2:25:50]** part of the

**[2:25:50 – 2:25:50]** update

**[2:25:50 – 2:25:52]** minus alpha

**[2:25:52 – 2:25:53]** times u k

**[2:25:53 – 2:25:54]** so now

**[2:25:54 – 2:25:55]** this is

**[2:25:55 – 2:25:55]** u k

**[2:25:55 – 2:25:57]** okay

**[2:25:57 – 2:26:00]** so we

**[2:26:00 – 2:26:00]** keep

**[2:26:00 – 2:26:02]** a part of

**[2:26:02 – 2:26:02]** the momentum

**[2:26:02 – 2:26:03]** and actually

**[2:26:03 – 2:26:04]** in practice

**[2:26:04 – 2:26:04]** let me tell

**[2:26:04 – 2:26:05]** you right away

**[2:26:05 – 2:26:06]** that in practice

**[2:26:06 – 2:26:06]** we keep a very

**[2:26:06 – 2:26:07]** large part of

**[2:26:07 – 2:26:08]** the momentum

**[2:26:08 – 2:26:08]** so whenever

**[2:26:08 – 2:26:09]** you have

**[2:26:09 – 2:26:10]** anything momentum

**[2:26:10 – 2:26:12]** like gamma

**[2:26:12 – 2:26:14]** is 0.95

**[2:26:14 – 2:26:16]** 0.99

**[2:26:16 – 2:26:16]** maybe even

**[2:26:16 – 2:26:17]** more

**[2:26:17 – 2:26:18]** so usually

**[2:26:18 – 2:26:19]** in practice

**[2:26:19 – 2:26:19]** you want to

**[2:26:19 – 2:26:19]** carry over

**[2:26:19 – 2:26:20]** a lot of

**[2:26:20 – 2:26:21]** the momentum

**[2:26:21 – 2:26:21]** there is

**[2:26:21 – 2:26:22]** little friction

**[2:26:22 – 2:26:23]** there should

**[2:26:23 – 2:26:23]** be some

**[2:26:23 – 2:26:24]** friction

**[2:26:24 – 2:26:24]** but not

**[2:26:24 – 2:26:24]** much

**[2:26:24 – 2:26:29]** and you

**[2:26:29 – 2:26:31]** just keep

**[2:26:31 – 2:26:31]** going in

**[2:26:31 – 2:26:32]** the same

**[2:26:32 – 2:26:32]** direction

**[2:26:32 – 2:26:33]** so what

**[2:26:33 – 2:26:33]** does it

**[2:26:33 – 2:26:33]** do

**[2:26:33 – 2:26:34]** why is it

**[2:26:34 – 2:26:34]** a good

**[2:26:34 – 2:26:35]** idea

**[2:26:35 – 2:26:36]** what it

**[2:26:36 – 2:26:37]** does is

**[2:26:37 – 2:26:39]** it keeps

**[2:26:39 – 2:26:40]** going forward

**[2:26:40 – 2:26:42]** along some

**[2:26:42 – 2:26:42]** direction

**[2:26:42 – 2:26:46]** keeps going

**[2:26:46 – 2:26:47]** forward along

**[2:26:47 – 2:26:47]** some direction

**[2:26:47 – 2:26:48]** and if

**[2:26:48 – 2:26:50]** the slope

**[2:26:50 – 2:26:51]** doesn't change

**[2:26:51 – 2:26:51]** in direction

**[2:26:51 – 2:26:52]** if we are

**[2:26:52 – 2:26:53]** still if the

**[2:26:53 – 2:26:54]** gradient still

**[2:26:54 – 2:26:54]** gets us to

**[2:26:54 – 2:26:55]** go in

**[2:26:55 – 2:26:57]** along in

**[2:26:57 – 2:26:57]** the same

**[2:26:57 – 2:26:58]** way then

**[2:26:58 – 2:26:59]** I will

**[2:26:59 – 2:27:00]** gradually go

**[2:27:00 – 2:27:00]** faster and

**[2:27:00 – 2:27:01]** faster right

**[2:27:01 – 2:27:02]** as the ball

**[2:27:02 – 2:27:02]** rolls down

**[2:27:02 – 2:27:03]** the slope

**[2:27:03 – 2:27:03]** it will roll

**[2:27:03 – 2:27:04]** faster and

**[2:27:04 – 2:27:04]** faster it will

**[2:27:04 – 2:27:05]** pick up

**[2:27:05 – 2:27:06]** speed and

**[2:27:06 – 2:27:07]** this is

**[2:27:07 – 2:27:09]** exactly what

**[2:27:09 – 2:27:10]** hopefully is

**[2:27:10 – 2:27:10]** going to

**[2:27:10 – 2:27:11]** happen over

**[2:27:11 – 2:27:12]** here

**[2:27:12 – 2:27:15]** I'll go to

**[2:27:15 – 2:27:15]** the picture

**[2:27:15 – 2:27:16]** later but

**[2:27:16 – 2:27:17]** hopefully what's

**[2:27:17 – 2:27:17]** going to happen

**[2:27:17 – 2:27:18]** over here

**[2:27:18 – 2:27:20]** so along

**[2:27:20 – 2:27:20]** the x

**[2:27:20 – 2:27:21]** direction

**[2:27:21 – 2:27:23]** the ball

**[2:27:23 – 2:27:24]** will go back

**[2:27:24 – 2:27:24]** and forth

**[2:27:24 – 2:27:25]** but then it

**[2:27:25 – 2:27:26]** will oscillate

**[2:27:26 – 2:27:27]** and stabilize

**[2:27:27 – 2:27:27]** in zero

**[2:27:27 – 2:27:30]** because in

**[2:27:30 – 2:27:30]** the x

**[2:27:30 – 2:27:31]** direction

**[2:27:31 – 2:27:32]** it's a steep

**[2:27:32 – 2:27:32]** slope

**[2:27:32 – 2:27:34]** and pretty

**[2:27:34 – 2:27:34]** soon we

**[2:27:34 – 2:27:36]** will go to

**[2:27:36 – 2:27:36]** the opposite

**[2:27:36 – 2:27:38]** part of the

**[2:27:38 – 2:27:38]** slope

**[2:27:38 – 2:27:39]** then back

**[2:27:39 – 2:27:39]** and back

**[2:27:39 – 2:27:40]** so if you

**[2:27:40 – 2:27:41]** imagine it

**[2:27:41 – 2:27:42]** as a ball

**[2:27:42 – 2:27:42]** actually rolling

**[2:27:42 – 2:27:44]** down this

**[2:27:44 – 2:27:45]** ravine

**[2:27:45 – 2:27:46]** then you

**[2:27:46 – 2:27:47]** will kind of

**[2:27:47 – 2:27:48]** intuitively see

**[2:27:48 – 2:27:48]** that that's

**[2:27:48 – 2:27:49]** what's going

**[2:27:49 – 2:27:49]** to happen

**[2:27:49 – 2:27:50]** but along

**[2:27:50 – 2:27:51]** the y-axis

**[2:27:51 – 2:27:52]** it will

**[2:27:52 – 2:27:52]** speed up

**[2:27:52 – 2:27:53]** right

**[2:27:53 – 2:27:54]** yes the

**[2:27:54 – 2:27:54]** slope is

**[2:27:54 – 2:27:55]** small

**[2:27:55 – 2:27:56]** yes y

**[2:27:56 – 2:27:56]** along the

**[2:27:56 – 2:27:57]** y-axis

**[2:27:57 – 2:27:58]** it's not

**[2:27:58 – 2:27:59]** steep

**[2:27:59 – 2:28:00]** it's shallow

**[2:28:00 – 2:28:02]** but it

**[2:28:02 – 2:28:03]** still goes

**[2:28:03 – 2:28:03]** and goes

**[2:28:03 – 2:28:04]** and you

**[2:28:04 – 2:28:04]** pick up

**[2:28:04 – 2:28:05]** speed as

**[2:28:05 – 2:28:05]** you go

**[2:28:05 – 2:28:07]** so this

**[2:28:07 – 2:28:07]** is the

**[2:28:07 – 2:28:08]** original

**[2:28:08 – 2:28:08]** motivation

**[2:28:08 – 2:28:09]** and the

**[2:28:09 – 2:28:09]** idea for

**[2:28:09 – 2:28:10]** the momentum

**[2:28:10 – 2:28:11]** approach

**[2:28:11 – 2:28:13]** and let

**[2:28:13 – 2:28:14]** me immediately

**[2:28:14 – 2:28:15]** tell you the

**[2:28:15 – 2:28:15]** next idea

**[2:28:15 – 2:28:16]** which is a

**[2:28:16 – 2:28:17]** small modification

**[2:28:17 – 2:28:17]** of the

**[2:28:17 – 2:28:18]** momentum

**[2:28:18 – 2:28:18]** approach

**[2:28:18 – 2:28:20]** a small

**[2:28:20 – 2:28:21]** but actually

**[2:28:21 – 2:28:22]** very very

**[2:28:22 – 2:28:23]** useful

**[2:28:23 – 2:28:24]** both theoretically

**[2:28:24 – 2:28:24]** and practically

**[2:28:24 – 2:28:25]** very very

**[2:28:25 – 2:28:25]** interesting

**[2:28:25 – 2:28:26]** modification

**[2:28:26 – 2:28:28]** the second

**[2:28:28 – 2:28:28]** approach

**[2:28:28 – 2:28:30]** is called

**[2:28:30 – 2:28:32]** Nesterov

**[2:28:32 – 2:28:33]** accelerated

**[2:28:33 – 2:28:34]** gradients

**[2:28:34 – 2:28:41]** you can see

**[2:28:41 – 2:28:42]** the acronym

**[2:28:42 – 2:28:42]** NEC

**[2:28:42 – 2:28:43]** sometimes

**[2:28:43 – 2:28:44]** or just

**[2:28:44 – 2:28:45]** Nesterov's

**[2:28:45 – 2:28:45]** method

**[2:28:45 – 2:28:46]** or something

**[2:28:46 – 2:28:46]** like that

**[2:28:46 – 2:28:47]** Yuri Nesterov

**[2:28:47 – 2:28:48]** was a Soviet

**[2:28:48 – 2:28:48]** mathematician

**[2:28:48 – 2:28:49]** who invented

**[2:28:49 – 2:28:50]** it sometime

**[2:28:50 – 2:28:51]** in the 1980s

**[2:28:51 – 2:28:53]** and Nesterov's

**[2:28:53 – 2:28:54]** idea is

**[2:28:54 – 2:28:55]** really simple

**[2:28:55 – 2:28:56]** and really

**[2:28:56 – 2:28:56]** great

**[2:28:56 – 2:28:59]** so let's

**[2:28:59 – 2:29:00]** go back

**[2:29:00 – 2:29:00]** to this picture

**[2:29:00 – 2:29:01]** I will not

**[2:29:01 – 2:29:01]** copy

**[2:29:01 – 2:29:02]** it doesn't

**[2:29:02 – 2:29:02]** matter

**[2:29:02 – 2:29:03]** but let's

**[2:29:03 – 2:29:03]** go back

**[2:29:03 – 2:29:03]** to this

**[2:29:03 – 2:29:03]** picture

**[2:29:03 – 2:29:07]** so what

**[2:29:07 – 2:29:08]** does the

**[2:29:08 – 2:29:08]** method of

**[2:29:08 – 2:29:09]** momentum

**[2:29:09 – 2:29:10]** tells us

**[2:29:10 – 2:29:11]** it tells us

**[2:29:11 – 2:29:12]** well we

**[2:29:12 – 2:29:12]** are here

**[2:29:12 – 2:29:13]** now

**[2:29:13 – 2:29:14]** and our

**[2:29:14 – 2:29:15]** next update

**[2:29:15 – 2:29:15]** has two

**[2:29:15 – 2:29:16]** components

**[2:29:16 – 2:29:16]** the gradient

**[2:29:16 – 2:29:17]** component

**[2:29:17 – 2:29:17]** and the

**[2:29:17 – 2:29:18]** momentum

**[2:29:18 – 2:29:18]** component

**[2:29:18 – 2:29:19]** so we

**[2:29:19 – 2:29:20]** stand over

**[2:29:20 – 2:29:20]** here

**[2:29:20 – 2:29:21]** we compute

**[2:29:21 – 2:29:21]** the gradient

**[2:29:21 – 2:29:22]** and we get

**[2:29:22 – 2:29:23]** both components

**[2:29:23 – 2:29:24]** and that gives

**[2:29:24 – 2:29:24]** us our update

**[2:29:24 – 2:29:27]** Nestor's idea

**[2:29:27 – 2:29:27]** is this

**[2:29:27 – 2:29:28]** wait

**[2:29:28 – 2:29:28]** okay

**[2:29:28 – 2:29:29]** so we are

**[2:29:29 – 2:29:29]** here

**[2:29:29 – 2:29:32]** and when

**[2:29:32 – 2:29:32]** we arrived

**[2:29:32 – 2:29:33]** here

**[2:29:33 – 2:29:33]** we don't

**[2:29:33 – 2:29:33]** yet know

**[2:29:33 – 2:29:34]** the gradient

**[2:29:34 – 2:29:34]** so we

**[2:29:34 – 2:29:35]** should be

**[2:29:35 – 2:29:35]** we should

**[2:29:35 – 2:29:36]** get to

**[2:29:36 – 2:29:36]** work on

**[2:29:36 – 2:29:37]** calculating

**[2:29:37 – 2:29:37]** gk

**[2:29:37 – 2:29:38]** right

**[2:29:38 – 2:29:39]** but wait

**[2:29:39 – 2:29:39]** but we

**[2:29:39 – 2:29:40]** already know

**[2:29:40 – 2:29:40]** the momentum

**[2:29:40 – 2:29:41]** part

**[2:29:41 – 2:29:41]** right

**[2:29:41 – 2:29:43]** so when

**[2:29:43 – 2:29:43]** we are

**[2:29:43 – 2:29:43]** standing over

**[2:29:43 – 2:29:44]** here

**[2:29:44 – 2:29:45]** after the

**[2:29:45 – 2:29:46]** previous

**[2:29:46 – 2:29:46]** update

**[2:29:46 – 2:29:48]** we already

**[2:29:48 – 2:29:49]** know

**[2:29:49 – 2:29:52]** a part

**[2:29:52 – 2:29:52]** and maybe

**[2:29:52 – 2:29:53]** a large

**[2:29:53 – 2:29:53]** part

**[2:29:53 – 2:29:54]** as I

**[2:29:54 – 2:29:54]** tell

**[2:29:54 – 2:29:54]** as I

**[2:29:54 – 2:29:55]** told you

**[2:29:55 – 2:29:56]** momentum

**[2:29:56 – 2:29:58]** can really

**[2:29:58 – 2:29:59]** pick up

**[2:29:59 – 2:29:59]** speed

**[2:29:59 – 2:30:00]** we know

**[2:30:00 – 2:30:01]** a large

**[2:30:01 – 2:30:01]** part of

**[2:30:01 – 2:30:02]** the next

**[2:30:02 – 2:30:02]** update

**[2:30:02 – 2:30:02]** already

**[2:30:02 – 2:30:04]** so why

**[2:30:04 – 2:30:04]** do we

**[2:30:04 – 2:30:05]** insist on

**[2:30:05 – 2:30:05]** computing

**[2:30:05 – 2:30:05]** the gradient

**[2:30:05 – 2:30:06]** over here

**[2:30:06 – 2:30:08]** why don't

**[2:30:08 – 2:30:09]** we go

**[2:30:09 – 2:30:10]** to this

**[2:30:10 – 2:30:10]** point

**[2:30:10 – 2:30:10]** which we

**[2:30:10 – 2:30:11]** already

**[2:30:11 – 2:30:11]** know

**[2:30:11 – 2:30:12]** it doesn't

**[2:30:12 – 2:30:12]** take

**[2:30:12 – 2:30:12]** anything

**[2:30:12 – 2:30:13]** to go

**[2:30:13 – 2:30:13]** there

**[2:30:13 – 2:30:14]** and calculate

**[2:30:14 – 2:30:15]** the gradient

**[2:30:15 – 2:30:16]** over there

**[2:30:16 – 2:30:19]** so this

**[2:30:19 – 2:30:20]** is

**[2:30:20 – 2:30:21]** negative alpha

**[2:30:21 – 2:30:21]** times

**[2:30:21 – 2:30:22]** let's say

**[2:30:22 – 2:30:23]** g prime

**[2:30:23 – 2:30:23]** k

**[2:30:23 – 2:30:24]** right

**[2:30:24 – 2:30:24]** the gradient

**[2:30:24 – 2:30:25]** computed

**[2:30:25 – 2:30:25]** at this

**[2:30:25 – 2:30:25]** point

**[2:30:25 – 2:30:28]** and then

**[2:30:28 – 2:30:28]** our

**[2:30:28 – 2:30:30]** new update

**[2:30:30 – 2:30:30]** will go

**[2:30:30 – 2:30:30]** here

**[2:30:30 – 2:30:32]** right

**[2:30:32 – 2:30:34]** so in

**[2:30:34 – 2:30:34]** Estorff's

**[2:30:34 – 2:30:35]** accelerated

**[2:30:35 – 2:30:36]** gradients

**[2:30:36 – 2:30:37]** xk

**[2:30:37 – 2:30:37]** plus 1

**[2:30:37 – 2:30:38]** is xk

**[2:30:38 – 2:30:39]** plus

**[2:30:39 – 2:30:40]** gamma

**[2:30:40 – 2:30:40]** times

**[2:30:40 – 2:30:41]** u k

**[2:30:41 – 2:30:42]** minus 1

**[2:30:42 – 2:30:43]** minus

**[2:30:43 – 2:30:44]** alpha

**[2:30:44 – 2:30:45]** times

**[2:30:45 – 2:30:46]** g prime

**[2:30:46 – 2:30:47]** let me

**[2:30:47 – 2:30:47]** write it

**[2:30:47 – 2:30:48]** down

**[2:30:48 – 2:30:49]** it's the

**[2:30:49 – 2:30:49]** gradient

**[2:30:49 – 2:30:50]** not w

**[2:30:50 – 2:30:52]** it's the

**[2:30:52 – 2:30:52]** gradient

**[2:30:52 – 2:30:52]** with respect

**[2:30:52 – 2:30:53]** to x

**[2:30:53 – 2:30:54]** of f

**[2:30:54 – 2:30:55]** not at

**[2:30:55 – 2:30:56]** point

**[2:30:56 – 2:30:56]** xk

**[2:30:56 – 2:30:57]** but at

**[2:30:57 – 2:30:58]** point

**[2:30:58 – 2:30:58]** xk

**[2:30:58 – 2:30:59]** plus

**[2:30:59 – 2:30:59]** gamma

**[2:30:59 – 2:31:00]** times

**[2:31:00 – 2:31:01]** u k

**[2:31:01 – 2:31:01]** minus 1

**[2:31:01 – 2:31:02]** so in

**[2:31:02 – 2:31:03]** this

**[2:31:03 – 2:31:03]** intermediate

**[2:31:03 – 2:31:10]** and

**[2:31:10 – 2:31:10]** yeah

**[2:31:10 – 2:31:12]** not what I

**[2:31:12 – 2:31:12]** meant

**[2:31:12 – 2:31:12]** and this

**[2:31:12 – 2:31:13]** is the

**[2:31:13 – 2:31:14]** UK

**[2:31:14 – 2:31:16]** now

**[2:31:16 – 2:31:32]** yeah

**[2:31:32 – 2:31:33]** and this

**[2:31:33 – 2:31:33]** is the

**[2:31:33 – 2:31:34]** UK

**[2:31:34 – 2:31:37]** so

**[2:31:37 – 2:31:41]** what is

**[2:31:41 – 2:31:42]** like

**[2:31:42 – 2:31:42]** what is

**[2:31:42 – 2:31:43]** the motivation

**[2:31:43 – 2:31:43]** behind this

**[2:31:43 – 2:31:44]** well first

**[2:31:44 – 2:31:44]** of all

**[2:31:44 – 2:31:44]** there is

**[2:31:44 – 2:31:45]** some beautiful

**[2:31:45 – 2:31:45]** mathematics

**[2:31:45 – 2:31:46]** behind it

**[2:31:46 – 2:31:46]** and

**[2:31:46 – 2:31:47]** actually

**[2:31:47 – 2:31:49]** gradient descent

**[2:31:49 – 2:31:50]** with this

**[2:31:50 – 2:31:50]** method

**[2:31:50 – 2:31:51]** starts to

**[2:31:51 – 2:31:52]** even converge

**[2:31:52 – 2:31:52]** asymptotically

**[2:31:52 – 2:31:53]** faster

**[2:31:53 – 2:31:53]** it's

**[2:31:53 – 2:31:54]** some of

**[2:31:54 – 2:31:55]** the asymptotics

**[2:31:55 – 2:31:55]** change

**[2:31:55 – 2:31:56]** when you

**[2:31:56 – 2:31:56]** go from

**[2:31:56 – 2:31:57]** regular

**[2:31:57 – 2:31:58]** momentum

**[2:31:58 – 2:31:58]** estrous

**[2:31:58 – 2:31:58]** momentum

**[2:31:58 – 2:31:59]** but

**[2:31:59 – 2:32:00]** we will not

**[2:32:00 – 2:32:01]** go there

**[2:32:01 – 2:32:02]** the intuitive

**[2:32:02 – 2:32:03]** motivation is

**[2:32:03 – 2:32:04]** this

**[2:32:04 – 2:32:06]** Nesterov's

**[2:32:06 – 2:32:07]** gradients

**[2:32:07 – 2:32:08]** basically do

**[2:32:08 – 2:32:09]** like a look

**[2:32:09 – 2:32:09]** ahead

**[2:32:09 – 2:32:10]** they

**[2:32:10 – 2:32:11]** look forward

**[2:32:11 – 2:32:12]** in time

**[2:32:12 – 2:32:13]** and they

**[2:32:13 – 2:32:15]** appreciate

**[2:32:15 – 2:32:17]** they try to

**[2:32:17 – 2:32:17]** predict

**[2:32:17 – 2:32:18]** what's going

**[2:32:18 – 2:32:18]** to happen

**[2:32:18 – 2:32:19]** and they

**[2:32:19 – 2:32:19]** update

**[2:32:19 – 2:32:20]** based on the

**[2:32:20 – 2:32:21]** future

**[2:32:21 – 2:32:21]** not based on

**[2:32:21 – 2:32:22]** the present

**[2:32:22 – 2:32:22]** which is of

**[2:32:22 – 2:32:23]** course great

**[2:32:23 – 2:32:24]** so if we

**[2:32:24 – 2:32:25]** are on a

**[2:32:25 – 2:32:25]** slope like

**[2:32:25 – 2:32:26]** this

**[2:32:26 – 2:32:27]** right

**[2:32:27 – 2:32:29]** and a

**[2:32:29 – 2:32:29]** ball gets

**[2:32:29 – 2:32:30]** rolling down

**[2:32:30 – 2:32:30]** here

**[2:32:30 – 2:32:31]** so it

**[2:32:31 – 2:32:32]** picks up

**[2:32:32 – 2:32:32]** speed it

**[2:32:32 – 2:32:33]** speeds up

**[2:32:33 – 2:32:34]** and now

**[2:32:34 – 2:32:34]** it's here

**[2:32:34 – 2:32:35]** and the

**[2:32:35 – 2:32:36]** next step

**[2:32:36 – 2:32:36]** would put

**[2:32:36 – 2:32:36]** it over

**[2:32:36 – 2:32:37]** here

**[2:32:37 – 2:32:37]** right

**[2:32:37 – 2:32:39]** so in

**[2:32:39 – 2:32:39]** regular

**[2:32:39 – 2:32:40]** momentum

**[2:32:40 – 2:32:42]** you would

**[2:32:42 – 2:32:43]** continue

**[2:32:43 – 2:32:43]** speeding up

**[2:32:43 – 2:32:44]** because the

**[2:32:44 – 2:32:45]** slope is

**[2:32:45 – 2:32:45]** still in

**[2:32:45 – 2:32:46]** this direction

**[2:32:46 – 2:32:47]** so in

**[2:32:47 – 2:32:47]** regular

**[2:32:47 – 2:32:47]** momentum

**[2:32:47 – 2:32:48]** you would

**[2:32:48 – 2:32:49]** go even

**[2:32:49 – 2:32:49]** further

**[2:32:49 – 2:32:51]** up the

**[2:32:51 – 2:32:51]** opposite

**[2:32:51 – 2:32:51]** wall

**[2:32:51 – 2:32:53]** right

**[2:32:53 – 2:32:55]** but in

**[2:32:55 – 2:32:55]** this

**[2:32:55 – 2:32:55]** terms

**[2:32:55 – 2:32:56]** momentum

**[2:32:56 – 2:32:57]** you would

**[2:32:57 – 2:32:57]** look ahead

**[2:32:57 – 2:32:58]** over here

**[2:32:58 – 2:32:59]** and you

**[2:32:59 – 2:32:59]** would see

**[2:32:59 – 2:33:00]** that now

**[2:33:00 – 2:33:00]** the gradient

**[2:33:00 – 2:33:01]** points in

**[2:33:01 – 2:33:01]** the opposite

**[2:33:01 – 2:33:02]** direction

**[2:33:02 – 2:33:02]** so you

**[2:33:02 – 2:33:03]** are facing

**[2:33:03 – 2:33:03]** a wall

**[2:33:03 – 2:33:04]** in some

**[2:33:04 – 2:33:04]** sense

**[2:33:04 – 2:33:06]** so let's

**[2:33:06 – 2:33:07]** slow down

**[2:33:07 – 2:33:07]** say

**[2:33:07 – 2:33:09]** says

**[2:33:09 – 2:33:09]** urinester

**[2:33:09 – 2:33:12]** and that

**[2:33:12 – 2:33:12]** makes a lot

**[2:33:12 – 2:33:13]** of sense

**[2:33:13 – 2:33:13]** right

**[2:33:13 – 2:33:14]** so

**[2:33:14 – 2:33:17]** that's

**[2:33:17 – 2:33:19]** that's

**[2:33:19 – 2:33:19]** exactly

**[2:33:19 – 2:33:21]** that's

**[2:33:21 – 2:33:21]** exactly

**[2:33:21 – 2:33:22]** what

**[2:33:22 – 2:33:24]** makes it

**[2:33:24 – 2:33:24]** better

**[2:33:24 – 2:33:27]** and

**[2:33:27 – 2:33:27]** if we

**[2:33:27 – 2:33:28]** look

**[2:33:28 – 2:33:29]** at our

**[2:33:29 – 2:33:30]** example

**[2:33:30 – 2:33:30]** here

**[2:33:30 – 2:33:31]** now

**[2:33:31 – 2:33:31]** now I

**[2:33:31 – 2:33:32]** can show

**[2:33:32 – 2:33:32]** you that

**[2:33:32 – 2:33:32]** picture

**[2:33:32 – 2:33:33]** previously

**[2:33:33 – 2:33:34]** we're not

**[2:33:34 – 2:33:34]** old enough

**[2:33:34 – 2:33:35]** to see

**[2:33:35 – 2:33:35]** it

**[2:33:35 – 2:33:36]** but

**[2:33:36 – 2:33:36]** now

**[2:33:36 – 2:33:37]** if you

**[2:33:37 – 2:33:38]** look at

**[2:33:38 – 2:33:38]** this picture

**[2:33:38 – 2:33:39]** it's

**[2:33:39 – 2:33:40]** the same

**[2:33:40 – 2:33:40]** alpha

**[2:33:40 – 2:33:42]** but

**[2:33:42 – 2:33:43]** along with

**[2:33:43 – 2:33:44]** regular

**[2:33:44 – 2:33:44]** gradient

**[2:33:44 – 2:33:44]** descent

**[2:33:44 – 2:33:45]** I also

**[2:33:45 – 2:33:45]** put here

**[2:33:45 – 2:33:46]** gradient

**[2:33:46 – 2:33:46]** descent

**[2:33:46 – 2:33:46]** with

**[2:33:46 – 2:33:47]** momentum

**[2:33:47 – 2:33:47]** it's

**[2:33:47 – 2:33:47]** the

**[2:33:47 – 2:33:48]** orange

**[2:33:48 – 2:33:48]** line

**[2:33:48 – 2:33:49]** and

**[2:33:49 – 2:33:49]** gradient

**[2:33:49 – 2:33:49]** descent

**[2:33:49 – 2:33:50]** with

**[2:33:50 – 2:33:50]** Nesterov's

**[2:33:50 – 2:33:51]** momentum

**[2:33:51 – 2:33:51]** it's

**[2:33:51 – 2:33:51]** the

**[2:33:51 – 2:33:51]** green

**[2:33:51 – 2:33:52]** line

**[2:33:52 – 2:33:53]** and

**[2:33:53 – 2:33:53]** you

**[2:33:53 – 2:33:53]** can

**[2:33:53 – 2:33:53]** see

**[2:33:53 – 2:33:55]** how

**[2:33:55 – 2:33:55]** the

**[2:33:55 – 2:33:56]** oscillations

**[2:33:56 – 2:33:59]** along

**[2:33:59 – 2:33:59]** the

**[2:33:59 – 2:33:59]** x-axis

**[2:33:59 – 2:34:00]** are

**[2:34:00 – 2:34:01]** much

**[2:34:01 – 2:34:01]** much

**[2:34:01 – 2:34:02]** less

**[2:34:02 – 2:34:03]** or

**[2:34:03 – 2:34:03]** much

**[2:34:03 – 2:34:03]** better

**[2:34:03 – 2:34:04]** contained

**[2:34:04 – 2:34:05]** when

**[2:34:05 – 2:34:06]** Nesterov's

**[2:34:06 – 2:34:06]** momentum

**[2:34:06 – 2:34:07]** are

**[2:34:07 – 2:34:07]** used

**[2:34:07 – 2:34:08]** right

**[2:34:08 – 2:34:09]** so

**[2:34:09 – 2:34:09]** again

**[2:34:09 – 2:34:10]** this

**[2:34:10 – 2:34:10]** is

**[2:34:10 – 2:34:10]** the

**[2:34:10 – 2:34:10]** exact

**[2:34:10 – 2:34:11]** same

**[2:34:11 – 2:34:11]** effect

**[2:34:11 – 2:34:11]** because

**[2:34:11 – 2:34:12]** along

**[2:34:12 – 2:34:12]** the

**[2:34:12 – 2:34:12]** x-axis

**[2:34:12 – 2:34:13]** the

**[2:34:13 – 2:34:13]** slope

**[2:34:13 – 2:34:13]** looks

**[2:34:13 – 2:34:14]** like

**[2:34:14 – 2:34:14]** this

**[2:34:14 – 2:34:15]** and

**[2:34:15 – 2:34:16]** the

**[2:34:16 – 2:34:17]** ball

**[2:34:17 – 2:34:17]** the

**[2:34:17 – 2:34:17]** material

**[2:34:17 – 2:34:18]** point

**[2:34:18 – 2:34:18]** rolling

**[2:34:18 – 2:34:18]** down

**[2:34:18 – 2:34:19]** oscillates

**[2:34:19 – 2:34:19]** like

**[2:34:19 – 2:34:19]** this

**[2:34:19 – 2:34:19]** but

**[2:34:19 – 2:34:20]** Nesterov's

**[2:34:20 – 2:34:20]** momentum

**[2:34:20 – 2:34:21]** looks

**[2:34:21 – 2:34:21]** ahead

**[2:34:21 – 2:34:21]** and

**[2:34:21 – 2:34:22]** starts

**[2:34:22 – 2:34:22]** slowing

**[2:34:22 – 2:34:22]** down

**[2:34:22 – 2:34:23]** before

**[2:34:23 – 2:34:23]** the

**[2:34:23 – 2:34:23]** turn

**[2:34:23 – 2:34:24]** like

**[2:34:24 – 2:34:24]** a

**[2:34:24 – 2:34:24]** good

**[2:34:24 – 2:34:25]** driver

**[2:34:25 – 2:34:25]** not

**[2:34:25 – 2:34:25]** like

**[2:34:25 – 2:34:26]** material

**[2:34:26 – 2:34:26]** point

**[2:34:26 – 2:34:28]** so

**[2:34:28 – 2:34:29]** okay

**[2:34:29 – 2:34:30]** so

**[2:34:30 – 2:34:31]** this

**[2:34:31 – 2:34:32]** is

**[2:34:32 – 2:34:33]** what

**[2:34:33 – 2:34:33]** it

**[2:34:33 – 2:34:33]** looks

**[2:34:33 – 2:34:33]** like

**[2:34:33 – 2:34:35]** but

**[2:34:35 – 2:34:36]** of

**[2:34:36 – 2:34:36]** course

**[2:34:36 – 2:34:37]** the

**[2:34:37 – 2:34:37]** idea

**[2:34:37 – 2:34:38]** didn't

**[2:34:38 – 2:34:38]** stop

**[2:34:38 – 2:34:38]** there

**[2:34:38 – 2:34:39]** right

**[2:34:39 – 2:34:41]** and

**[2:34:41 – 2:34:41]** actually

**[2:34:41 – 2:34:42]** both

**[2:34:42 – 2:34:43]** the

**[2:34:43 – 2:34:43]** classical

**[2:34:43 – 2:34:44]** momentum

**[2:34:44 – 2:34:44]** method

**[2:34:44 – 2:34:45]** of

**[2:34:45 – 2:34:45]** momentum

**[2:34:45 – 2:34:46]** which dates

**[2:34:46 – 2:34:46]** back I think

**[2:34:46 – 2:34:47]** to the

**[2:34:47 – 2:34:48]** 1960s

**[2:34:48 – 2:34:48]** and

**[2:34:48 – 2:34:49]** nester of

**[2:34:49 – 2:34:49]** gradients

**[2:34:49 – 2:34:50]** which

**[2:34:50 – 2:34:50]** dates

**[2:34:50 – 2:34:50]** back

**[2:34:50 – 2:34:50]** to the

**[2:34:50 – 2:34:51]** 1980s

**[2:34:51 – 2:34:52]** they come

**[2:34:52 – 2:34:52]** from

**[2:34:52 – 2:34:53]** classical

**[2:34:53 – 2:34:53]** optimization

**[2:34:53 – 2:34:54]** theory

**[2:34:54 – 2:34:55]** they

**[2:34:55 – 2:34:56]** are not

**[2:34:56 – 2:34:57]** special

**[2:34:57 – 2:34:57]** to

**[2:34:57 – 2:34:57]** deep

**[2:34:57 – 2:34:58]** learning

**[2:34:58 – 2:34:58]** in any

**[2:34:58 – 2:34:58]** way

**[2:34:58 – 2:35:01]** but

**[2:35:01 – 2:35:02]** when you

**[2:35:02 – 2:35:02]** actually

**[2:35:02 – 2:35:04]** consider

**[2:35:04 – 2:35:05]** the same

**[2:35:05 – 2:35:06]** kind

**[2:35:06 – 2:35:06]** of

**[2:35:06 – 2:35:06]** problems

**[2:35:06 – 2:35:07]** but in

**[2:35:07 – 2:35:07]** the

**[2:35:07 – 2:35:08]** context

**[2:35:08 – 2:35:08]** of

**[2:35:08 – 2:35:08]** deep

**[2:35:08 – 2:35:08]** learning

**[2:35:08 – 2:35:10]** you

**[2:35:10 – 2:35:12]** see

**[2:35:12 – 2:35:12]** the

**[2:35:12 – 2:35:13]** following

**[2:35:13 – 2:35:14]** point

**[2:35:14 – 2:35:15]** so

**[2:35:15 – 2:35:16]** in

**[2:35:16 – 2:35:16]** deep

**[2:35:16 – 2:35:16]** learning

**[2:35:16 – 2:35:19]** all

**[2:35:19 – 2:35:19]** that we

**[2:35:19 – 2:35:20]** have been

**[2:35:20 – 2:35:20]** doing so

**[2:35:20 – 2:35:21]** far

**[2:35:21 – 2:35:23]** was

**[2:35:23 – 2:35:23]** kind

**[2:35:23 – 2:35:23]** of

**[2:35:23 – 2:35:24]** defined

**[2:35:24 – 2:35:25]** and

**[2:35:25 – 2:35:26]** contained

**[2:35:26 – 2:35:27]** in

**[2:35:27 – 2:35:28]** inside

**[2:35:28 – 2:35:28]** in

**[2:35:28 – 2:35:28]** just

**[2:35:28 – 2:35:29]** the

**[2:35:29 – 2:35:29]** generic

**[2:35:29 – 2:35:30]** Euclidean

**[2:35:30 – 2:35:30]** space

**[2:35:30 – 2:35:31]** of this

**[2:35:31 – 2:35:31]** vector

**[2:35:31 – 2:35:32]** x

**[2:35:32 – 2:35:33]** I'm

**[2:35:33 – 2:35:34]** trying

**[2:35:34 – 2:35:34]** to

**[2:35:34 – 2:35:35]** convey

**[2:35:35 – 2:35:36]** the

**[2:35:36 – 2:35:36]** intuition

**[2:35:36 – 2:35:37]** so

**[2:35:37 – 2:35:37]** like

**[2:35:37 – 2:35:38]** for

**[2:35:38 – 2:35:39]** the

**[2:35:39 – 2:35:39]** method

**[2:35:39 – 2:35:40]** of

**[2:35:40 – 2:35:40]** momentum

**[2:35:40 – 2:35:41]** all

**[2:35:41 – 2:35:41]** directions

**[2:35:41 – 2:35:41]** are

**[2:35:41 – 2:35:42]** equal

**[2:35:42 – 2:35:43]** it

**[2:35:43 – 2:35:43]** doesn't

**[2:35:43 – 2:35:44]** treat

**[2:35:44 – 2:35:44]** x1

**[2:35:44 – 2:35:44]** the

**[2:35:44 – 2:35:45]** first

**[2:35:45 – 2:35:45]** component

**[2:35:45 – 2:35:46]** different

**[2:35:46 – 2:35:46]** from

**[2:35:46 – 2:35:46]** x2

**[2:35:46 – 2:35:46]** different

**[2:35:46 – 2:35:47]** from

**[2:35:47 – 2:35:47]** x10

**[2:35:47 – 2:35:49]** it

**[2:35:49 – 2:35:49]** will

**[2:35:49 – 2:35:50]** just

**[2:35:50 – 2:35:51]** add up

**[2:35:51 – 2:35:52]** some

**[2:35:52 – 2:35:52]** vectors

**[2:35:52 – 2:35:53]** in

**[2:35:53 – 2:35:53]** this

**[2:35:53 – 2:35:53]** space

**[2:35:53 – 2:35:55]** but it

**[2:35:55 – 2:35:56]** turns out

**[2:35:56 – 2:35:57]** that

**[2:35:57 – 2:35:58]** you can

**[2:35:58 – 2:35:58]** do

**[2:35:58 – 2:35:58]** even

**[2:35:58 – 2:35:59]** better

**[2:35:59 – 2:36:00]** if

**[2:36:00 – 2:36:02]** you

**[2:36:02 – 2:36:03]** treat

**[2:36:03 – 2:36:04]** different

**[2:36:04 – 2:36:04]** components

**[2:36:04 – 2:36:06]** of

**[2:36:06 – 2:36:06]** x

**[2:36:06 – 2:36:07]** differently

**[2:36:07 – 2:36:08]** if

**[2:36:08 – 2:36:08]** you

**[2:36:08 – 2:36:08]** for

**[2:36:08 – 2:36:09]** example

**[2:36:09 – 2:36:10]** pick

**[2:36:10 – 2:36:11]** a

**[2:36:11 – 2:36:12]** separate

**[2:36:12 – 2:36:12]** learning

**[2:36:12 – 2:36:13]** rate

**[2:36:13 – 2:36:14]** and

**[2:36:14 – 2:36:14]** a

**[2:36:14 – 2:36:14]** separate

**[2:36:14 – 2:36:15]** changing

**[2:36:15 – 2:36:15]** learning

**[2:36:15 – 2:36:16]** rate

**[2:36:16 – 2:36:17]** for

**[2:36:17 – 2:36:18]** every

**[2:36:18 – 2:36:19]** component

**[2:36:19 – 2:36:19]** of

**[2:36:19 – 2:36:19]** x

**[2:36:19 – 2:36:20]** when

**[2:36:20 – 2:36:20]** you

**[2:36:20 – 2:36:21]** do

**[2:36:21 – 2:36:21]** something

**[2:36:21 – 2:36:21]** like

**[2:36:21 – 2:36:22]** this

**[2:36:22 – 2:36:23]** it's

**[2:36:23 – 2:36:23]** called

**[2:36:23 – 2:36:24]** adaptive

**[2:36:24 – 2:36:24]** gradient

**[2:36:24 – 2:36:25]** descent

**[2:36:25 – 2:36:26]** or

**[2:36:26 – 2:36:27]** actually

**[2:36:27 – 2:36:27]** it's

**[2:36:27 – 2:36:27]** almost

**[2:36:27 – 2:36:28]** always

**[2:36:28 – 2:36:28]** stochastic

**[2:36:28 – 2:36:28]** because

**[2:36:28 – 2:36:29]** now

**[2:36:29 – 2:36:29]** we are

**[2:36:29 – 2:36:29]** in

**[2:36:29 – 2:36:30]** deep

**[2:36:30 – 2:36:30]** learning

**[2:36:30 – 2:36:30]** territory

**[2:36:30 – 2:36:31]** so it's

**[2:36:31 – 2:36:31]** called

**[2:36:31 – 2:36:32]** adaptive

**[2:36:32 – 2:36:33]** stochastic

**[2:36:33 – 2:36:33]** gradient

**[2:36:33 – 2:36:34]** descent

**[2:36:34 – 2:36:34]** and

**[2:36:34 – 2:36:36]** these

**[2:36:36 – 2:36:37]** kind of

**[2:36:37 – 2:36:37]** approaches

**[2:36:37 – 2:36:39]** are

**[2:36:39 – 2:36:39]** basically

**[2:36:39 – 2:36:40]** what we

**[2:36:40 – 2:36:40]** use

**[2:36:40 – 2:36:41]** in

**[2:36:41 – 2:36:41]** deep

**[2:36:41 – 2:36:41]** learning

**[2:36:41 – 2:36:41]** they are

**[2:36:41 – 2:36:42]** the

**[2:36:42 – 2:36:42]** optimization

**[2:36:42 – 2:36:43]** algorithms

**[2:36:43 – 2:36:43]** that you

**[2:36:43 – 2:36:44]** actually

**[2:36:44 – 2:36:44]** use

**[2:36:44 – 2:36:44]** in

**[2:36:44 – 2:36:44]** practice

**[2:36:44 – 2:36:45]** so

**[2:36:45 – 2:36:46]** let me

**[2:36:46 – 2:36:46]** walk you

**[2:36:46 – 2:36:47]** through

**[2:36:47 – 2:36:47]** some

**[2:36:47 – 2:36:47]** of

**[2:36:47 – 2:36:48]** them

**[2:36:48 – 2:36:49]** again

**[2:36:49 – 2:36:49]** it will

**[2:36:49 – 2:36:50]** be

**[2:36:50 – 2:36:50]** like

**[2:36:50 – 2:36:51]** a line

**[2:36:51 – 2:36:51]** of

**[2:36:51 – 2:36:51]** algorithms

**[2:36:51 – 2:36:52]** but

**[2:36:52 – 2:36:52]** they

**[2:36:52 – 2:36:53]** will

**[2:36:53 – 2:36:54]** culminate

**[2:36:54 – 2:36:55]** in

**[2:36:55 – 2:36:55]** ADEM

**[2:36:55 – 2:36:56]** of course

**[2:36:56 – 2:36:57]** and

**[2:36:57 – 2:36:58]** then

**[2:36:58 – 2:36:59]** but

**[2:36:59 – 2:37:00]** to get

**[2:37:00 – 2:37:01]** to ADEM

**[2:37:01 – 2:37:01]** we need

**[2:37:01 – 2:37:01]** to

**[2:37:01 – 2:37:02]** discuss

**[2:37:02 – 2:37:03]** some ideas

**[2:37:03 – 2:37:03]** along the

**[2:37:03 – 2:37:03]** way

**[2:37:03 – 2:37:05]** so

**[2:37:05 – 2:37:08]** adaptive

**[2:37:08 – 2:37:11]** SGD

**[2:37:11 – 2:37:12]** variations

**[2:37:12 – 2:37:16]** well

**[2:37:16 – 2:37:16]** the first

**[2:37:16 – 2:37:16]** variation

**[2:37:16 – 2:37:18]** called

**[2:37:18 – 2:37:19]** ADEGRED

**[2:37:19 – 2:37:20]** it was

**[2:37:20 – 2:37:21]** the original

**[2:37:21 – 2:37:21]** adaptive

**[2:37:21 – 2:37:23]** SGD

**[2:37:23 – 2:37:23]** version

**[2:37:23 – 2:37:24]** ADEGRED

**[2:37:24 – 2:37:25]** just literally

**[2:37:25 – 2:37:25]** means

**[2:37:25 – 2:37:25]** adaptive

**[2:37:25 – 2:37:26]** gradient

**[2:37:26 – 2:37:28]** the first

**[2:37:28 – 2:37:28]** variation

**[2:37:28 – 2:37:29]** worked like

**[2:37:29 – 2:37:30]** this

**[2:37:30 – 2:37:31]** the point

**[2:37:31 – 2:37:31]** was as

**[2:37:31 – 2:37:31]** follows

**[2:37:31 – 2:37:33]** what do

**[2:37:33 – 2:37:34]** we actually

**[2:37:34 – 2:37:34]** want

**[2:37:34 – 2:37:37]** for every

**[2:37:37 – 2:37:38]** direction

**[2:37:38 – 2:37:38]** in X

**[2:37:38 – 2:37:39]** like

**[2:37:39 – 2:37:39]** what

**[2:37:39 – 2:37:40]** kind

**[2:37:40 – 2:37:40]** of

**[2:37:40 – 2:37:41]** logic

**[2:37:41 – 2:37:42]** is behind

**[2:37:42 – 2:37:43]** choosing the

**[2:37:43 – 2:37:43]** learning crate

**[2:37:43 – 2:37:44]** and behind

**[2:37:44 – 2:37:45]** updating the

**[2:37:45 – 2:37:46]** learning crate

**[2:37:46 – 2:37:47]** the logic

**[2:37:47 – 2:37:48]** is this

**[2:37:48 – 2:37:49]** if you are

**[2:37:49 – 2:37:49]** on a

**[2:37:49 – 2:37:50]** shallow

**[2:37:50 – 2:37:50]** slope

**[2:37:50 – 2:37:51]** like this

**[2:37:51 – 2:37:51]** one

**[2:37:51 – 2:37:52]** and you

**[2:37:52 – 2:37:52]** basically

**[2:37:52 – 2:37:53]** go and

**[2:37:53 – 2:37:53]** go in

**[2:37:53 – 2:37:53]** the same

**[2:37:53 – 2:37:54]** direction

**[2:37:54 – 2:37:55]** then you

**[2:37:55 – 2:37:56]** should go

**[2:37:56 – 2:37:56]** quickly

**[2:37:56 – 2:37:57]** you should

**[2:37:57 – 2:37:57]** go fast

**[2:37:57 – 2:37:58]** right

**[2:37:58 – 2:38:01]** but if

**[2:38:01 – 2:38:01]** the slope

**[2:38:01 – 2:38:02]** becomes steep

**[2:38:02 – 2:38:04]** well it

**[2:38:04 – 2:38:05]** cannot be steep

**[2:38:05 – 2:38:05]** for long

**[2:38:05 – 2:38:06]** right

**[2:38:06 – 2:38:08]** if the slope

**[2:38:08 – 2:38:08]** becomes steep

**[2:38:08 – 2:38:09]** it means

**[2:38:09 – 2:38:09]** that the

**[2:38:09 – 2:38:10]** local

**[2:38:10 – 2:38:11]** optimum

**[2:38:11 – 2:38:11]** is close

**[2:38:11 – 2:38:13]** so if

**[2:38:13 – 2:38:13]** you land

**[2:38:13 – 2:38:13]** on a

**[2:38:13 – 2:38:14]** steep slope

**[2:38:14 – 2:38:16]** then you

**[2:38:16 – 2:38:16]** shouldn't

**[2:38:16 – 2:38:17]** carelessly

**[2:38:17 – 2:38:17]** jump

**[2:38:17 – 2:38:18]** further

**[2:38:18 – 2:38:19]** you should

**[2:38:19 – 2:38:20]** slow down

**[2:38:20 – 2:38:24]** and probably

**[2:38:24 – 2:38:25]** converge to

**[2:38:25 – 2:38:25]** the local

**[2:38:25 – 2:38:26]** minimum

**[2:38:26 – 2:38:26]** here

**[2:38:26 – 2:38:27]** so that's

**[2:38:27 – 2:38:27]** that's the

**[2:38:27 – 2:38:28]** idea

**[2:38:28 – 2:38:30]** how does

**[2:38:30 – 2:38:30]** adegret

**[2:38:30 – 2:38:31]** implement

**[2:38:31 – 2:38:31]** this idea

**[2:38:31 – 2:38:33]** well actually

**[2:38:33 – 2:38:33]** pretty simple

**[2:38:33 – 2:38:34]** so I will

**[2:38:34 – 2:38:34]** just write

**[2:38:34 – 2:38:35]** down the

**[2:38:35 – 2:38:35]** update rule

**[2:38:35 – 2:38:37]** x k

**[2:38:37 – 2:38:38]** plus 1

**[2:38:38 – 2:38:39]** i

**[2:38:39 – 2:38:40]** so now

**[2:38:40 – 2:38:40]** we are

**[2:38:40 – 2:38:40]** talking about

**[2:38:40 – 2:38:41]** one specific

**[2:38:41 – 2:38:42]** component

**[2:38:42 – 2:38:42]** in the

**[2:38:42 – 2:38:42]** vector

**[2:38:42 – 2:38:44]** is x

**[2:38:44 – 2:38:45]** k i

**[2:38:45 – 2:38:46]** plus

**[2:38:46 – 2:38:48]** minus

**[2:38:48 – 2:38:51]** minus

**[2:38:51 – 2:38:52]** alpha

**[2:38:52 – 2:38:54]** over the

**[2:38:54 – 2:38:54]** square root

**[2:38:54 – 2:38:56]** of g

**[2:38:56 – 2:38:56]** wait for

**[2:38:56 – 2:38:57]** it

**[2:38:57 – 2:38:58]** g i

**[2:38:58 – 2:39:00]** plus

**[2:39:00 – 2:39:00]** epsilon

**[2:39:00 – 2:39:02]** g i

**[2:39:02 – 2:39:02]** k

**[2:39:02 – 2:39:03]** plus

**[2:39:03 – 2:39:03]** epsilon

**[2:39:03 – 2:39:07]** k i

**[2:39:07 – 2:39:09]** plus

**[2:39:09 – 2:39:10]** epsilon

**[2:39:10 – 2:39:11]** times

**[2:39:11 – 2:39:13]** g

**[2:39:13 – 2:39:14]** k i

**[2:39:14 – 2:39:15]** so

**[2:39:15 – 2:39:17]** it's still

**[2:39:17 – 2:39:17]** it's the

**[2:39:17 – 2:39:17]** same

**[2:39:17 – 2:39:18]** gradient

**[2:39:18 – 2:39:19]** it's the

**[2:39:19 – 2:39:19]** same

**[2:39:19 – 2:39:19]** vector

**[2:39:19 – 2:39:19]** of

**[2:39:19 – 2:39:20]** gradient

**[2:39:20 – 2:39:22]** but

**[2:39:22 – 2:39:22]** the

**[2:39:22 – 2:39:22]** learning

**[2:39:22 – 2:39:23]** rate

**[2:39:23 – 2:39:23]** is now

**[2:39:23 – 2:39:23]** adaptive

**[2:39:23 – 2:39:24]** and what

**[2:39:24 – 2:39:25]** is

**[2:39:25 – 2:39:25]** capital

**[2:39:25 – 2:39:25]** G

**[2:39:25 – 2:39:26]** well

**[2:39:26 – 2:39:26]** capital

**[2:39:26 – 2:39:27]** G

**[2:39:27 – 2:39:29]** is

**[2:39:29 – 2:39:29]** the

**[2:39:29 – 2:39:30]** sum of

**[2:39:30 – 2:39:30]** squares

**[2:39:30 – 2:39:32]** of

**[2:39:32 – 2:39:32]** these

**[2:39:32 – 2:39:33]** gradients

**[2:39:33 – 2:39:34]** so

**[2:39:34 – 2:39:34]** like

**[2:39:34 – 2:39:34]** G

**[2:39:34 – 2:39:35]** K

**[2:39:35 – 2:39:35]** I

**[2:39:35 – 2:39:36]** is

**[2:39:36 – 2:39:36]** G

**[2:39:36 – 2:39:36]** K

**[2:39:36 – 2:39:37]** minus

**[2:39:37 – 2:39:37]** one

**[2:39:37 – 2:39:38]** I

**[2:39:38 – 2:39:38]** plus

**[2:39:38 – 2:39:39]** G

**[2:39:39 – 2:39:39]** K

**[2:39:39 – 2:39:39]** I

**[2:39:39 – 2:39:40]** squared

**[2:39:40 – 2:39:42]** so

**[2:39:42 – 2:39:43]** the

**[2:39:43 – 2:39:43]** capital

**[2:39:43 – 2:39:44]** G

**[2:39:44 – 2:39:46]** accumulates

**[2:39:46 – 2:39:48]** all of

**[2:39:48 – 2:39:48]** the history

**[2:39:48 – 2:39:49]** of the

**[2:39:49 – 2:39:49]** gradients

**[2:39:49 – 2:39:50]** and

**[2:39:50 – 2:39:50]** if

**[2:39:50 – 2:39:50]** there

**[2:39:50 – 2:39:50]** are

**[2:39:50 – 2:39:51]** large

**[2:39:51 – 2:39:51]** gradients

**[2:39:51 – 2:39:52]** then

**[2:39:52 – 2:39:53]** capital

**[2:39:53 – 2:39:53]** G

**[2:39:53 – 2:39:53]** is

**[2:39:53 – 2:39:54]** large

**[2:39:54 – 2:39:54]** and

**[2:39:54 – 2:39:54]** if

**[2:39:54 – 2:39:54]** all

**[2:39:54 – 2:39:55]** gradients

**[2:39:55 – 2:39:55]** are

**[2:39:55 – 2:39:55]** small

**[2:39:55 – 2:39:55]** then

**[2:39:55 – 2:39:56]** it's

**[2:39:56 – 2:39:56]** small

**[2:39:56 – 2:39:58]** this

**[2:39:58 – 2:39:59]** kind

**[2:39:59 – 2:39:59]** of

**[2:39:59 – 2:40:00]** corresponds

**[2:40:00 – 2:40:01]** to

**[2:40:01 – 2:40:01]** our

**[2:40:01 – 2:40:01]** logic

**[2:40:01 – 2:40:02]** right

**[2:40:02 – 2:40:02]** this

**[2:40:02 – 2:40:02]** kind

**[2:40:02 – 2:40:02]** of

**[2:40:02 – 2:40:03]** follows

**[2:40:03 – 2:40:03]** it

**[2:40:03 – 2:40:04]** so

**[2:40:04 – 2:40:04]** while

**[2:40:04 – 2:40:05]** we

**[2:40:05 – 2:40:05]** are

**[2:40:05 – 2:40:05]** on a

**[2:40:05 – 2:40:06]** shallow

**[2:40:06 – 2:40:06]** slope

**[2:40:06 – 2:40:07]** while

**[2:40:07 – 2:40:07]** we should

**[2:40:07 – 2:40:08]** be going

**[2:40:08 – 2:40:08]** fast

**[2:40:08 – 2:40:09]** then

**[2:40:09 – 2:40:10]** we are

**[2:40:10 – 2:40:10]** going

**[2:40:10 – 2:40:10]** fast

**[2:40:10 – 2:40:10]** so

**[2:40:10 – 2:40:11]** we

**[2:40:11 – 2:40:11]** start

**[2:40:11 – 2:40:11]** with

**[2:40:11 – 2:40:11]** a

**[2:40:11 – 2:40:12]** large

**[2:40:12 – 2:40:12]** alpha

**[2:40:12 – 2:40:13]** with

**[2:40:13 – 2:40:13]** a

**[2:40:13 – 2:40:13]** high

**[2:40:13 – 2:40:14]** level

**[2:40:14 – 2:40:14]** high

**[2:40:14 – 2:40:14]** learning

**[2:40:14 – 2:40:15]** rate

**[2:40:15 – 2:40:15]** so

**[2:40:15 – 2:40:15]** at

**[2:40:15 – 2:40:16]** first

**[2:40:16 – 2:40:16]** we

**[2:40:16 – 2:40:16]** start

**[2:40:16 – 2:40:17]** off

**[2:40:17 – 2:40:17]** going

**[2:40:17 – 2:40:18]** quickly

**[2:40:18 – 2:40:20]** and

**[2:40:20 – 2:40:20]** then

**[2:40:20 – 2:40:21]** it

**[2:40:21 – 2:40:21]** goes

**[2:40:21 – 2:40:21]** down

**[2:40:21 – 2:40:22]** but

**[2:40:22 – 2:40:22]** while

**[2:40:22 – 2:40:22]** we

**[2:40:22 – 2:40:23]** are

**[2:40:23 – 2:40:23]** on

**[2:40:23 – 2:40:23]** a

**[2:40:23 – 2:40:24]** shallow

**[2:40:24 – 2:40:25]** slope

**[2:40:25 – 2:40:25]** gk

**[2:40:25 – 2:40:26]** is

**[2:40:26 – 2:40:26]** small

**[2:40:26 – 2:40:26]** and

**[2:40:26 – 2:40:27]** it

**[2:40:27 – 2:40:28]** doesn't

**[2:40:28 – 2:40:28]** go

**[2:40:28 – 2:40:28]** down

**[2:40:28 – 2:40:28]** that

**[2:40:28 – 2:40:28]** much

**[2:40:28 – 2:40:29]** so

**[2:40:29 – 2:40:29]** we

**[2:40:29 – 2:40:29]** are

**[2:40:29 – 2:40:30]** still

**[2:40:30 – 2:40:30]** walking

**[2:40:30 – 2:40:31]** quickly

**[2:40:31 – 2:40:31]** along

**[2:40:31 – 2:40:32]** this

**[2:40:32 – 2:40:32]** line

**[2:40:32 – 2:40:34]** then

**[2:40:34 – 2:40:34]** when

**[2:40:34 – 2:40:34]** we

**[2:40:34 – 2:40:34]** get

**[2:40:34 – 2:40:35]** to

**[2:40:35 – 2:40:35]** a

**[2:40:35 – 2:40:35]** steep

**[2:40:35 – 2:40:35]** slope

**[2:40:35 – 2:40:36]** it

**[2:40:36 – 2:40:37]** means

**[2:40:37 – 2:40:37]** that

**[2:40:37 – 2:40:37]** the

**[2:40:37 – 2:40:38]** current

**[2:40:38 – 2:40:38]** G

**[2:40:38 – 2:40:39]** is

**[2:40:39 – 2:40:39]** high

**[2:40:39 – 2:40:40]** and

**[2:40:40 – 2:40:41]** that

**[2:40:41 – 2:40:41]** means

**[2:40:41 – 2:40:41]** the

**[2:40:41 – 2:40:41]** capital

**[2:40:41 – 2:40:42]** G

**[2:40:42 – 2:40:42]** gets

**[2:40:42 – 2:40:42]** these

**[2:40:42 – 2:40:43]** high

**[2:40:43 – 2:40:44]** terms

**[2:40:44 – 2:40:44]** and

**[2:40:44 – 2:40:44]** it

**[2:40:44 – 2:40:45]** becomes

**[2:40:45 – 2:40:46]** large

**[2:40:46 – 2:40:46]** by

**[2:40:46 – 2:40:46]** itself

**[2:40:46 – 2:40:47]** so

**[2:40:47 – 2:40:47]** now

**[2:40:47 – 2:40:48]** the

**[2:40:48 – 2:40:48]** learning

**[2:40:48 – 2:40:48]** rate

**[2:40:48 – 2:40:49]** shrinks

**[2:40:49 – 2:40:50]** and

**[2:40:50 – 2:40:50]** we

**[2:40:50 – 2:40:50]** go

**[2:40:50 – 2:40:50]** slow

**[2:40:50 – 2:40:51]** that's

**[2:40:51 – 2:40:51]** the

**[2:40:51 – 2:40:52]** idea

**[2:40:52 – 2:40:55]** what

**[2:40:55 – 2:40:56]** is

**[2:40:56 – 2:40:57]** the

**[2:40:57 – 2:40:57]** obvious

**[2:40:57 – 2:40:58]** drawback

**[2:40:58 – 2:40:59]** of

**[2:40:59 – 2:40:59]** this

**[2:40:59 – 2:40:59]** idea

**[2:40:59 – 2:41:00]** what

**[2:41:00 – 2:41:00]** is

**[2:41:00 – 2:41:00]** like

**[2:41:00 – 2:41:00]** what

**[2:41:00 – 2:41:01]** cannot

**[2:41:01 – 2:41:01]** it

**[2:41:01 – 2:41:01]** do

**[2:41:01 – 2:41:03]** well

**[2:41:03 – 2:41:04]** I

**[2:41:04 – 2:41:05]** mean

**[2:41:05 – 2:41:06]** if

**[2:41:06 – 2:41:06]** you

**[2:41:06 – 2:41:06]** look

**[2:41:06 – 2:41:06]** at

**[2:41:06 – 2:41:06]** the

**[2:41:06 – 2:41:07]** denominator

**[2:41:07 – 2:41:08]** and

**[2:41:08 – 2:41:08]** how

**[2:41:08 – 2:41:08]** it's

**[2:41:08 – 2:41:09]** defined

**[2:41:09 – 2:41:09]** and

**[2:41:09 – 2:41:09]** epsilon

**[2:41:09 – 2:41:10]** doesn't

**[2:41:10 – 2:41:10]** mean

**[2:41:10 – 2:41:10]** anything

**[2:41:10 – 2:41:10]** it's

**[2:41:10 – 2:41:11]** just

**[2:41:11 – 2:41:11]** so

**[2:41:11 – 2:41:11]** that

**[2:41:11 – 2:41:12]** we

**[2:41:12 – 2:41:12]** don't

**[2:41:12 – 2:41:12]** divide

**[2:41:12 – 2:41:13]** by

**[2:41:13 – 2:41:13]** zero

**[2:41:13 – 2:41:13]** so

**[2:41:13 – 2:41:13]** epsilon

**[2:41:13 – 2:41:14]** is

**[2:41:14 – 2:41:14]** just

**[2:41:14 – 2:41:14]** a

**[2:41:14 – 2:41:14]** small

**[2:41:14 – 2:41:14]** number

**[2:41:14 – 2:41:17]** if

**[2:41:17 – 2:41:17]** you

**[2:41:17 – 2:41:17]** look

**[2:41:17 – 2:41:17]** at

**[2:41:17 – 2:41:18]** the

**[2:41:18 – 2:41:19]** denominator

**[2:41:19 – 2:41:19]** you

**[2:41:19 – 2:41:19]** see

**[2:41:19 – 2:41:20]** that

**[2:41:20 – 2:41:20]** it

**[2:41:20 – 2:41:20]** grows

**[2:41:20 – 2:41:20]** with

**[2:41:20 – 2:41:21]** time

**[2:41:21 – 2:41:23]** what

**[2:41:23 – 2:41:23]** it

**[2:41:23 – 2:41:24]** means

**[2:41:24 – 2:41:25]** is

**[2:41:25 – 2:41:25]** that

**[2:41:25 – 2:41:27]** once

**[2:41:27 – 2:41:28]** we

**[2:41:28 – 2:41:28]** have

**[2:41:28 – 2:41:28]** been

**[2:41:28 – 2:41:30]** on

**[2:41:30 – 2:41:30]** a

**[2:41:30 – 2:41:31]** steep

**[2:41:31 – 2:41:31]** slope

**[2:41:31 – 2:41:32]** there

**[2:41:32 – 2:41:32]** is

**[2:41:32 – 2:41:32]** no

**[2:41:32 – 2:41:33]** way

**[2:41:33 – 2:41:33]** for

**[2:41:33 – 2:41:33]** us

**[2:41:33 – 2:41:33]** to

**[2:41:33 – 2:41:34]** speed

**[2:41:34 – 2:41:34]** back

**[2:41:34 – 2:41:34]** up

**[2:41:34 – 2:41:34]** again

**[2:41:34 – 2:41:35]** right

**[2:41:35 – 2:41:36]** so

**[2:41:36 – 2:41:37]** if

**[2:41:37 – 2:41:37]** our

**[2:41:37 – 2:41:37]** optimization

**[2:41:37 – 2:41:38]** landscape

**[2:41:38 – 2:41:38]** looks

**[2:41:38 – 2:41:39]** like

**[2:41:39 – 2:41:39]** this

**[2:41:39 – 2:41:41]** we

**[2:41:41 – 2:41:41]** are

**[2:41:41 – 2:41:42]** screwed

**[2:41:42 – 2:41:43]** because

**[2:41:43 – 2:41:44]** we

**[2:41:44 – 2:41:44]** go

**[2:41:44 – 2:41:45]** fast

**[2:41:45 – 2:41:46]** then

**[2:41:46 – 2:41:46]** we

**[2:41:46 – 2:41:46]** get

**[2:41:46 – 2:41:47]** here

**[2:41:47 – 2:41:47]** we

**[2:41:47 – 2:41:48]** slow

**[2:41:48 – 2:41:48]** down

**[2:41:48 – 2:41:49]** but

**[2:41:49 – 2:41:50]** when

**[2:41:50 – 2:41:50]** it

**[2:41:50 – 2:41:50]** becomes

**[2:41:50 – 2:41:51]** shallow

**[2:41:51 – 2:41:52]** again

**[2:41:52 – 2:41:53]** we

**[2:41:53 – 2:41:53]** cannot

**[2:41:53 – 2:41:53]** speed

**[2:41:53 – 2:41:54]** up

**[2:41:54 – 2:41:54]** this

**[2:41:54 – 2:41:55]** denominator

**[2:41:55 – 2:41:55]** will

**[2:41:55 – 2:41:55]** never

**[2:41:55 – 2:41:56]** get

**[2:41:56 – 2:41:56]** smaller

**[2:41:56 – 2:41:57]** right

**[2:41:57 – 2:41:58]** so

**[2:41:58 – 2:41:59]** now

**[2:41:59 – 2:41:59]** we

**[2:41:59 – 2:42:00]** are

**[2:42:00 – 2:42:00]** doomed

**[2:42:00 – 2:42:01]** to

**[2:42:01 – 2:42:01]** going

**[2:42:01 – 2:42:01]** very

**[2:42:01 – 2:42:01]** very

**[2:42:01 – 2:42:02]** slow

**[2:42:02 – 2:42:03]** this

**[2:42:03 – 2:42:03]** is

**[2:42:03 – 2:42:03]** a

**[2:42:03 – 2:42:03]** bad

**[2:42:03 – 2:42:04]** situation

**[2:42:04 – 2:42:04]** for

**[2:42:04 – 2:42:04]** Edegrad

**[2:42:04 – 2:42:07]** so

**[2:42:07 – 2:42:07]** what's

**[2:42:07 – 2:42:08]** what's

**[2:42:08 – 2:42:08]** the

**[2:42:08 – 2:42:09]** solution

**[2:42:09 – 2:42:10]** the

**[2:42:10 – 2:42:10]** obvious

**[2:42:10 – 2:42:11]** modification

**[2:42:11 – 2:42:12]** would be

**[2:42:12 – 2:42:13]** to not

**[2:42:13 – 2:42:14]** use

**[2:42:14 – 2:42:14]** just

**[2:42:14 – 2:42:15]** the

**[2:42:15 – 2:42:15]** sum

**[2:42:15 – 2:42:15]** of

**[2:42:15 – 2:42:16]** gradients

**[2:42:16 – 2:42:16]** but

**[2:42:16 – 2:42:16]** to

**[2:42:16 – 2:42:17]** use

**[2:42:17 – 2:42:17]** some

**[2:42:17 – 2:42:17]** kind

**[2:42:17 – 2:42:17]** of

**[2:42:17 – 2:42:18]** recent

**[2:42:18 – 2:42:18]** history

**[2:42:18 – 2:42:18]** of

**[2:42:18 – 2:42:19]** gradients

**[2:42:19 – 2:42:19]** so

**[2:42:19 – 2:42:20]** if

**[2:42:20 – 2:42:20]** we've

**[2:42:20 – 2:42:20]** had

**[2:42:20 – 2:42:21]** recently

**[2:42:21 – 2:42:25]** high

**[2:42:25 – 2:42:25]** values

**[2:42:25 – 2:42:26]** of

**[2:42:26 – 2:42:26]** G

**[2:42:26 – 2:42:27]** then

**[2:42:27 – 2:42:27]** we

**[2:42:27 – 2:42:27]** go

**[2:42:27 – 2:42:28]** slow

**[2:42:28 – 2:42:28]** but

**[2:42:28 – 2:42:28]** if

**[2:42:28 – 2:42:29]** G

**[2:42:29 – 2:42:29]** has

**[2:42:29 – 2:42:30]** been

**[2:42:30 – 2:42:30]** for

**[2:42:30 – 2:42:30]** a

**[2:42:30 – 2:42:31]** while

**[2:42:31 – 2:42:33]** pretty

**[2:42:33 – 2:42:33]** small

**[2:42:33 – 2:42:33]** then

**[2:42:33 – 2:42:34]** we

**[2:42:34 – 2:42:34]** can

**[2:42:34 – 2:42:34]** speed

**[2:42:34 – 2:42:34]** up

**[2:42:34 – 2:42:34]** again

**[2:42:34 – 2:42:35]** right

**[2:42:35 – 2:42:37]** how

**[2:42:37 – 2:42:38]** do

**[2:42:38 – 2:42:38]** you

**[2:42:38 – 2:42:38]** achieve

**[2:42:38 – 2:42:38]** that

**[2:42:38 – 2:42:39]** well

**[2:42:39 – 2:42:39]** you

**[2:42:39 – 2:42:39]** could

**[2:42:39 – 2:42:40]** do

**[2:42:40 – 2:42:40]** something

**[2:42:40 – 2:42:40]** like

**[2:42:40 – 2:42:40]** a

**[2:42:40 – 2:42:41]** sliding

**[2:42:41 – 2:42:41]** window

**[2:42:41 – 2:42:41]** but

**[2:42:41 – 2:42:42]** sliding

**[2:42:42 – 2:42:42]** windows

**[2:42:42 – 2:42:42]** are

**[2:42:42 – 2:42:42]** very

**[2:42:42 – 2:42:43]** expensive

**[2:42:43 – 2:42:44]** right

**[2:42:44 – 2:42:44]** to

**[2:42:44 – 2:42:44]** have

**[2:42:44 – 2:42:44]** a

**[2:42:44 – 2:42:44]** sliding

**[2:42:44 – 2:42:45]** window

**[2:42:45 – 2:42:45]** you

**[2:42:45 – 2:42:45]** need

**[2:42:45 – 2:42:45]** to

**[2:42:45 – 2:42:46]** keep

**[2:42:46 – 2:42:46]** in

**[2:42:46 – 2:42:46]** memory

**[2:42:46 – 2:42:46]** the

**[2:42:46 – 2:42:46]** whole

**[2:42:46 – 2:42:47]** window

**[2:42:47 – 2:42:47]** which

**[2:42:47 – 2:42:47]** is

**[2:42:47 – 2:42:48]** impractical

**[2:42:48 – 2:42:49]** so

**[2:42:49 – 2:42:50]** instead

**[2:42:50 – 2:42:50]** of

**[2:42:50 – 2:42:50]** a

**[2:42:50 – 2:42:50]** sliding

**[2:42:50 – 2:42:51]** window

**[2:42:51 – 2:42:51]** what

**[2:42:51 – 2:42:51]** we

**[2:42:51 – 2:42:52]** are

**[2:42:52 – 2:42:52]** going

**[2:42:52 – 2:42:52]** to

**[2:42:52 – 2:42:52]** do

**[2:42:52 – 2:42:52]** is

**[2:42:52 – 2:42:53]** we

**[2:42:53 – 2:42:53]** are

**[2:42:53 – 2:42:53]** going

**[2:42:53 – 2:42:53]** to

**[2:42:53 – 2:42:53]** do

**[2:42:53 – 2:42:55]** I

**[2:42:55 – 2:42:55]** hope

**[2:42:55 – 2:42:55]** you

**[2:42:55 – 2:42:56]** know

**[2:42:56 – 2:42:56]** this

**[2:42:56 – 2:42:56]** trick

**[2:42:56 – 2:42:56]** if

**[2:42:56 – 2:42:57]** not

**[2:42:57 – 2:42:57]** then

**[2:42:57 – 2:42:58]** it's

**[2:42:58 – 2:42:58]** very

**[2:42:58 – 2:42:58]** good

**[2:42:58 – 2:42:59]** that

**[2:42:59 – 2:42:59]** I

**[2:42:59 – 2:42:59]** am

**[2:42:59 – 2:42:59]** telling

**[2:42:59 – 2:42:59]** you

**[2:42:59 – 2:42:59]** about

**[2:42:59 – 2:43:00]** it

**[2:43:00 – 2:43:00]** because

**[2:43:00 – 2:43:01]** it's

**[2:43:01 – 2:43:01]** a

**[2:43:01 – 2:43:02]** crucial

**[2:43:02 – 2:43:02]** trick

**[2:43:02 – 2:43:02]** in

**[2:43:02 – 2:43:03]** all

**[2:43:03 – 2:43:03]** of

**[2:43:03 – 2:43:03]** applied

**[2:43:03 – 2:43:03]** math

**[2:43:03 – 2:43:03]** and

**[2:43:03 – 2:43:04]** computer

**[2:43:04 – 2:43:04]** science

**[2:43:04 – 2:43:05]** exponential

**[2:43:05 – 2:43:06]** moving

**[2:43:06 – 2:43:06]** average

**[2:43:06 – 2:43:08]** EMI

**[2:43:08 – 2:43:10]** the

**[2:43:10 – 2:43:11]** exponential

**[2:43:11 – 2:43:11]** moving

**[2:43:11 – 2:43:12]** average

**[2:43:12 – 2:43:14]** basically

**[2:43:14 – 2:43:15]** does

**[2:43:15 – 2:43:15]** this

**[2:43:15 – 2:43:16]** let me

**[2:43:16 – 2:43:17]** write it

**[2:43:17 – 2:43:17]** in this

**[2:43:17 – 2:43:17]** notation

**[2:43:17 – 2:43:18]** right

**[2:43:18 – 2:43:19]** away

**[2:43:19 – 2:43:19]** so

**[2:43:19 – 2:43:20]** GKI

**[2:43:20 – 2:43:21]** is

**[2:43:21 – 2:43:21]** not

**[2:43:21 – 2:43:21]** the

**[2:43:21 – 2:43:22]** sum

**[2:43:22 – 2:43:22]** of

**[2:43:22 – 2:43:22]** G

**[2:43:22 – 2:43:23]** squared

**[2:43:23 – 2:43:24]** but

**[2:43:24 – 2:43:24]** it's

**[2:43:24 – 2:43:25]** like

**[2:43:25 – 2:43:26]** some

**[2:43:26 – 2:43:26]** coefficient

**[2:43:26 – 2:43:27]** gamma

**[2:43:27 – 2:43:27]** times

**[2:43:27 – 2:43:28]** the

**[2:43:28 – 2:43:28]** previous

**[2:43:28 – 2:43:28]** one

**[2:43:28 – 2:43:29]** plus

**[2:43:29 – 2:43:30]** one

**[2:43:30 – 2:43:31]** minus

**[2:43:31 – 2:43:31]** gamma

**[2:43:31 – 2:43:32]** it's

**[2:43:32 – 2:43:32]** a

**[2:43:32 – 2:43:32]** convex

**[2:43:32 – 2:43:32]** combination

**[2:43:32 – 2:43:33]** of

**[2:43:33 – 2:43:33]** the

**[2:43:33 – 2:43:33]** previous

**[2:43:33 – 2:43:34]** value

**[2:43:34 – 2:43:34]** and

**[2:43:34 – 2:43:34]** the

**[2:43:34 – 2:43:35]** new

**[2:43:35 – 2:43:37]** value

**[2:43:37 – 2:43:39]** so

**[2:43:39 – 2:43:40]** what

**[2:43:40 – 2:43:40]** this

**[2:43:40 – 2:43:40]** actually

**[2:43:40 – 2:43:41]** means

**[2:43:41 – 2:43:41]** is

**[2:43:41 – 2:43:41]** if

**[2:43:41 – 2:43:42]** you

**[2:43:42 – 2:43:42]** just

**[2:43:42 – 2:43:43]** keep

**[2:43:43 – 2:43:44]** opening

**[2:43:44 – 2:43:45]** the

**[2:43:45 – 2:43:45]** brackets

**[2:43:45 – 2:43:46]** right

**[2:43:46 – 2:43:46]** it's

**[2:43:46 – 2:43:47]** like

**[2:43:47 – 2:43:47]** GKI

**[2:43:47 – 2:43:48]** comes

**[2:43:48 – 2:43:48]** with

**[2:43:48 – 2:43:49]** this

**[2:43:49 – 2:43:50]** coefficient

**[2:43:50 – 2:43:51]** and

**[2:43:51 – 2:43:51]** then

**[2:43:51 – 2:43:51]** it'll

**[2:43:51 – 2:43:52]** be

**[2:43:52 – 2:43:53]** gamma

**[2:43:53 – 2:43:53]** times

**[2:43:53 – 2:43:53]** one

**[2:43:53 – 2:43:54]** minus

**[2:43:54 – 2:43:54]** gamma

**[2:43:54 – 2:43:55]** times

**[2:43:55 – 2:43:55]** the

**[2:43:55 – 2:43:56]** next

**[2:43:56 – 2:43:56]** GK

**[2:43:56 – 2:43:57]** minus

**[2:43:57 – 2:43:57]** one

**[2:43:57 – 2:43:57]** I

**[2:43:57 – 2:43:58]** squared

**[2:43:58 – 2:43:59]** and

**[2:43:59 – 2:43:59]** then

**[2:43:59 – 2:43:59]** it'll

**[2:43:59 – 2:43:59]** be

**[2:43:59 – 2:44:00]** gamma

**[2:44:00 – 2:44:00]** squared

**[2:44:00 – 2:44:01]** times

**[2:44:01 – 2:44:01]** one

**[2:44:01 – 2:44:02]** minus

**[2:44:02 – 2:44:02]** gamma

**[2:44:02 – 2:44:03]** times

**[2:44:03 – 2:44:04]** GK

**[2:44:04 – 2:44:05]** minus

**[2:44:05 – 2:44:05]** two

**[2:44:05 – 2:44:05]** I

**[2:44:05 – 2:44:06]** squared

**[2:44:06 – 2:44:06]** and

**[2:44:06 – 2:44:07]** so

**[2:44:07 – 2:44:07]** on

**[2:44:07 – 2:44:07]** right

**[2:44:07 – 2:44:08]** so

**[2:44:08 – 2:44:08]** it's

**[2:44:08 – 2:44:08]** like

**[2:44:08 – 2:44:09]** as

**[2:44:09 – 2:44:09]** we

**[2:44:09 – 2:44:10]** go

**[2:44:10 – 2:44:11]** further

**[2:44:11 – 2:44:13]** every

**[2:44:13 – 2:44:13]** value

**[2:44:13 – 2:44:14]** that

**[2:44:14 – 2:44:14]** we

**[2:44:14 – 2:44:15]** want

**[2:44:15 – 2:44:15]** to

**[2:44:15 – 2:44:15]** add

**[2:44:15 – 2:44:16]** up

**[2:44:16 – 2:44:17]** comes

**[2:44:17 – 2:44:17]** with

**[2:44:17 – 2:44:18]** an

**[2:44:18 – 2:44:18]** exponentially

**[2:44:18 – 2:44:19]** decreasing

**[2:44:19 – 2:44:20]** coefficient

**[2:44:20 – 2:44:21]** gamma

**[2:44:21 – 2:44:22]** of course

**[2:44:22 – 2:44:22]** should be

**[2:44:22 – 2:44:23]** less

**[2:44:23 – 2:44:23]** than

**[2:44:23 – 2:44:23]** one

**[2:44:23 – 2:44:24]** otherwise

**[2:44:24 – 2:44:24]** nothing

**[2:44:24 – 2:44:24]** good

**[2:44:24 – 2:44:25]** will

**[2:44:25 – 2:44:25]** come

**[2:44:25 – 2:44:25]** up

**[2:44:25 – 2:44:28]** and

**[2:44:28 – 2:44:29]** this

**[2:44:29 – 2:44:29]** kind

**[2:44:29 – 2:44:29]** of

**[2:44:29 – 2:44:29]** averaging

**[2:44:29 – 2:44:31]** has the

**[2:44:31 – 2:44:32]** properties

**[2:44:32 – 2:44:32]** that we

**[2:44:32 – 2:44:32]** want

**[2:44:32 – 2:44:33]** right

**[2:44:33 – 2:44:33]** so

**[2:44:33 – 2:44:36]** recent

**[2:44:36 – 2:44:36]** history

**[2:44:36 – 2:44:37]** is

**[2:44:37 – 2:44:37]** weight

**[2:44:37 – 2:44:38]** high

**[2:44:38 – 2:44:39]** recent

**[2:44:39 – 2:44:39]** history

**[2:44:39 – 2:44:40]** has

**[2:44:40 – 2:44:41]** big

**[2:44:41 – 2:44:42]** weights

**[2:44:42 – 2:44:43]** and

**[2:44:43 – 2:44:44]** something

**[2:44:44 – 2:44:44]** that

**[2:44:44 – 2:44:44]** happened

**[2:44:44 – 2:44:45]** long

**[2:44:45 – 2:44:45]** ago

**[2:44:45 – 2:44:46]** faraway

**[2:44:46 – 2:44:47]** history

**[2:44:47 – 2:44:48]** has

**[2:44:48 – 2:44:48]** exponentially

**[2:44:48 – 2:44:49]** small

**[2:44:49 – 2:44:49]** weights

**[2:44:49 – 2:44:49]** so we

**[2:44:49 – 2:44:49]** kind of

**[2:44:49 – 2:44:50]** forget

**[2:44:50 – 2:44:50]** about

**[2:44:50 – 2:44:50]** it

**[2:44:50 – 2:44:50]** with

**[2:44:50 – 2:44:51]** time

**[2:44:51 – 2:44:52]** and

**[2:44:52 – 2:44:52]** unlike

**[2:44:52 – 2:44:53]** a

**[2:44:53 – 2:44:53]** moving

**[2:44:53 – 2:44:53]** window

**[2:44:53 – 2:44:54]** we only

**[2:44:54 – 2:44:55]** need to

**[2:44:55 – 2:44:55]** store

**[2:44:55 – 2:44:55]** this

**[2:44:55 – 2:44:56]** value

**[2:44:56 – 2:44:56]** that's

**[2:44:56 – 2:44:56]** it

**[2:44:56 – 2:44:57]** so only

**[2:44:57 – 2:44:57]** one

**[2:44:57 – 2:44:58]** value

**[2:44:58 – 2:44:58]** per

**[2:44:58 – 2:44:59]** weight

**[2:44:59 – 2:45:01]** not a

**[2:45:01 – 2:45:01]** whole

**[2:45:01 – 2:45:01]** window

**[2:45:01 – 2:45:01]** of

**[2:45:01 – 2:45:02]** radius

**[2:45:02 – 2:45:03]** so much

**[2:45:03 – 2:45:03]** more

**[2:45:03 – 2:45:03]** efficient

**[2:45:03 – 2:45:06]** and if

**[2:45:06 – 2:45:07]** you take

**[2:45:07 – 2:45:08]** k-degraat

**[2:45:08 – 2:45:09]** and you

**[2:45:09 – 2:45:09]** replace

**[2:45:09 – 2:45:11]** capital G

**[2:45:11 – 2:45:12]** with this

**[2:45:12 – 2:45:12]** formula

**[2:45:12 – 2:45:13]** what you

**[2:45:13 – 2:45:14]** get is

**[2:45:14 – 2:45:14]** an algorithm

**[2:45:14 – 2:45:15]** known as

**[2:45:15 – 2:45:16]** RMS

**[2:45:16 – 2:45:16]** prop

**[2:45:16 – 2:45:18]** and

**[2:45:18 – 2:45:20]** it's also

**[2:45:20 – 2:45:20]** one of

**[2:45:20 – 2:45:21]** standard

**[2:45:21 – 2:45:22]** approaches

**[2:45:22 – 2:45:22]** to

**[2:45:22 – 2:45:25]** well

**[2:45:25 – 2:45:26]** it's also

**[2:45:26 – 2:45:27]** one standard

**[2:45:27 – 2:45:27]** approach

**[2:45:27 – 2:45:28]** to

**[2:45:28 – 2:45:32]** to

**[2:45:32 – 2:45:32]** to

**[2:45:32 – 2:45:34]** do

**[2:45:34 – 2:45:34]** in

**[2:45:34 – 2:45:35]** stochastic

**[2:45:35 – 2:45:35]** gradient

**[2:45:35 – 2:45:36]** descent

**[2:45:36 – 2:45:36]** right

**[2:45:36 – 2:45:37]** it was

**[2:45:37 – 2:45:38]** popularized

**[2:45:38 – 2:45:38]** by

**[2:45:38 – 2:45:38]** by

**[2:45:38 – 2:45:39]** Jeffrey

**[2:45:39 – 2:45:39]** Hinton

**[2:45:39 – 2:45:39]** at some

**[2:45:39 – 2:45:40]** time

**[2:45:40 – 2:45:41]** but of

**[2:45:41 – 2:45:42]** course

**[2:45:42 – 2:45:42]** we don't

**[2:45:42 – 2:45:42]** stop there

**[2:45:42 – 2:45:43]** right

**[2:45:43 – 2:45:43]** so this

**[2:45:43 – 2:45:44]** this is

**[2:45:44 – 2:45:44]** also

**[2:45:44 – 2:45:45]** not the

**[2:45:45 – 2:45:45]** end

**[2:45:45 – 2:45:45]** of the

**[2:45:45 – 2:45:45]** story

**[2:45:45 – 2:45:47]** now

**[2:45:47 – 2:45:50]** I will

**[2:45:50 – 2:45:50]** go to

**[2:45:50 – 2:45:51]** ADEM

**[2:45:51 – 2:45:51]** almost

**[2:45:51 – 2:45:52]** straight

**[2:45:52 – 2:45:52]** away

**[2:45:52 – 2:45:53]** but

**[2:45:53 – 2:45:53]** before

**[2:45:53 – 2:45:54]** I go

**[2:45:54 – 2:45:54]** to

**[2:45:54 – 2:45:54]** ADEM

**[2:45:54 – 2:45:56]** let me

**[2:45:56 – 2:45:57]** explain

**[2:45:57 – 2:45:58]** to you

**[2:45:58 – 2:45:58]** one more

**[2:45:58 – 2:45:59]** like

**[2:45:59 – 2:45:59]** angle

**[2:45:59 – 2:46:00]** of looking

**[2:46:00 – 2:46:00]** at it

**[2:46:00 – 2:46:01]** I think

**[2:46:01 – 2:46:01]** it's

**[2:46:01 – 2:46:03]** a pretty

**[2:46:03 – 2:46:03]** fun

**[2:46:03 – 2:46:04]** and instructive

**[2:46:04 – 2:46:04]** angle

**[2:46:04 – 2:46:05]** although

**[2:46:05 – 2:46:05]** the algorithm

**[2:46:05 – 2:46:06]** that results

**[2:46:06 – 2:46:07]** from it

**[2:46:07 – 2:46:07]** wasn't

**[2:46:07 – 2:46:08]** very good

**[2:46:08 – 2:46:08]** and it's

**[2:46:08 – 2:46:09]** not really

**[2:46:09 – 2:46:09]** used

**[2:46:09 – 2:46:10]** but the

**[2:46:10 – 2:46:11]** basic idea

**[2:46:11 – 2:46:12]** the motivation

**[2:46:12 – 2:46:12]** behind it

**[2:46:12 – 2:46:13]** I think

**[2:46:13 – 2:46:13]** is really

**[2:46:13 – 2:46:13]** nice

**[2:46:13 – 2:46:15]** so

**[2:46:15 – 2:46:18]** the motivation

**[2:46:18 – 2:46:19]** behind

**[2:46:19 – 2:46:22]** so the

**[2:46:22 – 2:46:22]** motivation

**[2:46:22 – 2:46:23]** goes as

**[2:46:23 – 2:46:23]** follows

**[2:46:23 – 2:46:26]** we already

**[2:46:26 – 2:46:27]** discussed

**[2:46:27 – 2:46:28]** gradient

**[2:46:28 – 2:46:29]** descent

**[2:46:29 – 2:46:30]** as kind

**[2:46:30 – 2:46:31]** of

**[2:46:31 – 2:46:32]** points

**[2:46:32 – 2:46:33]** rolling down

**[2:46:33 – 2:46:33]** surfaces

**[2:46:33 – 2:46:34]** blah blah blah

**[2:46:34 – 2:46:35]** etc etc

**[2:46:35 – 2:46:36]** so

**[2:46:36 – 2:46:37]** why don't

**[2:46:37 – 2:46:39]** we keep

**[2:46:39 – 2:46:39]** looking at

**[2:46:39 – 2:46:39]** it from

**[2:46:39 – 2:46:40]** this

**[2:46:40 – 2:46:41]** physics

**[2:46:41 – 2:46:41]** perspective

**[2:46:41 – 2:46:42]** why don't

**[2:46:42 – 2:46:43]** we

**[2:46:43 – 2:46:44]** actually

**[2:46:44 – 2:46:47]** keep

**[2:46:47 – 2:46:48]** realizing

**[2:46:48 – 2:46:49]** what

**[2:46:49 – 2:46:51]** keep

**[2:46:51 – 2:46:52]** pursuing

**[2:46:52 – 2:46:53]** this

**[2:46:53 – 2:46:54]** physical

**[2:46:54 – 2:46:54]** connection

**[2:46:54 – 2:46:55]** this metaphor

**[2:46:55 – 2:46:56]** of points

**[2:46:56 – 2:46:57]** rolling downhill

**[2:46:57 – 2:46:57]** because

**[2:46:57 – 2:46:59]** it's a very

**[2:46:59 – 2:47:00]** direct correspondence

**[2:47:00 – 2:47:01]** right

**[2:47:01 – 2:47:01]** it's

**[2:47:01 – 2:47:01]** the only

**[2:47:01 – 2:47:02]** difference is

**[2:47:02 – 2:47:03]** that both

**[2:47:03 – 2:47:04]** roll

**[2:47:04 – 2:47:05]** in continuous

**[2:47:05 – 2:47:05]** time

**[2:47:05 – 2:47:06]** and here

**[2:47:06 – 2:47:06]** we are in

**[2:47:06 – 2:47:07]** discrete time

**[2:47:07 – 2:47:07]** otherwise

**[2:47:07 – 2:47:07]** it's the

**[2:47:07 – 2:47:08]** exact same

**[2:47:08 – 2:47:08]** process

**[2:47:08 – 2:47:10]** so

**[2:47:10 – 2:47:12]** why don't

**[2:47:12 – 2:47:12]** we

**[2:47:12 – 2:47:13]** look at

**[2:47:13 – 2:47:14]** the

**[2:47:14 – 2:47:15]** measurement

**[2:47:15 – 2:47:16]** units

**[2:47:16 – 2:47:17]** of what

**[2:47:17 – 2:47:18]** is going

**[2:47:18 – 2:47:18]** on

**[2:47:18 – 2:47:20]** and

**[2:47:20 – 2:47:20]** what are

**[2:47:20 – 2:47:21]** the measurement

**[2:47:21 – 2:47:22]** units here

**[2:47:22 – 2:47:23]** well

**[2:47:23 – 2:47:24]** let's start

**[2:47:24 – 2:47:24]** with the

**[2:47:24 – 2:47:25]** gradient

**[2:47:25 – 2:47:25]** because

**[2:47:25 – 2:47:26]** that's

**[2:47:26 – 2:47:27]** it's easier

**[2:47:27 – 2:47:28]** it's much

**[2:47:28 – 2:47:29]** more natural

**[2:47:29 – 2:47:29]** to start

**[2:47:29 – 2:47:29]** there

**[2:47:29 – 2:47:30]** so

**[2:47:30 – 2:47:32]** I want

**[2:47:32 – 2:47:33]** my gradient

**[2:47:33 – 2:47:34]** to be

**[2:47:34 – 2:47:34]** like the

**[2:47:34 – 2:47:35]** velocity

**[2:47:35 – 2:47:35]** right

**[2:47:35 – 2:47:37]** my intuition

**[2:47:37 – 2:47:37]** is that

**[2:47:37 – 2:47:38]** derivatives

**[2:47:38 – 2:47:39]** are

**[2:47:39 – 2:47:40]** velocities

**[2:47:40 – 2:47:40]** they are

**[2:47:40 – 2:47:40]** speeds

**[2:47:40 – 2:47:42]** so

**[2:47:42 – 2:47:43]** let's say

**[2:47:43 – 2:47:43]** that I want

**[2:47:43 – 2:47:44]** my g

**[2:47:44 – 2:47:45]** to be

**[2:47:45 – 2:47:45]** measured

**[2:47:45 – 2:47:46]** in meters

**[2:47:46 – 2:47:46]** per second

**[2:47:46 – 2:47:47]** okay

**[2:47:47 – 2:47:49]** so g

**[2:47:49 – 2:47:49]** is like

**[2:47:49 – 2:47:50]** df

**[2:47:50 – 2:47:51]** over dx

**[2:47:51 – 2:47:53]** so this

**[2:47:53 – 2:47:53]** means that

**[2:47:53 – 2:47:54]** x

**[2:47:54 – 2:47:55]** is measured

**[2:47:55 – 2:47:56]** in seconds

**[2:47:56 – 2:47:58]** and f

**[2:47:58 – 2:47:58]** of x

**[2:47:58 – 2:47:59]** is measured

**[2:47:59 – 2:48:00]** in meters

**[2:48:00 – 2:48:01]** so the

**[2:48:01 – 2:48:02]** function is

**[2:48:02 – 2:48:03]** how far

**[2:48:03 – 2:48:04]** the point

**[2:48:04 – 2:48:05]** has gone

**[2:48:05 – 2:48:07]** x is the

**[2:48:07 – 2:48:07]** time that

**[2:48:07 – 2:48:08]** has elapsed

**[2:48:08 – 2:48:09]** and g

**[2:48:09 – 2:48:10]** is the

**[2:48:10 – 2:48:10]** velocity of

**[2:48:10 – 2:48:11]** the point

**[2:48:11 – 2:48:13]** okay

**[2:48:13 – 2:48:15]** so now

**[2:48:15 – 2:48:15]** that we

**[2:48:15 – 2:48:16]** understand this

**[2:48:16 – 2:48:17]** let's look at

**[2:48:17 – 2:48:18]** gradient descent

**[2:48:18 – 2:48:19]** and see whether

**[2:48:19 – 2:48:20]** it actually works

**[2:48:20 – 2:48:22]** so my gradient

**[2:48:22 – 2:48:22]** descent says

**[2:48:22 – 2:48:23]** okay I take

**[2:48:23 – 2:48:24]** my x

**[2:48:24 – 2:48:25]** and I update

**[2:48:25 – 2:48:26]** it like this

**[2:48:26 – 2:48:28]** x is x

**[2:48:28 – 2:48:29]** minus some

**[2:48:29 – 2:48:30]** constant times

**[2:48:30 – 2:48:30]** g

**[2:48:30 – 2:48:32]** what about

**[2:48:32 – 2:48:32]** the measurement

**[2:48:32 – 2:48:33]** units

**[2:48:33 – 2:48:34]** well x

**[2:48:34 – 2:48:34]** is measured

**[2:48:34 – 2:48:35]** in seconds

**[2:48:35 – 2:48:36]** x is measured

**[2:48:36 – 2:48:37]** in seconds

**[2:48:37 – 2:48:38]** this is just

**[2:48:38 – 2:48:39]** a constant

**[2:48:39 – 2:48:40]** dimensionless

**[2:48:40 – 2:48:41]** unit

**[2:48:41 – 2:48:42]** and g

**[2:48:42 – 2:48:42]** is meters

**[2:48:42 – 2:48:43]** per second

**[2:48:43 – 2:48:46]** so we

**[2:48:46 – 2:48:48]** are subtracting

**[2:48:48 – 2:48:48]** velocity

**[2:48:48 – 2:48:50]** from time

**[2:48:50 – 2:48:51]** which doesn't

**[2:48:51 – 2:48:52]** make any

**[2:48:52 – 2:48:52]** physical sense

**[2:48:52 – 2:48:53]** right

**[2:48:53 – 2:48:55]** and when I say

**[2:48:55 – 2:48:56]** it doesn't make

**[2:48:56 – 2:48:57]** any physical sense

**[2:48:57 – 2:48:58]** mathematically

**[2:48:58 – 2:48:59]** what it means

**[2:48:59 – 2:48:59]** so what it means

**[2:48:59 – 2:49:00]** for us in practice

**[2:49:00 – 2:49:02]** it exactly means

**[2:49:02 – 2:49:04]** that the scales

**[2:49:04 – 2:49:04]** of these variables

**[2:49:04 – 2:49:05]** can be very different

**[2:49:05 – 2:49:07]** so

**[2:49:07 – 2:49:09]** it can happen

**[2:49:09 – 2:49:09]** that

**[2:49:09 – 2:49:10]** your axes

**[2:49:10 – 2:49:12]** are large

**[2:49:12 – 2:49:15]** in absolute values

**[2:49:15 – 2:49:16]** and g

**[2:49:16 – 2:49:18]** is relatively small

**[2:49:18 – 2:49:19]** and in this case

**[2:49:19 – 2:49:20]** you would need

**[2:49:20 – 2:49:21]** like a huge alpha

**[2:49:21 – 2:49:21]** to

**[2:49:21 – 2:49:24]** adjust for that

**[2:49:24 – 2:49:25]** or it could be

**[2:49:25 – 2:49:26]** the other way around

**[2:49:26 – 2:49:26]** so

**[2:49:26 – 2:49:27]** the g

**[2:49:27 – 2:49:28]** is not scaled

**[2:49:28 – 2:49:30]** well to x

**[2:49:30 – 2:49:32]** it's our job

**[2:49:32 – 2:49:33]** to scale it

**[2:49:33 – 2:49:33]** basically

**[2:49:33 – 2:49:36]** and

**[2:49:36 – 2:49:37]** physically it means

**[2:49:37 – 2:49:38]** that the dimensions

**[2:49:38 – 2:49:39]** are wrong

**[2:49:39 – 2:49:41]** the units of measurement

**[2:49:41 – 2:49:41]** do not match

**[2:49:41 – 2:49:43]** okay

**[2:49:43 – 2:49:44]** so

**[2:49:44 – 2:49:45]** okay

**[2:49:45 – 2:49:47]** in the method of moments

**[2:49:47 – 2:49:47]** it's the same

**[2:49:47 – 2:49:49]** what happens in

**[2:49:49 – 2:49:49]** say

**[2:49:49 – 2:49:50]** Eidegrad

**[2:49:50 – 2:49:52]** in Eidegrad

**[2:49:52 – 2:49:53]** we have

**[2:49:53 – 2:49:54]** minus alpha

**[2:49:54 – 2:49:55]** divided by

**[2:49:55 – 2:49:56]** capital G

**[2:49:56 – 2:49:57]** times G

**[2:49:57 – 2:49:58]** something like this

**[2:49:58 – 2:50:00]** so what are the units

**[2:50:00 – 2:50:01]** over here

**[2:50:01 – 2:50:03]** seconds

**[2:50:03 – 2:50:04]** seconds

**[2:50:04 – 2:50:06]** meters per second

**[2:50:06 – 2:50:06]** and G

**[2:50:06 – 2:50:07]** capital G

**[2:50:07 – 2:50:08]** is small g squared

**[2:50:08 – 2:50:10]** so it's 1 over

**[2:50:10 – 2:50:12]** meters

**[2:50:12 – 2:50:13]** squared

**[2:50:13 – 2:50:13]** per second

**[2:50:13 – 2:50:14]** squared

**[2:50:14 – 2:50:16]** and squared

**[2:50:16 – 2:50:18]** so basically

**[2:50:18 – 2:50:21]** the units

**[2:50:21 – 2:50:22]** cancel out

**[2:50:22 – 2:50:23]** and we get that

**[2:50:23 – 2:50:24]** all of this

**[2:50:24 – 2:50:26]** is a dimensionless thing

**[2:50:26 – 2:50:27]** so now we

**[2:50:27 – 2:50:29]** subtract

**[2:50:29 – 2:50:30]** from seconds

**[2:50:30 – 2:50:31]** from time

**[2:50:31 – 2:50:32]** some dimensionless

**[2:50:32 – 2:50:32]** constant

**[2:50:32 – 2:50:34]** which also doesn't

**[2:50:34 – 2:50:35]** sound right

**[2:50:35 – 2:50:35]** okay

**[2:50:35 – 2:50:39]** and notice

**[2:50:39 – 2:50:41]** that

**[2:50:41 – 2:50:44]** Newton's method

**[2:50:44 – 2:50:45]** second order

**[2:50:45 – 2:50:45]** optimization

**[2:50:45 – 2:50:46]** does not have

**[2:50:46 – 2:50:47]** this problem

**[2:50:47 – 2:50:48]** this is also

**[2:50:48 – 2:50:49]** an important point

**[2:50:49 – 2:50:49]** here

**[2:50:49 – 2:50:50]** so if

**[2:50:50 – 2:50:52]** you recall

**[2:50:52 – 2:50:52]** that formula

**[2:50:52 – 2:50:53]** that we had

**[2:50:53 – 2:50:54]** about second order

**[2:50:54 – 2:50:55]** method

**[2:50:55 – 2:50:56]** something like

**[2:50:56 – 2:50:57]** x minus

**[2:50:57 – 2:50:59]** h inverse

**[2:50:59 – 2:50:59]** times g

**[2:50:59 – 2:51:00]** right

**[2:51:00 – 2:51:02]** so now

**[2:51:02 – 2:51:03]** let's look at

**[2:51:03 – 2:51:04]** the units here

**[2:51:04 – 2:51:05]** now x

**[2:51:05 – 2:51:06]** is in seconds

**[2:51:06 – 2:51:07]** x is in seconds

**[2:51:07 – 2:51:09]** g is in meters

**[2:51:09 – 2:51:09]** per second

**[2:51:09 – 2:51:10]** what is h?

**[2:51:10 – 2:51:11]** h is the matrix

**[2:51:11 – 2:51:12]** of second derivatives

**[2:51:12 – 2:51:14]** it's accelerations

**[2:51:14 – 2:51:17]** so it's

**[2:51:17 – 2:51:18]** meters per second

**[2:51:18 – 2:51:19]** squared

**[2:51:19 – 2:51:20]** inverse

**[2:51:20 – 2:51:23]** well there you go

**[2:51:23 – 2:51:24]** it cancels out

**[2:51:24 – 2:51:25]** and only seconds

**[2:51:25 – 2:51:25]** remain

**[2:51:25 – 2:51:27]** so now the units

**[2:51:27 – 2:51:28]** actually match

**[2:51:28 – 2:51:29]** and mathematically

**[2:51:29 – 2:51:30]** it means that

**[2:51:30 – 2:51:31]** Newton's method

**[2:51:31 – 2:51:32]** actually

**[2:51:32 – 2:51:34]** scales

**[2:51:34 – 2:51:34]** correctly

**[2:51:34 – 2:51:36]** it gives you

**[2:51:36 – 2:51:36]** the

**[2:51:36 – 2:51:38]** local

**[2:51:38 – 2:51:40]** step size

**[2:51:40 – 2:51:41]** that you actually

**[2:51:41 – 2:51:41]** want

**[2:51:41 – 2:51:42]** so this

**[2:51:42 – 2:51:43]** is

**[2:51:43 – 2:51:44]** well I mean

**[2:51:44 – 2:51:44]** it's not a reason

**[2:51:44 – 2:51:45]** it's just an illustration

**[2:51:45 – 2:51:46]** but this is one

**[2:51:46 – 2:51:47]** good illustration

**[2:51:47 – 2:51:48]** for

**[2:51:48 – 2:51:50]** why

**[2:51:50 – 2:51:51]** Newton

**[2:51:51 – 2:51:52]** while second order

**[2:51:52 – 2:51:53]** techniques are

**[2:51:53 – 2:51:53]** better

**[2:51:53 – 2:51:54]** right

**[2:51:54 – 2:51:55]** so their dimensions

**[2:51:55 – 2:51:56]** match

**[2:51:56 – 2:51:57]** they scale

**[2:51:57 – 2:51:57]** automatically

**[2:51:57 – 2:52:00]** and out of this

**[2:52:00 – 2:52:02]** out of this

**[2:52:02 – 2:52:03]** idea

**[2:52:03 – 2:52:03]** there came

**[2:52:03 – 2:52:04]** a method

**[2:52:04 – 2:52:04]** called

**[2:52:04 – 2:52:05]** A to delta

**[2:52:05 – 2:52:08]** which tried

**[2:52:08 – 2:52:09]** to do

**[2:52:09 – 2:52:09]** the proper

**[2:52:09 – 2:52:10]** units

**[2:52:10 – 2:52:10]** and basically

**[2:52:10 – 2:52:11]** it was

**[2:52:11 – 2:52:11]** A to grad

**[2:52:11 – 2:52:13]** but alpha

**[2:52:13 – 2:52:14]** here

**[2:52:14 – 2:52:15]** was multiplied

**[2:52:15 – 2:52:16]** by something

**[2:52:16 – 2:52:17]** like the square

**[2:52:17 – 2:52:18]** root of u

**[2:52:18 – 2:52:19]** and

**[2:52:19 – 2:52:20]** u

**[2:52:20 – 2:52:20]** was

**[2:52:20 – 2:52:21]** something

**[2:52:21 – 2:52:22]** like

**[2:52:22 – 2:52:23]** the sum

**[2:52:23 – 2:52:24]** of updates

**[2:52:24 – 2:52:24]** squared

**[2:52:24 – 2:52:25]** something like

**[2:52:25 – 2:52:25]** that

**[2:52:25 – 2:52:26]** it wasn't

**[2:52:26 – 2:52:26]** a very good

**[2:52:26 – 2:52:27]** algorithm

**[2:52:27 – 2:52:28]** it didn't

**[2:52:28 – 2:52:28]** catch up

**[2:52:28 – 2:52:29]** catch on

**[2:52:29 – 2:52:30]** so

**[2:52:30 – 2:52:30]** you don't

**[2:52:30 – 2:52:31]** have to

**[2:52:31 – 2:52:31]** study

**[2:52:31 – 2:52:32]** the delta

**[2:52:32 – 2:52:33]** but

**[2:52:33 – 2:52:34]** I think

**[2:52:34 – 2:52:35]** the basic

**[2:52:35 – 2:52:35]** idea

**[2:52:35 – 2:52:35]** is very

**[2:52:35 – 2:52:36]** interesting

**[2:52:36 – 2:52:37]** the basic

**[2:52:37 – 2:52:37]** idea

**[2:52:37 – 2:52:37]** of

**[2:52:37 – 2:52:39]** having

**[2:52:39 – 2:52:44]** of

**[2:52:44 – 2:52:45]** having

**[2:52:45 – 2:52:46]** the

**[2:52:46 – 2:52:47]** unit

**[2:52:47 – 2:52:47]** the

**[2:52:47 – 2:52:47]** measurement

**[2:52:47 – 2:52:48]** units

**[2:52:48 – 2:52:49]** of different

**[2:52:49 – 2:52:49]** things

**[2:52:49 – 2:52:49]** match

**[2:52:49 – 2:52:51]** and with

**[2:52:51 – 2:52:52]** that

**[2:52:52 – 2:52:52]** let's

**[2:52:52 – 2:52:53]** go to

**[2:52:53 – 2:52:54]** the real

**[2:52:54 – 2:52:54]** thing

**[2:52:54 – 2:52:55]** the

**[2:52:55 – 2:52:56]** algorithm

**[2:52:56 – 2:52:56]** that

**[2:52:56 – 2:52:58]** people still

**[2:52:58 – 2:52:58]** use

**[2:52:58 – 2:52:59]** quite often

**[2:52:59 – 2:53:00]** although

**[2:53:00 – 2:53:01]** there are

**[2:53:01 – 2:53:02]** alternatives

**[2:53:02 – 2:53:02]** now

**[2:53:02 – 2:53:02]** I'll mention

**[2:53:02 – 2:53:03]** them

**[2:53:03 – 2:53:03]** we won't

**[2:53:03 – 2:53:03]** go into

**[2:53:03 – 2:53:04]** the details

**[2:53:04 – 2:53:04]** of them

**[2:53:04 – 2:53:05]** but I

**[2:53:05 – 2:53:05]** will mention

**[2:53:05 – 2:53:06]** them

**[2:53:06 – 2:53:07]** but the

**[2:53:07 – 2:53:08]** most popular

**[2:53:08 – 2:53:09]** optimization

**[2:53:09 – 2:53:09]** algorithm

**[2:53:09 – 2:53:10]** in deep

**[2:53:10 – 2:53:11]** learning

**[2:53:11 – 2:53:11]** is

**[2:53:11 – 2:53:11]** ADEM

**[2:53:11 – 2:53:14]** and

**[2:53:14 – 2:53:15]** ADEM

**[2:53:15 – 2:53:15]** is actually

**[2:53:15 – 2:53:16]** pretty

**[2:53:16 – 2:53:16]** similar

**[2:53:16 – 2:53:16]** to what

**[2:53:16 – 2:53:17]** we discussed

**[2:53:17 – 2:53:18]** with

**[2:53:18 – 2:53:18]** slight

**[2:53:18 – 2:53:19]** modifications

**[2:53:19 – 2:53:20]** so it's

**[2:53:20 – 2:53:20]** like

**[2:53:20 – 2:53:21]** xk

**[2:53:21 – 2:53:21]** plus

**[2:53:21 – 2:53:22]** 1i

**[2:53:22 – 2:53:23]** is

**[2:53:23 – 2:53:24]** xki

**[2:53:24 – 2:53:26]** minus

**[2:53:26 – 2:53:27]** alpha

**[2:53:27 – 2:53:28]** divided by

**[2:53:28 – 2:53:28]** g

**[2:53:28 – 2:53:29]** k

**[2:53:29 – 2:53:30]** i

**[2:53:30 – 2:53:30]** plus

**[2:53:30 – 2:53:31]** epsilon

**[2:53:31 – 2:53:32]** so far

**[2:53:32 – 2:53:32]** it's

**[2:53:32 – 2:53:33]** more or less

**[2:53:33 – 2:53:33]** the same

**[2:53:33 – 2:53:35]** but times

**[2:53:35 – 2:53:36]** m

**[2:53:36 – 2:53:37]** k

**[2:53:37 – 2:53:37]** i

**[2:53:37 – 2:53:38]** not just

**[2:53:38 – 2:53:38]** g

**[2:53:38 – 2:53:40]** and let me

**[2:53:40 – 2:53:41]** explain what this

**[2:53:41 – 2:53:41]** means

**[2:53:41 – 2:53:41]** so

**[2:53:41 – 2:53:42]** g

**[2:53:42 – 2:53:43]** k

**[2:53:43 – 2:53:44]** i

**[2:53:44 – 2:53:45]** is

**[2:53:45 – 2:53:46]** an exponential

**[2:53:46 – 2:53:46]** moving

**[2:53:46 – 2:53:47]** average

**[2:53:47 – 2:53:48]** of

**[2:53:48 – 2:53:50]** squared

**[2:53:50 – 2:53:51]** gradients

**[2:53:51 – 2:53:52]** beta

**[2:53:52 – 2:53:53]** 2

**[2:53:53 – 2:53:54]** times

**[2:53:54 – 2:53:54]** g

**[2:53:54 – 2:53:55]** k

**[2:53:55 – 2:53:55]** minus

**[2:53:55 – 2:53:56]** 1i

**[2:53:56 – 2:53:57]** plus

**[2:53:57 – 2:53:59]** 1

**[2:53:59 – 2:53:59]** minus

**[2:53:59 – 2:54:00]** beta

**[2:54:00 – 2:54:00]** 2

**[2:54:00 – 2:54:01]** times

**[2:54:01 – 2:54:01]** g

**[2:54:01 – 2:54:01]** i

**[2:54:01 – 2:54:02]** squared

**[2:54:02 – 2:54:04]** and

**[2:54:04 – 2:54:04]** m

**[2:54:04 – 2:54:06]** is

**[2:54:06 – 2:54:06]** an

**[2:54:06 – 2:54:07]** exponential

**[2:54:07 – 2:54:07]** moving

**[2:54:07 – 2:54:08]** average

**[2:54:08 – 2:54:08]** of

**[2:54:08 – 2:54:08]** the

**[2:54:08 – 2:54:08]** gradients

**[2:54:08 – 2:54:09]** themselves

**[2:54:09 – 2:54:10]** beta

**[2:54:10 – 2:54:11]** 1

**[2:54:11 – 2:54:11]** times

**[2:54:11 – 2:54:12]** m

**[2:54:12 – 2:54:12]** k

**[2:54:12 – 2:54:13]** minus

**[2:54:13 – 2:54:14]** 1i

**[2:54:14 – 2:54:14]** plus

**[2:54:14 – 2:54:16]** 1

**[2:54:16 – 2:54:16]** minus

**[2:54:16 – 2:54:17]** beta

**[2:54:17 – 2:54:17]** 1

**[2:54:17 – 2:54:18]** times

**[2:54:18 – 2:54:18]** g

**[2:54:18 – 2:54:18]** k

**[2:54:18 – 2:54:19]** i

**[2:54:19 – 2:54:19]** itself

**[2:54:19 – 2:54:23]** and

**[2:54:23 – 2:54:24]** that's

**[2:54:24 – 2:54:24]** it

**[2:54:24 – 2:54:24]** so

**[2:54:24 – 2:54:25]** basically

**[2:54:25 – 2:54:26]** it's

**[2:54:26 – 2:54:26]** rms

**[2:54:26 – 2:54:27]** prop

**[2:54:27 – 2:54:28]** and

**[2:54:28 – 2:54:29]** the only

**[2:54:29 – 2:54:29]** difference

**[2:54:29 – 2:54:30]** from rms

**[2:54:30 – 2:54:30]** prop

**[2:54:30 – 2:54:31]** is

**[2:54:31 – 2:54:31]** that

**[2:54:31 – 2:54:33]** we

**[2:54:33 – 2:54:33]** also

**[2:54:33 – 2:54:34]** smooth

**[2:54:34 – 2:54:34]** out

**[2:54:34 – 2:54:34]** the

**[2:54:34 – 2:54:35]** gradients

**[2:54:35 – 2:54:36]** themselves

**[2:54:36 – 2:54:37]** so

**[2:54:37 – 2:54:38]** we

**[2:54:38 – 2:54:39]** are

**[2:54:39 – 2:54:40]** instead of

**[2:54:40 – 2:54:40]** using the

**[2:54:40 – 2:54:41]** actual

**[2:54:41 – 2:54:42]** instantaneous

**[2:54:42 – 2:54:43]** value of

**[2:54:43 – 2:54:43]** the

**[2:54:43 – 2:54:43]** stochastic

**[2:54:43 – 2:54:44]** gradient

**[2:54:44 – 2:54:45]** we are

**[2:54:45 – 2:54:45]** doing like

**[2:54:45 – 2:54:46]** this moving

**[2:54:46 – 2:54:47]** average over

**[2:54:47 – 2:54:47]** recent history

**[2:54:47 – 2:54:49]** so we

**[2:54:49 – 2:54:49]** are smoothing

**[2:54:49 – 2:54:50]** the gradients

**[2:54:50 – 2:54:51]** we are

**[2:54:51 – 2:54:52]** making them

**[2:54:52 – 2:54:52]** less

**[2:54:52 – 2:54:54]** we are

**[2:54:54 – 2:54:54]** reducing their

**[2:54:54 – 2:54:55]** variance

**[2:54:55 – 2:54:56]** we are

**[2:54:56 – 2:54:56]** making them

**[2:54:56 – 2:54:57]** less

**[2:54:57 – 2:54:58]** janky

**[2:54:58 – 2:54:58]** as we

**[2:54:58 – 2:54:58]** sampled

**[2:54:58 – 2:54:59]** different

**[2:54:59 – 2:54:59]** mini

**[2:54:59 – 2:55:00]** batches

**[2:55:00 – 2:55:01]** and this

**[2:55:01 – 2:55:01]** smoothing

**[2:55:01 – 2:55:02]** has an

**[2:55:02 – 2:55:03]** excellent

**[2:55:03 – 2:55:03]** effect

**[2:55:03 – 2:55:05]** it's

**[2:55:05 – 2:55:06]** what makes

**[2:55:06 – 2:55:06]** ADEM

**[2:55:06 – 2:55:07]** work so

**[2:55:07 – 2:55:07]** well

**[2:55:07 – 2:55:09]** so

**[2:55:09 – 2:55:14]** what else

**[2:55:14 – 2:55:14]** do I want

**[2:55:14 – 2:55:14]** to say

**[2:55:14 – 2:55:15]** about

**[2:55:15 – 2:55:15]** ADEM

**[2:55:15 – 2:55:16]** well

**[2:55:16 – 2:55:16]** yeah

**[2:55:16 – 2:55:17]** another thing

**[2:55:17 – 2:55:18]** about

**[2:55:18 – 2:55:18]** ADEM

**[2:55:18 – 2:55:19]** is that

**[2:55:19 – 2:55:20]** you really

**[2:55:20 – 2:55:21]** don't

**[2:55:21 – 2:55:21]** have to

**[2:55:21 – 2:55:22]** I mean

**[2:55:22 – 2:55:22]** it looks

**[2:55:22 – 2:55:23]** like it

**[2:55:23 – 2:55:23]** has a

**[2:55:23 – 2:55:23]** lot of

**[2:55:23 – 2:55:24]** hyperparameters

**[2:55:24 – 2:55:25]** you got

**[2:55:25 – 2:55:26]** beta 1

**[2:55:26 – 2:55:27]** and beta 2

**[2:55:27 – 2:55:28]** and also

**[2:55:28 – 2:55:28]** epsilon

**[2:55:28 – 2:55:29]** it looks

**[2:55:29 – 2:55:29]** like you

**[2:55:29 – 2:55:29]** need to

**[2:55:29 – 2:55:30]** choose them

**[2:55:30 – 2:55:30]** carefully

**[2:55:30 – 2:55:31]** etc

**[2:55:31 – 2:55:31]** etc

**[2:55:31 – 2:55:31]** which

**[2:55:31 – 2:55:31]** would

**[2:55:31 – 2:55:31]** be

**[2:55:31 – 2:55:32]** difficult

**[2:55:32 – 2:55:33]** but

**[2:55:33 – 2:55:33]** actually

**[2:55:33 – 2:55:34]** it's

**[2:55:34 – 2:55:34]** very

**[2:55:34 – 2:55:34]** robust

**[2:55:34 – 2:55:35]** you can

**[2:55:35 – 2:55:35]** just

**[2:55:35 – 2:55:36]** keep

**[2:55:36 – 2:55:36]** the

**[2:55:36 – 2:55:37]** standard

**[2:55:37 – 2:55:38]** hyperparameters

**[2:55:38 – 2:55:38]** that

**[2:55:38 – 2:55:39]** they

**[2:55:39 – 2:55:40]** recommended

**[2:55:40 – 2:55:40]** in the

**[2:55:40 – 2:55:40]** original

**[2:55:40 – 2:55:41]** paper

**[2:55:41 – 2:55:42]** I think

**[2:55:42 – 2:55:42]** it's

**[2:55:42 – 2:55:42]** something

**[2:55:42 – 2:55:43]** like

**[2:55:43 – 2:55:43]** this

**[2:55:43 – 2:55:44]** maybe

**[2:55:44 – 2:55:45]** 0.995

**[2:55:45 – 2:55:46]** I'm not

**[2:55:46 – 2:55:46]** sure

**[2:55:46 – 2:55:46]** but

**[2:55:46 – 2:55:46]** something

**[2:55:46 – 2:55:47]** like

**[2:55:47 – 2:55:47]** that

**[2:55:47 – 2:55:48]** and

**[2:55:48 – 2:55:49]** epsilon

**[2:55:49 – 2:55:49]** is

**[2:55:49 – 2:55:49]** just

**[2:55:49 – 2:55:49]** a

**[2:55:49 – 2:55:50]** very

**[2:55:50 – 2:55:50]** small

**[2:55:50 – 2:55:50]** constant

**[2:55:50 – 2:55:51]** like

**[2:55:51 – 2:55:51]** this

**[2:55:51 – 2:55:52]** minus

**[2:55:52 – 2:55:52]** 8

**[2:55:52 – 2:55:53]** or

**[2:55:53 – 2:55:53]** something

**[2:55:53 – 2:55:53]** like

**[2:55:53 – 2:55:54]** that

**[2:55:54 – 2:55:55]** and

**[2:55:55 – 2:55:56]** basically

**[2:55:56 – 2:55:57]** it works

**[2:55:57 – 2:55:57]** so you

**[2:55:57 – 2:55:58]** don't need

**[2:55:58 – 2:55:59]** to tweak

**[2:55:59 – 2:56:00]** beta 1

**[2:56:00 – 2:56:00]** beta 2

**[2:56:00 – 2:56:01]** and epsilon

**[2:56:01 – 2:56:02]** you can

**[2:56:02 – 2:56:03]** just take

**[2:56:03 – 2:56:03]** them off

**[2:56:03 – 2:56:03]** the shelf

**[2:56:03 – 2:56:04]** and it

**[2:56:04 – 2:56:04]** will be

**[2:56:04 – 2:56:04]** fine

**[2:56:04 – 2:56:07]** and

**[2:56:07 – 2:56:07]** ADM

**[2:56:07 – 2:56:09]** is

**[2:56:09 – 2:56:09]** a really

**[2:56:09 – 2:56:10]** good algorithm

**[2:56:10 – 2:56:10]** it's still

**[2:56:10 – 2:56:11]** used

**[2:56:11 – 2:56:12]** it's still

**[2:56:12 – 2:56:12]** pretty good

**[2:56:12 – 2:56:13]** I don't

**[2:56:13 – 2:56:13]** think I

**[2:56:13 – 2:56:14]** can actually

**[2:56:14 – 2:56:15]** illustrate it

**[2:56:15 – 2:56:15]** to you

**[2:56:15 – 2:56:15]** here on

**[2:56:15 – 2:56:16]** pictures

**[2:56:16 – 2:56:17]** because

**[2:56:17 – 2:56:18]** you see

**[2:56:18 – 2:56:19]** the whole

**[2:56:19 – 2:56:19]** point of

**[2:56:19 – 2:56:24]** adaptive

**[2:56:24 – 2:56:25]** algorithms

**[2:56:25 – 2:56:26]** is to

**[2:56:26 – 2:56:27]** treat

**[2:56:27 – 2:56:28]** different

**[2:56:28 – 2:56:28]** components

**[2:56:28 – 2:56:29]** of the

**[2:56:29 – 2:56:29]** vector

**[2:56:29 – 2:56:30]** differently

**[2:56:30 – 2:56:31]** right

**[2:56:31 – 2:56:32]** and they

**[2:56:32 – 2:56:32]** shine

**[2:56:32 – 2:56:33]** when you

**[2:56:33 – 2:56:33]** have

**[2:56:33 – 2:56:34]** like

**[2:56:34 – 2:56:35]** lots of

**[2:56:35 – 2:56:36]** high

**[2:56:36 – 2:56:37]** dimension

**[2:56:37 – 2:56:38]** and in

**[2:56:38 – 2:56:38]** this high

**[2:56:38 – 2:56:39]** dimension

**[2:56:39 – 2:56:39]** there are

**[2:56:39 – 2:56:39]** some

**[2:56:39 – 2:56:40]** dimensions

**[2:56:40 – 2:56:40]** that

**[2:56:40 – 2:56:43]** have this

**[2:56:43 – 2:56:43]** kind of

**[2:56:43 – 2:56:44]** behavior

**[2:56:44 – 2:56:44]** this kind

**[2:56:44 – 2:56:45]** of

**[2:56:45 – 2:56:45]** optimization

**[2:56:45 – 2:56:46]** landscape

**[2:56:46 – 2:56:47]** other dimensions

**[2:56:47 – 2:56:48]** that have

**[2:56:48 – 2:56:48]** that kind

**[2:56:48 – 2:56:49]** of optimization

**[2:56:49 – 2:56:49]** landscape

**[2:56:49 – 2:56:50]** etc.

**[2:56:51 – 2:56:53]** And

**[2:56:53 – 2:56:59]** I cannot

**[2:56:59 – 2:57:00]** do this

**[2:57:00 – 2:57:00]** in dimension

**[2:57:00 – 2:57:01]** 2.

**[2:57:01 – 2:57:02]** I cannot

**[2:57:02 – 2:57:03]** give you

**[2:57:03 – 2:57:03]** an example

**[2:57:03 – 2:57:04]** on a plane

**[2:57:04 – 2:57:06]** where x

**[2:57:06 – 2:57:06]** and y

**[2:57:06 – 2:57:07]** are wildly

**[2:57:07 – 2:57:07]** different

**[2:57:07 – 2:57:08]** and there

**[2:57:08 – 2:57:09]** is a big

**[2:57:09 – 2:57:09]** difference

**[2:57:09 – 2:57:09]** between

**[2:57:09 – 2:57:10]** ADM

**[2:57:10 – 2:57:10]** and RMS

**[2:57:10 – 2:57:11]** prop.

**[2:57:11 – 2:57:12]** Not going

**[2:57:12 – 2:57:12]** to work.

**[2:57:13 – 2:57:13]** I cannot

**[2:57:13 – 2:57:13]** give you

**[2:57:13 – 2:57:14]** an example

**[2:57:14 – 2:57:14]** like that.

**[2:57:15 – 2:57:15]** So you

**[2:57:15 – 2:57:16]** will definitely

**[2:57:16 – 2:57:16]** have

**[2:57:16 – 2:57:17]** examples

**[2:57:17 – 2:57:18]** like that

**[2:57:18 – 2:57:20]** in the

**[2:57:20 – 2:57:20]** practical part

**[2:57:20 – 2:57:21]** and here

**[2:57:21 – 2:57:22]** I can

**[2:57:22 – 2:57:23]** and as

**[2:57:23 – 2:57:23]** for the

**[2:57:23 – 2:57:23]** pictures

**[2:57:23 – 2:57:25]** I can

**[2:57:25 – 2:57:26]** just show

**[2:57:26 – 2:57:26]** you

**[2:57:26 – 2:57:27]** some

**[2:57:27 – 2:57:28]** nice

**[2:57:28 – 2:57:28]** pictures

**[2:57:28 – 2:57:29]** this is

**[2:57:29 – 2:57:30]** the problem

**[2:57:30 – 2:57:30]** again

**[2:57:30 – 2:57:32]** like this

**[2:57:32 – 2:57:34]** I can

**[2:57:34 – 2:57:35]** show you

**[2:57:35 – 2:57:35]** some

**[2:57:35 – 2:57:35]** nice

**[2:57:35 – 2:57:36]** pictures

**[2:57:36 – 2:57:36]** but

**[2:57:36 – 2:57:37]** they don't

**[2:57:37 – 2:57:38]** really mean

**[2:57:38 – 2:57:38]** anything

**[2:57:38 – 2:57:38]** so

**[2:57:38 – 2:57:39]** here is

**[2:57:39 – 2:57:40]** another

**[2:57:40 – 2:57:41]** like

**[2:57:41 – 2:57:43]** standard

**[2:57:43 – 2:57:44]** function

**[2:57:44 – 2:57:44]** that

**[2:57:44 – 2:57:45]** has been

**[2:57:45 – 2:57:45]** a test

**[2:57:45 – 2:57:46]** bed

**[2:57:46 – 2:57:46]** of

**[2:57:46 – 2:57:46]** optimization

**[2:57:46 – 2:57:47]** in

**[2:57:47 – 2:57:48]** classical

**[2:57:48 – 2:57:48]** optimization

**[2:57:48 – 2:57:49]** theory

**[2:57:49 – 2:57:50]** it's called

**[2:57:50 – 2:57:51]** Beale's

**[2:57:51 – 2:57:51]** function

**[2:57:51 – 2:57:53]** or Rosenbrock's

**[2:57:53 – 2:57:53]** function

**[2:57:53 – 2:57:54]** I mix up

**[2:57:54 – 2:57:54]** the two

**[2:57:54 – 2:57:55]** and

**[2:57:55 – 2:57:56]** it's basically

**[2:57:56 – 2:57:57]** let me

**[2:57:57 – 2:57:58]** find it

**[2:57:58 – 2:57:58]** somewhere

**[2:57:58 – 2:58:00]** it's basically

**[2:58:00 – 2:58:02]** a complicated

**[2:58:02 – 2:58:02]** polynomial

**[2:58:02 – 2:58:03]** here it is

**[2:58:03 – 2:58:04]** it's basically

**[2:58:04 – 2:58:05]** some

**[2:58:05 – 2:58:06]** complicated

**[2:58:06 – 2:58:06]** polynomial

**[2:58:06 – 2:58:07]** you don't

**[2:58:07 – 2:58:07]** have to

**[2:58:07 – 2:58:08]** memorize

**[2:58:08 – 2:58:08]** that

**[2:58:08 – 2:58:08]** it's just

**[2:58:08 – 2:58:09]** some

**[2:58:09 – 2:58:10]** kind of

**[2:58:10 – 2:58:10]** constants

**[2:58:10 – 2:58:11]** that are

**[2:58:11 – 2:58:12]** tweaked

**[2:58:12 – 2:58:12]** in such

**[2:58:12 – 2:58:13]** a way

**[2:58:13 – 2:58:14]** that

**[2:58:14 – 2:58:16]** it has

**[2:58:16 – 2:58:17]** an interesting

**[2:58:17 – 2:58:17]** optimization

**[2:58:17 – 2:58:18]** landscape

**[2:58:18 – 2:58:19]** so you

**[2:58:19 – 2:58:19]** have this

**[2:58:19 – 2:58:20]** minimum

**[2:58:20 – 2:58:20]** over here

**[2:58:20 – 2:58:22]** but around

**[2:58:22 – 2:58:23]** this minimum

**[2:58:23 – 2:58:23]** you have

**[2:58:23 – 2:58:24]** like this

**[2:58:24 – 2:58:24]** very steep

**[2:58:24 – 2:58:25]** slope

**[2:58:25 – 2:58:25]** over here

**[2:58:25 – 2:58:26]** you see

**[2:58:26 – 2:58:26]** how close

**[2:58:26 – 2:58:27]** the

**[2:58:27 – 2:58:28]** contour lines

**[2:58:28 – 2:58:28]** are to

**[2:58:28 – 2:58:29]** each other

**[2:58:29 – 2:58:29]** but then

**[2:58:29 – 2:58:30]** this steep

**[2:58:30 – 2:58:30]** slope

**[2:58:30 – 2:58:31]** suddenly

**[2:58:31 – 2:58:31]** becomes

**[2:58:31 – 2:58:32]** a very

**[2:58:32 – 2:58:32]** shallow

**[2:58:32 – 2:58:32]** slope

**[2:58:32 – 2:58:33]** so it's

**[2:58:33 – 2:58:34]** like

**[2:58:34 – 2:58:34]** it's easy

**[2:58:34 – 2:58:35]** to go

**[2:58:35 – 2:58:35]** quick

**[2:58:35 – 2:58:36]** down

**[2:58:36 – 2:58:36]** this

**[2:58:36 – 2:58:36]** slope

**[2:58:36 – 2:58:37]** but then

**[2:58:37 – 2:58:37]** you need

**[2:58:37 – 2:58:38]** to recognize

**[2:58:38 – 2:58:38]** that now

**[2:58:38 – 2:58:39]** it's shallow

**[2:58:39 – 2:58:39]** and you need

**[2:58:39 – 2:58:39]** to kind

**[2:58:39 – 2:58:40]** of speed

**[2:58:40 – 2:58:40]** up

**[2:58:40 – 2:58:41]** which

**[2:58:41 – 2:58:41]** some

**[2:58:41 – 2:58:41]** algorithms

**[2:58:41 – 2:58:42]** really

**[2:58:42 – 2:58:42]** cannot

**[2:58:42 – 2:58:42]** do

**[2:58:42 – 2:58:44]** so

**[2:58:44 – 2:58:44]** this

**[2:58:44 – 2:58:45]** is a

**[2:58:45 – 2:58:45]** good

**[2:58:45 – 2:58:46]** test

**[2:58:46 – 2:58:46]** example

**[2:58:46 – 2:58:49]** but

**[2:58:49 – 2:58:50]** in fact

**[2:58:50 – 2:58:51]** I don't

**[2:58:51 – 2:58:51]** think I

**[2:58:51 – 2:58:52]** can actually

**[2:58:52 – 2:58:52]** illustrate

**[2:58:52 – 2:58:53]** real

**[2:58:53 – 2:58:53]** difference

**[2:58:53 – 2:58:54]** between

**[2:58:54 – 2:58:54]** Adam

**[2:58:54 – 2:58:55]** and

**[2:58:55 – 2:58:55]** other

**[2:58:55 – 2:58:56]** adaptive

**[2:58:56 – 2:58:56]** variants

**[2:58:56 – 2:58:58]** so

**[2:58:58 – 2:58:58]** here

**[2:58:58 – 2:58:58]** is what

**[2:58:58 – 2:58:59]** SGD

**[2:58:59 – 2:58:59]** does

**[2:58:59 – 2:59:00]** SGD

**[2:59:00 – 2:59:00]** goes

**[2:59:00 – 2:59:01]** as

**[2:59:01 – 2:59:02]** you would

**[2:59:02 – 2:59:03]** assume

**[2:59:03 – 2:59:03]** goes

**[2:59:03 – 2:59:04]** in the

**[2:59:04 – 2:59:04]** correct

**[2:59:04 – 2:59:04]** direction

**[2:59:04 – 2:59:05]** unless

**[2:59:05 – 2:59:06]** it diverges

**[2:59:06 – 2:59:07]** completely

**[2:59:07 – 2:59:07]** of course

**[2:59:07 – 2:59:07]** you can

**[2:59:07 – 2:59:08]** always

**[2:59:08 – 2:59:08]** have

**[2:59:08 – 2:59:08]** your

**[2:59:08 – 2:59:09]** learning

**[2:59:09 – 2:59:09]** rate

**[2:59:09 – 2:59:09]** to be

**[2:59:09 – 2:59:09]** too

**[2:59:09 – 2:59:10]** high

**[2:59:10 – 2:59:10]** so

**[2:59:10 – 2:59:10]** that

**[2:59:10 – 2:59:11]** everything

**[2:59:11 – 2:59:11]** diverges

**[2:59:11 – 2:59:12]** but

**[2:59:12 – 2:59:13]** if

**[2:59:13 – 2:59:13]** it's

**[2:59:13 – 2:59:13]** not

**[2:59:13 – 2:59:13]** too

**[2:59:13 – 2:59:14]** high

**[2:59:14 – 2:59:14]** then

**[2:59:14 – 2:59:14]** of course

**[2:59:14 – 2:59:14]** it

**[2:59:14 – 2:59:15]** goes

**[2:59:15 – 2:59:15]** in

**[2:59:15 – 2:59:15]** the

**[2:59:15 – 2:59:16]** necessary

**[2:59:16 – 2:59:16]** direction

**[2:59:16 – 2:59:17]** and

**[2:59:17 – 2:59:17]** the

**[2:59:17 – 2:59:18]** faster

**[2:59:18 – 2:59:18]** you

**[2:59:18 – 2:59:18]** go

**[2:59:18 – 2:59:18]** the

**[2:59:18 – 2:59:19]** closer

**[2:59:19 – 2:59:19]** you

**[2:59:19 – 2:59:19]** get

**[2:59:19 – 2:59:20]** but

**[2:59:20 – 2:59:21]** if

**[2:59:21 – 2:59:21]** you

**[2:59:21 – 2:59:22]** go

**[2:59:22 – 2:59:22]** too

**[2:59:22 – 2:59:22]** fast

**[2:59:22 – 2:59:22]** you

**[2:59:22 – 2:59:23]** risk

**[2:59:23 – 2:59:23]** divergence

**[2:59:23 – 2:59:24]** so

**[2:59:24 – 2:59:24]** with

**[2:59:24 – 2:59:25]** SGD

**[2:59:25 – 2:59:25]** it's

**[2:59:25 – 2:59:25]** always

**[2:59:25 – 2:59:26]** about

**[2:59:26 – 2:59:27]** finding

**[2:59:27 – 2:59:27]** the

**[2:59:27 – 2:59:27]** best

**[2:59:27 – 2:59:28]** learning

**[2:59:28 – 2:59:28]** rate

**[2:59:28 – 2:59:30]** if

**[2:59:30 – 2:59:30]** you

**[2:59:30 – 2:59:31]** add

**[2:59:31 – 2:59:31]** momentum

**[2:59:31 – 2:59:32]** you

**[2:59:32 – 2:59:32]** have

**[2:59:32 – 2:59:33]** exactly

**[2:59:33 – 2:59:33]** the

**[2:59:33 – 2:59:33]** same

**[2:59:33 – 2:59:33]** effects

**[2:59:33 – 2:59:34]** that

**[2:59:34 – 2:59:34]** we

**[2:59:34 – 2:59:34]** discussed

**[2:59:34 – 2:59:35]** right

**[2:59:35 – 2:59:36]** so

**[2:59:36 – 2:59:37]** standard

**[2:59:37 – 2:59:38]** SGD

**[2:59:38 – 2:59:38]** goes

**[2:59:38 – 2:59:38]** and

**[2:59:38 – 2:59:39]** goes

**[2:59:39 – 2:59:39]** but

**[2:59:39 – 2:59:39]** it

**[2:59:39 – 2:59:39]** still

**[2:59:39 – 2:59:39]** has

**[2:59:39 – 2:59:39]** a

**[2:59:39 – 2:59:40]** long

**[2:59:40 – 2:59:40]** way

**[2:59:40 – 2:59:40]** to

**[2:59:40 – 2:59:41]** go

**[2:59:41 – 2:59:42]** SGD

**[2:59:42 – 2:59:42]** with

**[2:59:42 – 2:59:43]** momentum

**[2:59:43 – 2:59:44]** almost

**[2:59:44 – 2:59:44]** left

**[2:59:44 – 2:59:45]** the

**[2:59:45 – 2:59:45]** basin

**[2:59:45 – 2:59:45]** of

**[2:59:45 – 2:59:45]** this

**[2:59:45 – 2:59:46]** minimum

**[2:59:46 – 2:59:46]** it

**[2:59:46 – 2:59:47]** almost

**[2:59:47 – 2:59:47]** failed

**[2:59:47 – 2:59:48]** over

**[2:59:48 – 2:59:48]** here

**[2:59:48 – 2:59:48]** but

**[2:59:48 – 2:59:49]** thankfully

**[2:59:49 – 2:59:49]** it

**[2:59:49 – 2:59:49]** could

**[2:59:49 – 2:59:50]** come

**[2:59:50 – 2:59:50]** back

**[2:59:50 – 2:59:50]** but

**[2:59:50 – 2:59:51]** then

**[2:59:51 – 2:59:51]** it

**[2:59:52 – 2:59:54]** is

**[2:59:54 – 2:59:55]** optimum

**[2:59:55 – 2:59:55]** by far

**[2:59:55 – 2:59:56]** and

**[2:59:56 – 2:59:56]** as you

**[2:59:56 – 2:59:57]** can see

**[2:59:57 – 2:59:57]** it

**[2:59:57 – 2:59:58]** disappeared

**[2:59:58 – 2:59:58]** on the

**[2:59:58 – 2:59:58]** right

**[2:59:58 – 2:59:58]** and

**[2:59:58 – 2:59:59]** hasn't

**[2:59:59 – 2:59:59]** come

**[2:59:59 – 2:59:59]** back

**[2:59:59 – 2:59:59]** yet

**[2:59:59 – 3:00:00]** in

**[3:00:00 – 3:00:00]** 200

**[3:00:00 – 3:00:00]** steps

**[3:00:00 – 3:00:02]** while

**[3:00:02 – 3:00:03]** Nesterov's

**[3:00:03 – 3:00:04]** momentum

**[3:00:04 – 3:00:05]** yeah

**[3:00:05 – 3:00:05]** it is

**[3:00:05 – 3:00:06]** already

**[3:00:06 – 3:00:06]** coming

**[3:00:06 – 3:00:06]** back

**[3:00:06 – 3:00:06]** it's

**[3:00:06 – 3:00:07]** still

**[3:00:07 – 3:00:07]** not

**[3:00:07 – 3:00:07]** here

**[3:00:07 – 3:00:08]** but

**[3:00:08 – 3:00:08]** obviously

**[3:00:08 – 3:00:08]** it's

**[3:00:08 – 3:00:09]** the

**[3:00:09 – 3:00:09]** best

**[3:00:09 – 3:00:09]** of

**[3:00:09 – 3:00:09]** the

**[3:00:09 – 3:00:09]** three

**[3:00:09 – 3:00:10]** so

**[3:00:10 – 3:00:10]** it's

**[3:00:10 – 3:00:11]** already

**[3:00:11 – 3:00:12]** coming

**[3:00:12 – 3:00:12]** back

**[3:00:12 – 3:00:12]** and

**[3:00:12 – 3:00:13]** it

**[3:00:13 – 3:00:13]** will

**[3:00:13 – 3:00:13]** be

**[3:00:13 – 3:00:14]** there

**[3:00:14 – 3:00:14]** soon

**[3:00:14 – 3:00:17]** and

**[3:00:17 – 3:00:17]** as

**[3:00:17 – 3:00:17]** for

**[3:00:17 – 3:00:18]** these

**[3:00:18 – 3:00:18]** algorithms

**[3:00:18 – 3:00:18]** that

**[3:00:18 – 3:00:19]** we

**[3:00:19 – 3:00:19]** discussed

**[3:00:19 – 3:00:19]** like

**[3:00:19 – 3:00:20]** SGD

**[3:00:20 – 3:00:20]** I

**[3:00:20 – 3:00:20]** the

**[3:00:20 – 3:00:20]** great

**[3:00:20 – 3:00:21]** delta

**[3:00:21 – 3:00:22]** well

**[3:00:22 – 3:00:23]** they

**[3:00:23 – 3:00:23]** kind

**[3:00:23 – 3:00:23]** of

**[3:00:23 – 3:00:24]** do

**[3:00:24 – 3:00:25]** better

**[3:00:26 – 3:00:26]** no real

**[3:00:26 – 3:00:27]** difference

**[3:00:27 – 3:00:27]** here

**[3:00:27 – 3:00:27]** so

**[3:00:27 – 3:00:28]** either

**[3:00:28 – 3:00:28]** delta

**[3:00:28 – 3:00:28]** is

**[3:00:28 – 3:00:29]** worse

**[3:00:29 – 3:00:29]** but

**[3:00:29 – 3:00:30]** also

**[3:00:30 – 3:00:30]** you

**[3:00:30 – 3:00:30]** shouldn't

**[3:00:30 – 3:00:30]** come

**[3:00:30 – 3:00:30]** to

**[3:00:30 – 3:00:31]** conclusions

**[3:00:31 – 3:00:31]** about

**[3:00:31 – 3:00:31]** this

**[3:00:31 – 3:00:32]** and

**[3:00:32 – 3:00:32]** either

**[3:00:32 – 3:00:33]** great

**[3:00:33 – 3:00:33]** and

**[3:00:33 – 3:00:33]** adem

**[3:00:33 – 3:00:34]** they

**[3:00:34 – 3:00:34]** just

**[3:00:34 – 3:00:34]** both

**[3:00:34 – 3:00:35]** do

**[3:00:35 – 3:00:35]** a

**[3:00:35 – 3:00:35]** good

**[3:00:35 – 3:00:35]** job

**[3:00:35 – 3:00:35]** over

**[3:00:35 – 3:00:36]** here

**[3:00:36 – 3:00:36]** so

**[3:00:36 – 3:00:38]** there

**[3:00:38 – 3:00:38]** is

**[3:00:38 – 3:00:38]** no

**[3:00:38 – 3:00:39]** significant

**[3:00:39 – 3:00:39]** difference

**[3:00:39 – 3:00:40]** but

**[3:00:40 – 3:00:40]** as

**[3:00:40 – 3:00:40]** an

**[3:00:40 – 3:00:41]** illustration

**[3:00:41 – 3:00:41]** again

**[3:00:41 – 3:00:42]** here

**[3:00:42 – 3:00:42]** is

**[3:00:42 – 3:00:43]** what

**[3:00:43 – 3:00:43]** optimization

**[3:00:43 – 3:00:43]** looks

**[3:00:43 – 3:00:44]** like

**[3:00:44 – 3:00:44]** in

**[3:00:44 – 3:00:44]** dimension

**[3:00:44 – 3:00:45]** 2

**[3:00:45 – 3:00:46]** it's

**[3:00:46 – 3:00:46]** not

**[3:00:46 – 3:00:46]** a

**[3:00:46 – 3:00:47]** good

**[3:00:47 – 3:00:47]** guide

**[3:00:47 – 3:00:48]** to

**[3:00:48 – 3:00:48]** what

**[3:00:48 – 3:00:48]** optimization

**[3:00:48 – 3:00:49]** looks

**[3:00:49 – 3:00:49]** like

**[3:00:49 – 3:00:49]** in

**[3:00:49 – 3:00:49]** dimension

**[3:00:49 – 3:00:50]** 100

**[3:00:50 – 3:00:50]** but

**[3:00:50 – 3:00:51]** unfortunately

**[3:00:51 – 3:00:51]** I

**[3:00:51 – 3:00:52]** cannot

**[3:00:52 – 3:00:52]** plot

**[3:00:52 – 3:00:53]** dimension

**[3:00:53 – 3:00:53]** 100

**[3:00:53 – 3:00:54]** for

**[3:00:59 – 3:00:59]** we wrap

**[3:00:59 – 3:01:00]** up

**[3:01:00 – 3:01:00]** I

**[3:01:00 – 3:01:00]** think

**[3:01:00 – 3:01:01]** I

**[3:01:01 – 3:01:01]** have

**[3:01:01 – 3:01:02]** just

**[3:01:02 – 3:01:02]** a

**[3:01:02 – 3:01:02]** couple

**[3:01:02 – 3:01:03]** more

**[3:01:03 – 3:01:04]** things

**[3:01:04 – 3:01:05]** that

**[3:01:05 – 3:01:05]** I

**[3:01:05 – 3:01:06]** wanted

**[3:01:06 – 3:01:07]** to

**[3:01:07 – 3:01:07]** mention

**[3:01:07 – 3:01:07]** today

**[3:01:07 – 3:01:10]** so

**[3:01:10 – 3:01:11]** one

**[3:01:11 – 3:01:11]** thing

**[3:01:11 – 3:01:12]** is

**[3:01:12 – 3:01:15]** a

**[3:01:15 – 3:01:16]** version

**[3:01:16 – 3:01:16]** of

**[3:01:16 – 3:01:16]** ADOM

**[3:01:16 – 3:01:18]** it's

**[3:01:18 – 3:01:19]** the

**[3:01:19 – 3:01:21]** and

**[3:01:21 – 3:01:21]** again

**[3:01:21 – 3:01:22]** it's

**[3:01:22 – 3:01:23]** a

**[3:01:23 – 3:01:23]** version

**[3:01:23 – 3:01:23]** of

**[3:01:23 – 3:01:23]** ADOM

**[3:01:23 – 3:01:24]** that

**[3:01:24 – 3:01:27]** first

**[3:01:27 – 3:01:28]** of

**[3:01:28 – 3:01:28]** all

**[3:01:28 – 3:01:28]** is

**[3:01:28 – 3:01:29]** practical

**[3:01:29 – 3:01:30]** you can

**[3:01:30 – 3:01:30]** actually

**[3:01:30 – 3:01:31]** encounter

**[3:01:31 – 3:01:31]** it

**[3:01:31 – 3:01:31]** in

**[3:01:31 – 3:01:32]** deep

**[3:01:32 – 3:01:32]** learning

**[3:01:32 – 3:01:32]** practice

**[3:01:32 – 3:01:33]** it

**[3:01:33 – 3:01:33]** actually

**[3:01:33 – 3:01:34]** happens

**[3:01:34 – 3:01:35]** but

**[3:01:35 – 3:01:46]** But also, it comes from a very interesting motivation.

**[3:01:46 – 3:01:52]** So let me explain the motivation to you, and then I will mention this version.

**[3:01:53 – 3:01:57]** The motivation comes from a different way of doing regularization.

**[3:02:00 – 3:02:08]** When people did classical neural networks back in the day, back in the 1980s, back in the 1990s,

**[3:02:08 – 3:02:13]** regularization was usually done through this process called weight decay.

**[3:02:13 – 3:02:15]** So what is weight decay?

**[3:02:15 – 3:02:19]** What is the difference between regularization that we discussed yesterday and weight decay like this?

**[3:02:21 – 3:02:36]** In regular regularization, pardon the pun, you have like L of W being your loss function plus something like alpha times a regularizer.

**[3:02:36 – 3:02:42]** And then you minimize your loss function with a regularizer.

**[3:02:43 – 3:02:43]** That's it.

**[3:02:45 – 3:02:52]** So notice that regularization like this, like L2 regularization, L1 regularization, it's very, very easy to do in deep learning.

**[3:02:52 – 3:02:56]** Because all that you do is, it's a slight modification of the loss function.

**[3:02:57 – 3:02:59]** The algorithms don't have to change.

**[3:03:00 – 3:03:03]** Just your computational graph gets a couple more nodes and that's it.

**[3:03:06 – 3:03:09]** But in classical neural networks, they did it differently.

**[3:03:09 – 3:03:10]** They did it like this.

**[3:03:11 – 3:03:12]** So weight decay looked like this.

**[3:03:13 – 3:03:18]** When you go from, in your gradient descent, when you go from WK to WK plus 1,

**[3:03:19 – 3:03:27]** before adding the gradient, you multiply, you shrink the weights that you have.

**[3:03:27 – 3:03:29]** You multiply them by a constant less than 1.

**[3:03:30 – 3:03:37]** And then you add or subtract the current value of the gradient.

**[3:03:38 – 3:03:41]** Okay, so regularization, why is it called weight decay?

**[3:03:41 – 3:03:46]** Because weights decay a little, and then you do your gradient step.

**[3:03:49 – 3:03:50]** It looks pretty weird.

**[3:03:51 – 3:03:57]** And actually, pretty soon people realize that it's the same thing as SL2 regularization.

**[3:03:57 – 3:04:01]** When you do gradient descent, you can just...

**[3:04:01 – 3:04:07]** So let's just continue this formula, and let me write it like this.

**[3:04:07 – 3:04:14]** So it's Wk minus 1 minus gamma time Wk, right?

**[3:04:14 – 3:04:23]** I'm just pulling out the Wk itself, minus alpha times Gk.

**[3:04:24 – 3:04:25]** And what is Gk? Sorry.

**[3:04:27 – 3:04:34]** Gk is the gradient of L with respect to W at point K.

**[3:04:35 – 3:04:42]** So why don't I take this part and just put it down to the gradient here, inside the gradient.

**[3:04:42 – 3:04:48]** So now I have Wk minus alpha times the gradient of what?

**[3:04:48 – 3:05:08]** Of L. And here I have like some constant, 1 minus gamma divided by alpha, whatever that is, times just Wk times W times W, right?

**[3:05:08 – 3:05:14]** Just the norm of W squared. And I need to do it at point Wk.

**[3:05:16 – 3:05:26]** So when you look at it this way, you see that weight decay like this is exactly equivalent to just L2 regularization with a certain,

**[3:05:26 – 3:05:31]** with a certain constant. It's completely equivalent, it's completely the same.

**[3:05:32 – 3:05:37]** So people kind of forgot about weight decay, didn't use it at the beginning of the deep learning revolution.

**[3:05:38 – 3:05:44]** But then people realized at some point, also a pretty interesting idea, that, okay,

**[3:05:44 – 3:05:50]** so classical weight decay in regular gradient descent is exactly equivalent to L2 regularizer.

**[3:05:51 – 3:05:59]** That's true. But if you are doing something like ADEM, if you are doing some complicated thing with

**[3:05:59 – 3:06:07]** momenta and cumulative exponential moving averages of gradients squared and so on and so forth,

**[3:06:08 – 3:06:15]** then this equivalence doesn't hold anymore. Now there is no equality if the update rule is not that

**[3:06:15 – 3:06:25]** simple, if the update rule is actually, say, ADEM. So what people did at some point, they carefully

**[3:06:25 – 3:06:38]** worked this kind of regularization through ADEM, and they saw what to modify inside ADEM.

**[3:06:38 – 3:06:42]** It was actually a pretty simple tweak, but you had to do the math to see where it is.

**[3:06:43 – 3:06:51]** What to modify inside ADEM to make it more like weight decay than L2 regularization.

**[3:06:52 – 3:07:01]** And the resulting algorithm is called ADEM-W, and it's also a popular gradient descent variant.

**[3:07:01 – 3:07:03]** It's also a popular algorithm.

**[3:07:04 – 3:07:10]** So, okay, I think I should be stopping here.

**[3:07:10 – 3:07:20]** So let me just mention, I didn't plan to discuss them in detail, but let me mention that, of course, the research didn't stop on ADEM and ADEM-W.

**[3:07:21 – 3:07:31]** There are recently developed algorithms like Lion and Muon, and they have their own interesting properties.

**[3:07:31 – 3:07:46]** There is an algorithm, one of them, I keep forgetting which one, that was obtained by actually automated search, like the automated search that produced Swish, the Swish activation function, but for gradient descent algorithms, why not?

**[3:07:47 – 3:07:55]** The other uses special properties of transformers and is very useful for internal layers of language models, whatever.

**[3:07:55 – 3:08:09]** So the research continues, but still I think even in 2026, the standard algorithm would be something like ADM or ADM-W, or actually, still very useful, classical SGD.

**[3:08:09 – 3:08:14]** It's still a reasonable algorithm if you can tweak the learning rate.

**[3:08:15 – 3:08:22]** So in conclusion, let me just quickly go through the slides to see what I forgot.

**[3:08:22 – 3:08:25]** Okay, so this is our example.

**[3:08:25 – 3:08:32]** This is Nesterov's, this is Yuri Nesterov, for some reason downscaled a lot, blah, blah, blah.

**[3:08:32 – 3:08:44]** AdaGrad, AdaDelta, RMSProb, ADM, that's what we just discussed, NAIDM, okay, there is a version of ADM with Nesterov momentum called NAIDM.

**[3:08:44 – 3:08:53]** It's a version of ADM with Nesterov momentum called NAIDM, never heard about it afterwards, et cetera, et cetera.

**[3:08:53 – 3:08:55]** Then I will definitely skip this.

**[3:08:55 – 3:08:57]** So fixing weight decay regularization in ADM.

**[3:08:57 – 3:09:04]** This is ADM W. SGD with weight decay, ADM with weight decay, it has some good properties,

**[3:09:04 – 3:09:07]** which I don't have time to go into now.

**[3:09:07 – 3:09:11]** And let me finish, yeah, let me finish with these slides.

**[3:09:11 – 3:09:20]** Two last stories that both make the same general point.

**[3:09:20 – 3:09:23]** The first is the story of Superconvergence.

**[3:09:23 – 3:09:33]** Back in 2017, there was a very famous paper called Superconvergence that proposed to do

**[3:09:33 – 3:09:36]** a cyclic learning rate schedule.

**[3:09:36 – 3:09:43]** What it means is we slow down the training, we decrease the learning rate, and then at

**[3:09:43 – 3:09:46]** some point we speed it back up again.

**[3:09:46 – 3:09:52]** So we go slow, slow, slow, and then suddenly we rise up again and do a large update, and

**[3:09:52 – 3:09:55]** then we slow down again.

**[3:09:55 – 3:10:00]** And they showed in some very convincing experiments, of course there couldn't be any theorems about

**[3:10:00 – 3:10:08]** it, but they did some very convincing experiments, and they actually showed that they can converge

**[3:10:08 – 3:10:13]** to approximately the same results, not better, but the same results, but much, much, much

**[3:10:13 – 3:10:28]** faster. Like 10x, 20x faster. And it was all the buzz in 2017, but now you never hear about it. So

**[3:10:28 – 3:10:34]** cyclical learning crates are still a thing, but they are not universally accepted, and you probably

**[3:10:34 – 3:10:46]** are not going to use them in practice. This is one example. And the other example, also related to

**[3:10:46 – 3:10:51]** stochastic gradient descent, which is why I'm talking about these examples here. The other

**[3:10:51 – 3:10:59]** example is AMS Grad. It was a great paper. In 2018, it won ICLR 2018 Best Paper Award.

**[3:11:00 – 3:11:10]** It was a great idea. So they basically took the ADEM paper. In the ADEM paper, they had a

**[3:11:10 – 3:11:15]** convergence proof. They couldn't estimate the rate of convergence, but they had the proof that ADEM

**[3:11:15 – 3:11:24]** converges. And these guys found the mistake in the proof. And these guys showed counterexamples

**[3:11:24 – 3:11:29]** where ADEM can actually diverge, where it does not converge, where it doesn't work at all.

**[3:11:29 – 3:11:39]** Right? And what's even better, they could fix it. They proposed a small modification of ADEM

**[3:11:39 – 3:11:46]** called AMSGrat that basically replaces the sum with the max somewhere or something like that.

**[3:11:47 – 3:11:55]** The algorithm is in front of you. And for this algorithm, they could prove convergence,

**[3:11:55 – 3:12:06]** and the proof now was correct. So they found a mistake in ADEM, and they fixed it. And now,

**[3:12:08 – 3:12:16]** for eight years, we've had an algorithm which is probably better than ADEM. But my point is,

**[3:12:16 – 3:12:22]** unfortunately, nobody uses it. I've never heard about anybody using AMSGrat in practice.

**[3:12:22 – 3:12:28]** I guess you can use it. It's probably implemented in all the libraries. I guess you can try it. It'll

**[3:12:28 – 3:12:36]** probably be either exactly the same as ADEM or even worse. So let me close with this slightly

**[3:12:36 – 3:12:44]** disappointing point that even good ideas, even ideas that get confirmed by your experiments,

**[3:12:44 – 3:12:49]** that get confirmed even by theory. So the theory is correct. There is indeed a mistake in the ADEM

**[3:12:49 – 3:12:57]** paper. And this paper does not have a mistake. This paper did fix it. But unfortunately, it's not

**[3:12:57 – 3:13:06]** enough to get a new universally accepted algorithm. It's still practice is the final

**[3:13:06 – 3:13:16]** arbiter. Still, we as a field are very applied, a very practical field, artificial intelligence,

**[3:13:16 – 3:13:20]** deep learning specifically. So ultimately, people are going to use what works.

**[3:13:21 – 3:13:28]** And ADM still works. So with this, I want to stop for today. Are there any

**[3:13:28 – 3:13:40]** questions, comments, discussion? Okay, thank you. Yes, of course, I want feedback about the lectures.

**[3:13:40 – 3:13:46]** Thank you very much. I'm a bit surprised that gradient descent and backprop are new for you,

**[3:13:46 – 3:13:53]** but good. Then it's good that we repeated it. Okay, wonderful. Okay, thank you very much. And

**[3:13:54 – 3:14:01]** with that, I'm pretty sure you're tired of listening to online lectures for three days straight. I would

**[3:14:01 – 3:14:09]** be, definitely. So it's a good thing that I cede the floor to Alex, whom you will meet tomorrow,

**[3:14:09 – 3:14:14]** and we will have practice starting tomorrow. Thank you. Bye-bye.

**[3:14:14 – 3:14:21]** Sorry, a question? Yeah, sure. So next week, are we going to continue these online lectures at the

**[3:14:21 – 3:14:30]** start of the week? That is a good question. Yeah, so there are scheduling difficulties for me personally,

**[3:14:30 – 3:14:35]** because I'll be traveling next week. So I hope there will be a few lectures next week,

**[3:14:35 – 3:14:48]** but at this point, I cannot promise which days. Okay, so I think our plan for now is like tomorrow

**[3:14:48 – 3:14:55]** definitely is practice day. Tomorrow is our two practices, and then hopefully we will have one

**[3:14:55 – 3:15:00]** practice and one lecture on Friday, and then next week is wide open. I don't know about next week yet.

**[3:15:04 – 3:15:11]** Okay, thank you very much, and bye-bye. I will upload everything as usual. Bye-bye.

## Full text

Good morning, everyone. We continue our investigations of machine learning and yesterday we finally got to neural networks. We got to our main topic of the class and we will be discussing neural networks for the rest of our time. But still, I'm glad that we went over some fundamentals and I hope they have been interesting and instructive for you. So maybe just as a quick recap first, what we did yesterday and where we are right now. So we discussed, yesterday we discussed things like linear models, but basically linear models or more complicated classical machine learning models like, I don't know, regression tree boosting or Gaussian processes or some probabilistic models with some, I don't know, variational clustering or whatever, all of these models followed classically the same pattern, followed the same structure. So you have your high dimensional input, like images, sound, videos, whatever, then you do feature extraction, right? We discussed that yesterday, then you get something like a vector of features and then you do your ML model, right? And the whole point and the ML model now gives you the output which you need. This is the Y and this is the X. So classical models, in classical machine learning, what people would do, they would think and do feature extraction manually. And the main advantage of deep learning when it came on, and by now we have many more advantages, but the main revolution, like the contents of the deep learning revolution of the late 2000s or early 2010s, was that this manual feature extraction switched to end-to-end learning of a single model, which was the neural network, right? So now in deep learning, mostly this is all a big neural network, right? And when we implement it, when we run it, it's just a single thing that we don't need to distinguish, but inside, of course, there is the first part, the main part, that still does the feature extraction, and then it produces the semantically relevant features, the features that are, by virtue of training, the most meaningful features for the output that we want, and then we do the final layer, which is, again, one of these linear models usually, either linear regression if we predict a number, or logistic regression if we do classification, as we actually usually do. It's rare to have numbers as outputs. We will have examples like that, but it's not really common. So then, what else we did yesterday? We started talking about the structure of neural networks, but we only started talking about individual perceptrons, individual artificial neurons. And this was, I think, where we stopped. We discussed that a common structure of a single unit in the neural network of the perceptron is a linear combination of the inputs followed by a non-linearity. And I think we didn't do, yesterday we didn't do a real survey of these functions, of activation functions, but it's a pretty short topic and let's just get it out of the way now. So what kinds of activation functions can be used in neurons? So again, we discussed yesterday that the whole point of neural networks is to take structures like this, to take small elementary functions like this, and then do like a computational graph based on them. And when you do a computational graph based on elementary functions that you understand, elementary functions that are easy, when you do compositions of easy things, like we discussed with this connectionism principle, which is basically just true, when you compose a lot of simple things, you can get some very complicated results. Of course, the question is, how do you tweak your composition in such a way that the result is what you want? And this is the whole point of deep learning, right? Training such big compositions, finding their weights, learning their weights. But at least theoretically, as soon as you have any kind of non-linearity here, you can more or less approximate anything you want. So our first topic for today, a brief one, will be what are the non-linearities that people actually use? And it's an interesting question, actually. It's a bit more interesting, maybe, than you would expect. So originally, in, I don't know, in 1943, in the original McCulloch-Pitts paper, and in 1958, in Frank Rosenblatt's Perceptron, people used threshold functions. So, the activation would be a threshold, have a side-step function, call it what you want, but basically there would be an A, and the rule would be if W times X is over A, then 1, else 0, right? This is a fine function if all you have is a single perceptron, then it's okay, you can do learning on this and everything more or less works, and that's how the original perceptron worked. But you can't really do networks of these guys, right? So I told you yesterday that you can't do networks of linear perceptrons because if the perceptrons are linear, then it doesn't make any sense to do a network. A composition of linear functions is linear again, so you just get your whole network equivalent to a single perceptron. Well, with these guys, it's not true. With these guys, there are universal approximation theorems. You can definitely approximate whatever you want, but you can't find this approximation, unfortunately, because the only way we have to train such big compositions-- and that will be our main topic for today, actually-- the only way to train such compositions is gradient descent and other techniques that are based on local movements of the weights, on local properties of the loss function. And when you have a piecewise constant activation function, gradients don't work. I mean, formally, they work, but they're just equal to zeros, right? The f' is equal to zero here, f' is equal to zero here. And when you sit over here with your w times x and you move to your w slightly, maybe you go here, maybe you go here, but the answer doesn't change. And the derivative is always zero and we don't know where to go, right? So these guys definitely don't work for networks. So what did people do? People looked at these threshold activations. They still had this idea that a threshold activation is supposed to be good. A threshold activation is like what we are actually trying to achieve. Like a neuron is either activated or not. And we want to have a big composition of neurons that are in various states of activated or not activated. But we cannot have this strict jump. So let's have a soft approximation to it. So for quite a while, throughout all of this classical phase of early neural networks up until 2011 or 12, I think, mostly people used sigmoid activation functions. And so when people say a sigmoid function, what they actually mean is that there is a horizontal asymptote on the left, there is a horizontal asymptote on the right, and the function monotonically goes like this from negative infinity to positive infinity. So the proverbial example, the archetypal example of a sigmoid is the logistic sigmoid, which we discussed yesterday. So sigma of a is one over one plus e to the power of minus a. It goes from zero to one. It's symmetrical. It doesn't have zero derivatives anywhere, et cetera, et cetera. And so there have been, there was a lot of, there were a lot of neural networks in the 1990s, 1980s, 2000s with activation functions like this and also with other sigmoids. So I won't go into details. It doesn't matter for us now. But for technical reasons, it's not really good that your sigmoid saturates at zero. So it's a separate technical problem that you don't really want to approximate zero. So a better sigmoid for at least internal layers would be something that goes from one to, say, minus one. And then it would be symmetrical around zero, actually. And actually, a more common sigmoid function for neural networks was the hyperbolic tangent. And I always forget where the minuses are. a to the power minus a minus, plus, plus, minus, I guess like this. I guess it's like this, yeah. So it goes to one on positive infinity. It goes to minus, yeah, right, it goes to minus one on negative infinity. And again, it's symmetrical, blah, blah, blah, same kind of thing. So people were using these sigmoid functions all the way through about, I don't remember the exact year, but about 2011 or 2012. And in 2011, 2012, there was a very influential paper, a very important remark, that where people tried a completely different activation function, a very, very simple one, and it turned out to work extremely well. So the function that they tried is called ReLU, which stands for Rectified Linear Unit and Linear Unit. And it basically goes like this. So on the negative part of the inputs over here, it's just zero. And on the positive part, it's just x. It equals to the input. So ReLU of A is... Formally, you can write it like max of zero and A, or you can write it with one Boolean operator. So 1 if A greater than zero, L is zero. That's it. Sorry, not 1, A. If A greater than zero, L is zero. That's it. And it proved to be a very cool, very nice activation function. So what were the benefits? Well, first of all, I just told you that it's now good to have piecewise constant activation functions because the gradients are zero. And indeed, if you go through a ReLU, if you go through a neuron, through a unit with ReLU activation, and you have a negative argument for ReLU. So if your W times A falls over here, or W times X falls over here, then you don't learn anything. So it's just straight zero, it propagates as zero, and when you go back, your gradients stop there. We don't yet know what it means to go back, but we'll understand it just now, just today. But in this case, it's okay. In many architectures, it's okay to have this kind of sparsity, and it's even a good thing to have this kind of sparsity. So in, for example, convolutional architectures, which we will discuss, I suppose, in our next lectures, in convolutional architectures, you have the same weights reused a lot of times all across the input. And when you have the same weights reused all across the input, it's fine and it's even desirable to have like half of them just zeroed out. So that's not really a problem. And it turned out that it's really a good property to have unbounded activations like this. So with any kind of sigmoids, you have this problem of saturation. You have the derivatives of your activation function go to zero on the left and on the right. Here the S will go to zero on the left immediately, but on the right they don't. And this means that this sigmoid, no sigmoid can distinguish between activated, really activated, and super-duper activated. It just activated. And what's even worse, when you go to this regime, when your input, when your sigmoid becomes, when your neuron becomes very sure in what it does, when the arguments to the sigmoid become large in absolute value, you stop hearing. So your derivatives are very close to zero, and the gradients just stop. Here, you explicitly stop on the negative side, but on the positive side, you never stop. You just keep learning, which is also great. So in a way, it's... And there is even a mathematical result about this. I don't remember if I have it on the slides. Maybe I do. Let me skip this, activation functions. Yeah, and there is even a mathematical result that says, well, if you take a few sigmoids and you stack them together, like an infinite series of sigmoids and you stack them together, what you get is more or less the real. So if you add up this series, of course, you don't get this exact kink at zero. Of course, it will be smooth. But then it will very soon asymptotically be just y equals x. It will go to a straight line and it will stay being a straight line. So in a way, the real activation is like staking a lot of sigmoids and looking how many of them actually activate, which is, of course, more information. So this is a good thing. What else do I want to say here? Oh, and there is... Yeah, sorry about the Russian on the picture, but there is also a very interesting remark here that connects back to what we discussed yesterday about the brains. Actually, if you look at how our biological neurons activate, it does look like a real activation function. So this is like a good model or whatever of the firing rates of neurons, basically of their activation strength, how much they're excited. And it looks like this black curve over here. So at first it doesn't go negative, of course. But then from zero for a while it just stays non-inactive, not activated at all. Then there is this complicated phase transition. But after the complicated phase transition, we basically get a straight line, which is pretty cool. I mean, it's pretty interesting and unexpected that it would be actually a straight line, but it looks like it is. Of course, it doesn't go to infinity. Please do not experiment with that. No, if you apply a thousand volts to your brain, you will not think faster and better. This will not end well. Do not do that. Of course, it saturates in real life and biology. But in a computer, it doesn't have to saturate, or at least we can stretch the straight line however far we want. Of course, these are just additional considerations. These are just some interesting facts about the real... Of course, the real bonus was that it worked very well. So in practice, as soon as people... it wasn't a new idea, real activations existed since the 1970s or something. But as soon as people tried them with real networks, with convolutional networks especially, and they saw the results in about 2011-2012, mostly everyone switched to realos. Of course, it did not stop there. So there has been a lot of further research on activation functions. There have been interesting results. So what was the next step? Well, the first next step was kind of straightforward. So I said that in some situations it is desirable to have this sparse UTM. In some situations it is a good thing to zero out some of the activations over here. But in other situations it's not. And when you don't want to lose the gradient flow through your network, when you don't want to be sparse, then of course you'd want something non-zero on the left. So the immediate modification was what we call a leaky relo. Basically the same thing, but on the left you also have a straight line, but it's a straight line which has a smaller slope than on the right. So it's still just a single hinge, a connection of two straight lines at zero, but now it's non-zero on the left. And then what people did at around 2017, I think, was they ran an automated search for the best possible activation function. And I do want to discuss this a little bit because we will see examples like that later also. So if you look at your activation functions, what are they? Like, what is their nature? They are just straightforward mathematical functions of one variable, right? Just a function in the high school sense of the word. And what is the representation of this? How do you represent functions? What is the structure of these guys? Well, they're defined by formulas, right? And what is a formula? A formula is a computational graph. So for example, how does ReLU look? What does ReLU look like? Well, you have your input, x, you have a constant zero, and then you have a maximum, and you have your output. Okay, very simple computational graph. Two inputs, one of them, a constant, and that's it. What about the logistic sigmo? Well, you have x, you have 1, you have, for example... I mean, I'm just making an example. You can define functions in a different way. But, for example, here, there is a unary function e to the power minus argument. And then there is plus 1. And then there is the inverse, right? Go 1 over. And as a result, you get sigma of x. For a hyperbolic tangent, you have x, you have e to the power, you have e to the negative power. And then you subtract, and then you add, and then you divide, and you get your hyperbolic tangent, right? And so on. So a function, if you write it as a formula, what the formula actually is, what is a formula is a mathematical object. It's a graph. It's a graph composed of elementary functions of operations that constitute this formula. And which means that you can sweep over these graphs, right? You can search through these graphs. I won't go into details on how exactly people do it. It doesn't matter for our class. But basically, at some point, they ran a very expensive search over a lot of graphs, a lot of activation functions like this. Of course, when you do a search like that, you cannot actually prove anything. There is no mathematical statement. It's all empirical, right? So you just try different stuff, you see what works better on the set of data sets, set of architectures that you set up, and then you just see what works better, right? And you see what works better, and you progress by mutating the graphs a little bit. It's basically an evolutionary thing usually because you can't take a gradient on the graph structure. So you need to do like crossover, like copying parts of one graph to the other, or small mutations, like change around things, see what works, go to the population of things that work, et cetera, et cetera. It's an evolutionary algorithm. And as a result, at that point, they came up with something called the switch activation function. Yeah, 2017, it was done by Google. Of course, who else would have all of that compute back in 2017? And the switch activation function, I mean, I cannot explain to you why it is better. I can only show it to you and say that, yeah, empirically it's better. So it looks kind of like a leaky ReLU, so it's very similar to ReLU on the right, and they are all very similar to ReLU on the right. And on the left, it at first goes like this, but then it goes back to zero. So it's not monotone, interestingly. And yeah, it proved to work better for some reason. And a lot of standard architectures, especially in computer vision, actually, you will see if you go inside, we won't go to that level of detail thinking class, but if you go inside, you will see that a lot of standard architectures actually use Swish activations. And of course, that is also not the end of the story. So let me, maybe, I don't want to spend too much time on that, but people keep doing that. These are experiments for yesterday. So I will publish this notebook as usual. These are the standard activations like threshold, logistics, sigmoid, hyperbolic tangent, and the ReLU. And then you have different leaky ReLUs, which are all the same on the right. You have exponential linear units, which is basically, again, a straight line on the right. And on the left is asymptotically going to somewhere curve. Then you have swishes, you have mish, which is a variant of swish, whatever, doesn't matter. And then, okay, let me skip that. And then you have this also pretty interesting function called the GLU, where G stands for Gaussian. And the Gaussian function is based on the cumulative distribution function of a standard Gaussian. So it also looks pretty much like a swish, but it's a little bit different. And again, so you can see the formula here. It's basically just the CDF of a Gaussian. And it's CDF of a Gaussian times X. And for some reason, it works better in many modern architectures. So I guess modern LLMs mostly use Chilo activations. Maybe there is a deep science behind it, but I'm just not an expert in that. I just wanted to mention that people are still working on ideas like this. But all of this is just... In a way, in this part, I just want to show you how all rabbit holes go deep. So wherever you look, you can find a long series of works. You can find a lot of different ideas. And for every idea, you will see some confirming experiments, of course, otherwise it wouldn't be published. Some may be even theoretical reasoning of why this idea is good. But then, you know, some ideas work out, some ideas disappear. And over here for activation functions, there was this like a different color. There was, I guess, the sequence of activations that you actually want to try is like ReLU, then Swish, then maybe GLU with the Gaussian linear unit, and maybe a Leaky ReLU as a variation. So that's where the field stands. Okay, don't want to spend more time on that. What I do want to spend a little bit more time on is, of course, backpropagation. So let me first motivate what we are going to talk about. And I know backpropagation is pretty simple, it's pretty straightforward, especially compared to what we've been talking about yesterday and the day before. But I still want to discuss it at least very quickly, because there is one or two points that I want to make in there. And also, well, I think it's worth reminding you about backpropagation. So, first of all, what problem are we solving? Where does backpropagation come from? Well, as we already discussed, a neural network is basically this huge function. So far, it's a small f, but this huge function, which computes, actually not even the output, but the function that computes the loss function for some input. So there are weights of the neural network. They constitute part of the inputs. There are inputs like the picture that we are classifying or whatever. This is x, and there is the correct answer, which is y. And the final output of a neural network on that would be the value of the loss function. So here it's still small l. Small l on x, y, and w, right? So, for example, if you are distinguishing between cats and dogs, what you actually do is this is your x, y is the cat class. So formally it's like, well, okay, since there are only two classes, let me just say it's one, as opposed to zero. If it was a dog, it would be zero. And then your picture, your input image goes through a very complicated neural network, and this very complicated neural network gives you, like, y hat, its prediction. And probably there was a logistic sigmoid at the end, as we discussed yesterday. But anyway, the output is y hat, which is like the estimated probability of the cat class, right? And then you can't take the gradient of that because you don't know where to go. To know where to go, you need to also combine it with the correct answer. And then here you compute the loss based on the prediction of your network and based on the correct answer. And the output in this case would be something like minus log y hat, which we are supposed to minimize so that y hat would grow and would be closer to 1. Minimize with respect to what? Minimize with respect to the weights. So this neural network has weights inside, the loss function probably doesn't have weights inside, but the neural network does have weights and we want to minimize it with respect to double. That's also not the end of the story, right? In machine learning, we don't have only one data point. We have lots of data points. We have a whole data set. So the actual loss function, capital L of W, now it's just of W, not of X and Y specifically, is something like the sum or the average. It doesn't matter, of course. We are just maximizing or minimizing. So it's the sum or the average of these small loss functions for every element in the dataset, right? So when we train, we are minimizing the average loss function on the dataset. Kind of makes sense. Maybe we have some weights inside. Maybe it's a bit more complicated. Maybe some samples are more important than others, whatever. For now, let's just stay simple. We want to minimize the total loss over the whole dataset. So we are minimizing this with respect to W. How do we do that? So I hope by now I've convinced you that this loss function is a very, very complicated function of W. I mean, we didn't even go into any architectures yet, but every architecture is also a huge composition of different stuff. But even in this formula, you can see that it's like a sum over the dataset. So it's a sum of a million terms, and every term is a pretty complicated function. So L of W is very complex. In practice, there are a lot of Ws. The length of the W vector is big. We are operating in high dimensions, almost inevitably. And L of W is hopelessly non-convex, is hopelessly complicated, and we definitely cannot hope to enumerate all possible Ws and look for the minimum or to do some complicated procedure here. Basically, almost all that we can do is to do some form of gradient descent. I will tell you later today why even slightly more complicated things fail. But basically, the only thing that works is to do gradient descent, which means update the weights locally with a rule like this one. So I want to make capital L smaller. So I am at point WK. On iteration K, I have the current checkpoint of the model and its weights are WK. So to get the next value of the weights, to get the next checkpoint, I subtract, I go in the direction opposite to the gradient. In the direction where the loss function decreases the quickest. I hope you know that already, right? So I want to go over here. I compute the gradient at point WK. And then I go slightly in the direction of this largest, of this most steepest slope downwards. This is the idea of gradient descent. We will see how it has evolved and where we are with gradient descent today. But the basic idea is still this. And what do we need to do to implement an iterative procedure like this to implement actual gradient descent? Well, if you look at the formula, you will see that the only thing that we really need to do is we need to be able to compute the gradient. That's it, right? After it's easy. So we need some kind of algorithm, we need some kind of procedure to compute gradients of big complicated functions. Well, we can't have a generic procedure for any function with however it is defined, but how is L defined? What do I mean actually physically when I say a big complicated function? Well, in neural networks, in deep learning, a complicated function is defined also as a computational graph, right? So what I actually have here is some kind of, so I have X, all of these different axes from the data set and the Ys and whatever. And they go into this impossibly complicated graph, but it's a directed acyclic graph that just does the computation from left to right. And we go through it and we can compute stuff. And then L falls out, right? So the assumption here is that this is a very big composition, but every element of this composition, every node in the graph is simple. It's simple enough that I can compute its values, compute all of the derivatives locally in this node, do anything I want inside this single node. Okay? So the single node is some kind of an elementary function. For example, this is a node, right? So it's just doing this dot product between two vectors. Very simple function. I definitely understand what the derivatives are, what the value is, blah, blah, blah. Or here is a node, an activation function, which is a fixed, known function of one variable, and of course I know it's derivative two. So I assume that my very complex function is computed through a computational graph of simple functions. And my task is, let's compute the gradient of this guy with respect to a part of the inputs. I didn't actually put the weights here, but they are also somewhere over here. And they're also part of the inputs for this computational graph. And I want to compute this at some specific point. So backpropagation is a way to do that. That's basically it. And to explain backpropagation, I think it's best to just go for an example. So let's, I don't know, you can give me some kind of polynomial of two variables. Usually that's enough. They give me an f of x and y. I don't know, some relatively complicated composition of simple things like pluses, squares, multiplications. I guess I'm not making myself clear what I want to see here, but something like, I don't know. Let's pull something out of x plus y squared times x squared plus y, plus xy maybe, something like this. It doesn't work too well. x plus y squared times x, okay, times x minus y plus y cubed or whatever. Let's put it this way. It doesn't really matter. So we have this kind of, okay, so for our example, we have this kind of function. And I write it as a formula, which means that I write it as a graph. Like we just discussed, it's a computational graph with elementary functions like plus, minus, squared, etc. So let me draw this graph. My question will be, I want to compute the gradient of f, so I want to compute df over dx and df over dy. That's the question. Let me draw the graph for you. I'm used to drawing it bottoms up, so here I have x and y. What do I do? I do a plus over here. I do a minus over here. x minus y, right? I do a cube over here. Then I do a square over here. Multiplication with the minus. And then I add the cube. Okay, so let me maybe go through this graph and put some letters here. So like, let's say a is x plus y. I want to denote the intermediate nodes here, the outputs of intermediate nodes. So b is x minus y. c is y cubed. d is a squared. Oh, perfect. e is d times b. And f, just like f, is e plus c. Okay, so notice what we've done. We've represented this function as a graph, which is exactly the same as a formula. When you write down a formula, you are actually writing down a graph like this one. And every single function in this graph is very, very simple. We know everything about taking the cube. We know what the derivative is. We know what the result is. Every function is simple. But we don't yet know, let's say, what is the global result of f. So what can we do with this graph? Well, first of all, we can use it to actually compute stuff. So we can, for example, let's say x is equal to 1, y is equal to, I don't know, minus 1. What will be the value of f? And we can go through this graph bottom-up, and compute every node, and we compute f, just like we would go through the formula, right? So in this case, a will be 0, b will be 2, c will be minus 1, d will be 0, oh, okay, it's too easy, but still, okay, e will be also 0, and f will be minus 1, okay. What else can we do? And this procedure, when we go bottom-up from the inputs to the output, this procedure is called forward propagation. So forward propagation or fprop is when you go from the inputs to the output, right? Bottom-up in this graph. And with forward propagation, of course, you can compute the value of the function. That's very straightforward. Interestingly, you can also compute derivatives with forward propagation. Isn't that right? So for example, let's say I want to compute df over dx. How do I compute df over dx while going bottoms up on this graph? Well, by induction, right? So I have the base of the induction which says dx over dx is 1, dy over dx is 0. Okay, now I go here and I say, oh, what is dA over dx? Well, since this is a plus, then dA over dx is dx over dx plus dy over dx. So it's 1 plus 0, it's 1. And so on. dB over dx will be 1 minus 0 will be 1. dC over dx will be 3 times y squared. Oh, sorry, I'm doing dx, it will be 0. I apologize. dC over dx will be 3y squared times dy over dx. And dy over dx is 0, so that will be 0. Now dD over dx is 2a times da over dx, right? And, okay, so let me maybe, sorry, let me change this example because all of these zeros will not be really interesting. So maybe let's say x is 2 and y is minus 1. So now here we have minus 1, here we have 3, here we have 9, here we have, oh sorry, here we have 1. I'm bad at arithmetic. Here we have 1, here we have 3, 1 times 3 is 3, and 3 minus 1 is 2. So we don't have a graph full of zeros. Okay, so dd over dx is 2a times da over dx, and da over dx is 1, so it's like 2a. So it's 2 times x plus y if you write down the formula. Then de, okay, so de over dx, let me write it down here, de over dx. E is a product, so how do you differentiate the product? It's d over dx times b plus db over dx times d, right? So that will be dd over dx is 2 times x plus y times b, which is x minus y, right? Plus db over dx is 1 times d, which is x plus y squared, okay? So this is going to be de over dx. Now df over dx finally, df over dx is just de over dx plus dc over dx, right? And we know all of these guys, so dc over dx is 0 and de over dx is this. So the answer is x plus y squared plus 2 times x plus y times x minus y. You can open the brackets, doesn't matter for us. Sounds about right. So if you just look at the formula and you do it in your head, it looks correct. Of course, in practice, you wouldn't be able to drag the formulas with you. So in practice, what you would actually do is you would compute the numerical values of these derivatives. So you would start with 1 and 0, and then here it's also 0. Okay, so here the formula and the value is the same. Here also 1 is both the formula and the value, and here also. But here you would not have a formula like 2 times x plus y, you would just have the numerical value. And actually what you would do if you were implementing it as an algorithm, you don't know x and y when you are inside this node. What you do know is a. You know this input that went here from a, and a was equal to 1. So we can just stop at this point and say that the derivative here is equal to 2. And similarly here, what we actually are computing is dd over dx, which is 2, times b, the value of b, which is 3. It goes here. Plus db over dx, which is 1, times the value of d, which is 1. So we'll get something like 7 here. And then we would add 7 and 0 and get 7, and I suppose that's correct. If I substitute 2 and minus 1, I get 6 plus 1, 7. So what have we done now? We have gone through the graph bottom-up, and we have only done it once. We don't need several passes, we just need one single pass. Yes, we do both when we go through the graph. We do both computing the functions and computing the derivative, everything over dx, right? But it's okay. We go through the graph, we compute these two things, and when we arrive at the end, we have both the value of f and the value of df over dx. So here is a question for you. I hope somebody is still with me, because I know this probably was boring. But here is a question for you. Why is that not enough? I just did a single pass through the graph and I got the derivative. Why can't I just use this algorithm? Why do I need backpropagation? What's the catch? What's wrong here? All the formulas are right. We did indeed get the derivative. But why can't we just use this approach? While you're thinking, I'll copy the graph because then we'll go to actually backpropagation. But why can't we just use forward propagation and be content with forward propagation? Okay, so we need gradients and we just got df over dx. We can do df over dy in the same way. What's the catch? I see. I knew that we need to repeat this even though we probably know backpropagation already. What's the catch? Why can't I just use this? Why do I need to invent anything else? Now I will proceed to backprop. I will tell you how to go from the end to the beginning of this graph. It will be slightly different. But why can't I use this? What's wrong with this? Theoretically, formally, we can, right? Everything is correct. We did get df over dx. And sure enough, we can do the same thing and get df over dy. No problem. So what is the problem if it's not in the formal correctness? How would we apply this algorithm to an actual neural network? What would be the procedure? So how would we apply this algorithm, this forward propagation derivative computing algorithm, to a real neural network or actually to any function? As you said, but for some reason didn't elaborate on it, we need the whole gradient as a result. In this case, we need both df over dx and df over dy. So this procedure, the one that I wrote down, gives you df over dx. How do I get df over dy? Well, I can go through the graph again, but this time I will compute. I will start with dx over dy, which is zero, dy over dy, which is one, and again go through the graph and get to f. And I will get df over dy, sure. Or alternatively, what I could do, I could compute this all in parallel. So as I go through the graph, I am doing everything at once. I am doing the values, I am doing dx, so d everything over dx, and I am also doing d everything over dy. That's also possible. Then I will only need one path, and during this one path, I will compute everything. But both of these approaches are completely impractical, you see. In a real neural network, how do we want to scale this up? For a function of two variables, it's fine. But how do we scale this up? When you scale it up to a real neural network, as I said, the length of the vector of the gradient is large. So modern neural networks may have billions of weights, at least millions for sure, right? So what does it mean to apply this algorithm to get a gradient over a million variables? It means we either need to go over the graph a million times, it doesn't sound good, or we go over the graph once, but in every node of the graph, we need a vector of size a million, because we actually do need all of these values when we go, and basically we need a huge amount of memory, we need a million times the size of the graph of memory to actually do this one over class. So neither of these actually works, right? As you probably understand, the networks are, the practical networks will be so large that they, maybe just one copy of them barely fits into your GPU, right? So, of course, you cannot fit a million copies of the neural network into memory to do this. And, of course, you can do a million passes over the network, but then it would take forever, right? So either the time doesn't work or the space doesn't work in this case. Fortunately, we can do it in a much better way. And that's what backpropagation is about. So backpropagation, Bprop, switches the question, switches, goes to the dual, I don't know, to the converse way of viewing this graph and to the inverse way of moving through this graph. So what did we do here in the straightforward approach when we go bottom-up? When we go bottom-up, we compute d everything over dx. So we get this sequence when we go through the graph of d every node over dx. And finally we get to df over dx. When you do it like this, obviously you need to do as much to get df over dy and so on. But what if, instead of starting from the inputs and doing d everything over dx, what if we did it the opposite? What if we start from top and we do df over d everything, you see? So we go, now the base of our induction is df over df, which is 1. And then what do we, for example, do here when we go to e? We say, all right, so what is df over de? Well, we only need to know locally how f is computed. So f is e plus c, so df over de is 1. Very easy. Here also df over dc is 1. Then it becomes a bit more interesting. So now what is, let's say, df? Okay, so here I want to put df over dd over here, right? And I write it separately, won't fit there. What is df over dd? Well, d goes to f only through e, right? So by the chain rule, as usual, df over dd is df over dd times d e over dd. So df over d is 1 and d e over dd is b. So it's 1 times b, right? And so on. So for example, so here I get b. Now let's say d, okay, what else? DF over DE, yeah, DF over DB is the next step, right? DF over DB is, again, B goes only through E, so it's DF over DE times DE over DB, and it's D, okay? DF over DA, again, A goes only through D, so it's D, okay, let me put it here, DF over DA is DF over DD times DD over DA, and it's, it's what, it's 2A times B, okay? So 2AB, and now comes the interesting part. So now I have DF over DA, DF over DB, and DF over DC, and now I need to compute, let's say, DF over DX, and X goes in two different things, right? So there are two outgoing edges here, which means that X is a part of A, which is then a part of F, and X is a part of B, which is then a part of F. So again, by the chain rule, it's really straightforward. I just need to add up the contributions, right? So DF over DA times DA over DX, plus DF over DB times DB over DX, that's it. So I know DF over DA, which is 2AB. DA over DX is one, right? This is straightforward. Plus DF over DB, which is B, times DB over DX, which is also one. So we got 2AB plus D. So this is 2 times X plus Y times X minus Y plus X plus Y squared, which is, I guess, correct. So we got the same result as before, right? DF over DX. But the beautiful part here is that without starting over, without re-computing everything that was happening above, we also can immediately get DF over DY over here, right? So now Y goes to three different things. Okay, let me, since you were not very quick to answer my questions, then let me write it down in a bit more detail. So DF over DA times DA over DY, right? Plus DF over DB times DB over DY, plus DF over DC times DC over DY. And what we get here? Well, DF over DA is two AB times one. DF over DB is D times minus one, right? DF DB over DY is minus one, so minus D. And DF over DC is one, but then we need to multiply by DC over DY, which is three Y squared. So we get like two times X plus Y time X minus Y minus X plus Y squared plus three Y squared. And I suppose that's also correct, right? If you go and look at this, yeah, obviously that's also correct. So notice the difference, right? Instead of going bottom up and computing D everything over DX and then, or in parallel, D everything over DY, thus doing a lot of unnecessary computations, we are going from top to the bottom and we are computing DF over D everything. And of course, these are two symmetrical approaches. They are dual to each other. They, it's, you can argue that it's basically the same, but neural networks are not symmetrical, right? You always have only one output because you want to, for example, minimize your output, right? You need to have a single function that you minimize. You cannot minimize several functions at once or a million functions at once. That doesn't work. If you have a million functions that you need to minimize, first, you need to compose them into a single function. So you always have only one output at the end and you have millions of inputs. So this approach scales well if you have lots of outputs and few inputs, then this is the proper way. But our situation is the opposite. In real neural networks, we have lots of inputs and one output. So we use backpropagation. Notice how, in this case, like what did we need to do these computations? I wrote down formulas because they are easier to follow than just numbers, because numbers don't mean anything. But in practice, of course, in actual computation, they would be numbers, right? This would be numerical values of these things. And so when you start out with df over df, of course, it's always one. But then, as we progressed through the graph backwards to compute, for example, df over dd, so what's happening? What gets transmitted on this edge? What gets transmitted from e to d? We needed not only df over d, which we got from above, but we also needed d over dd. And to compute d over dd, we needed the value of b. So we needed to know the values of these intermediate nodes. Again, it's all local. To compute this, I only need the nodes that go inside e. But I do need to know the values too, not only the derivatives. Because to compute the derivatives, I need to know the values. So in practice, backpropagation is not one pass through the graph. It's two passes. So how the algorithm actually works. First, you do forward propagation to compute values of intermediate nodes. And yes, you need to store them. So it's kind of like you need to store two numbers on every edge of this graph. And then backprop to compute df over d everything for every intermediate node. So that's backpropagation. And this is a very efficient and actually pretty straightforward way to compute gradients. And actually, if you look at any deep learning library like PyTorch that you will probably be using in practice in our class, if you look at any deep learning library, what you see is its basic operation, what it actually is supposed to do really, really well, its main job, is to do these two passes to the graph. So these are the key procedures, the key functions that the library needs to implement, and everything else is basically just syntactic sugar on top of that. So if you, I don't know, if you program in PyTorch, if you do the practical sessions of this class and you implement a new neural network, sure, you will see that PyTorch has thousands of classes with different layers, different kinds of components, and all of these components are only there, they are only needed to set up this graph. And these components can be relatively inefficient, it doesn't really matter. They are only run once and they don't do much, to be honest. What actually has to be efficient, what is the meat of everything, is computing the gradient along the graph. So I like to say that PyTorch and TensorFlow and whatever else, what they actually are, are automatic differentiation libraries. They are not... I mean, the deep learning is an afterthought. What actually has to be extremely efficient is the forward propagation and the backward propagation procedure. The rest can be done in any way. OK, what else do I want to say here? What else do I want to say? OK, forward propagation, backward propagation, example. OK, so while I'm thinking what else I missed, let me show you what I will also make available. I have some examples over here. So it's a different function, but something like what I just did on the board. And you can play with it. You can define a different computational graph and see how the values propagate through a network like this one, right? Oh, yeah. And also, just to circle back to how it actually applies to neural networks, notice that when you say, what is the input to a neural network? Your intuition, your default answer would be the input is X and Y, or actually only X. So if you ask what is the input of the neural network that distinguishes cats from dogs, well, that's an image. And that's true, right? So the default way to think of inputs is this. But if you think of the network as a computational graph, it has two different sorts of inputs. I think I already said that, right? So it has inputs that are fixed, that are always fixed, that we do not optimize. And these are like images, correct answers to the images and so on. These are the x's and the y's. And also there are the weights. And the weights, they are also inputs to the computational graph. They are not computed from anywhere. They are variables that appear in this huge, huge formula. And when we are doing training, when we learn, when we are doing training of neural networks, we are actually interested in gradients with respect to the weights. And so, yeah, if anybody asks, there are different kinds of inputs to a neural network, and the weights are also inputs. And when I was doing this example, there was no fixed input here. So I could have added a constant or something, but I mean, it wouldn't serve any purpose. Like x and y in this example are both weights, and we need to have a gradient with respect to x and y. All right, has this been clear? Did you already know this? Okay, so before the break, I guess I don't have too much time, so let me just maybe do a part of what I wanted to say about gradient descent. Specifically, let me motivate stochastic gradient descent and actually introduce it. And then after the break, we will discuss the actual algorithms of stochastic gradient descent. So here is a question. There are a lot of problems in deep learning, in practical deep learning, that come from the fact that we are using gradient descent. And we will discuss some of these problems in class. Of course, we don't yet see them. We are just on the beginning to look at this stuff. But basically, gradient descent is a pretty stupid algorithm. It's a first order algorithm. So gradient descent is a first order-- comes from the first order approximation to the loss. So I take L of W, and I say, well, OK, so right now, I am at point W_k. Let me do a Taylor series of L of W at point W_k. So I say, well, it's L of W_k plus W minus W_k times the gradient of L at point W_k. And gradient descent basically stops here. It just looks at this. It says, all right, so the gradient is the direction of steepest increase, therefore the opposite direction is the steepest decrease. Let's go there if you want to minimize. But we've had hundreds of years of optimization theory, right? So gradient descent could be done by, I don't know, Newton and Leibniz. And since then, we've had quite a lot of more involved but better optimization techniques, right? And the most straightforward idea, when you look at gradient descent like this, would be, well, what if we go one step further in the Taylor series? Why not? What if we also go to the second derivatives, w minus wk, that now there is a quadratic form in here, right? Times h inverse, not inverse, sorry, just h, times W minus WK plus something smaller. So now we are approximating, not by a surface, not by a linear surface, which, to be honest, is a pretty stupid idea for optimization. Well, I mean, it's not stupid in the sense that it can work, but it's stupid in the sense that it's naive. So if I'm looking at a complicated function and I'm trying to see, like, what is the derivative here, where to go, then all that the derivative tells me is that, well, you need to go here or you need to go here if we are in dimension one, right? And it doesn't tell you anything about how far you should go. And this is actually the main problem of gradient descent. This is what optimization theory to a large extent was about. It's a big topic. Like the gradient gives you the direction, but how far should you go along this direction? What should be the learning rate? What should be the step size? But if you go one step further, then what you are doing is you are approximating your difficult function locally with a quadratic surface. On here it would be a parabola, but with a quadratic surface. And now there are no equations anymore. You know where to go. You can go immediately to the minimum of this parabola, to the minimum of this quadratic surface. And it's a very simple formula, right? You look at this and you say, okay, I want to minimize this guy. So how do you minimize? Well, you take the gradient with respect to W. Okay, so what is going to be the gradient with respect to W? Let's say that, let me call this vector G, the gradient GK, the gradient at step K. And this is HK. This is the matrix of the second derivatives H because it's called the Hessian. And I take the gradient of the first part. This disappears. This disappears. There is just GK, right? And then I take the gradient of the second part. The two cancels out. And we get GK plus HK times W. And that's the gradient of this quadratic function. So it should be equal to zero. And I guess that's... Sorry, that's not it, of course. I forgot the first... I forgot HK times W minus WK, of course. And that should be equal to zero. So basically W is WK minus HK inverse times GK. That's it. And you can say that this is your next W. And you have no problem with the step size. And this procedure is far, far, far more robust, more stable. You will never or almost never go to some bad part of the search space. You will converge in far fewer iterations. Basically, it's better all around. And this is called Newton's method, by the way. Newton's method or second order optimization or second order optimization or whatever. So why can't we use Newton's method for gradient descent? Well, for Newton's method itself, the answer is kind of obvious. Because we cannot afford to do this computation, right? So, again, remember that w is a very, very long vector, right? It's like a million of numbers. It's a vector of size a million. So hk, the matrix of second derivatives, right? dL over dWi dWj is a matrix of size a million times a million. And we are supposed to compute this matrix, but more than compute, we're supposed to invert it. So of course, it's not going to work computationally, right? No question about this. But a more interesting question is, in optimization theory, in classical optimization theory, like in the 1960s, 1970s, 1980s, people also were thinking about this. There were no huge neural networks at the time, but there were functions to optimize, and there were difficult functions to optimize, and there were cases when second-order techniques were too difficult computationally. So there is this whole field of what is called quasi-Newton algorithms, quasi-Newton algorithms, and there are basically approximations to this. So the most famous such algorithm is called LBFGS, where L stands for limited memory, and BFGS are four last names, Fletcher, Boyden, Goldfarb, something like this. So it's a very famous algorithm. I won't go into details on how it works. It's definitely not relevant for us. But basically what it does is keeps an approximation to this kind of update and a very good approximation by only looking at the Ws themselves, W1, W2, and so on, and the gradient vectors. So like when you go from K to K plus 1, there is a procedure to update this approximate Hessean, approximate inverse Hessean. And this procedure is quick and it never deals with a million times a million matrices. Basically, it's a low-rank approximation, but let's not go there. So there are good ways to do something like the second-order technique without going actually to the second-order while only staying at the level of gradients and gradient vectors, and doing it in relatively low complexity. So why don't we do that in deep learning? And the answer is, again, we would be very happy to, and just as we would be very happy to use Newton's method, we would be very happy to do the second-order optimization, and we would be nearly as happy to do LBFGS for a neural network, but we can't. And here comes the interesting part. So why am I building up to this? So first, I wanted to mention second-order optimization, but also why doesn't an algorithm like this work? I didn't tell you what the algorithm is, but trust me, it only requires to know gradients at individual points, values at these points, and that's it in Europe. And the answer is, in deep learning, unfortunately, we cannot even apply gradient descent because we cannot even compute the gradient. Or, I mean, we can only compute it like once and not in every step. Why so? Well, for a very straightforward reason, and I actually already mentioned this reason. Where did I do that? I did it somewhere. Where did I mean? Yeah, here, right? So what is the function that we are actually minimizing in machine learning? The function L of W is like a huge average or a huge sum same thing of loss functions across the whole data set L of X, N Y, N, W You can think of it, by the way, usually as something like the negative log likelihood log P of or log posterior log P of W given X, N, Y, N to connect it to what we discussed yesterday and the day before but in any case your complicated neural network with a million weights leaves over here it computes the loss yes, but it computes the loss only on one training sample and to get the function that you minimize you need to go over the whole dataset so the actual honest-to-God gradient the actual GK would be a huge average of gradients of this loss function loss functions at point WK right and yes we can obviously compute every one of them but if I wanted to compute the true value of the gradient vector I would need to go over the whole dataset on every step which is kind of obviously impractical so yeah we will go over the whole dataset but maybe like once or twice not on every step of our optimization procedure that's not going to work so what is the actual setting how what is the problem that we are solving if I am telling you that we cannot even compute the function that we are optimizing right it's the same thing right we can compute the gradient because it's a huge sum and therefore we can't even compute the function itself because it's the same huge sum then what are we even doing well the answer is we are doing what is known as stochastic gradient descent I wrote I wrote all of these functions not as sums but as averages it doesn't matter for optimization but I wrote them as averages to make the following point you can view this loss function you can view the function that we are optimizing as an expectation over the data set over the uniform distribution over the data set of this small loss function so x and y here x and y are taken just uniformly at random from the data set right because well what is the expectation the expectation is the average weight with probabilities so if I take everything with equal probabilities I get just the average so our function is actually an expectation of a different function with respect to some of the variables with respect to x and y and I want to minimize it with respect to the other variables with respect to w when you have a problem like this this is what's called stochastic optimization and what is how can we do it if we cannot compute this expectation directly well there is basically always exactly one true way to approximate the expectation you take a sample and that's it so what we are actually doing in practice is on every step along the way we are taking not the gradient gk which is I mean the expectation is linear so it's the same thing it's the expectation of the gradients of l right but we are approximating the true gradient with let's say g hat k which is just the average over a small subsample of this 1 over let's say m times the sum gradient l of x i y i w so on every step along the way what we are actually doing and you probably already know this you just I just kind of think you never thought of it from this direction from this angle but the result you probably already know what we actually do when we train difficult complicated machine learning models we don't go over the whole data set to compute the loss we go through mini batches right and this mini batch formally it's a sample from the data set so what we are actually doing like mathematically what the meaning of what we are doing in stochastic gradient descent is we are approximating the true value of the gradient which is big and difficult with a sample sampled value of the gradient so on average if you take the average of this over the whole data set obviously you get the same thing so the the mean is correct and to be honest approximating the expectation with a sample is like one of the best things one of the best approximations ever it has all of the nice properties it converges it has it's unbiased it has lots of results known about it so it's as good an approximation as we can hope for and what we actually do in practice is we go on every step of gradient descent we sample a mini batch we take a small subset from the data set we compute the gradients on the subset and then we see what happens next and then we update the weights according only to the gradients on this subset you probably know this but now you can you can see what it actually means but even though this is a good approximation and even though indeed we will go to when we do stochastic gradient descent we do arrive at a good at the neighborhood of minimum etc etc we'll discuss it after the break what we actually get from SGD but it's still an approximation and in practice it's a pretty bad one I mean it's good theoretically but the specific numbers are like the size of the data set is in millions or more and the actual mini-batch size is like 4 or 8 maybe so the mini-batch size should be such that this many copies of the network would fit into your GPU memory and it's a small number the the data set is of course large so we are approximating the average of a million numbers by taking like 4 or 8 or even 1 number at random so of course mathematically it's the best we can do but it's still a pretty bad approximation it still has a pretty big variance and unfortunately this variance kills algorithms like LBFGS so since they are also doing approximations in order for those I can't explain without this whole separate lecture why but trust me since we are also doing approximations here in order for those approximations to actually work we need to have very good values of the actual gradients like true values or at least very good approximations we cannot just replace these GIs with sampled versions with huge variances and hope for the best the best will not come so it's it's an interesting and a very practical actually open problem for deep learning like can we do better can we can we maybe modify quasi-newton algorithms so that they are they will start working so that we can for example use stochastic gradients this sample estimates instead of true gradients and still go where we want to go this is unknown and probably we can't because lots of smart people have already thought about this and unfortunately no solution has come but of course stochastic gradient descent so now okay so now the actual formula of the update is this wk plus 1 is wk minus some learning rate times okay let me just call it times gk hat so times this sampled gradient I will call it sgd stochastic gradient descent and of course this is also not the end of the story this is the first natural step the simplest possible algorithm and of course there have been lots and lots of modifications and improvements of this idea so after the break we'll discuss those they also lie at the very heart of deep learning and for now are there any questions about sgd backprop okay if no questions then let's have a break and when we reconvene we go to sgd variations and algorithms that people actually use to train neural networks break let's let's continue so we stopped at the notion of stochastic gradient descent and I actually before I don't want to delve too deep into the theory of this stuff but I want to show you a couple of pictures and results about it before we actually proceed to to the new algorithms to variations of stochastic gradient descent so what actually happens in stochastic gradient descent you can actually analyze it and classical optimization theory has analyzed it in great detail and what actually happens like what is the correct way of looking at it so to speak well basically a lot of optimization theory was centered around this question so suppose that we are standing over here this is our wk and what does the gradient descent tell us well it tells us the direction where we are supposed to go right so we know that we are supposed to go in the direction of gk but we don't know how far we should go like do we stop here do we go all the way here or here we don't know it's only the direction not the end point so a lot of optimization actually a lot of optimization theory if you if you ever had a class on it or if you will have a class on it a lot of it centers on this one-dimensional optimization problem like we already know the direction and we are optimizing f of x we are let's say minimizing and at this point we already know that I want to go from x to the direction g right but I still don't know how far I want to go so let me treat this as a function of one variable and let me try to actually find the optimal step size let me actually try to find out how far I should go in this direction so it will still be an iterative procedure but hopefully we can say something about how far we should go so a lot of classical results like Wolff's rule or Micho's rule etc. etc. they are all about this kind of problem and we don't care about these results because they don't carry over to stochastic gradient descent that easily what does carry over? so what does classical optimization theory say about okay we discussed this so what does classical optimization theory say about stochastic gradient descent specifically? well SGD if you look at its trajectory if you look at how it works it actually works like this and I will make it precise in a moment but the picture is like this if you are optimizing a function you first go to the neighborhood of the minimum to the neighborhood of the optimum well it's a local optimum in general but this example is global doesn't matter so you go to the neighborhood of a n optimum quite quickly at first this is the initial part of these trajectories as you can see you go basically in the correct direction for a long time but then when you arrive you can't stop you can't converge or at least you can't converge by default so if you have a constant step size in gradient descent if you don't have a schedule of decaying atas down to zero then what's going to happen with stochastic gradient descent is it will go to the neighborhood of the optimum and it will then oscillate there back and forth because it cannot even recognize when it goes to the optimum itself because in the optimum the gradient is zero yes but we don't know the gradient we get a random sample of the gradient which will not be zero and then we will go out of the optimum and somewhere else so we can never know where exactly the optimum is but we can get to a neighborhood of it and then just go around this neighborhood due to our random sampling sounds pretty reasonable and if you do a little bit of math which I think I will skip it's not hard but just I don't think there is any point in us going through this if you do a little bit of math you arrive at an interesting estimate for like how long it's going to take and how stochastic gradient descent converges so this is the result the expected value of the function that we are optimizing at well not quite at xk this is xk head which is an intermediate point let's forget about the details basically after k iterations what we expect the function value to be what is its residue what is its difference with the optimal function value so we are minimizing the optimal value is lower but after k iterations we can expect to be pretty close to the optimum how close there is actually an answer there is a bound like this one so it's less than or equal to actually a previous slide should say less than or equal to r squared r squared is this guy it's the original residue it's how far we were from the optimum in the beginning so this is a constant basically it's fixed at the beginning of our optimization process and then there is this part which is more interesting so alpha i's are the step sizes right so on step size i we go to alpha i times g i we add this vector to alpha i times g i and here in the numerator we get the sum of the norms of this stochastic gradient squared times alpha i squared and in the denominator down here we get just the sum of alphas so if our stochastic gradients are bounded and probably they are even though they are stochastic then we can just plug in this bound whatever it is and we get this general form of the formula so this is exactly what explains the behavior of stochastic gradient descent because look suppose you have constant step size like we just did if we had constant step size let's say all alpha i's are equal to h then this splits into two terms and the first term is r squared over h which is basically over h times k which basically just goes to 0 pretty quickly as k grows we go from iteration to iteration k increases so k increases to infinity and the rest is constant so it goes to 0 and the second part is just constant so the first part depends on how far we were in the beginning and it goes to 0 which means that however far we were we will go close to the correct option on the other hand when we get there even when this part goes to 0 there is still the constant part over here which doesn't have k inside so it will remain a constant but of course this formula tells us more than that this is just a special case for the constant step size and this formula also tells us how do we choose alphas so that stochastic gradient descent converges and the answer is well if you want this guy to go to zero what is the easiest way to do it you want your denominator the sum of alphas to go to infinity and at the same time you want your numerator the sum of alpha squared to not go to infinity so the practical conclusion one practical conclusion from this formula is that if you want your stochastic gradient descent to converge and if you want it to converge to an optimum then probably you need to take alphas the step sizes you want to reduce them obviously otherwise you will never converge but how fast do you reduce them? what is the schedule of reducing them? well this formula gives you the answers you want to reduce them in such a way that the sum of alphas goes to infinity diverges but the sum of alpha squares does not go to infinity converges, right? so what would be the easiest example? the easiest example would be just alpha i if we go if we go back in our notation like eta k and we ask a question of how fast should eta k go to 0 then this formula gives you a possible answer like this I can do like eta k is something like 1 over k then the sum of eta k goes to infinity but the sum of eta k squared does not go to infinity and therefore stochastic gradient descent converges so it's just one possible answer and to be honest in practice this formula doesn't tell you much so it tells you this general convergence behavior but it doesn't really translate to like real, I don't know estimates on the size of this neighborhood for example because it always includes this g-squared and you can never know g-squared in practice it's bound on your sampled gradients so on like a sample of subsample of your data set which probably has a lot of variance so you don't know g-squared in practice but anyway it does tell you something useful about stochastic gradient descent but this is not really what I will be talking to you about now in the second part of our class what I am going to be talking to you about is a very different problem of stochastic gradient descent one second, sorry yeah, sorry so what I will be talking to you about is a different problem of stochastic gradient descent so let me show you what the problem actually is it's over here yeah so let me just let me first write down a very simple formula this okay, so we discussed SGD now let's say point number five is SGD improvements improvements and variations so what is the problem that we are solving what is an important problem of all of this of stochastic gradient descent let's consider the following example it's as simple as they come it's probably like the easiest optimization problem possible I will have a function of two variables x and y and it will look like this x squared plus a constant times y squared okay and I want to minimize it with respect to x and y so here sorry here is the function right the the contour plot of the function it's the very easiest problem the very easiest optimization problem possible right it's quadratic the minimum is at zero we immediately see that the minimum is at zero it's convex it goes to zero everything is great everything is fine right so very very simple problem however you want to look at it for example if you want to use Newton's method if you want to use the second order method you go to zero in one step because there is no approximation now the second order is just the function f but what does first order what do first order methods do how does gradient descent tackle this well it turns out that it depends a lot on the constant we shouldn't matter right but it does depend a lot on the constant so here I start with this constant so you can see that this is the function x squared plus rho times y squared and you can see that I begin with rho equal to one half so it's almost a circle it's like slightly elongated ellipse when it's almost a circle everything works works beautifully right so I tried a few learning rates and one okay so one over a hundred was a bit too slow and it didn't go all the way to zero that's fine of course I can choose a learning rate which is too slow that's in my hands but larger learning rates just went straight to zero it was all fine so there is absolutely no problem in actually sorry it shouldn't be SGD here it's just it's just gradient descent right there is no mini batch there are no mini batches nothing is stochastic here so let me fix that yeah so just regular gradient descent it goes straight to zero everything works fine but what if I start reducing row further what if it's now not 1 over 2 but 1 over 20 well what happens as I reduce row the coordinates become more like their scale becomes more different the coordinates become more imbalanced so for example here row is y changes 50 times slower than x so what does it mean for gradient descent it means that horizontally in terms of x it's exactly the same we go to 0 and we stay there no problem but in terms of y well now it takes a longer time to go to 0 right but while I am at the level of 0.05 it's still quite possible so but notice that like the the range of good learning rates begins to shrink right so before that for a more or less a circle it was fine unless I chose the learning rate like actively too low but now 0.1 is also kind of too low only 0.5 gets to 0 in 200 iterations which is quite a lot for such a simple function right and if I continue in this way then pretty soon everything will be too slow and here is the catch so you could say oh but why don't you just increase the learning rate of course for this function you should go faster but the point the problem is I really can't because okay I can go from 0.5 to 0.9 or even 0.99 and yeah it will get me a little bit closer to zero but I cannot go over one because if I go over one even a little bit then the x coordinate starts to diverge right because along the x coordinate the coefficient is still one so of course the problem is not that y changes slowly in absolute values that wouldn't be a problem of course the problem is that x and y are changing at very different rates x and y have very different scales and at this point even for something like 500-200 fold difference between them there's already no good learning rate for gradient descent even though it's so it either diverges or it just takes hopelessly long to go anywhere right so we can do 2,000 iterations then we will probably get there yeah okay with 2,000 iterations we will get there but 2,000 iterations of gradient descent for a quadratic function starting from 0.1 and 3 halves and going to 0 it doesn't make any sense right so here is the problem right when even even in very simple cases when the different variables in your optimization function in your set of variables when different variables begin to differ in scale when they begin to have different rates at which we should move along them everything kind of fails gradient descent cannot have a unified rate that we should do and I think yeah sorry this is the next step so this is the mostly this is the problem that we are solving and we will go through several different ideas that people had while solving it I will not this is not a historical lesson the ideas that we discuss are still real and useful so let's go through these ideas the first step the first idea okay so let me maybe maybe let's start with step zero I will set up the notation first because I will reuse it all the time so the notation is I go from x k minus 1 to x k okay so I'm optimizing something like f of x I have the vector x of variables and recently I went from x k minus 1 to x k I call this vector u k or u k u k minus 1 I think yeah so for the word update so u k minus 1 is x k minus x k minus 1 it's my last update and now I am at point x k and let's say I have a gradient g k here so at this point let's just assume that we are talking about stochastic gradient and this is not the true gradient this is the stochastic estimate or it could be a true gradient for what I'm going to tell you now it doesn't matter so there is a direction that the gradient tells you maybe it's a sample maybe it's the true one for what I'm about to say it doesn't matter but there is a gradient direction over here so classical SGD or GD or whatever would do it this way XK plus 1 would be XK plus some alpha times GK right so let me say that this is oh sorry minus right we are minimizing some minus so let me say that this is already minus alpha times GK minus alpha times GK and in the simplest example of SGD this is X plus 1 this is XK plus 1 and UK is just minus alpha times GK that's it so idea number 1 let's go over the ideas idea number 1 is called momentum momentum like like in school in high school physics right the impulse the momentum of motion what's the English word for that whatever okay so the the momentum which is like m times v in high school physics what how does it appear here well let's go back to our picture we had xk minus 1 and we just went to xk through a vector called uk minus 1 and there is a direction that the gradient wants us to go minus alpha times jk so the momentum method says well what are we really doing like what's the physical view of this what does it all mean well it looks like gradient descent looks like a bow rolling down some kind of a slope right it's like a material point and it's on a slope so it rolls down the direction where the gradient tells it to go in the steepest descent direction so so why don't we take this hint from regular Newtonian physics and why don't we actually apply it to how to say why don't we also add another physical thing from there inertia why don't we add this conservation of momentum here basically what this means is if your ball goes down the slope and the slope suddenly changes then for a while the ball will follow its current velocity right so it's going to have some momentum formally what it means is when I am here and I have come from here that's why I was drawing the previous update too I not only move along the gradient but I also conserve a bit of the previous update so I also add some gamma times u k minus one so this is the inertial motion I follow the already existing momentum and then so my final update will be the sum of these guys right so then I will go over here this will be x k plus one so now x k plus one is x k plus gamma times u k minus one we carry over part of the update minus alpha times u k so now this is u k okay so we keep a part of the momentum and actually in practice let me tell you right away that in practice we keep a very large part of the momentum so whenever you have anything momentum like gamma is 0.95 0.99 maybe even more so usually in practice you want to carry over a lot of the momentum there is little friction there should be some friction but not much and you just keep going in the same direction so what does it do why is it a good idea what it does is it keeps going forward along some direction keeps going forward along some direction and if the slope doesn't change in direction if we are still if the gradient still gets us to go in along in the same way then I will gradually go faster and faster right as the ball rolls down the slope it will roll faster and faster it will pick up speed and this is exactly what hopefully is going to happen over here I'll go to the picture later but hopefully what's going to happen over here so along the x direction the ball will go back and forth but then it will oscillate and stabilize in zero because in the x direction it's a steep slope and pretty soon we will go to the opposite part of the slope then back and back so if you imagine it as a ball actually rolling down this ravine then you will kind of intuitively see that that's what's going to happen but along the y-axis it will speed up right yes the slope is small yes y along the y-axis it's not steep it's shallow but it still goes and goes and you pick up speed as you go so this is the original motivation and the idea for the momentum approach and let me immediately tell you the next idea which is a small modification of the momentum approach a small but actually very very useful both theoretically and practically very very interesting modification the second approach is called Nesterov accelerated gradients you can see the acronym NEC sometimes or just Nesterov's method or something like that Yuri Nesterov was a Soviet mathematician who invented it sometime in the 1980s and Nesterov's idea is really simple and really great so let's go back to this picture I will not copy it doesn't matter but let's go back to this picture so what does the method of momentum tells us it tells us well we are here now and our next update has two components the gradient component and the momentum component so we stand over here we compute the gradient and we get both components and that gives us our update Nestor's idea is this wait okay so we are here and when we arrived here we don't yet know the gradient so we should be we should get to work on calculating gk right but wait but we already know the momentum part right so when we are standing over here after the previous update we already know a part and maybe a large part as I tell as I told you momentum can really pick up speed we know a large part of the next update already so why do we insist on computing the gradient over here why don't we go to this point which we already know it doesn't take anything to go there and calculate the gradient over there so this is negative alpha times let's say g prime k right the gradient computed at this point and then our new update will go here right so in Estorff's accelerated gradients xk plus 1 is xk plus gamma times u k minus 1 minus alpha times g prime let me write it down it's the gradient not w it's the gradient with respect to x of f not at point xk but at point xk plus gamma times u k minus 1 so in this intermediate and yeah not what I meant and this is the UK now yeah and this is the UK so what is like what is the motivation behind this well first of all there is some beautiful mathematics behind it and actually gradient descent with this method starts to even converge asymptotically faster it's some of the asymptotics change when you go from regular momentum estrous momentum but we will not go there the intuitive motivation is this Nesterov's gradients basically do like a look ahead they look forward in time and they appreciate they try to predict what's going to happen and they update based on the future not based on the present which is of course great so if we are on a slope like this right and a ball gets rolling down here so it picks up speed it speeds up and now it's here and the next step would put it over here right so in regular momentum you would continue speeding up because the slope is still in this direction so in regular momentum you would go even further up the opposite wall right but in this terms momentum you would look ahead over here and you would see that now the gradient points in the opposite direction so you are facing a wall in some sense so let's slow down say says urinester and that makes a lot of sense right so that's that's exactly that's exactly what makes it better and if we look at our example here now now I can show you that picture previously we're not old enough to see it but now if you look at this picture it's the same alpha but along with regular gradient descent I also put here gradient descent with momentum it's the orange line and gradient descent with Nesterov's momentum it's the green line and you can see how the oscillations along the x-axis are much much less or much better contained when Nesterov's momentum are used right so again this is the exact same effect because along the x-axis the slope looks like this and the ball the material point rolling down oscillates like this but Nesterov's momentum looks ahead and starts slowing down before the turn like a good driver not like material point so okay so this is what it looks like but of course the idea didn't stop there right and actually both the classical momentum method of momentum which dates back I think to the 1960s and nester of gradients which dates back to the 1980s they come from classical optimization theory they are not special to deep learning in any way but when you actually consider the same kind of problems but in the context of deep learning you see the following point so in deep learning all that we have been doing so far was kind of defined and contained in inside in just the generic Euclidean space of this vector x I'm trying to convey the intuition so like for the method of momentum all directions are equal it doesn't treat x1 the first component different from x2 different from x10 it will just add up some vectors in this space but it turns out that you can do even better if you treat different components of x differently if you for example pick a separate learning rate and a separate changing learning rate for every component of x when you do something like this it's called adaptive gradient descent or actually it's almost always stochastic because now we are in deep learning territory so it's called adaptive stochastic gradient descent and these kind of approaches are basically what we use in deep learning they are the optimization algorithms that you actually use in practice so let me walk you through some of them again it will be like a line of algorithms but they will culminate in ADEM of course and then but to get to ADEM we need to discuss some ideas along the way so adaptive SGD variations well the first variation called ADEGRED it was the original adaptive SGD version ADEGRED just literally means adaptive gradient the first variation worked like this the point was as follows what do we actually want for every direction in X like what kind of logic is behind choosing the learning crate and behind updating the learning crate the logic is this if you are on a shallow slope like this one and you basically go and go in the same direction then you should go quickly you should go fast right but if the slope becomes steep well it cannot be steep for long right if the slope becomes steep it means that the local optimum is close so if you land on a steep slope then you shouldn't carelessly jump further you should slow down and probably converge to the local minimum here so that's that's the idea how does adegret implement this idea well actually pretty simple so I will just write down the update rule x k plus 1 i so now we are talking about one specific component in the vector is x k i plus minus minus alpha over the square root of g wait for it g i plus epsilon g i k plus epsilon k i plus epsilon times g k i so it's still it's the same gradient it's the same vector of gradient but the learning rate is now adaptive and what is capital G well capital G is the sum of squares of these gradients so like G K I is G K minus one I plus G K I squared so the capital G accumulates all of the history of the gradients and if there are large gradients then capital G is large and if all gradients are small then it's small this kind of corresponds to our logic right this kind of follows it so while we are on a shallow slope while we should be going fast then we are going fast so we start with a large alpha with a high level high learning rate so at first we start off going quickly and then it goes down but while we are on a shallow slope gk is small and it doesn't go down that much so we are still walking quickly along this line then when we get to a steep slope it means that the current G is high and that means the capital G gets these high terms and it becomes large by itself so now the learning rate shrinks and we go slow that's the idea what is the obvious drawback of this idea what is like what cannot it do well I mean if you look at the denominator and how it's defined and epsilon doesn't mean anything it's just so that we don't divide by zero so epsilon is just a small number if you look at the denominator you see that it grows with time what it means is that once we have been on a steep slope there is no way for us to speed back up again right so if our optimization landscape looks like this we are screwed because we go fast then we get here we slow down but when it becomes shallow again we cannot speed up this denominator will never get smaller right so now we are doomed to going very very slow this is a bad situation for Edegrad so what's what's the solution the obvious modification would be to not use just the sum of gradients but to use some kind of recent history of gradients so if we've had recently high values of G then we go slow but if G has been for a while pretty small then we can speed up again right how do you achieve that well you could do something like a sliding window but sliding windows are very expensive right to have a sliding window you need to keep in memory the whole window which is impractical so instead of a sliding window what we are going to do is we are going to do I hope you know this trick if not then it's very good that I am telling you about it because it's a crucial trick in all of applied math and computer science exponential moving average EMI the exponential moving average basically does this let me write it in this notation right away so GKI is not the sum of G squared but it's like some coefficient gamma times the previous one plus one minus gamma it's a convex combination of the previous value and the new value so what this actually means is if you just keep opening the brackets right it's like GKI comes with this coefficient and then it'll be gamma times one minus gamma times the next GK minus one I squared and then it'll be gamma squared times one minus gamma times GK minus two I squared and so on right so it's like as we go further every value that we want to add up comes with an exponentially decreasing coefficient gamma of course should be less than one otherwise nothing good will come up and this kind of averaging has the properties that we want right so recent history is weight high recent history has big weights and something that happened long ago faraway history has exponentially small weights so we kind of forget about it with time and unlike a moving window we only need to store this value that's it so only one value per weight not a whole window of radius so much more efficient and if you take k-degraat and you replace capital G with this formula what you get is an algorithm known as RMS prop and it's also one of standard approaches to well it's also one standard approach to to to do in stochastic gradient descent right it was popularized by by Jeffrey Hinton at some time but of course we don't stop there right so this this is also not the end of the story now I will go to ADEM almost straight away but before I go to ADEM let me explain to you one more like angle of looking at it I think it's a pretty fun and instructive angle although the algorithm that results from it wasn't very good and it's not really used but the basic idea the motivation behind it I think is really nice so the motivation behind so the motivation goes as follows we already discussed gradient descent as kind of points rolling down surfaces blah blah blah etc etc so why don't we keep looking at it from this physics perspective why don't we actually keep realizing what keep pursuing this physical connection this metaphor of points rolling downhill because it's a very direct correspondence right it's the only difference is that both roll in continuous time and here we are in discrete time otherwise it's the exact same process so why don't we look at the measurement units of what is going on and what are the measurement units here well let's start with the gradient because that's it's easier it's much more natural to start there so I want my gradient to be like the velocity right my intuition is that derivatives are velocities they are speeds so let's say that I want my g to be measured in meters per second okay so g is like df over dx so this means that x is measured in seconds and f of x is measured in meters so the function is how far the point has gone x is the time that has elapsed and g is the velocity of the point okay so now that we understand this let's look at gradient descent and see whether it actually works so my gradient descent says okay I take my x and I update it like this x is x minus some constant times g what about the measurement units well x is measured in seconds x is measured in seconds this is just a constant dimensionless unit and g is meters per second so we are subtracting velocity from time which doesn't make any physical sense right and when I say it doesn't make any physical sense mathematically what it means so what it means for us in practice it exactly means that the scales of these variables can be very different so it can happen that your axes are large in absolute values and g is relatively small and in this case you would need like a huge alpha to adjust for that or it could be the other way around so the g is not scaled well to x it's our job to scale it basically and physically it means that the dimensions are wrong the units of measurement do not match okay so okay in the method of moments it's the same what happens in say Eidegrad in Eidegrad we have minus alpha divided by capital G times G something like this so what are the units over here seconds seconds meters per second and G capital G is small g squared so it's 1 over meters squared per second squared and squared so basically the units cancel out and we get that all of this is a dimensionless thing so now we subtract from seconds from time some dimensionless constant which also doesn't sound right okay and notice that Newton's method second order optimization does not have this problem this is also an important point here so if you recall that formula that we had about second order method something like x minus h inverse times g right so now let's look at the units here now x is in seconds x is in seconds g is in meters per second what is h? h is the matrix of second derivatives it's accelerations so it's meters per second squared inverse well there you go it cancels out and only seconds remain so now the units actually match and mathematically it means that Newton's method actually scales correctly it gives you the local step size that you actually want so this is well I mean it's not a reason it's just an illustration but this is one good illustration for why Newton while second order techniques are better right so their dimensions match they scale automatically and out of this out of this idea there came a method called A to delta which tried to do the proper units and basically it was A to grad but alpha here was multiplied by something like the square root of u and u was something like the sum of updates squared something like that it wasn't a very good algorithm it didn't catch up catch on so you don't have to study the delta but I think the basic idea is very interesting the basic idea of having of having the unit the measurement units of different things match and with that let's go to the real thing the algorithm that people still use quite often although there are alternatives now I'll mention them we won't go into the details of them but I will mention them but the most popular optimization algorithm in deep learning is ADEM and ADEM is actually pretty similar to what we discussed with slight modifications so it's like xk plus 1i is xki minus alpha divided by g k i plus epsilon so far it's more or less the same but times m k i not just g and let me explain what this means so g k i is an exponential moving average of squared gradients beta 2 times g k minus 1i plus 1 minus beta 2 times g i squared and m is an exponential moving average of the gradients themselves beta 1 times m k minus 1i plus 1 minus beta 1 times g k i itself and that's it so basically it's rms prop and the only difference from rms prop is that we also smooth out the gradients themselves so we are instead of using the actual instantaneous value of the stochastic gradient we are doing like this moving average over recent history so we are smoothing the gradients we are making them less we are reducing their variance we are making them less janky as we sampled different mini batches and this smoothing has an excellent effect it's what makes ADEM work so well so what else do I want to say about ADEM well yeah another thing about ADEM is that you really don't have to I mean it looks like it has a lot of hyperparameters you got beta 1 and beta 2 and also epsilon it looks like you need to choose them carefully etc etc which would be difficult but actually it's very robust you can just keep the standard hyperparameters that they recommended in the original paper I think it's something like this maybe 0.995 I'm not sure but something like that and epsilon is just a very small constant like this minus 8 or something like that and basically it works so you don't need to tweak beta 1 beta 2 and epsilon you can just take them off the shelf and it will be fine and ADM is a really good algorithm it's still used it's still pretty good I don't think I can actually illustrate it to you here on pictures because you see the whole point of adaptive algorithms is to treat different components of the vector differently right and they shine when you have like lots of high dimension and in this high dimension there are some dimensions that have this kind of behavior this kind of optimization landscape other dimensions that have that kind of optimization landscape etc. And I cannot do this in dimension 2. I cannot give you an example on a plane where x and y are wildly different and there is a big difference between ADM and RMS prop. Not going to work. I cannot give you an example like that. So you will definitely have examples like that in the practical part and here I can and as for the pictures I can just show you some nice pictures this is the problem again like this I can show you some nice pictures but they don't really mean anything so here is another like standard function that has been a test bed of optimization in classical optimization theory it's called Beale's function or Rosenbrock's function I mix up the two and it's basically let me find it somewhere it's basically a complicated polynomial here it is it's basically some complicated polynomial you don't have to memorize that it's just some kind of constants that are tweaked in such a way that it has an interesting optimization landscape so you have this minimum over here but around this minimum you have like this very steep slope over here you see how close the contour lines are to each other but then this steep slope suddenly becomes a very shallow slope so it's like it's easy to go quick down this slope but then you need to recognize that now it's shallow and you need to kind of speed up which some algorithms really cannot do so this is a good test example but in fact I don't think I can actually illustrate real difference between Adam and other adaptive variants so here is what SGD does SGD goes as you would assume goes in the correct direction unless it diverges completely of course you can always have your learning rate to be too high so that everything diverges but if it's not too high then of course it goes in the necessary direction and the faster you go the closer you get but if you go too fast you risk divergence so with SGD it's always about finding the best learning rate if you add momentum you have exactly the same effects that we discussed right so standard SGD goes and goes but it still has a long way to go SGD with momentum almost left the basin of this minimum it almost failed over here but thankfully it could come back but then it is optimum by far and as you can see it disappeared on the right and hasn't come back yet in 200 steps while Nesterov's momentum yeah it is already coming back it's still not here but obviously it's the best of the three so it's already coming back and it will be there soon and as for these algorithms that we discussed like SGD I the great delta well they kind of do better no real difference here so either delta is worse but also you shouldn't come to conclusions about this and either great and adem they just both do a good job over here so there is no significant difference but as an illustration again here is what optimization looks like in dimension 2 it's not a good guide to what optimization looks like in dimension 100 but unfortunately I cannot plot dimension 100 for we wrap up I think I have just a couple more things that I wanted to mention today so one thing is a version of ADOM it's the and again it's a version of ADOM that first of all is practical you can actually encounter it in deep learning practice it actually happens but But also, it comes from a very interesting motivation. So let me explain the motivation to you, and then I will mention this version. The motivation comes from a different way of doing regularization. When people did classical neural networks back in the day, back in the 1980s, back in the 1990s, regularization was usually done through this process called weight decay. So what is weight decay? What is the difference between regularization that we discussed yesterday and weight decay like this? In regular regularization, pardon the pun, you have like L of W being your loss function plus something like alpha times a regularizer. And then you minimize your loss function with a regularizer. That's it. So notice that regularization like this, like L2 regularization, L1 regularization, it's very, very easy to do in deep learning. Because all that you do is, it's a slight modification of the loss function. The algorithms don't have to change. Just your computational graph gets a couple more nodes and that's it. But in classical neural networks, they did it differently. They did it like this. So weight decay looked like this. When you go from, in your gradient descent, when you go from WK to WK plus 1, before adding the gradient, you multiply, you shrink the weights that you have. You multiply them by a constant less than 1. And then you add or subtract the current value of the gradient. Okay, so regularization, why is it called weight decay? Because weights decay a little, and then you do your gradient step. It looks pretty weird. And actually, pretty soon people realize that it's the same thing as SL2 regularization. When you do gradient descent, you can just... So let's just continue this formula, and let me write it like this. So it's Wk minus 1 minus gamma time Wk, right? I'm just pulling out the Wk itself, minus alpha times Gk. And what is Gk? Sorry. Gk is the gradient of L with respect to W at point K. So why don't I take this part and just put it down to the gradient here, inside the gradient. So now I have Wk minus alpha times the gradient of what? Of L. And here I have like some constant, 1 minus gamma divided by alpha, whatever that is, times just Wk times W times W, right? Just the norm of W squared. And I need to do it at point Wk. So when you look at it this way, you see that weight decay like this is exactly equivalent to just L2 regularization with a certain, with a certain constant. It's completely equivalent, it's completely the same. So people kind of forgot about weight decay, didn't use it at the beginning of the deep learning revolution. But then people realized at some point, also a pretty interesting idea, that, okay, so classical weight decay in regular gradient descent is exactly equivalent to L2 regularizer. That's true. But if you are doing something like ADEM, if you are doing some complicated thing with momenta and cumulative exponential moving averages of gradients squared and so on and so forth, then this equivalence doesn't hold anymore. Now there is no equality if the update rule is not that simple, if the update rule is actually, say, ADEM. So what people did at some point, they carefully worked this kind of regularization through ADEM, and they saw what to modify inside ADEM. It was actually a pretty simple tweak, but you had to do the math to see where it is. What to modify inside ADEM to make it more like weight decay than L2 regularization. And the resulting algorithm is called ADEM-W, and it's also a popular gradient descent variant. It's also a popular algorithm. So, okay, I think I should be stopping here. So let me just mention, I didn't plan to discuss them in detail, but let me mention that, of course, the research didn't stop on ADEM and ADEM-W. There are recently developed algorithms like Lion and Muon, and they have their own interesting properties. There is an algorithm, one of them, I keep forgetting which one, that was obtained by actually automated search, like the automated search that produced Swish, the Swish activation function, but for gradient descent algorithms, why not? The other uses special properties of transformers and is very useful for internal layers of language models, whatever. So the research continues, but still I think even in 2026, the standard algorithm would be something like ADM or ADM-W, or actually, still very useful, classical SGD. It's still a reasonable algorithm if you can tweak the learning rate. So in conclusion, let me just quickly go through the slides to see what I forgot. Okay, so this is our example. This is Nesterov's, this is Yuri Nesterov, for some reason downscaled a lot, blah, blah, blah. AdaGrad, AdaDelta, RMSProb, ADM, that's what we just discussed, NAIDM, okay, there is a version of ADM with Nesterov momentum called NAIDM. It's a version of ADM with Nesterov momentum called NAIDM, never heard about it afterwards, et cetera, et cetera. Then I will definitely skip this. So fixing weight decay regularization in ADM. This is ADM W. SGD with weight decay, ADM with weight decay, it has some good properties, which I don't have time to go into now. And let me finish, yeah, let me finish with these slides. Two last stories that both make the same general point. The first is the story of Superconvergence. Back in 2017, there was a very famous paper called Superconvergence that proposed to do a cyclic learning rate schedule. What it means is we slow down the training, we decrease the learning rate, and then at some point we speed it back up again. So we go slow, slow, slow, and then suddenly we rise up again and do a large update, and then we slow down again. And they showed in some very convincing experiments, of course there couldn't be any theorems about it, but they did some very convincing experiments, and they actually showed that they can converge to approximately the same results, not better, but the same results, but much, much, much faster. Like 10x, 20x faster. And it was all the buzz in 2017, but now you never hear about it. So cyclical learning crates are still a thing, but they are not universally accepted, and you probably are not going to use them in practice. This is one example. And the other example, also related to stochastic gradient descent, which is why I'm talking about these examples here. The other example is AMS Grad. It was a great paper. In 2018, it won ICLR 2018 Best Paper Award. It was a great idea. So they basically took the ADEM paper. In the ADEM paper, they had a convergence proof. They couldn't estimate the rate of convergence, but they had the proof that ADEM converges. And these guys found the mistake in the proof. And these guys showed counterexamples where ADEM can actually diverge, where it does not converge, where it doesn't work at all. Right? And what's even better, they could fix it. They proposed a small modification of ADEM called AMSGrat that basically replaces the sum with the max somewhere or something like that. The algorithm is in front of you. And for this algorithm, they could prove convergence, and the proof now was correct. So they found a mistake in ADEM, and they fixed it. And now, for eight years, we've had an algorithm which is probably better than ADEM. But my point is, unfortunately, nobody uses it. I've never heard about anybody using AMSGrat in practice. I guess you can use it. It's probably implemented in all the libraries. I guess you can try it. It'll probably be either exactly the same as ADEM or even worse. So let me close with this slightly disappointing point that even good ideas, even ideas that get confirmed by your experiments, that get confirmed even by theory. So the theory is correct. There is indeed a mistake in the ADEM paper. And this paper does not have a mistake. This paper did fix it. But unfortunately, it's not enough to get a new universally accepted algorithm. It's still practice is the final arbiter. Still, we as a field are very applied, a very practical field, artificial intelligence, deep learning specifically. So ultimately, people are going to use what works. And ADM still works. So with this, I want to stop for today. Are there any questions, comments, discussion? Okay, thank you. Yes, of course, I want feedback about the lectures. Thank you very much. I'm a bit surprised that gradient descent and backprop are new for you, but good. Then it's good that we repeated it. Okay, wonderful. Okay, thank you very much. And with that, I'm pretty sure you're tired of listening to online lectures for three days straight. I would be, definitely. So it's a good thing that I cede the floor to Alex, whom you will meet tomorrow, and we will have practice starting tomorrow. Thank you. Bye-bye. Sorry, a question? Yeah, sure. So next week, are we going to continue these online lectures at the start of the week? That is a good question. Yeah, so there are scheduling difficulties for me personally, because I'll be traveling next week. So I hope there will be a few lectures next week, but at this point, I cannot promise which days. Okay, so I think our plan for now is like tomorrow definitely is practice day. Tomorrow is our two practices, and then hopefully we will have one practice and one lecture on Friday, and then next week is wide open. I don't know about next week yet. Okay, thank you very much, and bye-bye. I will upload everything as usual. Bye-bye.
