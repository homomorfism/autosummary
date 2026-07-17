# Transcript — google_stt

- **Provider:** google_stt
- **Language:** en-US
- **Audio duration:** 1:28:19
- **Segments:** 632
- **model:** latest_long
- **use_enhanced:** True
- **latency_sec:** 792.54

## Segments

**[00:00 – 00:03]** Okay, hello everyone. We are

**[00:05 – 00:10]** continuing our discussions of declaring and this time, I'm in a very noisy and

**[00:12 – 00:16]** not really comfortable place, but I hope that the combination of

**[00:17 – 00:26]** Modern deep learning, based noise removal techniques will work and I hope you will hear me. Hope the recording of the fine.

**[00:27 – 00:29]** So in any case,

**[00:32 – 00:32]** We?

**[00:33 – 00:35]** Stopped last time.

**[00:36 – 00:48]** It's stochastic, gradient descent algorithms. Right, so basically what we discussed on the previous lecture was that you know, in your own network

**[00:49 – 00:52]** is a big composition of little things.

**[00:53 – 00:55]** Is a huge computational graph.

**[00:56 – 00:58]** And then there are

**[00:59 – 01:00]** two different.

**[01:03 – 01:06]** There are two different kinds of

**[01:09 – 01:17]** Inputs or the neural network, there is the actual input which is X like a picture. They will

**[01:18 – 01:20]** The switching to pictures mostly.

**[01:20 – 01:25]** And then there are the weights right and yesterday.

**[01:26 – 01:29]** not yesterday, but two days ago, we discussed

**[01:30 – 01:39]** That the output of this whole computational graph would be the loss function, right?

**[01:40 – 01:50]** Plus function of X Y, so the correct answer that comes in probably at the end somewhere.

**[01:52 – 01:53]** and then,

**[01:55 – 02:04]** what we actually do is we compute the overall was function at, which is like some

**[02:04 – 02:05]** For the average.

**[02:06 – 02:06]** Of.

**[02:08 – 02:09]** This smallest.

**[02:10 – 02:23]** Of those celebrating step along the way. And then we took it, right? I'm starting with the recap because you told me that some people might do it.

**[02:25 – 02:30]** So then we update the weights with something like this.

**[02:30 – 02:31]** Right.

**[02:34 – 02:45]** But not really so we we have something like this but really we use something much more involved in complicated. Like for example the a demo there is

**[02:49 – 02:49]** and,

**[02:51 – 02:52]** That's how.

**[02:52 – 02:54]** Deep Learning Works in general.

**[02:56 – 03:07]** They are still are a few General remarks that I want to make and that I will probably have to postpone definitely not today. So I have to respond them. Probably to

**[03:08 – 03:18]** The beginning of next week. I still want to discuss waiting in this realization, which is a picture interesting and

**[03:20 – 03:23]** Nice Topic in itself. And also I want to discuss

**[03:25 – 03:27]** those and also I want to discuss

**[03:29 – 03:36]** Organizational layers. You probably have heard of bachelor's National Organization. There are

**[03:36 – 03:49]** several different flavors of harmonization layers and what exactly they do and why they're necessary is, in my opinion, a pretty interesting topic.

**[03:50 – 03:51]** But today.

**[03:52 – 04:03]** We actually start talking about not in general. What happens with the loss function, still being a black box?

**[04:03 – 04:04]** but,

**[04:06 – 04:14]** What happens inside this black box, right? So today we start talking about architectures of neural networks.

**[04:15 – 04:16]** Architectures.

**[04:19 – 04:23]** The word architecture. In this case, basically means what's in here.

**[04:24 – 04:27]** What is the structure?

**[04:28 – 04:30]** Of this computational graph.

**[04:30 – 04:31]** and,

**[04:32 – 04:42]** they and we already kind of know that it can be any character graph and anything would work and

**[04:43 – 05:00]** The only requirement is that first there are no circles, right? So we need to be able to Traverse the graph in topological order in One Direction and then the opposite direction. But also, what we need to do is we need to be able to do is to

**[05:01 – 05:10]** I do the elementary computations, the forward propagation and the backward, propagation inside every one of these.

**[05:11 – 05:34]** Notes. So the general picture is like this. You have Elementary notes, they constitute a graph and we do one pass of propagation one passive back propagation and avoid. I have your gradient, then all of this old Christmas that we discussed last time.

**[05:36 – 05:36]** So,

**[05:40 – 05:42]** so, this

**[05:43 – 06:06]** Is the general picture and immediately we can start, you know, just thinking about how this graph might be organized. For example, you could do it and usually people do it in a layer Target texture. So they are layers, right? Onions, have layers and photographers have layers famously and

**[06:08 – 06:10]** What a layer means.

**[06:10 – 06:13]** is that as you go,

**[06:14 – 06:20]** Left to right through this architecture as you go, along the computational graph.

**[06:22 – 06:23]** The.

**[06:24 – 06:30]** Neurons, let's say, let's call them neurons for now the perceptron or whatever like the components of this layer.

**[06:32 – 06:44]** Talk mostly to the components of the next layer, and then those components talk to the components of the next layer, right? And so on, until the end,

**[06:45 – 06:47]** so layers are kind of this.

**[06:49 – 07:40]** Six, sequential slices of the computational graph and I'm deliberately not really trying to make it formal or anything. Because in reality, it's a Mercury concept, right? So yes, sometimes a layer in it is characterized exactly like this but sometimes you would have something like a skip connection for example. So we will see in our class, we will see networks. Where there are connections, that go around the layers, we will definitely see around the earthquake player, one to layer 3, and we will definitely see connections that go around even layer and just not touch it. That would be the residual connection and we will definitely talk about those there. One of the most important ideas here

**[07:41 – 08:02]** Car. But anyway the notion of layers is useful and the first, the easiest today, the most straightforward class of architectures are the fit forward or well. Okay. Fit forward is more general term but let's say fully connected Networks

**[08:02 – 08:04]** Fully connected.

**[08:05 – 08:05]** Networks.

**[08:08 – 08:16]** I don't want to make a big topic of them because there is really nothing to say. So in a fully connected Network, you have layers

**[08:18 – 08:40]** Every layer is a set of persons and this time it works exactly like you would expect. So the percept runs inside a layer, don't talk to each other. They talk they receive inputs from the previous layer and then they send out puts to all New Orleans of the next layer. That's that's what it means. In this case to be fully connected.

**[08:43 – 09:07]** It's not a fully connected graph, but it's a fully connected by part-time graph between everyone of between every pair of and then probably all comes together in a single, or, at least a smaller amount of perceptrons on the other end and that, and that gives you the output.

**[09:09 – 09:10]** Right, or whatever you want.

**[09:11 – 09:12]** Okay, so

**[09:13 – 09:26]** fully connected networks, they were important. Fully connected layers are still important you, if you will see a fully connected layer inside the transformer, for example, when we get the Transformers

**[09:27 – 09:40]** But today, we start discussing a more interesting kind of architecture. Slightly more involved kind of architecture and that is convolutional neural networks.

**[09:42 – 09:45]** So, what are convolution on your own networks? What is the

**[09:46 – 09:48]** What is the basic idea? Well,

**[09:50 – 10:00]** This is one of the last time, I think in class, maybe there will be one more time, but that's it. One of the last times in class and I will actually

**[10:01 – 10:07]** Go back to the biological motivation of everything that's happening, right? So

**[10:09 – 10:13]** we discussed how artificial neural networks.

**[10:13 – 10:38]** For how artificial neural networks were inspired by the human brain or by the animal brain and we discussed how the principle of connectionism actually works. But oh, and by the way, I think we didn't discuss it. So let me just take a very quick detour here. Let me give you a very, very short remark.

**[10:40 – 11:05]** We discussed gradient descent in neural networks and all artificial neural networks today are trained with radio in descent in one way or the other. So, it's different is not in the basic principle, the differences in the form of the laws function, from the form of the training set. Maybe this definitely the architecture Etc but not in the basic principle of this.

**[11:08 – 11:19]** Solving an optimization problem, right? You have lost function, you have a way to compute this gradients and then you use this gradient. Stop to my

**[11:20 – 11:22]** Oh, here here is a funny thing.

**[11:23 – 11:28]** The brain, the human brain cannot work this way at all.

**[11:29 – 11:45]** And that is kind of obvious when you look at the biological structure that we discussed. So even without actually understanding how it works even without actually knowing what the mechanism is, you can definitely say. It's not gradient descent.

**[11:45 – 12:00]** Why? Because as we discussed the biological neuron, this little guy has a lot of dendrites coming out of here, right? And the little guy also has a single Axon

**[12:00 – 12:02]** That is the output.

**[12:03 – 12:05]** Of the biological neuron, right?

**[12:08 – 12:09]** And that's it.

**[12:10 – 12:14]** So, a biological neuron and compute only one function.

**[12:15 – 12:28]** And to have gradient descent. You need every note in your network to compute at least two different functions. You need to be able to go forward, but you also need to be able to go backwards.

**[12:30 – 13:01]** All right, and I told you how to implement your own note in the computational graph and pytorch. What would you actually have to do is you would have to implement to procedures, f-pro, forward, propagation, and be prepared with propagation. How, what, what the function actually does. When it goes when the computer, and what are its derivative how it's the gradient should be computed as you do back propagation.

**[13:03 – 13:03]** Well.

**[13:05 – 13:06]** Here's the thing.

**[13:06 – 13:12]** The biological neurons and neurons in our heads cannot do that. They only have one output.

**[13:13 – 13:13]** so,

**[13:14 – 13:27]** What this actually means and this is this is an even deeper point and then it might seem so. Okay, they cannot upgrade in the sense so they have to do something else and all. So what it means

**[13:28 – 13:30]** Is that this something else that they do?

**[13:34 – 13:36]** Also has to somehow.

**[13:37 – 13:40]** and the signal back from the

**[13:41 – 13:53]** And from the point where the loss function is actually computed. I mean, I don't think it's ever is explicitly. Computed in our brains, but somehow, like, at least theoretically it's there. So between

**[13:55 – 13:59]** The end, the end goal and whether we achieved it or not.

**[14:01 – 14:07]** you need to have a connection from there from from the end of the chain to every neuron

**[14:08 – 14:10]** Out there. Right. So

**[14:12 – 14:12]** You need to.

**[14:16 – 14:17]** You need to.

**[14:20 – 14:42]** You need to have a Loops in, in the human brain, you need in the biological brain, you absolutely have to have connections that go from here or but back here, but there and everything you have to have a lot of feedback in the brain or train.

**[14:43 – 14:53]** And the brain does have hit back. Alright, so here is here is where the analogy like totally and completely ends.

**[14:54 – 15:18]** So we discussed that one. Neuron is actually a pretty good model of what's happening in the brain. One perceptron is a pretty good model of the biological neuron, especially with railroad activations. We discussed that PS that our brain also works on the principle of connectionism. That is a huge composition of simple functions. Gives you something can give you something very complicated but but

**[15:20 – 15:31]** It cannot run, gradient descent definitely. So and the architecture cannot be similar at all. So the brain also has layers will say it just now but

**[15:32 – 15:56]** Between every two layers there are feedback connections that go back and from later layers, they're a bit but connections that go all the way back it. I mean, it's a mess. We really don't really understand in detail how the brain, what the brain's architecture is, we understand it generally in terms of well this is the visual cortex in here at the layers in the visual cortex but they actually finds structure is very very difficult. Of course.

**[15:57 – 16:03]** Okay. So with that, remark out of the way, let's go back to this guy's

**[16:03 – 16:05]** this guys are

**[16:06 – 16:18]** Fuel and with all Torsten Wiesel and I forget the name of hubel who were to go there in a well price for studying the visual cortex.

**[16:20 – 16:20]** and,

**[16:21 – 16:50]** Convolutional networks are partly motivated by the visual cortex that's why I'm talking about this. But again there will be a point where the analogy just have to, we'll have to stop, I'll tell you when it happens but first let's begin with the bio. So back in the I think 1960 just they made their famous status of the visual cortex and is it quite often happens in biology and scientists like this.

**[16:52 – 16:56]** Their actual like truly Noble thing that they did.

**[16:57 – 17:20]** Was having a new device. So what they actually was what their advantage was compared to everybody who was before, that was that they could actually make such tiny electrodes. That you could attached the electro to a single neuron and rid of the activation of a single neuron

**[17:21 – 17:22]** On a live brain.

**[17:23 – 17:41]** Okay, so before that, all the people could do was, you know, hope that some guy would get in the motorcycle accident and then have a stroke and then the stroke will will give you some interesting information about what which part of the brain does. What?

**[17:42 – 17:52]** But this guy's they could actually well. Okay, this is this is not my favorite part but they could take a cat. If you look closely. There is very well.

**[17:55 – 18:16]** Fixated cat over here and then they would actually slice open the head of the cat of course, on painting orders. And then they would be able to actually throws to individual neurons and see what the individual neurons in the cat's brain actually respond to

**[18:17 – 18:57]** Ah, and what, what they did. So what they found was that, okay, so it had been known that the visual cortex is back here in the occipital lobe in mammals, in us. And in cats, it's actually a very bad decision of nature. It's it's a very fragile thing that makes absolutely no sense because your eyes are in front over here. And then, there is this optical nerve, this big fat, pile of connections, that goes all the way through your skull backwards.

**[18:58 – 19:00]** and,

**[19:01 – 19:26]** Of course, it will be easier to just have the visual cortex in front, but I think the evolutionary explanation is that back when we were very far from animals, we would have like the Proto eyes up here on top of on top of the head. And then somehow, the ice went over here and the part of the brain that processes that went over there. I have no idea why

