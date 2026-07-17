# Transcript — google_stt

- **Provider:** google_stt
- **Language:** en-US
- **Audio duration:** 1:35:51
- **Segments:** 759
- **model:** latest_long
- **use_enhanced:** True
- **latency_sec:** 824.28

## Segments

**[00:11 – 00:14]** Okay, hello everyone. And

**[00:15 – 00:16]** welcome to the last lecture.

**[00:17 – 00:18]** Of our class.

**[00:20 – 00:21]** It has been.

**[00:22 – 00:31]** I think it actually has been quite a long journey through our lectures. I think we've covered quite a lot of ground.

**[00:32 – 00:40]** We actually didn't quite get to the computer vision itself. We only had one lecture on.

**[00:42 – 01:01]** Object detection, I skipped segmentation and entirely, but generative models seem like important ideas too. And you usually, I choose one of the other and in this case, it's generated models. And they all

**[01:02 – 01:10]** Are great teaching tool in my opinion because they show some ideas in relatively simple form they had.

**[01:12 – 01:33]** Go through the whole of machine learning can today in our last lecture. Actually, I'm going to tell you one of this wonderful basic ideas. Maybe you have heard about it and some previous classes, but to be honest I sincerely doubt that somehow in Harbor space people

**[01:34 – 01:37]** Usually don't teach that stuff unless I did.

**[01:38 – 02:08]** So today we mostly talk about relational trainers. And therefore we talk about variational approximations which again in the variational attain coder, they rational approximation appears in its very simplest form and already in a very useful form. So I think it's perfect for our teaching at and then whatever time we have left, I hope we will have some time left. I will

**[02:09 – 02:20]** walk you through diffusion models. There there is a lot of very complicated maths which we definitely won't have time for. But again the basic idea is our kind of

**[02:22 – 02:22]** Easy to show.

**[02:23 – 02:24]** so,

**[02:26 – 02:30]** let's start with the motivation and let's start with the

**[02:33 – 02:37]** basic idea of the variational potent order.

**[02:39 – 02:41]** I started talking about.

**[02:43 – 02:45]** The motivation of wires yesterday.

**[02:46 – 03:07]** When I explained to you this basic problem of, why can't we have a generative model from an auto encoder? I hope you remember. So we have this x, which is like a picture or something, some complicated thing. Then we pass it through the encoder.

**[03:08 – 03:15]** We get in a regular we get like late and coat. The

**[03:16 – 03:23]** And Z is relatively small compared to X. And then there is the

**[03:24 – 03:31]** decoding part. The decoder that is supposed to recover reconstruct.

**[03:34 – 03:37]** Here, the original X, right? This, this is

**[03:38 – 03:41]** the very basic structure of not 10 quarter, and

**[03:42 – 03:54]** You can train it very straightforwardly. There is no problem in thinking of good loss functions here. So, you just want your x and x hat to be similar to each other.

**[03:55 – 03:58]** what is usually called reconstruction was

**[04:00 – 04:08]** And the Reconstruction was basically can be anything. It can be just the L2 Norm.

**[04:10 – 04:36]** It can be something like perception loss and not sure if I looked up to you about that, but like the similarity between some local features extracted by a couple of layers of a standard feature extractors and so on and so forth. So you can you can think of what you want, how you would like to Define.

**[04:37 – 04:48]** What it means to be similar and you just optimize it and the beauty of hot and colder systems that you don't need any label training date, right? You know, your data set can be.

**[04:50 – 04:52]** a just a set of access and

**[04:53 – 05:00]** you automatically get labeled samples because you just need to reconstruct the same except

**[05:00 – 05:00]** so,

**[05:02 – 05:17]** The big question is why can't we use the blue part? I intentionally made it in different color. Why why can't we use the blue part as a generative model and yesterday I told you why, right? We can't use it as a generative model because even though

**[05:18 – 05:30]** in the latent space, these live in a much simpler, much more structured. So to speak many fold, then they do.

**[05:32 – 05:35]** In the space of X. We just very, very complicated.

**[05:36 – 05:37]** They still.

**[05:38 – 05:44]** Do not cover the whole Space of Z, the space of the steel pretty complex. And

**[05:46 – 05:52]** we still need to do something because if we just take random point,

**[05:52 – 06:00]** Here in the latent. Spacey of course, it will not fall into this manifold of actual latent codes for

**[06:01 – 06:02]** Good cat, pictures.

**[06:04 – 06:04]** so,

**[06:05 – 06:40]** Yesterday, I told you one way to try to fix that and that way was to have a discriminator here, right? We just got we discussed adversarial, Auto encoders, where you would try, to distinguish fakes is from, so to speak. Reels is that are sampled from a gaussian or something or whatever distribution you want. And in that way, you can apply adversarial learning. You can apply the base again, idea to

**[06:41 – 06:45]** Try to regularize to try to fix this.

**[06:46 – 06:48]** Latent space. Try to fix this.

**[06:51 – 06:54]** Manifold of latent codes, right?

**[06:57 – 07:00]** And that was called the adversarial and coder.

**[07:01 – 07:25]** So today we discuss the different approach to the same problem and this approach to the same problem is actually better. I mean, at some point there was a competition between adversarial and attend coders Invitational and coders but by now with some recent in Innovations and so on

**[07:25 – 07:42]** variational to encoders are just better and they formed the basis for a lot of for a lot of what's happening in January of modeling in particular for the diffusion models that we will discuss later.

**[07:46 – 07:46]** so,

**[07:54 – 07:54]** Sorry.

**[08:06 – 08:10]** Yeah, so what is the

**[08:15 – 08:17]** What is the?

**[08:37 – 08:44]** I'm sorry. Sorry about that. Yeah. So what what is the variation approach? What is the approach?

**[08:45 – 08:47]** From the variational attacker.

**[08:47 – 08:48]** Well.

**[08:49 – 08:56]** They the idea is as follows you again have the same kind of encoder decoder.

**[08:57 – 08:58]** Construction.

**[09:00 – 09:01]** And other Z.

**[09:02 – 09:04]** D decoder.

**[09:05 – 09:14]** At you still have the same Auto encoder with some reconstruction losses or whatever. But now

**[09:16 – 09:21]** you do the following you say, well, what is the problem?

**[09:22 – 09:23]** With.

**[09:24 – 09:50]** What is the problem with the latent space here? Why isn't it covered? Like why, what is the core of the problem of why these are so hard to actually get why we cannot get to see with random sampling or something.

**[09:50 – 09:58]** And one answer to that is because every X from the training set corresponds to just one point Z.

**[09:59 – 10:18]** And that kind of leads to almost automatic overheating in the space of latent codes. So we are training on a data set. Yes, it may be data set but every Point corresponds to just one C and if you shift your ceiling a little bit, well, you fall off the

**[10:19 – 10:21]** You follow the.

**[10:24 – 10:32]** Many fold of good latent codes and nothing works anymore, right? And when you are sampling,

**[10:33 – 10:40]** Of course you don't know which directions are good, which directions are bad and of course you're very likely to follow the manifold.

**[10:41 – 10:41]** so,

**[10:42 – 10:49]** the approach of the variation of what encoder is to say the following. Now, instead of having just one latent code,

**[10:50 – 10:51]** Let's instead.

**[10:52 – 10:54]** Make the encoder.

**[10:54 – 10:56]** Output a whole distribution of this.

**[10:57 – 11:12]** Like P of C given X. So now when I have like a cat picture over here, it maps in the latent space not to a single point, but it maps to something like a ghost.

**[11:15 – 11:19]** It maps to a whole distribution of little codes.

**[11:21 – 11:24]** and then if I have a different picture,

**[11:25 – 11:28]** It maps to a different distribution of Latin quotes.

**[11:33 – 11:33]** and,

**[11:34 – 11:35]** Then.

**[11:37 – 11:46]** I would like to sample from this distribution. So I would like to pick a point out of say the orange distribution and still

**[11:47 – 11:48]** Reconstruct.

**[11:49 – 11:51]** The same orange cat.

**[11:52 – 11:57]** And if I pick a point from this distribution, I would like to still reconstruct the same.

**[11:58 – 11:58]** Green kits.

**[11:59 – 12:22]** Right? So, I sample from this, so they, they encoder will give me the distribution, actually, in the form of parameters, I'll show it a sec and then I sample from it. And I am supposed to get again at, which is supposed to be similar to it, again, with the Reconstruction was

**[12:24 – 12:25]** so, in this way,

**[12:26 – 12:28]** I will be able to,

**[12:29 – 12:37]** Try to cover the whole latent space or at least some reasonable portion of the latent space with this distributions.

**[12:38 – 12:50]** So, in fact, it's gonna work like that and you usually, it works like this. These distributions are ghosts. They are just normal distributions and they encoded gives you

**[12:52 – 12:52]** their parameters.

**[12:54 – 12:56]** Like, Millworks and sigma works.

**[12:57 – 13:16]** And sigma is a vector, usually just for Simplicity so it should be a covariance matrix. Of course, it's it's all multi-dimensional distributions. But basically I'm talking about diagonal matrix, then they're gonna covariance Matrix here.

**[13:18 – 13:18]** and then,

**[13:19 – 13:21]** From these.

**[13:22 – 13:28]** Two parameters. I can construct the gaussian, right.

**[13:29 – 13:31]** And I sample.

**[13:32 – 13:33]** The.

**[13:34 – 13:39]** From it and then those to the decoder and I get, right?

**[13:40 – 13:40]** So,

**[13:41 – 13:43]** I fix the gaussian shape.

**[13:44 – 13:44]** but,

**[13:45 – 13:49]** I'm basically saying that, well,

**[13:51 – 13:59]** The parameters of this goes and the variance. And the in the means are determined by the encoder, and I will train it to be as best as I can.

**[14:02 – 14:03]** Well.

**[14:04 – 14:15]** The natural question, and the obvious problem here is that why would they encoder actually want to produce any kind of reasonable distribution?

**[14:16 – 14:38]** Because of course, solving this problem with a single point is much much easier for the model, right? So here, it's supposed to reconstruct the same cat from a whole neighborhood of points in this high-dimensional space. Not just from a single point, it's strictly more difficult, right? It's strict strictly harder.

**[14:39 – 14:41]** At the same time.

**[14:42 – 14:44]** At the same time.

**[14:47 – 14:51]** Since the encoder controls the variance.

**[14:53 – 15:07]** Naturally, it can just send the very right. It can just say, well, yeah, I know I'm supposed to do the girls and but what if I just faked ago and say that okay, here is my ghost and just has very small variants

**[15:08 – 15:21]** That's exactly what's going to happen and practice unless your regular rice somehow. So another important component here is that we need some kind of regular

**[15:23 – 15:24]** recitation.

**[15:24 – 15:27]** On the distribution parameters.

**[15:28 – 15:32]** and in this case, also, we need to take this immune Sigma

**[15:34 – 15:35]** And we need to do.

**[15:38 – 15:44]** Regularization on them. We need to make sure that Sigma doesn't just uncontrollably goes to zero.

**[15:45 – 15:46]** and on the other hand, that mu

**[15:47 – 16:33]** Doesn't find control will go to Infinity. Because another way another way to make this problem very, very easy would be to say, okay, so I can't make the variance to small. All right, let me fix the variants to be one, but let's just drive this point so away from each other, so that nothing ever overlaps and everything is completely different. And for me, for me, for me, I think quarter, it just means risking of the space and I am still basically in the same situation of having a virtual points. So that also will definitely happen in practice unless you're regularize. So we need to have some kind of recovery for this. And actually, the regularization is very simple. It says that,

**[16:34 – 16:35]** Our distribution.

**[16:39 – 16:47]** Should be similar to just the standard normal distribution right with mean zero and Union, covariance Matrix.

**[16:50 – 16:53]** So this is the idea of the variation of what encoder.

**[16:54 – 16:56]** but there are some

**[16:57 – 16:59]** problems and unclear things here.

**[17:00 – 17:17]** So one problem, one, one thing that always kind of appears in deep learning cutting machine learning question. In general, is that you often kind of know what you want.

**[17:18 – 17:21]** Right, so let me actually draw the Reconstruction loss.

**[17:25 – 17:25]** Its really.

**[17:28 – 17:30]** You know.

**[17:30 – 17:32]** In principle what you want.

**[17:33 – 17:38]** Like I want to have a construction was that says, that are similar.

**[17:39 – 17:49]** Or I want to have a regularizer that says that mu is kind of like not very far from zero and sigma is kind of like not very close to zero.

**[17:51 – 17:57]** But how do I formalize this? This question number one, how do how do I formalize this? What

**[17:59 – 18:01]** What would different reconstruction losses mean?

**[18:02 – 18:14]** What would it mean to for this to distributions to be close to each other or better to say I know quite a lot of ways to say that they're close to each other which of them should they choose?

**[18:15 – 18:20]** Which reconstruction will they choose, right? This is always, there's always a question like this.

**[18:21 – 18:24]** and but in this case, there's also

**[18:25 – 18:31]** A special question, questions special for this architecture and this is the question of how do I do that?

**[18:33 – 18:34]** How do I?

**[18:35 – 18:39]** Insert a simple procedure intro.

**[18:41 – 18:42]** A deep neural network.

**[18:43 – 18:56]** And it sounds very simple, right? They encoder is a neural network. It has to vectors is output from vectors, and then you just simple. And in the forward propagation in the forward pass

**[18:57 – 18:59]** It is very simple. You just sample from the ghosts.

**[19:00 – 19:01]** You can you know how to do that.

**[19:02 – 19:08]** But what do we do with the backward pass? How does gradient go through a sampling procedure?

**[19:09 – 19:26]** Well, obviously it doesn't. And that is a big problem, and we need to somehow solve this problem, right? So, so let's tackle this problems and talking about them actually gives us this

**[19:28 – 19:36]** The idea is that I advertised in the very beginning, the this very basic idea that go through the whole machine learning.

**[19:37 – 19:40]** So, let's do.

**[19:41 – 19:46]** Like via formerly so to speak.

**[19:48 – 19:48]** and,

**[19:50 – 19:50]** The formal.

**[19:52 – 20:07]** Approach here. And for now, I will be concentrating on the first problem like where the loss functions come from, but to actually talk about this and to actually see where those functions come from. I need to

**[20:08 – 20:18]** Start a little bit further back. So let's look at what kind of variables not parameters variables appear in our model.

**[20:20 – 20:34]** In our model, has basically two variables X, which is the thing that the image, the whatever you are encoding and Z the latent code. So, two variables in the model,

**[20:34 – 20:48]** And what basically, every machine learning model does, right? We discussed in the very beginning of our class. It takes this joint distribution P of XC,

**[20:49 – 20:54]** And decomposes at somehow and then makes some assumptions and so on, right?

**[20:56 – 20:56]** So,

**[20:57 – 21:11]** Here. Poxy doesn't look very difficult and there's not not too many different ways, how you can decompose it. So let's try it. Both of this ways, right? You can start with X and say it's p of x times P of C given X.

**[21:12 – 21:14]** Or you can start with z.

