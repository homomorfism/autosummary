# Transcript — google_stt

- **Provider:** google_stt
- **Language:** en-US
- **Audio duration:** 1:35:54
- **Segments:** 657
- **model:** latest_long
- **use_enhanced:** True
- **latency_sec:** 839.26

## Segments

**[00:00 – 00:01]** Okay.

**[00:02 – 00:05]** Good day or good morning still everyone. And

**[00:06 – 00:10]** Welcome back to the lecture part of our class.

**[00:11 – 00:12]** which,

**[00:14 – 00:17]** is being done online this year, and

**[00:18 – 00:31]** last time we ended on conventional architectures and specifically on how CNN's work and what is their like

**[00:32 – 00:36]** What is their main?

**[00:37 – 00:47]** good thing that they do, what is the main advantage of using conversations and this main advantage was of course, to

**[00:49 – 00:51]** Reuse the same weights.

**[00:52 – 01:09]** Over the entire input and over all of the intermediate feature tensors that you see in in inside the neural network that are the outputs of intermediate players. So all of this can be actually

**[01:12 – 01:17]** all of this can can be processed in parallel and

**[01:18 – 01:22]** you can reduce the number of Weights by huge factors, right?

**[01:24 – 01:24]** So,

**[01:26 – 01:47]** Before we proceed with conversion architectures today. I understand that you already kind of started talking about convolutional architectures with Alex, and that is absolutely great because now we can skip part of this lecture and faster. Get to recurrent networks. I'm not sure if we get there today, but hopefully, yes,

**[01:48 – 01:50]** but before,

**[01:52 – 01:56]** Before we begin with the lecture.

**[01:56 – 01:57]** Let me.

**[01:58 – 01:58]** oh,

**[02:00 – 02:03]** before we begin with the lecture, let me

**[02:06 – 02:09]** show you a couple of things. I have this.

**[02:11 – 02:30]** Standard illustrations for CNN's that. I think you don't really know because you've already had practical sessions about and, but maybe I will, at least mention a couple of buzzwords that you can look up.

**[02:31 – 02:32]** so, I want

**[02:34 – 02:40]** I want to discuss all of these pictures in detail but basically like in classical computer vision.

**[02:41 – 02:52]** In the days before neural networks actually worked, what you would do, what you would actually do in computer vision, will still be using configurations, but you would be using like handmade conversations.

**[02:53 – 02:59]** They would be called filters and sometimes people call learnable conversations filters as well.

**[03:00 – 03:23]** And there were like filter banks for all kinds of purposes and if you look at classical utilities for say image processing, right? Sharpen blur at contrast emboss, and whatever. It's all done with this kind of filters. It's all done with filters that.

**[03:25 – 03:29]** Are apply that are basically this small matrices.

**[03:30 – 03:54]** Just like conversations that are applied in parallel over the image, right? And you pretty complicated stuff with this, you can do, for example, H detection, like, find out where the edges of objects on the image are. And here, for example, the the cat itself is pretty messy in terms of the ages, so you can see it here.

**[03:57 – 04:08]** Um there were classical filter brands like Gabor filters where you would do something like Edge detection and to be perfectly precise. You would do like

**[04:10 – 04:36]** discrete derivatives finite differences in different directions and you would like directed Edge detection. So like, where is I? Did this kind of filter fires up if there is a big difference, vertically, when you go vertical from one pixel to another and this one, if you go horizontally, from one pixel to another and a lot changes. So you can actually

**[04:37 – 04:58]** This way. Okay, have illustrations for pooling. It's not very interesting, but if you applying as a filter to an actual image, of course, Max pooling would look very strange because it would just clamp everything to the max brightness. So, to speak, and the average pooling would look better.

**[04:58 – 05:08]** But that's that's not its purpose, really? And finally I also have illustrations on real networks. So you already know what restaurants are and this are

**[05:10 – 05:18]** Filters. These are the convolutional the matrices of convolutions, on the first layer of resnet 18.

**[05:19 – 05:26]** and you can actually see what they are trying to recognize some fire up or some kind of lines like

**[05:28 – 05:34]** And diagonal lines, vertical lines. Some fire for colors or color gradients, or something like that.

**[05:35 – 05:35]** and,

**[05:37 – 05:38]** if you actually,

**[05:39 – 05:56]** Input an image and see what exactly this filter is fire on, like, where do they activate a lot? Then you will see that. For example, this guy is looking for something like grass, I suppose it's just looking for the color green. And here is this

**[05:57 – 05:58]** and,

**[05:59 – 06:17]** I don't know, it's interesting here. This this guy on the right is looking for horizontal ages and it or vertical it just probably, and it activates like the Gabriel filter on there. There is a horizontal line.

**[06:19 – 06:37]** And if then we go through the network, and we map, what if what filters what? What active filters on different layers of the network to. And again, we go through the rest of 18 and look at what happening inside

**[06:39 – 06:50]** Again, you will see that again here. The math becomes a little bit more complicated with me. Let me not go into that because for layer 1, you can just basically see

**[06:51 – 07:00]** Like the inputs are the pixels. Here is the filter where that's activated here then on subsequent layers as you understand now?

**[07:01 – 07:20]** There is not such a direct correspondence between pixels and outputs. Right? Because yeah, every picks, every feature has a reception field, you can find, which part of the image is looking at. But

**[07:21 – 07:23]** What exact pixel server?

**[07:24 – 07:38]** Contributing the most that requires a little bit of math. So I will skip that but you can actually look at what parts of the image. Even top layer features fire up for and you can see that for example in resonate 18,

**[07:40 – 07:49]** the second player Fires for some, I don't know how high frequency stuff in the

**[07:51 – 08:34]** In the image, I throw out the whole image but just some kind of, you know, stripes or something and edges and stuff like that and then we go for more Salient objects, right? So here, for example, there is some filter that fires for the eyes and the tips of the ears, something like that. And then when we go to later layers, we become like more and more semantics. So, in this picture, I don't think it's that clear their waiter blurry and Trust not, 18 is not a very good network, but still you can see that kind of there is a filter for the ears. There is a filter for for the head as a whole and so

**[08:36 – 08:37]** Or.

**[08:38 – 08:59]** You can actually go back from a deep feature, back to the pixel level, right? So this, yes, sir, I didn't explain it well, but this was on the level of the feature maps on the level of the feature maps. I mean it becomes blurry and blurred. There are. There is less Germany, just makes us cents.

**[08:59 – 09:26]** But you can also with this math, that I mentioned map, it back like the original image to the filters of the original image. And you can see approximately. Now, it's not precise but you can see approximately what the fires on, and it's pretty interesting, right? So, interesting at 18, on a deep layer, you can find the feature that, like selects most for the cats. So what that means to be Kettle left, if it means that

**[09:27 – 09:34]** Resonate was trained to distinguish classes from the image. Net, like it.

**[09:36 – 10:21]** And dogs, and you can actually find which feature gives you the most information regarding this specific class, which feature correlates like, who's activation correlates the best with this specific class. And if you look at the cat selector feature and you input an image, which is have like this one and just merge two together, that's it, then you will see that at first on the cat and the dog selector feature in deep fires up on the dock approximately. So this kind of works and also I want to mention again. I don't I don't want to spend time discussing the math but there is there are also methods for more

**[10:22 – 10:25]** the detailed interpretation of

**[10:29 – 10:58]** more detailed interpretation of what the network actually is doing. So there is, for example. Great chem. It's not the only one, but it's a good one. And if you can run it for for the network output, like the predicted class, a single class. Right? Again, we call it the networks output is this set of probabilities so every class in a classification network is a separate output which is convenient in cases like this because we can actually

**[11:00 – 11:16]** We can actually look at specific outputs and for example, the Egyptian cat output response to these and it has been has obtained the value that has due to the pixels like this.

**[11:17 – 11:31]** So it's not yet an attention mechanism will get to those tomorrow, but it's kind of an interpretation of what exactly why exactly. Due to which pixels the network shows this value for this.

**[11:32 – 11:45]** And sure enough, you can, you can run it for different classes, for example. Again, if you can't get the dog and the Egyptian cat output will look at the cat and they went heimes panel output, will look at the look that's

**[11:47 – 12:00]** Okay, so that was a brief remark about what we will not discuss in more detail, so about the basics of convolutional networks what they're looking.

**[12:01 – 12:18]** Now let's get to the main part, I think of today and the main part is important convolutional architectures. And hopefully this will be only the first main part because some of the most important stuff you have already discussed through that, right?

**[12:19 – 12:19]** so,

**[12:20 – 12:24]** The most important convolutional architecture and history.

**[12:24 – 12:36]** Was of course alexnet. And I hope that Alex discussed she's architecture with you and if not I guess by now we can skip it. So it was like the first

**[12:37 – 12:59]** convolutional Network that actually worked. They beat every competing method completely on the image. Net recognition, large-scale English or conditional competition, and that defines the state of the art in an extraordinary in extraordinary.

**[13:00 – 13:40]** A big margin. So in 2011, or 2012, when it was participating in this competition, the results were, like, like the error rate for all of the rest of the methods was like 22% 23 percent. Something like this. And the error rate for Alex was like 13%. So it was a huge jump, a huge gap. And of course, next year, the whole leaderboard was only conversational networks. Nobody ever went back to classical computer Asian since alexnet. This was this was the revolution that happened in image process.

**[13:44 – 13:57]** And technically and in terms of like specific ideas, what is most interesting in ALEKS and our two things. So it's pretty standard, polish, Mark architecture, but

**[13:58 – 14:02]** you can see first that it's split into,

**[14:04 – 14:10]** and that was the first actual, like industrial scale instance of

**[14:11 – 14:13]** Model, paralyzation.

**[14:13 – 14:32]** So this is very important. We won't have time to go into more details so now it's a good time to just mention it. In deep learning, you have huge models, you have huge data sets. So of course you need to paralyze. You need to make use of multiple say gpus if you have multiple gpus and

**[14:33 – 14:36]** there are two main ways that you can do it.

**[14:37 – 14:39]** You can do what is called Data, politicization.

**[14:40 – 14:46]** Data parallelization is when you I don't know when you have one, miniature GPU one.

**[14:47 – 15:18]** Another meaning patient GPU and other minimization GPS 3, you run the model and then you collect the results and you do a single update based on the weight updates from all of the GPS. So you don't have to change anything in your implementation are the network works. Just as usual. The only difference is that since now you have multiple GPS and parallel, you can collect, you can basically your chest increase in the mini batch size for yourself, right? So what you are actually doing.

**[15:20 – 15:21]** Yes, you are.

**[15:25 – 15:28]** You are expanding the.

**[15:29 – 15:50]** Your expanding the the size of very post your expanding your minimum wage size by splitting the Mini version of different gpus that that's data prioritization. There's a lot of work on that because you can do it in many different smart and interesting ways.

**[15:51 – 15:54]** But like the basic idea is very simple.

**[15:54 – 15:58]** Model prioritization is more complicated in model personalization.

**[15:59 – 16:11]** The assumption is that your model does not fit on your GPU, right? And if your model does not fit on your GPU, what can you do? Well, you need to put like half of your model online, you and another half on the

**[16:12 – 16:16]** other and that's exactly what Alex was doing back in 2001 already.

**[16:17 – 16:22]** so, 2212 is the paper, but the actual Network wasn't until

**[16:23 – 16:23]** and,

**[16:25 – 16:37]** Of course, that was like a huge hit of engineering back in here. 11 was a wonderful programmer. And she actually implemented all of this by hand.

**[16:38 – 16:39]** These days.

**[16:40 – 16:50]** Of course, we don't need to implement anything by hand and even our Cloud codes do not need to implement this. By hand, in Partnership, you can just say

**[16:51 – 17:00]** Well, I want this weight Matrix to leave on this GPU and that way it Matrix to leave and they GPU and by touch will just handle the rest of them.

**[17:01 – 17:12]** But still when you design a parallel Network like this network, that spans multiple gpus you want to minimize communication across the gpus because of course it will be slower than inside one appear.

**[17:13 – 17:15]** so here, for example, you can see that

**[17:17 – 17:29]** these guys talk to the two strands, the 2gbps talk to each other over here and then talk to each other at the very end. There are only two places where they actually exchanged information.

**[17:31 – 17:33]** anyway, I'll explain, it was

**[17:37 – 17:38]** the Breakthrough.

**[17:39 – 17:43]** People like to talk of like the Alex Smith moment or something.

**[17:44 – 17:45]** and, but then, of course,

**[17:46 – 17:56]** The field exploded. Everybody wanted to do convolutional networks, and it turned out that you can actually improved conversational networks. Quite a lot with relatively simple ideas.

**[17:57 – 17:58]** so,

**[18:00 – 18:02]** some of the most important ideas you already discussed,

**[18:03 – 18:07]** with Alex, not krishevsky but Alex the Widow and

**[18:09 – 18:11]** Like the first idea is vgm.

**[18:12 – 18:29]** And vtg is the reason why alexnet still had like 11 by 11 convolution on the first layer. But now you will never see 11 by 11 conversions. You will only see three by three, convolutions and maybe five five sometimes because

**[18:31 – 18:32]** We?

**[18:34 – 19:11]** Idea. You can represent a large convolution, as compositions of small conversations, and this is actually a great way to do things because it's like a convolution inside a conversation, right? And this convolution inside it in relation, reduces the number of ways Earth. I think you need this with calculations of how many ways and it's kind of additional structural organization. Again, you're saying to the network, you can process different parts of the input in the same way and usually just works better.

**[19:12 – 19:15]** so the second idea,

**[19:16 – 19:23]** That you also discussed through that, it's as far as he told me is Inception.

**[19:24 – 19:34]** And Googling it and generally like the idea that is known as Network and network. So I started

**[19:35 – 19:50]** talking about convolutional networks with you with this. I want page back to them, but you remember the slide with this boy, on a toy horse and all of this and like there.

**[19:51 – 20:00]** there were tiles being processed by what I call small neural networks on this what was called small neural network on this picture,

**[20:02 – 20:17]** And since then, when we actually implemented this morning on networks, they were always like the simplest possible in your own networks. They were always talking only about a single Matrix that processes, the whole input.

**[20:19 – 20:23]** And doesn't care and doesn't do anything. Interesting. Just

**[20:24 – 20:31]** And put everything together, throw it to a single Vector of numbers multiplied by this weight Matrix here is the output.

**[20:32 – 20:50]** But you don't have to limit yourself to that, right? You don't have to, you don't have to do that, right? You can do more interesting things and this Inception trick and basically this idea of

**[20:52 – 20:55]** network and network are exactly this. You can

**[20:59 – 21:08]** you can replace this simple convolution with a far more complicated approach, far more complicated Network, and when you do that,

**[21:09 – 21:10]** You still have.

**[21:11 – 21:14]** if they have the same idea of

**[21:15 – 21:22]** processing the tiles in parallel, with the same small Network, it's only that the small network is now more interesting.

**[21:23 – 21:41]** So yeah, I think you discussed Inception, I want to repeat that. What I want to know here, is that when you look at like this Inception units, when you look at this, small Network, so to speak, you see usually multiple parallel threads of processing.