**[19:27 – 19:46]** Anyway, it is known that the visual cortex is here. The part that processes visual input and it's easy to find like the first layer of the cortex. It's easier to see that. Okay, here is where the optical nerfect. So these neurons take the immediate inputs from the ice.

**[19:48 – 20:23]** And if you actually look at what a single neuron activates for, what a single neuron is doing on this first layer of the visual cortex, you will see that first of all, it cannot, of course, see the whole picture. It has only that many inputs, and it's basically a small, a small receptive field as it is called. It's it looks at a relatively small part of the of the general picture.

**[20:24 – 20:50]** And in this small part it recognizes something really, really simple. So on this slide is a simple neurons recognizes like vertical lines. So if it's a bright vertical line in its field of vision, great, it's activated a lot and test even even if you still have just single and but you start to rotate it, the activation days out and basically goes to zero,

**[20:52 – 20:52]** and then,

**[20:54 – 21:06]** what would you expect next? Well, you would definitely expect that. Then you would have player two, the second layer that would feed off the outputs of the first layer. So it would somehow

**[21:08 – 21:10]** Combine. The

**[21:12 – 21:35]** This simple shapes into something more complicated. Like if you had one neuron that recognizes vertical lines, another track recognizes, for example, lines, boom, you put an end, you have a neuron that gets and across them and oh, you have in your truck recognizes across and it's an Interceptor filter and visual. If you feel the fish.

**[21:37 – 21:46]** and people did this and they also started the second layer so they discovered neurons, like I just said,

**[21:47 – 21:47]** but then,

**[21:48 – 22:12]** They somehow didn't go any further and they, they started to other things. And actually, that was a pretty wise decision because again, the brain is very, very complicated. And if you look at some simplified representation of the visual cortex, you will actually see that they are

**[22:13 – 23:13]** Like layers from V1 to V4 then V5 V6, etc, etc. And yes, there are layers, but it's not an artificial neural network. The actual structure is much more complicated. There are, there is all sorts of feedback that goes back there, all sorts of connections. And, yeah, I keep showing this picture for the last 10 years or so. And I suppose that, since the last 10 years has become much more complicated. So, this, this is from somewhere in this picture, was called the most important neural Pathways in, in the visual, in the early layers of the visual cortex, so you can actually see that. Yeah, there is a very well defined first layer. Yes, the the optical nerve does come in somewhere. So, the first layer is easier. The second layer is also kind of clear, and then it's just a

**[23:13 – 23:19]** mess. Then it's like a lot of different components that do different things. There are all in interconnected with each other.

**[23:20 – 23:20]** Anyway.

**[23:22 – 23:22]** Anyway.

**[23:25 – 23:26]** When people saw that.

**[23:27 – 23:28]** When they saw how.

**[23:30 – 23:31]** Small geometric shapes.

**[23:32 – 23:33]** Regular.

**[23:34 – 24:00]** Go up layer by layer and we didn't have a clear picture of what happens next to that point. But clearly at some point, the picture would go to something like face recognition, right? So, some very complicated, computer vision problems would be soft in our human brain very quickly. So people, of course, try to imitate stuff like this in computers and

**[24:01 – 24:06]** Actually convolution and convolutional networks are very well Stadium.

**[24:08 – 24:14]** They date back at least to this very interesting architecture called the Neo cognitron.

**[24:14 – 24:38]** By the Japanese researcher named, he did it in the late 1970s and I actually if you're interested in the history of preparing actually, recommend you to read the papers, it's like it's a two-page paper, it's very short and you can definitely read it. There's nothing to complicated and there and

**[24:39 – 24:41]** When you read it, you see that?

**[24:42 – 24:46]** In 1979, he had a deep neural network, several layers.

**[24:47 – 24:49]** It was a convolutional network.

**[24:50 – 24:50]** and,

**[24:51 – 25:04]** it had real work activations, the this hinge activations that we discussed last time and that I told you were only only came into common practice in 2011 or 12

**[25:06 – 25:28]** But the thing, the thing he didn't have the thing, they didn't she didn't have a 1979 was learning. So there was a big composition of simple things, and they work on relationships, but they were not trainable conversations. They were just some fixed filters that he would apply across the anyway, whatever.

**[25:28 – 25:48]** So, in modern formulation on networks appeared, in the other ones group, that's the main claim to fame by Young. He developmental networks for many, many years for several decades, and in the late 1980s, they appeared already

**[25:50 – 25:50]** Certainly.

**[25:51 – 25:51]** In.

**[25:52 – 26:04]** Their modern form, they had training, they had conversions and everything. And let me just walk you through a few images that will show.

**[26:05 – 26:06]** How convolutional networks work?

**[26:07 – 26:09]** and it's an

**[26:10 – 26:12]** it's such a brilliant idea that

**[26:14 – 26:24]** It's oh, okay. It's just a brilliant idea. It's it's a very brilliant idea for what I would call structural regularization, you'll see what they mean.

**[26:24 – 26:25]** so, first of all,

**[26:26 – 26:33]** Let's have a picture like this one. And let's assume that I want to process this picture.

**[26:34 – 26:53]** So what do I mean by processing? Well, maybe I want to solve some computer vision tasks. Maybe I want to, for example, find the little boys head on the same image, so where that would be objective actually. We'll discuss object actually later. So where is the the boys head and the image?

**[26:54 – 26:58]** And the main observation.

**[26:59 – 27:12]** The main idea of the main assumption that that is behind CNN's, that is behind convolutional neural networks. Is that? Well, if I'm looking for something, for some feature on an image,

**[27:13 – 27:14]** Then.

**[27:16 – 27:18]** It's the exact same function.

**[27:19 – 27:21]** Applied all across the image.

**[27:22 – 27:31]** So if I have a black box that looks at a small window and says, well, that's the boys have or no, that's not the boys head and

**[27:32 – 27:34]** it'll be the exact same black box.

**[27:36 – 27:46]** That I that I'm supposed to apply across this whole big picture and just output will be different. So here it will say yes. And over here, it will say no, but

**[27:47 – 27:51]** The function is the same as the inputs are different. So the outputs of course are also if

**[27:53 – 28:11]** So the idea of conversion on your networks is this, let's take a picture or anyhow and input is just easier to more, you know, more clear to reason about pictures, but they can input break it into small Windows like this. Usually, they are overlapping like shown here.

**[28:12 – 28:14]** and then,

**[28:14 – 28:17]** For every tile like this one.

**[28:18 – 28:21]** Apply a small neural network.

**[28:22 – 28:38]** So now, this small neural network is a model that we need to trade. It will have weight there. We will, do gradient descent etcetera, but it will be small, it will be applied, only to this little tile a few pixels across

**[28:39 – 28:52]** That we split the picture enter, right? And the big game here, the prophet is that. Now I take the exact same. Small neural network.

**[28:53 – 28:56]** And they apply to every single tile.

**[28:57 – 28:57]** Across.

**[28:59 – 29:00]** The input.

**[29:01 – 29:15]** So I take this style, I applied in your own network. I get this let's say output Vector. Usually you would want to extract, not one feature. But several features, usually the output is several numbers.

**[29:17 – 29:21]** and then I take the next style I apply, I get some some more

**[29:22 – 29:30]** I am. So when I actually do that, get back to the board when I actually do that.

**[29:32 – 29:37]** What I get as a result. So here is my input picture.

**[29:38 – 29:42]** right, I break it into Windows like I showed and then

**[29:43 – 29:50]** I take each window. Okay, yeah. Okay, let them be overlap and whatever I take each window.

**[29:51 – 29:59]** I put it through my small, neural network and let me draw it. Horizontally, I get this Vector features, right?

**[30:02 – 30:06]** Then I take the next window over here.

**[30:07 – 30:10]** I put it through the exact same, you know, Network.

**[30:11 – 30:13]** And I get the different Vector officers.

**[30:14 – 30:15]** That goes here.

**[30:17 – 30:24]** Okay. Now this will be a mess with a picture. But anyway, as I take each one of this windows, I get

**[30:26 – 30:28]** I get to Vector of features.

**[30:29 – 30:37]** And then so forth these factors are features themselves. Also have this geometric structure,

**[30:38 – 30:51]** Right. So there is a top right window. There is a bottom left window and the bottom left window. Will give me this bottom left, Vector features, and so on.

**[30:51 – 30:56]** Right. So as the output of this procedure,

**[30:57 – 30:59]** I will get a three-dimensional tensor.

**[31:00 – 31:09]** Right? I will still have some width, some height and now I will also have a meaningful depth.

**[31:10 – 31:28]** So actually the input also usually has steps for example, because these days for the last few decades, pictures are usually in color. So even if even on the first step, if you have a color image you have the three at the right but

**[31:30 – 31:42]** in general what you get at the output of convolutional layer is a 3D tensor if you start with the 2D input in structure like a picture,

**[31:43 – 31:49]** And then you can do the same thing, right? So again, you take it, speaks holes.

**[31:50 – 31:53]** You take this structure over here.

**[31:54 – 31:54]** and,

**[31:55 – 31:55]** You.

**[31:57 – 31:58]** Try it with Windows.

**[32:00 – 32:01]** With small tiles.

**[32:02 – 32:13]** and then you take this small substances are the small window out of here and the opposite through the through another small, neural network and you get another

**[32:14 – 32:23]** Vector of features. And again, you repeat this, this was the top left Vector of features, but then you get another test.

**[32:24 – 32:35]** And so on and so forth. It's, I'm sorry, I'm not in the convenient place. Very nice picture, but I hope you understand what's going on. So, on every step we

**[32:36 – 32:42]** Tile the image into tiles like this one.

**[32:44 – 32:52]** It doesn't have to be the original image. You can change this layer's one after the other because

**[32:53 – 33:04]** Always you're working with like three-dimensional race, you're rich and declaring car, confusingly content, but what can you do? So you're working with three dimensional tensors.

**[33:05 – 33:06]** and,

**[33:07 – 33:12]** You just convert one 3D tensor to another as you go with this procedure.

**[33:13 – 33:14]** and then,

**[33:17 – 33:21]** Then you can have like, a whole sequence of this convolutional layers.

**[33:22 – 33:23]** Okay.

**[33:24 – 33:28]** so before we proceed, one more thing about this

**[33:30 – 33:39]** In classical, convolutional neural networks and then many architectures that we will see. Today, there is a

**[33:41 – 33:49]** Another type of layers like there is a convolutional layer. That's the one that we just discussed and then there is also what is called the pooling player.

**[33:50 – 34:00]** And let me maybe first, give you the maturation for it and then the actual layers is actually pretty simple. So the motivation is this

**[34:01 – 34:04]** Let's again, try to look at.

**[34:05 – 34:06]** What?

**[34:07 – 34:11]** The neurons do. So this is our original image.

**[34:12 – 34:15]** And it has lots and lots of pixels, right?

**[34:16 – 34:22]** It's it has big width, big height.

**[34:24 – 34:24]** Then.

**[34:25 – 34:44]** I slice it into very small tiles. So of course on my picture, they're not small, but in practice, there are small tiles. So I have this style of let's say three by three picks holes and it's a color image so it has depth 32. So it has a small height, a small width,

**[34:45 – 34:49]** and then it goes through the neural network and then,

**[34:50 – 34:52]** We get our Vector of features.

**[34:54 – 34:54]** so,

**[34:56 – 34:58]** This factor of features this one.

**[35:00 – 35:04]** Depends only on this small small three by three tile.

**[35:05 – 35:05]** Right.

**[35:06 – 35:06]** so,

**[35:09 – 35:16]** if if you look at it from the, in the other direction, you can say that for this feature, this feature,

**[35:17 – 35:19]** Has a receptive field.

**[35:21 – 35:33]** It's called in this part of science receptive. Field has a receptive field of three by three pixels. So yeah, it only looks at a very small, very local, part of the image.

**[35:34 – 35:34]** All right.

**[35:35 – 35:40]** So what happens next suppose that I cover?

**[35:41 – 35:41]** This.

**[35:42 – 35:44]** Whole image with three by three.

**[35:46 – 35:47]** Windows like this.

**[35:49 – 35:52]** And then in, as a result, I will have

**[35:53 – 35:55]** a 3D tensor like this.

**[35:56 – 36:01]** And then I do another convolution I do another three by three conversion over here.

**[36:02 – 36:03]** Okay, so I cut off.

**[36:04 – 36:15]** I cut out another three by three by something. Now the depths from probably more than three. But anyway I cut out another three by three by D tensor and they put it through a small neuron Network and so on.

**[36:17 – 36:18]** I get the feature over here.

**[36:20 – 36:21]** What is its receptive?

**[36:22 – 36:25]** Well, it looks at this.

**[36:26 – 36:27]** Features inside this.

**[36:28 – 36:34]** But a little bit, right? The features inside this small part of the tensor.

**[36:35 – 36:37]** And these features in turn.

**[36:38 – 36:47]** Are looking at more pixels than before, right? So if I had three by three over here and another three by three over here,

**[36:48 – 36:54]** Which those two ones here. So now like this guy corresponds to this,

**[36:55 – 37:02]** And this guy corresponds to a window over here. Alright, so overall

**[37:03 – 37:04]** Overall.

**[37:05 – 37:08]** This pixel over here would look.

**[37:08 – 37:20]** 85 by 5 window in the original pixels, right? That that's my point. So if you do a three by three and then there is also if your three by three you compose in another Shiba, three then

