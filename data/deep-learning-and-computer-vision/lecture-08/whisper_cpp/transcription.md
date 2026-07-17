# Transcript — whisper_cpp

- **Provider:** whisper_cpp
- **Language:** en
- **Audio duration:** 1:42:49
- **Segments:** 1034
- **model:** ggml-large-v3-turbo.bin
- **vad:** True
- **beam_size:** 5
- **entropy_thold:** 2.8
- **latency_sec:** 793.63

## Segments

**[00:11 – 00:32]** Okay. Hello, everyone. And welcome back. We have only two lectures left, which is, of course, very little time to cover a lot of the generative AI that we actually planned to go on to.

**[00:34 – 00:45]** But still, I think that even in two lectures, we can cover a couple of very interesting and very important and still very relevant ideas.

**[00:46 – 00:56]** Today, we talk about generative adversarial networks, GANs. It's a beautiful idea underlying the stuff, which is completely non-mathematical.

**[00:56 – 01:05]** It's just very cool and very logical, but it leads to very beautiful mathematics a little bit down the road.

**[01:06 – 01:18]** But before we go there, let me begin today with the structure of generative AI as a whole.

**[01:18 – 01:35]** Our first part today will be about generative models in general and what kinds of generative models exist in deep learning.

**[01:35 – 01:49]** So when we say generative AI, when we say generative models, it's not a very well-defined term because you can say that logistic regression generates the probability distribution over classes.

**[01:49 – 02:00]** So the divide is that in generative AI, you are producing something big.

**[02:00 – 02:11]** You are producing an object usually of high dimension and of complicated structure like an image or like text.

**[02:11 – 02:19]** So generative models are models that write, that draw, that produce music, videos, something like that.

**[02:19 – 02:30]** And when we talk about generative models, so let me draw a taxonomy for you, this will be our first subject for discussion.

**[02:30 – 02:42]** So of course I will be talking only about deep generative models, so models that are based on neural networks.

**[02:42 – 02:49]** And there are several important classes of these models.

**[02:49 – 02:52]** And today we will live in one of these classes, tomorrow we will live in another.

**[02:52 – 03:01]** But I still want to draw a general taxonomy so that you can actually better understand what's going on.

**[03:01 – 03:13]** The first divide, the first serious fork in deep generative models comes in the distinction between explicit density models.

**[03:13 – 03:23]** I'll explain in a sec. And implicit density models.

**[03:23 – 03:30]** So what does explicit and implicit density mean?

**[03:30 – 03:41]** When you have a generative model, it takes as input something like random noise or some condition or whatever.

**[03:41 – 03:44]** Then there is this black box which we are trying to define.

**[03:44 – 03:51]** And then at the output, there is like a picture of a cat or something.

**[03:51 – 03:55]** There is X that lives in a very high dimensional space.

**[03:55 – 03:59]** And this X has a very complicated distribution.

**[03:59 – 04:08]** If you try to imagine, as I think I made this argument once in our class,

**[04:08 – 04:17]** try to imagine the manifold of realistic photos in this 3 million dimensional space of 1 megapixel images.

**[04:17 – 04:24]** Obviously we cannot imagine anything like that, but also obviously it's very, very, very complicated.

**[04:24 – 04:30]** So P of X, the distribution of axes that we are trying to approximate, that we are trying to model,

**[04:30 – 04:32]** is very, very, very complicated.

**[04:32 – 04:38]** And the difference between explicit and implicit density models

**[04:38 – 04:44]** is that in explicit density models you get an explicit model for the density.

**[04:44 – 04:51]** So there is this P of X is actually equal to something in the model,

**[04:51 – 04:57]** and you can actually find out what it is equal to, so to speak.

**[04:57 – 05:06]** Naturally, we will not be able to get the actual distribution of CAD photos,

**[05:06 – 05:12]** but we can approximate, and we can try to approximate.

**[05:12 – 05:23]** And then, inside explicit density models, we have the next divide between tractable density models.

**[05:23 – 05:31]** And let me pause here and explain.

**[05:31 – 05:37]** So tractable density basically means that you can have a formula for P of X.

**[05:37 – 05:45]** It makes such strong assumptions that you actually can just write down that P of X is equal to something.

**[05:45 – 05:53]** And usually when we say tractable density, we mean an autoregressive model.

**[05:53 – 06:12]** So an autoregressive model is a model that makes use of this kind of obvious identity.

**[06:12 – 06:17]** That if you have this big, big X, then you can do something like...

**[06:17 – 06:31]** And you can decompose it into something like P of X1, P of X2 given X1, P of X3 given X1 and X2 and so on until P of Xn given X1, Xn minus 1.

**[06:31 – 06:33]** Right? So this is always true.

**[06:33 – 06:45]** And of course, since it's always true, it's also completely useless because you're not making anything easier for you because this is still a very big function of a lot of variables.

**[06:45 – 06:50]** But then you can simplify, then you can make assumptions.

**[06:50 – 06:56]** So you can make, I don't know, you can make a Markov chain out of this.

**[06:56 – 07:01]** You can say that every next X depends only on the previous ones.

**[07:01 – 07:16]** Or you can have an RNN here, which says that, OK, I model a sequence, but every next output depends only on the current.

**[07:16 – 07:24]** Input and the hidden state, which is also a part of the state, part of the model variables here.

**[07:24 – 07:28]** And then you get another simplified decomposition and so on.

**[07:28 – 07:42]** So, of course, it would be a lot of the models that exist happen to be in the autoregressive class.

**[07:42 – 07:52]** For example, all LLMs are here, almost all LLMs are here because LLMs predict the next token.

**[07:52 – 08:03]** So they model text, the sequence of tokens, as a sequence of, exactly as this, as p of x, k, given the previous context.

**[08:03 – 08:09]** And then, of course, the question is how to model this conditional distribution.

**[08:09 – 08:12]** And that's where transformers come in, that's where all the models come in.

**[08:12 – 08:18]** But the basic assumption is this: we produce and generate text one by one.

**[08:18 – 08:22]** And there have been models for pictures here, too.

**[08:22 – 08:30]** There were things like PixelCNN that produced images pixel by pixel,

**[08:30 – 08:33]** and it was a good model in terms of the output.

**[08:33 – 08:42]** But, of course, producing images pixel by pixel is just way too inefficient,

**[08:42 – 08:46]** because you need to generate a million pixels,

**[08:46 – 08:50]** and running your model a million times is, of course, infeasible,

**[08:50 – 08:53]** even if it's not very complicated.

**[08:53 – 08:59]** So pixel-wise autoregressive models are not really used,

**[08:59 – 09:02]** and we won't talk about them, but they also exist.

**[09:02 – 09:04]** It's a natural idea.

**[09:04 – 09:09]** And for text, basically everything is autoregressive.

**[09:09 – 09:17]** And then what else is there that we also will not have time to talk about?

**[09:17 – 09:24]** Interactable density, you can have something like a flow-based model.

**[09:24 – 09:30]** So one way to decompose a complicated distribution

**[09:30 – 09:36]** is to separate the variables inside x, like the autoregressive style.

**[09:36 – 09:48]** And another way is to say, well, okay, what if p of x is a big composition of simple transformations?

**[09:48 – 09:58]** Something like fk composed with fk minus 1, composed, composed, composed, f2, f1 of z.

**[09:58 – 10:05]** So we are still modeling something like this, and we are doing it explicitly.

**[10:05 – 10:15]** Each f is a simple thing like adding Gaussian noise or linear transformation or something like that.

**[10:15 – 10:22]** But when you compose a lot of simple transformations, like always in neural networks,

**[10:22 – 10:25]** this is not a neural network, but like always in neural networks,

**[10:25 – 10:33]** you get this capability of modeling something much, much more complicated, right?

**[10:33 – 10:38]** So we won't talk about flow-based models in all time, unfortunately.

**[10:38 – 10:46]** And apart from tractable density, you can have approximate density models.

**[10:46 – 10:52]** So here, in a way, you could repeat the same structure,

**[10:52 – 10:59]** but now instead of modeling p of x, instead of making assumptions about the distribution itself,

**[10:59 – 11:04]** we explicitly say that we approximate p of x with some simpler q,

**[11:04 – 11:08]** and now this q is a product of something easier.

**[11:08 – 11:16]** And here, the main example that is very, very relevant,

**[11:16 – 11:19]** it's a pity that probably we won't have time to talk,

**[11:19 – 11:23]** but maybe I'll talk about them tomorrow, maybe.

**[11:23 – 11:26]** The main example are variational autoencoders.

**[11:26 – 11:35]** This is one of the most important ideas in the whole deep learning,

**[11:35 – 11:45]** how to use variational approximations to get good loss functions for generative models.

**[11:45 – 11:50]** Variational autoencoders are used all the time.

**[11:50 – 11:54]** For example, tomorrow we will talk about diffusion models,

**[11:54 – 11:59]** and diffusion models usually operate in the latent space of a variational autoencoder,

**[11:59 – 12:02]** but I'm getting a bit ahead of myself.

**[12:02 – 12:09]** Now, of course, explicit density part is big and varied and rich.

**[12:09 – 12:12]** There are lots and lots and lots of different approaches here.

**[12:12 – 12:17]** The implicit density side is not that rich.

**[12:17 – 12:23]** There are much fewer examples here,

**[12:23 – 12:30]** and actually I won't even make any other examples because they are kind of esoteric.

**[12:30 – 12:38]** The main example of implicit density generative models are GANs that we discussed today.

**[12:38 – 12:42]** And what does it mean not to have a density for X?

**[12:42 – 12:55]** Like how can you have a model that produces axes that gives you cat photos,

**[12:55 – 13:01]** but does not have anywhere a formula for P of X or even an approximation to P of X?

**[13:01 – 13:06]** Well, you just have to take this picture literally, right?

**[13:06 – 13:12]** So an implicit density model will start with random noise,

**[13:12 – 13:18]** and then it will actually produce just a sample X,

**[13:18 – 13:25]** which is supposed to be taken from the distribution P of X.

**[13:25 – 13:30]** It will produce a sample cat picture that is supposed to be a good cat picture.

**[13:30 – 13:38]** And if you look at it this way, if you look at your neural network,

**[13:38 – 13:44]** at your model, as this sampling procedure, as a sampler,

**[13:44 – 13:51]** well, not a sampler, as a transformation of probability distributions

**[13:51 – 13:57]** from a simple one, from random noise like just standard Gaussian,

**[13:57 – 14:01]** to this very complicated one in this huge dimensional space, etc.,

**[14:01 – 14:05]** then it all kind of starts to make sense, right?

**[14:05 – 14:12]** So if you just have a black box that samples cat photos for you,

**[14:12 – 14:16]** you cannot really extract a formula from this black box.

**[14:16 – 14:19]** I mean, you could maybe make a trillion examples

**[14:19 – 14:22]** and then learn one of the explicit density models,

**[14:22 – 14:24]** but that doesn't count.

**[14:24 – 14:27]** The black box itself doesn't have the formula anywhere.

**[14:27 – 14:31]** So this is what GANs do.

**[14:31 – 14:36]** And now the first part is over.

**[14:36 – 14:38]** I've talked about this general structure

**[14:38 – 14:41]** and maybe we'll return to it tomorrow.

**[14:41 – 14:45]** And now, what are GANs?

**[14:45 – 14:48]** What is their main idea?

**[14:48 – 14:57]** So we talk about generative adversarial networks, GANs.

**[14:57 – 15:02]** And in the general...

**[15:02 – 15:04]** Sorry.

**[15:04 – 15:09]** The generative adversarial network is based on this very...

**[15:09 – 15:15]** ...interesting...

**[15:15 – 15:22]** It's one possible solution to a very deep problem in generative models.

**[15:22 – 15:24]** And we will discuss other...

**[15:24 – 15:29]** If we get to YS, we will discuss other solutions to this problem.

**[15:29 – 15:34]** But here is the problem, basically.

**[15:34 – 15:43]** The main problem of generative AI in general...

**[15:43 – 15:46]** I mean, there are many ways to solve it.

**[15:46 – 15:50]** It's not like it's an open problem, but the main deep problem...

**[15:50 – 15:54]** ...that you need to solve when you create a generative model...

**[15:54 – 15:57]** ...is what is your loss function?

**[15:57 – 16:02]** How do you score the results?

**[16:02 – 16:08]** So let me start drawing this picture for you, right?

**[16:08 – 16:13]** So I have this random noise scene...

**[16:13 – 16:18]** ...which is basically just taken from some standard distribution or whatever.

**[16:18 – 16:25]** And then this random noise scene gets to the generator network...

**[16:25 – 16:29]** ...gets to the model that maps random noise...

**[16:29 – 16:35]** ...to something that is supposed to be a cat picture, right?

**[16:35 – 16:40]** Let's call it X hat because it will be like a predicted cat...

**[16:40 – 16:44]** ...not yet a real cat.

**[16:44 – 16:51]** So let's think of it as a learning problem...

**[16:51 – 16:53]** ...as a machine learning problem.

**[16:53 – 16:55]** If you look at this as a machine learning problem...

**[16:55 – 16:59]** ...well, you do have a data set of axes, right?

**[16:59 – 17:01]** So what does your data look like?

**[17:01 – 17:07]** Your data is a lot of cats, a lot of cat photos.

**[17:07 – 17:12]** But you don't have paired data for this, right?

**[17:12 – 17:20]** You cannot just say that this X hat should be similar to some X in the training set...

**[17:20 – 17:23]** ...because you have no idea which one, right?

**[17:23 – 17:31]** There isn't and there will never be a dataset that pairs random noise...

**[17:31 – 17:36]** ...with images that are supposed to be produced from this random noise.

**[17:36 – 17:38]** This doesn't make sense.

**[17:38 – 17:42]** The whole point of learning a generator is to learn this mapping...

**[17:42 – 17:49]** ...and to get a good and relatively simple parameterization in the noise space...

**[17:49 – 17:58]** ...so that next week we would be able to just take random noise and still get reasonable cat pictures.

**[17:58 – 18:04]** So the data is unlabeled. It's unsupervised learning.

**[18:04 – 18:10]** So where will the loss function come from?

**[18:10 – 18:13]** Which X should Z be similar to?

**[18:13 – 18:19]** Well, you can say, okay, I don't have any specific X in mind.

**[18:19 – 18:23]** I just want the result, this X head, to be a good cat picture.

**[18:23 – 18:30]** And this sounds reasonable, and this is exactly what we'll do.

**[18:30 – 18:34]** But what does it mean to be a good cat picture?

**[18:34 – 18:38]** This is the deep question that we need to answer.

**[18:38 – 18:50]** Because there is really no mathematical function that you can run

**[18:50 – 18:55]** and say if this photo is a cat picture, is a good cat picture.

**[18:55 – 18:58]** If this set of pixels is a good cat picture.

**[18:58 – 19:00]** This is something that you have to learn yourself too.

**[19:00 – 19:05]** And this is like half of the problem, if not most of the problem.

**[19:05 – 19:09]** So generative adversarial networks say the following.

**[19:09 – 19:18]** They say, well, okay, you recognize that you need to learn your loss function.

**[19:18 – 19:20]** That you need to work for it.

**[19:20 – 19:29]** You do not have a fixed formula for evaluating how catchy this image looks.

**[19:29 – 19:32]** So let's do it. Let's work for it.

**[19:32 – 19:56]** Let's have a whole separate network, both a discriminator, whose only goal, whose only job is to say whether the input...

**[19:56 – 20:02]** So as input it takes photos, and as output it does just binary classification.

**[20:02 – 20:06]** Is it fake or is it real?

**[20:06 – 20:10]** Let's say that real is one and fake is zero.

**[20:10 – 20:23]** So the discriminator gets a picture, and if it's a picture produced by the generator, then it should say that it's fake.

**[20:23 – 20:33]** And if it's a real picture, so we can take our data and we can sample a real cat photo from it.

**[20:33 – 20:40]** This will be real x, x real, and this is x fake.