**[21:42 – 21:46]** And that is not a coincidence and we will talk more about that today.

**[21:49 – 21:50]** Okay, so

**[21:51 – 21:51]** Third.

**[21:52 – 22:13]** The most important idea of all of this, the idea that will be with us throughout the whole deep learning, it will be used in Transformers, it's used everywhere. The idea of physio connections and thus redness again, Alex said that you already discussed it, so I will mostly skip

**[22:14 – 23:04]** Basically, the idea is like this. I apologize. Keep forgetting to the redo the Russian picture, but anyways, this is, this is input. So the input is X and f of x. And the next layer is like this. F of x. And the rest have problem is that when f of x trains and saturates, the gradients will go to 0. They this layer will not want to change anymore, and when it doesn't want to change anymore, that's okay for the layer. But if you didn't have a residual connection, it would mean that nothing below that player will ever learned right? Because everything below the layer receives gradients through the Slayer multiplied by

**[23:05 – 23:49]** Derivatives and they both go to zero, then nothing changes below that. That's that's a bad thing. So what we do is we use residual connections like here, we do a connection that goes around here, we have something very simple and specifically just the plus and now our result is f of x plus XK and now f of x can saturate all at once the derivative can go to 0 that's fine if it goes to 0 then the great interest goes to the Matrix of derivatives just goes to an identity Matrix and the gradient will just flow through the Slayer and now through but throws flow around the Slayer and continue to the bottom layers.

**[23:50 – 23:50]** and,

**[23:52 – 23:54]** as soon as resonates or introduced,

**[23:55 – 24:14]** I mean here this guy who invented wrestlers and he is actually very cool researcher with a lot of great papers. I mean here called it the revolution of that and did it was so when residual connections were introduced and were used and deep convolutional architectures

**[24:16 – 24:41]** You immediately could train networks with hundreds and hundreds of layers. So like Alex, Ned had eight trainable layers. We don't count pulling here VGA had 19 layers googlenet had within the first Inception units, had 22 layers and resnet. Next year had like 150 layers and there was

**[24:42 – 24:44]** Total in no problem to.

**[24:47 – 24:49]** there was no problem to

**[24:54 – 25:04]** to grow further. There was no problem to increase the depth for further you can do resonate 200 300 500 to 1000 and it will still train.

**[25:05 – 25:08]** It will still be fine. The problem only is that

**[25:10 – 25:29]** It will stop improving, right? So it will still be trained and we'll still do the job, but if you increase your net, for another factor of two and the results don't improve well, maybe you shouldn't be doing that, right? So it only makes sense to it new layers while they still help.

**[25:30 – 25:37]** So actual resnet go up to about 200 layers and then I guess they run out of stem.

**[25:38 – 25:38]** Okay.

**[25:40 – 25:46]** So as far as I understood that, it's if I understood him correctly, this is approximately where you stopped.

**[25:47 – 26:07]** And let me complete this Arc. Let me continue this discussion of different conventional ideas of ideas that kind of Define conventional architectures with our next with our first

**[26:08 – 26:13]** Details point point one, which is the bottleneck layers.

**[26:15 – 26:21]** Bottle next and an idea that is usually called split Transformer.

**[26:22 – 26:26]** Sorry, I'm not yet. Used to write. Okay.

**[26:33 – 26:35]** Split Transformers.

**[26:37 – 26:38]** so,

**[26:39 – 26:41]** What the bottleneck idea?

**[26:41 – 26:46]** well actually, you can look at for example, the VGA idea,

**[26:47 – 26:47]** As.

**[26:48 – 27:02]** Another way to reduce the number of ways, right? Because you replace big conversation which has N squared weights with a sequence of small conversations, we have linear Enon weights and that's great.

**[27:03 – 27:03]** so,

**[27:04 – 27:07]** So, convolution by the cells already.

**[27:08 – 27:10]** Start off by saving a huge number of weights.

**[27:11 – 27:16]** You can actually try to do better. You can actually try to reduce even further.

**[27:17 – 27:19]** and let's just

**[27:20 – 27:26]** Step back. Look at a conversational layer and see where and what we can improve. So

**[27:27 – 27:34]** a standard conversational layer will have some 3D tensor as the input, so the input will be of size.

**[27:35 – 27:43]** okay, so let's let's actually say that this is already the window that I cut out because I never want to care about the

**[27:47 – 27:58]** and everyone to care about the full input. It's always just copy it over. So this is already the cars out window and it has like depth deep with w and height h.

**[27:59 – 28:02]** Right. Then we go to the convolutional layer.

**[28:03 – 28:09]** and as a result of the convolutional layer, we get a single Vector of

**[28:12 – 28:15]** features of size T Prime.

**[28:15 – 28:27]** So a standard convolutional layer will will be will have the Matrix of Weights of Dimensions, D times, W Times H times the prep

**[28:28 – 28:28]** Right.

**[28:30 – 28:38]** And as we discussed is much, much much, much better than if we try to do it with the fully connected layer or something else. But still, it can actually

**[28:39 – 28:41]** Add up, it can grow pretty quickly. So,

**[28:42 – 29:10]** If for example, I D is something like 2506 which is pretty standard Insight big Coalition architecture. And deprime is also something like the 56, to 56. Then even I mean, the beach chair idea. Let's you keep double and a small. But still in here, you have like this tensor of weights to 56 by 3, by 3, by 2506.

**[29:11 – 29:14]** And that's a pretty big number, right? So that's like,

**[29:15 – 29:27]** Oh, I don't know. 2500 times another 25. Okay. I embedded method this level but you can figure it out. What's 25 squared? It's not 725, right.

**[29:28 – 29:31]** So, it's 75k.

**[29:32 – 29:33]** I guess, no.

**[29:34 – 29:39]** No, it's 750k. So I'm 700 k something like this.

**[29:40 – 29:40]** Right.

**[29:42 – 29:50]** Wait. Yeah the 50 by 250 is 75k and times 9. Yes, or something like that. Something like that sound 100k.

**[29:52 – 29:54]** Which is quite a lot, right?

**[29:56 – 30:13]** So, how can we reduce this? Where, like, where is the, what is the problem that we might somehow solve here? Like, where where can we save on these weights?

**[30:14 – 30:17]** The bottleneck idea is actually it's a straightforward.

**[30:18 – 30:20]** And it goes like this. What if?

**[30:21 – 30:22]** instead of

**[30:23 – 30:28]** getting the full 256 by 256, multiplied, by 9

**[30:29 – 30:36]** what if we actually compressed the features down and only when did the convolution

**[30:37 – 30:42]** So, here is how it would work, you have your input.

**[30:44 – 30:51]** And your input is low. It's like e times double W Times h.

**[30:52 – 31:00]** And But first you would run it through a one by one conversation. I hope you discuss those with Alex, one by one conversion.

**[31:01 – 31:03]** Just by definition, that's not do anything geometric.

**[31:04 – 31:06]** It just takes one.

**[31:07 – 31:10]** feature Vector here and

**[31:14 – 31:25]** rearranges it, right? That's something interesting. Inside the feature Vector, but it doesn't, it doesn't do anything to the geometry to the receptive fields to anything like that.

**[31:26 – 31:41]** And what if we used this one by one? Convolution to actually reduce the depth to reduce the number of channels that now I would have something like deer. And double Prime Times, W Times H with e double Prime small.

**[31:42 – 31:47]** So if I had D like 256, maybe the double Prime is like 32.

**[31:50 – 31:54]** And then I would have my broken Revolution here.

**[31:55 – 31:57]** And it would give me.

**[32:00 – 32:07]** A short Vector so formerly. I would put like the triple prime here. But okay, let's just say it's the double Prime 2.

**[32:08 – 32:20]** And then I would have another one by one conversation. If I do want to have like, d Prime at the output, then I would have to stretch back this feature Vector to size the prime

**[32:22 – 32:33]** So, the convolution itself. So, the okay, the the one by one valuation. Now has like the times one times one.

**[32:34 – 32:36]** Times d. Double Prime weights.

**[32:38 – 32:42]** This is one by one. Convolution, this can valuation has how many weights?

**[32:44 – 32:48]** D double Prime Times W Times H times, d, double Prime.

**[32:49 – 32:54]** and also this conversion is the double Prime times one times, one times, the prime

**[32:56 – 33:04]** So you can kind of get a feeling for What's Happening Here, Right? I avoid multiplying 256 squared by 9.

**[33:05 – 33:16]** And actually I avoid to 56 squared completely. Right. There's still a nine in there. It still gets multiplied by something but that's something as much smaller than 2506.

**[33:16 – 33:30]** So let's plug in the numbers in this. In this example, it would be like 2:56 times 32 plus these 2. 56 times 9 times. Oh sorry, sorry sorry plus

**[33:32 – 33:41]** Plus 32 times, 9 times, 32, right plus again, 32 times to 56. So even though I have

**[33:42 – 34:01]** Reconciles instead of one now, I still save a lot of ways. So let me pull to 56 out of 32. Plus what? Now, I have to take a four out of this. So no I have to take an 8 out of this so for his left hand by four.

**[34:02 – 34:20]** And another 302. So it's 32 and 30 to 64 and 36, exactly. 100, that will be like, 2:56 times 100, right? And over there, I had to 56 times 2500, right? I'm still 56 times 9.

**[34:21 – 34:23]** so, this is about

**[34:24 – 34:29]** In our simple example, that's about like 25, its smaller.

**[34:30 – 34:33]** 25x smaller, and

**[34:34 – 34:37]** We have saved a lot of weights.

**[34:38 – 34:39]** Okay, a lot of ways.

**[34:42 – 34:43]** well, but

**[34:44 – 34:46]** now, when you look at this idea,

**[34:47 – 34:48]** Something.

**[34:49 – 34:59]** Should feel funny to you about it. Something should not sit right with you about this idea. And what is that? What is the problem here? Oh,

**[35:02 – 35:04]** What did I just do?

**[35:04 – 35:21]** I took effect of 2506 of a long character of the 56 features, so in the input every pixel, every feature map every teacher Rector was long and had a lot of information was like, 250 numbers.

**[35:22 – 35:25]** And then you just compressed it down to 32 numbers.

**[35:26 – 35:28]** Then I did interesting stuff on 32 numbers.

**[35:29 – 35:44]** And then somehow I decompressed that to 56 but then the compression cannot restore the information that I lost, right? So what I'm doing here is I'm taking a long and interesting Rector

**[35:45 – 35:54]** So, geometrically speaking, I'm leaving, I'm in the future space of

**[35:57 – 36:05]** a high dimension like 256. But inside this feature space, I am picking a specific

**[36:06 – 36:08]** Subspace specific projection.

**[36:09 – 36:14]** Of this much smaller damage.

**[36:15 – 36:15]** Right.

**[36:16 – 36:17]** so, I am reducing

**[36:19 – 36:30]** My features that are long and interesting, and the complicated down to a much simpler thing to a much smaller Dimension. I'm like, just taking one of you of this thing's

**[36:32 – 36:33]** and,

**[36:34 – 36:39]** That's doesn't sound that bad. But if you think about it,

**[36:40 – 36:45]** it doesn't make any sense to actually do what I'm proposing here. Because if

**[36:48 – 36:54]** I just compressed down to 56 for numbers worth of information to 32.

**[36:55 – 36:58]** Why on Earth do I need to 56 numbers at all?

**[36:58 – 37:04]** I mean, this is happening inside a network that I am designing myself.

**[37:04 – 37:12]** It's not these. 256 numbers. Did not grow on a tree. They came from an earlier layer. So if all I wanted to do was this

**[37:14 – 37:14]** Then.

**[37:15 – 37:19]** I would just replace d by the double Prime.

**[37:20 – 37:27]** I would just say, okay, so let the previous layer produce 32 features. Why do I need the artificial compression? Decompression stuff.

**[37:28 – 37:29]** and that would,

**[37:30 – 37:31]** That would save a little bit more weights.

**[37:34 – 37:34]** And that would be even better.

**[37:35 – 37:35]** Right.

**[37:37 – 37:49]** So, the way I told you this bottle neck, I idea it doesn't work by itself and he did it doesn't. And never appears like that, but it's suddenly starts to make a lot of sense.

**[37:51 – 37:55]** if you do it, not once but several times,

**[37:56 – 38:00]** so, how would actually gets used is

**[38:02 – 38:02]** You start.

**[38:03 – 38:09]** With this long, the simple answer did times. W Times h.

**[38:10 – 38:14]** And then you do like several copies of this of this processing.

**[38:16 – 38:17]** Pipelines.

**[38:17 – 38:21]** So like you have one by one then convolution you have

**[38:22 – 38:24]** One by one then convolution.

**[38:25 – 38:26]** And so on.

**[38:27 – 38:28]** and then,

**[38:30 – 38:37]** You somehow unite the results, you combine the results. So for example, in this case, it could be like this.

**[38:40 – 38:50]** I have D to 56 and out here. I have a vector of size 32, right? So

**[38:51 – 39:06]** How many vectors of 302? I need to have a new Vector of size to 56. Oh, eight of them, right? So why don't they just copy this eight times and concatenate the results like this,

**[39:10 – 39:12]** this is a pretty standard way, and this

**[39:12 – 39:17]** So, I do my processing eight separate times.

**[39:18 – 39:21]** notice that even though it's

**[39:22 – 39:45]** Ah, even though it's the same picture, it's the same structure of processing. The actual processing will be very different, right? Because this strands, this Pathways will learn different ways. They will do different things. You need to break the Symmetry and initialization, and then they will just hyper to go to different minimize to do different, to implement different ideas,

**[39:46 – 39:50]** And yes, now I'm not saying 25x rates.

**[39:51 – 40:08]** Because now to actually go from 256 to 56, I need to copy this for eight times, right? So now, instead of saving instead of saving 25x, I'm only saying Forex rates

**[40:10 – 40:16]** but it's still a pretty big sale, right? And actually it turns out that in practice, it's a pretty good idea.

**[40:17 – 40:22]** so what we are actually doing is in this huge space,

**[40:22 – 40:24]** we are choosing not one.

**[40:25 – 40:51]** Projection, not one way to reduce the dimension, but we are choosing multiple different ways. Multiple different viewpoints on on this complicated features. And so I look at it from this side and then I look at it from this side and then I look at it from that side and it's like different projections, different snapshots of this.

**[40:52 – 40:52]** Same.

**[40:54 – 40:59]** Big space of features. And when you actually do that, it's it's very interesting and it's

**[41:01 – 41:10]** Now it's not just it. Usually you can train it to not lose any important information but even better

**[41:11 – 41:13]** you can actually like,

**[41:15 – 41:18]** say this, you can actually

**[41:20 – 41:36]** Fit to do even better than if you just process this whole to 56 thing. So it's it's actually and I cannot get into food detail to explain why. But it's actually a good idea to do like

**[41:37 – 41:53]** Awards. If even do lots of random projections of your high dimensional object even that is usually a good idea. And here, the projections are not random right here, the projections are learned and they are learned to be useful, which is even better. So

**[41:55 – 41:56]** This is usually called.

**[41:57 – 41:58]** Split Transformer.