**[21:15 – 21:20]** And you can say it's p of Z times P of sorry x given Z.

**[21:21 – 21:28]** Right. This are the two possible decompositions, unless we go inside accents and right now, we don't want

**[21:30 – 21:31]** and if

**[21:31 – 21:40]** Look at this very simple formula like, you know, this, you know, the full probability formula Hotel, definition of conditional probability, you see?

**[21:41 – 21:51]** All of the components of our neural network. It's actually pretty straightforward and beautiful. So what are the components here?

**[21:52 – 22:06]** Well, what is p of Z given x p of C. Given X is this distribution. It's the in order distribution. It's what they encoder produces. So let me call it the encoder. So to say,

**[22:07 – 22:08]** Right.

**[22:10 – 22:27]** Where is the decoder distribution? Well, the decoder takes the as input and outputs exhibit and it doesn't output the exact X it outputs an approximation to X. So again like linear regression like any machine learning model.

**[22:28 – 22:31]** in actually the quarter produces some

**[22:33 – 22:34]** Noise distribution around X.

**[22:36 – 22:37]** so actually,

**[22:38 – 22:40]** This is the decoder.

**[22:41 – 22:41]** Right.

**[22:46 – 22:48]** Um, what is p of x?

**[22:50 – 23:02]** Oh, P of X is the global distribution of cat pictures, right? So P of X is that extremely difficult. Complicated thing that we have no ability to comprehend.

**[23:05 – 23:06]** And what is p of Z.

**[23:07 – 23:08]** Well, P of C.

**[23:09 – 23:16]** Is the prior distribution, right? Without any X, the prior Distribution on the latent codes.

**[23:16 – 23:19]** so what we would like,

**[23:20 – 23:21]** POC to be.

**[23:22 – 23:23]** Is some simple.

**[23:24 – 23:27]** Distribution that we can sample from.

**[23:28 – 23:31]** Because this whole thing is our generation process.

**[23:32 – 23:46]** Right? How do we produce a new epic picture? We samples Z and then we run it through the decoder, a sample, C. And then we plug it into P of x given C and basically, sample X,

**[23:49 – 23:52]** so, in order for that work,

**[23:52 – 23:55]** We need PLC to be simple.

**[23:56 – 23:56]** Right.

**[23:58 – 23:58]** Well.

**[23:59 – 24:10]** Here is the catch. Here is the end notice that I haven't done basically anything. I wrote like the most trivial formula of the whole probability Theory but

**[24:12 – 24:15]** We already see we can already make some conclusions.

**[24:16 – 24:18]** so, our first conclusion is this

**[24:19 – 24:21]** Well, what are these? Decadent Inquirer.

**[24:24 – 24:26]** The quadrant and colder distributions.

**[24:27 – 24:31]** Oh, the decoder and encoder distributions are

**[24:34 – 24:47]** Well, the decoder distribution is the distribution of noise at the output and it will be captured in the Reconstruction was. We'll see it a little bit later and the encoder distribution is

**[24:48 – 24:48]** Well.

**[24:50 – 24:58]** Something that I'm supposed to sample. This is z of x from. So, basically, it's like the true version of these ghosts.

**[25:02 – 25:02]** and,

**[25:03 – 25:06]** I would, of course, be very happy.

**[25:07 – 25:21]** To say that well hmm let's assume that. The decoder has gaussian noise let's assume that the encoder produces a ghost and let's plug it in and let's do the math and we will, I don't know, we learn some parameters.

**[25:22 – 25:22]** Unfortunately.

**[25:24 – 25:28]** Even without going any further, we see here that it doesn't work.

**[25:30 – 25:43]** Why doesn't it work? Because I need POC to be simple, right? So actually a p of C in the classical variational. 10 quarter will be just a standard goes and we pick views here, right? It's, it's our choice.

**[25:44 – 25:47]** So, P of C is simple.

**[25:48 – 25:57]** if the decoder is also simple and it will be if the decoder is also a ghost and let's say, so it's a gaussian with the mean,

**[25:58 – 26:04]** Specified by the decoder and some gaussian noise around this output.

**[26:05 – 26:18]** So our so our assumption is that we want to reconstruct the original X but of course we cannot do it perfectly. So actually X is near the

**[26:19 – 26:46]** A result of the decoder but with some noise, right? Just like in linear regression. They are supposed to recover the points, but we cannot do it perfectly. So we say that the points are around our straight line but with some noise, exactly exactly the same. So here, it would also be natural to assume some kind of simple noise like a gaussian nice. Otherwise we wouldn't be. We wouldn't know what to do with it.

**[26:46 – 26:49]** So here this is also simple distribution.

**[26:50 – 26:51]** but now,

**[26:53 – 26:58]** if I take the product of two girls, and it's gonna be a ghost,

**[26:59 – 27:00]** it's gonna be simple.

**[27:01 – 27:02]** And this guy over here.

**[27:04 – 27:09]** Is this incredibly complicated distribution in this huge dimensional space.

**[27:10 – 27:22]** There is no way that I can assume that get pictures for my gosh. That doesn't work. The whole point of our model is to somehow you know streamline and simplify this impossibly complicated distribution.

**[27:24 – 27:24]** so,

**[27:26 – 27:26]** Notice how?

**[27:28 – 27:56]** Just this simple equality already tells us that no, we cannot assume both the decoder and the encoder to be easy because if I now write the encoder, also to be a gaussian this quality will never happen, right? The encoder. If I want to have two simple things on the left, it means that the M coder will have to be something very complicated, because it will have to kind of cancel out with this and give you a ghost.

**[27:57 – 28:00]** so, this is gonna be

**[28:01 – 28:04]** Okay, let me just leave it with this POC given X.

**[28:05 – 28:11]** Okay, so I cannot really assume both the quarter and then quarter to be simple.

**[28:13 – 28:30]** I can choose I could assume the encoder to be simple, then the decoder would be difficult, but I want to keep the decoder easier that that is a more natural choice to have. The gaussian noise at the output, he will say. But this means that the AMC order cannot

**[28:31 – 28:32]** Really be simple.

**[28:33 – 28:45]** And the point of the operational encoder, why it's called, the variational 10 quarter is because we take the speed of C given X and we approximated.

**[28:46 – 28:50]** Bye. Oh sorry. Q of C by a simple distribution Q of Z.

**[28:51 – 28:54]** And this will be our goals. So,

**[28:59 – 29:22]** The whole point of the variational attend coder is to say, yeah, the encoder will produce, goes parameters for a ghost and, but, I know from the very beginning that this is not the true distribution, POC, given X. This cannot happen. I don't know. It, it's very complicated. This is an approximation to peer of C, given X.

**[29:26 – 29:30]** And the question is, how do I make this approximation?

**[29:33 – 29:33]** and,

**[29:35 – 29:50]** Here we come to this promised very important idea. One of the most basic ideas and machine learning, one that underlies, millions and millions of different models and that appears all through our film.

**[29:51 – 29:53]** And that's the idea of additional approximations.

**[29:54 – 29:59]** So let me explain it to you from the very beginning.

**[29:59 – 30:05]** Uh, so here, I've motivated that we need an approximation, right?

**[30:06 – 30:06]** and now,

**[30:08 – 30:10]** Let me explain to you how approximations work.

**[30:12 – 30:14]** So,

**[30:15 – 30:22]** again, let me start from scratch again, I start with a very simple formula and I will be doing some

**[30:23 – 30:40]** Simple, but kind of non-obvious Transformations. No not because in the sense that they will be easier, but you will wonder why there's am I doing that. That's okay. Just trust me, it'll take three or four lines and then you will see why we need it all there.

**[30:40 – 30:41]** so,

**[30:43 – 30:52]** We begin with the obvious identity. Say, okay, let me write it with locks lock P of x z. Now, I need to start with the right.

**[30:55 – 30:56]** Mr. Right.

**[30:57 – 31:16]** Variable. Yeah, I need P of X and POC given X. Right? So this is obviously true. This is just this very same identity and it contains the joint distribution. That contains this difficult complicated distribution. That I want to approximate doesn't have any queue yet.

**[31:17 – 31:23]** So first, I take the logs and I put P of X on one side and the rest on the other side.

**[31:24 – 31:25]** So, log P of x.

**[31:26 – 31:28]** Again, so far. Nothing is happening at all.

**[31:29 – 31:32]** Log P of XZ, minus log.

**[31:33 – 31:35]** P of C given X, right?

**[31:37 – 31:56]** Now I make the first tricky step which is I take the expectation so this is just an identity that's always true. Now I take the expectation with respect to cure of Z where Q is any distribution. This point

**[31:57 – 32:09]** On the left and on the right. So I take the expectation on both sides of the equality. It's still remains in the military. But no, just that, I think the expectation with respect to Z

**[32:10 – 32:16]** And here there is no see. So looks is a constant for for this respect to see.

**[32:16 – 32:34]** So on the left, nothing changes. Look payoffs, they yes just remains a constant and on the right, I have this expectation of. Look P of x z minus look P of Z given X.

**[32:34 – 32:35]** Okay.

**[32:37 – 32:38]** Um,

**[32:39 – 32:39]** and now,

**[32:40 – 32:41]** the final non-trivial step.

**[32:42 – 32:48]** I add and subtract the expectation.

**[32:49 – 32:50]** Of lock queue.

**[32:51 – 32:54]** So, like the entropy of the of the distribution queue.

**[32:54 – 32:56]** Again, at this point.

**[32:57 – 33:01]** You probably don't understand why I'm doing this. This will become clear in a couple of ways.

**[33:03 – 33:11]** So I add and subtract expectation of log q. And again, the Soviet doesn't change the identity and

**[33:13 – 33:14]** What do I get now?

**[33:15 – 33:32]** Now, I want to take like the minus from here and put it together with this lock and I want to take the plus from here and put it together with this book, right? So my final formula, is this look of X is

**[33:33 – 33:34]** They expectation.

**[33:35 – 33:36]** Of look.

**[33:37 – 33:43]** P of x z divided by Hills of C, right? I put this locked together with this.

**[33:46 – 33:51]** Minus or do I want plus? Yeah, I think I want plus so Plus

**[33:51 – 33:54]** Expectation of Q of Z.

**[33:55 – 33:57]** Look qz.

**[33:58 – 34:01]** Divided by log P of Z given X.

**[34:02 – 34:03]** Okay.

**[34:05 – 34:18]** So far so good. I hope I hope it hasn't been a problem for you to follow. I have just been writing some basic algebra and basic probability Theory. Not even probabilities here, just put the expectation on top.

**[34:20 – 34:27]** Nothing has been happening, right? It's, it's just a string of obvious. I didn't just not clear what this leads to.

**[34:29 – 34:31]** But yeah, but we are already done.

**[34:32 – 34:36]** So this is the main formula of variational approximation.

**[34:37 – 34:42]** And here is how it works, here is what the text actually means.

**[34:43 – 34:44]** On the left.

**[34:45 – 34:46]** You have a constant.

**[34:46 – 35:00]** Right now, let's look at this, as kind of from the point of view of our problem. So this is just an identity, it holds always for any of x. If and then you see, this is just always,

**[35:01 – 35:10]** But let's look at it from our point of view and our point of view is I want to find Q of Z. That would be a good approximation for p of Z given X.

**[35:11 – 35:19]** So in a way, I want to be optimizing something. Don't yet know what? With respect to QVC.

**[35:20 – 35:29]** Right? So let's view this as a functional as a dependence on QVC.

**[35:30 – 35:38]** So on the left I have I don't have cubes here on the left. It's just a global constant, they like a hood of the dates.

**[35:39 – 35:41]** On the right. I have this guy.

**[35:42 – 35:44]** Let's call it l.

**[35:44 – 35:45]** Of Q.

**[35:46 – 35:50]** Some know this cursive of Q.

**[35:52 – 36:02]** Plus and here is the the most beautiful part. What what is this guy? What is the second term here? It's the cool book, climber The Virgins.

**[36:02 – 36:05]** Between Q of Z.

**[36:06 – 36:06]** and,

**[36:07 – 36:10]** Look, look, I just pee.

**[36:11 – 36:15]** Of P of Z given X.

**[36:16 – 36:16]** Right.

**[36:17 – 36:20]** I hope, you know what, Global clever the Divergence is if not its

**[36:22 – 36:42]** It's a common metric that shows how similar to distributions are so I think I introduced at some point, right? Kyle from Q to P is integral Q Times. Log Q divided by P, the X. So this is exactly this right and

**[36:43 – 36:49]** Here we get a thing that shows how close you see?

**[36:50 – 36:53]** Is to the distribution that we want to approximate.

**[36:54 – 36:54]** Right.

**[36:56 – 37:03]** So basically this is a great optimization Target. I want to minimize it with respect to cure.

**[37:04 – 37:05]** Okay.

**[37:10 – 37:10]** and,

**[37:12 – 37:19]** I could just start with it. I didn't need to all of this formula to know that I want to minimize scale from Q to p.

**[37:19 – 37:27]** But p is a very complicated distribution. It's very hard to work with people of C given X because this P of C given X.

**[37:29 – 38:00]** I mean in a standard machine learning application of rational, approximations it would be some complicated posterior of huge probabilistic model with lots of hidden variables that you need to integrate over and it would be very unclear what it is and here too POC. Given access this strange complicated distribution that you need to multiply this distribution of Kit pixel kit photos by to get the same goes in.

**[38:01 – 38:07]** Who knows what it looks like? How can we evaluate? How can we work with it? No idea.

**[38:09 – 38:12]** And the whole point of this simple formulas,

**[38:12 – 38:18]** was to say that instead of working with this POC directly,

**[38:19 – 38:21]** I can just say that look,

**[38:22 – 38:26]** I have the sum of two terms and to gather,

**[38:27 – 38:31]** They make up a constant which is independent of queue.

**[38:32 – 38:37]** so, if I want to make this guy's smaller with respect to you,

**[38:38 – 38:41]** It's exactly equivalent to make this guy larger.

**[38:42 – 38:52]** With respect to Q, right? Because they should sum up to a constant. So, if there is this, this constant, it consists of two,

**[38:54 – 39:21]** Components and I want to make one component smaller, which means that the other is larger and piser. So if I make the other one larger, it means I make the first one small. So if I so the minimizing, the coil Divergence the global Clyde Divergence from Q to P, to P of C, given X to our posterior. To what we are interested in is equivalent to maximize in this beautiful thing.

**[39:23 – 39:24]** and,

**[39:25 – 39:27]** Doesn't sound like much of a result here.

**[39:28 – 39:34]** but if you look at this, so this this L is called the variational

**[39:36 – 39:37]** lower bound.

**[39:40 – 39:42]** or evidence or about,

**[39:44 – 39:48]** Elbow. Sometimes you see an acronym.

**[39:50 – 39:50]** So,

**[39:51 – 39:57]** They sell of Q is a lower bound to a constant that you want to maximize, right?

**[39:58 – 40:00]** and if you look at what it actually is,

**[40:02 – 40:03]** is L of Q.