**[20:40 – 20:46]** So if a real picture is fed into the discriminator, the output should be one.

**[20:46 – 20:54]** In this way, the generator and the discriminator are at odds with each other.

**[20:54 – 20:58]** They have opposing interests.

**[20:58 – 21:04]** The discriminator wants to learn to distinguish between real images and images produced by the generator.

**[21:04 – 21:09]** And the generator wants to fool the discriminator.

**[21:09 – 21:15]** So this general idea is called adversarial training.

**[21:15 – 21:23]** And you may hear that GANs are not what they used to be.

**[21:23 – 21:32]** And indeed, GANs are not, for the last few years, GANs are not at the forefront of image generation.

**[21:32 – 21:38]** The images these days are generated by diffusion models, which we will talk about tomorrow.

**[21:38 – 21:42]** But adversarial training is very much alive.

**[21:42 – 21:47]** And even in the diffusion models, we will see exactly this idea.

**[21:47 – 21:54]** And we will see a little bit of a GAN embedded into a diffusion model and making it better.

**[21:54 – 22:02]** So this is, of course, still a very important idea in machine learning.

**[22:02 – 22:06]** And it appears in many different fields.

**[22:06 – 22:10]** Of course, we are only talking about images, but still.

**[22:10 – 22:17]** So let me maybe show you some nice pictures.

**[22:17 – 22:21]** I think I have the intrapictures about GANs.

**[22:21 – 22:25]** This is the main idea, and as you can see, it's very simple.

**[22:25 – 22:35]** So the generator is like forging a picture, and the discriminator is the detective that needs to decide whether it's real.

**[22:35 – 22:43]** And ideally, it should look something like this.

**[22:43 – 22:53]** So this is an example where the generator, which is called reverse deep convolutional neural network here,

**[22:53 – 22:59]** the generator learns to counterfeit money, learns to produce pictures of real money.

**[22:59 – 23:02]** And at first, it just produces something.

**[23:02 – 23:08]** Actually, this is a few steps in, because at first, the generator will just produce random noise.

**[23:08 – 23:11]** But then it produces some very bad counterfeit.

**[23:11 – 23:18]** And then the discriminator will say, "Oh, well, I don't know any better.

**[23:18 – 23:23]** So this seems legit, and I am fooled."

**[23:23 – 23:29]** Okay, so I provide once on fake images.

**[23:29 – 23:36]** So then we train the discriminator, and now it learns to distinguish.

**[23:36 – 23:41]** It understands that this is not real money, not real American dollars.

**[23:41 – 23:47]** And then we actually, often it's done exactly like this.

**[23:47 – 23:54]** So we fix the discriminator that has trained for a while.

**[23:54 – 23:59]** So we train the generator to fool this current version of the discriminator.

**[23:59 – 24:05]** So we say, oh, okay, now the discriminator doesn't accept our counterfeits.

**[24:05 – 24:07]** What should we do?

**[24:07 – 24:10]** Let's train a little bit more and produce a slightly better counterfeit.

**[24:10 – 24:13]** It will still be bad.

**[24:13 – 24:21]** Because, again, there is no general loss function that will tell you if the image is good.

**[24:21 – 24:30]** There's only this specific discriminator that has learned to not be fooled by some attacks.

**[24:30 – 24:36]** So at this point, it will produce a better counterfeit.

**[24:36 – 24:39]** And then the discriminator will find some other features to discriminate on.

**[24:39 – 24:43]** And then the generator will have to learn to fake those features too, and so on.

**[24:43 – 24:46]** So they're kind of playing this game.

**[24:46 – 24:51]** And the hope is that everything happens.

**[24:51 – 24:53]** I will walk you through the formulas in a minute.

**[24:53 – 24:58]** But the hope is that everything happens like on this idealized image.

**[24:58 – 25:04]** So here, for example, the generator is represented by these arrows.

**[25:04 – 25:09]** These arrows, as you can see, in Z, we have the uniform distribution every time.

**[25:09 – 25:13]** And in X, we have like this Gaussian, the green Gaussian.

**[25:13 – 25:16]** And the black dots are the data points.

**[25:16 – 25:21]** And so at first, this Gaussian doesn't look like the black dots.

**[25:21 – 25:26]** So the blue dashed line is the discriminator. It's just a logistic sigmoid, right?

**[25:26 – 25:32]** So it's a sigmoid curve that distinguishes between these two Gaussians.

**[25:32 – 25:35]** And then here is the crucial part.

**[25:35 – 25:46]** At this point, the discriminator trains, but it's not training to mimic the data because that is impossible.

**[25:46 – 25:53]** I mean, in this case, it would be possible, but in the high dimensional case of pictures, it would not be possible.

**[25:53 – 26:01]** So the generator learns to fool the discriminator.

**[26:01 – 26:08]** So in this case, it's enough to move this Gaussian a little bit over here, and the discriminator is already fooled.

**[26:08 – 26:11]** It doesn't need to go all the way to the data points.

**[26:11 – 26:18]** But then, of course, the discriminator will be able to distinguish between these two bell curves and so on.

**[26:18 – 26:27]** But finally, we will get to this perfect picture where the generator is perfect and the discriminator has no idea what to do and just flips a coin.

**[26:27 – 26:34]** So, of course, in real life it's not going to work like that, but the idea is exactly this.

**[26:34 – 26:42]** So what is interesting about the problem setting here?

**[26:42 – 26:49]** Well, let's write down the loss functions. Let's see mathematically what is happening here.

**[26:49 – 26:56]** So first, the discriminator, right? So what is the discriminator loss LD?

**[26:56 – 27:01]** Well, let me write it in this form.

**[27:01 – 27:08]** So the discriminator is supposed to say zero if it's fake and one if it's real.

**[27:08 – 27:17]** So let me write it as expectations. Doesn't really matter, but this will be cleaner for what comes next.

**[27:17 – 27:28]** So if I take a real photo from the dataset, from the training set,

**[27:28 – 27:33]** then I'm supposed to increase the output.

**[27:33 – 27:38]** I'm supposed to produce the score that goes to positive infinity.

**[27:38 – 27:42]** So the probability after the sigma, it will go to one.

**[27:42 – 27:49]** So I'm supposed to increase, to have a loss function, something like log d of x.

**[27:49 – 27:52]** Actually, minus log d of x.

**[27:52 – 27:56]** And then, if x is fake...

**[27:56 – 28:01]** So x fake is taken...

**[28:01 – 28:03]** Where is it taken from?

**[28:03 – 28:07]** It's taken from the distribution of the generator.

**[28:07 – 28:11]** Sorry, not x pg of z, right?

**[28:11 – 28:13]** From the distribution of the generator.

**[28:13 – 28:17]** No, actually, it's pg of x, right?

**[28:17 – 28:20]** So I'm taking it from this distribution,

**[28:20 – 28:25]** from the distribution that has come through the generator.

**[28:25 – 28:28]** Then I'm supposed to output zero,

**[28:28 – 28:34]** so I'm supposed to do something like this, right?

**[28:34 – 28:40]** And I want to minimize this loss function

**[28:40 – 28:44]** with respect to the parameters of the discriminator.

**[28:44 – 28:51]** So when I fix the generator and I just train the discriminator,

**[28:51 – 28:55]** this is a very straightforward binary classification problem.

**[28:55 – 28:58]** What does the generator do?

**[28:58 – 29:04]** Well, the generator is supposed to produce axes

**[29:04 – 29:10]** that pass for real for the discriminator.

**[29:10 – 29:14]** So basically, I mean, it cannot influence this part.

**[29:14 – 29:16]** There is no generator here.

**[29:16 – 29:19]** But for this part, the job of the generator

**[29:19 – 29:22]** is exactly opposite to the discriminator, right?

**[29:22 – 29:25]** So let me write it now completely.

**[29:25 – 29:28]** We start with some random noise.

**[29:28 – 29:34]** And then I want to actually take the discriminator loss

**[29:34 – 29:41]** on my results on GOC and do the opposite.

**[29:41 – 29:45]** So if here I was minimizing minus this,

**[29:45 – 29:50]** then here I will be minimizing plus this, right?

**[29:50 – 29:55]** So basically, you can say that the discriminator

**[29:55 – 29:58]** and the generator have the exact same loss function.

**[29:58 – 30:00]** I can just copy it here, it won't matter

**[30:00 – 30:03]** because it's just a constant for the generator.

**[30:03 – 30:07]** And what they are actually doing,

**[30:07 – 30:10]** let's say that I have this loss function

**[30:10 – 30:13]** that depends on the parameters of the generator

**[30:13 – 30:16]** and parameters of the discriminator.

**[30:16 – 30:21]** For this loss function, let's say that the discriminator

**[30:21 – 30:25]** wants it to be as big as possible.

**[30:25 – 30:29]** So let's say that this is the loss function,

**[30:29 – 30:32]** the thing in the brackets.

**[30:32 – 30:36]** So the discriminator wants to make it bigger

**[30:36 – 30:41]** and the generator wants to make it smaller.

**[30:41 – 30:45]** So we have this minimax game.

**[30:45 – 30:51]** It's actually something that has never happened

**[30:51 – 30:53]** to us in machine learning before

**[30:53 – 30:56]** and that will not happen since.

**[30:56 – 31:01]** We are not just doing optimization here,

**[31:01 – 31:03]** at least formally.

**[31:03 – 31:05]** We are doing adversarial optimization

**[31:05 – 31:08]** in the sense of game theory.

**[31:08 – 31:14]** And if you have ever had any classes

**[31:14 – 31:16]** in game theory or anything,

**[31:16 – 31:21]** you know that as soon as these quantifiers,

**[31:21 – 31:26]** this optimization goals like min, max, max, min, etc.

**[31:26 – 31:29]** as soon as they start to stack up,

**[31:29 – 31:34]** as soon as you have a minimax instead of just a min or just a max,

**[31:34 – 31:36]** the complexity is of the charts, right?

**[31:36 – 31:38]** So it's extremely hard,

**[31:38 – 31:45]** it's extremely difficult to actually optimize for in-game theory.

**[31:45 – 31:50]** And on the surface of this,

**[31:50 – 31:54]** it looks like this should be a hopelessly difficult problem.

**[31:54 – 31:57]** I mean, for us, it's hard enough to do just minimization,

**[31:57 – 31:59]** to just minimize the loss function.

**[31:59 – 32:02]** And here we are asking to do a minimax,

**[32:02 – 32:05]** to basically find the equilibrium in the game.

**[32:05 – 32:08]** This sounds completely impossible.

**[32:08 – 32:13]** Well, in reality, of course, it's not impossible.

**[32:13 – 32:21]** And there are some properties of these loss functions that make it simpler.

**[32:21 – 32:24]** And I will not go into the mathematical details.

**[32:24 – 32:32]** But basically, let me just tell you the result here.

**[32:32 – 32:36]** Basically, if you fix the generator,

**[32:36 – 32:41]** then you know exactly what the optimal discriminator is,

**[32:41 – 32:44]** because it's just the optimal Bayesian classifier.

**[32:44 – 32:47]** Remember bias formula, blah, blah, blah.

**[32:47 – 32:51]** So here, if I know the data distribution pdata,

**[32:51 – 32:54]** and I know the generator distribution pg,

**[32:54 – 32:57]** the answer is just the bias rule.

**[32:57 – 33:07]** The probability that x was real is the density of x under pdata

**[33:07 – 33:10]** normalized to the sum of pdata and pg.

**[33:10 – 33:13]** This is exactly the bias rule.

**[33:13 – 33:17]** And then, so this is straightforward,

**[33:17 – 33:21]** but the interesting part is that now you can take this formula

**[33:21 – 33:24]** and you can plug it into the generator loss,

**[33:24 – 33:30]** and what you get is basically a very simple result.

**[33:30 – 33:35]** You get that the generator is perfect,

**[33:35 – 33:41]** attains the global minimum of this criterion if pg equals to pdata.

**[33:41 – 33:45]** So this verifies that we are actually doing the right thing,

**[33:45 – 33:51]** that the generator is actually minimizing,

**[33:51 – 33:59]** is actually making pg closer to the true data distribution to pdata.

**[33:59 – 34:07]** In fact, it's doing it in a pretty interesting, non-standard way.

**[34:07 – 34:11]** So for the optimal discriminator,

**[34:11 – 34:18]** the generator actually is minimizing these Jensen-Shenen diversions,

**[34:18 – 34:22]** not the Kuhlbeck-Libler divergence between two distributions,

**[34:22 – 34:24]** which we usually minimize in machine learning,

**[34:24 – 34:32]** but like this averaged symmetrical version of KL,

**[34:32 – 34:37]** which is called the Jensen-Shenen averages.

**[34:37 – 34:42]** And I won't go into details about these results.

**[34:42 – 34:44]** I don't want to discuss them further

**[34:44 – 34:48]** because, unfortunately, they are completely irrelevant.

**[34:48 – 34:54]** So everything that we can say, like this theoretically,

**[34:54 – 35:00]** about this kind of minimax problems and the game theory stuff here

**[35:00 – 35:06]** and how we can substitute the perfect discriminator

**[35:06 – 35:08]** into the generator loss function, etc.

**[35:08 – 35:20]** All of this makes the assumption that we actually have this common loss function

**[35:20 – 35:22]** for the generator and the discriminator.

**[35:22 – 35:25]** And that's just not true in practice.

**[35:25 – 35:30]** So in practice, it turns out that this kind of generator loss,

**[35:30 – 35:35]** they just take the binary cross-entropy from the discriminator and flip it,

**[35:35 – 35:39]** that this is a very bad idea for the generator.

**[35:39 – 35:44]** And why? Because it saturates.

**[35:44 – 35:48]** And it's exactly the same problem that we discussed in Deplering several times.

**[35:48 – 35:51]** Again, I don't have time to go into full detail here,

**[35:51 – 36:00]** but basically this thing, this cross-entropy, is the output of a sigmoid.

**[36:00 – 36:04]** And if it saturates, it saturates, right?

**[36:04 – 36:12]** So if you are classifying it like the discriminator does,

**[36:12 – 36:16]** that's actually a good thing, at least not a bad thing.

**[36:16 – 36:22]** You saturate when you give the right answer, and that's fine.

**[36:22 – 36:39]** So if you are already giving the right answer and you are confident in this decision,

**[36:39 – 36:42]** in the right decision, then you don't need to change anything, right?

**[36:42 – 36:49]** But now, when you look at the generator, if the discriminator is very certain that it's right,

**[36:49 – 36:58]** and the discriminator has saturated and it's doing a very good job,

**[36:58 – 37:00]** it means that the generator is failing.

**[37:00 – 37:05]** It means that the generator does not produce believable results.

**[37:05 – 37:09]** The discriminator is easy. It's easy to distinguish from the discriminator.

**[37:09 – 37:14]** So this is the situation where we are supposed to train the generator.

**[37:14 – 37:21]** We are supposed to actually update its weights, but we can't

**[37:21 – 37:29]** because in the backpropagation, the loss is only over here.

**[37:29 – 37:35]** So the gradients for the generator have to go through the gradients of the discriminator.

**[37:35 – 37:39]** And as I just said, the gradients for the discriminator become near zero

**[37:39 – 37:43]** because the discriminator is saturated and already working very well.

**[37:43 – 37:48]** So if I reuse the same loss function, it's really a bad idea

**[37:48 – 37:52]** because it means that when I have trained the discriminator

**[37:52 – 37:56]** and in practice there is this alternating training usually.

**[37:56 – 38:01]** So we train the discriminator a little, then the generator, then the discriminator and so on.

**[38:01 – 38:06]** So when I train the discriminator a little and it becomes good at separating stuff,

**[38:06 – 38:11]** this is exactly when its gradients become near zero and the generator is very hard to train.

**[38:11 – 38:16]** So the same effect that we had in a slightly different form.

**[38:16 – 38:22]** As you can see, I am teaching you general ideas that appear over and over,

**[38:22 – 38:25]** the same as in your serial training today.

