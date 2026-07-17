# Transcript — whisper_cpp

- **Provider:** whisper_cpp
- **Language:** en
- **Audio duration:** 1:28:19
- **Segments:** 855
- **model:** ggml-large-v3-turbo.bin
- **vad:** True
- **beam_size:** 5
- **entropy_thold:** 2.8
- **latency_sec:** 723.62

## Segments

**[00:01 – 00:22]** Okay. Hello, everyone. We are continuing our discussions of deep learning and this time I am in a very noisy and not really comfortable place, but I hope that the combination of modern deep learning based noise removal techniques will work.

**[00:22 – 00:39]** And I hope you will hear me fine. I hope the recording will be fine. So, in any case, we stopped last time at stochastic gradient descent algorithms, right?

**[00:39 – 00:55]** So, basically what we discussed on the previous lecture was that, you know, a neural network is a big composition of little things, is a huge computational graph.

**[00:55 – 01:20]** And then, there are two different kinds of inputs for the neural network. There is the actual input, which acts like a picture. Today we will be switching to pictures, mostly.

**[01:20 – 01:31]** And then there are the weights, right? And yesterday, not yesterday, but two days ago, we discussed that

**[01:31 – 01:44]** the output of this whole computational graph would be the loss function, right? Loss function of x, y, and w,

**[01:44 – 01:55]** and there is also the correct answer that comes in probably at the end somewhere. And then what we

**[01:55 – 02:05]** actually do is we compute the overall loss function L, w, which is like the sum or the average

**[02:05 – 02:18]** of the small losses, of the losses on every step along the way. And then we do gradient descent, right?

**[02:18 – 02:28]** I'm starting with the recap because you told me that some people might do it. So then we update the weights

**[02:28 – 02:39]** with something like this, but not really. So we use something like this, but really we use something

**[02:39 – 02:54]** much more involved and complicated like, for example, the A-demovers. And that's how deep learning works

**[02:54 – 03:02]** in general. There still are a few general remarks that I want to make and that I will probably have

**[03:02 – 03:11]** to postpone, definitely not today, so I will have to postpone them probably to the beginning of next week.

**[03:12 – 03:22]** I still want to discuss weight initialization, which is a pretty interesting and nice topic in itself.

**[03:22 – 03:35]** And also I want to discuss normalization layers. You probably have heard of batch norm, batch normalization.

**[03:35 – 03:43]** There are several different flavors of normalization layers and what exactly they do and why they are

**[03:43 – 03:57]** necessary is also, in my opinion, a pretty interesting topic. But today we actually start talking about not

**[03:57 – 04:07]** in general what happens with the loss function still being a black box, but what happens inside

**[04:07 – 04:14]** this black box, right? So today we start talking about architectures of neural networks.

**[04:15 – 04:28]** The word architecture, in this case, basically means what's in here, what is the structure

**[04:28 – 04:38]** of this computational graph, and we already kind of know that it can be any directed acyclic

**[04:38 – 04:48]** graph, anything would work, and the only requirement is that first there are no cycles, right, so

**[04:48 – 04:53]** you need to be able to traverse the graph in topological order in one direction and then

**[04:53 – 04:58]** in the opposite direction, but also what we need to do is, what we need to be able to do

**[04:58 – 05:08]** is to do the elementary computations, the forward propagation and the backward propagation inside

**[05:08 – 05:20]** every one of these nodes, so the general picture is like this, you have elementary nodes,

**[05:20 – 05:27]** they constitute a graph, and you do one pass of forward propagation, one pass of web propagation,

**[05:27 – 05:36]** and you have your gradient, then all of these algorithms that we discussed last time, you can.

**[05:36 – 05:51]** So, this is the general picture, and immediately we can start just thinking about how this graph might be organized.

**[05:51 – 06:02]** For example, you could do it, and usually people do it, in a layered architecture, so there are layers, right?

**[06:02 – 06:18]** Onions have layers, and ogres have layers, famously, and what a layer means is that as you go left to right through this architecture,

**[06:18 – 06:29]** as you go along the computational graph, the neurons, let's say, let's call them neurons for now, the perceptrons or whatever,

**[06:29 – 06:35]** like the components of this layer, talk mostly to the components of the next layer,

**[06:36 – 06:44]** and then those components talk to the components of the next layer, right, and so on until the end.

**[06:44 – 06:53]** So layers are kind of these sequential slices of the computational graph,

**[06:53 – 07:01]** and I'm deliberately not really trying to make it formal or anything because in reality, it's a murky concept, right?

**[07:02 – 07:07]** So, yes, sometimes a layer indeed is characterized exactly like this,

**[07:08 – 07:13]** but sometimes you would have something like a skip connection, for example.

**[07:13 – 07:21]** So, we will see in our class, we will see networks where there are connections that go around the layers.

**[07:22 – 07:25]** We will definitely see around the layers from layer 1 to layer 3,

**[07:26 – 07:32]** and we will definitely see connections that go around a given layer and just not touch it.

**[07:32 – 07:38]** That would be the residual connection, and we will definitely talk about those.

**[07:38 – 07:40]** They are one of the most important ideas here.

**[07:42 – 07:46]** But anyway, the notion of layers is useful,

**[07:47 – 07:54]** and the first, the easiest, the most straightforward class of architectures are the feed-forward,

**[07:55 – 08:01]** or, well, okay, feed-forward is a more general term, but let's say fully connected networks.

**[08:03 – 08:05]** Fully connected networks.

**[08:07 – 08:12]** I don't want to make a big topic of them because there is really nothing to say.

**[08:12 – 08:16]** So in a fully connected network, you have layers.

**[08:18 – 08:24]** Every layer is a set of perceptrons, and this time it works exactly like you would expect.

**[08:24 – 08:28]** So the perceptrons inside a layer don't talk to each other.

**[08:29 – 08:32]** They talk, they receive inputs from the previous layer,

**[08:32 – 08:37]** and then they send outputs to all neurons of the next layer.

**[08:37 – 08:40]** That's what it means in this case to be fully connected.

**[08:41 – 08:45]** It's not a fully connected graph.

**[08:46 – 08:54]** But it's a fully connected bipartite graph between every pair of layers.

**[08:54 – 09:05]** And then probably it all comes together in a single or at least a smaller amount of perceptrons on the other end,

**[09:05 – 09:10]** and that gives you the output Y or whatever you want.

**[09:12 – 09:17]** Okay, so fully connected networks, they were important.

**[09:17 – 09:20]** Fully connected layers are still important.

**[09:20 – 09:26]** You will see a fully connected layer inside the transformer, for example, when we get the transformers.

**[09:27 – 09:34]** But today we start discussing a more interesting kind of architecture,

**[09:35 – 09:40]** a slightly more involved kind of architecture, and that is convolutional neural networks.

**[09:41 – 09:44]** So what are convolutional neural networks?

**[09:44 – 09:47]** What is the basic idea?

**[09:47 – 09:54]** Well, this is one of the last times, I think, in class.

**[09:54 – 09:57]** Maybe there will be one more time, but that's it.

**[09:57 – 10:05]** One of the last times in class when I will actually go back to the biological motivation of everything that's happening.

**[10:06 – 10:19]** So we discussed how artificial neural networks were inspired

**[10:19 – 10:22]** by the human brain or by the animal brain,

**[10:22 – 10:27]** and we discussed how the principle of connectionism actually works.

**[10:28 – 10:31]** But, oh, and by the way, I think we didn't discuss it,

**[10:31 – 10:36]** so let me just take a very quick detour here.

**[10:36 – 10:38]** Let me give you a very, very short remark.

**[10:39 – 10:44]** We discussed gradient descent in neural networks,

**[10:44 – 10:50]** and all artificial neural networks today are trained with gradient descent

**[10:50 – 10:55]** in one way or the other, so the difference is not in the basic principle,

**[10:55 – 10:59]** the difference is in the form of the loss function,

**[10:59 – 11:03]** the form of the training set, maybe definitely the architecture, etc., etc.,

**[11:03 – 11:10]** but not in the basic principle of this solving an optimization problem, right?

**[11:10 – 11:16]** You have a loss function, you have a way to compute its gradients,

**[11:17 – 11:19]** and then you use these gradients to optimize.

**[11:19 – 11:22]** Well, here is a funny thing.

**[11:23 – 11:28]** The brain, the human brain, cannot work this way at all,

**[11:29 – 11:34]** and that is kind of obvious when you look at the biological structure that we discussed.

**[11:34 – 11:38]** So even without actually understanding how it works,

**[11:38 – 11:42]** even without actually knowing what the mechanism is,

**[11:42 – 11:45]** you can definitely say it's not gradient descent.

**[11:45 – 11:46]** Why?

**[11:46 – 11:51]** Because, as we discussed, the biological neuron, this little guy,

**[11:52 – 11:56]** has a lot of dendrites coming out of here, right?

**[11:56 – 12:00]** And the little guy also has a single axon

**[12:00 – 12:05]** that is the output of the biological neuron, right?

**[12:06 – 12:09]** And that's it.

**[12:09 – 12:14]** So a biological neuron can compute only one function.

**[12:15 – 12:17]** And to have gradient descent,

**[12:17 – 12:20]** you need every node in your network to compute

**[12:20 – 12:22]** at least two different functions.

**[12:23 – 12:25]** You need to be able to go forward,

**[12:25 – 12:30]** but you also need to be able to go backward, right?

**[12:31 – 12:36]** And I told you how to implement your own node

**[12:36 – 12:38]** in the computational graph in PyTorch.

**[12:38 – 12:41]** What you would actually have to do is

**[12:41 – 12:43]** you would have to implement two procedures,

**[12:43 – 12:45]** f-prop, forward propagation,

**[12:45 – 12:46]** and b-prop, backward propagation,

**[12:47 – 12:52]** what the function actually does when it goes,

**[12:53 – 12:54]** when you compute it,

**[12:54 – 12:58]** what are its derivatives,

**[12:58 – 13:00]** how the gradients should be recomputed

**[13:00 – 13:01]** as you do back propagation.

**[13:03 – 13:06]** Well, here is the thing.

**[13:07 – 13:08]** The biological neurons,

**[13:09 – 13:10]** the neurons in our heads cannot do that.

**[13:11 – 13:12]** They only have one output.

**[13:13 – 13:15]** So what this actually means,

**[13:16 – 13:19]** and this is an even deeper point than it might seem.

**[13:20 – 13:23]** So, okay, they cannot do gradient descent,

**[13:23 – 13:24]** so they have to do something else.

**[13:25 – 13:31]** And also what it means is that this something else that they do

**[13:31 – 13:41]** also has to somehow send the signal back from the end,

**[13:42 – 13:44]** from the point where the loss function is actually computed.

**[13:45 – 13:49]** I mean, I don't think it ever is explicitly computed in our brains,

**[13:49 – 13:52]** but somehow, at least theoretically, it's there.

**[13:52 – 13:59]** So between the end goal and whether we achieved it or not,

**[14:00 – 14:03]** you need to have a connection from there,

**[14:03 – 14:09]** from the end of the chain to every neuron up there, right?

**[14:09 – 14:26]** So you need to have loops in the human brain.

**[14:26 – 14:30]** In the biological brain, you absolutely have to have connections

**[14:30 – 14:37]** that go from here or back here, back there and everything.

**[14:37 – 14:42]** You have to have a lot of feedback in the brain in order to train.

**[14:44 – 14:46]** And the brain does have feedback, right?

**[14:47 – 14:53]** So here is where the analogy totally and completely ends.

**[14:54 – 14:59]** So we discussed that one neuron is actually a pretty good model

**[14:59 – 15:01]** of what's happening in the brain.

**[15:01 – 15:03]** One perceptron is a pretty good model of the biological neuron,

**[15:03 – 15:05]** especially with real activations.

**[15:06 – 15:09]** We discussed that, yes, our brain also works on the principle

**[15:09 – 15:13]** of connectionism, that is, a huge composition of simple functions

**[15:13 – 15:16]** can give you something very complicated.

**[15:17 – 15:23]** But, it cannot run on gradient descent, definitely.

**[15:24 – 15:27]** And the architecture cannot be similar at all.

**[15:27 – 15:30]** So, the brain also has layers, we'll see it just now,

**[15:31 – 15:35]** but between every two layers, there are feedback connections that go back.

**[15:36 – 15:40]** And from later layers, there are feedback connections that go all the way back.

**[15:40 – 15:41]** I mean, it's a mess.

**[15:42 – 15:47]** We don't really understand in detail what the brain's architecture is.

**[15:47 – 15:51]** We understand it generally in terms of, well, this is the visual cortex,

**[15:51 – 15:53]** and here are the layers in the visual cortex,

**[15:53 – 15:56]** but the actual fine structure is very, very difficult, of course.

**[15:57 – 16:03]** Okay, so with that remark out of the way, let's go back to these guys.

**[16:04 – 16:09]** These guys are Hubel and Weasel, Thorsten Weasel,

**[16:09 – 16:11]** and I forget the name of Hubel,

**[16:13 – 16:19]** who got their Nobel Prize for studying the visual cortex.

**[16:19 – 16:25]** And convolutional networks are partly motivated by the visual cortex.

**[16:26 – 16:27]** That's why I'm talking about this.

**[16:27 – 16:32]** But again, there will be a point where the analogy just will have to stop.

**[16:32 – 16:34]** I'll tell you when it happens.

**[16:35 – 16:37]** But first, let's begin with the bio.

**[16:38 – 16:42]** So back in the, I think, 1960s, 1970s,

**[16:42 – 16:45]** they made their famous studies of the visual cortex.

**[16:45 – 16:50]** And as it quite often happens in biology and in sciences like this,

**[16:51 – 17:00]** their actual truly novel thing that they did was having a new device.

**[17:01 – 17:07]** So what their advantage was compared to everybody who was before that

**[17:07 – 17:13]** was that they could actually make such tiny electrodes

**[17:13 – 17:18]** that you could attach the electrode to a single neuron

**[17:18 – 17:22]** and read off the activation of a single neuron on a live brain.

