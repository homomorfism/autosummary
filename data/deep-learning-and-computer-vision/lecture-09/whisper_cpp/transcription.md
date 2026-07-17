# Transcript — whisper_cpp

- **Provider:** whisper_cpp
- **Language:** en
- **Audio duration:** 1:35:51
- **Segments:** 949
- **model:** ggml-large-v3-turbo.bin
- **vad:** True
- **beam_size:** 5
- **entropy_thold:** 2.8
- **latency_sec:** 812.78

## Segments

**[00:11 – 00:31]** Okay. Hello everyone. And welcome to the last lecture of our class. It has been, I think it actually has been quite a long journey through our lectures. I think we've covered quite a lot of ground.

**[00:33 – 00:52]** We actually didn't quite get to the computer vision itself. We only had one lecture on object detection. I skipped segmentation entirely, but generative models seem like important ideas too.

**[00:52 – 01:15]** And usually I choose one or the other. In this case, it's generative models. And they also are a great teaching tool, in my opinion, because they show some ideas in relatively simple form that go through the whole of machine learning.

**[01:15 – 01:38]** And today in our last lecture, actually, I'm going to tell you one of these wonderful basic ideas. Maybe you have heard about it in some previous classes, but to be honest, I sincerely doubt that somehow in harborspace, people usually don't teach that stuff unless I do.

**[01:38 – 01:58]** So today we mostly talk about variational autoencoders, and therefore we talk about variational approximations, which, again, in the variational autoencoder, the variational approximation appears in its very simplest form and already in a very useful form.

**[01:58 – 02:11]** So I think it's perfect for teaching it. And then whatever time we have left, I hope we will have some time left, I will walk you through diffusion models.

**[02:11 – 02:23]** There, there is a lot of very complicated math, which we definitely won't have time for, but again, the basic ideas are kind of easy to show.

**[02:23 – 02:37]** So, let's start with the motivation and let's start with the basic idea of the variational autoencoder.

**[02:37 – 02:55]** I started talking about the motivation of YS yesterday when I explained to you this basic problem of why can't we have a generative model from an autoencoder.

**[02:55 – 03:04]** I hope you remember. So, we have this X which is a picture or something, some complicated thing.

**[03:04 – 03:16]** Then we pass it through the encoder. We get, in the regular autoencoder, we get like a latent code Z.

**[03:16 – 03:26]** And Z is relatively small compared to X. And then there is the decoding part, the decoder,

**[03:26 – 03:35]** that is supposed to recover, reconstruct the original X.

**[03:35 – 03:41]** Right? This is the very basic structure of an autoencoder.

**[03:41 – 03:45]** And you can train it very straightforwardly.

**[03:45 – 03:49]** There is no problem in thinking of good loss functions here.

**[03:49 – 03:54]** So you just want your X and X hat to be similar to each other.

**[03:54 – 03:58]** What is usually called the reconstruction loss.

**[03:58 – 04:03]** And the reconstruction loss basically can be anything.

**[04:03 – 04:11]** It can be just the L2 norm.

**[04:11 – 04:14]** It can be something like perception loss.

**[04:14 – 04:16]** I'm not sure if Alex talked to you about that.

**[04:16 – 04:25]** But like the similarity between some local features extracted by a couple of layers

**[04:26 – 04:31]** of a standard feature extractor and so on and so forth.

**[04:31 – 04:38]** So you can think of what you want, how you would like to define what it means to be similar,

**[04:38 – 04:41]** and you just optimize it.

**[04:41 – 04:46]** And the beauty of autoencoders is that you don't need any label training data, right?

**[04:46 – 04:57]** Your dataset can be just a set of axes and you automatically get labeled samples

**[04:57 – 04:59]** because you just need to reconstruct the same axis.

**[04:59 – 05:05]** So the big question is why can't we use the blue part?

**[05:05 – 05:07]** I intentionally made it in a different color.

**[05:07 – 05:10]** Why can't we use the blue part as a generative model?

**[05:11 – 05:13]** And yesterday I told you why, right?

**[05:13 – 05:19]** We can't use it as a generative model because even though in the latent space,

**[05:19 – 05:27]** these live in a much simpler, much more structured, so to speak,

**[05:27 – 05:35]** manifold than they do in the space of x, which is huge and very, very complicated,

**[05:36 – 05:41]** they still do not cover the whole space of z.

**[05:41 – 05:48]** The space of z is still pretty complex and we still need to do something

**[05:49 – 05:57]** because if we just take a random point here in the latent space z, of course it will not fall onto

**[05:57 – 06:02]** this manifold of actual latent codes for good cat pictures.

**[06:02 – 06:14]** So yesterday I told you one way to try to fix that and that way was to have a discriminator here.

**[06:14 – 06:24]** Right? We discussed adversarial lotto encoders where you would try to distinguish fake z from

**[06:24 – 06:31]** so-to-speak real z's that are sampled from a Gaussian or something or whatever distribution you want.

**[06:32 – 06:40]** And in that way you can apply adversarial learning, you can apply the basic GAN idea to

**[06:42 – 06:48]** try to regularize, to try to fix this latent space, to try to fix this

**[06:51 – 07:00]** manifold of latent codes. And that was called the adversarial autoencoder.

**[07:00 – 07:08]** So today we discussed a different approach to the same problem and this approach to the same problem

**[07:09 – 07:18]** is actually better. I mean at some point there was a competition between adversarial autoencoders

**[07:18 – 07:27]** and variational autoencoders but by now with some recent innovations and so on, variational autoencoders

**[07:27 – 07:36]** were just better and they formed the basis for a lot of what's happening in generative modeling,

**[07:37 – 07:42]** in particular for the diffusion models that we will discuss later.

**[08:08 – 08:47]** What is the variational approach? What is the approach from the variational autoencoder?

**[08:47 – 08:58]** Well, the idea is as follows: you again have the same kind of encoder-decoder construction.

**[09:03 – 09:12]** X-head. You still have the same autoencoder with some reconstruction losses or whatever,

**[09:13 – 09:22]** but now you do the following: you say, well, what is the problem with

**[09:26 – 09:44]** the latent space here? What is the core of the problem of why these are so hard to actually

**[09:45 – 09:55]** get? Why we cannot get to Zs with random sampling or something? And one answer to that is because every X

**[09:55 – 10:03]** from the training set corresponds to just one point Z. And that kind of leads to almost automatic

**[10:03 – 10:09]** overfitting in the space of latent codes. So we are training on a data set. Yes, it may be a huge

**[10:09 – 10:17]** data set, but every point corresponds to just one Z. And if you shift your Z a little bit, well,

**[10:17 – 10:31]** you've fallen off the manifold of good latent codes and nothing works anymore, right? And when you're

**[10:31 – 10:38]** sampling, of course, you don't know which directions are good, which directions are bad. And of course,

**[10:38 – 10:45]** you're very likely to follow the manifold. So the approach of the variational autoencoder is to say

**[10:45 – 10:55]** the following. Now, instead of having just one latent code, let's instead make the encoder output

**[10:55 – 11:06]** a whole distribution of these, like p of z given x. So now when I have like a cat picture over here,

**[11:06 – 11:13]** it maps in the latent space, not to a single point, but it maps to something like a Gaussian.

**[11:13 – 11:23]** It maps to a whole distribution of latent codes. And then if I have a different cat

**[11:23 – 11:38]** picture, it maps to a different distribution of latent codes. And then I would like to sample

**[11:38 – 11:45]** from this distribution. So I would like to pick a point out of, say, the orange distribution,

**[11:45 – 11:55]** and still reconstruct the same orange cat. And if I pick a point from this distribution,

**[11:55 – 12:05]** I would like to still reconstruct the same green cat. So the encoder will give me the distribution.

**[12:05 – 12:12]** Actually, in the form of parameters, I will show you in a sec. And then I sample from it, and

**[12:14 – 12:23]** I'm supposed to get, again, X hat, which is supposed to be similar to X, again with the reconstruction loss.

**[12:23 – 12:34]** So in this way, I will be able to try to cover the whole latent space, or at least some reasonable

**[12:34 – 12:42]** portion of the latent space with these distributions. So in fact, it's going to work like that, and

**[12:42 – 12:49]** usually it works like this. These distributions are Gaussians, they are just normal distributions,

**[12:49 – 12:59]** and the encoder gives you their parameters, like mu of X and sigma of X. And sigma is a vector

**[13:00 – 13:04]** usually just for simplicity, so it should be a covariance matrix. Of course, it's all

**[13:06 – 13:14]** multidimensional distributions, but basically I'm talking about a diagonal matrix,

**[13:15 – 13:27]** diagonal covariance matrix here. And then from these two parameters, I construct the Gaussian,

**[13:30 – 13:43]** and I sample Z from it, and then it goes to the decoder, and I get X hat. So I fix the Gaussian shape,

**[13:44 – 13:55]** but I'm basically saying that, well, the parameters of this Gaussian, the variances and the means

**[13:55 – 14:05]** are determined by the encoder, and I will train it to be as best as I can. Well, the natural question

**[14:05 – 14:14]** and the obvious problem here is that why would the encoder actually want to produce any kind of

**[14:14 – 14:23]** reasonable distribution? Because of course solving this problem with a single point is much, much easier

**[14:23 – 14:29]** for the model, right? So here it's supposed to reconstruct the same cat from a whole neighborhood

**[14:29 – 14:36]** of points in this high dimensional space, not just from a single point. It's strictly more difficult,

**[14:36 – 14:53]** right? It's strictly harder. At the same time, since the encoder controls the variances,

**[14:53 – 15:00]** naturally it can just send the variance to zero, right? It can just say, well, yeah, I know I'm

**[15:00 – 15:05]** supposed to do a Gaussian, but what if I just fake a Gaussian and say that, okay, here is my Gaussian,

**[15:05 – 15:13]** just has very small variance. That's exactly what's going to happen in practice, unless you regularize

**[15:13 – 15:24]** somehow. So another important component here is that we need some kind of regularization

**[15:25 – 15:33]** on the distribution parameters. And in this case also, we need to take this mu and sigma,

**[15:33 – 15:43]** and we need to do regularization on them. We need to make sure that sigma doesn't just uncontrollably

**[15:43 – 15:50]** goes to zero. And on the other hand, that mu doesn't uncontrollably go to infinity, because another

**[15:50 – 15:56]** way to make this problem very, very easy would be to say, "Okay, so I can't make the variance too small.

**[15:56 – 16:03]** All right, let me fix the variance to be one, but let's just drive these points away from each other

**[16:03 – 16:12]** so that nothing ever overlaps and everything is completely different." And for me as the encoder,

**[16:12 – 16:18]** it just means rescaling of the space and I am still basically in the same situation of having

**[16:18 – 16:24]** individual points. So that also will definitely happen in practice unless you regularize.

**[16:24 – 16:30]** So we need to have some kind of regularization for this and actually the regularization is very simple.

**[16:32 – 16:44]** It says that our distribution should be similar to just the standard normal distribution, right, with

**[16:44 – 16:55]** min zero and unit covariance matrix. So this is the idea of the Variational Autoencoder, but there are

**[16:55 – 17:10]** some problems and unclear things here. So one problem, one thing that always kind of appears

**[17:10 – 17:18]** in deep learning and in machine learning in general is that you often kind of know what you want, right?

**[17:18 – 17:32]** So let me actually draw the reconstruction loss. You know, in principle, what you want.

**[17:32 – 17:41]** Like I want to have a reconstruction loss that says that x index hat are similar, or I want to have

**[17:41 – 17:48]** a regularizer that says that mu is kind of like not very far from zero and sigma is kind of like

**[17:48 – 17:56]** not very close to zero. But how do I formalize this? So this is question number one. How do I

**[17:56 – 18:05]** formalize this? What would different reconstruction losses mean? What would it mean for these two

**[18:05 – 18:12]** distributions to be close to each other? Or better to say, I know quite a lot of ways to say that they

**[18:12 – 18:17]** are close to each other. Which of them should I choose? Which reconstruction loss should I choose?

**[18:17 – 18:26]** Right? There's always a question like this. But in this case, there's also a special question, a question

**[18:26 – 18:36]** special for this architecture. And this is the question of how do I do that? How do I insert

**[18:36 – 18:47]** a sampling procedure into a deep neural network? And it sounds very simple, right? The encoder is a

**[18:47 – 18:52]** neural network. It has two vectors as outputs. One vector is mu. The other is sigma. Then you just

**[18:52 – 18:59]** sample. And in the forward propagation, in the forward pass, it is very simple. You just sample

**[18:59 – 19:04]** from the Gaussian. You know how to do that. But what do we do with the backward pass?

**[19:05 – 19:13]** How does gradient go through a sampling procedure? Well, obviously it doesn't. And that is a big

**[19:13 – 19:20]** problem. And we need to somehow solve this problem, right? So let's tackle these problems. And

**[19:21 – 19:33]** talking about them actually gives us the ideas that I advertised in the very beginning, these very

**[19:33 – 19:46]** basic ideas that go through the whole machine learning. So let's do like via formally, so to speak.

**[19:48 – 19:57]** And the formal approach here, and for now I will be concentrating on the first problem,

**[19:57 – 20:05]** like where do the loss functions come from. But to actually talk about this and to actually see where

**[20:05 – 20:14]** those functions come from, I need to start a little bit further back. So let's look at what kind of

**[20:14 – 20:23]** variables, not parameters, but variables appear in our model. Our model has basically two variables,

**[20:23 – 20:31]** x, which is the thing, the image, whatever you are encoding, and z, the latent code. So

**[20:31 – 20:41]** two variables in the model. And what basically every machine learning model does, like we discussed

**[20:41 – 20:51]** in the very beginning of our class, it takes this joint distribution p of x, z and decomposes it

**[20:51 – 20:59]** somehow, and then makes some assumptions and so on, right? So here, p of x, z doesn't look very

**[20:59 – 21:06]** difficult. There's not too many different ways how you can decompose it. So let's write both of these

**[21:06 – 21:14]** ways, right? You can start with x and say it's p of x times p of z given x. Or you can start with z

**[21:14 – 21:23]** and you can say it's p of z times p of, sorry, x given z, right? These are the two possible

**[21:23 – 21:32]** decompositions unless we go inside x in the end. Right now we don't want it. And if you look at this

**[21:32 – 21:37]** very simple formula, like, you know, this full probability formula, whatever, definition of

**[21:37 – 21:46]** conditional probability, you see all of the components of our neural network. It's actually

**[21:46 – 21:55]** pretty straightforward and beautiful. So what are the components here? Well, what is p of z given x?

**[21:55 – 22:02]** p of z given x is this distribution. It's the encoder distribution. It's what the encoder produces.

**[22:02 – 22:13]** Let me call it the encoder, so to say, right? Where is the decoder distribution? Well, the decoder

**[22:13 – 22:24]** takes z as input and outputs x hat, and it doesn't output the exact x, it outputs an approximation to x.

**[22:24 – 22:35]** So again, like in linear regression, or like in any machine learning model, in actuality, the decoder produces some noise distribution around x.

**[22:36 – 22:55]** So actually, this is the decoder, right? What is P of x? Well, P of x is the global distribution of CAD pictures, right?

**[22:55 – 23:02]** So P of x is that extremely difficult, complicated thing that we have no ability to comprehend.

**[23:03 – 23:16]** And what is P of z? Well, P of z is the prior distribution, right, without any x, the prior distribution on the latent codes.

**[23:16 – 23:33]** So what we would like P of z to be is some simple distribution that we can sample from, because this whole thing is our regeneration process, right?

**[23:33 – 23:39]** How do we produce a new CAD picture? We sample z, and then we run it through the decoder.

**[23:40 – 23:46]** We sample z, and then we plug it into P of x given z, and basically sample x.

**[23:49 – 23:56]** So in order for that to work, we need P of z to be simple, right?

**[23:57 – 24:00]** Well, here is the catch.

