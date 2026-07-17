# Transcript — whisper_cpp

- **Provider:** whisper_cpp
- **Language:** en
- **Audio duration:** 1:35:54
- **Segments:** 967
- **model:** ggml-large-v3-turbo.bin
- **vad:** True
- **beam_size:** 5
- **entropy_thold:** 2.8
- **latency_sec:** 797.21

## Segments

**[00:00 – 00:16]** Okay. Good day or good morning still to everyone. And welcome back to the lecture part of our class, which is being done online this year.

**[00:16 – 00:43]** And last time we ended on convolutional architectures and specifically on how CNNs work and what is their main good thing that they do, what is the main advantage of using convolutions.

**[00:43 – 01:07]** And this main advantage was, of course, to reuse the same weights over the entire input and over all of the intermediate feature tensors that you see inside the neural network that are the outputs of intermediate layers.

**[01:07 – 01:22]** So all of this can be processed in parallel and you can reduce the number of weights by huge factors.

**[01:22 – 01:43]** So before we proceed with convolutional architectures today, I understand that you already kind of started talking about convolutional architectures with Alex, and that is absolutely great because now we can skip part of this lecture and faster get to recurrent networks.

**[01:43 – 02:07]** I'm not sure if we get there today, but hopefully yes. But before we begin with the lecture, let me show you a couple of things.

**[02:07 – 02:30]** I have these standard illustrations for CNNs that I think you don't really need now because you've already had practical sessions about CNNs, but maybe I will at least mention a couple of buzzwords that you can look up.

**[02:30 – 02:52]** So I won't discuss all of these pictures in detail, but basically like in classical computer vision in the days before neural networks actually worked, what you would do, what you would actually do in computer vision would still be using convolutions, but you would be using like handmade convolutions.

**[02:52 – 03:21]** They would be called filters and sometimes people call learnable convolutions filters as well. And there were like filter banks for all kinds of purposes. And if you look at classical utilities for say image processing, like sharpen, blur, add contrast, emboss and whatever, it's all done with this kind of filters.

**[03:21 – 03:47]** It's all done with filters that are applied, that are basically these small matrices, just like convolutions that are applied in parallel over the image. Right. And you can do pretty complicated stuff with this. You can do, for example, edge detection, like find out where the edges of objects on the image are.

**[03:48 – 03:56]** Here, for example, the cat itself is pretty messy in terms of the edges. So you can see it here.

**[03:56 – 04:15]** There were classical filter banks like Gabor filters, where you would do something like edge detection and to be perfectly precise, you would do like discrete derivatives, finite differences in different directions.

**[04:15 – 04:30]** And you would do like directed edge detection. So like where is, this kind of filter fires up if there is a big difference vertically, when you go vertically from one pixel to another.

**[04:30 – 04:39]** And this one, if you go horizontally from one pixel to another, a lot changes. So you can actually do it this way.

**[04:39 – 04:58]** Okay, I have illustrations for pooling. It's not very interesting, but if you apply pooling as a filter to an actual image, of course, max pooling would look very strange because it would just clamp everything to the max brightness, so to speak, and the average pooling would look better.

**[04:58 – 05:06]** That's not its purpose, really. And finally, I also have illustrations on real networks.

**[05:06 – 05:19]** So you already know what resnets are, and these are filters, these are the convolutional, the matrices of convolutions on the first layer of ResNet 18.

**[05:19 – 05:34]** And you can actually see what they're trying to recognize, some fire up for some kind of lines, like diagonal lines, vertical lines, some fire for colors or color gradients or something like that.

**[05:34 – 05:54]** And if you actually input an image and see what exactly this filters fire on, like where do they activate a lot, then you will see that, for example, this guy is looking for something like grass trees, I suppose.

**[05:54 – 06:01]** It's just looking for the color green. And here it is. And I don't know what's interesting here.

**[06:01 – 06:17]** This guy on the right is looking for horizontal edges, or vertical edges probably, and it activates the Gaber filter where there is a horizontal line.

**[06:17 – 06:32]** And if then we go through the network and we map what active filters on different layers of the network do.

**[06:32 – 06:38]** Again we go through the ResNet 18 and look at what's happening inside.

**[06:38 – 06:45]** Then you will see that, here the map becomes a little bit more complicated.

**[06:45 – 06:53]** Let me not go into that because for layer one you can just basically see like the inputs are the pixels.

**[06:53 – 06:55]** Here is the filter where does it activate, here.

**[06:57 – 07:06]** Then on subsequent layers as you understand now, there is not such a direct correspondence between pixels and outputs.

**[07:06 – 07:19]** Because every picture has a reception field. You can find which part of the image it's looking at.

**[07:19 – 07:27]** But what exact pixels are contributing the most, that requires a little bit of math.

**[07:27 – 07:36]** So I will skip that, but you can actually look at what parts of the image even top layer features fire up for.

**[07:36 – 07:53]** And you can see that, for example, in ResNet-18, the second layer fires for some high-frequency stuff in the image.

**[07:53 – 08:01]** Throughout the whole image, but just some kind of stripes or something and edges and stuff like that.

**[08:01 – 08:13]** And then we go for more salient objects, right? So here, for example, there is some filter that fires for the eyes and the tips of the ears, something like that.

**[08:13 – 08:22]** And then when we go to later layers, we become more and more semantic. So on these pictures, I don't think that clear.

**[08:22 – 08:34]** They're very blurry and TresNet-18 is not a very good network, but still you can see that kind of there is a filter for the ears, there is a filter for the head as a whole.

**[08:34 – 08:46]** Or you can actually go back from a deep feature back to the pixel level.

**[08:46 – 08:52]** Sorry, I didn't explain it well, but this was on the level of the feature maps.

**[08:52 – 08:58]** I mean, it becomes blurry and blur, there is less and less geometry, it just makes less sense.

**[08:58 – 09:06]** But you can also, with this map that I mentioned, map it back to the original image, to the filters of the original image.

**[09:06 – 09:13]** And you can see approximately, now it's not precise, but you can see approximately what it fires on.

**[09:13 – 09:15]** And it's pretty interesting, right?

**[09:15 – 09:23]** So, in ResNet 3.10, on a deep layer, you can find the feature that selects most for the cats.

**[09:23 – 09:37]** So, what it means to be cat-selective, it means that ResNet was trained to distinguish classes from either ImageNet, like cats and dogs.

**[09:37 – 09:43]** You can find which feature gives you the most information regarding this specific class,

**[09:43 – 09:50]** which feature correlates, whose activation correlates the best with this specific class.

**[09:50 – 09:57]** And if you look at the cat-selective feature, and you input an image which is half cat, half dog,

**[09:57 – 10:01]** like this one, I just merged two together, that's it.

**[10:01 – 10:06]** Then, you will see that it fires up on the cat, and the dog-selective feature,

**[10:06 – 10:10]** indeed, fires up on the dog, approximately.

**[10:10 – 10:12]** So, this kind of works.

**[10:12 – 10:18]** And also, I wanted to mention, again, I don't want to spend time discussing the math,

**[10:18 – 10:35]** but there are also methods for more detailed interpretation of what the network actually is doing.

**[10:35 – 10:39]** So, there is, for example, GradCam, it's not the only one, but it's a good one,

**[10:39 – 10:44]** and if you can run it for the network output, like the predicted class,

**[10:44 – 10:50]** a single class, again, recall that the network's output is this set of probabilities.

**[10:50 – 10:54]** So, every class in the classification network is a separate output,

**[10:54 – 11:02]** which is convenient in cases like this, because we can actually look at specific outputs,

**[11:02 – 11:13]** and, for example, the Egyptian cat output responds to this and has obtained the value that it has

**[11:13 – 11:17]** due to pixels like this.

**[11:17 – 11:21]** So, it's not yet an attention mechanism, we'll get to those tomorrow,

**[11:21 – 11:31]** but it's kind of an interpretation of why exactly, due to which pixels the network chose this value for this output.

**[11:31 – 11:36]** And sure enough, you can run it for different classes.

**[11:36 – 11:41]** For example, again, if you can't get the cat and the dog, then the Egyptian cat output will look at the cat,

**[11:41 – 11:46]** and the Blenheim-Spaniel output will look at the dog, that's it.

**[11:46 – 11:56]** Okay, so that was a brief remark about what we will not discuss in more detail.

**[11:56 – 12:01]** So, about the basics of convolutional networks, what they are looking at.

**[12:01 – 12:08]** Now, let's get to the main part, I think, of today,

**[12:08 – 12:11]** and the main part is important convolutional architectures,

**[12:11 – 12:13]** and hopefully this will be only the first main part,

**[12:13 – 12:18]** because some of the most important stuff you have already discussed with Alex, right?

**[12:18 – 12:26]** So, the most important convolutional architecture in history was, of course, AlexNet,

**[12:26 – 12:31]** and I hope that Alex discussed his architecture with you,

**[12:31 – 12:34]** and if not, I guess by now we can skip it.

**[12:34 – 12:40]** So, it was like the first convolutional network that actually worked,

**[12:40 – 12:48]** that beat every competing method completely on the ImageNet recognition,

**[12:48 – 12:51]** large-scale visual recognition competition,

**[12:51 – 13:01]** and that defines the state-of-the-art in an extraordinarily big margin.

**[13:01 – 13:08]** So, in 2011 or 2012, when it was participating in this competition,

**[13:08 – 13:15]** the results were like the error rate for all of the rest of the methods

**[13:15 – 13:20]** was like 22%, 23%, something like this,

**[13:20 – 13:24]** and the error rate for AlexNet was like 13%.

**[13:24 – 13:28]** So, it was a huge jump, a huge gap, and of course, next year,

**[13:28 – 13:32]** the whole leaderboard was only convolutional networks.

**[13:32 – 13:37]** Nobody ever went back to classical computer vision since AlexNet.

**[13:37 – 13:43]** This was the revolution that happened in image classes.

**[13:43 – 13:49]** And technically, and in terms of specific ideas,

**[13:49 – 13:54]** what is most interesting in AlexNet are two things.

**[13:54 – 13:57]** It's a pretty standard convolutional architecture,

**[13:57 – 14:02]** but you can see first that it's split in two.

**[14:02 – 14:13]** And that was the first actual industrial scale instance of model parallelization.

**[14:13 – 14:17]** So this is very important. We won't have time to go into more details.

**[14:17 – 14:19]** So now is a good time to just mention it.

**[14:19 – 14:24]** In deep learning, you have huge models, you have huge data sets.

**[14:24 – 14:31]** So of course you need to parallelize. You need to make use of multiple GPUs if you have multiple GPUs.

**[14:31 – 14:36]** And there are two main ways that you can do it.

**[14:36 – 14:39]** You can do what is called data parallelization.

**[14:39 – 14:50]** Data parallelization is when you have one mini-batch in GPU 1, another mini-batch in GPU 2, another mini-batch in GPU 3.

**[14:50 – 14:55]** You run them all in parallel and then you collect the results and you do a single update

**[14:55 – 14:58]** based on the weight updates from all of the GPUs.

**[14:58 – 15:02]** So you don't have to change anything in your implementation.

**[15:02 – 15:04]** The network works just as usual.

**[15:04 – 15:11]** The only difference is that since now you have multiple GPUs in parallel, you can collect...

**[15:11 – 15:16]** Basically, you're just increasing the mini-batch size for yourself.

**[15:16 – 15:36]** So what you're actually doing is you're expanding the size of...

**[15:36 – 15:42]** You're expanding your mini-batch size by splitting the mini-batch into different GPUs.

**[15:42 – 15:44]** That's data parallelization.

**[15:44 – 15:50]** There's a lot of work on that because you can do it in many different smart and interesting ways.

**[15:50 – 15:54]** But the basic idea is very simple.

**[15:54 – 15:56]** Model parallelization is more complicated.

**[15:56 – 16:03]** In model parallelization, the assumption is that your model does not fit on your GPU.

**[16:03 – 16:07]** And if your model does not fit on your GPU, what can you do?

**[16:07 – 16:11]** Well, you need to put half of your model on one GPU and another half on the other.

**[16:11 – 16:16]** And that's exactly what AlexNet was doing back in 2011 already.

**[16:16 – 16:22]** So 2012 was the paper, but the actual network was in 2011.

**[16:22 – 16:30]** And, of course, that was like a huge feat of engineering back in 2011.

**[16:30 – 16:37]** Alex Krajewski was a wonderful programmer and he actually implemented all of this by hand.

**[16:37 – 16:43]** These days, of course, we don't need to implement anything by hand.

**[16:43 – 16:48]** And even our cloud codes do not need to implement this by hand.

**[16:48 – 16:55]** In PyTorch, you can just say, well, I want this weight matrix to live on this GPU

**[16:55 – 17:00]** and that weight matrix to live on that GPU, and PyTorch will just handle the rest automatically.

**[17:00 – 17:07]** But still, when you design a parallel network like this, a network that spans multiple GPUs,

**[17:07 – 17:13]** you want to minimize communication across the GPUs because, of course, it will be slower than inside one GPU.

**[17:13 – 17:25]** So here, for example, you can see that these guys talk to the two strands, the two GPUs talk to each other over here and then talk to each other at the very end.

**[17:25 – 17:31]** There are only two places where they actually exchange information.

**[17:31 – 17:39]** Anyway, AlexNet was the breakthrough.

**[17:39 – 17:43]** People like to talk of like the AlexNet moment or something.

**[17:43 – 17:48]** But then, of course, the field exploded.

**[17:48 – 17:51]** Everybody wanted to do convolutional networks.

**[17:51 – 17:57]** And it turned out that you can actually improve convolutional networks quite a lot with relatively simple ideas.

**[17:57 – 18:07]** So some of the most important ideas we already discussed with Alex, not Krzyzewski, but Alex Davidov.

**[18:07 – 18:20]** And the first idea is VGG, and VGG is the reason why AlexNet still had 11 by 11 convolutions on the first layer.

**[18:20 – 18:28]** But now you will never see 11 by 11 convolutions, you will only see 3 by 3 convolutions and maybe 5 by 5 sometimes.

**[18:28 – 18:41]** Because with the VGG idea, you can represent large convolutions as compositions of small convolutions.

**[18:41 – 18:49]** And this is actually a great way to do things because it's like a convolution inside a convolution, right?

**[18:49 – 18:54]** And this convolution inside a convolution reduces the number of weights further.

**[18:54 – 18:58]** I think you did this with Alex, this calculations of how many weights.

**[18:58 – 19:02]** And it serves as kind of additional structural regularization.

**[19:02 – 19:08]** Again, you are saying to the network, you can process different parts of the input in the same way.

**[19:08 – 19:12]** And usually it just works better.

**[19:12 – 19:26]** So the second idea that you also discussed with Alex, as far as he told me, is Inception and Googling it.

**[19:26 – 19:31]** And generally, like the idea that is known as network and network.

**[19:31 – 19:39]** So I started talking about convolutional networks with you with this.

**[19:39 – 19:49]** I won't switch back to them, but you remember the slides with this boy on the toy horse and all of this.

**[19:49 – 20:01]** And right there, there were tiles being processed by what I called small neural networks on this, what was called small neural network on these pictures.

**[20:01 – 20:12]** And since then, when we actually implemented this small neural networks, they were always like the simplest possible neural networks.

**[20:12 – 20:22]** We were always talking only about a single matrix that processes the whole input and doesn't care and doesn't do anything interesting.

**[20:22 – 20:31]** Just put everything together, throw it to a single vector of numbers, multiply by this weight matrix, here is the output.

**[20:31 – 20:40]** But you don't have to limit yourself to that, right? You don't have to do that, right?

**[20:40 – 20:55]** You can do more interesting things and this inception trick and basically these ideas of network and network are exactly this.

**[20:55 – 21:07]** You can replace this simple convolution with a far more complicated approach, far more complicated network.

**[21:07 – 21:19]** When you do that, you still have exactly the same idea of processing the tiles in parallel with the same small network.

**[21:19 – 21:22]** It's only that the small network is now more interesting.

**[21:22 – 21:27]** So, yeah, I think you've discussed inception, I won't repeat that.