**[17:24 – 17:28]** Right? So before that, all the people could do was, you know,

**[17:28 – 17:33]** hope that some guy would get in the motorcycle accident

**[17:33 – 17:36]** and then have a stroke.

**[17:36 – 17:39]** And then the stroke will give you some interesting information

**[17:39 – 17:41]** about which part of the brain does what.

**[17:42 – 17:47]** But these guys, they could actually, well, okay,

**[17:47 – 17:50]** this is not my favorite part, but they could take a cat.

**[17:50 – 17:52]** If you look closely, there is a very well,

**[17:53 – 17:56]** fixated cat over here.

**[17:57 – 18:01]** And then they would actually slice open the head of the cat,

**[18:02 – 18:05]** of course, on painkillers.

**[18:05 – 18:08]** And then they would be able to attach electrodes

**[18:08 – 18:13]** to individual neurons and see what the individual neurons

**[18:13 – 18:16]** in the cat's brain actually respond to.

**[18:19 – 18:23]** And what they did, so what they found was that,

**[18:24 – 18:27]** okay, so it had been known that the visual cortex

**[18:27 – 18:29]** is back here in the occipital lobe,

**[18:29 – 18:32]** in mammals, in us and in cats.

**[18:34 – 18:39]** It's actually a very bad decision of nature.

**[18:40 – 18:44]** It's a very fragile thing that makes absolutely no sense

**[18:44 – 18:46]** because your eyes are in front over here.

**[18:47 – 18:49]** And then there is this optical nerve,

**[18:49 – 18:53]** this big fat pile of connections

**[18:53 – 18:57]** that goes all the way through your skull backwards.

**[18:59 – 19:02]** And, of course, it would be easier

**[19:02 – 19:05]** to just have the visual cortex in front,

**[19:05 – 19:09]** but I think the evolutionary explanation is that

**[19:09 – 19:12]** back when we were very far from mammals,

**[19:12 – 19:18]** we would have the proto-eyes up here on top of the head.

**[19:19 – 19:21]** And then somehow the eyes went over here

**[19:21 – 19:25]** and the part of the brain that processes it went over there.

**[19:25 – 19:27]** I have no idea why.

**[19:28 – 19:32]** Anyway, it is known that the visual cortex is here,

**[19:32 – 19:33]** the part that processes visual input,

**[19:34 – 19:38]** and it's easy to find like the first layer of the cortex.

**[19:38 – 19:40]** It's easy to see that, okay,

**[19:40 – 19:42]** here is where the optical nerve attaches,

**[19:43 – 19:46]** so these neurons take the immediate inputs from the eyes.

**[19:49 – 19:54]** And if you actually look at what a single neuron activates for,

**[19:54 – 19:59]** what a single neuron is doing on this first layer of the visual cortex,

**[20:00 – 20:01]** you will see that, first of all,

**[20:02 – 20:04]** it cannot, of course, see the whole picture.

**[20:04 – 20:07]** It has only that many inputs,

**[20:07 – 20:12]** and it has a small receptive field, as it is called.

**[20:15 – 20:23]** It looks at a relatively small part of the general picture,

**[20:24 – 20:26]** and in this small part,

**[20:26 – 20:28]** it recognizes something really, really simple.

**[20:28 – 20:32]** So on this slide, you see a sample neuron

**[20:32 – 20:34]** that recognizes vertical lines.

**[20:35 – 20:38]** So if it sees a bright vertical line in its field of vision,

**[20:38 – 20:40]** great, it's activated a lot,

**[20:41 – 20:43]** and even if you still have just a single line,

**[20:43 – 20:48]** but you start to rotate it, the activation dies out

**[20:48 – 20:50]** and basically goes to zero.

**[20:52 – 20:56]** And then what would you expect next?

**[20:56 – 21:01]** Well, you would definitely expect that then you would have layer two,

**[21:01 – 21:04]** the second layer that would feed off the outputs of the first layer.

**[21:04 – 21:14]** So it would somehow combine these simple shapes

**[21:14 – 21:16]** into something more complicated.

**[21:16 – 21:20]** Like if you had one neuron that recognizes vertical lines,

**[21:20 – 21:24]** another neuron that recognizes horizontal lines, boom, you put an end.

**[21:25 – 21:27]** You have a neuron that gets an end across them,

**[21:28 – 21:32]** and now you have a neuron that recognizes across

**[21:32 – 21:35]** in its receptive field and its visual field of vision.

**[21:37 – 21:43]** And Hebel and Weasel did this, and they also studied the second layer.

**[21:43 – 21:46]** So they discovered neurons like I just said.

**[21:47 – 21:51]** But then they somehow didn't go any further,

**[21:52 – 21:56]** and they started doing other things.

**[21:56 – 21:58]** And actually, that was a pretty wise decision

**[21:58 – 22:02]** because, again, the brain is very, very complicated.

**[22:03 – 22:07]** And if you look at some simplified representation

**[22:07 – 22:09]** of the visual cortex, you will actually see

**[22:09 – 22:16]** that there are layers from V1 to V4,

**[22:16 – 22:19]** then V5, V6, et cetera, et cetera,

**[22:19 – 22:21]** and, yes, there are layers,

**[22:22 – 22:24]** but it's not an artificial neural network.

**[22:24 – 22:27]** The actual structure is much more complicated.

**[22:27 – 22:30]** There is all sorts of feedback that goes back.

**[22:31 – 22:32]** There are all sorts of connections,

**[22:33 – 22:36]** and, yeah, I keep showing this picture

**[22:36 – 22:38]** for the last 10 years or so,

**[22:39 – 22:41]** and I suppose that since the last 10 years,

**[22:41 – 22:43]** it has become much more complicated.

**[22:44 – 22:47]** So this is from some survey,

**[22:47 – 22:48]** and this picture was called

**[22:48 – 22:53]** the most important neural pathways

**[22:53 – 22:57]** in the early layers of the visual cortex.

**[22:58 – 23:00]** So you can actually see that, yeah,

**[23:00 – 23:02]** there is a very well-defined first layer.

**[23:03 – 23:07]** Yes, the optical nerve does come in somewhere,

**[23:07 – 23:09]** so the first layer is easier.

**[23:09 – 23:11]** The second layer is also kind of clear,

**[23:11 – 23:13]** and then it's just a mess.

**[23:14 – 23:16]** Then it's like a lot of different components

**[23:16 – 23:17]** that do different things,

**[23:17 – 23:19]** so they are all interconnected with each other.

**[23:20 – 23:26]** Anyway, when people saw that,

**[23:27 – 23:31]** when they saw how small geometric shapes

**[23:31 – 23:37]** gradually go up layer by layer,

**[23:37 – 23:40]** and we didn't have a clear picture

**[23:40 – 23:42]** of what happens next at that point,

**[23:42 – 23:44]** but clearly at some point,

**[23:45 – 23:49]** the picture would go to something like face recognition, right?

**[23:49 – 23:52]** So some very complicated computer vision problems

**[23:52 – 23:54]** would be solved in our human brain very quickly.

**[23:55 – 23:59]** So people, of course, try to imitate stuff like this in computers.

**[24:00 – 24:05]** And actually, convolutions and convolutional networks

**[24:05 – 24:06]** are a very old idea.

**[24:08 – 24:12]** They date back at least to this very interesting architecture

**[24:12 – 24:14]** called the neocognitron

**[24:14 – 24:19]** by a Japanese researcher named Kunihiko Fukushima.

**[24:20 – 24:23]** He did it in the late 1970s,

**[24:23 – 24:25]** and I actually, if you're interested

**[24:25 – 24:27]** in the history of deep learning,

**[24:27 – 24:29]** I actually recommend you to read these papers.

**[24:29 – 24:32]** It's like, it's a two-page paper.

**[24:32 – 24:35]** It's very short, and you can definitely read it.

**[24:35 – 24:37]** There's nothing too complicated in there,

**[24:38 – 24:43]** and when you read it, you see that in 1979,

**[24:43 – 24:46]** he had a deep neural network, several layers.

**[24:47 – 24:49]** It was a convolutional network,

**[24:50 – 24:53]** and it had real low activations,

**[24:54 – 24:56]** these hinge activations

**[24:56 – 24:57]** that we discussed last time

**[24:57 – 25:02]** and that I told you only came into common practice

**[25:02 – 25:04]** in 2011 or 2012.

**[25:07 – 25:09]** But the thing he didn't have,

**[25:09 – 25:12]** the thing he didn't have in 1979 was learning.

**[25:13 – 25:16]** So there was a big composition of simple things,

**[25:16 – 25:18]** and they were convolutions,

**[25:18 – 25:20]** but they were not trainable convolutions.

**[25:21 – 25:22]** They were just some fixed filters

**[25:22 – 25:26]** that he would apply across the image.

**[25:26 – 25:28]** Anyway, whatever.

**[25:28 – 25:31]** So in a modern form,

**[25:31 – 25:35]** convolutional networks appeared in Jan LeCun's group.

**[25:35 – 25:39]** That's the main claim to fame by Jan LeCun.

**[25:39 – 25:42]** He developed convolutional networks for many, many years,

**[25:42 – 25:43]** for several decades.

**[25:45 – 25:47]** And in the late 1980s,

**[25:47 – 25:53]** they appeared already certainly in their modern form.

**[25:54 – 25:56]** They had training,

**[25:56 – 25:58]** they had convolutions and everything.

**[25:59 – 26:02]** And let me just walk you through a few images

**[26:02 – 26:07]** that will show how convolutional networks work.

**[26:07 – 26:15]** And it's such a brilliant idea that it's...

**[26:15 – 26:17]** Well, okay, it's just a brilliant idea.

**[26:18 – 26:21]** It's a very brilliant idea of what I would call

**[26:21 – 26:22]** structural regularization.

**[26:23 – 26:24]** You'll see what I mean.

**[26:24 – 26:29]** So first of all, let's have a picture like this one.

**[26:29 – 26:33]** And let's assume that I want to process this picture.

**[26:34 – 26:36]** So what do I mean by processing?

**[26:36 – 26:39]** Well, maybe I want to solve some computer vision task.

**[26:39 – 26:44]** Maybe I want to, for example, find the little boy's head on this image.

**[26:45 – 26:47]** So that would be object detection.

**[26:47 – 26:49]** We'll discuss object detection later.

**[26:49 – 26:53]** So where is the boy's head on this image?

**[26:53 – 27:01]** And the main observation, the main idea,

**[27:01 – 27:04]** the main assumption that is behind CNNs,

**[27:04 – 27:05]** that is behind convolutional neural networks,

**[27:06 – 27:09]** is that, well, if I'm looking for something,

**[27:10 – 27:12]** for some feature on an image,

**[27:14 – 27:18]** then it's the exact same function

**[27:18 – 27:21]** applied all across the image.

**[27:22 – 27:26]** So if I have a black box that looks at a small window

**[27:26 – 27:28]** and says, well, that's a boy's head,

**[27:28 – 27:30]** or no, that's not a boy's head,

**[27:31 – 27:34]** then it will be the exact same black box

**[27:34 – 27:40]** that I'm supposed to apply across this whole big picture,

**[27:40 – 27:42]** and just the output will be different.

**[27:42 – 27:45]** So here it will say yes, and over here it will say no.

**[27:46 – 27:48]** But the function is the same.

**[27:49 – 27:51]** The inputs are different, so the outputs, of course, are also different.

**[27:53 – 27:56]** So the idea of convolutional neural networks is this.

**[27:56 – 28:01]** Let's take a picture, or any input is just easier to,

**[28:01 – 28:04]** more clear to reason about pictures,

**[28:04 – 28:08]** but take any input, break it into small windows like this.

**[28:09 – 28:11]** Usually they are overlapping, like shown here.

**[28:13 – 28:21]** Then, for every tile like this one, apply a small neural network.

**[28:22 – 28:26]** So, now this small neural network is a model that we need to train,

**[28:26 – 28:30]** it will have weights, we will do gradient descent, etc., etc.,

**[28:30 – 28:32]** but it will be small.

**[28:32 – 28:36]** It will be applied only to this little tile,

**[28:37 – 28:43]** a few pixels across, that we split the picture into, right?

**[28:43 – 28:48]** And the big gain here, the profit,

**[28:48 – 28:53]** is that now I take the exact same small neural network

**[28:53 – 29:00]** and I apply it to every single tile across the input.

**[29:01 – 29:07]** So I take this tile, I apply the neural network,

**[29:07 – 29:09]** I get this, let's say, output vector.

**[29:10 – 29:12]** Usually you would want to extract not one feature,

**[29:12 – 29:13]** but several features.

**[29:13 – 29:16]** So usually the output is several numbers.

**[29:17 – 29:21]** And then I take the next tile, I apply, I get some more.

**[29:23 – 29:28]** And so when I actually do that, get back to the board,

**[29:29 – 29:34]** when I actually do that, what I get as a result,

**[29:35 – 29:38]** so here is my input picture, right?

**[29:38 – 29:41]** I break it into windows, like I showed.

**[29:41 – 29:46]** And then I take each window, okay, yeah, okay,

**[29:46 – 29:48]** let them be overlapping, whatever.

**[29:48 – 29:53]** I take each window, I put it through my small neural network,

**[29:53 – 29:59]** and let me draw it horizontally, I get this vector of features, right?

**[30:01 – 30:06]** Then I take the next window over here,

**[30:08 – 30:10]** I put it through the exact same neural network,

**[30:11 – 30:16]** and I get a different vector of features that goes here.

**[30:17 – 30:19]** Okay, now this will be a massive picture,

**[30:19 – 30:23]** but anyway, as I take each one of these windows,

**[30:24 – 30:28]** I get a vector of features,

**[30:29 – 30:33]** and then these vectors of features themselves

**[30:33 – 30:38]** also have this geometric structure, right?

**[30:38 – 30:44]** So there is a top right window,

**[30:44 – 30:46]** there is a bottom left window,

**[30:46 – 30:48]** and the bottom left window will give me