**[42:00 – 42:01]** Or obvious reasons.

**[42:02 – 42:12]** First is split, then you transform, then you merge and it's a pretty standard idea in convolutional architectures.

**[42:12 – 42:39]** So I guess that's the important thing that I wanted to say. Let's go back to the slide. Yes. But here is an example in the next kind of outdated. Now then it was 10 years ago but a perfect example of just and yeah like this just pleated to 56 into 32 path of four so it's like an extreme projection. But several extreme projections and that's better.

**[42:42 – 42:47]** So what else can I say about this classical convolutional architectures? Well,

**[42:48 – 43:29]** I probably should mention this line of inception networks and Inception, resnet networks. I'm not sure if you discuss them with Alex, you discussed Inception, you discussed resnet. But what about the combination and basically, the progression of this networks there? A pretty important family of networks. They were like, for a long time, the best available backbones for all sorts of computer vision tasks. When we get the object detection, we will discuss the object detection, segmentation we will be discussed how

**[43:30 – 43:31]** for example.

**[43:34 – 43:43]** How we will just discuss how when you do an object detection architecture or segmentation architecture. You can't really expect train it from scratch.

**[43:44 – 43:53]** So there will be not enough label data to train from scratch because labeling was very difficult for this complicated computer vision tasks.

**[43:54 – 44:13]** So what you actually do in practice is you take what is called the backbone? You take a network trained on image net. For example, to justify stuff, then you cut off its head and you use the rest of the network as a feature. Extractors, maybe you find units or maybe not.

**[44:14 – 44:26]** R and this Inception resnet, family was one of the most influential one of the best families of this backbones back in 2016. And

**[44:26 – 44:49]** What is its main idea? Of course doesn't make sense to learn them and big detail but its main idea was that you do this Inception trick you, you do this network and network thing, you replace a, you do better and better, basic blocks, that process, the inputs like the small neural networks,

**[44:50 – 44:52]** and from version to version, they

**[44:53 – 45:09]** Just invented better and better such basic blocks. Basically that that was the main component of progress. And another component. Interesting component of progress was that they all saw replaced pooling clears with blocks like this.

**[45:10 – 45:18]** and I think women, I mentioned this last time, like, if you want to reduce your dimension, if you want to reduce from,

**[45:19 – 46:19]** Ah sorry. If you want to reduce from 256 by 256 image down to 128 by 128 image. Yeah, you can do exponent but it's even better to have another Network and network thing. Another layer that can be trained and that can do it more interesting stuff, only that you tune this. You you compose this for air and such a way that the output becomes smaller how you do that. Usually, let's try it. Let's try that convention. That just reuse them in Geometry, that's what they do. So over here, the indeed in late later, Inception Network, stay indeed have this reduction blocks that can have pulling inside but it's again, this kind of Transformer split and merge idea. So there are several. Several several lines of

**[46:19 – 46:29]** Processing here that do different things and then they are merged together. And so in some way, so this has been influential idea in college.

**[46:31 – 46:45]** And then you have residual connections and we get Inception right now. That's it, won't go into more details, but basically, like conception resonate. V2 was a very influential, very interesting.

**[46:48 – 46:52]** Backbone. That was used very widely.

**[46:54 – 47:01]** Okay, so I will probably keep the rest mostly there were

**[47:02 – 47:29]** Some more ideas on how to further reduce the size of the network and also, to reduce the number of layers, and let me not go into this idea in detail, but this basic trade of not Trader. But this way there are basically two different things that you want to optimize one is memory. You want to have a smaller network if you want to, for example, fit to a mobile device or something.

**[47:30 – 47:36]** And that means, we use the number of ways because basically the size of the network is the number of ways. That's it.

**[47:39 – 47:48]** And then there is also another dimension which is latency, which is how quickly the network will actually operate.

**[47:49 – 48:23]** So in computer vision you often care about latency. For example, if you do something like trekking on a surveillance camera, then of course you needed to work in real time because this surveillance camera will work like 24/7. And of course, you can't leg behind the video stream while you're processing a continuous video stream. Right? So you definitely want your tracking or whatever you do with this stream, you definitely want it to work and like 30 frames per second at least.

**[48:25 – 48:27]** And preferably 60.

**[48:28 – 48:35]** So latency is also important. And what I wanted to just note here is that there are two different things

**[48:36 – 48:42]** I mean, to some extent. It's true that if you have a smaller Network, it will run faster.

**[48:43 – 48:46]** But actually, the latency depends on the number of layers.

**[48:47 – 48:51]** Because once the network fits into your GPO,

**[48:52 – 48:56]** the rest is more or less than parallel inside the layer.

**[48:57 – 48:57]** and,

**[49:00 – 49:16]** What actually matters is, how many steps you make? So every step. Okay, so depend on say, the intermediate representation size. Yes. Of course, it will. This forward, you have more weights inside every layer but the most important component is the number of players

**[49:17 – 49:19]** so, these two

**[49:19 – 49:20]** Things.

**[49:21 – 49:50]** Make networks faster or make them smaller. They don't conflict that much. But there are two different objectives just wanted to mention that and yeah, let's keep squeezing it. Nothing new for us here. Let's keep mobile net. Here it indeed. Was the whole thing was indeed to put computer original mobile devices. And finally, I think what I want to end this discussion with finally,

**[49:54 – 49:55]** the like,

**[49:56 – 49:59]** family of CNN's, that kind of

**[50:00 – 50:01]** topped.

**[50:01 – 50:12]** This progress of CNN, architectures. And that, I mean, probably there was something afterwards, but mostly even now everybody just uses this.

**[50:15 – 50:20]** The line of networks that proved to be the best work efficiently.

**[50:21 – 50:31]** And again, I don't want to go into too much detail, but it's again, the same story that we saw. We've

**[50:32 – 50:40]** Activation functions. And then I mentioned that we saw a similar story with

**[50:43 – 50:54]** gradient descent algorithms, but the gradient Central grid Transportation discuss that and here in efficient meth, the architecture was actually

**[50:57 – 51:04]** The architecture was actually found automatically with a big neural architecture search.

**[51:06 – 51:06]** So,

**[51:09 – 51:33]** Yeah, so what they did and again, not too much detail but just the basic idea what they did was they looked at how you scale a convolutional network. Like when you increase the network in, what ways can you increase and network like what are the different dimensions that you can change? What are they?

**[51:35 – 51:41]** notes that you can rotate and tweak in order to change put the network test,

**[51:42 – 51:51]** And it turns out there are quite a few knobs, right? So, you can change the depth of the network, obviously, you can change so you can add more layers.

**[51:52 – 51:56]** You can change the width of the network you can.

**[52:00 – 52:01]** More.

**[52:03 – 52:39]** That you can add so sorry, we usually call it depth, but yeah. Inefficient that is the number of layers which also is very reasonable to call that and with like the, the length of the feature Vector. So you can make the network wider by adding more features that allows you to make the network smarter, but Spain more weights. And also you can do something like higher resolution so you can increase the number of pixels in the input so to speak.

**[52:41 – 53:03]** And then what they did was, they just rolled down some very simple formulas, like, okay? So as I increase the network, I increase the depth, the wheat, and there is a lotion. How does the total size of the network change? Well, you multiply them all together. You get like, the product of three numbers and it goes into the exponent. And this is the number of ways.

**[53:03 – 53:10]** Okay. So what are we looking for? We are looking for the perfect balance between these three numbers.

**[53:11 – 53:12]** so, basically, the idea is

**[53:15 – 53:27]** If your depth grows exponentially with exponent Alpha your weed, growth exponentially with exponent beta, there's a solution, grows exponentially with exponent game.

**[53:28 – 53:35]** Then there is like an actual relation between alphabet and Gamma, but then you need to actually find the best ways.

**[53:36 – 53:36]** so,

**[53:38 – 54:01]** That's what they get. Then, they run like, huge evolutionary search, to find this best combinations of hyperparameters and they were successful. They were pretty successful, and this family of efficient efficient Network family. As you can see here, basically just Define

**[54:02 – 54:14]** The state of the art, right? Define a cross the whole field. So we will see plots like this later in for other computer vision tasks here at all. So it's pretty

**[54:15 – 54:36]** I think instructive to look at how this plot works. It's there are two axis, right? One of the x-axis is the number of parameters. So here the larger the network is, it's bad, right? So you want to to have an efficient Network. So you want to have fewer parameters and

**[54:37 – 54:46]** The y-axis is imaginative one accuracy. So basically how good the network is, what is the result here? Higher is better.

**[54:46 – 54:57]** So this means that your best networks will lie in the top left corner. You want to be in the top left corner, I want to have a small Network, that works very well.

**[54:58 – 55:04]** And, of course, you can't have both at once. There is a trade of here, large networks will work better than smaller. That's okay.

**[55:06 – 55:11]** so what people are actually looking for is like a Pareto Frontier,

**[55:12 – 55:13]** In this.

**[55:14 – 55:24]** Plot is the frontier where for every size you have the best possible Network and for every Target quality, you have the smallest possible Network.

**[55:25 – 55:27]** so as you can see, the efficient family,

**[55:28 – 55:31]** Pretty much succeeded with the filing. This Frontier everywhere.

**[55:31 – 55:32]** and,

**[55:33 – 55:34]** Ever since then.

**[55:36 – 55:52]** I think maybe I've missed something. It's not like I follow all of the papers that appear, but I think there hasn't been any Revolution since then, correlational networks. So of course, in a large extent, everybody switched to Transformers so we'll discuss that, of course, but

**[55:56 – 56:08]** But in conversation networks, I think the question at the still like the best underlying architecture and for some object detection pipelines and implementation pipelines, sufficient. Net is still the backbone.

**[56:09 – 56:09]** so,

**[56:10 – 56:11]** so, we got to

**[56:12 – 56:15]** We go to the state of the basic.

**[56:22 – 56:22]** Okay.

**[56:25 – 56:26]** Yeah. So

**[56:28 – 56:32]** I will skip bitch Norm because I said that you already just discussed it with him.

**[56:32 – 57:05]** So, let me, I mean, there's there's not much that I wanted to say here except explain how it works. So here is how it works. I think you've discussed this already and I also, yeah, also have this. Yeah, this nice picture of different variations of which Norm, so I'm not sure if you discussed that, but usually, you would have bleach normal where you ever reach over average, the same feature over.

**[57:07 – 57:09]** The spatial dimensions.

**[57:10 – 57:14]** So across the image and all so over the mini beach exams.

**[57:14 – 57:32]** But sometimes you would you would like to do something like layer Norm where you don't have reach over the meaning page. And to be honest, when you use layer Norm, usually, just means that, you're mean which says one. So there is no meaning to every shower, which means that

**[57:33 – 57:35]** instead, you just average over the whole

**[57:36 – 57:44]** Ends are features. So now you just have a global statistics for for the whole year.

**[57:45 – 58:04]** A layer Norms layer Norm is used all the time in Transformers because Transformers are big. And they're usually, you cannot expect to have any significant meaning page. So you need to you need to have normalization inside of a single training sample.

**[58:05 – 58:12]** And then you can actually do if even even something more interesting here, but let's not go into the test.

**[58:13 – 58:19]** And it's also a pretty big filled with dozens of papers, lots of results, blah.

**[58:20 – 58:20]** Okay.

**[58:21 – 58:22]** Interest that.

**[58:23 – 58:27]** I think I will. I have. I'm done with

**[58:29 – 58:30]** Relational Networks.

**[58:31 – 58:41]** they will note out encounter more of them in practice and practical sessions and

**[58:42 – 58:45]** I want to go to the next or next, big topic.

**[58:47 – 58:56]** Oh big in the sense of important and different but not that big. I think we will either finish it today or maybe have a little bit left over tomorrow.

**[58:57 – 59:00]** So, this big purpose is recurrent neural networks.

**[59:00 – 59:16]** And until Transformers appeared. They were like, they were like these two main strands of architectures in India, learning their work in evaluation on networks, and there were recurrent Networks.

**[59:17 – 59:24]** And recurrent networks were actually designed for and used for and with sequences.

**[59:25 – 59:28]** So what is the main idea?

**[59:29 – 59:32]** Of an RNN of a current neural network.

**[59:32 – 59:33]** Well.

**[59:34 – 59:34]** Quite often.

**[59:36 – 59:36]** You have.

**[59:38 – 59:42]** Quite quite quite often you, your input.

**[59:43 – 59:45]** Has the form of a sequence.

**[59:45 – 59:55]** So let me actually, yeah, let me go to the board and let's let's discuss this first module 8.

**[59:58 – 59:59]** Rnns. And

**[1:00:01 – 1:00:03]** Discuss what they actually.

**[1:00:04 – 1:00:16]** So when you have your input picture, when you have a big complicated input sometimes it doesn't have a natural way to

**[1:00:18 – 1:00:20]** to be represented as a sequence, for example,

**[1:00:22 – 1:00:23]** An image.

**[1:00:24 – 1:00:26]** Is not really a sequence.

**[1:00:26 – 1:00:29]** An image is a two-dimensional structure.

**[1:00:30 – 1:00:30]** and,

**[1:00:31 – 1:00:35]** It's not a 1D sequence of anything.

**[1:00:36 – 1:00:40]** So, for images, the natural way to go would be with something like cnns.

**[1:00:42 – 1:00:46]** but there are lots of types of inputs that are actually

**[1:00:47 – 1:00:48]** Like sequences.

**[1:00:49 – 1:00:53]** The probably the default example would be just Time series.

**[1:00:54 – 1:00:58]** Like, for example, Financial time series, or something like this.

**[1:00:59 – 1:01:02]** But there are more interesting examples, too sound.

**[1:01:03 – 1:01:41]** Is a sequence, right? It's a sequence of ticks with amplitude and yeah, in classical machine learning and classical digital found processing. You would they actually not be able to treat sound as just a sequence of amplitudes because in the sequence would be too long to long for classical machine learning to handle. So what you would actually do was, would be to, like, cut it up into packets of 2013 milliseconds or something. Then do feature obstruction on the packets but then still, you would have a sequence of this features.

**[1:01:42 – 1:01:43]** Picture actors.

**[1:01:44 – 1:01:46]** And of course, the main example is text.

**[1:01:47 – 1:01:48]** So text is

**[1:01:49 – 1:02:06]** Definitely a sequence. It's a sequence of tokens. We maybe will discuss a bit tokenization, in the context of Transformers, but Texas sequence of words, or generally speaking tokens or whatever, it definitely has one dimensional structure. All right.

**[1:02:08 – 1:02:10]** and when you have, when you work with sequences,

**[1:02:12 – 1:02:14]** there's a number of

**[1:02:15 – 1:02:16]** different things you can do.

**[1:02:17 – 1:02:25]** There is a number of different types of how you can frame a problem or what kinds of questions you can ask.

**[1:02:26 – 1:02:31]** So the simplest would be if you have a sequence like a text.

**[1:02:32 – 1:02:39]** Sequence of tokens and then you have just a single output. So this is your X and this is your why

**[1:02:40 – 1:02:42]** For example, classification.