**[21:27 – 21:41]** What I want to note here is that when you look at these inception units, when you look at this small network, so to speak, you see usually multiple parallel threads of processing.

**[21:41 – 21:46]** And that is not a coincidence and we will talk more about that today.

**[21:46 – 22:01]** OK, so third, the most important idea of all of this, the idea that will be with us throughout the whole deep learning.

**[22:01 – 22:04]** It will be used in transformers, it's used everywhere.

**[22:04 – 22:08]** The idea of residual connections and thus resonance.

**[22:08 – 22:13]** Again, Alex said that you already discussed it, so I will mostly skip.

**[22:13 – 22:17]** Basically, the idea is like this.

**[22:17 – 22:23]** I apologize, I keep forgetting to redo the Russian picture.

**[22:23 – 22:32]** But anyway, this is input, so the input is x, then f of x, then the next layer is like this, f of x.

**[22:32 – 22:42]** And the ResNet problem is that when f of x sort of drains and saturates, the gradient will go to zero.

**[22:42 – 22:46]** This layer will not want to change anymore.

**[22:46 – 22:51]** And when it doesn't want to change anymore, that's okay for the layer.

**[22:51 – 22:58]** But if you didn't have a residual connection, it would mean that nothing below that layer will ever learn.

**[22:58 – 23:07]** Because everything below the layer receives gradients through this layer multiplied by its derivatives.

**[23:07 – 23:10]** And if those go to zero, then nothing changes below that.

**[23:10 – 23:12]** That's a bad thing.

**[23:12 – 23:15]** So what we do is we use residual connections like here.

**[23:15 – 23:18]** We do a connection that goes around.

**[23:18 – 23:23]** Here we have something very simple and specifically just a plus.

**[23:23 – 23:26]** And now our result is f of x plus xk.

**[23:26 – 23:29]** And now f of x can saturate all at once.

**[23:29 – 23:31]** The derivative can go to zero.

**[23:31 – 23:32]** That's fine.

**[23:32 – 23:39]** If it goes to zero, then the gradient just goes to, the matrix of derivatives just goes to an identity matrix.

**[23:39 – 23:50]** The gradient will just flow through this layer and, not through, but flow around this layer and continue to the bottom layers.

**[23:50 – 24:06]** And as soon as resnets were introduced, Kamin He, this guy who invented resnets and he's actually a very cool researcher with a lot of great papers, Kamin He called it the revolution of depth.

**[24:06 – 24:21]** And indeed it was. So when residual connections were introduced and were used in deep convolutional architectures, you immediately could train networks with hundreds and hundreds of layers.

**[24:21 – 24:28]** So like AlexNet had eight trainable layers. We don't count pooling here.

**[24:28 – 24:39]** VGG had 19 layers. GoogleNet with the first inception units had 22 layers and resnet next year had like 150 layers.

**[24:39 – 24:55]** And there was totally no problem to, there was no problem to grow further.

**[24:55 – 24:58]** There was no problem to increase the depth further.

**[24:58 – 25:06]** You can do resnet 200, 300, 500, 2000 and it will still train. It will still be fine.

**[25:06 – 25:14]** The problem only is that it will stop improving, right? So it will still be trained

**[25:14 – 25:19]** and will still do the job. But if you increase your network by another factor of two

**[25:19 – 25:23]** and the results don't improve, well, maybe you shouldn't be doing that, right?

**[25:23 – 25:29]** So it only makes sense to add new layers while they still help.

**[25:29 – 25:37]** So actual resnets go up to about 200 layers and then I guess they run out of steam.

**[25:37 – 25:44]** Okay. So as far as I understood Alex, if I understood him correctly,

**[25:44 – 25:52]** this is approximately where you stopped and let me complete this arc.

**[25:52 – 25:57]** Let me continue this discussion of different convolutional ideas,

**[25:57 – 26:06]** of ideas that kind of define convolutional architectures with our next,

**[26:06 – 26:13]** with our first detailed point, point one, which is the bottleneck layers,

**[26:13 – 26:21]** bottlenecks and an idea that is usually called split transform merge.

**[26:21 – 26:27]** Sorry, I'm not yet used to writing here.

**[26:27 – 26:37]** Maybe I hope. Split transform merge.

**[26:37 – 26:41]** So what's the bottleneck idea?

**[26:41 – 26:52]** Well, actually, you can look at, for example, the VGG idea as another way to reduce the number of weights, right?

**[26:52 – 27:02]** Because you replace big convolution which has n squared weights with a sequence of small convolutions which have linear and n weights, and that's great.

**[27:02 – 27:13]** So even though convolutions by themselves already start off by saving a huge number of weights, you can actually try to do better.

**[27:13 – 27:16]** You can actually try to reduce even further.

**[27:16 – 27:25]** And let's just step back, look at a convolutional layer and see where and what we can improve.

**[27:25 – 27:32]** So a standard convolutional layer will have some 3D tensor as the input.

**[27:32 – 27:36]** So the input will be of size.

**[27:36 – 27:49]** OK, so let's actually say that this is already the window that I cut out because I never want to care about the full input.

**[27:49 – 27:52]** It's always just copied over.

**[27:52 – 27:59]** So this is already the cut out window and it has like depth D, width W and height H.

**[27:59 – 28:04]** Then we go to the convolutional layer.

**[28:04 – 28:14]** And as a result of the convolutional layer, we get a single vector of features of size T prime.

**[28:14 – 28:28]** So a standard convolutional layer will have the matrix of weights of dimensions D times W times H times D prime.

**[28:28 – 28:36]** And as we discussed, it's much, much, much better than if we tried to do it with a fully connected layer or something else.

**[28:36 – 28:40]** But still, it can actually add up. It can grow pretty quickly.

**[28:40 – 28:53]** So if, for example, like D is something like 256, which is pretty standard inside a big convolutional architecture,

**[28:53 – 29:02]** and D prime is also something like 256, then even, I mean, the VTG idea lets you keep W and H small.

**[29:02 – 29:10]** But still, in here, you have like these tensor of weights, 256 by 3 by 3 by 256.

**[29:10 – 29:13]** And that's a pretty big number, right?

**[29:13 – 29:19]** So that's like, oh, I don't know, 2500 times another 25.

**[29:19 – 29:23]** Okay, I embedded math at this level, but you can figure it out.

**[29:23 – 29:27]** What's 25 squared? It's 725, right?

**[29:27 – 29:32]** So it's 75K, I guess.

**[29:32 – 29:41]** No, no, it's 750K, 700K, something like this, right?

**[29:41 – 29:51]** Yeah, 250 by 250 is 75K times 9, something like that, something like 700K.

**[29:51 – 29:56]** Which is quite a lot, right?

**[29:56 – 29:59]** So how can we reduce this?

**[30:04 – 30:10]** What is the problem that we might somehow solve here?

**[30:10 – 30:13]** Where can we save on these weights?

**[30:13 – 30:19]** The bottleneck idea is actually pretty straightforward and it goes like this.

**[30:19 – 30:28]** What if instead of getting the full 256 by 256 multiplied by 9,

**[30:28 – 30:38]** what if we actually compressed the features down and only then did the convolution?

**[30:38 – 30:40]** So here is how it would work.

**[30:40 – 30:46]** You have your input and your input is long.

**[30:46 – 30:50]** It's like E times W times H.

**[30:50 – 30:56]** But first, you would run it through a one-by-one convolution.

**[30:56 – 30:58]** I hope you discussed those with Alex.

**[30:58 – 31:04]** A one-by-one convolution just by definition doesn't do anything geometric.

**[31:04 – 31:15]** It just takes one feature vector here and rearranges it.

**[31:15 – 31:19]** It does something interesting inside the feature vector.

**[31:19 – 31:25]** But it doesn't do anything to the geometry, to the receptive fields, to anything like that.

**[31:25 – 31:35]** And what if we use this one-by-one convolution to actually reduce the depth, to reduce the number of channels?

**[31:35 – 31:42]** So that now we would have something like d double prime times w times h with d double prime small.

**[31:42 – 31:49]** So if I had d like 256 maybe d double prime is like 32.

**[31:49 – 32:03]** And then I would have my true convolution here and it would give me a short vector.

**[32:03 – 32:08]** I would put like d triple prime here but okay let's just say it's d double prime too.

**[32:08 – 32:14]** And then I would have another one by one convolution if I do want to have like d prime at the output.

**[32:14 – 32:20]** Then I would have to stretch back this feature vector to size d prime.

**[32:20 – 32:36]** So the convolution itself, so the one by one convolution now has like d times one times one times d double prime weights.

**[32:36 – 32:40]** This is one by one convolution.

**[32:40 – 32:43]** This convolution has how many weights?

**[32:43 – 32:49]** d double prime times w times h times d double prime.

**[32:49 – 32:54]** And also this convolution is d double prime times one times one times d prime.

**[32:54 – 32:58]** So you can kind of get a feeling for what's happening here, right?

**[32:58 – 33:03]** I avoid multiplying 256 squared by nine.

**[33:03 – 33:09]** And actually I avoid 256 squared completely, right?

**[33:09 – 33:11]** There's still a 9 in there.

**[33:11 – 33:13]** It still gets multiplied by something,

**[33:13 – 33:15]** but that something is much smaller than 256.

**[33:16 – 33:20]** So let's plug in the numbers.

**[33:20 – 33:25]** In this example, it would be like 256 times 32

**[33:25 – 33:29]** plus this 256 times 9 times...

**[33:29 – 33:30]** Oh, sorry, sorry, sorry, sorry.

**[33:30 – 33:36]** Plus 32 times 9 times 32, right?

**[33:36 – 33:39]** Plus, again, 32 times 256.

**[33:40 – 33:44]** So even though I have three convolutions instead of one now,

**[33:44 – 33:46]** I still save a lot of weights.

**[33:47 – 33:49]** So let me pull 256 out.

**[33:49 – 33:52]** It will be 32 plus...

**[33:52 – 33:56]** What, now I have to take a 4 out of this.

**[33:56 – 33:59]** So now I have to take an 8 out of this.

**[34:00 – 34:03]** So 4 is left 9 by 4 and another 32.

**[34:04 – 34:08]** So with 32 and 32, 64 and 36, exactly 100.

**[34:08 – 34:12]** That will be like 256 times 100, right?

**[34:12 – 34:18]** And over there, I had 256 times 2,500, right?

**[34:18 – 34:20]** Times 256 times 9.

**[34:20 – 34:26]** So this is about, in our simple example,

**[34:26 – 34:32]** that's about like 25x smaller, 25x smaller.

**[34:32 – 34:38]** And we have saved a lot of weights, okay?

**[34:38 – 34:39]** A lot of weights.

**[34:42 – 34:46]** Well, but now when you look at this idea,

**[34:47 – 34:52]** something should feel funny to you about it.

**[34:52 – 34:56]** Something should not sit right with you about this idea.

**[34:56 – 34:57]** And what is that?

**[34:57 – 34:59]** What is the problem here?

**[34:59 – 35:04]** Oh, what did I just do?

**[35:04 – 35:08]** I took a vector of 256, a long vector,

**[35:09 – 35:10]** a vector of 256 features.

**[35:11 – 35:15]** So in the input, every pixel, every feature map,

**[35:16 – 35:20]** every feature vector was long and had a lot of information.

**[35:20 – 35:21]** It was like 256 numbers.

**[35:22 – 35:25]** And then I just compressed it down to 32 numbers.

**[35:25 – 35:28]** Then I did interesting stuff on 32 numbers.

**[35:28 – 35:32]** And then somehow I decompressed it back to 256.

**[35:32 – 35:37]** But that decompression cannot restore the information that I lost.

**[35:38 – 35:44]** So what I'm doing here is I'm taking a long and interesting vector.

**[35:46 – 35:48]** So geometrically speaking,

**[35:49 – 35:58]** I'm leaving in the feature space of a high dimension.

**[35:58 – 35:59]** Like 256.

**[36:00 – 36:02]** But inside this feature space,

**[36:02 – 36:06]** I am picking a specific subspace,

**[36:06 – 36:14]** a specific projection of this much smaller dimension.

**[36:15 – 36:20]** So I am reducing my features

**[36:20 – 36:24]** that are long and interesting and complicated

**[36:24 – 36:28]** down to a much simpler thing, to a much smaller dimension.

**[36:28 – 36:31]** I'm just taking one view of these things.

**[36:33 – 36:37]** And that doesn't sound that bad,

**[36:37 – 36:39]** but if you think about it,

**[36:39 – 36:42]** it doesn't make any sense

**[36:42 – 36:44]** to actually do what I am proposing here.

**[36:44 – 36:50]** Because if I just compress down

**[36:50 – 36:54]** 256 numbers worth of information to 32,

**[36:54 – 36:58]** why on earth do I need 256 numbers at all?

**[36:59 – 37:02]** I mean, this is happening inside a network

**[37:02 – 37:04]** that I am designing myself.

**[37:04 – 37:07]** These 256 numbers did not

**[37:07 – 37:08]** grow on a tree.

**[37:08 – 37:10]** They came from an earlier layer.

**[37:10 – 37:13]** So if all I wanted to do was this,

**[37:13 – 37:17]** then I would just replace D

**[37:17 – 37:19]** by D double prime.

**[37:20 – 37:21]** I would just say,

**[37:21 – 37:23]** okay, so let the previous layer

**[37:23 – 37:24]** produce 32 features.

**[37:24 – 37:26]** Why do I need this artificial compression

**[37:26 – 37:27]** decompression stuff?

**[37:29 – 37:31]** And that would save even more weights

**[37:31 – 37:36]** and that would be even better, right?

**[37:36 – 37:41]** So the way I told you this bottleneck idea,

**[37:41 – 37:43]** it doesn't work by itself.

**[37:43 – 37:46]** And the editor doesn't and never appears like that.

**[37:46 – 37:50]** But it suddenly starts to make a lot of sense

**[37:50 – 37:55]** if you do it not once, but several times.

**[37:56 – 38:01]** So how it actually gets used is

**[38:01 – 38:07]** you start with this input tensor,

**[38:07 – 38:09]** D times W times H,

**[38:10 – 38:12]** and then you do several copies

**[38:12 – 38:16]** of this processing pipelines.

**[38:18 – 38:20]** Like you have one by one then convolution,

**[38:21 – 38:24]** you have one by one then convolution,

**[38:25 – 38:26]** and so on.

**[38:27 – 38:32]** And then you somehow unite the results,

**[38:33 – 38:34]** you combine the results.

**[38:34 – 38:36]** So for example, in this case,

**[38:36 – 38:37]** it could be like this.

**[38:39 – 38:44]** I have D of 256,

**[38:44 – 38:48]** and out here I have a vector of size 32.

**[38:49 – 38:54]** So how many vectors of size 32 I need

**[38:54 – 38:57]** to have a new vector of size 3256?

**[38:58 – 39:00]** Well, eight of them, right?

**[39:00 – 39:03]** So why don't I just copy this eight times

**[39:03 – 39:06]** and concatenate the results like this?

**[39:09 – 39:12]** This is a pretty standard way of doing this.

**[39:12 – 39:17]** So I do my processing eight separate times.

**[39:18 – 39:25]** Notice that even though it's the same picture,

**[39:25 – 39:27]** it's the same structure of processing,

**[39:27 – 39:29]** the actual processing will be very different, right?

**[39:29 – 39:34]** Because these strands, these pathways will learn different weights.

**[39:35 – 39:35]** They will do different things.

**[39:36 – 39:38]** You need to break the symmetry and initialization,

**[39:38 – 39:41]** and then they will just happily go to different minima

**[39:41 – 39:45]** and to implement different ideas.

**[39:46 – 39:50]** And yes, now I'm not saving 25x weights,

**[39:51 – 39:55]** because now to actually go from 256 to 256,

**[39:55 – 39:59]** I need to copy this eight times, right?

**[40:00 – 40:06]** So now instead of saving 25x,

**[40:06 – 40:09]** I'm only saving 4x weights.

**[40:09 – 40:12]** But it's still a pretty big saving, right?

**[40:13 – 40:15]** And actually it turns out that in practice,

**[40:16 – 40:17]** it's a pretty good idea.

**[40:17 – 40:22]** So what we are actually doing is in this huge space,

