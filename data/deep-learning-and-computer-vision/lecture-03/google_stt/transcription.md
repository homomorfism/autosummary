# Transcript — google_stt

- **Provider:** google_stt
- **Language:** en-US
- **Audio duration:** 3:15:11
- **Segments:** 1436
- **model:** latest_long
- **use_enhanced:** True
- **latency_sec:** 1611.93

## Segments

**[00:11 – 00:12]** Good morning, everyone.

**[00:13 – 00:15]** We continue.

**[00:16 – 00:18]** our investigations of machine learning and

**[00:20 – 00:21]** yesterday, we

**[00:23 – 00:42]** Finally got the neural networks. We got to our main topic of the class and we will we will be discussing neural networks for the rest of our time. But still I'm glad that we went over some fundamentals and I hope they have been interesting and attractive for you.

**[00:43 – 00:52]** so maybe just as a quick recap first, what we did here today and where we are right now,

**[00:55 – 00:55]** so,

**[00:56 – 01:03]** we are discussed yesterday, we discussed things like linear models, but basically

**[01:04 – 01:28]** Linear models or more complicated classical machine learning models like I don't know regression tree boosting or gaussian processes or some probabilistic models which some, I don't know, variational clustering or whatever. All of this models, followed classically. The same

**[01:30 – 01:57]** Pattern followed the same structure. So you have your high-dimensional input, like image is sound videos, whatever. Then you do feature extraction, right? That's we discuss that yesterday. Then you get something like a vector of features and then you do your ml model.

**[01:58 – 02:08]** Right? And the whole point and the email model. Now, gives you the output, which you need. It's the why. And this is the X.

**[02:09 – 02:09]** so,

**[02:10 – 02:18]** Classical models in classical machine learning, what people would do, they would think and do feature extraction menu.

**[02:20 – 02:58]** Are and the main advantage of deep learning when it came on in by now we have many more advantages but the main Revolution like the contents of the deep learning revolution of the plate, 2000 to 1010 was that this manual feature extraction, switched to end-to-end learning of a single model, which was the neural network, right? So, now in deep learning mostly, this is all a big neural network, right?

**[02:59 – 03:01]** and when we,

**[03:02 – 03:23]** When we implemented, when we run it it's just a single thing. We don't need to distinguish but inside of course there is like the first part, the main part that still does the feature extraction and then it produces the semantically relevant features, the features that are

**[03:24 – 03:44]** By virtue of training, the most meaningful features for the output that we want. And then we do the final layer, which is again, one of these linear models. Usually either linear regression if we predict a number or logistic regression if we,

**[03:45 – 03:56]** A dual classification as we actually usually do some somehow. It's it's rare to have numbers as outputs. We will have examples like that but it's not really common.

**[03:57 – 03:58]** so,

**[04:00 – 04:17]** Then what, what else we did yesterday, we started talking about the structure of neural networks, but the only started, and we only started talking about like individual Perceptions in individual. Artificial neurons.

**[04:17 – 04:24]** So and this this was I think where we stopped. We discussed the

**[04:28 – 04:37]** Common structure of a single unit in the neural. Net worth of the perceptron is a linear combination of the inputs.

**[04:38 – 04:40]** Followed by an online linearity.

**[04:41 – 04:43]** and,

**[04:44 – 04:45]** I think.

**[04:46 – 05:29]** Yeah, so I I think we didn't do yesterday, we didn't do like a real survey of this functions of activation functions, but it's it's a pretty short topic and let's just get it out of the way now. So what kinds of activation functions can be used in neurons? So, like again, we just discussed yesterday that the whole point of neural networks is to take structures like this to take small Elementary functions like this and then do like a computational graph based on them. Right. And

**[05:30 – 05:33]** when you do a computational graph based on,

**[05:38 – 05:40]** Elementary functions that.

**[05:41 – 06:15]** You understand Elementary functions that are easy? When you do compositions of easy things? Like we discussed with this connection isn't principle, which is basically just true when you compose a lot of simple things, you can get some very complicated results. Of course, the question is, how how do tweak your composition such a way that they? The result is what you want. And this is the whole point of deep learning, right? Training such big compositions, finding their weights, learning their weights.

**[06:16 – 06:16]** but,

**[06:17 – 06:23]** at least theoretically, as soon as you have any kind of nonlinearity here, you can

**[06:25 – 06:28]** more or less approximating anything you want.

**[06:29 – 06:41]** And so, our first topic for today, brief one will be, what are the nonlinearities that people actually use?

**[06:43 – 06:44]** and it's

**[06:45 – 07:07]** It's an interesting question. Actually it's like more a bit more interesting maybe than you would expect. So originally in, I don't know in 1943, in the regional McCullough, it's paper and a 1958 in France. Was perceptron people use threshold functions

**[07:08 – 07:26]** So the activation would be a threshold heavy side, step function called it what you want, but basically there would be an A and the rule would be, if W Times X is over a then 1 L 0, right?

**[07:30 – 07:44]** This is a fine function, if all you have is a single perceptron and it's okay, you can do a learning on this and everything more or less works and that's how the perceptron the original perceptron worked.

**[07:46 – 08:45]** But you can't really do networks of these guys. Right. So I told you yesterday that you can't do networks of linear perceptrons, because if the pressure transfer linear, then it doesn't make any sense to do a network. A composition of linear functions as linear again, so you just get your whole network equivalent to a single person. Well, with this guys, it's not true. Is this guy's there are like Universal approximation theorems. You can definitely approximate whatever you want, but you can't find this approximation unfortunately because the only way we have to train such big composition that's that will be our main topic for today. Actually. The only way to train such compositions is gradient descent and other techniques that are based on local movements of the weights, right? On on local properties of

**[08:46 – 08:46]** The last function.

**[08:47 – 08:53]** And when you have a piecewise constant, actuation function.

**[08:54 – 08:59]** Gradients don't work. I mean formerly they work but they're just equal to 0, right? They

**[09:00 – 09:29]** F Prime is equal to 0 here F. Prime is equal to 0 here. And when when you see it over here with your W Times X and you move to your W slightly, maybe you go here, maybe you go here but the answer doesn't change and the derivative is always zero and we don't know where to go, right? So this guy is definitely don't work for from Networks.

**[09:31 – 09:32]** So what did people do?

**[09:34 – 09:39]** People are looked at this threshold activation. They still had this idea that

**[09:42 – 10:04]** Threshold, activation is supposed to be good at threshold. Activation is like what we are actually trying to achieve. Like a neuron is either activated or not and we want to have a big composition of neurons that are in various states of activated or not activated.

**[10:05 – 10:12]** But we cannot have this straight jump, so let's have a soft approximation.

**[10:13 – 10:26]** so, for quite a while throughout all of this classical phase of early neural, networks up until 2011 or 12, I think mostly people used

**[10:28 – 10:30]** sigmoid activation functions.

**[10:32 – 10:40]** And when so when people say a sigmoid function, what they actually mean is that there is a

**[10:43 – 10:47]** There is an asymptote, a horizontal asymptote on the left.

**[10:48 – 10:50]** There is a horizontal asymptote on the right.

**[10:51 – 10:55]** And the function monotonically goes like this from negative Infinity.

**[10:57 – 11:21]** So they preverbal, the example, the archetype of example of a sigma, it is logistic Sigma which we discussed yesterday. So Sigma of a is 101, plus e to the power minus a, it goes from 0 to 1. It's a metrical, it's it doesn't have 0 derivative of anywhere. Etc, etc.

**[11:22 – 11:22]** and,

**[11:24 – 11:26]** so, there have been

**[11:27 – 11:33]** there was a lot of, there were a lot of neural networks in the 1990s 1980s with

**[11:34 – 11:36]** Activation functions like this.

**[11:36 – 11:48]** And also with other Sigma it's so I won't go into details. It doesn't matter for us now. But for technical reasons, it's not really good that your sigmoid saturates at 0.

**[11:49 – 12:03]** So it's, it's, it's a separate technical problem that you don't really want to like, approximate zero, so a better signal it for at least internal layers would be something that those from one to say, minus one.

**[12:04 – 12:26]** Right? And and then it would be symmetrical around zero actually. So, and actually more common sigmoid function for for neural networks for was the hyperbolic tangent, right? I always forget where the minuses are eight to the power, minus a minus

**[12:28 – 12:30]** Plus, I guess like this.

**[12:31 – 12:34]** so, it's the

**[12:35 – 12:37]** I guess it's like this. Yeah.

**[12:38 – 12:50]** So it goes to, it goes to one on positive, Infinity. It goes to minus here, right? That goes to minus 1 negative infinity and again it's symmetrical, blah, same kind of

**[12:51 – 13:00]** So, people were using this sigmoidal functions all the way through about. I don't remember the exact year, but about

**[13:02 – 13:04]** 2011, or 2012?

**[13:05 – 13:06]** and,

**[13:07 – 13:15]** in 2011 to 2012, there was a very influential paper, very important remark

**[13:16 – 13:25]** that where people try a completely different activation function. A very, very simple one and it turned out to work extremely well.

**[13:26 – 13:30]** so, the function that they tried is called ryloo,

**[13:31 – 13:33]** Which stands for rectified linear unit.

**[13:35 – 13:36]** and,

**[13:37 – 13:40]** Linear unit and it basically goes like this.

**[13:46 – 13:46]** on the

**[13:47 – 13:54]** Uh, so on, on the negative part of the inputs over here, it's just zero.

**[13:55 – 13:57]** and on the positive part, it's just

**[13:58 – 14:00]** X. It equals to the input.

**[14:00 – 14:26]** So I really of a is you can like formally. You can write it like Max of 0 and a or you can write it with one Boolean operator, right? So like one if a greater than 0 L. 0 that's it. Sorry not won a a greater than 0 L 0.

**[14:28 – 14:29]** That's it.

**[14:30 – 14:30]** and,

**[14:31 – 14:37]** It proved to be a very cool, very nice activation function.

**[14:38 – 14:48]** So what were, what are the benefits? Well, first of all, I just told you that it's now good to have.

**[14:48 – 14:52]** Piecewise constant activation functions because the gradients are 0.

**[14:52 – 14:56]** and indeed, if you go through a real,

**[14:59 – 15:07]** if you go through a neuron through a unit with real activation and you have a negative,

**[15:08 – 15:31]** Argument for you. So if you're W Times a false over here or W Times x Falls over here, then you don't learn anything right so it's just straight 0 it propagates a 0 and when you go back your gradient, stop there we don't have know what it means to go, but we will understand it just now just today.

**[15:33 – 15:34]** and, but

**[15:35 – 15:58]** But in this case, it's okay. So in in many architectures, it's okay to have this kind of sparsity, and it's even a good thing to have this kind of sparsity. So in, for example, conventional architectures, which we will discuss. I suppose in our next lectures in conventional architectures, you have the same ways to reuse a lot of times.

**[15:59 – 16:09]** All acrossed input. And when you have the same way, it's used all across the input. It's fine. And it's 7:05 to have like half of them. Just

**[16:10 – 16:11]** Zeroed out.

**[16:12 – 16:16]** So that that's not really a problem and it turned out that

**[16:17 – 16:23]** It's really a good property to have unbounded activations like this. So,

**[16:24 – 16:53]** With any kind of signal. It's you have this problem of situation, you have the derivatives of your activation function, go to 0 on the left and on the right here, the rest will go to their own, the left immediately. But on the right, they don't. And this means that this Sigma know Sigma, it can distinguish between like activated really to it and you producer activated, it just activated

**[16:54 – 17:15]** And what's even worse? When you go to this regime, when you're inputs, when you're sigmoid becomes, when you're neuron becomes, very sure and what it does when the arguments to the sigmoid become large and absolute value and you stop hearing, so your derivative are very close to 0 and the gradients just stop

**[17:16 – 17:25]** Here you explicitly stop on the negative side but on the positive side you never stop you just you keep learning which is also great.

**[17:26 – 17:35]** So in a way it's and there is even a mathematical result about this, I don't remember if you have it on the slides, maybe I do.

**[17:36 – 17:54]** You know, let me skip this situation functions. Yeah. And there is even a mathematical result that says well if you take a few Sigma it's and you stack them together, I can infinite series of Sigma and use them together. What you get is more or less.

**[17:55 – 17:56]** The real.

**[17:56 – 18:28]** So like, if you add up this series, of course, you don't get this exact ink at 0. Of course, it will be smooth, but then, it will very soon. Asymptotically, be just like that. It will go to straight line and it will stay being straight line. So, in a way, the real situation is like staking a lot of Sigma. It's and looking how many of them actually activate which is, of course, more information, right? So this this this is a good thing.

**[18:32 – 19:31]** What else do I want to say here? Yeah, so oh, and there is yes. Sorry about the Russian on the picture. But there is also a very interesting remark here. That connects back to what we discussed yesterday about the brains actually, if you look at how our biological neurons activated, it does look like a real activation function. So this is like a good model or whatever of, of the firing rates of neurons, basically of their activation strength. How well how, how much their excited. And it looks like this black curve over here. So at first, so it doesn't go negative of course. But then from 0 for a while, just state stays known inactive not activated at all. Then there is this complicated phase transition, but after the complicated phase transition.

**[19:32 – 19:33]** We basically get a straight line.

**[19:34 – 19:35]** Which is.

**[19:36 – 19:44]** Pretty cool. I mean, it's it, it's pretty interesting and expected. It would be actually a straight line but looks like it is

**[19:45 – 20:14]** Are of course, it doesn't go to Infinity. Please do not experiment with that. Know, if you apply 1,000 volts to your brain, you will not think faster and better and this will not end well, do not do that. Of course, it's actually it's in real life and biology, but in the computer doesn't have to situate or at least it. We can stretch this straight line, however far we want.

**[20:15 – 20:38]** So and of course, this are just additional considerations this. These are, this is just, this is just some interesting facts. About the real, of course, the real bonus was that it worked very well. So in practice as soon as people, it wasn't a new idea, real activation existed since 1976 or something. But

**[20:41 – 20:55]** as soon as people tried them, with real networks, with convolutional networks special and they saw the results in about 2011, to 1012 are mostly everyone's finished the rules.

**[20:57 – 21:07]** Of course, it did not stop there. So there has been a lot of further restoration activation functions. There have been interesting results. So

**[21:08 – 21:11]** What what what was what was the next step?

**[21:12 – 21:12]** Well.

**[21:13 – 21:14]** The first.

**[21:15 – 21:22]** Next Step was kind of straightforward. So I said that in some

**[21:25 – 21:32]** In some situations, it is desirable to have this participant in some situations. It is a good thing to

**[21:34 – 21:54]** It is a good thing to zero out some of the activations over here, but in other situations it's not. And when you don't want to lose the gradient flow through your network, when you don't want to be sparse, then of course you you'd want something non-zero and the left.

**[21:55 – 22:01]** So the immediate modification was what we call a leaky real.

**[22:02 – 22:24]** Basically the same thing, but on the left, you have a straight line. But it's it's a straight line, which is, which has a smaller slope and on the right. So it's still just a single hinge, a connection of two straight lines, but at 0, but now it's non-zero on the left.

**[22:25 – 22:28]** are, and then, and then,

**[22:29 – 22:49]** What people did at around 2017? I think was this, they they ran an automated search for the best possible activation function. And I do want to discuss this a little bit because we will see examples like that later also.

**[22:50 – 22:51]** so, if you look,

**[22:52 – 22:54]** At your activation functions.

**[22:56 – 23:06]** What are they like, what is their nature? They are just straightforward. Mathematical functions of one variable, right? Just a function in the high school sense of the world,

**[23:07 – 23:07]** and,

**[23:09 – 23:23]** What is the representation of this? How do you represent functions? How would what is the structure of this, guys? Well, their defined by formulas, right? And what is a formula formula is a computational graph

**[23:24 – 23:26]** so, for example, how does

**[23:27 – 23:35]** Real. Look, what does real look like? Oh, you have your input X. You have a constant zero

**[23:36 – 23:37]** And then you have a maximum.

**[23:38 – 23:39]** And you have your output.

**[23:40 – 23:46]** Okay, very simple computational graph, two inputs, one of them constant and that's it.

**[23:49 – 24:17]** What about the logistics segment? Well, you have X, you have one. You have, for example. And I mean, I'm just making an example. You can Define functions in different way, but for example, here, there is a urinary function, e to the power minus argument. And then there is plus one, and then there is the inverse, right? Go one over. And as a result, you get Sigma effects.

**[24:20 – 24:34]** For a hyperbolic tension, you have X, you have e to the power, you have it to the negative power and then you subtract and then you add and then you divide.

**[24:35 – 24:40]** And you get your hyperbole attention, right? And so on. So a function,

**[24:41 – 24:52]** if you write it as a formula, what the formula actually is, what what is a formula, is a mathematical object, that's a graph. It's a graph, composed of Elementary functions of operations, that constitute this form.

**[24:53 – 24:56]** are and which, which means that you can

**[24:58 – 25:07]** Sweep over this graphs, right? You can search through these grows. I won't go into details on how exactly people do it. It doesn't matter for our class, but basically,

**[25:09 – 25:28]** At some point, they ran a very expensive search over a lot of graphs. A lot of activation functions like this. Of course, when you do a search like that, you cannot actually prove anything. There is no mathematical statement, it's all empirical, right? So you just try different stuff.

**[25:29 – 25:46]** You see what works better on the set of data sets set of architectures that you that you set up. And then you just see what works better, right. And you see what works better and you.

**[25:47 – 26:14]** Progress by mutating the graphs a little bit. It's basically an evolutionary thing. Usually because you can't take a gradient on the graph structure. So you need to do like crossover, like, copying parts of one graph to the other or small mutations, like, change around things. See what works. Go to the population of things that work, etc, etc. It's it enabled us.

**[26:15 – 26:57]** Um, and as a result at that point, they came up with something called The Switch activation function. Yeah, 2017. It was done by Google, of course, whales would have all of that compute back in 2017. And this fish activation function. I mean I cannot explain to you why it is better. I can only show it to you and say that the empirical it's better. So it looks kind of like a leaky real or so it's very similar to real on the right and they are all very similar to real on the right and on the left it at first goes like this, but then it goes back to 0 so it's not monotone interesting.

**[26:58 – 27:06]** and yeah, it proved the work better for some reason and

**[27:07 – 27:22]** a lot of standard architectures is in computer vision. Actually, you will see if you go inside. We won't go to that level of detail thinking class, but if you go inside, will see that a lot of standard architectures actually use swish activation.

**[27:24 – 27:39]** And the course that is not the end of the story. So, let me maybe, I don't want to spend too much time on that but people keep doing that. Yeah, this is our experiments for

**[27:41 – 28:13]** Ah, yesterday. Yeah. So I I will publish this an old book as usual. These are the standard activations like threshold Logistics Sigma hyperbolic tangent and the reload and then you have differently careers which are all the same on the right. You have exponential linear units which which is basically again a straight line on the on the right. And on the left this asymptotically going to somewhere curve.

**[28:14 – 28:19]** Then you have switches, you have Mich, which is a variant of fish, whatever doesn't matter.

**[28:22 – 28:36]** And then, okay, let me skip that and then you have this all. So pretty interesting function called the glue which where she stands for gaussian and the gaussian function is based on the

**[28:38 – 28:41]** Cumulative distribution function of Central Coast.

**[28:42 – 28:47]** So, it also looks pretty much like a swoosh.

**[28:48 – 28:48]** but,

**[28:50 – 29:03]** It's a little bit different and again, so you can see the, the formula here. It's it's basically just the CDF of gaussian and

**[29:06 – 29:11]** It's CDF from gaussian times x. Yes. Sorry and it's

**[29:14 – 29:33]** For some reason, it works better in many modern architectures so I guess modern Netherlands, mostly use chill work durations. They're probably maybe there is a deep science behind it, but I'm just not an expert in that just wanted to mention that people are still working on ideas like this.

**[29:35 – 29:36]** Okay, so

**[29:37 – 30:07]** But all of this is just and in a way, just in this part. I just want to show you how that all rabbit holes go deep, right? So wherever you look, you can find a long series of works. You can find a lot of different ideas and for every idea you will see some confirming experiments. Of course. Otherwise don't be published. Some may be even theoretical reasoning of why this idea is good.

**[30:08 – 30:36]** But then you know some ideas work out some ideas disappear and over here for Activation functions there was this like use a different color. There was I guess the the sequence of activations that you actually want to try is like really then swish. Then maybe gilu with the gaussian linear unit and maybe a leaky real is a variation.

**[30:37 – 30:40]** So let's let's get very difficult stands.

**[30:40 – 30:42]** Okay, don't want to spend more time on that.

**[30:44 – 30:49]** what I do want to spend a little bit more time on is

**[30:50 – 30:53]** of course, that propagation.

**[30:53 – 30:54]** so,

**[30:55 – 31:22]** Let me first motivate what we are going to talk about and I know back propagation is pretty simple. It's pretty straightforward. It's a specialty compared to what we've been talking about yesterday and the day before. But I still want to discuss with at least very quickly to because there is one or two points that I want to make in there and also well

**[31:22 – 31:27]** I think it's it, it's worth. Reminding you about back propagation?

**[31:28 – 31:28]** so,

**[31:30 – 31:36]** First of all, what problem are we solving? Where where does back propagation come from?

**[31:36 – 31:40]** Well, as we already discussed.

**[31:41 – 31:44]** Sorry, as we already discussed.

**[31:44 – 31:50]** A neural network is basically this huge function.

**[31:51 – 32:34]** Let's guess so far, it's a small left, but this huge function which computes actually not even the output but the function that computes the loss function for some input, right? So there are weights of the neural network, this, they constitute part of the inputs. There are inputs, like, like inputs inputs, like the, the picture that we are classified or whatever this is X, and there is the correct answer, which is why. And the final output when neural network on that would be the value of the Lost function, right? So here, it's still smaller.

**[32:36 – 32:44]** Small L on our x y w, right? So for example, if you are

**[32:47 – 33:05]** Distinguishing between cats and dogs. What you actually do is this is your X Y is the cat class. So it formally it's like well. Okay, since they're only two classes, let me just say it's one as opposed to 0. If it was a dog it would be 0.

**[33:06 – 33:07]** and then,

**[33:08 – 33:52]** Your picture, your input image goes through a very complicated neural network and this very computer complicated. Neural network, gives you like why hat? It's pretty dictionary. And probably there was which is logistics sigmoid at the end as we discussed yesterday. But anyway they output is why hat which is like the estimated probability of the cat class, right? And then you can take the gradient of that because you don't know where to go to know where to go. You need to also combine it with the correct answer. And then here you compute the loss based on the prediction of your network. And based on the

**[33:53 – 34:12]** Uh, based on the correct answer and the output. In this case would be something like minus log, y hat, which we are supposed to minimize. So that y hat would grow and would be closer to one, right?

**[34:14 – 34:26]** Minimize with respect to what minimize with respect to the weights, right? So this neural network has weights inside. The loss function probably doesn't have rates inside but the neural network does have weights and we want to minimize it with respect to double.

**[34:28 – 34:57]** And that's all not the end of the story, right? And in machine learning, we don't have only one data point. We have lots of it data points, we have a whole data set so the actual was function like L capital, L of w. Now, it's just of w naught affects and why specifically is something like the sum or the average? Doesn't matter? Of course, we're just maximize or minimize in. So it's the sum or the average of this small loss functions for every

**[34:59 – 35:05]** Element in the data set, right? So when we train

**[35:06 – 35:07]** We?

**[35:08 – 35:14]** Are minimizing the average loss function on the dataset.

**[35:14 – 35:28]** And it makes sense. Maybe we have some weights inside, maybe it's a bit more complicated. Maybe some samples are more important than others, whatever. For now let's just stay simple. We want to mix the minimize the total loss of over the whole dates.

**[35:30 – 35:33]** so, we are minimizing this with respect to the

**[35:35 – 35:36]** How do we do that?

**[35:37 – 35:45]** So I hope by now, I've convinced you that this loss function is a very, very complicated function of w.

**[35:46 – 35:55]** I mean we didn't even go into any architecture here but every architecture is also if you composed of different stuff but

**[35:57 – 36:07]** Even in this formula you can see that it's like a sum over the data set. So it's a sum of million terms and every term is a pretty complicated function.

**[36:09 – 36:11]** so, L of w is

**[36:12 – 36:13]** Very complex.

**[36:14 – 36:26]** In practice, there are a lot of WS in the length of the W. Vector is Big. We are operating on high in high Dimensions almost inevitably and

**[36:28 – 36:29]** um,

**[36:30 – 36:30]** sorry.

**[36:31 – 36:31]** Yeah.

**[36:32 – 36:33]** and,

**[36:35 – 36:57]** The L of w is hopelessly, non-convex, is hopelessly complicated. And we definitely cannot hope to. I don't know. Enumerate. All possible W's. And look for the minimum, or to do some complicated procedure here basically,

**[36:58 – 37:06]** Almost anything. Almost all that we can do is to do some form of gradient descent.

**[37:08 – 37:25]** I will tell you later today, why even slightly more complicated things fail, but the only base, basically, the only thing that works is to do gradient descent, which means update the weights local there.

**[37:26 – 37:30]** With a role like this one. So I want to make

**[37:31 – 38:17]** I want to make a capital l smaller so I am at point w. Okay. On iteration K have the current checkpoint of the model and its weights are WK. So to get the next value of the weights to get the next checkpoint. I subtract I go in the Direction slide, oh, slide I go in the direction opposite to the gradient. So, in the direction, where the loss function, decreases, the quickest, I hope, you know that. All right, all right, so I want to go over here. I compute the gradients, the gradient at Point WK. And then I

**[38:18 – 38:27]** Go slightly in the direction of this. Largest of this most steepest slope downwards. This is the idea of gradients.

**[38:28 – 38:34]** And today we will see how it has evolved and where, where we are with creating the center today. But

**[38:35 – 38:37]** The basic idea is still this.

**[38:38 – 38:57]** And what do we need to do to implement an iterative procedure like this Implement actual gradient descent? Well, if you look at the formula, he will see that. The only thing that we really need to do is we need to be able to compute the gradient. That's it right after it's easy.

**[38:58 – 39:02]** So, we need some kind of algorithm, we need some kind of procedure.

**[39:04 – 39:08]** To compute gradients of big complicated functions.

**[39:10 – 39:23]** Well, we can't have a generic procedure for any function with, however, it is defined. But how is L defined? Like, what is, what do, I mean? Actually, physically, when I say a big complicated function,

**[39:24 – 39:33]** well, in neural networks, in deep learning a complicated function, is defined also as a computational graph

**[39:34 – 39:38]** Right. So what I actually have here.

**[39:39 – 39:53]** Is some kind of. So, I have X all of this different texts from the data set, and the wise and whatever. And they go into this impossibly complicated graph.

**[39:54 – 40:03]** But it's a directed a cyclic graph that just does the computation from left to, right? And we go through it and we can compute stuff.

**[40:04 – 40:06]** and then,

**[40:06 – 40:07]** L.

**[40:08 – 40:09]** It falls out, right?

**[40:10 – 40:15]** So, the Assumption here is that this is a very big composition.

**[40:16 – 40:22]** But every element of this composition, every note in the graph is simple.

**[40:24 – 41:01]** It's simple enough to take in compute, its values compute, all of the derivatives locally in the node. Do anything I want inside the single node, okay? So the single note is some kind of an elementary function. For example, for example, this this is a note, right? So it's just doing this dot product between two vectors very simple function, I definitely understand what the derivatives are, what they really is blah or here is an activation function which is a fixed known function of one variable. And of course I know it's derivative to

**[41:02 – 41:09]** So I assume that my very complex function is computed through a computational graph of simple functions.