**[24:03 – 24:05]** Notice that I haven't done basically anything.

**[24:05 – 24:09]** I wrote the most trivial formula of the whole probability theory.

**[24:10 – 24:15]** But we can already make some conclusions.

**[24:16 – 24:18]** So our first conclusion is this.

**[24:19 – 24:26]** Well, what are these decoder and encoder distributions?

**[24:28 – 24:34]** Well, the decoder and encoder distributions are...

**[24:34 – 24:39]** Well, the decoder distribution is the distribution of noise at the output,

**[24:39 – 24:41]** and it will be captured in the reconstruction loss.

**[24:42 – 24:43]** We'll see it a little bit later.

**[24:43 – 24:54]** And the encoder distribution is, well, something that I'm supposed to sample this Z of X from.

**[24:55 – 24:58]** So basically, it's like the true version of this Gaussian.

**[25:01 – 25:08]** And I would, of course, be very happy to say that,

**[25:08 – 25:13]** well, let's assume that the decoder has Gaussian noise.

**[25:13 – 25:16]** Let's assume that the encoder produces a Gaussian.

**[25:16 – 25:21]** Let's plug it in and let's do the math and we will, I don't know, learn some parameters.

**[25:22 – 25:28]** Unfortunately, even without going any further, we see here that it doesn't work.

**[25:30 – 25:31]** Why doesn't it work?

**[25:31 – 25:34]** Because I need P of Z to be simple, right?

**[25:34 – 25:39]** So actually, P of Z in the classical variational-to-encoder will be just a standard Gaussian.

**[25:40 – 25:42]** And we pick P of Z, right?

**[25:42 – 25:43]** It's our choice.

**[25:44 – 25:47]** So P of Z is simple.

**[25:47 – 25:55]** If the decoder is also simple, and it will be, if the decoder is also a Gaussian, let's say.

**[25:55 – 26:04]** So it's a Gaussian with the mean specified by the decoder and some Gaussian noise around this output.

**[26:05 – 26:14]** So our assumption is that we want to reconstruct the original X, but of course we cannot do it perfectly.

**[26:14 – 26:23]** So actually X is near the result of the decoder, but with some noise, right?

**[26:23 – 26:29]** Just like in linear regression, we are supposed to recover the points, but we cannot do it perfectly.

**[26:29 – 26:35]** So we say that the points are around our straight line, but with some noise.

**[26:36 – 26:37]** Exactly the same.

**[26:38 – 26:43]** So here it would also be natural to assume some kind of simple noise like a Gaussian noise.

**[26:43 – 26:46]** Otherwise, we wouldn't know what to do with it.

**[26:47 – 26:49]** So here, this is also a simple distribution.

**[26:50 – 26:58]** But now, if I take the product of two Gaussians, it's going to be a Gaussian.

**[26:59 – 27:00]** It's going to be simple.

**[27:01 – 27:10]** And this guy over here is this incredibly complicated distribution in this huge dimensional space.

**[27:10 – 27:14]** There is no way that I can assume that cat pictures form a Gaussian.

**[27:14 – 27:15]** That doesn't work.

**[27:15 – 27:22]** The whole point of our model is to somehow, you know, streamline and simplify this impossibly complicated distribution.

**[27:24 – 27:36]** So notice how just this simple equality already tells us that we cannot assume both the decoder and the encoder to be easy.

**[27:37 – 27:42]** Because if I now write the encoder also to be a Gaussian, this equality will never happen, right?

**[27:43 – 27:52]** The encoder, if I want to have two simple things on the left, it means that the encoder will have to be something very complicated.

**[27:53 – 27:56]** Because it will have to kind of cancel out with this and give you a ghost.

**[27:58 – 28:05]** So this is going to be, okay, let me just leave it as P of Z given X, okay?

**[28:06 – 28:11]** So I cannot really assume both the decoder and the encoder to be simple.

**[28:14 – 28:19]** I can choose. I could assume the encoder to be simple, then the decoder would be difficult.

**[28:19 – 28:21]** But I want to keep the decoder easier.

**[28:21 – 28:27]** That is a more natural choice to have the Gaussian noise at the output, as you will see.

**[28:27 – 28:32]** But this means that the encoder cannot really be simple.

**[28:32 – 28:39]** And the point of the variational autoencoder, why it's called the variational autoencoder,

**[28:39 – 28:50]** is because we take this p of z given x and we approximate it by, sorry, q of z, by a simple distribution q of z.

**[28:51 – 28:53]** And this will be our Gaussian.

**[28:53 – 29:07]** So the whole point of the variational autoencoder is to say, yeah, the encoder will produce Gaussian, the parameters for a Gaussian.

**[29:07 – 29:14]** But I know from the very beginning that this is not the true distribution p of z given x.

**[29:15 – 29:15]** This cannot happen.

**[29:16 – 29:17]** I don't know it.

**[29:17 – 29:18]** It's very complicated.

**[29:18 – 29:22]** This is an approximation to p of z given x.

**[29:22 – 29:30]** And the question is, how do I make this approximation?

**[29:33 – 29:50]** And here we come to this promised very important idea, one of the most basic ideas in machine learning, one that underlies millions and millions of different models and that appears all through our field.

**[29:51 – 29:53]** And that's the idea of variational approximations.

**[29:53 – 29:59]** So let me explain it to you from the very beginning.

**[30:00 – 30:05]** So here I've motivated that we need an approximation, right?

**[30:05 – 30:11]** And now let me explain to you how approximations work.

**[30:13 – 30:17]** So again, let me start from scratch.

**[30:17 – 30:27]** Again, I start with a very simple formula and I will be doing some simple but kind of non-obvious transformations.

**[30:27 – 30:33]** Non-obvious in the sense that they will be easier, but you will wonder why on earth am I doing that?

**[30:33 – 30:34]** That's okay.

**[30:34 – 30:35]** Just trust me.

**[30:35 – 30:40]** It will take three or four lines and then you will see why we needed all that.

**[30:41 – 30:48]** So we begin with the obvious identity and say, okay, let me write it with logs.

**[30:48 – 30:50]** Log P of X, Z.

**[30:50 – 30:58]** Now I need to start with the right variable.

**[30:58 – 31:02]** Yeah, I need P of X and P of Z given X, right?

**[31:02 – 31:05]** So this is obviously true.

**[31:05 – 31:07]** This is just this very same identity.

**[31:07 – 31:14]** And it contains the joint distribution and it contains this difficult, complicated distribution that I want to approximate.

**[31:14 – 31:16]** It doesn't have any Q yet.

**[31:17 – 31:23]** So first I take the logs and I put P of X on one side and the rest on the other side.

**[31:24 – 31:25]** So log P of X.

**[31:26 – 31:28]** Again, so far nothing is happening at all.

**[31:28 – 31:34]** Log P of X, Z minus log P of Z given X.

**[31:37 – 31:46]** Now I make the first tricky step, which is I take the expectation.

**[31:46 – 31:47]** So this is just an identity.

**[31:47 – 31:48]** It's always true.

**[31:49 – 31:59]** Now I take the expectation with respect to Q of Z, where Q is any distribution at this point, on the left and on the right.

**[31:59 – 32:02]** So I take the expectation on both sides of the equality.

**[32:02 – 32:11]** Obviously, it still remains in equality, but notice that I take the expectation with respect to Z, and here there is no Z.

**[32:12 – 32:16]** So log P of X is a constant with respect to Z.

**[32:17 – 32:19]** So on the left, nothing changes.

**[32:19 – 32:23]** Log P of X just remains a constant.

**[32:24 – 32:34]** And on the right, I have this expectation of log P of X Z minus log P of Z given X.

**[32:34 – 32:42]** OK, and now the final non-trivial step.

**[32:43 – 32:50]** I add and subtract the expectation of log Q.

**[32:51 – 32:54]** So like the entropy of the distribution Q.

**[32:54 – 32:59]** Again, at this point, you probably don't understand why I'm doing this.

**[33:00 – 33:01]** This will become clear in a couple of ways.

**[33:02 – 33:06]** So I add and subtract expectation of log Q.

**[33:07 – 33:09]** Again, this obviously doesn't change the identity.

**[33:11 – 33:14]** So what do I get now?

**[33:15 – 33:22]** Now I want to take the minus from here and put it together with this log.

**[33:23 – 33:27]** And I want to take the plus from here and put it together with this log.

**[33:28 – 33:30]** So my final formula is this.

**[33:31 – 33:41]** Log P of X is the expectation of log P of XZ divided by P of Z.

**[33:41 – 33:44]** I put this log together with this.

**[33:45 – 33:49]** Minus or do I want plus?

**[33:49 – 33:50]** Yeah, I think I want plus.

**[33:50 – 34:01]** So plus expectation of Q of Z log Q of Z divided by log P of Z given X.

**[34:03 – 34:06]** Okay, so far so good.

**[34:06 – 34:09]** I hope it hasn't been a problem for you to follow.

**[34:10 – 34:15]** I have just been writing some basic algebra and basic probability theory,

**[34:15 – 34:18]** not even probability theory, just put the expectation on top.

**[34:19 – 34:22]** Nothing has been happening, right?

**[34:22 – 34:25]** It's just a string of obvious identities.

**[34:25 – 34:27]** It's just not clear what this leads to.

**[34:29 – 34:32]** But we are already done.

**[34:32 – 34:36]** So this is the main formula of variational approximations.

**[34:38 – 34:40]** And here is how it works.

**[34:40 – 34:42]** Here is what it actually means.

**[34:43 – 34:47]** On the left, you have a constant, right?

**[34:47 – 34:53]** Now let's look at this as kind of from the point of view of our problem.

**[34:53 – 34:55]** So this is just an identity.

**[34:55 – 34:59]** It holds always for any p of x, z and any q of z.

**[34:59 – 35:00]** This is just always true.

**[35:01 – 35:04]** But let's look at it from our point of view.

**[35:04 – 35:07]** And our point of view is I want to find q of z.

**[35:07 – 35:10]** That would be a good approximation for p of z given x.

**[35:11 – 35:15]** So in a way, I want to be optimizing something.

**[35:15 – 35:17]** Don't yet know what.

**[35:18 – 35:21]** With respect to q of z, right?

**[35:21 – 35:29]** So let's view this as a functional, as a dependence on q of z.

**[35:30 – 35:33]** So on the left, I don't have q of z.

**[35:33 – 35:38]** On the left, it's just a global constant, the likelihood of the data set.

**[35:38 – 35:41]** On the right, I have this guy.

**[35:43 – 35:45]** Let's call it L of q.

**[35:46 – 35:50]** Some, I don't know, this cursive L of q.

**[35:51 – 35:55]** Plus, and here is the most beautiful part.

**[35:55 – 35:57]** What is this guy?

**[35:57 – 35:59]** What is the second term here?

**[35:59 – 36:16]** It's the Kuhlbach-Leibler divergence between q of z and log, sorry, not log, just p, p of z given x, right?

**[36:17 – 36:20]** I hope you know what Kuhlbach-Leibler divergence is.

**[36:20 – 36:27]** If not, it's a common metric that shows how similar two distributions are.

**[36:28 – 36:30]** So I think I introduced it at some point, right?

**[36:30 – 36:39]** So Kuhlbach from Q to P is integral Q times log Q divided by P dx.

**[36:39 – 36:41]** So this is exactly this, right?

**[36:41 – 36:55]** And here we get a thing that shows how close Q of z is to the distribution that we want to approximate, right?

**[36:55 – 37:00]** So basically, this is a great optimization target.

**[37:00 – 37:05]** I want to minimize it with respect to Q, okay?

**[37:07 – 37:13]** And I could just start with it.

**[37:14 – 37:19]** I didn't need all of these formulas to know that I want to minimize KL from Q to P.

**[37:19 – 37:22]** But P is a very complicated distribution.

**[37:22 – 37:24]** It's very hard to work with P of z given x.

**[37:25 – 37:34]** Because this P of z given x, I mean, in a standard machine learning application of rational approximations,

**[37:34 – 37:44]** it would be some complicated posterior of a huge probabilistic model with lots of hidden variables that we need to integrate over.

**[37:45 – 37:47]** And it would be very unclear what it is.

**[37:48 – 38:00]** And here, too, P of z given x is this strange, complicated distribution that you need to multiply this distribution of cat photos by to get a simple Gaussian.

**[38:00 – 38:07]** Who knows what it looks like? How can we evaluate it? How can we work with it? No idea.

**[38:09 – 38:18]** And the whole point of this simple formulas was to say that instead of working with this P of z directly,

**[38:18 – 38:31]** I can just say that, look, I have the sum of two terms, and together they make up a constant which is independent of Q.

**[38:31 – 38:43]** So, if I want to make this guy smaller with respect to Q, it's exactly equivalent to making this guy larger with respect to Q, right?

**[38:44 – 38:45]** Because they should sum up to a constant.

**[38:46 – 39:00]** So, if there is this constant, it consists of two components, and I want to make one component smaller, which means that the other is larger.

**[39:00 – 39:03]** And vice versa, if I make the other one larger, it means I make the first one smaller.

**[39:04 – 39:21]** So, minimizing the KL divergence, the Kluber-Klider divergence from Q to P, to P of Z given X, to our posterior, to what we are interested in, is equivalent to maximizing this beautiful thing.

**[39:24 – 39:48]** And it doesn't sound like much of a result yet, but if you look at this, so this L is called the variational lower bound, or evidence lower bound, ELBO, sometimes you see an acronym.

**[39:49 – 40:12]** So, this L of Q is a lower bound to a constant that you want to maximize, right? And if you look at what it actually is, this L of Q, it's this, let's say, integral, okay, let me rewrite the expectation as an integral, doesn't matter, just to show you the formula both ways.

**[40:12 – 40:40]** Log P of xz divided by Q of z dz, right? So it's like, let me open the logs back, dz minus P of z log P of xz dz, something like that.

**[40:42 – 41:00]** And if you look at it, you see that now all that it involves are, well, first the distribution that we are optimizing Q, and second, it involves the join distribution, P of xz.

**[41:01 – 41:03]** And this is a huge difference.

**[41:03 – 41:21]** So usually in machine learning, basically always in machine learning, when you define your model, if you know all of the variables, like usually this is applied for probabilistic models, where x are the visible variables, the observables, and z are the hidden variables.

**[41:22 – 41:27]** So if you know both observable and hidden variables, then everything is easy.

**[41:28 – 41:32]** The distribution, all the distributions decompose, P of xz is probably very simple.

**[41:32 – 41:35]** It's big, but it's simple.

**[41:36 – 41:40]** But if you need to do something like this, now it's very complicated.

**[41:41 – 41:48]** Or if you need to do something like this, for example, to integrate over all these, it's also very complicated.

**[41:49 – 41:53]** But the joint distribution is probably very simple.

**[41:53 – 41:55]** Otherwise, you don't have a good model.

**[41:55 – 42:03]** So the whole point of rational approximations is to switch from working with a very difficult distribution,

**[42:03 – 42:09]** very complicated distribution that you can't work with, to working with a simple distribution that you can work with.

**[42:11 – 42:18]** And so getting back to the variational autoencoder, in our variational autoencoder,

**[42:18 – 42:24]** this is really obvious and it's shown in a very clear form.

**[42:24 – 42:28]** So what is this p of z given x?

**[42:28 – 42:32]** It's something very, very complicated that we have no idea how to handle.

**[42:32 – 42:36]** But what is p of x and z? What is the join distribution?

**[42:37 – 42:40]** Well, it's a product of two Gaussians. There we go.

**[42:42 – 42:47]** So to make it easier, we just need to decompose it in a different way.

**[42:48 – 42:58]** So let's just look at it as log p of z plus log p of x given z and not the other way around.

**[42:59 – 43:01]** Not in this decomposition.

**[43:04 – 43:15]** So this idea is the variational approximation and basically how it is used in practice,