**[40:22 – 40:26]** we are choosing not one projection,

**[40:27 – 40:30]** not one way to reduce the dimension,

**[40:31 – 40:33]** but we are choosing multiple different ways,

**[40:33 – 40:38]** multiple different viewpoints on these complicated features.

**[40:39 – 40:42]** And so I look at it from this side

**[40:42 – 40:44]** and then I look at it from this side

**[40:44 – 40:46]** and then I look at it from that side

**[40:46 – 40:50]** and it's like different projections,

**[40:50 – 40:55]** different snapshots of this same big space of features.

**[40:56 – 40:59]** And when you actually do that, it's pretty interesting.

**[40:59 – 41:05]** And now it's not just usually you can train it

**[41:05 – 41:08]** to not lose any important information,

**[41:09 – 41:21]** but even better, you can actually expect it to do even better

**[41:21 – 41:24]** than if you just process this whole 256 thing.

**[41:25 – 41:31]** So it's actually, and I cannot get into full detail to explain why,

**[41:31 – 41:41]** but it's actually a good idea to even do lots of random projections

**[41:41 – 41:42]** of your high-dimensional object.

**[41:42 – 41:44]** Even that is usually a good idea.

**[41:45 – 41:46]** And here the projections are not random.

**[41:47 – 41:49]** Here the projections are learned,

**[41:49 – 41:52]** and they are learned to be useful, which is even better.

**[41:53 – 42:01]** So this is usually called split, transform, merge for obvious reasons.

**[42:02 – 42:06]** First you split, then you transform, then you merge.

**[42:07 – 42:12]** And it's a pretty standard idea in convolutional architectures.

**[42:13 – 42:18]** So I guess that's the important thing that I wanted to say.

**[42:18 – 42:19]** Let's go back to the slides.

**[42:20 – 42:22]** Yes, but here is an example in ResNext.

**[42:23 – 42:25]** Kind of outdated now.

**[42:25 – 42:30]** It was 10 years ago, but a perfect example of just an idea like this.

**[42:30 – 42:34]** You split the 256 into 32 paths of four.

**[42:34 – 42:39]** So it's like an extreme projection, but several extreme projections, and that's better.

**[42:41 – 42:47]** So what else can I say about these classical convolutional architectures?

**[42:47 – 42:56]** Well, I probably should mention this line of inception networks and inception ResNet networks.

**[42:57 – 43:03]** I'm not sure if you discussed them with Alex, you discussed inception, you discussed ResNet, but what about the combination?

**[43:04 – 43:14]** And basically, the progression of these networks, they are a pretty important family of networks.

**[43:14 – 43:22]** They were, like for a long time, the best available backbones for all sorts of computer vision tasks.

**[43:22 – 43:43]** When we get to object detection and segmentation, we will discuss how, for example, we will discuss how when you do an object detection architecture or a segmentation architecture, you can't really expect to train it from scratch.

**[43:43 – 43:53]** So there will be not enough labeled data to train it from scratch because labeling is very difficult for these complicated computer vision tasks.

**[43:55 – 44:10]** So what you actually do in practice is you take what is called the backbone, you take a network trained on ImageNet, for example, to just classify stuff, then you cut off its head and you use the rest of the network as a feature extractor.

**[44:10 – 44:25]** Maybe you find Unity a little, maybe even not, and this Inception ResNet family was one of the most influential, one of the best families of these backbones back in 2016.

**[44:25 – 44:49]** And what is its main idea, of course, doesn't make sense to learn them in big detail, but its main idea was that you do this Inception trip, you do this network and network thing, you replace, you do better and better basic blocks that process the inputs, like the small neural networks.

**[44:50 – 45:15]** And from version to version, they just invented better and better such basic blocks, basically, that was the main component of progress And another interesting component of progress was that they also replaced pooling layers with blocks like this, and I think I mentioned this last time,

**[45:15 – 45:32]** if you want to reduce your dimension, if you want to reduce from 256 by 256 image down to 128 by 128 image, yeah, you can do max pooling.

**[45:32 – 45:43]** But it's even better to have another network and network thing, another layer that can be trained and that can do more interesting stuff.

**[45:43 – 45:51]** Only that you tune this, you compose this layer in such a way that the output becomes smaller.

**[45:51 – 45:59]** Usually with strides, with strided convolutions that just reduce the geometry, that's what they do.

**[45:59 – 46:10]** So over here, they indeed, in later inception networks, they indeed had this reduction blocks that can have pooling inside.

**[46:10 – 46:14]** But it's again this kind of transfer, split, then merge idea.

**[46:14 – 46:25]** So there are several parallel lines of processing here that do different things and then their results are merged together in some way.

**[46:25 – 46:30]** So this has been an influential idea in convolutional architecture.

**[46:30 – 46:36]** Then you get residual connections and you get Inception ResNet, that's it.

**[46:36 – 46:52]** I won't go into more details, but basically Inception ResNet V2 was a very influential, very interesting backbone that was used very widely.

**[46:52 – 46:59]** Okay, so I will probably keep the rest mostly.

**[46:59 – 47:12]** There were some more ideas on how to further reduce the size of the network and also to reduce the number of layers.

**[47:12 – 47:22]** And let me not go into these ideas in detail, but this basic trade-off, not trade-off, but this basic, there are basically two different things that you want to optimize.

**[47:22 – 47:30]** One is memory. You want to have a smaller network if you want to, for example, feed to a mobile device or something.

**[47:30 – 47:40]** And that means reduce the number of weights, because basically the size of the network is the number of weights, that's it.

**[47:40 – 47:48]** And then there is also another dimension, which is latency, which is how quickly the network will actually operate.

**[47:48 – 47:53]** So in computer vision, you often care about latency.

**[47:53 – 48:03]** For example, if you do something like tracking on a surveillance camera, then of course you need it to work in real time, because the surveillance

**[48:03 – 48:14]** camera will work like 24/7, and of course you can't lag behind the video stream while you are processing a continuous video stream.

**[48:14 – 48:26]** So you definitely want your tracking or whatever you do with this stream, you definitely want it to work in like 30 frames per second at least, and preferably 60.

**[48:26 – 48:36]** So latency is also important, and what I wanted to just note here is that there are two different things.

**[48:36 – 48:43]** I mean, to some extent, it's true that if you have a smaller network, it will run faster.

**[48:43 – 48:57]** But actually, the latency depends on the number of layers, because once the network fits into your GPU, the rest is more or less unparalleled inside the layer.

**[48:57 – 49:03]** And what actually matters is how many steps you make.

**[49:03 – 49:08]** So every step, okay, it will also depend on, say, the intermediate representation size.

**[49:08 – 49:13]** Yes, of course, it will be slower if you have more weights inside every layer.

**[49:13 – 49:16]** But the most important component is the number of layers.

**[49:16 – 49:24]** So these two things make networks faster or make them smaller.

**[49:24 – 49:27]** They don't conflict that much, but they are two different objectives.

**[49:27 – 49:29]** Just wanted to mention that.

**[49:29 – 49:31]** And yeah, let's keep SqueezeNet.

**[49:31 – 49:35]** Nothing new for us here. Let's keep MobileNet here.

**[49:35 – 49:44]** The whole thing was indeed to put computer vision on mobile devices.

**[49:44 – 49:49]** And finally, I think what I want to end this discussion with.

**[49:49 – 50:05]** Finally, the family of CNNs that kind of topped this progress of CNN architectures.

**[50:05 – 50:13]** I mean, probably there was something afterwards, but mostly even now everybody just uses this.

**[50:13 – 50:20]** The line of networks that proved to be the best were EfficientNet.

**[50:20 – 50:34]** And again, I don't want to go into too much detail, but it's again the same story that we saw with activation functions.

**[50:34 – 50:49]** And then I mentioned that we saw a similar story with gradient descent algorithms, but gradient descent algorithms we didn't discuss that.

**[50:49 – 51:06]** And here in EfficientNet, the architecture was actually found automatically with a big neural architecture search.

**[51:06 – 51:23]** So what they did, and again, not too much detail, but just the basic idea, what they did was they looked at how you scale a convolutional network.

**[51:23 – 51:30]** Like when you increase the network, in what ways can you increase the network?

**[51:30 – 51:42]** Like what are the different dimensions that you can change? What are the knobs that you can rotate and tweak in order to change what the network does?

**[51:42 – 51:48]** and it turns out there are quite a few knobs right so you can change the depth of the network

**[51:48 – 51:56]** obviously you can change so you can add more layers you can change the width of the network you can

**[51:59 – 52:01]** add more

**[52:04 – 52:11]** depth to it you can add so sorry we usually call it depth but yeah inefficient net depth is the

**[52:11 – 52:18]** number of layers which also is very reasonable to call that and width is like the the the length of

**[52:18 – 52:24]** the feature vector so you can make the network wider by adding more features it also allows you

**[52:24 – 52:32]** to make the network smarter but spending more weights and also you can do something like higher

**[52:32 – 52:43]** resolution so you can increase the the number of pixels in the input so to speak and then what they

**[52:43 – 52:50]** did was they just rolled down some very simple formulas like okay so as i increase the network

**[52:50 – 52:57]** i increase the depth the width and the resolution how does the total size of the network change well

**[52:57 – 53:01]** you multiply them all together you get like the product of three numbers and it goes into the

**[53:01 – 53:08]** exponent and this is the number of weights okay so what are we looking for we are looking for the

**[53:08 – 53:18]** the perfect balance between these three numbers basically the idea is if your depth grows

**[53:18 – 53:24]** exponentially with exponent alpha your width grows exponentially with exponent beta your

**[53:24 – 53:31]** resolution grows exponentially with exponent gamma then there is like a natural relation between alpha

**[53:31 – 53:40]** beta and gamma but then you need to actually find the best values of those so that's what they did

**[53:40 – 53:48]** then they run like huge evolutionary search to find this best combinations of hyperparameters

**[53:48 – 53:56]** and they were successful they were pretty successful and this family of efficient this

**[53:56 – 54:04]** efficient net family as you can see here basically just defined the state of the art right defined

**[54:04 – 54:13]** across the whole field so we will see plots like this later in for other computer vision tasks here it

**[54:13 – 54:22]** also is pretty i think instructive to look at how this plot works it's uh there are two axes right

**[54:22 – 54:30]** one of the the x-axis is the number of parameters so here the larger the network is it's bad right so

**[54:30 – 54:38]** you want to to have an efficient network so you want to have fewer parameters and the y-axis is

**[54:38 – 54:45]** image net of one accuracy so basically how good the network is what is the result here higher is

**[54:45 – 54:54]** better so this means that your best networks will lie in the top left corner you want to be in the

**[54:54 – 54:59]** top left corner you want to have a small network that works very well and of course you can't have

**[54:59 – 55:04]** both at once there is a trade-off here large networks will work better than smaller networks

**[55:04 – 55:16]** that's okay so people are actually looking for is like a pareto frontier in this plot is the frontier

**[55:17 – 55:22]** where like for every size you have the best possible network and for every target quality

**[55:22 – 55:29]** you have the smallest possible network so as you can see the efficient net family pretty much succeeded

**[55:29 – 55:38]** with defining this frontier everywhere and ever since then i think maybe i've missed something it's

**[55:38 – 55:43]** not like i follow all of the papers that appear but i think there hasn't been any revolution since

**[55:43 – 55:50]** then in convolutional networks so of course in to a large extent everybody switched to transformers

**[55:50 – 55:59]** we'll discuss that of course but um but in convolutional networks i think efficient net

**[55:59 – 56:05]** is still like the best underlying architecture and for some object detection pipelines and

**[56:05 – 56:14]** segmentation pipelines efficient net is still the backbone so um so we got to uh we got to the state

**[56:14 – 56:31]** of the art basically okay um okay yeah so um i will skip batch norm because alex said that you already

**[56:31 – 56:39]** discussed it with him so let me i mean there's there's not much that i wanted to say here except

**[56:39 – 56:47]** explain how it works so here is how it works i think you you've discussed this already uh and um

**[56:47 – 56:56]** i also yeah i also have this yeah this nice picture of um different variations of batch norm so i'm not

**[56:56 – 57:03]** sure if you discussed that but usually you would have batch norm where you average over like you

**[57:03 – 57:12]** average the same feature over uh the spatial dimensions across the image and also over the

**[57:12 – 57:19]** mini-batch example but sometimes you would you would like to do something like layer norm where

**[57:19 – 57:26]** you don't average over the mini-batch and to be honest when you use layer norm usually it just

**[57:26 – 57:32]** means that your mini-batch has size one so there is no mini-batch to average over which means that

**[57:32 – 57:41]** instead you just average over the whole tensor of features so now um you you just have a global

**[57:41 – 57:51]** statistics for for for the whole layer uh layer norms layer norm is used all the time in transformers

**[57:51 – 57:58]** because transformers are big and they're usually you cannot expect to have any significant mini-batch

**[57:58 – 58:06]** so you need to uh you need to have normalization inside of of a single training sample and then

**[58:06 – 58:11]** you can actually do even if even even something more interesting here but let's let's not go into

**[58:11 – 58:19]** details and it's also a pretty big field with dozens of papers lots of results blah blah blah

**[58:19 – 58:32]** okay and with that i think i will uh i i have i'm done with um uh convolutional networks they will

**[58:33 – 58:45]** encounter more of them in uh practice in practical sessions uh and i want to go to the next or next big

**[58:45 – 58:53]** topic uh oh big in the sense of important and different but not that big i think we will either

**[58:53 – 58:59]** finish it today or maybe have a little bit left over for tomorrow so this big topic is recurrent neural

**[58:59 – 59:08]** networks and until transformers appeared they were like there were like these two main strengths of

**[59:08 – 59:16]** architectures in uh in in deep learning there were convolutional networks and there were recurrent

**[59:16 – 59:25]** networks and recurrent networks were actually designed for and used for and with uh sequences

**[59:25 – 59:40]** so what is the main idea of an rnn of a recurrent neural network well quite often you have um quite

**[59:40 – 59:51]** quite quite often your your input has the form of a sequence sorry so let me um actually yeah let

**[59:51 – 59:59]** let me go to the board and let's let's let's discuss let's first motivate um rnns and then

**[1:00:01 – 1:00:10]** discuss what they actually do so when you have uh so your your input pretty often uh when you have

**[1:00:10 – 1:00:19]** a big complicated input uh sometimes it doesn't have a natural uh way to to be represented as a

**[1:00:19 – 1:00:29]** sequence for example uh an image is not really a sequence an image is is a two-dimensional structure

**[1:00:29 – 1:00:39]** and it's not a 1d sequence of anything so for images the natural way to go would be with something like

**[1:00:39 – 1:00:51]** cnns but there are lots of types of inputs that are actually like sequences the probably the default

**[1:00:51 – 1:00:59]** example would be just time series like for example financial time series or something like this but

**[1:00:59 – 1:01:07]** there are more interesting examples too sound is a sequence right it's a sequence of ticks with

**[1:01:07 – 1:01:15]** amplitudes and yeah in classical machine learning and classical digital phone processing you would

**[1:01:15 – 1:01:22]** actually not be able to treat sound as just a sequence of amplitudes because then the sequence

**[1:01:22 – 1:01:28]** would be too long too long for classical machine learning to handle so what you would actually do

**[1:01:28 – 1:01:35]** would be to like cut it up into packets of 20-30 milliseconds or something then do feature

**[1:01:35 – 1:01:43]** extraction on the packets but then still you would have a sequence of these features feature vectors

**[1:01:43 – 1:01:52]** and of course the main example is text so text is definitely a sequence it's a sequence of tokens

**[1:01:52 – 1:01:59]** we maybe will discuss a bit tokenization in the context of transformers but text is a sequence of

**[1:01:59 – 1:02:06]** words or generally speaking tokens or whatever it definitely has one-dimensional structure right

**[1:02:06 – 1:02:16]** and when you have when you work with sequences there's a number of different things you can do

**[1:02:16 – 1:02:25]** there's a number of different types of how you can frame a problem like what kinds of questions

**[1:02:25 – 1:02:33]** you can ask so this the simplest would be if you have a sequence like a text sequence of tokens