**[41:10 – 41:12]** And my task is.

**[41:13 – 41:22]** Let's compute the gradient of this guy with respect to a part of the inputs. I didn't actually put the weights here but they are also

**[41:22 – 41:29]** Somewhere over here and they're also part. They're also part of the inputs for this computational graph.

**[41:29 – 41:34]** And I want to compute this, add some specific point numerically.

**[41:37 – 41:45]** So bad propagation is a way to do that, that's basically it and to explain back propagation. I think it's best to just

**[41:46 – 41:48]** go for an example.

**[41:48 – 41:49]** so, let's

**[41:50 – 41:59]** I don't know, you can, you can give me some kind of, you know, polynomial of two variables. Usually, that's enough. Give me an f of x and y.

**[42:00 – 42:02]** and some

**[42:03 – 42:10]** Relatively complicated, composition of of simple things like classes, squares, multiplications.

**[42:14 – 42:15]** I guess I'm not.

**[42:16 – 42:23]** Making myself clear. What what I want to see here but something like and okay, let's pull something out of

**[42:26 – 42:29]** X Plus y Square now times.

**[42:30 – 42:32]** X squared plus.

**[42:39 – 42:39]** Why?

**[42:40 – 42:48]** Plus X Y, maybe something like this and it doesn't, that's doesn't work too well, X Plus y squared times.

**[42:49 – 42:51]** X.

**[42:53 – 42:58]** I okay times x, minus y, plus y.

**[43:00 – 43:18]** Cubed or whatever. Let's, let's put it this way. I doesn't really matter. So we have this kind of. Okay, so for our example, we have this kind of function and I write it as a formula which means that I write it as a graph, like we just discussed as a computational graph with Elementry functions like plasma squared Etc.

**[43:20 – 43:20]** and,

**[43:22 – 43:24]** So let me draw this graph.

**[43:25 – 43:37]** Yeah. And my question will be, I want to compute the gradient of f. So I want to compute DF over DX and DF over d y. Okay, that's that's the question.

**[43:40 – 43:42]** Let me draw the graph for you.

**[43:43 – 43:48]** So I have. I'm used to drawing it. What comes up? So here I have X and Y.

**[43:49 – 43:57]** What do I do? I do it. Plus over here, I do a minus over here. X minus y.

**[43:58 – 44:03]** Right, I do a cube over here.

**[44:04 – 44:06]** Then I do a square over here.

**[44:08 – 44:13]** Multiplication with the minus and then I add the cube.

**[44:14 – 44:15]** Okay.

**[44:17 – 44:34]** So let me maybe go through this graph and put some letters here. So, like let's say a is X Plus y. I want to denote the intermediate notes Here. The outputs of intermediate notes. So, B is x minus y.

**[44:34 – 44:36]** C is y cubed.

**[44:37 – 44:40]** D is a square.

**[44:41 – 44:46]** Oh perfect. E is D times B.

**[44:47 – 44:52]** And F just like f. Right is e plus C, Okay? So

**[44:55 – 45:03]** Notice what we've done, we've represented this function as a graph, which is exactly the same as a formula. When you write down the formula, you are actually

**[45:04 – 45:10]** All right. Now a graph like this one and every single function in this graph.

**[45:11 – 45:21]** Is very, very simple, right? We know everything about, you know, taking the cube. We know what the derivative is, we know what the result is, every function is simple,

**[45:22 – 45:28]** But we don't yet know, let's say, what is the global result of f?

**[45:29 – 45:31]** So, what can we do with this graph?

**[45:32 – 45:51]** Well first of all we can use it to actually compute stuff, right? So we can for example I don't know let's say x is equal to 1. Y is equal to I don't know minus 1. What will be the what what will be the value of?

**[45:52 – 46:14]** And we can go through this graph button up and compute every note and we compute. If just like we would go through the formula, right? So in this case, a will be 0. B will be two, will be minus one. D, will be 0, okay? So easy, but still okay. He will be also zero and there will be minus one.

**[46:14 – 46:15]** Okay.

**[46:17 – 46:27]** What else can we do? And this procedure, when we go bottom up from the inputs to the output, this procedure is called forward propagation.

**[46:28 – 46:30]** So, forward propagation.

**[46:31 – 46:32]** Or.

**[46:33 – 46:34]** F probe.

**[46:35 – 46:41]** is when you go from the inputs to the output, right, but bottom up in this graph,

**[46:42 – 46:47]** And with forward propagation, of course, you can compute the value of the function, that's very straightforward.

**[46:49 – 46:49]** Interestingly.

**[46:50 – 46:54]** You can also compute it. There is for propagation.

**[46:55 – 46:55]** Isn't that right?

**[46:56 – 46:57]** So, for example,

**[46:59 – 47:02]** Let's say, I want to compute DF over the X.

**[47:03 – 47:08]** How do I compute jfa for DX while going Bottoms Up on this graph?

**[47:09 – 47:10]** Well.

**[47:10 – 47:20]** By induction. Right? So I have the base of the induction which says the X over DX is one d. Y over DX is 0.

**[47:21 – 47:26]** Okay, now I go here and they say, oh what is the a over DX?

**[47:27 – 47:37]** Well, it's since this is a plus and du over DX is DX over DX, plus dy over DX. So it's one plus zero, it's one

**[47:38 – 47:41]** And, and so on DB over DX will be.

**[47:42 – 47:44]** 1 minus 0 will be 1.

**[47:45 – 47:51]** DC over DX will be 3 times y squared.

**[47:52 – 48:06]** Oh, sorry, I'm doing DX will be zero apologize. This over the X, will be three y squared, times d. Y, over the X and the Y over the x is 0. So that will be 0.

**[48:07 – 48:09]** Now d.

**[48:10 – 48:16]** D over DX is 2A times the a over DX.

**[48:17 – 48:42]** Right. And okay. So let me maybe sorry, let me change this example, because all of these zeros will not be really interesting. So maybe let's say, maybe let's say x is 2. And why is minus 1? So here, we have minus 1. Here, we have three here, we have nine here, we have,

**[48:44 – 48:45]** I will start. Here, we have one.

**[48:47 – 49:06]** I'm bad at arithmetic. Here we have one here, we have three, one times, three, three and three. Minus 1 is 2, so we don't have a graph full of zeros. Okay, so DD over DX is 28 times, the a over DX and du over DX is 1. So it's like 2A.

**[49:06 – 49:11]** So it's two times X Plus y. If you write down the formula,

**[49:12 – 49:22]** Then the E. Okay, so D over DX, let me write it down. Here the E over the x e is a product. So

**[49:23 – 49:43]** How do you differentiate the product? It's the D over DX times B plus DB over DX times d, right? So, that will be DD over. The x is 2 times X Plus y times B, which is x minus 5, right? Plus

**[49:44 – 49:46]** DB over DX is one.

**[49:47 – 49:50]** Times D, which is X Plus y squared.

**[49:52 – 49:52]** Okay.

**[49:53 – 50:01]** So that this is going to be the over there. Now, the F over the X. Finally,

**[50:02 – 50:16]** The F over DX is just the E over DX plus DC over DX, right? And we know all of this guys. So this here over the x is 0 and D over DX is this

**[50:16 – 50:18]** So it the answer is.

**[50:20 – 50:28]** X Plus y squared, plus 2 times X, Plus y times, x, minus y, you can open the brackets doesn't matter for us.

**[50:31 – 50:38]** It sounds about, right? So if you just look at the formula and you do it in your head, what's correct?

**[50:40 – 50:53]** Of course in practice, you wouldn't be able to drag the formulas with you. So in practice, what you would actually do is you would compute the numerical values of this derivatives. So you would go like

**[50:56 – 50:58]** You would start with one and zero.

**[50:59 – 51:24]** And then here, it's all so 0. Okay. So here the formula in the values, the same here. Also, one is both the formula and the value and here also. But here you would not have a formula, like, two times X plus 5, which just have the numerical value. And actually what you would, what you would do in, if you were implementing it as an algorithm, you don't know, excellent, why? When you are inside the note,

**[51:25 – 51:27]** what you do know is a

**[51:28 – 51:39]** You know, this input that went here from from a and a was equal to 1. So we can just stop at this point and say that the the derivative here is equal to 2

**[51:40 – 51:41]** Okay.

**[51:42 – 51:49]** And similarly here, what we actually are Computing is Didi over DX, which is 2.

**[51:50 – 51:53]** times B, the value of B, which is 3

**[51:54 – 52:01]** It goes here. Plus DB over DX which is 1 times the value of D, which is 1.

**[52:02 – 52:04]** So we'll get something like seven here.

**[52:05 – 52:13]** And then we would add 7 and 0 and gets seven and I suppose that's correct. All right, if I substitute two and minus 1

**[52:15 – 52:17]** Oh, I get. Yes, six plus one. Yes.

**[52:19 – 52:19]** so,

**[52:21 – 52:22]** so what have we done now?

**[52:23 – 52:26]** We have gone through the graph.

**[52:26 – 52:27]** Bottom up.

**[52:28 – 52:55]** And we have only done it once. We don't need several passes, we just need one single pass. Yes. We you we do both when we go through the graph, we do both Computing, the functions and Computing the derivative the everything over the X, right? But it's okay, we go through the graph, these two things and when we arrived at the end we have both the value of f.

**[52:56 – 52:58]** And the value of the air, over the X.

**[53:01 – 53:13]** So here's a question for you. I hope somebody is still with me because yeah, I know this probably was boring but here is a question for you. Why isn't that? Why is that not enough?

**[53:14 – 53:18]** I just did a single pass from the graph and they got the derivative

**[53:19 – 53:23]** Why can't you just use this all this? Why do I need back propagation?

**[53:27 – 53:29]** What's the catch? What's wrong here?

**[53:30 – 53:33]** All the formulas are right. We did indeed, get the derivative.

**[53:33 – 53:36]** But why can't we just use this approach?

**[53:48 – 53:53]** While you're thinking no copy the graph because then we'll go to actually back propagation.

**[53:54 – 54:00]** But why can't we just use forward navigation and be content with forward propagation?

**[54:27 – 54:30]** Because we need gradients, Maybe

**[54:31 – 54:34]** Okay, so where we move?

**[54:36 – 54:42]** Okay, so we need gradients and we just got there for the X. We can do the afford the way in the same way.

**[54:48 – 54:49]** What's the catch?

**[54:59 – 55:05]** Yes. See I I need to repeat this even though we probably know but propagation already but

**[55:08 – 55:08]** um,

**[55:11 – 55:15]** what's the cash? Why can't I just use this? Why do I need to to invent anything else?

**[55:16 – 55:27]** Now I will proceed to back probe. I will tell you how to go from from the end to the beginning of this graph. It will be slightly different, but why can't I use this? What's wrong with this?

**[55:58 – 56:06]** So, theoretically formally, we can write everything is correct. We did get there for the X.

**[56:07 – 56:11]** And sure enough we can do the same thing. Get there for you. Why no problem.

**[56:12 – 56:14]** So, what is the problem? If it's not in the

**[56:16 – 56:18]** Here in the formal correctness.

**[57:00 – 57:04]** How would we apply this algorithm to an actual neural network?

**[57:07 – 57:08]** What would be the procedure?

**[58:30 – 58:35]** yeah, all right, so how would we

**[58:36 – 58:44]** Apply this algorithm. This forward propagation derivative Computing algorithm to a real neural network.

**[58:45 – 58:47]** Or actually to any function.

**[58:49 – 59:02]** As you said but for some reason didn't elaborate on it. We need the whole gradient as the result, right? So we need in this case we need both AFR or DX and therefore divide.

**[59:04 – 59:08]** So this procedure that the one that I wrote down gives you therefore DX

**[59:09 – 59:11]** How do I get there for the Y?

**[59:12 – 59:23]** Well, I can go through the graph again, but this time, I will compute. I will start with the X over The Y, which is 0 the Y over the Y, which is 1 and again go through the graph and get to

**[59:24 – 59:25]** And get.

**[59:27 – 59:28]** and I will get there for do I sure

**[59:29 – 59:37]** Or alternatively, what I could do, I could compute the soul and parallel, right? So as I go through the graph,

**[59:38 – 59:48]** I am doing everything at once. I am doing the values, I'm doing dxo D, everything over DX. And I'm also doing everything over dye

**[59:49 – 59:50]** That's all.

**[59:52 – 59:57]** So then I will only need one pass. And during this one pass, I will compute everything.

**[1:00:00 – 1:00:02]** But both of these approaches are completely impractical.

**[1:00:03 – 1:00:10]** You see in the real neural network, like how do we want to scale this up for a function of two variables? That's fine.

**[1:00:11 – 1:00:12]** But how do we scale this up?

**[1:00:13 – 1:00:28]** When you scale it up to a real neural network they as I said, the length of the vector of the gradient is large, right? So modern neural networks may have billions of weights at least Millions for sure, right?

**[1:00:29 – 1:00:29]** so,

**[1:00:30 – 1:00:31]** How do we?

**[1:00:32 – 1:00:40]** So, what does it mean to apply the salary to get a gradient over a million variables?

**[1:00:41 – 1:00:45]** It means we either need to go over the graph a million times.

**[1:00:47 – 1:00:47]** It doesn't sound good.

**[1:00:48 – 1:01:12]** Or we go over the graph from once. But in every note of the graph, we need the vector of Sesame million because we actually do need it. All of this way really values when we go and we basically we need a huge amount of memory. We need a million times. The size of the graph of memory to actually do this one for us.

**[1:01:14 – 1:01:14]** so,

**[1:01:15 – 1:01:39]** neither of this actually works, right? As you probably understand, the networks are the practical networks will be so large that they just one copy of them. Barely fits into your GPU, right? So, of course, you cannot fit a million copies of the neural network into in, into your into memory to do this.

**[1:01:40 – 1:01:51]** And of course, you can do a million passes over the network and then it would take forever, right? So either the time doesn't work or the space test work. In this case,

**[1:01:53 – 1:01:58]** fortunately, we can do it in a much better way.

**[1:01:58 – 1:02:01]** And that's what back propagation is about.

**[1:02:02 – 1:02:04]** So, back propagation.

**[1:02:08 – 1:02:08]** Be proper.

**[1:02:13 – 1:02:28]** Switches the, the question switches goes to the duel, and to the converse way of viewing this graph, and to the inverse way of moving through this graph.

**[1:02:29 – 1:02:34]** So what did we do here in the straightforward approach when we go bottom up?

**[1:02:34 – 1:02:40]** We compute like when we go bottom up we compute the everything over DX.

**[1:02:41 – 1:02:47]** So we get this sequence when we go through the graph of D, every node over DX,

**[1:02:47 – 1:02:50]** And finally, we get to the F overdose.

**[1:02:50 – 1:02:55]** When you do it like this, obviously you need to, to do as much.

**[1:02:57 – 1:03:00]** To get the over the wire and so on.

**[1:03:02 – 1:03:03]** But, what if?

**[1:03:03 – 1:03:08]** instead of starting from the inputs and doing the everything over the X

**[1:03:09 – 1:03:13]** What if we did the opposite? What if we start from Top?

**[1:03:14 – 1:03:17]** And we do the F over the everything.

**[1:03:18 – 1:03:25]** You see? So we go. Now, the base of our induction is the F over the DF, which is one

**[1:03:27 – 1:03:32]** And then are what do we for example, do here. When we go to E,

**[1:03:33 – 1:03:36]** We say all right. So what is the F over d e.

**[1:03:37 – 1:03:45]** Well, we need we only need to know. Locally how FS computed. So f is e, plus C. So DF over D is one very easy.

**[1:03:46 – 1:03:48]** Here. Also the F over DC is one.

**[1:03:50 – 1:03:56]** Then it becomes a bit more interesting. So now what is let's say, DF

**[1:03:56 – 1:04:11]** Okay, so here I want to put the F over DD over here, right? And all right. Separately won't fit there. What is the F over GD? Well, d goes to F only through e.

**[1:04:11 – 1:04:21]** Right. So by the chain rule, as usual DFO over DD is the F over d. E times d e over DD.

**[1:04:21 – 1:04:23]** So the F over D is 1.

**[1:04:24 – 1:04:26]** And the over DD is B.

**[1:04:28 – 1:04:30]** So it's one time speed write.

**[1:04:34 – 1:04:37]** And so on. So for example, so here, I get B.

**[1:04:38 – 1:04:58]** Now let's say d. Okay what else? GF or D? Yeah, DF over DB it's the next step right there. For DB is again B goes only through e so it's D over D times d e over D B and it's D.

**[1:04:59 – 1:04:59]** Okay.

**[1:05:00 – 1:05:16]** The air for the a again a goes only through D so it's D. Okay let me put it here. DF over de is the F over DD times DD over de and it's

**[1:05:17 – 1:05:22]** it's what it's 2A times B.

**[1:05:23 – 1:05:24]** Okay.

**[1:05:25 – 1:05:27]** So two a b.

**[1:05:30 – 1:05:32]** And now comes the interesting part.

**[1:05:33 – 1:05:38]** So now I have DFO over de DF over DB and the over DC.

**[1:05:39 – 1:05:42]** And now I need to compute, let's say DF over DX.

**[1:05:44 – 1:05:45]** And X.

**[1:05:46 – 1:05:46]** Goes.

**[1:05:47 – 1:06:17]** Into different things, right? So there are two outgoing ages here which means that X is a part of a, which is then part of and X is a part of B, which is the part of. So again, by the chain rule, it's really straightforward. I just need to add up the contributions, right? So the F over D. A times d, a over DX, plus the F over DB times DB over there. Let's say

**[1:06:18 – 1:06:32]** so I know there for day which is 2 a b d over DX is 1 and this is straightforward plus DF or DB which is B times DB over DX which is also one

**[1:06:32 – 1:06:46]** So, we go to a B plus d. So this is 2 times X Plus y times x, minus y, plus X, Plus y squared, which is, I guess, correct.

**[1:06:48 – 1:06:49]** So we go.

**[1:06:50 – 1:06:55]** The same result as before right there for the X but the beautiful part here.

**[1:06:56 – 1:07:07]** Is that with without starting over with without three Computing, everything that was happening above, we all can immediately get there for UI over here.

**[1:07:09 – 1:07:30]** Right. So now why goes to three different things? Okay, let me since you're not very quick ones from equation and let me write it down a bit more in a bit more detail. So DF over d8 times over the wire, right? Plus the F over DB times t b over d y plus the F over DC times this is over, do I

**[1:07:31 – 1:07:34]** And what we get here. Well,

**[1:07:35 – 1:07:39]** therefore de is 2 a b times 1.

**[1:07:40 – 1:07:58]** The AF over DB is D times, minus 1, right? The DFD over device minus 1. So minus D and therefore, this is 1. But then we need to multiply by DC over the Y, which is 3 y squared,

**[1:07:59 – 1:08:07]** so we get like two times X Plus y times x, minus y, minus X, Plus, y squared, plus,

**[1:08:08 – 1:08:09]** Three y squared.

**[1:08:10 – 1:08:16]** And I suppose that's all correct, right? If you go and look at this. Yeah, obviously that's all correct.

**[1:08:17 – 1:08:17]** so,

**[1:08:19 – 1:08:30]** Notice the difference, right? In stead of going Bottom up and Computing, D everything over DX, and then or in parallel, the everything over the why

**[1:08:31 – 1:08:36]** Thus like doing a lot of unnecessary, computations, we are going.

**[1:08:37 – 1:08:41]** From top to the bottom and we are Computing. DF over the everything.

**[1:08:42 – 1:08:59]** In there. And of course this is these are two symmetrical approaches. They are dual to each other. They it's you can argue that it's basically the same but neural networks are not symmetrical, right? You always have only one output because

**[1:09:00 – 1:09:17]** You want to, for example, minimize your output right. You, you need to have a single function that you minimize, your cannot minimize several functions or a million functions. At once that doesn't work, if you have a million functions that you need to minimize first, you need to compose them into a single function.

**[1:09:19 – 1:09:20]** so,

**[1:09:22 – 1:09:24]** You always have only one output at the end.

**[1:09:25 – 1:09:27]** And you have millions of inputs.

**[1:09:28 – 1:09:36]** So this approach skills, well if you have lots of arts and few inputs, then this is the proper way.

**[1:09:37 – 1:09:44]** but our situation is the opposite in real networks we have lots of inputs and one output so

**[1:09:45 – 1:09:47]** So, we use bad propagation.

**[1:09:48 – 1:09:49]** No test.

**[1:09:50 – 1:09:55]** How in this case, like what did we need to?

**[1:09:56 – 1:10:12]** Uh to do this computations I wrote down formulas because they are easier to to follow than just numbers because numbers don't mean anything. But in practice, of course, in actual computation they would be numbers right there. This this would be numerical values of these things.

**[1:10:13 – 1:10:14]** and,

**[1:10:14 – 1:10:14]** so,

**[1:10:16 – 1:10:20]** When you start start out with the F over the F, of course, it's always one.

**[1:10:21 – 1:10:29]** But then, as we progressed through the graph backwards to compute, for example, DF over DD.

**[1:10:29 – 1:10:36]** So what what's happening on? What? What gets transmitted on this Edge. What gets transmitted from E to D?

**[1:10:39 – 1:10:43]** We need it. Not only there for D, which we got from, from above.

**[1:10:44 – 1:10:46]** But we also needed D over DD.

**[1:10:47 – 1:10:50]** And to compute the over DD. We needed the value of B.

**[1:10:51 – 1:10:56]** So we needed to know the values of this intermediate notes.

**[1:10:58 – 1:11:04]** Again it's all local to compute this. I only need the notes that go inside.

**[1:11:05 – 1:11:10]** But I do need to know the ways to not only the lyrics.

**[1:11:11 – 1:11:13]** Because to compute the derivatives, I need to know the radius.

**[1:11:14 – 1:11:21]** So in practice bad propagation is not one pass through the graph. It's two passes.

**[1:11:22 – 1:11:28]** So how the algorithm actually works first. You do forward propagation.

**[1:11:29 – 1:11:30]** To compute.

**[1:11:31 – 1:11:33]** Values of intermediate nodes.

**[1:11:35 – 1:11:44]** And yes, you need to store them. So it's kind of like the you need to store two numbers on every edge of this of this graph.

**[1:11:45 – 1:11:46]** and then,

**[1:11:47 – 1:11:48]** back prop to compute.

**[1:11:50 – 1:11:52]** DF over the everything.

**[1:11:53 – 1:11:55]** For for every intermediate.

**[1:11:56 – 1:11:59]** so, let's back propagation, okay and

**[1:12:00 – 1:12:08]** This is a very efficient and actually pretty straightforward. Wait to compute gradients.

**[1:12:09 – 1:12:12]** and actually, I, if you look at

**[1:12:13 – 1:12:30]** Any deep learning library like pytorch that you will probably be using in practice in our class. If you look at any preparing Library, what you see is it's basic

**[1:12:30 – 1:12:38]** Operation, what it actually is supposed to do really, really well its main job.

**[1:12:38 – 1:12:40]** Is to do this, to passes to the graph.

**[1:12:41 – 1:12:41]** So,

**[1:12:42 – 1:12:44]** These are the key.

**[1:12:45 – 1:12:57]** Procedures. The key functions that the library needs to implement and everything else is basically just syntactic sugar. On top of that.

**[1:12:58 – 1:12:58]** so,

**[1:13:00 – 1:13:29]** If you, I don't know if your program and pytorch, if you do the Practical sessions of this class and you implement a new neural network, sure, you will see that by Turkish has thousands of classes with different layers, different kinds of components. And all of this components are only there, they are only needed to set up this graph.

**[1:13:30 – 1:13:40]** And this components can be relatively inefficient, it doesn't really matter. They are only around once and they don't don't do much to be honest.

**[1:13:41 – 1:13:49]** What actually has to be efficient. What is like the meat of the of everything? Is Computing. The gradient of the ground graph.

**[1:13:50 – 1:14:00]** So I like to say that pytorch and tensorflow and whatever else, what, what they actually are, are, automatic differentiation, libraries.

**[1:14:01 – 1:14:05]** They are not, I mean, the Deep learning is an afterthought.

**[1:14:05 – 1:14:13]** What is actually what actually has to be extremely efficient is the forward propagation and the backward propagation procedure.

**[1:14:13 – 1:14:17]** The rest can be done in any way.

**[1:14:19 – 1:14:20]** Okay.

**[1:14:22 – 1:14:25]** What else do I want to say here? I want to see.

**[1:14:27 – 1:14:36]** Okay, for propagation backward propagation and example. Okay, so well, I'm thinking what they'll say missed, let me show you.

**[1:14:37 – 1:14:40]** What I will sew make available. I have some

**[1:14:41 – 1:14:42]** examples over here.

**[1:14:44 – 1:14:59]** So it's a different function but something something like what I just did on the board and you can play with it. You can, you can Define different computational graph and see how the values propagate through a network like this one.

**[1:15:00 – 1:15:00]** Right.

**[1:15:01 – 1:15:09]** Oh yeah, and also just to Circle back to how it actually applies to neural networks. Notice that

**[1:15:11 – 1:15:32]** When like, when you say, what is the input to the to a neural network, the in your intuition, like your default answer would be the input is X and Y or actually on the X. So like if if you ask, what is the input of the neural network that distinguishes gets from dogs? Well, that's an image.

**[1:15:33 – 1:15:39]** And that's that's true, right? So the default weight to think of inputs is, is this but

**[1:15:40 – 1:15:52]** If you think of the network as a competition on graph, it has two different source of inputs. I think I already said that, right? So it has inputs that are fixed. That are always fixed that we do not optimize.

**[1:15:53 – 1:15:53]** And these are.

**[1:15:55 – 1:16:00]** Like images, correct? Answers to the images. And so on, these are the access and the wise

**[1:16:01 – 1:16:03]** And the weights.

**[1:16:04 – 1:16:15]** And the weights are inputs to the computational graph. They're not computed from anywhere, they are variables that appear in this huge formula.

**[1:16:16 – 1:16:17]** and when we are doing,

**[1:16:18 – 1:16:28]** Training. When we learn, when we are doing a training of neural networks, we are actually interested in gradients with respect to the weights.

**[1:16:29 – 1:16:58]** And so yeah, if anybody asks, there are different kinds of inputs in your own network and the weights are also inputs. And that's and when I was doing this, this example, there was no fixed input here, so I could have had it a constant or something, but I mean, wouldn't surf any purpose like X and Y? And this example are both weights and we need to have a gradient with respect to X and Y.

**[1:17:00 – 1:17:00]** Um,

**[1:17:01 – 1:17:02]** all right.

**[1:17:04 – 1:17:05]** Has been clear.

**[1:17:06 – 1:17:08]** Did you already know this?

**[1:17:10 – 1:17:10]** Or.

**[1:17:11 – 1:17:12]** Yeah. Okay.

**[1:17:15 – 1:17:16]** Okay, so

**[1:17:18 – 1:17:20]** Before the break before the break.

**[1:17:21 – 1:17:36]** I guess I don't have too much time. So let me just maybe do a part of what I wanted to to say about gradient descent. Specifically, let me

**[1:17:37 – 1:17:41]** Motivate stochastic, gradient descent and actually introduce it.

**[1:17:43 – 1:17:48]** And then after the break, we will discuss the actual algorithms of stochastic gradient descent.

**[1:17:49 – 1:17:49]** so,

**[1:17:51 – 1:17:54]** Here is here is a question.

**[1:17:55 – 1:18:05]** There are a lot of problems in deep learning in Practical, deep learning that come from, from the fact that we are using gradient descent.