**[43:15 – 43:27]** like how you would actually use it is you go through this math, you have to go through this math.

**[43:27 – 43:35]** Well, this math is always the same, but then you need to substitute your specific distributions, your specific model, and it gives you those functions.

**[43:35 – 43:39]** So, let's see how it goes with the variational attaincoder.

**[43:39 – 43:43]** Let me continue this equality.

**[43:43 – 44:01]** So, I plug in this decomposition, and I get something like expectation P of Z log P of X given Z, right?

**[44:01 – 44:09]** Plus expectation log P of Z, that's the first term,

**[44:09 – 44:15]** minus expectation log Q of Z, right?

**[44:15 – 44:20]** And let me put together the second and third term,

**[44:20 – 44:26]** so that again it will be more clear what's happening.

**[44:26 – 44:38]** Minus expectation log Q of Z divided by P of Z, okay?

**[44:38 – 44:45]** So, what is this guy over here?

**[44:45 – 44:56]** Well, this guy over here is the chi-L divergence between Q of Z and P of Z, right?

**[44:56 – 45:06]** So Q of Z is our distribution that will be an approximation over here.

**[45:06 – 45:10]** So this guy is Q of Z.

**[45:10 – 45:17]** And P of Z is this orange guy, is the simple distribution that I want to sample from.

**[45:17 – 45:30]** So basically, this says that my distribution Q, okay, let me actually write it, my Gaussian

**[45:30 – 45:44]** distribution with some parameters mu X and sigma X should be close to a standard Gaussian.

**[45:44 – 45:52]** P of Z is this simple Gaussian that I want to sample from.

**[45:52 – 45:55]** And this is exactly the regularizer.

**[45:55 – 46:02]** So this is the part of the loss which is the regularizer.

**[46:02 – 46:14]** Again, notice how it is kind of at the same time, just like we discussed, but also more precise.

**[46:14 – 46:23]** So I told you that, well, probably I will need to regularize this, otherwise bad stuff will happen.

**[46:23 – 46:31]** And, you know, the distributions in the latent space will float away from each other and they will become smaller.

**[46:31 – 46:36]** Variance will go to zero, blah, blah, blah, you probably need to regularize.

**[46:36 – 46:41]** But how? What should be the form of the regularizer?

**[46:41 – 46:49]** We honestly had no idea, but after this little bit of math, now we see an exact formula.

**[46:49 – 46:57]** I will not go through the details, but you can just write it down and you will see like an exact formula,

**[46:57 – 47:04]** a function of mu and sigma that you can just plug into PyTorch, right?

**[47:04 – 47:09]** So, and you wouldn't be able to arrive at this formula in any other way.

**[47:09 – 47:16]** Somehow you need to understand that your regularizer should be specifically this value.

**[47:16 – 47:18]** And where do you get it from?

**[47:18 – 47:23]** Well, you get it from the variational approximation, at least I don't know any other way.

**[47:23 – 47:29]** So, yeah, it seems very natural, but if you are looking at the problem from here,

**[47:29 – 47:32]** then it seems just as natural as any other thing.

**[47:32 – 47:44]** You could have just said, oh, okay, so let me put the Gaussian on mu and some gamma distribution on sigma or whatever, right?

**[47:44 – 47:52]** You could have chosen this regularizer, but it would be just one of very many ideas.

**[47:52 – 47:56]** And here we see why we choose this idea.

**[47:56 – 48:05]** So the variational approximation gives you the loss functions, and this is basically all you need, right?

**[48:05 – 48:07]** And what is the first part?

**[48:07 – 48:09]** What is this guy?

**[48:09 – 48:17]** Well, yeah, let's make it purple because the decoder was purple, and this is about the decoder.

**[48:17 – 48:20]** So what is this log P given C?

**[48:20 – 48:22]** It's the decoder distribution, right?

**[48:22 – 48:32]** So it's the expectation of the log of this Gaussian, of this Gaussian over here, right?

**[48:32 – 48:46]** Of the Gaussian of X around the result of the decoder with some noise, right?

**[48:46 – 48:55]** And then you can just open the brackets in the sense you can just plug in what the density

**[48:55 – 49:02]** of the normal distribution, take the log, and again, I won't bore you with the full derivation,

**[49:02 – 49:05]** but we kind of know what's going to happen.

**[49:05 – 49:08]** We know the density of the normal distribution, right?

**[49:08 – 49:16]** So it's like some constant, maybe complicated, but still, minus 1 over 2c to the power d or

**[49:16 – 49:26]** something times, what, times x minus the result of the decoder squared, right?

**[49:26 – 49:31]** That's the exponent of the normal distribution.

**[49:31 – 49:42]** So this is basically a constant, which I don't care about, minus some other constant, which

**[49:42 – 49:59]** I don't know, I don't care about, times the expectation of the least squares loss between

**[49:59 – 50:06]** x and the decoder result, right?

**[50:06 – 50:15]** So this, actually, is the part which is the reconstruction loss.

**[50:15 – 50:23]** The expectation over Q basically just means that I take the average over the training data.

**[50:23 – 50:28]** In practice, it just means averaging over the dataset.

**[50:28 – 50:31]** We approximate this expectation with the average over the dataset.

**[50:31 – 50:45]** So it's like the actual loss is something like one over n times the sum xn minus the decoder of zn.

**[50:45 – 50:52]** And zn actually comes from where does this come from?

**[50:52 – 50:58]** It comes from the encoder of xn, something like this, right?

**[50:58 – 51:11]** So what have we done? I didn't go through all the math in detail, but I hope the ideas are already here.

**[51:11 – 51:14]** I hope that they are clear to you. What have we done?

**[51:14 – 51:22]** We started with this very basic decomposition, which is not much of an idea, to be honest.

**[51:22 – 51:33]** We applied the variational approximation, and as a result, we see that our variational lower bound,

**[51:33 – 51:57]** our L is minus some constant, minus some constant times this, times the reconstruction loss, minus the regularizer.

**[51:57 – 52:04]** And of course I want to do it like this. I need to maximize this lower bound,

**[52:04 – 52:15]** which means that I need to minimize the sum of these two losses.

**[52:15 – 52:26]** So I need to maximize the variational lower bound, which means that I need to minimize this with respect to,

**[52:26 – 52:33]** and what is Q? Q are these mu and sigma parameters of the output of the encoder.

**[52:33 – 52:40]** So that's how it works, that's the whole thing. Or at least that's the first part of the thing,

**[52:40 – 52:53]** that's the thing with the loss functions. So again, to summarize, we have come from this general idea

**[52:53 – 52:58]** of let's have some sampling inside an autoencoder, and let's have some

**[52:58 – 53:04]** regularizer on the sampling distributions because otherwise they're not going to work.

**[53:04 – 53:12]** We have come to exact formulas. We basically just see that, oh, what should be the regularizer?

**[53:12 – 53:17]** Well, the regularizer should be this, and this is just a very specific formula.

**[53:17 – 53:23]** You can look it up. It's actually not very trivial. You wouldn't be able to guess it if you didn't know.

**[53:23 – 53:27]** But it's a specific formula of mu and sigma.

**[53:27 – 53:33]** And how do I define the reconstruction loss?

**[53:33 – 53:40]** Well, the reconstruction loss just follows from the noise assumption in the decoder.

**[53:40 – 53:45]** So why was it the least squares? Because I chose the Gaussian over here.

**[53:45 – 53:49]** I could have chosen a different noise model. I would have gotten a different reconstruction loss.

**[53:49 – 53:56]** So there are no surprises here. This we kind of expected. But the variational to encoder also

**[53:56 – 54:03]** gives you an exact form of the regularizer. So this is nice. I think this is a very beautiful

**[54:03 – 54:11]** application of this variational idea in deep learning. But that was only one of our problems,

**[54:11 – 54:18]** right? There was also the second problem, the sampling problem. How do I put gradients

**[54:18 – 54:27]** through sampling stuff? And that's actually much easier. It's called the re-parameterization trick.

**[54:33 – 54:45]** Trick. And the re-parameterization trick works as follows. So let me copy this basic structure again.

**[54:46 – 54:58]** X goes to the encoder. The encoder produces mu and sigma. And then I'm supposed to kind of sample Z

**[55:00 – 55:13]** from this, right? And then it will go to the decoder and will produce X hat. So,

**[55:14 – 55:25]** the trick is, instead of sampling from this Gaussian, I want to restructure this

**[55:25 – 55:30]** neural network in such a way. That's why it's called reparameterization. I want to

**[55:30 – 55:38]** reparameterize the sampling distribution so that I could sample in advance. So that I could sample

**[55:39 – 55:51]** before I know mu and sigma, right? And so that I could have some just separate input

**[55:51 – 56:02]** here. Let's call it z prime, z zero or something. Let's call it u. I could have a separate input here

**[56:02 – 56:10]** that would be sampled by itself with no regard for x in advance. And then something would happen

**[56:10 – 56:16]** inside and I would get the same output. If I can do that, then I've solved the problem because now

**[56:16 – 56:22]** it's not a problem if I need to sample part of the inputs, right? It's only a problem if I need to

**[56:23 – 56:34]** inside the gradient flow. So how do I do this? Well, it depends on the specific distribution.

**[56:35 – 56:42]** Sometimes you can do it, sometimes you can't, but for Gaussians you definitely can. So what do we

**[56:42 – 56:48]** need to know about Gaussians? We just need to know that if you want to sample from a Gaussian

**[56:48 – 56:58]** with a given mean and a given covariance matrix, it's the same as sampling from a standard Gaussian.

**[56:58 – 57:11]** And then multiplying, so let's call it u times sigma. Okay, let me write it as distribution first.

**[57:11 – 57:19]** So this distribution is just a linear function of the standard normal. So it's the same as sampling z

**[57:19 – 57:27]** from a standard Gaussian, then doing component-wise multiplication by sigmas, and then adding mu.

**[57:27 – 57:34]** So mu is a shift, right, in the Gaussian, and sigma is a rescaling of the Gaussian.

**[57:35 – 57:42]** But the shape of the distribution is the same, and you can start with a standard Gaussian

**[57:42 – 57:43]** and apply the parameters afterwards.

**[57:45 – 57:49]** So that's exactly what we are going to do. That's the whole trick.

**[57:50 – 57:56]** We are going to say that this additional input, this u, is sampled from a standard Gaussian.

**[57:57 – 58:00]** And then what do I need to do with it?

**[58:00 – 58:10]** Well, I need to multiply it component-wise by sigma, and then I need to add mu.

**[58:11 – 58:17]** And here I get z, which is actually sampled from this distribution.

**[58:19 – 58:22]** So it's a property of the Gaussian specifically.

**[58:22 – 58:30]** If I had a different distribution of the output of the encoder, I would need to have a different thing here.

**[58:30 – 58:32]** And maybe I wouldn't even be able to do this.

**[58:32 – 58:35]** But for a Gaussian, I definitely am able to do this.

**[58:35 – 58:38]** And it's really straightforward.

**[58:40 – 58:40]** And that's it.

**[58:41 – 58:44]** And I take this Z and I plug it into the decoder and I'm done.

**[58:46 – 58:46]** Okay.

**[58:47 – 58:51]** So this is the whole trick.

**[58:51 – 58:53]** So the sampling part is conceptually interesting.

**[58:54 – 58:57]** I think it's a very beautiful trick, but it's quite simple.

**[58:59 – 59:04]** And with that, we are basically done with the variational autoencoders.

**[59:04 – 59:11]** So for the remaining half an hour, I will probably mostly switch to the slides

**[59:11 – 59:19]** because it will be just a review of diffusion models

**[59:19 – 59:24]** and we'll discuss some ideas that underlie them.

**[59:24 – 59:28]** But of course, the mass of the diffusion models actually also involves

**[59:28 – 59:33]** a lot of variational approximations, but that will be too difficult for us.

**[59:33 – 59:40]** So, let me first quickly go through the slides on bias.

**[59:41 – 59:46]** I will show you the same pictures in a more beautiful way, I hope.

**[59:47 – 59:48]** Okay, so, oh, yeah.

**[59:49 – 59:55]** This is my picture of the taxonomy that I talked about yesterday.

**[59:56 – 59:58]** Let me come back to it at the end.

**[59:59 – 1:00:00]** Rational lot encoders.

**[1:00:01 – 1:00:05]** So, this is the problem, right?

**[1:00:05 – 1:00:07]** This is the motivation that I started with.

**[1:00:07 – 1:00:10]** It's relatively easy to train a lot of encoder,

**[1:00:11 – 1:00:15]** but the high-dimensional manifold is, of course, very, very difficult,

**[1:00:15 – 1:00:18]** but even the lower-dimensional latent space is also non-trivial.

**[1:00:18 – 1:00:19]** So, how do we simplify?

**[1:00:22 – 1:00:24]** Even in a low-dimensional space,

**[1:00:24 – 1:00:27]** if I start just sampling from a Gaussian,

**[1:00:27 – 1:00:28]** I will not fall in this manifold.

**[1:00:32 – 1:00:34]** So, the idea of the variational lot of encoder

**[1:00:34 – 1:00:36]** that I started with today

**[1:00:37 – 1:00:41]** is let's have whole distributions of these

**[1:00:41 – 1:00:43]** produced by the encoder.

**[1:00:44 – 1:00:47]** So, we can have one distribution here,

**[1:00:48 – 1:00:49]** then we sample from it,

**[1:00:49 – 1:00:50]** and we are supposed to reconstruct

**[1:00:50 – 1:00:52]** the original cat picture

**[1:00:52 – 1:00:56]** from any point sampled from this distribution.

**[1:00:56 – 1:00:59]** Of course, it won't always succeed,

**[1:00:59 – 1:01:01]** but that's the goal, right?

**[1:01:02 – 1:01:06]** And our intuition is that

**[1:01:06 – 1:01:08]** we want to kind of cover the space

**[1:01:08 – 1:01:10]** of latent codes with these distributions

**[1:01:10 – 1:01:12]** and we want to have them wide enough

**[1:01:12 – 1:01:14]** and we want to have them close enough

**[1:01:14 – 1:01:17]** to each other so that afterwards

**[1:01:17 – 1:01:22]** when I sample from just a standard Gaussian,

**[1:01:22 – 1:01:40]** I get to a good part of the space

**[1:01:40 – 1:01:42]** because any part of the space is a good part.

**[1:01:42 – 1:01:45]** It's kind of covered by these small distributions.

**[1:01:46 – 1:01:50]** But of course, it's not going to happen in reality

**[1:01:50 – 1:01:51]** unless I do regularization.

**[1:01:52 – 1:01:53]** So here is the effect that I mentioned.

**[1:01:54 – 1:01:56]** The points will fly away from each other

**[1:01:56 – 1:01:58]** and the variances will shrink to zero.

**[1:01:59 – 1:02:03]** So we need to have both a reconstruction loss

**[1:02:03 – 1:02:08]** and some regularization for the encoder output.

**[1:02:13 – 1:02:16]** And here are the two questions that we discussed.

**[1:02:16 – 1:02:18]** How do we choose the loss function in the regularizer

**[1:02:18 – 1:02:21]** and how do we pass the gradients through the sampling process?

**[1:02:23 – 1:02:26]** So here is the derivation that we did.

**[1:02:27 – 1:02:30]** We started with this simple equality.

**[1:02:31 – 1:02:35]** And in this equality, we know that this guy is the encoder,

**[1:02:35 – 1:02:36]** this guy is the decoder,

**[1:02:36 – 1:02:38]** this guy is the distribution we want to sample z from.

**[1:02:38 – 1:02:41]** And this is this extremely complicated thing.

**[1:02:41 – 1:02:44]** So both the encoder and the decoder cannot be simple.

**[1:02:46 – 1:02:51]** So instead, we are going to model the decoder distribution

**[1:02:51 – 1:02:54]** as a simple one, as just a round Gaussian.

**[1:02:54 – 1:03:00]** And we are going to approximate this complicated encoder distribution