**[1:02:34 – 1:02:42]** and then you have just a single output so this is your x and this is your y for example classification

**[1:02:42 – 1:02:51]** you have a text and you want to say oh is it what is it about what is the topic and maybe it's like a

**[1:02:51 – 1:02:58]** news stream and for every piece of news you want to say is it in sports or in politics or in science

**[1:02:58 – 1:03:11]** whatever uh maybe it's uh the other way around maybe it's like a single input and then you

**[1:03:11 – 1:03:21]** need to unroll it into a sequence in the output so this would be like sequence generation problems

**[1:03:21 – 1:03:30]** right so uh just write text uh about something for example uh here there would be a problem like

**[1:03:30 – 1:03:37]** captioning i think you'll have examples of networks for captioning like the x is an image

**[1:03:37 – 1:03:43]** and then you take this image so it's not a sequence but you want to convert it into a sequence into text

**[1:03:43 – 1:03:52]** that will explain what you see on this image right so that that's caption and then of course uh the most

**[1:03:52 – 1:03:58]** interesting for us problems would be something like sec to sex sequence to sequence problems

**[1:03:58 – 1:04:09]** where you have an input that is a sequence and then you need to have an output which is also a sequence

**[1:04:09 – 1:04:16]** so this would be problems like machine translation or something when you have text as input

**[1:04:16 – 1:04:24]** and text as output. Or in other domains or even in text too, you could have like sequence labeling

**[1:04:24 – 1:04:35]** problems, right? Sequence labeling problems where your input is a sequence and your output is a

**[1:04:35 – 1:04:44]** sequence. So this is X, this will also be X, this is Y. And your output is also a sequence, but it's

**[1:04:44 – 1:04:55]** a sequence that's aligned to the input. So for example, so like in sec to sec problems,

**[1:04:55 – 1:05:01]** in sequence to sequence problems, you read the sequence, the input sequence, you understand

**[1:05:01 – 1:05:06]** what it's about, like you read the input paragraph, you understand what it is, and then you write

**[1:05:06 – 1:05:13]** out the output, you write out the translation. In sequence labeling, in NLP, in natural language

**[1:05:13 – 1:05:19]** processing, it would be problems like part of speech tagging, for example, so you have

**[1:05:19 – 1:05:29]** a sequence of words, and you need to assign a label to every one of these words, why not,

**[1:05:30 – 1:05:39]** right, or for example, I don't know, adding subtitles to a movie, like you have this sequence,

**[1:05:39 – 1:05:45]** which is a video, oh, and by the way, I didn't mention videos here, but of course, video is

**[1:05:45 – 1:05:52]** also a sequence, right, it's a sequence of frames, and every frame is an image, but a sequence of

**[1:05:52 – 1:06:01]** images now is a video, or you can have something like putting subtitles behind the video, so for

**[1:06:01 – 1:06:09]** every frame, you would have the specific text that should be shown there, or for example, object

**[1:06:09 – 1:06:17]** tracking, in object tracking, you have a video, and you're supposed to follow an object inside this

**[1:06:17 – 1:06:22]** video, like do, for example, segmentation, but not on a single image, but on a sequence of

**[1:06:22 – 1:06:29]** images so that it tracks the same object as it moves, and yeah, I was struggling to recall

**[1:06:29 – 1:06:36]** something from computer vision, here is an example from computer vision. Okay, but whatever

**[1:06:36 – 1:06:45]** you do with that, kind of like the methods that we have, the approaches that we have like

**[1:06:45 – 1:06:52]** convolutional networks, they're not quite well suited for dealing with sequences.

**[1:06:52 – 1:07:02]** What I mean here is yes, you can do something like this. So sorry about the

**[1:07:02 – 1:07:06]** right part, look at the left part. You can do something like this. You can do a

**[1:07:06 – 1:07:14]** sliding window that goes along your input sequence and then it processes this part

**[1:07:14 – 1:07:23]** of the input sequence. And to an extent it can work. There was a time when like

**[1:07:23 – 1:07:27]** convolutional approaches to natural language processing were like rivals

**[1:07:27 – 1:07:33]** to recurrent approaches. Then of course transformers changed everything.

**[1:07:33 – 1:07:43]** But it's still like it seems to be prohibiting the most important thing.

**[1:07:43 – 1:07:52]** The most important thing is we need to have a way to recall inputs from long ago.

**[1:07:52 – 1:08:00]** Like we need to be able to have this understanding of the whole sentence and the ability to recall

**[1:08:00 – 1:08:03]** what was happening in the sequence a long time ago.

**[1:08:03 – 1:08:08]** When you read a paragraph of text, you definitely need to remember what the beginning was.

**[1:08:08 – 1:08:13]** Otherwise, the end will not make any sense.

**[1:08:13 – 1:08:21]** So how can we achieve this with a neural architecture?

**[1:08:21 – 1:08:24]** Recurrent neural networks do it like this.

**[1:08:24 – 1:08:30]** So let's say we have an input x1, x2, xt.

**[1:08:30 – 1:08:35]** Now, it's natural to think of this axis like something in time, right?

**[1:08:35 – 1:08:43]** And we will do it like this.

**[1:08:43 – 1:08:56]** We will process every x, every input in the sequence separately with this, let's say, small

**[1:08:56 – 1:09:03]** neural network, which would be called a recurrent unit.

**[1:09:03 – 1:09:12]** But this unit, let me draw it separately, this unit will have two inputs and

**[1:09:12 – 1:09:14]** one or two outputs.

**[1:09:14 – 1:09:22]** So it will have x as the input and also a hidden state, h, another input.

**[1:09:22 – 1:09:30]** And its main job will be to process this new input and update, modify the hidden state,

**[1:09:30 – 1:09:39]** so that now it captures the sequence up to and including x.

**[1:09:39 – 1:09:44]** And the assumption is that h actually captured the previous part of the sequence.

**[1:09:44 – 1:09:46]** The sequence before x.

**[1:09:46 – 1:09:55]** So formally, it just means that our recurrent unit is a function of two inputs, x and h,

**[1:09:55 – 1:09:59]** and it outputs h' and maybe it also outputs like the output.

**[1:09:59 – 1:10:02]** So at some point we do need to have the output, right?

**[1:10:02 – 1:10:07]** Sometimes it makes sense to put it like it's the output of every cell.

**[1:10:07 – 1:10:15]** Sometimes it makes sense to just use the last hidden state to do some kind of head

**[1:10:15 – 1:10:20]** and then produce the output that depends on a specific problem, that's not that important.

**[1:10:20 – 1:10:25]** What is important is that we have this hidden state, this vector of numbers basically,

**[1:10:25 – 1:10:33]** that goes along the network and is updated every time as we read another X, as we read another input.

**[1:10:33 – 1:10:47]** And we go, go, go, go, and hopefully this X is modified in such a way that it actually combines all of the relevant

**[1:10:47 – 1:10:54]** information from the sequence so that we can just look at this X and we can just say,

**[1:10:54 – 1:10:59]** all right, that is what the sequence is about, okay?

**[1:10:59 – 1:11:13]** So we need to initialize it with some kind of H0 and then here the output will be H1, H2, Ht, Ht+1 and so on, right?

**[1:11:13 – 1:11:23]** So this is a standard recurrent network.

**[1:11:23 – 1:11:34]** Like classical recurrent networks, what you would do in classical recurrent networks, how would these cells look like?

**[1:11:34 – 1:11:38]** They would be, again, some kind of simple linear things.

**[1:11:38 – 1:11:51]** So you would have your X, not here, maybe here, but what's inside this black box, what's inside this recurrent cell?

**[1:11:51 – 1:11:56]** You would have your X maybe multiplied by some matrix.

**[1:11:56 – 1:12:13]** You would have your H maybe multiplied by some other matrix, then you would add them together, and then you would, okay, H is taken, so you would pass them through some kind of activation function, okay?

**[1:12:13 – 1:12:28]** So one standard approach to making recurrent cells would be something like H prime is G of A times X plus B times H, and here G is an activation function.

**[1:12:28 – 1:12:36]** Something like hyperbolic tangent or ELU, and A and B are weight matrices, okay?

**[1:12:36 – 1:12:46]** What else can, what do I want to say here?

**[1:12:46 – 1:12:54]** Yeah, so this is how a classical recurrent network would look like, and actually it's a very old idea.

**[1:12:54 – 1:13:07]** So recurrent networks have been around since a long ago, long time ago, since the 1980s, in the second half of the 1980s,

**[1:13:07 – 1:13:11]** made actual neural networks that look like this.

**[1:13:11 – 1:13:22]** People didn't have enough compute to actually train them, we will talk in a minute about what's difficult about training recurrent networks,

**[1:13:22 – 1:13:36]** but in general, this is a very old idea that has been with us for a very long time.

**[1:13:36 – 1:13:43]** Oh yeah, and one more thing before I proceed to actually discussing the training.

**[1:13:43 – 1:13:49]** There is also one general remark about recurrent networks here,

**[1:13:49 – 1:13:54]** that goes through all possible architectures.

**[1:13:54 – 1:14:05]** The general remark is this, notice how the recurrent network,

**[1:14:05 – 1:14:07]** as I explained it to you just now,

**[1:14:07 – 1:14:11]** notice how it goes through the input in only one direction,

**[1:14:11 – 1:14:13]** left to right.

**[1:14:13 – 1:14:17]** It reads x1, then it reads x2, and so on and so on.

**[1:14:17 – 1:14:23]** And if your goal is to read the whole sentence,

**[1:14:23 – 1:14:26]** the whole input, and then say classify it

**[1:14:26 – 1:14:29]** based on the last hidden state, then probably it's okay.

**[1:14:29 – 1:14:32]** So of course you could read it left to right or right to left,

**[1:14:32 – 1:14:37]** but still you would need to read it and then make a decision.

**[1:14:37 – 1:14:42]** But if your actual problem is something like sequence labeling,

**[1:14:42 – 1:14:47]** so if you are supposed to have a yt over here,

**[1:14:47 – 1:14:51]** then it suddenly stops making sense, right?

**[1:14:51 – 1:14:57]** So I'm supposed to do, I don't know,

**[1:14:57 – 1:15:00]** I'm supposed to do part of speech tagging over here.

**[1:15:00 – 1:15:04]** So this is a word and I'm supposed to say whether it's a noun

**[1:15:04 – 1:15:09]** or a verb or an adjective or whatever.

**[1:15:09 – 1:15:14]** But if I do it with a recurrent network like this,

**[1:15:14 – 1:15:18]** it would mean that I am only allowed to look at the words

**[1:15:18 – 1:15:21]** before this one and I'm not allowed to read the sentence

**[1:15:21 – 1:15:24]** to the end before I have to make my decision,

**[1:15:24 – 1:15:28]** or I have to assign the parts of speech.

**[1:15:28 – 1:15:29]** It doesn't make any sense.

**[1:15:29 – 1:15:31]** Why should I lose information like that?

**[1:15:31 – 1:15:35]** So depending on the problem,

**[1:15:35 – 1:15:36]** but in many cases,

**[1:15:36 – 1:15:41]** it's very natural to have what are called bidirectional,

**[1:15:41 – 1:15:47]** bidirectional RNNs.

**[1:15:47 – 1:15:48]** Let me draw a picture.

**[1:15:48 – 1:15:52]** It's pretty simple, but just a little bit messier.

**[1:15:52 – 1:15:58]** x1, x2, xt, xt plus one, x capital T.

**[1:15:58 – 1:16:11]** And I still have a recurrent network that goes like this,

**[1:16:11 – 1:16:18]** and it still reads the input sequence left to right.

**[1:16:18 – 1:16:25]** But also, there is another recurrent network starting from here

**[1:16:25 – 1:16:30]** that will read the same network right to left.

**[1:16:30 – 1:16:33]** So it will, the same input right to left.

**[1:16:33 – 1:16:39]** So it will start from xt and then go over here.

**[1:16:39 – 1:16:43]** Let's say this is, okay, so let's say this is h prime t.

**[1:16:43 – 1:16:46]** So this is h prime t minus one.

**[1:16:46 – 1:16:50]** Then this becomes h prime small t.

**[1:16:50 – 1:16:59]** And it goes here and so on like this, right?

**[1:16:59 – 1:17:02]** And on every step, it's just a recurrent network

**[1:17:02 – 1:17:04]** that reads the exact same sequence,

**[1:17:04 – 1:17:06]** but in the opposite direction.

**[1:17:06 – 1:17:09]** So it goes right to left.

**[1:17:09 – 1:17:11]** And that is enough.

**[1:17:11 – 1:17:15]** Now, when we are sitting at xt,

**[1:17:15 – 1:17:19]** we have the red part, the left to right part,

**[1:17:19 – 1:17:21]** capturing the context from the left,

**[1:17:21 – 1:17:24]** capturing these guys,

**[1:17:24 – 1:17:25]** and the blue part,

**[1:17:25 – 1:17:27]** capturing context from the right,

**[1:17:27 – 1:17:28]** from these guys.

**[1:17:28 – 1:17:31]** So now we can just have

**[1:17:31 – 1:17:34]** some kind of merging of the results,

**[1:17:34 – 1:17:37]** some kind of classification head over here,

**[1:17:37 – 1:17:39]** and output yt,

**[1:17:39 – 1:17:44]** and it will actually be able to account

**[1:17:44 – 1:17:46]** for both left context and right context

**[1:17:46 – 1:17:48]** for what we had before

**[1:17:48 – 1:17:52]** and what's coming in the so-called future.

**[1:17:52 – 1:17:55]** So, basically there is no reason

**[1:17:55 – 1:18:00]** to not use a bidirectional recurrent network

**[1:18:00 – 1:18:03]** unless the problem is like,

**[1:18:03 – 1:18:06]** the problem prohibits you from doing that.

**[1:18:06 – 1:18:09]** So, for example, if you do language modeling,

**[1:18:09 – 1:18:11]** we'll talk about language models a lot later,

**[1:18:11 – 1:18:13]** but if you do language modeling,

**[1:18:13 – 1:18:16]** you're supposed to predict the next word in text.

**[1:18:16 – 1:18:18]** And when you are writing text

**[1:18:18 – 1:18:20]** and when you are predicting the next word,

**[1:18:20 – 1:18:21]** of course you don't know the word

**[1:18:21 – 1:18:23]** that will be after that, right?

**[1:18:23 – 1:18:26]** It's your job to write them.

**[1:18:26 – 1:18:31]** So in this case, if you have a recurrent language model,

**[1:18:31 – 1:18:34]** it doesn't make sense to be directional, right?

**[1:18:34 – 1:18:37]** You want to predict only from the left context.

**[1:18:37 – 1:18:41]** Or actually if you do object tracking, for example,

**[1:18:41 – 1:18:46]** I mentioned here, in object tracking too,

**[1:18:46 – 1:18:50]** when you are applying it in the real world,

**[1:18:50 – 1:18:54]** you have a stream, a video stream that comes at you,

**[1:18:54 – 1:18:58]** and maybe you can look a couple of frames ahead,

**[1:18:58 – 1:19:02]** like maybe you can delay your output for a few frames,

**[1:19:02 – 1:19:04]** but you definitely will not have access

**[1:19:04 – 1:19:06]** to like the next 10 seconds, right?

**[1:19:06 – 1:19:12]** So you will need to keep tracking online in real time

**[1:19:13 – 1:19:19]** and you definitely want to have one sided networks.

**[1:19:22 – 1:19:25]** But very often in many, many problems,

**[1:19:25 – 1:19:27]** you are allowed to look at the whole input

**[1:19:27 – 1:19:28]** before making a decision.

**[1:19:28 – 1:19:33]** For example, in all sorts of sequence to sequence problems,

**[1:19:33 – 1:19:36]** of course, you are allowed to read the whole paragraph

**[1:19:36 – 1:19:38]** before translating it, of course.

**[1:19:38 – 1:19:42]** So, okay, so these are like standard RNNs,

**[1:19:42 – 1:19:46]** standard recurrent networks, bidirectional recurrent networks.

**[1:19:46 – 1:19:48]** And now let's discuss the problems

**[1:19:48 – 1:19:50]** with the recurrent networks.

**[1:19:50 – 1:19:52]** I guess we will discuss the problems today