**[1:18:06 – 1:18:17]** And we will discuss some of these problems in class. Of course we don't yet, see them, we are just on the beginning to look at this stuff. But basically a gradient descent is a pretty stupid algorithm.

**[1:18:18 – 1:18:24]** It's it's a first order. So gradient descent is the first order, first order.

**[1:18:25 – 1:18:29]** Comes from the first order approximation to the loss.

**[1:18:30 – 1:18:47]** Right? So I take like of double w and they say well, okay, so right now, I am at Point WK, let me do it. Taylor series of all of w, write at Point WK. So I say, well, it's all of WK.

**[1:18:48 – 1:18:53]** Plus W minus w k right times.

**[1:18:54 – 1:18:59]** The gradient of L at Point WK.

**[1:19:00 – 1:19:00]** Right.

**[1:19:01 – 1:19:16]** And gradient descent basically stops here. It just looks at this, it says, all right, so the gradient is the direction of steepest increase, therefore the opposite direction is the steepest decreased. Let's go there.

**[1:19:17 – 1:19:18]** If you want to minimize.

**[1:19:20 – 1:19:20]** but,

**[1:19:21 – 1:19:30]** We have years of optimization Theory, right? So, gradient descent could be done by, I don't know.

**[1:19:30 – 1:19:32]** Newton and leibnitz.

**[1:19:32 – 1:19:37]** And since then, we've had quite a lot of more.

**[1:19:39 – 1:19:52]** Involved, but better optimization techniques, right? And the most straightforward idea, when you look at gradient descent, like this would be well, what if we go one step further in the Taylor series?

**[1:19:53 – 1:19:53]** Why not?

**[1:19:54 – 1:19:57]** what if we all so,

**[1:19:58 – 1:20:10]** Go to the second, derivatives, I believe, minus, I WK that now now, there is a quadratic form and here, right times H inverse nothing, we're just h.

**[1:20:10 – 1:20:14]** A times W minus W. Okay.

**[1:20:15 – 1:20:18]** Plus something smaller, right?

**[1:20:20 – 1:20:25]** so now we are approximating not by a surface, not by

**[1:20:26 – 1:21:24]** linear surface, which, to be honest is a pretty stupid idea for optimization. Well, I mean, it's not stupid in the sense that it can work, but it's cheap and the sense that it's naive. So, if I'm looking at a complicated function and I am trying to to see like, what is the derivative here where to go, then all that, the derivative tells me is that. Well, you need to go here or you need to go here if we are dimensional one, right? And it doesn't tell you anything about how far you should go, and this is actually the main problem of gradient descent. This is what optimization Theory to a large extent was about. It's a big topic like great, the gradient gives you Direction but how far should you go along this direction? What should be the learning great. What should be the step-size?

**[1:21:26 – 1:21:26]** but,

**[1:21:27 – 1:21:28]** if you go one step further,

**[1:21:29 – 1:21:33]** then what you are doing is you're approximating your

**[1:21:35 – 1:21:39]** difficult function, locally with a

**[1:21:39 – 1:21:40]** Quadratic surface.

**[1:21:41 – 1:21:43]** on here, it would be a parabola but

**[1:21:45 – 1:21:47]** with a quadratic surface and now,

**[1:21:49 – 1:21:55]** There are no questions anymore, you know, where to go, you can go immediately to the minimum of this parable.

**[1:21:56 – 1:21:57]** The minimum of this quadratic surface.

**[1:21:58 – 1:22:19]** And it's it's a very simple formula, right? You'll look at this and you say, Okay, I want to minimize this guy. So how do you minimize? Well, you take the gradient with respect to W. Okay, so what is going to be the gradient with respect to W? Let's say that let me call this Vector, G the gradient g k gradient at step k.

**[1:22:20 – 1:22:26]** And this is HK. This is the Matrix of the second derivatives H because it's called the Hessian.

**[1:22:27 – 1:22:28]** and,

**[1:22:30 – 1:22:35]** I take the gradient of the first part. This disappears, this disappears. There is just GK.

**[1:22:36 – 1:22:52]** Right? And then I take the gradient of the second part, the two cancels out, and we get JK plus HK times W and that's the gradient of this quadratic function. So it should be equal to 0.

**[1:22:55 – 1:23:00]** And I guess that's sorry that's that's not it. Of course I forgot the first.

**[1:23:02 – 1:23:08]** I forgot h, k times W minus w k of course, sorry.

**[1:23:09 – 1:23:10]** And that should be equal to 0.

**[1:23:11 – 1:23:16]** So basically W is WK.

**[1:23:17 – 1:23:21]** Minus HK, inverse times JK.

**[1:23:22 – 1:23:22]** That's it.

**[1:23:23 – 1:23:47]** And you can say that this is your next W and you have no problem with the step-size. And this procedure is far, far more robust, more stable. You will never almost never goes to some bad part of the search space. You will converge and far. Fewer iterations basically it's better all around.

**[1:23:50 – 1:23:52]** And this is called Newton's method, by the way.

**[1:23:53 – 1:23:56]** Newton's method or second order optimization.

**[1:23:58 – 1:24:01]** Thought or second order optimization or whatever.

**[1:24:02 – 1:24:06]** So why can't we use Newton's method for gradient descent?

**[1:24:09 – 1:24:31]** For for Newton's method itself, the answer is kind of obvious because we cannot afford to do the to do this computation, right? So again remember that W is a very, very long Factor, right? It's, it's like a million of numbers. It's a vector of size, a million.

**[1:24:32 – 1:24:33]** So HK.

**[1:24:34 – 1:24:45]** The Matrix of second derivative. Right? The L over d w, i d w. J is a matrix of size a million times a million.

**[1:24:46 – 1:24:53]** And we are supposed to compute this Matrix but more than computers to invert it. So of course it's not going to work computation, right?

**[1:24:54 – 1:24:55]** No question about this.

**[1:24:57 – 1:24:58]** but,

**[1:24:59 – 1:25:01]** a more interesting question is

**[1:25:02 – 1:25:12]** in optimization theory in classical optimization Theory, like in the 1960s and 1970s and 1980s. People also were thinking about this

**[1:25:13 – 1:25:26]** There were no huge neural networks at the time, but there were functions to optimize. And there were difficult functions to optimize and error cases, when secondary techniques were to difficult computationally.

**[1:25:26 – 1:25:28]** So there is this whole field.

**[1:25:30 – 1:25:33]** of what is called quality in youth, from algorithms,

**[1:25:34 – 1:25:37]** Course in Newton algorithms.

**[1:25:40 – 1:25:42]** And they are basically approximation to this.

**[1:25:43 – 1:25:46]** so, the most famous such algorithm is called lbfgs

**[1:25:48 – 1:25:56]** Where else stands for limited? Memory and bfgs are for last names, Fletcher, void and Goldfarb something like this.

**[1:25:58 – 1:26:07]** So it's a very famous algorithm. I won't go into details on how it works. It's definitely not relevant for us but basically what it does is it

**[1:26:08 – 1:26:13]** Keeps an approximation to this kind of update.

**[1:26:14 – 1:26:16]** Ah, and the very good approximation.

**[1:26:17 – 1:26:20]** By only looking at the W's themselves.

**[1:26:21 – 1:26:25]** W1w 2 and so on, and the gradient vectors.

**[1:26:27 – 1:26:40]** So like when you go from K to K plus 1 you there is a procedure to update. This approximate Hessian approximate inversion and this procedure is quick.

**[1:26:41 – 1:26:50]** And it never deals with a million times, a million matrices. Basically it's a lower rank approximation, but let's not go there. So

**[1:26:51 – 1:26:52]** There are good ways.

**[1:26:54 – 1:26:56]** To do something like the second order technique.

**[1:26:58 – 1:27:11]** Without going actually to the second order. Well, only staying at the level of gradients and gradient factors and doing doing it in relatively low complexity.

**[1:27:13 – 1:27:16]** So why don't we do that in the appearing?

**[1:27:17 – 1:27:22]** And the answer is again, we would be very happy to

**[1:27:23 – 1:27:29]** and just as we would be very happy to use Newton's method will be very happy to do the second order optimization.

**[1:27:30 – 1:27:32]** And we would be nearly as happy.

**[1:27:33 – 1:27:36]** To do lbfgs for any neural network.

**[1:27:37 – 1:27:38]** But we can't.

**[1:27:39 – 1:27:51]** And here comes the interesting part. So why am I a billionaire to this? So first I wanted to mention second-order optimization but but also, why am I, why doesn't an algorithm like this work?

**[1:27:52 – 1:28:02]** I didn't tell you what the algorithm is, but trust me. It only need requires to know, gradients at individual points values at this point, and that's it on your

**[1:28:04 – 1:28:05]** Own, and the answer is.

**[1:28:06 – 1:28:07]** In deep learning.

**[1:28:08 – 1:28:09]** Unfortunately.

**[1:28:10 – 1:28:13]** We cannot even apply gradient descent.

**[1:28:14 – 1:28:17]** Because we cannot even compute the gradient.

**[1:28:19 – 1:28:23]** Or, I mean we can only compute it like once and not never step.

**[1:28:26 – 1:28:27]** Why, why? So

**[1:28:28 – 1:28:35]** For a very straightforward reason and I, actually already mentioned this reason. Where did they do that? I did it.

**[1:28:37 – 1:28:43]** Where did I hear, right? So what is the function that we are actually minimizing in machine learning?

**[1:28:45 – 1:28:47]** The function L of w.

**[1:28:48 – 1:28:50]** Is like a huge average.

**[1:28:52 – 1:28:55]** or a huge sum same thing of

**[1:28:56 – 1:28:58]** form of loss functions.

**[1:29:00 – 1:29:01]** Across the whole data set.

**[1:29:02 – 1:29:06]** Of X and Y and W.

**[1:29:07 – 1:29:22]** You can think of it, by the way, usually is something like the negative log likelihood, right? Lock P of or block posterior. Look of w given X and Y and

**[1:29:23 – 1:29:29]** to connect it to what we discussed yesterday and the day before. But in any case,

**[1:29:30 – 1:29:33]** Your complicated neural network with a million ways.

**[1:29:34 – 1:29:35]** Leaves over here.

**[1:29:38 – 1:29:44]** It computes the laws. Yes. But it computes the laws on known one training sample.

**[1:29:44 – 1:29:50]** And to get the function that you minimize, you need to go over the whole data set.

**[1:29:51 – 1:29:56]** so, the actual honest to God, gradient, the actual G,

**[1:29:57 – 1:29:58]** Okay.

**[1:29:58 – 1:29:59]** Would be.

**[1:30:00 – 1:30:01]** A future average.

**[1:30:02 – 1:30:06]** Of a gradients of this loss function.

**[1:30:10 – 1:30:20]** Was functions at Point WK, right? And yes, we can obviously compute every one of them, but if I wanted to compute,

**[1:30:21 – 1:30:28]** The true value of the gradient Vector, I would need to go over the whole data set on every step.

**[1:30:30 – 1:30:41]** Which is kind of obviously impractical. So yeah, we will go over the whole data set but maybe like once or twice, not not on every step of our optimization procedure, that that's not gonna work.

**[1:30:46 – 1:31:04]** So what is the actual setting? How what what is the problem? And we are solving if I am telling you that we cannot even compute, the function, that we are optimizing, right? It's the same in the same thing, right? We can compute the gradient because it's a huge sum and therefore, we can't even compute the function itself because it's the same here, some

**[1:31:08 – 1:31:09]** What are we even doing?

**[1:31:11 – 1:31:12]** Well, the answer is.

**[1:31:13 – 1:31:16]** We are doing what is known as stochastic gradient descent.

**[1:31:24 – 1:31:39]** I wrote, I wrote all of this functions, not a sums, but as averages, it doesn't matter for optimization but I wrote them whenever for as averages to make the following point, you can view this loss function, you can view the function that we are optimizing.

**[1:31:40 – 1:31:42]** As an expectation.

**[1:31:44 – 1:31:46]** Over the data set.

**[1:31:47 – 1:31:50]** Over the uniform distribution of the data set.

**[1:31:51 – 1:31:52]** Of this.

**[1:31:56 – 1:31:56]** Small loss function.

**[1:31:58 – 1:32:00]** So X and Y here, X and Y.

**[1:32:02 – 1:32:15]** Are taken just uniformly at random from the dataset, right? Because what is the expectation of the expectation is the average weight is probably just. So if I take everything is equal probabilities, I get just over average.

**[1:32:17 – 1:32:19]** So, our function.

**[1:32:22 – 1:32:34]** Is actually an expectation of a different function with respect to some of the variables with respect to X and Y. And I want to minimize it with respect to the other variables, to the respect to w.

**[1:32:36 – 1:32:40]** When you have a problem like this, this is what's called stochastic optimization.

**[1:32:44 – 1:32:44]** and,

**[1:32:48 – 1:32:54]** What is, how can we do it? If we cannot compute this expectation directly,

**[1:32:55 – 1:32:55]** Well.

**[1:32:56 – 1:33:03]** There is basically always exactly one true way to approximate the expectation. You take a sample and that's it.

**[1:33:04 – 1:33:06]** So what we are actually doing?

**[1:33:07 – 1:33:09]** In practice.

**[1:33:10 – 1:33:12]** Is on every step along the way.

**[1:33:14 – 1:33:14]** We are taking.

**[1:33:15 – 1:33:18]** Not the gradient GK.

**[1:33:20 – 1:33:25]** Which is, I mean, expectation is linear, so it's the same thing. It's the expectation of the gradients of

**[1:33:28 – 1:33:33]** hell, right? But we are approximating the true gradient.

**[1:33:34 – 1:33:34]** With.

**[1:33:35 – 1:33:38]** Let's say G hat. Okay?

**[1:33:39 – 1:33:43]** Which is just the average over a small subsample of this.

**[1:33:44 – 1:33:46]** 1 over, let's say, m

**[1:33:47 – 1:33:48]** Times the sum.

**[1:33:50 – 1:33:51]** Gradient.

**[1:33:53 – 1:33:55]** L of x, i y, i

**[1:33:56 – 1:33:56]** W.

**[1:33:59 – 1:34:02]** So on every step along the way.

**[1:34:03 – 1:34:23]** What we are actually doing, and you probably already know this, you just, I just kind of think you never thought with from this direction from this angle, but there is also probably already know what we actually do when we train difficult, duplicated machine learning models. We don't go over the whole data set to compute the loss,

**[1:34:23 – 1:34:24]** We go.

**[1:34:25 – 1:34:26]** Through mini beaches, right?

**[1:34:28 – 1:34:29]** And this meaning batch.

**[1:34:32 – 1:34:34]** Formerly. It's a sample from the data set.

**[1:34:35 – 1:34:49]** So what we are actually doing like what the meaning of what we're doing. Okay, great in the scent is we are approximating the true value of the gradient. Which is bacon difficult with a

**[1:34:50 – 1:34:50]** Sample.

**[1:34:51 – 1:34:53]** Sample to the gradient.

**[1:34:53 – 1:35:01]** So on average, if you take the average of this, over the whole dataset, obviously you get the same thing. So the the mean is correct.

**[1:35:02 – 1:35:26]** And to be honest, approximating the expectation with a sample is like one of the best things you the one of the best approximations ever. It has all of the nice properties. It converges. It's it has its unbiased that has lots of results known about it so it's as good an approximation as we can hope for

**[1:35:28 – 1:35:53]** And what we actually do in practice is we go on every step of gradient descent with sample a mini beach. We take a small subset from the data set. We compute the gradients on the subset and then we see what happens next. And then we update the weights, according only to the gradients from this subject, probably know this. But now you can you can see what it actually means.

**[1:35:55 – 1:35:55]** but,

**[1:35:57 – 1:36:06]** Even though this is a good approximation and even though indeed we will go to. We when we do to test the gradient descent, we do.

**[1:36:08 – 1:36:19]** arrive at a good at the neighborhood of minimum, etc, etc, will discuss it after the break, what we actually get from from SGD, but

**[1:36:21 – 1:36:22]** it's still an approximation.

**[1:36:23 – 1:36:23]** and,

**[1:36:24 – 1:36:26]** In practice. It's a pretty bad one.

**[1:36:27 – 1:36:29]** I mean, it's good theoretically, but

**[1:36:30 – 1:36:36]** The specific numbers are like the size of the data set is in millions or more.

**[1:36:36 – 1:36:40]** And they actually mini batch size, is like four.

**[1:36:42 – 1:36:43]** Or eight, Maybe.

**[1:36:44 – 1:36:52]** So the minion based size should be such that this may cause of the network would fit into your GPU memory and it's a small number.

**[1:36:53 – 1:36:54]** They?

**[1:36:54 – 1:37:06]** The data set is, of course, large. So we are approximating the average of a Million numbers by taking like four or eight or even one number at random.

**[1:37:07 – 1:37:14]** So of course, mathematical is the best we can do, but it's still a pretty bad approximation. It's still has a pretty big variance.

**[1:37:15 – 1:37:18]** And unfortunately, this variance kills.

**[1:37:19 – 1:37:21]** Algorithms, like lbfgs. So,

**[1:37:22 – 1:37:25]** Since they are all doing approximations.

**[1:37:26 – 1:37:32]** In order for those approached that I can can't explain without this whole separate lecture why but trust me.

**[1:37:35 – 1:37:56]** Since there are also doing approximations here. In order for those approximations to actually work, we need to have very good values of the actual gradients, but true various or at least very good. Approximations, we cannot just replace this GIS with sampled versions with huge variants and hope for the best. The best one will not come.

**[1:37:57 – 1:38:23]** So it's it's an interesting and a very practical actually open problem for deep learning can be due better. Can we, can we may be modified was in Newton algorithms so that they are, they will start working. So that we can, for example, use case the gradients, this sample estimates, instead of true gradients and still

**[1:38:24 – 1:38:25]** Go where we want to go.

**[1:38:26 – 1:38:37]** this is a known and probably we cannot because lots of smart people have already thought about this and unfortunately no solution has come

**[1:38:39 – 1:38:40]** but,

**[1:38:42 – 1:38:54]** of course, stochastic gradient descent. So now, okay, so now the actual like formula of the update is this WK, plus 1 is WK,

**[1:38:54 – 1:38:56]** Minus some learning rate.

**[1:38:57 – 1:39:06]** Times. Okay, let me just call it times JK head. So times, this sampled gradient.

**[1:39:07 – 1:39:34]** I will call it SGD, stochastic gradient descent, and of course, this is also not the end of the story. This is the first natural step, the simplest possible algorithm. And of course, there have been lots and lots of modifications and improvements of this idea. So after the break will discuss those, they also like the very heart of the appearing. And for now, are there any questions about SGD backprop?

**[1:39:40 – 1:39:41]** Okay.

**[1:39:42 – 1:39:46]** If now questions, then let's have a break. And when we can win, we go to

**[1:39:47 – 1:39:51]** SGD, variations and algorithms that people actually use to train your Networks.

**[1:39:52 – 1:39:52]** Break.

**[2:01:14 – 2:01:17]** Okay, let's let's continue.

**[2:01:18 – 2:01:18]** so,

**[2:01:21 – 2:01:25]** We stopped at the notion of stochastic gradient descent.

**[2:01:26 – 2:01:36]** and I actually, before we, I don't want to delve to deepen to the theory of this stuff, but I want to show you a couple of

**[2:01:36 – 2:01:41]** pictures and results about it before we actually proceed to

**[2:01:46 – 2:01:51]** To the new algorithms to variations of stochastic gradient descent. So

**[2:01:54 – 2:02:17]** What actually happened in stochastic gradient descent? You can actually analyze it. And classical optimization theory, has analyzed it in great detail. And what, what, actually happens like, what, what is the correct way of looking at it so to speak? Well, basically

**[2:02:18 – 2:02:24]** A lot of optimization theory was centered around this question.

**[2:02:25 – 2:02:27]** so, suppose that

**[2:02:28 – 2:02:32]** We are standing over here. This is our WK.

**[2:02:33 – 2:02:46]** And what does the gradient, descent? Tell us. Well, it tells us the direction where we are supposed to go, right? So we know that we are supposed to go in the direction of JK.

**[2:02:46 – 2:02:56]** But we don't know how far we should go. Like, do we stop here? Do we go all the way here or here? We don't know. It's it's only the direction, not the endpoint.

**[2:02:57 – 2:03:00]** So a lot of optimization actually.

**[2:03:01 – 2:03:23]** A lot of optimization theory if you, if you ever had a class on it or if you will have a class on it, a lot about centers on this one dimensional optimization problem. Like we already know that direction and be like, we are optimizing f of x. We are let's say minimizing and at this point,

**[2:03:25 – 2:03:28]** We already know that I want to go from X.

**[2:03:29 – 2:03:30]** To the direction.

**[2:03:31 – 2:03:32]** G right.

**[2:03:35 – 2:03:49]** But I still don't know how far I want to go. So let me treat this as a function of one variable and let me try to actually find the optimal step size, let me actually try to find out how far I should go in this direction.

**[2:03:50 – 2:03:56]** So, it will still be an iterative procedure, but hopefully we can say something about how far we should go.

**[2:03:57 – 2:04:05]** So a lot of classical results like we'll throw our myjoe's rule etc. Etc. They are all about this kind of problem.

**[2:04:06 – 2:04:11]** And we don't care about this results because they don't carry over to stochastic gradient descent that easily.

**[2:04:13 – 2:04:27]** What does carryover. So what what does classical optimization Theory? Say about. Okay, we discussed this. So what does classical optimization Theory? Say about stochastic gradient descent specifically?

**[2:04:28 – 2:04:28]** Well.

**[2:04:29 – 2:04:44]** SGD. If you look at its rejected, if you look at how it works, it actually works like this and I will make it precise in a moment. But the picture is like this, if you are optimizing a function

**[2:04:45 – 2:04:46]** You.

**[2:04:47 – 2:05:02]** First. Go to the neighborhood of the minimum, the neighborhood of the optimum. It's a local Optimum and general, but it's matter. So you go to the neighborhood of a m Optimum.

**[2:05:04 – 2:05:12]** Quite quickly at first, this is the initial part of this trajectory. As you can see it, Go basically in the correct direction for for a long time.

**[2:05:13 – 2:05:32]** But then when you arrive, you can't stop. You can't converge, or at least you can't converge by default. So if you have a constant step size in gradient descent, if you don't have a schedule of decaying haters down to 0,

**[2:05:33 – 2:06:08]** then what's going to happen with stochastic? Gradient descent is, it will go to the neighborhood of the optimum and that will then oscillate their back and forth, right? Because it cannot even recognize when it goes to the optimum itself because in the optimum, the gradient is zero. Yes. But we don't know the great and we get random sample of the gradient, which will not be zero, and then we will go out of the optimum somewhere else so we can never know where exactly the optimum is, but we can get to a neighborhood and then just go around this neighborhood. Due to our random sampling.

**[2:06:09 – 2:06:11]** Sounds pretty reasonable.

**[2:06:12 – 2:06:33]** And if you do a little bit of math, which I think I will Skip, it's not hard but just I don't think there is any point in us, going through this. If you do a little bit of math, you arrive at an interesting estimate for like how long it's going to take and how stochastic gradient descent.

**[2:06:34 – 2:06:34]** and we're just

**[2:06:36 – 2:06:39]** so this is the result.

**[2:06:40 – 2:06:44]** The expected value of the function that we are optimizing.

**[2:06:45 – 2:06:46]** At.

**[2:06:46 – 2:06:54]** Well, not quite a text K. This is x k had, which is an intermediate Point. Let's forget about the details. Basically, after Kate durations,

**[2:06:55 – 2:06:58]** What we expect the function really to be.

**[2:06:59 – 2:07:12]** What is its residue? What is it different with the optimal function? Really? So we are minimizing so the optimal value is lower. But after K iterations, we can expect to be pretty close to the optimum. How close

**[2:07:13 – 2:07:19]** There is actually an answer. There is about like this one. Right? So it's less than or equal to

**[2:07:20 – 2:07:36]** Actually previously right less than or equal to our squared r squared. Is this guy, it's the original relationship. It's how far we were from the optimum and the beginning. So this is a constant basically. It's it's fixed at the beginning of our optimization process.

**[2:07:37 – 2:08:03]** Ah, and then there is this part, which is more interesting. So alpha eyes are the step sizes, right? So on step size, I we go to Alpha, I times given this Vector Alpha items, right? And here in the numerator, we get the sum of the Norms of this stochastic. Gradient squared times, Alpha squared,

**[2:08:04 – 2:08:08]** and in the denominator down here, we get just the sum of

**[2:08:09 – 2:08:32]** So if our stochastic gradients are bounded and probably they are, even though there's statistic, then we can just plug in this Bond, whatever it is, and we get this general form of the formulas. So, this is exactly what explains the behavior of stochastic gradient descent. Because look,

**[2:08:33 – 2:08:42]** suppose you have constant step size like we just did, if you had constant step size for all five star equal to H, then this

**[2:08:43 – 2:08:45]** Splits into two terms.

**[2:08:46 – 2:08:54]** And the first term is our squared over H which is basically over time scale, right? They should be basically just goes to 0.

**[2:08:55 – 2:09:05]** Pretty quickly as K growth, we go from iteration to iteration, K increases, right? So K increases to infinity and the rest is constant. So we goes to the

**[2:09:06 – 2:09:12]** second part is just constant, right? The second part. So the first part depends on how far we were in the beginning.

**[2:09:13 – 2:09:18]** And that goes to zero, which means that however forever we will go close to the correct option.

**[2:09:19 – 2:09:29]** On the other hand, when we get there, even when this part goes to 0 there, still the constant part over here, which doesn't have K inside.

**[2:09:30 – 2:09:33]** So it will be. It will remain constant.

**[2:09:34 – 2:09:39]** But of course, this formula tells us more than that.

**[2:09:39 – 2:10:02]** This is just a special case for the constant step size. And this formula also tells us how do we choose Alphas, so that's the case, the great in the sand converges. And the answer is, well, if you want this guy to go to zero, what is the easiest way to do it? You want your denominator, they sum of Alphas to go to Infinity.

**[2:10:03 – 2:10:09]** And at the same time, you want your newer, the sum of alpha squared to not go to image, right?

**[2:10:12 – 2:10:42]** So the Practical conclusion, one practical conclusion from this formula is that if you want your, stochastic gradient descent to converge, but in the, if you want to converge to an Optimum, then probably you need to take Alphas the step size as you want to reduce them. Obviously, otherwise you will never converge. But how fast do you reduce? And what is the schedule of reducing them all? This formula gives you the answers, are you want to reduce them on such a way?

**[2:10:43 – 2:10:51]** Let the sum of Alphas goes to Infinity. They were just but the sum of alpha squares does not go to Infinity converges, right? So,

**[2:10:52 – 2:11:10]** What would be the easiest example? This is example would be just I'll find if we go if you go back in our annotation like 8, okay. And we ask a question of how fast should a decade go to 0.

**[2:11:11 – 2:11:20]** Then this formula gives you a possible answer like this. I can do, like all 8K is something like 1 over k.

**[2:11:20 – 2:11:31]** Then the sum of 8, the case goes to Infinity, but the sum of 80 K squared does not go to infinity and therefore stochastic, gradient descent converges.

**[2:11:32 – 2:11:38]** So it's just one possible answer and to be honest in practice, this formula doesn't tell you much.

**[2:11:39 – 2:12:09]** So it tells you this General conversions Behavior, but it doesn't really translate to like real. I don't know estimates on the size of this neighborhood for example, because it always includes this g-square and you can never know, just Square it and practice it's about on your sampled gradients. So on like a sample of sub-sample of your data set which probably has a lot of variance so you don't know just Square to practice. But anyway, it does tell you something useful about stochastic gradient descent.