**[1:03:00 – 1:03:02]** with also a Gaussian.

**[1:03:05 – 1:03:08]** And then we do the variational approximation.

**[1:03:08 – 1:03:12]** We get that our variational lower bound

**[1:03:12 – 1:03:17]** plus the KL divergence between our approximation

**[1:03:17 – 1:03:20]** and what we need to approximate equal constant.

**[1:03:20 – 1:03:23]** So as we make the lower bound bigger,

**[1:03:24 – 1:03:26]** the KL divergence shrinks.

**[1:03:26 – 1:03:31]** And this gives us exactly the losses.

**[1:03:31 – 1:03:36]** So we know what is the reconstruction loss

**[1:03:36 – 1:03:38]** that follows from the decoder model.

**[1:03:38 – 1:03:44]** And we know exactly what regularizer we should be using.

**[1:03:44 – 1:03:47]** So this is the idea of variational autoencoders.

**[1:03:49 – 1:03:51]** And here is the reparametrization trick.

**[1:03:52 – 1:03:56]** So fortunately for Gaussians,

**[1:03:56 – 1:03:57]** it's really simple and straightforward.

**[1:03:57 – 1:03:59]** We just need to sample from a standard Gaussian

**[1:03:59 – 1:04:03]** and then we multiply by sigma,

**[1:04:03 – 1:04:05]** we add mu, and we're done.

**[1:04:08 – 1:04:10]** Okay, so this is what,

**[1:04:13 – 1:04:17]** this is, let me call it,

**[1:04:17 – 1:04:19]** this is the proper way to do autoencoders.

**[1:04:21 – 1:04:26]** When it appeared, it did not really catch on.

**[1:04:27 – 1:04:31]** And if you read early papers from 10 years ago,

**[1:04:31 – 1:04:33]** you will see the variational autoencoder

**[1:04:33 – 1:04:35]** always like this baseline

**[1:04:35 – 1:04:37]** that you kind of need to beat,

**[1:04:37 – 1:04:38]** but it's not very difficult to beat.

**[1:04:39 – 1:04:42]** The real competitors are not the YS.

**[1:04:43 – 1:04:47]** But since then, there have been a number of extensions

**[1:04:47 – 1:04:49]** which I don't have time to discuss,

**[1:04:49 – 1:04:53]** but by now, the YS have been extended

**[1:04:53 – 1:04:55]** to discrete latent spaces,

**[1:04:56 – 1:05:01]** which is, let me not talk about this,

**[1:05:01 – 1:05:03]** otherwise I won't have time for the diffusion,

**[1:05:04 – 1:05:08]** but they have been extended to discrete latent spaces,

**[1:05:09 – 1:05:12]** that is, Z is now a set of tokens, sequence of tokens,

**[1:05:13 – 1:05:19]** and this has opened up a lot of doors, so to speak.

**[1:05:19 – 1:05:22]** This has opened up possibilities to, for example,

**[1:05:22 – 1:05:25]** write these latent codes with a transformer,

**[1:05:25 – 1:05:27]** starting from text.

**[1:05:27 – 1:05:29]** It becomes like machine translation,

**[1:05:29 – 1:05:31]** which transformers are perfect for,

**[1:05:32 – 1:05:36]** to convert the prompt into, the text prompt,

**[1:05:37 – 1:05:38]** into this sequence of tokens

**[1:05:38 – 1:05:45]** that will then be decoded into a picture.

**[1:05:46 – 1:05:49]** And that's how DALI worked in 2020 or 2021.

**[1:05:50 – 1:05:53]** And there have been more ideas.

**[1:05:54 – 1:05:57]** I won't discuss them in too much detail,

**[1:05:57 – 1:06:00]** but basically, by now,

**[1:06:01 – 1:06:05]** variational autoencoders underlie a lot of stuff.

**[1:06:06 – 1:06:09]** And, for example, the diffusion models

**[1:06:09 – 1:06:11]** that we are going to discuss now,

**[1:06:11 – 1:06:16]** they usually happen not in the space of images themselves.

**[1:06:16 – 1:06:19]** I will show you interesting pictures

**[1:06:19 – 1:06:21]** that look like they happen in the space of images,

**[1:06:22 – 1:06:23]** just to explain things.

**[1:06:23 – 1:06:26]** But then we will see that, actually,

**[1:06:26 – 1:06:30]** diffusion models operate in the latent space of some model.

**[1:06:32 – 1:06:36]** It would be too computationally expensive

**[1:06:36 – 1:06:41]** to have them operate on pixels.

**[1:06:41 – 1:06:45]** It's much easier and much better

**[1:06:45 – 1:06:47]** to have them operate in the latent space.

**[1:06:47 – 1:06:50]** And usually it's the latent space of what?

**[1:06:50 – 1:06:56]** Usually it's the latent space of a modern variational autoencoder,

**[1:06:56 – 1:07:01]** which, actually, let me just mention maybe one architecture

**[1:07:01 – 1:07:07]** that you might hear about VQ again.

**[1:07:10 – 1:07:16]** It's a variational autoencoder with a discrete latent space,

**[1:07:16 – 1:07:18]** which I won't go into,

**[1:07:18 – 1:07:22]** but it also adds some adversarial losses inside.

**[1:07:23 – 1:07:28]** So it kind of, again, let's not go into details,

**[1:07:28 – 1:07:33]** but it has the basic structure of a variational autoencoder,

**[1:07:34 – 1:07:37]** plus it has an adversarial loss

**[1:07:37 – 1:07:44]** that looks at small patches of the resulting image

**[1:07:44 – 1:07:47]** and makes sure they're realistic,

**[1:07:47 – 1:07:52]** makes sure that locally the small patches look nice

**[1:07:52 – 1:07:54]** and similar to patches from real images.

**[1:07:54 – 1:07:58]** So there is a whole separate discriminator there

**[1:07:58 – 1:08:04]** to make this fine local structure good.

**[1:08:06 – 1:08:09]** And usually like modern diffusion models work

**[1:08:09 – 1:08:11]** in the latent space of some kind of EQ again

**[1:08:11 – 1:08:12]** or something like that.

**[1:08:13 – 1:08:18]** Anyway, on to the diffusion models.

**[1:08:19 – 1:08:23]** This is our last big idea.

**[1:08:25 – 1:08:32]** And it's a very, very simple idea in essence

**[1:08:32 – 1:08:34]** and a very, very difficult idea

**[1:08:34 – 1:08:37]** if I write it down in full detail mathematically.

**[1:08:37 – 1:08:38]** So I won't.

**[1:08:38 – 1:08:39]** Okay.

**[1:08:40 – 1:08:41]** In variational autoencoders,

**[1:08:41 – 1:08:44]** the mathematical formalization was also pretty simple.

**[1:08:44 – 1:08:47]** Here, it's also a variational bound,

**[1:08:47 – 1:08:48]** but much more difficult one.

**[1:08:48 – 1:08:52]** So let me just give you the basic idea.

**[1:08:53 – 1:08:56]** And it dates back to 2015.

**[1:08:57 – 1:09:00]** This is like the foundational paper and diffusion models,

**[1:09:00 – 1:09:03]** Solvig-Stein and co-authors.

**[1:09:03 – 1:09:06]** And it has a very interesting title,

**[1:09:06 – 1:09:10]** Deep Unsupervised Learning Using Non-Equilibrium Thermodynamics.

**[1:09:10 – 1:09:13]** Actually, as an aside,

**[1:09:13 – 1:09:16]** physics, thermodynamics, and deep learning

**[1:09:16 – 1:09:18]** have a lot in common.

**[1:09:19 – 1:09:21]** I'm actually doing some research

**[1:09:21 – 1:09:23]** on the thermodynamics of stochastic gradient descent.

**[1:09:24 – 1:09:27]** If you go to my website,

**[1:09:27 – 1:09:28]** you will see a long blog post

**[1:09:28 – 1:09:30]** with an introduction to this area.

**[1:09:30 – 1:09:32]** I think it's very cool.

**[1:09:32 – 1:09:38]** And there are some real parallels there.

**[1:09:38 – 1:09:41]** And there is like an ideal gas law

**[1:09:41 – 1:09:43]** about stochastic gradient descent.

**[1:09:44 – 1:09:47]** So, but here it's in a different sense.

**[1:09:47 – 1:09:49]** Here the analogy is different.

**[1:09:50 – 1:09:53]** Here the analogy actually just comes

**[1:09:53 – 1:09:55]** from a basic fact on Markov chains.

**[1:09:55 – 1:09:58]** I'm not even sure you need statistical physics here.

**[1:09:58 – 1:09:59]** I think you don't.

**[1:10:00 – 1:10:04]** The basic idea of Markov chains is that,

**[1:10:04 – 1:10:10]** well, if you, you can train a Markov chain

**[1:10:10 – 1:10:13]** that will add noise

**[1:10:13 – 1:10:20]** and will add more and more noise to the input.

**[1:10:21 – 1:10:25]** And after enough steps, after some hundreds of steps,

**[1:10:26 – 1:10:28]** the result will be indistinguishable from randomness.

**[1:10:30 – 1:10:33]** So this is kind of straightforward, right?

**[1:10:33 – 1:10:36]** If I start with a crisp, nice picture

**[1:10:36 – 1:10:39]** and I start just adding Gaussian noise to it,

**[1:10:39 – 1:10:42]** well, I didn't do it to the very end

**[1:10:42 – 1:10:47]** so that you can still see some shade of the original.

**[1:10:48 – 1:10:51]** But if you do it like 500 times,

**[1:10:51 – 1:10:54]** of course, as a result, you will see just Gaussian noise

**[1:10:54 – 1:10:58]** that's indistinguishable from just random sampling.

**[1:10:58 – 1:11:09]** And the point of diffusion models is to try and reverse this process.

**[1:11:11 – 1:11:16]** So you have this noising chain that adds noise

**[1:11:16 – 1:11:20]** and you want to turn it into a denoising chain.

**[1:11:21 – 1:11:26]** So in the forward direction, the transformation is trivial.

**[1:11:26 – 1:11:29]** You just add, let's say, Gaussian noise.

**[1:11:29 – 1:11:34]** In the opposite direction, it's a denoising procedure.

**[1:11:36 – 1:11:40]** So you are supposed to remove Gaussian noise,

**[1:11:40 – 1:11:43]** which is, of course, a much more difficult thing.

**[1:11:44 – 1:11:47]** You can't really do it exactly.

**[1:11:48 – 1:11:50]** You don't know what kind of noise was added.

**[1:11:51 – 1:11:54]** I mean, you would be able to do it exactly only if you knew what you were supposed to get.

**[1:11:55 – 1:11:59]** If you know where you're going, then yes, sure, you can reverse the process.

**[1:12:00 – 1:12:03]** Conditional on x0, conditional on the original image.

**[1:12:04 – 1:12:07]** But obviously, we want to apply it without the original image.

**[1:12:08 – 1:12:09]** We want to apply it as a generative model.

**[1:12:09 – 1:12:15]** We want to then, after training this chain, we want to start with just random noise

**[1:12:15 – 1:12:19]** and gradually turn it into something real.

**[1:12:20 – 1:12:22]** And it turns out you can still do that.

**[1:12:23 – 1:12:29]** So the forward chain is just a Gaussian.

**[1:12:29 – 1:12:32]** A backward chain is some very complicated distribution,

**[1:12:33 – 1:12:35]** but you can try to approximate it with a Gaussian.

**[1:12:36 – 1:12:40]** And then there is a lot of math, which I will skip.

**[1:12:40 – 1:12:47]** So we need to write down the forward diffusion chain formally.

**[1:12:47 – 1:12:51]** We need to compress to get closed-form formulas

**[1:12:51 – 1:12:57]** for getting to several steps ahead in the forward chain.

**[1:12:58 – 1:13:01]** And then we need to reverse this process,

**[1:13:01 – 1:13:04]** and then we need to derive formulas where we actually reverse it

**[1:13:04 – 1:13:07]** if we know where we are going.

**[1:13:07 – 1:13:11]** So like conditional on x0, everything is, well, maybe not easy,

**[1:13:11 – 1:13:12]** but everything is possible.

**[1:13:12 – 1:13:18]** You can actually do denoising perfectly and in closed analytic form

**[1:13:18 – 1:13:21]** if you know the result of the denoising.

**[1:13:22 – 1:13:32]** Yeah, but then you kind of do a big variational approximation

**[1:13:32 – 1:13:39]** that jointly approximates every step in this very long chain.

**[1:13:39 – 1:13:47]** And I know I cannot really explain it without going into a whole lecture on it,

**[1:13:47 – 1:13:52]** but ultimately we want to get to something like this.

**[1:13:52 – 1:13:55]** So we want to have our transformations.

**[1:13:56 – 1:13:59]** You will see that they have the theta over here.

**[1:13:59 – 1:14:04]** So now they are these parametric transformations modeled by neural networks probably.

**[1:14:04 – 1:14:10]** And we want it to be so that here as P of Xn,

**[1:14:11 – 1:14:15]** we can substitute something very simple like a standard Gaussian.

**[1:14:15 – 1:14:24]** And then after some denoising chain, we will get to a sample from this target distribution of cat pictures or whatever,

**[1:14:25 – 1:14:26]** to this very complicated distribution.

**[1:14:30 – 1:14:31]** So how do we do that?

**[1:14:32 – 1:14:32]** We approximate.

**[1:14:33 – 1:14:35]** Okay, let me skip this part.

**[1:14:35 – 1:14:36]** There is a lot.

**[1:14:36 – 1:14:40]** So again, it's the same idea of rational approximations,

**[1:14:40 – 1:14:43]** but applied in a quite more difficult way.

**[1:14:43 – 1:14:46]** But in the end, again, it works.

**[1:14:47 – 1:14:49]** So let me just say that it works.

**[1:14:50 – 1:14:55]** In the end, we get to a specific set of loss functions,

**[1:14:55 – 1:14:56]** well, actually a single loss function,

**[1:14:57 – 1:14:59]** which is a sum of multiple terms.

**[1:15:00 – 1:15:02]** And we can write down these terms.

**[1:15:02 – 1:15:04]** They are like pullback library divergences

**[1:15:04 – 1:15:06]** between the ausians or something.

**[1:15:07 – 1:15:11]** And yeah, and we can just take this loss function

**[1:15:11 – 1:15:15]** and optimize it, train it by gradient descent.

**[1:15:15 – 1:15:22]** And we can train these parameters of these distributions, right?

**[1:15:22 – 1:15:25]** So, okay, so this distribution, we don't train this one.

**[1:15:25 – 1:15:26]** This is just a standard Gaussian.

**[1:15:27 – 1:15:30]** But we train the parameters of this distribution.

**[1:15:30 – 1:15:32]** We train the parameters of the transformation

**[1:15:32 – 1:15:34]** that goes one step back.

**[1:15:36 – 1:15:38]** And when we train it, when it works,

**[1:15:38 – 1:15:40]** when it becomes a good approximation

**[1:15:40 – 1:15:42]** for the whole denoising chain,

**[1:15:42 – 1:15:45]** then you can apply it like this.

**[1:15:45 – 1:15:48]** You can start with pure random noise

**[1:15:48 – 1:15:52]** and gradually turn it into a good sample.

**[1:15:53 – 1:15:54]** And this is your generative model.

**[1:15:55 – 1:15:56]** This is how diffusion models

**[1:15:56 – 1:15:58]** actually produce their results.

**[1:16:01 – 1:16:04]** And in the original paper...

**[1:16:04 – 1:16:07]** So, okay, let's stop with the math now.

**[1:16:07 – 1:16:09]** In the original paper,

**[1:16:09 – 1:16:13]** it only worked for some really, really small dimensions.

**[1:16:13 – 1:16:15]** So like on CIFAR, it kind of worked.

**[1:16:16 – 1:16:19]** When anything larger, they didn't have the capabilities to train it.