**[30:48 – 30:52]** this bottom left vector of features and so on, right?

**[30:52 – 30:56]** So as the output of this procedure,

**[30:57 – 31:00]** I will get a three-dimensional tensor, right?

**[31:00 – 31:04]** I will still have some width, some height,

**[31:05 – 31:09]** and now I will also have a meaningful depth.

**[31:10 – 31:12]** So actually, the input also usually has depth,

**[31:13 – 31:16]** for example, because these days,

**[31:16 – 31:19]** for the last few decades,

**[31:19 – 31:21]** pictures are usually in color.

**[31:22 – 31:24]** So even on the first step,

**[31:25 – 31:26]** if you have a color image,

**[31:26 – 31:28]** you have depth three at the input, right?

**[31:29 – 31:33]** In general, what you get

**[31:33 – 31:36]** at the output of a convolutional layer

**[31:36 – 31:38]** is a 3D tensor,

**[31:38 – 31:41]** if you start with a 2D input

**[31:41 – 31:42]** in structure, like a picture,

**[31:44 – 31:46]** and then you can do the same thing, right?

**[31:46 – 31:49]** So again, you take its pixels,

**[31:50 – 31:53]** you take this structure over here,

**[31:53 – 31:58]** and you tile it with windows,

**[32:00 – 32:01]** with small tiles,

**[32:01 – 32:05]** and then you take this small sub tensor,

**[32:05 – 32:08]** this small window out of here,

**[32:08 – 32:12]** and you pass it through another small neural network,

**[32:12 – 32:16]** and you get another vector of features.

**[32:17 – 32:19]** And again, you repeat this,

**[32:19 – 32:21]** this was the top left vector of features,

**[32:21 – 32:23]** but then you get another tensor,

**[32:24 – 32:25]** and so on and so forth.

**[32:26 – 32:29]** I'm sorry, I'm not in a convenient place

**[32:29 – 32:29]** to draw a nice picture,

**[32:30 – 32:31]** but I hope you understand what's going on.

**[32:31 – 32:33]** So on every step,

**[32:34 – 32:42]** we tile the image into tiles like this one.

**[32:43 – 32:47]** It doesn't have to be the original image.

**[32:47 – 32:51]** You can chain these layers one after the other

**[32:51 – 32:54]** because always you are working

**[32:54 – 32:56]** with like three-dimensional arrays,

**[32:56 – 32:59]** which in deep learning are confusingly called tensors,

**[32:59 – 33:00]** but what can you do?

**[33:01 – 33:04]** So you're working with three-dimensional tensors,

**[33:05 – 33:10]** and you just convert one 3D tensor to another

**[33:10 – 33:12]** as you go with this procedure.

**[33:13 – 33:20]** And then you can have like a whole sequence

**[33:20 – 33:21]** of these convolutional layers.

**[33:25 – 33:28]** So before we proceed, one more thing about this.

**[33:29 – 33:33]** In classical convolutional neural networks

**[33:33 – 33:36]** and in many architectures that we will see today,

**[33:37 – 33:43]** there is another type of layers.

**[33:43 – 33:44]** Like there is a convolutional layer.

**[33:45 – 33:46]** That's the one that we just discussed.

**[33:47 – 33:49]** And then there is also what is called the pooling layer.

**[33:49 – 33:55]** And let me maybe first give you the motivation for it.

**[33:55 – 33:58]** And then the actual layer is actually pretty simple.

**[33:59 – 34:00]** So the motivation is this.

**[34:02 – 34:09]** Let's again try to look at what the neurons do.

**[34:09 – 34:11]** So this is our original image.

**[34:12 – 34:15]** And it has lots and lots of pixels, right?

**[34:17 – 34:22]** It has big width, big height.

**[34:23 – 34:28]** Then I slice it into very small tiles.

**[34:29 – 34:32]** So, of course, in my picture, they're not small, but in practice, they're small tiles.

**[34:33 – 34:37]** So I have this tile of, let's say, three by three pixels.

**[34:38 – 34:41]** And it's a color image, so it has depth three too.

**[34:41 – 34:48]** So it has a small height, a small width, and then it goes through the neural network,

**[34:48 – 34:53]** and then we get our vector of features.

**[34:54 – 35:06]** So this vector of features, this one, depends only on this small three by three tile, right?

**[35:06 – 35:15]** So if you look at it in the other direction, you can say that for this feature,

**[35:15 – 35:24]** this feature has a receptive field, it's called in this part of science,

**[35:24 – 35:28]** receptive field, has a receptive field of three by three pixels.

**[35:29 – 35:34]** So it only looks at a very small, very local part of the image, right?

**[35:34 – 35:37]** So what happens next?

**[35:37 – 35:47]** Suppose that I cover this whole image with three by three windows like this,

**[35:47 – 35:55]** and then as a result, I will have a 3D tensor like this,

**[35:56 – 35:58]** and then I do another convolution.

**[35:58 – 36:02]** I do another three by three convolution over here, okay?

**[36:02 – 36:07]** So I cut off, I cut out another three by three by something.

**[36:08 – 36:10]** Now the depth is probably more than three, but anyway,

**[36:10 – 36:12]** I cut out another three by three by D tensor,

**[36:13 – 36:15]** and I put it through a small neural network and so on.

**[36:16 – 36:18]** I get a feature over here.

**[36:19 – 36:21]** What is its receptive field?

**[36:21 – 36:29]** Well, it looks at these features inside this parallelepiped, right?

**[36:30 – 36:34]** At the features inside this small part of the tensor.

**[36:35 – 36:40]** And these features in turn are looking at more pixels than before, right?

**[36:41 – 36:47]** So if I had a three by three over here and another three by three over here,

**[36:48 – 36:54]** which goes to one here, so now this guy corresponds to this,

**[36:54 – 37:00]** and this guy corresponds to a window over here, right?

**[37:01 – 37:12]** So overall, this pixel over here would look at a five by five window in the original pixels, right?

**[37:12 – 37:14]** That's my point.

**[37:14 – 37:19]** So if you do a three by three, and then the results of your three by three you compose in another three by three,

**[37:20 – 37:26]** then you collect information from a five by five window originally, right?

**[37:27 – 37:31]** But five by five is also a pretty small window.

**[37:32 – 37:37]** So like how many layers would you need to have neurons that look at the whole picture?

**[37:38 – 37:43]** On every three by three convolutional layer, you just add two to the width,

**[37:43 – 37:46]** and you don't multiply by two, you just add two to the width,

**[37:47 – 37:50]** and add two to the height of this receptor field, right?

**[37:51 – 37:59]** So if I want to process a 256 by 256 image, I would need like 130 layers.

**[38:00 – 38:01]** That doesn't make any sense.

**[38:01 – 38:03]** I don't want to have that many layers.

**[38:04 – 38:13]** So in the original convolutional networks, you would somehow need to solve this problem.

**[38:13 – 38:19]** That is, you would need to reduce the geometry, and this is an important way of looking at it.

**[38:19 – 38:22]** We will talk about reducing the geometry a lot in this class.

**[38:22 – 38:33]** But you want to reduce the geometry quicker than by just tiling everything and hoping that, you know,

**[38:33 – 38:36]** convolutions will do it by themselves.

**[38:36 – 38:47]** So in the original neural networks, in the original CNNs, they had, and you can still see it today in some architectures,

**[38:47 – 38:50]** they had this idea of a pooling layer.

**[38:50 – 39:01]** So let's suppose that I had a convolutional layer, I expected some features, and then I can say, well, you know, there are too many.

**[39:01 – 39:05]** The width and height are too big, I want to reduce the geometry.

**[39:05 – 39:06]** How could I reduce the geometry?

**[39:06 – 39:33]** Well, I could just slice it into small windows, this time no overlaps, that's the whole point, no overlaps, usually it's two by two windows, but of course you can say it whatever you want, and just replace in every two by two window, out of four features leave only one, according to some rule, right?

**[39:33 – 39:55]** And there are two commonly used rules, I think anything else just reduces basically to one of these two in effect, so there is max pooling, where you take the maximum of the feature values in this small window, and there is average pooling, where you average them.

**[39:56 – 40:07]** I don't think I've ever seen anything else in practice, and usually it's max pooling, so usually it's max pooling, why? Because it kind of makes sense for feature extraction.

**[40:07 – 40:24]** So, okay, so the real answer is because it works better usually, but the justification is that it urges convolutional layers to actually extract more meaningful features.

**[40:24 – 40:44]** So if you, for example, so let's look at this picture and let's say, okay, so I want to like have a black box, have a feature extractor that says, is there a little boy's head in this tile?

**[40:44 – 40:58]** And so when I run it on this tile, I get a one, right? But when I run it, say, on this tile or on this tile, I get basically a zero, even if it's like perfectly understands everything.

**[40:59 – 41:11]** So then let's suppose that I have this bigger tile that combines the small tiles over here that glues them together like pooling does.

**[41:11 – 41:23]** And then I ask, well, what is the proper composition? What is the proper combination of features that will answer the question, is there a little boy's hat in this tile?

**[41:23 – 41:25]** And that would be the max, right?

**[41:25 – 41:32]** If I average, I get some pretty low average because most tiles don't have a little boy's hat, right?

**[41:32 – 41:36]** And only one tile would have the little boy's hat and the rest wouldn't.

**[41:38 – 41:45]** But meaningful features like something is there, they obey the max law, right?

**[41:45 – 41:52]** And less meaningful but sometimes also useful features like how green it is, this feature

**[41:52 – 41:53]** would obey the average law, right?

**[41:53 – 42:00]** If I have a big tile which is half green and half blue, I would probably want to say that

**[42:00 – 42:02]** it's half green.

**[42:02 – 42:03]** It's not fully green.

**[42:03 – 42:11]** But for features corresponding to objects or whatever shapes, max is usually the way

**[42:11 – 42:11]** to go.

**[42:12 – 42:19]** Anyway, that's just a rambling justification of why max pooling.

**[42:22 – 42:22]** All right.

**[42:23 – 42:36]** And so now when you combine convolutional and pooling layers, you can start reducing the

**[42:36 – 42:42]** geometry really, really quickly because every pooling layer cuts the width and the half

**[42:42 – 42:43]** by two.

**[42:43 – 42:45]** Let's assume it's two by two pooling.

**[42:45 – 42:47]** It's almost always two by two pooling.

**[42:47 – 42:52]** So every pooling layer cuts the width by two, cuts the height by two.

**[42:52 – 42:59]** So you get twice, you get four times fewer pixels, four times fewer numbers.

**[42:59 – 43:03]** And then you can do another convolution, blah, blah, blah, and so on.

**[43:04 – 43:18]** So at this point, what I want to do is I want to actually discuss how you would define a convolution,

**[43:18 – 43:26]** like what it actually is, and then we will just work through an example where, I apologize,

**[43:26 – 43:35]** then we would just work through an example where we would see the beauty of convolutions,

**[43:36 – 43:43]** where we would actually realize why convolutions save so much,

**[43:43 – 43:47]** why they are such a great way to process large inputs.

**[43:48 – 43:52]** So, what exactly could this neural network be?

**[43:54 – 44:03]** Well, the word convolution doesn't really mean anything specific,

**[44:03 – 44:09]** it just means that I tile the input with small tiles,

**[44:09 – 44:15]** and I apply my transformation to every tile separately.

**[44:15 – 44:17]** So, this is what the word convolution means.

**[44:18 – 44:21]** It doesn't tell you what exactly this transformation should be.

**[44:21 – 44:24]** But usually when people talk about convolutional layers,

**[44:24 – 44:28]** they mean the simplest neural network possible.

**[44:29 – 44:30]** The simplest neural network possible,

**[44:31 – 44:32]** that is just one fully connected layer.

**[44:34 – 44:36]** So, it looks like this.

**[44:37 – 44:41]** I have my input, now let me do it in full generality.

**[44:42 – 44:43]** So, I have a three-dimensional input.

**[44:44 – 44:49]** It has some width capital W, some height capital H, some depth D.

**[44:50 – 44:54]** And I cut out a subset, a tile,

**[44:55 – 45:02]** which has width small W and height small H and still depth D.

**[45:02 – 45:03]** So, this is also important.

**[45:03 – 45:06]** I always cut through all the features.

**[45:06 – 45:08]** I take all the features, all the depth.

**[45:09 – 45:17]** So, then I take this guy and basically I say,

**[45:17 – 45:23]** well, okay, here I have like a D times W times H tensor, right?

**[45:23 – 45:29]** I have this three-dimensional matrix of three-dimensional array of numbers, right?

**[45:30 – 45:34]** But when I go inside this neural network,

**[45:34 – 45:36]** I don't care about the structure of this array.

**[45:36 – 45:37]** I just lose it.

**[45:37 – 45:41]** I just say, okay, so I have this many numbers.

**[45:41 – 45:47]** You can actually visualize it as flattening it to a single vector

**[45:47 – 45:54]** of size dWh, and then I just apply a matrix of weights to it.

**[45:54 – 45:56]** I have some matrix of weights.

**[45:56 – 46:02]** So the output will be a vector of size, let's say, d'.

**[46:02 – 46:16]** And this vector of size d' is just w times this d'.

**[46:16 – 46:24]** So the matrix w, how many weights does a convolutional layer have?

**[46:24 – 46:34]** the matrix w uh has is supposed to have like um uh it's supposed to be well okay so just to

**[46:34 – 46:50]** make it more convenient let's say um it's z times w so w uh would be like dwh times d prime okay um

**[46:50 – 47:08]** so it would be dwh times d prime uh and um and then and and then yes i lost my train of thought a

**[47:08 – 47:19]** little um dwh times d prime yeah and then uh the beauty of convolutional networks is that now when

**[47:19 – 47:28]** i take another window over here i also have an input of the same size and i reuse the exact same

**[47:28 – 47:40]** matrix w right so uh these many weights are needed to process the whole image i don't uh i don't have

**[47:40 – 47:47]** a different w for a different window i have the same double i reuse the weights so these many weights

