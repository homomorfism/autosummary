# Transcript — google_stt

- **Provider:** google_stt
- **Language:** en-US
- **Audio duration:** 1:42:49
- **Segments:** 750
- **model:** latest_long
- **use_enhanced:** True
- **latency_sec:** 849.23

## Segments

**[00:11 – 00:15]** Okay, hello everyone and welcome back.

**[00:16 – 00:21]** We have only two lectures left, which is, of course, very little time to

**[00:22 – 00:27]** cover a lot of the January that.

**[00:29 – 00:32]** We actually plan to go on to.

**[00:34 – 00:44]** But still, I think that even until lectures, we can cover a couple of very interesting and very important and still very relevant ideas.

**[00:45 – 00:53]** Today, we talk about January on networks games. It's a beautiful idea, underlying the stuff which

**[00:54 – 00:56]** is completely on my medical. It's like

**[00:58 – 01:01]** it's just very cool and very logical, but

**[01:02 – 01:08]** it leads to very beautiful, made the Matrix a little bit down the road, but before we go there,

**[01:09 – 01:18]** before we go there, let me begin today with the structure of generative a whole

**[01:19 – 01:25]** so, like our first part today will be

**[01:26 – 01:35]** about generative models in general and what kinds of generative models exist in deep learning,

**[01:35 – 01:55]** So when we say generative, AI when we say generative models, what? It's not a very well defined term because, you know, you can say that logistic regression, generates the probability distribution of our classes, right? So the Divide is that in January AI.

**[01:56 – 02:19]** You are producing something big right, your producing an object usually of high dimension and of complicated structure. They can image or like text. So generative models are models that right? That raw, that produce music videos, something like that.

**[02:20 – 02:20]** and,

**[02:21 – 02:37]** When we talk about generative models. So let me draw a taxonomy for you. This will be our first subject for discussion. So of course, I will be talking on about deep generative models. So models that

**[02:38 – 02:41]** Are based on neural networks.

**[02:43 – 03:00]** But and and there is there are several important classes of this models. And today we will live in one of these classes tomorrow. We will live in another but I still want to draw a general taxonomy so that you can actually better understand what's going on.

**[03:01 – 03:13]** The first divide, the first like serious Fork. Inn in deep generative models comes in the distinction between explicit and models.

**[03:16 – 03:17]** I'll explain in a sec.

**[03:18 – 03:21]** and implicit instrumentals,

**[03:24 – 03:24]** so,

**[03:26 – 03:29]** What does explicit and implicit density mean?

**[03:32 – 03:34]** When you have a generative model.

**[03:35 – 03:48]** It takes as input, something like random noise or some condition or whatever. Then there is this black box which are trying to Define. And then at the output there is like

**[03:50 – 03:55]** A picture of a cat or something. There is X that lives in a very high dimensional space.

**[03:55 – 04:02]** and this x has a very complicated distribution, if you if you try to imagine

**[04:03 – 04:32]** As I think I made this argument once in our class, try to imagine the manifold of realistic photos in this three million dimensional space of one megapixel images. Obviously, we cannot imagine anything like that but also obviously it's very very, very complicated, right? So pox the distribution of access that we are trying to approximate that we are trying to model is very, very, very complicated.

**[04:33 – 04:55]** And the difference between explicit and implicit density models. Is that in explicit density models you get an explicit model for the density, right? So like there is this P of X is actually equal to Something in the model and you can actually find out what is it, what is it called to so to speak.

**[04:57 – 04:58]** Naturally.

**[04:59 – 05:11]** We will not be able to approximate. Well, we will not be able to get the actual distribution of, like cat photos, but we can proximate, right? And we can try to approx.

**[05:12 – 05:15]** And then inside explicit density models.

**[05:16 – 05:16]** We have.

**[05:18 – 05:23]** The next divide between tractable density models.

**[05:28 – 05:37]** And let me pause here and explain. So, tractable density basically means that you can have a formula for p of x.

**[05:37 – 05:45]** It makes so such strong assumptions that you actually can just write down. The P of X is equal to something.

**[05:46 – 05:53]** And usually, usually when we say tractable density, we mean an auto regressive model.

**[05:54 – 05:57]** So, not a regressive model.

**[05:59 – 06:04]** Is a model that makes use of this.

**[06:06 – 06:07]** Kind of obvious.

**[06:10 – 06:33]** Identity that if you have this big big X, then you can do something like and you can decompose it into something like pox, one pox to give an X1 pox 3. Give an X1 and X2. And so on until if x and give an X1 X and minus 1, right? So this is always true.

**[06:34 – 07:02]** And of course, since it's always true, it's also completely useless because you are not making anything easier for you. Because this is still a very big function of a lot of variables, but then you can simplify then you can make assumptions so you can make and you can make a Markov chain out of this. You can say that every next X depends on the previous ones, or you can have

**[07:03 – 07:14]** An RNN here which says that okay model is sequence. But every next output,

**[07:15 – 07:17]** Depends on the current input.

**[07:18 – 07:32]** And the hidden state which is also a part of the of the state part of the model variables here, and then you get another simplified in position. So on so of course, it would be a lot of

**[07:34 – 07:50]** Their, a lot of the models that exist happened to be in the auto regressive class. For example, all llms are here, almost, all the lamps are here because LMS

**[07:50 – 08:04]** Predict the next token. So the model text, the sequence of tokens as a sequence of as exactly as this as P of x k. Given the previous context, and

**[08:05 – 08:26]** Then of course the question is how to model this conditional distribution and that's where Transformers come in. That's where all the models come in but the basic assumption is this right? We produce. We generate text one by one. And there have been models for pictures here too. There were things like pixel. CNN.

**[08:26 – 08:36]** That produced Images pixel, baby pixel, and it was a good model in terms of the output. But of course, you know producing

**[08:39 – 09:04]** Images pixel by pixel is just wait to inefficient because you need to generate like a million pixels and running your model. Emilion times is of course invisible even if it's not very complicated. So the pixel Wise auto regressive models are not really used and we want to about them. But but they also accepted it's an actual idea.

**[09:05 – 09:08]** And for text basically, everything is not very aggressive.

**[09:09 – 09:10]** and then,

**[09:12 – 09:23]** Like what else is there that we also will not have time to talk about intractable density. You can have something like flow, a flow based model.

**[09:25 – 09:42]** so, one way to decompose a complicated distribution is to have is to separate it variables inside X, like the autographs of style and another way is to say, well, okay, what if P of X is

**[09:44 – 09:47]** a big composition of simple transformations.

**[09:48 – 09:48]** something like,

**[09:50 – 09:50]** If?

**[09:51 – 10:02]** A composed with f k minus 1 composed composed composed of two F1 of the so we are still modeling something like this.

**[10:04 – 10:18]** And we are doing it. Explicitly each f is a simple thing like Aidan gaussian noise or linear transformation or something like that. But when you compose a lot of

**[10:19 – 10:30]** A simple Transformations like always in your own networks. This is not a neural network but like always in neural networks you get this capability of modeling something much much more

**[10:32 – 10:38]** Complicated, right? So we want to talk about flow-based models no time unfortunately. And

**[10:41 – 10:45]** apart from tractable density, you can have approximately density models.

**[10:46 – 10:48]** So here.

**[10:50 – 11:08]** In a way you could repeat the same structure. But now, instead of modeling P of X instead, of making assumptions about the distribution itself, we explicitly say that like we approximate pox with some simpler queue and now this queue is a product of something easier.

**[11:09 – 11:31]** And here, the main example that is very, very relevant that it's a Pity that probably we won't have time to talk. Maybe we'll talk about them tomorrow. Maybe the main example are very well and coders. This is one of the most important ideas in the hole.

**[11:32 – 11:33]** And deep learning.

**[11:35 – 11:40]** How to use variational approximations to get.

**[11:41 – 12:01]** Good loss functions for generative models and variation of 10 others. I used all the time. And for example tomorrow we will talk about diffusion models and diffusion models, they usually operate in the latent space of a variational. I'm getting a bit ahead of myself.

**[12:02 – 12:12]** So of course explicit density part is like big and area and reach. There are lots and lots and lots of different approaches here.

**[12:13 – 12:20]** The implicit and such is not that rich, there are much fewer.

**[12:22 – 12:34]** Examples here. And actually, I won't even make any other examples because they are kind of as a terrific. The main example of implicit density, generative models are against

**[12:36 – 12:37]** That we just discussed today.

**[12:38 – 12:45]** and what does it mean not to have a density for X, like, how can you have a model that

**[12:47 – 13:01]** A produces access that gives you that gives you cat photos but does not have anywhere formula for p of X or even an approximation to P of x.

**[13:02 – 13:10]** Well, you just have to take this picture literally, right? So, an implicit density model, will start with random noise.

**[13:13 – 13:18]** And then it will actually produce just a sample.

**[13:19 – 13:30]** X, which is supposed to be taken from the distribution. Pure effects. It will produce a simple cat picture that is supposed to be a good cat picture.

**[13:31 – 13:41]** and this and if you look at this way, if you look at your neural network at your model as this,

**[13:42 – 14:03]** Sampling procedure as a sampler. That, well, not a sampler as a transformation of probability distributions from a simple one from random noise, like just standard goes in to this very complicated one in this huge dimensional space Etc. Then it all kind of

**[14:04 – 14:08]** Starts to make sense, right? So if you just have a black box that

**[14:10 – 14:12]** Samples, get photos for you.

**[14:13 – 14:27]** You cannot really extract the formula from this black box. I mean you could maybe make a trillion examples and then learn one of the explicit density models. But that doesn't count the Black Box itself doesn't have the formula anywhere.

**[14:28 – 14:30]** So so this is what again do.

**[14:32 – 14:40]** And now, the first part is over, I've talked about this General structure and maybe we'll return to tomorrow.

**[14:40 – 14:44]** And now, what are games?

**[14:45 – 14:46]** What is their main idea?

**[14:47 – 14:52]** So we talked about January of adversarial Networks.

**[14:56 – 14:57]** Yes.

**[14:59 – 14:59]** and,

**[15:01 – 15:06]** In the general. Sorry, the general Network.

**[15:07 – 15:08]** Is based.

**[15:08 – 15:10]** on this very

**[15:13 – 15:13]** interesting.

**[15:14 – 15:21]** Like it's one possible solution to a very deep problem in generative models.

**[15:22 – 15:29]** And we will discuss other. If we get to wires we will discuss other solutions to this problem.

**[15:30 – 15:30]** but,

**[15:32 – 15:34]** Here is the problem, basically.

**[15:36 – 15:37]** The main problem.

**[15:38 – 15:38]** Of.

**[15:41 – 15:58]** Generative AI in general. I mean it there are many ways to solve it. It's not like it's an open problem but the main deep problem that you need to solve and you create a generative model is what is your lost function? How do you

**[16:00 – 16:02]** Or the results.

**[16:03 – 16:03]** So,

**[16:04 – 16:28]** Let me start drawing this picture for you, right? So I have this random noisy which is basically just taken from some standard distribution or whatever. And then this random noise, he gets to the January Network gets to the model that Maps random noise.

**[16:31 – 16:34]** Two. Something that is supposed to be a cat picture.

**[16:35 – 16:35]** Right.

**[16:36 – 16:41]** Let's call it X head because it will be like a predicted kit not not yet real.

**[16:43 – 16:44]** so,

**[16:46 – 17:07]** Think of it. Okay, let's think of it as a learning problem as a machine learning problem. If you look at this as a machine learning problem, well you do have a data set of access, right? So what does your data look like your data is a lot of gets a lot of cat photos.

**[17:08 – 17:23]** But if you don't have beer data for this, right? You cannot just say that this x had should be similar to some X in in the training set because you have no idea which one, right

**[17:25 – 17:43]** There there isn't and there will never be a data set that pairs random noise with images that are supposed to be produced from this random noise. That's doesn't make sense. The whole point of hearing a generator is to learn this, this may concern so to get

**[17:45 – 18:03]** A good and relatively simple. Parameterization in the noise space. So that next week, we would be able to just take random noise and still get reasonable cat pictures. So the data the data is unlabeled it's it's unsupervised learning.

**[18:03 – 18:04]** but,

**[18:05 – 18:05]** so,

**[18:07 – 18:12]** Where we will the loss function come from, which X should see be.

**[18:13 – 18:14]** similar to

**[18:15 – 18:23]** Well, you can say, okay, I don't have any specifics in mind, I just want the result this x head to be a good cat picture.

**[18:24 – 18:24]** Okay.

**[18:25 – 18:26]** And this.

**[18:27 – 18:34]** Sounds reasonable and this is exactly what we'll do. But what does it mean to be a good cat picture?

**[18:36 – 18:38]** This, this is the Deep question that we need to answer because

**[18:40 – 18:41]** There is really.

**[18:44 – 19:04]** No function no mathematical function that you can run and say if this photo is a cat. Picture is a good cat picture. If this set of picks pixels is a good picture. This is something that you have to learn yourself too, and this is like half of the problem if not most of the problem.

**[19:05 – 19:27]** So change ready for their cereal networks. Say the following they say, well, okay, you recognize that you need to learn your loss function that you need to work for it. You cannot have you do not have a fixed formula for evaluating how Kate this image looks.

**[19:29 – 19:29]** so,

**[19:30 – 19:31]** Let's do it.

**[19:31 – 19:37]** Let's work for it. Let's have a whole separate Network called a discriminator.

**[19:42 – 19:43]** That.

**[19:46 – 19:48]** Who's only?

**[19:50 – 19:55]** Go who's only job is to say whether?

**[19:56 – 20:04]** The input. So, as input, it takes photos and as output, the dust just binary classification. Is it fake?

**[20:06 – 20:10]** Or is it real? Let's say the trails one. Because 0

**[20:12 – 20:14]** So, the discriminator gets a picture.

**[20:15 – 20:18]** and if it's a picture produced, by the generator,

**[20:19 – 20:23]** Then it should say that it's fake.

**[20:24 – 20:24]** Right.

**[20:24 – 20:32]** And if it's a real picture, so we can, we can take our data and we can sample a real cat photo from it.

**[20:33 – 20:40]** Right. This will be real x x real and this is X fake.

**[20:41 – 20:46]** So, if a real picture is fit into the discriminator, the output should be one, right?