**[1:02:43 – 1:02:58]** You have a text and you want to say oh is it, what is it about? What is the topic? And maybe it's like news stream and for every piece of news, you want to say is it sports or in politics or onions, whatever.

**[1:03:02 – 1:03:03]** A maybe.

**[1:03:04 – 1:03:10]** It's the other way around. Maybe it's like a single input.

**[1:03:11 – 1:03:15]** And then you need to enroll it into a sequence in the output.

**[1:03:17 – 1:03:30]** So this would be like sequence, generation problems, right? So just write text about something, for example, here, there would be a problem like captioning.

**[1:03:32 – 1:03:37]** I think we'll have examples of networks for captioning, like the x is an image.

**[1:03:38 – 1:03:46]** And then you take this image so it's not a sequence but you want to convert it into a sequence into text that will explain what you see on this image.

**[1:03:47 – 1:03:49]** Right? So that that's caption.

**[1:03:50 – 1:04:00]** And then of course, the most interesting for us problems would be something like sector 6 sequence to sequence problems where you have an input

**[1:04:01 – 1:04:03]** That is a sequence.

**[1:04:04 – 1:04:07]** And then you need to have an output, which is also a sequence.

**[1:04:09 – 1:04:13]** So this would be a problem, so I commissioned translation or something.

**[1:04:14 – 1:04:17]** when you have text as input and text as output,

**[1:04:19 – 1:04:24]** Or in other domains or even in text to, you could have like sequence labeling problems.

**[1:04:25 – 1:04:26]** Right.

**[1:04:27 – 1:04:32]** Sequence, labeling problems where you your input is a sequence.

**[1:04:33 – 1:04:42]** And your output is a sequence. So, this is X. This will be X. This is why, and your output is also a sequence.

**[1:04:43 – 1:04:47]** but it's a sequence that aligned to the input,

**[1:04:48 – 1:04:50]** so, for example,

**[1:04:52 – 1:05:08]** So like insect to set problems and sickness to sickness problems. You read the sequence. Your the input sequence. You understand what it's about? Like input paragraph. You understand what it is? And then you write out the output on the translation.

**[1:05:09 – 1:05:21]** In sequence labeling in NLP natural language processing. It would be problems like part of speech tagging for example. So you have a sequence of words and

**[1:05:23 – 1:05:29]** You need to assign a label to every one of these words. Why not?

**[1:05:29 – 1:05:30]** Right.

**[1:05:30 – 1:05:32]** Or.

**[1:05:33 – 1:05:46]** For example, you know, adding subtitles to it to a movie like you have this sequence, which is a video, I Want, by the way, I didn't mention videos here but of course, video is also a sequence.

**[1:05:46 – 1:05:53]** Right. It's a sequence of frames and every frame is an image but a sequence of images. Now is a video

**[1:05:54 – 1:05:56]** or you can have something like,

**[1:05:58 – 1:06:01]** putting subtitles subtitles behind the videos. So, for every frame,

**[1:06:03 – 1:06:09]** You would have the specific text that should be shown there, or, for example, object tracking.

**[1:06:10 – 1:06:24]** An object tracking. You have a video and you're supposed to follow an object inside this video, like do for example segmentation, but not on a single image but on a sequence of image, so that it tracks, the same object as it moves.

**[1:06:25 – 1:06:32]** And yeah, I was struggling to recall something from computerization. Here is an example from computer.

**[1:06:33 – 1:06:34]** okay, but

**[1:06:36 – 1:06:37]** whatever you do is there.

**[1:06:39 – 1:06:43]** It kind of like the methods that we have.

**[1:06:43 – 1:06:46]** The approaches that we have like convolutional Networks.

**[1:06:47 – 1:06:50]** They're they're not quite well suited.

**[1:06:50 – 1:06:52]** For dealing with sequences.

**[1:06:54 – 1:06:56]** what, what I mean here is

**[1:06:58 – 1:07:00]** Yes, you can do something like this.

**[1:07:01 – 1:07:10]** So, sorry about the right part. Look at the left part, you can do something like this, you can do a sliding window that goes along your input sequence. And then,

**[1:07:11 – 1:07:15]** It processes this part of the input sequence.

**[1:07:17 – 1:07:39]** And to an extent, it can work. There was a time when like convolutional approaches to natural language processing, more like Rivals to recurrent approaches then, of course, Transformers change everything. But it's it still like, it seems to be

**[1:07:41 – 1:07:52]** Prohibiting, the most important thing. The most important thing is we need to have a way a way to recall, inputs, from long ago.

**[1:07:53 – 1:08:10]** When we need to be able to have this understanding of the whole team sentence and ability to recall what was happening in the, in the sequence. A long time ago, when you read the paragraph of text, you definitely need to remember what the beginning was. Otherwise, the end will not make any sense,

**[1:08:12 – 1:08:13]** so,

**[1:08:14 – 1:08:18]** how can we achieve this with the neural architecture?

**[1:08:20 – 1:08:22]** Recurrent neural networks.

**[1:08:22 – 1:08:36]** Do it like this. So let's say we have an input, X1 X2, x t. Now it's natural to think of this excess like something in time, right? So Escape at all team.

**[1:08:37 – 1:08:40]** And we will do it like this.

**[1:08:43 – 1:08:52]** We will process every X, every input in the sequence separately.

**[1:08:54 – 1:08:54]** With this.

**[1:08:55 – 1:08:57]** Let's say small, neural network.

**[1:08:58 – 1:09:01]** Which would be called the recurrent unit.

**[1:09:02 – 1:09:09]** But this unit, let me draw it set correctly. This unit will have

**[1:09:10 – 1:09:32]** Two inputs and one or two outputs so it will have X as the input and also a hidden State age and other input. And its main job will be to process this new input and update modify, the hidden state. So that now it captures

**[1:09:34 – 1:09:46]** The sequence up and then up to and including X. And the assumption is that H actually captured the previous part of the sequence, the sequence before X,

**[1:09:46 – 1:10:33]** So formally just means that our recurrent unit is a function of two inputs X and H and the outputs H prime. It may be it also outputs like the output. So at some point we do need to have the output, right? Sometimes it makes sense to put it like at the output of every cell. Sometimes it makes sense to just use the last hidden state to do some kind of head and then produce the output. That depends on a specific problem. That's not that important. What is important is that we have this hidden State. This Vector numbers basically that goes along the network and is updated every time as very another accessory and other input.

**[1:10:34 – 1:10:36]** And we go go and hope for him.

**[1:10:37 – 1:10:43]** This x is modified in such a way that it actually like

**[1:10:45 – 1:10:57]** combines all of the relevant information from from the sequence so that we can just look at this X. And we can just say, all right, that is what the sequences about.

**[1:10:58 – 1:10:58]** Okay.

**[1:11:00 – 1:11:12]** So we need to initialize it with some kind of h0, and then here the output will be H1 H2 HT HD plus 1 and so on.

**[1:11:12 – 1:11:13]** Right.

**[1:11:14 – 1:11:14]** so,

**[1:11:15 – 1:11:19]** This is a standard recurrent Network.

**[1:11:22 – 1:11:26]** In like classical recurrent networks, what you would do.

**[1:11:29 – 1:11:38]** In classical recurrent networks, how would this cells look like they would be against some kind of simple linear things?

**[1:11:39 – 1:11:49]** So you would have your ex not here. Mainly here like what's inside this black box? What's inside this recurrence? So

**[1:11:51 – 1:11:53]** you would have your ex,

**[1:11:54 – 1:11:56]** Maybe multiplied by some Matrix.

**[1:11:57 – 1:12:12]** You would have your age, maybe, multiplied, by some other Matrix, then you did them together, and then you would okay, just take. So you would, you would pass them through some kind of activation function.

**[1:12:12 – 1:12:36]** Okay, so one standard approach to make in recurrent cells would be something like H Prime is G of a times X plus b times, H and here G is an activation function, something like hyperbolic tangent or real and a and b are weight matrices.

**[1:12:40 – 1:12:40]** Okay.

**[1:12:44 – 1:12:46]** What else can what I want to say here?

**[1:12:48 – 1:12:55]** Yeah, so this is how a classical recurrent Network would look like and actually it's available to you.

**[1:12:56 – 1:12:58]** So recurrent networks have been around since

**[1:13:00 – 1:13:10]** Alone no long time ago since the 1980s in the second, half of the 1980s, there were already actual neural networks that look like this.

**[1:13:10 – 1:13:17]** People didn't have enough compute to actually train them. We will just, we will talk in a minute about what's

**[1:13:18 – 1:13:20]** Difficult about training, recurrent Network.

**[1:13:22 – 1:13:23]** but in general,

**[1:13:25 – 1:13:28]** This was how.

**[1:13:30 – 1:13:35]** Like this is a very old idea that has been with us for a very, very long time.

**[1:13:36 – 1:13:44]** oh yeah, and one more thing before I proceed to actually discussing the training and there is also

**[1:13:45 – 1:13:52]** One General remark about the current networks here that goes through all possible, architectures.

**[1:13:54 – 1:13:56]** The general remark is this.

**[1:13:57 – 1:13:57]** Notice.

**[1:13:59 – 1:13:59]** How?

**[1:14:01 – 1:14:11]** Notice how the recurrent Network as I explained it to you. Just now know, just how it goes through the input and Only One Direction left to right.

**[1:14:12 – 1:14:16]** It creates one then three six two and so on and so on.

**[1:14:17 – 1:14:18]** And if your

**[1:14:19 – 1:14:36]** Goal is to read the whole sentence, the whole input, and then say classify it based on the last hidden State and probably, it's okay. So of course, you could read it left to right or right or left but still, you need to read it and then make a decision.

**[1:14:37 – 1:14:45]** But if your actual problem is something like sequence labeling. So if you are supposed to have a white over here,

**[1:14:47 – 1:14:50]** Then it sounds suddenly stops making sense.

**[1:14:51 – 1:15:06]** Right. So what if so, like, I am supposed to do, I don't know. I'm supposed to do part of speech, tagging cover here. So this is a word and I'm supposed to say that whether it's a noun or a verb, or an adjective or whatever

**[1:15:08 – 1:15:12]** but if I do it with a recurrent Network,

**[1:15:13 – 1:15:13]** Like this.

**[1:15:14 – 1:15:18]** It would mean that. I am only allowed to look at the words before this one.

**[1:15:19 – 1:15:30]** And I'm not allowed to read the sentence to the end. Before I have to make my decision before I have to, to assign the parts of speech doesn't make any sense. Why should I wasn't information with it?

**[1:15:31 – 1:15:33]** so, depending on the problem,

**[1:15:34 – 1:15:40]** but in many cases, it's very natural to have water cold be directional.

**[1:15:41 – 1:15:43]** BT directional.

**[1:15:44 – 1:15:44]** I don't.

**[1:15:46 – 1:15:54]** Let me draw a picture. It's pretty simple, but just a little bit Messier x, 1, x, 2, x t.

**[1:15:55 – 1:16:02]** X, t, plus 1, x capital T, and I still have a recurrent Network that goes like this.

**[1:16:09 – 1:16:12]** And it's still reads.

**[1:16:14 – 1:16:16]** The input sequence left, right?

**[1:16:17 – 1:16:18]** but also,

**[1:16:19 – 1:16:22]** There is another recurrent Network.

**[1:16:23 – 1:16:28]** Starting from here that will read the same network right to lift.

**[1:16:30 – 1:16:36]** So it the same input, right left. So it will start from x t and then go?

**[1:16:37 – 1:16:37]** Go over here.

**[1:16:39 – 1:16:49]** Let's say this is okay, so let's see. This is H Prime T. So this is H Prime. T minus 1 and this becomes H Prime small team.

**[1:16:51 – 1:16:52]** And goes here.

**[1:16:56 – 1:16:57]** Like this.

**[1:16:58 – 1:17:06]** Right. And on every step, it's just a current Network that creates the exact same thing, but in the opposite direction. So it goes

**[1:17:07 – 1:17:08]** All right, the left.

**[1:17:09 – 1:17:14]** And and that is enough. Now when we are seating at XT,

**[1:17:15 – 1:17:22]** We have the red part, the left to right part capturing the context from the left. Capturing these guys.

**[1:17:24 – 1:17:30]** And the blue part capturing context from the right from these guys. So now we can just have

**[1:17:31 – 1:17:33]** some kind of merchants of the results.

**[1:17:34 – 1:17:50]** Some kind of classification, head over here and output YT. And it will actually be able to account for both left contacts and right contacts for what we had before and what's coming in the sole called here.

**[1:17:51 – 1:17:55]** So basically there is no reason to

**[1:17:57 – 1:18:00]** to not use a bidirectional return Network, unless

**[1:18:01 – 1:18:24]** The problem is like the problem prohibits you from doing that. For example, if you do language modeling will talk about language models a lot later. But if you, the language modeling here, are supposed to predict the next word in text. And when you are writing text, and when you are predicting the next word, of course, you don't know the word that will be after that, right? It's your job to write them.

**[1:18:25 – 1:18:36]** So here in this case if you have a recurrent language model it doesn't make sense to be to be directional right? You want to predict only from from the left context

**[1:18:37 – 1:19:15]** or actually if you do object tracking. For example that I mentioned here in object tracking too, when you are applying it in the real world, you have a stream video stream that comes at you. And maybe you can look a couple of frames ahead. Like, maybe you can delay your output for a few friends, but you definitely will not have access to like the next 10 seconds, right? So you will need to to keep tracking online in real time and you definitely want to

**[1:19:18 – 1:19:30]** You definitely want to have one side networks, but very often in many, many problems. You are allowed to look at the whole input before making a decision. For example, in all sorts of

**[1:19:31 – 1:19:38]** Where was, I sequence to sequence problems? Of course, you are allowed to read the whole paragraph before translating it, of course.

**[1:19:39 – 1:19:59]** So, okay, so these are like standards are RNs standard, recurrent methods, be directional, recurrent networks. And now, let's discuss the problems with the current networks. I guess we will discuss the problems today. And then solutions to the most important problem. I will not have time for that a bit more little come tomorrow.

**[1:20:01 – 1:20:08]** So what is the like, how does a current neural network trained? That's actually a pretty interesting.

**[1:20:12 – 1:20:16]** Thought and it I think it's pretty instructive to actually understand how it works.

**[1:20:17 – 1:20:25]** So you have the same simple right? Just for Simplicity. Let's have a one directional unit directional Network just left. Right?

**[1:20:27 – 1:20:30]** It plus one like this.

**[1:20:34 – 1:20:36]** And we go to extreme.

**[1:20:37 – 1:20:38]** And let's assume.

**[1:20:39 – 1:20:39]** That.

**[1:20:41 – 1:20:45]** The output. We only need the output at the end, so I read the whole sequence.

**[1:20:46 – 1:20:52]** And then we let's say classified. So we have some kind of head over here.

**[1:20:53 – 1:20:56]** And after this head, we have the loss function.

**[1:20:59 – 1:21:12]** And the loss function. Okay, so to do this here, to this last function also goes like the correct answer. This here gives us our predicted answer and then we compare it. We get a loss function, whatever.

**[1:21:13 – 1:21:14]** As usual.