**[37:21 – 37:25]** You collect information from a 5 by 5 in the storage, right?

**[37:29 – 37:31]** But if it's a pretty small windows,

**[37:32 – 37:34]** So like, how many layers would you need?

**[37:34 – 37:37]** so if neurons that look at the whole picture,

**[37:38 – 38:03]** On every, on every three by three conversational layer, you just add two to the tweets and you don't multiply by it too. Just add to do it and add to the height of this receptor showed, right? So, if I want the process and 2:56 by 256, same, which I would need like 100 and 130 layers, that doesn't make any sense. I don't want to have that many layers.

**[38:04 – 38:04]** so,

**[38:06 – 38:10]** so in the original convolutional Networks,

**[38:11 – 38:34]** You would somehow need to solve this problem. That is you would need to reduce the geometry. And this this is an important way of looking at. We will talk about reducing the geometry or what in this class. But you you want to reduce the geometry quicker, then by just dialing, everything and hoping that, you know, convolution will do it by themselves.

**[38:36 – 38:36]** So,

**[38:37 – 38:41]** in the original neural networks in the relationships, they had

**[38:43 – 38:49]** And you can see today in some architectures and they had this idea of a pooling clear.

**[38:50 – 38:57]** so let's suppose that I had a convolutional year extracted some features and then I can say, well, you know,

**[39:00 – 39:08]** there are too many, The Beatles hide her to be. I want to reduce the geometry. Oh, there it is. The temperature. Well, I could just

**[39:09 – 39:21]** Slice it into small Windows. This time. No overlaps. That's the whole point. No, overlaps, usually, it's two by two in those but of course you can set whatever you want and

**[39:22 – 39:26]** Just replace in every 2x window.

**[39:28 – 39:30]** Out of four features. Leave only one.

**[39:31 – 39:32]** According to some rule.

**[39:33 – 39:33]** Right.

**[39:34 – 39:55]** And there are two commonly used roles. I think anything else. Just reduces basically one of these two in effect. So there is max volume where you take the maximum of the feature really is in this small window and there is average pulling, very average them

**[39:56 – 40:32]** I don't think I've ever seen anything else in practice and usually, it's Max bowling. So usually it's Max pooling. Why? Because it kind of makes sense for feature extraction. So, okay, so the real answer is because it's works but usually, but they justification is that like it urges kind of layers to actually extract more meaningful features. So if you, for example. So let's look at this picture and let's say, okay, so I want to like however,

**[40:34 – 40:44]** A black box have a feature extractor. That says, is there a little boy's head in this in this style?

**[40:45 – 40:58]** And so when I run it on this style, I get a one right. But when I read and say on this style or on this tile I get basically a zero even if it's like perfectly understands everything.

**[40:59 – 41:07]** So then, let's suppose that they have this bigger tail, that combines the small tiles over here. That

**[41:08 – 41:11]** Glues them together like pulling this.

**[41:12 – 41:14]** And then I asked, well, what is the proper?

**[41:16 – 41:20]** Composition. What is the proper combination of features that will answer? The question is there?

**[41:21 – 42:09]** A little boy's head in this tail and that would be the max, right? If I ever actually get some pretty low average because most tiles don't have a little spray head, right. And only one tile would have the little boy's head and the rest wouldn't, but but like meaningful features, like something is there they obey the max flow, right? And last meaningful but sometimes also useful features like how green it is. This feature would have made the average for right. If a have a big tile delicious half green and half blue, I would probably want to say that it's half green. It's not fully green but for like features corresponding to objects or whatever shapes.

**[42:10 – 42:14]** Max is usually the way to go anyway that that's just

**[42:16 – 42:19]** a rambling justification of why max volume.

**[42:21 – 42:22]** All right.

**[42:23 – 42:24]** And so now,

**[42:25 – 42:39]** When you combine when you come by convolution know and fooling clears, you can start using the geometry really quickly, because every pool in clear.

**[42:41 – 42:54]** Cuts the width and the half by two. Let's assume it's 2 by 2 pulling. It's almost always so better pulling. So every pulling clear cuts the width by two cuts, the height by 2. You get twice, you get four times.

**[42:55 – 43:02]** Fewer pixels for four times, your numbers, and then you can do another conversion, blah blah. And so

**[43:03 – 43:08]** so at this point, at this point, what I want to do

**[43:09 – 43:10]** Is.

**[43:11 – 43:12]** I want to.

**[43:14 – 43:24]** Actually discuss how you would Define a convolution like what it actually is. And then we will just work through an example where

**[43:25 – 43:31]** oh, just and we would just work through an example, where we would

**[43:33 – 43:37]** eh the beauty of convolution, where we would actually

**[43:38 – 43:39]** Like realize.

**[43:41 – 43:46]** Why can't I save so much? Why why? There such a great way to process large inputs.

**[43:48 – 43:51]** So what exactly what this neural network be?

**[43:54 – 43:54]** Yeah. Well

**[43:55 – 43:59]** the like the Deport, convolution

**[44:00 – 44:28]** Doesn't really mean anything specific. It just means that I trial a tiled, the input with small tiles and I apply my transformation to every tile separately. So this is what the word convolution means. It doesn't tell you what exactly this transformation should be. But usually, when people talk about volitional layers, they mean the simplest neural network possible.

**[44:28 – 44:32]** The simplest neural network possible. That is just one fully connected layer.

**[44:34 – 44:36]** So, it looks like this.

**[44:37 – 44:49]** I have my input. Now let me do it and full generally. So I have a 3-dimensional input. It has some wheat, capital W, some great Capital, H, some tips deep.

**[44:50 – 44:54]** And I cut out. ASAP subset a tile.

**[44:55 – 45:04]** Which has a width small W and height small age and still. So this is also important. I always cut

**[45:05 – 45:08]** Through all the features. I take all the features. All the depths

**[45:09 – 45:10]** so then,

**[45:11 – 45:12]** I take this guy.

**[45:15 – 45:29]** And basically I say well okay here I have like a d times. W Times H tensor, right? I have the three dimensional Matrix of three-dimensional array of numbers, right?

**[45:30 – 45:44]** But when I go inside this neural network, I don't care about the structure of this array. I just lose it. I just say, okay, so I have this many numbers. You can actually visualize it. Is flattening it

**[45:45 – 45:50]** to a single Vector of size dwh.

**[45:50 – 45:51]** and then, I just

**[45:52 – 46:02]** Apply a matrix of waste it. I have some Matrix of Waits so the output will be a vector of size. Let's say d Prime

**[46:03 – 46:07]** and this Vector of says, the prime is

**[46:09 – 46:14]** Vector of size. The prime is just W Times this day.

**[46:16 – 46:29]** Okay, so the Matrix W, how many weights does a convolutional layer have? The Matrix W has a supposed to have like

**[46:30 – 46:46]** Supposed to be okay, so just to make it more convenient, let's say it's Z times W. So w would be like, dwh times D Prime.

**[46:46 – 46:47]** Okay.

**[46:57 – 47:00]** So, it would be dwh times the prep.

**[47:01 – 47:02]** and,

**[47:04 – 47:08]** And then and then yes, sir, it was my trainer. So it's a little

**[47:11 – 47:18]** Time is the prime. Yeah, and then the beauty of convolutional networks is that now

**[47:19 – 47:21]** when I take another window over here,

**[47:22 – 47:29]** I also have an input of the same size and I reuse the exact same Matrix that I believe.

**[47:30 – 47:37]** Right? So this many weights are needed to process the whole image.

**[47:39 – 48:11]** I don't I don't have a different W for a different window. Have the same w, i reused the weights. So these many ways are needed to process the whole D times. Big W Times Big H, input. And as you can notice, the number of ways doesn't depend on the size of the input, it only depends on the size of the window. So when I have a convolutional layer, it's very easy for me to say. Oh, okay. So my, my input image is now twice larger but let's just run the convolution across the larger image. I don't care.

**[48:12 – 48:14]** I only care about the size of the window.

**[48:16 – 48:17]** and of course,

**[48:18 – 49:07]** Formally. And like, in reality what you have here is a matrix of this Dimensions, but it would be very, very inconvenient. If we humans had to think of this matrices is, you know, some huge number times D Prime. And then this huge number we would have to memorize and think of, oh, okay, so that was like three by three by 32. How many is that all this? This should be the size. Of course, that's very inconvenient. So in practice, if you for example, set up a convolutional layer and pytorch, it wouldn't be a 2d Matrix. The convolutional the convolution would be defined by four dimensional tensor. So your tensor of Weights would have size. D times, W Times H times. The prime

**[49:08 – 49:12]** And what would actually happen is your input.

**[49:13 – 49:14]** Is a three-dimensional tensor.

**[49:15 – 49:20]** Which is supposed to make the first three dimensions of w.

**[49:21 – 49:25]** And that means that your output is a vector of this damage.

**[49:27 – 49:27]** Okay.

**[49:29 – 49:37]** Uh so in practice, you would Define like four dimensional tensors when you when you set up convolutional layers.

**[49:39 – 49:40]** and by the way,

**[49:41 – 50:14]** While we are at this while we are defining this note that it is absolutely positively. It's absolutely positively, doesn't matter that the input is specifically a picture, that's specifically, is like a 3D tensor with some, with some height, and some depths you can surely have convolutional networks for other kinds of inputs, for example, at some point. Now, of course, nobody the test is, but, at some point,

**[50:17 – 50:17]** You could.

**[50:19 – 50:21]** Never see announced design for text process.

**[50:22 – 50:43]** And what is text is a sequence, right? It's a sequence of tokens and every token gets represented by some Vector. So it's a sequence of vectors, right? It's a, it's a 1D object, one dimensional object that produces a two-dimensional input tensor.

**[50:44 – 50:54]** And sure enough you can have one dimensional convolutions no problem at all. You just adjust your windows are now sliding Windows like this. You take like

**[50:54 – 50:58]** Three neighboring, vectors.

**[51:00 – 51:19]** Your small input is like this. It's well it's D times length of the window and then you multiply it by The Matrix W which now is a three-dimensional tensor D times, L times D Prime and you get

**[51:20 – 51:23]** The result, which is a vector of safety prep.

**[51:23 – 51:29]** Almost no difference at all. Just all all Dimensions change by one. That's

**[51:30 – 51:37]** or you can go in the other direction you can say well, but what if I have, let's say a video.

**[51:38 – 51:41]** I have a video which means that I have a sequence of images.

**[51:42 – 52:10]** So now my input is like, d times W Times H times. Let's say t for time, right? If this is a video. So now they are, there is a sequence of images and every image is a W Times, H times these tensor and of course you can multiply it by 5 dimensional transfer, which is cheap times, W Times H times, T times the prime that's it, right? So

**[52:12 – 52:36]** You can apply the same idea of cutting stuff into small tiles and processing digital separately. You can apply it to anything. It just so happens that it was especially productive for images and basically all of the examples in our class since it's a computer vision. Quest, of course, all of the examples in our class will be will be images.

**[52:37 – 52:39]** Okay, so

**[52:41 – 52:47]** Okay. Okay, so with this, let's maybe look at a specific example.

**[52:48 – 52:53]** Let's look at the specific example, over convolutional Network,

**[52:54 – 52:59]** yeah, this one and I just want to

**[53:00 – 53:18]** Go through this network layer by layer. It's some classical learning architecture from, I don't know, 2001 or something. It's very small. It's very small input, not very powerful but I want to go through the circuit texture to count the weights.

**[53:19 – 53:31]** To get a feeling of what convolutional networks look like and we will see like what's the whole point of conversation when we just asked how many ways they have.

**[53:32 – 53:32]** so,

**[53:34 – 53:40]** So let's look at this slide. What do we have here? We have the input, which is a 32 by 32 picture.

**[53:40 – 53:45]** And it's a black and white picture. Well, a gray, scale it picture so it has depth one.

**[53:46 – 53:48]** so, our input and

**[53:50 – 53:51]** Let me.

**[53:52 – 53:59]** Switch from from the picture to the board for a little bit. So our input is

**[54:00 – 54:05]** a tensor of size 1 times, 32 times 32.

**[54:07 – 54:07]** Okay.

**[54:09 – 54:09]** Then.

**[54:10 – 54:11]** You layer happens.

**[54:12 – 54:22]** And this picture doesn't show you the weights, doesn't show you the layers themselves. It shows you the intermediate results, the dancers that result from every layer.

**[54:22 – 54:26]** so now it's says that after the first layer you have

**[54:28 – 54:30]** when 8 by 28 then sir.

**[54:31 – 54:44]** We see six feature Maps, when people say fisher Maps, it's the same as channels, the same as depths. So basically it says that it's a twin but 28 by 6 and 6 different features,

**[54:45 – 54:48]** ah, so we started with a

**[54:49 – 54:51]** 32 by 32, by one.

**[54:52 – 54:52]** Then.

**[54:53 – 54:54]** Something happened.

**[54:55 – 55:04]** I can relational layer happened and now we have a tensor of size 6 by 28 by 28.

**[55:07 – 55:09]** so, the question to you,

**[55:10 – 55:12]** how large do you think was the convolution?

**[55:14 – 55:15]** What was the size of the window?

**[55:27 – 55:32]** If we went from 32 by 32 pixels to 2828 pixels,

**[55:43 – 55:50]** why would, why would they geometry be reduced? Why would the conventional Network actually have less pixels at the output?

**[56:08 – 56:13]** It. So I am covering the input by overlapping tiles.

**[56:14 – 56:15]** All possible tiles.

**[56:19 – 56:21]** How many tiles are possible.