**[20:49 – 20:56]** In this way, the generator and the discriminator are at with each other, they have opposing interests.

**[20:57 – 21:06]** They discriminator wants to learn to distinguish between real images and images produced by the generator and the generator wants to fool the discriminator.

**[21:08 – 21:13]** So, this general idea is called adversarial training.

**[21:15 – 21:15]** and,

**[21:18 – 21:44]** You may hear that like games are not what they used to be and indeed games are not for the last few years. Cans are not at the Forefront of image generation. The images, they start Generation by the fusion models which will talk about tomorrow but Reserve training is very much alive. And even in the diffusion models we will see

**[21:45 – 21:54]** Exactly this idea. And we will see like a little bit of again, embed it into a diffusion model and making it better.

**[21:55 – 21:55]** So,

**[21:56 – 22:08]** This is, of course, still very important idea in machine learning, and it appears in many different fields. Of course, we're only talking about images, but still

**[22:10 – 22:10]** so,

**[22:12 – 22:18]** Let's now, okay, so let me maybe show you some nice pictures. I think I have the

**[22:19 – 22:34]** intra pictures about games. This is the main idea. And as you can see, it's very simple, right? So the generator is like Fortune a picture and they discriminate or is the detective that needs to decide whether it's real.

**[22:35 – 22:36]** and,

**[22:37 – 22:39]** Ideally.

**[22:40 – 23:15]** It should look something like this. So at first, so this this is an example where like the generator which is called Traverse, tip convolutional neural network here, the generator, learns to, like, counterfeit money. There is to produce pictures of real money, and at first, it just produces something. Actually, this is a few steps in because at first, the generator will just produce random noise. But then like it produces some very bad counterfeit and then the discriminator will say, oh, well,

**[23:16 – 23:32]** I don't know any better. So this this seems legit and I am full, okay? So I I provide once on on fake images. So then we train the discriminator

**[23:33 – 23:43]** and now it learns to distinguish, it understands that this is not real money, not real American dollars and then we

**[23:45 – 24:14]** Actually often, it's done. Exactly like this. So we fix the discriminator that has trained for a while. And now we train the generator to full this current version of the job of the discriminator. So we say, oh, okay. Now the discriminator doesn't accept our counterfeit. What what should we do? Let's train a little bit more and produce a slightly better counterfeit. It will still be bad it. Because again there is no.

**[24:18 – 24:29]** General loss function. That will tell you if the image is good, there's only this specific discriminator that has learned to not before by some attacks.

**[24:30 – 24:30]** so,

**[24:32 – 24:57]** This point, it will produce a better counterfeit and then this commentary will find some other features to discriminate on and then the generator will have to learn to fake those features. So and so on so there they're kind of playing this game and they and they hope is that everything happens. I will walk through the formulas in a minute but the hope is that everything happens like on this idealized image.

**[24:58 – 25:18]** So here for example, the generator is represented by this arrows, this arrows, as you can see in the we have the uniform distribution every time and in X we have like this, gaussian the green gaussian, and the black dots are the data points. And so, at first,

**[25:19 – 25:35]** This gaussian doesn't look like the black dots. So they blue dashed line is the discriminator. It's just Logistics Sigma, right? So it's a sigma it, curved that distinguishes between these two gaussians and then here is the crucial part.

**[25:36 – 25:38]** at this point, the discriminator

**[25:39 – 25:40]** Trains. But

**[25:41 – 25:43]** It's not training to mimic the data.

**[25:44 – 26:00]** Because that is impossible. I mean in this case it would be possible but in in the high dimensional case of pictures it would not be possible. So the discriminator learns to fool the generator, learns to fool the discriminator

**[26:01 – 26:26]** So in this case, it's enough to move this gaussian little bit over here and they discriminator is already folded. It doesn't need to go all the way to the data points but then of course, the discriminator will be able to distinguish between these two bills and so on. And finally we will get to this perfect picture where the generator is perfect and the discriminator has no idea what to do and just flips a coin.

**[26:27 – 26:30]** So of course, in real life, it's not gonna work like that.

**[26:31 – 26:34]** But the idea is exactly this.

**[26:36 – 26:38]** So, what is interesting?

**[26:39 – 26:40]** About the problem setting here.

**[26:42 – 26:49]** Well, let's write down the loss functions. Let's let's see like mathematically. What is happening here?

**[26:50 – 26:56]** So first they discriminate, right? So what is the discriminator was LD?

**[26:58 – 26:59]** Well.

**[27:00 – 27:02]** Let me write it in in this form. So,

**[27:03 – 27:08]** The discriminator is supposed to say 0 if it's fake and one, if it's real.

**[27:09 – 27:22]** So, let me write this as expectations doesn't really matter, but this will be cleaner for for what comes in next. So if I take a real photo,

**[27:24 – 27:26]** From the data set.

**[27:27 – 27:42]** From the training set, then I am supposed to like increase the output. I'm supposed to produce the score that goes to positive Infinity, so the probability of the sigma, it will go to one.

**[27:43 – 27:51]** So, I am supposed to increase to have a loss function, something like log D of X actually, might minus will be your website.

**[27:52 – 27:53]** and then,

**[27:54 – 27:57]** If x is fake.

**[27:58 – 28:00]** So X fake.

**[28:01 – 28:13]** Is taken of where is it taken from its taken from the distribution of the generator? Sorry, not xpg of Z, right from the distribution of the generator.

**[28:14 – 28:17]** No, actually it's video effects, right? So I'm

**[28:18 – 28:24]** I'm taking it from this distribution from the distribution that has come through through, through the generator.

**[28:25 – 28:30]** Then I am supposed to Output zero, so I'm supposed to do something like this.

**[28:32 – 28:32]** Right.

**[28:33 – 28:35]** and,

**[28:36 – 28:40]** And I want to minimize this loss function.

**[28:41 – 28:44]** With respect to the parameters of the discriminator.

**[28:44 – 28:55]** So when I, when I fixed the generator and I just train the discriminator, this is a very straightforward like binary classification problem.

**[28:56 – 28:58]** What does the generator do?

**[28:58 – 29:00]** Well, the generator.

**[29:01 – 29:08]** Is supposed to produce access that pass for real for the discriminator.

**[29:09 – 29:10]** So basically,

**[29:11 – 29:28]** I mean, it cannot influence this part there is no generator here, but for this part, the job of the generator is exactly opposite to the discriminator, right? So let me write it now. Completely, we start with some random noise.

**[29:29 – 29:38]** And then I want to actually take the discriminator loss on my results from Josie.

**[29:39 – 29:40]** and,

**[29:41 – 29:48]** Do the opposite. So if here I was minimizing minus this and here I will be minimizing Plus

**[29:49 – 29:50]** Right. So

**[29:53 – 30:03]** basically, you can say that the discriminator and the generator have the exact same loss function. I can just copy it here, it won't matter because it's just a constant for the generator.

**[30:04 – 30:06]** And what they're actually doing.

**[30:08 – 30:17]** If let's say that I have this loss function, that depends on the parameters of the generator and parameters of the discriminator for this loss function.

**[30:18 – 30:22]** Let's say that the discriminator wants it to be.

**[30:24 – 30:31]** As being as possible. So let's say that. Okay, this is the loss function. The thing in the brackets

**[30:32 – 30:32]** so,

**[30:34 – 30:36]** the discriminator wants to make it bigger.

**[30:37 – 30:40]** And the generator wants to make it smaller.

**[30:42 – 30:45]** So we have this Minimax game.

**[30:46 – 30:48]** It's actually.

**[30:50 – 31:00]** Something that has never happened to us in machine learning before and that will not happen since we are not just doing optimization here.

**[31:01 – 31:08]** At least formally we are doing adversarial optimization in the sense of Game Theory.

**[31:08 – 31:09]** And if you

**[31:11 – 31:17]** if you have ever had any classes in Game Theory or anything, you know that

**[31:18 – 32:08]** As soon as this quantifiers, this optimization goals like min max, max me and Etc. As soon as they start to stack up, as soon as you have like a Minimax instead of chest. I mean or just a mix the complexity of the charts, right? So it's it's extremely hard. Extremely difficult to actually optimize for in Game Theory and on the surface of this and it looks like this is this should be hopelessly difficult problem. I mean for us it's hard enough to do just minimization to, just be minimize the Lost function. And here we are asking to do a Minimax. So basically Define the equilibrium and the game. This is this sounds completely impossible.

**[32:09 – 32:55]** Well, in reality, of course, it's not impossible. And the that there are some properties of this loss functions that make it that make it simpler. And I will not go into the mathematical details, but basically let me just tell you the result here. Basically, if you fix the generator, then you know exactly what the optimal discriminator is because it's just the optimal base and classifier remember bias formula. So here, if I know the data is distribution and I know the generator distribution PG, the answer is just

**[32:56 – 33:11]** the best role. So they probability that X was real, is the density of EX underpaid data. Normalized to the summer of predate and PG, right? This is exactly the best role.

**[33:13 – 33:38]** Are and then like so this is straightforward, but the interesting part is that now you can take this formula and you can plug it into the generator loss and what you get is, basically a very simple result. You get that the generator is perfect. The attains the global minimum of this Criterion, if

**[33:39 – 33:46]** Pg' equals to data. So the this, this verifies that we are actually doing the right thing that the generator is actually.

**[33:48 – 33:52]** Minimizing is actually making PG.

**[33:54 – 33:56]** Closer to the true data distribution to predator.

**[33:58 – 34:00]** In fact.

**[34:00 – 34:15]** It's doing it in a pretty interesting, non-standard way. So for optimal for the optimal, discriminator the generator actually is minimizing this

**[34:16 – 34:28]** Johnson and aberrations. Not the cool book Library versions between the distributions, which we usually minimize machine learning, but like this average symmetrical,

**[34:29 – 34:36]** The version of Kyle where which is called the instance Jansen Shannon Divergence.

**[34:38 – 34:44]** And I won't go into details about this results. I don't want to discuss them further because

**[34:45 – 34:47]** Unfortunately, there are completely irrelevant.

**[34:48 – 35:09]** So everything that we can say this, theoretically about this kind of Minimax problems and you know, the game theory stuff here and how we can substitute the perfect discriminator into the generator was function, Etc. All of this.

**[35:10 – 35:16]** Makes the assumption that we are actually.

**[35:18 – 35:22]** We actually have this common was function for the generator in the discriminator.

**[35:23 – 35:37]** And that's just not throwing practice. So, in practice, it turns out that this kind of generator loss, they like just take the binary presently from the discriminator and flip it. This is a very bad idea for the generator.

**[35:38 – 35:40]** And why? Because

**[35:42 – 35:52]** It saturates and that's exactly the same problem that we discussed in the appearing several times. Again, I don't have time to go into full detail here, but basically

**[35:54 – 35:54]** This.

**[35:55 – 35:59]** Thing, this cross entropy is the output of a sigma.

**[36:00 – 36:12]** And if it's actually, it's right so if you're classifying it in the, if your classifying it like the discriminator does.

**[36:13 – 36:27]** Actually a good thing at least not a bad thing. Like if you you search for it, when you give the right answer and that's fine. So if you are already giving the right answer and you're confident in in this

**[36:29 – 36:32]** And and your confidence in this area.

**[36:36 – 36:42]** You are confident in this decision in the right decision, then you don't need to change anything, right?

**[36:43 – 36:58]** But now I have when you look at the generator, if the discriminator is very certain that it's true, that's right. And they discriminator has saturated and doesn't and it's doing a very good job.

**[36:59 – 37:08]** It means that the generator is failing, it means that the generator does not produce believable results, the discriminator is easy. It's easy to distinguish for the discriminator.

**[37:09 – 37:12]** So, this is the situation where we are supposed to.

**[37:14 – 37:23]** Train the generator. We are supposed to like actually update its weights, but we can't, because in the back propagation,

**[37:24 – 38:00]** This. The the loss is only over here. So, the gradients for the generator, have to go through the gradients of the discriminator. And as I just said, the gradients for the discriminator become near zero because the discriminatory saturated and already working very well. So, if I reuse the same loss function, it's really a better idea because it means that when the when I have trained the discriminator and then practice there is this alternating training usually. So we train the discriminator, then the generator and discrimination.

**[38:01 – 38:11]** When I trained the discriminatory little and it becomes good at separating stuff. This is exactly when it's gradients become near zero and the generator is very hard to train.

**[38:12 – 38:15]** So the same effect that we had in slightly different form.

**[38:17 – 38:25]** As you can see, I am teaching you General ideas that appear over and over the same as a result training today. So,

**[38:26 – 38:32]** So what do we do? Well, we changed the loss function, and let me skip the

**[38:32 – 38:46]** Early attempts at changing this loss function. Let me just show you the path that we have the the original against how they worked.

**[38:47 – 39:15]** And that was what 12 years ago and that's 2410 and in 2014 as you can see, on this picture. So the green ones are like real training samples, there near us, Neighbors From the training set, to the next, to the name of the chest picture right here. So you can actually verify that. The model did not just memorize a few elements of the training set, but that's actually generating stuff.

**[39:16 – 39:28]** So as you can see, it worked wonderfully for Ms. And it worked much worse for this small, black and white human faces and the basically was

**[39:28 – 39:34]** Very bad for anything else. For anything more diverse.

**[39:34 – 39:42]** So, in 2014 against appeared but they were no match to other generative models at that point.

**[39:44 – 39:45]** So what happened next?

**[39:46 – 40:06]** Next there was this again this again is basically the same kind of game but with a new better architecture. Convolutional architecture for the January and the discriminator again. No no point in going to the details but I want to make one remark here. So

**[40:08 – 40:14]** In. So, this again, already started to produce some reasonable pictures on some data sets.

**[40:14 – 40:16]** Still very small, still.

**[40:18 – 40:28]** Obviously better than some ways. It was 10 years ago, image generation was very bad back at the time. So this was actually a state of the art and years ago.

**[40:29 – 40:42]** And yeah, just a side remark. Yeah. If you look through old papers on gants, and on Ys, and on very generative models, you'll see a lot of bedrooms.

**[40:42 – 41:00]** I don't know who started it but at some point like there is this data set called large-scale, not large scale large-scale scene understanding. So as you stand for scene understanding and it basically is like several subsets of photos from different environments.

**[41:01 – 41:15]** and one of them was a bedroom and first, once somebody chose this set of pictures for their tests and of course, after that, everybody had to follow suit and had