**[2:12:11 – 2:12:11]** but,

**[2:12:13 – 2:12:22]** But this is not really what I will be talking to you about. Now in, in the second part of our class, what I am going to be talking to you about

**[2:12:23 – 2:12:27]** is a very different problem of statistic, creating this and

**[2:12:30 – 2:12:31]** One second. Sorry.

**[2:12:46 – 2:12:53]** Yeah, sorry. So what what I will be talking to you about is a different problem of stochastic, gradient descent.

**[2:12:54 – 2:12:54]** so, let me

**[2:12:55 – 2:12:57]** show you what the problem actually is.

**[2:12:58 – 2:12:58]** So, we're here.

**[2:13:01 – 2:13:01]** Yeah.

**[2:13:02 – 2:13:02]** so,

**[2:13:05 – 2:13:14]** Let me guess what? My first write down. The very simple formula this. Okay, so we discussed SGD now let's say,

**[2:13:15 – 2:13:16]** Point number five.

**[2:13:17 – 2:13:17]** Is.

**[2:13:18 – 2:13:20]** SGD improvements.

**[2:13:22 – 2:13:25]** Improvements and variations.

**[2:13:29 – 2:13:38]** So what is the problem that we are solving? What is an important problem of all of this of stochastic gradients?

**[2:13:39 – 2:13:42]** Let's consider the following example.

**[2:13:42 – 2:13:54]** It's as simple as they come. It's probably like the easiest optimization problem possible. I will have a function

**[2:13:55 – 2:13:57]** of two variables X and Y.

**[2:13:58 – 2:14:07]** And it will look like this x squared plus a constant times y squared, okay? And I want to minimize it with respect to X and Y.

**[2:14:09 – 2:14:15]** So here, sorry here is the function right? The control plot of the function.

**[2:14:17 – 2:14:22]** Very easiest problem, the very easiest optimization problem possible, right? It's quadratic.

**[2:14:23 – 2:14:37]** The minimum is at 0. We immediately see that the minimum is at 0. It's convex, it goes to 0. Everything is great. Everything is fine, right? So very, very simple problem. However, you want to look at

**[2:14:38 – 2:14:48]** For example, if you want to use Newton's method, if you want to use the second order method, you go to 0 in one step because there is no approximation. Now, the second order is just the function of

**[2:14:50 – 2:14:53]** but what does first order?

**[2:14:54 – 2:14:59]** What the first order methods do? How does gradient descent tackle this?

**[2:15:00 – 2:15:05]** Well, it turns out that it depends a lot on the constant.

**[2:15:06 – 2:15:07]** We shouldn't matter, right?

**[2:15:07 – 2:15:17]** But it does depend a lot on the constant. So here I start with this concept so you can see that this is the function x squared plus rho times y squared.

**[2:15:18 – 2:15:21]** And you can see that I begin with row equal to 1 1/2.

**[2:15:22 – 2:15:26]** So it's almost a circle. It's like slightly elongated lips.

**[2:15:26 – 2:15:48]** When it's almost a circle everything. Where it's beautiful, right? So, I tried a few learning creates and one. Okay. So, one over 100 was a bit too slow, and they didn't go to all the way to zero. That's fine. Of course I can chose to learn create which is too slow. That's my hands, but large other increase. Just went straight to zero. It was all fine.

**[2:15:48 – 2:16:04]** So there is absolutely no problem and in actually, sorry it's not SGD here, it's just it's just creating descent right. There is no miniature. There are no mini batches, nothing is okay. So let me fix that.

**[2:16:06 – 2:16:10]** Ah, yeah. So just regular gradient descent that goes straight to zero. Everything works fine.

**[2:16:12 – 2:16:19]** But what if I start reducing Crow further? What if it's now not one over two but one hour 20

**[2:16:21 – 2:16:27]** well, what happens as I reduce Row the coordinates become

**[2:16:28 – 2:16:34]** More like their scale becomes more different. The coordinates become more imbalanced.

**[2:16:35 – 2:16:36]** so,

**[2:16:38 – 2:16:46]** For example, here row is, why changes 50 times slower than x?

**[2:16:47 – 2:16:56]** So what does it mean for gradient descent? It means that horizontally in terms of X. It's exactly the same though to zero. And we stay there. No problem.

**[2:16:57 – 2:16:58]** but, in terms of why,

**[2:16:59 – 2:17:03]** Well, now it takes a longer time to go to zero, right?

**[2:17:04 – 2:17:27]** But while I am at the level of 0.05, it's still quite possible. So, but now notice that, like, the the range of good learning creates begins to shrink, right? So before that for for a more or less a circle, it was fine. Unless they chose the learning create like actively to low but now 0.1 is also kind of slow.

**[2:17:28 – 2:17:34]** On this 0.5 gets gets to 0 into 200 iterations, which is quite a lot for such a simple function, right?

**[2:17:36 – 2:17:38]** and if I continue in this way,

**[2:17:39 – 2:17:41]** then pretty soon.

**[2:17:42 – 2:17:43]** Everything will be too slow.

**[2:17:45 – 2:18:09]** And here is the cage, so you could say a little bit. Why don't you just increase the learning rate, of course, for this function, you should go faster, but the point, the problem is I really can't because, okay, I can go from 0.5 to 0.9 or even 0.99, and yeah, it will get me a little bit closer to 0.

**[2:18:10 – 2:18:10]** but,

**[2:18:11 – 2:18:12]** I cannot go over one.

**[2:18:13 – 2:18:22]** Because if I go over one even a little bit, then the x coordinates starts to diverge, right? Because along the x coordinate.

**[2:18:23 – 2:18:26]** The coefficient is still one.

**[2:18:26 – 2:18:41]** So, of course, it's the problem is not that why changes slowly in absolute ways, that wouldn't be a problem. Of course, the problem is that X and Y are changing. It's very different rates. Excellent. Why have a very different scale?

**[2:18:42 – 2:18:45]** and at this point, even for something like,

**[2:18:47 – 2:18:57]** 500, 200 full difference between them. There's already know good learning rate for gradient descent. Even though it's

**[2:18:57 – 2:19:20]** So it's I tighter diverges? Or it just takes hopelessly long to go anywhere, right? So we can do 2000 iterations, then we will probably get there. Yeah, okay, we still 2000 deterrents, we will get there. But 2000, iterations of great of gradient descent for a quadratic function, starting from point one and three halves, and going to 0.

**[2:19:21 – 2:19:22]** Doesn't make any sense, right?

**[2:19:25 – 2:19:28]** So, here is the problem, right? When

**[2:19:32 – 2:19:48]** If even even in very simple case, yes, when the different variables in your optimization function, if in your set of variables from different variables, begin to different scale.

**[2:19:49 – 2:19:55]** When they begin to have different rates at which we should move along them.

**[2:19:56 – 2:20:03]** Everything kind of fails, gradient descent cannot have a unified rated, we should goes.

**[2:20:04 – 2:20:05]** and I think,

**[2:20:06 – 2:20:17]** Yeah, sorry this, this is next upload. So, so this is the mostly mostly. This is the problem that we are solving and we will go through several different.

**[2:20:19 – 2:20:30]** Ideas that people had well solving it, I will not. This is not a historical lesson. The ideas that we discuss are still real and useful. So

**[2:20:31 – 2:20:33]** Let's go through this idea.

**[2:20:34 – 2:20:47]** The first step and the first idea. Okay, so let me maybe, maybe, let's start with stamps 0. I will set up the notation first because I will reuse it all the time. So the notation is

**[2:20:50 – 2:20:51]** I go from.

**[2:20:52 – 2:20:54]** X k minus 1.

**[2:20:55 – 2:21:01]** 2x K. Okay, so I'm optimizing something like f4x.

**[2:21:02 – 2:21:10]** I have the vector X of variables and recently I went from XK minus 1 to XK

**[2:21:11 – 2:21:23]** I call this Vector UK for or you can minus one, I think. Yeah. So for the word update, so you can minus 1 is x. K, minus x k minus 1. It's my last update.

**[2:21:23 – 2:21:26]** And now I am a point x k.

**[2:21:26 – 2:21:29]** And let's say I have a gradient.

**[2:21:30 – 2:21:31]** GK here.

**[2:21:32 – 2:21:58]** So at this point for at this point, let's just assume that we are talking about stochastic gradient and this is not the true gradient. This is the stochastic estimate, or it could be a true gradient for, for what. I'm going to tell you now, it doesn't matter. So there is a direction that the gradient tells you. Maybe it's a simple. Maybe it's the true one for what I'm about to say. It doesn't matter. But there is a great interaction over here.

**[2:22:00 – 2:22:01]** so,

**[2:22:02 – 2:22:03]** classical SGD.

**[2:22:05 – 2:22:22]** Or GD or whatever would do it this way, okay? Plus one would be a SK last some Alpha times JK, right? So let me say that this is oh sorry minus, right? We are minimizing minus

**[2:22:23 – 2:22:27]** So let me say that this is already minus Alpha times g k.

**[2:22:28 – 2:22:44]** Minus Alpha times g k. And in the simplest example of SGD, this is X Plus 1. This is X K plus 1. And UK is just minus Alpha times GK. That's it.

**[2:22:48 – 2:22:50]** so idea number one,

**[2:22:51 – 2:22:52]** let's let's go over there. Yes.

**[2:22:53 – 2:22:57]** Idea number one is called momentum.

**[2:23:00 – 2:23:17]** Momentum, like, like, in school in high school physics, right? The impulse, the momentum of motion, what's the English word for that? Whatever? Okay. So the the momentum, which is like M times V in high school physics.

**[2:23:17 – 2:23:19]** What?

**[2:23:20 – 2:23:39]** How does it appear here? Well, let's go back to our picture. We had x k minus 1 and we just went to XK through a vector called UK minus one. And there is a direction that the gradient wants us to go minus JK

**[2:23:41 – 2:23:46]** uh, so the momentum method says, well,

**[2:23:47 – 2:23:57]** What, what are we really doing, like, what's the physical view of this? What what is the, what does it all mean? Well, it looks like gradient descent looks like

**[2:23:58 – 2:24:13]** Bow. Rolling down some kind of a slope, right? It's like a material point and it's on a slope. So it rolls down the direction where the gradient tells it to go and the steepest descent Direction. So,

**[2:24:15 – 2:24:24]** so, why don't we take this hint from regular Newtonian physics and why don't we actually apply it to

**[2:24:25 – 2:24:26]** Say.

**[2:24:28 – 2:24:37]** Why don't feel so add another physical thing from their inertia? Why don't we add this conservation of momentum here?

**[2:24:38 – 2:24:50]** Basically what this means is if your ball goes down the slope and the slope suddenly changes, then for a while, the ball will follow its current position, right? So it's it's gonna have some moment.

**[2:24:53 – 2:24:55]** a formerly, what it means is,

**[2:24:55 – 2:24:56]** When I am here.

**[2:24:58 – 2:25:01]** And I have come from here. That's why I was

**[2:25:02 – 2:25:04]** drawing the previous update too.

**[2:25:05 – 2:25:12]** I not only move along the gradient, but I also can serve.

**[2:25:13 – 2:25:15]** A bit of the previous update.

**[2:25:16 – 2:25:25]** So I also add some game times. UK minus 1. So this is the inertial motion. I follow the already existing moment

**[2:25:28 – 2:25:28]** and then,

**[2:25:29 – 2:25:33]** So, my final update will be the sum of this guys, right?

**[2:25:33 – 2:25:34]** So,

**[2:25:34 – 2:25:53]** Then I will go over here. This will be Escape plus one. So now Escape plus one is XK plus gamma times UK. Minus one, we carry over part of the update minus Alpha times JK.

**[2:25:54 – 2:25:55]** So, this is UK.

**[2:25:57 – 2:26:00]** okay, so we keep

**[2:26:01 – 2:26:24]** A part of the momentum. And actually, in practice, let me tell you right away that in practice with capability, large part of the momentum. So whenever you have anything momentum like gamma is, you know, 0.95, 0.99 maybe even more. So usually in practice you want to carry over. A lot of the momentum, there is little friction there should be some friction but not much.

**[2:26:25 – 2:26:26]** and,

**[2:26:28 – 2:26:29]** you just,

**[2:26:30 – 2:26:40]** Keep going the same direction. So what does it do? Why is it a good idea what it does is it keeps going forward.

**[2:26:41 – 2:26:42]** Along some Direction.

**[2:26:45 – 2:26:58]** Keeps going forward on some direction. And if the slope doesn't change in direction, if you are still, if the gradients still gets us to go in the same way then.

**[2:26:58 – 2:27:05]** I will grade you go faster and faster right? As the ball rolls down the slope, it will roll faster and faster to pick up speed.

**[2:27:06 – 2:27:12]** And this is exactly what hopefully is going to happen over here.

**[2:27:13 – 2:27:18]** um okay, I'll go to the picture later but hopefully what's gonna happen over here so

**[2:27:19 – 2:27:21]** Along the X Direction.

**[2:27:22 – 2:27:28]** the ball will go back and forth but then it will oscillate and stabilize some zero because

**[2:27:30 – 2:27:49]** In the X Direction, it's a steep slope, and pretty soon. We will go to the opposite part of the slope and back and back. So if you, if you imagine it as a ball, actually rolling down this Ravine and you will kind of intuitively see that, that's what happened.

**[2:27:49 – 2:28:00]** But along the y-axis, it will spin up, right? Yes, the slope is small. Yes. Why along the y-axis? It, it's not cheap. It's shallow but

**[2:28:02 – 2:28:05]** It's still goes and goes and you pick up speed as you go.

**[2:28:05 – 2:28:11]** So this is the original motivation and the idea for for the momentum approach.

**[2:28:12 – 2:28:17]** And let me immediately tell you the next idea, which is a small modification of the moment.

**[2:28:20 – 2:28:29]** Small. But actually very, very useful. Both theoretically, and practically. Very interesting manifestation. The second, the approach is called

**[2:28:30 – 2:28:34]** A Nestor of accelerated gradients.

**[2:28:40 – 2:28:52]** You can see the acronym neck sometimes or just Nestor of methods or something like this urinary for the Soviet mathematician who invented at some time in the 1980s.

**[2:28:52 – 2:28:56]** And yesterday's idea is really simple, and really great.

**[2:28:58 – 2:29:03]** So let's go back to this picture that I will not copy, it doesn't matter but let's go back to this picture.

**[2:29:06 – 2:29:13]** While. So what does the method of moment tells us? It tells us. Well, we are here now.

**[2:29:13 – 2:29:24]** And our next update has two components, the gradient component, and the momentum components. So we stand over here, we compute the gradient, and we get both components, and that gives us our update.

**[2:29:26 – 2:29:29]** Yesterday is this? Wait, okay. So we are here.

**[2:29:30 – 2:29:37]** And when we arrived here, we don't yet know the gradient so we should be we should get to work on calculating GK, right?

**[2:29:38 – 2:29:46]** But wait, but we already know the momentum part, right? So when we are standing over here after the previous update,

**[2:29:47 – 2:29:49]** We already know.

**[2:29:51 – 2:30:03]** Are part and maybe a large part. As I tell as I told you momentum's momentum can really pick up speed, we know a large part of the next update on radio.

**[2:30:03 – 2:30:06]** So why do we insist in Computing? The gradient over here?

**[2:30:07 – 2:30:08]** Why don't we?

**[2:30:09 – 2:30:13]** Go to this point which we already know, doesn't take anything to go there.

**[2:30:13 – 2:30:16]** And calculate the gradient over there.

**[2:30:19 – 2:30:25]** So this is negative Alpha times, let's say, G Prime K. Write the gradient computed at this point

**[2:30:27 – 2:30:28]** and then our

**[2:30:29 – 2:30:30]** new update will go here.

**[2:30:32 – 2:30:32]** Right.

**[2:30:33 – 2:30:54]** So, in Esther of acceleration, gradients, Escape plus one is XK plus gamma times. UK, minus 1, minus Alpha times, G Prime. Let me write it down. It's the gradient, believe it's the gradient, with respect to X of f.

**[2:30:55 – 2:31:01]** Note that point XK, but at point x k plus gamma times UK minus one.

**[2:31:02 – 2:31:03]** so, in this intermediate,

**[2:31:09 – 2:31:14]** And not what I meant. And this is the UK now,

**[2:31:29 – 2:31:29]** Sorry.

**[2:31:32 – 2:31:34]** Yeah and and this is the UK.

**[2:31:36 – 2:31:37]** so,

**[2:31:39 – 2:32:12]** What is like, what is the motivation behind this? Well, first of all, there is some beautiful mathematics behind it and actually gradient descent with this method starts to even converge asymptotically faster. It's some of the asymptotics change when you go from regular moment that's transformative. But we will not go there. The intuitive motivation. Is this Nestor of gradients basically do like a look ahead. They look forward in time and they

**[2:32:13 – 2:32:25]** It appreciate they try to predict what's going to happen and they update based on the future not based on the present which is, of course great. So if we are on a slope like this,

**[2:32:26 – 2:32:51]** Right? And a ball gets rolling down here so it picks up speed at speeds up and now it's here and the next step would put it over here. Right? So in regular momentum, you would continue speeding up because the slope is still in this direction. So, in regular momentum, you would go even further up. The opposite fold.

**[2:32:53 – 2:32:58]** Right. But in terms of momentum, you would look ahead over here.

**[2:32:58 – 2:33:04]** And you would see that. Now the gradient points in the opposite direction. So you are facing a wall in some sense.

**[2:33:05 – 2:33:07]** so, let's slow down say

**[2:33:08 – 2:33:09]** Say Siri.

**[2:33:11 – 2:33:14]** And that makes a lot of sense, right? So,

**[2:33:15 – 2:33:24]** That's that's exactly what makes it better.

**[2:33:26 – 2:33:28]** and if we look,

**[2:33:29 – 2:33:35]** At our example here. Now, now I can show you that picture previously, we're not old enough to see it.

**[2:33:35 – 2:33:41]** But now if you look at this picture, it's the same Alpha.

**[2:33:41 – 2:33:42]** but,

**[2:33:42 – 2:33:52]** Along with regular gradient descent. Also put here gradient descent with momentum, it's the orange line and gradient descent with an extra momentum, it's the green line.

**[2:33:52 – 2:34:07]** And you can see how the oscillations this x oscillations along. The x-axis are much much, much less, or much better contained, when Esther's momentum are used.

**[2:34:08 – 2:34:26]** Right. So again, this is the exact same effect, okay? So along the x-axis, the slope looks like this and the ball, the material Point rolling down. So it's like this, but looks ahead and starts slowing down before the turn, like a good driver, not like material.

**[2:34:27 – 2:34:29]** So okay.

**[2:34:30 – 2:34:33]** So this this is, this is what it looks like.

**[2:34:35 – 2:34:36]** but, of course,

**[2:34:37 – 2:34:38]** The idea didn't stop there.

**[2:34:39 – 2:34:39]** All right.

**[2:34:40 – 2:34:58]** And actually both the classical momentum method of momentum which dates back I think to the 1960s and master of gradients which date back to the 1980s. They come from classical, optimization Theory. They are not special to the appearing in any way.

**[2:35:00 – 2:35:00]** but,

**[2:35:01 – 2:35:02]** when you actually,

**[2:35:04 – 2:35:08]** consider the same kind of problems, but in the context of the planning,

**[2:35:09 – 2:35:10]** You.

**[2:35:11 – 2:35:16]** See the following like the following point. So in deep learning

**[2:35:17 – 2:35:20]** All that we have been doing so far.

**[2:35:22 – 2:35:32]** Was kind of defined and contained. In in just a generic, you can space of this Vector X.

**[2:35:32 – 2:35:34]** But I'm trying to.

**[2:35:35 – 2:35:38]** Convey the intuition. So like, for

**[2:35:39 – 2:35:42]** The method of momentum. All directions are equal.

**[2:35:42 – 2:35:47]** It does not treat X1 the first component different from a two different from extend.

**[2:35:48 – 2:35:50]** it will just

**[2:35:51 – 2:35:53]** add up some vectors in this space.

**[2:35:54 – 2:35:58]** but it turns out that you can do even better,

**[2:36:00 – 2:36:00]** If?

**[2:36:02 – 2:36:04]** You treat different components.

**[2:36:06 – 2:36:10]** Of X differently. If you for example, pick

**[2:36:11 – 2:36:13]** A separate learning create.

**[2:36:13 – 2:36:19]** And the separate changing learning rate for every component of x.

**[2:36:20 – 2:36:21]** When you do something like this,

**[2:36:22 – 2:36:25]** it's called adaptive gradient descent.

**[2:36:26 – 2:36:37]** Or actually, it's almost always stochastic because now we are in deep learning territory. So it's called adaptive stochastic, gradient descent and this kind of approaches.

**[2:36:38 – 2:36:44]** Are basically what we use in the learning. They are the optimization algorithms that you actually use in practice.

**[2:36:45 – 2:36:52]** So, let me walk you through some of them. Again, it will be like a line of algorithms but they will.

**[2:36:53 – 2:37:03]** Culminate in Adam of course and then but to get rid of, we need to discuss some ideas along the way.

**[2:37:05 – 2:37:05]** so,

**[2:37:07 – 2:37:08]** Adaptive.

**[2:37:10 – 2:37:11]** SGD.

**[2:37:12 – 2:37:12]** Radiations.

**[2:37:15 – 2:37:26]** Well, the first variation are called a the grid. It was the original adaptive SGD version a great just literally means adaptive gradient.

**[2:37:27 – 2:37:31]** The first variation worked like this, and the point was as follows.

**[2:37:32 – 2:37:34]** What do we actually want?

**[2:37:37 – 2:37:46]** For every direction in X. Like what kind of logic is behind choosing the learning rate and behind updating the learning rate.

**[2:37:47 – 2:37:58]** The logic is this, if you are on a shallow slope, like this one, and you basically go and go in the same direction, then you should go quickly, if you should go fast, right?

**[2:37:59 – 2:38:02]** But if the slope becomes steep,

**[2:38:03 – 2:38:06]** well, it cannot be steep for long, right?

**[2:38:07 – 2:38:11]** If the slope becomes cheap, it means the local Optimum was closed.

**[2:38:12 – 2:38:20]** So, if you land on a chips slope then you shouldn't carelessly jump further. You should slow down.

**[2:38:23 – 2:38:28]** And probably converge to the local minimum here. So that's that's the idea.

**[2:38:29 – 2:38:31]** How does a the great implement this idea?

**[2:38:32 – 2:38:35]** Well, actually pretty simple. So I will just write down the update rule

**[2:38:36 – 2:38:42]** X k plus 1. I so now, we are talking about one specific component in the vector.

**[2:38:44 – 2:38:49]** Is xki plus minus, right?

**[2:38:50 – 2:39:03]** Minus Alpha over the square root of G. Wait for it g. I plus Epsilon the ik Plus

**[2:39:09 – 2:39:11]** on time.

**[2:39:12 – 2:39:12]** G.

**[2:39:13 – 2:39:14]** K. I

**[2:39:15 – 2:39:20]** So, it's still, it's the same gradient. It's the same Vector of gradient.

**[2:39:21 – 2:39:27]** But the learning rate is now adaptive and what is capital cheap? Okay, capital G.

**[2:39:28 – 2:39:31]** Is the sum of squares.

**[2:39:32 – 2:39:40]** Of this gradients. So like gki is g k, minus 1. I plus g k i squared

**[2:39:42 – 2:39:44]** So, the capital G.

**[2:39:44 – 2:39:56]** Accumulates are all of the history of the gradients, and if there are large gradients, then capital G is large. And therefore, gradients are small and small.

**[2:39:58 – 2:39:59]** this kind of

**[2:40:00 – 2:40:17]** Corresponds to our logic, right? This kind of follows it. So while we are on a shallow slope, while we should be going fast, then we are going fast. So we start with a large Alpha with a high level high learning rate. So at first, we start off going quickly.

**[2:40:19 – 2:40:20]** and then,

**[2:40:20 – 2:40:32]** It goes down but while we are on a shallow slope GK small and it doesn't go down that much. So we are still working quickly along this line.

**[2:40:33 – 2:40:35]** then when we get to step slope,

**[2:40:36 – 2:40:39]** it means that the current G is high.

**[2:40:40 – 2:40:52]** And that means the capital cheek gets this High terms and it becomes large, it's self. So now the learning create Shanks and we go slow, that's that's the idea.

**[2:40:55 – 2:40:56]** Uh, what is?

**[2:40:56 – 2:41:01]** The obvious drawback of this idea. What is like, what cannot do?

**[2:41:03 – 2:41:03]** Well.

**[2:41:04 – 2:41:04]** I mean.

**[2:41:06 – 2:41:14]** If you look at the denominator and how it's defined and apps on doesn't mean anything, it's just so that we don't divide by zero. So Epsilon, it's just a small number.

**[2:41:16 – 2:41:21]** If you look at the denominator, you see that it grows with time.

**[2:41:23 – 2:41:24]** What it means.

**[2:41:24 – 2:41:25]** Is that?

**[2:41:27 – 2:41:28]** once we have been,

**[2:41:30 – 2:41:34]** On a step slope, there is no way for us to speed back up again.

**[2:41:35 – 2:41:39]** right, so if our optimization landscape looks like this,

**[2:41:41 – 2:41:42]** we are screwed.

**[2:41:42 – 2:41:45]** Because we go fast.

**[2:41:45 – 2:41:48]** Then we get here. We slow down.

**[2:41:49 – 2:41:51]** but when it becomes shallow again,

**[2:41:52 – 2:41:53]** it cannot speed up.

**[2:41:54 – 2:42:02]** Its denominator will never gets smaller, right? So now we are doomed to go in very, very slow.

**[2:42:02 – 2:42:04]** This is a bad situation for integrate.

**[2:42:06 – 2:42:21]** So what's what's the solution? The obvious modification would be to not use just the sum of gradients but to use some kind of recent history of gradients. So if we've had recently

**[2:42:23 – 2:42:30]** High values of G. Then we go slow. But if G has been for a while,

**[2:42:32 – 2:42:35]** Pretty small, then we can speed up again, right?

**[2:42:36 – 2:42:48]** How do you achieve that? Well, you could do something like a sliding window. But sliding windows are very expensive, right? To have a sliding window. We need to keep in memory, the whole window, which is impractical,

**[2:42:49 – 2:43:06]** So instead of a sliding Queen though, what we are gonna do is we're gonna do, I hope, you know this trick if not then it's it's very good that I'm telling you about it because it's a crucial trick, you know, all of a plate and computer science, exponential moving average.

**[2:43:08 – 2:43:08]** Am I?

**[2:43:10 – 2:43:37]** Ah, the exponential moving average, basically does this. Let me write it in this notation right away. So, gki is not the sum of J's, G squared. But it's like some coefficient gamma times the previous one, plus one minus gamma. It's a convex combination of the previous value and the new and, and the new value.

**[2:43:39 – 2:43:42]** so, what this actually means is if you just keep

**[2:43:44 – 2:44:00]** Opening the brackets, right? It's like gki comes with this coefficient and then it will be game times. One minus gamma times, the next, she came, minus 1, I squared and then it will become a square.

**[2:44:01 – 2:44:03]** Times 1 minus gamma times G.

**[2:44:04 – 2:44:16]** K. Minus 2, I squared and so on. Right? So it's like as we go further everywhere, will you that we want to add up?

**[2:44:16 – 2:44:20]** Comes with an exponentially decreasing coefficient.

**[2:44:21 – 2:44:25]** The gamma of course should be less than one. Otherwise, nothing will come up to it.

**[2:44:28 – 2:44:30]** And this kind of averaging.

**[2:44:30 – 2:44:33]** Has the properties that we want, right? So,