**[56:28 – 56:33]** Okay, so this is this is our first remark here. So I have this input

**[56:35 – 56:40]** which is like 32 by 32 pixels image.

**[56:41 – 56:50]** Course, I won't draw the full 32 and then I start covering it by tiles of some kind of size. Right. Let's say three by three tiles.

**[56:53 – 56:53]** but,

**[56:55 – 56:57]** How many tiles will fit?

**[56:58 – 57:00]** Not search up by search too, right?

**[57:01 – 57:01]** So,

**[57:03 – 57:31]** You see for every time every tile is defined by its centerpiece. So let's say, right? So this Center pixel corresponds to this three by three window usually it's what they're very few even convolution. So I I am safe talking about the center pixel. So there is a center pixel corresponding to the three by three tile this Center pixel corresponds with 333, so on. But there is no tile that will correspond to this pixel, right?

**[57:32 – 57:33]** It doesn't fit.

**[57:35 – 57:36]** so, in effect,

**[57:38 – 57:41]** How many if I had a 3 by 3? Convolution,

**[57:42 – 57:56]** The output if I just do the tile and if I just use all possible tiles, not use any special tricks here. The tiling would be would would not be able to use this pixels.

**[57:57 – 58:04]** And also wouldn't be able to use this pixels, right? So it would cut off one pixel, on top, one pixel, on bottom, one on the left, one on the right.

**[58:05 – 58:20]** So, if I did a three by three convertion, and I had like a W Times, H image at the input. I would go to something like that. Will you minus two times H, minus 2, right? Because I would need to cut off. Two, picks rolls on the sides.

**[58:22 – 58:28]** Well, here we go. To w minus 4 and H minus 4. So, how big was the windows?

**[58:53 – 58:55]** Yeah, exactly. So

**[58:58 – 59:12]** I mean, of course it's not guaranteed, there could have been tricks, Etc, but the most plausible version of how this convolution what this convolution looks like, judging by that picture and it's true. In fact it's true, is that

**[59:13 – 59:15]** It was, we were covering.

**[59:18 – 59:20]** The input by 5 by 5.

**[59:22 – 59:28]** Tiles. And then, so, what what is the size of the weight Matrix here?

**[59:29 – 1:00:04]** Yeah, I didn't tell you that. Sorry I am when I talk about the weight Matrix I of course, simplify a little bit because in addition to the weight Matrix there is also the intercept. So in fact, of course, this output is like Z W plus some constant. So there is an additional deep Prime. Wait, which is also wait, right? I wish we should also trained, but let's forget about that. It doesn't matter for us. Now let's just count the way to the Matrix system. So

**[1:00:05 – 1:00:07]** What would be the Matrix size over here?

**[1:00:08 – 1:00:28]** The Matrix size would be as we discussed their D times, W Times H times D Prime, right? So here we have a conventional weight Matrix weight tensor of size 1 times 5 times 5 and we have six features at the output time 6.

**[1:00:29 – 1:00:29]** Right.

**[1:00:31 – 1:00:41]** So five, five by five is 25 256 150, right? So, over here, in this layer, we have 150 weights

**[1:00:42 – 1:00:44]** Trainable. It's that we will need to learn.

**[1:00:45 – 1:00:45]** By gradient.

**[1:00:48 – 1:00:54]** Well, there you have it. That's that's that's the first point that I want to make this example.

**[1:00:55 – 1:01:00]** The convolutional idea, the idea of sliding a window over the input.

**[1:01:01 – 1:01:04]** Saves, if you amount of weights.

**[1:01:05 – 1:01:09]** So, suppose that I need to have a fully connected layer over here.

**[1:01:10 – 1:01:18]** Suppose that I just want to have a single weight Matrix that takes. This guy is input and outputs this.

**[1:01:19 – 1:01:30]** Then how many weights would I have? What? What kind of Matrix would? It be a fully connected? First layer would be like, 32 times 32.

**[1:01:31 – 1:01:31]** Times.

**[1:01:32 – 1:01:34]** 6 times, 28 times 28.

**[1:01:35 – 1:01:51]** Right? So it would be a matrix of size input times, output. Input size times. Output says, if I didn't have this conventional structure and I still for some unfathomable first, enable reason would want to have this kind of output.

**[1:01:52 – 1:01:53]** The Matrix would have this kind of says,

**[1:01:54 – 1:02:15]** So, of course, I cannot do this in my head, but like, 30 to square this about a 1000. So this is like, you know, five million or something you can count if you want, but this like several million Waits and the convolutional idea reduced this five million ways.

**[1:02:16 – 1:02:17]** Down to 100.50.

**[1:02:18 – 1:02:25]** So that this is the the power of convolution, the main power of convolution. They save a lot of weights.

**[1:02:26 – 1:02:37]** and that's why I always say that what convolutions actually are, they are an excellent technique of structural regularization

**[1:02:39 – 1:02:43]** we discussed last some

**[1:02:44 – 1:02:47]** previous lectures that regularization is when you

**[1:02:50 – 1:03:11]** Regularization is when you compress compress the weights, Magnum smaller, or it use like reduced the set from which the weights are taken, right? But in this case, it's even more straightforward extraction means. All right? So I have five million ways.

**[1:03:12 – 1:03:31]** And you could like, if you think of it from a proper view, it from a proper angle, you will see that you can actually think of evolutionary or so as a transformation of this guy to this guy. But when I do this transformation, I say, oh okay, so I want this thousand of ways to be equal to each other.

**[1:03:33 – 1:03:57]** And I just said, this constraint that. I always process every window beat over here, or over here, or over here. I process it in the exact same way, with the exact same ways that. So that's structural organization. When you impose constraints, like, this way, it should be equal to each other. This way should just disappear or something. So,

**[1:03:58 – 1:03:58]** so,

**[1:04:01 – 1:04:16]** So this is the power of the violations. And let's so let's finish the exercise that there are still a couple of points that they want to make here. So after the first convolutional layer,

**[1:04:17 – 1:04:22]** There is a pool and clear sub. Sampling is the same as Boolean clears as synonyms.

**[1:04:23 – 1:04:31]** So the pool and clear is obviously has two by two windows, right? So we go from 28 by 28 to 14 by 14.

**[1:04:33 – 1:04:35]** Question to you. How many weights?

**[1:04:36 – 1:04:38]** Does this pulling clear have?

**[1:04:42 – 1:05:05]** I had the sick 28 by 28 by 6 input. I have four seen my fortune by 6 output, which means that. Okay. Let's assume it's Mark spawning. I don't remember which was actually, but I take two by two window. And in every two indoors every feature I take the max of these four numbers

**[1:05:07 – 1:05:09]** How many ways is that?

**[1:05:12 – 1:05:14]** How many trainable weights?

**[1:05:43 – 1:05:46]** So, the pulling transformation takes the input.

**[1:05:48 – 1:05:56]** Cuts it into tiles. And for every tile you take the numbers that are parts of your input and you leave only the max of these numbers.

**[1:05:58 – 1:06:00]** Right, you take a two-way to window.

**[1:06:01 – 1:06:06]** A little bit of a window becomes just its maximum. How many trainable weights are in transformation like this.

**[1:06:24 – 1:06:24]** Yeah.

**[1:06:32 – 1:06:47]** All right, I'm not talking to me today. Anyway, how many ways are in this transformation? Of course? None, of course, there are no weights, it's a deterministic function. There is nothing to trade. They just take the max

**[1:06:48 – 1:06:50]** Right. So the

**[1:06:52 – 1:06:53]** The.

**[1:06:54 – 1:07:06]** Pooling clears. Don't have weights. There is no no point for the for them to have weights. There is nothing to train. I just do a specific fixed thing.

**[1:07:07 – 1:07:08]** so,

**[1:07:10 – 1:07:14]** Okay, so let me draw this next, I have a clear.

**[1:07:16 – 1:07:18]** a Poland player goes to

**[1:07:20 – 1:07:23]** 6 by 14 by 14.

**[1:07:24 – 1:07:26]** The pooling. Clear has no. It's

**[1:07:28 – 1:07:30]** and then I have another conversation there.

**[1:07:32 – 1:07:33]** Right.

**[1:07:34 – 1:07:38]** Check, I have another convolutional layer that goes down to 10 by 10.

**[1:07:40 – 1:07:40]** so,

**[1:07:43 – 1:07:48]** Sorry, check 10 by 10, by by how many 10 by 10 by 16.

**[1:07:49 – 1:07:52]** so, my next Generation layer goes,

**[1:07:53 – 1:07:54]** Makes it.

**[1:07:55 – 1:07:56]** Like this.

**[1:07:58 – 1:08:11]** 16, right? And by 10. So I I put depth first here but you have to, you can put it very one. So how many ways are here? Well, again, we reduce the width and the height by

**[1:08:12 – 1:08:22]** Four. So it's a five by five convolution but now we need to transfer translate six features into 16 features.

**[1:08:23 – 1:08:27]** So let's see. Bye bye. 555 by 610.

**[1:08:28 – 1:08:36]** Okay, that's more ways, right? So we know six by five by five phases, 150, and 150 times 16.

**[1:08:38 – 1:08:43]** I want 50 times 4 is 6. So 6 times 4 is.

**[1:08:44 – 1:08:46]** 2400 rates.

**[1:08:46 – 1:08:48]** Right, I suppose that's correct.

**[1:08:51 – 1:09:17]** 24th 2400 rates over here. Okay, then another pulling this part, I remember. And then we get wait for it. There will be a little bit more interesting stuff here. So now I have like 6016 by 5 by 5 and that this point, I say, oh okay so now I have a five by five.

**[1:09:18 – 1:09:21]** Tensor with depth 16.

**[1:09:22 – 1:09:33]** So, if I keep doing five by five convolution, it means that now there are no tiles really. Like the whole answer is a single tile.

**[1:09:34 – 1:09:48]** I don't have to cut it any longer, which means that, okay, in the picture, they call the convolution layer, but now it really doesn't matter. You could call it a conversational layer or you could call it a fully connected layer. You just take the whole input.

**[1:09:49 – 1:09:53]** And you convert it to okay. How many

**[1:09:54 – 1:10:01]** Features. So next you go to 100 Fishers then 84 features and then finally out of 10

**[1:10:02 – 1:10:05]** so, you go to

**[1:10:06 – 1:10:07]** 120.

**[1:10:10 – 1:10:14]** Then another fully connected layer. You go to 84

**[1:10:15 – 1:10:18]** And another fully connected layer, may be a softmax layer.

**[1:10:20 – 1:10:22]** You go to 10?

**[1:10:24 – 1:10:26]** So, how many ways are here?

**[1:10:27 – 1:10:35]** Well, in this fully connected layer, I have 16 times 5 times, 5 times 120.

**[1:10:36 – 1:10:53]** Right. So I compress the whole input down to the vector and I just lose all the geometry. Don't care about the Germany anymore. This is just Global features numbers about the, the input image and but I still need to

**[1:10:54 – 1:11:12]** You know, do stuff with them. I still need to toss them around a little to do some linear combinations of them to actually extract the signal. That I want, not just reasonable signal, but signal that I want to actually get to get to the

**[1:11:15 – 1:11:19]** the classes, for example, that I want to recognize

**[1:11:20 – 1:11:33]** So off in classical, conversational networks, after you go through all of this layer. So after you down sample and downsample and Sample at the end, you can have a couple of fully connected layers. Usually

**[1:11:34 – 1:11:37]** it's sometimes it's called the head of the network.

**[1:11:38 – 1:11:39]** Head.

**[1:11:40 – 1:11:52]** And sometimes our networks will have multiple heads that the different things. But for now let's just say that I do need to have some kind of a classification at the end with a couple of connections.

**[1:11:54 – 1:11:55]** And interestingly.

**[1:11:56 – 1:11:59]** It turns out that this classification head?

**[1:12:00 – 1:12:04]** Holds the vast majority of all the ways.

**[1:12:04 – 1:12:17]** You see? So over here, we have like, what? 400 times 120. We have 40. 8,000 weights over here.

**[1:12:18 – 1:12:23]** And here we have 120 times 84 which is I don't know about 10K more.

**[1:12:24 – 1:12:24]** Right.

**[1:12:25 – 1:12:25]** so,

**[1:12:27 – 1:12:29]** Out of the total.

**[1:12:30 – 1:12:40]** 60,000 weights on this network about 60,000 about 57,058,000 why in the classification head?

**[1:12:41 – 1:12:41]** And only.

**[1:12:44 – 1:12:48]** Two and a half thousand weights are in the convolutional layers.

**[1:12:49 – 1:12:51]** But the convolutional layers.

**[1:12:51 – 1:12:53]** Are doing the most important job.

**[1:12:54 – 1:12:55]** They are the Fisher, extractors.

**[1:12:56 – 1:12:57]** and,

**[1:12:58 – 1:13:05]** So how does it actually work during training? Oh, remember how we just discussed.

**[1:13:07 – 1:13:20]** Remember how we just asked that propagation. So, if you have a single input, go in into several different places, then in the graph, then when you

**[1:13:20 – 1:13:31]** Go back to the back problem. Bye, propagation, here. Your update, your gradient will be by the chain rule. The sum of

**[1:13:34 – 1:13:41]** Not the great agent. They partial derivative of this note will be by the chain rule, the sum

**[1:13:42 – 1:13:46]** Across all of the paths, right? And in the convolutional network,

**[1:13:48 – 1:13:52]** every weight over here, every weight in this convolution, in this Matrix,