**[38:25 – 38:27]** So what do we do?

**[38:27 – 38:30]** Well, we change the loss function.

**[38:30 – 38:36]** And let me skip the early attempts at changing this loss function.

**[38:36 – 38:47]** Let me just show you the path that we have, the original GANs, how they work.

**[38:47 – 38:50]** And that was, what, 12 years ago?

**[38:50 – 38:52]** That's 2014.

**[38:52 – 38:59]** And in 2014, as you can see on these pictures, the green ones are real training samples.

**[38:59 – 39:06]** They are nearest neighbors from the training set to the adjacent picture.

**[39:06 – 39:13]** So you can actually verify that the model did not just memorize a few elements of the training set,

**[39:13 – 39:15]** but it's actually generating stuff.

**[39:15 – 39:20]** So as you can see, it worked wonderfully for Amnist.

**[39:20 – 39:25]** It worked much worse for these small black and white human faces.

**[39:25 – 39:33]** And it basically was very bad for anything else, for anything more diverse.

**[39:33 – 39:42]** So in 2014, GANs appeared, but they were no match to other generative models at that point.

**[39:42 – 39:45]** So what happened next?

**[39:45 – 39:48]** Next, there was DCGAN.

**[39:48 – 39:54]** DCGAN is basically the same kind of GAN, but with a new, better architecture,

**[39:54 – 39:58]** convolutional architecture for the generator and the discriminator.

**[39:58 – 40:05]** Again, no point in going into the details, but I want to make one remark here.

**[40:05 – 40:14]** So DCGAN already started to produce some reasonable pictures on some data sets.

**[40:14 – 40:20]** Still very small, still obviously bad in some ways.

**[40:20 – 40:26]** It was 10 years ago. Image generation was very bad back at the time.

**[40:26 – 40:29]** So this was actually state of the art 10 years ago.

**[40:29 – 40:33]** And yeah, just a side remark.

**[40:33 – 40:40]** If you look through old papers on GANs and on YS and on various generative models,

**[40:40 – 40:42]** you will see a lot of bedrooms.

**[40:42 – 40:51]** I don't know who started it, but at some point there is this data set called Large Scale Scene Understanding.

**[40:51 – 40:54]** So SU stands for Scene Understanding.

**[40:54 – 41:01]** And it basically is like several subsets of photos of different environments.

**[41:01 – 41:03]** And one of the environments was a bedroom.

**[41:03 – 41:10]** And when somebody chose this set of pictures for their tests,

**[41:10 – 41:21]** and of course after that everybody had to follow suit and had to compare their bedrooms with previous bedrooms.

**[41:21 – 41:24]** So you will see a lot of bedroom pictures.

**[41:24 – 41:33]** They are relatively small, like I think 64 by 64 pixels or maybe 128 by 128, something like that.

**[41:33 – 41:40]** But they are in color and they already kind of are supposed to look like real photos.

**[41:40 – 41:44]** And this is DC again after one epoch, still very bad.

**[41:44 – 41:49]** But after five epochs it starts to be more or less okay.

**[41:49 – 41:56]** So obviously nothing exciting by today's standards, but back then it was okay.

**[41:56 – 41:59]** And what I wanted to mention here is this idea.

**[41:59 – 42:02]** So this is important.

**[42:02 – 42:11]** Again, how do you illustrate, how do you understand yourself that you've got a good generative model?

**[42:11 – 42:13]** The discriminator will not tell you that.

**[42:13 – 42:16]** Because the discriminator will tell you, oh, I can't distinguish.

**[42:16 – 42:18]** It doesn't mean that the pictures are good.

**[42:18 – 42:22]** It doesn't mean that the latent space is good.

**[42:22 – 42:25]** It just means that the discriminator can't distinguish.

**[42:25 – 42:29]** Maybe you didn't train it well enough, maybe it's not large enough, it's not powerful enough.

**[42:29 – 42:31]** Who knows, right?

**[42:31 – 42:46]** So how do you, well maybe not measure, the metrics are a different story, but how do you at least see for yourself if the generator actually makes any sense?

**[42:46 – 43:06]** And the usual illustration goes like this, and I want to explain it because it's really a good illustration to what we are doing intuitively, geometrically in the latent spaces and so on.

**[43:06 – 43:37]** What is the generator actually doing? It's taking this random noise, this vector from the latent space Z, so this will be the latent space, and it's mapping Z to a point X, which is in pixel space, so to say, right?

**[43:37 – 43:56]** And in pixel space, in this huge million-dimensional space of images, the actual images that we are looking for form this extremely complicated and completely un-understandable manifold, right?

**[43:56 – 44:11]** So they have this very, very complicated structure. But in the latent space, our goal is to actually flatten this structure completely. Because what is our goal, really?

**[44:11 – 44:27]** Our goal is to be able to generate new images, right? So our goal is to be able to do the following: to take a random Z over here, Z from a standard Gaussian, right?

**[44:27 – 44:37]** From some very simple distribution. Doesn't matter if it's the Gaussian specifically, but Z from some very simple distribution that we can sample from directly.

**[44:37 – 45:02]** And take this random noise, put it through our generator, map it over here, and actually hope that the result will fall in this extremely complicated, very difficult, completely unimaginable manifold of real pictures, real photos, right?

**[45:02 – 45:14]** So this is the job of the generator. Here is the generator.

**[45:14 – 45:23]** So how do we test this? How can we understand if we actually did a good job in this?

**[45:23 – 45:30]** Well, here is one test that was very popular and that you can immediately see for yourself.

**[45:30 – 45:36]** It's very visual. And the test is, let's do a linear walk in the latent space.

**[45:36 – 45:51]** So in the latent space, if I take, for example, two different Zs, one here, one here, so they will produce two different pictures.

**[45:51 – 46:01]** They will produce two different pictures, right? The green one and the orange one.

**[46:01 – 46:19]** Then in the latent space, if I'm supposed to get them from the standard Gaussian, it means that if I just walk from one of the Zs to the other, let's say this is Z2 and that one was Z1.

**[46:19 – 46:41]** So if I walk from one random sample to another random sample over here, this I can do just along a straight line and along the straight line, all of the intermediate Zs should give me reasonable images.

**[46:41 – 47:01]** OK, this is the main test. So if G, if the generator was stupid and it wasn't doing much and they just memorized a few data points and then the Zs would get mapped to these data points, it would still look good on the training set.

**[47:01 – 47:07]** But if I go from one Z to another, then here it would do something nonsensical.

**[47:07 – 47:14]** For example, it might walk along a straight line in the pixel space.

**[47:14 – 47:21]** And if you go along the straight line in the pixel space, you don't get realistic photos, right?

**[47:21 – 47:27]** You get one photo and then the other kind of appearing through it

**[47:27 – 47:34]** and it's like you're making one of them more transparent and the other shows up underneath.

**[47:34 – 47:39]** So it's definitely not a walk through realistic photographs.

**[47:39 – 47:49]** What you are supposed to have in the ideal case is a walk in the pixel space

**[47:49 – 47:55]** that also follows this manifold and goes from one X to the other.

**[47:55 – 48:02]** So on every intermediate step through this straight line,

**[48:02 – 48:10]** you are supposed to get a realistic photo somewhere on the manifold.

**[48:10 – 48:14]** And if you get that and if you see it consistently true,

**[48:14 – 48:19]** then it does mean that you can sample, or at least you can hope to sample random Zs

**[48:19 – 48:22]** and get realistic images.

**[48:22 – 48:30]** So if you look in these papers and generative models,

**[48:30 – 48:37]** you will often see this kind of walks through the feature space or through the latent space.

**[48:37 – 48:44]** The left and the right part are actual images or something from the training set

**[48:44 – 48:48]** or some images that are guaranteed to be good.

**[48:48 – 48:51]** And now you walk through the latent space and you see...

**[48:51 – 48:54]** So in the latent space, you walk along the straight line

**[48:54 – 48:57]** and you see what happens in the pixel space.

**[48:57 – 49:02]** And as you can see here, there may be some strange stuff happening in the middle,

**[49:02 – 49:06]** but more or less, they are all kind of realistic,

**[49:06 – 49:13]** at least on the same level of realistic as the images on the side.

**[49:13 – 49:18]** So this was, I think, the first GAN

**[49:18 – 49:22]** which was already the state of the art of image generation.

**[49:22 – 49:26]** It even had some kind of vector arithmetic.

**[49:26 – 49:29]** It didn't work out later, so let me skip.

**[49:29 – 49:36]** But also, that was the time when GANs,

**[49:36 – 49:39]** they were already state of the art.

**[49:39 – 49:45]** And what I just showed to you was indeed state of the art image generation 10 years ago.

**[49:45 – 49:50]** You can, again, marvel at the progress, at the rate of progress.

**[49:50 – 49:54]** But they were still kind of bad.

**[49:54 – 50:01]** You wouldn't use them for generating production images like today.

**[50:01 – 50:07]** I obviously generate, get pictures like this one, and I like the results.

**[50:07 – 50:13]** But back then, these are not real bedroom photos.

**[50:13 – 50:25]** And back then, there were some common problems with generation, specifically with GAN-based generation, that you may remember.

**[50:25 – 50:35]** I mean, they were all across the internet and stuff like that were like common failure modes of GANs.

**[50:35 – 50:41]** And maybe you will actually see some failure modes like this in your practical sessions.

**[50:41 – 50:45]** So they definitely had problems with counting.

**[50:45 – 50:49]** I mean, the recent meme was about six fingers on a hand.

**[50:49 – 50:52]** Like a couple of years ago, it was still a problem.

**[50:52 – 50:53]** Today it's not.

**[50:53 – 51:01]** But back like 10 years ago, it was much worse than six fingers on a hand, right?

**[51:01 – 51:07]** There would be like three heads of a dog with who knows how many eyes and so on.

**[51:07 – 51:17]** And that actually makes sense as a failure because when you look at something like this reverse convolutional network,

**[51:17 – 51:22]** what it's doing is it has this general idea, the general features,

**[51:22 – 51:29]** and then it specializes and it draws different parts of the image then more or less independently.

**[51:29 – 51:39]** And basically what this failure mode means is that, well, I am here and I only have a small context

**[51:39 – 51:45]** around this eye. So I'm not really sure, is it the right eye or the left eye?

**[51:45 – 51:50]** And I decide, okay, so maybe this is the right eye and I need another one.

**[51:50 – 51:55]** And then I do the other one and again, I'm not sure, is it the left or the right?

**[51:55 – 52:00]** And again, I do another one. So I think the mechanism was something like this.

**[52:00 – 52:04]** And the same goes for problems with perspective.

**[52:04 – 52:11]** So here I was generating this dog and they got to the head of the dog.

**[52:11 – 52:16]** And now I don't have enough context to understand what was the angle I was looking from.

**[52:16 – 52:21]** And now the other half of the dog is from a completely different thing.

**[52:21 – 52:24]** And actually, this stuff is hard.

**[52:24 – 52:32]** So these kind of mistakes, they stand out for us because our vision is very good.

**[52:32 – 52:35]** We know the world. We know how it's supposed to look like.

**[52:35 – 52:39]** And we learned it in the first years of our lives.

**[52:39 – 52:42]** But it's actually very, very difficult.

**[52:42 – 52:52]** And this kind of, for example, generating stuff in proper perspective as if it was a three-dimensional world is really difficult.

**[52:52 – 53:01]** And for example, among these images, if we were offline, I would say raise your hands.

**[53:01 – 53:10]** But just how many of you actually realized that one of these images does not belong here?

**[53:10 – 53:23]** And usually it takes a few questions for people to actually see that this cat over here is just a real photo.

**[53:23 – 53:30]** There is nothing bad about this. It's just a cat which is sleeping all curled up like this. Cats do it, right?

**[53:30 – 53:37]** So it's difficult. And it was difficult.

**[53:37 – 53:43]** But image generation has made tremendous progress.

**[53:43 – 53:49]** And this picture, of course, I have been showing it since 2018.

**[53:49 – 53:57]** But honestly, you can extend it. There are, of course, newer and better models for human faces too.

**[53:57 – 54:03]** But it would be pointless because in 2018, you already probably cannot see the imperfections.

**[54:03 – 54:10]** There are imperfections here, but on a slide, I don't think you can see them.

**[54:10 – 54:16]** But in 2014, I think you can see, right?

**[54:16 – 54:26]** And you can actually see how much progress GAN-based generation made in just these four or five years.

**[54:26 – 54:30]** So how did that happen? What were the main ideas?

**[54:30 – 54:37]** Again, let me concentrate on the important ideas and the technical ideas.

**[54:37 – 54:41]** I will just pass through very quickly.

**[54:41 – 54:48]** And I want to discuss with you at least one conceptually very interesting idea.

**[54:48 – 54:56]** One idea that, again, maybe illuminates what's happening in all of these latent spaces and stuff.

**[54:56 – 55:09]** But also an important technical idea was that you don't have to generate a whole picture at once.

**[55:09 – 55:16]** And the implementation of this idea was the following.

**[55:16 – 55:19]** You can have what is called a conditional again.

**[55:19 – 55:28]** Like when you give a condition and you expect the output to change depending on this condition.

**[55:28 – 55:38]** And one, like especially relatively simple version of conditional generation is called super resolution.

**[55:38 – 55:42]** It's still generation because you're inventing new stuff.

**[55:42 – 55:50]** But super resolution is like this problem where you have a low resolution image and you want to make it into a high resolution image.

**[55:50 – 55:56]** So you're like replacing every pixel with four pixels or something like that.

**[55:56 – 56:03]** And this is a generative problem because, again, the information is not there, you have to invent it.

**[56:03 – 56:10]** But it's a much easier problem than just making new images from scratch, right?

**[56:10 – 56:16]** Because the image is basically here, you just need to get some details right.

**[56:16 – 56:28]** And so the idea for general generation was, well, why don't we start small and then just do like a sequence of super resolutions?

**[56:28 – 56:31]** This was called ProGAN, Progressive GrowingGAN.

**[56:31 – 56:37]** And this is the GAN that gave us this guy in 2017.

**[56:37 – 56:46]** There was a website called ThisPersonDoesNotExist, which was kind of famous back then, but I don't expect you to remember.

**[56:46 – 56:53]** And so how does it work? Very simple.

**[56:53 – 56:58]** You have a data set of human faces, you want to generate human faces.

**[56:58 – 57:08]** So your first GAN, pretty simple generator, pretty simple discriminator, and it learns to generate 4x4 human faces.

**[57:08 – 57:15]** Human faces with 4x4 pixels. Trust me, you can do it. Even from scratch, it's not a hard problem.

**[57:15 – 57:27]** 16 pixels are okay. And then you use these generated 16 pixels as the condition to do super resolution and to do an 8x8 image.

**[57:27 – 57:33]** And then 16x16, and 32x32, and so on, and so on, and then you train it for quite a while.

**[57:33 – 57:42]** And in two weeks of training, back then, that was one of the first famous results from NVIDIA.

**[57:42 – 57:50]** Back then, NVIDIA was only starting in the AI world, but they already, of course, had a lot of compute.

**[57:50 – 58:05]** So after two weeks of training like this, you get a 1-megapixel image, and that's pretty good.

**[58:05 – 58:14]** So the architecture is very simple, et cetera, et cetera, and later you can click on the links.

**[58:14 – 58:21]** I don't want to waste time on this, but there are some nice long videos of exactly these walks through the latent space,

**[58:21 – 58:28]** and they look pretty cool. Even in 2018, they look pretty cool.

**[58:28 – 58:38]** But this is not the interesting part. This is still an idea that is useful and is still applied,

**[58:38 – 58:46]** but the interesting part is what did they use for the loss function?

**[58:46 – 58:56]** Well, they actually, by that time, there were two main loss functions in GANs for the generator

**[58:56 – 59:02]** and for the discriminator too. One of them was the least squares GAN.

**[59:02 – 59:10]** I don't want to spend time on the least squares GAN because it's solving the same kind of saturation problem