**[47:47 – 47:55]** are needed to process the whole d times big w times big h input and as as you can notice the number of

**[47:55 – 48:01]** weights doesn't depend on the size of the input it only depends on the size of the window so when i

**[48:01 – 48:07]** have a convolutional layer it's very easy for me to say oh okay so my my input image is now twice

**[48:07 – 48:13]** larger but let's just run the convolution across the larger image i don't care uh i only care about

**[48:13 – 48:24]** the size of the window uh and of course formally and like in reality what you have here is a matrix

**[48:24 – 48:30]** of of these dimensions but it would be very very inconvenient if if we humans had to think of of

**[48:30 – 48:36]** this matrices as you know some huge number times d prime and then this huge number we would have to

**[48:36 – 48:43]** memorize and think of oh okay so that was like three by three by 32 how many is that oh this

**[48:43 – 48:49]** this should be the size of course that's very inconvenient so in in practice if you for

**[48:49 – 48:57]** example set up a convolutional layer in pytorch um it wouldn't be a 2d matrix uh the convolutional

**[48:57 – 49:02]** the convolution would be defined by a four-dimensional tensor so your tensor of weights

**[49:02 – 49:12]** would have size d times w times h times d prime and what would actually happen is your input

**[49:13 – 49:21]** is a three-dimensional tensor which is supposed to match the first uh three dimensions of w

**[49:21 – 49:32]** and that means that your output is is a vector of this dimension okay uh so in practice you would

**[49:32 – 49:41]** define like four-dimensional tensors when you when you set up convolutional layers and by the way while

**[49:41 – 49:50]** we are at this while while we are defining this note that uh it is absolutely positively uh it

**[49:50 – 50:00]** absolutely positively uh doesn't matter uh that the input is specifically uh a picture that specifically

**[50:00 – 50:06]** is like a 3d tensor with some width some height and some depth uh you can surely have convolutional

**[50:06 – 50:14]** networks for other kinds of inputs for example uh at some point now of course nobody does this but at

**[50:14 – 50:24]** some point uh you could there were cnn's designed for text processing and what is text text is a

**[50:24 – 50:31]** sequence right it's a sequence of tokens and um every token gets represented in by some vector

**[50:31 – 50:40]** uh so it's a sequence of vectors right it's a it's a 1d object one-dimensional object that

**[50:40 – 50:46]** produces a two-dimensional input tensor and sure enough you can have one-dimensional

**[50:46 – 50:52]** convolutions no problem at all you just just your windows are now sliding windows like this

**[50:52 – 51:03]** you take like three uh neighboring vectors your small input is like this it's um

**[51:03 – 51:12]** well it's d times l length of the window and then you multiply it by the matrix w

**[51:14 – 51:22]** which now is a three-dimensional tensor d times l times d prime and you get the result which is a

**[51:22 – 51:29]** vector of size t prime almost no difference at all just all all dimensions uh change by one and that's

**[51:31 – 51:39]** or you can go in the other direction you can say well but what if i have let's say a video i have a

**[51:39 – 51:49]** video which means that i have a sequence of images so now my input is like d times w times h times

**[51:49 – 51:56]** let's say t for time right if this is a video so now there are there is a sequence of images and every

**[51:56 – 52:05]** image is a w times h times d tensor and of course you can multiply it by a five-dimensional tensor w

**[52:05 – 52:14]** which is t times w times h times t times d prime that's it right so um you can apply the same idea

**[52:14 – 52:19]** of cutting stuff into small tiles and processing each tile separately you can apply it to anything

**[52:19 – 52:27]** it just so happens that it was especially productive for uh images and basically

**[52:27 – 52:31]** all of the examples in our class since it's a computer vision class of course

**[52:31 – 52:45]** all of the examples in our class will be uh will be images okay so um okay okay so with this let's

**[52:45 – 52:53]** maybe look at a specific example um let's look at a specific example of a convolutional network

**[52:55 – 53:04]** yeah this one uh and i just want to go through this network layer by layer it's some classical

**[53:04 – 53:12]** leonet architecture from i don't know 2001 or something uh it's very small it has very small

**[53:12 – 53:19]** input not very powerful but i want to to go through this architecture to count the weights to get a

**[53:19 – 53:27]** feeling of what convolutional networks look like and we will see like what's the whole point of

**[53:27 – 53:35]** convolutional networks when we discuss how many weights they have so um so let's look at this

**[53:35 – 53:41]** slide what do we have here we have the input which is a 32 by 32 picture and it's a black and white

**[53:41 – 53:52]** picture well a gray scaly picture so it has depth one so our input and let me switch from

**[53:53 – 54:05]** from the picture to the board for a little bit so our input uh is a tensor of size 1 times 32 times 32

**[54:05 – 54:15]** okay then a convolutional layer happens and this picture doesn't show you the weights doesn't show

**[54:15 – 54:21]** you the layers themselves it shows you the intermediate results the tensors that result

**[54:21 – 54:32]** from every layer so now it says that after the first layer you have 28 by 28 tensor uh with six

**[54:32 – 54:38]** feature maps when people say feature maps it's the same as channels the same as depth so basically it

**[54:38 – 54:50]** says that it's a 28 by 28 by 6 tensor okay six different features uh so we started with a 32 by

**[54:50 – 55:00]** 32 by one then something happened a convolutional layer happened and now we have a tensor of size

**[55:00 – 55:15]** uh 6 by 28 by 28 so the question to you how large do you think was the convolution what was the size

**[55:15 – 55:45]** of the window if we went from 32 by 32 pixels to 28 by 28 pixels why would why would the geometry be

**[55:45 – 56:11]** reduced why would the convolutional network actually have less pixels at the output so i'm covering the

**[56:11 – 56:29]** input by overlapping tiles all possible tiles how many tiles are possible okay so this this is our

**[56:29 – 56:41]** first remark here so i have this input which is like a 32 by 32 pixel image of course i won't draw

**[56:41 – 56:49]** the full 32 and then i start covering it by tiles of some kind of size right let's say three by three

**[56:49 – 57:06]** tiles but how many tiles will fit not 32 by 32 right so you see uh for every tile uh every tile

**[57:06 – 57:12]** is defined by its center pixel let's say right so this center pixel corresponds to this three by three

**[57:12 – 57:19]** window usually it's odd there are very few even convolutions so i i will i'm safe uh talking

**[57:19 – 57:25]** about the center pixel so there is a center pixel corresponding to the three by three tile this

**[57:25 – 57:30]** center pixel corresponds to the three by three and so on but there is no tile that will correspond to

**[57:30 – 57:41]** this pixel right uh it doesn't fit so in effect uh how many if i had a three by three convolution

**[57:42 – 57:49]** the output if i just do the tiling if i just use all possible tiles not use any special tricks here

**[57:50 – 57:59]** the tiling would be would would not be able to use these pixels and also wouldn't be able to use

**[57:59 – 58:04]** these pixels right so it would cut off one pixel on top one pixel on bottom one on the left one on

**[58:04 – 58:13]** the right so if i did a three by three convolution and i had like a w times h image at the input i

**[58:13 – 58:18]** would go to something like w minus two times h minus two right because i would need to cut off

**[58:18 – 58:28]** two pixels on the sides well in here we go to w minus four and h minus four so how how big was the

**[58:28 – 59:01]** window yeah exactly so uh i mean of course it's not guaranteed there could have been tricks etc but

**[59:02 – 59:08]** the most plausible version of how this convolution what this convolution looks like judging by that

**[59:08 – 59:20]** picture and it's true in fact it's true uh is that it was we were covering the input by five by five

**[59:22 – 59:30]** tiles and then uh so what what is the size of the weight matrix here um yeah i didn't tell you that

**[59:30 – 59:37]** sorry uh i i'm when i talk about the weight matrix i of course simplify a little bit because in addition

**[59:37 – 59:44]** to the weight matrix there is also the intercept so in fact of course this output is like

**[59:46 – 59:55]** z w plus some constant so there there is an additional d prime weights which is also a weight

**[59:55 – 1:00:01]** right which is also which are also trained but let's forget about that it doesn't matter for us

**[1:00:01 – 1:00:07]** now let's just count the weights and the matrices themselves so what would be the matrix size over

**[1:00:07 – 1:00:17]** here the matrix size would be as we discussed uh there d times w times h times d prime right so here

**[1:00:17 – 1:00:27]** we have a convolutional weight matrix weight tensor of size one times five times five and we have six

**[1:00:27 – 1:00:38]** features at the output times six right so five five by five is 25 25 times six 150 right so over here in

**[1:00:38 – 1:00:49]** this layer we have 150 weights trainable weights that we will need to learn by gradient descent well

**[1:00:49 – 1:00:56]** there you have it that's that's that's the first point that i want to make with this example uh the

**[1:00:56 – 1:01:05]** convolutional idea the idea of sliding a window over the input saves a huge amount of weights so

**[1:01:05 – 1:01:11]** suppose that i wanted to have a fully connected layer over here suppose that i just wanted to

**[1:01:11 – 1:01:21]** have a single weight matrix that takes this guy's input and outputs this then how many weights would

**[1:01:21 – 1:01:27]** i have what what what kind of matrix would it be a fully connected uh first layer would be like

**[1:01:28 – 1:01:40]** 32 times 32 times 6 times 28 times 28 right so it would be a matrix of size input times output input

**[1:01:40 – 1:01:46]** size times output size if i didn't have this convolutional structure um and i still for some

**[1:01:46 – 1:01:53]** unfathomable reason would would want to to have this kind of output the matrix would have this kind

**[1:01:53 – 1:02:01]** of size so uh of course i cannot do this in my head but like 32 squared is about a thousand

**[1:02:01 – 1:02:07]** so this is like you know five million or something you can count if you want but this is like several

**[1:02:07 – 1:02:19]** million weights and the convolutional idea reduced this five million weights down to 150 so that this is

**[1:02:19 – 1:02:26]** the the power of convolutions the main power of convolutions they save a lot of weights and that's

**[1:02:26 – 1:02:36]** why i always say that what convolutions actually are they are an excellent technique of structural

**[1:02:36 – 1:02:48]** regularization we discussed uh last some previous lectures that regularization is when you um

**[1:02:51 – 1:03:00]** regularization is when you compress uh could compress the weights magnum smaller uh or reduce

**[1:03:00 – 1:03:07]** like reduce the set from which the weights are taken right but in this case it's even more

**[1:03:07 – 1:03:12]** straightforward like structural regularization means all right so i have five million weights

**[1:03:12 – 1:03:18]** and you could like if you think of it from a proper view view it from a proper angle you will see that

**[1:03:18 – 1:03:23]** you can actually think of a convolutional layer also as a transformation of this guy to this guy

**[1:03:23 – 1:03:31]** but when i do this transformation i say oh okay so i want this thousand of weights to be equal to each

**[1:03:31 – 1:03:41]** other and i just said this constraint that i always process every window be it over here or over here or

**[1:03:41 – 1:03:48]** over here i process it in the exact same way with the exact same weights that so that structural

**[1:03:48 – 1:03:54]** regularization when you impose constraints like this way it should be equal to each other this way it

**[1:03:54 – 1:04:05]** should just disappear to zero or something so so um so this is the power of convolutions and let's um

**[1:04:05 – 1:04:10]** so let's finish the the exercise that there are still a couple of points that i want to make here

**[1:04:10 – 1:04:20]** so after the first convolutional layer there is a pooling layer subsampling is the same as

**[1:04:20 – 1:04:30]** pooling layers so the pooling layer is obviously has two by two windows right so we go from 28 by

**[1:04:30 – 1:04:43]** 28 to 14 by 14 a question to you how many weights does this pooling layer have i had the

**[1:04:43 – 1:04:52]** 28 by 28 by 6 input i have 14 by 14 by 6 output which means that okay let's assume it's max

**[1:04:52 – 1:05:00]** pooling i don't remember which it was actually but i take a two by two window and in every two

**[1:05:00 – 1:05:09]** by two window across every feature i take the max of these four numbers um how many weights is that

**[1:05:09 – 1:05:49]** how many trainable weights so the pooling transformation takes the input uh cuts it into

**[1:05:49 – 1:05:55]** tiles and for every tile uh you take the numbers that are parts of your input and you leave

**[1:05:55 – 1:06:03]** only the max of these numbers like you take a two by two window every two by two window becomes just

**[1:06:03 – 1:06:34]** its maximum how many trainable weights are in transformation like this no all right not talking

**[1:06:34 – 1:06:41]** to me today anyway uh how many weights are in this transformation of course none of course there are

**[1:06:41 – 1:06:47]** no weights it's a deterministic function there is nothing to train i just take the

**[1:06:47 – 1:07:00]** max right so the uh the uh the pooling layers don't have weights and there is no no point for

**[1:07:00 – 1:07:11]** for them to have weights there is nothing to train i just do a specific fixed thing uh so okay so let

**[1:07:11 – 1:07:22]** me draw this uh next i have a pooling layer uh a pooling layer goes to 6 by 14 by 14

**[1:07:22 – 1:07:33]** uh the pooling layer has no weights and then i have another convolutional layer uh right

**[1:07:33 – 1:07:45]** let's check i have another convolutional layer that goes down to 10 by 10 so um sorry check

**[1:07:45 – 1:07:58]** 10 by 10 by how many 10 by 10 by 16 so my next knowledge layer goes makes it like this um 16

**[1:07:58 – 1:08:05]** by 10 by 10 so i i put depth first here but you don't have to you can put it wherever you want

**[1:08:05 – 1:08:14]** um so how many weights are here well again we reduce the width and the height by uh four so it's

**[1:08:14 – 1:08:22]** a five by five convolution but now we need to transfer uh translate six features into 16 features

**[1:08:22 – 1:08:33]** so like six by five by five by 16 okay that's more weights right so we know six by five by five is

**[1:08:33 – 1:08:48]** 150 and 150 times 16 uh 150 times four is six so six times four is 2400 weights right i i suppose

**[1:08:48 – 1:08:59]** that's correct uh 2400 weights over here okay then another pooling uh this part i remember