**[40:04 – 40:17]** It's this, let's say integral okay. Let me write the expectation as an internal doesn't matter. Just to show you the formula. Both ways log P of XZ divided by Q of z, d.

**[40:18 – 40:19]** Right. So it's like

**[40:22 – 40:22]** Let me.

**[40:23 – 40:25]** Open the locks back.

**[40:28 – 40:29]** This year, minus.

**[40:31 – 40:33]** Q Z Lock.

**[40:36 – 40:37]** You.

**[40:38 – 40:40]** See, something like that.

**[40:42 – 40:42]** and,

**[40:44 – 40:44]** if you look at it,

**[40:45 – 40:47]** You see that now?

**[40:48 – 40:57]** All that it involves are well. Firstly distribution that we are optimizing pure and second it involves

**[40:58 – 41:00]** the joint distribution. Poxy.

**[41:01 – 41:23]** And this is a huge difference. So, usually in machine learning, basically, always a machine learning when you define your model, if you know, all of the variables. Like usually, this is applied for probabilistic models, where X are divisible variables, they observables and z are the hidden variants. So if you know both,

**[41:24 – 41:32]** Observable and hidden variables and everything is easy. The distribution, all the distributions decompose. It's a p of X is probably very simple.

**[41:33 – 41:35]** It's big, but it's simple.

**[41:36 – 41:40]** And, but if you need to do something like this, now, it's very complicated.

**[41:41 – 41:48]** Or if you need to do something like this, for example, to integrate over all these. It's also very complicated.

**[41:48 – 41:51]** But the joint distribution is.

**[41:52 – 41:54]** Probably very simple. Otherwise you don't have a good one.

**[41:56 – 41:56]** so,

**[41:57 – 42:09]** the whole point of rational approximation is to switch from working with a very difficult distribution, very complicated distribution that you can work with to work with a simple distribution that you can work with.

**[42:10 – 42:10]** and,

**[42:11 – 42:19]** In. So getting back to the original and coder in our operational, encoder this is

**[42:20 – 42:39]** Like really obvious and it, it's shown in the very clear form. So what is this? POC given X? It's something very, very complicated that we have no idea how to handle, but what is pure facts and see? What is the Chinese distribution? Well, it's a product of two girls sense.

**[42:39 – 42:40]** Here we go.

**[42:42 – 43:01]** So to to make it easier, we just need to decompose it in a different way. So we just, let's just look at it as log P of Z, Plus, log P of x, given Z, and not the other way around. Not not in this, in this decomposition.

**[43:05 – 43:06]** so,

**[43:06 – 43:07]** This.

**[43:08 – 43:45]** Idea is the variational approximation and basically how it is used in practice. What you would actually, how you would actually use it as you go through the smart, you have to go through this math. Well, this math is always the same, but then you need to substitute your specific distributions or specific model and it gives you those functions. So let's see how it goes with the original and Order. Let's let me continue this. Let's say, so I plug in this, this composition

**[43:46 – 43:48]** and I get something like,

**[43:51 – 43:54]** Expectation Q of Z.

**[43:54 – 43:56]** Lock.

**[43:56 – 43:59]** P of x given Z, right?

**[44:00 – 44:01]** Plus.

**[44:02 – 44:04]** Expectation.

**[44:04 – 44:07]** Log P of C.

**[44:08 – 44:12]** That's the first term. Minus expectation. Looks

**[44:14 – 44:14]** Right.

**[44:15 – 44:21]** And let me put together the second and third term, so that again.

**[44:22 – 44:26]** It will be more clear. What's happening? Minus

**[44:27 – 44:28]** Expectation.

**[44:31 – 44:31]** Lock.

**[44:32 – 44:35]** Q of Z divided by P of Z.

**[44:36 – 44:37]** Okay.

**[44:38 – 44:38]** so,

**[44:40 – 44:43]** What is this guy over here?

**[44:44 – 44:51]** Oh, this guy over here is the Kyle Divergence between QFC.

**[44:52 – 44:53]** and,

**[44:55 – 44:56]** Right. So

**[44:58 – 45:08]** Cube C is our distribution that is that will be an approximation over here. So this this guy's Cube Z

**[45:10 – 45:15]** And P of the is this orange guy is the simple distribution that I want to sample from.

**[45:17 – 45:18]** So basically,

**[45:19 – 45:24]** This says that my distribution queue.

**[45:26 – 45:31]** Okay, let me let me actually write it. So my gaussian distribution.

**[45:33 – 45:37]** With some parameters, mux and sigma X.

**[45:38 – 45:39]** Should be closed.

**[45:40 – 45:41]** To a standard goes.

**[45:44 – 45:50]** P of Z. Is this simple gaussian that I want to sample from

**[45:52 – 45:54]** and this is exactly the regular eraser.

**[45:55 – 45:59]** So this is the part of the loss, which is the regularizer.

**[46:01 – 46:05]** Again, notice how it how it is. Kind of.

**[46:07 – 46:08]** At the same time.

**[46:09 – 46:10]** Just like, we discussed.

**[46:11 – 46:13]** But also more precise.

**[46:14 – 46:17]** So I told you that well.

**[46:19 – 46:24]** probably I will need to regularize this otherwise bad stuff will happen and you know the

**[46:26 – 46:35]** Distributions in the latent, space will float away from each other and they will become smaller variance will go to zero. Blah blah, we probably need to regularize.

**[46:36 – 46:36]** But how?

**[46:38 – 46:40]** What should be the form of the regular eraser.

**[46:41 – 46:42]** Honestly had no idea.

**[46:44 – 47:01]** But after this little bit of math, now we see an exact formula. I will not go through the details, but you can just write it down and you will see like, an exact formula, a function of mu and sigma that you can just plug into Twitter.

**[47:03 – 47:04]** Right. So

**[47:05 – 47:15]** And you wouldn't be able to arrive at this formula. In any other way, somehow you need to understand that your regular eraser should be specifically this this value.

**[47:16 – 47:28]** And where do we get it from? Well, you get it from variation, the relational proximation. Please don't know any other way. So yeah, it's seems very nature, but if you are looking at the problem from here,

**[47:29 – 47:36]** then it seems just as natural as any other thing you could have just said, okay, so let me put the gaussian on new and some

**[47:38 – 47:40]** gamma Distribution on Sigma.

**[47:41 – 47:46]** Or whatever, right? You could have chosen this

**[47:47 – 47:51]** Regularizer. But it would be just one of very many ideas.

**[47:52 – 47:53]** And here we see.

**[47:54 – 48:00]** Why we chose this idea? So the Aboriginal approximation gives you the most functions.

**[48:01 – 48:03]** And this is basically a linear, right?

**[48:04 – 48:06]** And what is the first part?

**[48:07 – 48:08]** What is this guy?

**[48:08 – 48:08]** Well.

**[48:11 – 48:23]** Yeah, let's make it purple because the decoder was purple and this is about the decoder. So what is this log P of Thanksgiving? Say it's the decoder distribution, right? So it's the expectation.

**[48:25 – 48:27]** Of the look of this house.

**[48:28 – 48:30]** Of this cows and over here.

**[48:31 – 48:33]** right of the house and of

**[48:35 – 48:36]** x.

**[48:37 – 48:41]** Around. There is a result of the decoder with some

**[48:42 – 48:42]** Nice.

**[48:44 – 48:44]** Right.

**[48:46 – 48:46]** and then,

**[48:48 – 49:04]** You can just open the breakers in the sense. You can just plug in with what the density of the normal distribution. Take the look and I again, I want bore you with the full derivation but obviously we kind of know what kind of happened.

**[49:06 – 49:21]** We know the density of the normal distribution, right? So it's like some constant maybe complicated but still minus 1 over 2, C to the power D or something times what times x minus

**[49:22 – 49:24]** The result of the decoder Square.

**[49:26 – 49:30]** Right. That's the exponent of the normal distribution.

**[49:31 – 49:32]** so, this

**[49:34 – 49:36]** is basically a constant.

**[49:37 – 49:47]** Which I don't care about minus some other questions which I don't know. I don't care about times the expectation of

**[49:48 – 49:48]** The.

**[49:55 – 49:59]** Of the list where of the list squares lost between X.

**[50:00 – 50:01]** And they.

**[50:03 – 50:04]** Decoder result.

**[50:05 – 50:05]** Right.

**[50:06 – 50:08]** so, this actually

**[50:09 – 50:14]** Is the part which is the Reconstruction loss.

**[50:15 – 50:40]** The expectation over Q. Basically just means that I take the average over the training data and in practice, it just means averaging over the data set, we approximate this expectation with the average of the data sets. So it's like, the actual loss is something like one over. N times the sum xn minus

**[50:42 – 50:44]** The decoder of CNN.

**[50:45 – 50:48]** actually go comes from where

**[50:50 – 50:55]** Where does this come from? It comes from the encoder of X, something like this.

**[50:57 – 50:58]** Right. So

**[51:01 – 51:02]** what have we done?

**[51:03 – 51:08]** I didn't go through all the detail, but I

**[51:08 – 51:14]** hope the idea is already here and I hope that have done we

**[51:15 – 51:20]** Started with this very basic decomposition which is not much of an idea to be honest.

**[51:22 – 51:26]** We applied the variational approximation and as a result.

**[51:27 – 51:28]** we see that our

**[51:31 – 51:34]** operational lower bound our lfq.

**[51:35 – 51:40]** Is like minus, so it's some constant.

**[51:41 – 51:44]** Minus some constant times.

**[51:47 – 51:50]** this times, the Reconstruction was

**[51:52 – 51:56]** Minus the regularizer.

**[51:57 – 52:01]** And of course, I want to do it like this. I need to

**[52:02 – 52:06]** maximize this lower bound, which means that I need to minimize.

**[52:07 – 52:08]** the sum of,

**[52:08 – 52:10]** This tools.

**[52:14 – 52:14]** Directing.

**[52:16 – 52:17]** Let's put it like this.

**[52:19 – 52:26]** So I need to maximize the variational lower bound, which means that I need to minimize this with respect to you.

**[52:27 – 52:33]** And what is q q. Are this mu and sigma parameters of the output of the encoder.

**[52:35 – 52:43]** So that's how it works. That's the whole thing. Or at least that's the first part of the thing. That's the thing with the with those functions.

**[52:46 – 52:46]** so,

**[52:47 – 52:47]** Again.

**[52:48 – 52:48]** To summarize.

**[52:50 – 53:07]** We have come from this general idea of let's have some sampling inside and auto encoder and let's have some regularizer on this on the sampling distribution because otherwise, they're not gonna work, we have come to exact formulas.

**[53:08 – 53:26]** We basically just see that oh what should be the regularizer? Well the regularizer should be this and this is just a very specific formula. You can look it up it's actually not not very trivial. You wouldn't be able to guess that if you didn't know but it's a specific formula of man Sigma

**[53:29 – 53:29]** and,

**[53:30 – 53:39]** How do I Define the Reconstruction was well, let a construction was just follows from the noise assumption in the decoder.

**[53:40 – 53:45]** So why was it the least squares? Because I chose the gaussian over here.

**[53:45 – 53:53]** I could have chosen a different noise model, I would have gotten a different reconstruction was. So there are no surprises here this, we kind of expected

**[53:53 – 54:08]** But the traditional 10 quarter also gives you an exact form of the regularizer. So this this is nice. I think this, this is a very beautiful application of this variational idea in the player.

**[54:09 – 54:14]** But that was only one of our problems. Right there was also the second problem, the sampling problem.

**[54:16 – 54:19]** How do I put gradients through samplings stuff?

**[54:21 – 54:23]** And that's actually much easier.

**[54:24 – 54:27]** It's called The Reaper. Parameterization trick.

**[54:31 – 54:33]** Very parameterization.

**[54:37 – 54:41]** And the republication. Tricks were three works as follows.

**[54:41 – 54:48]** So let me copy this, basic structure again, X goes to the encoder.

**[54:48 – 54:51]** The encoder produces new and sigma.

**[54:53 – 54:58]** Ah, and then I am supposed to kind of sample Z.

**[54:59 – 55:00]** From.

**[55:01 – 55:02]** From this.

**[55:06 – 55:12]** Right? And then it will go to the decoder and will produce except

**[55:13 – 55:15]** so, the trick is

**[55:16 – 55:22]** instead of instead of sampling from this gaussian,

**[55:23 – 55:26]** I want to restructure this neural network and such a way.

**[55:27 – 55:35]** That's why it's called representation. I want to repetitive repetitive simple distribution so that I could sample in advance.

**[55:37 – 55:42]** so that I could sample before, I know, mu and sigma,

**[55:43 – 55:44]** Right. And

**[55:47 – 55:59]** So that I could have some just separate input here. Let's call it the prime 0 or something. Let's call it. You know, you

**[55:59 – 56:10]** I have a separate input here, that would be sampled in itself by itself with no regard for X in advance and then something would happen inside.

**[56:11 – 56:12]** And I would get the same output.

**[56:13 – 56:24]** If I can do that, then I've solved the problem because now, it's not a problem. If I need to sample part of the inputs, right? It's only a problem. If I need to sample inside the gradient flow,

**[56:28 – 56:28]** so,

**[56:30 – 56:38]** how do I do this? Well, it depends on the specific distribution. Sometimes you can, sometimes you can, but for gaussians, you definitely can.

**[56:40 – 56:53]** So what what do we need to know about gaussians? We just need to know that if you want to sample from a gaussian which with a game and mean and the game's matrix, it's the same.

**[56:54 – 56:54]** As.

**[56:56 – 56:58]** Same thing from a standard goes.

**[56:59 – 57:06]** And then multiplying so it's let's call it. You times Sigma

**[57:07 – 57:15]** Okay, let me write this distribution first. So this distribution is just a linear function of the standard normal.

**[57:16 – 57:40]** So it's the same as sampling. Z from a standard. Gaussian then doing component, wise, multiplication by sigmas and then adding milk. So mu is a shift right in the gaussian and sigma is very scaling of the ghosts, but the shape of the distribution is the same and you can start with a stand.

**[57:41 – 57:47]** Standard gaussian and apply the parameters afterwards. So that's what we're going to do.

**[57:48 – 57:49]** That's the whole trick.

**[57:50 – 57:54]** We are going to say that this additional input, this you?

**[57:54 – 57:56]** Is sampled from a standard dose.

**[57:58 – 58:06]** And then what do I need to do with it? Oh, I need to multiply it component Wise by Sigma.

**[58:07 – 58:08]** and then I need to add

**[58:10 – 58:10]** milk.

**[58:12 – 58:17]** And here I get Z which is actually sampled from this distribution.

**[58:18 – 58:38]** Okay, so it's it's appropriate of the gaussian specifically if I had a different distribution of the output of the encoder, I would need to have a different thing here and maybe I wouldn't even be able to do this. But for a question I definitely am able to do this and here it's it's really straightforward.

**[58:40 – 58:44]** And that's it. And I take this e and they plug it into the decoder and I'm done.

**[58:46 – 58:46]** Okay.

**[58:48 – 58:56]** So this is this is the whole trick. So the sampling part is conceptually interesting. I think it's it's a very beautiful trick but it's it's quite