**[1:13:55 – 1:14:10]** Occurs in the computational. Graph is input into the computational graph, many, many, many, many, many, many times. So I don't think they can draw a competition graph for it here. But basically, like this, you have this input, right?

**[1:14:10 – 1:14:12]** In the input.

**[1:14:13 – 1:14:16]** Every pixel is a value. Let's say, and

**[1:14:17 – 1:14:18]** Now.

**[1:14:19 – 1:14:32]** Let's let's suppose that this weight, like wi gets multiplied by the way, you of, and no middle, right? Pixel in the three by three window.

**[1:14:33 – 1:14:37]** which means that when we process this window,

**[1:14:38 – 1:14:43]** I will multiply it by this pixel and then up and everything.

**[1:14:44 – 1:14:46]** when I process this window,

**[1:14:48 – 1:14:58]** I will multiply it by this pixel so and then up and everything. So the same way, the same input to the computational graph will occur many many many times.

**[1:14:59 – 1:15:04]** For on every it will occur in the processing of every every single tail.

**[1:15:04 – 1:15:06]** by by the nature of

**[1:15:08 – 1:15:10]** and that's why, by the way,

**[1:15:12 – 1:15:13]** real activations.

**[1:15:14 – 1:15:16]** Are such a good fit here.

**[1:15:16 – 1:15:20]** Because this means that we don't mind sparsity.

**[1:15:21 – 1:15:23]** Sparsity is bad, if you have.

**[1:15:24 – 1:16:02]** Little signal. If you don't have enough signal, if you don't want to lose anything but sparsity is great. If you have an abundance of signal, if you have a lot of computational paths now, sparsity just saves, you time. It doesn't really, it doesn't really hurt. You doesn't really hurt train. It just says that. Oh, okay, so like in the processing of this window, doesn't matter right now. So this guy will be 0 and this part of the graph should not matter, but the processing of this window will still matter. So this way it will still get the meaning for update.

**[1:16:03 – 1:16:14]** So usually when you have the same way the current and many, many different places, it's it's a good idea to its some sparsity and really provides this kind of first

**[1:16:16 – 1:16:16]** Okay.

**[1:16:17 – 1:16:26]** So what have we discussed so far? We discussed the basic idea of convolutional networks. How you slide across the input.

**[1:16:26 – 1:16:41]** We discussed how the receptive field, grows this time, that it grows not fast enough, and that's why you want to have pooling from time to time, pulling layers, we discussed that

**[1:16:43 – 1:16:59]** We just discussed that you can apply convolution to inputs of other dimensions, to inputs of other different nature. It doesn't matter. As long as you can tile it with something, you can do it on that.

**[1:17:00 – 1:17:04]** And we all went through a specific example.

**[1:17:05 – 1:17:26]** Oh if I honestly think I need to go pretty soon. But before before we close let me just tell you a couple more practical tricks about how can I actually work? Because you will need them and practice and you will need them to understand but what goes next?

**[1:17:27 – 1:17:28]** ah,

**[1:17:28 – 1:17:29]** so, um,

**[1:17:30 – 1:17:31]** trick number one.

**[1:17:32 – 1:17:34]** Let's go back.

**[1:17:35 – 1:17:36]** to this, like,

**[1:17:37 – 1:17:45]** Input tensor, this time I will not be drawing the depth. So let me just draw it as a two-dimensional grid.

**[1:17:47 – 1:17:48]** Like this.

**[1:17:51 – 1:17:54]** and,

**[1:17:55 – 1:17:59]** What am I doing with it? I'm dialing it by

**[1:18:00 – 1:18:03]** let's say, three by three windows or

**[1:18:04 – 1:18:07]** I'm telling it by three by three by three windows.

**[1:18:09 – 1:18:11]** And as we just discussed,

**[1:18:13 – 1:18:14]** Every time.

**[1:18:15 – 1:18:38]** That I apply three by three. Convolution, not. Every pixel can be the center with 3 by 3 window. Right? So we just discussed that if I when I apply conversions by just by overlapping everything and feeding as my as many as I can, well I I can't fit, oh I can't fit as many tells us there were pixels.

**[1:18:39 – 1:18:41]** And sometimes that's really inconvenient.

**[1:18:42 – 1:19:02]** So sometimes what you really want is you want to preserve the shape of your tensor. So if you had D times, W Times H is input. Then after a convolutional layer, you would have a d times W minus K times H, minus k.

**[1:19:03 – 1:19:06]** And I don't want this minus case.

**[1:19:07 – 1:19:20]** I want I want to have a tensor of the exact same shape, it will be. For example, I want to have like adults and such convolutional layers in a row. I want to repeat this, I want to Stack the same layers and I don't want to change the image.

**[1:19:22 – 1:19:25]** oh, when that happens, what you

**[1:19:26 – 1:19:27]** actually.

**[1:19:28 – 1:19:30]** Want to do, is you want to use?

**[1:19:31 – 1:19:32]** So cold in.

**[1:19:34 – 1:19:35]** Just means that.

**[1:19:36 – 1:19:42]** Suppose that I need to have this pixel also be the center of a three by three window.

**[1:19:43 – 1:19:48]** So I draw a window three by three and around the specs. So and I know just that

**[1:19:49 – 1:19:51]** it goes out of the image, right?

**[1:19:52 – 1:19:57]** Well, why don't we just played it. Let's say we zeros.

**[1:19:58 – 1:20:00]** Just say that this pixels are zeros, that's it.

**[1:20:01 – 1:20:05]** And now that would be 0 padding.

**[1:20:06 – 1:20:07]** and now,

**[1:20:08 – 1:20:23]** We are not, and now we are done, we can preserve the size. So that's just stupid practical trick to pad the image with something in order to be able to fit more.

**[1:20:25 – 1:20:34]** Windows. And so there are two common ways to do painting. One is paid with zeros and the other is let's say I want to

**[1:20:36 – 1:21:14]** Have a window like this so when you pay with zeros, there can be a strange effect. Like, you could have like a border around your image of some not really plausible features because this features take this lots of zeros on the side, right? So if you want to wait that you might want to have mirror painting, you may want to just take this, this guy's from here and just copy them by doing a mirror image of of your of your image over there. That's all available to the plating often people do that.

**[1:21:14 – 1:21:17]** okay, so but the whole point is

**[1:21:18 – 1:21:26]** To be able to fit more tiles, to be able to make any pixel in the input, the center of a tail.

**[1:21:29 – 1:21:30]** And one more trick.

**[1:21:32 – 1:21:34]** One more trick is this.

**[1:21:35 – 1:21:35]** so,

**[1:21:36 – 1:21:37]** as I said,

**[1:21:41 – 1:21:47]** if you just keep dialing your tensors with all possible tiles,

**[1:21:49 – 1:21:50]** You will not.

**[1:21:51 – 1:21:51]** Have.

**[1:21:54 – 1:21:55]** You will not have.

**[1:21:59 – 1:22:00]** You will not have.

**[1:22:02 – 1:22:03]** You will not have.

**[1:22:04 – 1:22:14]** You will not be reducing the geometry fast enough, it will have to resort to things like pulling clears. You have to reduce your geometry artificial

**[1:22:15 – 1:22:15]** Well.

**[1:22:16 – 1:22:30]** There is a different way, okay? Very, very simple. What if I just take? Not every pixel as the center of a tile? But what if I take like, every second

**[1:22:33 – 1:22:34]** Like this.

**[1:22:35 – 1:22:39]** So I have like the green window, the green three by three window over here.

**[1:22:40 – 1:22:42]** The light blue over here.

**[1:22:44 – 1:22:45]** The red one over here.

**[1:22:48 – 1:22:48]** and the

**[1:22:50 – 1:22:51]** dark blue one over here.

**[1:22:53 – 1:22:54]** No. So

**[1:22:55 – 1:22:57]** at this point, I have

**[1:22:58 – 1:23:04]** Four times, fewer tiles, right? I have cut my number of tiles in half.

**[1:23:05 – 1:23:08]** Across to it and then half across the height.

**[1:23:08 – 1:23:24]** So now when I get to the output from this, I will have a tensor of size approximately double w over to and they showed over to, right? Depending on the painting there may be some plus or minus ones but more or less like this

**[1:23:26 – 1:23:32]** So it's exactly the geometric effect that we have. No one will reduce the geometry, my factor of two.

**[1:23:33 – 1:23:33]** Right.

**[1:23:34 – 1:23:38]** On the other hand, know, just how? I am not losing anything.

**[1:23:39 – 1:23:41]** Like every pixel is still covered.

**[1:23:42 – 1:23:44]** It's just covered not as many times.

**[1:23:45 – 1:24:11]** So, before if I tile everything, then, like, this pixel is part of this window. And this window and this window, and this window, and this window and many different Windows over here. Well, now, the maximum number of Windows is 4 and usually, it's less like, this guy will only be covered by two windows two tiles but still every pixel is covered.

**[1:24:12 – 1:24:20]** Right? So we are not missing anything. We are not losing any information, the network is still perfectly able to get everything in process everything.

**[1:24:22 – 1:24:28]** So this is a reasonable way to reduce geometry too. And when it happens, it's called a straight.

**[1:24:30 – 1:24:33]** Straight. So, for example, this would be straight too.

**[1:24:34 – 1:24:37]** like if you don't do anything for this trade one, if you just dial

**[1:24:38 – 1:24:40]** With every possible tile.

**[1:24:40 – 1:24:46]** So when you so to summarize what we've discussed today, when you do it in, relational are

**[1:24:48 – 1:24:50]** What do you define?

**[1:24:50 – 1:24:53]** Well, you define the shape of the tensor.

**[1:24:54 – 1:25:02]** Like, did you stop W Times, H times T Prime, right? And DST steps of the input. The prime minister is the output.

**[1:25:03 – 1:25:12]** ah, you define the padding if you want to pad the input with zeros or something else, and you also Define the stride

**[1:25:14 – 1:25:46]** And for, I mean, nobody actually uses it. But formerly, of course, the stride is a two-dimensional thing because it's two numbers because nothing prevents you from going like every second pixel across the x coordinate and every third pixel across the y coordinate, right? It doesn't have to be the equal so formerly. It's two different numbers, of course, most usually there is the same but the stride defines, how you tile.

**[1:25:46 – 1:25:50]** Waiting also defines how you tile, and what do you add to the?

**[1:25:52 – 1:26:03]** well, what do you add and the convolution the the convolutional dancer the size of the dancer defines, how many features you get

**[1:26:06 – 1:26:07]** Okay.

**[1:26:10 – 1:26:10]** Okay.

**[1:26:12 – 1:26:12]** Well.

**[1:26:14 – 1:26:15]** I think, actually,

**[1:26:18 – 1:26:20]** actually, I think I want to

**[1:26:21 – 1:26:22]** stop at this point.

**[1:26:23 – 1:26:26]** So, I don't, unfortunately I have to go.

**[1:26:27 – 1:26:32]** Are there any okay, question, are there any downsides to doing this during the Straits? Well,

**[1:26:34 – 1:26:39]** Again, every pixel now participates in the processing, fewer types.

**[1:26:39 – 1:26:44]** so, maybe you don't want as much sparsity or something but actually the general

**[1:26:46 – 1:26:57]** the general, like trend of how convolutional networks developed,

**[1:26:57 – 1:26:58]** Was.

**[1:26:59 – 1:27:56]** As time went by, we did pulling less and less often so pulling actually has some undesirable properties. Pulling like cuts off, lots of computational paths as well, and pulling kind of distorts. The gradients, I won't go into details. Basically, there are bad side effects of pulling, and when we get to Modern architectures, you will see that starting from things, like, Inception, resnet, and some more involved architectures. You will see that they reduce the geometry, of course, but they reduce it with not exactly with a stride but they reduce it with like a complex sub-network that basically at some point does Australia conversation at some point. That's something like this. And then also that's something else. But we'll get there when we get

**[1:28:00 – 1:28:16]** Okay guys, it's been a pleasure talking to you today. Sorry that this lecture is a little bit messy, but I hope that I'll get settled by next week and we will continue.

**[1:28:17 – 1:28:19]** Thanks a lot and bye. Bye.

## Full text