**[2:44:35 – 2:44:42]** Recent history is wait. Hi. Recent history has has a big weights and

**[2:44:43 – 2:44:45]** something that happened long ago.

**[2:44:46 – 2:45:03]** Far away. History has exponential is always so we kind of forget about it this time and unlike a moving Queen though the only need to store this value that's it. So only one really per parade not the whole window first so much more efficient.

**[2:45:05 – 2:45:16]** And if you take the grad and you replace capital gain, is this formula what you get is an algorithm known as RMS prop.

**[2:45:17 – 2:45:22]** And it's also one of standard approaches to

**[2:45:23 – 2:45:28]** wow, it's also one standard approach to

**[2:45:31 – 2:45:40]** To do in stochastic gradient descent, right? It was popularized by by Geoffrey Hinton at some point.

**[2:45:41 – 2:45:46]** But of course we don't stop there, right? So this this is also not the end of the story.

**[2:45:46 – 2:45:47]** Now.

**[2:45:50 – 2:45:54]** I will go to Aiden, almost straight away, but before I go to Aiden,

**[2:45:55 – 2:45:56]** Let me.

**[2:45:57 – 2:46:00]** Explain to you one more, like angle of looking at it.

**[2:46:01 – 2:46:13]** I think it's it's a pretty fun and instructive angle although the algorithm that results from it wasn't very good and it's not really used but they the basic idea of the motivation behind it. I think is really nice.

**[2:46:15 – 2:46:15]** So,

**[2:46:16 – 2:46:19]** The motivation behind.

**[2:46:21 – 2:46:23]** So the motivation goes as follows.

**[2:46:25 – 2:46:30]** We already discussed gradient descent. Yes, kind of

**[2:46:31 – 2:46:34]** Points rolling down. Surfaces blah, blah Etc.

**[2:46:36 – 2:46:44]** so why don't we keep looking at it from this physics perspective, why don't we actually

**[2:46:47 – 2:47:08]** Keep realizing, what? Keep pursuing, this physical connection, this metaphor of points rolling downhill because it's a very direct correspondence, right? It's the only difference is that both role. Continuum, continuous time. And here we are in discrete time. Otherwise it's the exact same process.

**[2:47:09 – 2:47:18]** So why don't we look at the measurement units of what is going on?

**[2:47:19 – 2:47:21]** And what are the measurement units here?

**[2:47:22 – 2:47:40]** Well, let's start with the gradient because that's it's, it's easier. It's much more natural to start there. So I want my gradient to be like the velocity right. My intuition is that derivative derivatives are velocities their speeds

**[2:47:41 – 2:47:46]** So, let's say that I want my G to be measured and meters per second.

**[2:47:47 – 2:47:51]** Okay, so G is like DF over DX.

**[2:47:52 – 2:47:56]** So this means that X is measured in seconds.

**[2:47:57 – 2:48:00]** And f of x is measured in meters.

**[2:48:00 – 2:48:11]** So the function is how far the point has gone. The x is the time that has elapsed and G is the velocity of the point.

**[2:48:13 – 2:48:13]** Okay.

**[2:48:14 – 2:48:20]** So now that we understand this, let's look at gradient descent and see whether it actually works.

**[2:48:21 – 2:48:30]** So migration the senses. Okay, I take my ex and I updated. Like this x is x minus some constant times chip.

**[2:48:31 – 2:48:41]** What about the measurement units? Well, access measured and seconds. This is just a constant dimensionless unit.

**[2:48:42 – 2:48:43]** And G is meters per second.

**[2:48:45 – 2:48:49]** So we are subtracting velocity from time.

**[2:48:50 – 2:48:52]** Which doesn't make any physical sense.

**[2:48:53 – 2:48:53]** Right.

**[2:48:54 – 2:49:05]** And when I say, doesn't make any physical sense, mathematically what that means. So, what means for us and practice, it. Exactly means that the scale of this variables can be very different

**[2:49:06 – 2:49:12]** So it can happen that your access are large.

**[2:49:13 – 2:49:33]** Here in absolute values and she is relatively small and in this case you would need like a huge Alpha to adjust for that or it could be the other way around. So the G is not scaled well to X it. It's our job to scale it basically.

**[2:49:35 – 2:49:41]** And physically, it means that the dimension the dimensions are on the units of measurement, do not match.

**[2:49:42 – 2:49:43]** Okay.

**[2:49:44 – 2:49:50]** so, okay, in the method of moments, it's the same what happens in say, 8, the grad

**[2:49:51 – 2:49:58]** In adagrad, we have minus Alpha divided by capital G times G something like this.

**[2:49:59 – 2:50:01]** So what are the units over here?

**[2:50:02 – 2:50:02]** Second.

**[2:50:04 – 2:50:14]** Mistress per second and g capital G is small Jesus squared. So it's one over meters squared per second squared.

**[2:50:16 – 2:50:16]** And square root.

**[2:50:18 – 2:50:18]** So basically,

**[2:50:20 – 2:50:25]** The unions can cancel out and we get that all of this is a dimensionless.

**[2:50:26 – 2:50:32]** So now we subtract from seconds from time. Some Dimension was constant.

**[2:50:33 – 2:50:35]** Which also doesn't sound, right? Okay.

**[2:50:37 – 2:50:38]** and,

**[2:50:38 – 2:50:41]** No tears. That

**[2:50:42 – 2:51:00]** Newton's method. Second-order optimization does not have this problem. This is also an important Point here. So if, if you recall that formula that we had about the second order method or something like x minus H, inverse time is G, right?

**[2:51:01 – 2:51:14]** So now, let's look at the units here. Now, X is in seconds. X is in seconds. Gee is a meters per second. What is h? H is the Matrix of second, derivatives its acceleration.

**[2:51:15 – 2:51:18]** So, it's meters per second squared.

**[2:51:20 – 2:51:20]** Inverse.

**[2:51:22 – 2:51:25]** Well, there you go, it cancels out. And on the second remain,

**[2:51:26 – 2:51:48]** So now the units actually match and mathematically, it means that Newton's method actually scale correctly. It gives you the local step-size that you actually want. So this is well, I mean, it's not the reason it's just illustration, but this is one good illustration for

**[2:51:49 – 2:51:57]** Why Newton, while second order techniques are better, right? So there they mentioned this match, they scale automatic

**[2:51:59 – 2:52:05]** And out of this, they're out of this idea. There came method called Aida Delta,

**[2:52:06 – 2:52:39]** Delta which tried to to do the proper units. And basically it was a great but Alpha here was multiplied by something like the square root of U and you was something like the sum of updates squared, something like that. It was not a very good algorithm, it didn't catch up catch on so you don't have to study at the Delta, but I think the basic idea is very interesting. The basic idea of having

**[2:52:41 – 2:52:49]** Of having the unit the measurement units of different things match.

**[2:52:51 – 2:52:59]** And with that, let's go to the real thing. They algorithm that people still use quite often

**[2:53:00 – 2:53:11]** Although there are alternatives. Now I'll mentioned that we won't go into the details of them, but I will mention them, but the most popular optimization algorithm in deep learning is Aiden.

**[2:53:13 – 2:53:34]** And Aiden was actually pretty similar to what we discussed with slight modifications. So it's like x k plus 1. I is x k. I minus Alpha divided by g k. I plus Epsilon. So far, it's more or less the same but times.

**[2:53:35 – 2:53:38]** M k. I not just G.

**[2:53:39 – 2:53:47]** And let me explain what this means. So, g k. I is an exponential moving average of

**[2:53:48 – 2:53:51]** square gradients.

**[2:53:52 – 2:53:57]** wait to times g k minus 1, I Plus

**[2:53:58 – 2:54:02]** 1 minus beta 2 times, gki squared.

**[2:54:03 – 2:54:04]** And M.

**[2:54:06 – 2:54:09]** Is an exponential moving average of the gradient systems.

**[2:54:10 – 2:54:19]** Beta 1 times M. Okay, minus one. I plus 1 minus beta 1 times, gki itself.

**[2:54:23 – 2:54:27]** And that's it. So basically, it's RMS probe.

**[2:54:27 – 2:54:31]** and the only difference from RMS probe is that

**[2:54:32 – 2:54:36]** we also smooth out the gradients themselves.

**[2:54:36 – 2:54:47]** So we are instead of using the actual instantaneous value of the test gradient, we are doing like this moving average over recent history.

**[2:54:48 – 2:54:55]** So we are smoothing the gradients. We are making them less, we are reducing their variants.

**[2:54:56 – 2:55:00]** You're making them less janky as be simple, different mini batches.

**[2:55:00 – 2:55:01]** and this smoothie,

**[2:55:02 – 2:55:07]** Has an excellent effect. It's it's what makes Adam works so well.

**[2:55:08 – 2:55:09]** So,

**[2:55:11 – 2:55:38]** Uh, so what else do I want to say about Adam? Well, yeah, another thing about Adam is that you really don't have to. I mean, it looks like it has a lot of hyperparameters. You got the beta 1 and beta 2 and also Epsilon, and looks like you need to choose them. Carefully etc, etc, which would be difficult but actually it's very robust. You can just keep the standard hyper parameters that

**[2:55:39 – 2:55:43]** They recommended in the original paper. I think it's something like this.

**[2:55:44 – 2:56:04]** Maybe 0.995. I'm not sure. But something like that. And Epsilon is just a very small constant like this minus 8 or something like that and basically it works. So you don't need to tweak beta 1 beta 2 in depth. So they can be just you can just take them off the shelf and a little bit fine.

**[2:56:06 – 2:56:07]** And Adam.

**[2:56:08 – 2:56:19]** Is a really good algorithm. It's so used. It's it's so pretty good. I don't think I can actually illustrate it to you here on pictures because you see the whole point of

**[2:56:20 – 2:56:50]** Oh sorry. The whole point of adaptive algorithms is to treat different components of the vector differently, right? And they shine when you have like lots of them high dimension and in this high dimension, there are some Dimensions that have this kind of behavior, this kind of optimization landscape other dimensions that have that kind of optimization landscape, etc, etc.

**[2:56:53 – 2:56:53]** and,

**[2:56:59 – 2:57:26]** I cannot do this in dimension too, right. I cannot give you an example, on a plane where X and Y, are wildly different. And, you know, there is a big difference between and RMS prop, not gonna work. I cannot give you an example like that. So it will definitely have examples like that in in Practical part and here I can. And as for the pictures, I can just show you some

**[2:57:27 – 2:57:30]** Nice pictures. Okay, so this is the problem again.

**[2:57:31 – 2:57:32]** Yeah, yeah, like this.

**[2:57:33 – 2:57:40]** I can show you some nice pictures but they don't really mean anything. So here is another like

**[2:57:42 – 2:58:00]** Standard function that has been a test bet of optimization and classical optimization Theory. It's called bills function, rosenberg's function. I mix up the two and it's basically let me find it somewhere. It's basically

**[2:58:01 – 2:58:14]** A complicated polynomial. Here it is. It's basically some some complicated polynomial. You don't have to memorize it. It's just some some kind of constant that are to be picked and such a way that

**[2:58:14 – 2:58:20]** It has an interesting optimization landscape. So you have this minimum over here?

**[2:58:21 – 2:58:42]** But around this minimum, you have like this very steep slope over here. You see how close the control lines are to each other, but then the steep slopes suddenly becomes a very shallows of. So it's like it's easy to go quick down this hope, but then you need to recognize it now, it's shell in to kind of speed up, which some algorithms really cannot.

**[2:58:44 – 2:58:46]** So this this is a good test test example.

**[2:58:48 – 2:59:19]** But in fact, I don't think I can actually illustrate real difference between Aiden and other adaptive variants. So here is what SGD does SGD goes. As, as you would assume goes in the correct direction, unless it diverges, completely. Of course, you can always have your learning create to be too high so that everything diverges, but if it's not too high then of course it goes in the necessary Direction and the faster you go the closer you get. But

**[2:59:21 – 2:59:28]** If you go too fast, you risk Divergence, so with SGD, it's always about finding the best learning rate.

**[2:59:30 – 2:59:40]** If you had momentum, you have exactly the same effects that we discussed. Right? So standard test gd, goes and goes but it's still has a long way to go.

**[2:59:41 – 3:00:00]** SGD with momentum almost left the base of this minimum at all most fail to over here. But thankfully it could come back but then it overshoots. The optimal by a long time by by far and as you can see this appeared on the right hasn't come back yet into 200 steps.

**[3:00:01 – 3:00:14]** While Nestor of momentum, yeah, it is already coming back. It's still not here, but obviously it's the best of the three. So it's, it's already coming back and it will be theirs.

**[3:00:16 – 3:00:22]** And that's for this algorithms that we discussed, like SGD is a great Delta. Well,

**[3:00:22 – 3:00:44]** they kind of do better but there is no real difference here. So, a Delta is worse but also, you shouldn't come to continuous about this and a great and Aiden they just both do a good job over here. So, there is no significant difference but as an illustration again, here is what optimization looks like Dimension too.

**[3:00:46 – 3:00:54]** It's not a good guide to vote optimization looks like in dimension 100 but for unfortunately cannot plot dimensional 100 for you.

**[3:00:56 – 3:01:03]** And before we wrap up, I think I have just a couple more.

**[3:01:04 – 3:01:07]** Things that I wanted to mention today.

**[3:01:10 – 3:01:11]** so, one thing is,

**[3:01:12 – 3:01:16]** Mmm, one thing is a version of freedom.

**[3:01:17 – 3:01:18]** It's the

**[3:01:20 – 3:01:24]** and again it's it's a version of Freedom that

**[3:01:25 – 3:01:34]** First of all is practical it. You can actually encounter it in deep learning practice. It actually happens.

**[3:01:34 – 3:01:56]** But also, it comes from a, very interesting, it comes from a very interesting motivation. So let me explain the motivation to you and then I will mention this. This version the motivation comes from a different way of doing regularization

**[3:02:00 – 3:02:00]** When you?

**[3:02:01 – 3:02:13]** when people did classical on neural networks, back in the day, back in the 1980s, back in the 1990s, regularization was usually done through this process called Wade, decay

**[3:02:14 – 3:02:19]** So what is weight Decay? What is the difference between regularization that we just discussed yesterday and wait till like this?

**[3:02:20 – 3:02:22]** In regular.

**[3:02:23 – 3:02:36]** Regularization part in the pan. You have like L of w being your loss function, plus something like Alpha times irregular eraser.

**[3:02:36 – 3:02:43]** And then you minimize your loss function with regularized, that's it.

**[3:02:44 – 3:03:03]** So notice that regularization like this, like L2 regularization one regularization, it's very, very easy to do in the blurry because all that you do is it's a slight modification of the Lost function. The algorithms don't have to change, just your computational graph gets a couple more notes and that's it.

**[3:03:05 – 3:03:18]** But in classical neural networks, they did a different. It, did it like this? So, wait, the K looked like this when you go from in your gradient descent, when you go from wkwk plus one

**[3:03:19 – 3:03:23]** before adding the gradient, you multiply

**[3:03:24 – 3:03:29]** you shrink the ways that you have, you multiply them by a constant list and one

**[3:03:30 – 3:03:30]** and then,

**[3:03:31 – 3:03:33]** You add or subtract?

**[3:03:35 – 3:03:37]** The current value of the gradient.

**[3:03:37 – 3:03:46]** Okay, so regularization. Why is it called weight Decay? Because weights, Decay a little and then you do your gradients.

**[3:03:48 – 3:03:52]** it looks pretty weird and actually

**[3:03:53 – 3:04:00]** pretty soon people realized that it's the same thing as SL2 regularization. When it over again, just send it. You can just

**[3:04:01 – 3:04:01]** so,

**[3:04:02 – 3:04:22]** Let's just continue this formula and let me write it like this. So it's a WK minus 1. Minus. What time double, okay? Right. I'm just pulling out the WK itself. Minus Alpha times UK.

**[3:04:24 – 3:04:31]** So and what is JK? Sorry, JK is the gradient of L.

**[3:04:32 – 3:04:34]** With respect to W at Point k.

**[3:04:35 – 3:04:40]** So why don't I take this part and just put it down to gradient here?

**[3:04:41 – 3:04:48]** Inside the gradient. So now I have WK minus Alpha times. The gradient of what

**[3:04:48 – 3:04:49]** Of L.

**[3:04:51 – 3:04:51]** and,

**[3:04:52 – 3:04:54]** Here, I have.

**[3:04:55 – 3:04:57]** Like some constant.

**[3:04:58 – 3:05:10]** One minus gamma divided by Alpha whatever that is times, just WK times, W Times W, right? Just the norm of W squared,

**[3:05:11 – 3:05:14]** And I need to do it at Point WK.

**[3:05:15 – 3:05:21]** So, when you look at this way, you see that weight Decay like this?

**[3:05:22 – 3:05:28]** Is exactly equivalent to just tell to regularization with a certain the certain constant. It's

**[3:05:29 – 3:05:38]** Completely equivalent, it's completely the same. So people kind of forgot about wait, okay, didn't use it at the beginning of the deep learning Revolution, but then

**[3:05:40 – 3:05:51]** People realize at some point, also a pretty interesting idea. That okay, so classical way decay in regular gradient descent is exactly equivalent to 12 regular eraser. That's true.

**[3:05:53 – 3:05:55]** but if you are doing something like Adam,

**[3:05:56 – 3:06:07]** If you are doing some complicated thing with momentum and cumulative, exponential, moving averages of gradients squared and so on and so forth.

**[3:06:08 – 3:06:10]** Then this equivalence doesn't hold anymore.

**[3:06:11 – 3:06:20]** Right now. There is no equality. If if the update rule is not that simple. If the update rule is actually say Aiden.

**[3:06:20 – 3:06:30]** Right. So what people did at some point, they carefully worked this kind of regularization through

**[3:06:32 – 3:06:33]** Adam.

**[3:06:33 – 3:06:34]** And they.

**[3:06:35 – 3:06:51]** Saw what to modify inside it and it was actually pretty simple to it. But you had to do the math to see where it is. What to modify inside. Atom to make it more like weight Decay than more than elsewhere regularization.

**[3:06:52 – 3:06:54]** And the resulting algorithm is called Adam w.

**[3:06:56 – 3:06:58]** And the popular.

**[3:06:59 – 3:07:03]** Gradients and variant. So a popular algorithm

**[3:07:04 – 3:07:04]** so,

**[3:07:06 – 3:07:26]** Okay, I I think I should be stopping here. So let me just mention, I didn't plan to discuss them and detail, but let me mention that of course the the research didn't stop on Adam and Adam W. There are recently developed algorithms like sealion and muon.

**[3:07:28 – 3:07:46]** And they have their own interesting properties. There is an algorithm one of them. I will keep forgetting which one that was obtained by actually automated search like the automated search that produced switch. Actually this fish activation function but for gradient descent algorithms. Why not?

**[3:07:48 – 3:07:57]** The other uses special properties of Transformers and this very useful for internal layers of language, models, whatever. So, the research continues, but

**[3:07:58 – 3:08:14]** Still. I think even in 2026 the standard algorithm would be something like aide or Aid in W or actually still very useful classical SGD. It's still, it's still a reasonable algorithm if you can pick the learning grid.

**[3:08:15 – 3:08:20]** So in conclusion, let me just quickly go through the slide to see what I've forgot.

**[3:08:21 – 3:08:30]** Okay, so this this is our example. This is Nestor of this is Uranus of for some reason, don't scale a lot.

**[3:08:35 – 3:08:40]** RMS probe Adam. That's what we just discussed.

**[3:08:40 – 3:08:49]** I made them. Okay, there is a, there is a version of Adam with Nestor of momentum called natum. Never heard about it afterwards.

**[3:08:50 – 3:08:51]** Etc. Etc.

**[3:08:52 – 3:08:58]** Then I will definitely skip this so fixing way. Decatur recognization item. This is Adam w.

**[3:08:59 – 3:09:12]** Https weight decade. I was very Decay, it has some good properties, which I don't have time to go into now and let me finish. Yeah, let me finish with this slide one.

**[3:09:13 – 3:09:16]** Like two, two last stories that both make the same general point.

**[3:09:20 – 3:09:22]** The first is the story of super conversions.

**[3:09:23 – 3:09:24]** Back in 2017.

**[3:09:25 – 3:09:35]** There was a very famous paper called super convergence that proposed to do a cycling learning creates schedule.

**[3:09:36 – 3:09:37]** What that means is.

**[3:09:38 – 3:09:54]** We slow down the training, we decreased learning create. And then at some point, we speeded back up again. So we go so slow. And then suddenly, We rise up again and do a large update and then we'll be sold on again.

**[3:09:55 – 3:10:19]** And they showed in some very convincing experiments. Of course there couldn't be any theorems about it, but they did and some very did some very convincing experiments and they actually showed that they can converge to approximately the same results, not better, but the same results, but much much, much faster, like that doesn't 10 10x 20x faster.

**[3:10:22 – 3:10:25]** And it was all the boss in 2017.

**[3:10:26 – 3:10:36]** But now we never hear about it. So say I click on learning creates are still a thing but they're not universally accepted and they probably are not going to use them in practice.

**[3:10:39 – 3:10:41]** This is one example.

**[3:10:42 – 3:10:44]** and the, after example,

**[3:10:45 – 3:10:52]** Also related to those stochastic gradient descent, which is why I'm talking about. This example here, the answer and example is a mass grad.

**[3:10:53 – 3:11:01]** It was a great paper in 2018 at one iclr 2018, best paper award, it was a great idea.

**[3:11:02 – 3:11:06]** So, they basically took the Aiden paper.

**[3:11:07 – 3:11:16]** Ah, in the Aiden paper, they had a convergence proof. They they couldn't estimate the rate of conversation but they had approved. The Tatum converges

**[3:11:16 – 3:11:17]** and these guys,

**[3:11:18 – 3:11:20]** Found the mistake in the proof.

**[3:11:20 – 3:11:27]** And these guys showed counterexamples where Aiden can actually diverged, where it does not converge.

**[3:11:28 – 3:11:34]** Where it doesn't work at all, right? And what's even better, they could fix it.

**[3:11:35 – 3:11:36]** They proposed.

**[3:11:37 – 3:11:40]** As a small modification of atom, called M as grad.

**[3:11:41 – 3:11:49]** That basically replaces like the sum with the max somewhere or something like that. I they algorithm is in front of you.

**[3:11:51 – 3:11:51]** and,

**[3:11:52 – 3:11:56]** For this algorithm they could prove convergence and the proof. Now was correct.

**[3:11:58 – 3:11:58]** so,

**[3:12:00 – 3:12:12]** They found a mistake in Adam and they fixed it and now you have four eight years. We've heard an algorithm, which is probably better than Adam.

**[3:12:14 – 3:12:18]** but my point is unfortunately, nobody is at

**[3:12:19 – 3:12:32]** I've never heard about anybody using, Ms, Groton practice. I guess you can use it. It's probably implemented to know the libraries. I guess you can try it. It'll probably be either exactly the same as Adam or even worse.

**[3:12:33 – 3:12:37]** So, let me close with this slightly disappointing point that.

**[3:12:38 – 3:12:53]** Even good ideas even ideas that get confirmed by your experiments that get confirmed even by Theory. So the theory is correct. There is indeed a mistake in their paper and this paper does not have a mistake this paper that did fix it.

**[3:12:54 – 3:12:57]** But unfortunately, it's not enough.

**[3:12:58 – 3:13:23]** To get a new universally accepted algorithm. It's still still practice is the final Arbiter, still? We like, we as a field are very applied, very practical filter, artificial intelligence, deep learning specifically. So ultimately people are going to use what works and Adam still works.

**[3:13:24 – 3:13:24]** so,

**[3:13:25 – 3:13:30]** with this, I want to stop for today. Are there any questions comments discussion?

**[3:13:36 – 3:13:41]** Okay, thank you. Yes, of course, I want feedback about the lectures. Thank you very much.

**[3:13:42 – 3:13:50]** I'm a bit surprised that gradient descent and back. Proper new for you, but good, then it's good that we repeated it. Okay? Wonderful.

**[3:13:51 – 3:13:53]** okay, thank you very much and

**[3:13:55 – 3:14:04]** with that, I pretty sure you're tired of listening to online lectures for three days straight, I would be definitely. So it's a good thing that I

**[3:14:05 – 3:14:15]** See the floor to Alex. Whom you will meet tomorrow and he will have practice starting tomorrow. Thank you and bye. Bye. Good question. Yeah.

**[3:14:17 – 3:14:38]** So are we next week? We're going to continue this online, lectures. That is a good question. Yeah, yeah. So that there is a scheduling there are scheduled in difficulties for me personally because I'll be traveling next week. So I hope there will be if you'll actually next week but at this point I cannot promise wish they

**[3:14:39 – 3:14:39]** okay.

**[3:14:40 – 3:14:41]** so, I think

**[3:14:43 – 3:14:45]** I think our plan for now.

**[3:14:46 – 3:15:00]** Is like tomorrow, definitely is practice day tomorrow is our top practices and then hopefully I will have one, we will have one practice in one lecture on Friday and then next week is wide open. I don't know about next two kids.

**[3:15:06 – 3:15:10]** Okay, thank you very much and bye-bye. I will upload everything as usual. Bye.

## Full text