**[1:21:15 – 1:21:18]** So how do the gradients flow like where are the weights here?

**[1:21:19 – 1:21:20]** Here is the thing.

**[1:21:21 – 1:21:28]** Whatever is the recurrent cell inside, maybe, but let's assume that looks like this doesn't really matter for us.

**[1:21:29 – 1:21:30]** but,

**[1:21:31 – 1:21:33]** Importantly.

**[1:21:33 – 1:21:34]** Importantly.

**[1:21:35 – 1:21:37]** Every recurrence cell here.

**[1:21:38 – 1:21:42]** Works and exactly the same way. It has the exact same weights.

**[1:21:43 – 1:21:51]** Right. So actually like if you look at the computational graph behind what Android you have this Waits,

**[1:21:52 – 1:22:02]** Of herself and this weights are copied are shared not Cooper share across all of the recurrent cells over here.

**[1:22:03 – 1:22:11]** Right? So it's the same Matrix W, the same weight answers that participates in every so.

**[1:22:14 – 1:22:24]** Here, we can't have it any other way, really? Because we would never be able to train, like, separate matrices for going from step. One to step two. And from step two to step, three, and so on.

**[1:22:25 – 1:22:37]** Moreover, it's a pretty good thing in the sense that when you do it like this, you can actually process arbitrary sequences of arbitrary length. You don't care about the length anymore.

**[1:22:39 – 1:22:44]** You can just run this for however long, you want to still the same w?

**[1:22:45 – 1:22:47]** But it also leads to interesting problems.

**[1:22:48 – 1:22:50]** So here is the last function.

**[1:22:51 – 1:22:56]** And you start Computing, the gradients of the loss function from here.

**[1:22:57 – 1:23:09]** And as the flow through the nip, through the sequence, they flow back right? And the actual like participation of this weight Matrix.

**[1:23:10 – 1:23:11]** Is.

**[1:23:13 – 1:23:23]** Is that every way from here. So, let me write, just, like, partial derivative, like the L over some specific W from here.

**[1:23:24 – 1:23:26]** It's this big sum, because the w.

**[1:23:28 – 1:23:32]** Influences the loss along the way on every single step.

**[1:23:33 – 1:23:38]** So it's like DL over d w.

**[1:23:39 – 1:24:11]** T whatever that means. So like the the part that goes over here and then it's also the L over D W, T minus 1 and so on the yellow over DW one so to speak. So they are not different ways, they're like different participation like different ages and the computational graph that go out of the grow out of that belief. So the actual influence of the same weight is

**[1:24:14 – 1:24:21]** is done is even many many times along the sequence for every element in the sequence you again, have this inference of them

**[1:24:23 – 1:24:33]** So on one hand, this is good. This is just like this is the same good effect that we had in relational Networks.

**[1:24:34 – 1:24:38]** because in convolutional networks, we have

**[1:24:39 – 1:24:58]** How to say this, informational networks, we had this effect that the same weight participates in this parallel processing across the whole image with me, which means that you can have sparse activations. You can have sparse gradients, it's fine, it's okay. It's not a problem because your sparse activations can

**[1:25:01 – 1:25:04]** Your sparse activation can be accumulate anyway.

**[1:25:05 – 1:25:09]** So here there is little bit of that. So every way is very, very important.

**[1:25:11 – 1:25:18]** But on the other hand, there there is a problem with this influence of w, going through the whole sequence.

**[1:25:19 – 1:25:38]** And the problem is this actually I think it's 7 easier to to think of this problem, not during their backward pass like I do here but just simply during the forward, pass through the network from left to right because as you go from left to right. Oh so w participates every time, right.

**[1:25:40 – 1:25:40]** so,

**[1:25:41 – 1:25:42]** let's,

**[1:25:42 – 1:25:55]** Just make things much much, much much more simple. Let's just say that in every recurrence like this, we take the input, say h, and b multiplied by The Matrix level.

**[1:25:56 – 1:26:14]** Here and this becomes H1. And then we again multiplied by W. This becomes H2. And so this is a very simplified picture. Of course you cannot in reality, you cannot have it without activation functions. In reality, there is also X and so on, but for illustration, this will be enough.

**[1:26:15 – 1:26:16]** so, as you go,

**[1:26:17 – 1:26:18]** Through the recurrent Network.

**[1:26:19 – 1:26:34]** Your like H1 is W Times, H 0, your H2 is like w times H1 so it's W squared times, H 0 and your HT is W to the power T times H 0.

**[1:26:35 – 1:26:35]** Right.

**[1:26:39 – 1:26:42]** And this can be a better thing. This can be a problem.

**[1:26:43 – 1:26:50]** What can be the problem here? Well, Matrix is have this property called the spectral radius.

**[1:26:51 – 1:26:52]** Or.

**[1:26:53 – 1:27:02]** You can think of it is just a convenience store, doesn't matter. Actually, what the spectral radius, basically tells you is how

**[1:27:03 – 1:27:10]** What does the Matrix when apply to a veteran multiplied by Vector? What does the Matrix do to this vectors length?

**[1:27:11 – 1:27:16]** Here. So basically like the norm of HT

**[1:27:18 – 1:27:30]** Layered, I guess not Square. No, not Square. Just the length. The norm of HT will be something like the spectral radius of W Times. The norm of HD minus 1.

**[1:27:31 – 1:27:39]** So every time you apply a matrix, you are on average multiplying the length of the vector, by some constant.

**[1:27:41 – 1:27:43]** and this constants accumulate, as you see

**[1:27:44 – 1:27:47]** so when, when you go to HT,

**[1:27:48 – 1:27:50]** The length of HT.

**[1:27:50 – 1:27:55]** Is like a road to the power T times, the length of a zero.

**[1:27:56 – 1:28:01]** so, if you started with a vector of length one, which kind of makes sense,

**[1:28:03 – 1:28:05]** Why didn't become so?

**[1:28:06 – 1:28:07]** I think.

**[1:28:08 – 1:28:10]** so, if you started with a vector of

**[1:28:11 – 1:28:12]** Length one.

**[1:28:15 – 1:28:18]** Then, by the end, you have a vector of this thing.

**[1:28:19 – 1:28:26]** So, if row, if the Spectrum radios is greater than one, then it means that your activation is just explode.

**[1:28:27 – 1:28:55]** Ah so if row is like given 1.1 or 1.05 or something with a long enough sequence, it will obviously go to Infinity exponentially and it will just explode you will have I don't know problems like overflows in the numbers and the numbers stop making any sense. It's like huge, huge, huge activations, which don't really reflect anything.

**[1:28:56 – 1:29:10]** And the same will happen as you go back because as you go back through a matrix like this, when you compute the gradients your multiplying by W. Oh, but by W transpose, but post a difference. So you're all also dependent on this kind of spectral radius.

**[1:29:12 – 1:29:14]** So you can have two kinds of problems.

**[1:29:15 – 1:29:16]** You can have exploding ingredients.

**[1:29:19 – 1:29:20]** Exploding gradients.

**[1:29:22 – 1:29:26]** When role is greater than one and everything goes to Infinity.

**[1:29:27 – 1:29:29]** Or you can have Vanishing gradients.

**[1:29:32 – 1:29:37]** When row is smaller or smaller than one and it all goes to 0.

**[1:29:38 – 1:29:46]** So, this is also a bad thing, right? So now this means that as the gradient travels along this path,

**[1:29:47 – 1:29:48]** It.

**[1:29:48 – 1:29:51]** Exponentially goes to zero.

**[1:29:52 – 1:29:59]** On the first elements of the sequence. So it basically means that you cannot have any long-term memory, the influence of early.

**[1:30:00 – 1:30:05]** Part of parts of the sequence will just vanish completely and we'll go to 0 is very quickly.

**[1:30:07 – 1:30:07]** so,

**[1:30:08 – 1:30:11]** In exploring gradients, just everything breaks.

**[1:30:12 – 1:30:17]** In Vanishing gradients, well, nothing breaks. But your network doesn't work as you as you would like

**[1:30:18 – 1:30:19]** So, how do we solve this problems?

**[1:30:20 – 1:30:27]** How I will relegate Vanishing gradients to tomorrow because this is a long discussion but exploring gradients is very, very simple.

**[1:30:28 – 1:30:42]** All. I mean, as you go along the network, your problem is that your gradients start to grow uncontrollably. And it's your gradient. Vector will be longer and longer and longer.

**[1:30:44 – 1:30:47]** Well, you can notice this right? As you go along the network.

**[1:30:48 – 1:30:49]** Your gradient.

**[1:30:49 – 1:30:56]** It becomes longer and you can see it as you go along the network. So why don't you just clip the gradient?

**[1:30:56 – 1:30:57]** And that's the answer.

**[1:30:58 – 1:31:17]** So the answer actually took the exploding, gradients problem is not to do something smart and interesting to limit row, to make it equal to one or something. No, the answer is just let's clip the gradients.

**[1:31:19 – 1:31:35]** So like, if you have a gradient, which exceeds, you know, one in length, let's just project it back to the unit sphere. Let's just say, okay, so now it's too long. We projected back. That's it. Next. After the next step, it will be too long. Again, we will project it again.

**[1:31:36 – 1:31:38]** That's the only the only thing with them.

**[1:31:40 – 1:31:44]** So let me go through this fight, there's probably some more stations here.

**[1:31:45 – 1:32:14]** Okay, the current networks. This is what we discussed, blah blah. There are two problems, exploding gradients and radiation gradients. And in exploding gradients, we just clip it. So I think this is still from careers but it doesn't matter. Of course. Every and of course by gradients for yeah this is the illustration. I was looking for the there was a very nice paper, 10 years ago, in 2013 By pescano

**[1:32:15 – 1:32:26]** He who studied the behavior of recurring networks. There are several very interesting points in their recommend. You read the paper actually but

**[1:32:26 – 1:32:27]** and,

**[1:32:27 – 1:33:05]** It's like it's not about any new architecture, sorry about like making it work better. It's about what's going on in the space of activations, in the space of Weights. What's going on, is the train and so on, and as for exploding gradients, the picture looks like this. So what does it mean to have an exploding gradient to have this gradient? Go to Infinity. Well, if you look at the loss function, it basically means that you have some normal part where the gradient does not explode and then boom, at some point, this there is just this vertical wall.

**[1:33:06 – 1:33:18]** This wall that goes to really use very, very quickly, it grows very quickly, it's basically Works called the the gradients explode.

**[1:33:18 – 1:33:21]** So, what happens is you go over here?

**[1:33:22 – 1:33:25]** And then you bounce off this wall.

**[1:33:26 – 1:33:30]** And if you don't clip the gradients, well you fly away gotten elsewhere.

**[1:33:31 – 1:33:43]** But if you do clip the gradients, well, you go back to this normal regime and you keep trying alone and you keep going in the general direction that you want so clipping, the gradients is not.

**[1:33:44 – 1:33:57]** A problem from the like theoretical and practical point of view. It's, it's not a bad transformation to make, it's okay. We are still, we will still continue to go in the approximately the same direction.

**[1:34:00 – 1:34:00]** and,

**[1:34:02 – 1:34:03]** Probably let me stop here.

**[1:34:04 – 1:34:04]** So,

**[1:34:06 – 1:34:08]** We've discussed recurrent neural networks.

**[1:34:09 – 1:34:10]** We've discussed.

**[1:34:11 – 1:34:12]** What we?

**[1:34:13 – 1:34:47]** How we process sequences with this kinds of architectures and we have discussed the main problem. The main problem is that as gradients flow in this, activation flow and forward propagation. They either blow up or vanish and it's difficult to pin the spectral radius. Exactly to one. So something needs to be done and the exploding part turns out to be easy but the initial part is real estate tomorrow will turn out to be pretty and interesting.

**[1:34:49 – 1:34:54]** Okay. So at this point, I want to stop any questions about what we discussed today.

**[1:34:57 – 1:35:06]** While you're thinking about the questions tomorrow is lecture day. So please join on time.

**[1:35:07 – 1:35:08]** and then,

**[1:35:09 – 1:35:15]** you will go back to Alex for practical sessions on Thursday and

**[1:35:18 – 1:35:37]** Yeah, I think they should be available today. So, yeah, just what I wanted to say on Friday on Friday. There will be a midterm presentation. We, I sent Alex list of papers yesterday evening. I think he wanted to add something from himself. I hope it will be made available today.

**[1:35:38 – 1:35:38]** Okay.

**[1:35:39 – 1:35:43]** So on Friday, on Friday, we will be listening to you.

**[1:35:44 – 1:35:48]** okay, thanks a lot and here, tomorrow tomorrow to lectures

**[1:35:50 – 1:35:50]** Be.

**[1:35:51 – 1:35:51]** Fresh and ready.

**[1:35:52 – 1:35:53]** In the morning. Bye.

## Full text