**[59:10 – 59:14]** and it's solving it in a relatively straightforward way.

**[59:14 – 59:23]** So it just says, well, instead of having a sigmoid, let's just have a squared deviation.

**[59:23 – 59:33]** So instead of saying, oh, I want my d of x to be as large as possible, then it goes through the sigmoid and becomes close to one.

**[59:33 – 59:41]** I just say, okay, I want my d of x to be close to a constant, like a constant one or something.

**[59:41 – 59:45]** And which means that overshooting this constant is also bad.

**[59:45 – 59:51]** So nothing goes to infinity. Everything is supposed to cluster around this target constants.

**[59:51 – 59:56]** And usually in classification, it's a very bad idea.

**[59:56 – 1:00:01]** If you were doing like a detailed class with the first part on linear models,

**[1:00:01 – 1:00:05]** I would explain to you why it's a bad idea to use least squares for classification.

**[1:00:05 – 1:00:09]** But here it works because it solves the situation problem.

**[1:00:09 – 1:00:17]** But, and I will skip this, yeah, I will skip the other ideas.

**[1:00:17 – 1:00:19]** We don't have time for them.

**[1:00:19 – 1:00:28]** But the interesting idea here, let's make it 0.3, and this will be our, I guess, the main content,

**[1:00:28 – 1:00:38]** is called Wasserstein Gens, or W again, sometimes you see the abbreviation.

**[1:00:38 – 1:00:43]** Wasserstein is a famous mathematician, whatever.

**[1:00:43 – 1:00:48]** But I want to explain the, and I will not explain all the math, it's too difficult for us.

**[1:00:48 – 1:00:53]** But I want to explain the motivation because I think it's really cool and really inviting.

**[1:00:53 – 1:01:00]** So what is Wasserstein again? What problem is it solving?

**[1:01:00 – 1:01:05]** Well, what is the goal of our generative models?

**[1:01:05 – 1:01:16]** We want p g of x, our distribution at the output of the generator, to be close to p dot of x.

**[1:01:16 – 1:01:23]** To the distribution of the real true photos.

**[1:01:23 – 1:01:26]** What does it mean that one distribution is close to the other?

**[1:01:26 – 1:01:35]** Well, in machine learning, usually it means that we are minimizing what is called the Kuhlbach-Leibler divergence.

**[1:01:35 – 1:01:40]** I think I already mentioned it today, but let me remind you.

**[1:01:40 – 1:01:42]** I hope you've heard of this term before.

**[1:01:42 – 1:01:56]** So kL from p to q is something like the integral of p of x times log p of x divided by q of x dx.

**[1:01:56 – 1:02:04]** And when p and q are the same, this log becomes zero.

**[1:02:04 – 1:02:08]** The fraction becomes one and this log becomes zero.

**[1:02:08 – 1:02:20]** And the Kulbeck library divergence goes to zero as, let's say, q goes to p or p goes to q or whatever.

**[1:02:20 – 1:02:27]** And usually in machine learning, when you want to make one distribution similar to the other,

**[1:02:27 – 1:02:33]** you are minimizing something like this. And it's a long story.

**[1:02:33 – 1:02:40]** There is an important difference between minimizing Kul from p to q and Kul from q to p,

**[1:02:40 – 1:02:44]** because as you see, it's not symmetric, different properties, whatever.

**[1:02:44 – 1:02:52]** It's not the point now. The point now is actually very interesting.

**[1:02:52 – 1:03:01]** So usually we are doing this in relatively small spaces, right?

**[1:03:01 – 1:03:10]** But here in generative AI, in image generation models, for example,

**[1:03:10 – 1:03:19]** we are doing our x is this very high dimensional vector of pixel values, right?

**[1:03:19 – 1:03:24]** So it lives in a very big space.

**[1:03:24 – 1:03:31]** And the actual distributions, both pData and pG,

**[1:03:31 – 1:03:47]** are actually concentrated in low dimensional subsets, subspaces,

**[1:03:47 – 1:03:50]** manifolds in this high dimensional space.

**[1:03:50 – 1:03:55]** So I will try to draw like a two dimensional picture because that's all I can do.

**[1:03:55 – 1:04:02]** But if you are looking at two dimensions, then it's like here is like we are living on the plane.

**[1:04:02 – 1:04:06]** So the plane is like the space of images.

**[1:04:06 – 1:04:13]** And P data is actually concentrated along just a single line,

**[1:04:13 – 1:04:18]** along a one dimensional subspace of the plane.

**[1:04:18 – 1:04:22]** So this is P data. This is our goal, let's say.

**[1:04:22 – 1:04:29]** And our model, something like this, our PG or P model or whatever,

**[1:04:29 – 1:04:36]** well, it's concentrated along some other straight line.

**[1:04:36 – 1:04:43]** So this looks very natural because the generator changes random noise,

**[1:04:43 – 1:04:47]** which is lower dimensional, into an image.

**[1:04:47 – 1:04:51]** So by definition, it has a low dimensional thing here.

**[1:04:51 – 1:04:58]** And P data, I mean, also kind of obvious that the realistic CAD photos

**[1:04:58 – 1:05:00]** do not take up the whole image space.

**[1:05:00 – 1:05:03]** So it's also in a low dimensional manifold.

**[1:05:03 – 1:05:07]** And our goal is kind of to, you know, match these two distributions.

**[1:05:07 – 1:05:12]** We want to make the purple distribution similar to the green distribution.

**[1:05:12 – 1:05:15]** Here is the problem.

**[1:05:15 – 1:05:18]** If they are both in low dimensional manifolds,

**[1:05:18 – 1:05:21]** it means they don't really overlap.

**[1:05:21 – 1:05:30]** It means that if P data of x is non-zero,

**[1:05:30 – 1:05:33]** then probably Pg of x is zero.

**[1:05:33 – 1:05:35]** And vice versa.

**[1:05:35 – 1:05:39]** If Pg of x is non-zero,

**[1:05:39 – 1:05:42]** then probably Pdata of x is zero.

**[1:05:42 – 1:05:48]** With probability one, basically.

**[1:05:48 – 1:05:50]** Because, again, their supports are different.

**[1:05:50 – 1:05:52]** We cannot just hope to, you know, in the very beginning,

**[1:05:52 – 1:05:54]** to just get the right manifold.

**[1:05:54 – 1:05:56]** That's not going to happen.

**[1:05:56 – 1:05:58]** We are going to get a different manifold.

**[1:05:58 – 1:06:00]** We are going to get a different straight line on the plane.

**[1:06:00 – 1:06:06]** And our goal is supposed to be to move the straight line

**[1:06:06 – 1:06:10]** to the correct straight line, to the straight line of Pdata.

**[1:06:10 – 1:06:18]** But we can't, because if something like this happens,

**[1:06:18 – 1:06:21]** the Kulbach library divergences become meaningless.

**[1:06:21 – 1:06:23]** They become infinite, basically.

**[1:06:23 – 1:06:27]** So I integrate over this space,

**[1:06:27 – 1:06:35]** and whenever P of x is present, Q of x is zero.

**[1:06:35 – 1:06:42]** So I am integrating over something here.

**[1:06:42 – 1:06:45]** I'm taking the expectation, and I'm taking the expectation

**[1:06:45 – 1:06:48]** of something which is basically always infinite.

**[1:06:48 – 1:06:50]** Not a good idea.

**[1:06:50 – 1:06:52]** Or the other way around.

**[1:06:52 – 1:06:57]** If Q is non-zero, then P is zero.

**[1:06:57 – 1:06:59]** And also doesn't make so.

**[1:06:59 – 1:07:02]** If I write down kL from Q to P, nothing changes.

**[1:07:02 – 1:07:05]** It's still infinite.

**[1:07:05 – 1:07:09]** And this means that if I keep using something

**[1:07:09 – 1:07:12]** like the Kulbeck library divergence,

**[1:07:12 – 1:07:14]** I will not be able to train anything.

**[1:07:14 – 1:07:18]** Because if I tweak my generator a little bit,

**[1:07:18 – 1:07:23]** and I move this straight line a little bit, let's say,

**[1:07:23 – 1:07:26]** then it will still not be matching the green line.

**[1:07:26 – 1:07:28]** It will still be different,

**[1:07:28 – 1:07:32]** and the Kulbeck divergence will still remain infinite.

**[1:07:32 – 1:07:34]** And I will not be able to distinguish

**[1:07:34 – 1:07:37]** between the correct direction and the wrong direction.

**[1:07:37 – 1:07:39]** So I need to understand in what direction

**[1:07:39 – 1:07:42]** to move the straight line, and I can't.

**[1:07:42 – 1:07:47]** This kind of losses don't say anything about this.

**[1:07:47 – 1:07:52]** Well, here is a question.

**[1:07:52 – 1:07:56]** I hope you understood what the problem here is.

**[1:07:56 – 1:07:59]** But it sounds like it kind of invalidates

**[1:07:59 – 1:08:01]** the entire field of machine learning.

**[1:08:01 – 1:08:06]** Because we are always, in a way, trying to do this.

**[1:08:06 – 1:08:09]** We are always trying to match distributions,

**[1:08:09 – 1:08:12]** and pretty often they are going to be

**[1:08:12 – 1:08:17]** in separate subspaces.

**[1:08:17 – 1:08:23]** So why doesn't the same kind of stuff happen,

**[1:08:23 – 1:08:25]** I don't know, in linear regression, for example?

**[1:08:25 – 1:08:42]** So in linear regression we have data points,

**[1:08:42 – 1:08:47]** and we have this correct straight line,

**[1:08:47 – 1:08:51]** and we have our current incorrect straight line.

**[1:08:51 – 1:08:53]** And they also don't overlap.

**[1:08:53 – 1:08:57]** They intersect at a single point, which doesn't help us.

**[1:08:57 – 1:08:59]** It still measures zero.

**[1:08:59 – 1:09:02]** So why doesn't the same effect happen in linear regression?

**[1:09:02 – 1:09:06]** Well, it doesn't happen because we add noise, right?

**[1:09:06 – 1:09:13]** So our presumed straight line still has some reasonable,

**[1:09:13 – 1:09:20]** some non-zero likelihood because we add noise.

**[1:09:20 – 1:09:23]** We cannot do anything with pData.

**[1:09:23 – 1:09:31]** Oh, sorry, sorry.

**[1:09:31 – 1:09:34]** I think, yeah, I apologize.

**[1:09:34 – 1:09:37]** Recording in progress.

**[1:09:37 – 1:09:39]** Yeah, hello, hello.

**[1:09:39 – 1:09:42]** Sorry, I think I lost connection.

**[1:09:42 – 1:09:46]** Hope it hasn't been for long.

**[1:09:46 – 1:09:53]** One, two, three.

**[1:09:53 – 1:09:57]** Yeah, I hope I'm back.

**[1:09:57 – 1:09:59]** Right.

**[1:09:59 – 1:10:11]** So this kind of thing does not happen in standard machine learning,

**[1:10:11 – 1:10:14]** this kind of problem, because we are adding noise,

**[1:10:14 – 1:10:16]** because we cannot do anything with pData.

**[1:10:16 – 1:10:22]** The data is fixed, but we are smoothing out our pG.

**[1:10:22 – 1:10:25]** We are smoothing out pG.

**[1:10:25 – 1:10:29]** We are adding something like Gaussian noise to it.

**[1:10:29 – 1:10:34]** And it means that now pG of x is always greater than zero.

**[1:10:34 – 1:10:36]** It can be exponentially small, but that's okay.

**[1:10:36 – 1:10:39]** But it's always greater than zero.

**[1:10:39 – 1:10:42]** It's never going to get us something...

**[1:10:42 – 1:10:49]** Okay, everybody left. Strange.

**[1:10:49 – 1:10:53]** I guess there are internet problems on the other side too.

**[1:10:53 – 1:19:45]** Let me maybe take a small break.

**[1:19:45 – 1:19:47]** Did something happen on your side?

**[1:19:47 – 1:20:06]** Hello, hello?

**[1:20:06 – 1:20:30]** Well, I guess I don't have a choice.

**[1:20:30 – 1:20:33]** I mean, my recording will be good.

**[1:20:33 – 1:20:38]** Anyway, so let me continue.

**[1:20:38 – 1:20:43]** I'm not sure if you hear me,

**[1:20:43 – 1:20:47]** because I didn't hear anything from you.

**[1:20:47 – 1:20:53]** But Zoom looks to be working.

**[1:20:53 – 1:20:58]** And the microphone icon seems to be filling up.

**[1:20:58 – 1:21:05]** So, anyway, where were we?

**[1:21:05 – 1:21:07]** Where were we?

**[1:21:07 – 1:21:11]** We were here at the idea of the Wasserstein GANs.

**[1:21:11 – 1:21:13]** I think a very beautiful idea,

**[1:21:13 – 1:21:16]** one of the most important and influential in GANs

**[1:21:16 – 1:21:19]** and in adversarial training.

**[1:21:19 – 1:21:25]** So, as I explained to you before we got interrupted,

**[1:21:25 – 1:21:30]** we can't really match two distributions

**[1:21:30 – 1:21:32]** that are disjoint,

**[1:21:32 – 1:21:34]** that have non-intersection support,

**[1:21:34 – 1:21:37]** because there is no metric that will...

**[1:21:37 – 1:21:39]** Our standard metrics,

**[1:21:39 – 1:21:42]** the Kulbeck library divergence and their variations,

**[1:21:42 – 1:21:44]** will not...

**[1:21:44 – 1:21:51]** No, I'm out.

**[1:21:51 – 1:21:53]** I'm sorry, guys.

**[1:21:53 – 1:21:55]** Okay, so this time it's on my side.

**[1:21:55 – 1:21:59]** Recording in progress.

**[1:21:59 – 1:22:00]** Yes, sorry.

**[1:22:00 – 1:22:02]** This time it was on my side.

**[1:22:02 – 1:22:06]** I don't know why I keep losing connection,

**[1:22:06 – 1:22:12]** because I'm pretty sure the internet works fine.

**[1:22:12 – 1:22:17]** When I dropped out the last time, I checked it.

**[1:22:17 – 1:22:19]** Yeah, I can Google stuff.

**[1:22:19 – 1:22:22]** Works.

**[1:22:22 – 1:22:23]** Very strange.

**[1:22:23 – 1:22:31]** Alright, anyway.

**[1:22:31 – 1:22:33]** Again, this will not affect the recording,

**[1:22:33 – 1:22:36]** and even in the worst case,

**[1:22:36 – 1:22:40]** you can always watch the last 15 minutes on YouTube.

**[1:22:40 – 1:22:44]** So, let me finish.

**[1:22:44 – 1:22:51]** The Westersteingen, over here,

**[1:22:51 – 1:22:55]** proposes a way around this.

**[1:22:55 – 1:22:59]** So, we cannot match two distributions with disjoint supports,

**[1:22:59 – 1:23:01]** or with almost disjoint supports.

**[1:23:01 – 1:23:03]** We cannot...

**[1:23:03 – 1:23:06]** In standard machine learning, in classical machine learning,

**[1:23:06 – 1:23:08]** what you do is you add noise.

**[1:23:08 – 1:23:14]** So, you say, "Okay, my PG is this low-dimensional stuff,

**[1:23:14 – 1:23:18]** plus Gaussian noise that extends to the whole space."

**[1:23:18 – 1:23:20]** And now everything works.

**[1:23:20 – 1:23:22]** The KL divergence does what it's supposed to do,

**[1:23:22 – 1:23:24]** and you can just maximize the likelihood.

**[1:23:24 – 1:23:29]** But it doesn't really work for generative models,

**[1:23:29 – 1:23:32]** because after that you cannot really remove noise,

**[1:23:32 – 1:23:34]** or at least in implicit generative models,

**[1:23:34 – 1:23:36]** you cannot really remove noise.

**[1:23:36 – 1:23:43]** So, in linear regression, we have our straight line.

**[1:23:43 – 1:23:49]** We are assuming Gaussian noise around this straight line, right?