Good morning, everyone. We continue. our investigations of machine learning and yesterday, we Finally got the neural networks. We got to our main topic of the class and we will we will be discussing neural networks for the rest of our time. But still I'm glad that we went over some fundamentals and I hope they have been interesting and attractive for you. so maybe just as a quick recap first, what we did here today and where we are right now, so, we are discussed yesterday, we discussed things like linear models, but basically Linear models or more complicated classical machine learning models like I don't know regression tree boosting or gaussian processes or some probabilistic models which some, I don't know, variational clustering or whatever. All of this models, followed classically. The same Pattern followed the same structure. So you have your high-dimensional input, like image is sound videos, whatever. Then you do feature extraction, right? That's we discuss that yesterday. Then you get something like a vector of features and then you do your ml model. Right? And the whole point and the email model. Now, gives you the output, which you need. It's the why. And this is the X. so, Classical models in classical machine learning, what people would do, they would think and do feature extraction menu. Are and the main advantage of deep learning when it came on in by now we have many more advantages but the main Revolution like the contents of the deep learning revolution of the plate, 2000 to 1010 was that this manual feature extraction, switched to end-to-end learning of a single model, which was the neural network, right? So, now in deep learning mostly, this is all a big neural network, right? and when we, When we implemented, when we run it it's just a single thing. We don't need to distinguish but inside of course there is like the first part, the main part that still does the feature extraction and then it produces the semantically relevant features, the features that are By virtue of training, the most meaningful features for the output that we want. And then we do the final layer, which is again, one of these linear models. Usually either linear regression if we predict a number or logistic regression if we, A dual classification as we actually usually do some somehow. It's it's rare to have numbers as outputs. We will have examples like that but it's not really common. so, Then what, what else we did yesterday, we started talking about the structure of neural networks, but the only started, and we only started talking about like individual Perceptions in individual. Artificial neurons. So and this this was I think where we stopped. We discussed the Common structure of a single unit in the neural. Net worth of the perceptron is a linear combination of the inputs. Followed by an online linearity. and, I think. Yeah, so I I think we didn't do yesterday, we didn't do like a real survey of this functions of activation functions, but it's it's a pretty short topic and let's just get it out of the way now. So what kinds of activation functions can be used in neurons? So, like again, we just discussed yesterday that the whole point of neural networks is to take structures like this to take small Elementary functions like this and then do like a computational graph based on them. Right. And when you do a computational graph based on, Elementary functions that. You understand Elementary functions that are easy? When you do compositions of easy things? Like we discussed with this connection isn't principle, which is basically just true when you compose a lot of simple things, you can get some very complicated results. Of course, the question is, how how do tweak your composition such a way that they? The result is what you want. And this is the whole point of deep learning, right? Training such big compositions, finding their weights, learning their weights. but, at least theoretically, as soon as you have any kind of nonlinearity here, you can more or less approximating anything you want. And so, our first topic for today, brief one will be, what are the nonlinearities that people actually use? and it's It's an interesting question. Actually it's like more a bit more interesting maybe than you would expect. So originally in, I don't know in 1943, in the regional McCullough, it's paper and a 1958 in France. Was perceptron people use threshold functions So the activation would be a threshold heavy side, step function called it what you want, but basically there would be an A and the rule would be, if W Times X is over a then 1 L 0, right? This is a fine function, if all you have is a single perceptron and it's okay, you can do a learning on this and everything more or less works and that's how the perceptron the original perceptron worked. But you can't really do networks of these guys. Right. So I told you yesterday that you can't do networks of linear perceptrons, because if the pressure transfer linear, then it doesn't make any sense to do a network. A composition of linear functions as linear again, so you just get your whole network equivalent to a single person. Well, with this guys, it's not true. Is this guy's there are like Universal approximation theorems. You can definitely approximate whatever you want, but you can't find this approximation unfortunately because the only way we have to train such big composition that's that will be our main topic for today. Actually. The only way to train such compositions is gradient descent and other techniques that are based on local movements of the weights, right? On on local properties of The last function. And when you have a piecewise constant, actuation function. Gradients don't work. I mean formerly they work but they're just equal to 0, right? They F Prime is equal to 0 here F. Prime is equal to 0 here. And when when you see it over here with your W Times X and you move to your W slightly, maybe you go here, maybe you go here but the answer doesn't change and the derivative is always zero and we don't know where to go, right? So this guy is definitely don't work for from Networks. So what did people do? People are looked at this threshold activation. They still had this idea that Threshold, activation is supposed to be good at threshold. Activation is like what we are actually trying to achieve. Like a neuron is either activated or not and we want to have a big composition of neurons that are in various states of activated or not activated. But we cannot have this straight jump, so let's have a soft approximation. so, for quite a while throughout all of this classical phase of early neural, networks up until 2011 or 12, I think mostly people used sigmoid activation functions. And when so when people say a sigmoid function, what they actually mean is that there is a There is an asymptote, a horizontal asymptote on the left. There is a horizontal asymptote on the right. And the function monotonically goes like this from negative Infinity. So they preverbal, the example, the archetype of example of a sigma, it is logistic Sigma which we discussed yesterday. So Sigma of a is 101, plus e to the power minus a, it goes from 0 to 1. It's a metrical, it's it doesn't have 0 derivative of anywhere. Etc, etc. and, so, there have been there was a lot of, there were a lot of neural networks in the 1990s 1980s with Activation functions like this. And also with other Sigma it's so I won't go into details. It doesn't matter for us now. But for technical reasons, it's not really good that your sigmoid saturates at 0. So it's, it's, it's a separate technical problem that you don't really want to like, approximate zero, so a better signal it for at least internal layers would be something that those from one to say, minus one. Right? And and then it would be symmetrical around zero actually. So, and actually more common sigmoid function for for neural networks for was the hyperbolic tangent, right? I always forget where the minuses are eight to the power, minus a minus Plus, I guess like this. so, it's the I guess it's like this. Yeah. So it goes to, it goes to one on positive, Infinity. It goes to minus here, right? That goes to minus 1 negative infinity and again it's symmetrical, blah, same kind of So, people were using this sigmoidal functions all the way through about. I don't remember the exact year, but about 2011, or 2012? and, in 2011 to 2012, there was a very influential paper, very important remark that where people try a completely different activation function. A very, very simple one and it turned out to work extremely well. so, the function that they tried is called ryloo, Which stands for rectified linear unit. and, Linear unit and it basically goes like this. on the Uh, so on, on the negative part of the inputs over here, it's just zero. and on the positive part, it's just X. It equals to the input. So I really of a is you can like formally. You can write it like Max of 0 and a or you can write it with one Boolean operator, right? So like one if a greater than 0 L. 0 that's it. Sorry not won a a greater than 0 L 0. That's it. and, It proved to be a very cool, very nice activation function. So what were, what are the benefits? Well, first of all, I just told you that it's now good to have. Piecewise constant activation functions because the gradients are 0. and indeed, if you go through a real, if you go through a neuron through a unit with real activation and you have a negative, Argument for you. So if you're W Times a false over here or W Times x Falls over here, then you don't learn anything right so it's just straight 0 it propagates a 0 and when you go back your gradient, stop there we don't have know what it means to go, but we will understand it just now just today. and, but But in this case, it's okay. So in in many architectures, it's okay to have this kind of sparsity, and it's even a good thing to have this kind of sparsity. So in, for example, conventional architectures, which we will discuss. I suppose in our next lectures in conventional architectures, you have the same ways to reuse a lot of times. All acrossed input. And when you have the same way, it's used all across the input. It's fine. And it's 7:05 to have like half of them. Just Zeroed out. So that that's not really a problem and it turned out that It's really a good property to have unbounded activations like this. So, With any kind of signal. It's you have this problem of situation, you have the derivatives of your activation function, go to 0 on the left and on the right here, the rest will go to their own, the left immediately. But on the right, they don't. And this means that this Sigma know Sigma, it can distinguish between like activated really to it and you producer activated, it just activated And what's even worse? When you go to this regime, when you're inputs, when you're sigmoid becomes, when you're neuron becomes, very sure and what it does when the arguments to the sigmoid become large and absolute value and you stop hearing, so your derivative are very close to 0 and the gradients just stop Here you explicitly stop on the negative side but on the positive side you never stop you just you keep learning which is also great. So in a way it's and there is even a mathematical result about this, I don't remember if you have it on the slides, maybe I do. You know, let me skip this situation functions. Yeah. And there is even a mathematical result that says well if you take a few Sigma it's and you stack them together, I can infinite series of Sigma and use them together. What you get is more or less. The real. So like, if you add up this series, of course, you don't get this exact ink at 0. Of course, it will be smooth, but then, it will very soon. Asymptotically, be just like that. It will go to straight line and it will stay being straight line. So, in a way, the real situation is like staking a lot of Sigma. It's and looking how many of them actually activate which is, of course, more information, right? So this this this is a good thing. What else do I want to say here? Yeah, so oh, and there is yes. Sorry about the Russian on the picture. But there is also a very interesting remark here. That connects back to what we discussed yesterday about the brains actually, if you look at how our biological neurons activated, it does look like a real activation function. So this is like a good model or whatever of, of the firing rates of neurons, basically of their activation strength. How well how, how much their excited. And it looks like this black curve over here. So at first, so it doesn't go negative of course. But then from 0 for a while, just state stays known inactive not activated at all. Then there is this complicated phase transition, but after the complicated phase transition. We basically get a straight line. Which is. Pretty cool. I mean, it's it, it's pretty interesting and expected. It would be actually a straight line but looks like it is Are of course, it doesn't go to Infinity. Please do not experiment with that. Know, if you apply 1,000 volts to your brain, you will not think faster and better and this will not end well, do not do that. Of course, it's actually it's in real life and biology, but in the computer doesn't have to situate or at least it. We can stretch this straight line, however far we want. So and of course, this are just additional considerations this. These are, this is just, this is just some interesting facts. About the real, of course, the real bonus was that it worked very well. So in practice as soon as people, it wasn't a new idea, real activation existed since 1976 or something. But as soon as people tried them, with real networks, with convolutional networks special and they saw the results in about 2011, to 1012 are mostly everyone's finished the rules. Of course, it did not stop there. So there has been a lot of further restoration activation functions. There have been interesting results. So What what what was what was the next step? Well. The first. Next Step was kind of straightforward. So I said that in some In some situations, it is desirable to have this participant in some situations. It is a good thing to It is a good thing to zero out some of the activations over here, but in other situations it's not. And when you don't want to lose the gradient flow through your network, when you don't want to be sparse, then of course you you'd want something non-zero and the left. So the immediate modification was what we call a leaky real. Basically the same thing, but on the left, you have a straight line. But it's it's a straight line, which is, which has a smaller slope and on the right. So it's still just a single hinge, a connection of two straight lines, but at 0, but now it's non-zero on the left. are, and then, and then, What people did at around 2017? I think was this, they they ran an automated search for the best possible activation function. And I do want to discuss this a little bit because we will see examples like that later also. so, if you look, At your activation functions. What are they like, what is their nature? They are just straightforward. Mathematical functions of one variable, right? Just a function in the high school sense of the world, and, What is the representation of this? How do you represent functions? How would what is the structure of this, guys? Well, their defined by formulas, right? And what is a formula formula is a computational graph so, for example, how does Real. Look, what does real look like? Oh, you have your input X. You have a constant zero And then you have a maximum. And you have your output. Okay, very simple computational graph, two inputs, one of them constant and that's it. What about the logistics segment? Well, you have X, you have one. You have, for example. And I mean, I'm just making an example. You can Define functions in different way, but for example, here, there is a urinary function, e to the power minus argument. And then there is plus one, and then there is the inverse, right? Go one over. And as a result, you get Sigma effects. For a hyperbolic tension, you have X, you have e to the power, you have it to the negative power and then you subtract and then you add and then you divide. And you get your hyperbole attention, right? And so on. So a function, if you write it as a formula, what the formula actually is, what what is a formula, is a mathematical object, that's a graph. It's a graph, composed of Elementary functions of operations, that constitute this form. are and which, which means that you can Sweep over this graphs, right? You can search through these grows. I won't go into details on how exactly people do it. It doesn't matter for our class, but basically, At some point, they ran a very expensive search over a lot of graphs. A lot of activation functions like this. Of course, when you do a search like that, you cannot actually prove anything. There is no mathematical statement, it's all empirical, right? So you just try different stuff. You see what works better on the set of data sets set of architectures that you that you set up. And then you just see what works better, right. And you see what works better and you. Progress by mutating the graphs a little bit. It's basically an evolutionary thing. Usually because you can't take a gradient on the graph structure. So you need to do like crossover, like, copying parts of one graph to the other or small mutations, like, change around things. See what works. Go to the population of things that work, etc, etc. It's it enabled us. Um, and as a result at that point, they came up with something called The Switch activation function. Yeah, 2017. It was done by Google, of course, whales would have all of that compute back in 2017. And this fish activation function. I mean I cannot explain to you why it is better. I can only show it to you and say that the empirical it's better. So it looks kind of like a leaky real or so it's very similar to real on the right and they are all very similar to real on the right and on the left it at first goes like this, but then it goes back to 0 so it's not monotone interesting. and yeah, it proved the work better for some reason and a lot of standard architectures is in computer vision. Actually, you will see if you go inside. We won't go to that level of detail thinking class, but if you go inside, will see that a lot of standard architectures actually use swish activation. And the course that is not the end of the story. So, let me maybe, I don't want to spend too much time on that but people keep doing that. Yeah, this is our experiments for Ah, yesterday. Yeah. So I I will publish this an old book as usual. These are the standard activations like threshold Logistics Sigma hyperbolic tangent and the reload and then you have differently careers which are all the same on the right. You have exponential linear units which which is basically again a straight line on the on the right. And on the left this asymptotically going to somewhere curve. Then you have switches, you have Mich, which is a variant of fish, whatever doesn't matter. And then, okay, let me skip that and then you have this all. So pretty interesting function called the glue which where she stands for gaussian and the gaussian function is based on the Cumulative distribution function of Central Coast. So, it also looks pretty much like a swoosh. but, It's a little bit different and again, so you can see the, the formula here. It's it's basically just the CDF of gaussian and It's CDF from gaussian times x. Yes. Sorry and it's For some reason, it works better in many modern architectures so I guess modern Netherlands, mostly use chill work durations. They're probably maybe there is a deep science behind it, but I'm just not an expert in that just wanted to mention that people are still working on ideas like this. Okay, so But all of this is just and in a way, just in this part. I just want to show you how that all rabbit holes go deep, right? So wherever you look, you can find a long series of works. You can find a lot of different ideas and for every idea you will see some confirming experiments. Of course. Otherwise don't be published. Some may be even theoretical reasoning of why this idea is good. But then you know some ideas work out some ideas disappear and over here for Activation functions there was this like use a different color. There was I guess the the sequence of activations that you actually want to try is like really then swish. Then maybe gilu with the gaussian linear unit and maybe a leaky real is a variation. So let's let's get very difficult stands. Okay, don't want to spend more time on that. what I do want to spend a little bit more time on is of course, that propagation. so, Let me first motivate what we are going to talk about and I know back propagation is pretty simple. It's pretty straightforward. It's a specialty compared to what we've been talking about yesterday and the day before. But I still want to discuss with at least very quickly to because there is one or two points that I want to make in there and also well I think it's it, it's worth. Reminding you about back propagation? so, First of all, what problem are we solving? Where where does back propagation come from? Well, as we already discussed. Sorry, as we already discussed. A neural network is basically this huge function. Let's guess so far, it's a small left, but this huge function which computes actually not even the output but the function that computes the loss function for some input, right? So there are weights of the neural network, this, they constitute part of the inputs. There are inputs, like, like inputs inputs, like the, the picture that we are classified or whatever this is X, and there is the correct answer, which is why. And the final output when neural network on that would be the value of the Lost function, right? So here, it's still smaller. Small L on our x y w, right? So for example, if you are Distinguishing between cats and dogs. What you actually do is this is your X Y is the cat class. So it formally it's like well. Okay, since they're only two classes, let me just say it's one as opposed to 0. If it was a dog it would be 0. and then, Your picture, your input image goes through a very complicated neural network and this very computer complicated. Neural network, gives you like why hat? It's pretty dictionary. And probably there was which is logistics sigmoid at the end as we discussed yesterday. But anyway they output is why hat which is like the estimated probability of the cat class, right? And then you can take the gradient of that because you don't know where to go to know where to go. You need to also combine it with the correct answer. And then here you compute the loss based on the prediction of your network. And based on the Uh, based on the correct answer and the output. In this case would be something like minus log, y hat, which we are supposed to minimize. So that y hat would grow and would be closer to one, right? Minimize with respect to what minimize with respect to the weights, right? So this neural network has weights inside. The loss function probably doesn't have rates inside but the neural network does have weights and we want to minimize it with respect to double. And that's all not the end of the story, right? And in machine learning, we don't have only one data point. We have lots of it data points, we have a whole data set so the actual was function like L capital, L of w. Now, it's just of w naught affects and why specifically is something like the sum or the average? Doesn't matter? Of course, we're just maximize or minimize in. So it's the sum or the average of this small loss functions for every Element in the data set, right? So when we train We? Are minimizing the average loss function on the dataset. And it makes sense. Maybe we have some weights inside, maybe it's a bit more complicated. Maybe some samples are more important than others, whatever. For now let's just stay simple. We want to mix the minimize the total loss of over the whole dates. so, we are minimizing this with respect to the How do we do that? So I hope by now, I've convinced you that this loss function is a very, very complicated function of w. I mean we didn't even go into any architecture here but every architecture is also if you composed of different stuff but Even in this formula you can see that it's like a sum over the data set. So it's a sum of million terms and every term is a pretty complicated function. so, L of w is Very complex. In practice, there are a lot of WS in the length of the W. Vector is Big. We are operating on high in high Dimensions almost inevitably and um, sorry. Yeah. and, The L of w is hopelessly, non-convex, is hopelessly complicated. And we definitely cannot hope to. I don't know. Enumerate. All possible W's. And look for the minimum, or to do some complicated procedure here basically, Almost anything. Almost all that we can do is to do some form of gradient descent. I will tell you later today, why even slightly more complicated things fail, but the only base, basically, the only thing that works is to do gradient descent, which means update the weights local there. With a role like this one. So I want to make I want to make a capital l smaller so I am at point w. Okay. On iteration K have the current checkpoint of the model and its weights are WK. So to get the next value of the weights to get the next checkpoint. I subtract I go in the Direction slide, oh, slide I go in the direction opposite to the gradient. So, in the direction, where the loss function, decreases, the quickest, I hope, you know that. All right, all right, so I want to go over here. I compute the gradients, the gradient at Point WK. And then I Go slightly in the direction of this. Largest of this most steepest slope downwards. This is the idea of gradients. And today we will see how it has evolved and where, where we are with creating the center today. But The basic idea is still this. And what do we need to do to implement an iterative procedure like this Implement actual gradient descent? Well, if you look at the formula, he will see that. The only thing that we really need to do is we need to be able to compute the gradient. That's it right after it's easy. So, we need some kind of algorithm, we need some kind of procedure. To compute gradients of big complicated functions. Well, we can't have a generic procedure for any function with, however, it is defined. But how is L defined? Like, what is, what do, I mean? Actually, physically, when I say a big complicated function, well, in neural networks, in deep learning a complicated function, is defined also as a computational graph Right. So what I actually have here. Is some kind of. So, I have X all of this different texts from the data set, and the wise and whatever. And they go into this impossibly complicated graph. But it's a directed a cyclic graph that just does the computation from left to, right? And we go through it and we can compute stuff. and then, L. It falls out, right? So, the Assumption here is that this is a very big composition. But every element of this composition, every note in the graph is simple. It's simple enough to take in compute, its values compute, all of the derivatives locally in the node. Do anything I want inside the single node, okay? So the single note is some kind of an elementary function. For example, for example, this this is a note, right? So it's just doing this dot product between two vectors very simple function, I definitely understand what the derivatives are, what they really is blah or here is an activation function which is a fixed known function of one variable. And of course I know it's derivative to So I assume that my very complex function is computed through a computational graph of simple functions. And my task is. Let's compute the gradient of this guy with respect to a part of the inputs. I didn't actually put the weights here but they are also Somewhere over here and they're also part. They're also part of the inputs for this computational graph. And I want to compute this, add some specific point numerically. So bad propagation is a way to do that, that's basically it and to explain back propagation. I think it's best to just go for an example. so, let's I don't know, you can, you can give me some kind of, you know, polynomial of two variables. Usually, that's enough. Give me an f of x and y. and some Relatively complicated, composition of of simple things like classes, squares, multiplications. I guess I'm not. Making myself clear. What what I want to see here but something like and okay, let's pull something out of X Plus y Square now times. X squared plus. Why? Plus X Y, maybe something like this and it doesn't, that's doesn't work too well, X Plus y squared times. X. I okay times x, minus y, plus y. Cubed or whatever. Let's, let's put it this way. I doesn't really matter. So we have this kind of. Okay, so for our example, we have this kind of function and I write it as a formula which means that I write it as a graph, like we just discussed as a computational graph with Elementry functions like plasma squared Etc. and, So let me draw this graph. Yeah. And my question will be, I want to compute the gradient of f. So I want to compute DF over DX and DF over d y. Okay, that's that's the question. Let me draw the graph for you. So I have. I'm used to drawing it. What comes up? So here I have X and Y. What do I do? I do it. Plus over here, I do a minus over here. X minus y. Right, I do a cube over here. Then I do a square over here. Multiplication with the minus and then I add the cube. Okay. So let me maybe go through this graph and put some letters here. So, like let's say a is X Plus y. I want to denote the intermediate notes Here. The outputs of intermediate notes. So, B is x minus y. C is y cubed. D is a square. Oh perfect. E is D times B. And F just like f. Right is e plus C, Okay? So Notice what we've done, we've represented this function as a graph, which is exactly the same as a formula. When you write down the formula, you are actually All right. Now a graph like this one and every single function in this graph. Is very, very simple, right? We know everything about, you know, taking the cube. We know what the derivative is, we know what the result is, every function is simple, But we don't yet know, let's say, what is the global result of f? So, what can we do with this graph? Well first of all we can use it to actually compute stuff, right? So we can for example I don't know let's say x is equal to 1. Y is equal to I don't know minus 1. What will be the what what will be the value of? And we can go through this graph button up and compute every note and we compute. If just like we would go through the formula, right? So in this case, a will be 0. B will be two, will be minus one. D, will be 0, okay? So easy, but still okay. He will be also zero and there will be minus one. Okay. What else can we do? And this procedure, when we go bottom up from the inputs to the output, this procedure is called forward propagation. So, forward propagation. Or. F probe. is when you go from the inputs to the output, right, but bottom up in this graph, And with forward propagation, of course, you can compute the value of the function, that's very straightforward. Interestingly. You can also compute it. There is for propagation. Isn't that right? So, for example, Let's say, I want to compute DF over the X. How do I compute jfa for DX while going Bottoms Up on this graph? Well. By induction. Right? So I have the base of the induction which says the X over DX is one d. Y over DX is 0. Okay, now I go here and they say, oh what is the a over DX? Well, it's since this is a plus and du over DX is DX over DX, plus dy over DX. So it's one plus zero, it's one And, and so on DB over DX will be. 1 minus 0 will be 1. DC over DX will be 3 times y squared. Oh, sorry, I'm doing DX will be zero apologize. This over the X, will be three y squared, times d. Y, over the X and the Y over the x is 0. So that will be 0. Now d. D over DX is 2A times the a over DX. Right. And okay. So let me maybe sorry, let me change this example, because all of these zeros will not be really interesting. So maybe let's say, maybe let's say x is 2. And why is minus 1? So here, we have minus 1. Here, we have three here, we have nine here, we have, I will start. Here, we have one. I'm bad at arithmetic. Here we have one here, we have three, one times, three, three and three. Minus 1 is 2, so we don't have a graph full of zeros. Okay, so DD over DX is 28 times, the a over DX and du over DX is 1. So it's like 2A. So it's two times X Plus y. If you write down the formula, Then the E. Okay, so D over DX, let me write it down. Here the E over the x e is a product. So How do you differentiate the product? It's the D over DX times B plus DB over DX times d, right? So, that will be DD over. The x is 2 times X Plus y times B, which is x minus 5, right? Plus DB over DX is one. Times D, which is X Plus y squared. Okay. So that this is going to be the over there. Now, the F over the X. Finally, The F over DX is just the E over DX plus DC over DX, right? And we know all of this guys. So this here over the x is 0 and D over DX is this So it the answer is. X Plus y squared, plus 2 times X, Plus y times, x, minus y, you can open the brackets doesn't matter for us. It sounds about, right? So if you just look at the formula and you do it in your head, what's correct? Of course in practice, you wouldn't be able to drag the formulas with you. So in practice, what you would actually do is you would compute the numerical values of this derivatives. So you would go like You would start with one and zero. And then here, it's all so 0. Okay. So here the formula in the values, the same here. Also, one is both the formula and the value and here also. But here you would not have a formula, like, two times X plus 5, which just have the numerical value. And actually what you would, what you would do in, if you were implementing it as an algorithm, you don't know, excellent, why? When you are inside the note, what you do know is a You know, this input that went here from from a and a was equal to 1. So we can just stop at this point and say that the the derivative here is equal to 2 Okay. And similarly here, what we actually are Computing is Didi over DX, which is 2. times B, the value of B, which is 3 It goes here. Plus DB over DX which is 1 times the value of D, which is 1. So we'll get something like seven here. And then we would add 7 and 0 and gets seven and I suppose that's correct. All right, if I substitute two and minus 1 Oh, I get. Yes, six plus one. Yes. so, so what have we done now? We have gone through the graph. Bottom up. And we have only done it once. We don't need several passes, we just need one single pass. Yes. We you we do both when we go through the graph, we do both Computing, the functions and Computing the derivative the everything over the X, right? But it's okay, we go through the graph, these two things and when we arrived at the end we have both the value of f. And the value of the air, over the X. So here's a question for you. I hope somebody is still with me because yeah, I know this probably was boring but here is a question for you. Why isn't that? Why is that not enough? I just did a single pass from the graph and they got the derivative Why can't you just use this all this? Why do I need back propagation? What's the catch? What's wrong here? All the formulas are right. We did indeed, get the derivative. But why can't we just use this approach? While you're thinking no copy the graph because then we'll go to actually back propagation. But why can't we just use forward navigation and be content with forward propagation? Because we need gradients, Maybe Okay, so where we move? Okay, so we need gradients and we just got there for the X. We can do the afford the way in the same way. What's the catch? Yes. See I I need to repeat this even though we probably know but propagation already but um, what's the cash? Why can't I just use this? Why do I need to to invent anything else? Now I will proceed to back probe. I will tell you how to go from from the end to the beginning of this graph. It will be slightly different, but why can't I use this? What's wrong with this? So, theoretically formally, we can write everything is correct. We did get there for the X. And sure enough we can do the same thing. Get there for you. Why no problem. So, what is the problem? If it's not in the Here in the formal correctness. How would we apply this algorithm to an actual neural network? What would be the procedure? yeah, all right, so how would we Apply this algorithm. This forward propagation derivative Computing algorithm to a real neural network. Or actually to any function. As you said but for some reason didn't elaborate on it. We need the whole gradient as the result, right? So we need in this case we need both AFR or DX and therefore divide. So this procedure that the one that I wrote down gives you therefore DX How do I get there for the Y? Well, I can go through the graph again, but this time, I will compute. I will start with the X over The Y, which is 0 the Y over the Y, which is 1 and again go through the graph and get to And get. and I will get there for do I sure Or alternatively, what I could do, I could compute the soul and parallel, right? So as I go through the graph, I am doing everything at once. I am doing the values, I'm doing dxo D, everything over DX. And I'm also doing everything over dye That's all. So then I will only need one pass. And during this one pass, I will compute everything. But both of these approaches are completely impractical. You see in the real neural network, like how do we want to scale this up for a function of two variables? That's fine. But how do we scale this up? When you scale it up to a real neural network they as I said, the length of the vector of the gradient is large, right? So modern neural networks may have billions of weights at least Millions for sure, right? so, How do we? So, what does it mean to apply the salary to get a gradient over a million variables? It means we either need to go over the graph a million times. It doesn't sound good. Or we go over the graph from once. But in every note of the graph, we need the vector of Sesame million because we actually do need it. All of this way really values when we go and we basically we need a huge amount of memory. We need a million times. The size of the graph of memory to actually do this one for us. so, neither of this actually works, right? As you probably understand, the networks are the practical networks will be so large that they just one copy of them. Barely fits into your GPU, right? So, of course, you cannot fit a million copies of the neural network into in, into your into memory to do this. And of course, you can do a million passes over the network and then it would take forever, right? So either the time doesn't work or the space test work. In this case, fortunately, we can do it in a much better way. And that's what back propagation is about. So, back propagation. Be proper. Switches the, the question switches goes to the duel, and to the converse way of viewing this graph, and to the inverse way of moving through this graph. So what did we do here in the straightforward approach when we go bottom up? We compute like when we go bottom up we compute the everything over DX. So we get this sequence when we go through the graph of D, every node over DX, And finally, we get to the F overdose. When you do it like this, obviously you need to, to do as much. To get the over the wire and so on. But, what if? instead of starting from the inputs and doing the everything over the X What if we did the opposite? What if we start from Top? And we do the F over the everything. You see? So we go. Now, the base of our induction is the F over the DF, which is one And then are what do we for example, do here. When we go to E, We say all right. So what is the F over d e. Well, we need we only need to know. Locally how FS computed. So f is e, plus C. So DF over D is one very easy. Here. Also the F over DC is one. Then it becomes a bit more interesting. So now what is let's say, DF Okay, so here I want to put the F over DD over here, right? And all right. Separately won't fit there. What is the F over GD? Well, d goes to F only through e. Right. So by the chain rule, as usual DFO over DD is the F over d. E times d e over DD. So the F over D is 1. And the over DD is B. So it's one time speed write. And so on. So for example, so here, I get B. Now let's say d. Okay what else? GF or D? Yeah, DF over DB it's the next step right there. For DB is again B goes only through e so it's D over D times d e over D B and it's D. Okay. The air for the a again a goes only through D so it's D. Okay let me put it here. DF over de is the F over DD times DD over de and it's it's what it's 2A times B. Okay. So two a b. And now comes the interesting part. So now I have DFO over de DF over DB and the over DC. And now I need to compute, let's say DF over DX. And X. Goes. Into different things, right? So there are two outgoing ages here which means that X is a part of a, which is then part of and X is a part of B, which is the part of. So again, by the chain rule, it's really straightforward. I just need to add up the contributions, right? So the F over D. A times d, a over DX, plus the F over DB times DB over there. Let's say so I know there for day which is 2 a b d over DX is 1 and this is straightforward plus DF or DB which is B times DB over DX which is also one So, we go to a B plus d. So this is 2 times X Plus y times x, minus y, plus X, Plus y squared, which is, I guess, correct. So we go. The same result as before right there for the X but the beautiful part here. Is that with without starting over with without three Computing, everything that was happening above, we all can immediately get there for UI over here. Right. So now why goes to three different things? Okay, let me since you're not very quick ones from equation and let me write it down a bit more in a bit more detail. So DF over d8 times over the wire, right? Plus the F over DB times t b over d y plus the F over DC times this is over, do I And what we get here. Well, therefore de is 2 a b times 1. The AF over DB is D times, minus 1, right? The DFD over device minus 1. So minus D and therefore, this is 1. But then we need to multiply by DC over the Y, which is 3 y squared, so we get like two times X Plus y times x, minus y, minus X, Plus, y squared, plus, Three y squared. And I suppose that's all correct, right? If you go and look at this. Yeah, obviously that's all correct. so, Notice the difference, right? In stead of going Bottom up and Computing, D everything over DX, and then or in parallel, the everything over the why Thus like doing a lot of unnecessary, computations, we are going. From top to the bottom and we are Computing. DF over the everything. In there. And of course this is these are two symmetrical approaches. They are dual to each other. They it's you can argue that it's basically the same but neural networks are not symmetrical, right? You always have only one output because You want to, for example, minimize your output right. You, you need to have a single function that you minimize, your cannot minimize several functions or a million functions. At once that doesn't work, if you have a million functions that you need to minimize first, you need to compose them into a single function. so, You always have only one output at the end. And you have millions of inputs. So this approach skills, well if you have lots of arts and few inputs, then this is the proper way. but our situation is the opposite in real networks we have lots of inputs and one output so So, we use bad propagation. No test. How in this case, like what did we need to? Uh to do this computations I wrote down formulas because they are easier to to follow than just numbers because numbers don't mean anything. But in practice, of course, in actual computation they would be numbers right there. This this would be numerical values of these things. and, so, When you start start out with the F over the F, of course, it's always one. But then, as we progressed through the graph backwards to compute, for example, DF over DD. So what what's happening on? What? What gets transmitted on this Edge. What gets transmitted from E to D? We need it. Not only there for D, which we got from, from above. But we also needed D over DD. And to compute the over DD. We needed the value of B. So we needed to know the values of this intermediate notes. Again it's all local to compute this. I only need the notes that go inside. But I do need to know the ways to not only the lyrics. Because to compute the derivatives, I need to know the radius. So in practice bad propagation is not one pass through the graph. It's two passes. So how the algorithm actually works first. You do forward propagation. To compute. Values of intermediate nodes. And yes, you need to store them. So it's kind of like the you need to store two numbers on every edge of this of this graph. and then, back prop to compute. DF over the everything. For for every intermediate. so, let's back propagation, okay and This is a very efficient and actually pretty straightforward. Wait to compute gradients. and actually, I, if you look at Any deep learning library like pytorch that you will probably be using in practice in our class. If you look at any preparing Library, what you see is it's basic Operation, what it actually is supposed to do really, really well its main job. Is to do this, to passes to the graph. So, These are the key. Procedures. The key functions that the library needs to implement and everything else is basically just syntactic sugar. On top of that. so, If you, I don't know if your program and pytorch, if you do the Practical sessions of this class and you implement a new neural network, sure, you will see that by Turkish has thousands of classes with different layers, different kinds of components. And all of this components are only there, they are only needed to set up this graph. And this components can be relatively inefficient, it doesn't really matter. They are only around once and they don't don't do much to be honest. What actually has to be efficient. What is like the meat of the of everything? Is Computing. The gradient of the ground graph. So I like to say that pytorch and tensorflow and whatever else, what, what they actually are, are, automatic differentiation, libraries. They are not, I mean, the Deep learning is an afterthought. What is actually what actually has to be extremely efficient is the forward propagation and the backward propagation procedure. The rest can be done in any way. Okay. What else do I want to say here? I want to see. Okay, for propagation backward propagation and example. Okay, so well, I'm thinking what they'll say missed, let me show you. What I will sew make available. I have some examples over here. So it's a different function but something something like what I just did on the board and you can play with it. You can, you can Define different computational graph and see how the values propagate through a network like this one. Right. Oh yeah, and also just to Circle back to how it actually applies to neural networks. Notice that When like, when you say, what is the input to the to a neural network, the in your intuition, like your default answer would be the input is X and Y or actually on the X. So like if if you ask, what is the input of the neural network that distinguishes gets from dogs? Well, that's an image. And that's that's true, right? So the default weight to think of inputs is, is this but If you think of the network as a competition on graph, it has two different source of inputs. I think I already said that, right? So it has inputs that are fixed. That are always fixed that we do not optimize. And these are. Like images, correct? Answers to the images. And so on, these are the access and the wise And the weights. And the weights are inputs to the computational graph. They're not computed from anywhere, they are variables that appear in this huge formula. and when we are doing, Training. When we learn, when we are doing a training of neural networks, we are actually interested in gradients with respect to the weights. And so yeah, if anybody asks, there are different kinds of inputs in your own network and the weights are also inputs. And that's and when I was doing this, this example, there was no fixed input here, so I could have had it a constant or something, but I mean, wouldn't surf any purpose like X and Y? And this example are both weights and we need to have a gradient with respect to X and Y. Um, all right. Has been clear. Did you already know this? Or. Yeah. Okay. Okay, so Before the break before the break. I guess I don't have too much time. So let me just maybe do a part of what I wanted to to say about gradient descent. Specifically, let me Motivate stochastic, gradient descent and actually introduce it. And then after the break, we will discuss the actual algorithms of stochastic gradient descent. so, Here is here is a question. There are a lot of problems in deep learning in Practical, deep learning that come from, from the fact that we are using gradient descent. And we will discuss some of these problems in class. Of course we don't yet, see them, we are just on the beginning to look at this stuff. But basically a gradient descent is a pretty stupid algorithm. It's it's a first order. So gradient descent is the first order, first order. Comes from the first order approximation to the loss. Right? So I take like of double w and they say well, okay, so right now, I am at Point WK, let me do it. Taylor series of all of w, write at Point WK. So I say, well, it's all of WK. Plus W minus w k right times. The gradient of L at Point WK. Right. And gradient descent basically stops here. It just looks at this, it says, all right, so the gradient is the direction of steepest increase, therefore the opposite direction is the steepest decreased. Let's go there. If you want to minimize. but, We have years of optimization Theory, right? So, gradient descent could be done by, I don't know. Newton and leibnitz. And since then, we've had quite a lot of more. Involved, but better optimization techniques, right? And the most straightforward idea, when you look at gradient descent, like this would be well, what if we go one step further in the Taylor series? Why not? what if we all so, Go to the second, derivatives, I believe, minus, I WK that now now, there is a quadratic form and here, right times H inverse nothing, we're just h. A times W minus W. Okay. Plus something smaller, right? so now we are approximating not by a surface, not by linear surface, which, to be honest is a pretty stupid idea for optimization. Well, I mean, it's not stupid in the sense that it can work, but it's cheap and the sense that it's naive. So, if I'm looking at a complicated function and I am trying to to see like, what is the derivative here where to go, then all that, the derivative tells me is that. Well, you need to go here or you need to go here if we are dimensional one, right? And it doesn't tell you anything about how far you should go, and this is actually the main problem of gradient descent. This is what optimization Theory to a large extent was about. It's a big topic like great, the gradient gives you Direction but how far should you go along this direction? What should be the learning great. What should be the step-size? but, if you go one step further, then what you are doing is you're approximating your difficult function, locally with a Quadratic surface. on here, it would be a parabola but with a quadratic surface and now, There are no questions anymore, you know, where to go, you can go immediately to the minimum of this parable. The minimum of this quadratic surface. And it's it's a very simple formula, right? You'll look at this and you say, Okay, I want to minimize this guy. So how do you minimize? Well, you take the gradient with respect to W. Okay, so what is going to be the gradient with respect to W? Let's say that let me call this Vector, G the gradient g k gradient at step k. And this is HK. This is the Matrix of the second derivatives H because it's called the Hessian. and, I take the gradient of the first part. This disappears, this disappears. There is just GK. Right? And then I take the gradient of the second part, the two cancels out, and we get JK plus HK times W and that's the gradient of this quadratic function. So it should be equal to 0. And I guess that's sorry that's that's not it. Of course I forgot the first. I forgot h, k times W minus w k of course, sorry. And that should be equal to 0. So basically W is WK. Minus HK, inverse times JK. That's it. And you can say that this is your next W and you have no problem with the step-size. And this procedure is far, far more robust, more stable. You will never almost never goes to some bad part of the search space. You will converge and far. Fewer iterations basically it's better all around. And this is called Newton's method, by the way. Newton's method or second order optimization. Thought or second order optimization or whatever. So why can't we use Newton's method for gradient descent? For for Newton's method itself, the answer is kind of obvious because we cannot afford to do the to do this computation, right? So again remember that W is a very, very long Factor, right? It's, it's like a million of numbers. It's a vector of size, a million. So HK. The Matrix of second derivative. Right? The L over d w, i d w. J is a matrix of size a million times a million. And we are supposed to compute this Matrix but more than computers to invert it. So of course it's not going to work computation, right? No question about this. but, a more interesting question is in optimization theory in classical optimization Theory, like in the 1960s and 1970s and 1980s. People also were thinking about this There were no huge neural networks at the time, but there were functions to optimize. And there were difficult functions to optimize and error cases, when secondary techniques were to difficult computationally. So there is this whole field. of what is called quality in youth, from algorithms, Course in Newton algorithms. And they are basically approximation to this. so, the most famous such algorithm is called lbfgs Where else stands for limited? Memory and bfgs are for last names, Fletcher, void and Goldfarb something like this. So it's a very famous algorithm. I won't go into details on how it works. It's definitely not relevant for us but basically what it does is it Keeps an approximation to this kind of update. Ah, and the very good approximation. By only looking at the W's themselves. W1w 2 and so on, and the gradient vectors. So like when you go from K to K plus 1 you there is a procedure to update. This approximate Hessian approximate inversion and this procedure is quick. And it never deals with a million times, a million matrices. Basically it's a lower rank approximation, but let's not go there. So There are good ways. To do something like the second order technique. Without going actually to the second order. Well, only staying at the level of gradients and gradient factors and doing doing it in relatively low complexity. So why don't we do that in the appearing? And the answer is again, we would be very happy to and just as we would be very happy to use Newton's method will be very happy to do the second order optimization. And we would be nearly as happy. To do lbfgs for any neural network. But we can't. And here comes the interesting part. So why am I a billionaire to this? So first I wanted to mention second-order optimization but but also, why am I, why doesn't an algorithm like this work? I didn't tell you what the algorithm is, but trust me. It only need requires to know, gradients at individual points values at this point, and that's it on your Own, and the answer is. In deep learning. Unfortunately. We cannot even apply gradient descent. Because we cannot even compute the gradient. Or, I mean we can only compute it like once and not never step. Why, why? So For a very straightforward reason and I, actually already mentioned this reason. Where did they do that? I did it. Where did I hear, right? So what is the function that we are actually minimizing in machine learning? The function L of w. Is like a huge average. or a huge sum same thing of form of loss functions. Across the whole data set. Of X and Y and W. You can think of it, by the way, usually is something like the negative log likelihood, right? Lock P of or block posterior. Look of w given X and Y and to connect it to what we discussed yesterday and the day before. But in any case, Your complicated neural network with a million ways. Leaves over here. It computes the laws. Yes. But it computes the laws on known one training sample. And to get the function that you minimize, you need to go over the whole data set. so, the actual honest to God, gradient, the actual G, Okay. Would be. A future average. Of a gradients of this loss function. Was functions at Point WK, right? And yes, we can obviously compute every one of them, but if I wanted to compute, The true value of the gradient Vector, I would need to go over the whole data set on every step. Which is kind of obviously impractical. So yeah, we will go over the whole data set but maybe like once or twice, not not on every step of our optimization procedure, that that's not gonna work. So what is the actual setting? How what what is the problem? And we are solving if I am telling you that we cannot even compute, the function, that we are optimizing, right? It's the same in the same thing, right? We can compute the gradient because it's a huge sum and therefore, we can't even compute the function itself because it's the same here, some What are we even doing? Well, the answer is. We are doing what is known as stochastic gradient descent. I wrote, I wrote all of this functions, not a sums, but as averages, it doesn't matter for optimization but I wrote them whenever for as averages to make the following point, you can view this loss function, you can view the function that we are optimizing. As an expectation. Over the data set. Over the uniform distribution of the data set. Of this. Small loss function. So X and Y here, X and Y. Are taken just uniformly at random from the dataset, right? Because what is the expectation of the expectation is the average weight is probably just. So if I take everything is equal probabilities, I get just over average. So, our function. Is actually an expectation of a different function with respect to some of the variables with respect to X and Y. And I want to minimize it with respect to the other variables, to the respect to w. When you have a problem like this, this is what's called stochastic optimization. and, What is, how can we do it? If we cannot compute this expectation directly, Well. There is basically always exactly one true way to approximate the expectation. You take a sample and that's it. So what we are actually doing? In practice. Is on every step along the way. We are taking. Not the gradient GK. Which is, I mean, expectation is linear, so it's the same thing. It's the expectation of the gradients of hell, right? But we are approximating the true gradient. With. Let's say G hat. Okay? Which is just the average over a small subsample of this. 1 over, let's say, m Times the sum. Gradient. L of x, i y, i W. So on every step along the way. What we are actually doing, and you probably already know this, you just, I just kind of think you never thought with from this direction from this angle, but there is also probably already know what we actually do when we train difficult, duplicated machine learning models. We don't go over the whole data set to compute the loss, We go. Through mini beaches, right? And this meaning batch. Formerly. It's a sample from the data set. So what we are actually doing like what the meaning of what we're doing. Okay, great in the scent is we are approximating the true value of the gradient. Which is bacon difficult with a Sample. Sample to the gradient. So on average, if you take the average of this, over the whole dataset, obviously you get the same thing. So the the mean is correct. And to be honest, approximating the expectation with a sample is like one of the best things you the one of the best approximations ever. It has all of the nice properties. It converges. It's it has its unbiased that has lots of results known about it so it's as good an approximation as we can hope for And what we actually do in practice is we go on every step of gradient descent with sample a mini beach. We take a small subset from the data set. We compute the gradients on the subset and then we see what happens next. And then we update the weights, according only to the gradients from this subject, probably know this. But now you can you can see what it actually means. but, Even though this is a good approximation and even though indeed we will go to. We when we do to test the gradient descent, we do. arrive at a good at the neighborhood of minimum, etc, etc, will discuss it after the break, what we actually get from from SGD, but it's still an approximation. and, In practice. It's a pretty bad one. I mean, it's good theoretically, but The specific numbers are like the size of the data set is in millions or more. And they actually mini batch size, is like four. Or eight, Maybe. So the minion based size should be such that this may cause of the network would fit into your GPU memory and it's a small number. They? The data set is, of course, large. So we are approximating the average of a Million numbers by taking like four or eight or even one number at random. So of course, mathematical is the best we can do, but it's still a pretty bad approximation. It's still has a pretty big variance. And unfortunately, this variance kills. Algorithms, like lbfgs. So, Since they are all doing approximations. In order for those approached that I can can't explain without this whole separate lecture why but trust me. Since there are also doing approximations here. In order for those approximations to actually work, we need to have very good values of the actual gradients, but true various or at least very good. Approximations, we cannot just replace this GIS with sampled versions with huge variants and hope for the best. The best one will not come. So it's it's an interesting and a very practical actually open problem for deep learning can be due better. Can we, can we may be modified was in Newton algorithms so that they are, they will start working. So that we can, for example, use case the gradients, this sample estimates, instead of true gradients and still Go where we want to go. this is a known and probably we cannot because lots of smart people have already thought about this and unfortunately no solution has come but, of course, stochastic gradient descent. So now, okay, so now the actual like formula of the update is this WK, plus 1 is WK, Minus some learning rate. Times. Okay, let me just call it times JK head. So times, this sampled gradient. I will call it SGD, stochastic gradient descent, and of course, this is also not the end of the story. This is the first natural step, the simplest possible algorithm. And of course, there have been lots and lots of modifications and improvements of this idea. So after the break will discuss those, they also like the very heart of the appearing. And for now, are there any questions about SGD backprop? Okay. If now questions, then let's have a break. And when we can win, we go to SGD, variations and algorithms that people actually use to train your Networks. Break. Okay, let's let's continue. so, We stopped at the notion of stochastic gradient descent. and I actually, before we, I don't want to delve to deepen to the theory of this stuff, but I want to show you a couple of pictures and results about it before we actually proceed to To the new algorithms to variations of stochastic gradient descent. So What actually happened in stochastic gradient descent? You can actually analyze it. And classical optimization theory, has analyzed it in great detail. And what, what, actually happens like, what, what is the correct way of looking at it so to speak? Well, basically A lot of optimization theory was centered around this question. so, suppose that We are standing over here. This is our WK. And what does the gradient, descent? Tell us. Well, it tells us the direction where we are supposed to go, right? So we know that we are supposed to go in the direction of JK. But we don't know how far we should go. Like, do we stop here? Do we go all the way here or here? We don't know. It's it's only the direction, not the endpoint. So a lot of optimization actually. A lot of optimization theory if you, if you ever had a class on it or if you will have a class on it, a lot about centers on this one dimensional optimization problem. Like we already know that direction and be like, we are optimizing f of x. We are let's say minimizing and at this point, We already know that I want to go from X. To the direction. G right. But I still don't know how far I want to go. So let me treat this as a function of one variable and let me try to actually find the optimal step size, let me actually try to find out how far I should go in this direction. So, it will still be an iterative procedure, but hopefully we can say something about how far we should go. So a lot of classical results like we'll throw our myjoe's rule etc. Etc. They are all about this kind of problem. And we don't care about this results because they don't carry over to stochastic gradient descent that easily. What does carryover. So what what does classical optimization Theory? Say about. Okay, we discussed this. So what does classical optimization Theory? Say about stochastic gradient descent specifically? Well. SGD. If you look at its rejected, if you look at how it works, it actually works like this and I will make it precise in a moment. But the picture is like this, if you are optimizing a function You. First. Go to the neighborhood of the minimum, the neighborhood of the optimum. It's a local Optimum and general, but it's matter. So you go to the neighborhood of a m Optimum. Quite quickly at first, this is the initial part of this trajectory. As you can see it, Go basically in the correct direction for for a long time. But then when you arrive, you can't stop. You can't converge, or at least you can't converge by default. So if you have a constant step size in gradient descent, if you don't have a schedule of decaying haters down to 0, then what's going to happen with stochastic? Gradient descent is, it will go to the neighborhood of the optimum and that will then oscillate their back and forth, right? Because it cannot even recognize when it goes to the optimum itself because in the optimum, the gradient is zero. Yes. But we don't know the great and we get random sample of the gradient, which will not be zero, and then we will go out of the optimum somewhere else so we can never know where exactly the optimum is, but we can get to a neighborhood and then just go around this neighborhood. Due to our random sampling. Sounds pretty reasonable. And if you do a little bit of math, which I think I will Skip, it's not hard but just I don't think there is any point in us, going through this. If you do a little bit of math, you arrive at an interesting estimate for like how long it's going to take and how stochastic gradient descent. and we're just so this is the result. The expected value of the function that we are optimizing. At. Well, not quite a text K. This is x k had, which is an intermediate Point. Let's forget about the details. Basically, after Kate durations, What we expect the function really to be. What is its residue? What is it different with the optimal function? Really? So we are minimizing so the optimal value is lower. But after K iterations, we can expect to be pretty close to the optimum. How close There is actually an answer. There is about like this one. Right? So it's less than or equal to Actually previously right less than or equal to our squared r squared. Is this guy, it's the original relationship. It's how far we were from the optimum and the beginning. So this is a constant basically. It's it's fixed at the beginning of our optimization process. Ah, and then there is this part, which is more interesting. So alpha eyes are the step sizes, right? So on step size, I we go to Alpha, I times given this Vector Alpha items, right? And here in the numerator, we get the sum of the Norms of this stochastic. Gradient squared times, Alpha squared, and in the denominator down here, we get just the sum of So if our stochastic gradients are bounded and probably they are, even though there's statistic, then we can just plug in this Bond, whatever it is, and we get this general form of the formulas. So, this is exactly what explains the behavior of stochastic gradient descent. Because look, suppose you have constant step size like we just did, if you had constant step size for all five star equal to H, then this Splits into two terms. And the first term is our squared over H which is basically over time scale, right? They should be basically just goes to 0. Pretty quickly as K growth, we go from iteration to iteration, K increases, right? So K increases to infinity and the rest is constant. So we goes to the second part is just constant, right? The second part. So the first part depends on how far we were in the beginning. And that goes to zero, which means that however forever we will go close to the correct option. On the other hand, when we get there, even when this part goes to 0 there, still the constant part over here, which doesn't have K inside. So it will be. It will remain constant. But of course, this formula tells us more than that. This is just a special case for the constant step size. And this formula also tells us how do we choose Alphas, so that's the case, the great in the sand converges. And the answer is, well, if you want this guy to go to zero, what is the easiest way to do it? You want your denominator, they sum of Alphas to go to Infinity. And at the same time, you want your newer, the sum of alpha squared to not go to image, right? So the Practical conclusion, one practical conclusion from this formula is that if you want your, stochastic gradient descent to converge, but in the, if you want to converge to an Optimum, then probably you need to take Alphas the step size as you want to reduce them. Obviously, otherwise you will never converge. But how fast do you reduce? And what is the schedule of reducing them all? This formula gives you the answers, are you want to reduce them on such a way? Let the sum of Alphas goes to Infinity. They were just but the sum of alpha squares does not go to Infinity converges, right? So, What would be the easiest example? This is example would be just I'll find if we go if you go back in our annotation like 8, okay. And we ask a question of how fast should a decade go to 0. Then this formula gives you a possible answer like this. I can do, like all 8K is something like 1 over k. Then the sum of 8, the case goes to Infinity, but the sum of 80 K squared does not go to infinity and therefore stochastic, gradient descent converges. So it's just one possible answer and to be honest in practice, this formula doesn't tell you much. So it tells you this General conversions Behavior, but it doesn't really translate to like real. I don't know estimates on the size of this neighborhood for example, because it always includes this g-square and you can never know, just Square it and practice it's about on your sampled gradients. So on like a sample of sub-sample of your data set which probably has a lot of variance so you don't know just Square to practice. But anyway, it does tell you something useful about stochastic gradient descent. but, But this is not really what I will be talking to you about. Now in, in the second part of our class, what I am going to be talking to you about is a very different problem of statistic, creating this and One second. Sorry. Yeah, sorry. So what what I will be talking to you about is a different problem of stochastic, gradient descent. so, let me show you what the problem actually is. So, we're here. Yeah. so, Let me guess what? My first write down. The very simple formula this. Okay, so we discussed SGD now let's say, Point number five. Is. SGD improvements. Improvements and variations. So what is the problem that we are solving? What is an important problem of all of this of stochastic gradients? Let's consider the following example. It's as simple as they come. It's probably like the easiest optimization problem possible. I will have a function of two variables X and Y. And it will look like this x squared plus a constant times y squared, okay? And I want to minimize it with respect to X and Y. So here, sorry here is the function right? The control plot of the function. Very easiest problem, the very easiest optimization problem possible, right? It's quadratic. The minimum is at 0. We immediately see that the minimum is at 0. It's convex, it goes to 0. Everything is great. Everything is fine, right? So very, very simple problem. However, you want to look at For example, if you want to use Newton's method, if you want to use the second order method, you go to 0 in one step because there is no approximation. Now, the second order is just the function of but what does first order? What the first order methods do? How does gradient descent tackle this? Well, it turns out that it depends a lot on the constant. We shouldn't matter, right? But it does depend a lot on the constant. So here I start with this concept so you can see that this is the function x squared plus rho times y squared. And you can see that I begin with row equal to 1 1/2. So it's almost a circle. It's like slightly elongated lips. When it's almost a circle everything. Where it's beautiful, right? So, I tried a few learning creates and one. Okay. So, one over 100 was a bit too slow, and they didn't go to all the way to zero. That's fine. Of course I can chose to learn create which is too slow. That's my hands, but large other increase. Just went straight to zero. It was all fine. So there is absolutely no problem and in actually, sorry it's not SGD here, it's just it's just creating descent right. There is no miniature. There are no mini batches, nothing is okay. So let me fix that. Ah, yeah. So just regular gradient descent that goes straight to zero. Everything works fine. But what if I start reducing Crow further? What if it's now not one over two but one hour 20 well, what happens as I reduce Row the coordinates become More like their scale becomes more different. The coordinates become more imbalanced. so, For example, here row is, why changes 50 times slower than x? So what does it mean for gradient descent? It means that horizontally in terms of X. It's exactly the same though to zero. And we stay there. No problem. but, in terms of why, Well, now it takes a longer time to go to zero, right? But while I am at the level of 0.05, it's still quite possible. So, but now notice that, like, the the range of good learning creates begins to shrink, right? So before that for for a more or less a circle, it was fine. Unless they chose the learning create like actively to low but now 0.1 is also kind of slow. On this 0.5 gets gets to 0 into 200 iterations, which is quite a lot for such a simple function, right? and if I continue in this way, then pretty soon. Everything will be too slow. And here is the cage, so you could say a little bit. Why don't you just increase the learning rate, of course, for this function, you should go faster, but the point, the problem is I really can't because, okay, I can go from 0.5 to 0.9 or even 0.99, and yeah, it will get me a little bit closer to 0. but, I cannot go over one. Because if I go over one even a little bit, then the x coordinates starts to diverge, right? Because along the x coordinate. The coefficient is still one. So, of course, it's the problem is not that why changes slowly in absolute ways, that wouldn't be a problem. Of course, the problem is that X and Y are changing. It's very different rates. Excellent. Why have a very different scale? and at this point, even for something like, 500, 200 full difference between them. There's already know good learning rate for gradient descent. Even though it's So it's I tighter diverges? Or it just takes hopelessly long to go anywhere, right? So we can do 2000 iterations, then we will probably get there. Yeah, okay, we still 2000 deterrents, we will get there. But 2000, iterations of great of gradient descent for a quadratic function, starting from point one and three halves, and going to 0. Doesn't make any sense, right? So, here is the problem, right? When If even even in very simple case, yes, when the different variables in your optimization function, if in your set of variables from different variables, begin to different scale. When they begin to have different rates at which we should move along them. Everything kind of fails, gradient descent cannot have a unified rated, we should goes. and I think, Yeah, sorry this, this is next upload. So, so this is the mostly mostly. This is the problem that we are solving and we will go through several different. Ideas that people had well solving it, I will not. This is not a historical lesson. The ideas that we discuss are still real and useful. So Let's go through this idea. The first step and the first idea. Okay, so let me maybe, maybe, let's start with stamps 0. I will set up the notation first because I will reuse it all the time. So the notation is I go from. X k minus 1. 2x K. Okay, so I'm optimizing something like f4x. I have the vector X of variables and recently I went from XK minus 1 to XK I call this Vector UK for or you can minus one, I think. Yeah. So for the word update, so you can minus 1 is x. K, minus x k minus 1. It's my last update. And now I am a point x k. And let's say I have a gradient. GK here. So at this point for at this point, let's just assume that we are talking about stochastic gradient and this is not the true gradient. This is the stochastic estimate, or it could be a true gradient for, for what. I'm going to tell you now, it doesn't matter. So there is a direction that the gradient tells you. Maybe it's a simple. Maybe it's the true one for what I'm about to say. It doesn't matter. But there is a great interaction over here. so, classical SGD. Or GD or whatever would do it this way, okay? Plus one would be a SK last some Alpha times JK, right? So let me say that this is oh sorry minus, right? We are minimizing minus So let me say that this is already minus Alpha times g k. Minus Alpha times g k. And in the simplest example of SGD, this is X Plus 1. This is X K plus 1. And UK is just minus Alpha times GK. That's it. so idea number one, let's let's go over there. Yes. Idea number one is called momentum. Momentum, like, like, in school in high school physics, right? The impulse, the momentum of motion, what's the English word for that? Whatever? Okay. So the the momentum, which is like M times V in high school physics. What? How does it appear here? Well, let's go back to our picture. We had x k minus 1 and we just went to XK through a vector called UK minus one. And there is a direction that the gradient wants us to go minus JK uh, so the momentum method says, well, What, what are we really doing, like, what's the physical view of this? What what is the, what does it all mean? Well, it looks like gradient descent looks like Bow. Rolling down some kind of a slope, right? It's like a material point and it's on a slope. So it rolls down the direction where the gradient tells it to go and the steepest descent Direction. So, so, why don't we take this hint from regular Newtonian physics and why don't we actually apply it to Say. Why don't feel so add another physical thing from their inertia? Why don't we add this conservation of momentum here? Basically what this means is if your ball goes down the slope and the slope suddenly changes, then for a while, the ball will follow its current position, right? So it's it's gonna have some moment. a formerly, what it means is, When I am here. And I have come from here. That's why I was drawing the previous update too. I not only move along the gradient, but I also can serve. A bit of the previous update. So I also add some game times. UK minus 1. So this is the inertial motion. I follow the already existing moment and then, So, my final update will be the sum of this guys, right? So, Then I will go over here. This will be Escape plus one. So now Escape plus one is XK plus gamma times UK. Minus one, we carry over part of the update minus Alpha times JK. So, this is UK. okay, so we keep A part of the momentum. And actually, in practice, let me tell you right away that in practice with capability, large part of the momentum. So whenever you have anything momentum like gamma is, you know, 0.95, 0.99 maybe even more. So usually in practice you want to carry over. A lot of the momentum, there is little friction there should be some friction but not much. and, you just, Keep going the same direction. So what does it do? Why is it a good idea what it does is it keeps going forward. Along some Direction. Keeps going forward on some direction. And if the slope doesn't change in direction, if you are still, if the gradients still gets us to go in the same way then. I will grade you go faster and faster right? As the ball rolls down the slope, it will roll faster and faster to pick up speed. And this is exactly what hopefully is going to happen over here. um okay, I'll go to the picture later but hopefully what's gonna happen over here so Along the X Direction. the ball will go back and forth but then it will oscillate and stabilize some zero because In the X Direction, it's a steep slope, and pretty soon. We will go to the opposite part of the slope and back and back. So if you, if you imagine it as a ball, actually rolling down this Ravine and you will kind of intuitively see that, that's what happened. But along the y-axis, it will spin up, right? Yes, the slope is small. Yes. Why along the y-axis? It, it's not cheap. It's shallow but It's still goes and goes and you pick up speed as you go. So this is the original motivation and the idea for for the momentum approach. And let me immediately tell you the next idea, which is a small modification of the moment. Small. But actually very, very useful. Both theoretically, and practically. Very interesting manifestation. The second, the approach is called A Nestor of accelerated gradients. You can see the acronym neck sometimes or just Nestor of methods or something like this urinary for the Soviet mathematician who invented at some time in the 1980s. And yesterday's idea is really simple, and really great. So let's go back to this picture that I will not copy, it doesn't matter but let's go back to this picture. While. So what does the method of moment tells us? It tells us. Well, we are here now. And our next update has two components, the gradient component, and the momentum components. So we stand over here, we compute the gradient, and we get both components, and that gives us our update. Yesterday is this? Wait, okay. So we are here. And when we arrived here, we don't yet know the gradient so we should be we should get to work on calculating GK, right? But wait, but we already know the momentum part, right? So when we are standing over here after the previous update, We already know. Are part and maybe a large part. As I tell as I told you momentum's momentum can really pick up speed, we know a large part of the next update on radio. So why do we insist in Computing? The gradient over here? Why don't we? Go to this point which we already know, doesn't take anything to go there. And calculate the gradient over there. So this is negative Alpha times, let's say, G Prime K. Write the gradient computed at this point and then our new update will go here. Right. So, in Esther of acceleration, gradients, Escape plus one is XK plus gamma times. UK, minus 1, minus Alpha times, G Prime. Let me write it down. It's the gradient, believe it's the gradient, with respect to X of f. Note that point XK, but at point x k plus gamma times UK minus one. so, in this intermediate, And not what I meant. And this is the UK now, Sorry. Yeah and and this is the UK. so, What is like, what is the motivation behind this? Well, first of all, there is some beautiful mathematics behind it and actually gradient descent with this method starts to even converge asymptotically faster. It's some of the asymptotics change when you go from regular moment that's transformative. But we will not go there. The intuitive motivation. Is this Nestor of gradients basically do like a look ahead. They look forward in time and they It appreciate they try to predict what's going to happen and they update based on the future not based on the present which is, of course great. So if we are on a slope like this, Right? And a ball gets rolling down here so it picks up speed at speeds up and now it's here and the next step would put it over here. Right? So in regular momentum, you would continue speeding up because the slope is still in this direction. So, in regular momentum, you would go even further up. The opposite fold. Right. But in terms of momentum, you would look ahead over here. And you would see that. Now the gradient points in the opposite direction. So you are facing a wall in some sense. so, let's slow down say Say Siri. And that makes a lot of sense, right? So, That's that's exactly what makes it better. and if we look, At our example here. Now, now I can show you that picture previously, we're not old enough to see it. But now if you look at this picture, it's the same Alpha. but, Along with regular gradient descent. Also put here gradient descent with momentum, it's the orange line and gradient descent with an extra momentum, it's the green line. And you can see how the oscillations this x oscillations along. The x-axis are much much, much less, or much better contained, when Esther's momentum are used. Right. So again, this is the exact same effect, okay? So along the x-axis, the slope looks like this and the ball, the material Point rolling down. So it's like this, but looks ahead and starts slowing down before the turn, like a good driver, not like material. So okay. So this this is, this is what it looks like. but, of course, The idea didn't stop there. All right. And actually both the classical momentum method of momentum which dates back I think to the 1960s and master of gradients which date back to the 1980s. They come from classical, optimization Theory. They are not special to the appearing in any way. but, when you actually, consider the same kind of problems, but in the context of the planning, You. See the following like the following point. So in deep learning All that we have been doing so far. Was kind of defined and contained. In in just a generic, you can space of this Vector X. But I'm trying to. Convey the intuition. So like, for The method of momentum. All directions are equal. It does not treat X1 the first component different from a two different from extend. it will just add up some vectors in this space. but it turns out that you can do even better, If? You treat different components. Of X differently. If you for example, pick A separate learning create. And the separate changing learning rate for every component of x. When you do something like this, it's called adaptive gradient descent. Or actually, it's almost always stochastic because now we are in deep learning territory. So it's called adaptive stochastic, gradient descent and this kind of approaches. Are basically what we use in the learning. They are the optimization algorithms that you actually use in practice. So, let me walk you through some of them. Again, it will be like a line of algorithms but they will. Culminate in Adam of course and then but to get rid of, we need to discuss some ideas along the way. so, Adaptive. SGD. Radiations. Well, the first variation are called a the grid. It was the original adaptive SGD version a great just literally means adaptive gradient. The first variation worked like this, and the point was as follows. What do we actually want? For every direction in X. Like what kind of logic is behind choosing the learning rate and behind updating the learning rate. The logic is this, if you are on a shallow slope, like this one, and you basically go and go in the same direction, then you should go quickly, if you should go fast, right? But if the slope becomes steep, well, it cannot be steep for long, right? If the slope becomes cheap, it means the local Optimum was closed. So, if you land on a chips slope then you shouldn't carelessly jump further. You should slow down. And probably converge to the local minimum here. So that's that's the idea. How does a the great implement this idea? Well, actually pretty simple. So I will just write down the update rule X k plus 1. I so now, we are talking about one specific component in the vector. Is xki plus minus, right? Minus Alpha over the square root of G. Wait for it g. I plus Epsilon the ik Plus on time. G. K. I So, it's still, it's the same gradient. It's the same Vector of gradient. But the learning rate is now adaptive and what is capital cheap? Okay, capital G. Is the sum of squares. Of this gradients. So like gki is g k, minus 1. I plus g k i squared So, the capital G. Accumulates are all of the history of the gradients, and if there are large gradients, then capital G is large. And therefore, gradients are small and small. this kind of Corresponds to our logic, right? This kind of follows it. So while we are on a shallow slope, while we should be going fast, then we are going fast. So we start with a large Alpha with a high level high learning rate. So at first, we start off going quickly. and then, It goes down but while we are on a shallow slope GK small and it doesn't go down that much. So we are still working quickly along this line. then when we get to step slope, it means that the current G is high. And that means the capital cheek gets this High terms and it becomes large, it's self. So now the learning create Shanks and we go slow, that's that's the idea. Uh, what is? The obvious drawback of this idea. What is like, what cannot do? Well. I mean. If you look at the denominator and how it's defined and apps on doesn't mean anything, it's just so that we don't divide by zero. So Epsilon, it's just a small number. If you look at the denominator, you see that it grows with time. What it means. Is that? once we have been, On a step slope, there is no way for us to speed back up again. right, so if our optimization landscape looks like this, we are screwed. Because we go fast. Then we get here. We slow down. but when it becomes shallow again, it cannot speed up. Its denominator will never gets smaller, right? So now we are doomed to go in very, very slow. This is a bad situation for integrate. So what's what's the solution? The obvious modification would be to not use just the sum of gradients but to use some kind of recent history of gradients. So if we've had recently High values of G. Then we go slow. But if G has been for a while, Pretty small, then we can speed up again, right? How do you achieve that? Well, you could do something like a sliding window. But sliding windows are very expensive, right? To have a sliding window. We need to keep in memory, the whole window, which is impractical, So instead of a sliding Queen though, what we are gonna do is we're gonna do, I hope, you know this trick if not then it's it's very good that I'm telling you about it because it's a crucial trick, you know, all of a plate and computer science, exponential moving average. Am I? Ah, the exponential moving average, basically does this. Let me write it in this notation right away. So, gki is not the sum of J's, G squared. But it's like some coefficient gamma times the previous one, plus one minus gamma. It's a convex combination of the previous value and the new and, and the new value. so, what this actually means is if you just keep Opening the brackets, right? It's like gki comes with this coefficient and then it will be game times. One minus gamma times, the next, she came, minus 1, I squared and then it will become a square. Times 1 minus gamma times G. K. Minus 2, I squared and so on. Right? So it's like as we go further everywhere, will you that we want to add up? Comes with an exponentially decreasing coefficient. The gamma of course should be less than one. Otherwise, nothing will come up to it. And this kind of averaging. Has the properties that we want, right? So, Recent history is wait. Hi. Recent history has has a big weights and something that happened long ago. Far away. History has exponential is always so we kind of forget about it this time and unlike a moving Queen though the only need to store this value that's it. So only one really per parade not the whole window first so much more efficient. And if you take the grad and you replace capital gain, is this formula what you get is an algorithm known as RMS prop. And it's also one of standard approaches to wow, it's also one standard approach to To do in stochastic gradient descent, right? It was popularized by by Geoffrey Hinton at some point. But of course we don't stop there, right? So this this is also not the end of the story. Now. I will go to Aiden, almost straight away, but before I go to Aiden, Let me. Explain to you one more, like angle of looking at it. I think it's it's a pretty fun and instructive angle although the algorithm that results from it wasn't very good and it's not really used but they the basic idea of the motivation behind it. I think is really nice. So, The motivation behind. So the motivation goes as follows. We already discussed gradient descent. Yes, kind of Points rolling down. Surfaces blah, blah Etc. so why don't we keep looking at it from this physics perspective, why don't we actually Keep realizing, what? Keep pursuing, this physical connection, this metaphor of points rolling downhill because it's a very direct correspondence, right? It's the only difference is that both role. Continuum, continuous time. And here we are in discrete time. Otherwise it's the exact same process. So why don't we look at the measurement units of what is going on? And what are the measurement units here? Well, let's start with the gradient because that's it's, it's easier. It's much more natural to start there. So I want my gradient to be like the velocity right. My intuition is that derivative derivatives are velocities their speeds So, let's say that I want my G to be measured and meters per second. Okay, so G is like DF over DX. So this means that X is measured in seconds. And f of x is measured in meters. So the function is how far the point has gone. The x is the time that has elapsed and G is the velocity of the point. Okay. So now that we understand this, let's look at gradient descent and see whether it actually works. So migration the senses. Okay, I take my ex and I updated. Like this x is x minus some constant times chip. What about the measurement units? Well, access measured and seconds. This is just a constant dimensionless unit. And G is meters per second. So we are subtracting velocity from time. Which doesn't make any physical sense. Right. And when I say, doesn't make any physical sense, mathematically what that means. So, what means for us and practice, it. Exactly means that the scale of this variables can be very different So it can happen that your access are large. Here in absolute values and she is relatively small and in this case you would need like a huge Alpha to adjust for that or it could be the other way around. So the G is not scaled well to X it. It's our job to scale it basically. And physically, it means that the dimension the dimensions are on the units of measurement, do not match. Okay. so, okay, in the method of moments, it's the same what happens in say, 8, the grad In adagrad, we have minus Alpha divided by capital G times G something like this. So what are the units over here? Second. Mistress per second and g capital G is small Jesus squared. So it's one over meters squared per second squared. And square root. So basically, The unions can cancel out and we get that all of this is a dimensionless. So now we subtract from seconds from time. Some Dimension was constant. Which also doesn't sound, right? Okay. and, No tears. That Newton's method. Second-order optimization does not have this problem. This is also an important Point here. So if, if you recall that formula that we had about the second order method or something like x minus H, inverse time is G, right? So now, let's look at the units here. Now, X is in seconds. X is in seconds. Gee is a meters per second. What is h? H is the Matrix of second, derivatives its acceleration. So, it's meters per second squared. Inverse. Well, there you go, it cancels out. And on the second remain, So now the units actually match and mathematically, it means that Newton's method actually scale correctly. It gives you the local step-size that you actually want. So this is well, I mean, it's not the reason it's just illustration, but this is one good illustration for Why Newton, while second order techniques are better, right? So there they mentioned this match, they scale automatic And out of this, they're out of this idea. There came method called Aida Delta, Delta which tried to to do the proper units. And basically it was a great but Alpha here was multiplied by something like the square root of U and you was something like the sum of updates squared, something like that. It was not a very good algorithm, it didn't catch up catch on so you don't have to study at the Delta, but I think the basic idea is very interesting. The basic idea of having Of having the unit the measurement units of different things match. And with that, let's go to the real thing. They algorithm that people still use quite often Although there are alternatives. Now I'll mentioned that we won't go into the details of them, but I will mention them, but the most popular optimization algorithm in deep learning is Aiden. And Aiden was actually pretty similar to what we discussed with slight modifications. So it's like x k plus 1. I is x k. I minus Alpha divided by g k. I plus Epsilon. So far, it's more or less the same but times. M k. I not just G. And let me explain what this means. So, g k. I is an exponential moving average of square gradients. wait to times g k minus 1, I Plus 1 minus beta 2 times, gki squared. And M. Is an exponential moving average of the gradient systems. Beta 1 times M. Okay, minus one. I plus 1 minus beta 1 times, gki itself. And that's it. So basically, it's RMS probe. and the only difference from RMS probe is that we also smooth out the gradients themselves. So we are instead of using the actual instantaneous value of the test gradient, we are doing like this moving average over recent history. So we are smoothing the gradients. We are making them less, we are reducing their variants. You're making them less janky as be simple, different mini batches. and this smoothie, Has an excellent effect. It's it's what makes Adam works so well. So, Uh, so what else do I want to say about Adam? Well, yeah, another thing about Adam is that you really don't have to. I mean, it looks like it has a lot of hyperparameters. You got the beta 1 and beta 2 and also Epsilon, and looks like you need to choose them. Carefully etc, etc, which would be difficult but actually it's very robust. You can just keep the standard hyper parameters that They recommended in the original paper. I think it's something like this. Maybe 0.995. I'm not sure. But something like that. And Epsilon is just a very small constant like this minus 8 or something like that and basically it works. So you don't need to tweak beta 1 beta 2 in depth. So they can be just you can just take them off the shelf and a little bit fine. And Adam. Is a really good algorithm. It's so used. It's it's so pretty good. I don't think I can actually illustrate it to you here on pictures because you see the whole point of Oh sorry. The whole point of adaptive algorithms is to treat different components of the vector differently, right? And they shine when you have like lots of them high dimension and in this high dimension, there are some Dimensions that have this kind of behavior, this kind of optimization landscape other dimensions that have that kind of optimization landscape, etc, etc. and, I cannot do this in dimension too, right. I cannot give you an example, on a plane where X and Y, are wildly different. And, you know, there is a big difference between and RMS prop, not gonna work. I cannot give you an example like that. So it will definitely have examples like that in in Practical part and here I can. And as for the pictures, I can just show you some Nice pictures. Okay, so this is the problem again. Yeah, yeah, like this. I can show you some nice pictures but they don't really mean anything. So here is another like Standard function that has been a test bet of optimization and classical optimization Theory. It's called bills function, rosenberg's function. I mix up the two and it's basically let me find it somewhere. It's basically A complicated polynomial. Here it is. It's basically some some complicated polynomial. You don't have to memorize it. It's just some some kind of constant that are to be picked and such a way that It has an interesting optimization landscape. So you have this minimum over here? But around this minimum, you have like this very steep slope over here. You see how close the control lines are to each other, but then the steep slopes suddenly becomes a very shallows of. So it's like it's easy to go quick down this hope, but then you need to recognize it now, it's shell in to kind of speed up, which some algorithms really cannot. So this this is a good test test example. But in fact, I don't think I can actually illustrate real difference between Aiden and other adaptive variants. So here is what SGD does SGD goes. As, as you would assume goes in the correct direction, unless it diverges, completely. Of course, you can always have your learning create to be too high so that everything diverges, but if it's not too high then of course it goes in the necessary Direction and the faster you go the closer you get. But If you go too fast, you risk Divergence, so with SGD, it's always about finding the best learning rate. If you had momentum, you have exactly the same effects that we discussed. Right? So standard test gd, goes and goes but it's still has a long way to go. SGD with momentum almost left the base of this minimum at all most fail to over here. But thankfully it could come back but then it overshoots. The optimal by a long time by by far and as you can see this appeared on the right hasn't come back yet into 200 steps. While Nestor of momentum, yeah, it is already coming back. It's still not here, but obviously it's the best of the three. So it's, it's already coming back and it will be theirs. And that's for this algorithms that we discussed, like SGD is a great Delta. Well, they kind of do better but there is no real difference here. So, a Delta is worse but also, you shouldn't come to continuous about this and a great and Aiden they just both do a good job over here. So, there is no significant difference but as an illustration again, here is what optimization looks like Dimension too. It's not a good guide to vote optimization looks like in dimension 100 but for unfortunately cannot plot dimensional 100 for you. And before we wrap up, I think I have just a couple more. Things that I wanted to mention today. so, one thing is, Mmm, one thing is a version of freedom. It's the and again it's it's a version of Freedom that First of all is practical it. You can actually encounter it in deep learning practice. It actually happens. But also, it comes from a, very interesting, it comes from a very interesting motivation. So let me explain the motivation to you and then I will mention this. This version the motivation comes from a different way of doing regularization When you? when people did classical on neural networks, back in the day, back in the 1980s, back in the 1990s, regularization was usually done through this process called Wade, decay So what is weight Decay? What is the difference between regularization that we just discussed yesterday and wait till like this? In regular. Regularization part in the pan. You have like L of w being your loss function, plus something like Alpha times irregular eraser. And then you minimize your loss function with regularized, that's it. So notice that regularization like this, like L2 regularization one regularization, it's very, very easy to do in the blurry because all that you do is it's a slight modification of the Lost function. The algorithms don't have to change, just your computational graph gets a couple more notes and that's it. But in classical neural networks, they did a different. It, did it like this? So, wait, the K looked like this when you go from in your gradient descent, when you go from wkwk plus one before adding the gradient, you multiply you shrink the ways that you have, you multiply them by a constant list and one and then, You add or subtract? The current value of the gradient. Okay, so regularization. Why is it called weight Decay? Because weights, Decay a little and then you do your gradients. it looks pretty weird and actually pretty soon people realized that it's the same thing as SL2 regularization. When it over again, just send it. You can just so, Let's just continue this formula and let me write it like this. So it's a WK minus 1. Minus. What time double, okay? Right. I'm just pulling out the WK itself. Minus Alpha times UK. So and what is JK? Sorry, JK is the gradient of L. With respect to W at Point k. So why don't I take this part and just put it down to gradient here? Inside the gradient. So now I have WK minus Alpha times. The gradient of what Of L. and, Here, I have. Like some constant. One minus gamma divided by Alpha whatever that is times, just WK times, W Times W, right? Just the norm of W squared, And I need to do it at Point WK. So, when you look at this way, you see that weight Decay like this? Is exactly equivalent to just tell to regularization with a certain the certain constant. It's Completely equivalent, it's completely the same. So people kind of forgot about wait, okay, didn't use it at the beginning of the deep learning Revolution, but then People realize at some point, also a pretty interesting idea. That okay, so classical way decay in regular gradient descent is exactly equivalent to 12 regular eraser. That's true. but if you are doing something like Adam, If you are doing some complicated thing with momentum and cumulative, exponential, moving averages of gradients squared and so on and so forth. Then this equivalence doesn't hold anymore. Right now. There is no equality. If if the update rule is not that simple. If the update rule is actually say Aiden. Right. So what people did at some point, they carefully worked this kind of regularization through Adam. And they. Saw what to modify inside it and it was actually pretty simple to it. But you had to do the math to see where it is. What to modify inside. Atom to make it more like weight Decay than more than elsewhere regularization. And the resulting algorithm is called Adam w. And the popular. Gradients and variant. So a popular algorithm so, Okay, I I think I should be stopping here. So let me just mention, I didn't plan to discuss them and detail, but let me mention that of course the the research didn't stop on Adam and Adam W. There are recently developed algorithms like sealion and muon. And they have their own interesting properties. There is an algorithm one of them. I will keep forgetting which one that was obtained by actually automated search like the automated search that produced switch. Actually this fish activation function but for gradient descent algorithms. Why not? The other uses special properties of Transformers and this very useful for internal layers of language, models, whatever. So, the research continues, but Still. I think even in 2026 the standard algorithm would be something like aide or Aid in W or actually still very useful classical SGD. It's still, it's still a reasonable algorithm if you can pick the learning grid. So in conclusion, let me just quickly go through the slide to see what I've forgot. Okay, so this this is our example. This is Nestor of this is Uranus of for some reason, don't scale a lot. RMS probe Adam. That's what we just discussed. I made them. Okay, there is a, there is a version of Adam with Nestor of momentum called natum. Never heard about it afterwards. Etc. Etc. Then I will definitely skip this so fixing way. Decatur recognization item. This is Adam w. Https weight decade. I was very Decay, it has some good properties, which I don't have time to go into now and let me finish. Yeah, let me finish with this slide one. Like two, two last stories that both make the same general point. The first is the story of super conversions. Back in 2017. There was a very famous paper called super convergence that proposed to do a cycling learning creates schedule. What that means is. We slow down the training, we decreased learning create. And then at some point, we speeded back up again. So we go so slow. And then suddenly, We rise up again and do a large update and then we'll be sold on again. And they showed in some very convincing experiments. Of course there couldn't be any theorems about it, but they did and some very did some very convincing experiments and they actually showed that they can converge to approximately the same results, not better, but the same results, but much much, much faster, like that doesn't 10 10x 20x faster. And it was all the boss in 2017. But now we never hear about it. So say I click on learning creates are still a thing but they're not universally accepted and they probably are not going to use them in practice. This is one example. and the, after example, Also related to those stochastic gradient descent, which is why I'm talking about. This example here, the answer and example is a mass grad. It was a great paper in 2018 at one iclr 2018, best paper award, it was a great idea. So, they basically took the Aiden paper. Ah, in the Aiden paper, they had a convergence proof. They they couldn't estimate the rate of conversation but they had approved. The Tatum converges and these guys, Found the mistake in the proof. And these guys showed counterexamples where Aiden can actually diverged, where it does not converge. Where it doesn't work at all, right? And what's even better, they could fix it. They proposed. As a small modification of atom, called M as grad. That basically replaces like the sum with the max somewhere or something like that. I they algorithm is in front of you. and, For this algorithm they could prove convergence and the proof. Now was correct. so, They found a mistake in Adam and they fixed it and now you have four eight years. We've heard an algorithm, which is probably better than Adam. but my point is unfortunately, nobody is at I've never heard about anybody using, Ms, Groton practice. I guess you can use it. It's probably implemented to know the libraries. I guess you can try it. It'll probably be either exactly the same as Adam or even worse. So, let me close with this slightly disappointing point that. Even good ideas even ideas that get confirmed by your experiments that get confirmed even by Theory. So the theory is correct. There is indeed a mistake in their paper and this paper does not have a mistake this paper that did fix it. But unfortunately, it's not enough. To get a new universally accepted algorithm. It's still still practice is the final Arbiter, still? We like, we as a field are very applied, very practical filter, artificial intelligence, deep learning specifically. So ultimately people are going to use what works and Adam still works. so, with this, I want to stop for today. Are there any questions comments discussion? Okay, thank you. Yes, of course, I want feedback about the lectures. Thank you very much. I'm a bit surprised that gradient descent and back. Proper new for you, but good, then it's good that we repeated it. Okay? Wonderful. okay, thank you very much and with that, I pretty sure you're tired of listening to online lectures for three days straight, I would be definitely. So it's a good thing that I See the floor to Alex. Whom you will meet tomorrow and he will have practice starting tomorrow. Thank you and bye. Bye. Good question. Yeah. So are we next week? We're going to continue this online, lectures. That is a good question. Yeah, yeah. So that there is a scheduling there are scheduled in difficulties for me personally because I'll be traveling next week. So I hope there will be if you'll actually next week but at this point I cannot promise wish they okay. so, I think I think our plan for now. Is like tomorrow, definitely is practice day tomorrow is our top practices and then hopefully I will have one, we will have one practice in one lecture on Friday and then next week is wide open. I don't know about next two kids. Okay, thank you very much and bye-bye. I will upload everything as usual. Bye.