**[41:17 – 41:24]** compared their bedrooms with previous better. So you will see a lot of bedroom pictures they are.

**[41:25 – 41:34]** Relatively small, like, I think 64 by 64 pixels for maybe one 28 by 128 something like that.

**[41:34 – 41:56]** But they are in color, and they already kind of are supposed to look like real forces. And this is DC again after one epoxy still very bad, but after five epic sets to be like more or less, okay? So nothing obvious nothing. Exciting by today's standards, but back then it was okay.

**[41:56 – 42:01]** And what I wanted to mention here, is this idea. So this this is important like,

**[42:03 – 42:04]** again, how do you

**[42:05 – 42:21]** Illustrate. How do you understand yourself that you've got a good generative model? They discriminator will not tell you that because the discriminator will tell you. Oh, I can't distinguish. It doesn't mean that the pictures are good. It doesn't mean that the latent space is good.

**[42:22 – 42:39]** It just means that the discriminator can distinguish. Maybe you didn't train it? Well enough, maybe it's not large enough, it's not powerful enough, who knows, right? So how do you well, maybe not measure the metrics are different story, but how do you

**[42:40 – 42:44]** At least, see for yourself. If the generator actually makes any sense.

**[42:45 – 42:53]** And the usual is illustration goes like this and I want to explain it because it's really a good.

**[42:55 – 43:00]** It's a good illustration. So what we are doing like

**[43:00 – 43:03]** intuitively geometrically in the latent space and so on.

**[43:05 – 43:08]** So what is the generator actually?

**[43:10 – 43:20]** It's taking the this random noise this Vector from the latent space, the so this will be the latent space.

**[43:23 – 43:25]** and its mapping the

**[43:26 – 43:26]** two.

**[43:29 – 43:35]** Point x, which is in pixel 6 space. So to say,

**[43:36 – 43:36]** Right.

**[43:38 – 43:38]** and,

**[43:39 – 43:48]** In pixel space in this huge million dimensional space of images. The actual images that we are looking for.

**[43:49 – 43:59]** Form. This extremely complicated and completely and un understandable manifold, right? So they have this very, very complicated structure.

**[44:00 – 44:02]** But in the latent space.

**[44:04 – 44:04]** Our goal.

**[44:05 – 44:08]** Is to actually like flat in the structure completely.

**[44:09 – 44:22]** Because what is our goal, really? Our goal is to be able to generate new images, right? So our goal is to be able to do the following to take a random deal over here.

**[44:23 – 44:40]** He from a standard Gauss, right from some very simple distribution, doesn't matter if it's the gaussian specifically. But Z from some very simple distribution that we can sample from directly and take this random noise,

**[44:41 – 45:02]** Put it through our generator method over here and actually hope that the result will fall in this. Extremely complicated, very difficult. Completely under animation of real pictures, real photos,

**[45:03 – 45:04]** Right. So

**[45:05 – 45:09]** this is the job of the generator. Here is the January, right?

**[45:16 – 45:22]** So how do we test this? Like how can we understand if we actually did a good job in this?

**[45:24 – 45:36]** Well, here is one test that was very popular and that you can immediately see for yourself, it's very Visual and the test is, let's do a linear walk in the late space.

**[45:37 – 45:39]** so, in the latent space,

**[45:41 – 45:50]** if I take for example, two differences, one here, one here so they will produce two different pictures

**[45:55 – 46:00]** They will produce two different pictures, right? The green one, and the orange one.

**[46:02 – 46:27]** Then in the latent space, if I'm supposed to get them from a standard gaussian, it means that if I just walk from one of these East to the others, this is E2. And that one was, he won. So if I, if I want to walk, if I walk from one random sample to another random sample over here,

**[46:30 – 46:34]** this I can do just along a straight line and along the straight line.

**[46:36 – 46:38]** all of the intermediate, this

**[46:39 – 46:43]** Should give me reasonable images. Okay, this is the main test.

**[46:43 – 46:47]** so, if G, if the generator,

**[46:48 – 47:00]** Was stupid and it was not doing much and they just memorized a few data points and then disease would get mapped to this data points. It will still look good on the training set.

**[47:00 – 47:13]** But if I go from one Z to another, then here it would do something nonsensical. Like, for example, it might walk along a straight line and in the pixel space.

**[47:14 – 47:17]** and if you go along the straight line and the pixel space,

**[47:18 – 47:35]** you don't get realistic photos, right? You get like one photo and then the other kind of, you know, appearing through it. And it's like you're making one of the more transparent and the other shows up underneath underneath so,

**[47:36 – 47:39]** It's, it's definitely not a walk through realistic photographs.

**[47:41 – 47:46]** What you are supposed to have in the perfect in the ideal case?

**[47:46 – 47:49]** As a walk in the pixel space.

**[47:50 – 47:53]** That all. So follows this manifold.

**[47:54 – 48:02]** And goes from one next to the other. So on every intermediate step through this straight line,

**[48:03 – 48:05]** You are supposed to get.

**[48:07 – 48:24]** A realistic photo somewhere on the manifold. And if you get that and if you see it like consistently true, then it does mean that you can sample. Or at least you can hope to sample random season and get realistic images, right? So if you

**[48:25 – 48:36]** Look in this again, papers and generative models. You will often see this kind of walks through the feature space or late in space,

**[48:37 – 49:12]** the left and the right part are like actual images or something from the training set or some images that are like guaranteed to be good. And now you walk through the latent space and you see. So in the latent space you walk along straight line and you see what happens in the pixels space. And as you can see here, there may be some strange stuff happening in the middle but more or less. They're all kind of rare listing at least on the same level of realistic as the images on the side.

**[49:13 – 49:13]** So,

**[49:15 – 49:22]** So this this was, I think, the first game, which was already at the state of the art of famous generation.

**[49:24 – 49:28]** It even had some kind of factor arithmetic, it didn't work out later. So let me skip that.

**[49:29 – 49:32]** but also, that was the

**[49:33 – 49:39]** the time when against they were already state of the art, and

**[49:41 – 49:50]** What I just showed to you. What's indeed state of the Artemis generation. 10 years ago, you can again Marvel at the progress at the rate of progress.

**[49:51 – 49:52]** but,

**[49:53 – 50:18]** They were still kind of bad. You wouldn't use them for generating like a production images like today, I obviously generate cat pictures like this one, and I like the results. But back then these are not real bedroom photos. And back then there were some common

**[50:20 – 50:41]** Problems with Generations specifically with Guinness generation that you may remember. I mean they were all across the internet and stuff like that were like common failure modes of games and maybe he will actually see some failure. Most like this in your practical sessions.

**[50:42 – 51:06]** So they definitely had problems with counting. I mean, the recent meme was about six fingers on a hand, like a couple of years ago. It was still a problem today. It's not. But back like 10 years ago, it was much worse than six fingers on the hand. Right there would be like three heads of a dog with who knows how many eyes.

**[51:08 – 51:12]** and that actually makes sense as a failure because

**[51:13 – 51:33]** When you look at something like this reversed convolutional Network, what it's doing, is it, it has this general idea, the general feature and then it's specialized and that, like drawers different parts of the image then more or less independently. And basically, what this failure modes means is that, well,

**[51:34 – 51:35]** I am here.

**[51:36 – 51:59]** And I only have a small context around this eye, so I'm not really sure is it the right tire or the left eye and I decided. Okay. So maybe it's the, maybe this is the right. I need another one and then I do the other one. Again, I'm not sure. Is it the left or the right? And again, I do another one. So, I think the mechanism was something like this

**[52:00 – 52:20]** Yeah, and the same goes for like problems with perspective. So here I I was generating this dog and they go to the head of the dog and now I don't have enough context to understand what was the angle. I was looking from. And now the other half of the dog is from a different, completely different thing.

**[52:21 – 52:27]** And actually this stuff is hard so it this kind of mistakes.

**[52:29 – 52:55]** They stand out for us because our vision is very good. We know the world we know how it's supposed to look like and we learned it in the first years of our lives, but it's actually very very difficult. And this kind of, for example perspective, generating stuff and proper perspective as if it was a three-dimensional world is really difficult. And for example

**[52:56 – 53:10]** Among the signatures if we're flying and I would say erase your hands but just how many of you actually realized that one of these images does not belong here.

**[53:13 – 53:30]** Um, and usually, it takes a few questions for people to actually see that. This cat over here is just a real photo. There is nothing bad about this. It's just a cat, which is sleeping all curled up like this cats. Do it, right? So

**[53:32 – 53:37]** It's, it's difficult and it was it was difficult.

**[53:38 – 53:38]** but,

**[53:39 – 54:10]** Imagination has made tremendous progress and this picture. Of course, I have been showing it since 2018, but honestly, you can extend it. There are, of course, newer and better models for human faces, too. But it would be points list because in 2018, you already, probably cannot see the imperfections. There are imperfections here, but on a slide, I don't think you can see that.

**[54:11 – 54:27]** So, but in 2013, I think you can see, right? And you can actually see how how much progress game-based generation made between in just this four or five years.

**[54:28 – 54:30]** So how did that happen? What are the main ideas?

**[54:31 – 54:31]** Again.

**[54:32 – 54:57]** Let me concentrate on the important ideas and the technical ideas. I will just pass through very quickly and I I want to discuss with you at least one conceptual, very interesting idea. One idea that again, bring maybe illuminates, what's happening? And all of this latent spaces and stuff.

**[54:58 – 55:00]** but the technical idea was that

**[55:01 – 55:09]** An important. Also, an important technical idea was that well you don't have to generate a whole picture at once.

**[55:11 – 55:11]** and,

**[55:13 – 55:21]** The implementation of this idea was the following. You can have, what is called the conditional again? Like when you give a condition and you

**[55:24 – 55:26]** expect the output to change depending on the condition.

**[55:28 – 55:38]** And one like specialty relatively simple version of conditional generation is called super resolution.

**[55:38 – 55:55]** It's still generation because you are inventing, new stuff, but super resolution is like this problem where you have a low resolution image and you want to make it into a high resolution image, so you're like you're replacing every pixel width 4 pixels, or something like that.

**[55:56 – 56:02]** And this is a change generative problem because again, the information is not there, you have to invent it.

**[56:03 – 56:15]** But it's a much easier problem than just making new images from scratch, right? Because the image is basically here, you just need to you know get some details right?

**[56:16 – 56:28]** And so the idea for General generation was, well, why don't we start small? And then just do like a sequence of super resolution.

**[56:29 – 56:44]** This was called program Progressive growing again, and this is the game that gave us this guy in 2017. There was a website called this person does not exist, which was kind of famous back then, but I don't expect you to remember

**[56:45 – 56:47]** and,

**[56:48 – 57:04]** So how does it work? Very simple. You have a data set of human faces, you want to generate human faces. So your first game pretty simple generator. Pretty simple discriminator and it turns to generate

**[57:05 – 57:06]** 4 by 4.

**[57:07 – 57:16]** Human phases, human faces with 4 by 4 pixels, trust me. You can do it even from scratch. It's not a hard problem. 16 pixels are. Okay.

**[57:17 – 57:26]** And then you use this generated 16 pixels as the condition to do super resolution and to do an 8 by 8 image.

**[57:27 – 57:46]** And then 16 by 16 and 32 by 32 and so on and so on. And then you train it for quite a while and like, in two weeks, you get in two weeks of training back then that was one of the first famous results from Nvidia. But then in media was only starting in the AI world.

**[57:47 – 57:58]** But they already, of course, had a lot of compute. So after two years of training like this, you know,

**[58:00 – 58:05]** sorry, two weeks of training like this here. You get to one megapixel Mission, that's pretty.

**[58:06 – 58:23]** So, the architecture is very simple, etc. Etc. And you can later, you can click on the links on the time on this, but there are some nice long videos of exactly this walks of the latent space and they look pretty cool.

**[58:24 – 58:26]** Even into 2018, they look pretty cool.

**[58:29 – 58:31]** But this is not the interesting part.

**[58:33 – 58:34]** This is,

**[58:34 – 58:39]** Still an idea that is useful and it's still applied. But the interesting part.

**[58:40 – 58:43]** Is what did the use for the loss function?

**[58:45 – 58:45]** Well.

**[58:48 – 58:58]** They actually by the time there were two main loss functions in games for the generator and for the discriminator 2.

**[58:59 – 59:20]** One of them was the least where scanner. I don't want to spend time on the list Square scan because oh, it's solving the same kind of situation problem and that's only it in a relatively straightforward way. So it just says, well instead of having a sigmoid let's just have

**[59:21 – 59:23]** a square deviation. So

**[59:24 – 59:39]** instead of saying, oh, I want my deal of x to be as large as possible and it goes through the same way and become close to one. I just say, Okay, I want my idea of x to be close to a constant, like a constant one or something.

**[59:40 – 59:50]** Ah, and which means that overshooting, this constant is also bad. So, nothing goes to Infinity. Everything is supposed to Cluster around this target constants.

**[59:51 – 1:00:08]** And usually in classification, it's a very bad idea. If you were doing like detailed class on with the first part on linear models. I would explain to you why it's better yet, they usually squares for classification, but here it works because it solves the situation problem.

**[1:00:10 – 1:00:10]** but,

**[1:00:12 – 1:00:25]** And I will skip this. Yeah, I will skip the authority ideas don't have time for them but the interesting idea here. Let's make a point three in this will be our

**[1:00:25 – 1:00:27]** I guess the main content.

**[1:00:29 – 1:00:31]** Is called wasserstein games.

**[1:00:33 – 1:00:52]** Or W again. Sometimes you see the abbreviation is famous mathematician, whatever, but I want to explain the and I will not explain all the maths, it's traditional for us, but I want to explain the maturation because I think it's really cool and really right?

**[1:00:54 – 1:00:56]** ah, so, um

**[1:00:57 – 1:01:01]** What is MasterChef again? What problem is it solving

**[1:01:01 – 1:01:06]** Well, what is the goal of our generative models? We want

**[1:01:07 – 1:01:20]** PG of X our distribution at the output of the generator to be close to pidato effects, right? To distribution of the real true photos.

**[1:01:22 – 1:01:26]** Are, what does it mean that one distribution is close to the other?