**[58:59 – 59:14]** And with that, we are basically done with with the variational attenders. So for the remaining half an hour, I will just I will probably mostly switch to the slides because it'll be just a review of

**[59:18 – 59:24]** Diffusion models and we'll discuss some some ideas that underlying them. But of course,

**[59:26 – 59:38]** The mass of the diffusion models, actually also involves a lot of relational approximation, but that will be too difficult for us. So let me first quickly go through

**[59:39 – 59:45]** The slides on wires. I will show you the same pictures in a more beautiful way, I hope.

**[59:47 – 59:58]** Okay, so, oh yeah, this is the my picture of the taxonomy that I talked about yesterday. Let me come back to it at the end.

**[59:59 – 1:00:02]** A rational attenders. So this is

**[1:00:03 – 1:00:20]** The problem, right? This is the motivation that I started with, It's relatively easy to train, not to encoder, but the high dimensional manifold is, of course, very, very difficult but even the lower dimensional latent spaces, also non-trivial. So how do we simplify it?

**[1:00:21 – 1:00:28]** Even in a low-dimensional space, if I start just simple just sampling from a gaussian, I will not fall in this manifold.

**[1:00:31 – 1:00:41]** So the idea of the relational, ten quarter that I started with today is, let's have hold distributions of these.

**[1:00:42 – 1:00:43]** Produced by the encoder.

**[1:00:44 – 1:01:01]** So we can have one distribution here, then we sample from it and they are supposed to reconstruct their original cat picture from any Point sample from the distribution of course at once always succeed. But that's the goal, right?

**[1:01:02 – 1:01:02]** and,

**[1:01:04 – 1:01:22]** Our intuition is that we want to kind of cover the space of latent codes with this distributions and we want to have the white enough and we want to have them close enough to each other. So that afterwards when I sample from just sorry, when I sample from just a standard gaussian.

**[1:01:24 – 1:01:26]** I get to.

**[1:01:31 – 1:01:32]** I get to this.

**[1:01:35 – 1:01:46]** I get to a good part of the space because like, any part of the space is a good part. It's kind of covered by this small distributions.

**[1:01:47 – 1:01:58]** But of course it's not going to happen in reality unless I do regularization. So here is the effect that I mentioned. The points will fly away from each other and the variance will shrink to 0.

**[1:01:59 – 1:02:03]** So, we need to have both reconstruction laws.

**[1:02:03 – 1:02:04]** and,

**[1:02:05 – 1:02:08]** Some regularization for the encoder outputs.

**[1:02:12 – 1:02:21]** And here at the two questions that we just discussed, how do we chose to those function regular eraser and how do we pass the gradients through the simple process?

**[1:02:22 – 1:02:44]** So, here is the derivation that we did. We started with this simple equality, and in this equality, we know that one of the disc is the encoder. This guy is the decoder. This guy is the distribution. Want to sample G from this, is this extremely complicated thing. So, both they encoder and the decoder cannot be simple.

**[1:02:46 – 1:02:47]** ah, so instead

**[1:02:48 – 1:02:54]** We are gonna model the decoder distribution as a simple one, it's just round gaussian.

**[1:02:55 – 1:03:02]** And we are going to approximate this complicated encoder distribution with also goes.

**[1:03:05 – 1:03:12]** And then we do the variational approximation. We get that our variational lower bound.

**[1:03:13 – 1:03:26]** Plus the Kyle Divergence between our approximation and what we need to approximate equal constant. So as we make the lower bound bigger, the car Divergence strings.

**[1:03:27 – 1:03:40]** And this gives us exactly the losses. So we know what is their reconstruction loss at follows from the decoder model? And we know

**[1:03:41 – 1:03:43]** exactly what regularizer should be used.

**[1:03:44 – 1:03:47]** So this is the idea of relational.

**[1:03:49 – 1:03:52]** And here is the repair materialization trick. So,

**[1:03:54 – 1:04:04]** fortunately forgot since it's really simple and straightforward which is just need to sample from a standard gaussian and then we multiplied by Sigma we add Mill and

**[1:04:07 – 1:04:10]** um, okay, so this is what

**[1:04:12 – 1:04:13]** this is,

**[1:04:15 – 1:04:20]** What myths? Let me call it. This is the proper way to do it and quarters, right?

**[1:04:22 – 1:04:23]** when it appeared,

**[1:04:24 – 1:04:42]** It did not really catch on and in, if you read like early papers from 10 years ago, you will see the variational open code. They're always like, you know, this Baseline that you kind of need to beat, but it's not very difficult to beat, right. The real competitors are not the bias.

**[1:04:43 – 1:04:58]** But since then, there have been a number of extensions which I don't have time to discuss. But by now the virus have been extended to discrete weight and spaces. Which is guess what? Let me

**[1:04:59 – 1:05:12]** Yeah, let me not talk about this. Otherwise I won't have time for the diffusion but they have been extended to discrete late and spaces. It is z is now a set of tokens sequence of tokens.

**[1:05:13 – 1:05:16]** And this has opened up.

**[1:05:17 – 1:05:49]** A lot of doors. So to speak. This has opened up possibilities to. For example, write this latent codes with the Transformer, starting from text. It becomes like machine translation, which Transformers are perfect for to convert The Prompt into the text prompt into this sequence of tokens, that will then be decoded into a picture, and that's how they worked and 2020 or 2021.

**[1:05:50 – 1:05:57]** And there have been more ideas. What I want, discuss them to match the tail but

**[1:05:58 – 1:06:02]** Basically, by now operational and quarters.

**[1:06:03 – 1:06:05]** Underlying a lot of stuff.

**[1:06:06 – 1:06:11]** And for example, the diffusion models that we are going to discuss now.

**[1:06:12 – 1:06:30]** They usually happen. Not in the space of images themselves. I will show you interesting pictures that look like they happen in the space of images just to explain things but then we will see that. Actually, if you shouldn't models operate in the latent space of some model.

**[1:06:31 – 1:06:34]** Ah, it would be too computationally.

**[1:06:36 – 1:06:51]** Expensive to have them operate on pixels, it's much easier and much better to have them operate in a latent space and usually it's late in space of what. Usually it's latent space.

**[1:06:52 – 1:07:02]** Of operational encoder. Oh, for modern variation. What encoder? Which actually let me just mention. Maybe one architecture that.

**[1:07:04 – 1:07:07]** You might hear about VQ again.

**[1:07:09 – 1:07:22]** It's it's a rational and quarter with a discrete latent space, which I won't go into but it also adds some adversarial losses inside.

**[1:07:23 – 1:07:33]** So it kind of again, let's not go into details but it's kind of it has the basic structure of operational and quarter.

**[1:07:34 – 1:07:35]** Plus.

**[1:07:36 – 1:07:54]** It has 100% of us that looks at pitches of small patches of the resulting image and make sure they really make sure that the local the small Pages. Look nice and similar to pages from real images.

**[1:07:55 – 1:07:58]** so, there is like a whole separate discriminator there to

**[1:08:01 – 1:08:04]** Make this fine. Local structure, good.

**[1:08:05 – 1:08:12]** And usually like modern diffusion models work in the latent, space of some kind of EQ again or something like that.

**[1:08:13 – 1:08:13]** Anyway.

**[1:08:14 – 1:08:15]** on to

**[1:08:16 – 1:08:18]** the diffusion models.

**[1:08:21 – 1:08:23]** This is our last big idea.

**[1:08:26 – 1:08:26]** and,

**[1:08:28 – 1:08:52]** It's a very, very simple idea in essence and the very, very difficult idea. If I write down in full detail mathematically. So I want okay inspirational and coders the main medical from organization was also pretty simple here. It's it's also additional Bond but much more difficult one. So let me just give you the gist. Give you the the basic idea.

**[1:08:53 – 1:09:01]** And it did Back to 2015. And this this is like the foundational paper and diffusion models. So next time,

**[1:09:02 – 1:09:10]** And callers. And it has a very interesting type of deep unsupervised. Learning using non equilibrium thermodynamics

**[1:09:11 – 1:09:18]** Actually, as an aside physics and thermodynamics, and deep learning are have a lot in common.

**[1:09:19 – 1:09:24]** I'm actually doing some research on the thermodynamics of stochastic gradient descent. If you

**[1:09:26 – 1:09:49]** Go to my website, you will see a Long blog posts with an introduction to this area. It's I think it's it's very cool and there are some real parallels there and there is like an ideal gas law about stochastic gradient descent. So but but here it's in a different sense here, the analogy is different.

**[1:09:49 – 1:09:59]** Here the analogy actually just comes from a basic effect on Markov chains that I'm not even sure you need statistical physics here. I think you don't.

**[1:10:01 – 1:10:18]** The basic idea of Mark chances that well, if you, you can train a Markov chain that we will add noise and we'll add more and more noise.

**[1:10:19 – 1:10:28]** To the input. And after enough steps after some hundreds of steps, the result will be in distinguishable from randomness.

**[1:10:29 – 1:10:58]** Uh, so this this is kind of straightforward, right? If I start with a crisp nice picture and they start just adding gaussian noise to it. Well, I didn't do it to the variant so that you would, you can still see some shade of the of the original. But if you do it like 500 times, of course, as a result, you will see, just the ocean noise that's indistinguishable from from just random sampling.

**[1:11:00 – 1:11:02]** and the point of,

**[1:11:04 – 1:11:09]** Diffusion models is to try and reverse this process.

**[1:11:10 – 1:11:16]** So, you have this noising chain that adds noise.

**[1:11:17 – 1:11:20]** And you want to turn it into a denoise chain?

**[1:11:20 – 1:11:29]** So in the forward Direction, the transformation is distributable. You just add a gaussian nurse

**[1:11:30 – 1:11:34]** in the opposite direction. It's a noise in procedure.

**[1:11:34 – 1:11:40]** Right? So you are supposed to remove ghosts and Noise.

**[1:11:40 – 1:11:43]** Which is of course a much more difficult thing, right?

**[1:11:45 – 1:12:04]** You can't really do it. Exactly. You don't know what kind of noise was added. I mean, you would be able to do it exactly. Only, if you knew what you were supposed to get, if, you know where you're going then yes, sure. You can reverse the process, a conditional on x0, conditional, the original image. But

**[1:12:05 – 1:12:18]** Obviously, we want to apply it without the original image. I want to apply it as a generative model. We want to, then, after training this chain, we want to start with just random noise, and great. Surely turn it into something real.

**[1:12:20 – 1:12:22]** In the turns out, you can still do that.

**[1:12:23 – 1:12:23]** so,

**[1:12:25 – 1:12:35]** the forward chain is just a ghost and backward. Chain is some very complicated distribution, but you can try to approximate it with the ghosts.

**[1:12:36 – 1:12:37]** and then there is

**[1:12:38 – 1:12:40]** a lot of math, which I will skip.

**[1:12:41 – 1:12:53]** So we need to like write down the forward diffusion chain, formally. We need to compress to get closed form formulas for getting like to

**[1:12:54 – 1:13:20]** Several Step Ahead, steps ahead and in the forward chain and then we need to reverse this process. And then we need to derive formulas where we actually reverse it. If we know where we are going. So like conditional not zero, everything is well, maybe not easy, but everything is possible. You can actually do the noising perfectly and in close and analytic form. If you know the result that you know,

**[1:13:24 – 1:13:26]** but then,

**[1:13:27 – 1:13:35]** you kind of do a big variational approximation that jointly proximate every

**[1:13:36 – 1:13:47]** Step in this very long chain and I know it doesn't, I know it. I cannot really explain it without going into a whole lecture on it but

**[1:13:48 – 1:14:26]** Ultimately, we want to get to something like this, so we want to have our Transformations, you will see that they have Theta over here. So now there this parametric Transformations model by neural networks, probably, and we want it to be. So that here SP of xn, we can substitute something very simple like a standard goes and and then after some chain, we will get to a sample from the target distribution of get pictures or whatever to this very complicated distribution.

**[1:14:29 – 1:14:43]** So how do we do that? We approximate. Okay, let me skip this part. This, there's a lot of. So again it's the same idea of rational approximations but applied in quite more difficult way.

**[1:14:44 – 1:14:44]** But in the end,

**[1:14:45 – 1:14:51]** Again, it works. So let me just say that it works in the end, we get

**[1:14:52 – 1:15:20]** A two specific set of loss functions. Well, actually a single loss function, which is a sum of multiple terms and we can write down this terms. They are like Global Library divergences between the oceans or something. And yeah, and we can just take this loss function and optimize it trained and by gradient descent and we can train this parameters of these distributions.

**[1:15:21 – 1:15:29]** Right. So okay, so this is distribution, we don't train this one, this is just standard gaussian but we train the parameters of this distribution.

**[1:15:30 – 1:15:33]** we train the parameters of the transformation that goes, once that

**[1:15:36 – 1:15:42]** and when we train it, when it works, when it becomes a good approximation for the whole organizing chain then,

**[1:15:43 – 1:15:58]** You can apply it like this. You can start with pure random noise and gradually turn it into a good sample and this is your generative model. This is how diffusion models actually produce their results.

**[1:16:00 – 1:16:01]** and,

**[1:16:03 – 1:16:19]** Here in the original paper, so okay. Well let's stop with the mess. Now, in the original paper, it only worked for some really, really small Dimensions so I can see far. It kind of worked on anything larger, they didn't have the capabilities to train it.

**[1:16:20 – 1:16:24]** And for quite a while, this paper just was forgotten.

**[1:16:26 – 1:16:30]** Everybody kind of assumed that. Yeah, it's a cool idea.

**[1:16:30 – 1:16:38]** But it's also difficult. And even if you succeeded in scaling it up, you would still probably

**[1:16:39 – 1:16:41]** would not be able to apply it because

**[1:16:43 – 1:16:44]** you need to.

**[1:16:45 – 1:16:53]** Like to actually apply this reverse chain and this one, you need to go through all the steps.

**[1:16:53 – 1:16:58]** Okay, and if you need to go through all the steps, it means that you need to run your neural network.

**[1:17:00 – 1:17:11]** Hundreds of times because this chain in order for the whole thing to work for approximation to be visible, this chain actually is pretty long. It's in fact on the order of hundreds of steps

**[1:17:12 – 1:17:12]** so,

**[1:17:14 – 1:17:21]** if you need hundreds of brands of your neural network, to get one image,

**[1:17:21 – 1:17:29]** Well, you don't really want to scale it up, right? It's how it begins to sound quite infeasible even if you succeed somehow.

**[1:17:30 – 1:17:55]** So people thought of it as a very interesting work very But ultimately just the Curiosity but then things started happening. Yes, it's started in the DPMS in 2020, the United States division probabilistic models. So I will not explain in detail what they did because they are just a collection of small tricks.

**[1:17:56 – 1:17:56]** but,

**[1:17:57 – 1:18:07]** Basically, they kind of made it work. So did you pay PMS? So some of the other technical problems that diffusion models had

**[1:18:08 – 1:18:10]** And were able to achieve.