**[1:19:52 – 1:19:56]** and then solutions to the most important problem.

**[1:19:56 – 1:19:58]** I will not have time for that.

**[1:19:58 – 1:19:59]** That will come tomorrow.

**[1:20:01 – 1:20:03]** So what is the, like,

**[1:20:03 – 1:20:07]** how does a recurrent neural network train?

**[1:20:07 – 1:20:12]** That's actually a pretty interesting thought

**[1:20:12 – 1:20:14]** and I think it's pretty instructive

**[1:20:14 – 1:20:17]** to actually understand how it works.

**[1:20:17 – 1:20:20]** So you have this input, right?

**[1:20:20 – 1:20:22]** Just for simplicity, let's have a one-directional,

**[1:20:22 – 1:20:27]** unidirectional neural network just left to right.

**[1:20:27 – 1:20:36]** xt, xt plus one like this and we go to xt

**[1:20:36 – 1:20:42]** and let's assume that the output,

**[1:20:42 – 1:20:43]** we only need the output at the end.

**[1:20:43 – 1:20:45]** So like we read the whole sequence

**[1:20:45 – 1:20:49]** and then we let's say classify it.

**[1:20:49 – 1:20:53]** So we have some kind of head over here

**[1:20:53 – 1:20:57]** and after this head we have the loss function

**[1:20:57 – 1:21:01]** and the loss function, okay,

**[1:21:01 – 1:21:05]** so to this loss function also goes like the correct answer.

**[1:21:07 – 1:21:10]** This here gives us our predicted answer

**[1:21:10 – 1:21:14]** and then we compare it, we get a loss function as usual.

**[1:21:14 – 1:21:17]** So how do the gradients flow?

**[1:21:17 – 1:21:19]** Like where are the weights here?

**[1:21:19 – 1:21:24]** Here is the thing, whatever is the recurrent cell inside,

**[1:21:24 – 1:21:27]** maybe let's assume that it looks like this,

**[1:21:27 – 1:21:28]** doesn't really matter for us.

**[1:21:30 – 1:21:38]** But importantly, every recurrent cell here

**[1:21:38 – 1:21:40]** works in exactly the same way.

**[1:21:40 – 1:21:44]** It has the exact same weights, right?

**[1:21:44 – 1:21:47]** So actually, if you look at the computational graph

**[1:21:47 – 1:21:49]** behind what I am drawing to you,

**[1:21:49 – 1:21:53]** you have this weights of a cell,

**[1:21:53 – 1:21:57]** and these weights are copied, are shared,

**[1:21:57 – 1:22:04]** not copied, shared, across all of the recurrent cells over here, right?

**[1:22:04 – 1:22:10]** So it's the same matrix W, the same weight tensor

**[1:22:10 – 1:22:11]** that participates in every cell.

**[1:22:11 – 1:22:16]** We can't have it any other way, really,

**[1:22:16 – 1:22:20]** because we would never be able to train like separate matrices

**[1:22:20 – 1:22:25]** for going from step one to step two and from step two to step three and so on.

**[1:22:25 – 1:22:28]** Moreover, it's a pretty good thing in the sense that

**[1:22:28 – 1:22:32]** when you do it like this, you can actually process arbitrary

**[1:22:34 – 1:22:35]** sequences of arbitrary length.

**[1:22:35 – 1:22:37]** You don't care about the length anymore.

**[1:22:39 – 1:22:42]** You can just run this for however long you want.

**[1:22:42 – 1:22:44]** It's still the same W.

**[1:22:44 – 1:22:48]** But it also leads to interesting problems.

**[1:22:48 – 1:22:54]** So here is the loss function and you start computing the gradients

**[1:22:54 – 1:23:00]** of the loss function from here and as they flow through the net,

**[1:23:00 – 1:23:04]** through the sequence, they flow back, right?

**[1:23:04 – 1:23:15]** And the actual participation of this weight matrix is that every weight from here,

**[1:23:15 – 1:23:20]** so let me write it just like partial derivative,

**[1:23:20 – 1:23:25]** like dl over some specific w from here is this big sum

**[1:23:25 – 1:23:32]** because the w influences the loss along the way on every single step,

**[1:23:32 – 1:23:40]** so it's like dl over dwt, whatever that means,

**[1:23:40 – 1:23:44]** so like the part that goes over here,

**[1:23:45 – 1:23:50]** and then it's also dl over dwt minus one

**[1:23:50 – 1:23:54]** and so on, dl over dw one, so to speak,

**[1:23:54 – 1:23:56]** so they are not different weights,

**[1:23:56 – 1:24:00]** they are like different participations,

**[1:24:00 – 1:24:02]** like different edges in the computational graph

**[1:24:02 – 1:24:06]** that go out of, that grow out of dwt,

**[1:24:06 – 1:24:10]** so the actual influence of the same weight

**[1:24:10 – 1:24:17]** is done, is given many, many times along the sequence,

**[1:24:17 – 1:24:19]** for every element in the sequence,

**[1:24:19 – 1:24:23]** you again have this influence of dwt,

**[1:24:23 – 1:24:27]** so on one hand, this is good,

**[1:24:27 – 1:24:31]** this is just like, this is the same good effect

**[1:24:31 – 1:24:33]** that we had in convolutional networks,

**[1:24:33 – 1:24:38]** because in convolutional networks we had,

**[1:24:38 – 1:24:40]** how to say this,

**[1:24:40 – 1:24:42]** in convolutional networks we had this effect

**[1:24:42 – 1:24:45]** that the same weight participates in this parallel processing

**[1:24:45 – 1:24:46]** across the whole image,

**[1:24:46 – 1:24:50]** which means that you can have sparse activations,

**[1:24:50 – 1:24:51]** you can have sparse gradients,

**[1:24:51 – 1:24:53]** it's fine, it's okay,

**[1:24:54 – 1:24:55]** it's not a problem,

**[1:24:55 – 1:24:58]** because your sparse activations can,

**[1:25:01 – 1:25:03]** your sparse activations can,

**[1:25:03 – 1:25:04]** will accumulate anyway,

**[1:25:04 – 1:25:07]** so here there is a little bit of that,

**[1:25:07 – 1:25:11]** so every weight is very, very important,

**[1:25:11 – 1:25:12]** but on the other hand,

**[1:25:13 – 1:25:17]** there is a problem with this influence of W

**[1:25:17 – 1:25:18]** going through the whole sequence,

**[1:25:18 – 1:25:20]** and the problem is this,

**[1:25:20 – 1:25:24]** actually I think it's even easier to think of this problem,

**[1:25:24 – 1:25:28]** not during the backward pass like I do here,

**[1:25:28 – 1:25:31]** but just simply during the forward pass

**[1:25:31 – 1:25:33]** through the network from left to right,

**[1:25:33 – 1:25:35]** because as you go from left to right,

**[1:25:35 – 1:25:39]** also W participates every time, right,

**[1:25:39 – 1:25:45]** so let's just make things much, much, much more simple,

**[1:25:45 – 1:25:51]** let's just say that in every recurrent cell like this,

**[1:25:51 – 1:25:57]** we take the input say H and we multiply it by the matrix W,

**[1:25:57 – 1:26:01]** and this becomes H1 and then we again multiply by W,

**[1:26:01 – 1:26:03]** this becomes H2 and so on,

**[1:26:03 – 1:26:06]** this is a very simplified picture of course,

**[1:26:06 – 1:26:10]** you cannot, in reality you cannot have it without activation functions,

**[1:26:10 – 1:26:12]** in reality there is also X and so on,

**[1:26:12 – 1:26:14]** but for illustration this will be enough,

**[1:26:14 – 1:26:19]** so as you go through the recurrent network,

**[1:26:19 – 1:26:23]** your like H1 is W times H0,

**[1:26:23 – 1:26:27]** your H2 is like W times H1,

**[1:26:27 – 1:26:29]** so it's W squared times H0,

**[1:26:29 – 1:26:35]** and your HT is W to the power T times H0,

**[1:26:35 – 1:26:41]** right, and this can be a bad thing,

**[1:26:41 – 1:26:42]** this can be a problem,

**[1:26:42 – 1:26:44]** what can be the problem here?

**[1:26:44 – 1:26:50]** Well, matrices have this property called the spectral radius,

**[1:26:50 – 1:26:56]** or you can think of it as just a Provenius norm,

**[1:26:56 – 1:26:57]** doesn't matter actually,

**[1:26:58 – 1:27:00]** what the spectral radius basically tells you is

**[1:27:04 – 1:27:06]** what does the matrix when applied to a vector,

**[1:27:06 – 1:27:07]** when multiplied by a vector,

**[1:27:07 – 1:27:11]** what does the matrix do to this vector's length,

**[1:27:11 – 1:27:17]** so basically like the norm of ht,

**[1:27:17 – 1:27:21]** where I guess, not squared,

**[1:27:21 – 1:27:22]** yeah, no, not squared,

**[1:27:22 – 1:27:24]** just the length, the norm of ht,

**[1:27:24 – 1:27:27]** will be something like the spectral radius of w

**[1:27:27 – 1:27:30]** times the norm of ht minus one,

**[1:27:30 – 1:27:33]** so every time you apply a matrix,

**[1:27:33 – 1:27:38]** you are on average multiplying the length of the vector

**[1:27:38 – 1:27:39]** by some constant,

**[1:27:39 – 1:27:44]** and these constants accumulate as you see,

**[1:27:44 – 1:27:48]** so when you go to ht,

**[1:27:48 – 1:27:53]** the length of ht is like rho to the power t

**[1:27:53 – 1:27:56]** times the length of h0,

**[1:27:56 – 1:28:00]** so if you started with a vector of length one,

**[1:28:00 – 1:28:03]** which kind of makes sense,

**[1:28:03 – 1:28:07]** why did it become so big,

**[1:28:07 – 1:28:16]** so if you started with a vector of length one,

**[1:28:16 – 1:28:19]** then by the end you have a vector of this length,

**[1:28:19 – 1:28:23]** so if rho, if the spectral radius is greater than one,

**[1:28:23 – 1:28:27]** then it means that your activations just explode,

**[1:28:27 – 1:28:33]** so if rho is like even 1.1 or 1.05 or something,

**[1:28:33 – 1:28:37]** with long enough segments it will obviously go to infinity exponentially,

**[1:28:37 – 1:28:42]** and it will just explode, you will have, I don't know,

**[1:28:43 – 1:28:47]** problems like overflows in the numbers,

**[1:28:47 – 1:28:50]** and the numbers stop making any sense,

**[1:28:50 – 1:28:55]** it's like huge, huge, huge activations which don't really reflect anything,

**[1:28:55 – 1:28:58]** and the same will happen as you go back,

**[1:28:58 – 1:29:01]** because as you go back through a matrix like this,

**[1:29:01 – 1:29:02]** when you compute the gradients,

**[1:29:02 – 1:29:04]** you're also multiplying by W,

**[1:29:04 – 1:29:07]** well by W transpose, but what's the difference,

**[1:29:07 – 1:29:11]** so you're all also dependent on this kind of spectral radius,

**[1:29:11 – 1:29:14]** so you can have two kinds of problems,

**[1:29:14 – 1:29:21]** you can have exploding gradients, exploding gradients,

**[1:29:21 – 1:29:26]** when rho is greater than one and everything goes to infinity,

**[1:29:26 – 1:29:30]** or you can have vanishing gradients,

**[1:29:30 – 1:29:38]** when rho is smaller than one and it all goes to zero.

**[1:29:38 – 1:29:42]** So this is also a bad thing, right?

**[1:29:42 – 1:29:47]** So now this means that as the gradient travels along this path,

**[1:29:47 – 1:29:53]** it exponentially goes to zero on the first elements of the sequence,

**[1:29:53 – 1:29:56]** so it basically means that you cannot have any long-term memory.

**[1:29:57 – 1:30:03]** The influence of earlier parts of the sequence will just vanish completely

**[1:30:03 – 1:30:06]** and will go to zero very quickly here.

**[1:30:06 – 1:30:11]** So in exploding gradients, just everything breaks.

**[1:30:11 – 1:30:14]** In vanishing gradients, well, nothing breaks,

**[1:30:14 – 1:30:17]** but your network doesn't work as you'd like.

**[1:30:17 – 1:30:20]** So how do you solve these problems?

**[1:30:20 – 1:30:23]** Well, I will relegate vanishing gradients to tomorrow

**[1:30:23 – 1:30:25]** because this is a long discussion,

**[1:30:25 – 1:30:27]** but exploring gradients is very, very simple.

**[1:30:29 – 1:30:33]** I mean, as you go along the network,

**[1:30:33 – 1:30:39]** your problem is that your gradients start to grow uncontrollably

**[1:30:39 – 1:30:43]** and your gradient vector will be longer and longer and longer.

**[1:30:43 – 1:30:46]** Well, you can notice this, right?

**[1:30:46 – 1:30:51]** As you go along the network, your gradient becomes longer

**[1:30:51 – 1:30:53]** and you can see it as you go along the network.

**[1:30:53 – 1:30:56]** So why don't you just clip the gradient?

**[1:30:56 – 1:30:57]** And that's the answer.

**[1:30:57 – 1:31:03]** So the answer actually to the exploding gradients problem

**[1:31:03 – 1:31:07]** is not to do something smart and interesting

**[1:31:07 – 1:31:11]** to limit rho to make it equal to one or something.

**[1:31:11 – 1:31:17]** No, the answer is just let's clip the gradients.

**[1:31:19 – 1:31:24]** So like if you have a gradient which exceeds one in length,

**[1:31:24 – 1:31:27]** let's just project it back to the unit sphere.

**[1:31:27 – 1:31:29]** Let's just say, okay, so now it's too long.

**[1:31:29 – 1:31:31]** We project it back.

**[1:31:31 – 1:31:32]** That's it.

**[1:31:32 – 1:31:34]** And after the next step, it will be too long again.

**[1:31:34 – 1:31:35]** We will project it again.

**[1:31:35 – 1:31:39]** That's the only thing we do.

**[1:31:39 – 1:31:42]** So, okay, let me go through the slides.

**[1:31:42 – 1:31:45]** There's probably some illustration here.

**[1:31:45 – 1:31:46]** Okay, recurrent neural networks.

**[1:31:46 – 1:31:49]** This is what we discussed, blah, blah, blah.

**[1:31:49 – 1:31:50]** There are two problems.

**[1:31:50 – 1:31:52]** Exploding radians and radiation radians.

**[1:31:52 – 1:31:57]** And in exploding radians, we just clip it.

**[1:31:57 – 1:32:00]** So, I think this is still from Keras, not even PyTorch,

**[1:32:00 – 1:32:01]** but it doesn't matter.

**[1:32:01 – 1:32:05]** Of course, PyTorch can also clip radians for.

**[1:32:05 – 1:32:07]** Yeah, and this is the illustration I was looking for.

**[1:32:09 – 1:32:14]** There was a very nice paper 10 years ago in 2013 by Pascano

**[1:32:15 – 1:32:19]** who studied the behavior of recurrent networks.

**[1:32:19 – 1:32:22]** There are several very interesting points in there.

**[1:32:22 – 1:32:24]** I recommend you read the paper, actually.

**[1:32:25 – 1:32:33]** But it's not about any new architectures or about making it work better.

**[1:32:33 – 1:32:36]** It's about what's going on in the space of activations,

**[1:32:36 – 1:32:39]** in the space of weights, what's going on as they train and so on.

**[1:32:39 – 1:32:44]** And as for exploding radians, the picture looks like this.

**[1:32:44 – 1:32:47]** So what does it mean to have an exploding gradient, to have

**[1:32:47 – 1:32:51]** this gradient go to infinity?

**[1:32:51 – 1:32:53]** Well, if you look at the loss function,

**[1:32:55 – 1:33:01]** it basically means that you have some normal part where the gradient doesn't explode.

**[1:33:01 – 1:33:05]** And then, boom, at some point, there is just this vertical wall.

**[1:33:05 – 1:33:12]** This wall that goes to huge values very, very quickly.

**[1:33:12 – 1:33:15]** It grows very quickly. It's basically vertical.

**[1:33:15 – 1:33:19]** The gradients explode.