**[1:23:49 – 1:23:51]** And then we learn the straight line.

**[1:23:51 – 1:23:53]** We have this green line over here.

**[1:23:53 – 1:23:58]** But when I do predictions, when I get a new X,

**[1:23:58 – 1:24:02]** and I say, "Okay, so now what is the Y for this X?"

**[1:24:02 – 1:24:08]** I am not adding artificial noise, right?

**[1:24:08 – 1:24:11]** I am just saying, "Okay, so my prediction,

**[1:24:11 – 1:24:15]** my Y hat is on this green straight line."

**[1:24:15 – 1:24:19]** I am not saying, "Oh, wait, I had this assumption

**[1:24:19 – 1:24:21]** that there is a Gaussian noise around here,

**[1:24:21 – 1:24:24]** so let me take the straight line,

**[1:24:24 – 1:24:27]** let me take what my model gives me,

**[1:24:27 – 1:24:31]** and then add noise, and then this will be my Y hat over here."

**[1:24:31 – 1:24:33]** This does not happen.

**[1:24:33 – 1:24:35]** I just go to the expectation.

**[1:24:35 – 1:24:39]** I go to the most probable hypothesis if I need the point estimate.

**[1:24:39 – 1:24:42]** If I need predictive distribution, it's another story.

**[1:24:42 – 1:24:47]** But for the point estimate, it's like this.

**[1:24:47 – 1:24:51]** Okay, so it looks like it's my internet anyway.

**[1:24:51 – 1:24:59]** Recording in progress.

**[1:24:59 – 1:25:23]** Yeah, sorry.

**[1:25:23 – 1:25:26]** Sorry again, now it's on my side, definitely.

**[1:25:26 – 1:25:30]** Sorry, now it's on my side, definitely.

**[1:25:30 – 1:25:35]** But again, what can we do?

**[1:25:35 – 1:25:36]** Right.

**[1:25:36 – 1:25:39]** So, anyway, Wasserstein Gantz.

**[1:25:39 – 1:25:44]** Yeah, again, my apologies for the technical problems today.

**[1:25:44 – 1:25:52]** So, if I had an explicit density model, like an LLM or something,

**[1:25:52 – 1:25:58]** then I can add noise, like in the LLM, for example,

**[1:25:58 – 1:26:02]** I produce a whole distribution of tokens for the next token.

**[1:26:02 – 1:26:03]** Right? I do.

**[1:26:03 – 1:26:06]** But I choose only one token.

**[1:26:06 – 1:26:09]** Actually, not necessarily the most probable one.

**[1:26:09 – 1:26:13]** It may be a sampling process, but I do choose only one token,

**[1:26:13 – 1:26:15]** and I just drop the noise.

**[1:26:15 – 1:26:22]** But if I have again, if I have this implicit density model,

**[1:26:22 – 1:26:25]** then I cannot drop the noise, because my output

**[1:26:25 – 1:26:29]** already includes the noise.

**[1:26:29 – 1:26:34]** My distribution that I have trained includes this noise,

**[1:26:34 – 1:26:36]** and that makes the images bad.

**[1:26:36 – 1:26:40]** It basically means, okay, so you have created your image,

**[1:26:40 – 1:26:42]** now add some Gaussian noise to your image,

**[1:26:42 – 1:26:45]** which makes it all blurry and unrealistic,

**[1:26:45 – 1:26:48]** and this is the output that you have to do.

**[1:26:48 – 1:26:52]** So I don't want to add noise to generative models,

**[1:26:52 – 1:26:56]** to implicit density generative models.

**[1:26:56 – 1:27:00]** But even though I don't want to add noise

**[1:27:00 – 1:27:03]** to implicit density generative models,

**[1:27:03 – 1:27:05]** I also cannot...

**[1:27:05 – 1:27:07]** Recording in progress.

**[1:27:07 – 1:27:09]** Yeah, sorry, sorry, yeah.

**[1:27:09 – 1:27:12]** Today is not my day, unfortunately,

**[1:27:12 – 1:27:14]** and not the day of my internet.

**[1:27:14 – 1:27:16]** But I don't...

**[1:27:16 – 1:27:21]** I can't really add this...

**[1:27:24 – 1:27:29]** I can't really avoid adding this noise,

**[1:27:29 – 1:27:31]** because I don't have a good loss function.

**[1:27:31 – 1:27:33]** So the idea of Wasserstein GAN

**[1:27:33 – 1:27:36]** is to create a loss function

**[1:27:36 – 1:27:38]** that will work without adding noise.

**[1:27:38 – 1:27:41]** And this loss function is based

**[1:27:41 – 1:27:45]** on what is called the Earth Mover Distance

**[1:27:45 – 1:27:48]** or Wasserstein Distance.

**[1:27:48 – 1:27:50]** Earth Mover is, of course, easier to understand

**[1:27:50 – 1:27:53]** because it immediately tells you what it's doing.

**[1:27:53 – 1:27:57]** So the Earth Mover Distance goes like this.

**[1:27:57 – 1:28:00]** I have a distribution over here.

**[1:28:00 – 1:28:02]** What is the distribution?

**[1:28:02 – 1:28:03]** What is the distribution?

**[1:28:03 – 1:28:07]** It's like a pile of Earth, amount of Earth,

**[1:28:07 – 1:28:17]** that has integral 1, that has total volume 1.

**[1:28:17 – 1:28:20]** And then I have another distribution over here.

**[1:28:20 – 1:28:27]** It's also like amount of Earth that has total volume 1.

**[1:28:27 – 1:28:31]** So in principle, I can take a shovel,

**[1:28:31 – 1:28:33]** I can take this distribution,

**[1:28:33 – 1:28:37]** and I can just move it over there with a shovel.

**[1:28:37 – 1:28:43]** And as I am doing this, I will be doing some work.

**[1:28:43 – 1:28:47]** Work in the straightforward sense of high school physics,

**[1:28:47 – 1:28:51]** of mass times distance.

**[1:28:51 – 1:28:56]** And if I take the optimal way

**[1:28:56 – 1:28:59]** to move one mount of Earth to the other,

**[1:28:59 – 1:29:04]** if I take the optimal transport between these two mounts,

**[1:29:04 – 1:29:07]** these two masses, these two volumes,

**[1:29:07 – 1:29:10]** and they are equal volumes, so I can do that,

**[1:29:10 – 1:29:14]** but then this will be the Earth-mover distance.

**[1:29:14 – 1:29:20]** So then there will be lots and lots of very complicated math

**[1:29:20 – 1:29:23]** that I will definitely not go into,

**[1:29:23 – 1:29:25]** but the idea is this:

**[1:29:25 – 1:29:31]** I want to match the two distributions

**[1:29:31 – 1:29:35]** while spending as little effort as possible,

**[1:29:35 – 1:29:37]** spending as little work as possible,

**[1:29:37 – 1:29:43]** and as I do that,

**[1:29:43 – 1:29:46]** I want them to minimize this minimal effort.

**[1:29:46 – 1:29:48]** So it sounds very, very complicated.

**[1:29:48 – 1:29:51]** It sounds like it would be completely infeasible to train

**[1:29:51 – 1:29:54]** because it's like a minimization problem

**[1:29:54 – 1:29:56]** inside the minimization problem,

**[1:29:56 – 1:29:59]** and the internal one is very difficult.

**[1:29:59 – 1:30:02]** But there is math that lets us go around this.

**[1:30:02 – 1:30:06]** I will not explain it in full detail,

**[1:30:06 – 1:30:10]** but basically, if you can do it,

**[1:30:10 – 1:30:13]** then this loss function

**[1:30:13 – 1:30:15]** becomes exactly what we need,

**[1:30:15 – 1:30:16]** becomes exactly what we want,

**[1:30:16 – 1:30:18]** because now it doesn't matter

**[1:30:18 – 1:30:23]** that these two distributions have disjoint support.

**[1:30:23 – 1:30:26]** If I move this red line over here,

**[1:30:26 – 1:30:30]** well, they still don't intersect,

**[1:30:30 – 1:30:32]** but now there is less distance to go

**[1:30:32 – 1:30:36]** from the red distribution to the green distribution,

**[1:30:36 – 1:30:40]** which means exactly that I need less work.

**[1:30:40 – 1:30:44]** So the EarthMover distance doesn't have this problem.

**[1:30:44 – 1:30:47]** It doesn't need to add noise or do anything artificial

**[1:30:47 – 1:30:51]** in order to bring distributions closer together.

**[1:30:51 – 1:30:58]** And Wasserstein GAN is still one of the most popular loss functions

**[1:30:58 – 1:31:06]** for GANs and for all sorts of adversarial training applications.

**[1:31:06 – 1:31:08]** And probably in practice,

**[1:31:08 – 1:31:12]** you will also be training GANs with WGAN losses.

**[1:31:12 – 1:31:19]** And yeah, so this is the main mathematical idea that I wanted to mention.

**[1:31:19 – 1:31:23]** Let me maybe skip this part.

**[1:31:23 – 1:31:29]** So the next big step was bigGAN in 2019,

**[1:31:29 – 1:31:34]** which already produced kind of reasonable, kind of good images.

**[1:31:34 – 1:31:38]** It had some very nice interpolations.

**[1:31:38 – 1:31:44]** It had, as you can see, you can go from a bird to a dog,

**[1:31:44 – 1:31:49]** and in between you get some strange artificial hybrid,

**[1:31:49 – 1:31:58]** but the strange artificial hybrid still kind of makes sense.

**[1:31:58 – 1:32:00]** Kind of makes sense, right?

**[1:32:00 – 1:32:04]** And let me also skip the quality metrics.

**[1:32:04 – 1:32:07]** And maybe the last thing that I want to discuss

**[1:32:07 – 1:32:11]** is this idea of the adversarial autoencoder.

**[1:32:11 – 1:32:17]** So today we have discussed generative models in general.

**[1:32:17 – 1:32:20]** We have discussed specifically GANs,

**[1:32:20 – 1:32:22]** what is the main idea behind GANs,

**[1:32:22 – 1:32:24]** the idea of adversarial training.

**[1:32:24 – 1:32:29]** And we have discussed the main loss function for GANs,

**[1:32:29 – 1:32:31]** the Wasserstein GAN idea.

**[1:32:31 – 1:32:34]** It didn't do the math, but I didn't expect to anyway.

**[1:32:34 – 1:32:39]** And now the last idea that I want to discuss,

**[1:32:39 – 1:32:45]** because it really segues into variational autoencoders,

**[1:32:45 – 1:32:50]** and it also really adds this to our understanding

**[1:32:50 – 1:32:53]** of how generative models operate,

**[1:32:53 – 1:32:57]** it's the idea of an adversarial autoencoder.

**[1:32:57 – 1:33:02]** So let me motivate it, let me explain it,

**[1:33:02 – 1:33:08]** and then we will stop here.

**[1:33:08 – 1:33:22]** So I started with this main problem of generative modeling.

**[1:33:22 – 1:33:25]** The main problem is how do you define the loss function?

**[1:33:25 – 1:33:30]** For example, here you go from the latent space to the pixel space,

**[1:33:30 – 1:33:32]** but how do you define the loss function

**[1:33:32 – 1:33:34]** of whether it's a good cat picture?

**[1:33:34 – 1:33:38]** Well, there is actually, I didn't mention it then

**[1:33:38 – 1:33:40]** in the beginning of the lecture,

**[1:33:40 – 1:33:45]** but there is one answer that we already know

**[1:33:45 – 1:33:47]** and that kind of looks reasonable.

**[1:33:47 – 1:33:49]** And the answer is let's train an autoencoder.

**[1:33:49 – 1:33:57]** So where do we get, like, again, we don't have a data set

**[1:33:57 – 1:34:00]** of these that match X's?

**[1:34:00 – 1:34:02]** If we did, it would be just supervised learning.

**[1:34:02 – 1:34:07]** But what if we close the loop?

**[1:34:07 – 1:34:10]** What if we close the loop with an autoencoder?

**[1:34:10 – 1:34:13]** So now we are here.

**[1:34:13 – 1:34:18]** We start here in pixel space with an X.

**[1:34:18 – 1:34:20]** Let's put it this way.

**[1:34:20 – 1:34:25]** This is some very complicated distribution, huge space.

**[1:34:25 – 1:34:28]** Then we go through, not the generator,

**[1:34:28 – 1:34:33]** we go through the encoder and we get a Z,

**[1:34:33 – 1:34:39]** which lives hopefully on a much more understandable distribution

**[1:34:39 – 1:34:42]** in a smaller space, the latent code.

**[1:34:42 – 1:34:51]** And then we have the decoder that unravels Z back,

**[1:34:51 – 1:34:55]** decompresses Z back into the pixel space, right?

**[1:34:55 – 1:34:59]** And if you have an autoencoder,

**[1:34:59 – 1:35:02]** then you automatically get some very simple,

**[1:35:02 – 1:35:04]** very straightforward loss functions, right?

**[1:35:04 – 1:35:06]** Because you can just take this X,

**[1:35:06 – 1:35:08]** you can take this X hat,

**[1:35:08 – 1:35:13]** and you can do something like an L2 loss on X hat index.

**[1:35:13 – 1:35:15]** It's not a problem.

**[1:35:15 – 1:35:19]** You just want X hat to be similar to X.

**[1:35:19 – 1:35:24]** So you want Z to be a good compressed representation of the original X.

**[1:35:24 – 1:35:28]** And when you look at an autoencoder,

**[1:35:28 – 1:35:34]** it looks like you have a generative model right here.

**[1:35:34 – 1:35:39]** Because look, how does the autoencoder work?

**[1:35:39 – 1:35:44]** You start from here, you map to the latent space,

**[1:35:44 – 1:35:50]** and then you decompress back and you go to the pixel space.

**[1:35:50 – 1:35:54]** So why can't I just cut off the encoder

**[1:35:54 – 1:35:59]** and say that this part is a great generative model?

**[1:35:59 – 1:36:06]** Because the decoder is already used to converting latent codes

**[1:36:06 – 1:36:10]** into, let's say, good cat pictures.

**[1:36:10 – 1:36:19]** Well, the problem is that even in the latent space,

**[1:36:19 – 1:36:23]** even over here where the dimension is relatively small,

**[1:36:23 – 1:36:28]** it's still a pretty complicated distribution,

**[1:36:28 – 1:36:31]** a pretty complicated manifold of latent codes too.

**[1:36:31 – 1:36:37]** So in reality, axes live in a distribution with some,

**[1:36:37 – 1:36:40]** I don't know, dimension a million or something.

**[1:36:40 – 1:36:46]** And in reality, these cannot live in three-dimensional space.

**[1:36:46 – 1:36:49]** There will be not enough information to capture a whole image.

**[1:36:49 – 1:36:54]** So they live in a space of, I don't know, 500 dimensions.

**[1:36:54 – 1:36:58]** And in the distribution of dimension 500,

**[1:36:58 – 1:37:02]** the space of dimension 500 is still a pretty complicated space.

**[1:37:02 – 1:37:04]** And it's still pretty big,

**[1:37:04 – 1:37:08]** and there can still be very complicated manifolds inside.

**[1:37:08 – 1:37:10]** So the problem with this approach,

**[1:37:10 – 1:37:14]** why can't I just take the decoder of an autoencoder and say,

**[1:37:14 – 1:37:16]** here's your generative model?

**[1:37:16 – 1:37:20]** The problem is I cannot sample from this red thing.

**[1:37:20 – 1:37:24]** And if I start sampling from a standard Gaussian,

**[1:37:24 – 1:37:27]** then with overwhelming probability,

**[1:37:27 – 1:37:34]** I will not get on the red thing, on the right manifold.

**[1:37:34 – 1:37:38]** And if I don't get on the right manifold here,

**[1:37:38 – 1:37:42]** then of course I will also not get on the right manifold here.

**[1:37:42 – 1:37:45]** And it will be a nonsensical image, not a nice catfart.

**[1:37:45 – 1:37:59]** So in order to fix this problem,