**[1:01:27 – 1:01:35]** Well, in machine learning. Usually it means that we are minimizing what is called the cool book. Why are they originates?

**[1:01:35 – 1:01:39]** I think I already mentioned it today, but let me remind you

**[1:01:40 – 1:01:52]** I hope you if you've heard of this term before. So Kyle from P to kill something like the integral of P of X time slope

**[1:01:53 – 1:01:56]** of x divided by Q facts. Yeah.

**[1:01:58 – 1:02:20]** And when he and Q are the same, this look becomes zero, right? The friction becomes one. And this this little becomes zero and the Callback Library diversion Divergence goes to 0, goes to zero, as let's say, Q goes to P or p goes to kill or whatever. Right?

**[1:02:21 – 1:02:22]** and usually,

**[1:02:24 – 1:02:30]** In machine learning, when you want to make one distribution, similar to the other, you are minimizing something like this.

**[1:02:31 – 1:02:42]** And it's a long story, there is an important difference between minimizing, Kyle from P to q and Kyle from Q to P. Because as you see, it's not symmetric.

**[1:02:43 – 1:02:46]** Different properties, whatever. It's it's not the point now.

**[1:02:47 – 1:02:50]** the point now is actually

**[1:02:51 – 1:03:02]** Very interesting. So, let's so, usually, we are doing this in relatively like, small spaces, right? But

**[1:03:04 – 1:03:04]** Here.

**[1:03:05 – 1:03:13]** In January fair, I in image generation models. For example, we are doing our X is this.

**[1:03:14 – 1:03:14]** very,

**[1:03:15 – 1:03:22]** High dimensional, Vector of pixel values, right? So, it's it, it leaves in a very big space.

**[1:03:24 – 1:03:24]** and,

**[1:03:26 – 1:03:31]** The actual distributions, both be dated and PG.

**[1:03:32 – 1:03:34]** Are actually concentrated in.

**[1:03:34 – 1:03:36]** Low dimensional.

**[1:03:40 – 1:03:42]** In low dimensional.

**[1:03:45 – 1:04:02]** Subsets subspaces manifolds in this high-dimensional space. So I will try to draw like two-dimensional picture because that's all I can do. But if you're looking at two dimensions, then it's like, here is we are leaving on the plane.

**[1:04:03 – 1:04:07]** So the plane is like the space of images and P data.

**[1:04:08 – 1:04:10]** Is actually concentrated.

**[1:04:12 – 1:04:21]** Along just a single line along one dimensional Subspace of the plane, right? So this is Benedict, this is our goal. Let's say

**[1:04:22 – 1:04:23]** And our model.

**[1:04:24 – 1:04:28]** Something like this our PG or P model or whatever.

**[1:04:30 – 1:04:34]** Well, it's concentrated along some other straight line.

**[1:04:35 – 1:04:38]** Right. So this looks very natural because

**[1:04:39 – 1:04:53]** It's the generator changes random noise which is lower dimensional into into an image. So by definition, it has a low dimensional thing here and the data

**[1:04:54 – 1:05:03]** I mean, also kind of obvious that they realistic cat photos, do not take up the whole image space, so it's also in a low dimensional manifold

**[1:05:04 – 1:05:13]** And our goal is kind of to you know match these two distributions. We want to make the purple distribution, similar to the green distribution.

**[1:05:14 – 1:05:15]** Here is the problem.

**[1:05:16 – 1:05:20]** If they are both low dimensional, manifolds it means they don't really overlap.

**[1:05:21 – 1:05:22]** It means that.

**[1:05:24 – 1:05:24]** If?

**[1:05:25 – 1:05:26]** The data.

**[1:05:27 – 1:05:33]** Of X is non-zero. Then probably P of x is 0.

**[1:05:34 – 1:05:35]** And twice, averse.

**[1:05:36 – 1:05:38]** if PNG of x,

**[1:05:38 – 1:05:45]** Is non-zero. Then probably Predator effects is 0 with probability one. Basically.

**[1:05:48 – 1:05:57]** Because again, their supports are different. We cannot just hope to you know in the very beginning to just get the right manifold, that's not gonna happen. We are going to get a different menu.

**[1:05:58 – 1:06:00]** We're going to get a different straight line on the plane.

**[1:06:01 – 1:06:03]** And our goal is supposed to.

**[1:06:04 – 1:06:09]** Be like to move this straight line to the to the correct straight line to the straight line of pay data.

**[1:06:11 – 1:06:11]** but,

**[1:06:12 – 1:06:17]** we can't, because if something like this happens,

**[1:06:18 – 1:06:26]** the cool book liner Divergence has become meaningless. They become infinite basically. So I integrate over this space.

**[1:06:27 – 1:06:31]** and whenever pox,

**[1:06:32 – 1:06:47]** Is present P of x is 0. So I am integrating over something here. I'm taking the expectation. And I'm thinking the expectation of something, which is basically always infinite.

**[1:06:49 – 1:06:51]** Not a good idea or the other way around.

**[1:06:53 – 1:07:03]** If Q is non-zero, then peace zero and all that doesn't make. So if I write down Kyle from here, the nothing changes, it's still interested.

**[1:07:05 – 1:07:12]** And this means that if I keep using something like the book, cover their versions,

**[1:07:13 – 1:07:32]** I will not be able to train anything because if I to be my generator a little bit and I move this straight line a little bit, let's say then it will still not be mentioned the green line, right? It will still be different and they versions will still remain in infinite.

**[1:07:32 – 1:07:41]** Or and I will not be able to distinguish between the correct direction and the wrong direction. So I need to understand and what direction to move the straight line.

**[1:07:42 – 1:07:47]** And I can't this this kind of losses. Don't don't say anything about this.

**[1:07:48 – 1:07:49]** Okay.

**[1:07:50 – 1:07:55]** Here is a question. I hope you understood what the problem here is.

**[1:07:56 – 1:07:56]** but,

**[1:07:58 – 1:08:01]** It sounds like it kind of invalidates the entire field of machine learning.

**[1:08:02 – 1:08:17]** Because we are always in a way, trying to do this. We are always trying to manage distributions and pretty careful. They are going to be on separate Subspace in separate Subspace.

**[1:08:19 – 1:08:25]** So like why doesn't the same kind of stuff happen? I don't know in linear regression, for example.

**[1:08:26 – 1:08:30]** So in linear regression.

**[1:08:34 – 1:08:35]** linear regression are

**[1:08:36 – 1:08:37]** We have.

**[1:08:41 – 1:08:42]** Data points.

**[1:08:43 – 1:08:47]** Right? And we have like this correct straight line.

**[1:08:48 – 1:09:02]** And we have our current incorrect straight line and they also don't overlap the intersect at a single point which which doesn't help us it still measures 0. So why doesn't the same effect happen? Linear regression.

**[1:09:03 – 1:09:11]** Well, it doesn't happen because we had noise, right? So our presumed straight line still has some

**[1:09:13 – 1:09:17]** reasonable some non-zero likelihood because

**[1:09:18 – 1:09:24]** We add noise we we cannot do anything with speed date. Oh

**[1:09:27 – 1:09:27]** sorry.

**[1:09:30 – 1:09:33]** Sorry, I think. Yeah, I apologize.

**[1:09:36 – 1:09:40]** Yeah. Hello sorry. I think I was connection.

**[1:09:42 – 1:09:44]** Hope it hasn't been for a long.

**[1:09:47 – 1:09:48]** One, two, three.

**[1:09:51 – 1:09:52]** Yeah.

**[1:09:54 – 1:09:55]** I hope I'm back.

**[1:09:58 – 1:09:58]** All right.

**[1:09:59 – 1:09:59]** so,

**[1:10:02 – 1:10:02]** This.

**[1:10:03 – 1:10:03]** kind of,

**[1:10:06 – 1:10:09]** Thing does not happen in standard machine learning.

**[1:10:10 – 1:10:22]** This kind of problem because we are reading noise because we cannot do anything with the data. The data is fixed but we are like smoothing out our PG.

**[1:10:24 – 1:10:25]** We are smoothing out PG.

**[1:10:26 – 1:10:34]** We are adding something like, ghosts and noise to it, and it means that now PG of X is always greater than 0.

**[1:10:34 – 1:10:41]** It can be exponentially small, that's okay, but it's always greater than zero. It's never gonna get us something.

**[1:10:44 – 1:10:46]** Okay, everybody that left.

**[1:10:49 – 1:10:54]** Yes, sir internet problems on the other side too. So let me maybe

**[1:10:56 – 1:10:57]** Take a small break.

**[1:19:44 – 1:19:47]** It's something happening on your side, right?

**[1:19:55 – 1:19:56]** Hello.

**[1:19:58 – 1:19:59]** One, two, one, two.

**[1:20:05 – 1:20:06]** Hello, hello.

**[1:20:27 – 1:20:34]** Well, I guess you don't have a choice. I will, I mean there my recording will be good anyway, so

**[1:20:35 – 1:20:40]** Let me, let me continue. I'm not sure if you hear me.

**[1:20:42 – 1:20:47]** Because I don't I didn't hear anything from you.

**[1:20:51 – 1:20:53]** but some looks to be working and they

**[1:20:54 – 1:20:57]** the microphone icon seems to be feeling up.

**[1:20:58 – 1:20:58]** So,

**[1:21:00 – 1:21:02]** anyway, we are

**[1:21:04 – 1:21:07]** We?

**[1:21:07 – 1:21:18]** We were here, the idea of the wasserstein gains, I think a very beautiful idea, one of the most important tenant Financial in Ghent and then Reserve training.

**[1:21:19 – 1:21:19]** so,

**[1:21:21 – 1:21:26]** As I explained to you before, we're going to interrupt it. We can't really

**[1:21:27 – 1:21:43]** match two distributions that are disjoint that have non intersection support because there is no metric that will that our standard metrics that will be collabor Divergence and their variations will not

**[1:21:46 – 1:21:48]** Know, I am here.

**[1:21:51 – 1:21:56]** I'm sorry guys. Okay, so this time it's on my side.

**[1:21:58 – 1:22:02]** Yes. Sorry, this time it was on my side.

**[1:22:03 – 1:22:06]** I don't know why I keep losing connection because

**[1:22:07 – 1:22:10]** I'm pretty sure the internet works fine.

**[1:22:12 – 1:22:16]** when I dropped out the last time I checked it,

**[1:22:16 – 1:22:20]** And yeah, I can Google stuff. It works.

**[1:22:21 – 1:22:22]** Very strange.

**[1:22:30 – 1:22:39]** All right. Anyway again this will not affect the recording and even in the worst case, you can always watch the last 15 minutes on YouTube.

**[1:22:40 – 1:22:42]** So yeah, so let me finish.

**[1:22:44 – 1:22:44]** The.

**[1:22:45 – 1:22:46]** Best restaurant again.

**[1:22:47 – 1:22:48]** Over here.

**[1:22:53 – 1:23:01]** Proposes a way around this. So we cannot match to this distributions with this sharing supports or with almost just trying supports

**[1:23:02 – 1:23:24]** We cannot and in standard machine learning classical machine learning. What you do is you had noise. So you say okay, my PG is this load dimensional Stuff. Plus gaussian knows that extends to the whole space and how everything works, okay, diversions. That's what it's supposed to do and you can just maximize like,

**[1:23:25 – 1:23:25]** but,

**[1:23:26 – 1:23:36]** It doesn't really work for generative models. Because after that, you cannot really remove noise or at least in an implicit generative models. You cannot really remove noise.

**[1:23:37 – 1:23:38]** so, in

**[1:23:39 – 1:23:40]** In linear regression.

**[1:23:41 – 1:23:43]** We have our straight line.

**[1:23:44 – 1:23:48]** We are assuming gaussian noise around the straight line.

**[1:23:48 – 1:23:49]** Right.

**[1:23:50 – 1:24:30]** And then we learn the straight line. We have this green line over here, but when I do predictions, when I get a new X, and I say, okay, so now, what is the wife for this x? I am not adding artificial noise, right, I am just saying. Okay, so my prediction, my wife had is on this screen straight line. I am not saying oh wait I had this assumption that there is a gaussian know it's around here. So let me take this straight line, let me take what my model gives me. And then at noises and then this will be my wife had over here.

**[1:24:32 – 1:24:43]** This does not have I just go to the expectation. I go to the most probable hypothesis, if I need the point estimate, if I need to distribution. It's not a story. But for the point,

**[1:24:44 – 1:24:47]** A estimate. It's like this.

**[1:24:49 – 1:24:52]** Okay, so it looks like it's my internet anyway.

**[1:24:57 – 1:24:58]** Recording in progress.

**[1:25:22 – 1:25:26]** Yeah, I'm sorry. Sorry again now it's my side. Definitely

**[1:25:28 – 1:25:33]** Sorry. Now it's on my side differently, but again, what can you do?

**[1:25:34 – 1:25:38]** Right. So anyway,

**[1:25:38 – 1:25:43]** First time again. Yeah, again my apologies for for the technical problems today.

**[1:25:44 – 1:25:45]** so,

**[1:25:47 – 1:25:52]** if I had an explicit density model like an llm or something,

**[1:25:53 – 1:26:03]** then I can add noise like in the llm. For example, I produce a whole distribution of tokens for the next token, right? I do.

**[1:26:04 – 1:26:14]** But I chose only one talking actually. Not necessarily the the most probable one. It may be a sampling process, but I do choose only one talking and I just dropped the noise.

**[1:26:16 – 1:26:30]** But if I have again, if I have this implicit density model, then I Cannot drop the noise because my output already includes the noise. My distribution that I have trained.

**[1:26:31 – 1:26:32]** Includes.

**[1:26:33 – 1:26:36]** This noise and that makes the images bad.

**[1:26:37 – 1:26:52]** It basically means. Okay, so you have created your image now add some gaussian noise to your image which makes it all blurry and unrealistic. And this is this is the output that you have to do. So I don't want to admit to generate more models.

**[1:26:53 – 1:26:54]** To implicit dance studio models.

**[1:26:56 – 1:26:56]** but,

**[1:26:58 – 1:27:20]** Even though I don't want to admit to implement this generative models. I also cannot. Yeah. Sorry sorry. Yeah. Today is not my unfortunately, and not the main internet but I don't I can't really add this.

**[1:27:22 – 1:27:24]** um,