**[1:16:20 – 1:16:24]** And for quite a while, this paper just was forgotten.

**[1:16:26 – 1:16:30]** Everybody kind of assumed that, yeah, it's a cool idea,

**[1:16:31 – 1:16:33]** but it's so, so difficult.

**[1:16:34 – 1:16:37]** And even if you succeeded in scaling it up,

**[1:16:37 – 1:16:41]** you would still probably would not be able to apply it

**[1:16:41 – 1:16:49]** because you need to actually apply this reverse chain,

**[1:16:50 – 1:16:54]** this one, you need to go through all the steps, okay?

**[1:16:54 – 1:16:56]** And if you need to go through all the steps,

**[1:16:57 – 1:17:01]** it means that you need to run your neural network hundreds of times

**[1:17:01 – 1:17:04]** because this chain, in order for the whole thing to work,

**[1:17:04 – 1:17:08]** for approximation to be feasible, this chain actually is pretty long.

**[1:17:08 – 1:17:12]** It's, in fact, on the order of hundreds of steps.

**[1:17:12 – 1:17:21]** So if you need hundreds of runs of your neural network to get one image,

**[1:17:21 – 1:17:24]** well, you don't really want to scale it up, right?

**[1:17:25 – 1:17:29]** It begins to sound quite infeasible, even if you succeed somehow.

**[1:17:30 – 1:17:33]** So people thought of it as a very interesting work,

**[1:17:33 – 1:17:36]** but ultimately just a curiosity.

**[1:17:37 – 1:17:40]** But then things started happening.

**[1:17:41 – 1:17:47]** It started in DDPMs in 2020, denoising diffusion probabilistic models.

**[1:17:48 – 1:17:55]** So I will not explain in detail what they did because these are just a collection of small tricks.

**[1:17:56 – 1:18:00]** But basically they kind of made it work.

**[1:18:00 – 1:18:07]** So DDPMs solved some of the other technical problems that diffusion models had

**[1:18:07 – 1:18:14]** and were able to achieve generation basically comparable,

**[1:18:14 – 1:18:17]** basically on par with the best GANs of the time.

**[1:18:18 – 1:18:26]** I showed you some sample generations from GANs yesterday.

**[1:18:26 – 1:18:36]** And back at the day they were very good in doing human faces like this

**[1:18:36 – 1:18:43]** and still quite poor in doing anything else because everything else was just too diverse.

**[1:18:43 – 1:18:47]** It was too... they couldn't capture the full diversity.

**[1:18:47 – 1:18:55]** So, for example, cat images from GANs would also look like this.

**[1:18:55 – 1:18:57]** And so this was actually a kind of state of the art.

**[1:18:57 – 1:19:02]** But DDPMs, even though they did excellent generation,

**[1:19:02 – 1:19:09]** they couldn't... they didn't solve this fundamental problem that I mentioned.

**[1:19:09 – 1:19:16]** They need to go through the chain hundreds of times to make hundreds of steps.

**[1:19:16 – 1:19:22]** So these were nice generations, but they were extremely slow.

**[1:19:22 – 1:19:25]** They took a lot of time to generate these spaces.

**[1:19:27 – 1:19:33]** But in that very year, they actually solved this problem.

**[1:19:33 – 1:19:37]** Well, not they, a different group, but this problem got solved.

**[1:19:37 – 1:19:43]** And again, I will skip the math, but I will just show you this basic idea.

**[1:19:45 – 1:19:54]** So the basic idea is to switch from approximating a step.

**[1:19:54 – 1:20:02]** So as the standard diffusion model or DDPM, you go from xt plus 1 to xt.

**[1:20:02 – 1:20:08]** And you approximate going from xt plus 1 to xt.

**[1:20:10 – 1:20:14]** And then you approximate going from xt to xt minus 1 and so on.

**[1:20:14 – 1:20:21]** So you actually need to make this step because if you don't make this step,

**[1:20:21 – 1:20:24]** you don't know where to start the next step from, right?

**[1:20:24 – 1:20:28]** So you actually need to go through all of the intermediate points.

**[1:20:28 – 1:20:35]** In DDPM, instead of trying to approximate the direction to the next point,

**[1:20:35 – 1:20:40]** we are always approximating the direction to the original x0.

**[1:20:40 – 1:20:45]** x0 lies in the same space, it's just kind of far away.

**[1:20:45 – 1:20:51]** And we have this long path that gets us from x capital T to x0.

**[1:20:51 – 1:20:57]** And in DDPM, we approximate step by step.

**[1:20:57 – 1:21:03]** In DDIM, on every time slot, on every step of the Markov chain,

**[1:21:03 – 1:21:07]** we approximate this whole, this direction right to the goal.

**[1:21:07 – 1:21:12]** And of course, it doesn't mean that we can just go to the goal in one step.

**[1:21:12 – 1:21:14]** No, that doesn't work.

**[1:21:14 – 1:21:16]** Our approximation is not that good.

**[1:21:16 – 1:21:21]** We cannot just jump immediately to a good picture, what's going to happen.

**[1:21:21 – 1:21:24]** But we can go quite a bit further.

**[1:21:24 – 1:21:27]** So like instead of...

**[1:21:27 – 1:21:33]** So in DDPM, we cannot skip steps because if we skip a step,

**[1:21:33 – 1:21:35]** we don't know where to begin the next one.

**[1:21:35 – 1:21:42]** In DDIM, I can say, okay, so I'm supposed to get closer to x0 on every step.

**[1:21:42 – 1:21:47]** And then, yes, it's an approximation, but I know that on the next step,

**[1:21:47 – 1:21:50]** I will also be trying to get closer to x0.

**[1:21:50 – 1:22:00]** So even if my original chain had hundreds and hundreds and thousands of steps,

**[1:22:00 – 1:22:07]** here I will go in the general direction of x0 just faster.

**[1:22:07 – 1:22:11]** I will just take wider steps.

**[1:22:11 – 1:22:15]** So, and that will not be a problem.

**[1:22:15 – 1:22:22]** I will not lose where I am, lose track of where I am, because wherever I am,

**[1:22:22 – 1:22:28]** my next approximation, my next step will be, well, trying to go to x0.

**[1:22:28 – 1:22:32]** So I will not be able to jump all the way there in one step.

**[1:22:32 – 1:22:35]** My approximation will not work like that.

**[1:22:35 – 1:22:41]** But I will be able to get there in a few dozen steps instead of a few thousand.

**[1:22:41 – 1:22:52]** So DDIMs did like 10 or 100x speedup compared to the original diffusion models

**[1:22:52 – 1:22:56]** with no loss of quality, not much improvement on quality either,

**[1:22:56 – 1:22:58]** but that was good enough.

**[1:22:58 – 1:23:05]** And that's where diffusion models actually started working, right?

**[1:23:05 – 1:23:09]** But it was still slow.

**[1:23:09 – 1:23:12]** It was still expensive.

**[1:23:12 – 1:23:16]** And there was this one last step that people actually needed to do

**[1:23:16 – 1:23:21]** before diffusion models started working completely like they work now.

**[1:23:23 – 1:23:27]** And that last step, I actually already mentioned to you,

**[1:23:27 – 1:23:37]** that last step was to do the diffusion not in the space of pixels like those papers did,

**[1:23:37 – 1:23:41]** but in the latent space of some autoencoder.

**[1:23:41 – 1:23:48]** So here is this very famous picture from the paper on stable diffusion.

**[1:23:48 – 1:23:50]** You probably have heard of stable diffusion.

**[1:23:50 – 1:23:56]** It's like the original actually working text-to-image diffusion model, right?

**[1:23:58 – 1:24:07]** It was done in 2022, so not that long ago.

**[1:24:07 – 1:24:11]** Naturally, AI image generation has come a long way since then,

**[1:24:11 – 1:24:15]** but the basic idea still is basically the same.

**[1:24:15 – 1:24:20]** And stable diffusion works like this.

**[1:24:20 – 1:24:22]** It has a diffusion process.

**[1:24:22 – 1:24:25]** It has a denoising architecture here.

**[1:24:25 – 1:24:28]** So it has a diffusion model.

**[1:24:28 – 1:24:34]** And as you can see here, we start with ZKey and we go through a network.

**[1:24:34 – 1:24:42]** This network is some kind of self-attention based unit or whatever.

**[1:24:42 – 1:24:47]** Let's not dwell on the specific architecture.

**[1:24:47 – 1:24:48]** It doesn't really matter.

**[1:24:48 – 1:24:54]** What matters is that, first, this architecture can take a condition.

**[1:24:54 – 1:24:59]** And this condition will be, for example, the prompt.

**[1:24:59 – 1:25:05]** So we need to somehow inform the model what we are trying to draw.

**[1:25:05 – 1:25:07]** This text should go somewhere.

**[1:25:07 – 1:25:09]** And where does it go?

**[1:25:09 – 1:25:13]** Well, the text gets encoded into a vector by some transformer.

**[1:25:13 – 1:25:22]** And then this vector goes into, well, in this case, into self-attention blocks,

**[1:25:22 – 1:25:26]** like we discussed a couple of lectures back with encoder-decoder attention.

**[1:25:26 – 1:25:28]** But it could be a different architecture or whatever.

**[1:25:28 – 1:25:31]** It goes into every denoising step.

**[1:25:31 – 1:25:43]** So every denoising step has this conditional thing, has this another input that comes from the problem.

**[1:25:43 – 1:25:54]** And the most, of course, important novelty here is that all of this happens in the latent space.

**[1:25:54 – 1:26:01]** So all of this happens in the space of vector representations of images,

**[1:26:01 – 1:26:06]** not images themselves, not pixels, vector representations.

**[1:26:06 – 1:26:11]** After this denoising process, we start with random noise, we add this condition,

**[1:26:11 – 1:26:14]** we go through many steps of denoising.

**[1:26:14 – 1:26:23]** What we get is not an image, but a code that will then be decoded by the decoder.

**[1:26:23 – 1:26:28]** And this guy here, the red part, is a variational latent coder.

**[1:26:28 – 1:26:33]** Well, a complicated modern variational latent coder, not quite exactly the one I explained to you,

**[1:26:33 – 1:26:36]** but a variational latent coder.

**[1:26:36 – 1:26:41]** And that's how it works.

**[1:26:41 – 1:26:50]** Another similar thing was done in DALI 2.

**[1:26:50 – 1:26:59]** DALI 2 worked a little bit differently because it used pre-trained clip embeddings.

**[1:26:59 – 1:27:07]** We did not have time to talk about clip and unsupervised learning and contrastive learning in our class.

**[1:27:07 – 1:27:14]** But clip is this standard way of doing joint text image embeddings.

**[1:27:14 – 1:27:21]** So it's like a joint latent space for where both images and text can go.

**[1:27:21 – 1:27:43]** And the idea of DALI 2, for example, was let's put the text into this space and let's train--now clip doesn't include this--but let's train a decoder that will produce an image back from the clip representation.

**[1:27:43 – 1:27:55]** And also let's train a diffusion model inside the latent space that will convert the representation of text into the representation of this image from the decoder.

**[1:27:55 – 1:28:02]** So again, no details here, but you get the idea that diffusion is still happening in the latent space.

**[1:28:02 – 1:28:04]** And DALI 2 was pretty good.

**[1:28:04 – 1:28:13]** Okay, now we would laugh at these images, but in 2022 this was completely awe-inspiring.

**[1:28:13 – 1:28:21]** And this is a very famous image from the original mid-journey that won some contest.

**[1:28:21 – 1:28:31]** And then it was revealed that it's AI-generated and there was this big controversy, the first controversy of this kind.

**[1:28:31 – 1:28:37]** Now, of course, these controversies are everywhere.

**[1:28:37 – 1:28:44]** The next step was to do what was called the Diffusion Transformer, DIT.

**[1:28:44 – 1:28:49]** And I don't have time to explain it in detail.

**[1:28:49 – 1:29:00]** Basically, it's the same kind of latent diffusion model, but now they use a full transformer instead of a unit with some self-attention inside.

**[1:29:00 – 1:29:04]** So the difference is in the internal architecture, not in the approach.

**[1:29:04 – 1:29:09]** The approach is basically the same. You do diffusion in the latent space of some autoencoder.

**[1:29:09 – 1:29:21]** And DITs were good, blah, blah, blah. And these were the samples from the DIT of 2022, already starting to look pretty good.

**[1:29:21 – 1:29:30]** Then there was this flux model. I think it's the last one that I really followed because...

**[1:29:30 – 1:29:35]** So again, I don't have time to explain this picture in detail, but it's also...

**[1:29:35 – 1:29:41]** It's the direct successor of stable diffusion. It was done by the same team.

**[1:29:41 – 1:29:50]** And it was actually very good when it was released.

**[1:29:50 – 1:29:53]** I think obviously you can still download and use it.

**[1:29:53 – 1:29:59]** I'm not sure if it's the best local model right now, but for a long time it definitely was.

**[1:29:59 – 1:30:09]** And yeah, I used to use flux for images for my slides for a very long time.

**[1:30:09 – 1:30:14]** This is all flux generated. It couldn't do text.

**[1:30:14 – 1:30:21]** It wasn't too good with following detailed prompts on composition and stuff that the characters do, etc.

**[1:30:21 – 1:30:26]** But it was like this huge step forward.

**[1:30:26 – 1:30:32]** And yeah, this is also flux, all this bias, etc.

**[1:30:32 – 1:30:42]** And unfortunately after that, it's not like I wanted to stop following.

**[1:30:42 – 1:30:46]** But I lost the ability to follow state-of-the-art text-to-image models

**[1:30:46 – 1:30:54]** because now the best models are basically just GPT, right?

**[1:30:54 – 1:30:58]** GPT or Gemini, they sometimes switch around.

**[1:30:58 – 1:31:00]** For a while, Gemini was better.

**[1:31:00 – 1:31:04]** Now I think GPT Images 2 is again the best.

**[1:31:04 – 1:31:08]** And of course nobody tells us exactly how they work.

**[1:31:08 – 1:31:14]** So right now I have no idea how the best image generation models work.

**[1:31:14 – 1:31:18]** Not because I don't want to know, but because nobody tells us.

**[1:31:18 – 1:31:21]** And MidJourney is still, I guess, competitive.

**[1:31:21 – 1:31:23]** And it was closed from the very beginning,

**[1:31:23 – 1:31:27]** so I don't even know exactly how it worked back then.

**[1:31:27 – 1:31:29]** Probably approximately the same.

**[1:31:29 – 1:31:36]** But still, image generation nowadays is done by diffusion models,

**[1:31:36 – 1:31:44]** most probably operating in the latent space of some big autoencoder.

**[1:31:44 – 1:31:47]** Yeah, so let me skip this.

**[1:31:47 – 1:31:55]** Yeah, and maybe to conclude this part of the class

**[1:31:55 – 1:31:59]** and the whole class, actually, all of the lectures,

**[1:31:59 – 1:32:01]** let me go back to this picture

**[1:32:01 – 1:32:08]** and kind of put all the generative models in place on this picture.

**[1:32:08 – 1:32:13]** I guess I already talked through it, but let's spend another minute.

**[1:32:13 – 1:32:20]** So generative models, they are divided, first of all,

**[1:32:20 – 1:32:23]** into explicit and implicit density models.

**[1:32:23 – 1:32:28]** And basically generative stochastic networks didn't take off.

**[1:32:28 – 1:32:36]** So the only relevant representative of the implicit density class is GANs.

**[1:32:36 – 1:32:41]** And GANs are still relevant, only they are a bit more niche now,

**[1:32:41 – 1:32:44]** a bit more specialized than they used to be.

**[1:32:44 – 1:32:49]** In explicit density models, you have this huge class of autoregressive models.

**[1:32:49 – 1:32:55]** Autoregressive models like WaveNet for producing sound.

**[1:32:55 – 1:32:58]** Autoregressive models like language models.