**[1:37:59 – 1:38:02]** in order to still use autoencoders as generative models,

**[1:38:02 – 1:38:06]** we need to do something about this latent space.

**[1:38:06 – 1:38:11]** We need to, well, what do we need to do?

**[1:38:11 – 1:38:14]** There can be different approaches.

**[1:38:14 – 1:38:19]** A variational autoencoder would say, let's regularize.

**[1:38:19 – 1:38:25]** And hopefully we will discuss YS tomorrow at least a little bit.

**[1:38:25 – 1:38:27]** They are really, really important.

**[1:38:27 – 1:38:32]** But you can also do an adversarial thing.

**[1:38:32 – 1:38:35]** You can say, oh, okay.

**[1:38:35 – 1:38:39]** So I have this distribution of latent codes over here.

**[1:38:39 – 1:38:51]** Why don't I say that the Z's that come from real images are this kind of fake Z's?

**[1:38:51 – 1:39:02]** And the true Z's, the real Z's, come from some standard simple distribution like the standard Gaussian.

**[1:39:02 – 1:39:13]** And let's put a discriminator over here to distinguish not between images, but between the latent codes.

**[1:39:13 – 1:39:18]** So it's the same adversarial idea.

**[1:39:18 – 1:39:20]** Let me show you a better picture over here.

**[1:39:20 – 1:39:22]** It's the same adversarial idea.

**[1:39:22 – 1:39:42]** But now I am trying to make the distribution of latent codes over here match some kind of standard distribution over here.

**[1:39:42 – 1:39:54]** And the assumption is if the discriminator cannot distinguish between what actually gets produced from real images and a standard Gaussian,

**[1:39:54 – 1:39:59]** well, then maybe I can use the standard Gaussian to sample new Zs and to get new real images.

**[1:39:59 – 1:40:09]** At some point, it's a pretty old idea. It's almost as old as GANs themselves.

**[1:40:09 – 1:40:13]** Still gets around sometimes.

**[1:40:13 – 1:40:20]** I think variational autoencoders are a cleaner conceptual solution to the same problem, so they are used, of course, much more.

**[1:40:20 – 1:40:30]** But it's still an interesting variation. I think in the practical session you also have AAEs.

**[1:40:30 – 1:40:38]** So it can be even better than a variational autoencoder, although it depends on how you cook it.

**[1:40:38 – 1:40:44]** And then, of course, you can do all sorts of modifications, extensions, etc.

**[1:40:44 – 1:40:50]** You can make the distributions conditional, for example, if you want to draw a specific digit from MNIST,

**[1:40:50 – 1:40:53]** then, of course, you need to specify the digit.

**[1:40:53 – 1:41:00]** So you can add a label here and then now you can have different distributions for different labels or whatever.

**[1:41:00 – 1:41:05]** So lots of interesting stuff.

**[1:41:05 – 1:41:14]** And I think I have to stop here, especially since we were having some problems with the internet, unfortunately.

**[1:41:14 – 1:41:22]** But GANs were very cool in 2020 or something.

**[1:41:22 – 1:41:25]** They were definitely state-of-the-art image generation.

**[1:41:25 – 1:41:33]** They remain state-of-the-art in some specific domains like, for example, super-resolution.

**[1:41:33 – 1:41:37]** Super-resolution is an interesting topic in itself.

**[1:41:37 – 1:41:40]** I could do a whole lecture on it, but definitely not today.

**[1:41:40 – 1:41:45]** They remain important in style transfer.

**[1:41:45 – 1:41:58]** Fortunately, we don't have time to discuss style transfer, but the family of style GAN models is still alive, I think.

**[1:41:58 – 1:42:08]** But overall, for straightforward image generation, or especially for prompted image generation, for text-to-image problems,

**[1:42:08 – 1:42:12]** they have been completely replaced by diffusion models.

**[1:42:12 – 1:42:20]** And tomorrow, in our last lecture, we will discuss the diffusion models.

**[1:42:20 – 1:42:29]** And again, definitely I will have to skip all of the difficult math in the diffusion models.

**[1:42:29 – 1:42:40]** But at least I hope to be able to explain the basic idea, the intuition, and how this all fits together

**[1:42:40 – 1:42:45]** and how it brings us to where we are today, more or less.

**[1:42:45 – 1:42:48]** So thank you and see you tomorrow.

## Full text