**[1:27:25 – 1:27:34]** I, I can't really it avoiding this noise because I don't have a good loss function. So the idea of extra stain. Again is

**[1:27:35 – 1:27:39]** To create a loss function, that will work without adding noise.

**[1:27:39 – 1:27:47]** And this loss function is based on what is called the earth mover distance, or Vaseline distance.

**[1:27:48 – 1:28:06]** Earth mover is, of course easier to understand because it immediately tells you what it's what it's doing. So the earth mover distance. Those like this are I have a distribution over here. What is the distribution? What is the distribution? It's like a pile of Earth amount of Earth.

**[1:28:07 – 1:28:08]** That has.

**[1:28:13 – 1:28:16]** Integral one that has total volume one.

**[1:28:18 – 1:28:20]** And then I have another distribution over here.

**[1:28:21 – 1:28:26]** It's all like a mount of Earth that has total volume one.

**[1:28:27 – 1:28:35]** So in principle, I can take a show, I can take this distribution and taking just move it over there.

**[1:28:36 – 1:28:37]** With a shovel.

**[1:28:38 – 1:28:40]** And as I am doing this,

**[1:28:40 – 1:28:42]** I will be doing some work.

**[1:28:43 – 1:28:49]** Work in the you know, straightforward sense of high school physics of mass times distance.

**[1:28:51 – 1:29:12]** And if I take like the optimal way to move, one of the first to the other, if I take the optimal transport between these two mounts, these two masses, these two volumes and they are equal volumes. So I can do that, then this will be the Earth over this.

**[1:29:13 – 1:29:24]** So now there will be the then there will be lots and lots of very complicated math. That I will definitely not go into but the idea is this

**[1:29:25 – 1:29:38]** so I want to like, match the two distributions while spending as little effort, as possible, spending as little work as possible, and as I do that,

**[1:29:41 – 1:30:08]** I want them to minimize this minimal effort, okay? So it sounds very very complicated that sounds like it will be completely invisible to train because it's like a minimization problem inside the minimization problem and the internal one is very difficult, but there is math that lets us go around this. I will not explain it in full detail but basically, if you can do it,

**[1:30:09 – 1:30:10]** Then.

**[1:30:11 – 1:30:22]** The distance, they lost function becomes exactly what we need. Becomes exactly what we want because now it doesn't matter that these two distributions have this joint support.

**[1:30:23 – 1:30:24]** if I move this,

**[1:30:25 – 1:30:26]** Red line over here.

**[1:30:27 – 1:30:38]** Well, they still don't intersect. But now there is less distance to go from the red distribution, to the green distribution, which means exactly that. I need less work.

**[1:30:39 – 1:30:40]** so, this

**[1:30:41 – 1:30:51]** The earth move over distance does not have this problem, doesn't need to know, a sort to anything artificial in order to bring distribution schools or together.

**[1:30:53 – 1:31:04]** And what sustained again is still one of the most popular loss functions for gains and for all sorts of adversarial training applications.

**[1:31:05 – 1:31:14]** And probably in practice, you will also be training against Vista with W again, losses. And yeah. So.

**[1:31:15 – 1:31:22]** This is the main mathematical idea that I wanted to mention. Let Me Maybe skip this part

**[1:31:23 – 1:31:34]** So the next big step was big again in 2019 which already produced kind of reasonable and the good images.

**[1:31:35 – 1:31:50]** It had some very nice interpolations it had. As you can see, you can go from a bird to the dog and in between you get some strange artificial hybrid. But

**[1:31:51 – 1:32:11]** The strange, artificial hybrids still still kind of makes sense, kind of makes sense. Right. And let me also skip the quality metrics. Yeah. And maybe the last thing that I want to discuss is this idea of the adversarial in coder

**[1:32:12 – 1:32:14]** so today we have discussed

**[1:32:16 – 1:32:24]** Generative models. In general, we have discussed specifically against what is the main idea behind the ends? The idea of adversarial training.

**[1:32:25 – 1:32:37]** And we have discussed the main loss function for genes. They were sustained again idea, they didn't do the math but I didn't expect to anyway. And now the last idea that I want to

**[1:32:38 – 1:32:42]** to discuss because it really Segways into

**[1:32:44 – 1:32:57]** variational and coders. And it also really adds this to our understanding of how generative models models operate. It's the idea of an adversarial and coder.

**[1:33:00 – 1:33:03]** so, let me motivate it, let me explain it and

**[1:33:05 – 1:33:08]** Then we will stop here.

**[1:33:13 – 1:33:13]** so,

**[1:33:14 – 1:33:25]** I started with this main problem of generative modeling, right? The main problem is how do you define the loss function?

**[1:33:26 – 1:33:34]** For example, here you go from the latent space to the pixel space but how do we Define the loss function of whether it's a good cat picture?

**[1:33:37 – 1:33:40]** actually, I didn't mention it then in the beginning of the lecture, but

**[1:33:42 – 1:33:47]** There is one answer that we already know, and that kind of looks reasonable.

**[1:33:48 – 1:33:50]** And the answer is, let's train Auto encoder.

**[1:33:51 – 1:34:02]** So where do we get? Like again we don't have a data set of these that match assess if we did it would be just supervised learning.

**[1:34:03 – 1:34:04]** but,

**[1:34:04 – 1:34:16]** What if we close the loop? What if we close the loop with not encoder? So, now we are here. We start here in pixel space with an X.

**[1:34:18 – 1:34:23]** Let's put it this way. This is some very complicated distribution, huge space.

**[1:34:24 – 1:34:25]** Then.

**[1:34:26 – 1:34:30]** We go through, not the generator. We go through the encoder.

**[1:34:32 – 1:34:34]** And we get to see.

**[1:34:34 – 1:34:42]** Which lives. Hopefully on a much more understandable, distribution, and smaller space. The late code.

**[1:34:43 – 1:34:44]** and then,

**[1:34:44 – 1:34:46]** We have the decoder.

**[1:34:47 – 1:34:54]** That unravels Z back. Decompresses. The back into the pixel space.

**[1:34:55 – 1:34:57]** right, and if you have an autoencoder,

**[1:34:59 – 1:35:15]** Then you automatically get some very simple, very straightforward loss functions, right? Because you can just take this x. You can take this x head and you can do something like, an lto on x-hat index. It's not a problem.

**[1:35:17 – 1:35:24]** You just want X head to be similar to X. So you won't see to be a good compressed representation of The Originals.

**[1:35:26 – 1:35:29]** And when you look at an auto encoder,

**[1:35:30 – 1:35:35]** it's looks like you have a generative model right here because look

**[1:35:37 – 1:35:42]** How does not uncover work? You start from here, you map?

**[1:35:42 – 1:35:46]** to the latent space and then you

**[1:35:47 – 1:35:50]** decompress back and you go to the pixel space.

**[1:35:51 – 1:35:53]** so, why can't I just

**[1:35:53 – 1:35:57]** Cut off the encoder and say that this part.

**[1:35:58 – 1:35:59]** Is a great generative model.

**[1:36:00 – 1:36:04]** Because the decoder is already used to converting.

**[1:36:05 – 1:36:10]** Latent codes into good. Let's say good cat picture.

**[1:36:15 – 1:36:15]** Well.

**[1:36:16 – 1:36:19]** the problem is that even in the latent space,

**[1:36:20 – 1:36:24]** even over here, where the dimension is relatively small.

**[1:36:25 – 1:36:40]** It still a pretty complicated distribution, a pretty complicated manifold of latent codes to. So, in reality, access live in the distribution with some, I don't know, dimensional million or something.

**[1:36:42 – 1:36:54]** And in reality is these cannot leave in three-dimensional space, there will be not enough information to capture, holy image. So they live in a space of 500 dimensions.

**[1:36:55 – 1:37:08]** And in the distribution of Dimension, 500 space of Dimension, 500 is still a pretty complicated space and there, it's still pretty big and there can still be very complicated manifolds inside.

**[1:37:09 – 1:37:17]** So the problem with this approach, why can't I just take the decoder of an autoencoder and say here is your generative model. The problem is

**[1:37:18 – 1:37:20]** I cannot sample from this red thing.

**[1:37:20 – 1:37:24]** And if I start sampling from a standard gaussian.

**[1:37:25 – 1:37:29]** Then with overwhelming probability, I will not.

**[1:37:30 – 1:37:46]** Get on on the right on the right thing on the right manifold and if I don't get on the right manifold here then of course I will also not get in the right manifold here and it will be a nonsensical image, not a nice cat forth.

**[1:37:48 – 1:37:48]** so,

**[1:37:49 – 1:37:50]** In order.

**[1:37:51 – 1:37:52]** To.

**[1:37:54 – 1:38:05]** In order to fix this problem, in order to steal use Auto encoders, as generative models, we need to do something about this latent space.

**[1:38:06 – 1:38:07]** We need to.

**[1:38:08 – 1:38:10]** Well, what do we need to do?

**[1:38:10 – 1:38:12]** There can be different approaches.

**[1:38:13 – 1:38:15]** A variational auto encoder.

**[1:38:16 – 1:38:19]** Would say rest. Let's regularize.

**[1:38:20 – 1:38:27]** And hopefully we will discuss. Why is tomorrow at least a little bit, they are really, really important.

**[1:38:28 – 1:38:29]** but,

**[1:38:30 – 1:38:35]** You can also do an adversarial thing. You can say, oh, okay.

**[1:38:36 – 1:38:40]** So I have this distribution of latent codes over here.

**[1:38:41 – 1:38:42]** Why don't I?

**[1:38:43 – 1:38:48]** Say that disease that get that, that come from real images.

**[1:38:49 – 1:38:52]** Are they kind of fake this?

**[1:38:54 – 1:39:01]** And the truth is the reels is come from some standard simple distribution. Like the standard goes

**[1:39:04 – 1:39:07]** and let's put a discriminator over here.

**[1:39:09 – 1:39:13]** To distinguish not between images, but between the latent codes.

**[1:39:16 – 1:39:23]** So it's the same adversarial idea. Let me show you a better picture over here. It's the same adversarial idea.

**[1:39:24 – 1:39:24]** but,

**[1:39:25 – 1:39:30]** Now, I am trying to make the distribution of late and quotes over here.

**[1:39:32 – 1:39:34]** match the

**[1:39:38 – 1:39:41]** Match there. Some kind of standard distribution over here.

**[1:39:42 – 1:39:59]** And the assumption is if the discriminator cannot distinguish between what actually gets produced from real images and a standard gaussian. Well, then maybe I can use the standard gaussian to sample news and to get new real images.

**[1:40:00 – 1:40:10]** At some point. It was and so it it's a pretty old idea. It's almost as old as the scans themselves still.

**[1:40:11 – 1:40:22]** Gets around, sometimes, I think variational, I think others are cleaner conceptual solution to the same problem. So they are used of course much more, but it's still an interesting.

**[1:40:23 – 1:40:30]** Variation on on their Cellular in. I, I think in the Practical session you also have A's

**[1:40:31 – 1:40:38]** So it can be even better than than a variational and quadrille. So it depends on how you cook it.

**[1:40:38 – 1:41:03]** Ah, and then of course, you can do all sorts of modifications, extensions, Etc, you can make the distributions conditional. For example, if you want to draw a specific digit from Eminence, then of course you need to specify the digit so you can add a label here. And then now, you can have different distributions for different labels or whatever. So lots of interesting stuff.

**[1:41:04 – 1:41:10]** and I think I have to stop here, especially since we were having some

**[1:41:11 – 1:41:16]** problems with the internet, unfortunately. But yes.

**[1:41:17 – 1:41:21]** We're very cool in 2020 or something.

**[1:41:22 – 1:41:25]** They were definitely state of their attention.

**[1:41:26 – 1:41:40]** They remain state of the art and some specific domains. Like, for example, super resolution, super solution is a interesting topic in itself. I could do the whole lecture and but if not today,

**[1:41:41 – 1:41:44]** They remain important in style transfer.

**[1:41:45 – 1:41:49]** Fortunately, we don't have time to discuss style transfer, but it's

**[1:41:51 – 1:41:58]** It's, it's still the the family of stylegan models are still alive. I think.

**[1:41:59 – 1:42:08]** But overall for like straightforward image generation or specially for prompted, image generation for text to image problems.

**[1:42:08 – 1:42:12]** They have been completely replaced by diffusion models.

**[1:42:13 – 1:42:20]** and tomorrow, in our last lecture, we will discuss the diffusion models and

**[1:42:21 – 1:42:31]** Again, probably I will definitely will have to skip all of the difficult math in the diffusion models. But at least

**[1:42:32 – 1:42:45]** I hope to be able to explain the basic idea, the intuition and how this all fits together and how it brings us to where we are today, more or less.

**[1:42:46 – 1:42:47]** So, thank you. And

## Full text