**[1:32:58 – 1:33:02]** Like all of the LLMs, they all are in here.

**[1:33:02 – 1:33:10]** Because the transformer decoder produces tokens one by one, autoregressively.

**[1:33:10 – 1:33:13]** Conditional on the prefix that it has already generated.

**[1:33:13 – 1:33:19]** Or you can have flow-based models where you start with a simple distribution

**[1:33:19 – 1:33:25]** and you gradually transform it into something more complicated.

**[1:33:25 – 1:33:34]** Or you can have approximate density models where you do not make assumptions about your distribution,

**[1:33:34 – 1:33:38]** but you make assumptions about an approximation to the distribution.

**[1:33:38 – 1:33:43]** And it wasn't clear what it means when I first talked to you about this,

**[1:33:43 – 1:33:45]** but I hope today it has become clear.

**[1:33:45 – 1:33:52]** So there are two main representatives here.

**[1:33:52 – 1:34:01]** The Ys, the Variational Autoencoders, they actually embody this.

**[1:34:01 – 1:34:07]** So we do not make assumptions on p of z given x.

**[1:34:07 – 1:34:11]** We approximate it, and then we make assumptions on the approximation.

**[1:34:11 – 1:34:14]** And how does it work? Through the variational order.

**[1:34:14 – 1:34:17]** And the same goes for diffusion models.

**[1:34:17 – 1:34:22]** Again, we cannot make strong assumptions about the reverse chain,

**[1:34:22 – 1:34:23]** about this denoising chain.

**[1:34:23 – 1:34:28]** What we can do is we can make strong assumptions

**[1:34:28 – 1:34:32]** about an approximation to the reverse chain and then do a variational order.

**[1:34:32 – 1:34:41]** So same approach, the diffusion approach is just a bit more complicated.

**[1:34:41 – 1:34:43]** And basically that's it.

**[1:34:43 – 1:34:48]** So all of the stuff that you hear about in the news is somewhere in this picture

**[1:34:48 – 1:34:52]** and most probably either here in the autoregressive models

**[1:34:52 – 1:34:56]** or here in bias and diffusion.

**[1:34:56 – 1:35:06]** And I guess with that, I want to close our lectures.

**[1:35:06 – 1:35:12]** We have come a long way from the bias theorem back to the bias theorem today.

**[1:35:12 – 1:35:19]** And from the original motivation of neural networks and backpropagation,

**[1:35:19 – 1:35:24]** we got to transformers, we got to variational autoencoders,

**[1:35:24 – 1:35:26]** we got to diffusion models.

**[1:35:26 – 1:35:29]** I think it has been a long journey.

**[1:35:29 – 1:35:31]** I hope it has been an interesting one.

**[1:35:31 – 1:35:33]** And thank you. Any questions?

**[1:35:33 – 1:35:40]** Thank you so much.

**[1:35:40 – 1:35:42]** All right. So thank you very much.

**[1:35:42 – 1:35:46]** I hope we will see each other on Friday still.

**[1:35:46 – 1:35:48]** But the lectures are over.

**[1:35:48 – 1:35:50]** Thank you. Bye-bye.

## Full text