**[1:08:59 – 1:09:07]** and then we get uh wait for it there will be a little bit more interesting stuff here so

**[1:09:07 – 1:09:19]** now i have like 16 by 5 by 5 and at this point i say oh okay so now i have a 5 by 5 tensor

**[1:09:19 – 1:09:31]** with depth 16 so if i keep doing 5 by 5 convolutions it means that now there are no tiles really like

**[1:09:31 – 1:09:39]** the whole tensor is a single tile i don't have to cut it any longer which means that uh okay in the

**[1:09:39 – 1:09:43]** picture they call it a convolutional layer but now it really doesn't matter you could call it a

**[1:09:43 – 1:09:49]** convolutional layer or you could call it a fully connected layer you just take the whole input

**[1:09:49 – 1:10:00]** and you convert it to okay how many features so next you go to 120 features then 84 features and

**[1:10:00 – 1:10:13]** then finally the output of 10 so um you go to 120 then another fully connected layer you go to 84

**[1:10:13 – 1:10:26]** and another fully connected layer maybe a softmax layer um you go to 10 so how many weights are here

**[1:10:26 – 1:10:38]** well in this fully connected layer i have 16 times 5 times 5 times 120 right so i compress

**[1:10:38 – 1:10:46]** the whole input down to the to a vector and i just lose all the geometry i don't care about the

**[1:10:46 – 1:10:53]** geometry anymore these are just global features numbers about the the the input image and but i

**[1:10:53 – 1:11:03]** still need to, you know, do stuff with them. I still need to toss them around a little to do

**[1:11:03 – 1:11:07]** some linear combinations of them to actually extract the signal that I want, not just reasonable

**[1:11:07 – 1:11:19]** signal, but signal that I want to actually get to the classes, for example, that I want to recognize.

**[1:11:19 – 1:11:27]** So, in classical conversational networks, after you go through all of these layers, after you

**[1:11:27 – 1:11:32]** downsample and downsample and downsample, at the end, you have a couple of fully connected

**[1:11:32 – 1:11:43]** layers usually. Sometimes it's called the head of the network, and sometimes our networks

**[1:11:43 – 1:11:48]** will have multiple heads that do different things, but for now, let's just say that I

**[1:11:48 – 1:11:52]** do need to have some kind of a classification head at the end with a couple of fully connected

**[1:11:52 – 1:12:03]** layers. And interestingly, it turns out that this classification head holds the vast majority

**[1:12:03 – 1:12:16]** of all the weights. You see? So over here, we have like, what, 400 times 120. We have 48,000

**[1:12:16 – 1:12:24]** weights over here. And here we have 120 times 84, which is, I don't know, about 10k more, right?

**[1:12:24 – 1:12:39]** So out of the total 60,000 weights in this network, about 60,000, about 57,000, 58,000 lie in the

**[1:12:39 – 1:12:50]** classification head. And only 2,500 weights are in the convolutional layers. But the convolutional

**[1:12:50 – 1:13:00]** layers are doing the most important job. They are the Fisher extractors. And so how does

**[1:13:00 – 1:13:12]** it actually work during training? Well, remember how we discussed backpropagation. So if you

**[1:13:12 – 1:13:21]** have a single input going into several different places, then in the graph, then when you go

**[1:13:21 – 1:13:30]** back to the backpropagation here, your update, your gradient will be by the chain rule, the

**[1:13:30 – 1:13:41]** sum of, not the gradient, the partial derivative at this node will be by the chain rule, the

**[1:13:41 – 1:13:50]** sum across all of the paths. And in the convolutional network, every weight over here, every weight

**[1:13:50 – 1:13:59]** in this convolution, in this matrix, occurs in the computational graph, is input into the

**[1:13:59 – 1:14:04]** computational graph many, many, many, many times. So I don't think I can draw a computational

**[1:14:04 – 1:14:13]** graph for it here, but basically like this, you have this input, right? In the input, every

**[1:14:13 – 1:14:24]** pixel is a value, let's say, and now let's suppose that this weight like WI gets multiplied

**[1:14:24 – 1:14:37]** by the value of middle right pixel in the 3x3 window, which means that when we process this

**[1:14:37 – 1:14:45]** window, I will multiply it by this pixel and then add up and everything. When I process

**[1:14:45 – 1:14:54]** this window, I will multiply it by this pixel and then add up and everything. So the same weight,

**[1:14:54 – 1:15:02]** the same input to the computational graph will occur many, many, many times. It will occur in the

**[1:15:02 – 1:15:11]** processing of every single tile by the nature of convolutional networks. And that's why, by the way,

**[1:15:12 – 1:15:22]** ReLU activations are such a good fit here, because this means that we don't mind sparsity. Sparsity is

**[1:15:22 – 1:15:28]** bad if you have little signal, if you don't have enough signal, if you don't want to lose

**[1:15:28 – 1:15:35]** anything. But sparsity is great if you have an abundance of signal, if you have a lot of

**[1:15:35 – 1:15:43]** computational paths. Now, sparsity just saves you time. It doesn't really hurt you. It doesn't

**[1:15:43 – 1:15:51]** really hurt training. It just says that, oh, okay, so like in the processing of this window doesn't

**[1:15:51 – 1:15:58]** matter right now. So this guy will be a zero, and this part of the graph will not matter. But the

**[1:15:58 – 1:16:02]** processing of this window will still matter. So this weight will still get a meaningful update.

**[1:16:03 – 1:16:09]** So usually when you have the same weight occurring in many, many different places,

**[1:16:10 – 1:16:14]** it's a good idea to add some sparsity, and ReLU provides this kind of sparsity.

**[1:16:16 – 1:16:24]** Okay, so what have we discussed so far? We discussed the basic idea of convolutional networks,

**[1:16:24 – 1:16:31]** how you slide across the input. We discussed how the receptive field grows with time,

**[1:16:31 – 1:16:37]** that it grows not fast enough, and that's why you want to have pooling from time to time,

**[1:16:37 – 1:16:51]** pooling layers. We discussed that you can apply convolutions to inputs of other dimensions,

**[1:16:51 – 1:16:57]** to inputs of other different nature, it doesn't matter. As long as you can tile it with something,

**[1:16:58 – 1:17:04]** you can do a convolutional net. And we also went through a specific example.

**[1:17:05 – 1:17:10]** Well, before we close, I honestly think I need to go pretty soon,

**[1:17:10 – 1:17:17]** but before we close, let me just tell you a couple more practical tricks

**[1:17:17 – 1:17:23]** about how convolutions actually work, because you will need them in practice,

**[1:17:23 – 1:17:26]** and you will need them to understand what goes next.

**[1:17:28 – 1:17:39]** So trick number one, let's go back to this input tensor.

**[1:17:40 – 1:17:42]** This time I will not be drawing the depth,

**[1:17:43 – 1:17:45]** so let me just draw it as a two-dimensional grid,

**[1:17:46 – 1:17:56]** so a grid like this, and what am I doing with it?

**[1:17:57 – 1:18:03]** I'm tiling it by, let's say, 3x3 windows or whatever.

**[1:18:05 – 1:18:11]** I'm tiling it by 3x3 windows, and as we just discussed,

**[1:18:11 – 1:18:17]** every time that I apply a 3x3 convolution,

**[1:18:17 – 1:18:21]** not every pixel can be the center of a 3x3 window, right?

**[1:18:21 – 1:18:26]** So we just discussed that when I apply convolutions

**[1:18:26 – 1:18:30]** just by overlapping everything and fitting as many tiles as I can,

**[1:18:31 – 1:18:38]** well, I can't fit as many tiles as there were pixels.

**[1:18:39 – 1:18:41]** And sometimes that's really inconvenient.

**[1:18:41 – 1:18:48]** So sometimes what you really want is you want to preserve the shape of your tensor.

**[1:18:48 – 1:18:52]** So if you had D times W times H as input,

**[1:18:53 – 1:18:55]** then after a convolutional layer,

**[1:18:55 – 1:19:03]** you would have a D times W minus K times H minus K.

**[1:19:03 – 1:19:06]** And I don't want this minus Ks.

**[1:19:07 – 1:19:10]** I want to have a tensor of the exact same shape.

**[1:19:10 – 1:19:15]** It will be, for example, I want to have like a dozen such convolutional layers in a row.

**[1:19:15 – 1:19:16]** I want to repeat this.

**[1:19:16 – 1:19:20]** I want to stack the same layers, and I don't want to change the dimensions.

**[1:19:22 – 1:19:32]** Well, when that happens, what you actually want to do is you want to use so-called padding.

**[1:19:33 – 1:19:42]** Padding just means that suppose that I need to have this pixel also be the center of a 3x3 window.

**[1:19:42 – 1:19:51]** So I draw a window, a 3x3 window around this pixel, and I notice that it goes outside of the image, right?

**[1:19:52 – 1:19:57]** Well, why don't we just play that, let's say, with zeros?

**[1:19:58 – 1:20:00]** Just say that these pixels are zeros.

**[1:20:00 – 1:20:00]** That's it.

**[1:20:02 – 1:20:04]** And now that would be zero padding.

**[1:20:07 – 1:20:14]** And now we are done, we can preserve the size.

**[1:20:14 – 1:20:26]** So that's just a stupid practical trick to pad the image with something in order to be able to hit more windows.

**[1:20:27 – 1:20:29]** And so there are two common ways to do padding.

**[1:20:30 – 1:20:37]** One is pad with zeros and the other is, let's say, I want to have a window like this.

**[1:20:37 – 1:20:41]** So when you pad with zeros, there can be a strange effect.

**[1:20:41 – 1:20:51]** Like you could have like a border around your image of some not really plausible features

**[1:20:51 – 1:20:55]** because these features take lots of zeros on the side, right?

**[1:20:55 – 1:21:01]** So if you want to avoid that, you may want to have like mirror padding.

**[1:21:01 – 1:21:06]** You may want to just take these guys from here and just copy them,

**[1:21:06 – 1:21:09]** like do a mirror image of your image over there.

**[1:21:09 – 1:21:13]** That's also a valid way to do padding.

**[1:21:13 – 1:21:14]** Often people do that.

**[1:21:15 – 1:21:21]** But the whole point is to be able to fit more tiles,

**[1:21:21 – 1:21:26]** to be able to make any pixel in the input the center of a tile.

**[1:21:30 – 1:21:34]** And one more trick is this.

**[1:21:35 – 1:21:47]** So as I said, if you just keep tiling your tensors with all possible tiles,

**[1:21:47 – 1:22:08]** you will not be reducing the geometry fast enough.

**[1:22:08 – 1:22:12]** You will have to resort to things like pooling layers.

**[1:22:12 – 1:22:14]** You will have to reduce your geometry artificial.

**[1:22:15 – 1:22:18]** Well, there is a different way.

**[1:22:19 – 1:22:21]** Okay, very simple.

**[1:22:21 – 1:22:28]** What if I just take not every pixel as the center of a tile,

**[1:22:28 – 1:22:34]** but what if I take like every second pixel as the center like this?

**[1:22:36 – 1:22:51]** So I have like the green window, the green 3x3 window over here, the light blue over here, the red one over here, and the dark blue one over here.

**[1:22:53 – 1:23:01]** So at this point, I have four times fewer tiles, right?

**[1:23:01 – 1:23:08]** I have cut my number of tiles in half across the width and in half across the height.

**[1:23:09 – 1:23:20]** So now when I get to the output from this, I will have a tensor of size approximately W over 2 and H over 2, right?

**[1:23:20 – 1:23:24]** Depending on the padding, there may be some plus or minus ones, but more or less like this.

**[1:23:26 – 1:23:29]** So it's exactly the geometric effect that we often want.

**[1:23:29 – 1:23:33]** We reduce the geometry by a factor of 2, right?

**[1:23:33 – 1:23:38]** On the other hand, notice how I'm not losing anything.

**[1:23:39 – 1:23:41]** Like every pixel is still covered.

**[1:23:42 – 1:23:44]** It's just covered not as many times.

**[1:23:46 – 1:23:58]** So before, if I tile everything, then like this pixel is part of this window and this window and this window and this window and this window and many different windows.

**[1:23:59 – 1:24:05]** Over here, well, now the maximum number of windows is 4 and usually it's less.

**[1:24:05 – 1:24:13]** Like this guy will only be covered by two windows, two tiles, but still every pixel is covered, right?

**[1:24:13 – 1:24:16]** So we are not missing anything, we are not losing any information.

**[1:24:16 – 1:24:21]** The network is still perfectly able to get everything and process everything.

**[1:24:22 – 1:24:28]** So this is a reasonable way to reduce geometry 2 and when it happens, it's called a stride.

**[1:24:30 – 1:24:40]** Stride, so for example, this would be stride 2, like if you don't do anything, it will be stride 1 if you just tile with every possible tile.

**[1:24:40 – 1:24:50]** So to summarize what we've discussed today, when you do a convolutional layer, what do you define?

**[1:24:50 – 1:24:58]** Well, you define the shape of the tensor, like d times w times h times d prime, right?

**[1:24:59 – 1:25:03]** And d is the depth of the input, d prime is the depth of the output.

**[1:25:04 – 1:25:09]** You define the padding if you want to pad the input with zeros or something else.

**[1:25:09 – 1:25:12]** And you also define the stride.

**[1:25:14 – 1:25:24]** And for, I mean, nobody actually uses it, but formally, of course, the stride is a two-dimensional thing because it's two numbers,

**[1:25:24 – 1:25:35]** because nothing prevents you from going like every second pixel across the x-coordinate and every third pixel across the y-coordinate, right?

**[1:25:35 – 1:25:37]** It doesn't have to be that equal.

**[1:25:37 – 1:25:39]** So formally, it's two different numbers.

**[1:25:39 – 1:25:46]** Of course, most usually they're the same, but the stride defines how you tile.

**[1:25:46 – 1:25:54]** Rating also defines how you tile and what do you add to the, what do you add?

**[1:25:54 – 1:26:04]** And the convolution, the convolutional tensor, the size of the tensor defines how many features you get.