**[1:33:19 – 1:33:26]** So what happens is you go over here and then you bounce off this wall.

**[1:33:26 – 1:33:31]** And if you don't clip the gradients, well, you fly away God knows where.

**[1:33:31 – 1:33:35]** But if you do clip the gradients, well, you go back to this normal regime

**[1:33:35 – 1:33:40]** and you keep trudging along and you keep going in the general direction that you want.

**[1:33:40 – 1:33:48]** So clipping the gradients is not a problem from the theoretical and practical point of view.

**[1:33:48 – 1:33:52]** It's not a bad transformation to make. It's okay.

**[1:33:52 – 1:33:57]** We will still continue to go in approximately the same direction.

**[1:34:00 – 1:34:04]** And probably let me stop here.

**[1:34:04 – 1:34:09]** So we've discussed recurrent neural networks.

**[1:34:09 – 1:34:19]** We've discussed how we process sequences with these kinds of architectures.

**[1:34:19 – 1:34:21]** And we've discussed the main problem.

**[1:34:21 – 1:34:26]** The main problem is that as gradients flow and as activations flow and forward propagation,

**[1:34:27 – 1:34:30]** they either blow up or vanish.

**[1:34:30 – 1:34:36]** And it's difficult to pin the spectral radius exactly to one.

**[1:34:36 – 1:34:38]** So something needs to be done.

**[1:34:38 – 1:34:41]** And the exploding part turns out to be easy.

**[1:34:41 – 1:34:48]** But the vanishing part, as we will see tomorrow, will turn out to be pretty difficult and interesting.

**[1:34:48 – 1:34:54]** Okay, so at this point I want to stop any questions about what we discussed today.

**[1:34:54 – 1:35:03]** While you're thinking about the questions, tomorrow is lecture day.

**[1:35:03 – 1:35:07]** So please join on time.

**[1:35:07 – 1:35:14]** And then you will go back to Alex for practical sessions on Thursday.

**[1:35:14 – 1:35:22]** And yeah, I think they should be available today.

**[1:35:22 – 1:35:24]** So yeah, that's just what I wanted to say.

**[1:35:24 – 1:35:27]** On Friday, there will be a midterm presentation.

**[1:35:29 – 1:35:32]** I sent Alex a list of papers yesterday evening.

**[1:35:32 – 1:35:35]** I think he wanted to add something from himself.

**[1:35:35 – 1:35:38]** I hope it will be made available today.

**[1:35:38 – 1:35:43]** So on Friday, we will be listening to you.

**[1:35:43 – 1:35:45]** Okay.

**[1:35:45 – 1:35:46]** Thanks a lot.

**[1:35:46 – 1:35:47]** And see you tomorrow.

**[1:35:47 – 1:35:49]** Tomorrow, two lectures.

**[1:35:49 – 1:35:53]** Be fresh and ready in the morning.

**[1:35:53 – 1:35:54]** Bye-bye.

## Full text