Okay. Hello everyone. And welcome to the last lecture of our class. It has been, I think it actually has been quite a long journey through our lectures. I think we've covered quite a lot of ground. We actually didn't quite get to the computer vision itself. We only had one lecture on object detection. I skipped segmentation entirely, but generative models seem like important ideas too. And usually I choose one or the other. In this case, it's generative models. And they also are a great teaching tool, in my opinion, because they show some ideas in relatively simple form that go through the whole of machine learning. And today in our last lecture, actually, I'm going to tell you one of these wonderful basic ideas. Maybe you have heard about it in some previous classes, but to be honest, I sincerely doubt that somehow in harborspace, people usually don't teach that stuff unless I do. So today we mostly talk about variational autoencoders, and therefore we talk about variational approximations, which, again, in the variational autoencoder, the variational approximation appears in its very simplest form and already in a very useful form. So I think it's perfect for teaching it. And then whatever time we have left, I hope we will have some time left, I will walk you through diffusion models. There, there is a lot of very complicated math, which we definitely won't have time for, but again, the basic ideas are kind of easy to show. So, let's start with the motivation and let's start with the basic idea of the variational autoencoder. I started talking about the motivation of YS yesterday when I explained to you this basic problem of why can't we have a generative model from an autoencoder. I hope you remember. So, we have this X which is a picture or something, some complicated thing. Then we pass it through the encoder. We get, in the regular autoencoder, we get like a latent code Z. And Z is relatively small compared to X. And then there is the decoding part, the decoder, that is supposed to recover, reconstruct the original X. Right? This is the very basic structure of an autoencoder. And you can train it very straightforwardly. There is no problem in thinking of good loss functions here. So you just want your X and X hat to be similar to each other. What is usually called the reconstruction loss. And the reconstruction loss basically can be anything. It can be just the L2 norm. It can be something like perception loss. I'm not sure if Alex talked to you about that. But like the similarity between some local features extracted by a couple of layers of a standard feature extractor and so on and so forth. So you can think of what you want, how you would like to define what it means to be similar, and you just optimize it. And the beauty of autoencoders is that you don't need any label training data, right? Your dataset can be just a set of axes and you automatically get labeled samples because you just need to reconstruct the same axis. So the big question is why can't we use the blue part? I intentionally made it in a different color. Why can't we use the blue part as a generative model? And yesterday I told you why, right? We can't use it as a generative model because even though in the latent space, these live in a much simpler, much more structured, so to speak, manifold than they do in the space of x, which is huge and very, very complicated, they still do not cover the whole space of z. The space of z is still pretty complex and we still need to do something because if we just take a random point here in the latent space z, of course it will not fall onto this manifold of actual latent codes for good cat pictures. So yesterday I told you one way to try to fix that and that way was to have a discriminator here. Right? We discussed adversarial lotto encoders where you would try to distinguish fake z from so-to-speak real z's that are sampled from a Gaussian or something or whatever distribution you want. And in that way you can apply adversarial learning, you can apply the basic GAN idea to try to regularize, to try to fix this latent space, to try to fix this manifold of latent codes. And that was called the adversarial autoencoder. So today we discussed a different approach to the same problem and this approach to the same problem is actually better. I mean at some point there was a competition between adversarial autoencoders and variational autoencoders but by now with some recent innovations and so on, variational autoencoders were just better and they formed the basis for a lot of what's happening in generative modeling, in particular for the diffusion models that we will discuss later. What is the variational approach? What is the approach from the variational autoencoder? Well, the idea is as follows: you again have the same kind of encoder-decoder construction. X-head. You still have the same autoencoder with some reconstruction losses or whatever, but now you do the following: you say, well, what is the problem with the latent space here? What is the core of the problem of why these are so hard to actually get? Why we cannot get to Zs with random sampling or something? And one answer to that is because every X from the training set corresponds to just one point Z. And that kind of leads to almost automatic overfitting in the space of latent codes. So we are training on a data set. Yes, it may be a huge data set, but every point corresponds to just one Z. And if you shift your Z a little bit, well, you've fallen off the manifold of good latent codes and nothing works anymore, right? And when you're sampling, of course, you don't know which directions are good, which directions are bad. And of course, you're very likely to follow the manifold. So the approach of the variational autoencoder is to say the following. Now, instead of having just one latent code, let's instead make the encoder output a whole distribution of these, like p of z given x. So now when I have like a cat picture over here, it maps in the latent space, not to a single point, but it maps to something like a Gaussian. It maps to a whole distribution of latent codes. And then if I have a different cat picture, it maps to a different distribution of latent codes. And then I would like to sample from this distribution. So I would like to pick a point out of, say, the orange distribution, and still reconstruct the same orange cat. And if I pick a point from this distribution, I would like to still reconstruct the same green cat. So the encoder will give me the distribution. Actually, in the form of parameters, I will show you in a sec. And then I sample from it, and I'm supposed to get, again, X hat, which is supposed to be similar to X, again with the reconstruction loss. So in this way, I will be able to try to cover the whole latent space, or at least some reasonable portion of the latent space with these distributions. So in fact, it's going to work like that, and usually it works like this. These distributions are Gaussians, they are just normal distributions, and the encoder gives you their parameters, like mu of X and sigma of X. And sigma is a vector usually just for simplicity, so it should be a covariance matrix. Of course, it's all multidimensional distributions, but basically I'm talking about a diagonal matrix, diagonal covariance matrix here. And then from these two parameters, I construct the Gaussian, and I sample Z from it, and then it goes to the decoder, and I get X hat. So I fix the Gaussian shape, but I'm basically saying that, well, the parameters of this Gaussian, the variances and the means are determined by the encoder, and I will train it to be as best as I can. Well, the natural question and the obvious problem here is that why would the encoder actually want to produce any kind of reasonable distribution? Because of course solving this problem with a single point is much, much easier for the model, right? So here it's supposed to reconstruct the same cat from a whole neighborhood of points in this high dimensional space, not just from a single point. It's strictly more difficult, right? It's strictly harder. At the same time, since the encoder controls the variances, naturally it can just send the variance to zero, right? It can just say, well, yeah, I know I'm supposed to do a Gaussian, but what if I just fake a Gaussian and say that, okay, here is my Gaussian, just has very small variance. That's exactly what's going to happen in practice, unless you regularize somehow. So another important component here is that we need some kind of regularization on the distribution parameters. And in this case also, we need to take this mu and sigma, and we need to do regularization on them. We need to make sure that sigma doesn't just uncontrollably goes to zero. And on the other hand, that mu doesn't uncontrollably go to infinity, because another way to make this problem very, very easy would be to say, "Okay, so I can't make the variance too small. All right, let me fix the variance to be one, but let's just drive these points away from each other so that nothing ever overlaps and everything is completely different." And for me as the encoder, it just means rescaling of the space and I am still basically in the same situation of having individual points. So that also will definitely happen in practice unless you regularize. So we need to have some kind of regularization for this and actually the regularization is very simple. It says that our distribution should be similar to just the standard normal distribution, right, with min zero and unit covariance matrix. So this is the idea of the Variational Autoencoder, but there are some problems and unclear things here. So one problem, one thing that always kind of appears in deep learning and in machine learning in general is that you often kind of know what you want, right? So let me actually draw the reconstruction loss. You know, in principle, what you want. Like I want to have a reconstruction loss that says that x index hat are similar, or I want to have a regularizer that says that mu is kind of like not very far from zero and sigma is kind of like not very close to zero. But how do I formalize this? So this is question number one. How do I formalize this? What would different reconstruction losses mean? What would it mean for these two distributions to be close to each other? Or better to say, I know quite a lot of ways to say that they are close to each other. Which of them should I choose? Which reconstruction loss should I choose? Right? There's always a question like this. But in this case, there's also a special question, a question special for this architecture. And this is the question of how do I do that? How do I insert a sampling procedure into a deep neural network? And it sounds very simple, right? The encoder is a neural network. It has two vectors as outputs. One vector is mu. The other is sigma. Then you just sample. And in the forward propagation, in the forward pass, it is very simple. You just sample from the Gaussian. You know how to do that. But what do we do with the backward pass? How does gradient go through a sampling procedure? Well, obviously it doesn't. And that is a big problem. And we need to somehow solve this problem, right? So let's tackle these problems. And talking about them actually gives us the ideas that I advertised in the very beginning, these very basic ideas that go through the whole machine learning. So let's do like via formally, so to speak. And the formal approach here, and for now I will be concentrating on the first problem, like where do the loss functions come from. But to actually talk about this and to actually see where those functions come from, I need to start a little bit further back. So let's look at what kind of variables, not parameters, but variables appear in our model. Our model has basically two variables, x, which is the thing, the image, whatever you are encoding, and z, the latent code. So two variables in the model. And what basically every machine learning model does, like we discussed in the very beginning of our class, it takes this joint distribution p of x, z and decomposes it somehow, and then makes some assumptions and so on, right? So here, p of x, z doesn't look very difficult. There's not too many different ways how you can decompose it. So let's write both of these ways, right? You can start with x and say it's p of x times p of z given x. Or you can start with z and you can say it's p of z times p of, sorry, x given z, right? These are the two possible decompositions unless we go inside x in the end. Right now we don't want it. And if you look at this very simple formula, like, you know, this full probability formula, whatever, definition of conditional probability, you see all of the components of our neural network. It's actually pretty straightforward and beautiful. So what are the components here? Well, what is p of z given x? p of z given x is this distribution. It's the encoder distribution. It's what the encoder produces. Let me call it the encoder, so to say, right? Where is the decoder distribution? Well, the decoder takes z as input and outputs x hat, and it doesn't output the exact x, it outputs an approximation to x. So again, like in linear regression, or like in any machine learning model, in actuality, the decoder produces some noise distribution around x. So actually, this is the decoder, right? What is P of x? Well, P of x is the global distribution of CAD pictures, right? So P of x is that extremely difficult, complicated thing that we have no ability to comprehend. And what is P of z? Well, P of z is the prior distribution, right, without any x, the prior distribution on the latent codes. So what we would like P of z to be is some simple distribution that we can sample from, because this whole thing is our regeneration process, right? How do we produce a new CAD picture? We sample z, and then we run it through the decoder. We sample z, and then we plug it into P of x given z, and basically sample x. So in order for that to work, we need P of z to be simple, right? Well, here is the catch. Notice that I haven't done basically anything. I wrote the most trivial formula of the whole probability theory. But we can already make some conclusions. So our first conclusion is this. Well, what are these decoder and encoder distributions? Well, the decoder and encoder distributions are... Well, the decoder distribution is the distribution of noise at the output, and it will be captured in the reconstruction loss. We'll see it a little bit later. And the encoder distribution is, well, something that I'm supposed to sample this Z of X from. So basically, it's like the true version of this Gaussian. And I would, of course, be very happy to say that, well, let's assume that the decoder has Gaussian noise. Let's assume that the encoder produces a Gaussian. Let's plug it in and let's do the math and we will, I don't know, learn some parameters. Unfortunately, even without going any further, we see here that it doesn't work. Why doesn't it work? Because I need P of Z to be simple, right? So actually, P of Z in the classical variational-to-encoder will be just a standard Gaussian. And we pick P of Z, right? It's our choice. So P of Z is simple. If the decoder is also simple, and it will be, if the decoder is also a Gaussian, let's say. So it's a Gaussian with the mean specified by the decoder and some Gaussian noise around this output. So our assumption is that we want to reconstruct the original X, but of course we cannot do it perfectly. So actually X is near the result of the decoder, but with some noise, right? Just like in linear regression, we are supposed to recover the points, but we cannot do it perfectly. So we say that the points are around our straight line, but with some noise. Exactly the same. So here it would also be natural to assume some kind of simple noise like a Gaussian noise. Otherwise, we wouldn't know what to do with it. So here, this is also a simple distribution. But now, if I take the product of two Gaussians, it's going to be a Gaussian. It's going to be simple. And this guy over here is this incredibly complicated distribution in this huge dimensional space. There is no way that I can assume that cat pictures form a Gaussian. That doesn't work. The whole point of our model is to somehow, you know, streamline and simplify this impossibly complicated distribution. So notice how just this simple equality already tells us that we cannot assume both the decoder and the encoder to be easy. Because if I now write the encoder also to be a Gaussian, this equality will never happen, right? The encoder, if I want to have two simple things on the left, it means that the encoder will have to be something very complicated. Because it will have to kind of cancel out with this and give you a ghost. So this is going to be, okay, let me just leave it as P of Z given X, okay? So I cannot really assume both the decoder and the encoder to be simple. I can choose. I could assume the encoder to be simple, then the decoder would be difficult. But I want to keep the decoder easier. That is a more natural choice to have the Gaussian noise at the output, as you will see. But this means that the encoder cannot really be simple. And the point of the variational autoencoder, why it's called the variational autoencoder, is because we take this p of z given x and we approximate it by, sorry, q of z, by a simple distribution q of z. And this will be our Gaussian. So the whole point of the variational autoencoder is to say, yeah, the encoder will produce Gaussian, the parameters for a Gaussian. But I know from the very beginning that this is not the true distribution p of z given x. This cannot happen. I don't know it. It's very complicated. This is an approximation to p of z given x. And the question is, how do I make this approximation? And here we come to this promised very important idea, one of the most basic ideas in machine learning, one that underlies millions and millions of different models and that appears all through our field. And that's the idea of variational approximations. So let me explain it to you from the very beginning. So here I've motivated that we need an approximation, right? And now let me explain to you how approximations work. So again, let me start from scratch. Again, I start with a very simple formula and I will be doing some simple but kind of non-obvious transformations. Non-obvious in the sense that they will be easier, but you will wonder why on earth am I doing that? That's okay. Just trust me. It will take three or four lines and then you will see why we needed all that. So we begin with the obvious identity and say, okay, let me write it with logs. Log P of X, Z. Now I need to start with the right variable. Yeah, I need P of X and P of Z given X, right? So this is obviously true. This is just this very same identity. And it contains the joint distribution and it contains this difficult, complicated distribution that I want to approximate. It doesn't have any Q yet. So first I take the logs and I put P of X on one side and the rest on the other side. So log P of X. Again, so far nothing is happening at all. Log P of X, Z minus log P of Z given X. Now I make the first tricky step, which is I take the expectation. So this is just an identity. It's always true. Now I take the expectation with respect to Q of Z, where Q is any distribution at this point, on the left and on the right. So I take the expectation on both sides of the equality. Obviously, it still remains in equality, but notice that I take the expectation with respect to Z, and here there is no Z. So log P of X is a constant with respect to Z. So on the left, nothing changes. Log P of X just remains a constant. And on the right, I have this expectation of log P of X Z minus log P of Z given X. OK, and now the final non-trivial step. I add and subtract the expectation of log Q. So like the entropy of the distribution Q. Again, at this point, you probably don't understand why I'm doing this. This will become clear in a couple of ways. So I add and subtract expectation of log Q. Again, this obviously doesn't change the identity. So what do I get now? Now I want to take the minus from here and put it together with this log. And I want to take the plus from here and put it together with this log. So my final formula is this. Log P of X is the expectation of log P of XZ divided by P of Z. I put this log together with this. Minus or do I want plus? Yeah, I think I want plus. So plus expectation of Q of Z log Q of Z divided by log P of Z given X. Okay, so far so good. I hope it hasn't been a problem for you to follow. I have just been writing some basic algebra and basic probability theory, not even probability theory, just put the expectation on top. Nothing has been happening, right? It's just a string of obvious identities. It's just not clear what this leads to. But we are already done. So this is the main formula of variational approximations. And here is how it works. Here is what it actually means. On the left, you have a constant, right? Now let's look at this as kind of from the point of view of our problem. So this is just an identity. It holds always for any p of x, z and any q of z. This is just always true. But let's look at it from our point of view. And our point of view is I want to find q of z. That would be a good approximation for p of z given x. So in a way, I want to be optimizing something. Don't yet know what. With respect to q of z, right? So let's view this as a functional, as a dependence on q of z. So on the left, I don't have q of z. On the left, it's just a global constant, the likelihood of the data set. On the right, I have this guy. Let's call it L of q. Some, I don't know, this cursive L of q. Plus, and here is the most beautiful part. What is this guy? What is the second term here? It's the Kuhlbach-Leibler divergence between q of z and log, sorry, not log, just p, p of z given x, right? I hope you know what Kuhlbach-Leibler divergence is. If not, it's a common metric that shows how similar two distributions are. So I think I introduced it at some point, right? So Kuhlbach from Q to P is integral Q times log Q divided by P dx. So this is exactly this, right? And here we get a thing that shows how close Q of z is to the distribution that we want to approximate, right? So basically, this is a great optimization target. I want to minimize it with respect to Q, okay? And I could just start with it. I didn't need all of these formulas to know that I want to minimize KL from Q to P. But P is a very complicated distribution. It's very hard to work with P of z given x. Because this P of z given x, I mean, in a standard machine learning application of rational approximations, it would be some complicated posterior of a huge probabilistic model with lots of hidden variables that we need to integrate over. And it would be very unclear what it is. And here, too, P of z given x is this strange, complicated distribution that you need to multiply this distribution of cat photos by to get a simple Gaussian. Who knows what it looks like? How can we evaluate it? How can we work with it? No idea. And the whole point of this simple formulas was to say that instead of working with this P of z directly, I can just say that, look, I have the sum of two terms, and together they make up a constant which is independent of Q. So, if I want to make this guy smaller with respect to Q, it's exactly equivalent to making this guy larger with respect to Q, right? Because they should sum up to a constant. So, if there is this constant, it consists of two components, and I want to make one component smaller, which means that the other is larger. And vice versa, if I make the other one larger, it means I make the first one smaller. So, minimizing the KL divergence, the Kluber-Klider divergence from Q to P, to P of Z given X, to our posterior, to what we are interested in, is equivalent to maximizing this beautiful thing. And it doesn't sound like much of a result yet, but if you look at this, so this L is called the variational lower bound, or evidence lower bound, ELBO, sometimes you see an acronym. So, this L of Q is a lower bound to a constant that you want to maximize, right? And if you look at what it actually is, this L of Q, it's this, let's say, integral, okay, let me rewrite the expectation as an integral, doesn't matter, just to show you the formula both ways. Log P of xz divided by Q of z dz, right? So it's like, let me open the logs back, dz minus P of z log P of xz dz, something like that. And if you look at it, you see that now all that it involves are, well, first the distribution that we are optimizing Q, and second, it involves the join distribution, P of xz. And this is a huge difference. So usually in machine learning, basically always in machine learning, when you define your model, if you know all of the variables, like usually this is applied for probabilistic models, where x are the visible variables, the observables, and z are the hidden variables. So if you know both observable and hidden variables, then everything is easy. The distribution, all the distributions decompose, P of xz is probably very simple. It's big, but it's simple. But if you need to do something like this, now it's very complicated. Or if you need to do something like this, for example, to integrate over all these, it's also very complicated. But the joint distribution is probably very simple. Otherwise, you don't have a good model. So the whole point of rational approximations is to switch from working with a very difficult distribution, very complicated distribution that you can't work with, to working with a simple distribution that you can work with. And so getting back to the variational autoencoder, in our variational autoencoder, this is really obvious and it's shown in a very clear form. So what is this p of z given x? It's something very, very complicated that we have no idea how to handle. But what is p of x and z? What is the join distribution? Well, it's a product of two Gaussians. There we go. So to make it easier, we just need to decompose it in a different way. So let's just look at it as log p of z plus log p of x given z and not the other way around. Not in this decomposition. So this idea is the variational approximation and basically how it is used in practice, like how you would actually use it is you go through this math, you have to go through this math. Well, this math is always the same, but then you need to substitute your specific distributions, your specific model, and it gives you those functions. So, let's see how it goes with the variational attaincoder. Let me continue this equality. So, I plug in this decomposition, and I get something like expectation P of Z log P of X given Z, right? Plus expectation log P of Z, that's the first term, minus expectation log Q of Z, right? And let me put together the second and third term, so that again it will be more clear what's happening. Minus expectation log Q of Z divided by P of Z, okay? So, what is this guy over here? Well, this guy over here is the chi-L divergence between Q of Z and P of Z, right? So Q of Z is our distribution that will be an approximation over here. So this guy is Q of Z. And P of Z is this orange guy, is the simple distribution that I want to sample from. So basically, this says that my distribution Q, okay, let me actually write it, my Gaussian distribution with some parameters mu X and sigma X should be close to a standard Gaussian. P of Z is this simple Gaussian that I want to sample from. And this is exactly the regularizer. So this is the part of the loss which is the regularizer. Again, notice how it is kind of at the same time, just like we discussed, but also more precise. So I told you that, well, probably I will need to regularize this, otherwise bad stuff will happen. And, you know, the distributions in the latent space will float away from each other and they will become smaller. Variance will go to zero, blah, blah, blah, you probably need to regularize. But how? What should be the form of the regularizer? We honestly had no idea, but after this little bit of math, now we see an exact formula. I will not go through the details, but you can just write it down and you will see like an exact formula, a function of mu and sigma that you can just plug into PyTorch, right? So, and you wouldn't be able to arrive at this formula in any other way. Somehow you need to understand that your regularizer should be specifically this value. And where do you get it from? Well, you get it from the variational approximation, at least I don't know any other way. So, yeah, it seems very natural, but if you are looking at the problem from here, then it seems just as natural as any other thing. You could have just said, oh, okay, so let me put the Gaussian on mu and some gamma distribution on sigma or whatever, right? You could have chosen this regularizer, but it would be just one of very many ideas. And here we see why we choose this idea. So the variational approximation gives you the loss functions, and this is basically all you need, right? And what is the first part? What is this guy? Well, yeah, let's make it purple because the decoder was purple, and this is about the decoder. So what is this log P given C? It's the decoder distribution, right? So it's the expectation of the log of this Gaussian, of this Gaussian over here, right? Of the Gaussian of X around the result of the decoder with some noise, right? And then you can just open the brackets in the sense you can just plug in what the density of the normal distribution, take the log, and again, I won't bore you with the full derivation, but we kind of know what's going to happen. We know the density of the normal distribution, right? So it's like some constant, maybe complicated, but still, minus 1 over 2c to the power d or something times, what, times x minus the result of the decoder squared, right? That's the exponent of the normal distribution. So this is basically a constant, which I don't care about, minus some other constant, which I don't know, I don't care about, times the expectation of the least squares loss between x and the decoder result, right? So this, actually, is the part which is the reconstruction loss. The expectation over Q basically just means that I take the average over the training data. In practice, it just means averaging over the dataset. We approximate this expectation with the average over the dataset. So it's like the actual loss is something like one over n times the sum xn minus the decoder of zn. And zn actually comes from where does this come from? It comes from the encoder of xn, something like this, right? So what have we done? I didn't go through all the math in detail, but I hope the ideas are already here. I hope that they are clear to you. What have we done? We started with this very basic decomposition, which is not much of an idea, to be honest. We applied the variational approximation, and as a result, we see that our variational lower bound, our L is minus some constant, minus some constant times this, times the reconstruction loss, minus the regularizer. And of course I want to do it like this. I need to maximize this lower bound, which means that I need to minimize the sum of these two losses. So I need to maximize the variational lower bound, which means that I need to minimize this with respect to, and what is Q? Q are these mu and sigma parameters of the output of the encoder. So that's how it works, that's the whole thing. Or at least that's the first part of the thing, that's the thing with the loss functions. So again, to summarize, we have come from this general idea of let's have some sampling inside an autoencoder, and let's have some regularizer on the sampling distributions because otherwise they're not going to work. We have come to exact formulas. We basically just see that, oh, what should be the regularizer? Well, the regularizer should be this, and this is just a very specific formula. You can look it up. It's actually not very trivial. You wouldn't be able to guess it if you didn't know. But it's a specific formula of mu and sigma. And how do I define the reconstruction loss? Well, the reconstruction loss just follows from the noise assumption in the decoder. So why was it the least squares? Because I chose the Gaussian over here. I could have chosen a different noise model. I would have gotten a different reconstruction loss. So there are no surprises here. This we kind of expected. But the variational to encoder also gives you an exact form of the regularizer. So this is nice. I think this is a very beautiful application of this variational idea in deep learning. But that was only one of our problems, right? There was also the second problem, the sampling problem. How do I put gradients through sampling stuff? And that's actually much easier. It's called the re-parameterization trick. Trick. And the re-parameterization trick works as follows. So let me copy this basic structure again. X goes to the encoder. The encoder produces mu and sigma. And then I'm supposed to kind of sample Z from this, right? And then it will go to the decoder and will produce X hat. So, the trick is, instead of sampling from this Gaussian, I want to restructure this neural network in such a way. That's why it's called reparameterization. I want to reparameterize the sampling distribution so that I could sample in advance. So that I could sample before I know mu and sigma, right? And so that I could have some just separate input here. Let's call it z prime, z zero or something. Let's call it u. I could have a separate input here that would be sampled by itself with no regard for x in advance. And then something would happen inside and I would get the same output. If I can do that, then I've solved the problem because now it's not a problem if I need to sample part of the inputs, right? It's only a problem if I need to inside the gradient flow. So how do I do this? Well, it depends on the specific distribution. Sometimes you can do it, sometimes you can't, but for Gaussians you definitely can. So what do we need to know about Gaussians? We just need to know that if you want to sample from a Gaussian with a given mean and a given covariance matrix, it's the same as sampling from a standard Gaussian. And then multiplying, so let's call it u times sigma. Okay, let me write it as distribution first. So this distribution is just a linear function of the standard normal. So it's the same as sampling z from a standard Gaussian, then doing component-wise multiplication by sigmas, and then adding mu. So mu is a shift, right, in the Gaussian, and sigma is a rescaling of the Gaussian. But the shape of the distribution is the same, and you can start with a standard Gaussian and apply the parameters afterwards. So that's exactly what we are going to do. That's the whole trick. We are going to say that this additional input, this u, is sampled from a standard Gaussian. And then what do I need to do with it? Well, I need to multiply it component-wise by sigma, and then I need to add mu. And here I get z, which is actually sampled from this distribution. So it's a property of the Gaussian specifically. If I had a different distribution of the output of the encoder, I would need to have a different thing here. And maybe I wouldn't even be able to do this. But for a Gaussian, I definitely am able to do this. And it's really straightforward. And that's it. And I take this Z and I plug it into the decoder and I'm done. Okay. So this is the whole trick. So the sampling part is conceptually interesting. I think it's a very beautiful trick, but it's quite simple. And with that, we are basically done with the variational autoencoders. So for the remaining half an hour, I will probably mostly switch to the slides because it will be just a review of diffusion models and we'll discuss some ideas that underlie them. But of course, the mass of the diffusion models actually also involves a lot of variational approximations, but that will be too difficult for us. So, let me first quickly go through the slides on bias. I will show you the same pictures in a more beautiful way, I hope. Okay, so, oh, yeah. This is my picture of the taxonomy that I talked about yesterday. Let me come back to it at the end. Rational lot encoders. So, this is the problem, right? This is the motivation that I started with. It's relatively easy to train a lot of encoder, but the high-dimensional manifold is, of course, very, very difficult, but even the lower-dimensional latent space is also non-trivial. So, how do we simplify? Even in a low-dimensional space, if I start just sampling from a Gaussian, I will not fall in this manifold. So, the idea of the variational lot of encoder that I started with today is let's have whole distributions of these produced by the encoder. So, we can have one distribution here, then we sample from it, and we are supposed to reconstruct the original cat picture from any point sampled from this distribution. Of course, it won't always succeed, but that's the goal, right? And our intuition is that we want to kind of cover the space of latent codes with these distributions and we want to have them wide enough and we want to have them close enough to each other so that afterwards when I sample from just a standard Gaussian, I get to a good part of the space because any part of the space is a good part. It's kind of covered by these small distributions. But of course, it's not going to happen in reality unless I do regularization. So here is the effect that I mentioned. The points will fly away from each other and the variances will shrink to zero. So we need to have both a reconstruction loss and some regularization for the encoder output. And here are the two questions that we discussed. How do we choose the loss function in the regularizer and how do we pass the gradients through the sampling process? So here is the derivation that we did. We started with this simple equality. And in this equality, we know that this guy is the encoder, this guy is the decoder, this guy is the distribution we want to sample z from. And this is this extremely complicated thing. So both the encoder and the decoder cannot be simple. So instead, we are going to model the decoder distribution as a simple one, as just a round Gaussian. And we are going to approximate this complicated encoder distribution with also a Gaussian. And then we do the variational approximation. We get that our variational lower bound plus the KL divergence between our approximation and what we need to approximate equal constant. So as we make the lower bound bigger, the KL divergence shrinks. And this gives us exactly the losses. So we know what is the reconstruction loss that follows from the decoder model. And we know exactly what regularizer we should be using. So this is the idea of variational autoencoders. And here is the reparametrization trick. So fortunately for Gaussians, it's really simple and straightforward. We just need to sample from a standard Gaussian and then we multiply by sigma, we add mu, and we're done. Okay, so this is what, this is, let me call it, this is the proper way to do autoencoders. When it appeared, it did not really catch on. And if you read early papers from 10 years ago, you will see the variational autoencoder always like this baseline that you kind of need to beat, but it's not very difficult to beat. The real competitors are not the YS. But since then, there have been a number of extensions which I don't have time to discuss, but by now, the YS have been extended to discrete latent spaces, which is, let me not talk about this, otherwise I won't have time for the diffusion, but they have been extended to discrete latent spaces, that is, Z is now a set of tokens, sequence of tokens, and this has opened up a lot of doors, so to speak. This has opened up possibilities to, for example, write these latent codes with a transformer, starting from text. It becomes like machine translation, which transformers are perfect for, to convert the prompt into, the text prompt, into this sequence of tokens that will then be decoded into a picture. And that's how DALI worked in 2020 or 2021. And there have been more ideas. I won't discuss them in too much detail, but basically, by now, variational autoencoders underlie a lot of stuff. And, for example, the diffusion models that we are going to discuss now, they usually happen not in the space of images themselves. I will show you interesting pictures that look like they happen in the space of images, just to explain things. But then we will see that, actually, diffusion models operate in the latent space of some model. It would be too computationally expensive to have them operate on pixels. It's much easier and much better to have them operate in the latent space. And usually it's the latent space of what? Usually it's the latent space of a modern variational autoencoder, which, actually, let me just mention maybe one architecture that you might hear about VQ again. It's a variational autoencoder with a discrete latent space, which I won't go into, but it also adds some adversarial losses inside. So it kind of, again, let's not go into details, but it has the basic structure of a variational autoencoder, plus it has an adversarial loss that looks at small patches of the resulting image and makes sure they're realistic, makes sure that locally the small patches look nice and similar to patches from real images. So there is a whole separate discriminator there to make this fine local structure good. And usually like modern diffusion models work in the latent space of some kind of EQ again or something like that. Anyway, on to the diffusion models. This is our last big idea. And it's a very, very simple idea in essence and a very, very difficult idea if I write it down in full detail mathematically. So I won't. Okay. In variational autoencoders, the mathematical formalization was also pretty simple. Here, it's also a variational bound, but much more difficult one. So let me just give you the basic idea. And it dates back to 2015. This is like the foundational paper and diffusion models, Solvig-Stein and co-authors. And it has a very interesting title, Deep Unsupervised Learning Using Non-Equilibrium Thermodynamics. Actually, as an aside, physics, thermodynamics, and deep learning have a lot in common. I'm actually doing some research on the thermodynamics of stochastic gradient descent. If you go to my website, you will see a long blog post with an introduction to this area. I think it's very cool. And there are some real parallels there. And there is like an ideal gas law about stochastic gradient descent. So, but here it's in a different sense. Here the analogy is different. Here the analogy actually just comes from a basic fact on Markov chains. I'm not even sure you need statistical physics here. I think you don't. The basic idea of Markov chains is that, well, if you, you can train a Markov chain that will add noise and will add more and more noise to the input. And after enough steps, after some hundreds of steps, the result will be indistinguishable from randomness. So this is kind of straightforward, right? If I start with a crisp, nice picture and I start just adding Gaussian noise to it, well, I didn't do it to the very end so that you can still see some shade of the original. But if you do it like 500 times, of course, as a result, you will see just Gaussian noise that's indistinguishable from just random sampling. And the point of diffusion models is to try and reverse this process. So you have this noising chain that adds noise and you want to turn it into a denoising chain. So in the forward direction, the transformation is trivial. You just add, let's say, Gaussian noise. In the opposite direction, it's a denoising procedure. So you are supposed to remove Gaussian noise, which is, of course, a much more difficult thing. You can't really do it exactly. You don't know what kind of noise was added. I mean, you would be able to do it exactly only if you knew what you were supposed to get. If you know where you're going, then yes, sure, you can reverse the process. Conditional on x0, conditional on the original image. But obviously, we want to apply it without the original image. We want to apply it as a generative model. We want to then, after training this chain, we want to start with just random noise and gradually turn it into something real. And it turns out you can still do that. So the forward chain is just a Gaussian. A backward chain is some very complicated distribution, but you can try to approximate it with a Gaussian. And then there is a lot of math, which I will skip. So we need to write down the forward diffusion chain formally. We need to compress to get closed-form formulas for getting to several steps ahead in the forward chain. And then we need to reverse this process, and then we need to derive formulas where we actually reverse it if we know where we are going. So like conditional on x0, everything is, well, maybe not easy, but everything is possible. You can actually do denoising perfectly and in closed analytic form if you know the result of the denoising. Yeah, but then you kind of do a big variational approximation that jointly approximates every step in this very long chain. And I know I cannot really explain it without going into a whole lecture on it, but ultimately we want to get to something like this. So we want to have our transformations. You will see that they have the theta over here. So now they are these parametric transformations modeled by neural networks probably. And we want it to be so that here as P of Xn, we can substitute something very simple like a standard Gaussian. And then after some denoising chain, we will get to a sample from this target distribution of cat pictures or whatever, to this very complicated distribution. So how do we do that? We approximate. Okay, let me skip this part. There is a lot. So again, it's the same idea of rational approximations, but applied in a quite more difficult way. But in the end, again, it works. So let me just say that it works. In the end, we get to a specific set of loss functions, well, actually a single loss function, which is a sum of multiple terms. And we can write down these terms. They are like pullback library divergences between the ausians or something. And yeah, and we can just take this loss function and optimize it, train it by gradient descent. And we can train these parameters of these distributions, right? So, okay, so this distribution, we don't train this one. This is just a standard Gaussian. But we train the parameters of this distribution. We train the parameters of the transformation that goes one step back. And when we train it, when it works, when it becomes a good approximation for the whole denoising chain, then you can apply it like this. You can start with pure random noise and gradually turn it into a good sample. And this is your generative model. This is how diffusion models actually produce their results. And in the original paper... So, okay, let's stop with the math now. In the original paper, it only worked for some really, really small dimensions. So like on CIFAR, it kind of worked. When anything larger, they didn't have the capabilities to train it. And for quite a while, this paper just was forgotten. Everybody kind of assumed that, yeah, it's a cool idea, but it's so, so difficult. And even if you succeeded in scaling it up, you would still probably would not be able to apply it because you need to actually apply this reverse chain, this one, you need to go through all the steps, okay? And if you need to go through all the steps, it means that you need to run your neural network hundreds of times because this chain, in order for the whole thing to work, for approximation to be feasible, this chain actually is pretty long. It's, in fact, on the order of hundreds of steps. So if you need hundreds of runs of your neural network to get one image, well, you don't really want to scale it up, right? It begins to sound quite infeasible, even if you succeed somehow. So people thought of it as a very interesting work, but ultimately just a curiosity. But then things started happening. It started in DDPMs in 2020, denoising diffusion probabilistic models. So I will not explain in detail what they did because these are just a collection of small tricks. But basically they kind of made it work. So DDPMs solved some of the other technical problems that diffusion models had and were able to achieve generation basically comparable, basically on par with the best GANs of the time. I showed you some sample generations from GANs yesterday. And back at the day they were very good in doing human faces like this and still quite poor in doing anything else because everything else was just too diverse. It was too... they couldn't capture the full diversity. So, for example, cat images from GANs would also look like this. And so this was actually a kind of state of the art. But DDPMs, even though they did excellent generation, they couldn't... they didn't solve this fundamental problem that I mentioned. They need to go through the chain hundreds of times to make hundreds of steps. So these were nice generations, but they were extremely slow. They took a lot of time to generate these spaces. But in that very year, they actually solved this problem. Well, not they, a different group, but this problem got solved. And again, I will skip the math, but I will just show you this basic idea. So the basic idea is to switch from approximating a step. So as the standard diffusion model or DDPM, you go from xt plus 1 to xt. And you approximate going from xt plus 1 to xt. And then you approximate going from xt to xt minus 1 and so on. So you actually need to make this step because if you don't make this step, you don't know where to start the next step from, right? So you actually need to go through all of the intermediate points. In DDPM, instead of trying to approximate the direction to the next point, we are always approximating the direction to the original x0. x0 lies in the same space, it's just kind of far away. And we have this long path that gets us from x capital T to x0. And in DDPM, we approximate step by step. In DDIM, on every time slot, on every step of the Markov chain, we approximate this whole, this direction right to the goal. And of course, it doesn't mean that we can just go to the goal in one step. No, that doesn't work. Our approximation is not that good. We cannot just jump immediately to a good picture, what's going to happen. But we can go quite a bit further. So like instead of... So in DDPM, we cannot skip steps because if we skip a step, we don't know where to begin the next one. In DDIM, I can say, okay, so I'm supposed to get closer to x0 on every step. And then, yes, it's an approximation, but I know that on the next step, I will also be trying to get closer to x0. So even if my original chain had hundreds and hundreds and thousands of steps, here I will go in the general direction of x0 just faster. I will just take wider steps. So, and that will not be a problem. I will not lose where I am, lose track of where I am, because wherever I am, my next approximation, my next step will be, well, trying to go to x0. So I will not be able to jump all the way there in one step. My approximation will not work like that. But I will be able to get there in a few dozen steps instead of a few thousand. So DDIMs did like 10 or 100x speedup compared to the original diffusion models with no loss of quality, not much improvement on quality either, but that was good enough. And that's where diffusion models actually started working, right? But it was still slow. It was still expensive. And there was this one last step that people actually needed to do before diffusion models started working completely like they work now. And that last step, I actually already mentioned to you, that last step was to do the diffusion not in the space of pixels like those papers did, but in the latent space of some autoencoder. So here is this very famous picture from the paper on stable diffusion. You probably have heard of stable diffusion. It's like the original actually working text-to-image diffusion model, right? It was done in 2022, so not that long ago. Naturally, AI image generation has come a long way since then, but the basic idea still is basically the same. And stable diffusion works like this. It has a diffusion process. It has a denoising architecture here. So it has a diffusion model. And as you can see here, we start with ZKey and we go through a network. This network is some kind of self-attention based unit or whatever. Let's not dwell on the specific architecture. It doesn't really matter. What matters is that, first, this architecture can take a condition. And this condition will be, for example, the prompt. So we need to somehow inform the model what we are trying to draw. This text should go somewhere. And where does it go? Well, the text gets encoded into a vector by some transformer. And then this vector goes into, well, in this case, into self-attention blocks, like we discussed a couple of lectures back with encoder-decoder attention. But it could be a different architecture or whatever. It goes into every denoising step. So every denoising step has this conditional thing, has this another input that comes from the problem. And the most, of course, important novelty here is that all of this happens in the latent space. So all of this happens in the space of vector representations of images, not images themselves, not pixels, vector representations. After this denoising process, we start with random noise, we add this condition, we go through many steps of denoising. What we get is not an image, but a code that will then be decoded by the decoder. And this guy here, the red part, is a variational latent coder. Well, a complicated modern variational latent coder, not quite exactly the one I explained to you, but a variational latent coder. And that's how it works. Another similar thing was done in DALI 2. DALI 2 worked a little bit differently because it used pre-trained clip embeddings. We did not have time to talk about clip and unsupervised learning and contrastive learning in our class. But clip is this standard way of doing joint text image embeddings. So it's like a joint latent space for where both images and text can go. And the idea of DALI 2, for example, was let's put the text into this space and let's train--now clip doesn't include this--but let's train a decoder that will produce an image back from the clip representation. And also let's train a diffusion model inside the latent space that will convert the representation of text into the representation of this image from the decoder. So again, no details here, but you get the idea that diffusion is still happening in the latent space. And DALI 2 was pretty good. Okay, now we would laugh at these images, but in 2022 this was completely awe-inspiring. And this is a very famous image from the original mid-journey that won some contest. And then it was revealed that it's AI-generated and there was this big controversy, the first controversy of this kind. Now, of course, these controversies are everywhere. The next step was to do what was called the Diffusion Transformer, DIT. And I don't have time to explain it in detail. Basically, it's the same kind of latent diffusion model, but now they use a full transformer instead of a unit with some self-attention inside. So the difference is in the internal architecture, not in the approach. The approach is basically the same. You do diffusion in the latent space of some autoencoder. And DITs were good, blah, blah, blah. And these were the samples from the DIT of 2022, already starting to look pretty good. Then there was this flux model. I think it's the last one that I really followed because... So again, I don't have time to explain this picture in detail, but it's also... It's the direct successor of stable diffusion. It was done by the same team. And it was actually very good when it was released. I think obviously you can still download and use it. I'm not sure if it's the best local model right now, but for a long time it definitely was. And yeah, I used to use flux for images for my slides for a very long time. This is all flux generated. It couldn't do text. It wasn't too good with following detailed prompts on composition and stuff that the characters do, etc. But it was like this huge step forward. And yeah, this is also flux, all this bias, etc. And unfortunately after that, it's not like I wanted to stop following. But I lost the ability to follow state-of-the-art text-to-image models because now the best models are basically just GPT, right? GPT or Gemini, they sometimes switch around. For a while, Gemini was better. Now I think GPT Images 2 is again the best. And of course nobody tells us exactly how they work. So right now I have no idea how the best image generation models work. Not because I don't want to know, but because nobody tells us. And MidJourney is still, I guess, competitive. And it was closed from the very beginning, so I don't even know exactly how it worked back then. Probably approximately the same. But still, image generation nowadays is done by diffusion models, most probably operating in the latent space of some big autoencoder. Yeah, so let me skip this. Yeah, and maybe to conclude this part of the class and the whole class, actually, all of the lectures, let me go back to this picture and kind of put all the generative models in place on this picture. I guess I already talked through it, but let's spend another minute. So generative models, they are divided, first of all, into explicit and implicit density models. And basically generative stochastic networks didn't take off. So the only relevant representative of the implicit density class is GANs. And GANs are still relevant, only they are a bit more niche now, a bit more specialized than they used to be. In explicit density models, you have this huge class of autoregressive models. Autoregressive models like WaveNet for producing sound. Autoregressive models like language models. Like all of the LLMs, they all are in here. Because the transformer decoder produces tokens one by one, autoregressively. Conditional on the prefix that it has already generated. Or you can have flow-based models where you start with a simple distribution and you gradually transform it into something more complicated. Or you can have approximate density models where you do not make assumptions about your distribution, but you make assumptions about an approximation to the distribution. And it wasn't clear what it means when I first talked to you about this, but I hope today it has become clear. So there are two main representatives here. The Ys, the Variational Autoencoders, they actually embody this. So we do not make assumptions on p of z given x. We approximate it, and then we make assumptions on the approximation. And how does it work? Through the variational order. And the same goes for diffusion models. Again, we cannot make strong assumptions about the reverse chain, about this denoising chain. What we can do is we can make strong assumptions about an approximation to the reverse chain and then do a variational order. So same approach, the diffusion approach is just a bit more complicated. And basically that's it. So all of the stuff that you hear about in the news is somewhere in this picture and most probably either here in the autoregressive models or here in bias and diffusion. And I guess with that, I want to close our lectures. We have come a long way from the bias theorem back to the bias theorem today. And from the original motivation of neural networks and backpropagation, we got to transformers, we got to variational autoencoders, we got to diffusion models. I think it has been a long journey. I hope it has been an interesting one. And thank you. Any questions? Thank you so much. All right. So thank you very much. I hope we will see each other on Friday still. But the lectures are over. Thank you. Bye-bye.