**[1:18:12 – 1:18:19]** generation basically comparable basically on par with the best games of the time I showed you some

**[1:18:21 – 1:18:27]** sample Generations from games the last yesterday and

**[1:18:28 – 1:19:01]** A back at the day, they were very good in doing human faces like this and still quite poor in doing anything else because everything else had just was just too diverse it. Had it. What? It was too? They couldn't capture the full diversity. So for example, cat images for again, from Gans for those who look like this, and yeah, and so this was actually kind of state up there but gdpm even though they did excellent generation.

**[1:19:02 – 1:19:04]** They couldn't.

**[1:19:05 – 1:19:12]** They didn't solve this fundamental problem. That I mentioned, they need to go through the chains of times.

**[1:19:13 – 1:19:16]** To make hundreds of steps.

**[1:19:17 – 1:19:25]** So this for nice Generations but they were extremely slow. They took a lot of time to generate this place.

**[1:19:28 – 1:19:30]** but in that very year,

**[1:19:31 – 1:19:36]** they actually solved this problem. Well, not not a different group, but this problem got solved.

**[1:19:37 – 1:19:40]** And again, I will skip the math.

**[1:19:41 – 1:19:43]** But I will just show you this this basic idea.

**[1:19:44 – 1:19:45]** So,

**[1:19:46 – 1:19:48]** the basic idea.

**[1:19:49 – 1:19:58]** Is to switch from approximating a step. So, as the standard diffusion model or ddpm,

**[1:19:59 – 1:20:02]** You go from x t plus 1 to x t.

**[1:20:03 – 1:20:08]** And you approximate going from x t plus 1 to XT.

**[1:20:09 – 1:20:14]** And then you approximate going from XT to XT, minus 1, and so on.

**[1:20:15 – 1:20:27]** So you actually need to to make this step because if you don't make the step you don't know where to start the next step from. Right. So you actually need to go through all of the intermediate points.

**[1:20:28 – 1:20:35]** In DD. I am in the state of trying to approximate the direction to the next point.

**[1:20:36 – 1:20:50]** We are always approximating the direction to the original xero license. The same space, it's just kind of far away and we have this long path that gets us from x capital.

**[1:20:52 – 1:20:58]** And in ddpm we approximate step by step, indeed. I am on every

**[1:21:00 – 1:21:03]** Time slot on every step of the Markov chain.

**[1:21:03 – 1:21:07]** We approximate this whole distraction right to the go.

**[1:21:09 – 1:21:20]** And of course, it doesn't mean that we can just go to the goal in one step. Now that doesn't work, our approximation is not that good. We cannot just jump immediately to a good picture. One gonna happen

**[1:21:21 – 1:21:24]** but we can go quite a bit further.

**[1:21:25 – 1:21:35]** So like in stead of so in GDP, we cannot skip steps because if we skip a step we don't know where to begin. The next one.

**[1:21:36 – 1:21:41]** In TD, I am, I can say, okay, so I'm supposed to get closer to 0 on every step.

**[1:21:42 – 1:21:50]** and then yes, it's an approximation, but I know that on the next step, I will also be trying to get closer to zero

**[1:21:50 – 1:21:55]** so, even if my original chain,

**[1:21:56 – 1:21:56]** Had.

**[1:21:57 – 1:22:08]** Hundreds and hundreds and thousands of steps here. I will go in the general direction of xero just faster. I will just take

**[1:22:09 – 1:22:10]** Wider steps.

**[1:22:12 – 1:22:18]** So and that will will not be a problem. I will not lose where I am lose track of where I am. Because

**[1:22:20 – 1:22:27]** What? Wherever I am my next approximation. My next step will be well trying to go to zero.

**[1:22:28 – 1:22:28]** so,

**[1:22:29 – 1:22:35]** I will not be able to jump all the way there in one step. My approximation will not work like that, but

**[1:22:36 – 1:22:41]** I will be able to like get there in a few dozen steps instead of a few thousand.

**[1:22:42 – 1:22:43]** So ddim.

**[1:22:45 – 1:22:57]** Did like tense or 100x speed up compared to their original. Diffusion models with no loss of quality not much improvement in quality either but that was good enough.

**[1:22:58 – 1:23:03]** And that's where the fusion models actually started working.

**[1:23:04 – 1:23:04]** Right.

**[1:23:05 – 1:23:08]** But it was still slow.

**[1:23:09 – 1:23:10]** It was still expensive.

**[1:23:12 – 1:23:21]** And there was this one last step that people actually needed to do before the fusion models started working completely like the work now.

**[1:23:22 – 1:23:26]** Ah, and that last step I actually already mentioned to you.

**[1:23:26 – 1:23:28]** That last step was.

**[1:23:30 – 1:23:31]** To do the effusion.

**[1:23:32 – 1:23:33]** Not in.

**[1:23:34 – 1:23:40]** The space of pixels like those papers did but in the latent space of some autoencoder.

**[1:23:42 – 1:23:58]** So here is this very famous picture from the paper unstable, diffusion? You probably have heard of stable. Diffusion, it's like the original actually working. Text to image diffusion model, right? It was

**[1:24:00 – 1:24:06]** Done in 2022. So not not that that long ago.

**[1:24:07 – 1:24:14]** naturally, AI image generation has come a long ways since then, but the basic idea still is basically the same

**[1:24:14 – 1:24:17]** And stable. Diffusion works like this.

**[1:24:20 – 1:24:21]** It has a diffusion process.

**[1:24:22 – 1:24:32]** It has a denoising architecture here so it has diffusion model. And as you can see here, we start with ziti and we go through.

**[1:24:34 – 1:24:53]** Network. This network is some kind of Transformer self-attention based unit or whatever, but it's not going to dwelling on the specific architecture doesn't really matter. What matters is that first? This architecture can take a condition

**[1:24:54 – 1:25:06]** And this condition will be, for example, The Prompt, right? So we need to somehow inform the model. What we are trying to draw like this text should go somewhere.

**[1:25:07 – 1:25:15]** And where does it go? Well, the text gets encoded into a vector by some Transformer. And then, this vector

**[1:25:16 – 1:25:16]** Goes.

**[1:25:17 – 1:25:18]** Into.

**[1:25:19 – 1:25:41]** Well, in this case into self-attention blocks like we discussed a couple of lectures back with other attention, but it could be a different architecture, whatever it goes into every device in Step. So every nice step has this conditional thing has this another input. The comes from the prompt.

**[1:25:43 – 1:25:49]** and the most of course, important novelty here is that all of this

**[1:25:50 – 1:25:52]** Happens in the latent space.

**[1:25:53 – 1:25:53]** Okay.

**[1:25:54 – 1:25:56]** so, all of this

**[1:25:56 – 1:26:03]** Happens in the space of vector, representations of images, not images themselves, not pixels.

**[1:26:04 – 1:26:05]** Vector representations.

**[1:26:06 – 1:26:17]** And after this denoising process, we start with random noise with this condition. We go through many steps of the noising, what we get is not an image.

**[1:26:18 – 1:26:22]** But a code that will then be decoded by the decoder.

**[1:26:23 – 1:26:33]** And this guy here, the red part is a rational and coder. Well, a complicated modern irrational, not quite exactly the one I explained to you, but

**[1:26:37 – 1:26:39]** and that's how it works. So,

**[1:26:40 – 1:27:14]** Another similar thing was was done in Daily 2 daily 2. Worked a little bit differently in the because it used a pre-trained clip in bathing suits we did not have time to talk about clip and answering in and contrastive learning can in our class. But clip is this standard way of doing joint text image in bennings

**[1:27:15 – 1:27:19]** so it's like a joint latent space for where both images and

**[1:27:20 – 1:27:37]** Text can go and the idea of value 2. For example, was let's put the text into the space and let's train now. Clip doesn't include this, but let's train a decoder that will

**[1:27:38 – 1:27:48]** produce an image back from the clip representation and also let's train a diffusion model inside.

**[1:27:49 – 1:27:55]** The latent space, that will convert the representation of text in to the representation of the image for the decoder.

**[1:27:56 – 1:28:02]** So again, no details here but you get the idea that diffusion is still happening in the latent space.

**[1:28:03 – 1:28:10]** And that was pretty good. Okay, now, we will love this image but in 2022, this was

**[1:28:11 – 1:28:13]** Completely all inspiring.

**[1:28:14 – 1:28:34]** This is a very famous image from the original mid-journey that one some contests and then it was revealed that it's not, it's a age in your rated and there was this big controversy, the first controversy of this kind. Now, of course, this kontrovers are everywhere.

**[1:28:37 – 1:28:43]** um, The Next Step was to do was what it was called the diffusion Transformer the it

**[1:28:44 – 1:29:10]** And let me I don't I don't have time to explain it in detail. Basically it's the same kind of late in diffusion model but now they use a Transformer instead of a full Transformer, instead of a unit with some self-attention inside. So the difference is in the internal architecture not and they approached, the approach is basically the same. You do diffusion in the latent space of someone encoder.

**[1:29:10 – 1:29:20]** And the it is for good blah blah and this for the samples from the data of 2022 already. Starting to pretty good.

**[1:29:21 – 1:29:22]** Then.

**[1:29:23 – 1:29:29]** there was this flux model, I think it's the last one that I really followed because

**[1:29:30 – 1:29:59]** So again, I don't have time to explain this this picture in detail, but it's also it's, it's the direct successor of stable, diffusion. It was done by the same team, and it was actually very good when it was released. I think, obviously, you can still download and use it. It's not sure if it's the best local model right now. But for a long time, a definitely was

**[1:30:00 – 1:30:01]** ah, and

**[1:30:03 – 1:30:09]** Yeah, flat. I used to use flux for images for my slides, for a very long time.

**[1:30:10 – 1:30:21]** This this is all flux generated. It couldn't do text. It wasn't too good with following detailed prompts on compositions and stuff that the characters do Etc but

**[1:30:23 – 1:30:24]** it was like this huge step forward.

**[1:30:25 – 1:30:28]** And yeah, this is all so flux.

**[1:30:30 – 1:30:31]** By et cetera.

**[1:30:32 – 1:30:32]** and,

**[1:30:34 – 1:30:35]** Unfortunately, after that.

**[1:30:36 – 1:30:37]** After that.

**[1:30:38 – 1:30:52]** it's not like I wanted to stop following but I lost the ability to follow state of the art text image models because now the best models are basically just GPC

**[1:30:53 – 1:31:04]** Right GPT or Gemini. They sometimes switch around for a while and I was veteran. Now, I think GTM, which is two is, again best

**[1:31:05 – 1:31:08]** And of course, nobody tells us exactly how they work.

**[1:31:09 – 1:31:27]** So right now, I have no idea how the best image generation models work. Not because I don't want no but because nobody tells us and yeah my journey still I guess completed for in it was closed from the very beginning so I don't even know exactly how it worked back then.

**[1:31:27 – 1:31:29]** Probably approximately the same.

**[1:31:30 – 1:31:31]** But still.

**[1:31:32 – 1:31:42]** Image generation nowadays is done by diffusion models, promos, probably operating in the latent space of some bigotry encoder.

**[1:31:44 – 1:31:47]** Yeah, so let me skip this.

**[1:31:49 – 1:31:51]** Yeah, and maybe to conclude.

**[1:31:52 – 1:32:01]** To conclude this part of the class and the whole class, actually, the all of the lectures. Let me go back to this picture.

**[1:32:02 – 1:32:13]** And kind of put all the generative models in place on this picture. I guess I already talked through it, but let's let's spend another minute.

**[1:32:14 – 1:32:15]** So, generative models.

**[1:32:16 – 1:32:30]** They are divided, first of all, into explicit and implicit instrumentals. And basically, generative stochastic networks didn't take off. So the only

**[1:32:32 – 1:32:36]** Relevant representative of the implicit and City class is against.

**[1:32:36 – 1:32:43]** And Cancers are still relevant, only their bit more Niche. Now a bit more specialized and they used to be

**[1:32:44 – 1:32:50]** A inexplicit density models. You have this huge class of Auto regressive models.

**[1:32:50 – 1:33:08]** Auto regressive models, like, wave net for producing sound autoregressive models, like language models. Like all of the llms they all are in here because the Transformer decoder produces tokens one by one.

**[1:33:09 – 1:33:13]** Auto regressively conditional on the prefix that it has already generated.

**[1:33:14 – 1:33:16]** Or you can have flow based models.

**[1:33:17 – 1:33:22]** Where you start with a simple distribution and you gradually transform it into something more complicated.

**[1:33:25 – 1:33:59]** Or you can have approximate density models where you do not make assumptions about your distribution but you make assumptions about an approximation to the distribution. And it wasn't clear what it means when I first talked to you about this but I hope today it has become clear so the main so there are two main Representatives here, the virus, the variational auto encoders, they actually

**[1:34:00 – 1:34:14]** The embroider this, right? So, we do not make assumptions on P of Z, given X. We approximate it and then we make assumptions on the approximation. And how does it work through the variational Orbot?

**[1:34:15 – 1:34:19]** The same goes for diffusion models. Again, we cannot

**[1:34:20 – 1:34:32]** make strong assumptions about the reverse chain about this. Denoising chain, what we can do is we can make strong assumptions about an approximation to the reverse chain and then the original Orban

**[1:34:33 – 1:34:36]** So, same approach, the diffusion.

**[1:34:37 – 1:34:39]** Approach is just a bit more complicated.

**[1:34:40 – 1:34:50]** And basically, that's it. So, like all of the stuff that you hear about in the news, is somewhere in this picture and most probably either here.

**[1:34:51 – 1:34:56]** In the water, regressive model or here in Rios. And if you

**[1:34:59 – 1:35:00]** Guess who's there?

**[1:35:04 – 1:35:10]** Want to close our lectures, we have come a long way from the base area back to the bath area today.

**[1:35:11 – 1:35:12]** um, and

**[1:35:14 – 1:35:25]** From the I don't know from the original motivation of neural networks and back propagation. We go to Transformers, we go to variational water. Encoders we go to diffusion models.

**[1:35:27 – 1:35:29]** I think it has been a long journey.

**[1:35:30 – 1:35:34]** I hope it has been an interesting one and thank you. Any questions at this point?

**[1:35:37 – 1:35:50]** Questions, thank you. All right, so thank you very much. I hope we will see each other on Friday still but the lectures are over. Thank you. Bye.

## Full text