Okay. Hello, everyone. And welcome back. We have only two lectures left, which is, of course, very little time to cover a lot of the generative AI that we actually planned to go on to. But still, I think that even in two lectures, we can cover a couple of very interesting and very important and still very relevant ideas. Today, we talk about generative adversarial networks, GANs. It's a beautiful idea underlying the stuff, which is completely non-mathematical. It's just very cool and very logical, but it leads to very beautiful mathematics a little bit down the road. But before we go there, let me begin today with the structure of generative AI as a whole. Our first part today will be about generative models in general and what kinds of generative models exist in deep learning. So when we say generative AI, when we say generative models, it's not a very well-defined term because you can say that logistic regression generates the probability distribution over classes. So the divide is that in generative AI, you are producing something big. You are producing an object usually of high dimension and of complicated structure like an image or like text. So generative models are models that write, that draw, that produce music, videos, something like that. And when we talk about generative models, so let me draw a taxonomy for you, this will be our first subject for discussion. So of course I will be talking only about deep generative models, so models that are based on neural networks. And there are several important classes of these models. And today we will live in one of these classes, tomorrow we will live in another. But I still want to draw a general taxonomy so that you can actually better understand what's going on. The first divide, the first serious fork in deep generative models comes in the distinction between explicit density models. I'll explain in a sec. And implicit density models. So what does explicit and implicit density mean? When you have a generative model, it takes as input something like random noise or some condition or whatever. Then there is this black box which we are trying to define. And then at the output, there is like a picture of a cat or something. There is X that lives in a very high dimensional space. And this X has a very complicated distribution. If you try to imagine, as I think I made this argument once in our class, try to imagine the manifold of realistic photos in this 3 million dimensional space of 1 megapixel images. Obviously we cannot imagine anything like that, but also obviously it's very, very, very complicated. So P of X, the distribution of axes that we are trying to approximate, that we are trying to model, is very, very, very complicated. And the difference between explicit and implicit density models is that in explicit density models you get an explicit model for the density. So there is this P of X is actually equal to something in the model, and you can actually find out what it is equal to, so to speak. Naturally, we will not be able to get the actual distribution of CAD photos, but we can approximate, and we can try to approximate. And then, inside explicit density models, we have the next divide between tractable density models. And let me pause here and explain. So tractable density basically means that you can have a formula for P of X. It makes such strong assumptions that you actually can just write down that P of X is equal to something. And usually when we say tractable density, we mean an autoregressive model. So an autoregressive model is a model that makes use of this kind of obvious identity. That if you have this big, big X, then you can do something like... And you can decompose it into something like P of X1, P of X2 given X1, P of X3 given X1 and X2 and so on until P of Xn given X1, Xn minus 1. Right? So this is always true. And of course, since it's always true, it's also completely useless because you're not making anything easier for you because this is still a very big function of a lot of variables. But then you can simplify, then you can make assumptions. So you can make, I don't know, you can make a Markov chain out of this. You can say that every next X depends only on the previous ones. Or you can have an RNN here, which says that, OK, I model a sequence, but every next output depends only on the current. Input and the hidden state, which is also a part of the state, part of the model variables here. And then you get another simplified decomposition and so on. So, of course, it would be a lot of the models that exist happen to be in the autoregressive class. For example, all LLMs are here, almost all LLMs are here because LLMs predict the next token. So they model text, the sequence of tokens, as a sequence of, exactly as this, as p of x, k, given the previous context. And then, of course, the question is how to model this conditional distribution. And that's where transformers come in, that's where all the models come in. But the basic assumption is this: we produce and generate text one by one. And there have been models for pictures here, too. There were things like PixelCNN that produced images pixel by pixel, and it was a good model in terms of the output. But, of course, producing images pixel by pixel is just way too inefficient, because you need to generate a million pixels, and running your model a million times is, of course, infeasible, even if it's not very complicated. So pixel-wise autoregressive models are not really used, and we won't talk about them, but they also exist. It's a natural idea. And for text, basically everything is autoregressive. And then what else is there that we also will not have time to talk about? Interactable density, you can have something like a flow-based model. So one way to decompose a complicated distribution is to separate the variables inside x, like the autoregressive style. And another way is to say, well, okay, what if p of x is a big composition of simple transformations? Something like fk composed with fk minus 1, composed, composed, composed, f2, f1 of z. So we are still modeling something like this, and we are doing it explicitly. Each f is a simple thing like adding Gaussian noise or linear transformation or something like that. But when you compose a lot of simple transformations, like always in neural networks, this is not a neural network, but like always in neural networks, you get this capability of modeling something much, much more complicated, right? So we won't talk about flow-based models in all time, unfortunately. And apart from tractable density, you can have approximate density models. So here, in a way, you could repeat the same structure, but now instead of modeling p of x, instead of making assumptions about the distribution itself, we explicitly say that we approximate p of x with some simpler q, and now this q is a product of something easier. And here, the main example that is very, very relevant, it's a pity that probably we won't have time to talk, but maybe I'll talk about them tomorrow, maybe. The main example are variational autoencoders. This is one of the most important ideas in the whole deep learning, how to use variational approximations to get good loss functions for generative models. Variational autoencoders are used all the time. For example, tomorrow we will talk about diffusion models, and diffusion models usually operate in the latent space of a variational autoencoder, but I'm getting a bit ahead of myself. Now, of course, explicit density part is big and varied and rich. There are lots and lots and lots of different approaches here. The implicit density side is not that rich. There are much fewer examples here, and actually I won't even make any other examples because they are kind of esoteric. The main example of implicit density generative models are GANs that we discussed today. And what does it mean not to have a density for X? Like how can you have a model that produces axes that gives you cat photos, but does not have anywhere a formula for P of X or even an approximation to P of X? Well, you just have to take this picture literally, right? So an implicit density model will start with random noise, and then it will actually produce just a sample X, which is supposed to be taken from the distribution P of X. It will produce a sample cat picture that is supposed to be a good cat picture. And if you look at it this way, if you look at your neural network, at your model, as this sampling procedure, as a sampler, well, not a sampler, as a transformation of probability distributions from a simple one, from random noise like just standard Gaussian, to this very complicated one in this huge dimensional space, etc., then it all kind of starts to make sense, right? So if you just have a black box that samples cat photos for you, you cannot really extract a formula from this black box. I mean, you could maybe make a trillion examples and then learn one of the explicit density models, but that doesn't count. The black box itself doesn't have the formula anywhere. So this is what GANs do. And now the first part is over. I've talked about this general structure and maybe we'll return to it tomorrow. And now, what are GANs? What is their main idea? So we talk about generative adversarial networks, GANs. And in the general... Sorry. The generative adversarial network is based on this very... ...interesting... It's one possible solution to a very deep problem in generative models. And we will discuss other... If we get to YS, we will discuss other solutions to this problem. But here is the problem, basically. The main problem of generative AI in general... I mean, there are many ways to solve it. It's not like it's an open problem, but the main deep problem... ...that you need to solve when you create a generative model... ...is what is your loss function? How do you score the results? So let me start drawing this picture for you, right? So I have this random noise scene... ...which is basically just taken from some standard distribution or whatever. And then this random noise scene gets to the generator network... ...gets to the model that maps random noise... ...to something that is supposed to be a cat picture, right? Let's call it X hat because it will be like a predicted cat... ...not yet a real cat. So let's think of it as a learning problem... ...as a machine learning problem. If you look at this as a machine learning problem... ...well, you do have a data set of axes, right? So what does your data look like? Your data is a lot of cats, a lot of cat photos. But you don't have paired data for this, right? You cannot just say that this X hat should be similar to some X in the training set... ...because you have no idea which one, right? There isn't and there will never be a dataset that pairs random noise... ...with images that are supposed to be produced from this random noise. This doesn't make sense. The whole point of learning a generator is to learn this mapping... ...and to get a good and relatively simple parameterization in the noise space... ...so that next week we would be able to just take random noise and still get reasonable cat pictures. So the data is unlabeled. It's unsupervised learning. So where will the loss function come from? Which X should Z be similar to? Well, you can say, okay, I don't have any specific X in mind. I just want the result, this X head, to be a good cat picture. And this sounds reasonable, and this is exactly what we'll do. But what does it mean to be a good cat picture? This is the deep question that we need to answer. Because there is really no mathematical function that you can run and say if this photo is a cat picture, is a good cat picture. If this set of pixels is a good cat picture. This is something that you have to learn yourself too. And this is like half of the problem, if not most of the problem. So generative adversarial networks say the following. They say, well, okay, you recognize that you need to learn your loss function. That you need to work for it. You do not have a fixed formula for evaluating how catchy this image looks. So let's do it. Let's work for it. Let's have a whole separate network, both a discriminator, whose only goal, whose only job is to say whether the input... So as input it takes photos, and as output it does just binary classification. Is it fake or is it real? Let's say that real is one and fake is zero. So the discriminator gets a picture, and if it's a picture produced by the generator, then it should say that it's fake. And if it's a real picture, so we can take our data and we can sample a real cat photo from it. This will be real x, x real, and this is x fake. So if a real picture is fed into the discriminator, the output should be one. In this way, the generator and the discriminator are at odds with each other. They have opposing interests. The discriminator wants to learn to distinguish between real images and images produced by the generator. And the generator wants to fool the discriminator. So this general idea is called adversarial training. And you may hear that GANs are not what they used to be. And indeed, GANs are not, for the last few years, GANs are not at the forefront of image generation. The images these days are generated by diffusion models, which we will talk about tomorrow. But adversarial training is very much alive. And even in the diffusion models, we will see exactly this idea. And we will see a little bit of a GAN embedded into a diffusion model and making it better. So this is, of course, still a very important idea in machine learning. And it appears in many different fields. Of course, we are only talking about images, but still. So let me maybe show you some nice pictures. I think I have the intrapictures about GANs. This is the main idea, and as you can see, it's very simple. So the generator is like forging a picture, and the discriminator is the detective that needs to decide whether it's real. And ideally, it should look something like this. So this is an example where the generator, which is called reverse deep convolutional neural network here, the generator learns to counterfeit money, learns to produce pictures of real money. And at first, it just produces something. Actually, this is a few steps in, because at first, the generator will just produce random noise. But then it produces some very bad counterfeit. And then the discriminator will say, "Oh, well, I don't know any better. So this seems legit, and I am fooled." Okay, so I provide once on fake images. So then we train the discriminator, and now it learns to distinguish. It understands that this is not real money, not real American dollars. And then we actually, often it's done exactly like this. So we fix the discriminator that has trained for a while. So we train the generator to fool this current version of the discriminator. So we say, oh, okay, now the discriminator doesn't accept our counterfeits. What should we do? Let's train a little bit more and produce a slightly better counterfeit. It will still be bad. Because, again, there is no general loss function that will tell you if the image is good. There's only this specific discriminator that has learned to not be fooled by some attacks. So at this point, it will produce a better counterfeit. And then the discriminator will find some other features to discriminate on. And then the generator will have to learn to fake those features too, and so on. So they're kind of playing this game. And the hope is that everything happens. I will walk you through the formulas in a minute. But the hope is that everything happens like on this idealized image. So here, for example, the generator is represented by these arrows. These arrows, as you can see, in Z, we have the uniform distribution every time. And in X, we have like this Gaussian, the green Gaussian. And the black dots are the data points. And so at first, this Gaussian doesn't look like the black dots. So the blue dashed line is the discriminator. It's just a logistic sigmoid, right? So it's a sigmoid curve that distinguishes between these two Gaussians. And then here is the crucial part. At this point, the discriminator trains, but it's not training to mimic the data because that is impossible. I mean, in this case, it would be possible, but in the high dimensional case of pictures, it would not be possible. So the generator learns to fool the discriminator. So in this case, it's enough to move this Gaussian a little bit over here, and the discriminator is already fooled. It doesn't need to go all the way to the data points. But then, of course, the discriminator will be able to distinguish between these two bell curves and so on. But finally, we will get to this perfect picture where the generator is perfect and the discriminator has no idea what to do and just flips a coin. So, of course, in real life it's not going to work like that, but the idea is exactly this. So what is interesting about the problem setting here? Well, let's write down the loss functions. Let's see mathematically what is happening here. So first, the discriminator, right? So what is the discriminator loss LD? Well, let me write it in this form. So the discriminator is supposed to say zero if it's fake and one if it's real. So let me write it as expectations. Doesn't really matter, but this will be cleaner for what comes next. So if I take a real photo from the dataset, from the training set, then I'm supposed to increase the output. I'm supposed to produce the score that goes to positive infinity. So the probability after the sigma, it will go to one. So I'm supposed to increase, to have a loss function, something like log d of x. Actually, minus log d of x. And then, if x is fake... So x fake is taken... Where is it taken from? It's taken from the distribution of the generator. Sorry, not x pg of z, right? From the distribution of the generator. No, actually, it's pg of x, right? So I'm taking it from this distribution, from the distribution that has come through the generator. Then I'm supposed to output zero, so I'm supposed to do something like this, right? And I want to minimize this loss function with respect to the parameters of the discriminator. So when I fix the generator and I just train the discriminator, this is a very straightforward binary classification problem. What does the generator do? Well, the generator is supposed to produce axes that pass for real for the discriminator. So basically, I mean, it cannot influence this part. There is no generator here. But for this part, the job of the generator is exactly opposite to the discriminator, right? So let me write it now completely. We start with some random noise. And then I want to actually take the discriminator loss on my results on GOC and do the opposite. So if here I was minimizing minus this, then here I will be minimizing plus this, right? So basically, you can say that the discriminator and the generator have the exact same loss function. I can just copy it here, it won't matter because it's just a constant for the generator. And what they are actually doing, let's say that I have this loss function that depends on the parameters of the generator and parameters of the discriminator. For this loss function, let's say that the discriminator wants it to be as big as possible. So let's say that this is the loss function, the thing in the brackets. So the discriminator wants to make it bigger and the generator wants to make it smaller. So we have this minimax game. It's actually something that has never happened to us in machine learning before and that will not happen since. We are not just doing optimization here, at least formally. We are doing adversarial optimization in the sense of game theory. And if you have ever had any classes in game theory or anything, you know that as soon as these quantifiers, this optimization goals like min, max, max, min, etc. as soon as they start to stack up, as soon as you have a minimax instead of just a min or just a max, the complexity is of the charts, right? So it's extremely hard, it's extremely difficult to actually optimize for in-game theory. And on the surface of this, it looks like this should be a hopelessly difficult problem. I mean, for us, it's hard enough to do just minimization, to just minimize the loss function. And here we are asking to do a minimax, to basically find the equilibrium in the game. This sounds completely impossible. Well, in reality, of course, it's not impossible. And there are some properties of these loss functions that make it simpler. And I will not go into the mathematical details. But basically, let me just tell you the result here. Basically, if you fix the generator, then you know exactly what the optimal discriminator is, because it's just the optimal Bayesian classifier. Remember bias formula, blah, blah, blah. So here, if I know the data distribution pdata, and I know the generator distribution pg, the answer is just the bias rule. The probability that x was real is the density of x under pdata normalized to the sum of pdata and pg. This is exactly the bias rule. And then, so this is straightforward, but the interesting part is that now you can take this formula and you can plug it into the generator loss, and what you get is basically a very simple result. You get that the generator is perfect, attains the global minimum of this criterion if pg equals to pdata. So this verifies that we are actually doing the right thing, that the generator is actually minimizing, is actually making pg closer to the true data distribution to pdata. In fact, it's doing it in a pretty interesting, non-standard way. So for the optimal discriminator, the generator actually is minimizing these Jensen-Shenen diversions, not the Kuhlbeck-Libler divergence between two distributions, which we usually minimize in machine learning, but like this averaged symmetrical version of KL, which is called the Jensen-Shenen averages. And I won't go into details about these results. I don't want to discuss them further because, unfortunately, they are completely irrelevant. So everything that we can say, like this theoretically, about this kind of minimax problems and the game theory stuff here and how we can substitute the perfect discriminator into the generator loss function, etc. All of this makes the assumption that we actually have this common loss function for the generator and the discriminator. And that's just not true in practice. So in practice, it turns out that this kind of generator loss, they just take the binary cross-entropy from the discriminator and flip it, that this is a very bad idea for the generator. And why? Because it saturates. And it's exactly the same problem that we discussed in Deplering several times. Again, I don't have time to go into full detail here, but basically this thing, this cross-entropy, is the output of a sigmoid. And if it saturates, it saturates, right? So if you are classifying it like the discriminator does, that's actually a good thing, at least not a bad thing. You saturate when you give the right answer, and that's fine. So if you are already giving the right answer and you are confident in this decision, in the right decision, then you don't need to change anything, right? But now, when you look at the generator, if the discriminator is very certain that it's right, and the discriminator has saturated and it's doing a very good job, it means that the generator is failing. It means that the generator does not produce believable results. The discriminator is easy. It's easy to distinguish from the discriminator. So this is the situation where we are supposed to train the generator. We are supposed to actually update its weights, but we can't because in the backpropagation, the loss is only over here. So the gradients for the generator have to go through the gradients of the discriminator. And as I just said, the gradients for the discriminator become near zero because the discriminator is saturated and already working very well. So if I reuse the same loss function, it's really a bad idea because it means that when I have trained the discriminator and in practice there is this alternating training usually. So we train the discriminator a little, then the generator, then the discriminator and so on. So when I train the discriminator a little and it becomes good at separating stuff, this is exactly when its gradients become near zero and the generator is very hard to train. So the same effect that we had in a slightly different form. As you can see, I am teaching you general ideas that appear over and over, the same as in your serial training today. So what do we do? Well, we change the loss function. And let me skip the early attempts at changing this loss function. Let me just show you the path that we have, the original GANs, how they work. And that was, what, 12 years ago? That's 2014. And in 2014, as you can see on these pictures, the green ones are real training samples. They are nearest neighbors from the training set to the adjacent picture. So you can actually verify that the model did not just memorize a few elements of the training set, but it's actually generating stuff. So as you can see, it worked wonderfully for Amnist. It worked much worse for these small black and white human faces. And it basically was very bad for anything else, for anything more diverse. So in 2014, GANs appeared, but they were no match to other generative models at that point. So what happened next? Next, there was DCGAN. DCGAN is basically the same kind of GAN, but with a new, better architecture, convolutional architecture for the generator and the discriminator. Again, no point in going into the details, but I want to make one remark here. So DCGAN already started to produce some reasonable pictures on some data sets. Still very small, still obviously bad in some ways. It was 10 years ago. Image generation was very bad back at the time. So this was actually state of the art 10 years ago. And yeah, just a side remark. If you look through old papers on GANs and on YS and on various generative models, you will see a lot of bedrooms. I don't know who started it, but at some point there is this data set called Large Scale Scene Understanding. So SU stands for Scene Understanding. And it basically is like several subsets of photos of different environments. And one of the environments was a bedroom. And when somebody chose this set of pictures for their tests, and of course after that everybody had to follow suit and had to compare their bedrooms with previous bedrooms. So you will see a lot of bedroom pictures. They are relatively small, like I think 64 by 64 pixels or maybe 128 by 128, something like that. But they are in color and they already kind of are supposed to look like real photos. And this is DC again after one epoch, still very bad. But after five epochs it starts to be more or less okay. So obviously nothing exciting by today's standards, but back then it was okay. And what I wanted to mention here is this idea. So this is important. Again, how do you illustrate, how do you understand yourself that you've got a good generative model? The discriminator will not tell you that. Because the discriminator will tell you, oh, I can't distinguish. It doesn't mean that the pictures are good. It doesn't mean that the latent space is good. It just means that the discriminator can't distinguish. Maybe you didn't train it well enough, maybe it's not large enough, it's not powerful enough. Who knows, right? So how do you, well maybe not measure, the metrics are a different story, but how do you at least see for yourself if the generator actually makes any sense? And the usual illustration goes like this, and I want to explain it because it's really a good illustration to what we are doing intuitively, geometrically in the latent spaces and so on. What is the generator actually doing? It's taking this random noise, this vector from the latent space Z, so this will be the latent space, and it's mapping Z to a point X, which is in pixel space, so to say, right? And in pixel space, in this huge million-dimensional space of images, the actual images that we are looking for form this extremely complicated and completely un-understandable manifold, right? So they have this very, very complicated structure. But in the latent space, our goal is to actually flatten this structure completely. Because what is our goal, really? Our goal is to be able to generate new images, right? So our goal is to be able to do the following: to take a random Z over here, Z from a standard Gaussian, right? From some very simple distribution. Doesn't matter if it's the Gaussian specifically, but Z from some very simple distribution that we can sample from directly. And take this random noise, put it through our generator, map it over here, and actually hope that the result will fall in this extremely complicated, very difficult, completely unimaginable manifold of real pictures, real photos, right? So this is the job of the generator. Here is the generator. So how do we test this? How can we understand if we actually did a good job in this? Well, here is one test that was very popular and that you can immediately see for yourself. It's very visual. And the test is, let's do a linear walk in the latent space. So in the latent space, if I take, for example, two different Zs, one here, one here, so they will produce two different pictures. They will produce two different pictures, right? The green one and the orange one. Then in the latent space, if I'm supposed to get them from the standard Gaussian, it means that if I just walk from one of the Zs to the other, let's say this is Z2 and that one was Z1. So if I walk from one random sample to another random sample over here, this I can do just along a straight line and along the straight line, all of the intermediate Zs should give me reasonable images. OK, this is the main test. So if G, if the generator was stupid and it wasn't doing much and they just memorized a few data points and then the Zs would get mapped to these data points, it would still look good on the training set. But if I go from one Z to another, then here it would do something nonsensical. For example, it might walk along a straight line in the pixel space. And if you go along the straight line in the pixel space, you don't get realistic photos, right? You get one photo and then the other kind of appearing through it and it's like you're making one of them more transparent and the other shows up underneath. So it's definitely not a walk through realistic photographs. What you are supposed to have in the ideal case is a walk in the pixel space that also follows this manifold and goes from one X to the other. So on every intermediate step through this straight line, you are supposed to get a realistic photo somewhere on the manifold. And if you get that and if you see it consistently true, then it does mean that you can sample, or at least you can hope to sample random Zs and get realistic images. So if you look in these papers and generative models, you will often see this kind of walks through the feature space or through the latent space. The left and the right part are actual images or something from the training set or some images that are guaranteed to be good. And now you walk through the latent space and you see... So in the latent space, you walk along the straight line and you see what happens in the pixel space. And as you can see here, there may be some strange stuff happening in the middle, but more or less, they are all kind of realistic, at least on the same level of realistic as the images on the side. So this was, I think, the first GAN which was already the state of the art of image generation. It even had some kind of vector arithmetic. It didn't work out later, so let me skip. But also, that was the time when GANs, they were already state of the art. And what I just showed to you was indeed state of the art image generation 10 years ago. You can, again, marvel at the progress, at the rate of progress. But they were still kind of bad. You wouldn't use them for generating production images like today. I obviously generate, get pictures like this one, and I like the results. But back then, these are not real bedroom photos. And back then, there were some common problems with generation, specifically with GAN-based generation, that you may remember. I mean, they were all across the internet and stuff like that were like common failure modes of GANs. And maybe you will actually see some failure modes like this in your practical sessions. So they definitely had problems with counting. I mean, the recent meme was about six fingers on a hand. Like a couple of years ago, it was still a problem. Today it's not. But back like 10 years ago, it was much worse than six fingers on a hand, right? There would be like three heads of a dog with who knows how many eyes and so on. And that actually makes sense as a failure because when you look at something like this reverse convolutional network, what it's doing is it has this general idea, the general features, and then it specializes and it draws different parts of the image then more or less independently. And basically what this failure mode means is that, well, I am here and I only have a small context around this eye. So I'm not really sure, is it the right eye or the left eye? And I decide, okay, so maybe this is the right eye and I need another one. And then I do the other one and again, I'm not sure, is it the left or the right? And again, I do another one. So I think the mechanism was something like this. And the same goes for problems with perspective. So here I was generating this dog and they got to the head of the dog. And now I don't have enough context to understand what was the angle I was looking from. And now the other half of the dog is from a completely different thing. And actually, this stuff is hard. So these kind of mistakes, they stand out for us because our vision is very good. We know the world. We know how it's supposed to look like. And we learned it in the first years of our lives. But it's actually very, very difficult. And this kind of, for example, generating stuff in proper perspective as if it was a three-dimensional world is really difficult. And for example, among these images, if we were offline, I would say raise your hands. But just how many of you actually realized that one of these images does not belong here? And usually it takes a few questions for people to actually see that this cat over here is just a real photo. There is nothing bad about this. It's just a cat which is sleeping all curled up like this. Cats do it, right? So it's difficult. And it was difficult. But image generation has made tremendous progress. And this picture, of course, I have been showing it since 2018. But honestly, you can extend it. There are, of course, newer and better models for human faces too. But it would be pointless because in 2018, you already probably cannot see the imperfections. There are imperfections here, but on a slide, I don't think you can see them. But in 2014, I think you can see, right? And you can actually see how much progress GAN-based generation made in just these four or five years. So how did that happen? What were the main ideas? Again, let me concentrate on the important ideas and the technical ideas. I will just pass through very quickly. And I want to discuss with you at least one conceptually very interesting idea. One idea that, again, maybe illuminates what's happening in all of these latent spaces and stuff. But also an important technical idea was that you don't have to generate a whole picture at once. And the implementation of this idea was the following. You can have what is called a conditional again. Like when you give a condition and you expect the output to change depending on this condition. And one, like especially relatively simple version of conditional generation is called super resolution. It's still generation because you're inventing new stuff. But super resolution is like this problem where you have a low resolution image and you want to make it into a high resolution image. So you're like replacing every pixel with four pixels or something like that. And this is a generative problem because, again, the information is not there, you have to invent it. But it's a much easier problem than just making new images from scratch, right? Because the image is basically here, you just need to get some details right. And so the idea for general generation was, well, why don't we start small and then just do like a sequence of super resolutions? This was called ProGAN, Progressive GrowingGAN. And this is the GAN that gave us this guy in 2017. There was a website called ThisPersonDoesNotExist, which was kind of famous back then, but I don't expect you to remember. And so how does it work? Very simple. You have a data set of human faces, you want to generate human faces. So your first GAN, pretty simple generator, pretty simple discriminator, and it learns to generate 4x4 human faces. Human faces with 4x4 pixels. Trust me, you can do it. Even from scratch, it's not a hard problem. 16 pixels are okay. And then you use these generated 16 pixels as the condition to do super resolution and to do an 8x8 image. And then 16x16, and 32x32, and so on, and so on, and then you train it for quite a while. And in two weeks of training, back then, that was one of the first famous results from NVIDIA. Back then, NVIDIA was only starting in the AI world, but they already, of course, had a lot of compute. So after two weeks of training like this, you get a 1-megapixel image, and that's pretty good. So the architecture is very simple, et cetera, et cetera, and later you can click on the links. I don't want to waste time on this, but there are some nice long videos of exactly these walks through the latent space, and they look pretty cool. Even in 2018, they look pretty cool. But this is not the interesting part. This is still an idea that is useful and is still applied, but the interesting part is what did they use for the loss function? Well, they actually, by that time, there were two main loss functions in GANs for the generator and for the discriminator too. One of them was the least squares GAN. I don't want to spend time on the least squares GAN because it's solving the same kind of saturation problem and it's solving it in a relatively straightforward way. So it just says, well, instead of having a sigmoid, let's just have a squared deviation. So instead of saying, oh, I want my d of x to be as large as possible, then it goes through the sigmoid and becomes close to one. I just say, okay, I want my d of x to be close to a constant, like a constant one or something. And which means that overshooting this constant is also bad. So nothing goes to infinity. Everything is supposed to cluster around this target constants. And usually in classification, it's a very bad idea. If you were doing like a detailed class with the first part on linear models, I would explain to you why it's a bad idea to use least squares for classification. But here it works because it solves the situation problem. But, and I will skip this, yeah, I will skip the other ideas. We don't have time for them. But the interesting idea here, let's make it 0.3, and this will be our, I guess, the main content, is called Wasserstein Gens, or W again, sometimes you see the abbreviation. Wasserstein is a famous mathematician, whatever. But I want to explain the, and I will not explain all the math, it's too difficult for us. But I want to explain the motivation because I think it's really cool and really inviting. So what is Wasserstein again? What problem is it solving? Well, what is the goal of our generative models? We want p g of x, our distribution at the output of the generator, to be close to p dot of x. To the distribution of the real true photos. What does it mean that one distribution is close to the other? Well, in machine learning, usually it means that we are minimizing what is called the Kuhlbach-Leibler divergence. I think I already mentioned it today, but let me remind you. I hope you've heard of this term before. So kL from p to q is something like the integral of p of x times log p of x divided by q of x dx. And when p and q are the same, this log becomes zero. The fraction becomes one and this log becomes zero. And the Kulbeck library divergence goes to zero as, let's say, q goes to p or p goes to q or whatever. And usually in machine learning, when you want to make one distribution similar to the other, you are minimizing something like this. And it's a long story. There is an important difference between minimizing Kul from p to q and Kul from q to p, because as you see, it's not symmetric, different properties, whatever. It's not the point now. The point now is actually very interesting. So usually we are doing this in relatively small spaces, right? But here in generative AI, in image generation models, for example, we are doing our x is this very high dimensional vector of pixel values, right? So it lives in a very big space. And the actual distributions, both pData and pG, are actually concentrated in low dimensional subsets, subspaces, manifolds in this high dimensional space. So I will try to draw like a two dimensional picture because that's all I can do. But if you are looking at two dimensions, then it's like here is like we are living on the plane. So the plane is like the space of images. And P data is actually concentrated along just a single line, along a one dimensional subspace of the plane. So this is P data. This is our goal, let's say. And our model, something like this, our PG or P model or whatever, well, it's concentrated along some other straight line. So this looks very natural because the generator changes random noise, which is lower dimensional, into an image. So by definition, it has a low dimensional thing here. And P data, I mean, also kind of obvious that the realistic CAD photos do not take up the whole image space. So it's also in a low dimensional manifold. And our goal is kind of to, you know, match these two distributions. We want to make the purple distribution similar to the green distribution. Here is the problem. If they are both in low dimensional manifolds, it means they don't really overlap. It means that if P data of x is non-zero, then probably Pg of x is zero. And vice versa. If Pg of x is non-zero, then probably Pdata of x is zero. With probability one, basically. Because, again, their supports are different. We cannot just hope to, you know, in the very beginning, to just get the right manifold. That's not going to happen. We are going to get a different manifold. We are going to get a different straight line on the plane. And our goal is supposed to be to move the straight line to the correct straight line, to the straight line of Pdata. But we can't, because if something like this happens, the Kulbach library divergences become meaningless. They become infinite, basically. So I integrate over this space, and whenever P of x is present, Q of x is zero. So I am integrating over something here. I'm taking the expectation, and I'm taking the expectation of something which is basically always infinite. Not a good idea. Or the other way around. If Q is non-zero, then P is zero. And also doesn't make so. If I write down kL from Q to P, nothing changes. It's still infinite. And this means that if I keep using something like the Kulbeck library divergence, I will not be able to train anything. Because if I tweak my generator a little bit, and I move this straight line a little bit, let's say, then it will still not be matching the green line. It will still be different, and the Kulbeck divergence will still remain infinite. And I will not be able to distinguish between the correct direction and the wrong direction. So I need to understand in what direction to move the straight line, and I can't. This kind of losses don't say anything about this. Well, here is a question. I hope you understood what the problem here is. But it sounds like it kind of invalidates the entire field of machine learning. Because we are always, in a way, trying to do this. We are always trying to match distributions, and pretty often they are going to be in separate subspaces. So why doesn't the same kind of stuff happen, I don't know, in linear regression, for example? So in linear regression we have data points, and we have this correct straight line, and we have our current incorrect straight line. And they also don't overlap. They intersect at a single point, which doesn't help us. It still measures zero. So why doesn't the same effect happen in linear regression? Well, it doesn't happen because we add noise, right? So our presumed straight line still has some reasonable, some non-zero likelihood because we add noise. We cannot do anything with pData. Oh, sorry, sorry. I think, yeah, I apologize. Recording in progress. Yeah, hello, hello. Sorry, I think I lost connection. Hope it hasn't been for long. One, two, three. Yeah, I hope I'm back. Right. So this kind of thing does not happen in standard machine learning, this kind of problem, because we are adding noise, because we cannot do anything with pData. The data is fixed, but we are smoothing out our pG. We are smoothing out pG. We are adding something like Gaussian noise to it. And it means that now pG of x is always greater than zero. It can be exponentially small, but that's okay. But it's always greater than zero. It's never going to get us something... Okay, everybody left. Strange. I guess there are internet problems on the other side too. Let me maybe take a small break. Did something happen on your side? Hello, hello? Well, I guess I don't have a choice. I mean, my recording will be good. Anyway, so let me continue. I'm not sure if you hear me, because I didn't hear anything from you. But Zoom looks to be working. And the microphone icon seems to be filling up. So, anyway, where were we? Where were we? We were here at the idea of the Wasserstein GANs. I think a very beautiful idea, one of the most important and influential in GANs and in adversarial training. So, as I explained to you before we got interrupted, we can't really match two distributions that are disjoint, that have non-intersection support, because there is no metric that will... Our standard metrics, the Kulbeck library divergence and their variations, will not... No, I'm out. I'm sorry, guys. Okay, so this time it's on my side. Recording in progress. Yes, sorry. This time it was on my side. I don't know why I keep losing connection, because I'm pretty sure the internet works fine. When I dropped out the last time, I checked it. Yeah, I can Google stuff. Works. Very strange. Alright, anyway. Again, this will not affect the recording, and even in the worst case, you can always watch the last 15 minutes on YouTube. So, let me finish. The Westersteingen, over here, proposes a way around this. So, we cannot match two distributions with disjoint supports, or with almost disjoint supports. We cannot... In standard machine learning, in classical machine learning, what you do is you add noise. So, you say, "Okay, my PG is this low-dimensional stuff, plus Gaussian noise that extends to the whole space." And now everything works. The KL divergence does what it's supposed to do, and you can just maximize the likelihood. But it doesn't really work for generative models, because after that you cannot really remove noise, or at least in implicit generative models, you cannot really remove noise. So, in linear regression, we have our straight line. We are assuming Gaussian noise around this straight line, right? And then we learn the straight line. We have this green line over here. But when I do predictions, when I get a new X, and I say, "Okay, so now what is the Y for this X?" I am not adding artificial noise, right? I am just saying, "Okay, so my prediction, my Y hat is on this green straight line." I am not saying, "Oh, wait, I had this assumption that there is a Gaussian noise around here, so let me take the straight line, let me take what my model gives me, and then add noise, and then this will be my Y hat over here." This does not happen. I just go to the expectation. I go to the most probable hypothesis if I need the point estimate. If I need predictive distribution, it's another story. But for the point estimate, it's like this. Okay, so it looks like it's my internet anyway. Recording in progress. Yeah, sorry. Sorry again, now it's on my side, definitely. Sorry, now it's on my side, definitely. But again, what can we do? Right. So, anyway, Wasserstein Gantz. Yeah, again, my apologies for the technical problems today. So, if I had an explicit density model, like an LLM or something, then I can add noise, like in the LLM, for example, I produce a whole distribution of tokens for the next token. Right? I do. But I choose only one token. Actually, not necessarily the most probable one. It may be a sampling process, but I do choose only one token, and I just drop the noise. But if I have again, if I have this implicit density model, then I cannot drop the noise, because my output already includes the noise. My distribution that I have trained includes this noise, and that makes the images bad. It basically means, okay, so you have created your image, now add some Gaussian noise to your image, which makes it all blurry and unrealistic, and this is the output that you have to do. So I don't want to add noise to generative models, to implicit density generative models. But even though I don't want to add noise to implicit density generative models, I also cannot... Recording in progress. Yeah, sorry, sorry, yeah. Today is not my day, unfortunately, and not the day of my internet. But I don't... I can't really add this... I can't really avoid adding this noise, because I don't have a good loss function. So the idea of Wasserstein GAN is to create a loss function that will work without adding noise. And this loss function is based on what is called the Earth Mover Distance or Wasserstein Distance. Earth Mover is, of course, easier to understand because it immediately tells you what it's doing. So the Earth Mover Distance goes like this. I have a distribution over here. What is the distribution? What is the distribution? It's like a pile of Earth, amount of Earth, that has integral 1, that has total volume 1. And then I have another distribution over here. It's also like amount of Earth that has total volume 1. So in principle, I can take a shovel, I can take this distribution, and I can just move it over there with a shovel. And as I am doing this, I will be doing some work. Work in the straightforward sense of high school physics, of mass times distance. And if I take the optimal way to move one mount of Earth to the other, if I take the optimal transport between these two mounts, these two masses, these two volumes, and they are equal volumes, so I can do that, but then this will be the Earth-mover distance. So then there will be lots and lots of very complicated math that I will definitely not go into, but the idea is this: I want to match the two distributions while spending as little effort as possible, spending as little work as possible, and as I do that, I want them to minimize this minimal effort. So it sounds very, very complicated. It sounds like it would be completely infeasible to train because it's like a minimization problem inside the minimization problem, and the internal one is very difficult. But there is math that lets us go around this. I will not explain it in full detail, but basically, if you can do it, then this loss function becomes exactly what we need, becomes exactly what we want, because now it doesn't matter that these two distributions have disjoint support. If I move this red line over here, well, they still don't intersect, but now there is less distance to go from the red distribution to the green distribution, which means exactly that I need less work. So the EarthMover distance doesn't have this problem. It doesn't need to add noise or do anything artificial in order to bring distributions closer together. And Wasserstein GAN is still one of the most popular loss functions for GANs and for all sorts of adversarial training applications. And probably in practice, you will also be training GANs with WGAN losses. And yeah, so this is the main mathematical idea that I wanted to mention. Let me maybe skip this part. So the next big step was bigGAN in 2019, which already produced kind of reasonable, kind of good images. It had some very nice interpolations. It had, as you can see, you can go from a bird to a dog, and in between you get some strange artificial hybrid, but the strange artificial hybrid still kind of makes sense. Kind of makes sense, right? And let me also skip the quality metrics. And maybe the last thing that I want to discuss is this idea of the adversarial autoencoder. So today we have discussed generative models in general. We have discussed specifically GANs, what is the main idea behind GANs, the idea of adversarial training. And we have discussed the main loss function for GANs, the Wasserstein GAN idea. It didn't do the math, but I didn't expect to anyway. And now the last idea that I want to discuss, because it really segues into variational autoencoders, and it also really adds this to our understanding of how generative models operate, it's the idea of an adversarial autoencoder. So let me motivate it, let me explain it, and then we will stop here. So I started with this main problem of generative modeling. The main problem is how do you define the loss function? For example, here you go from the latent space to the pixel space, but how do you define the loss function of whether it's a good cat picture? Well, there is actually, I didn't mention it then in the beginning of the lecture, but there is one answer that we already know and that kind of looks reasonable. And the answer is let's train an autoencoder. So where do we get, like, again, we don't have a data set of these that match X's? If we did, it would be just supervised learning. But what if we close the loop? What if we close the loop with an autoencoder? So now we are here. We start here in pixel space with an X. Let's put it this way. This is some very complicated distribution, huge space. Then we go through, not the generator, we go through the encoder and we get a Z, which lives hopefully on a much more understandable distribution in a smaller space, the latent code. And then we have the decoder that unravels Z back, decompresses Z back into the pixel space, right? And if you have an autoencoder, then you automatically get some very simple, very straightforward loss functions, right? Because you can just take this X, you can take this X hat, and you can do something like an L2 loss on X hat index. It's not a problem. You just want X hat to be similar to X. So you want Z to be a good compressed representation of the original X. And when you look at an autoencoder, it looks like you have a generative model right here. Because look, how does the autoencoder work? You start from here, you map to the latent space, and then you decompress back and you go to the pixel space. So why can't I just cut off the encoder and say that this part is a great generative model? Because the decoder is already used to converting latent codes into, let's say, good cat pictures. Well, the problem is that even in the latent space, even over here where the dimension is relatively small, it's still a pretty complicated distribution, a pretty complicated manifold of latent codes too. So in reality, axes live in a distribution with some, I don't know, dimension a million or something. And in reality, these cannot live in three-dimensional space. There will be not enough information to capture a whole image. So they live in a space of, I don't know, 500 dimensions. And in the distribution of dimension 500, the space of dimension 500 is still a pretty complicated space. And it's still pretty big, and there can still be very complicated manifolds inside. So the problem with this approach, why can't I just take the decoder of an autoencoder and say, here's your generative model? The problem is I cannot sample from this red thing. And if I start sampling from a standard Gaussian, then with overwhelming probability, I will not get on the red thing, on the right manifold. And if I don't get on the right manifold here, then of course I will also not get on the right manifold here. And it will be a nonsensical image, not a nice catfart. So in order to fix this problem, in order to still use autoencoders as generative models, we need to do something about this latent space. We need to, well, what do we need to do? There can be different approaches. A variational autoencoder would say, let's regularize. And hopefully we will discuss YS tomorrow at least a little bit. They are really, really important. But you can also do an adversarial thing. You can say, oh, okay. So I have this distribution of latent codes over here. Why don't I say that the Z's that come from real images are this kind of fake Z's? And the true Z's, the real Z's, come from some standard simple distribution like the standard Gaussian. And let's put a discriminator over here to distinguish not between images, but between the latent codes. So it's the same adversarial idea. Let me show you a better picture over here. It's the same adversarial idea. But now I am trying to make the distribution of latent codes over here match some kind of standard distribution over here. And the assumption is if the discriminator cannot distinguish between what actually gets produced from real images and a standard Gaussian, well, then maybe I can use the standard Gaussian to sample new Zs and to get new real images. At some point, it's a pretty old idea. It's almost as old as GANs themselves. Still gets around sometimes. I think variational autoencoders are a cleaner conceptual solution to the same problem, so they are used, of course, much more. But it's still an interesting variation. I think in the practical session you also have AAEs. So it can be even better than a variational autoencoder, although it depends on how you cook it. And then, of course, you can do all sorts of modifications, extensions, etc. You can make the distributions conditional, for example, if you want to draw a specific digit from MNIST, then, of course, you need to specify the digit. So you can add a label here and then now you can have different distributions for different labels or whatever. So lots of interesting stuff. And I think I have to stop here, especially since we were having some problems with the internet, unfortunately. But GANs were very cool in 2020 or something. They were definitely state-of-the-art image generation. They remain state-of-the-art in some specific domains like, for example, super-resolution. Super-resolution is an interesting topic in itself. I could do a whole lecture on it, but definitely not today. They remain important in style transfer. Fortunately, we don't have time to discuss style transfer, but the family of style GAN models is still alive, I think. But overall, for straightforward image generation, or especially for prompted image generation, for text-to-image problems, they have been completely replaced by diffusion models. And tomorrow, in our last lecture, we will discuss the diffusion models. And again, definitely I will have to skip all of the difficult math in the diffusion models. But at least I hope to be able to explain the basic idea, the intuition, and how this all fits together and how it brings us to where we are today, more or less. So thank you and see you tomorrow.