**[1:26:07 – 1:26:07]** Okay.

**[1:26:08 – 1:26:10]** Okay.

**[1:26:11 – 1:26:11]** Okay.

**[1:26:12 – 1:26:22]** Well, I think, actually, actually, I think I want to stop at this point.

**[1:26:22 – 1:26:27]** So, I, unfortunately, I have to go.

**[1:26:28 – 1:26:31]** Are there any, okay, question, are there any downsides to doing this, to doing the strides?

**[1:26:32 – 1:26:39]** Well, again, every pixel now participates in the processing fewer times.

**[1:26:39 – 1:26:42]** So, maybe you don't want as much sparsity or something.

**[1:26:43 – 1:27:05]** But actually, the general trend of how convolutional networks developed was, as time went by, we did pooling less and less often.

**[1:27:05 – 1:27:09]** So, pooling actually has some undesirable properties.

**[1:27:09 – 1:27:16]** Pooling cuts off lots of computational paths as well, and pooling kind of distorts the gradients.

**[1:27:17 – 1:27:23]** I won't go into details, but basically, there are bad side effects of pooling.

**[1:27:23 – 1:27:34]** And when we get to modern architectures, you will see that, starting from things like Inception ResNet and some more involved architectures,

**[1:27:34 – 1:27:42]** you will see that they reduce the geometry, of course, but they reduce it with, not exactly with a stride,

**[1:27:42 – 1:27:49]** but they reduce it with like a complex subnetwork that basically, at some point, does strided convolution,

**[1:27:50 – 1:27:55]** that at some point does something like this, and then also does something else.

**[1:27:55 – 1:27:56]** But we'll get there when we get there.

**[1:27:56 – 1:28:06]** Okay, guys, it's been a pleasure talking to you today.

**[1:28:07 – 1:28:16]** Sorry that this lecture is a little bit messy, but I hope that I'll get settled by next week, and we will continue.

**[1:28:17 – 1:28:19]** Thanks a lot, and bye-bye.

## Full text