Okay. Good day or good morning still everyone. And Welcome back to the lecture part of our class. which, is being done online this year, and last time we ended on conventional architectures and specifically on how CNN's work and what is their like What is their main? good thing that they do, what is the main advantage of using conversations and this main advantage was of course, to Reuse the same weights. Over the entire input and over all of the intermediate feature tensors that you see in in inside the neural network that are the outputs of intermediate players. So all of this can be actually all of this can can be processed in parallel and you can reduce the number of Weights by huge factors, right? So, Before we proceed with conversion architectures today. I understand that you already kind of started talking about convolutional architectures with Alex, and that is absolutely great because now we can skip part of this lecture and faster. Get to recurrent networks. I'm not sure if we get there today, but hopefully, yes, but before, Before we begin with the lecture. Let me. oh, before we begin with the lecture, let me show you a couple of things. I have this. Standard illustrations for CNN's that. I think you don't really know because you've already had practical sessions about and, but maybe I will, at least mention a couple of buzzwords that you can look up. so, I want I want to discuss all of these pictures in detail but basically like in classical computer vision. In the days before neural networks actually worked, what you would do, what you would actually do in computer vision, will still be using configurations, but you would be using like handmade conversations. They would be called filters and sometimes people call learnable conversations filters as well. And there were like filter banks for all kinds of purposes and if you look at classical utilities for say image processing, right? Sharpen blur at contrast emboss, and whatever. It's all done with this kind of filters. It's all done with filters that. Are apply that are basically this small matrices. Just like conversations that are applied in parallel over the image, right? And you pretty complicated stuff with this, you can do, for example, H detection, like, find out where the edges of objects on the image are. And here, for example, the the cat itself is pretty messy in terms of the ages, so you can see it here. Um there were classical filter brands like Gabor filters where you would do something like Edge detection and to be perfectly precise. You would do like discrete derivatives finite differences in different directions and you would like directed Edge detection. So like, where is I? Did this kind of filter fires up if there is a big difference, vertically, when you go vertical from one pixel to another and this one, if you go horizontally, from one pixel to another and a lot changes. So you can actually This way. Okay, have illustrations for pooling. It's not very interesting, but if you applying as a filter to an actual image, of course, Max pooling would look very strange because it would just clamp everything to the max brightness. So, to speak, and the average pooling would look better. But that's that's not its purpose, really? And finally I also have illustrations on real networks. So you already know what restaurants are and this are Filters. These are the convolutional the matrices of convolutions, on the first layer of resnet 18. and you can actually see what they are trying to recognize some fire up or some kind of lines like And diagonal lines, vertical lines. Some fire for colors or color gradients, or something like that. and, if you actually, Input an image and see what exactly this filter is fire on, like, where do they activate a lot? Then you will see that. For example, this guy is looking for something like grass, I suppose it's just looking for the color green. And here is this and, I don't know, it's interesting here. This this guy on the right is looking for horizontal ages and it or vertical it just probably, and it activates like the Gabriel filter on there. There is a horizontal line. And if then we go through the network, and we map, what if what filters what? What active filters on different layers of the network to. And again, we go through the rest of 18 and look at what happening inside Again, you will see that again here. The math becomes a little bit more complicated with me. Let me not go into that because for layer 1, you can just basically see Like the inputs are the pixels. Here is the filter where that's activated here then on subsequent layers as you understand now? There is not such a direct correspondence between pixels and outputs. Right? Because yeah, every picks, every feature has a reception field, you can find, which part of the image is looking at. But What exact pixel server? Contributing the most that requires a little bit of math. So I will skip that but you can actually look at what parts of the image. Even top layer features fire up for and you can see that for example in resonate 18, the second player Fires for some, I don't know how high frequency stuff in the In the image, I throw out the whole image but just some kind of, you know, stripes or something and edges and stuff like that and then we go for more Salient objects, right? So here, for example, there is some filter that fires for the eyes and the tips of the ears, something like that. And then when we go to later layers, we become like more and more semantics. So, in this picture, I don't think it's that clear their waiter blurry and Trust not, 18 is not a very good network, but still you can see that kind of there is a filter for the ears. There is a filter for for the head as a whole and so Or. You can actually go back from a deep feature, back to the pixel level, right? So this, yes, sir, I didn't explain it well, but this was on the level of the feature maps on the level of the feature maps. I mean it becomes blurry and blurred. There are. There is less Germany, just makes us cents. But you can also with this math, that I mentioned map, it back like the original image to the filters of the original image. And you can see approximately. Now, it's not precise but you can see approximately what the fires on, and it's pretty interesting, right? So, interesting at 18, on a deep layer, you can find the feature that, like selects most for the cats. So what that means to be Kettle left, if it means that Resonate was trained to distinguish classes from the image. Net, like it. And dogs, and you can actually find which feature gives you the most information regarding this specific class, which feature correlates like, who's activation correlates the best with this specific class. And if you look at the cat selector feature and you input an image, which is have like this one and just merge two together, that's it, then you will see that at first on the cat and the dog selector feature in deep fires up on the dock approximately. So this kind of works and also I want to mention again. I don't I don't want to spend time discussing the math but there is there are also methods for more the detailed interpretation of more detailed interpretation of what the network actually is doing. So there is, for example. Great chem. It's not the only one, but it's a good one. And if you can run it for for the network output, like the predicted class, a single class. Right? Again, we call it the networks output is this set of probabilities so every class in a classification network is a separate output which is convenient in cases like this because we can actually We can actually look at specific outputs and for example, the Egyptian cat output response to these and it has been has obtained the value that has due to the pixels like this. So it's not yet an attention mechanism will get to those tomorrow, but it's kind of an interpretation of what exactly why exactly. Due to which pixels the network shows this value for this. And sure enough, you can, you can run it for different classes, for example. Again, if you can't get the dog and the Egyptian cat output will look at the cat and they went heimes panel output, will look at the look that's Okay, so that was a brief remark about what we will not discuss in more detail, so about the basics of convolutional networks what they're looking. Now let's get to the main part, I think of today and the main part is important convolutional architectures. And hopefully this will be only the first main part because some of the most important stuff you have already discussed through that, right? so, The most important convolutional architecture and history. Was of course alexnet. And I hope that Alex discussed she's architecture with you and if not I guess by now we can skip it. So it was like the first convolutional Network that actually worked. They beat every competing method completely on the image. Net recognition, large-scale English or conditional competition, and that defines the state of the art in an extraordinary in extraordinary. A big margin. So in 2011, or 2012, when it was participating in this competition, the results were, like, like the error rate for all of the rest of the methods was like 22% 23 percent. Something like this. And the error rate for Alex was like 13%. So it was a huge jump, a huge gap. And of course, next year, the whole leaderboard was only conversational networks. Nobody ever went back to classical computer Asian since alexnet. This was this was the revolution that happened in image process. And technically and in terms of like specific ideas, what is most interesting in ALEKS and our two things. So it's pretty standard, polish, Mark architecture, but you can see first that it's split into, and that was the first actual, like industrial scale instance of Model, paralyzation. So this is very important. We won't have time to go into more details so now it's a good time to just mention it. In deep learning, you have huge models, you have huge data sets. So of course you need to paralyze. You need to make use of multiple say gpus if you have multiple gpus and there are two main ways that you can do it. You can do what is called Data, politicization. Data parallelization is when you I don't know when you have one, miniature GPU one. Another meaning patient GPU and other minimization GPS 3, you run the model and then you collect the results and you do a single update based on the weight updates from all of the GPS. So you don't have to change anything in your implementation are the network works. Just as usual. The only difference is that since now you have multiple GPS and parallel, you can collect, you can basically your chest increase in the mini batch size for yourself, right? So what you are actually doing. Yes, you are. You are expanding the. Your expanding the the size of very post your expanding your minimum wage size by splitting the Mini version of different gpus that that's data prioritization. There's a lot of work on that because you can do it in many different smart and interesting ways. But like the basic idea is very simple. Model prioritization is more complicated in model personalization. The assumption is that your model does not fit on your GPU, right? And if your model does not fit on your GPU, what can you do? Well, you need to put like half of your model online, you and another half on the other and that's exactly what Alex was doing back in 2001 already. so, 2212 is the paper, but the actual Network wasn't until and, Of course, that was like a huge hit of engineering back in here. 11 was a wonderful programmer. And she actually implemented all of this by hand. These days. Of course, we don't need to implement anything by hand and even our Cloud codes do not need to implement this. By hand, in Partnership, you can just say Well, I want this weight Matrix to leave on this GPU and that way it Matrix to leave and they GPU and by touch will just handle the rest of them. But still when you design a parallel Network like this network, that spans multiple gpus you want to minimize communication across the gpus because of course it will be slower than inside one appear. so here, for example, you can see that these guys talk to the two strands, the 2gbps talk to each other over here and then talk to each other at the very end. There are only two places where they actually exchanged information. anyway, I'll explain, it was the Breakthrough. People like to talk of like the Alex Smith moment or something. and, but then, of course, The field exploded. Everybody wanted to do convolutional networks, and it turned out that you can actually improved conversational networks. Quite a lot with relatively simple ideas. so, some of the most important ideas you already discussed, with Alex, not krishevsky but Alex the Widow and Like the first idea is vgm. And vtg is the reason why alexnet still had like 11 by 11 convolution on the first layer. But now you will never see 11 by 11 conversions. You will only see three by three, convolutions and maybe five five sometimes because We? Idea. You can represent a large convolution, as compositions of small conversations, and this is actually a great way to do things because it's like a convolution inside a conversation, right? And this convolution inside it in relation, reduces the number of ways Earth. I think you need this with calculations of how many ways and it's kind of additional structural organization. Again, you're saying to the network, you can process different parts of the input in the same way and usually just works better. so the second idea, That you also discussed through that, it's as far as he told me is Inception. And Googling it and generally like the idea that is known as Network and network. So I started talking about convolutional networks with you with this. I want page back to them, but you remember the slide with this boy, on a toy horse and all of this and like there. there were tiles being processed by what I call small neural networks on this what was called small neural network on this picture, And since then, when we actually implemented this morning on networks, they were always like the simplest possible in your own networks. They were always talking only about a single Matrix that processes, the whole input. And doesn't care and doesn't do anything. Interesting. Just And put everything together, throw it to a single Vector of numbers multiplied by this weight Matrix here is the output. But you don't have to limit yourself to that, right? You don't have to, you don't have to do that, right? You can do more interesting things and this Inception trick and basically this idea of network and network are exactly this. You can you can replace this simple convolution with a far more complicated approach, far more complicated Network, and when you do that, You still have. if they have the same idea of processing the tiles in parallel, with the same small Network, it's only that the small network is now more interesting. So yeah, I think you discussed Inception, I want to repeat that. What I want to know here, is that when you look at like this Inception units, when you look at this, small Network, so to speak, you see usually multiple parallel threads of processing. And that is not a coincidence and we will talk more about that today. Okay, so Third. The most important idea of all of this, the idea that will be with us throughout the whole deep learning, it will be used in Transformers, it's used everywhere. The idea of physio connections and thus redness again, Alex said that you already discussed it, so I will mostly skip Basically, the idea is like this. I apologize. Keep forgetting to the redo the Russian picture, but anyways, this is, this is input. So the input is X and f of x. And the next layer is like this. F of x. And the rest have problem is that when f of x trains and saturates, the gradients will go to 0. They this layer will not want to change anymore, and when it doesn't want to change anymore, that's okay for the layer. But if you didn't have a residual connection, it would mean that nothing below that player will ever learned right? Because everything below the layer receives gradients through the Slayer multiplied by Derivatives and they both go to zero, then nothing changes below that. That's that's a bad thing. So what we do is we use residual connections like here, we do a connection that goes around here, we have something very simple and specifically just the plus and now our result is f of x plus XK and now f of x can saturate all at once the derivative can go to 0 that's fine if it goes to 0 then the great interest goes to the Matrix of derivatives just goes to an identity Matrix and the gradient will just flow through the Slayer and now through but throws flow around the Slayer and continue to the bottom layers. and, as soon as resonates or introduced, I mean here this guy who invented wrestlers and he is actually very cool researcher with a lot of great papers. I mean here called it the revolution of that and did it was so when residual connections were introduced and were used and deep convolutional architectures You immediately could train networks with hundreds and hundreds of layers. So like Alex, Ned had eight trainable layers. We don't count pulling here VGA had 19 layers googlenet had within the first Inception units, had 22 layers and resnet. Next year had like 150 layers and there was Total in no problem to. there was no problem to to grow further. There was no problem to increase the depth for further you can do resonate 200 300 500 to 1000 and it will still train. It will still be fine. The problem only is that It will stop improving, right? So it will still be trained and we'll still do the job, but if you increase your net, for another factor of two and the results don't improve well, maybe you shouldn't be doing that, right? So it only makes sense to it new layers while they still help. So actual resnet go up to about 200 layers and then I guess they run out of stem. Okay. So as far as I understood that, it's if I understood him correctly, this is approximately where you stopped. And let me complete this Arc. Let me continue this discussion of different conventional ideas of ideas that kind of Define conventional architectures with our next with our first Details point point one, which is the bottleneck layers. Bottle next and an idea that is usually called split Transformer. Sorry, I'm not yet. Used to write. Okay. Split Transformers. so, What the bottleneck idea? well actually, you can look at for example, the VGA idea, As. Another way to reduce the number of ways, right? Because you replace big conversation which has N squared weights with a sequence of small conversations, we have linear Enon weights and that's great. so, So, convolution by the cells already. Start off by saving a huge number of weights. You can actually try to do better. You can actually try to reduce even further. and let's just Step back. Look at a conversational layer and see where and what we can improve. So a standard conversational layer will have some 3D tensor as the input, so the input will be of size. okay, so let's let's actually say that this is already the window that I cut out because I never want to care about the and everyone to care about the full input. It's always just copy it over. So this is already the cars out window and it has like depth deep with w and height h. Right. Then we go to the convolutional layer. and as a result of the convolutional layer, we get a single Vector of features of size T Prime. So a standard convolutional layer will will be will have the Matrix of Weights of Dimensions, D times, W Times H times the prep Right. And as we discussed is much, much much, much better than if we try to do it with the fully connected layer or something else. But still, it can actually Add up, it can grow pretty quickly. So, If for example, I D is something like 2506 which is pretty standard Insight big Coalition architecture. And deprime is also something like the 56, to 56. Then even I mean, the beach chair idea. Let's you keep double and a small. But still in here, you have like this tensor of weights to 56 by 3, by 3, by 2506. And that's a pretty big number, right? So that's like, Oh, I don't know. 2500 times another 25. Okay. I embedded method this level but you can figure it out. What's 25 squared? It's not 725, right. So, it's 75k. I guess, no. No, it's 750k. So I'm 700 k something like this. Right. Wait. Yeah the 50 by 250 is 75k and times 9. Yes, or something like that. Something like that sound 100k. Which is quite a lot, right? So, how can we reduce this? Where, like, where is the, what is the problem that we might somehow solve here? Like, where where can we save on these weights? The bottleneck idea is actually it's a straightforward. And it goes like this. What if? instead of getting the full 256 by 256, multiplied, by 9 what if we actually compressed the features down and only when did the convolution So, here is how it would work, you have your input. And your input is low. It's like e times double W Times h. And But first you would run it through a one by one conversation. I hope you discuss those with Alex, one by one conversion. Just by definition, that's not do anything geometric. It just takes one. feature Vector here and rearranges it, right? That's something interesting. Inside the feature Vector, but it doesn't, it doesn't do anything to the geometry to the receptive fields to anything like that. And what if we used this one by one? Convolution to actually reduce the depth to reduce the number of channels that now I would have something like deer. And double Prime Times, W Times H with e double Prime small. So if I had D like 256, maybe the double Prime is like 32. And then I would have my broken Revolution here. And it would give me. A short Vector so formerly. I would put like the triple prime here. But okay, let's just say it's the double Prime 2. And then I would have another one by one conversation. If I do want to have like, d Prime at the output, then I would have to stretch back this feature Vector to size the prime So, the convolution itself. So, the okay, the the one by one valuation. Now has like the times one times one. Times d. Double Prime weights. This is one by one. Convolution, this can valuation has how many weights? D double Prime Times W Times H times, d, double Prime. and also this conversion is the double Prime times one times, one times, the prime So you can kind of get a feeling for What's Happening Here, Right? I avoid multiplying 256 squared by 9. And actually I avoid to 56 squared completely. Right. There's still a nine in there. It still gets multiplied by something but that's something as much smaller than 2506. So let's plug in the numbers in this. In this example, it would be like 2:56 times 32 plus these 2. 56 times 9 times. Oh sorry, sorry sorry plus Plus 32 times, 9 times, 32, right plus again, 32 times to 56. So even though I have Reconciles instead of one now, I still save a lot of ways. So let me pull to 56 out of 32. Plus what? Now, I have to take a four out of this. So no I have to take an 8 out of this so for his left hand by four. And another 302. So it's 32 and 30 to 64 and 36, exactly. 100, that will be like, 2:56 times 100, right? And over there, I had to 56 times 2500, right? I'm still 56 times 9. so, this is about In our simple example, that's about like 25, its smaller. 25x smaller, and We have saved a lot of weights. Okay, a lot of ways. well, but now, when you look at this idea, Something. Should feel funny to you about it. Something should not sit right with you about this idea. And what is that? What is the problem here? Oh, What did I just do? I took effect of 2506 of a long character of the 56 features, so in the input every pixel, every feature map every teacher Rector was long and had a lot of information was like, 250 numbers. And then you just compressed it down to 32 numbers. Then I did interesting stuff on 32 numbers. And then somehow I decompressed that to 56 but then the compression cannot restore the information that I lost, right? So what I'm doing here is I'm taking a long and interesting Rector So, geometrically speaking, I'm leaving, I'm in the future space of a high dimension like 256. But inside this feature space, I am picking a specific Subspace specific projection. Of this much smaller damage. Right. so, I am reducing My features that are long and interesting, and the complicated down to a much simpler thing to a much smaller Dimension. I'm like, just taking one of you of this thing's and, That's doesn't sound that bad. But if you think about it, it doesn't make any sense to actually do what I'm proposing here. Because if I just compressed down to 56 for numbers worth of information to 32. Why on Earth do I need to 56 numbers at all? I mean, this is happening inside a network that I am designing myself. It's not these. 256 numbers. Did not grow on a tree. They came from an earlier layer. So if all I wanted to do was this Then. I would just replace d by the double Prime. I would just say, okay, so let the previous layer produce 32 features. Why do I need the artificial compression? Decompression stuff. and that would, That would save a little bit more weights. And that would be even better. Right. So, the way I told you this bottle neck, I idea it doesn't work by itself and he did it doesn't. And never appears like that, but it's suddenly starts to make a lot of sense. if you do it, not once but several times, so, how would actually gets used is You start. With this long, the simple answer did times. W Times h. And then you do like several copies of this of this processing. Pipelines. So like you have one by one then convolution you have One by one then convolution. And so on. and then, You somehow unite the results, you combine the results. So for example, in this case, it could be like this. I have D to 56 and out here. I have a vector of size 32, right? So How many vectors of 302? I need to have a new Vector of size to 56. Oh, eight of them, right? So why don't they just copy this eight times and concatenate the results like this, this is a pretty standard way, and this So, I do my processing eight separate times. notice that even though it's Ah, even though it's the same picture, it's the same structure of processing. The actual processing will be very different, right? Because this strands, this Pathways will learn different ways. They will do different things. You need to break the Symmetry and initialization, and then they will just hyper to go to different minimize to do different, to implement different ideas, And yes, now I'm not saying 25x rates. Because now to actually go from 256 to 56, I need to copy this for eight times, right? So now, instead of saving instead of saving 25x, I'm only saying Forex rates but it's still a pretty big sale, right? And actually it turns out that in practice, it's a pretty good idea. so what we are actually doing is in this huge space, we are choosing not one. Projection, not one way to reduce the dimension, but we are choosing multiple different ways. Multiple different viewpoints on on this complicated features. And so I look at it from this side and then I look at it from this side and then I look at it from that side and it's like different projections, different snapshots of this. Same. Big space of features. And when you actually do that, it's it's very interesting and it's Now it's not just it. Usually you can train it to not lose any important information but even better you can actually like, say this, you can actually Fit to do even better than if you just process this whole to 56 thing. So it's it's actually and I cannot get into food detail to explain why. But it's actually a good idea to do like Awards. If even do lots of random projections of your high dimensional object even that is usually a good idea. And here, the projections are not random right here, the projections are learned and they are learned to be useful, which is even better. So This is usually called. Split Transformer. Or obvious reasons. First is split, then you transform, then you merge and it's a pretty standard idea in convolutional architectures. So I guess that's the important thing that I wanted to say. Let's go back to the slide. Yes. But here is an example in the next kind of outdated. Now then it was 10 years ago but a perfect example of just and yeah like this just pleated to 56 into 32 path of four so it's like an extreme projection. But several extreme projections and that's better. So what else can I say about this classical convolutional architectures? Well, I probably should mention this line of inception networks and Inception, resnet networks. I'm not sure if you discuss them with Alex, you discussed Inception, you discussed resnet. But what about the combination and basically, the progression of this networks there? A pretty important family of networks. They were like, for a long time, the best available backbones for all sorts of computer vision tasks. When we get the object detection, we will discuss the object detection, segmentation we will be discussed how for example. How we will just discuss how when you do an object detection architecture or segmentation architecture. You can't really expect train it from scratch. So there will be not enough label data to train from scratch because labeling was very difficult for this complicated computer vision tasks. So what you actually do in practice is you take what is called the backbone? You take a network trained on image net. For example, to justify stuff, then you cut off its head and you use the rest of the network as a feature. Extractors, maybe you find units or maybe not. R and this Inception resnet, family was one of the most influential one of the best families of this backbones back in 2016. And What is its main idea? Of course doesn't make sense to learn them and big detail but its main idea was that you do this Inception trick you, you do this network and network thing, you replace a, you do better and better, basic blocks, that process, the inputs like the small neural networks, and from version to version, they Just invented better and better such basic blocks. Basically that that was the main component of progress. And another component. Interesting component of progress was that they all saw replaced pooling clears with blocks like this. and I think women, I mentioned this last time, like, if you want to reduce your dimension, if you want to reduce from, Ah sorry. If you want to reduce from 256 by 256 image down to 128 by 128 image. Yeah, you can do exponent but it's even better to have another Network and network thing. Another layer that can be trained and that can do it more interesting stuff, only that you tune this. You you compose this for air and such a way that the output becomes smaller how you do that. Usually, let's try it. Let's try that convention. That just reuse them in Geometry, that's what they do. So over here, the indeed in late later, Inception Network, stay indeed have this reduction blocks that can have pulling inside but it's again, this kind of Transformer split and merge idea. So there are several. Several several lines of Processing here that do different things and then they are merged together. And so in some way, so this has been influential idea in college. And then you have residual connections and we get Inception right now. That's it, won't go into more details, but basically, like conception resonate. V2 was a very influential, very interesting. Backbone. That was used very widely. Okay, so I will probably keep the rest mostly there were Some more ideas on how to further reduce the size of the network and also, to reduce the number of layers, and let me not go into this idea in detail, but this basic trade of not Trader. But this way there are basically two different things that you want to optimize one is memory. You want to have a smaller network if you want to, for example, fit to a mobile device or something. And that means, we use the number of ways because basically the size of the network is the number of ways. That's it. And then there is also another dimension which is latency, which is how quickly the network will actually operate. So in computer vision you often care about latency. For example, if you do something like trekking on a surveillance camera, then of course you needed to work in real time because this surveillance camera will work like 24/7. And of course, you can't leg behind the video stream while you're processing a continuous video stream. Right? So you definitely want your tracking or whatever you do with this stream, you definitely want it to work and like 30 frames per second at least. And preferably 60. So latency is also important. And what I wanted to just note here is that there are two different things I mean, to some extent. It's true that if you have a smaller Network, it will run faster. But actually, the latency depends on the number of layers. Because once the network fits into your GPO, the rest is more or less than parallel inside the layer. and, What actually matters is, how many steps you make? So every step. Okay, so depend on say, the intermediate representation size. Yes. Of course, it will. This forward, you have more weights inside every layer but the most important component is the number of players so, these two Things. Make networks faster or make them smaller. They don't conflict that much. But there are two different objectives just wanted to mention that and yeah, let's keep squeezing it. Nothing new for us here. Let's keep mobile net. Here it indeed. Was the whole thing was indeed to put computer original mobile devices. And finally, I think what I want to end this discussion with finally, the like, family of CNN's, that kind of topped. This progress of CNN, architectures. And that, I mean, probably there was something afterwards, but mostly even now everybody just uses this. The line of networks that proved to be the best work efficiently. And again, I don't want to go into too much detail, but it's again, the same story that we saw. We've Activation functions. And then I mentioned that we saw a similar story with gradient descent algorithms, but the gradient Central grid Transportation discuss that and here in efficient meth, the architecture was actually The architecture was actually found automatically with a big neural architecture search. So, Yeah, so what they did and again, not too much detail but just the basic idea what they did was they looked at how you scale a convolutional network. Like when you increase the network in, what ways can you increase and network like what are the different dimensions that you can change? What are they? notes that you can rotate and tweak in order to change put the network test, And it turns out there are quite a few knobs, right? So, you can change the depth of the network, obviously, you can change so you can add more layers. You can change the width of the network you can. More. That you can add so sorry, we usually call it depth, but yeah. Inefficient that is the number of layers which also is very reasonable to call that and with like the, the length of the feature Vector. So you can make the network wider by adding more features that allows you to make the network smarter, but Spain more weights. And also you can do something like higher resolution so you can increase the number of pixels in the input so to speak. And then what they did was, they just rolled down some very simple formulas, like, okay? So as I increase the network, I increase the depth, the wheat, and there is a lotion. How does the total size of the network change? Well, you multiply them all together. You get like, the product of three numbers and it goes into the exponent. And this is the number of ways. Okay. So what are we looking for? We are looking for the perfect balance between these three numbers. so, basically, the idea is If your depth grows exponentially with exponent Alpha your weed, growth exponentially with exponent beta, there's a solution, grows exponentially with exponent game. Then there is like an actual relation between alphabet and Gamma, but then you need to actually find the best ways. so, That's what they get. Then, they run like, huge evolutionary search, to find this best combinations of hyperparameters and they were successful. They were pretty successful, and this family of efficient efficient Network family. As you can see here, basically just Define The state of the art, right? Define a cross the whole field. So we will see plots like this later in for other computer vision tasks here at all. So it's pretty I think instructive to look at how this plot works. It's there are two axis, right? One of the x-axis is the number of parameters. So here the larger the network is, it's bad, right? So you want to to have an efficient Network. So you want to have fewer parameters and The y-axis is imaginative one accuracy. So basically how good the network is, what is the result here? Higher is better. So this means that your best networks will lie in the top left corner. You want to be in the top left corner, I want to have a small Network, that works very well. And, of course, you can't have both at once. There is a trade of here, large networks will work better than smaller. That's okay. so what people are actually looking for is like a Pareto Frontier, In this. Plot is the frontier where for every size you have the best possible Network and for every Target quality, you have the smallest possible Network. so as you can see, the efficient family, Pretty much succeeded with the filing. This Frontier everywhere. and, Ever since then. I think maybe I've missed something. It's not like I follow all of the papers that appear, but I think there hasn't been any Revolution since then, correlational networks. So of course, in a large extent, everybody switched to Transformers so we'll discuss that, of course, but But in conversation networks, I think the question at the still like the best underlying architecture and for some object detection pipelines and implementation pipelines, sufficient. Net is still the backbone. so, so, we got to We go to the state of the basic. Okay. Yeah. So I will skip bitch Norm because I said that you already just discussed it with him. So, let me, I mean, there's there's not much that I wanted to say here except explain how it works. So here is how it works. I think you've discussed this already and I also, yeah, also have this. Yeah, this nice picture of different variations of which Norm, so I'm not sure if you discussed that, but usually, you would have bleach normal where you ever reach over average, the same feature over. The spatial dimensions. So across the image and all so over the mini beach exams. But sometimes you would you would like to do something like layer Norm where you don't have reach over the meaning page. And to be honest, when you use layer Norm, usually, just means that, you're mean which says one. So there is no meaning to every shower, which means that instead, you just average over the whole Ends are features. So now you just have a global statistics for for the whole year. A layer Norms layer Norm is used all the time in Transformers because Transformers are big. And they're usually, you cannot expect to have any significant meaning page. So you need to you need to have normalization inside of a single training sample. And then you can actually do if even even something more interesting here, but let's not go into the test. And it's also a pretty big filled with dozens of papers, lots of results, blah. Okay. Interest that. I think I will. I have. I'm done with Relational Networks. they will note out encounter more of them in practice and practical sessions and I want to go to the next or next, big topic. Oh big in the sense of important and different but not that big. I think we will either finish it today or maybe have a little bit left over tomorrow. So, this big purpose is recurrent neural networks. And until Transformers appeared. They were like, they were like these two main strands of architectures in India, learning their work in evaluation on networks, and there were recurrent Networks. And recurrent networks were actually designed for and used for and with sequences. So what is the main idea? Of an RNN of a current neural network. Well. Quite often. You have. Quite quite quite often you, your input. Has the form of a sequence. So let me actually, yeah, let me go to the board and let's let's discuss this first module 8. Rnns. And Discuss what they actually. So when you have your input picture, when you have a big complicated input sometimes it doesn't have a natural way to to be represented as a sequence, for example, An image. Is not really a sequence. An image is a two-dimensional structure. and, It's not a 1D sequence of anything. So, for images, the natural way to go would be with something like cnns. but there are lots of types of inputs that are actually Like sequences. The probably the default example would be just Time series. Like, for example, Financial time series, or something like this. But there are more interesting examples, too sound. Is a sequence, right? It's a sequence of ticks with amplitude and yeah, in classical machine learning and classical digital found processing. You would they actually not be able to treat sound as just a sequence of amplitudes because in the sequence would be too long to long for classical machine learning to handle. So what you would actually do was, would be to, like, cut it up into packets of 2013 milliseconds or something. Then do feature obstruction on the packets but then still, you would have a sequence of this features. Picture actors. And of course, the main example is text. So text is Definitely a sequence. It's a sequence of tokens. We maybe will discuss a bit tokenization, in the context of Transformers, but Texas sequence of words, or generally speaking tokens or whatever, it definitely has one dimensional structure. All right. and when you have, when you work with sequences, there's a number of different things you can do. There is a number of different types of how you can frame a problem or what kinds of questions you can ask. So the simplest would be if you have a sequence like a text. Sequence of tokens and then you have just a single output. So this is your X and this is your why For example, classification. You have a text and you want to say oh is it, what is it about? What is the topic? And maybe it's like news stream and for every piece of news, you want to say is it sports or in politics or onions, whatever. A maybe. It's the other way around. Maybe it's like a single input. And then you need to enroll it into a sequence in the output. So this would be like sequence, generation problems, right? So just write text about something, for example, here, there would be a problem like captioning. I think we'll have examples of networks for captioning, like the x is an image. And then you take this image so it's not a sequence but you want to convert it into a sequence into text that will explain what you see on this image. Right? So that that's caption. And then of course, the most interesting for us problems would be something like sector 6 sequence to sequence problems where you have an input That is a sequence. And then you need to have an output, which is also a sequence. So this would be a problem, so I commissioned translation or something. when you have text as input and text as output, Or in other domains or even in text to, you could have like sequence labeling problems. Right. Sequence, labeling problems where you your input is a sequence. And your output is a sequence. So, this is X. This will be X. This is why, and your output is also a sequence. but it's a sequence that aligned to the input, so, for example, So like insect to set problems and sickness to sickness problems. You read the sequence. Your the input sequence. You understand what it's about? Like input paragraph. You understand what it is? And then you write out the output on the translation. In sequence labeling in NLP natural language processing. It would be problems like part of speech tagging for example. So you have a sequence of words and You need to assign a label to every one of these words. Why not? Right. Or. For example, you know, adding subtitles to it to a movie like you have this sequence, which is a video, I Want, by the way, I didn't mention videos here but of course, video is also a sequence. Right. It's a sequence of frames and every frame is an image but a sequence of images. Now is a video or you can have something like, putting subtitles subtitles behind the videos. So, for every frame, You would have the specific text that should be shown there, or, for example, object tracking. An object tracking. You have a video and you're supposed to follow an object inside this video, like do for example segmentation, but not on a single image but on a sequence of image, so that it tracks, the same object as it moves. And yeah, I was struggling to recall something from computerization. Here is an example from computer. okay, but whatever you do is there. It kind of like the methods that we have. The approaches that we have like convolutional Networks. They're they're not quite well suited. For dealing with sequences. what, what I mean here is Yes, you can do something like this. So, sorry about the right part. Look at the left part, you can do something like this, you can do a sliding window that goes along your input sequence. And then, It processes this part of the input sequence. And to an extent, it can work. There was a time when like convolutional approaches to natural language processing, more like Rivals to recurrent approaches then, of course, Transformers change everything. But it's it still like, it seems to be Prohibiting, the most important thing. The most important thing is we need to have a way a way to recall, inputs, from long ago. When we need to be able to have this understanding of the whole team sentence and ability to recall what was happening in the, in the sequence. A long time ago, when you read the paragraph of text, you definitely need to remember what the beginning was. Otherwise, the end will not make any sense, so, how can we achieve this with the neural architecture? Recurrent neural networks. Do it like this. So let's say we have an input, X1 X2, x t. Now it's natural to think of this excess like something in time, right? So Escape at all team. And we will do it like this. We will process every X, every input in the sequence separately. With this. Let's say small, neural network. Which would be called the recurrent unit. But this unit, let me draw it set correctly. This unit will have Two inputs and one or two outputs so it will have X as the input and also a hidden State age and other input. And its main job will be to process this new input and update modify, the hidden state. So that now it captures The sequence up and then up to and including X. And the assumption is that H actually captured the previous part of the sequence, the sequence before X, So formally just means that our recurrent unit is a function of two inputs X and H and the outputs H prime. It may be it also outputs like the output. So at some point we do need to have the output, right? Sometimes it makes sense to put it like at the output of every cell. Sometimes it makes sense to just use the last hidden state to do some kind of head and then produce the output. That depends on a specific problem. That's not that important. What is important is that we have this hidden State. This Vector numbers basically that goes along the network and is updated every time as very another accessory and other input. And we go go and hope for him. This x is modified in such a way that it actually like combines all of the relevant information from from the sequence so that we can just look at this X. And we can just say, all right, that is what the sequences about. Okay. So we need to initialize it with some kind of h0, and then here the output will be H1 H2 HT HD plus 1 and so on. Right. so, This is a standard recurrent Network. In like classical recurrent networks, what you would do. In classical recurrent networks, how would this cells look like they would be against some kind of simple linear things? So you would have your ex not here. Mainly here like what's inside this black box? What's inside this recurrence? So you would have your ex, Maybe multiplied by some Matrix. You would have your age, maybe, multiplied, by some other Matrix, then you did them together, and then you would okay, just take. So you would, you would pass them through some kind of activation function. Okay, so one standard approach to make in recurrent cells would be something like H Prime is G of a times X plus b times, H and here G is an activation function, something like hyperbolic tangent or real and a and b are weight matrices. Okay. What else can what I want to say here? Yeah, so this is how a classical recurrent Network would look like and actually it's available to you. So recurrent networks have been around since Alone no long time ago since the 1980s in the second, half of the 1980s, there were already actual neural networks that look like this. People didn't have enough compute to actually train them. We will just, we will talk in a minute about what's Difficult about training, recurrent Network. but in general, This was how. Like this is a very old idea that has been with us for a very, very long time. oh yeah, and one more thing before I proceed to actually discussing the training and there is also One General remark about the current networks here that goes through all possible, architectures. The general remark is this. Notice. How? Notice how the recurrent Network as I explained it to you. Just now know, just how it goes through the input and Only One Direction left to right. It creates one then three six two and so on and so on. And if your Goal is to read the whole sentence, the whole input, and then say classify it based on the last hidden State and probably, it's okay. So of course, you could read it left to right or right or left but still, you need to read it and then make a decision. But if your actual problem is something like sequence labeling. So if you are supposed to have a white over here, Then it sounds suddenly stops making sense. Right. So what if so, like, I am supposed to do, I don't know. I'm supposed to do part of speech, tagging cover here. So this is a word and I'm supposed to say that whether it's a noun or a verb, or an adjective or whatever but if I do it with a recurrent Network, Like this. It would mean that. I am only allowed to look at the words before this one. And I'm not allowed to read the sentence to the end. Before I have to make my decision before I have to, to assign the parts of speech doesn't make any sense. Why should I wasn't information with it? so, depending on the problem, but in many cases, it's very natural to have water cold be directional. BT directional. I don't. Let me draw a picture. It's pretty simple, but just a little bit Messier x, 1, x, 2, x t. X, t, plus 1, x capital T, and I still have a recurrent Network that goes like this. And it's still reads. The input sequence left, right? but also, There is another recurrent Network. Starting from here that will read the same network right to lift. So it the same input, right left. So it will start from x t and then go? Go over here. Let's say this is okay, so let's see. This is H Prime T. So this is H Prime. T minus 1 and this becomes H Prime small team. And goes here. Like this. Right. And on every step, it's just a current Network that creates the exact same thing, but in the opposite direction. So it goes All right, the left. And and that is enough. Now when we are seating at XT, We have the red part, the left to right part capturing the context from the left. Capturing these guys. And the blue part capturing context from the right from these guys. So now we can just have some kind of merchants of the results. Some kind of classification, head over here and output YT. And it will actually be able to account for both left contacts and right contacts for what we had before and what's coming in the sole called here. So basically there is no reason to to not use a bidirectional return Network, unless The problem is like the problem prohibits you from doing that. For example, if you do language modeling will talk about language models a lot later. But if you, the language modeling here, are supposed to predict the next word in text. And when you are writing text, and when you are predicting the next word, of course, you don't know the word that will be after that, right? It's your job to write them. So here in this case if you have a recurrent language model it doesn't make sense to be to be directional right? You want to predict only from from the left context or actually if you do object tracking. For example that I mentioned here in object tracking too, when you are applying it in the real world, you have a stream video stream that comes at you. And maybe you can look a couple of frames ahead. Like, maybe you can delay your output for a few friends, but you definitely will not have access to like the next 10 seconds, right? So you will need to to keep tracking online in real time and you definitely want to You definitely want to have one side networks, but very often in many, many problems. You are allowed to look at the whole input before making a decision. For example, in all sorts of Where was, I sequence to sequence problems? Of course, you are allowed to read the whole paragraph before translating it, of course. So, okay, so these are like standards are RNs standard, recurrent methods, be directional, recurrent networks. And now, let's discuss the problems with the current networks. I guess we will discuss the problems today. And then solutions to the most important problem. I will not have time for that a bit more little come tomorrow. So what is the like, how does a current neural network trained? That's actually a pretty interesting. Thought and it I think it's pretty instructive to actually understand how it works. So you have the same simple right? Just for Simplicity. Let's have a one directional unit directional Network just left. Right? It plus one like this. And we go to extreme. And let's assume. That. The output. We only need the output at the end, so I read the whole sequence. And then we let's say classified. So we have some kind of head over here. And after this head, we have the loss function. And the loss function. Okay, so to do this here, to this last function also goes like the correct answer. This here gives us our predicted answer and then we compare it. We get a loss function, whatever. As usual. So how do the gradients flow like where are the weights here? Here is the thing. Whatever is the recurrent cell inside, maybe, but let's assume that looks like this doesn't really matter for us. but, Importantly. Importantly. Every recurrence cell here. Works and exactly the same way. It has the exact same weights. Right. So actually like if you look at the computational graph behind what Android you have this Waits, Of herself and this weights are copied are shared not Cooper share across all of the recurrent cells over here. Right? So it's the same Matrix W, the same weight answers that participates in every so. Here, we can't have it any other way, really? Because we would never be able to train, like, separate matrices for going from step. One to step two. And from step two to step, three, and so on. Moreover, it's a pretty good thing in the sense that when you do it like this, you can actually process arbitrary sequences of arbitrary length. You don't care about the length anymore. You can just run this for however long, you want to still the same w? But it also leads to interesting problems. So here is the last function. And you start Computing, the gradients of the loss function from here. And as the flow through the nip, through the sequence, they flow back right? And the actual like participation of this weight Matrix. Is. Is that every way from here. So, let me write, just, like, partial derivative, like the L over some specific W from here. It's this big sum, because the w. Influences the loss along the way on every single step. So it's like DL over d w. T whatever that means. So like the the part that goes over here and then it's also the L over D W, T minus 1 and so on the yellow over DW one so to speak. So they are not different ways, they're like different participation like different ages and the computational graph that go out of the grow out of that belief. So the actual influence of the same weight is is done is even many many times along the sequence for every element in the sequence you again, have this inference of them So on one hand, this is good. This is just like this is the same good effect that we had in relational Networks. because in convolutional networks, we have How to say this, informational networks, we had this effect that the same weight participates in this parallel processing across the whole image with me, which means that you can have sparse activations. You can have sparse gradients, it's fine, it's okay. It's not a problem because your sparse activations can Your sparse activation can be accumulate anyway. So here there is little bit of that. So every way is very, very important. But on the other hand, there there is a problem with this influence of w, going through the whole sequence. And the problem is this actually I think it's 7 easier to to think of this problem, not during their backward pass like I do here but just simply during the forward, pass through the network from left to right because as you go from left to right. Oh so w participates every time, right. so, let's, Just make things much much, much much more simple. Let's just say that in every recurrence like this, we take the input, say h, and b multiplied by The Matrix level. Here and this becomes H1. And then we again multiplied by W. This becomes H2. And so this is a very simplified picture. Of course you cannot in reality, you cannot have it without activation functions. In reality, there is also X and so on, but for illustration, this will be enough. so, as you go, Through the recurrent Network. Your like H1 is W Times, H 0, your H2 is like w times H1 so it's W squared times, H 0 and your HT is W to the power T times H 0. Right. And this can be a better thing. This can be a problem. What can be the problem here? Well, Matrix is have this property called the spectral radius. Or. You can think of it is just a convenience store, doesn't matter. Actually, what the spectral radius, basically tells you is how What does the Matrix when apply to a veteran multiplied by Vector? What does the Matrix do to this vectors length? Here. So basically like the norm of HT Layered, I guess not Square. No, not Square. Just the length. The norm of HT will be something like the spectral radius of W Times. The norm of HD minus 1. So every time you apply a matrix, you are on average multiplying the length of the vector, by some constant. and this constants accumulate, as you see so when, when you go to HT, The length of HT. Is like a road to the power T times, the length of a zero. so, if you started with a vector of length one, which kind of makes sense, Why didn't become so? I think. so, if you started with a vector of Length one. Then, by the end, you have a vector of this thing. So, if row, if the Spectrum radios is greater than one, then it means that your activation is just explode. Ah so if row is like given 1.1 or 1.05 or something with a long enough sequence, it will obviously go to Infinity exponentially and it will just explode you will have I don't know problems like overflows in the numbers and the numbers stop making any sense. It's like huge, huge, huge activations, which don't really reflect anything. And the same will happen as you go back because as you go back through a matrix like this, when you compute the gradients your multiplying by W. Oh, but by W transpose, but post a difference. So you're all also dependent on this kind of spectral radius. So you can have two kinds of problems. You can have exploding ingredients. Exploding gradients. When role is greater than one and everything goes to Infinity. Or you can have Vanishing gradients. When row is smaller or smaller than one and it all goes to 0. So, this is also a bad thing, right? So now this means that as the gradient travels along this path, It. Exponentially goes to zero. On the first elements of the sequence. So it basically means that you cannot have any long-term memory, the influence of early. Part of parts of the sequence will just vanish completely and we'll go to 0 is very quickly. so, In exploring gradients, just everything breaks. In Vanishing gradients, well, nothing breaks. But your network doesn't work as you as you would like So, how do we solve this problems? How I will relegate Vanishing gradients to tomorrow because this is a long discussion but exploring gradients is very, very simple. All. I mean, as you go along the network, your problem is that your gradients start to grow uncontrollably. And it's your gradient. Vector will be longer and longer and longer. Well, you can notice this right? As you go along the network. Your gradient. It becomes longer and you can see it as you go along the network. So why don't you just clip the gradient? And that's the answer. So the answer actually took the exploding, gradients problem is not to do something smart and interesting to limit row, to make it equal to one or something. No, the answer is just let's clip the gradients. So like, if you have a gradient, which exceeds, you know, one in length, let's just project it back to the unit sphere. Let's just say, okay, so now it's too long. We projected back. That's it. Next. After the next step, it will be too long. Again, we will project it again. That's the only the only thing with them. So let me go through this fight, there's probably some more stations here. Okay, the current networks. This is what we discussed, blah blah. There are two problems, exploding gradients and radiation gradients. And in exploding gradients, we just clip it. So I think this is still from careers but it doesn't matter. Of course. Every and of course by gradients for yeah this is the illustration. I was looking for the there was a very nice paper, 10 years ago, in 2013 By pescano He who studied the behavior of recurring networks. There are several very interesting points in their recommend. You read the paper actually but and, It's like it's not about any new architecture, sorry about like making it work better. It's about what's going on in the space of activations, in the space of Weights. What's going on, is the train and so on, and as for exploding gradients, the picture looks like this. So what does it mean to have an exploding gradient to have this gradient? Go to Infinity. Well, if you look at the loss function, it basically means that you have some normal part where the gradient does not explode and then boom, at some point, this there is just this vertical wall. This wall that goes to really use very, very quickly, it grows very quickly, it's basically Works called the the gradients explode. So, what happens is you go over here? And then you bounce off this wall. And if you don't clip the gradients, well you fly away gotten elsewhere. But if you do clip the gradients, well, you go back to this normal regime and you keep trying alone and you keep going in the general direction that you want so clipping, the gradients is not. A problem from the like theoretical and practical point of view. It's, it's not a bad transformation to make, it's okay. We are still, we will still continue to go in the approximately the same direction. and, Probably let me stop here. So, We've discussed recurrent neural networks. We've discussed. What we? How we process sequences with this kinds of architectures and we have discussed the main problem. The main problem is that as gradients flow in this, activation flow and forward propagation. They either blow up or vanish and it's difficult to pin the spectral radius. Exactly to one. So something needs to be done and the exploding part turns out to be easy but the initial part is real estate tomorrow will turn out to be pretty and interesting. Okay. So at this point, I want to stop any questions about what we discussed today. While you're thinking about the questions tomorrow is lecture day. So please join on time. and then, you will go back to Alex for practical sessions on Thursday and Yeah, I think they should be available today. So, yeah, just what I wanted to say on Friday on Friday. There will be a midterm presentation. We, I sent Alex list of papers yesterday evening. I think he wanted to add something from himself. I hope it will be made available today. Okay. So on Friday, on Friday, we will be listening to you. okay, thanks a lot and here, tomorrow tomorrow to lectures Be. Fresh and ready. In the morning. Bye.