Okay, hello everyone. We are continuing our discussions of declaring and this time, I'm in a very noisy and not really comfortable place, but I hope that the combination of Modern deep learning, based noise removal techniques will work and I hope you will hear me. Hope the recording of the fine. So in any case, We? Stopped last time. It's stochastic, gradient descent algorithms. Right, so basically what we discussed on the previous lecture was that you know, in your own network is a big composition of little things. Is a huge computational graph. And then there are two different. There are two different kinds of Inputs or the neural network, there is the actual input which is X like a picture. They will The switching to pictures mostly. And then there are the weights right and yesterday. not yesterday, but two days ago, we discussed That the output of this whole computational graph would be the loss function, right? Plus function of X Y, so the correct answer that comes in probably at the end somewhere. and then, what we actually do is we compute the overall was function at, which is like some For the average. Of. This smallest. Of those celebrating step along the way. And then we took it, right? I'm starting with the recap because you told me that some people might do it. So then we update the weights with something like this. Right. But not really so we we have something like this but really we use something much more involved in complicated. Like for example the a demo there is and, That's how. Deep Learning Works in general. They are still are a few General remarks that I want to make and that I will probably have to postpone definitely not today. So I have to respond them. Probably to The beginning of next week. I still want to discuss waiting in this realization, which is a picture interesting and Nice Topic in itself. And also I want to discuss those and also I want to discuss Organizational layers. You probably have heard of bachelor's National Organization. There are several different flavors of harmonization layers and what exactly they do and why they're necessary is, in my opinion, a pretty interesting topic. But today. We actually start talking about not in general. What happens with the loss function, still being a black box? but, What happens inside this black box, right? So today we start talking about architectures of neural networks. Architectures. The word architecture. In this case, basically means what's in here. What is the structure? Of this computational graph. and, they and we already kind of know that it can be any character graph and anything would work and The only requirement is that first there are no circles, right? So we need to be able to Traverse the graph in topological order in One Direction and then the opposite direction. But also, what we need to do is we need to be able to do is to I do the elementary computations, the forward propagation and the backward, propagation inside every one of these. Notes. So the general picture is like this. You have Elementary notes, they constitute a graph and we do one pass of propagation one passive back propagation and avoid. I have your gradient, then all of this old Christmas that we discussed last time. So, so, this Is the general picture and immediately we can start, you know, just thinking about how this graph might be organized. For example, you could do it and usually people do it in a layer Target texture. So they are layers, right? Onions, have layers and photographers have layers famously and What a layer means. is that as you go, Left to right through this architecture as you go, along the computational graph. The. Neurons, let's say, let's call them neurons for now the perceptron or whatever like the components of this layer. Talk mostly to the components of the next layer, and then those components talk to the components of the next layer, right? And so on, until the end, so layers are kind of this. Six, sequential slices of the computational graph and I'm deliberately not really trying to make it formal or anything. Because in reality, it's a Mercury concept, right? So yes, sometimes a layer in it is characterized exactly like this but sometimes you would have something like a skip connection for example. So we will see in our class, we will see networks. Where there are connections, that go around the layers, we will definitely see around the earthquake player, one to layer 3, and we will definitely see connections that go around even layer and just not touch it. That would be the residual connection and we will definitely talk about those there. One of the most important ideas here Car. But anyway the notion of layers is useful and the first, the easiest today, the most straightforward class of architectures are the fit forward or well. Okay. Fit forward is more general term but let's say fully connected Networks Fully connected. Networks. I don't want to make a big topic of them because there is really nothing to say. So in a fully connected Network, you have layers Every layer is a set of persons and this time it works exactly like you would expect. So the percept runs inside a layer, don't talk to each other. They talk they receive inputs from the previous layer and then they send out puts to all New Orleans of the next layer. That's that's what it means. In this case to be fully connected. It's not a fully connected graph, but it's a fully connected by part-time graph between everyone of between every pair of and then probably all comes together in a single, or, at least a smaller amount of perceptrons on the other end and that, and that gives you the output. Right, or whatever you want. Okay, so fully connected networks, they were important. Fully connected layers are still important you, if you will see a fully connected layer inside the transformer, for example, when we get the Transformers But today, we start discussing a more interesting kind of architecture. Slightly more involved kind of architecture and that is convolutional neural networks. So, what are convolution on your own networks? What is the What is the basic idea? Well, This is one of the last time, I think in class, maybe there will be one more time, but that's it. One of the last times in class and I will actually Go back to the biological motivation of everything that's happening, right? So we discussed how artificial neural networks. For how artificial neural networks were inspired by the human brain or by the animal brain and we discussed how the principle of connectionism actually works. But oh, and by the way, I think we didn't discuss it. So let me just take a very quick detour here. Let me give you a very, very short remark. We discussed gradient descent in neural networks and all artificial neural networks today are trained with radio in descent in one way or the other. So, it's different is not in the basic principle, the differences in the form of the laws function, from the form of the training set. Maybe this definitely the architecture Etc but not in the basic principle of this. Solving an optimization problem, right? You have lost function, you have a way to compute this gradients and then you use this gradient. Stop to my Oh, here here is a funny thing. The brain, the human brain cannot work this way at all. And that is kind of obvious when you look at the biological structure that we discussed. So even without actually understanding how it works even without actually knowing what the mechanism is, you can definitely say. It's not gradient descent. Why? Because as we discussed the biological neuron, this little guy has a lot of dendrites coming out of here, right? And the little guy also has a single Axon That is the output. Of the biological neuron, right? And that's it. So, a biological neuron and compute only one function. And to have gradient descent. You need every note in your network to compute at least two different functions. You need to be able to go forward, but you also need to be able to go backwards. All right, and I told you how to implement your own note in the computational graph and pytorch. What would you actually have to do is you would have to implement to procedures, f-pro, forward, propagation, and be prepared with propagation. How, what, what the function actually does. When it goes when the computer, and what are its derivative how it's the gradient should be computed as you do back propagation. Well. Here's the thing. The biological neurons and neurons in our heads cannot do that. They only have one output. so, What this actually means and this is this is an even deeper point and then it might seem so. Okay, they cannot upgrade in the sense so they have to do something else and all. So what it means Is that this something else that they do? Also has to somehow. and the signal back from the And from the point where the loss function is actually computed. I mean, I don't think it's ever is explicitly. Computed in our brains, but somehow, like, at least theoretically it's there. So between The end, the end goal and whether we achieved it or not. you need to have a connection from there from from the end of the chain to every neuron Out there. Right. So You need to. You need to. You need to have a Loops in, in the human brain, you need in the biological brain, you absolutely have to have connections that go from here or but back here, but there and everything you have to have a lot of feedback in the brain or train. And the brain does have hit back. Alright, so here is here is where the analogy like totally and completely ends. So we discussed that one. Neuron is actually a pretty good model of what's happening in the brain. One perceptron is a pretty good model of the biological neuron, especially with railroad activations. We discussed that PS that our brain also works on the principle of connectionism. That is a huge composition of simple functions. Gives you something can give you something very complicated but but It cannot run, gradient descent definitely. So and the architecture cannot be similar at all. So the brain also has layers will say it just now but Between every two layers there are feedback connections that go back and from later layers, they're a bit but connections that go all the way back it. I mean, it's a mess. We really don't really understand in detail how the brain, what the brain's architecture is, we understand it generally in terms of well this is the visual cortex in here at the layers in the visual cortex but they actually finds structure is very very difficult. Of course. Okay. So with that, remark out of the way, let's go back to this guy's this guys are Fuel and with all Torsten Wiesel and I forget the name of hubel who were to go there in a well price for studying the visual cortex. and, Convolutional networks are partly motivated by the visual cortex that's why I'm talking about this. But again there will be a point where the analogy just have to, we'll have to stop, I'll tell you when it happens but first let's begin with the bio. So back in the I think 1960 just they made their famous status of the visual cortex and is it quite often happens in biology and scientists like this. Their actual like truly Noble thing that they did. Was having a new device. So what they actually was what their advantage was compared to everybody who was before, that was that they could actually make such tiny electrodes. That you could attached the electro to a single neuron and rid of the activation of a single neuron On a live brain. Okay, so before that, all the people could do was, you know, hope that some guy would get in the motorcycle accident and then have a stroke and then the stroke will will give you some interesting information about what which part of the brain does. What? But this guy's they could actually well. Okay, this is this is not my favorite part but they could take a cat. If you look closely. There is very well. Fixated cat over here and then they would actually slice open the head of the cat of course, on painting orders. And then they would be able to actually throws to individual neurons and see what the individual neurons in the cat's brain actually respond to Ah, and what, what they did. So what they found was that, okay, so it had been known that the visual cortex is back here in the occipital lobe in mammals, in us. And in cats, it's actually a very bad decision of nature. It's it's a very fragile thing that makes absolutely no sense because your eyes are in front over here. And then, there is this optical nerve, this big fat, pile of connections, that goes all the way through your skull backwards. and, Of course, it will be easier to just have the visual cortex in front, but I think the evolutionary explanation is that back when we were very far from animals, we would have like the Proto eyes up here on top of on top of the head. And then somehow, the ice went over here and the part of the brain that processes that went over there. I have no idea why Anyway, it is known that the visual cortex is here. The part that processes visual input and it's easy to find like the first layer of the cortex. It's easier to see that. Okay, here is where the optical nerfect. So these neurons take the immediate inputs from the ice. And if you actually look at what a single neuron activates for, what a single neuron is doing on this first layer of the visual cortex, you will see that first of all, it cannot, of course, see the whole picture. It has only that many inputs, and it's basically a small, a small receptive field as it is called. It's it looks at a relatively small part of the of the general picture. And in this small part it recognizes something really, really simple. So on this slide is a simple neurons recognizes like vertical lines. So if it's a bright vertical line in its field of vision, great, it's activated a lot and test even even if you still have just single and but you start to rotate it, the activation days out and basically goes to zero, and then, what would you expect next? Well, you would definitely expect that. Then you would have player two, the second layer that would feed off the outputs of the first layer. So it would somehow Combine. The This simple shapes into something more complicated. Like if you had one neuron that recognizes vertical lines, another track recognizes, for example, lines, boom, you put an end, you have a neuron that gets and across them and oh, you have in your truck recognizes across and it's an Interceptor filter and visual. If you feel the fish. and people did this and they also started the second layer so they discovered neurons, like I just said, but then, They somehow didn't go any further and they, they started to other things. And actually, that was a pretty wise decision because again, the brain is very, very complicated. And if you look at some simplified representation of the visual cortex, you will actually see that they are Like layers from V1 to V4 then V5 V6, etc, etc. And yes, there are layers, but it's not an artificial neural network. The actual structure is much more complicated. There are, there is all sorts of feedback that goes back there, all sorts of connections. And, yeah, I keep showing this picture for the last 10 years or so. And I suppose that, since the last 10 years has become much more complicated. So, this, this is from somewhere in this picture, was called the most important neural Pathways in, in the visual, in the early layers of the visual cortex, so you can actually see that. Yeah, there is a very well defined first layer. Yes, the the optical nerve does come in somewhere. So, the first layer is easier. The second layer is also kind of clear, and then it's just a mess. Then it's like a lot of different components that do different things. There are all in interconnected with each other. Anyway. Anyway. When people saw that. When they saw how. Small geometric shapes. Regular. Go up layer by layer and we didn't have a clear picture of what happens next to that point. But clearly at some point, the picture would go to something like face recognition, right? So, some very complicated, computer vision problems would be soft in our human brain very quickly. So people, of course, try to imitate stuff like this in computers and Actually convolution and convolutional networks are very well Stadium. They date back at least to this very interesting architecture called the Neo cognitron. By the Japanese researcher named, he did it in the late 1970s and I actually if you're interested in the history of preparing actually, recommend you to read the papers, it's like it's a two-page paper, it's very short and you can definitely read it. There's nothing to complicated and there and When you read it, you see that? In 1979, he had a deep neural network, several layers. It was a convolutional network. and, it had real work activations, the this hinge activations that we discussed last time and that I told you were only only came into common practice in 2011 or 12 But the thing, the thing he didn't have the thing, they didn't she didn't have a 1979 was learning. So there was a big composition of simple things, and they work on relationships, but they were not trainable conversations. They were just some fixed filters that he would apply across the anyway, whatever. So, in modern formulation on networks appeared, in the other ones group, that's the main claim to fame by Young. He developmental networks for many, many years for several decades, and in the late 1980s, they appeared already Certainly. In. Their modern form, they had training, they had conversions and everything. And let me just walk you through a few images that will show. How convolutional networks work? and it's an it's such a brilliant idea that It's oh, okay. It's just a brilliant idea. It's it's a very brilliant idea for what I would call structural regularization, you'll see what they mean. so, first of all, Let's have a picture like this one. And let's assume that I want to process this picture. So what do I mean by processing? Well, maybe I want to solve some computer vision tasks. Maybe I want to, for example, find the little boys head on the same image, so where that would be objective actually. We'll discuss object actually later. So where is the the boys head and the image? And the main observation. The main idea of the main assumption that that is behind CNN's, that is behind convolutional neural networks. Is that? Well, if I'm looking for something, for some feature on an image, Then. It's the exact same function. Applied all across the image. So if I have a black box that looks at a small window and says, well, that's the boys have or no, that's not the boys head and it'll be the exact same black box. That I that I'm supposed to apply across this whole big picture and just output will be different. So here it will say yes. And over here, it will say no, but The function is the same as the inputs are different. So the outputs of course are also if So the idea of conversion on your networks is this, let's take a picture or anyhow and input is just easier to more, you know, more clear to reason about pictures, but they can input break it into small Windows like this. Usually, they are overlapping like shown here. and then, For every tile like this one. Apply a small neural network. So now, this small neural network is a model that we need to trade. It will have weight there. We will, do gradient descent etcetera, but it will be small, it will be applied, only to this little tile a few pixels across That we split the picture enter, right? And the big game here, the prophet is that. Now I take the exact same. Small neural network. And they apply to every single tile. Across. The input. So I take this style, I applied in your own network. I get this let's say output Vector. Usually you would want to extract, not one feature. But several features, usually the output is several numbers. and then I take the next style I apply, I get some some more I am. So when I actually do that, get back to the board when I actually do that. What I get as a result. So here is my input picture. right, I break it into Windows like I showed and then I take each window. Okay, yeah. Okay, let them be overlap and whatever I take each window. I put it through my small, neural network and let me draw it. Horizontally, I get this Vector features, right? Then I take the next window over here. I put it through the exact same, you know, Network. And I get the different Vector officers. That goes here. Okay. Now this will be a mess with a picture. But anyway, as I take each one of this windows, I get I get to Vector of features. And then so forth these factors are features themselves. Also have this geometric structure, Right. So there is a top right window. There is a bottom left window and the bottom left window. Will give me this bottom left, Vector features, and so on. Right. So as the output of this procedure, I will get a three-dimensional tensor. Right? I will still have some width, some height and now I will also have a meaningful depth. So actually the input also usually has steps for example, because these days for the last few decades, pictures are usually in color. So even if even on the first step, if you have a color image you have the three at the right but in general what you get at the output of convolutional layer is a 3D tensor if you start with the 2D input in structure like a picture, And then you can do the same thing, right? So again, you take it, speaks holes. You take this structure over here. and, You. Try it with Windows. With small tiles. and then you take this small substances are the small window out of here and the opposite through the through another small, neural network and you get another Vector of features. And again, you repeat this, this was the top left Vector of features, but then you get another test. And so on and so forth. It's, I'm sorry, I'm not in the convenient place. Very nice picture, but I hope you understand what's going on. So, on every step we Tile the image into tiles like this one. It doesn't have to be the original image. You can change this layer's one after the other because Always you're working with like three-dimensional race, you're rich and declaring car, confusingly content, but what can you do? So you're working with three dimensional tensors. and, You just convert one 3D tensor to another as you go with this procedure. and then, Then you can have like, a whole sequence of this convolutional layers. Okay. so before we proceed, one more thing about this In classical, convolutional neural networks and then many architectures that we will see. Today, there is a Another type of layers like there is a convolutional layer. That's the one that we just discussed and then there is also what is called the pooling player. And let me maybe first, give you the maturation for it and then the actual layers is actually pretty simple. So the motivation is this Let's again, try to look at. What? The neurons do. So this is our original image. And it has lots and lots of pixels, right? It's it has big width, big height. Then. I slice it into very small tiles. So of course on my picture, they're not small, but in practice, there are small tiles. So I have this style of let's say three by three picks holes and it's a color image so it has depth 32. So it has a small height, a small width, and then it goes through the neural network and then, We get our Vector of features. so, This factor of features this one. Depends only on this small small three by three tile. Right. so, if if you look at it from the, in the other direction, you can say that for this feature, this feature, Has a receptive field. It's called in this part of science receptive. Field has a receptive field of three by three pixels. So yeah, it only looks at a very small, very local, part of the image. All right. So what happens next suppose that I cover? This. Whole image with three by three. Windows like this. And then in, as a result, I will have a 3D tensor like this. And then I do another convolution I do another three by three conversion over here. Okay, so I cut off. I cut out another three by three by something. Now the depths from probably more than three. But anyway I cut out another three by three by D tensor and they put it through a small neuron Network and so on. I get the feature over here. What is its receptive? Well, it looks at this. Features inside this. But a little bit, right? The features inside this small part of the tensor. And these features in turn. Are looking at more pixels than before, right? So if I had three by three over here and another three by three over here, Which those two ones here. So now like this guy corresponds to this, And this guy corresponds to a window over here. Alright, so overall Overall. This pixel over here would look. 85 by 5 window in the original pixels, right? That that's my point. So if you do a three by three and then there is also if your three by three you compose in another Shiba, three then You collect information from a 5 by 5 in the storage, right? But if it's a pretty small windows, So like, how many layers would you need? so if neurons that look at the whole picture, On every, on every three by three conversational layer, you just add two to the tweets and you don't multiply by it too. Just add to do it and add to the height of this receptor showed, right? So, if I want the process and 2:56 by 256, same, which I would need like 100 and 130 layers, that doesn't make any sense. I don't want to have that many layers. so, so in the original convolutional Networks, You would somehow need to solve this problem. That is you would need to reduce the geometry. And this this is an important way of looking at. We will talk about reducing the geometry or what in this class. But you you want to reduce the geometry quicker, then by just dialing, everything and hoping that, you know, convolution will do it by themselves. So, in the original neural networks in the relationships, they had And you can see today in some architectures and they had this idea of a pooling clear. so let's suppose that I had a convolutional year extracted some features and then I can say, well, you know, there are too many, The Beatles hide her to be. I want to reduce the geometry. Oh, there it is. The temperature. Well, I could just Slice it into small Windows. This time. No overlaps. That's the whole point. No, overlaps, usually, it's two by two in those but of course you can set whatever you want and Just replace in every 2x window. Out of four features. Leave only one. According to some rule. Right. And there are two commonly used roles. I think anything else. Just reduces basically one of these two in effect. So there is max volume where you take the maximum of the feature really is in this small window and there is average pulling, very average them I don't think I've ever seen anything else in practice and usually, it's Max bowling. So usually it's Max pooling. Why? Because it kind of makes sense for feature extraction. So, okay, so the real answer is because it's works but usually, but they justification is that like it urges kind of layers to actually extract more meaningful features. So if you, for example. So let's look at this picture and let's say, okay, so I want to like however, A black box have a feature extractor. That says, is there a little boy's head in this in this style? And so when I run it on this style, I get a one right. But when I read and say on this style or on this tile I get basically a zero even if it's like perfectly understands everything. So then, let's suppose that they have this bigger tail, that combines the small tiles over here. That Glues them together like pulling this. And then I asked, well, what is the proper? Composition. What is the proper combination of features that will answer? The question is there? A little boy's head in this tail and that would be the max, right? If I ever actually get some pretty low average because most tiles don't have a little spray head, right. And only one tile would have the little boy's head and the rest wouldn't, but but like meaningful features, like something is there they obey the max flow, right? And last meaningful but sometimes also useful features like how green it is. This feature would have made the average for right. If a have a big tile delicious half green and half blue, I would probably want to say that it's half green. It's not fully green but for like features corresponding to objects or whatever shapes. Max is usually the way to go anyway that that's just a rambling justification of why max volume. All right. And so now, When you combine when you come by convolution know and fooling clears, you can start using the geometry really quickly, because every pool in clear. Cuts the width and the half by two. Let's assume it's 2 by 2 pulling. It's almost always so better pulling. So every pulling clear cuts the width by two cuts, the height by 2. You get twice, you get four times. Fewer pixels for four times, your numbers, and then you can do another conversion, blah blah. And so so at this point, at this point, what I want to do Is. I want to. Actually discuss how you would Define a convolution like what it actually is. And then we will just work through an example where oh, just and we would just work through an example, where we would eh the beauty of convolution, where we would actually Like realize. Why can't I save so much? Why why? There such a great way to process large inputs. So what exactly what this neural network be? Yeah. Well the like the Deport, convolution Doesn't really mean anything specific. It just means that I trial a tiled, the input with small tiles and I apply my transformation to every tile separately. So this is what the word convolution means. It doesn't tell you what exactly this transformation should be. But usually, when people talk about volitional layers, they mean the simplest neural network possible. The simplest neural network possible. That is just one fully connected layer. So, it looks like this. I have my input. Now let me do it and full generally. So I have a 3-dimensional input. It has some wheat, capital W, some great Capital, H, some tips deep. And I cut out. ASAP subset a tile. Which has a width small W and height small age and still. So this is also important. I always cut Through all the features. I take all the features. All the depths so then, I take this guy. And basically I say well okay here I have like a d times. W Times H tensor, right? I have the three dimensional Matrix of three-dimensional array of numbers, right? But when I go inside this neural network, I don't care about the structure of this array. I just lose it. I just say, okay, so I have this many numbers. You can actually visualize it. Is flattening it to a single Vector of size dwh. and then, I just Apply a matrix of waste it. I have some Matrix of Waits so the output will be a vector of size. Let's say d Prime and this Vector of says, the prime is Vector of size. The prime is just W Times this day. Okay, so the Matrix W, how many weights does a convolutional layer have? The Matrix W has a supposed to have like Supposed to be okay, so just to make it more convenient, let's say it's Z times W. So w would be like, dwh times D Prime. Okay. So, it would be dwh times the prep. and, And then and then yes, sir, it was my trainer. So it's a little Time is the prime. Yeah, and then the beauty of convolutional networks is that now when I take another window over here, I also have an input of the same size and I reuse the exact same Matrix that I believe. Right? So this many weights are needed to process the whole image. I don't I don't have a different W for a different window. Have the same w, i reused the weights. So these many ways are needed to process the whole D times. Big W Times Big H, input. And as you can notice, the number of ways doesn't depend on the size of the input, it only depends on the size of the window. So when I have a convolutional layer, it's very easy for me to say. Oh, okay. So my, my input image is now twice larger but let's just run the convolution across the larger image. I don't care. I only care about the size of the window. and of course, Formally. And like, in reality what you have here is a matrix of this Dimensions, but it would be very, very inconvenient. If we humans had to think of this matrices is, you know, some huge number times D Prime. And then this huge number we would have to memorize and think of, oh, okay, so that was like three by three by 32. How many is that all this? This should be the size. Of course, that's very inconvenient. So in practice, if you for example, set up a convolutional layer and pytorch, it wouldn't be a 2d Matrix. The convolutional the convolution would be defined by four dimensional tensor. So your tensor of Weights would have size. D times, W Times H times. The prime And what would actually happen is your input. Is a three-dimensional tensor. Which is supposed to make the first three dimensions of w. And that means that your output is a vector of this damage. Okay. Uh so in practice, you would Define like four dimensional tensors when you when you set up convolutional layers. and by the way, While we are at this while we are defining this note that it is absolutely positively. It's absolutely positively, doesn't matter that the input is specifically a picture, that's specifically, is like a 3D tensor with some, with some height, and some depths you can surely have convolutional networks for other kinds of inputs, for example, at some point. Now, of course, nobody the test is, but, at some point, You could. Never see announced design for text process. And what is text is a sequence, right? It's a sequence of tokens and every token gets represented by some Vector. So it's a sequence of vectors, right? It's a, it's a 1D object, one dimensional object that produces a two-dimensional input tensor. And sure enough you can have one dimensional convolutions no problem at all. You just adjust your windows are now sliding Windows like this. You take like Three neighboring, vectors. Your small input is like this. It's well it's D times length of the window and then you multiply it by The Matrix W which now is a three-dimensional tensor D times, L times D Prime and you get The result, which is a vector of safety prep. Almost no difference at all. Just all all Dimensions change by one. That's or you can go in the other direction you can say well, but what if I have, let's say a video. I have a video which means that I have a sequence of images. So now my input is like, d times W Times H times. Let's say t for time, right? If this is a video. So now they are, there is a sequence of images and every image is a W Times, H times these tensor and of course you can multiply it by 5 dimensional transfer, which is cheap times, W Times H times, T times the prime that's it, right? So You can apply the same idea of cutting stuff into small tiles and processing digital separately. You can apply it to anything. It just so happens that it was especially productive for images and basically all of the examples in our class since it's a computer vision. Quest, of course, all of the examples in our class will be will be images. Okay, so Okay. Okay, so with this, let's maybe look at a specific example. Let's look at the specific example, over convolutional Network, yeah, this one and I just want to Go through this network layer by layer. It's some classical learning architecture from, I don't know, 2001 or something. It's very small. It's very small input, not very powerful but I want to go through the circuit texture to count the weights. To get a feeling of what convolutional networks look like and we will see like what's the whole point of conversation when we just asked how many ways they have. so, So let's look at this slide. What do we have here? We have the input, which is a 32 by 32 picture. And it's a black and white picture. Well, a gray, scale it picture so it has depth one. so, our input and Let me. Switch from from the picture to the board for a little bit. So our input is a tensor of size 1 times, 32 times 32. Okay. Then. You layer happens. And this picture doesn't show you the weights, doesn't show you the layers themselves. It shows you the intermediate results, the dancers that result from every layer. so now it's says that after the first layer you have when 8 by 28 then sir. We see six feature Maps, when people say fisher Maps, it's the same as channels, the same as depths. So basically it says that it's a twin but 28 by 6 and 6 different features, ah, so we started with a 32 by 32, by one. Then. Something happened. I can relational layer happened and now we have a tensor of size 6 by 28 by 28. so, the question to you, how large do you think was the convolution? What was the size of the window? If we went from 32 by 32 pixels to 2828 pixels, why would, why would they geometry be reduced? Why would the conventional Network actually have less pixels at the output? It. So I am covering the input by overlapping tiles. All possible tiles. How many tiles are possible. Okay, so this is this is our first remark here. So I have this input which is like 32 by 32 pixels image. Course, I won't draw the full 32 and then I start covering it by tiles of some kind of size. Right. Let's say three by three tiles. but, How many tiles will fit? Not search up by search too, right? So, You see for every time every tile is defined by its centerpiece. So let's say, right? So this Center pixel corresponds to this three by three window usually it's what they're very few even convolution. So I I am safe talking about the center pixel. So there is a center pixel corresponding to the three by three tile this Center pixel corresponds with 333, so on. But there is no tile that will correspond to this pixel, right? It doesn't fit. so, in effect, How many if I had a 3 by 3? Convolution, The output if I just do the tile and if I just use all possible tiles, not use any special tricks here. The tiling would be would would not be able to use this pixels. And also wouldn't be able to use this pixels, right? So it would cut off one pixel, on top, one pixel, on bottom, one on the left, one on the right. So, if I did a three by three convertion, and I had like a W Times, H image at the input. I would go to something like that. Will you minus two times H, minus 2, right? Because I would need to cut off. Two, picks rolls on the sides. Well, here we go. To w minus 4 and H minus 4. So, how big was the windows? Yeah, exactly. So I mean, of course it's not guaranteed, there could have been tricks, Etc, but the most plausible version of how this convolution what this convolution looks like, judging by that picture and it's true. In fact it's true, is that It was, we were covering. The input by 5 by 5. Tiles. And then, so, what what is the size of the weight Matrix here? Yeah, I didn't tell you that. Sorry I am when I talk about the weight Matrix I of course, simplify a little bit because in addition to the weight Matrix there is also the intercept. So in fact, of course, this output is like Z W plus some constant. So there is an additional deep Prime. Wait, which is also wait, right? I wish we should also trained, but let's forget about that. It doesn't matter for us. Now let's just count the way to the Matrix system. So What would be the Matrix size over here? The Matrix size would be as we discussed their D times, W Times H times D Prime, right? So here we have a conventional weight Matrix weight tensor of size 1 times 5 times 5 and we have six features at the output time 6. Right. So five, five by five is 25 256 150, right? So, over here, in this layer, we have 150 weights Trainable. It's that we will need to learn. By gradient. Well, there you have it. That's that's that's the first point that I want to make this example. The convolutional idea, the idea of sliding a window over the input. Saves, if you amount of weights. So, suppose that I need to have a fully connected layer over here. Suppose that I just want to have a single weight Matrix that takes. This guy is input and outputs this. Then how many weights would I have? What? What kind of Matrix would? It be a fully connected? First layer would be like, 32 times 32. Times. 6 times, 28 times 28. Right? So it would be a matrix of size input times, output. Input size times. Output says, if I didn't have this conventional structure and I still for some unfathomable first, enable reason would want to have this kind of output. The Matrix would have this kind of says, So, of course, I cannot do this in my head, but like, 30 to square this about a 1000. So this is like, you know, five million or something you can count if you want, but this like several million Waits and the convolutional idea reduced this five million ways. Down to 100.50. So that this is the the power of convolution, the main power of convolution. They save a lot of weights. and that's why I always say that what convolutions actually are, they are an excellent technique of structural regularization we discussed last some previous lectures that regularization is when you Regularization is when you compress compress the weights, Magnum smaller, or it use like reduced the set from which the weights are taken, right? But in this case, it's even more straightforward extraction means. All right? So I have five million ways. And you could like, if you think of it from a proper view, it from a proper angle, you will see that you can actually think of evolutionary or so as a transformation of this guy to this guy. But when I do this transformation, I say, oh okay, so I want this thousand of ways to be equal to each other. And I just said, this constraint that. I always process every window beat over here, or over here, or over here. I process it in the exact same way, with the exact same ways that. So that's structural organization. When you impose constraints, like, this way, it should be equal to each other. This way should just disappear or something. So, so, So this is the power of the violations. And let's so let's finish the exercise that there are still a couple of points that they want to make here. So after the first convolutional layer, There is a pool and clear sub. Sampling is the same as Boolean clears as synonyms. So the pool and clear is obviously has two by two windows, right? So we go from 28 by 28 to 14 by 14. Question to you. How many weights? Does this pulling clear have? I had the sick 28 by 28 by 6 input. I have four seen my fortune by 6 output, which means that. Okay. Let's assume it's Mark spawning. I don't remember which was actually, but I take two by two window. And in every two indoors every feature I take the max of these four numbers How many ways is that? How many trainable weights? So, the pulling transformation takes the input. Cuts it into tiles. And for every tile you take the numbers that are parts of your input and you leave only the max of these numbers. Right, you take a two-way to window. A little bit of a window becomes just its maximum. How many trainable weights are in transformation like this. Yeah. All right, I'm not talking to me today. Anyway, how many ways are in this transformation? Of course? None, of course, there are no weights, it's a deterministic function. There is nothing to trade. They just take the max Right. So the The. Pooling clears. Don't have weights. There is no no point for the for them to have weights. There is nothing to train. I just do a specific fixed thing. so, Okay, so let me draw this next, I have a clear. a Poland player goes to 6 by 14 by 14. The pooling. Clear has no. It's and then I have another conversation there. Right. Check, I have another convolutional layer that goes down to 10 by 10. so, Sorry, check 10 by 10, by by how many 10 by 10 by 16. so, my next Generation layer goes, Makes it. Like this. 16, right? And by 10. So I I put depth first here but you have to, you can put it very one. So how many ways are here? Well, again, we reduce the width and the height by Four. So it's a five by five convolution but now we need to transfer translate six features into 16 features. So let's see. Bye bye. 555 by 610. Okay, that's more ways, right? So we know six by five by five phases, 150, and 150 times 16. I want 50 times 4 is 6. So 6 times 4 is. 2400 rates. Right, I suppose that's correct. 24th 2400 rates over here. Okay, then another pulling this part, I remember. And then we get wait for it. There will be a little bit more interesting stuff here. So now I have like 6016 by 5 by 5 and that this point, I say, oh okay so now I have a five by five. Tensor with depth 16. So, if I keep doing five by five convolution, it means that now there are no tiles really. Like the whole answer is a single tile. I don't have to cut it any longer, which means that, okay, in the picture, they call the convolution layer, but now it really doesn't matter. You could call it a conversational layer or you could call it a fully connected layer. You just take the whole input. And you convert it to okay. How many Features. So next you go to 100 Fishers then 84 features and then finally out of 10 so, you go to 120. Then another fully connected layer. You go to 84 And another fully connected layer, may be a softmax layer. You go to 10? So, how many ways are here? Well, in this fully connected layer, I have 16 times 5 times, 5 times 120. Right. So I compress the whole input down to the vector and I just lose all the geometry. Don't care about the Germany anymore. This is just Global features numbers about the, the input image and but I still need to You know, do stuff with them. I still need to toss them around a little to do some linear combinations of them to actually extract the signal. That I want, not just reasonable signal, but signal that I want to actually get to get to the the classes, for example, that I want to recognize So off in classical, conversational networks, after you go through all of this layer. So after you down sample and downsample and Sample at the end, you can have a couple of fully connected layers. Usually it's sometimes it's called the head of the network. Head. And sometimes our networks will have multiple heads that the different things. But for now let's just say that I do need to have some kind of a classification at the end with a couple of connections. And interestingly. It turns out that this classification head? Holds the vast majority of all the ways. You see? So over here, we have like, what? 400 times 120. We have 40. 8,000 weights over here. And here we have 120 times 84 which is I don't know about 10K more. Right. so, Out of the total. 60,000 weights on this network about 60,000 about 57,058,000 why in the classification head? And only. Two and a half thousand weights are in the convolutional layers. But the convolutional layers. Are doing the most important job. They are the Fisher, extractors. and, So how does it actually work during training? Oh, remember how we just discussed. Remember how we just asked that propagation. So, if you have a single input, go in into several different places, then in the graph, then when you Go back to the back problem. Bye, propagation, here. Your update, your gradient will be by the chain rule. The sum of Not the great agent. They partial derivative of this note will be by the chain rule, the sum Across all of the paths, right? And in the convolutional network, every weight over here, every weight in this convolution, in this Matrix, Occurs in the computational. Graph is input into the computational graph, many, many, many, many, many, many times. So I don't think they can draw a competition graph for it here. But basically, like this, you have this input, right? In the input. Every pixel is a value. Let's say, and Now. Let's let's suppose that this weight, like wi gets multiplied by the way, you of, and no middle, right? Pixel in the three by three window. which means that when we process this window, I will multiply it by this pixel and then up and everything. when I process this window, I will multiply it by this pixel so and then up and everything. So the same way, the same input to the computational graph will occur many many many times. For on every it will occur in the processing of every every single tail. by by the nature of and that's why, by the way, real activations. Are such a good fit here. Because this means that we don't mind sparsity. Sparsity is bad, if you have. Little signal. If you don't have enough signal, if you don't want to lose anything but sparsity is great. If you have an abundance of signal, if you have a lot of computational paths now, sparsity just saves, you time. It doesn't really, it doesn't really hurt. You doesn't really hurt train. It just says that. Oh, okay, so like in the processing of this window, doesn't matter right now. So this guy will be 0 and this part of the graph should not matter, but the processing of this window will still matter. So this way it will still get the meaning for update. So usually when you have the same way the current and many, many different places, it's it's a good idea to its some sparsity and really provides this kind of first Okay. So what have we discussed so far? We discussed the basic idea of convolutional networks. How you slide across the input. We discussed how the receptive field, grows this time, that it grows not fast enough, and that's why you want to have pooling from time to time, pulling layers, we discussed that We just discussed that you can apply convolution to inputs of other dimensions, to inputs of other different nature. It doesn't matter. As long as you can tile it with something, you can do it on that. And we all went through a specific example. Oh if I honestly think I need to go pretty soon. But before before we close let me just tell you a couple more practical tricks about how can I actually work? Because you will need them and practice and you will need them to understand but what goes next? ah, so, um, trick number one. Let's go back. to this, like, Input tensor, this time I will not be drawing the depth. So let me just draw it as a two-dimensional grid. Like this. and, What am I doing with it? I'm dialing it by let's say, three by three windows or I'm telling it by three by three by three windows. And as we just discussed, Every time. That I apply three by three. Convolution, not. Every pixel can be the center with 3 by 3 window. Right? So we just discussed that if I when I apply conversions by just by overlapping everything and feeding as my as many as I can, well I I can't fit, oh I can't fit as many tells us there were pixels. And sometimes that's really inconvenient. So sometimes what you really want is you want to preserve the shape of your tensor. So if you had D times, W Times H is input. Then after a convolutional layer, you would have a d times W minus K times H, minus k. And I don't want this minus case. I want I want to have a tensor of the exact same shape, it will be. For example, I want to have like adults and such convolutional layers in a row. I want to repeat this, I want to Stack the same layers and I don't want to change the image. oh, when that happens, what you actually. Want to do, is you want to use? So cold in. Just means that. Suppose that I need to have this pixel also be the center of a three by three window. So I draw a window three by three and around the specs. So and I know just that it goes out of the image, right? Well, why don't we just played it. Let's say we zeros. Just say that this pixels are zeros, that's it. And now that would be 0 padding. and now, We are not, and now we are done, we can preserve the size. So that's just stupid practical trick to pad the image with something in order to be able to fit more. Windows. And so there are two common ways to do painting. One is paid with zeros and the other is let's say I want to Have a window like this so when you pay with zeros, there can be a strange effect. Like, you could have like a border around your image of some not really plausible features because this features take this lots of zeros on the side, right? So if you want to wait that you might want to have mirror painting, you may want to just take this, this guy's from here and just copy them by doing a mirror image of of your of your image over there. That's all available to the plating often people do that. okay, so but the whole point is To be able to fit more tiles, to be able to make any pixel in the input, the center of a tail. And one more trick. One more trick is this. so, as I said, if you just keep dialing your tensors with all possible tiles, You will not. Have. You will not have. You will not have. You will not have. You will not be reducing the geometry fast enough, it will have to resort to things like pulling clears. You have to reduce your geometry artificial Well. There is a different way, okay? Very, very simple. What if I just take? Not every pixel as the center of a tile? But what if I take like, every second Like this. So I have like the green window, the green three by three window over here. The light blue over here. The red one over here. and the dark blue one over here. No. So at this point, I have Four times, fewer tiles, right? I have cut my number of tiles in half. Across to it and then half across the height. So now when I get to the output from this, I will have a tensor of size approximately double w over to and they showed over to, right? Depending on the painting there may be some plus or minus ones but more or less like this So it's exactly the geometric effect that we have. No one will reduce the geometry, my factor of two. Right. On the other hand, know, just how? I am not losing anything. Like every pixel is still covered. It's just covered not as many times. So, before if I tile everything, then, like, this pixel is part of this window. And this window and this window, and this window, and this window and many different Windows over here. Well, now, the maximum number of Windows is 4 and usually, it's less like, this guy will only be covered by two windows two tiles but still every pixel is covered. Right? So we are not missing anything. We are not losing any information, the network is still perfectly able to get everything in process everything. So this is a reasonable way to reduce geometry too. And when it happens, it's called a straight. Straight. So, for example, this would be straight too. like if you don't do anything for this trade one, if you just dial With every possible tile. So when you so to summarize what we've discussed today, when you do it in, relational are What do you define? Well, you define the shape of the tensor. Like, did you stop W Times, H times T Prime, right? And DST steps of the input. The prime minister is the output. ah, you define the padding if you want to pad the input with zeros or something else, and you also Define the stride And for, I mean, nobody actually uses it. But formerly, of course, the stride is a two-dimensional thing because it's two numbers because nothing prevents you from going like every second pixel across the x coordinate and every third pixel across the y coordinate, right? It doesn't have to be the equal so formerly. It's two different numbers, of course, most usually there is the same but the stride defines, how you tile. Waiting also defines how you tile, and what do you add to the? well, what do you add and the convolution the the convolutional dancer the size of the dancer defines, how many features you get Okay. Okay. Well. I think, actually, actually, I think I want to stop at this point. So, I don't, unfortunately I have to go. Are there any okay, question, are there any downsides to doing this during the Straits? Well, Again, every pixel now participates in the processing, fewer types. so, maybe you don't want as much sparsity or something but actually the general the general, like trend of how convolutional networks developed, Was. As time went by, we did pulling less and less often so pulling actually has some undesirable properties. Pulling like cuts off, lots of computational paths as well, and pulling kind of distorts. The gradients, I won't go into details. Basically, there are bad side effects of pulling, and when we get to Modern architectures, you will see that starting from things, like, Inception, resnet, and some more involved architectures. You will see that they reduce the geometry, of course, but they reduce it with not exactly with a stride but they reduce it with like a complex sub-network that basically at some point does Australia conversation at some point. That's something like this. And then also that's something else. But we'll get there when we get Okay guys, it's been a pleasure talking to you today. Sorry that this lecture is a little bit messy, but I hope that I'll get settled by next week and we will continue. Thanks a lot and bye. Bye.