Okay, hello everyone and welcome back. We have only two lectures left, which is, of course, very little time to cover a lot of the January that. We actually plan to go on to. But still, I think that even until lectures, we can cover a couple of very interesting and very important and still very relevant ideas. Today, we talk about January on networks games. It's a beautiful idea, underlying the stuff which is completely on my medical. It's like it's just very cool and very logical, but it leads to very beautiful, made the Matrix a little bit down the road, but before we go there, before we go there, let me begin today with the structure of generative a whole so, like our first part today will be about generative models in general and what kinds of generative models exist in deep learning, So when we say generative, AI when we say generative models, what? It's not a very well defined term because, you know, you can say that logistic regression, generates the probability distribution of our classes, right? So the Divide is that in January AI. You are producing something big right, your producing an object usually of high dimension and of complicated structure. They can image or like text. So generative models are models that right? That raw, that produce music videos, something like that. and, When we talk about generative models. So let me draw a taxonomy for you. This will be our first subject for discussion. So of course, I will be talking on about deep generative models. So models that Are based on neural networks. But and and there is there are several important classes of this models. And today we will live in one of these classes tomorrow. We will live in another but I still want to draw a general taxonomy so that you can actually better understand what's going on. The first divide, the first like serious Fork. Inn in deep generative models comes in the distinction between explicit and models. I'll explain in a sec. and implicit instrumentals, so, What does explicit and implicit density mean? When you have a generative model. It takes as input, something like random noise or some condition or whatever. Then there is this black box which are trying to Define. And then at the output there is like A picture of a cat or something. There is X that lives in a very high dimensional space. and this x has a very complicated distribution, if you if you try to imagine As I think I made this argument once in our class, try to imagine the manifold of realistic photos in this three million dimensional space of one megapixel images. Obviously, we cannot imagine anything like that but also obviously it's very very, very complicated, right? So pox the distribution of access that we are trying to approximate that we are trying to model is very, very, very complicated. And the difference between explicit and implicit density models. Is that in explicit density models you get an explicit model for the density, right? So like there is this P of X is actually equal to Something in the model and you can actually find out what is it, what is it called to so to speak. Naturally. We will not be able to approximate. Well, we will not be able to get the actual distribution of, like cat photos, but we can proximate, right? And we can try to approx. And then inside explicit density models. We have. The next divide between tractable density models. And let me pause here and explain. So, tractable density basically means that you can have a formula for p of x. It makes so such strong assumptions that you actually can just write down. The P of X is equal to something. And usually, usually when we say tractable density, we mean an auto regressive model. So, not a regressive model. Is a model that makes use of this. Kind of obvious. Identity that if you have this big big X, then you can do something like and you can decompose it into something like pox, one pox to give an X1 pox 3. Give an X1 and X2. And so on until if x and give an X1 X and minus 1, right? So this is always true. And of course, since it's always true, it's also completely useless because you are not making anything easier for you. Because this is still a very big function of a lot of variables, but then you can simplify then you can make assumptions so you can make and you can make a Markov chain out of this. You can say that every next X depends on the previous ones, or you can have An RNN here which says that okay model is sequence. But every next output, Depends on the current input. And the hidden state which is also a part of the of the state part of the model variables here, and then you get another simplified in position. So on so of course, it would be a lot of Their, a lot of the models that exist happened to be in the auto regressive class. For example, all llms are here, almost, all the lamps are here because LMS Predict the next token. So the model text, the sequence of tokens as a sequence of as exactly as this as P of x k. Given the previous context, and Then of course the question is how to model this conditional distribution and that's where Transformers come in. That's where all the models come in but the basic assumption is this right? We produce. We generate text one by one. And there have been models for pictures here too. There were things like pixel. CNN. That produced Images pixel, baby pixel, and it was a good model in terms of the output. But of course, you know producing Images pixel by pixel is just wait to inefficient because you need to generate like a million pixels and running your model. Emilion times is of course invisible even if it's not very complicated. So the pixel Wise auto regressive models are not really used and we want to about them. But but they also accepted it's an actual idea. And for text basically, everything is not very aggressive. and then, Like what else is there that we also will not have time to talk about intractable density. You can have something like flow, a flow based model. so, one way to decompose a complicated distribution is to have is to separate it variables inside X, like the autographs of style and another way is to say, well, okay, what if P of X is a big composition of simple transformations. something like, If? A composed with f k minus 1 composed composed composed of two F1 of the so we are still modeling something like this. And we are doing it. Explicitly each f is a simple thing like Aidan gaussian noise or linear transformation or something like that. But when you compose a lot of A simple Transformations like always in your own networks. This is not a neural network but like always in neural networks you get this capability of modeling something much much more Complicated, right? So we want to talk about flow-based models no time unfortunately. And apart from tractable density, you can have approximately density models. So here. In a way you could repeat the same structure. But now, instead of modeling P of X instead, of making assumptions about the distribution itself, we explicitly say that like we approximate pox with some simpler queue and now this queue is a product of something easier. And here, the main example that is very, very relevant that it's a Pity that probably we won't have time to talk. Maybe we'll talk about them tomorrow. Maybe the main example are very well and coders. This is one of the most important ideas in the hole. And deep learning. How to use variational approximations to get. Good loss functions for generative models and variation of 10 others. I used all the time. And for example tomorrow we will talk about diffusion models and diffusion models, they usually operate in the latent space of a variational. I'm getting a bit ahead of myself. So of course explicit density part is like big and area and reach. There are lots and lots and lots of different approaches here. The implicit and such is not that rich, there are much fewer. Examples here. And actually, I won't even make any other examples because they are kind of as a terrific. The main example of implicit density, generative models are against That we just discussed today. and what does it mean not to have a density for X, like, how can you have a model that A produces access that gives you that gives you cat photos but does not have anywhere formula for p of X or even an approximation to P of x. Well, you just have to take this picture literally, right? So, an implicit density model, will start with random noise. And then it will actually produce just a sample. X, which is supposed to be taken from the distribution. Pure effects. It will produce a simple cat picture that is supposed to be a good cat picture. and this and if you look at this way, if you look at your neural network at your model as this, Sampling procedure as a sampler. That, well, not a sampler as a transformation of probability distributions from a simple one from random noise, like just standard goes in to this very complicated one in this huge dimensional space Etc. Then it all kind of Starts to make sense, right? So if you just have a black box that Samples, get photos for you. You cannot really extract the formula from this black box. I mean you could maybe make a trillion examples and then learn one of the explicit density models. But that doesn't count the Black Box itself doesn't have the formula anywhere. So so this is what again do. And now, the first part is over, I've talked about this General structure and maybe we'll return to tomorrow. And now, what are games? What is their main idea? So we talked about January of adversarial Networks. Yes. and, In the general. Sorry, the general Network. Is based. on this very interesting. Like it's one possible solution to a very deep problem in generative models. And we will discuss other. If we get to wires we will discuss other solutions to this problem. but, Here is the problem, basically. The main problem. Of. Generative AI in general. I mean it there are many ways to solve it. It's not like it's an open problem but the main deep problem that you need to solve and you create a generative model is what is your lost function? How do you Or the results. So, Let me start drawing this picture for you, right? So I have this random noisy which is basically just taken from some standard distribution or whatever. And then this random noise, he gets to the January Network gets to the model that Maps random noise. Two. Something that is supposed to be a cat picture. Right. Let's call it X head because it will be like a predicted kit not not yet real. so, Think of it. Okay, let's think of it as a learning problem as a machine learning problem. If you look at this as a machine learning problem, well you do have a data set of access, right? So what does your data look like your data is a lot of gets a lot of cat photos. But if you don't have beer data for this, right? You cannot just say that this x had should be similar to some X in in the training set because you have no idea which one, right There there isn't and there will never be a data set that pairs random noise with images that are supposed to be produced from this random noise. That's doesn't make sense. The whole point of hearing a generator is to learn this, this may concern so to get A good and relatively simple. Parameterization in the noise space. So that next week, we would be able to just take random noise and still get reasonable cat pictures. So the data the data is unlabeled it's it's unsupervised learning. but, so, Where we will the loss function come from, which X should see be. similar to Well, you can say, okay, I don't have any specifics in mind, I just want the result this x head to be a good cat picture. Okay. And this. Sounds reasonable and this is exactly what we'll do. But what does it mean to be a good cat picture? This, this is the Deep question that we need to answer because There is really. No function no mathematical function that you can run and say if this photo is a cat. Picture is a good cat picture. If this set of picks pixels is a good picture. This is something that you have to learn yourself too, and this is like half of the problem if not most of the problem. So change ready for their cereal networks. Say the following they say, well, okay, you recognize that you need to learn your loss function that you need to work for it. You cannot have you do not have a fixed formula for evaluating how Kate this image looks. so, Let's do it. Let's work for it. Let's have a whole separate Network called a discriminator. That. Who's only? Go who's only job is to say whether? The input. So, as input, it takes photos and as output, the dust just binary classification. Is it fake? Or is it real? Let's say the trails one. Because 0 So, the discriminator gets a picture. and if it's a picture produced, by the generator, Then it should say that it's fake. Right. And if it's a real picture, so we can, we can take our data and we can sample a real cat photo from it. Right. This will be real x x real and this is X fake. So, if a real picture is fit into the discriminator, the output should be one, right? In this way, the generator and the discriminator are at with each other, they have opposing interests. They discriminator wants to learn to distinguish between real images and images produced by the generator and the generator wants to fool the discriminator. So, this general idea is called adversarial training. and, You may hear that like games are not what they used to be and indeed games are not for the last few years. Cans are not at the Forefront of image generation. The images, they start Generation by the fusion models which will talk about tomorrow but Reserve training is very much alive. And even in the diffusion models we will see Exactly this idea. And we will see like a little bit of again, embed it into a diffusion model and making it better. So, This is, of course, still very important idea in machine learning, and it appears in many different fields. Of course, we're only talking about images, but still so, Let's now, okay, so let me maybe show you some nice pictures. I think I have the intra pictures about games. This is the main idea. And as you can see, it's very simple, right? So the generator is like Fortune a picture and they discriminate or is the detective that needs to decide whether it's real. and, Ideally. It should look something like this. So at first, so this this is an example where like the generator which is called Traverse, tip convolutional neural network here, the generator, learns to, like, counterfeit money. There is to produce pictures of real money, and at first, it just produces something. Actually, this is a few steps in because at first, the generator will just produce random noise. But then like it produces some very bad counterfeit and then the discriminator will say, oh, well, I don't know any better. So this this seems legit and I am full, okay? So I I provide once on on fake images. So then we train the discriminator and now it learns to distinguish, it understands that this is not real money, not real American dollars and then we Actually often, it's done. Exactly like this. So we fix the discriminator that has trained for a while. And now we train the generator to full this current version of the job of the discriminator. So we say, oh, okay. Now the discriminator doesn't accept our counterfeit. What what should we do? Let's train a little bit more and produce a slightly better counterfeit. It will still be bad it. Because again there is no. General loss function. That will tell you if the image is good, there's only this specific discriminator that has learned to not before by some attacks. so, This point, it will produce a better counterfeit and then this commentary will find some other features to discriminate on and then the generator will have to learn to fake those features. So and so on so there they're kind of playing this game and they and they hope is that everything happens. I will walk through the formulas in a minute but the hope is that everything happens like on this idealized image. So here for example, the generator is represented by this arrows, this arrows, as you can see in the we have the uniform distribution every time and in X we have like this, gaussian the green gaussian, and the black dots are the data points. And so, at first, This gaussian doesn't look like the black dots. So they blue dashed line is the discriminator. It's just Logistics Sigma, right? So it's a sigma it, curved that distinguishes between these two gaussians and then here is the crucial part. at this point, the discriminator Trains. But It's not training to mimic the data. Because that is impossible. I mean in this case it would be possible but in in the high dimensional case of pictures it would not be possible. So the discriminator learns to fool the generator, learns to fool the discriminator So in this case, it's enough to move this gaussian little bit over here and they discriminator is already folded. It doesn't need to go all the way to the data points but then of course, the discriminator will be able to distinguish between these two bills and so on. And finally we will get to this perfect picture where the generator is perfect and the discriminator has no idea what to do and just flips a coin. So of course, in real life, it's not gonna work like that. But the idea is exactly this. So, what is interesting? About the problem setting here. Well, let's write down the loss functions. Let's let's see like mathematically. What is happening here? So first they discriminate, right? So what is the discriminator was LD? Well. Let me write it in in this form. So, The discriminator is supposed to say 0 if it's fake and one, if it's real. So, let me write this as expectations doesn't really matter, but this will be cleaner for for what comes in next. So if I take a real photo, From the data set. From the training set, then I am supposed to like increase the output. I'm supposed to produce the score that goes to positive Infinity, so the probability of the sigma, it will go to one. So, I am supposed to increase to have a loss function, something like log D of X actually, might minus will be your website. and then, If x is fake. So X fake. Is taken of where is it taken from its taken from the distribution of the generator? Sorry, not xpg of Z, right from the distribution of the generator. No, actually it's video effects, right? So I'm I'm taking it from this distribution from the distribution that has come through through, through the generator. Then I am supposed to Output zero, so I'm supposed to do something like this. Right. and, And I want to minimize this loss function. With respect to the parameters of the discriminator. So when I, when I fixed the generator and I just train the discriminator, this is a very straightforward like binary classification problem. What does the generator do? Well, the generator. Is supposed to produce access that pass for real for the discriminator. So basically, I mean, it cannot influence this part there is no generator here, but for this part, the job of the generator is exactly opposite to the discriminator, right? So let me write it now. Completely, we start with some random noise. And then I want to actually take the discriminator loss on my results from Josie. and, Do the opposite. So if here I was minimizing minus this and here I will be minimizing Plus Right. So basically, you can say that the discriminator and the generator have the exact same loss function. I can just copy it here, it won't matter because it's just a constant for the generator. And what they're actually doing. If let's say that I have this loss function, that depends on the parameters of the generator and parameters of the discriminator for this loss function. Let's say that the discriminator wants it to be. As being as possible. So let's say that. Okay, this is the loss function. The thing in the brackets so, the discriminator wants to make it bigger. And the generator wants to make it smaller. So we have this Minimax game. It's actually. Something that has never happened to us in machine learning before and that will not happen since we are not just doing optimization here. At least formally we are doing adversarial optimization in the sense of Game Theory. And if you if you have ever had any classes in Game Theory or anything, you know that As soon as this quantifiers, this optimization goals like min max, max me and Etc. As soon as they start to stack up, as soon as you have like a Minimax instead of chest. I mean or just a mix the complexity of the charts, right? So it's it's extremely hard. Extremely difficult to actually optimize for in Game Theory and on the surface of this and it looks like this is this should be hopelessly difficult problem. I mean for us it's hard enough to do just minimization to, just be minimize the Lost function. And here we are asking to do a Minimax. So basically Define the equilibrium and the game. This is this sounds completely impossible. Well, in reality, of course, it's not impossible. And the that there are some properties of this loss functions that make it that make it simpler. And I will not go into the mathematical details, but basically let me just tell you the result here. Basically, if you fix the generator, then you know exactly what the optimal discriminator is because it's just the optimal base and classifier remember bias formula. So here, if I know the data is distribution and I know the generator distribution PG, the answer is just the best role. So they probability that X was real, is the density of EX underpaid data. Normalized to the summer of predate and PG, right? This is exactly the best role. Are and then like so this is straightforward, but the interesting part is that now you can take this formula and you can plug it into the generator loss and what you get is, basically a very simple result. You get that the generator is perfect. The attains the global minimum of this Criterion, if Pg' equals to data. So the this, this verifies that we are actually doing the right thing that the generator is actually. Minimizing is actually making PG. Closer to the true data distribution to predator. In fact. It's doing it in a pretty interesting, non-standard way. So for optimal for the optimal, discriminator the generator actually is minimizing this Johnson and aberrations. Not the cool book Library versions between the distributions, which we usually minimize machine learning, but like this average symmetrical, The version of Kyle where which is called the instance Jansen Shannon Divergence. And I won't go into details about this results. I don't want to discuss them further because Unfortunately, there are completely irrelevant. So everything that we can say this, theoretically about this kind of Minimax problems and you know, the game theory stuff here and how we can substitute the perfect discriminator into the generator was function, Etc. All of this. Makes the assumption that we are actually. We actually have this common was function for the generator in the discriminator. And that's just not throwing practice. So, in practice, it turns out that this kind of generator loss, they like just take the binary presently from the discriminator and flip it. This is a very bad idea for the generator. And why? Because It saturates and that's exactly the same problem that we discussed in the appearing several times. Again, I don't have time to go into full detail here, but basically This. Thing, this cross entropy is the output of a sigma. And if it's actually, it's right so if you're classifying it in the, if your classifying it like the discriminator does. Actually a good thing at least not a bad thing. Like if you you search for it, when you give the right answer and that's fine. So if you are already giving the right answer and you're confident in in this And and your confidence in this area. You are confident in this decision in the right decision, then you don't need to change anything, right? But now I have when you look at the generator, if the discriminator is very certain that it's true, that's right. And they discriminator has saturated and doesn't and it's doing a very good job. It means that the generator is failing, it means that the generator does not produce believable results, the discriminator is easy. It's easy to distinguish for the discriminator. So, this is the situation where we are supposed to. Train the generator. We are supposed to like actually update its weights, but we can't, because in the back propagation, This. The the loss is only over here. So, the gradients for the generator, have to go through the gradients of the discriminator. And as I just said, the gradients for the discriminator become near zero because the discriminatory saturated and already working very well. So, if I reuse the same loss function, it's really a better idea because it means that when the when I have trained the discriminator and then practice there is this alternating training usually. So we train the discriminator, then the generator and discrimination. When I trained the discriminatory little and it becomes good at separating stuff. This is exactly when it's gradients become near zero and the generator is very hard to train. So the same effect that we had in slightly different form. As you can see, I am teaching you General ideas that appear over and over the same as a result training today. So, So what do we do? Well, we changed the loss function, and let me skip the Early attempts at changing this loss function. Let me just show you the path that we have the the original against how they worked. And that was what 12 years ago and that's 2410 and in 2014 as you can see, on this picture. So the green ones are like real training samples, there near us, Neighbors From the training set, to the next, to the name of the chest picture right here. So you can actually verify that. The model did not just memorize a few elements of the training set, but that's actually generating stuff. So as you can see, it worked wonderfully for Ms. And it worked much worse for this small, black and white human faces and the basically was Very bad for anything else. For anything more diverse. So, in 2014 against appeared but they were no match to other generative models at that point. So what happened next? Next there was this again this again is basically the same kind of game but with a new better architecture. Convolutional architecture for the January and the discriminator again. No no point in going to the details but I want to make one remark here. So In. So, this again, already started to produce some reasonable pictures on some data sets. Still very small, still. Obviously better than some ways. It was 10 years ago, image generation was very bad back at the time. So this was actually a state of the art and years ago. And yeah, just a side remark. Yeah. If you look through old papers on gants, and on Ys, and on very generative models, you'll see a lot of bedrooms. I don't know who started it but at some point like there is this data set called large-scale, not large scale large-scale scene understanding. So as you stand for scene understanding and it basically is like several subsets of photos from different environments. and one of them was a bedroom and first, once somebody chose this set of pictures for their tests and of course, after that, everybody had to follow suit and had compared their bedrooms with previous better. So you will see a lot of bedroom pictures they are. Relatively small, like, I think 64 by 64 pixels for maybe one 28 by 128 something like that. But they are in color, and they already kind of are supposed to look like real forces. And this is DC again after one epoxy still very bad, but after five epic sets to be like more or less, okay? So nothing obvious nothing. Exciting by today's standards, but back then it was okay. And what I wanted to mention here, is this idea. So this this is important like, again, how do you Illustrate. How do you understand yourself that you've got a good generative model? They discriminator will not tell you that because the discriminator will tell you. Oh, I can't distinguish. It doesn't mean that the pictures are good. It doesn't mean that the latent space is good. It just means that the discriminator can distinguish. Maybe you didn't train it? Well enough, maybe it's not large enough, it's not powerful enough, who knows, right? So how do you well, maybe not measure the metrics are different story, but how do you At least, see for yourself. If the generator actually makes any sense. And the usual is illustration goes like this and I want to explain it because it's really a good. It's a good illustration. So what we are doing like intuitively geometrically in the latent space and so on. So what is the generator actually? It's taking the this random noise this Vector from the latent space, the so this will be the latent space. and its mapping the two. Point x, which is in pixel 6 space. So to say, Right. and, In pixel space in this huge million dimensional space of images. The actual images that we are looking for. Form. This extremely complicated and completely and un understandable manifold, right? So they have this very, very complicated structure. But in the latent space. Our goal. Is to actually like flat in the structure completely. Because what is our goal, really? Our goal is to be able to generate new images, right? So our goal is to be able to do the following to take a random deal over here. He from a standard Gauss, right from some very simple distribution, doesn't matter if it's the gaussian specifically. But Z from some very simple distribution that we can sample from directly and take this random noise, Put it through our generator method over here and actually hope that the result will fall in this. Extremely complicated, very difficult. Completely under animation of real pictures, real photos, Right. So this is the job of the generator. Here is the January, right? So how do we test this? Like how can we understand if we actually did a good job in this? Well, here is one test that was very popular and that you can immediately see for yourself, it's very Visual and the test is, let's do a linear walk in the late space. so, in the latent space, if I take for example, two differences, one here, one here so they will produce two different pictures They will produce two different pictures, right? The green one, and the orange one. Then in the latent space, if I'm supposed to get them from a standard gaussian, it means that if I just walk from one of these East to the others, this is E2. And that one was, he won. So if I, if I want to walk, if I walk from one random sample to another random sample over here, this I can do just along a straight line and along the straight line. all of the intermediate, this Should give me reasonable images. Okay, this is the main test. so, if G, if the generator, Was stupid and it was not doing much and they just memorized a few data points and then disease would get mapped to this data points. It will still look good on the training set. But if I go from one Z to another, then here it would do something nonsensical. Like, for example, it might walk along a straight line and in the pixel space. and if you go along the straight line and the pixel space, you don't get realistic photos, right? You get like one photo and then the other kind of, you know, appearing through it. And it's like you're making one of the more transparent and the other shows up underneath underneath so, It's, it's definitely not a walk through realistic photographs. What you are supposed to have in the perfect in the ideal case? As a walk in the pixel space. That all. So follows this manifold. And goes from one next to the other. So on every intermediate step through this straight line, You are supposed to get. A realistic photo somewhere on the manifold. And if you get that and if you see it like consistently true, then it does mean that you can sample. Or at least you can hope to sample random season and get realistic images, right? So if you Look in this again, papers and generative models. You will often see this kind of walks through the feature space or late in space, the left and the right part are like actual images or something from the training set or some images that are like guaranteed to be good. And now you walk through the latent space and you see. So in the latent space you walk along straight line and you see what happens in the pixels space. And as you can see here, there may be some strange stuff happening in the middle but more or less. They're all kind of rare listing at least on the same level of realistic as the images on the side. So, So this this was, I think, the first game, which was already at the state of the art of famous generation. It even had some kind of factor arithmetic, it didn't work out later. So let me skip that. but also, that was the the time when against they were already state of the art, and What I just showed to you. What's indeed state of the Artemis generation. 10 years ago, you can again Marvel at the progress at the rate of progress. but, They were still kind of bad. You wouldn't use them for generating like a production images like today, I obviously generate cat pictures like this one, and I like the results. But back then these are not real bedroom photos. And back then there were some common Problems with Generations specifically with Guinness generation that you may remember. I mean they were all across the internet and stuff like that were like common failure modes of games and maybe he will actually see some failure. Most like this in your practical sessions. So they definitely had problems with counting. I mean, the recent meme was about six fingers on a hand, like a couple of years ago. It was still a problem today. It's not. But back like 10 years ago, it was much worse than six fingers on the hand. Right there would be like three heads of a dog with who knows how many eyes. and that actually makes sense as a failure because When you look at something like this reversed convolutional Network, what it's doing, is it, it has this general idea, the general feature and then it's specialized and that, like drawers different parts of the image then more or less independently. And basically, what this failure modes means is that, well, I am here. And I only have a small context around this eye, so I'm not really sure is it the right tire or the left eye and I decided. Okay. So maybe it's the, maybe this is the right. I need another one and then I do the other one. Again, I'm not sure. Is it the left or the right? And again, I do another one. So, I think the mechanism was something like this Yeah, and the same goes for like problems with perspective. So here I I was generating this dog and they go to the head of the dog and now I don't have enough context to understand what was the angle. I was looking from. And now the other half of the dog is from a different, completely different thing. And actually this stuff is hard so it this kind of mistakes. They stand out for us because our vision is very good. We know the world we know how it's supposed to look like and we learned it in the first years of our lives, but it's actually very very difficult. And this kind of, for example perspective, generating stuff and proper perspective as if it was a three-dimensional world is really difficult. And for example Among the signatures if we're flying and I would say erase your hands but just how many of you actually realized that one of these images does not belong here. Um, and usually, it takes a few questions for people to actually see that. This cat over here is just a real photo. There is nothing bad about this. It's just a cat, which is sleeping all curled up like this cats. Do it, right? So It's, it's difficult and it was it was difficult. but, Imagination has made tremendous progress and this picture. Of course, I have been showing it since 2018, but honestly, you can extend it. There are, of course, newer and better models for human faces, too. But it would be points list because in 2018, you already, probably cannot see the imperfections. There are imperfections here, but on a slide, I don't think you can see that. So, but in 2013, I think you can see, right? And you can actually see how how much progress game-based generation made between in just this four or five years. So how did that happen? What are the main ideas? Again. Let me concentrate on the important ideas and the technical ideas. I will just pass through very quickly and I I want to discuss with you at least one conceptual, very interesting idea. One idea that again, bring maybe illuminates, what's happening? And all of this latent spaces and stuff. but the technical idea was that An important. Also, an important technical idea was that well you don't have to generate a whole picture at once. and, The implementation of this idea was the following. You can have, what is called the conditional again? Like when you give a condition and you expect the output to change depending on the condition. And one like specialty relatively simple version of conditional generation is called super resolution. It's still generation because you are inventing, new stuff, but super resolution is like this problem where you have a low resolution image and you want to make it into a high resolution image, so you're like you're replacing every pixel width 4 pixels, or something like that. And this is a change generative problem because again, the information is not there, you have to invent it. But it's a much easier problem than just making new images from scratch, right? Because the image is basically here, you just need to you know get some details right? And so the idea for General generation was, well, why don't we start small? And then just do like a sequence of super resolution. This was called program Progressive growing again, and this is the game that gave us this guy in 2017. There was a website called this person does not exist, which was kind of famous back then, but I don't expect you to remember and, So how does it work? Very simple. You have a data set of human faces, you want to generate human faces. So your first game pretty simple generator. Pretty simple discriminator and it turns to generate 4 by 4. Human phases, human faces with 4 by 4 pixels, trust me. You can do it even from scratch. It's not a hard problem. 16 pixels are. Okay. And then you use this generated 16 pixels as the condition to do super resolution and to do an 8 by 8 image. And then 16 by 16 and 32 by 32 and so on and so on. And then you train it for quite a while and like, in two weeks, you get in two weeks of training back then that was one of the first famous results from Nvidia. But then in media was only starting in the AI world. But they already, of course, had a lot of compute. So after two years of training like this, you know, sorry, two weeks of training like this here. You get to one megapixel Mission, that's pretty. So, the architecture is very simple, etc. Etc. And you can later, you can click on the links on the time on this, but there are some nice long videos of exactly this walks of the latent space and they look pretty cool. Even into 2018, they look pretty cool. But this is not the interesting part. This is, Still an idea that is useful and it's still applied. But the interesting part. Is what did the use for the loss function? Well. They actually by the time there were two main loss functions in games for the generator and for the discriminator 2. One of them was the least where scanner. I don't want to spend time on the list Square scan because oh, it's solving the same kind of situation problem and that's only it in a relatively straightforward way. So it just says, well instead of having a sigmoid let's just have a square deviation. So instead of saying, oh, I want my deal of x to be as large as possible and it goes through the same way and become close to one. I just say, Okay, I want my idea of x to be close to a constant, like a constant one or something. Ah, and which means that overshooting, this constant is also bad. So, nothing goes to Infinity. Everything is supposed to Cluster around this target constants. And usually in classification, it's a very bad idea. If you were doing like detailed class on with the first part on linear models. I would explain to you why it's better yet, they usually squares for classification, but here it works because it solves the situation problem. but, And I will skip this. Yeah, I will skip the authority ideas don't have time for them but the interesting idea here. Let's make a point three in this will be our I guess the main content. Is called wasserstein games. Or W again. Sometimes you see the abbreviation is famous mathematician, whatever, but I want to explain the and I will not explain all the maths, it's traditional for us, but I want to explain the maturation because I think it's really cool and really right? ah, so, um What is MasterChef again? What problem is it solving Well, what is the goal of our generative models? We want PG of X our distribution at the output of the generator to be close to pidato effects, right? To distribution of the real true photos. Are, what does it mean that one distribution is close to the other? Well, in machine learning. Usually it means that we are minimizing what is called the cool book. Why are they originates? I think I already mentioned it today, but let me remind you I hope you if you've heard of this term before. So Kyle from P to kill something like the integral of P of X time slope of x divided by Q facts. Yeah. And when he and Q are the same, this look becomes zero, right? The friction becomes one. And this this little becomes zero and the Callback Library diversion Divergence goes to 0, goes to zero, as let's say, Q goes to P or p goes to kill or whatever. Right? and usually, In machine learning, when you want to make one distribution, similar to the other, you are minimizing something like this. And it's a long story, there is an important difference between minimizing, Kyle from P to q and Kyle from Q to P. Because as you see, it's not symmetric. Different properties, whatever. It's it's not the point now. the point now is actually Very interesting. So, let's so, usually, we are doing this in relatively like, small spaces, right? But Here. In January fair, I in image generation models. For example, we are doing our X is this. very, High dimensional, Vector of pixel values, right? So, it's it, it leaves in a very big space. and, The actual distributions, both be dated and PG. Are actually concentrated in. Low dimensional. In low dimensional. Subsets subspaces manifolds in this high-dimensional space. So I will try to draw like two-dimensional picture because that's all I can do. But if you're looking at two dimensions, then it's like, here is we are leaving on the plane. So the plane is like the space of images and P data. Is actually concentrated. Along just a single line along one dimensional Subspace of the plane, right? So this is Benedict, this is our goal. Let's say And our model. Something like this our PG or P model or whatever. Well, it's concentrated along some other straight line. Right. So this looks very natural because It's the generator changes random noise which is lower dimensional into into an image. So by definition, it has a low dimensional thing here and the data I mean, also kind of obvious that they realistic cat photos, do not take up the whole image space, so it's also in a low dimensional manifold And our goal is kind of to you know match these two distributions. We want to make the purple distribution, similar to the green distribution. Here is the problem. If they are both low dimensional, manifolds it means they don't really overlap. It means that. If? The data. Of X is non-zero. Then probably P of x is 0. And twice, averse. if PNG of x, Is non-zero. Then probably Predator effects is 0 with probability one. Basically. Because again, their supports are different. We cannot just hope to you know in the very beginning to just get the right manifold, that's not gonna happen. We are going to get a different menu. We're going to get a different straight line on the plane. And our goal is supposed to. Be like to move this straight line to the to the correct straight line to the straight line of pay data. but, we can't, because if something like this happens, the cool book liner Divergence has become meaningless. They become infinite basically. So I integrate over this space. and whenever pox, Is present P of x is 0. So I am integrating over something here. I'm taking the expectation. And I'm thinking the expectation of something, which is basically always infinite. Not a good idea or the other way around. If Q is non-zero, then peace zero and all that doesn't make. So if I write down Kyle from here, the nothing changes, it's still interested. And this means that if I keep using something like the book, cover their versions, I will not be able to train anything because if I to be my generator a little bit and I move this straight line a little bit, let's say then it will still not be mentioned the green line, right? It will still be different and they versions will still remain in infinite. Or and I will not be able to distinguish between the correct direction and the wrong direction. So I need to understand and what direction to move the straight line. And I can't this this kind of losses. Don't don't say anything about this. Okay. Here is a question. I hope you understood what the problem here is. but, It sounds like it kind of invalidates the entire field of machine learning. Because we are always in a way, trying to do this. We are always trying to manage distributions and pretty careful. They are going to be on separate Subspace in separate Subspace. So like why doesn't the same kind of stuff happen? I don't know in linear regression, for example. So in linear regression. linear regression are We have. Data points. Right? And we have like this correct straight line. And we have our current incorrect straight line and they also don't overlap the intersect at a single point which which doesn't help us it still measures 0. So why doesn't the same effect happen? Linear regression. Well, it doesn't happen because we had noise, right? So our presumed straight line still has some reasonable some non-zero likelihood because We add noise we we cannot do anything with speed date. Oh sorry. Sorry, I think. Yeah, I apologize. Yeah. Hello sorry. I think I was connection. Hope it hasn't been for a long. One, two, three. Yeah. I hope I'm back. All right. so, This. kind of, Thing does not happen in standard machine learning. This kind of problem because we are reading noise because we cannot do anything with the data. The data is fixed but we are like smoothing out our PG. We are smoothing out PG. We are adding something like, ghosts and noise to it, and it means that now PG of X is always greater than 0. It can be exponentially small, that's okay, but it's always greater than zero. It's never gonna get us something. Okay, everybody that left. Yes, sir internet problems on the other side too. So let me maybe Take a small break. It's something happening on your side, right? Hello. One, two, one, two. Hello, hello. Well, I guess you don't have a choice. I will, I mean there my recording will be good anyway, so Let me, let me continue. I'm not sure if you hear me. Because I don't I didn't hear anything from you. but some looks to be working and they the microphone icon seems to be feeling up. So, anyway, we are We? We were here, the idea of the wasserstein gains, I think a very beautiful idea, one of the most important tenant Financial in Ghent and then Reserve training. so, As I explained to you before, we're going to interrupt it. We can't really match two distributions that are disjoint that have non intersection support because there is no metric that will that our standard metrics that will be collabor Divergence and their variations will not Know, I am here. I'm sorry guys. Okay, so this time it's on my side. Yes. Sorry, this time it was on my side. I don't know why I keep losing connection because I'm pretty sure the internet works fine. when I dropped out the last time I checked it, And yeah, I can Google stuff. It works. Very strange. All right. Anyway again this will not affect the recording and even in the worst case, you can always watch the last 15 minutes on YouTube. So yeah, so let me finish. The. Best restaurant again. Over here. Proposes a way around this. So we cannot match to this distributions with this sharing supports or with almost just trying supports We cannot and in standard machine learning classical machine learning. What you do is you had noise. So you say okay, my PG is this load dimensional Stuff. Plus gaussian knows that extends to the whole space and how everything works, okay, diversions. That's what it's supposed to do and you can just maximize like, but, It doesn't really work for generative models. Because after that, you cannot really remove noise or at least in an implicit generative models. You cannot really remove noise. so, in In linear regression. We have our straight line. We are assuming gaussian noise around the straight line. Right. And then we learn the straight line. We have this green line over here, but when I do predictions, when I get a new X, and I say, okay, so now, what is the wife for this x? I am not adding artificial noise, right, I am just saying. Okay, so my prediction, my wife had is on this screen straight line. I am not saying oh wait I had this assumption that there is a gaussian know it's around here. So let me take this straight line, let me take what my model gives me. And then at noises and then this will be my wife had over here. This does not have I just go to the expectation. I go to the most probable hypothesis, if I need the point estimate, if I need to distribution. It's not a story. But for the point, A estimate. It's like this. Okay, so it looks like it's my internet anyway. Recording in progress. Yeah, I'm sorry. Sorry again now it's my side. Definitely Sorry. Now it's on my side differently, but again, what can you do? Right. So anyway, First time again. Yeah, again my apologies for for the technical problems today. so, if I had an explicit density model like an llm or something, then I can add noise like in the llm. For example, I produce a whole distribution of tokens for the next token, right? I do. But I chose only one talking actually. Not necessarily the the most probable one. It may be a sampling process, but I do choose only one talking and I just dropped the noise. But if I have again, if I have this implicit density model, then I Cannot drop the noise because my output already includes the noise. My distribution that I have trained. Includes. This noise and that makes the images bad. It basically means. Okay, so you have created your image now add some gaussian noise to your image which makes it all blurry and unrealistic. And this is this is the output that you have to do. So I don't want to admit to generate more models. To implicit dance studio models. but, Even though I don't want to admit to implement this generative models. I also cannot. Yeah. Sorry sorry. Yeah. Today is not my unfortunately, and not the main internet but I don't I can't really add this. um, I, I can't really it avoiding this noise because I don't have a good loss function. So the idea of extra stain. Again is To create a loss function, that will work without adding noise. And this loss function is based on what is called the earth mover distance, or Vaseline distance. Earth mover is, of course easier to understand because it immediately tells you what it's what it's doing. So the earth mover distance. Those like this are I have a distribution over here. What is the distribution? What is the distribution? It's like a pile of Earth amount of Earth. That has. Integral one that has total volume one. And then I have another distribution over here. It's all like a mount of Earth that has total volume one. So in principle, I can take a show, I can take this distribution and taking just move it over there. With a shovel. And as I am doing this, I will be doing some work. Work in the you know, straightforward sense of high school physics of mass times distance. And if I take like the optimal way to move, one of the first to the other, if I take the optimal transport between these two mounts, these two masses, these two volumes and they are equal volumes. So I can do that, then this will be the Earth over this. So now there will be the then there will be lots and lots of very complicated math. That I will definitely not go into but the idea is this so I want to like, match the two distributions while spending as little effort, as possible, spending as little work as possible, and as I do that, I want them to minimize this minimal effort, okay? So it sounds very very complicated that sounds like it will be completely invisible to train because it's like a minimization problem inside the minimization problem and the internal one is very difficult, but there is math that lets us go around this. I will not explain it in full detail but basically, if you can do it, Then. The distance, they lost function becomes exactly what we need. Becomes exactly what we want because now it doesn't matter that these two distributions have this joint support. if I move this, Red line over here. Well, they still don't intersect. But now there is less distance to go from the red distribution, to the green distribution, which means exactly that. I need less work. so, this The earth move over distance does not have this problem, doesn't need to know, a sort to anything artificial in order to bring distribution schools or together. And what sustained again is still one of the most popular loss functions for gains and for all sorts of adversarial training applications. And probably in practice, you will also be training against Vista with W again, losses. And yeah. So. This is the main mathematical idea that I wanted to mention. Let Me Maybe skip this part So the next big step was big again in 2019 which already produced kind of reasonable and the good images. It had some very nice interpolations it had. As you can see, you can go from a bird to the dog and in between you get some strange artificial hybrid. But The strange, artificial hybrids still still kind of makes sense, kind of makes sense. Right. And let me also skip the quality metrics. Yeah. And maybe the last thing that I want to discuss is this idea of the adversarial in coder so today we have discussed Generative models. In general, we have discussed specifically against what is the main idea behind the ends? The idea of adversarial training. And we have discussed the main loss function for genes. They were sustained again idea, they didn't do the math but I didn't expect to anyway. And now the last idea that I want to to discuss because it really Segways into variational and coders. And it also really adds this to our understanding of how generative models models operate. It's the idea of an adversarial and coder. so, let me motivate it, let me explain it and Then we will stop here. so, I started with this main problem of generative modeling, right? The main problem is how do you define the loss function? For example, here you go from the latent space to the pixel space but how do we Define the loss function of whether it's a good cat picture? actually, I didn't mention it then in the beginning of the lecture, but There is one answer that we already know, and that kind of looks reasonable. And the answer is, let's train Auto encoder. So where do we get? Like again we don't have a data set of these that match assess if we did it would be just supervised learning. but, What if we close the loop? What if we close the loop with not encoder? So, now we are here. We start here in pixel space with an X. Let's put it this way. This is some very complicated distribution, huge space. Then. We go through, not the generator. We go through the encoder. And we get to see. Which lives. Hopefully on a much more understandable, distribution, and smaller space. The late code. and then, We have the decoder. That unravels Z back. Decompresses. The back into the pixel space. right, and if you have an autoencoder, Then you automatically get some very simple, very straightforward loss functions, right? Because you can just take this x. You can take this x head and you can do something like, an lto on x-hat index. It's not a problem. You just want X head to be similar to X. So you won't see to be a good compressed representation of The Originals. And when you look at an auto encoder, it's looks like you have a generative model right here because look How does not uncover work? You start from here, you map? to the latent space and then you decompress back and you go to the pixel space. so, why can't I just Cut off the encoder and say that this part. Is a great generative model. Because the decoder is already used to converting. Latent codes into good. Let's say good cat picture. Well. the problem is that even in the latent space, even over here, where the dimension is relatively small. It still a pretty complicated distribution, a pretty complicated manifold of latent codes to. So, in reality, access live in the distribution with some, I don't know, dimensional million or something. And in reality is these cannot leave in three-dimensional space, there will be not enough information to capture, holy image. So they live in a space of 500 dimensions. And in the distribution of Dimension, 500 space of Dimension, 500 is still a pretty complicated space and there, it's still pretty big and there can still be very complicated manifolds inside. So the problem with this approach, why can't I just take the decoder of an autoencoder and say here is your generative model. The problem is I cannot sample from this red thing. And if I start sampling from a standard gaussian. Then with overwhelming probability, I will not. Get on on the right on the right thing on the right manifold and if I don't get on the right manifold here then of course I will also not get in the right manifold here and it will be a nonsensical image, not a nice cat forth. so, In order. To. In order to fix this problem, in order to steal use Auto encoders, as generative models, we need to do something about this latent space. We need to. Well, what do we need to do? There can be different approaches. A variational auto encoder. Would say rest. Let's regularize. And hopefully we will discuss. Why is tomorrow at least a little bit, they are really, really important. but, You can also do an adversarial thing. You can say, oh, okay. So I have this distribution of latent codes over here. Why don't I? Say that disease that get that, that come from real images. Are they kind of fake this? And the truth is the reels is come from some standard simple distribution. Like the standard goes and let's put a discriminator over here. To distinguish not between images, but between the latent codes. So it's the same adversarial idea. Let me show you a better picture over here. It's the same adversarial idea. but, Now, I am trying to make the distribution of late and quotes over here. match the Match there. Some kind of standard distribution over here. And the assumption is if the discriminator cannot distinguish between what actually gets produced from real images and a standard gaussian. Well, then maybe I can use the standard gaussian to sample news and to get new real images. At some point. It was and so it it's a pretty old idea. It's almost as old as the scans themselves still. Gets around, sometimes, I think variational, I think others are cleaner conceptual solution to the same problem. So they are used of course much more, but it's still an interesting. Variation on on their Cellular in. I, I think in the Practical session you also have A's So it can be even better than than a variational and quadrille. So it depends on how you cook it. Ah, and then of course, you can do all sorts of modifications, extensions, Etc, you can make the distributions conditional. For example, if you want to draw a specific digit from Eminence, then of course you need to specify the digit so you can add a label here. And then now, you can have different distributions for different labels or whatever. So lots of interesting stuff. and I think I have to stop here, especially since we were having some problems with the internet, unfortunately. But yes. We're very cool in 2020 or something. They were definitely state of their attention. They remain state of the art and some specific domains. Like, for example, super resolution, super solution is a interesting topic in itself. I could do the whole lecture and but if not today, They remain important in style transfer. Fortunately, we don't have time to discuss style transfer, but it's It's, it's still the the family of stylegan models are still alive. I think. But overall for like straightforward image generation or specially for prompted, image generation for text to image problems. They have been completely replaced by diffusion models. and tomorrow, in our last lecture, we will discuss the diffusion models and Again, probably I will definitely will have to skip all of the difficult math in the diffusion models. But at least I hope to be able to explain the basic idea, the intuition and how this all fits together and how it brings us to where we are today, more or less. So, thank you. And