Okay, hello everyone. And welcome to the last lecture. Of our class. It has been. I think it actually has been quite a long journey through our lectures. I think we've covered quite a lot of ground. We actually didn't quite get to the computer vision itself. We only had one lecture on. Object detection, I skipped segmentation and entirely, but generative models seem like important ideas too. And you usually, I choose one of the other and in this case, it's generated models. And they all Are great teaching tool in my opinion because they show some ideas in relatively simple form they had. Go through the whole of machine learning can today in our last lecture. Actually, I'm going to tell you one of this wonderful basic ideas. Maybe you have heard about it and some previous classes, but to be honest I sincerely doubt that somehow in Harbor space people Usually don't teach that stuff unless I did. So today we mostly talk about relational trainers. And therefore we talk about variational approximations which again in the variational attain coder, they rational approximation appears in its very simplest form and already in a very useful form. So I think it's perfect for our teaching at and then whatever time we have left, I hope we will have some time left. I will walk you through diffusion models. There there is a lot of very complicated maths which we definitely won't have time for. But again the basic idea is our kind of Easy to show. so, let's start with the motivation and let's start with the basic idea of the variational potent order. I started talking about. The motivation of wires yesterday. When I explained to you this basic problem of, why can't we have a generative model from an auto encoder? I hope you remember. So we have this x, which is like a picture or something, some complicated thing. Then we pass it through the encoder. We get in a regular we get like late and coat. The And Z is relatively small compared to X. And then there is the decoding part. The decoder that is supposed to recover reconstruct. Here, the original X, right? This, this is the very basic structure of not 10 quarter, and You can train it very straightforwardly. There is no problem in thinking of good loss functions here. So, you just want your x and x hat to be similar to each other. what is usually called reconstruction was And the Reconstruction was basically can be anything. It can be just the L2 Norm. It can be something like perception loss and not sure if I looked up to you about that, but like the similarity between some local features extracted by a couple of layers of a standard feature extractors and so on and so forth. So you can you can think of what you want, how you would like to Define. What it means to be similar and you just optimize it and the beauty of hot and colder systems that you don't need any label training date, right? You know, your data set can be. a just a set of access and you automatically get labeled samples because you just need to reconstruct the same except so, The big question is why can't we use the blue part? I intentionally made it in different color. Why why can't we use the blue part as a generative model and yesterday I told you why, right? We can't use it as a generative model because even though in the latent space, these live in a much simpler, much more structured. So to speak many fold, then they do. In the space of X. We just very, very complicated. They still. Do not cover the whole Space of Z, the space of the steel pretty complex. And we still need to do something because if we just take random point, Here in the latent. Spacey of course, it will not fall into this manifold of actual latent codes for Good cat, pictures. so, Yesterday, I told you one way to try to fix that and that way was to have a discriminator here, right? We just got we discussed adversarial, Auto encoders, where you would try, to distinguish fakes is from, so to speak. Reels is that are sampled from a gaussian or something or whatever distribution you want. And in that way, you can apply adversarial learning. You can apply the base again, idea to Try to regularize to try to fix this. Latent space. Try to fix this. Manifold of latent codes, right? And that was called the adversarial and coder. So today we discuss the different approach to the same problem and this approach to the same problem is actually better. I mean, at some point there was a competition between adversarial and attend coders Invitational and coders but by now with some recent in Innovations and so on variational to encoders are just better and they formed the basis for a lot of for a lot of what's happening in January of modeling in particular for the diffusion models that we will discuss later. so, Sorry. Yeah, so what is the What is the? I'm sorry. Sorry about that. Yeah. So what what is the variation approach? What is the approach? From the variational attacker. Well. They the idea is as follows you again have the same kind of encoder decoder. Construction. And other Z. D decoder. At you still have the same Auto encoder with some reconstruction losses or whatever. But now you do the following you say, well, what is the problem? With. What is the problem with the latent space here? Why isn't it covered? Like why, what is the core of the problem of why these are so hard to actually get why we cannot get to see with random sampling or something. And one answer to that is because every X from the training set corresponds to just one point Z. And that kind of leads to almost automatic overheating in the space of latent codes. So we are training on a data set. Yes, it may be data set but every Point corresponds to just one C and if you shift your ceiling a little bit, well, you fall off the You follow the. Many fold of good latent codes and nothing works anymore, right? And when you are sampling, Of course you don't know which directions are good, which directions are bad and of course you're very likely to follow the manifold. so, the approach of the variation of what encoder is to say the following. Now, instead of having just one latent code, Let's instead. Make the encoder. Output a whole distribution of this. Like P of C given X. So now when I have like a cat picture over here, it maps in the latent space not to a single point, but it maps to something like a ghost. It maps to a whole distribution of little codes. and then if I have a different picture, It maps to a different distribution of Latin quotes. and, Then. I would like to sample from this distribution. So I would like to pick a point out of say the orange distribution and still Reconstruct. The same orange cat. And if I pick a point from this distribution, I would like to still reconstruct the same. Green kits. Right? So, I sample from this, so they, they encoder will give me the distribution, actually, in the form of parameters, I'll show it a sec and then I sample from it. And I am supposed to get again at, which is supposed to be similar to it, again, with the Reconstruction was so, in this way, I will be able to, Try to cover the whole latent space or at least some reasonable portion of the latent space with this distributions. So, in fact, it's gonna work like that and you usually, it works like this. These distributions are ghosts. They are just normal distributions and they encoded gives you their parameters. Like, Millworks and sigma works. And sigma is a vector, usually just for Simplicity so it should be a covariance matrix. Of course, it's it's all multi-dimensional distributions. But basically I'm talking about diagonal matrix, then they're gonna covariance Matrix here. and then, From these. Two parameters. I can construct the gaussian, right. And I sample. The. From it and then those to the decoder and I get, right? So, I fix the gaussian shape. but, I'm basically saying that, well, The parameters of this goes and the variance. And the in the means are determined by the encoder, and I will train it to be as best as I can. Well. The natural question, and the obvious problem here is that why would they encoder actually want to produce any kind of reasonable distribution? Because of course, solving this problem with a single point is much much easier for the model, right? So here, it's supposed to reconstruct the same cat from a whole neighborhood of points in this high-dimensional space. Not just from a single point, it's strictly more difficult, right? It's strict strictly harder. At the same time. At the same time. Since the encoder controls the variance. Naturally, it can just send the very right. It can just say, well, yeah, I know I'm supposed to do the girls and but what if I just faked ago and say that okay, here is my ghost and just has very small variants That's exactly what's going to happen and practice unless your regular rice somehow. So another important component here is that we need some kind of regular recitation. On the distribution parameters. and in this case, also, we need to take this immune Sigma And we need to do. Regularization on them. We need to make sure that Sigma doesn't just uncontrollably goes to zero. and on the other hand, that mu Doesn't find control will go to Infinity. Because another way another way to make this problem very, very easy would be to say, okay, so I can't make the variance to small. All right, let me fix the variants to be one, but let's just drive this point so away from each other, so that nothing ever overlaps and everything is completely different. And for me, for me, for me, I think quarter, it just means risking of the space and I am still basically in the same situation of having a virtual points. So that also will definitely happen in practice unless you're regularize. So we need to have some kind of recovery for this. And actually, the regularization is very simple. It says that, Our distribution. Should be similar to just the standard normal distribution right with mean zero and Union, covariance Matrix. So this is the idea of the variation of what encoder. but there are some problems and unclear things here. So one problem, one, one thing that always kind of appears in deep learning cutting machine learning question. In general, is that you often kind of know what you want. Right, so let me actually draw the Reconstruction loss. Its really. You know. In principle what you want. Like I want to have a construction was that says, that are similar. Or I want to have a regularizer that says that mu is kind of like not very far from zero and sigma is kind of like not very close to zero. But how do I formalize this? This question number one, how do how do I formalize this? What What would different reconstruction losses mean? What would it mean to for this to distributions to be close to each other or better to say I know quite a lot of ways to say that they're close to each other which of them should they choose? Which reconstruction will they choose, right? This is always, there's always a question like this. and but in this case, there's also A special question, questions special for this architecture and this is the question of how do I do that? How do I? Insert a simple procedure intro. A deep neural network. And it sounds very simple, right? They encoder is a neural network. It has to vectors is output from vectors, and then you just simple. And in the forward propagation in the forward pass It is very simple. You just sample from the ghosts. You can you know how to do that. But what do we do with the backward pass? How does gradient go through a sampling procedure? Well, obviously it doesn't. And that is a big problem, and we need to somehow solve this problem, right? So, so let's tackle this problems and talking about them actually gives us this The idea is that I advertised in the very beginning, the this very basic idea that go through the whole machine learning. So, let's do. Like via formerly so to speak. and, The formal. Approach here. And for now, I will be concentrating on the first problem like where the loss functions come from, but to actually talk about this and to actually see where those functions come from. I need to Start a little bit further back. So let's look at what kind of variables not parameters variables appear in our model. In our model, has basically two variables X, which is the thing that the image, the whatever you are encoding and Z the latent code. So, two variables in the model, And what basically, every machine learning model does, right? We discussed in the very beginning of our class. It takes this joint distribution P of XC, And decomposes at somehow and then makes some assumptions and so on, right? So, Here. Poxy doesn't look very difficult and there's not not too many different ways, how you can decompose it. So let's try it. Both of this ways, right? You can start with X and say it's p of x times P of C given X. Or you can start with z. And you can say it's p of Z times P of sorry x given Z. Right. This are the two possible decompositions, unless we go inside accents and right now, we don't want and if Look at this very simple formula like, you know, this, you know, the full probability formula Hotel, definition of conditional probability, you see? All of the components of our neural network. It's actually pretty straightforward and beautiful. So what are the components here? Well, what is p of Z given x p of C. Given X is this distribution. It's the in order distribution. It's what they encoder produces. So let me call it the encoder. So to say, Right. Where is the decoder distribution? Well, the decoder takes the as input and outputs exhibit and it doesn't output the exact X it outputs an approximation to X. So again like linear regression like any machine learning model. in actually the quarter produces some Noise distribution around X. so actually, This is the decoder. Right. Um, what is p of x? Oh, P of X is the global distribution of cat pictures, right? So P of X is that extremely difficult. Complicated thing that we have no ability to comprehend. And what is p of Z. Well, P of C. Is the prior distribution, right? Without any X, the prior Distribution on the latent codes. so what we would like, POC to be. Is some simple. Distribution that we can sample from. Because this whole thing is our generation process. Right? How do we produce a new epic picture? We samples Z and then we run it through the decoder, a sample, C. And then we plug it into P of x given C and basically, sample X, so, in order for that work, We need PLC to be simple. Right. Well. Here is the catch. Here is the end notice that I haven't done basically anything. I wrote like the most trivial formula of the whole probability Theory but We already see we can already make some conclusions. so, our first conclusion is this Well, what are these? Decadent Inquirer. The quadrant and colder distributions. Oh, the decoder and encoder distributions are Well, the decoder distribution is the distribution of noise at the output and it will be captured in the Reconstruction was. We'll see it a little bit later and the encoder distribution is Well. Something that I'm supposed to sample. This is z of x from. So, basically, it's like the true version of these ghosts. and, I would, of course, be very happy. To say that well hmm let's assume that. The decoder has gaussian noise let's assume that the encoder produces a ghost and let's plug it in and let's do the math and we will, I don't know, we learn some parameters. Unfortunately. Even without going any further, we see here that it doesn't work. Why doesn't it work? Because I need POC to be simple, right? So actually a p of C in the classical variational. 10 quarter will be just a standard goes and we pick views here, right? It's, it's our choice. So, P of C is simple. if the decoder is also simple and it will be if the decoder is also a ghost and let's say, so it's a gaussian with the mean, Specified by the decoder and some gaussian noise around this output. So our so our assumption is that we want to reconstruct the original X but of course we cannot do it perfectly. So actually X is near the A result of the decoder but with some noise, right? Just like in linear regression. They are supposed to recover the points, but we cannot do it perfectly. So we say that the points are around our straight line but with some noise, exactly exactly the same. So here, it would also be natural to assume some kind of simple noise like a gaussian nice. Otherwise we wouldn't be. We wouldn't know what to do with it. So here this is also simple distribution. but now, if I take the product of two girls, and it's gonna be a ghost, it's gonna be simple. And this guy over here. Is this incredibly complicated distribution in this huge dimensional space. There is no way that I can assume that get pictures for my gosh. That doesn't work. The whole point of our model is to somehow you know streamline and simplify this impossibly complicated distribution. so, Notice how? Just this simple equality already tells us that no, we cannot assume both the decoder and the encoder to be easy because if I now write the encoder, also to be a gaussian this quality will never happen, right? The encoder. If I want to have two simple things on the left, it means that the M coder will have to be something very complicated, because it will have to kind of cancel out with this and give you a ghost. so, this is gonna be Okay, let me just leave it with this POC given X. Okay, so I cannot really assume both the quarter and then quarter to be simple. I can choose I could assume the encoder to be simple, then the decoder would be difficult, but I want to keep the decoder easier that that is a more natural choice to have. The gaussian noise at the output, he will say. But this means that the AMC order cannot Really be simple. And the point of the operational encoder, why it's called, the variational 10 quarter is because we take the speed of C given X and we approximated. Bye. Oh sorry. Q of C by a simple distribution Q of Z. And this will be our goals. So, The whole point of the variational attend coder is to say, yeah, the encoder will produce, goes parameters for a ghost and, but, I know from the very beginning that this is not the true distribution, POC, given X. This cannot happen. I don't know. It, it's very complicated. This is an approximation to peer of C, given X. And the question is, how do I make this approximation? and, Here we come to this promised very important idea. One of the most basic ideas and machine learning, one that underlies, millions and millions of different models and that appears all through our film. And that's the idea of additional approximations. So let me explain it to you from the very beginning. Uh, so here, I've motivated that we need an approximation, right? and now, Let me explain to you how approximations work. So, again, let me start from scratch again, I start with a very simple formula and I will be doing some Simple, but kind of non-obvious Transformations. No not because in the sense that they will be easier, but you will wonder why there's am I doing that. That's okay. Just trust me, it'll take three or four lines and then you will see why we need it all there. so, We begin with the obvious identity. Say, okay, let me write it with locks lock P of x z. Now, I need to start with the right. Mr. Right. Variable. Yeah, I need P of X and POC given X. Right? So this is obviously true. This is just this very same identity and it contains the joint distribution. That contains this difficult complicated distribution. That I want to approximate doesn't have any queue yet. So first, I take the logs and I put P of X on one side and the rest on the other side. So, log P of x. Again, so far. Nothing is happening at all. Log P of XZ, minus log. P of C given X, right? Now I make the first tricky step which is I take the expectation so this is just an identity that's always true. Now I take the expectation with respect to cure of Z where Q is any distribution. This point On the left and on the right. So I take the expectation on both sides of the equality. It's still remains in the military. But no, just that, I think the expectation with respect to Z And here there is no see. So looks is a constant for for this respect to see. So on the left, nothing changes. Look payoffs, they yes just remains a constant and on the right, I have this expectation of. Look P of x z minus look P of Z given X. Okay. Um, and now, the final non-trivial step. I add and subtract the expectation. Of lock queue. So, like the entropy of the of the distribution queue. Again, at this point. You probably don't understand why I'm doing this. This will become clear in a couple of ways. So I add and subtract expectation of log q. And again, the Soviet doesn't change the identity and What do I get now? Now, I want to take like the minus from here and put it together with this lock and I want to take the plus from here and put it together with this book, right? So my final formula, is this look of X is They expectation. Of look. P of x z divided by Hills of C, right? I put this locked together with this. Minus or do I want plus? Yeah, I think I want plus so Plus Expectation of Q of Z. Look qz. Divided by log P of Z given X. Okay. So far so good. I hope I hope it hasn't been a problem for you to follow. I have just been writing some basic algebra and basic probability Theory. Not even probabilities here, just put the expectation on top. Nothing has been happening, right? It's, it's just a string of obvious. I didn't just not clear what this leads to. But yeah, but we are already done. So this is the main formula of variational approximation. And here is how it works, here is what the text actually means. On the left. You have a constant. Right now, let's look at this, as kind of from the point of view of our problem. So this is just an identity, it holds always for any of x. If and then you see, this is just always, But let's look at it from our point of view and our point of view is I want to find Q of Z. That would be a good approximation for p of Z given X. So in a way, I want to be optimizing something. Don't yet know what? With respect to QVC. Right? So let's view this as a functional as a dependence on QVC. So on the left I have I don't have cubes here on the left. It's just a global constant, they like a hood of the dates. On the right. I have this guy. Let's call it l. Of Q. Some know this cursive of Q. Plus and here is the the most beautiful part. What what is this guy? What is the second term here? It's the cool book, climber The Virgins. Between Q of Z. and, Look, look, I just pee. Of P of Z given X. Right. I hope, you know what, Global clever the Divergence is if not its It's a common metric that shows how similar to distributions are so I think I introduced at some point, right? Kyle from Q to P is integral Q Times. Log Q divided by P, the X. So this is exactly this right and Here we get a thing that shows how close you see? Is to the distribution that we want to approximate. Right. So basically this is a great optimization Target. I want to minimize it with respect to cure. Okay. and, I could just start with it. I didn't need to all of this formula to know that I want to minimize scale from Q to p. But p is a very complicated distribution. It's very hard to work with people of C given X because this P of C given X. I mean in a standard machine learning application of rational, approximations it would be some complicated posterior of huge probabilistic model with lots of hidden variables that you need to integrate over and it would be very unclear what it is and here too POC. Given access this strange complicated distribution that you need to multiply this distribution of Kit pixel kit photos by to get the same goes in. Who knows what it looks like? How can we evaluate? How can we work with it? No idea. And the whole point of this simple formulas, was to say that instead of working with this POC directly, I can just say that look, I have the sum of two terms and to gather, They make up a constant which is independent of queue. so, if I want to make this guy's smaller with respect to you, It's exactly equivalent to make this guy larger. With respect to Q, right? Because they should sum up to a constant. So, if there is this, this constant, it consists of two, Components and I want to make one component smaller, which means that the other is larger and piser. So if I make the other one larger, it means I make the first one small. So if I so the minimizing, the coil Divergence the global Clyde Divergence from Q to P, to P of C, given X to our posterior. To what we are interested in is equivalent to maximize in this beautiful thing. and, Doesn't sound like much of a result here. but if you look at this, so this this L is called the variational lower bound. or evidence or about, Elbow. Sometimes you see an acronym. So, They sell of Q is a lower bound to a constant that you want to maximize, right? and if you look at what it actually is, is L of Q. It's this, let's say integral okay. Let me write the expectation as an internal doesn't matter. Just to show you the formula. Both ways log P of XZ divided by Q of z, d. Right. So it's like Let me. Open the locks back. This year, minus. Q Z Lock. You. See, something like that. and, if you look at it, You see that now? All that it involves are well. Firstly distribution that we are optimizing pure and second it involves the joint distribution. Poxy. And this is a huge difference. So, usually in machine learning, basically, always a machine learning when you define your model, if you know, all of the variables. Like usually, this is applied for probabilistic models, where X are divisible variables, they observables and z are the hidden variants. So if you know both, Observable and hidden variables and everything is easy. The distribution, all the distributions decompose. It's a p of X is probably very simple. It's big, but it's simple. And, but if you need to do something like this, now, it's very complicated. Or if you need to do something like this, for example, to integrate over all these. It's also very complicated. But the joint distribution is. Probably very simple. Otherwise you don't have a good one. so, the whole point of rational approximation is to switch from working with a very difficult distribution, very complicated distribution that you can work with to work with a simple distribution that you can work with. and, In. So getting back to the original and coder in our operational, encoder this is Like really obvious and it, it's shown in the very clear form. So what is this? POC given X? It's something very, very complicated that we have no idea how to handle, but what is pure facts and see? What is the Chinese distribution? Well, it's a product of two girls sense. Here we go. So to to make it easier, we just need to decompose it in a different way. So we just, let's just look at it as log P of Z, Plus, log P of x, given Z, and not the other way around. Not not in this, in this decomposition. so, This. Idea is the variational approximation and basically how it is used in practice. What you would actually, how you would actually use it as you go through the smart, you have to go through this math. Well, this math is always the same, but then you need to substitute your specific distributions or specific model and it gives you those functions. So let's see how it goes with the original and Order. Let's let me continue this. Let's say, so I plug in this, this composition and I get something like, Expectation Q of Z. Lock. P of x given Z, right? Plus. Expectation. Log P of C. That's the first term. Minus expectation. Looks Right. And let me put together the second and third term, so that again. It will be more clear. What's happening? Minus Expectation. Lock. Q of Z divided by P of Z. Okay. so, What is this guy over here? Oh, this guy over here is the Kyle Divergence between QFC. and, Right. So Cube C is our distribution that is that will be an approximation over here. So this this guy's Cube Z And P of the is this orange guy is the simple distribution that I want to sample from. So basically, This says that my distribution queue. Okay, let me let me actually write it. So my gaussian distribution. With some parameters, mux and sigma X. Should be closed. To a standard goes. P of Z. Is this simple gaussian that I want to sample from and this is exactly the regular eraser. So this is the part of the loss, which is the regularizer. Again, notice how it how it is. Kind of. At the same time. Just like, we discussed. But also more precise. So I told you that well. probably I will need to regularize this otherwise bad stuff will happen and you know the Distributions in the latent, space will float away from each other and they will become smaller variance will go to zero. Blah blah, we probably need to regularize. But how? What should be the form of the regular eraser. Honestly had no idea. But after this little bit of math, now we see an exact formula. I will not go through the details, but you can just write it down and you will see like, an exact formula, a function of mu and sigma that you can just plug into Twitter. Right. So And you wouldn't be able to arrive at this formula. In any other way, somehow you need to understand that your regular eraser should be specifically this this value. And where do we get it from? Well, you get it from variation, the relational proximation. Please don't know any other way. So yeah, it's seems very nature, but if you are looking at the problem from here, then it seems just as natural as any other thing you could have just said, okay, so let me put the gaussian on new and some gamma Distribution on Sigma. Or whatever, right? You could have chosen this Regularizer. But it would be just one of very many ideas. And here we see. Why we chose this idea? So the Aboriginal approximation gives you the most functions. And this is basically a linear, right? And what is the first part? What is this guy? Well. Yeah, let's make it purple because the decoder was purple and this is about the decoder. So what is this log P of Thanksgiving? Say it's the decoder distribution, right? So it's the expectation. Of the look of this house. Of this cows and over here. right of the house and of x. Around. There is a result of the decoder with some Nice. Right. and then, You can just open the breakers in the sense. You can just plug in with what the density of the normal distribution. Take the look and I again, I want bore you with the full derivation but obviously we kind of know what kind of happened. We know the density of the normal distribution, right? So it's like some constant maybe complicated but still minus 1 over 2, C to the power D or something times what times x minus The result of the decoder Square. Right. That's the exponent of the normal distribution. so, this is basically a constant. Which I don't care about minus some other questions which I don't know. I don't care about times the expectation of The. Of the list where of the list squares lost between X. And they. Decoder result. Right. so, this actually Is the part which is the Reconstruction loss. The expectation over Q. Basically just means that I take the average over the training data and in practice, it just means averaging over the data set, we approximate this expectation with the average of the data sets. So it's like, the actual loss is something like one over. N times the sum xn minus The decoder of CNN. actually go comes from where Where does this come from? It comes from the encoder of X, something like this. Right. So what have we done? I didn't go through all the detail, but I hope the idea is already here and I hope that have done we Started with this very basic decomposition which is not much of an idea to be honest. We applied the variational approximation and as a result. we see that our operational lower bound our lfq. Is like minus, so it's some constant. Minus some constant times. this times, the Reconstruction was Minus the regularizer. And of course, I want to do it like this. I need to maximize this lower bound, which means that I need to minimize. the sum of, This tools. Directing. Let's put it like this. So I need to maximize the variational lower bound, which means that I need to minimize this with respect to you. And what is q q. Are this mu and sigma parameters of the output of the encoder. So that's how it works. That's the whole thing. Or at least that's the first part of the thing. That's the thing with the with those functions. so, Again. To summarize. We have come from this general idea of let's have some sampling inside and auto encoder and let's have some regularizer on this on the sampling distribution because otherwise, they're not gonna work, we have come to exact formulas. We basically just see that oh what should be the regularizer? Well the regularizer should be this and this is just a very specific formula. You can look it up it's actually not not very trivial. You wouldn't be able to guess that if you didn't know but it's a specific formula of man Sigma and, How do I Define the Reconstruction was well, let a construction was just follows from the noise assumption in the decoder. So why was it the least squares? Because I chose the gaussian over here. I could have chosen a different noise model, I would have gotten a different reconstruction was. So there are no surprises here this, we kind of expected But the traditional 10 quarter also gives you an exact form of the regularizer. So this this is nice. I think this, this is a very beautiful application of this variational idea in the player. But that was only one of our problems. Right there was also the second problem, the sampling problem. How do I put gradients through samplings stuff? And that's actually much easier. It's called The Reaper. Parameterization trick. Very parameterization. And the republication. Tricks were three works as follows. So let me copy this, basic structure again, X goes to the encoder. The encoder produces new and sigma. Ah, and then I am supposed to kind of sample Z. From. From this. Right? And then it will go to the decoder and will produce except so, the trick is instead of instead of sampling from this gaussian, I want to restructure this neural network and such a way. That's why it's called representation. I want to repetitive repetitive simple distribution so that I could sample in advance. so that I could sample before, I know, mu and sigma, Right. And So that I could have some just separate input here. Let's call it the prime 0 or something. Let's call it. You know, you I have a separate input here, that would be sampled in itself by itself with no regard for X in advance and then something would happen inside. And I would get the same output. If I can do that, then I've solved the problem because now, it's not a problem. If I need to sample part of the inputs, right? It's only a problem. If I need to sample inside the gradient flow, so, how do I do this? Well, it depends on the specific distribution. Sometimes you can, sometimes you can, but for gaussians, you definitely can. So what what do we need to know about gaussians? We just need to know that if you want to sample from a gaussian which with a game and mean and the game's matrix, it's the same. As. Same thing from a standard goes. And then multiplying so it's let's call it. You times Sigma Okay, let me write this distribution first. So this distribution is just a linear function of the standard normal. So it's the same as sampling. Z from a standard. Gaussian then doing component, wise, multiplication by sigmas and then adding milk. So mu is a shift right in the gaussian and sigma is very scaling of the ghosts, but the shape of the distribution is the same and you can start with a stand. Standard gaussian and apply the parameters afterwards. So that's what we're going to do. That's the whole trick. We are going to say that this additional input, this you? Is sampled from a standard dose. And then what do I need to do with it? Oh, I need to multiply it component Wise by Sigma. and then I need to add milk. And here I get Z which is actually sampled from this distribution. Okay, so it's it's appropriate of the gaussian specifically if I had a different distribution of the output of the encoder, I would need to have a different thing here and maybe I wouldn't even be able to do this. But for a question I definitely am able to do this and here it's it's really straightforward. And that's it. And I take this e and they plug it into the decoder and I'm done. Okay. So this is this is the whole trick. So the sampling part is conceptually interesting. I think it's it's a very beautiful trick but it's it's quite And with that, we are basically done with with the variational attenders. So for the remaining half an hour, I will just I will probably mostly switch to the slides because it'll be just a review of Diffusion models and we'll discuss some some ideas that underlying them. But of course, The mass of the diffusion models, actually also involves a lot of relational approximation, but that will be too difficult for us. So let me first quickly go through The slides on wires. I will show you the same pictures in a more beautiful way, I hope. Okay, so, oh yeah, this is the my picture of the taxonomy that I talked about yesterday. Let me come back to it at the end. A rational attenders. So this is The problem, right? This is the motivation that I started with, It's relatively easy to train, not to encoder, but the high dimensional manifold is, of course, very, very difficult but even the lower dimensional latent spaces, also non-trivial. So how do we simplify it? Even in a low-dimensional space, if I start just simple just sampling from a gaussian, I will not fall in this manifold. So the idea of the relational, ten quarter that I started with today is, let's have hold distributions of these. Produced by the encoder. So we can have one distribution here, then we sample from it and they are supposed to reconstruct their original cat picture from any Point sample from the distribution of course at once always succeed. But that's the goal, right? and, Our intuition is that we want to kind of cover the space of latent codes with this distributions and we want to have the white enough and we want to have them close enough to each other. So that afterwards when I sample from just sorry, when I sample from just a standard gaussian. I get to. I get to this. I get to a good part of the space because like, any part of the space is a good part. It's kind of covered by this small distributions. But of course it's not going to happen in reality unless I do regularization. So here is the effect that I mentioned. The points will fly away from each other and the variance will shrink to 0. So, we need to have both reconstruction laws. and, Some regularization for the encoder outputs. And here at the two questions that we just discussed, how do we chose to those function regular eraser and how do we pass the gradients through the simple process? So, here is the derivation that we did. We started with this simple equality, and in this equality, we know that one of the disc is the encoder. This guy is the decoder. This guy is the distribution. Want to sample G from this, is this extremely complicated thing. So, both they encoder and the decoder cannot be simple. ah, so instead We are gonna model the decoder distribution as a simple one, it's just round gaussian. And we are going to approximate this complicated encoder distribution with also goes. And then we do the variational approximation. We get that our variational lower bound. Plus the Kyle Divergence between our approximation and what we need to approximate equal constant. So as we make the lower bound bigger, the car Divergence strings. And this gives us exactly the losses. So we know what is their reconstruction loss at follows from the decoder model? And we know exactly what regularizer should be used. So this is the idea of relational. And here is the repair materialization trick. So, fortunately forgot since it's really simple and straightforward which is just need to sample from a standard gaussian and then we multiplied by Sigma we add Mill and um, okay, so this is what this is, What myths? Let me call it. This is the proper way to do it and quarters, right? when it appeared, It did not really catch on and in, if you read like early papers from 10 years ago, you will see the variational open code. They're always like, you know, this Baseline that you kind of need to beat, but it's not very difficult to beat, right. The real competitors are not the bias. But since then, there have been a number of extensions which I don't have time to discuss. But by now the virus have been extended to discrete weight and spaces. Which is guess what? Let me Yeah, let me not talk about this. Otherwise I won't have time for the diffusion but they have been extended to discrete late and spaces. It is z is now a set of tokens sequence of tokens. And this has opened up. A lot of doors. So to speak. This has opened up possibilities to. For example, write this latent codes with the Transformer, starting from text. It becomes like machine translation, which Transformers are perfect for to convert The Prompt into the text prompt into this sequence of tokens, that will then be decoded into a picture, and that's how they worked and 2020 or 2021. And there have been more ideas. What I want, discuss them to match the tail but Basically, by now operational and quarters. Underlying a lot of stuff. And for example, the diffusion models that we are going to discuss now. They usually happen. Not in the space of images themselves. I will show you interesting pictures that look like they happen in the space of images just to explain things but then we will see that. Actually, if you shouldn't models operate in the latent space of some model. Ah, it would be too computationally. Expensive to have them operate on pixels, it's much easier and much better to have them operate in a latent space and usually it's late in space of what. Usually it's latent space. Of operational encoder. Oh, for modern variation. What encoder? Which actually let me just mention. Maybe one architecture that. You might hear about VQ again. It's it's a rational and quarter with a discrete latent space, which I won't go into but it also adds some adversarial losses inside. So it kind of again, let's not go into details but it's kind of it has the basic structure of operational and quarter. Plus. It has 100% of us that looks at pitches of small patches of the resulting image and make sure they really make sure that the local the small Pages. Look nice and similar to pages from real images. so, there is like a whole separate discriminator there to Make this fine. Local structure, good. And usually like modern diffusion models work in the latent, space of some kind of EQ again or something like that. Anyway. on to the diffusion models. This is our last big idea. and, It's a very, very simple idea in essence and the very, very difficult idea. If I write down in full detail mathematically. So I want okay inspirational and coders the main medical from organization was also pretty simple here. It's it's also additional Bond but much more difficult one. So let me just give you the gist. Give you the the basic idea. And it did Back to 2015. And this this is like the foundational paper and diffusion models. So next time, And callers. And it has a very interesting type of deep unsupervised. Learning using non equilibrium thermodynamics Actually, as an aside physics and thermodynamics, and deep learning are have a lot in common. I'm actually doing some research on the thermodynamics of stochastic gradient descent. If you Go to my website, you will see a Long blog posts with an introduction to this area. It's I think it's it's very cool and there are some real parallels there and there is like an ideal gas law about stochastic gradient descent. So but but here it's in a different sense here, the analogy is different. Here the analogy actually just comes from a basic effect on Markov chains that I'm not even sure you need statistical physics here. I think you don't. The basic idea of Mark chances that well, if you, you can train a Markov chain that we will add noise and we'll add more and more noise. To the input. And after enough steps after some hundreds of steps, the result will be in distinguishable from randomness. Uh, so this this is kind of straightforward, right? If I start with a crisp nice picture and they start just adding gaussian noise to it. Well, I didn't do it to the variant so that you would, you can still see some shade of the of the original. But if you do it like 500 times, of course, as a result, you will see, just the ocean noise that's indistinguishable from from just random sampling. and the point of, Diffusion models is to try and reverse this process. So, you have this noising chain that adds noise. And you want to turn it into a denoise chain? So in the forward Direction, the transformation is distributable. You just add a gaussian nurse in the opposite direction. It's a noise in procedure. Right? So you are supposed to remove ghosts and Noise. Which is of course a much more difficult thing, right? You can't really do it. Exactly. You don't know what kind of noise was added. I mean, you would be able to do it exactly. Only, if you knew what you were supposed to get, if, you know where you're going then yes, sure. You can reverse the process, a conditional on x0, conditional, the original image. But Obviously, we want to apply it without the original image. I want to apply it as a generative model. We want to, then, after training this chain, we want to start with just random noise, and great. Surely turn it into something real. In the turns out, you can still do that. so, the forward chain is just a ghost and backward. Chain is some very complicated distribution, but you can try to approximate it with the ghosts. and then there is a lot of math, which I will skip. So we need to like write down the forward diffusion chain, formally. We need to compress to get closed form formulas for getting like to Several Step Ahead, steps ahead and in the forward chain and then we need to reverse this process. And then we need to derive formulas where we actually reverse it. If we know where we are going. So like conditional not zero, everything is well, maybe not easy, but everything is possible. You can actually do the noising perfectly and in close and analytic form. If you know the result that you know, but then, you kind of do a big variational approximation that jointly proximate every Step in this very long chain and I know it doesn't, I know it. I cannot really explain it without going into a whole lecture on it but Ultimately, we want to get to something like this, so we want to have our Transformations, you will see that they have Theta over here. So now there this parametric Transformations model by neural networks, probably, and we want it to be. So that here SP of xn, we can substitute something very simple like a standard goes and and then after some chain, we will get to a sample from the target distribution of get pictures or whatever to this very complicated distribution. So how do we do that? We approximate. Okay, let me skip this part. This, there's a lot of. So again it's the same idea of rational approximations but applied in quite more difficult way. But in the end, Again, it works. So let me just say that it works in the end, we get A two specific set of loss functions. Well, actually a single loss function, which is a sum of multiple terms and we can write down this terms. They are like Global Library divergences between the oceans or something. And yeah, and we can just take this loss function and optimize it trained and by gradient descent and we can train this parameters of these distributions. Right. So okay, so this is distribution, we don't train this one, this is just standard gaussian but we train the parameters of this distribution. we train the parameters of the transformation that goes, once that and when we train it, when it works, when it becomes a good approximation for the whole organizing chain then, You can apply it like this. You can start with pure random noise and gradually turn it into a good sample and this is your generative model. This is how diffusion models actually produce their results. and, Here in the original paper, so okay. Well let's stop with the mess. Now, in the original paper, it only worked for some really, really small Dimensions so I can see far. It kind of worked on anything larger, they didn't have the capabilities to train it. And for quite a while, this paper just was forgotten. Everybody kind of assumed that. Yeah, it's a cool idea. But it's also difficult. And even if you succeeded in scaling it up, you would still probably would not be able to apply it because you need to. Like to actually apply this reverse chain and this one, you need to go through all the steps. Okay, and if you need to go through all the steps, it means that you need to run your neural network. Hundreds of times because this chain in order for the whole thing to work for approximation to be visible, this chain actually is pretty long. It's in fact on the order of hundreds of steps so, if you need hundreds of brands of your neural network, to get one image, Well, you don't really want to scale it up, right? It's how it begins to sound quite infeasible even if you succeed somehow. So people thought of it as a very interesting work very But ultimately just the Curiosity but then things started happening. Yes, it's started in the DPMS in 2020, the United States division probabilistic models. So I will not explain in detail what they did because they are just a collection of small tricks. but, Basically, they kind of made it work. So did you pay PMS? So some of the other technical problems that diffusion models had And were able to achieve. generation basically comparable basically on par with the best games of the time I showed you some sample Generations from games the last yesterday and A back at the day, they were very good in doing human faces like this and still quite poor in doing anything else because everything else had just was just too diverse it. Had it. What? It was too? They couldn't capture the full diversity. So for example, cat images for again, from Gans for those who look like this, and yeah, and so this was actually kind of state up there but gdpm even though they did excellent generation. They couldn't. They didn't solve this fundamental problem. That I mentioned, they need to go through the chains of times. To make hundreds of steps. So this for nice Generations but they were extremely slow. They took a lot of time to generate this place. but in that very year, they actually solved this problem. Well, not not a different group, but this problem got solved. And again, I will skip the math. But I will just show you this this basic idea. So, the basic idea. Is to switch from approximating a step. So, as the standard diffusion model or ddpm, You go from x t plus 1 to x t. And you approximate going from x t plus 1 to XT. And then you approximate going from XT to XT, minus 1, and so on. So you actually need to to make this step because if you don't make the step you don't know where to start the next step from. Right. So you actually need to go through all of the intermediate points. In DD. I am in the state of trying to approximate the direction to the next point. We are always approximating the direction to the original xero license. The same space, it's just kind of far away and we have this long path that gets us from x capital. And in ddpm we approximate step by step, indeed. I am on every Time slot on every step of the Markov chain. We approximate this whole distraction right to the go. And of course, it doesn't mean that we can just go to the goal in one step. Now that doesn't work, our approximation is not that good. We cannot just jump immediately to a good picture. One gonna happen but we can go quite a bit further. So like in stead of so in GDP, we cannot skip steps because if we skip a step we don't know where to begin. The next one. In TD, I am, I can say, okay, so I'm supposed to get closer to 0 on every step. and then yes, it's an approximation, but I know that on the next step, I will also be trying to get closer to zero so, even if my original chain, Had. Hundreds and hundreds and thousands of steps here. I will go in the general direction of xero just faster. I will just take Wider steps. So and that will will not be a problem. I will not lose where I am lose track of where I am. Because What? Wherever I am my next approximation. My next step will be well trying to go to zero. so, I will not be able to jump all the way there in one step. My approximation will not work like that, but I will be able to like get there in a few dozen steps instead of a few thousand. So ddim. Did like tense or 100x speed up compared to their original. Diffusion models with no loss of quality not much improvement in quality either but that was good enough. And that's where the fusion models actually started working. Right. But it was still slow. It was still expensive. And there was this one last step that people actually needed to do before the fusion models started working completely like the work now. Ah, and that last step I actually already mentioned to you. That last step was. To do the effusion. Not in. The space of pixels like those papers did but in the latent space of some autoencoder. So here is this very famous picture from the paper unstable, diffusion? You probably have heard of stable. Diffusion, it's like the original actually working. Text to image diffusion model, right? It was Done in 2022. So not not that that long ago. naturally, AI image generation has come a long ways since then, but the basic idea still is basically the same And stable. Diffusion works like this. It has a diffusion process. It has a denoising architecture here so it has diffusion model. And as you can see here, we start with ziti and we go through. Network. This network is some kind of Transformer self-attention based unit or whatever, but it's not going to dwelling on the specific architecture doesn't really matter. What matters is that first? This architecture can take a condition And this condition will be, for example, The Prompt, right? So we need to somehow inform the model. What we are trying to draw like this text should go somewhere. And where does it go? Well, the text gets encoded into a vector by some Transformer. And then, this vector Goes. Into. Well, in this case into self-attention blocks like we discussed a couple of lectures back with other attention, but it could be a different architecture, whatever it goes into every device in Step. So every nice step has this conditional thing has this another input. The comes from the prompt. and the most of course, important novelty here is that all of this Happens in the latent space. Okay. so, all of this Happens in the space of vector, representations of images, not images themselves, not pixels. Vector representations. And after this denoising process, we start with random noise with this condition. We go through many steps of the noising, what we get is not an image. But a code that will then be decoded by the decoder. And this guy here, the red part is a rational and coder. Well, a complicated modern irrational, not quite exactly the one I explained to you, but and that's how it works. So, Another similar thing was was done in Daily 2 daily 2. Worked a little bit differently in the because it used a pre-trained clip in bathing suits we did not have time to talk about clip and answering in and contrastive learning can in our class. But clip is this standard way of doing joint text image in bennings so it's like a joint latent space for where both images and Text can go and the idea of value 2. For example, was let's put the text into the space and let's train now. Clip doesn't include this, but let's train a decoder that will produce an image back from the clip representation and also let's train a diffusion model inside. The latent space, that will convert the representation of text in to the representation of the image for the decoder. So again, no details here but you get the idea that diffusion is still happening in the latent space. And that was pretty good. Okay, now, we will love this image but in 2022, this was Completely all inspiring. This is a very famous image from the original mid-journey that one some contests and then it was revealed that it's not, it's a age in your rated and there was this big controversy, the first controversy of this kind. Now, of course, this kontrovers are everywhere. um, The Next Step was to do was what it was called the diffusion Transformer the it And let me I don't I don't have time to explain it in detail. Basically it's the same kind of late in diffusion model but now they use a Transformer instead of a full Transformer, instead of a unit with some self-attention inside. So the difference is in the internal architecture not and they approached, the approach is basically the same. You do diffusion in the latent space of someone encoder. And the it is for good blah blah and this for the samples from the data of 2022 already. Starting to pretty good. Then. there was this flux model, I think it's the last one that I really followed because So again, I don't have time to explain this this picture in detail, but it's also it's, it's the direct successor of stable, diffusion. It was done by the same team, and it was actually very good when it was released. I think, obviously, you can still download and use it. It's not sure if it's the best local model right now. But for a long time, a definitely was ah, and Yeah, flat. I used to use flux for images for my slides, for a very long time. This this is all flux generated. It couldn't do text. It wasn't too good with following detailed prompts on compositions and stuff that the characters do Etc but it was like this huge step forward. And yeah, this is all so flux. By et cetera. and, Unfortunately, after that. After that. it's not like I wanted to stop following but I lost the ability to follow state of the art text image models because now the best models are basically just GPC Right GPT or Gemini. They sometimes switch around for a while and I was veteran. Now, I think GTM, which is two is, again best And of course, nobody tells us exactly how they work. So right now, I have no idea how the best image generation models work. Not because I don't want no but because nobody tells us and yeah my journey still I guess completed for in it was closed from the very beginning so I don't even know exactly how it worked back then. Probably approximately the same. But still. Image generation nowadays is done by diffusion models, promos, probably operating in the latent space of some bigotry encoder. Yeah, so let me skip this. Yeah, and maybe to conclude. To conclude this part of the class and the whole class, actually, the all of the lectures. Let me go back to this picture. And kind of put all the generative models in place on this picture. I guess I already talked through it, but let's let's spend another minute. So, generative models. They are divided, first of all, into explicit and implicit instrumentals. And basically, generative stochastic networks didn't take off. So the only Relevant representative of the implicit and City class is against. And Cancers are still relevant, only their bit more Niche. Now a bit more specialized and they used to be A inexplicit density models. You have this huge class of Auto regressive models. Auto regressive models, like, wave net for producing sound autoregressive models, like language models. Like all of the llms they all are in here because the Transformer decoder produces tokens one by one. Auto regressively conditional on the prefix that it has already generated. Or you can have flow based models. Where you start with a simple distribution and you gradually transform it into something more complicated. Or you can have approximate density models where you do not make assumptions about your distribution but you make assumptions about an approximation to the distribution. And it wasn't clear what it means when I first talked to you about this but I hope today it has become clear so the main so there are two main Representatives here, the virus, the variational auto encoders, they actually The embroider this, right? So, we do not make assumptions on P of Z, given X. We approximate it and then we make assumptions on the approximation. And how does it work through the variational Orbot? The same goes for diffusion models. Again, we cannot make strong assumptions about the reverse chain about this. Denoising chain, what we can do is we can make strong assumptions about an approximation to the reverse chain and then the original Orban So, same approach, the diffusion. Approach is just a bit more complicated. And basically, that's it. So, like all of the stuff that you hear about in the news, is somewhere in this picture and most probably either here. In the water, regressive model or here in Rios. And if you Guess who's there? Want to close our lectures, we have come a long way from the base area back to the bath area today. um, and From the I don't know from the original motivation of neural networks and back propagation. We go to Transformers, we go to variational water. Encoders we go to diffusion models. I think it has been a long journey. I hope it has been an interesting one and thank you. Any questions at this point? Questions, thank you. All right, so thank you very much. I hope we will see each other on Friday still but the lectures are over. Thank you. Bye.