Okay. Hello, everyone. We are continuing our discussions of deep learning and this time I am in a very noisy and not really comfortable place, but I hope that the combination of modern deep learning based noise removal techniques will work. And I hope you will hear me fine. I hope the recording will be fine. So, in any case, we stopped last time at stochastic gradient descent algorithms, right? So, basically what we discussed on the previous lecture was that, you know, a neural network is a big composition of little things, is a huge computational graph. And then, there are two different kinds of inputs for the neural network. There is the actual input, which acts like a picture. Today we will be switching to pictures, mostly. And then there are the weights, right? And yesterday, not yesterday, but two days ago, we discussed that the output of this whole computational graph would be the loss function, right? Loss function of x, y, and w, and there is also the correct answer that comes in probably at the end somewhere. And then what we actually do is we compute the overall loss function L, w, which is like the sum or the average of the small losses, of the losses on every step along the way. And then we do gradient descent, right? I'm starting with the recap because you told me that some people might do it. So then we update the weights with something like this, but not really. So we use something like this, but really we use something much more involved and complicated like, for example, the A-demovers. And that's how deep learning works in general. There still are a few general remarks that I want to make and that I will probably have to postpone, definitely not today, so I will have to postpone them probably to the beginning of next week. I still want to discuss weight initialization, which is a pretty interesting and nice topic in itself. And also I want to discuss normalization layers. You probably have heard of batch norm, batch normalization. There are several different flavors of normalization layers and what exactly they do and why they are necessary is also, in my opinion, a pretty interesting topic. But today we actually start talking about not in general what happens with the loss function still being a black box, but what happens inside this black box, right? So today we start talking about architectures of neural networks. The word architecture, in this case, basically means what's in here, what is the structure of this computational graph, and we already kind of know that it can be any directed acyclic graph, anything would work, and the only requirement is that first there are no cycles, right, so you need to be able to traverse the graph in topological order in one direction and then in the opposite direction, but also what we need to do is, what we need to be able to do is to do the elementary computations, the forward propagation and the backward propagation inside every one of these nodes, so the general picture is like this, you have elementary nodes, they constitute a graph, and you do one pass of forward propagation, one pass of web propagation, and you have your gradient, then all of these algorithms that we discussed last time, you can. So, this is the general picture, and immediately we can start just thinking about how this graph might be organized. For example, you could do it, and usually people do it, in a layered architecture, so there are layers, right? Onions have layers, and ogres have layers, famously, and what a layer means is that as you go left to right through this architecture, as you go along the computational graph, the neurons, let's say, let's call them neurons for now, the perceptrons or whatever, like the components of this layer, talk mostly to the components of the next layer, and then those components talk to the components of the next layer, right, and so on until the end. So layers are kind of these sequential slices of the computational graph, and I'm deliberately not really trying to make it formal or anything because in reality, it's a murky concept, right? So, yes, sometimes a layer indeed is characterized exactly like this, but sometimes you would have something like a skip connection, for example. So, we will see in our class, we will see networks where there are connections that go around the layers. We will definitely see around the layers from layer 1 to layer 3, and we will definitely see connections that go around a given layer and just not touch it. That would be the residual connection, and we will definitely talk about those. They are one of the most important ideas here. But anyway, the notion of layers is useful, and the first, the easiest, the most straightforward class of architectures are the feed-forward, or, well, okay, feed-forward is a more general term, but let's say fully connected networks. Fully connected networks. I don't want to make a big topic of them because there is really nothing to say. So in a fully connected network, you have layers. Every layer is a set of perceptrons, and this time it works exactly like you would expect. So the perceptrons inside a layer don't talk to each other. They talk, they receive inputs from the previous layer, and then they send outputs to all neurons of the next layer. That's what it means in this case to be fully connected. It's not a fully connected graph. But it's a fully connected bipartite graph between every pair of layers. And then probably it all comes together in a single or at least a smaller amount of perceptrons on the other end, and that gives you the output Y or whatever you want. Okay, so fully connected networks, they were important. Fully connected layers are still important. You will see a fully connected layer inside the transformer, for example, when we get the transformers. But today we start discussing a more interesting kind of architecture, a slightly more involved kind of architecture, and that is convolutional neural networks. So what are convolutional neural networks? What is the basic idea? Well, this is one of the last times, I think, in class. Maybe there will be one more time, but that's it. One of the last times in class when I will actually go back to the biological motivation of everything that's happening. So we discussed how artificial neural networks were inspired by the human brain or by the animal brain, and we discussed how the principle of connectionism actually works. But, oh, and by the way, I think we didn't discuss it, so let me just take a very quick detour here. Let me give you a very, very short remark. We discussed gradient descent in neural networks, and all artificial neural networks today are trained with gradient descent in one way or the other, so the difference is not in the basic principle, the difference is in the form of the loss function, the form of the training set, maybe definitely the architecture, etc., etc., but not in the basic principle of this solving an optimization problem, right? You have a loss function, you have a way to compute its gradients, and then you use these gradients to optimize. Well, here is a funny thing. The brain, the human brain, cannot work this way at all, and that is kind of obvious when you look at the biological structure that we discussed. So even without actually understanding how it works, even without actually knowing what the mechanism is, you can definitely say it's not gradient descent. Why? Because, as we discussed, the biological neuron, this little guy, has a lot of dendrites coming out of here, right? And the little guy also has a single axon that is the output of the biological neuron, right? And that's it. So a biological neuron can compute only one function. And to have gradient descent, you need every node in your network to compute at least two different functions. You need to be able to go forward, but you also need to be able to go backward, right? And I told you how to implement your own node in the computational graph in PyTorch. What you would actually have to do is you would have to implement two procedures, f-prop, forward propagation, and b-prop, backward propagation, what the function actually does when it goes, when you compute it, what are its derivatives, how the gradients should be recomputed as you do back propagation. Well, here is the thing. The biological neurons, the neurons in our heads cannot do that. They only have one output. So what this actually means, and this is an even deeper point than it might seem. So, okay, they cannot do gradient descent, so they have to do something else. And also what it means is that this something else that they do also has to somehow send the signal back from the end, from the point where the loss function is actually computed. I mean, I don't think it ever is explicitly computed in our brains, but somehow, at least theoretically, it's there. So between the end goal and whether we achieved it or not, you need to have a connection from there, from the end of the chain to every neuron up there, right? So you need to have loops in the human brain. In the biological brain, you absolutely have to have connections that go from here or back here, back there and everything. You have to have a lot of feedback in the brain in order to train. And the brain does have feedback, right? So here is where the analogy totally and completely ends. So we discussed that one neuron is actually a pretty good model of what's happening in the brain. One perceptron is a pretty good model of the biological neuron, especially with real activations. We discussed that, yes, our brain also works on the principle of connectionism, that is, a huge composition of simple functions can give you something very complicated. But, it cannot run on gradient descent, definitely. And the architecture cannot be similar at all. So, the brain also has layers, we'll see it just now, but between every two layers, there are feedback connections that go back. And from later layers, there are feedback connections that go all the way back. I mean, it's a mess. We don't really understand in detail what the brain's architecture is. We understand it generally in terms of, well, this is the visual cortex, and here are the layers in the visual cortex, but the actual fine structure is very, very difficult, of course. Okay, so with that remark out of the way, let's go back to these guys. These guys are Hubel and Weasel, Thorsten Weasel, and I forget the name of Hubel, who got their Nobel Prize for studying the visual cortex. And convolutional networks are partly motivated by the visual cortex. That's why I'm talking about this. But again, there will be a point where the analogy just will have to stop. I'll tell you when it happens. But first, let's begin with the bio. So back in the, I think, 1960s, 1970s, they made their famous studies of the visual cortex. And as it quite often happens in biology and in sciences like this, their actual truly novel thing that they did was having a new device. So what their advantage was compared to everybody who was before that was that they could actually make such tiny electrodes that you could attach the electrode to a single neuron and read off the activation of a single neuron on a live brain. Right? So before that, all the people could do was, you know, hope that some guy would get in the motorcycle accident and then have a stroke. And then the stroke will give you some interesting information about which part of the brain does what. But these guys, they could actually, well, okay, this is not my favorite part, but they could take a cat. If you look closely, there is a very well, fixated cat over here. And then they would actually slice open the head of the cat, of course, on painkillers. And then they would be able to attach electrodes to individual neurons and see what the individual neurons in the cat's brain actually respond to. And what they did, so what they found was that, okay, so it had been known that the visual cortex is back here in the occipital lobe, in mammals, in us and in cats. It's actually a very bad decision of nature. It's a very fragile thing that makes absolutely no sense because your eyes are in front over here. And then there is this optical nerve, this big fat pile of connections that goes all the way through your skull backwards. And, of course, it would be easier to just have the visual cortex in front, but I think the evolutionary explanation is that back when we were very far from mammals, we would have the proto-eyes up here on top of the head. And then somehow the eyes went over here and the part of the brain that processes it went over there. I have no idea why. Anyway, it is known that the visual cortex is here, the part that processes visual input, and it's easy to find like the first layer of the cortex. It's easy to see that, okay, here is where the optical nerve attaches, so these neurons take the immediate inputs from the eyes. And if you actually look at what a single neuron activates for, what a single neuron is doing on this first layer of the visual cortex, you will see that, first of all, it cannot, of course, see the whole picture. It has only that many inputs, and it has a small receptive field, as it is called. It looks at a relatively small part of the general picture, and in this small part, it recognizes something really, really simple. So on this slide, you see a sample neuron that recognizes vertical lines. So if it sees a bright vertical line in its field of vision, great, it's activated a lot, and even if you still have just a single line, but you start to rotate it, the activation dies out and basically goes to zero. And then what would you expect next? Well, you would definitely expect that then you would have layer two, the second layer that would feed off the outputs of the first layer. So it would somehow combine these simple shapes into something more complicated. Like if you had one neuron that recognizes vertical lines, another neuron that recognizes horizontal lines, boom, you put an end. You have a neuron that gets an end across them, and now you have a neuron that recognizes across in its receptive field and its visual field of vision. And Hebel and Weasel did this, and they also studied the second layer. So they discovered neurons like I just said. But then they somehow didn't go any further, and they started doing other things. And actually, that was a pretty wise decision because, again, the brain is very, very complicated. And if you look at some simplified representation of the visual cortex, you will actually see that there are layers from V1 to V4, then V5, V6, et cetera, et cetera, and, yes, there are layers, but it's not an artificial neural network. The actual structure is much more complicated. There is all sorts of feedback that goes back. There are all sorts of connections, and, yeah, I keep showing this picture for the last 10 years or so, and I suppose that since the last 10 years, it has become much more complicated. So this is from some survey, and this picture was called the most important neural pathways in the early layers of the visual cortex. So you can actually see that, yeah, there is a very well-defined first layer. Yes, the optical nerve does come in somewhere, so the first layer is easier. The second layer is also kind of clear, and then it's just a mess. Then it's like a lot of different components that do different things, so they are all interconnected with each other. Anyway, when people saw that, when they saw how small geometric shapes gradually go up layer by layer, and we didn't have a clear picture of what happens next at that point, but clearly at some point, the picture would go to something like face recognition, right? So some very complicated computer vision problems would be solved in our human brain very quickly. So people, of course, try to imitate stuff like this in computers. And actually, convolutions and convolutional networks are a very old idea. They date back at least to this very interesting architecture called the neocognitron by a Japanese researcher named Kunihiko Fukushima. He did it in the late 1970s, and I actually, if you're interested in the history of deep learning, I actually recommend you to read these papers. It's like, it's a two-page paper. It's very short, and you can definitely read it. There's nothing too complicated in there, and when you read it, you see that in 1979, he had a deep neural network, several layers. It was a convolutional network, and it had real low activations, these hinge activations that we discussed last time and that I told you only came into common practice in 2011 or 2012. But the thing he didn't have, the thing he didn't have in 1979 was learning. So there was a big composition of simple things, and they were convolutions, but they were not trainable convolutions. They were just some fixed filters that he would apply across the image. Anyway, whatever. So in a modern form, convolutional networks appeared in Jan LeCun's group. That's the main claim to fame by Jan LeCun. He developed convolutional networks for many, many years, for several decades. And in the late 1980s, they appeared already certainly in their modern form. They had training, they had convolutions and everything. And let me just walk you through a few images that will show how convolutional networks work. And it's such a brilliant idea that it's... Well, okay, it's just a brilliant idea. It's a very brilliant idea of what I would call structural regularization. You'll see what I mean. So first of all, let's have a picture like this one. And let's assume that I want to process this picture. So what do I mean by processing? Well, maybe I want to solve some computer vision task. Maybe I want to, for example, find the little boy's head on this image. So that would be object detection. We'll discuss object detection later. So where is the boy's head on this image? And the main observation, the main idea, the main assumption that is behind CNNs, that is behind convolutional neural networks, is that, well, if I'm looking for something, for some feature on an image, then it's the exact same function applied all across the image. So if I have a black box that looks at a small window and says, well, that's a boy's head, or no, that's not a boy's head, then it will be the exact same black box that I'm supposed to apply across this whole big picture, and just the output will be different. So here it will say yes, and over here it will say no. But the function is the same. The inputs are different, so the outputs, of course, are also different. So the idea of convolutional neural networks is this. Let's take a picture, or any input is just easier to, more clear to reason about pictures, but take any input, break it into small windows like this. Usually they are overlapping, like shown here. Then, for every tile like this one, apply a small neural network. So, now this small neural network is a model that we need to train, it will have weights, we will do gradient descent, etc., etc., but it will be small. It will be applied only to this little tile, a few pixels across, that we split the picture into, right? And the big gain here, the profit, is that now I take the exact same small neural network and I apply it to every single tile across the input. So I take this tile, I apply the neural network, I get this, let's say, output vector. Usually you would want to extract not one feature, but several features. So usually the output is several numbers. And then I take the next tile, I apply, I get some more. And so when I actually do that, get back to the board, when I actually do that, what I get as a result, so here is my input picture, right? I break it into windows, like I showed. And then I take each window, okay, yeah, okay, let them be overlapping, whatever. I take each window, I put it through my small neural network, and let me draw it horizontally, I get this vector of features, right? Then I take the next window over here, I put it through the exact same neural network, and I get a different vector of features that goes here. Okay, now this will be a massive picture, but anyway, as I take each one of these windows, I get a vector of features, and then these vectors of features themselves also have this geometric structure, right? So there is a top right window, there is a bottom left window, and the bottom left window will give me this bottom left vector of features and so on, right? So as the output of this procedure, I will get a three-dimensional tensor, right? I will still have some width, some height, and now I will also have a meaningful depth. So actually, the input also usually has depth, for example, because these days, for the last few decades, pictures are usually in color. So even on the first step, if you have a color image, you have depth three at the input, right? In general, what you get at the output of a convolutional layer is a 3D tensor, if you start with a 2D input in structure, like a picture, and then you can do the same thing, right? So again, you take its pixels, you take this structure over here, and you tile it with windows, with small tiles, and then you take this small sub tensor, this small window out of here, and you pass it through another small neural network, and you get another vector of features. And again, you repeat this, this was the top left vector of features, but then you get another tensor, and so on and so forth. I'm sorry, I'm not in a convenient place to draw a nice picture, but I hope you understand what's going on. So on every step, we tile the image into tiles like this one. It doesn't have to be the original image. You can chain these layers one after the other because always you are working with like three-dimensional arrays, which in deep learning are confusingly called tensors, but what can you do? So you're working with three-dimensional tensors, and you just convert one 3D tensor to another as you go with this procedure. And then you can have like a whole sequence of these convolutional layers. So before we proceed, one more thing about this. In classical convolutional neural networks and in many architectures that we will see today, there is another type of layers. Like there is a convolutional layer. That's the one that we just discussed. And then there is also what is called the pooling layer. And let me maybe first give you the motivation for it. And then the actual layer is actually pretty simple. So the motivation is this. Let's again try to look at what the neurons do. So this is our original image. And it has lots and lots of pixels, right? It has big width, big height. Then I slice it into very small tiles. So, of course, in my picture, they're not small, but in practice, they're small tiles. So I have this tile of, let's say, three by three pixels. And it's a color image, so it has depth three too. So it has a small height, a small width, and then it goes through the neural network, and then we get our vector of features. So this vector of features, this one, depends only on this small three by three tile, right? So if you look at it in the other direction, you can say that for this feature, this feature has a receptive field, it's called in this part of science, receptive field, has a receptive field of three by three pixels. So it only looks at a very small, very local part of the image, right? So what happens next? Suppose that I cover this whole image with three by three windows like this, and then as a result, I will have a 3D tensor like this, and then I do another convolution. I do another three by three convolution over here, okay? So I cut off, I cut out another three by three by something. Now the depth is probably more than three, but anyway, I cut out another three by three by D tensor, and I put it through a small neural network and so on. I get a feature over here. What is its receptive field? Well, it looks at these features inside this parallelepiped, right? At the features inside this small part of the tensor. And these features in turn are looking at more pixels than before, right? So if I had a three by three over here and another three by three over here, which goes to one here, so now this guy corresponds to this, and this guy corresponds to a window over here, right? So overall, this pixel over here would look at a five by five window in the original pixels, right? That's my point. So if you do a three by three, and then the results of your three by three you compose in another three by three, then you collect information from a five by five window originally, right? But five by five is also a pretty small window. So like how many layers would you need to have neurons that look at the whole picture? On every three by three convolutional layer, you just add two to the width, and you don't multiply by two, you just add two to the width, and add two to the height of this receptor field, right? So if I want to process a 256 by 256 image, I would need like 130 layers. That doesn't make any sense. I don't want to have that many layers. So in the original convolutional networks, you would somehow need to solve this problem. That is, you would need to reduce the geometry, and this is an important way of looking at it. We will talk about reducing the geometry a lot in this class. But you want to reduce the geometry quicker than by just tiling everything and hoping that, you know, convolutions will do it by themselves. So in the original neural networks, in the original CNNs, they had, and you can still see it today in some architectures, they had this idea of a pooling layer. So let's suppose that I had a convolutional layer, I expected some features, and then I can say, well, you know, there are too many. The width and height are too big, I want to reduce the geometry. How could I reduce the geometry? Well, I could just slice it into small windows, this time no overlaps, that's the whole point, no overlaps, usually it's two by two windows, but of course you can say it whatever you want, and just replace in every two by two window, out of four features leave only one, according to some rule, right? And there are two commonly used rules, I think anything else just reduces basically to one of these two in effect, so there is max pooling, where you take the maximum of the feature values in this small window, and there is average pooling, where you average them. I don't think I've ever seen anything else in practice, and usually it's max pooling, so usually it's max pooling, why? Because it kind of makes sense for feature extraction. So, okay, so the real answer is because it works better usually, but the justification is that it urges convolutional layers to actually extract more meaningful features. So if you, for example, so let's look at this picture and let's say, okay, so I want to like have a black box, have a feature extractor that says, is there a little boy's head in this tile? And so when I run it on this tile, I get a one, right? But when I run it, say, on this tile or on this tile, I get basically a zero, even if it's like perfectly understands everything. So then let's suppose that I have this bigger tile that combines the small tiles over here that glues them together like pooling does. And then I ask, well, what is the proper composition? What is the proper combination of features that will answer the question, is there a little boy's hat in this tile? And that would be the max, right? If I average, I get some pretty low average because most tiles don't have a little boy's hat, right? And only one tile would have the little boy's hat and the rest wouldn't. But meaningful features like something is there, they obey the max law, right? And less meaningful but sometimes also useful features like how green it is, this feature would obey the average law, right? If I have a big tile which is half green and half blue, I would probably want to say that it's half green. It's not fully green. But for features corresponding to objects or whatever shapes, max is usually the way to go. Anyway, that's just a rambling justification of why max pooling. All right. And so now when you combine convolutional and pooling layers, you can start reducing the geometry really, really quickly because every pooling layer cuts the width and the half by two. Let's assume it's two by two pooling. It's almost always two by two pooling. So every pooling layer cuts the width by two, cuts the height by two. So you get twice, you get four times fewer pixels, four times fewer numbers. And then you can do another convolution, blah, blah, blah, and so on. So at this point, what I want to do is I want to actually discuss how you would define a convolution, like what it actually is, and then we will just work through an example where, I apologize, then we would just work through an example where we would see the beauty of convolutions, where we would actually realize why convolutions save so much, why they are such a great way to process large inputs. So, what exactly could this neural network be? Well, the word convolution doesn't really mean anything specific, it just means that I tile the input with small tiles, and I apply my transformation to every tile separately. So, this is what the word convolution means. It doesn't tell you what exactly this transformation should be. But usually when people talk about convolutional layers, they mean the simplest neural network possible. The simplest neural network possible, that is just one fully connected layer. So, it looks like this. I have my input, now let me do it in full generality. So, I have a three-dimensional input. It has some width capital W, some height capital H, some depth D. And I cut out a subset, a tile, which has width small W and height small H and still depth D. So, this is also important. I always cut through all the features. I take all the features, all the depth. So, then I take this guy and basically I say, well, okay, here I have like a D times W times H tensor, right? I have this three-dimensional matrix of three-dimensional array of numbers, right? But when I go inside this neural network, I don't care about the structure of this array. I just lose it. I just say, okay, so I have this many numbers. You can actually visualize it as flattening it to a single vector of size dWh, and then I just apply a matrix of weights to it. I have some matrix of weights. So the output will be a vector of size, let's say, d'. And this vector of size d' is just w times this d'. So the matrix w, how many weights does a convolutional layer have? the matrix w uh has is supposed to have like um uh it's supposed to be well okay so just to make it more convenient let's say um it's z times w so w uh would be like dwh times d prime okay um so it would be dwh times d prime uh and um and then and and then yes i lost my train of thought a little um dwh times d prime yeah and then uh the beauty of convolutional networks is that now when i take another window over here i also have an input of the same size and i reuse the exact same matrix w right so uh these many weights are needed to process the whole image i don't uh i don't have a different w for a different window i have the same double i reuse the weights so these many weights are needed to process the whole d times big w times big h input and as as you can notice the number of weights doesn't depend on the size of the input it only depends on the size of the window so when i have a convolutional layer it's very easy for me to say oh okay so my my input image is now twice larger but let's just run the convolution across the larger image i don't care uh i only care about the size of the window uh and of course formally and like in reality what you have here is a matrix of of these dimensions but it would be very very inconvenient if if we humans had to think of of this matrices as you know some huge number times d prime and then this huge number we would have to memorize and think of oh okay so that was like three by three by 32 how many is that oh this this should be the size of course that's very inconvenient so in in practice if you for example set up a convolutional layer in pytorch um it wouldn't be a 2d matrix uh the convolutional the convolution would be defined by a four-dimensional tensor so your tensor of weights would have size d times w times h times d prime and what would actually happen is your input is a three-dimensional tensor which is supposed to match the first uh three dimensions of w and that means that your output is is a vector of this dimension okay uh so in practice you would define like four-dimensional tensors when you when you set up convolutional layers and by the way while we are at this while while we are defining this note that uh it is absolutely positively uh it absolutely positively uh doesn't matter uh that the input is specifically uh a picture that specifically is like a 3d tensor with some width some height and some depth uh you can surely have convolutional networks for other kinds of inputs for example uh at some point now of course nobody does this but at some point uh you could there were cnn's designed for text processing and what is text text is a sequence right it's a sequence of tokens and um every token gets represented in by some vector uh so it's a sequence of vectors right it's a it's a 1d object one-dimensional object that produces a two-dimensional input tensor and sure enough you can have one-dimensional convolutions no problem at all you just just your windows are now sliding windows like this you take like three uh neighboring vectors your small input is like this it's um well it's d times l length of the window and then you multiply it by the matrix w which now is a three-dimensional tensor d times l times d prime and you get the result which is a vector of size t prime almost no difference at all just all all dimensions uh change by one and that's or you can go in the other direction you can say well but what if i have let's say a video i have a video which means that i have a sequence of images so now my input is like d times w times h times let's say t for time right if this is a video so now there are there is a sequence of images and every image is a w times h times d tensor and of course you can multiply it by a five-dimensional tensor w which is t times w times h times t times d prime that's it right so um you can apply the same idea of cutting stuff into small tiles and processing each tile separately you can apply it to anything it just so happens that it was especially productive for uh images and basically all of the examples in our class since it's a computer vision class of course all of the examples in our class will be uh will be images okay so um okay okay so with this let's maybe look at a specific example um let's look at a specific example of a convolutional network yeah this one uh and i just want to go through this network layer by layer it's some classical leonet architecture from i don't know 2001 or something uh it's very small it has very small input not very powerful but i want to to go through this architecture to count the weights to get a feeling of what convolutional networks look like and we will see like what's the whole point of convolutional networks when we discuss how many weights they have so um so let's look at this slide what do we have here we have the input which is a 32 by 32 picture and it's a black and white picture well a gray scaly picture so it has depth one so our input and let me switch from from the picture to the board for a little bit so our input uh is a tensor of size 1 times 32 times 32 okay then a convolutional layer happens and this picture doesn't show you the weights doesn't show you the layers themselves it shows you the intermediate results the tensors that result from every layer so now it says that after the first layer you have 28 by 28 tensor uh with six feature maps when people say feature maps it's the same as channels the same as depth so basically it says that it's a 28 by 28 by 6 tensor okay six different features uh so we started with a 32 by 32 by one then something happened a convolutional layer happened and now we have a tensor of size uh 6 by 28 by 28 so the question to you how large do you think was the convolution what was the size of the window if we went from 32 by 32 pixels to 28 by 28 pixels why would why would the geometry be reduced why would the convolutional network actually have less pixels at the output so i'm covering the input by overlapping tiles all possible tiles how many tiles are possible okay so this this is our first remark here so i have this input which is like a 32 by 32 pixel image of course i won't draw the full 32 and then i start covering it by tiles of some kind of size right let's say three by three tiles but how many tiles will fit not 32 by 32 right so you see uh for every tile uh every tile is defined by its center pixel let's say right so this center pixel corresponds to this three by three window usually it's odd there are very few even convolutions so i i will i'm safe uh talking about the center pixel so there is a center pixel corresponding to the three by three tile this center pixel corresponds to the three by three and so on but there is no tile that will correspond to this pixel right uh it doesn't fit so in effect uh how many if i had a three by three convolution the output if i just do the tiling if i just use all possible tiles not use any special tricks here the tiling would be would would not be able to use these pixels and also wouldn't be able to use these pixels right so it would cut off one pixel on top one pixel on bottom one on the left one on the right so if i did a three by three convolution and i had like a w times h image at the input i would go to something like w minus two times h minus two right because i would need to cut off two pixels on the sides well in here we go to w minus four and h minus four so how how big was the window yeah exactly so uh i mean of course it's not guaranteed there could have been tricks etc but the most plausible version of how this convolution what this convolution looks like judging by that picture and it's true in fact it's true uh is that it was we were covering the input by five by five tiles and then uh so what what is the size of the weight matrix here um yeah i didn't tell you that sorry uh i i'm when i talk about the weight matrix i of course simplify a little bit because in addition to the weight matrix there is also the intercept so in fact of course this output is like z w plus some constant so there there is an additional d prime weights which is also a weight right which is also which are also trained but let's forget about that it doesn't matter for us now let's just count the weights and the matrices themselves so what would be the matrix size over here the matrix size would be as we discussed uh there d times w times h times d prime right so here we have a convolutional weight matrix weight tensor of size one times five times five and we have six features at the output times six right so five five by five is 25 25 times six 150 right so over here in this layer we have 150 weights trainable weights that we will need to learn by gradient descent well there you have it that's that's that's the first point that i want to make with this example uh the convolutional idea the idea of sliding a window over the input saves a huge amount of weights so suppose that i wanted to have a fully connected layer over here suppose that i just wanted to have a single weight matrix that takes this guy's input and outputs this then how many weights would i have what what what kind of matrix would it be a fully connected uh first layer would be like 32 times 32 times 6 times 28 times 28 right so it would be a matrix of size input times output input size times output size if i didn't have this convolutional structure um and i still for some unfathomable reason would would want to to have this kind of output the matrix would have this kind of size so uh of course i cannot do this in my head but like 32 squared is about a thousand so this is like you know five million or something you can count if you want but this is like several million weights and the convolutional idea reduced this five million weights down to 150 so that this is the the power of convolutions the main power of convolutions they save a lot of weights and that's why i always say that what convolutions actually are they are an excellent technique of structural regularization we discussed uh last some previous lectures that regularization is when you um regularization is when you compress uh could compress the weights magnum smaller uh or reduce like reduce the set from which the weights are taken right but in this case it's even more straightforward like structural regularization means all right so i have five million weights and you could like if you think of it from a proper view view it from a proper angle you will see that you can actually think of a convolutional layer also as a transformation of this guy to this guy but when i do this transformation i say oh okay so i want this thousand of weights to be equal to each other and i just said this constraint that i always process every window be it over here or over here or over here i process it in the exact same way with the exact same weights that so that structural regularization when you impose constraints like this way it should be equal to each other this way it should just disappear to zero or something so so um so this is the power of convolutions and let's um so let's finish the the exercise that there are still a couple of points that i want to make here so after the first convolutional layer there is a pooling layer subsampling is the same as pooling layers so the pooling layer is obviously has two by two windows right so we go from 28 by 28 to 14 by 14 a question to you how many weights does this pooling layer have i had the 28 by 28 by 6 input i have 14 by 14 by 6 output which means that okay let's assume it's max pooling i don't remember which it was actually but i take a two by two window and in every two by two window across every feature i take the max of these four numbers um how many weights is that how many trainable weights so the pooling transformation takes the input uh cuts it into tiles and for every tile uh you take the numbers that are parts of your input and you leave only the max of these numbers like you take a two by two window every two by two window becomes just its maximum how many trainable weights are in transformation like this no all right not talking to me today anyway uh how many weights are in this transformation of course none of course there are no weights it's a deterministic function there is nothing to train i just take the max right so the uh the uh the pooling layers don't have weights and there is no no point for for them to have weights there is nothing to train i just do a specific fixed thing uh so okay so let me draw this uh next i have a pooling layer uh a pooling layer goes to 6 by 14 by 14 uh the pooling layer has no weights and then i have another convolutional layer uh right let's check i have another convolutional layer that goes down to 10 by 10 so um sorry check 10 by 10 by how many 10 by 10 by 16 so my next knowledge layer goes makes it like this um 16 by 10 by 10 so i i put depth first here but you don't have to you can put it wherever you want um so how many weights are here well again we reduce the width and the height by uh four so it's a five by five convolution but now we need to transfer uh translate six features into 16 features so like six by five by five by 16 okay that's more weights right so we know six by five by five is 150 and 150 times 16 uh 150 times four is six so six times four is 2400 weights right i i suppose that's correct uh 2400 weights over here okay then another pooling uh this part i remember and then we get uh wait for it there will be a little bit more interesting stuff here so now i have like 16 by 5 by 5 and at this point i say oh okay so now i have a 5 by 5 tensor with depth 16 so if i keep doing 5 by 5 convolutions it means that now there are no tiles really like the whole tensor is a single tile i don't have to cut it any longer which means that uh okay in the picture they call it a convolutional layer but now it really doesn't matter you could call it a convolutional layer or you could call it a fully connected layer you just take the whole input and you convert it to okay how many features so next you go to 120 features then 84 features and then finally the output of 10 so um you go to 120 then another fully connected layer you go to 84 and another fully connected layer maybe a softmax layer um you go to 10 so how many weights are here well in this fully connected layer i have 16 times 5 times 5 times 120 right so i compress the whole input down to the to a vector and i just lose all the geometry i don't care about the geometry anymore these are just global features numbers about the the the input image and but i still need to, you know, do stuff with them. I still need to toss them around a little to do some linear combinations of them to actually extract the signal that I want, not just reasonable signal, but signal that I want to actually get to the classes, for example, that I want to recognize. So, in classical conversational networks, after you go through all of these layers, after you downsample and downsample and downsample, at the end, you have a couple of fully connected layers usually. Sometimes it's called the head of the network, and sometimes our networks will have multiple heads that do different things, but for now, let's just say that I do need to have some kind of a classification head at the end with a couple of fully connected layers. And interestingly, it turns out that this classification head holds the vast majority of all the weights. You see? So over here, we have like, what, 400 times 120. We have 48,000 weights over here. And here we have 120 times 84, which is, I don't know, about 10k more, right? So out of the total 60,000 weights in this network, about 60,000, about 57,000, 58,000 lie in the classification head. And only 2,500 weights are in the convolutional layers. But the convolutional layers are doing the most important job. They are the Fisher extractors. And so how does it actually work during training? Well, remember how we discussed backpropagation. So if you have a single input going into several different places, then in the graph, then when you go back to the backpropagation here, your update, your gradient will be by the chain rule, the sum of, not the gradient, the partial derivative at this node will be by the chain rule, the sum across all of the paths. And in the convolutional network, every weight over here, every weight in this convolution, in this matrix, occurs in the computational graph, is input into the computational graph many, many, many, many times. So I don't think I can draw a computational graph for it here, but basically like this, you have this input, right? In the input, every pixel is a value, let's say, and now let's suppose that this weight like WI gets multiplied by the value of middle right pixel in the 3x3 window, which means that when we process this window, I will multiply it by this pixel and then add up and everything. When I process this window, I will multiply it by this pixel and then add up and everything. So the same weight, the same input to the computational graph will occur many, many, many times. It will occur in the processing of every single tile by the nature of convolutional networks. And that's why, by the way, ReLU activations are such a good fit here, because this means that we don't mind sparsity. Sparsity is bad if you have little signal, if you don't have enough signal, if you don't want to lose anything. But sparsity is great if you have an abundance of signal, if you have a lot of computational paths. Now, sparsity just saves you time. It doesn't really hurt you. It doesn't really hurt training. It just says that, oh, okay, so like in the processing of this window doesn't matter right now. So this guy will be a zero, and this part of the graph will not matter. But the processing of this window will still matter. So this weight will still get a meaningful update. So usually when you have the same weight occurring in many, many different places, it's a good idea to add some sparsity, and ReLU provides this kind of sparsity. Okay, so what have we discussed so far? We discussed the basic idea of convolutional networks, how you slide across the input. We discussed how the receptive field grows with time, that it grows not fast enough, and that's why you want to have pooling from time to time, pooling layers. We discussed that you can apply convolutions to inputs of other dimensions, to inputs of other different nature, it doesn't matter. As long as you can tile it with something, you can do a convolutional net. And we also went through a specific example. Well, before we close, I honestly think I need to go pretty soon, but before we close, let me just tell you a couple more practical tricks about how convolutions actually work, because you will need them in practice, and you will need them to understand what goes next. So trick number one, let's go back to this input tensor. This time I will not be drawing the depth, so let me just draw it as a two-dimensional grid, so a grid like this, and what am I doing with it? I'm tiling it by, let's say, 3x3 windows or whatever. I'm tiling it by 3x3 windows, and as we just discussed, every time that I apply a 3x3 convolution, not every pixel can be the center of a 3x3 window, right? So we just discussed that when I apply convolutions just by overlapping everything and fitting as many tiles as I can, well, I can't fit as many tiles as there were pixels. And sometimes that's really inconvenient. So sometimes what you really want is you want to preserve the shape of your tensor. So if you had D times W times H as input, then after a convolutional layer, you would have a D times W minus K times H minus K. And I don't want this minus Ks. I want to have a tensor of the exact same shape. It will be, for example, I want to have like a dozen such convolutional layers in a row. I want to repeat this. I want to stack the same layers, and I don't want to change the dimensions. Well, when that happens, what you actually want to do is you want to use so-called padding. Padding just means that suppose that I need to have this pixel also be the center of a 3x3 window. So I draw a window, a 3x3 window around this pixel, and I notice that it goes outside of the image, right? Well, why don't we just play that, let's say, with zeros? Just say that these pixels are zeros. That's it. And now that would be zero padding. And now we are done, we can preserve the size. So that's just a stupid practical trick to pad the image with something in order to be able to hit more windows. And so there are two common ways to do padding. One is pad with zeros and the other is, let's say, I want to have a window like this. So when you pad with zeros, there can be a strange effect. Like you could have like a border around your image of some not really plausible features because these features take lots of zeros on the side, right? So if you want to avoid that, you may want to have like mirror padding. You may want to just take these guys from here and just copy them, like do a mirror image of your image over there. That's also a valid way to do padding. Often people do that. But the whole point is to be able to fit more tiles, to be able to make any pixel in the input the center of a tile. And one more trick is this. So as I said, if you just keep tiling your tensors with all possible tiles, you will not be reducing the geometry fast enough. You will have to resort to things like pooling layers. You will have to reduce your geometry artificial. Well, there is a different way. Okay, very simple. What if I just take not every pixel as the center of a tile, but what if I take like every second pixel as the center like this? So I have like the green window, the green 3x3 window over here, the light blue over here, the red one over here, and the dark blue one over here. So at this point, I have four times fewer tiles, right? I have cut my number of tiles in half across the width and in half across the height. So now when I get to the output from this, I will have a tensor of size approximately W over 2 and H over 2, right? Depending on the padding, there may be some plus or minus ones, but more or less like this. So it's exactly the geometric effect that we often want. We reduce the geometry by a factor of 2, right? On the other hand, notice how I'm not losing anything. Like every pixel is still covered. It's just covered not as many times. So before, if I tile everything, then like this pixel is part of this window and this window and this window and this window and this window and many different windows. Over here, well, now the maximum number of windows is 4 and usually it's less. Like this guy will only be covered by two windows, two tiles, but still every pixel is covered, right? So we are not missing anything, we are not losing any information. The network is still perfectly able to get everything and process everything. So this is a reasonable way to reduce geometry 2 and when it happens, it's called a stride. Stride, so for example, this would be stride 2, like if you don't do anything, it will be stride 1 if you just tile with every possible tile. So to summarize what we've discussed today, when you do a convolutional layer, what do you define? Well, you define the shape of the tensor, like d times w times h times d prime, right? And d is the depth of the input, d prime is the depth of the output. You define the padding if you want to pad the input with zeros or something else. And you also define the stride. And for, I mean, nobody actually uses it, but formally, of course, the stride is a two-dimensional thing because it's two numbers, because nothing prevents you from going like every second pixel across the x-coordinate and every third pixel across the y-coordinate, right? It doesn't have to be that equal. So formally, it's two different numbers. Of course, most usually they're the same, but the stride defines how you tile. Rating also defines how you tile and what do you add to the, what do you add? And the convolution, the convolutional tensor, the size of the tensor defines how many features you get. Okay. Okay. Okay. Well, I think, actually, actually, I think I want to stop at this point. So, I, unfortunately, I have to go. Are there any, okay, question, are there any downsides to doing this, to doing the strides? Well, again, every pixel now participates in the processing fewer times. So, maybe you don't want as much sparsity or something. But actually, the general trend of how convolutional networks developed was, as time went by, we did pooling less and less often. So, pooling actually has some undesirable properties. Pooling cuts off lots of computational paths as well, and pooling kind of distorts the gradients. I won't go into details, but basically, there are bad side effects of pooling. And when we get to modern architectures, you will see that, starting from things like Inception ResNet and some more involved architectures, you will see that they reduce the geometry, of course, but they reduce it with, not exactly with a stride, but they reduce it with like a complex subnetwork that basically, at some point, does strided convolution, that at some point does something like this, and then also does something else. But we'll get there when we get there. Okay, guys, it's been a pleasure talking to you today. Sorry that this lecture is a little bit messy, but I hope that I'll get settled by next week, and we will continue. Thanks a lot, and bye-bye.