Okay. Good day or good morning still to everyone. And welcome back to the lecture part of our class, which is being done online this year. And last time we ended on convolutional architectures and specifically on how CNNs work and what is their main good thing that they do, what is the main advantage of using convolutions. And this main advantage was, of course, to reuse the same weights over the entire input and over all of the intermediate feature tensors that you see inside the neural network that are the outputs of intermediate layers. So all of this can be processed in parallel and you can reduce the number of weights by huge factors. So before we proceed with convolutional architectures today, I understand that you already kind of started talking about convolutional architectures with Alex, and that is absolutely great because now we can skip part of this lecture and faster get to recurrent networks. I'm not sure if we get there today, but hopefully yes. But before we begin with the lecture, let me show you a couple of things. I have these standard illustrations for CNNs that I think you don't really need now because you've already had practical sessions about CNNs, but maybe I will at least mention a couple of buzzwords that you can look up. So I won't discuss all of these pictures in detail, but basically like in classical computer vision in the days before neural networks actually worked, what you would do, what you would actually do in computer vision would still be using convolutions, but you would be using like handmade convolutions. They would be called filters and sometimes people call learnable convolutions filters as well. And there were like filter banks for all kinds of purposes. And if you look at classical utilities for say image processing, like sharpen, blur, add contrast, emboss and whatever, it's all done with this kind of filters. It's all done with filters that are applied, that are basically these small matrices, just like convolutions that are applied in parallel over the image. Right. And you can do pretty complicated stuff with this. You can do, for example, edge detection, like find out where the edges of objects on the image are. Here, for example, the cat itself is pretty messy in terms of the edges. So you can see it here. There were classical filter banks like Gabor filters, where you would do something like edge detection and to be perfectly precise, you would do like discrete derivatives, finite differences in different directions. And you would do like directed edge detection. So like where is, this kind of filter fires up if there is a big difference vertically, when you go vertically from one pixel to another. And this one, if you go horizontally from one pixel to another, a lot changes. So you can actually do it this way. Okay, I have illustrations for pooling. It's not very interesting, but if you apply pooling as a filter to an actual image, of course, max pooling would look very strange because it would just clamp everything to the max brightness, so to speak, and the average pooling would look better. That's not its purpose, really. And finally, I also have illustrations on real networks. So you already know what resnets are, and these are filters, these are the convolutional, the matrices of convolutions on the first layer of ResNet 18. And you can actually see what they're trying to recognize, some fire up for some kind of lines, like diagonal lines, vertical lines, some fire for colors or color gradients or something like that. And if you actually input an image and see what exactly this filters fire on, like where do they activate a lot, then you will see that, for example, this guy is looking for something like grass trees, I suppose. It's just looking for the color green. And here it is. And I don't know what's interesting here. This guy on the right is looking for horizontal edges, or vertical edges probably, and it activates the Gaber filter where there is a horizontal line. And if then we go through the network and we map what active filters on different layers of the network do. Again we go through the ResNet 18 and look at what's happening inside. Then you will see that, here the map becomes a little bit more complicated. Let me not go into that because for layer one you can just basically see like the inputs are the pixels. Here is the filter where does it activate, here. Then on subsequent layers as you understand now, there is not such a direct correspondence between pixels and outputs. Because every picture has a reception field. You can find which part of the image it's looking at. But what exact pixels are contributing the most, that requires a little bit of math. So I will skip that, but you can actually look at what parts of the image even top layer features fire up for. And you can see that, for example, in ResNet-18, the second layer fires for some high-frequency stuff in the image. Throughout the whole image, but just some kind of stripes or something and edges and stuff like that. And then we go for more salient objects, right? So here, for example, there is some filter that fires for the eyes and the tips of the ears, something like that. And then when we go to later layers, we become more and more semantic. So on these pictures, I don't think that clear. They're very blurry and TresNet-18 is not a very good network, but still you can see that kind of there is a filter for the ears, there is a filter for the head as a whole. Or you can actually go back from a deep feature back to the pixel level. Sorry, I didn't explain it well, but this was on the level of the feature maps. I mean, it becomes blurry and blur, there is less and less geometry, it just makes less sense. But you can also, with this map that I mentioned, map it back to the original image, to the filters of the original image. And you can see approximately, now it's not precise, but you can see approximately what it fires on. And it's pretty interesting, right? So, in ResNet 3.10, on a deep layer, you can find the feature that selects most for the cats. So, what it means to be cat-selective, it means that ResNet was trained to distinguish classes from either ImageNet, like cats and dogs. You can find which feature gives you the most information regarding this specific class, which feature correlates, whose activation correlates the best with this specific class. And if you look at the cat-selective feature, and you input an image which is half cat, half dog, like this one, I just merged two together, that's it. Then, you will see that it fires up on the cat, and the dog-selective feature, indeed, fires up on the dog, approximately. So, this kind of works. And also, I wanted to mention, again, I don't want to spend time discussing the math, but there are also methods for more detailed interpretation of what the network actually is doing. So, there is, for example, GradCam, it's not the only one, but it's a good one, and if you can run it for the network output, like the predicted class, a single class, again, recall that the network's output is this set of probabilities. So, every class in the classification network is a separate output, which is convenient in cases like this, because we can actually look at specific outputs, and, for example, the Egyptian cat output responds to this and has obtained the value that it has due to pixels like this. So, it's not yet an attention mechanism, we'll get to those tomorrow, but it's kind of an interpretation of why exactly, due to which pixels the network chose this value for this output. And sure enough, you can run it for different classes. For example, again, if you can't get the cat and the dog, then the Egyptian cat output will look at the cat, and the Blenheim-Spaniel output will look at the dog, that's it. Okay, so that was a brief remark about what we will not discuss in more detail. So, about the basics of convolutional networks, what they are looking at. Now, let's get to the main part, I think, of today, and the main part is important convolutional architectures, and hopefully this will be only the first main part, because some of the most important stuff you have already discussed with Alex, right? So, the most important convolutional architecture in history was, of course, AlexNet, and I hope that Alex discussed his architecture with you, and if not, I guess by now we can skip it. So, it was like the first convolutional network that actually worked, that beat every competing method completely on the ImageNet recognition, large-scale visual recognition competition, and that defines the state-of-the-art in an extraordinarily big margin. So, in 2011 or 2012, when it was participating in this competition, the results were like the error rate for all of the rest of the methods was like 22%, 23%, something like this, and the error rate for AlexNet was like 13%. So, it was a huge jump, a huge gap, and of course, next year, the whole leaderboard was only convolutional networks. Nobody ever went back to classical computer vision since AlexNet. This was the revolution that happened in image classes. And technically, and in terms of specific ideas, what is most interesting in AlexNet are two things. It's a pretty standard convolutional architecture, but you can see first that it's split in two. And that was the first actual industrial scale instance of model parallelization. So this is very important. We won't have time to go into more details. So now is a good time to just mention it. In deep learning, you have huge models, you have huge data sets. So of course you need to parallelize. You need to make use of multiple GPUs if you have multiple GPUs. And there are two main ways that you can do it. You can do what is called data parallelization. Data parallelization is when you have one mini-batch in GPU 1, another mini-batch in GPU 2, another mini-batch in GPU 3. You run them all in parallel and then you collect the results and you do a single update based on the weight updates from all of the GPUs. So you don't have to change anything in your implementation. The network works just as usual. The only difference is that since now you have multiple GPUs in parallel, you can collect... Basically, you're just increasing the mini-batch size for yourself. So what you're actually doing is you're expanding the size of... You're expanding your mini-batch size by splitting the mini-batch into different GPUs. That's data parallelization. There's a lot of work on that because you can do it in many different smart and interesting ways. But the basic idea is very simple. Model parallelization is more complicated. In model parallelization, the assumption is that your model does not fit on your GPU. And if your model does not fit on your GPU, what can you do? Well, you need to put half of your model on one GPU and another half on the other. And that's exactly what AlexNet was doing back in 2011 already. So 2012 was the paper, but the actual network was in 2011. And, of course, that was like a huge feat of engineering back in 2011. Alex Krajewski was a wonderful programmer and he actually implemented all of this by hand. These days, of course, we don't need to implement anything by hand. And even our cloud codes do not need to implement this by hand. In PyTorch, you can just say, well, I want this weight matrix to live on this GPU and that weight matrix to live on that GPU, and PyTorch will just handle the rest automatically. But still, when you design a parallel network like this, a network that spans multiple GPUs, you want to minimize communication across the GPUs because, of course, it will be slower than inside one GPU. So here, for example, you can see that these guys talk to the two strands, the two GPUs talk to each other over here and then talk to each other at the very end. There are only two places where they actually exchange information. Anyway, AlexNet was the breakthrough. People like to talk of like the AlexNet moment or something. But then, of course, the field exploded. Everybody wanted to do convolutional networks. And it turned out that you can actually improve convolutional networks quite a lot with relatively simple ideas. So some of the most important ideas we already discussed with Alex, not Krzyzewski, but Alex Davidov. And the first idea is VGG, and VGG is the reason why AlexNet still had 11 by 11 convolutions on the first layer. But now you will never see 11 by 11 convolutions, you will only see 3 by 3 convolutions and maybe 5 by 5 sometimes. Because with the VGG idea, you can represent large convolutions as compositions of small convolutions. And this is actually a great way to do things because it's like a convolution inside a convolution, right? And this convolution inside a convolution reduces the number of weights further. I think you did this with Alex, this calculations of how many weights. And it serves as kind of additional structural regularization. Again, you are saying to the network, you can process different parts of the input in the same way. And usually it just works better. So the second idea that you also discussed with Alex, as far as he told me, is Inception and Googling it. And generally, like the idea that is known as network and network. So I started talking about convolutional networks with you with this. I won't switch back to them, but you remember the slides with this boy on the toy horse and all of this. And right there, there were tiles being processed by what I called small neural networks on this, what was called small neural network on these pictures. And since then, when we actually implemented this small neural networks, they were always like the simplest possible neural networks. We were always talking only about a single matrix that processes the whole input and doesn't care and doesn't do anything interesting. Just put everything together, throw it to a single vector of numbers, multiply by this weight matrix, here is the output. But you don't have to limit yourself to that, right? You don't have to do that, right? You can do more interesting things and this inception trick and basically these ideas of network and network are exactly this. You can replace this simple convolution with a far more complicated approach, far more complicated network. When you do that, you still have exactly the same idea of processing the tiles in parallel with the same small network. It's only that the small network is now more interesting. So, yeah, I think you've discussed inception, I won't repeat that. What I want to note here is that when you look at these inception units, when you look at this small network, so to speak, you see usually multiple parallel threads of processing. And that is not a coincidence and we will talk more about that today. OK, so third, the most important idea of all of this, the idea that will be with us throughout the whole deep learning. It will be used in transformers, it's used everywhere. The idea of residual connections and thus resonance. Again, Alex said that you already discussed it, so I will mostly skip. Basically, the idea is like this. I apologize, I keep forgetting to redo the Russian picture. But anyway, this is input, so the input is x, then f of x, then the next layer is like this, f of x. And the ResNet problem is that when f of x sort of drains and saturates, the gradient will go to zero. This layer will not want to change anymore. And when it doesn't want to change anymore, that's okay for the layer. But if you didn't have a residual connection, it would mean that nothing below that layer will ever learn. Because everything below the layer receives gradients through this layer multiplied by its derivatives. And if those go to zero, then nothing changes below that. That's a bad thing. So what we do is we use residual connections like here. We do a connection that goes around. Here we have something very simple and specifically just a plus. And now our result is f of x plus xk. And now f of x can saturate all at once. The derivative can go to zero. That's fine. If it goes to zero, then the gradient just goes to, the matrix of derivatives just goes to an identity matrix. The gradient will just flow through this layer and, not through, but flow around this layer and continue to the bottom layers. And as soon as resnets were introduced, Kamin He, this guy who invented resnets and he's actually a very cool researcher with a lot of great papers, Kamin He called it the revolution of depth. And indeed it was. So when residual connections were introduced and were used in deep convolutional architectures, you immediately could train networks with hundreds and hundreds of layers. So like AlexNet had eight trainable layers. We don't count pooling here. VGG had 19 layers. GoogleNet with the first inception units had 22 layers and resnet next year had like 150 layers. And there was totally no problem to, there was no problem to grow further. There was no problem to increase the depth further. You can do resnet 200, 300, 500, 2000 and it will still train. It will still be fine. The problem only is that it will stop improving, right? So it will still be trained and will still do the job. But if you increase your network by another factor of two and the results don't improve, well, maybe you shouldn't be doing that, right? So it only makes sense to add new layers while they still help. So actual resnets go up to about 200 layers and then I guess they run out of steam. Okay. So as far as I understood Alex, if I understood him correctly, this is approximately where you stopped and let me complete this arc. Let me continue this discussion of different convolutional ideas, of ideas that kind of define convolutional architectures with our next, with our first detailed point, point one, which is the bottleneck layers, bottlenecks and an idea that is usually called split transform merge. Sorry, I'm not yet used to writing here. Maybe I hope. Split transform merge. So what's the bottleneck idea? Well, actually, you can look at, for example, the VGG idea as another way to reduce the number of weights, right? Because you replace big convolution which has n squared weights with a sequence of small convolutions which have linear and n weights, and that's great. So even though convolutions by themselves already start off by saving a huge number of weights, you can actually try to do better. You can actually try to reduce even further. And let's just step back, look at a convolutional layer and see where and what we can improve. So a standard convolutional layer will have some 3D tensor as the input. So the input will be of size. OK, so let's actually say that this is already the window that I cut out because I never want to care about the full input. It's always just copied over. So this is already the cut out window and it has like depth D, width W and height H. Then we go to the convolutional layer. And as a result of the convolutional layer, we get a single vector of features of size T prime. So a standard convolutional layer will have the matrix of weights of dimensions D times W times H times D prime. And as we discussed, it's much, much, much better than if we tried to do it with a fully connected layer or something else. But still, it can actually add up. It can grow pretty quickly. So if, for example, like D is something like 256, which is pretty standard inside a big convolutional architecture, and D prime is also something like 256, then even, I mean, the VTG idea lets you keep W and H small. But still, in here, you have like these tensor of weights, 256 by 3 by 3 by 256. And that's a pretty big number, right? So that's like, oh, I don't know, 2500 times another 25. Okay, I embedded math at this level, but you can figure it out. What's 25 squared? It's 725, right? So it's 75K, I guess. No, no, it's 750K, 700K, something like this, right? Yeah, 250 by 250 is 75K times 9, something like that, something like 700K. Which is quite a lot, right? So how can we reduce this? What is the problem that we might somehow solve here? Where can we save on these weights? The bottleneck idea is actually pretty straightforward and it goes like this. What if instead of getting the full 256 by 256 multiplied by 9, what if we actually compressed the features down and only then did the convolution? So here is how it would work. You have your input and your input is long. It's like E times W times H. But first, you would run it through a one-by-one convolution. I hope you discussed those with Alex. A one-by-one convolution just by definition doesn't do anything geometric. It just takes one feature vector here and rearranges it. It does something interesting inside the feature vector. But it doesn't do anything to the geometry, to the receptive fields, to anything like that. And what if we use this one-by-one convolution to actually reduce the depth, to reduce the number of channels? So that now we would have something like d double prime times w times h with d double prime small. So if I had d like 256 maybe d double prime is like 32. And then I would have my true convolution here and it would give me a short vector. I would put like d triple prime here but okay let's just say it's d double prime too. And then I would have another one by one convolution if I do want to have like d prime at the output. Then I would have to stretch back this feature vector to size d prime. So the convolution itself, so the one by one convolution now has like d times one times one times d double prime weights. This is one by one convolution. This convolution has how many weights? d double prime times w times h times d double prime. And also this convolution is d double prime times one times one times d prime. So you can kind of get a feeling for what's happening here, right? I avoid multiplying 256 squared by nine. And actually I avoid 256 squared completely, right? There's still a 9 in there. It still gets multiplied by something, but that something is much smaller than 256. So let's plug in the numbers. In this example, it would be like 256 times 32 plus this 256 times 9 times... Oh, sorry, sorry, sorry, sorry. Plus 32 times 9 times 32, right? Plus, again, 32 times 256. So even though I have three convolutions instead of one now, I still save a lot of weights. So let me pull 256 out. It will be 32 plus... What, now I have to take a 4 out of this. So now I have to take an 8 out of this. So 4 is left 9 by 4 and another 32. So with 32 and 32, 64 and 36, exactly 100. That will be like 256 times 100, right? And over there, I had 256 times 2,500, right? Times 256 times 9. So this is about, in our simple example, that's about like 25x smaller, 25x smaller. And we have saved a lot of weights, okay? A lot of weights. Well, but now when you look at this idea, something should feel funny to you about it. Something should not sit right with you about this idea. And what is that? What is the problem here? Oh, what did I just do? I took a vector of 256, a long vector, a vector of 256 features. So in the input, every pixel, every feature map, every feature vector was long and had a lot of information. It was like 256 numbers. And then I just compressed it down to 32 numbers. Then I did interesting stuff on 32 numbers. And then somehow I decompressed it back to 256. But that decompression cannot restore the information that I lost. So what I'm doing here is I'm taking a long and interesting vector. So geometrically speaking, I'm leaving in the feature space of a high dimension. Like 256. But inside this feature space, I am picking a specific subspace, a specific projection of this much smaller dimension. So I am reducing my features that are long and interesting and complicated down to a much simpler thing, to a much smaller dimension. I'm just taking one view of these things. And that doesn't sound that bad, but if you think about it, it doesn't make any sense to actually do what I am proposing here. Because if I just compress down 256 numbers worth of information to 32, why on earth do I need 256 numbers at all? I mean, this is happening inside a network that I am designing myself. These 256 numbers did not grow on a tree. They came from an earlier layer. So if all I wanted to do was this, then I would just replace D by D double prime. I would just say, okay, so let the previous layer produce 32 features. Why do I need this artificial compression decompression stuff? And that would save even more weights and that would be even better, right? So the way I told you this bottleneck idea, it doesn't work by itself. And the editor doesn't and never appears like that. But it suddenly starts to make a lot of sense if you do it not once, but several times. So how it actually gets used is you start with this input tensor, D times W times H, and then you do several copies of this processing pipelines. Like you have one by one then convolution, you have one by one then convolution, and so on. And then you somehow unite the results, you combine the results. So for example, in this case, it could be like this. I have D of 256, and out here I have a vector of size 32. So how many vectors of size 32 I need to have a new vector of size 3256? Well, eight of them, right? So why don't I just copy this eight times and concatenate the results like this? This is a pretty standard way of doing this. So I do my processing eight separate times. Notice that even though it's the same picture, it's the same structure of processing, the actual processing will be very different, right? Because these strands, these pathways will learn different weights. They will do different things. You need to break the symmetry and initialization, and then they will just happily go to different minima and to implement different ideas. And yes, now I'm not saving 25x weights, because now to actually go from 256 to 256, I need to copy this eight times, right? So now instead of saving 25x, I'm only saving 4x weights. But it's still a pretty big saving, right? And actually it turns out that in practice, it's a pretty good idea. So what we are actually doing is in this huge space, we are choosing not one projection, not one way to reduce the dimension, but we are choosing multiple different ways, multiple different viewpoints on these complicated features. And so I look at it from this side and then I look at it from this side and then I look at it from that side and it's like different projections, different snapshots of this same big space of features. And when you actually do that, it's pretty interesting. And now it's not just usually you can train it to not lose any important information, but even better, you can actually expect it to do even better than if you just process this whole 256 thing. So it's actually, and I cannot get into full detail to explain why, but it's actually a good idea to even do lots of random projections of your high-dimensional object. Even that is usually a good idea. And here the projections are not random. Here the projections are learned, and they are learned to be useful, which is even better. So this is usually called split, transform, merge for obvious reasons. First you split, then you transform, then you merge. And it's a pretty standard idea in convolutional architectures. So I guess that's the important thing that I wanted to say. Let's go back to the slides. Yes, but here is an example in ResNext. Kind of outdated now. It was 10 years ago, but a perfect example of just an idea like this. You split the 256 into 32 paths of four. So it's like an extreme projection, but several extreme projections, and that's better. So what else can I say about these classical convolutional architectures? Well, I probably should mention this line of inception networks and inception ResNet networks. I'm not sure if you discussed them with Alex, you discussed inception, you discussed ResNet, but what about the combination? And basically, the progression of these networks, they are a pretty important family of networks. They were, like for a long time, the best available backbones for all sorts of computer vision tasks. When we get to object detection and segmentation, we will discuss how, for example, we will discuss how when you do an object detection architecture or a segmentation architecture, you can't really expect to train it from scratch. So there will be not enough labeled data to train it from scratch because labeling is very difficult for these complicated computer vision tasks. So what you actually do in practice is you take what is called the backbone, you take a network trained on ImageNet, for example, to just classify stuff, then you cut off its head and you use the rest of the network as a feature extractor. Maybe you find Unity a little, maybe even not, and this Inception ResNet family was one of the most influential, one of the best families of these backbones back in 2016. And what is its main idea, of course, doesn't make sense to learn them in big detail, but its main idea was that you do this Inception trip, you do this network and network thing, you replace, you do better and better basic blocks that process the inputs, like the small neural networks. And from version to version, they just invented better and better such basic blocks, basically, that was the main component of progress And another interesting component of progress was that they also replaced pooling layers with blocks like this, and I think I mentioned this last time, if you want to reduce your dimension, if you want to reduce from 256 by 256 image down to 128 by 128 image, yeah, you can do max pooling. But it's even better to have another network and network thing, another layer that can be trained and that can do more interesting stuff. Only that you tune this, you compose this layer in such a way that the output becomes smaller. Usually with strides, with strided convolutions that just reduce the geometry, that's what they do. So over here, they indeed, in later inception networks, they indeed had this reduction blocks that can have pooling inside. But it's again this kind of transfer, split, then merge idea. So there are several parallel lines of processing here that do different things and then their results are merged together in some way. So this has been an influential idea in convolutional architecture. Then you get residual connections and you get Inception ResNet, that's it. I won't go into more details, but basically Inception ResNet V2 was a very influential, very interesting backbone that was used very widely. Okay, so I will probably keep the rest mostly. There were some more ideas on how to further reduce the size of the network and also to reduce the number of layers. And let me not go into these ideas in detail, but this basic trade-off, not trade-off, but this basic, there are basically two different things that you want to optimize. One is memory. You want to have a smaller network if you want to, for example, feed to a mobile device or something. And that means reduce the number of weights, because basically the size of the network is the number of weights, that's it. And then there is also another dimension, which is latency, which is how quickly the network will actually operate. So in computer vision, you often care about latency. For example, if you do something like tracking on a surveillance camera, then of course you need it to work in real time, because the surveillance camera will work like 24/7, and of course you can't lag behind the video stream while you are processing a continuous video stream. So you definitely want your tracking or whatever you do with this stream, you definitely want it to work in like 30 frames per second at least, and preferably 60. So latency is also important, and what I wanted to just note here is that there are two different things. I mean, to some extent, it's true that if you have a smaller network, it will run faster. But actually, the latency depends on the number of layers, because once the network fits into your GPU, the rest is more or less unparalleled inside the layer. And what actually matters is how many steps you make. So every step, okay, it will also depend on, say, the intermediate representation size. Yes, of course, it will be slower if you have more weights inside every layer. But the most important component is the number of layers. So these two things make networks faster or make them smaller. They don't conflict that much, but they are two different objectives. Just wanted to mention that. And yeah, let's keep SqueezeNet. Nothing new for us here. Let's keep MobileNet here. The whole thing was indeed to put computer vision on mobile devices. And finally, I think what I want to end this discussion with. Finally, the family of CNNs that kind of topped this progress of CNN architectures. I mean, probably there was something afterwards, but mostly even now everybody just uses this. The line of networks that proved to be the best were EfficientNet. And again, I don't want to go into too much detail, but it's again the same story that we saw with activation functions. And then I mentioned that we saw a similar story with gradient descent algorithms, but gradient descent algorithms we didn't discuss that. And here in EfficientNet, the architecture was actually found automatically with a big neural architecture search. So what they did, and again, not too much detail, but just the basic idea, what they did was they looked at how you scale a convolutional network. Like when you increase the network, in what ways can you increase the network? Like what are the different dimensions that you can change? What are the knobs that you can rotate and tweak in order to change what the network does? and it turns out there are quite a few knobs right so you can change the depth of the network obviously you can change so you can add more layers you can change the width of the network you can add more depth to it you can add so sorry we usually call it depth but yeah inefficient net depth is the number of layers which also is very reasonable to call that and width is like the the the length of the feature vector so you can make the network wider by adding more features it also allows you to make the network smarter but spending more weights and also you can do something like higher resolution so you can increase the the number of pixels in the input so to speak and then what they did was they just rolled down some very simple formulas like okay so as i increase the network i increase the depth the width and the resolution how does the total size of the network change well you multiply them all together you get like the product of three numbers and it goes into the exponent and this is the number of weights okay so what are we looking for we are looking for the the perfect balance between these three numbers basically the idea is if your depth grows exponentially with exponent alpha your width grows exponentially with exponent beta your resolution grows exponentially with exponent gamma then there is like a natural relation between alpha beta and gamma but then you need to actually find the best values of those so that's what they did then they run like huge evolutionary search to find this best combinations of hyperparameters and they were successful they were pretty successful and this family of efficient this efficient net family as you can see here basically just defined the state of the art right defined across the whole field so we will see plots like this later in for other computer vision tasks here it also is pretty i think instructive to look at how this plot works it's uh there are two axes right one of the the x-axis is the number of parameters so here the larger the network is it's bad right so you want to to have an efficient network so you want to have fewer parameters and the y-axis is image net of one accuracy so basically how good the network is what is the result here higher is better so this means that your best networks will lie in the top left corner you want to be in the top left corner you want to have a small network that works very well and of course you can't have both at once there is a trade-off here large networks will work better than smaller networks that's okay so people are actually looking for is like a pareto frontier in this plot is the frontier where like for every size you have the best possible network and for every target quality you have the smallest possible network so as you can see the efficient net family pretty much succeeded with defining this frontier everywhere and ever since then i think maybe i've missed something it's not like i follow all of the papers that appear but i think there hasn't been any revolution since then in convolutional networks so of course in to a large extent everybody switched to transformers we'll discuss that of course but um but in convolutional networks i think efficient net is still like the best underlying architecture and for some object detection pipelines and segmentation pipelines efficient net is still the backbone so um so we got to uh we got to the state of the art basically okay um okay yeah so um i will skip batch norm because alex said that you already discussed it with him so let me i mean there's there's not much that i wanted to say here except explain how it works so here is how it works i think you you've discussed this already uh and um i also yeah i also have this yeah this nice picture of um different variations of batch norm so i'm not sure if you discussed that but usually you would have batch norm where you average over like you average the same feature over uh the spatial dimensions across the image and also over the mini-batch example but sometimes you would you would like to do something like layer norm where you don't average over the mini-batch and to be honest when you use layer norm usually it just means that your mini-batch has size one so there is no mini-batch to average over which means that instead you just average over the whole tensor of features so now um you you just have a global statistics for for for the whole layer uh layer norms layer norm is used all the time in transformers because transformers are big and they're usually you cannot expect to have any significant mini-batch so you need to uh you need to have normalization inside of of a single training sample and then you can actually do even if even even something more interesting here but let's let's not go into details and it's also a pretty big field with dozens of papers lots of results blah blah blah okay and with that i think i will uh i i have i'm done with um uh convolutional networks they will encounter more of them in uh practice in practical sessions uh and i want to go to the next or next big topic uh oh big in the sense of important and different but not that big i think we will either finish it today or maybe have a little bit left over for tomorrow so this big topic is recurrent neural networks and until transformers appeared they were like there were like these two main strengths of architectures in uh in in deep learning there were convolutional networks and there were recurrent networks and recurrent networks were actually designed for and used for and with uh sequences so what is the main idea of an rnn of a recurrent neural network well quite often you have um quite quite quite often your your input has the form of a sequence sorry so let me um actually yeah let let me go to the board and let's let's let's discuss let's first motivate um rnns and then discuss what they actually do so when you have uh so your your input pretty often uh when you have a big complicated input uh sometimes it doesn't have a natural uh way to to be represented as a sequence for example uh an image is not really a sequence an image is is a two-dimensional structure and it's not a 1d sequence of anything so for images the natural way to go would be with something like cnns but there are lots of types of inputs that are actually like sequences the probably the default example would be just time series like for example financial time series or something like this but there are more interesting examples too sound is a sequence right it's a sequence of ticks with amplitudes and yeah in classical machine learning and classical digital phone processing you would actually not be able to treat sound as just a sequence of amplitudes because then the sequence would be too long too long for classical machine learning to handle so what you would actually do would be to like cut it up into packets of 20-30 milliseconds or something then do feature extraction on the packets but then still you would have a sequence of these features feature vectors and of course the main example is text so text is definitely a sequence it's a sequence of tokens we maybe will discuss a bit tokenization in the context of transformers but text is a sequence of words or generally speaking tokens or whatever it definitely has one-dimensional structure right and when you have when you work with sequences there's a number of different things you can do there's a number of different types of how you can frame a problem like what kinds of questions you can ask so this the simplest would be if you have a sequence like a text sequence of tokens and then you have just a single output so this is your x and this is your y for example classification you have a text and you want to say oh is it what is it about what is the topic and maybe it's like a news stream and for every piece of news you want to say is it in sports or in politics or in science whatever uh maybe it's uh the other way around maybe it's like a single input and then you need to unroll it into a sequence in the output so this would be like sequence generation problems right so uh just write text uh about something for example uh here there would be a problem like captioning i think you'll have examples of networks for captioning like the x is an image and then you take this image so it's not a sequence but you want to convert it into a sequence into text that will explain what you see on this image right so that that's caption and then of course uh the most interesting for us problems would be something like sec to sex sequence to sequence problems where you have an input that is a sequence and then you need to have an output which is also a sequence so this would be problems like machine translation or something when you have text as input and text as output. Or in other domains or even in text too, you could have like sequence labeling problems, right? Sequence labeling problems where your input is a sequence and your output is a sequence. So this is X, this will also be X, this is Y. And your output is also a sequence, but it's a sequence that's aligned to the input. So for example, so like in sec to sec problems, in sequence to sequence problems, you read the sequence, the input sequence, you understand what it's about, like you read the input paragraph, you understand what it is, and then you write out the output, you write out the translation. In sequence labeling, in NLP, in natural language processing, it would be problems like part of speech tagging, for example, so you have a sequence of words, and you need to assign a label to every one of these words, why not, right, or for example, I don't know, adding subtitles to a movie, like you have this sequence, which is a video, oh, and by the way, I didn't mention videos here, but of course, video is also a sequence, right, it's a sequence of frames, and every frame is an image, but a sequence of images now is a video, or you can have something like putting subtitles behind the video, so for every frame, you would have the specific text that should be shown there, or for example, object tracking, in object tracking, you have a video, and you're supposed to follow an object inside this video, like do, for example, segmentation, but not on a single image, but on a sequence of images so that it tracks the same object as it moves, and yeah, I was struggling to recall something from computer vision, here is an example from computer vision. Okay, but whatever you do with that, kind of like the methods that we have, the approaches that we have like convolutional networks, they're not quite well suited for dealing with sequences. What I mean here is yes, you can do something like this. So sorry about the right part, look at the left part. You can do something like this. You can do a sliding window that goes along your input sequence and then it processes this part of the input sequence. And to an extent it can work. There was a time when like convolutional approaches to natural language processing were like rivals to recurrent approaches. Then of course transformers changed everything. But it's still like it seems to be prohibiting the most important thing. The most important thing is we need to have a way to recall inputs from long ago. Like we need to be able to have this understanding of the whole sentence and the ability to recall what was happening in the sequence a long time ago. When you read a paragraph of text, you definitely need to remember what the beginning was. Otherwise, the end will not make any sense. So how can we achieve this with a neural architecture? Recurrent neural networks do it like this. So let's say we have an input x1, x2, xt. Now, it's natural to think of this axis like something in time, right? And we will do it like this. We will process every x, every input in the sequence separately with this, let's say, small neural network, which would be called a recurrent unit. But this unit, let me draw it separately, this unit will have two inputs and one or two outputs. So it will have x as the input and also a hidden state, h, another input. And its main job will be to process this new input and update, modify the hidden state, so that now it captures the sequence up to and including x. And the assumption is that h actually captured the previous part of the sequence. The sequence before x. So formally, it just means that our recurrent unit is a function of two inputs, x and h, and it outputs h' and maybe it also outputs like the output. So at some point we do need to have the output, right? Sometimes it makes sense to put it like it's the output of every cell. Sometimes it makes sense to just use the last hidden state to do some kind of head and then produce the output that depends on a specific problem, that's not that important. What is important is that we have this hidden state, this vector of numbers basically, that goes along the network and is updated every time as we read another X, as we read another input. And we go, go, go, go, and hopefully this X is modified in such a way that it actually combines all of the relevant information from the sequence so that we can just look at this X and we can just say, all right, that is what the sequence is about, okay? So we need to initialize it with some kind of H0 and then here the output will be H1, H2, Ht, Ht+1 and so on, right? So this is a standard recurrent network. Like classical recurrent networks, what you would do in classical recurrent networks, how would these cells look like? They would be, again, some kind of simple linear things. So you would have your X, not here, maybe here, but what's inside this black box, what's inside this recurrent cell? You would have your X maybe multiplied by some matrix. You would have your H maybe multiplied by some other matrix, then you would add them together, and then you would, okay, H is taken, so you would pass them through some kind of activation function, okay? So one standard approach to making recurrent cells would be something like H prime is G of A times X plus B times H, and here G is an activation function. Something like hyperbolic tangent or ELU, and A and B are weight matrices, okay? What else can, what do I want to say here? Yeah, so this is how a classical recurrent network would look like, and actually it's a very old idea. So recurrent networks have been around since a long ago, long time ago, since the 1980s, in the second half of the 1980s, made actual neural networks that look like this. People didn't have enough compute to actually train them, we will talk in a minute about what's difficult about training recurrent networks, but in general, this is a very old idea that has been with us for a very long time. Oh yeah, and one more thing before I proceed to actually discussing the training. There is also one general remark about recurrent networks here, that goes through all possible architectures. The general remark is this, notice how the recurrent network, as I explained it to you just now, notice how it goes through the input in only one direction, left to right. It reads x1, then it reads x2, and so on and so on. And if your goal is to read the whole sentence, the whole input, and then say classify it based on the last hidden state, then probably it's okay. So of course you could read it left to right or right to left, but still you would need to read it and then make a decision. But if your actual problem is something like sequence labeling, so if you are supposed to have a yt over here, then it suddenly stops making sense, right? So I'm supposed to do, I don't know, I'm supposed to do part of speech tagging over here. So this is a word and I'm supposed to say whether it's a noun or a verb or an adjective or whatever. But if I do it with a recurrent network like this, it would mean that I am only allowed to look at the words before this one and I'm not allowed to read the sentence to the end before I have to make my decision, or I have to assign the parts of speech. It doesn't make any sense. Why should I lose information like that? So depending on the problem, but in many cases, it's very natural to have what are called bidirectional, bidirectional RNNs. Let me draw a picture. It's pretty simple, but just a little bit messier. x1, x2, xt, xt plus one, x capital T. And I still have a recurrent network that goes like this, and it still reads the input sequence left to right. But also, there is another recurrent network starting from here that will read the same network right to left. So it will, the same input right to left. So it will start from xt and then go over here. Let's say this is, okay, so let's say this is h prime t. So this is h prime t minus one. Then this becomes h prime small t. And it goes here and so on like this, right? And on every step, it's just a recurrent network that reads the exact same sequence, but in the opposite direction. So it goes right to left. And that is enough. Now, when we are sitting at xt, we have the red part, the left to right part, capturing the context from the left, capturing these guys, and the blue part, capturing context from the right, from these guys. So now we can just have some kind of merging of the results, some kind of classification head over here, and output yt, and it will actually be able to account for both left context and right context for what we had before and what's coming in the so-called future. So, basically there is no reason to not use a bidirectional recurrent network unless the problem is like, the problem prohibits you from doing that. So, for example, if you do language modeling, we'll talk about language models a lot later, but if you do language modeling, you're supposed to predict the next word in text. And when you are writing text and when you are predicting the next word, of course you don't know the word that will be after that, right? It's your job to write them. So in this case, if you have a recurrent language model, it doesn't make sense to be directional, right? You want to predict only from the left context. Or actually if you do object tracking, for example, I mentioned here, in object tracking too, when you are applying it in the real world, you have a stream, a video stream that comes at you, and maybe you can look a couple of frames ahead, like maybe you can delay your output for a few frames, but you definitely will not have access to like the next 10 seconds, right? So you will need to keep tracking online in real time and you definitely want to have one sided networks. But very often in many, many problems, you are allowed to look at the whole input before making a decision. For example, in all sorts of sequence to sequence problems, of course, you are allowed to read the whole paragraph before translating it, of course. So, okay, so these are like standard RNNs, standard recurrent networks, bidirectional recurrent networks. And now let's discuss the problems with the recurrent networks. I guess we will discuss the problems today and then solutions to the most important problem. I will not have time for that. That will come tomorrow. So what is the, like, how does a recurrent neural network train? That's actually a pretty interesting thought and I think it's pretty instructive to actually understand how it works. So you have this input, right? Just for simplicity, let's have a one-directional, unidirectional neural network just left to right. xt, xt plus one like this and we go to xt and let's assume that the output, we only need the output at the end. So like we read the whole sequence and then we let's say classify it. So we have some kind of head over here and after this head we have the loss function and the loss function, okay, so to this loss function also goes like the correct answer. This here gives us our predicted answer and then we compare it, we get a loss function as usual. So how do the gradients flow? Like where are the weights here? Here is the thing, whatever is the recurrent cell inside, maybe let's assume that it looks like this, doesn't really matter for us. But importantly, every recurrent cell here works in exactly the same way. It has the exact same weights, right? So actually, if you look at the computational graph behind what I am drawing to you, you have this weights of a cell, and these weights are copied, are shared, not copied, shared, across all of the recurrent cells over here, right? So it's the same matrix W, the same weight tensor that participates in every cell. We can't have it any other way, really, because we would never be able to train like separate matrices for going from step one to step two and from step two to step three and so on. Moreover, it's a pretty good thing in the sense that when you do it like this, you can actually process arbitrary sequences of arbitrary length. You don't care about the length anymore. You can just run this for however long you want. It's still the same W. But it also leads to interesting problems. So here is the loss function and you start computing the gradients of the loss function from here and as they flow through the net, through the sequence, they flow back, right? And the actual participation of this weight matrix is that every weight from here, so let me write it just like partial derivative, like dl over some specific w from here is this big sum because the w influences the loss along the way on every single step, so it's like dl over dwt, whatever that means, so like the part that goes over here, and then it's also dl over dwt minus one and so on, dl over dw one, so to speak, so they are not different weights, they are like different participations, like different edges in the computational graph that go out of, that grow out of dwt, so the actual influence of the same weight is done, is given many, many times along the sequence, for every element in the sequence, you again have this influence of dwt, so on one hand, this is good, this is just like, this is the same good effect that we had in convolutional networks, because in convolutional networks we had, how to say this, in convolutional networks we had this effect that the same weight participates in this parallel processing across the whole image, which means that you can have sparse activations, you can have sparse gradients, it's fine, it's okay, it's not a problem, because your sparse activations can, your sparse activations can, will accumulate anyway, so here there is a little bit of that, so every weight is very, very important, but on the other hand, there is a problem with this influence of W going through the whole sequence, and the problem is this, actually I think it's even easier to think of this problem, not during the backward pass like I do here, but just simply during the forward pass through the network from left to right, because as you go from left to right, also W participates every time, right, so let's just make things much, much, much more simple, let's just say that in every recurrent cell like this, we take the input say H and we multiply it by the matrix W, and this becomes H1 and then we again multiply by W, this becomes H2 and so on, this is a very simplified picture of course, you cannot, in reality you cannot have it without activation functions, in reality there is also X and so on, but for illustration this will be enough, so as you go through the recurrent network, your like H1 is W times H0, your H2 is like W times H1, so it's W squared times H0, and your HT is W to the power T times H0, right, and this can be a bad thing, this can be a problem, what can be the problem here? Well, matrices have this property called the spectral radius, or you can think of it as just a Provenius norm, doesn't matter actually, what the spectral radius basically tells you is what does the matrix when applied to a vector, when multiplied by a vector, what does the matrix do to this vector's length, so basically like the norm of ht, where I guess, not squared, yeah, no, not squared, just the length, the norm of ht, will be something like the spectral radius of w times the norm of ht minus one, so every time you apply a matrix, you are on average multiplying the length of the vector by some constant, and these constants accumulate as you see, so when you go to ht, the length of ht is like rho to the power t times the length of h0, so if you started with a vector of length one, which kind of makes sense, why did it become so big, so if you started with a vector of length one, then by the end you have a vector of this length, so if rho, if the spectral radius is greater than one, then it means that your activations just explode, so if rho is like even 1.1 or 1.05 or something, with long enough segments it will obviously go to infinity exponentially, and it will just explode, you will have, I don't know, problems like overflows in the numbers, and the numbers stop making any sense, it's like huge, huge, huge activations which don't really reflect anything, and the same will happen as you go back, because as you go back through a matrix like this, when you compute the gradients, you're also multiplying by W, well by W transpose, but what's the difference, so you're all also dependent on this kind of spectral radius, so you can have two kinds of problems, you can have exploding gradients, exploding gradients, when rho is greater than one and everything goes to infinity, or you can have vanishing gradients, when rho is smaller than one and it all goes to zero. So this is also a bad thing, right? So now this means that as the gradient travels along this path, it exponentially goes to zero on the first elements of the sequence, so it basically means that you cannot have any long-term memory. The influence of earlier parts of the sequence will just vanish completely and will go to zero very quickly here. So in exploding gradients, just everything breaks. In vanishing gradients, well, nothing breaks, but your network doesn't work as you'd like. So how do you solve these problems? Well, I will relegate vanishing gradients to tomorrow because this is a long discussion, but exploring gradients is very, very simple. I mean, as you go along the network, your problem is that your gradients start to grow uncontrollably and your gradient vector will be longer and longer and longer. Well, you can notice this, right? As you go along the network, your gradient becomes longer and you can see it as you go along the network. So why don't you just clip the gradient? And that's the answer. So the answer actually to the exploding gradients problem is not to do something smart and interesting to limit rho to make it equal to one or something. No, the answer is just let's clip the gradients. So like if you have a gradient which exceeds one in length, let's just project it back to the unit sphere. Let's just say, okay, so now it's too long. We project it back. That's it. And after the next step, it will be too long again. We will project it again. That's the only thing we do. So, okay, let me go through the slides. There's probably some illustration here. Okay, recurrent neural networks. This is what we discussed, blah, blah, blah. There are two problems. Exploding radians and radiation radians. And in exploding radians, we just clip it. So, I think this is still from Keras, not even PyTorch, but it doesn't matter. Of course, PyTorch can also clip radians for. Yeah, and this is the illustration I was looking for. There was a very nice paper 10 years ago in 2013 by Pascano who studied the behavior of recurrent networks. There are several very interesting points in there. I recommend you read the paper, actually. But it's not about any new architectures or about making it work better. It's about what's going on in the space of activations, in the space of weights, what's going on as they train and so on. And as for exploding radians, the picture looks like this. So what does it mean to have an exploding gradient, to have this gradient go to infinity? Well, if you look at the loss function, it basically means that you have some normal part where the gradient doesn't explode. And then, boom, at some point, there is just this vertical wall. This wall that goes to huge values very, very quickly. It grows very quickly. It's basically vertical. The gradients explode. So what happens is you go over here and then you bounce off this wall. And if you don't clip the gradients, well, you fly away God knows where. But if you do clip the gradients, well, you go back to this normal regime and you keep trudging along and you keep going in the general direction that you want. So clipping the gradients is not a problem from the theoretical and practical point of view. It's not a bad transformation to make. It's okay. We will still continue to go in approximately the same direction. And probably let me stop here. So we've discussed recurrent neural networks. We've discussed how we process sequences with these kinds of architectures. And we've discussed the main problem. The main problem is that as gradients flow and as activations flow and forward propagation, they either blow up or vanish. And it's difficult to pin the spectral radius exactly to one. So something needs to be done. And the exploding part turns out to be easy. But the vanishing part, as we will see tomorrow, will turn out to be pretty difficult and interesting. Okay, so at this point I want to stop any questions about what we discussed today. While you're thinking about the questions, tomorrow is lecture day. So please join on time. And then you will go back to Alex for practical sessions on Thursday. And yeah, I think they should be available today. So yeah, that's just what I wanted to say. On Friday, there will be a midterm presentation. I sent Alex a list of papers yesterday evening. I think he wanted to add something from himself. I hope it will be made available today. So on Friday, we will be listening to you. Okay. Thanks a lot. And see you tomorrow. Tomorrow, two lectures. Be fresh and ready in the morning. Bye-bye.
