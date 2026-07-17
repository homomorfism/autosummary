# Transcript — whisper_cpp

- **Provider:** whisper_cpp
- **Language:** en
- **Audio duration:** 3:12:14
- **Segments:** 1682
- **model:** ggml-large-v3-turbo.bin
- **vad:** True
- **beam_size:** 5
- **entropy_thold:** 2.8
- **latency_sec:** 1587.2

## Segments

**[00:01 – 00:33]** Good morning, everyone. Welcome to our next class. Today is lecture day and we will discuss transformers. This is probably the single most important lecture in our class, but before we get to transformers naturally, we need to finish what we started yesterday on recurrent neural networks, then we need to discuss attention mechanisms,

**[00:33 – 00:49]** and then from recurrent attention, we will get to self-attention and therefore transformers. They will indeed transform the entire field of deep learning as they did 10 years ago.

**[00:49 – 01:05]** Yesterday we stopped at the main problems of recurrent networks.

**[01:06 – 01:13]** Actually, I didn't make this point yesterday, so let me make it now.

**[01:13 – 01:23]** The main problems of recurrent networks are exactly the same problems that you have in deep networks in general,

**[01:23 – 01:33]** in networks with a lot of layers like the ones we've already seen in the convolutional side of things.

**[01:33 – 01:40]** So, the problem is that the signal gets saturated, right?

**[01:40 – 02:05]** The signal, oops, sorry, looks like my, my waveform is not working, no, okay.

**[02:05 – 02:16]** So, the problem with deep neural networks was that as you go through the layers,

**[02:16 – 02:20]** and especially as gradients go through the layers, right,

**[02:20 – 02:26]** you start losing signal when some of the layers get saturated.

**[02:26 – 02:31]** So, when a layer doesn't want to train anymore, its derivatives become zero,

**[02:31 – 02:36]** you multiply by that zero and nothing below it trains.

**[02:36 – 02:43]** Well, guess what? A recurrent neural network is in a way a very, very deep network, right?

**[02:43 – 02:50]** So, it has, usually you think of its input as a single thing, right?

**[02:50 – 02:57]** But what's actually going on is when you process the input,

**[02:57 – 03:04]** the activations go through as many layers, actually real physical layers,

**[03:04 – 03:07]** neural layers, right, with trainable weights and everything,

**[03:07 – 03:12]** as many layers as elements in your sequence.

**[03:12 – 03:19]** So, any recurrent network is, by default, a very deep network.

**[03:19 – 03:25]** And when people talk about deep recurrent networks,

**[03:25 – 03:32]** what they usually mean is like several layers of processing for the recurrences.

**[03:32 – 03:35]** So, there are constructions like this, like this.

**[03:35 – 03:39]** This would be called the three-layered recurrent network, right?

**[03:39 – 03:44]** But in actuality, if you compare it with,

**[03:44 – 03:50]** or if you look at it on the level of the computational graph,

**[03:50 – 03:55]** any recurrent network, even one with only one level of cells,

**[03:55 – 03:58]** is actually a very deep network.

**[03:58 – 04:00]** It's as deep as the input sequence,

**[04:00 – 04:03]** which is probably very deep, right?

**[04:03 – 04:07]** So, the problem is exactly the same.

**[04:07 – 04:09]** As you go back with the gradients,

**[04:09 – 04:11]** or as you go forward with activations,

**[04:11 – 04:13]** strange stuff begins to happen,

**[04:13 – 04:20]** because you keep multiplying by this same matrix of weights, more or less.

**[04:20 – 04:23]** And, of course, in recurrent networks it's a little bit different,

**[04:23 – 04:27]** because now you have the same weight matrix for every cell, right?

**[04:27 – 04:30]** So, they all share the same W,

**[04:30 – 04:34]** and this gives us even more problems.

**[04:34 – 04:38]** But the vanishing gradients problem is more or less the same.

**[04:38 – 04:45]** So, if your W has a spectral radius under 1,

**[04:45 – 04:49]** then as you go from left to right with the gradients,

**[04:49 – 04:53]** you keep multiplying by smaller and smaller.

**[04:53 – 04:57]** You keep multiplying by this number which is less than 1,

**[04:57 – 05:01]** more or less, and your vectors, your gradients shrink,

**[05:01 – 05:03]** and basically they shrink to 0.

**[05:03 – 05:07]** And that's a bad thing.

**[05:07 – 05:12]** But the additional problem here is that

**[05:12 – 05:17]** you can notice it if you look inside your network,

**[05:17 – 05:20]** but from the behavior, from the graph of the loss function,

**[05:20 – 05:25]** you will never notice it because it's not like exploding gradients.

**[05:25 – 05:32]** When gradients explode, it means that just everything is a huge mess.

**[05:32 – 05:33]** Nothing works, right?

**[05:33 – 05:43]** When gradients explode, you start seeing things like numerical overflows in your code,

**[05:43 – 05:46]** and it's completely obvious that everything has broken down.

**[05:46 – 05:50]** Not so with vanishing gradients, right?

**[05:50 – 05:57]** So when vanishing gradients become smaller when you go from right to left,

**[05:57 – 06:03]** it doesn't mean that W stops training, W still trains.

**[06:03 – 06:04]** Why?

**[06:04 – 06:10]** Because it still participates in the last cells of the network, right?

**[06:10 – 06:23]** So even if your gradients become basically exactly zero after the second step on their way back from the loss function,

**[06:23 – 06:26]** even if that happens, W will still train.

**[06:26 – 06:32]** It will still look fine at first glance because it will still participate in here.

**[06:32 – 06:34]** It will still give you some signal.

**[06:34 – 06:39]** The gradients with respect to the weights will not be zero.

**[06:39 – 06:43]** You will not notice it by looking at the gradients with respect to W.

**[06:43 – 06:52]** Everything will be fine, but your network will make its decisions based only on the last two elements of the sequence.

**[06:52 – 06:56]** It will not be able to have long-term memory for the rest of the sequence.

**[06:56 – 07:05]** So the actual problem with vanishing gradients is like this guy's problem from this classic Nolan movie.

**[07:05 – 07:08]** The networks cannot have long-term memory.

**[07:08 – 07:24]** They cannot have this x1 influence the output at step t.

**[07:24 – 07:25]** So what do we do?

**[07:25 – 07:30]** Well, we do exactly the same thing that we already learned how to do with resnets.

**[07:30 – 07:36]** We add something like residual connections.

**[07:36 – 07:41]** And in fact, it was recurrent networks that pioneered this idea

**[07:41 – 07:45]** because recurrent networks simply don't work at all without this idea.

**[07:45 – 07:56]** And so it actually originated in the 1990s in Juergen Schmidhuber's group.

**[07:56 – 08:03]** And these constructions have been known for a long time,

**[08:03 – 08:07]** but only in like 2015 they were actually applied to deep neural networks

**[08:07 – 08:13]** because we didn't have so deep neural networks before.

**[08:13 – 08:15]** And the idea is the same.

**[08:15 – 08:26]** You need to have like this way for gradients to flow around multiplying them by weight matrices.

**[08:26 – 08:30]** So you need to have some, Schmidt-Kober sometimes called it highways,

**[08:30 – 08:34]** you need to have a highway for the gradient to go through.

**[08:34 – 08:41]** And yes, of course you will change what's happening on the highway,

**[08:41 – 08:46]** but not by multiplying directly by a weight matrix that could go to zero.

**[08:46 – 08:58]** And I will explain to you this very famous and still very important construction, LSTM,

**[08:58 – 09:08]** which stands for long short-term memory, kind of a strange name, but there we go.

**[09:08 – 09:18]** And the basic idea of LSTMs is that, yes, you do have this highway for memory to flow.

**[09:18 – 09:24]** So I will be drawing here one cell of the LSTM.

**[09:24 – 09:37]** So we are in here, and our inputs are the hidden state and the current x, and our output should be the next hidden state.

**[09:37 – 09:44]** So in LSTMs, the hidden state is artificially split in two.

**[09:44 – 09:51]** So, of course, formally it's just a single vector, but we treat two halves of this vector very differently.

**[09:51 – 09:55]** So I will draw them as two different vectors.

**[09:55 – 10:03]** One half is like this long-term memory.

**[10:03 – 10:09]** This is the part that will stay on the highway.

**[10:09 – 10:11]** This is the highway, actually.

**[10:11 – 10:15]** So it will stay not unchanged.

**[10:15 – 10:18]** We will write to memory, read from memory, etc.

**[10:18 – 10:28]** But this is the part that we don't want to multiply by weight matrices.

**[10:28 – 10:37]** This is, in terms that we already know, this is the equivalent of this path around the layers.

**[10:37 – 10:44]** And then there will be also, let's call it h.

**[10:44 – 10:47]** ht is just a regular "hidden state".

**[10:47 – 10:51]** It will participate in everything that happens in the LSTM.

**[10:51 – 10:54]** And you will see how it gets used.

**[10:54 – 11:01]** And actually as the output we will need to produce this vector for the next step.

**[11:01 – 11:05]** So C is kind of this long-term memory.

**[11:05 – 11:07]** And this is the correct intuition.

**[11:07 – 11:13]** This is like a memory cell where you write stuff, where you read stuff from.

**[11:13 – 11:20]** And the whole LSTM is devoted to operations with this long-term memory.

**[11:20 – 11:23]** And then of course we have x.

**[11:23 – 11:26]** So we have like x, t over here.

**[11:26 – 11:28]** This will also be an input for us.

**[11:28 – 11:31]** And what's happening inside?

**[11:31 – 11:35]** Well, LSTM consists of gates.

**[11:35 – 11:41]** This is also a pretty important concept because in many modern architectures

**[11:41 – 11:44]** you will see some kind of gating mechanisms.

**[11:44 – 11:46]** You will see some kind of gates like this.

**[11:46 – 11:53]** Here I will draw gates like this.

**[11:53 – 11:56]** Let me show it separately.

**[11:56 – 12:02]** There will be a gate, for example, with two inputs.

**[12:02 – 12:04]** I will put matrices over here.

**[12:04 – 12:07]** These are two inputs, x and y.

**[12:07 – 12:12]** And then the gate itself will look like this.

**[12:12 – 12:16]** And there will be a function over here, the activation function.

**[12:16 – 12:26]** And so the output of this gate will be like f of a times x plus b times y.

**[12:26 – 12:34]** And probably plus a bias term, but I will not draw the bias terms explicitly.

**[12:34 – 12:40]** So this is basically this one linear cell, right?

**[12:40 – 12:44]** So two inputs, every input gets multiplied by a matrix.

**[12:44 – 12:46]** This will be weight matrices.

**[12:46 – 12:51]** Then we add them together and we push them through an activation function.

**[12:51 – 12:58]** But here they will be used in many different and creative ways, these kinds of gates.

**[12:58 – 13:03]** So let's begin. Let's see.

**[13:03 – 13:09]** Our first gate will be over here.

**[13:09 – 13:18]** I will call it the input gate.

**[13:18 – 13:30]** The input gate, right? Okay, let me draw it and then I will explain what's going on here.

**[13:30 – 13:33]** No, sorry. Let's start with the forget gate.

**[13:33 – 13:41]** This will be the forget gate. Just a cleaner picture this way.

**[13:41 – 13:49]** So it receives as input H with the weight matrix WHF, right?

**[13:49 – 13:51]** H for hidden, F for forget.

**[13:51 – 13:58]** It also receives as input X with the weight matrix WXF.

**[13:58 – 14:01]** Then you go here.

**[14:01 – 14:16]** And then what happens is I multiply CT by the output of this gate, like component-wise.

**[14:16 – 14:27]** So its output is a vector, let me call it FT, and I multiply CT by FT.

**[14:27 – 14:34]** So let's unpack what's happening here and then the rest of the gates will work in about the same way.

**[14:34 – 14:36]** So what is happening here?

**[14:36 – 14:43]** We have this kind of linear thing that just combines H and X with some coefficients, whatever.

**[14:43 – 14:48]** And importantly, we pass it through a logistic sigma.

**[14:48 – 14:53]** We pass it through the sigma function, this function that goes from 0 to 1.

**[14:53 – 14:58]** And that basically converts any score to a probability.

**[14:58 – 15:06]** So as a result, we have this vector full of values from 0 to 1.

**[15:06 – 15:12]** So it's like it goes from 0 to 1 and there are several values from 0 to 1.

**[15:12 – 15:17]** And actually 0 and 1 not included.

**[15:17 – 15:21]** And then we multiply it component-wise by our memory cell.

**[15:21 – 15:23]** So what's going on? What's the intuition?

**[15:23 – 15:29]** The intuition is we want to be able to erase something from memory.

**[15:29 – 15:34]** How do you erase something from memory?

**[15:34 – 15:36]** Well, you multiply it by 0.

**[15:36 – 15:41]** So basically the forget gate, if the output is close to 1,

**[15:41 – 15:45]** it means keep it, retain the cell in memory.

**[15:45 – 15:51]** If the output is close to 0, that means don't keep it, erase it.

**[15:51 – 15:57]** And that's mostly how gates work.

**[15:57 – 16:04]** So in modern architectures like mixtures of experts,

**[16:04 – 16:06]** I don't think we all will have time to discuss those,

**[16:06 – 16:11]** but very often you will see some kind of a gating mechanism.

**[16:11 – 16:17]** And usually it means that you have some small part of your network,

**[16:17 – 16:19]** in this case just this linear cell,

**[16:19 – 16:25]** producing a control vector that will control what's happening

**[16:25 – 16:28]** with other stuff inside the network.

**[16:28 – 16:31]** So this is not like data really.

**[16:31 – 16:35]** This is not something that I want to treat as numbers.

**[16:35 – 16:37]** And of course it's still numbers, right?

**[16:37 – 16:39]** It's all numbers inside the neural network.

**[16:39 – 16:44]** But the meaning of the vector f here at the output of this gate

**[16:44 – 16:47]** is which memory cells to erase.

**[16:47 – 16:50]** It's not some additional number that I want to multiply

**[16:50 – 16:54]** because I care about the multiplication result.

**[16:54 – 16:56]** That's the point of gating here.

**[16:56 – 16:59]** You cannot do real logic gates

**[16:59 – 17:02]** because then gradients would not fall through.

**[17:02 – 17:07]** Logic gates are piecewise constant and you cannot train through them.

**[17:07 – 17:13]** But you can do some kind of continuous approximation

**[17:13 – 17:15]** to these kinds of gates.

**[17:15 – 17:19]** And here it's basically about erasing from it.

**[17:19 – 17:25]** And now that we have one gate clear, the rest basically follows.

**[17:25 – 17:33]** So next you have, let's say you have the candidate cell state.

**[17:33 – 17:36]** Candidate cell state.

**[17:36 – 17:43]** Okay, probably we'll need more space and that will come later.

**[17:43 – 17:53]** Candidate cell state, which will produce the new numbers to write down to memory.

**[17:53 – 17:56]** So this is like C prime tip.

**[17:56 – 18:01]** This is something that we may want to write to memory.

**[18:01 – 18:05]** Where do we produce them from?

**[18:05 – 18:07]** Well, of course, from the same inputs.

**[18:07 – 18:12]** So we have W, H, C, another matrix of weights, right?

**[18:12 – 18:16]** And we have W, X, C, another matrix of weights.

**[18:16 – 18:23]** Notice that for controlling gates, for gates like the forget gate,

**[18:23 – 18:26]** it's important that I have the sigmoid function at the end.

**[18:26 – 18:30]** Because I do want numbers from zero to one, I actually want them to be saturated.

**[18:30 – 18:33]** I want them to be either close to zero or close to one.

**[18:33 – 18:34]** That's the whole point.

**[18:34 – 18:37]** Here, not so much, right?

**[18:37 – 18:40]** So here, I just want to produce new numbers to store in memory.

**[18:40 – 18:47]** So here, this sigma cannot be exchanged for something else.

**[18:47 – 18:51]** It's important that it's a sigmoid.

**[18:51 – 18:56]** But this hyperbolic tangent, I'm just copying it from classical LSTM construction,

**[18:56 – 18:59]** but this is not written, set in stone.

**[18:59 – 19:03]** This can be modified.

**[19:03 – 19:11]** And so now we have C' and the question is which part of this vector I want to write to memory.

**[19:11 – 19:15]** And guess what? There is a gate to control that.

**[19:15 – 19:20]** So we have another gate which is called the input gate.

**[19:20 – 19:23]** Here it is.

**[19:23 – 19:26]** And now this one is a control gate with a sigma.

**[19:26 – 19:43]** And what it does is it decides which of this candidate cell, which parts of C' I want to write into memory.

**[19:43 – 19:48]** So I multiply C' component-wise by the output of the input gate.

**[19:48 – 19:50]** And then the result I write into memory.

**[19:50 – 19:54]** What does it mean to write something into memory that's just addition.

**[19:54 – 19:58]** Okay? That's it.

**[19:58 – 20:05]** And of course I need to do it from inputs.

**[20:05 – 20:13]** W-H-I-W-X-I.

**[20:13 – 20:18]** I need one more gate.

**[20:18 – 20:27]** Right. So at this point we are able to erase something from memory.

**[20:27 – 20:30]** And we are able to write something back to memory.

**[20:30 – 20:35]** So again, this plus is not really a plus.

**[20:35 – 20:41]** I mean, the LSTM usually does not learn to actually add stuff.

**[20:41 – 20:44]** It's not about this addition.

**[20:44 – 20:47]** It's about writing to memory.

**[20:47 – 20:51]** So the main mechanism is sometimes I want to erase something from memory.

**[20:51 – 20:54]** So I multiply by something very close to zero.

**[20:54 – 20:57]** I get a zero in that position of CT.

**[20:57 – 21:01]** And now when I add something there, it means I'm just writing to this cell.

**[21:01 – 21:07]** And the only remaining thing is to define this H for the next step.

**[21:07 – 21:13]** And here I will actually look it up because the rest is very logical.

**[21:13 – 21:17]** And here with me, yeah, it's a hyperbolic tangent.

**[21:17 – 21:28]** So now H is actually produced from the long-term memory.

**[21:28 – 21:33]** So it's basically kind of a copy of long-term memory.

**[21:33 – 21:38]** But for some reason, which I cannot really explain, it goes through a hyperbolic tangent over here.

**[21:38 – 21:45]** And then it's a part, and then we read the result from, and then we read it from long-term memory.

**[21:45 – 21:47]** But what does it mean to read?

**[21:47 – 21:53]** Again, it means that there will be a gate controlling which part of CT I want to write to HT.

**[21:53 – 22:03]** So there will be another gate, let's call it the output gate, or output, yeah, I think output.

**[22:03 – 22:14]** The output gate, again with the sigmoid, and you have a vector here.

**[22:14 – 22:21]** And this vector will decide what to read from memory for the next H.

**[22:21 – 22:31]** And again, WHO and WXO.

**[22:31 – 22:34]** That's it, that's the LSTM.

**[22:34 – 22:41]** So the LSTM cell is everything that's inside here, right?

**[22:41 – 22:49]** So this is the LSTM cell.

**[22:49 – 22:56]** And it looks complicated.

**[22:56 – 22:59]** It's not really complicated.

**[22:59 – 23:04]** Meaningfully, I can explain to you the intuition behind everything here.

**[23:04 – 23:06]** Maybe except that hyperbolic tangent.

**[23:06 – 23:08]** I have no idea why it's exactly that.

**[23:08 – 23:16]** But I can explain to you how things flow inside an LSTM.

**[23:16 – 23:18]** And it makes sense, right?

**[23:18 – 23:21]** So the beauty of this construction is that it makes perfect sense.

**[23:21 – 23:27]** It's like a program for memory manipulation procedures, right?

**[23:27 – 23:33]** There is this memory, you can delete from it, you can write to it, that's it.

**[23:33 – 23:37]** And also you need to decide what to write to it.

**[23:37 – 23:39]** So hence the candidate cell state.

**[23:39 – 23:43]** That's how it works.

**[23:43 – 23:50]** And it actually is an extremely successful construction.

**[23:50 – 24:01]** It's still relevant now, even though it was constructed, I think 1995 was their first paper.

**[24:01 – 24:06]** And by the year 2000, they already had exactly this construction.

**[24:06 – 24:08]** The first construction was a bit simpler.

**[24:08 – 24:12]** But by the year 2000 in Schmidt-Fober's group, they already had exactly this.

**[24:12 – 24:17]** And ever since, it just works.

**[24:17 – 24:26]** And when you build a recurrent network today, you will actually use LSTMs, surprisingly enough.

**[24:26 – 24:30]** So I don't want to spend too much time on recurrent networks.

**[24:30 – 24:36]** So let me be quick about what's coming next here.

**[24:36 – 24:43]** And the LSTM is the most important recurrent construction ever.

**[24:43 – 24:49]** And again, its main meaning is that it provides you with this straight line,

**[24:49 – 24:55]** with this highway through which the gradients will flow without any interruptions,

**[24:55 – 24:59]** or better to say, only with interruptions that we intend.

**[24:59 – 25:03]** So of course, they will be interrupted if I erase something from memory.

**[25:03 – 25:09]** Of course, this will stop the gradients, but that's how I want it to.

**[25:09 – 25:19]** But the LSTM has a big cost, and the cost is it has a lot of weights.

**[25:19 – 25:26]** So if you look at all of these matrices, you will see that there are a lot of matrices.

**[25:26 – 25:34]** In the construction that I drew here, there are eight weight matrices,

**[25:34 – 25:43]** and they are basically, so if like x is r d prime, and I think I said that this is d,

**[25:43 – 25:52]** so h and c are of length d, then like half of these matrices are like d times d matrices,

**[25:52 – 25:58]** and half of these matrices are d times d prime matrices.

**[25:58 – 26:04]** And of course you want your memory to be large.

**[26:04 – 26:11]** You cannot have a meaningful LSTM with like a cell of size 2.

**[26:11 – 26:18]** So in reality, like in practice, d is something like at least 256,

**[26:18 – 26:23]** maybe in small cases something like 64, in large cases something like 1000.

**[26:23 – 26:28]** And d prime is what it is, that's your x, probably some embedding of x,

**[26:28 – 26:35]** some representation, but also probably on the same kind of size level.

**[26:35 – 26:42]** So these are big weight matrices and for a long time it was very difficult to train LSTMs.

**[26:42 – 26:51]** Everybody knew that they are cool and in toy examples they were actually delivering very good results,

**[26:51 – 26:55]** but nobody could really train a huge LSTM.

**[26:55 – 27:04]** And I think it only began to be possible in like 2015 or so.

**[27:04 – 27:14]** But ever since, big LSTMs are indeed what people use for big recurrent networks.

**[27:14 – 27:22]** And for example, I think, to take an example you may have heard about, I think AlphaStar.

**[27:22 – 27:29]** The StarCraft playing network.

**[27:29 – 27:35]** It was actually a recurrent network and AlphaStar used LSTMs.

**[27:35 – 27:41]** Which sounds pretty strange, right?

**[27:41 – 27:49]** Like, how does it happen that this basically first...

**[27:49 – 27:53]** Okay, very smart people did it. It makes a lot of sense.

**[27:53 – 28:01]** But this is like the first successful attempt to build an architecture for this kind of memory manipulation stuff.

**[28:01 – 28:08]** And it was 25 years ago and it still stands and nobody has done better.

**[28:08 – 28:12]** That sounds unbelievable, right?

**[28:12 – 28:18]** And indeed, of course, there have been lots of attempts to do something better.

**[28:18 – 28:25]** So let me not draw anything new here, anything on the board.

**[28:25 – 28:28]** I will just walk through the slides to save time.

**[28:28 – 28:33]** Okay, so this is the LSTM cell that I have been drawing just now.

**[28:33 – 28:37]** For gate gate, input gate, candidate cell state, output gate.

**[28:37 – 28:42]** These are the matrices, the formulas, whatever.

**[28:42 – 28:48]** Yeah, so completely in its modern form, it already appeared in 2000, in the year 2000.

**[28:48 – 28:53]** And there have been some modifications.

**[28:53 – 28:57]** There have been modifications like let's add the pip holes.

**[28:57 – 29:04]** So one problem of the LSTM is that once you have fixed your age,

**[29:04 – 29:07]** all of these gates do not have access to memory.

**[29:07 – 29:13]** So it's like you are erasing from memory, but you cannot look inside the memory

**[29:13 – 29:16]** to see what you are erasing, which is pretty strange.

**[29:16 – 29:24]** And people added more inputs from C over here, which means even more weight matrices.

**[29:24 – 29:32]** And at some point, people tried to maybe lose a few of these matrices.

**[29:32 – 29:39]** Maybe you can do without some of the gates.

**[29:39 – 29:43]** Maybe you can tweak the LSTM a little bit.

**[29:43 – 29:52]** And it turned out that, yes, for every, like this, there was this famous paper called LSTM is Rich Space Odyssey.

**[29:52 – 30:07]** And basically it said, yeah, on our two examples where we could test a lot of LSTM variations, you can actually remove a whole gate and nothing much changes.

**[30:07 – 30:13]** And then there were even better attempts.

**[30:13 – 30:41]** So let us try to achieve the same goal, the goal of having memory that goes through this free highway of gradient flow.

**[30:41 – 30:51]** And let's keep it that way, but let's tweak the structure of the recurrent cell so that it will be more efficient.

**[30:51 – 30:53]** And people have been successful.

**[30:53 – 30:59]** So, for example, like the second very famous recurrent unit is called the GRU, Gated Recurrent Unit.

**[30:59 – 31:02]** Back in 2014, it was developed.

**[31:02 – 31:09]** And if you look at it, it's very similar to the LSTM, but it has much less, much fewer matrices.

**[31:09 – 31:16]** So let me just walk you through here without drawing it separately.

**[31:16 – 31:23]** So it still has, of course, the candidate cell state, but now it doesn't distinguish between C and H.

**[31:23 – 31:27]** So you only have one hidden state.

**[31:27 – 31:39]** And instead of updating it separately with erasing stuff and writing stuff, you do it all at once with the update gate.

**[31:39 – 31:49]** So basically the update gate, again, it's a control gate with a sigma at the output and it gives you numbers between zero and one.

**[31:49 – 31:53]** But now they are like coefficients of a convex combination.

**[31:53 – 32:01]** So if you look here on the right, you multiply H, the current memory state, by U.

**[32:01 – 32:13]** And then you add this H prime, the candidate that you proposed, times one minus U, right?

**[32:13 – 32:18]** So it sounds like it makes a lot of sense, right?

**[32:18 – 32:22]** Why do we want to erase from memory, to write something there?

**[32:22 – 32:24]** Why do we want to add something to memory?

**[32:24 – 32:26]** Because we've already erased this cell.

**[32:26 – 32:33]** And as I said, LSTM is not about actual addition, it's about erasing and writing back to memory.

**[32:33 – 32:36]** So it makes a lot of sense to combine it into one gate.

**[32:36 – 32:39]** And that saves like two weight matrices, right?

**[32:39 – 32:50]** And instead of the output gate, we have the reset gate, which does basically the same thing, only in the same cell and not in the cell as that before.

**[32:50 – 32:57]** It just looks at the memory and chooses which part of it should go into the candidate cell state.

**[32:57 – 33:11]** So GRUs look great, looks like they do exactly the same as LSTMs, only more efficiently because now you have only 6 weight matrices instead of 8 or instead of 11.

**[33:11 – 33:15]** If you count pip holes, you don't need pip holes now.

**[33:15 – 33:22]** So it's more efficient, should be better, and so on and so forth.

**[33:22 – 33:31]** Indeed, in like 2015, 2016, if you look in, for example, papers on natural language processing, I was actually working in the field at that point,

**[33:31 – 33:39]** and if you look at the papers on NLP back in 2015, they all used GRUs.

**[33:39 – 33:44]** They all switched to GRUs, and that was a big thing, etc., etc.

**[33:44 – 33:52]** And then, for some reason, which I cannot explain to you theoretically, the whole field switched back to LSTMs.

**[33:52 – 34:00]** So, I mentioned AlphaStar, AlphaStar, I don't remember the year, but of course, it's much later, it's like 2020 or something.

**[34:00 – 34:08]** And if you have a recurrent network now, probably it's more likely to be an LSTM than a GRU.

**[34:08 – 34:17]** Somehow, Schmidt-Huber's construction is better, and I'm sure the actual decision-making here is just empirical.

**[34:17 – 34:23]** You're just saying, "Oh, okay, we've tried LSTMs, we've tried GRUs, so LSTMs work better,

**[34:23 – 34:27]** we can bear the costs, so to speak, let's use LSTMs."

**[34:27 – 34:32]** But why they are better, I have no idea.

**[34:32 – 34:41]** What's so special about the LSTM architecture, I don't know, but it's really interesting and it's really beautiful that it stands for so long.

**[34:41 – 34:50]** And remember, all through the class, from time to time, I was mentioning stuff like,

**[34:50 – 34:59]** "Oh, and then Google came and they had lots of compute, and they ran this big neural architecture search,

**[34:59 – 35:03]** and now we have EfficientNet, which is better.

**[35:03 – 35:10]** Or now we have Swish, which is a great activation function, and then people did something else, but at the point it was the best."

**[35:10 – 35:15]** And so, well, of course, they tried it with recurrent cells.

**[35:15 – 35:22]** Of course, there is a paper from Google where they develop exactly this kind of thing.

**[35:22 – 35:26]** They try to make recurrent cells more efficient.

**[35:26 – 35:39]** And yes, on the examples on the datasets where they test their recurrent cells are better than LSTMs and GRUs.

**[35:39 – 35:42]** And here is an example of their cell.

**[35:42 – 35:48]** Of course, we won't go through it, but as you can see, it has only four weight matrices.

**[35:48 – 35:52]** It's kind of similar to GRU, but it's even better.

**[35:52 – 35:54]** It's even more efficient.

**[35:54 – 35:59]** And nobody has ever heard about these cells.

**[35:59 – 36:06]** So most probably they don't work as advertised or, I mean, they don't, I'm not saying Google is lying.

**[36:06 – 36:14]** I'm saying they probably work on those examples where they were developed, but they don't generalize to other situations.

**[36:14 – 36:21]** And for some reason LSTM is still the best. It still stands.

**[36:21 – 36:33]** Okay. So with this, I think I want to end our discussions of recurrent networks specifically.

**[36:33 – 36:42]** If there are any questions, now is a good time and I will show you an example here.

**[36:42 – 36:54]** Yeah. So I have some code for today, not very deep, not very difficult, but I hope more interesting codes will be in the practice session.

**[36:54 – 37:02]** So this is just an illustration of exploding and vanishing gradients.

**[37:02 – 37:12]** It's not even a real recurrent network. It just shows you that if you keep multiplying by a number less than one, you vanish.

**[37:12 – 37:17]** And if you keep multiplying by a number greater than one, you explode.

**[37:17 – 37:19]** And here is a real experiment.

**[37:19 – 37:28]** So this is the classic LSTM benchmark from very long ago, from Hohreiter and Schmidhuber.

**[37:28 – 37:35]** And it goes like this. You have an input with two components.

**[37:35 – 37:42]** So there are two input channels. One is just a set of numbers.

**[37:42 – 37:45]** It just goes to random numbers from 0 to 1.

**[37:45 – 37:52]** And another is a channel of zeros with exactly two ones.

**[37:52 – 37:55]** So like here is a sample input.

**[37:55 – 38:02]** The markers show, the bars show these random values that go between 0 and 1.

**[38:02 – 38:07]** And the stars mark the ones in the marker channel.

**[38:07 – 38:13]** So it's like a vector, a long stream of numbers, and two of them are highlighted.

**[38:13 – 38:20]** And the question is add the two highlighted numbers, give me the sum of two highlighted numbers.

**[38:20 – 38:27]** So it's like a perfect toy test problem for memory, right?

**[38:27 – 38:37]** You need to, when the marker channel tells you to, you need to memorize this value.

**[38:37 – 38:42]** And then when it tells to you again, you need to add this value to the one you memorized.

**[38:42 – 38:49]** And sure enough, LSTMs and GRUs, they both work well on this.

**[38:49 – 38:57]** And this is actually, since it is so simple, this is actually a good example for GRUs, not LSTMs.

**[38:57 – 39:03]** So here you will see that like a simple linear RNN doesn't work.

**[39:03 – 39:10]** It just like, it stays on the baseline, which means no training at all.

**[39:10 – 39:27]** LSTMs at some point get what they are asked to do and they start learning, but in like 600 steps, 600 iterations, they didn't yet train.

**[39:27 – 39:32]** And GRUs have trained much faster and from a much earlier point.

**[39:32 – 39:41]** So this is the kind of plot that you would see convincing people that GRUs are better, but this is a very easy problem, right?

**[39:41 – 39:45]** So that's the point for a very easy problem.

**[39:45 – 39:54]** Of course, a more efficient cell will be better, but probably it doesn't scale to really difficult problems.

**[39:54 – 40:02]** And here is another sample from the LSTM.

**[40:02 – 40:11]** It's the same problem, it's just I take one of the inputs, here is the input, and then I look at what is actually the contents of memory.

**[40:11 – 40:24]** What are the outputs of the gates and what is the current prediction of the sum that you, what is your running guess?

**[40:24 – 40:29]** What would be the output if your sequence stopped right now?

**[40:29 – 40:34]** And as you can see, a trained LSTM does some very reasonable stuff.

**[40:34 – 40:43]** When it sees a star, when it sees a marker, the thing that it writes to the cell actually spikes.

**[40:43 – 40:48]** So you write a lot of stuff here and you don't write much over here.

**[40:48 – 40:54]** And your cell just grows to the correct value. That's it.

**[40:54 – 41:03]** So if you take your running guess, then it indeed tracks the true sum and it goes to the true sum after the second sum.

**[41:03 – 41:07]** So it works. It's a very simple problem.

**[41:07 – 41:18]** But interestingly, the interesting part here is straightforward recurrent networks cannot do that.

**[41:18 – 41:29]** If you have just this linear cell, you simply cannot have this long-term memory that goes back and recalls it.

**[41:29 – 41:34]** "Oh yeah, I had that number 15 steps ago. Now I need to add it to the present number."

**[41:34 – 41:40]** And that's the idea behind all of these recurrent cells.

**[41:40 – 41:48]** Okay, so any questions about this? No questions.

**[41:48 – 41:54]** All right, well, with that we go to our next topic.

**[41:54 – 42:01]** And our next topic is probably the last time in class

**[42:01 – 42:06]** when I again start from a neurobiological motivation,

**[42:06 – 42:09]** when I again tell you about the brain and everything.

**[42:09 – 42:11]** But now we're in a very superficial way.

**[42:11 – 42:16]** Now we don't go from a bird's eye view,

**[42:16 – 42:19]** we don't go to the details of how neurons operate.

**[42:19 – 42:25]** We actually just stay on the level of how we think in general.

**[42:25 – 42:32]** And we are interested in the notion of attention.

**[42:32 – 42:34]** And if you think about attention,

**[42:34 – 42:37]** I hope that you are paying attention to me right now,

**[42:37 – 42:39]** even though I'm really not sure.

**[42:39 – 42:45]** But if you think about how attention works,

**[42:45 – 42:48]** and especially how lack of attention works,

**[42:48 – 42:51]** it's a really funny thing,

**[42:51 – 42:54]** it's really unclear how it's supposed to work.

**[42:54 – 42:59]** Our brain seems to work very differently

**[42:59 – 43:04]** in this regard from how networks that we have seen so far,

**[43:04 – 43:07]** artificial neural networks work.

**[43:07 – 43:12]** We are in the computer vision class,

**[43:12 – 43:16]** so think of an image.

**[43:16 – 43:21]** Think of looking at an image

**[43:21 – 43:24]** and registering some stuff,

**[43:24 – 43:27]** some objects that are on this image, etc.

**[43:27 – 43:35]** I told you that our visual cortex,

**[43:35 – 43:38]** the part of the brain that processes images,

**[43:38 – 43:41]** is kind of similar to convolutional networks,

**[43:41 – 43:42]** at least in spirit.

**[43:42 – 43:44]** They cannot really be similar in architecture,

**[43:44 – 43:47]** but in spirit it's like extracting local features,

**[43:47 – 43:51]** then combining them to better,

**[43:51 – 43:53]** to more global features,

**[43:53 – 43:56]** to semantically richer features, etc.

**[43:56 – 44:03]** But if I look at an image,

**[44:03 – 44:06]** like right now I am looking at my computer, obviously,

**[44:06 – 44:09]** but my field of vision is, of course,

**[44:09 – 44:12]** much wider than just the computer.

**[44:12 – 44:18]** So if something happens outside of the computer

**[44:18 – 44:21]** and right now I'm thinking about our lecture

**[44:21 – 44:23]** and I'm writing something on the board,

**[44:23 – 44:25]** most probably I'll miss it, right?

**[44:25 – 44:27]** Because I'm not paying attention to that.

**[44:27 – 44:29]** I'm paying attention to the board.

**[44:29 – 44:36]** But the stuff that's outside is still in my field of vision.

**[44:36 – 44:40]** So if you try to map this kind of attention thing

**[44:40 – 44:46]** to how neural networks work, it's really strange.

**[44:46 – 44:54]** So when you go with a convolution over an image of any size,

**[44:54 – 44:59]** you get features extracted from every part of the image, right?

**[44:59 – 45:05]** And then these features on the next layers,

**[45:05 – 45:07]** they get combined into more global features.

**[45:07 – 45:10]** I showed you some pictures yesterday, et cetera, et cetera.

**[45:10 – 45:14]** And there is no place to lose stuff there, right?

**[45:14 – 45:18]** If I have a huge image, okay, I will need to spend more compute,

**[45:18 – 45:22]** but it's not like I'm going to lose some object from there.

**[45:22 – 45:25]** I will still extract features from every part of the image,

**[45:25 – 45:28]** and they will still be combined into more global stuff.

**[45:28 – 45:33]** They will still have this, I don't know, tabic cat neuron up there,

**[45:33 – 45:35]** that will still activate on the cats.

**[45:35 – 45:38]** It's not like a convolutional network can just miss the cat.

**[45:38 – 45:43]** Completely impossible. But we do. What's the difference?

**[45:43 – 45:47]** The difference is an attention mechanism.

**[45:47 – 45:51]** And how it works is actually a pretty difficult question.

**[45:51 – 45:57]** There was this guy, Alexander Luria, he was a very interesting man,

**[45:57 – 46:05]** he had a very interesting career because it was 1930s-1940s,

**[46:05 – 46:10]** he lived in Italianist Russia, but still he was like a man of the world.

**[46:10 – 46:15]** He traveled to all the conferences, he published in all international journals

**[46:15 – 46:23]** and he was like one of the internationally recognized fathers of the field of neurobiology.

**[46:23 – 46:32]** And Alexander Luria, when he posed the main research program of neurobiology in general,

**[46:32 – 46:51]** he said that there are three main pillars, three main components to the field of neurobiology.

**[46:51 – 46:57]** And he said it's attention, memory and cognitive functions, which is basically like how we think.

**[46:57 – 47:07]** So to him and to the whole field of neurobiology, attention is up there on the level of memory and cognition.

**[47:07 – 47:14]** Well, of course, since Luria there has been a lot of progress, we kind of understand how attention works in the brain.

**[47:14 – 47:22]** But it's not really important for us from the computer science point of view, because in the brain attention works through memory.

**[47:22 – 47:33]** More or less, it works through memory. There are different types of memory in the brain.

**[47:33 – 47:41]** So there is this kind of working memory, which is a very short-term memory that stores just a few latest objects.

**[47:41 – 47:49]** Like if we were offline in class, I would be able to demonstrate.

**[47:49 – 47:59]** So if you give a lecture and if you ask any person, a person who is not paying attention to you at all,

**[47:59 – 48:04]** like this person is on their phone chatting with somebody, etc.

**[48:04 – 48:08]** But if you suddenly ask this person, "Tell me what I just said,"

**[48:08 – 48:14]** even if they were not paying attention at all, they would be able to recite the last five words or so.

**[48:14 – 48:19]** They would say, "Oh, yeah, you were just saying blah, blah, blah," and it would be right.

**[48:19 – 48:24]** But if you ask what I was saying 30 seconds ago, it would be blank.

**[48:24 – 48:30]** So working memory is this very short-term mechanism of what's happening just now,

**[48:30 – 48:42]** and mostly everything goes there, but then there is this filter,

**[48:42 – 48:54]** which parts of this recent stuff are actually important to process further,

**[48:54 – 48:58]** and that's where stuff gets lost.

**[48:58 – 49:05]** And I won't spend more time on attention, neurobiology, etc.

**[49:05 – 49:11]** It's an interesting topic, but I think for us it's more important to go further.

**[49:11 – 49:15]** If you've never seen, so I will just recommend you one thing,

**[49:15 – 49:23]** if you've never seen this video where there are two teams of players passing basketballs,

**[49:23 – 49:26]** the team in white and the team in black,

**[49:26 – 49:30]** and you're supposed to count the passes of the team in white.

**[49:30 – 49:35]** If you haven't seen that video, please see it when I publish the slides.

**[49:35 – 49:39]** I can copy it here.

**[49:39 – 49:41]** Look at it and pass the test.

**[49:41 – 49:43]** It's interesting if people still fall for it,

**[49:43 – 49:47]** because back in the 1990s people definitely fell for it.

**[49:47 – 49:50]** Now I'm not so sure.

**[49:50 – 49:54]** Our attention mechanisms have changed a little bit.

**[49:54 – 50:08]** Anyway, so neurobiological words on attention actually show that

**[50:08 – 50:11]** even if you are looking directly at some stuff,

**[50:11 – 50:15]** this video shows that if you are actually even looking directly at some stuff,

**[50:15 – 50:28]** you still don't have to process it.

**[50:28 – 50:30]** It still may be lost.

**[50:30 – 50:34]** You still may like very early in the brain, you can decide to drop it.

**[50:34 – 50:39]** But also there is another thing which you probably have heard about

**[50:39 – 50:43]** and it's about our vision in general.

**[50:43 – 50:49]** And our vision also kind of doesn't process the whole field of view.

**[50:49 – 50:51]** You probably know that.

**[50:51 – 50:59]** You have this, for VL Spotlight, we have this small part of our field of vision

**[50:59 – 51:05]** where we can see stuff very, very clearly in high definition

**[51:05 – 51:09]** and then it gets blurry and blurrier, right?

**[51:09 – 51:14]** And we don't notice it because our gaze constantly wanders around.

**[51:14 – 51:18]** Even if you're looking at your computer, still you're constantly like,

**[51:18 – 51:23]** it's called saccadic motion, your gaze constantly shifts

**[51:23 – 51:26]** and you look, you get different snippets of the whole picture

**[51:26 – 51:31]** and then your brain just kind of constructs the whole picture

**[51:31 – 51:36]** from these relatively blurry components.

**[51:36 – 51:40]** It's like several photographs of the same scene,

**[51:40 – 51:44]** but the focus is on different parts.

**[51:44 – 51:50]** And the original motivation to add attention mechanisms to deep learning

**[51:50 – 51:56]** was to actually emulate this, to emulate how we see things,

**[51:56 – 51:59]** to emulate this blurriness in the peripheral vision.

**[51:59 – 52:02]** And that, of course, sounds very strange.

**[52:02 – 52:04]** Why on earth would you do that?

**[52:04 – 52:08]** Why would you make things blurry if you don't have to?

**[52:08 – 52:10]** In computer vision, in a convolutional network,

**[52:10 – 52:12]** you can just put in the whole picture.

**[52:12 – 52:14]** You don't need to blur anything.

**[52:14 – 52:17]** Why would you want to do that?

**[52:17 – 52:22]** In our eyes, I mean, of course, they have evolved to do stuff

**[52:22 – 52:26]** and maybe they didn't have the energy, the capabilities to do that.

**[52:26 – 52:29]** But why do we need to do this in computers?

**[52:29 – 52:32]** And the answer originally was to save weights,

**[52:32 – 52:36]** to save input size, to make it more efficient.

**[52:36 – 52:42]** So if you have a big image and if you can actually,

**[52:42 – 52:45]** instead of looking at the big image,

**[52:45 – 52:50]** you can actually do like three snippets of the big image

**[52:50 – 52:58]** where you only actually use the pixels from a few small parts of this image,

**[52:58 – 53:01]** and then the rest can be blurrier.

**[53:01 – 53:05]** What it means to be blurrier, it means there are fewer pixels, right?

**[53:05 – 53:10]** So the input size becomes smaller, and much smaller actually.

**[53:10 – 53:16]** And if you have like three glimpses and everyone is just looking at a small part of the input,

**[53:16 – 53:19]** then of course even the total input size will be much smaller.

**[53:19 – 53:28]** So originally people wanted to save processing by doing attention mechanisms.

**[53:28 – 53:38]** And the new thing here is that now in addition to just recognizing stuff,

**[53:38 – 53:44]** in addition to doing your classification problem or whatever from these blurred images,

**[53:44 – 53:46]** you also need to choose where you look.

**[53:46 – 53:50]** So you need to choose the positions of the glimpses.

**[53:50 – 54:01]** And these positions, they form a sequence.

**[54:01 – 54:09]** So this becomes a sequence problem because the next glimps, of course,

**[54:09 – 54:12]** can depend on what you see in the previous glimps.

**[54:12 – 54:17]** So your first position can be chosen somehow generally,

**[54:17 – 54:21]** but then your second position will depend on what you've seen in the first one.

**[54:21 – 54:26]** So early models of attention were recurrent.

**[54:26 – 54:28]** There is this field of recurrent visual attention.

**[54:28 – 54:34]** I won't go into details because that's not too relevant now.

**[54:34 – 54:37]** Now it's all very different.

**[54:37 – 54:43]** But more or less the point was, let's look at this picture,

**[54:43 – 54:47]** more or less the point was given a relatively big picture,

**[54:47 – 54:52]** let's walk around it and choose where to look and blur the rest.

**[54:52 – 54:58]** And then you can actually be more accurate while being more efficient.

**[54:58 – 55:03]** And there is a recurrent mechanism in choosing these subsequent glimpses.

**[55:03 – 55:07]** But yeah, this is outdated, you don't have to learn that.

**[55:07 – 55:17]** What is more relevant and more interesting is what happened with attention

**[55:17 – 55:27]** at the point where attention got applied to encoder-decoder mechanisms.

**[55:27 – 55:36]** So let me go back to the board because now I do want to explain stuff.

**[55:36 – 55:44]** And let me first explain to you what the problem is.

**[55:44 – 56:00]** So let first LSTM and now our second part for today is encoder-decoder with attention.

**[56:00 – 56:10]** So what is the problem that we are solving?

**[56:10 – 56:16]** Well, let me motivate this with machine translation.

**[56:16 – 56:25]** I mentioned machine translation before and it sounds like a perfect problem for recurrent encoder-decoder architectures.

**[56:25 – 56:36]** So you have your input, which is like, I don't know, hello world, exclamation mark.

**[56:36 – 56:48]** You read your input, this gives you some kind of hidden state.

**[56:48 – 56:58]** And then the last hidden state, or maybe the last hidden state pushed through some kind of output head, whatever,

**[56:58 – 57:12]** gives you this vector, let's call it z, this intermediate representation of the input sequence of the sentence.

**[57:12 – 57:21]** And then you take this z and you decode it into the output.

**[57:21 – 57:23]** I only know English and Russian, so let me write that.

**[57:23 – 57:38]** Privyet, comma, mir, exclamation mark, something like this, right?

**[57:38 – 57:44]** And probably you want to, so yeah, it probably doesn't look like this.

**[57:44 – 57:51]** Probably you have a hidden state over here, h prime, and z is just the input to every,

**[57:51 – 57:59]** to every cell. So probably the data current decoder looks like this.

**[57:59 – 58:06]** And when people did this, when people had the compute to train vehicle STMs,

**[58:06 – 58:16]** and they actually tried to apply LSTMs and GRUs with this kind of architectures

**[58:16 – 58:27]** to, say, machine translation, they realized that they have an unsolvable problem,

**[58:27 – 58:30]** at least a problem unsolvable in this kind of architecture.

**[58:30 – 58:39]** So, yes, this works. This defined state-of-the-art in 2014 or whatever.

**[58:39 – 58:50]** And this actually gives you good results with short sentences.

**[58:50 – 58:54]** With sentences like "hello world", it will work great.

**[58:54 – 59:02]** But you cannot scale it up. So here is the thing.

**[59:02 – 59:13]** The problem of encoder-decoder architectures like this is in the dimension of this intermediate representation Z.

**[59:13 – 59:21]** And the problem is you cannot have a good dimension that will be either too small or too big.

**[59:21 – 59:29]** If you have a Z which is too short, D is too small, then everything will train, everything will be perfect.

**[59:29 – 59:39]** It will run fine but it will not be able to fit a lot of meaning, a lot of information into a small Z of course.

**[59:39 – 59:46]** So for hello world it will work but of course I'm not talking about putting war and peace inside a single vector.

**[59:46 – 59:51]** But even for long sentences it will start to break down.

**[59:51 – 59:59]** And if you try to fix that by making Z longer, by extending Z further and further and further,

**[59:59 – 1:00:03]** then it becomes harder and harder to train.

**[1:00:03 – 1:00:16]** So if you have a huge or very long Z, it means that your hidden state in the LSTMs or your input to the decoder LSTMs will become longer and longer.

**[1:00:16 – 1:00:26]** And that means you have quadratically more weights and now you don't have enough data and enough compute to actually train them.

**[1:00:26 – 1:00:36]** So this is like a problem that you can't really solve inside this architecture.

**[1:00:36 – 1:00:57]** You can either have a good encoder-decoder LSTMs with small Zs but it won't scale up or you can have large Zs but then the training will be impossible.

**[1:00:57 – 1:01:11]** So in architectures like this, if you look at the graph of like, I don't know, whatever quality, I'm abstract here, but some kind of quality metric.

**[1:01:11 – 1:01:19]** And this is like T, the sequence length, the input-out-output sequence length.

**[1:01:19 – 1:01:29]** What you actually see is like it's very good while we have short sentences and then it just drops and it's very bad.

**[1:01:29 – 1:01:40]** So of course as sentences get longer the quality will drop, but of course you would want your graph to look like this.

**[1:01:40 – 1:01:49]** You would want it to drop gracefully and still work for longer sequences too.

**[1:01:49 – 1:01:58]** So this is what attention mechanisms for encoder-decoder recurrent networks were supposed to fix.

**[1:01:58 – 1:02:03]** And this is an important concept that I think is still relevant.

**[1:02:03 – 1:02:11]** So what is the problem with Z? Where do we get this idea for this attention mechanism from?

**[1:02:11 – 1:02:20]** The problem with Z is that it's only one vector for the whole input, for the whole sequence.

**[1:02:20 – 1:02:23]** And this is what we need to change.

**[1:02:23 – 1:02:29]** And in transformers also there will not be a single vector for the whole input.

**[1:02:29 – 1:02:37]** Because we kind of understand that sometimes we translate specific words.

**[1:02:37 – 1:02:43]** And when I'm writing out mir over here, I'm translating the word world.

**[1:02:43 – 1:02:50]** And world should be more important as the input over here than anything else.

**[1:02:50 – 1:02:54]** And here there is no way to express that.

**[1:02:54 – 1:02:57]** I just need to cram everything into this single vector.

**[1:02:57 – 1:03:07]** So the first step is to get rid of this assumption that everything needs to be in a single vector.

**[1:03:07 – 1:03:14]** So in this encoder-decoder with attention, the first thing that I do is...

**[1:03:14 – 1:03:26]** Okay, let me say "Hello world!" and it's still a recurrent network at the input.

**[1:03:26 – 1:03:31]** Let's say it's bidirectional, because of course it's bidirectional.

**[1:03:31 – 1:03:34]** It doesn't make sense not to read the whole sentence.

**[1:03:34 – 1:03:44]** But it produces outputs for every x in the input.

**[1:03:44 – 1:03:56]** So there is a vector, let's say z1, there is a vector z2, and there is a vector z3.

**[1:03:56 – 1:04:01]** So far it's easy, almost nothing has changed.

**[1:04:01 – 1:04:05]** Of course, if I can produce a vector at the end, I can produce it at every step.

**[1:04:05 – 1:04:18]** I just take the two hidden states, I push them through one feedforward layer, and there you go, here is your z.

**[1:04:18 – 1:04:25]** So now I have these vectors for every input word, for every token.

**[1:04:25 – 1:04:31]** But I can't just concatenate them all and feed them all over here.

**[1:04:31 – 1:04:37]** This is exactly the z is too long situation.

**[1:04:37 – 1:04:57]** I don't want to make them longer because that wouldn't make any sense, that this would be just the same thing restated differently.

**[1:04:57 – 1:05:04]** I want to have as input on every step here, I want to have one vector of this size.

**[1:05:04 – 1:05:09]** So how do I combine them into this single vector?

**[1:05:09 – 1:05:11]** And this is the attention mechanism.

**[1:05:11 – 1:05:14]** I do the following.

**[1:05:14 – 1:05:26]** I have a small network, the attention network, that receives as input.

**[1:05:26 – 1:05:28]** Okay, I need to draw the decoder too.

**[1:05:28 – 1:05:36]** So let's say that we are inside the decoder and it's got like HT prime over here.

**[1:05:36 – 1:05:39]** And we are writing the next word right now.

**[1:05:39 – 1:05:46]** And we need to find out what is the current input over here, right?

**[1:05:46 – 1:05:52]** So that it will write this token and will produce h prime t plus one and so on.

**[1:05:52 – 1:05:55]** So we are at some point in the decoding process.

**[1:05:55 – 1:06:10]** So the attention network receives as input a z from here and an h prime from here.

**[1:06:10 – 1:06:16]** So it needs to know where we are in the decoding process, of course,

**[1:06:16 – 1:06:22]** because the attention weights will be different for different words that I write.

**[1:06:22 – 1:06:30]** And then it will produce a score, A1, just a number,

**[1:06:30 – 1:06:40]** that shows how important this token is right now.

**[1:06:40 – 1:06:43]** You will see how it gets used.

**[1:06:43 – 1:06:49]** So it's the score for token number one at step t.

**[1:06:49 – 1:06:57]** So at the point characterized by this hidden state of the decoder.

**[1:06:57 – 1:07:02]** And then you do it for every z.

**[1:07:02 – 1:07:12]** So you get a2 for z2 over here.

**[1:07:12 – 1:07:16]** And you get a3 for z3.

**[1:07:16 – 1:07:30]** Then I convert this a, so let's call them the vector a,

**[1:07:30 – 1:07:35]** into probabilities, into a convex combination,

**[1:07:35 – 1:07:38]** by passing it through a softmax.

**[1:07:38 – 1:07:40]** You see how it all comes together.

**[1:07:40 – 1:07:45]** We talked about softmaxes, logistic sigmoids, etc.

**[1:07:45 – 1:07:49]** We talked about their properties in lecture 2 or something.

**[1:07:49 – 1:07:51]** And now we are using all of these properties.

**[1:07:51 – 1:07:55]** So it's not noticed that I'm using softmax not just as the output,

**[1:07:55 – 1:08:00]** but I'm also just using it to convert every time I need to convert

**[1:08:00 – 1:08:04]** just a set of numbers to a convex combination to something that sums to 1.

**[1:08:04 – 1:08:08]** And here I get something like alphas.

**[1:08:08 – 1:08:13]** Now they are from 0 to 1 and they sum up to 1.

**[1:08:13 – 1:08:18]** And that's it.

**[1:08:18 – 1:08:24]** These are the coefficients for my combination.

**[1:08:24 – 1:08:28]** So now I just do like a dot product.

**[1:08:28 – 1:08:41]** And Z_t here is just the sum of alpha_i times Z_i.

**[1:08:41 – 1:08:43]** Okay, so Z_t is not a good letter.

**[1:08:43 – 1:08:45]** Let's call it... I don't know.

**[1:08:45 – 1:08:51]** Let's call it...

**[1:08:51 – 1:08:53]** What other words do I have?

**[1:08:53 – 1:08:55]** Letters do I have U_t.

**[1:08:55 – 1:09:07]** So the input for the decoder at time step t

**[1:09:07 – 1:09:12]** is a linear combination of the representations of every token

**[1:09:12 – 1:09:17]** with weights determined by the separate attention network.

**[1:09:17 – 1:09:23]** So what this means, the intuition behind this,

**[1:09:23 – 1:09:38]** is that I want this to express what specific tokens I'm translating right now.

**[1:09:38 – 1:09:45]** So like on step 3, when I'm producing the third token, the third word,

**[1:09:45 – 1:09:52]** I want the word world to have a high weight over here

**[1:09:52 – 1:09:55]** because I'm mostly translating the word world.

**[1:09:55 – 1:09:59]** Well, in the context of the rest of the sentence, but mostly that.

**[1:09:59 – 1:10:04]** And also notice, and the last important point about this

**[1:10:04 – 1:10:09]** before I proceed to just show you the results and everything in discussion.

**[1:10:09 – 1:10:11]** The last important point is this.

**[1:10:11 – 1:10:17]** When I tell you these intuitions, when I tell you stuff like,

**[1:10:17 – 1:10:22]** "Oh, so the attention network is supposed to give you a high score for the word that we are translating right now."

**[1:10:22 – 1:10:29]** This is not any formal input for the network.

**[1:10:29 – 1:10:34]** There is no labeling in the dataset that will tell you,

**[1:10:34 – 1:10:38]** "Ah, now I'm translating this token, now I'm translating that token."

**[1:10:38 – 1:10:42]** The dataset is still the same.

**[1:10:42 – 1:10:47]** The dataset is a set of pairs like sentence in English, sentence in Russian.

**[1:10:47 – 1:10:51]** They match. They are translations of each other.

**[1:10:51 – 1:10:55]** And here you go, 100,000 pairs of sentences trained on that.

**[1:10:55 – 1:11:08]** So when I'm talking to you of intuitions like this, what I mean is we kind of want the network to work like that.

**[1:11:08 – 1:11:15]** And miraculously, after training, it indeed works like that.

**[1:11:15 – 1:11:19]** But we never explicitly train the attention network.

**[1:11:19 – 1:11:23]** The attention network is just this very small, tiny component.

**[1:11:23 – 1:11:28]** It has very few weights compared to the LSTMs.

**[1:11:28 – 1:11:37]** So a practical number, if I remember correctly, would be something like 2% of the weights of the whole network go to the attention mechanism.

**[1:11:37 – 1:11:42]** So it's a very small component compared to the rest of the network.

**[1:11:42 – 1:11:50]** But this very small component actually drives the results.

**[1:11:50 – 1:11:54]** This component is the difference between the red curve and the purple curve over here.

**[1:11:54 – 1:12:13]** This component actually does train to do this job of finding out which tokens we are translating right now and producing the correct weights.

**[1:12:13 – 1:12:19]** So it's a general principle of deep learning that we see quite often.

**[1:12:19 – 1:12:24]** And I think we already saw it in convolutional networks, I just didn't pull it out.

**[1:12:24 – 1:12:30]** The general principle that very often you just need to give the network a chance.

**[1:12:30 – 1:12:43]** You just need to introduce some components inside that have this potential ability to do the job that you want.

**[1:12:43 – 1:12:55]** And even if you have no data to train them on, even if you cannot take the attention network out of this whole thing and train it separately and then plug it back in because you don't have the inputs for this.

**[1:12:55 – 1:12:59]** The inputs are also changing as we train.

**[1:12:59 – 1:13:05]** And you don't have the outputs, you don't have the correct answers here.

**[1:13:05 – 1:13:16]** But still, if you just structurally give the network a chance to do it right, sometimes, not always, but sometimes it will do that.

**[1:13:16 – 1:13:25]** And everything will work and it will be a very nice example of a new structure inside your network.

**[1:13:25 – 1:13:35]** So this was what happened with encoder-decoder architectures around 2015.

**[1:13:35 – 1:13:40]** So in 2014, this was the state of the art.

**[1:13:40 – 1:13:48]** And even in late 2014, Badenow with colleagues introduced this kind of attention mechanism.

**[1:13:48 – 1:13:52]** So this is exactly what I was just drawing.

**[1:13:52 – 1:13:56]** The attention network that receives the current state of the decoder

**[1:13:56 – 1:14:00]** and the representation of a token from the input

**[1:14:00 – 1:14:07]** and it gets you a score and then you do a softmax.

**[1:14:07 – 1:14:12]** Yeah, here are the full formulas.

**[1:14:12 – 1:14:19]** And indeed, it does train to do what you want.

**[1:14:19 – 1:14:26]** And also, like a common feature of attention mechanisms,

**[1:14:26 – 1:14:28]** you will see that in transformers too.

**[1:14:28 – 1:14:34]** A common feature of attention mechanisms is that they also give you something to look at.

**[1:14:34 – 1:14:40]** They give you some attention weights when you actually draw them and look at them.

**[1:14:40 – 1:14:44]** They're usually very easy to interpret.

**[1:14:44 – 1:14:51]** For example, this is from one of the original machine translation applications.

**[1:14:51 – 1:14:56]** Here they're translating from French to English.

**[1:14:56 – 1:15:00]** La Destruction, Deletivement Signifier, blah, blah, blah.

**[1:15:00 – 1:15:05]** For example, French and English mostly match.

**[1:15:05 – 1:15:11]** Mostly it's a diagonal matrix where the high attention weight is on the diagonal.

**[1:15:11 – 1:15:15]** You're translating this word by word, more or less.

**[1:15:15 – 1:15:17]** But notice the exceptions.

**[1:15:17 – 1:15:25]** For example, la destruction is translated as destruction and it's two words into one.

**[1:15:25 – 1:15:27]** There is no article in English here.

**[1:15:27 – 1:15:36]** So here the attention weight is high for both la and destruction while we are writing the destruction.

**[1:15:36 – 1:15:40]** And here, for example, arm chemique, chemical weapons.

**[1:15:40 – 1:15:45]** In French the adjective goes after the noun, in English the opposite.

**[1:15:45 – 1:15:52]** So here the attention weight swap and you see an off diagram.

**[1:15:52 – 1:15:59]** I think I have examples for you here too.

**[1:15:59 – 1:16:10]** So here is a very simple recurrent network with attention that just learns to reverse the input.

**[1:16:10 – 1:16:17]** So if the input is a sequence like 3, 4, 0, 5, 7, blah, blah, blah, the output will be blah, blah, blah, 7, 5, 0, 4, 3.

**[1:16:17 – 1:16:25]** And of course the recurrent network can train to do the same. It's not hard.

**[1:16:25 – 1:16:35]** Actually, by the way, without an attention mechanism, I don't have these experiments here, but I'm pretty sure that without the attention mechanism, it would be hard.

**[1:16:35 – 1:16:52]** It would be very difficult because if you have just an encoder-decoder thing, if you don't have this attention mechanism, then you need to memorize the whole input sequence in order to write it down in the reverse order.

**[1:16:52 – 1:17:04]** So if you cannot memorize the whole input, if you don't have enough space, enough capacity in your intermediate representation to just memorize the whole input, you are screwed.

**[1:17:04 – 1:17:10]** You cannot do the reverse unless you remember it exactly.

**[1:17:10 – 1:17:14]** And with attention, you don't have to remember anything.

**[1:17:14 – 1:17:21]** You just train to have this reverse diagonal attention matrix.

**[1:17:21 – 1:17:32]** And so it's not on the diagonal because you also have special tokens like, yeah, whatever.

**[1:17:32 – 1:17:36]** You also have a special token here like end sequence.

**[1:17:36 – 1:17:48]** But anyway, there is this clear diagonal structure that basically just tells you where to look and what to copy, right?

**[1:17:48 – 1:17:57]** Or here is a more difficult example. I'm sorry, I'm not running them online because it takes a little bit of time to train.

**[1:17:57 – 1:18:04]** So just not to waste time waiting, but I will publish it and you will be able to run it yourself.

**[1:18:04 – 1:18:09]** So here is a slightly more difficult thing. Here is like a sorting thing.

**[1:18:09 – 1:18:16]** So now the input is a sequence of numbers and you need to sort them in the output.

**[1:18:16 – 1:18:26]** And here also you can see that at step t, we attend to the current t smallest value.

**[1:18:26 – 1:18:34]** So like the decoder steps are along the vertical axis, this is the source position.

**[1:18:34 – 1:18:43]** And on the first step, the most attention is paid to position where there is a one.

**[1:18:43 – 1:18:49]** On the second step, where there is a three, then to the four, then to six and so on.

**[1:18:49 – 1:18:59]** So you can see that indeed the attention mechanism has trained to do what it wants.

**[1:18:59 – 1:19:05]** And this was a big thing in 2015.

**[1:19:05 – 1:19:10]** And through the next couple of years, people were like exploring this stuff.

**[1:19:10 – 1:19:16]** And this kind of attention mechanism has a lot of benefits.

**[1:19:16 – 1:19:20]** Let me not waste time. I'm talking too much about this.

**[1:19:20 – 1:19:22]** It can do word order better.

**[1:19:22 – 1:19:28]** It can do some very interesting stuff like doing grammar as a foreign language.

**[1:19:28 – 1:19:32]** So you can sometimes fit even...

**[1:19:32 – 1:19:36]** Okay, let me talk about this because with Transformers it's even more relevant.

**[1:19:36 – 1:19:46]** So sometimes your output has some kind of complicated structure that doesn't look like a sequence.

**[1:19:46 – 1:19:52]** For example, if you're doing a syntax tree of your input, then your output is a tree.

**[1:19:52 – 1:19:55]** It's a graph, right?

**[1:19:55 – 1:20:09]** So it doesn't look like you should use a recurrent network to write out a graph.

**[1:20:09 – 1:20:12]** The graph is not a sequence, it's more complicated.

**[1:20:12 – 1:20:21]** But it turns out that if you just write down your tree as a string, and there are ways to represent the tree as a string,

**[1:20:21 – 1:20:28]** and you just treat these three strings as a language to which you translate, it works.

**[1:20:28 – 1:20:33]** And I think with Transformers it would work even better.

**[1:20:33 – 1:20:46]** In 2016 there was a very interesting paper from Google where they basically published how Google's neural machine translation system works.

**[1:20:46 – 1:20:55]** And I won't go into details here, but basically it was interesting to learn that Google Translate also works in the exact same way.

**[1:20:55 – 1:21:03]** Of course, Google being Google, it was bigger, there were some tricks, etc., etc., but basically it wasn't coder decoder with attention.

**[1:21:03 – 1:21:17]** And by the way, my personal experience was that around 2015, 2016, when they switched from whatever they had before to this kind of architectures,

**[1:21:17 – 1:21:23]** Google Translate actually became much better.

**[1:21:23 – 1:21:35]** I mean, I was using it all the time, better to say I wasn't, but I had a side job at the time translating research papers from Russian to English.

**[1:21:35 – 1:21:44]** And before about 2016, of course, I tried to use Google Translate, but it was completely hopeless.

**[1:21:44 – 1:21:53]** So you would spend much more time on fixing the results of Google Translate than you would on just typing the stuff from scratch.

**[1:21:53 – 1:21:57]** It was completely useless.

**[1:21:57 – 1:22:02]** And in 2016, 2015, there was a phase transition.

**[1:22:02 – 1:22:07]** Suddenly, sure, it was still bad. Sure, you still needed to edit it.

**[1:22:07 – 1:22:12]** You still do need to edit translations, even from the latest cloud of GPT.

**[1:22:12 – 1:22:19]** But now, it was more efficient to first do a pass with Google Translate

**[1:22:19 – 1:22:25]** and then fix the mistakes or the bad writing

**[1:22:25 – 1:22:29]** than to do everything from scratch yourself.

**[1:22:29 – 1:22:38]** This was the moment when machine translation actually started doing some useful work for me.

**[1:22:38 – 1:22:49]** The last point here is that when I'm talking about encoder-decoder architectures,

**[1:22:49 – 1:22:55]** usually I talk about the same kind of architecture in the encoder and the decoder.

**[1:22:55 – 1:23:01]** So now we were doing machine translation, it was a recurrent encoder that reads text

**[1:23:01 – 1:23:05]** and the recurrent decoder that writes text. It doesn't have to be this way.

**[1:23:05 – 1:23:11]** So you can definitely have encoder-decoder architectures where the input has one modality,

**[1:23:11 – 1:23:16]** one kind of network, and the output is a completely different kind of network,

**[1:23:16 – 1:23:22]** completely different modality. I don't even think this counts as multimodal architectures

**[1:23:22 – 1:23:27]** because, well, they are multimodal, but the two modalities are separate, really,

**[1:23:27 – 1:23:34]** because all you need from the encoder is to give you a vector representation,

**[1:23:34 – 1:23:39]** and then you take this vector representation and plug it into the decoder.

**[1:23:39 – 1:23:44]** So, for example, I mentioned at some point, I think, the captioning problem.

**[1:23:44 – 1:23:51]** Here is the captioning problem as it was in 2015 with a straightforward encoder-decoder thing.

**[1:23:51 – 1:23:57]** The encoder was a googling net that we discussed, the decoder was an LSTM,

**[1:23:57 – 1:24:04]** and it became much better when people added an attention mechanism.

**[1:24:04 – 1:24:08]** And again, this is also important and important for what will come later.

**[1:24:08 – 1:24:19]** Notice that you can do the exact same thing, this kind of attention highlighting specific parts of the input,

**[1:24:19 – 1:24:24]** even if your input is not text, even if your input is not a sequence.

**[1:24:24 – 1:24:36]** So if you have a picture, for example, the only difference here is that now we don't compress the whole picture to a single feature vector,

**[1:24:36 – 1:24:40]** like we would do if it was a straightforward encoder-to-coder.

**[1:24:40 – 1:24:47]** We have the same CNN, the same convolutional thing.

**[1:24:47 – 1:24:56]** And then I just top it a little bit short of the end, a little bit in the middle, so that I still have some geometry left.

**[1:24:56 – 1:25:08]** Like in this example, the input is 256 by 256, and I stop the feature extraction when I have a 14 by 14 feature map.

**[1:25:08 – 1:25:20]** And now I have these "pixels", elements of the feature map vectors, and I can do attention over these vectors.

**[1:25:20 – 1:25:33]** So now I can have an attention network that combines, that gives me coefficients to combine these 192...

**[1:25:33 – 1:25:48]** ...196, no, 14 by 14, 192, right? No, 196, yeah.

**[1:25:48 – 1:25:59]** So, this 14 by 14 different vectors, and they have this, so my coefficients will combine these 14 squared vectors.

**[1:25:59 – 1:26:10]** And again, it kind of works, I won't go into details, and another nice thing is that it gives you the actual attention weights.

**[1:26:10 – 1:26:12]** You can look at them and you can interpret them.

**[1:26:12 – 1:26:21]** So, we will kind of see that in transformers too, but it will be actually less clear and more complicated in transformers.

**[1:26:21 – 1:26:28]** But here, it's very clear, it's very straightforward, you can just see what the network is looking at right now...

**[1:26:28 – 1:26:34]** ...as it actually writes this piece of the output.

**[1:26:34 – 1:26:41]** So, a woman is throwing a frisbee in the park. Here is woman, we are writing woman, we look at the people...

**[1:26:41 – 1:26:48]** ...and then throwing, and we start concentrating on the throwing, and frisbee, we are concentrating on the frisbee...

**[1:26:48 – 1:26:55]** ...and when I write down the park, then we are not looking at the people, we are looking at the background.

**[1:26:55 – 1:26:58]** So that's just perfect.

**[1:26:58 – 1:27:05]** Okay, so I want to stop here, are there any questions at this point?

**[1:27:05 – 1:27:10]** You've actually covered quite a lot, starting from LSTMs...

**[1:27:10 – 1:27:19]** ...of the attention mechanisms, recurrent attention, and on to encoder-decoder attention.

**[1:27:19 – 1:27:24]** Wonderful, so let's have a break, please let's not have a half an hour break...

**[1:27:24 – 1:27:35]** ...because today our administration asked me to call it 1:20...

**[1:27:35 – 1:27:39]** ...so let's have a 15-minute break and then we'll reconvene...

**[1:27:39 – 1:27:48]** ...and we'll discuss the main architecture of the entire Deep Learning right now...

**[1:27:48 – 1:27:53]** ...for the last 10 years, the transformer break.

**[1:27:53 – 1:46:31]** Okay, so on to the Transformers.

**[1:46:31 – 1:46:40]** Transformers appeared in 2017 and was kind of...

**[1:46:40 – 1:46:45]** ...I mean, let me start with a brief historical remark.

**[1:46:45 – 1:46:49]** In 2017, when this paper appeared at the end of the year...

**[1:46:49 – 1:46:56]** ...I don't think, I'm pretty sure, the authors of the transformer paper...

**[1:46:56 – 1:47:01]** ...if the transformer paper of attention is all you need, actually understood what they were doing.

**[1:47:01 – 1:47:05]** So the paper is not that ambitious.

**[1:47:05 – 1:47:12]** We will see what its results were originally, and they are mostly about...

**[1:47:12 – 1:47:21]** ...here is a different way to do stuff which provides approximately the same results...

**[1:47:21 – 1:47:28]** ...but which is more efficient, so maybe let's switch to this more efficient way of doing basically the same.

**[1:47:28 – 1:47:36]** But since then, the whole field of machine learning switched to transformers, as we all know...

**[1:47:36 – 1:47:42]** ...and much of the rest of our class will be built on the transformers.

**[1:47:42 – 1:47:48]** We will use transformers in different ways.

**[1:47:48 – 1:47:56]** The main, I think, positive qualities that the transformer had...

**[1:47:56 – 1:48:02]** ...that the original paper couldn't really notice from its experiments...

**[1:48:02 – 1:48:05]** ...are two things.

**[1:48:05 – 1:48:09]** One, it turned out it proved to be very, very general...

**[1:48:09 – 1:48:15]** ...in the sense that the transformer is just very good...

**[1:48:15 – 1:48:20]** ...at noticing internal correlations within complicated data.

**[1:48:20 – 1:48:27]** And it doesn't really matter for the transformer whether it's text...

**[1:48:27 – 1:48:33]** ...or images or whatever, it just works with sequences of vectors.

**[1:48:33 – 1:48:38]** It doesn't care where these vectors come from.

**[1:48:38 – 1:48:41]** So this is a great thing.

**[1:48:41 – 1:48:45]** And an even more important thing is that...

**[1:48:45 – 1:48:53]** ...transformers prove to be extremely scalable.

**[1:48:53 – 1:48:58]** You can take a transformer, you can scale it up, and it works better.

**[1:48:58 – 1:49:02]** You can scale it further up without changing anything inside.

**[1:49:02 – 1:49:06]** Well, sure, there have been novelties. Sure, modern transformers...

**[1:49:06 – 1:49:11]** ...is slightly different from the one we had years ago, but it's mostly the same.

**[1:49:11 – 1:49:16]** And still you scale it up and it works better and better and better...

**[1:49:16 – 1:49:18]** ...and it never saturates.

**[1:49:18 – 1:49:23]** With our large language models, I hope I will have time to talk about that next week.

**[1:49:23 – 1:49:29]** With large language models, we keep going from tens of millions...

**[1:49:29 – 1:49:32]** ...to hundreds of millions, to billions, to hundreds of billions...

**[1:49:32 – 1:49:36]** ...to now trillions of parameters, and they just keep getting better.

**[1:49:36 – 1:49:40]** And this had never happened before.

**[1:49:40 – 1:49:43]** You can't scale LSTMs in the same way.

**[1:49:43 – 1:49:47]** Or I mean, maybe you can, but we don't have enough compute to do that...

**[1:49:47 – 1:49:54]** ...but the complexity grows too fast, or they saturate...

**[1:49:54 – 1:49:58]** ...and even if you can't train, they stop providing any benefit.

**[1:49:58 – 1:50:03]** And in the transformer, it kind of all came together.

**[1:50:03 – 1:50:07]** So what is the transformer?

**[1:50:07 – 1:50:12]** I will actually go through the slides first, through some of the slides first...

**[1:50:12 – 1:50:16]** ...because the basic structure is very similar to what we were just discussing.

**[1:50:16 – 1:50:22]** I don't have to redraw it, but then the main core will be the self-attention mechanism...

**[1:50:22 – 1:50:27]** ...and that is completely new, and that I will, of course, discuss in detail.

**[1:50:27 – 1:50:31]** So this is the most famous picture from the original paper...

**[1:50:31 – 1:50:36]** ...but I think it's pretty hard to understand, so I make my own pictures here.

**[1:50:36 – 1:50:42]** Here is the structure of the original transform...

**[1:50:42 – 1:50:46]** ...without details, without the interesting parts...

**[1:50:46 – 1:50:52]** ...but the general structure is actually very straightforward...

**[1:50:52 – 1:50:56]** ...and it's very similar to what we just had in...

**[1:50:56 – 1:51:00]** ...recurrent encoder-decoder with attention architectures.

**[1:51:00 – 1:51:07]** So it's an encoder-decoder architecture, and yes, the original transformer...

**[1:51:07 – 1:51:10]** ...doing machine translation.

**[1:51:10 – 1:51:15]** It has an encoder which consists of six identical layers.

**[1:51:15 – 1:51:20]** It has a decoder which consists of six identical layers.

**[1:51:20 – 1:51:25]** And the encoder receives text in one language.

**[1:51:25 – 1:51:29]** The decoder produces text in another language.

**[1:51:29 – 1:51:32]** Let's stay in this paradigm for now.

**[1:51:32 – 1:51:36]** Interesting parts here.

**[1:51:36 – 1:51:38]** What can we see on this picture?

**[1:51:38 – 1:51:42]** So first of all, the input to the actual transformer,

**[1:51:42 – 1:51:47]** the actual encoder layers, is not just a sequence of tokens.

**[1:51:47 – 1:51:50]** And we didn't discuss it in detail.

**[1:51:50 – 1:51:58]** I mean, text is not our thing, but it had been very common

**[1:51:58 – 1:52:01]** in natural language processing even ten years ago

**[1:52:01 – 1:52:09]** to convert one-hot representations of words, of tokens,

**[1:52:09 – 1:52:14]** to continuous representations that are usually called embeddings.

**[1:52:14 – 1:52:18]** This is, again, very, very common, very straightforward,

**[1:52:18 – 1:52:20]** all through deep learning.

**[1:52:20 – 1:52:24]** If you have a large vocabulary of different stuff that you want to input,

**[1:52:24 – 1:52:30]** like in this case, different words or tokens, parts of words,

**[1:52:30 – 1:52:44]** then you first want to convert them to dense vectors.

**[1:52:44 – 1:52:48]** And there is like a whole line of work in NLP on this,

**[1:52:48 – 1:52:53]** like work2vec, glove, fast text, different embeddings, we won't go there.

**[1:52:53 – 1:52:56]** But here, the embeddings are really straightforward.

**[1:52:56 – 1:52:59]** There is just one very interesting technical thing

**[1:52:59 – 1:53:02]** that I will talk to afterwards, at the end.

**[1:53:02 – 1:53:06]** But mostly, it's just a matrix of vectors.

**[1:53:06 – 1:53:11]** So for every input token, there is a vector, and we look it up,

**[1:53:11 – 1:53:15]** and we put it in place of this token. That's it.

**[1:53:15 – 1:53:20]** But importantly, it's not some external representation,

**[1:53:20 – 1:53:23]** it's not some work2vec that we copy here,

**[1:53:23 – 1:53:27]** it's an embedding layer that is trained with the rest of the network.

**[1:53:27 – 1:53:33]** So you train these vector representations along with the other weights.

**[1:53:33 – 1:53:38]** And after this embedding layer, the input sequence becomes a sequence of vectors.

**[1:53:38 – 1:53:43]** And all the actual transformer is doing,

**[1:53:43 – 1:53:48]** it's rewriting sequences of vectors into sequences of vectors.

**[1:53:48 – 1:53:54]** So every encoder layer will take a sequence of vectors as input

**[1:53:54 – 1:53:59]** and produce the same sequence of vectors.

**[1:53:59 – 1:54:03]** Well, I mean, a sequence of vectors of the same size as output.

**[1:54:03 – 1:54:11]** And that will rewrite this kind of structure for, in this case, six times.

**[1:54:11 – 1:54:15]** And then we get a vector for every input token.

**[1:54:15 – 1:54:20]** After all of this encoding, it's no longer just a representation of the token,

**[1:54:20 – 1:54:25]** it's now a representation of the token in the context of all the other tokens.

**[1:54:25 – 1:54:29]** And I mean, many times it has looked at all the other tokens,

**[1:54:29 – 1:54:32]** the whole sentence, the whole sequence, et cetera, et cetera.

**[1:54:32 – 1:54:36]** So by now, by the top here, we have these representations

**[1:54:36 – 1:54:40]** of smart, semantically rich representations of input tokens.

**[1:54:40 – 1:54:42]** And now what does the decoder do?

**[1:54:42 – 1:54:47]** The decoder is a language model.

**[1:54:47 – 1:54:49]** I hope you've heard of language models.

**[1:54:49 – 1:54:58]** So the decoder is producing output tokens one by one, autoregressively.

**[1:54:58 – 1:55:05]** So its input is what it has already written,

**[1:55:05 – 1:55:11]** the history of output until now.

**[1:55:11 – 1:55:14]** And its output is the next token.

**[1:55:19 – 1:55:26]** You have to run the transformer decoder as many times as the number of tokens that you want to produce.

**[1:55:26 – 1:55:35]** Again, this is one kind of restriction that in modern language models you need to work around in some way.

**[1:55:35 – 1:55:43]** There is a big science around it with speculative decoding and stuff like that, but you won't go there.

**[1:55:43 – 1:55:51]** Anyway, by default, it's an autoregressive thing. You produce the output token by token.

**[1:55:51 – 1:56:11]** And these guys, the stuff that you are actually translating... Sorry, I don't really understand this. Can you see my cursor? You can't, right? Yeah, okay, so pointing with the mouse doesn't really work.

**[1:56:11 – 1:56:29]** Alright, so the stuff that is at the output of the encoder on top left here, it's getting used in the decoder on every layer, on every step of the way.

**[1:56:29 – 1:56:41]** And of course we will discuss how exactly. But this high level structure is very similar to what we just saw, right?

**[1:56:41 – 1:56:50]** Decoder and there is no separate attention network here, the attention will be hidden inside the encoder and the decoder.

**[1:56:50 – 1:57:06]** So if you look inside an encoder layer in the decoder layer, you will see that the encoder layer, actually I think you see, yeah I have it here.

**[1:57:06 – 1:57:24]** So the encoder layer is what, it's a self-attention layer, then layer normalization, then interestingly a feed-forward layer, a fully connected layer, then another layer norm and that's it.

**[1:57:24 – 1:57:32]** So of course the interesting part, the part we are going to discuss in detail is self-attention, right, the self-attention is the first layer here.

**[1:57:32 – 1:57:47]** But the rest also uses these components that we have been discussing, right, so it's not, we are not discussing ancient history, everything that, all the ideas that I'm telling you are actually being used right now.

**[1:57:47 – 1:58:03]** For example, here we see a residual connection that goes around the self-attention layer, right, and it lands, actually I forget in front or afterwards, but near this layer normalization layer,

**[1:58:03 – 1:58:11]** which is a kind of batch norm, right, so you discussed it with Alex in practice, layer norm is like batch norm,

**[1:58:11 – 1:58:18]** but not across the mini-batch, but across all of the outputs of the current layer.

**[1:58:18 – 1:58:29]** So transformers are big, and then transformers, oops, what happened, sorry.

**[1:58:29 – 1:58:33]** Recording in progress.

**[1:58:33 – 1:58:38]** Yeah, I apologize, I'm not sure what happened, but somehow I got disconnected from Zoom.

**[1:58:38 – 1:58:46]** The internet works, I hope you can see.

**[1:58:46 – 1:58:56]** Yeah, so the, where did I stop?

**[1:58:56 – 1:59:06]** Yeah, so the encoder layer uses this layer norm at the output of self-attention,

**[1:59:06 – 1:59:12]** and layer norm, as you discussed with Alex, just averages out the gradients,

**[1:59:12 – 1:59:22]** keeps the loss landscape smooth, keeps it under control in terms of the absolute values of outputs, etc.

**[1:59:22 – 1:59:35]** And here, transformers are big, so we cannot really rely on batch norm,

**[1:59:35 – 1:59:41]** because probably there is no batch, probably only one copy of the transformer fits into our memory,

**[1:59:41 – 1:59:46]** and we have only one instance, so we use layer norm.

**[1:59:46 – 1:59:50]** And then, interestingly, there is just a feedforward layer, and it's actually very important.

**[1:59:50 – 2:00:01]** It has a lot of weights. If you look at it, it takes up quite a big fraction of the entire weights of the transformer.

**[2:00:01 – 2:00:11]** And there is nothing to say about it, it's just rearranging the features, mixing together the features in every vector separately,

**[2:00:11 – 2:00:20]** as you can see, it's applied to every Z' individually, and then there is another layer, and that's the encoder layer.

**[2:00:20 – 2:00:31]** In the decoder, you also have self-attention. It's exactly the same as the self-attention here, except for the word masked, but we'll get there.

**[2:00:31 – 2:00:42]** There's also a feed-forward layer, also layer norms after everything, and the only difference is this encoder-decoder attention layer.

**[2:00:42 – 2:00:48]** The outputs of the encoder, these vector representations, they should go somewhere, right?

**[2:00:48 – 2:00:51]** They should be doing something, and they go here.

**[2:00:51 – 2:00:54]** And when we get there, I'll explain what exactly they do.

**[2:00:54 – 2:01:03]** And then after the decoder has, after we've gone through the decoder, then of course we have to do some classification.

**[2:01:03 – 2:01:13]** So there is a linear layer that goes to a softmax layer, and the softmax produces probabilities, and then you sample the next token with these probabilities.

**[2:01:13 – 2:01:20]** So again, as you can see, it's exactly a logistic regression at the end, so it all kind of comes together.

**[2:01:20 – 2:01:34]** All right, so this is the general structure, and on this picture there should be absolutely nothing new to you, except, of course, the self-attention stuff.

**[2:01:34 – 2:01:41]** So what is self-attention? What exactly? How do we understand it? Where does it come from?

**[2:01:41 – 2:01:47]** Item number three for today, self-attention.

**[2:01:47 – 2:02:02]** Well, to actually discuss self-attention, I need to take a step back and I need to talk to you, surprisingly, about information retrieval,

**[2:02:02 – 2:02:10]** which is not the subject of our class, but turns out to be very relevant.

**[2:02:10 – 2:02:20]** So how does search work in deep learning? How does information retrieval work when you have neural networks?

**[2:02:20 – 2:02:34]** Well, basically it works like this. You have the queries, query one, query two, and you have documents.

**[2:02:34 – 2:02:42]** Document one, document two, document three, document four.

**[2:02:42 – 2:02:54]** And in usual information retrieval, what you would do, you would establish a similarity.

**[2:02:54 – 2:02:59]** You need to establish some kind of similarity between queries and documents.

**[2:02:59 – 2:03:05]** This kind of similarity will be called relevance and you will train it to be the relevance.

**[2:03:05 – 2:03:12]** So it should be higher when this document is relevant to this query.

**[2:03:12 – 2:03:16]** This is how search generally works, whatever it is.

**[2:03:16 – 2:03:23]** But when you have deep learning, when you have these neural networks that can process any kinds of input

**[2:03:23 – 2:03:29]** and that can train to process long texts, large images, etc.

**[2:03:29 – 2:03:45]** What you usually do is this. You get documents through an encoder, and the documents will become vectors.

**[2:03:45 – 2:03:53]** You get queries through their own encoder, so they become vectors too.

**[2:03:53 – 2:04:02]** And the idea is that all of these vectors should live in the same space.

**[2:04:02 – 2:04:09]** So even though encoders are different, they cannot be the same because documents can be images, for example.

**[2:04:09 – 2:04:15]** So they are different, but they should produce vectors in the same latent space.

**[2:04:15 – 2:04:26]** So documents get mapped over here, and then you map your query over here,

**[2:04:26 – 2:04:36]** and you are supposed to train the whole system so that the relevant documents will be close,

**[2:04:36 – 2:04:43]** the representations of relevant documents will be close to the representations of the queries.

**[2:04:43 – 2:04:51]** So then, inside this latent space, you will be able to just take nearest neighbors,

**[2:04:51 – 2:04:56]** and these nearest neighbors will be a good answer to the search query.

**[2:04:56 – 2:05:03]** So I was drawing this, but I think I have a picture about it.

**[2:05:03 – 2:05:11]** So you have a query, you have a document, documents go through their own encoders,

**[2:05:11 – 2:05:23]** and then the whole point of it is so that in the latent space,

**[2:05:23 – 2:05:35]** you actually have the structure that relevant documents will be near the images of the queries.

**[2:05:35 – 2:05:41]** There is a whole field of study about how to do that.

**[2:05:41 – 2:05:52]** It's obviously a very big subfield of learning,

**[2:05:52 – 2:05:56]** and we could have a whole class on information retrieval, maybe you will,

**[2:05:56 – 2:05:58]** so I won't go into more details.

**[2:05:58 – 2:06:07]** But what we need now is this basic intuition that different stuff gets mapped to the same latent space,

**[2:06:07 – 2:06:11]** and in that latent space we are just looking for nearest neighbors.

**[2:06:11 – 2:06:19]** And since you can do it linearly, as a linear space,

**[2:06:19 – 2:06:25]** basically the similarity here between the query and the document

**[2:06:25 – 2:06:34]** can be thought of as just the dot product of the corresponding vectors.

**[2:06:34 – 2:06:40]** So I encode the document and I multiply it by the encoding of the query.

**[2:06:40 – 2:06:44]** That's it, okay?

**[2:06:44 – 2:06:48]** And this approach has lots of advantages for information retrieval.

**[2:06:48 – 2:06:52]** You can just store the vectors, you don't have to think about anything else.

**[2:06:52 – 2:06:57]** It's fast to do it in the low dimensional space, blah, blah, blah.

**[2:06:57 – 2:07:04]** And self-attention, interestingly enough, draws on this intuition,

**[2:07:04 – 2:07:10]** but since it's self-attention, it applies these ideas to the same set of vectors

**[2:07:10 – 2:07:15]** that are both queries and documents.

**[2:07:15 – 2:07:23]** So here is how it works.

**[2:07:38 – 2:07:40]** Here is how it works.

**[2:07:40 – 2:07:46]** So we begin with a set of vectors.

**[2:07:46 – 2:07:54]** As I said, every layer of the transformer gets just a sequence of vectors as input.

**[2:07:54 – 2:08:07]** So we have this, putting down here, x1, x2, and so on, xn.

**[2:08:07 – 2:08:12]** We have these vector inputs.

**[2:08:12 – 2:08:21]** Now I want to make this kind of query document thing.

**[2:08:21 – 2:08:33]** In information retrieval, the terminology is inherited from classical information retrieval.

**[2:08:33 – 2:08:41]** You would sometimes call these images of documents, the representation of documents, you would call the keys.

**[2:08:41 – 2:08:46]** In classical retrieval, the query would not need to be encoded, it would be just the query.

**[2:08:46 – 2:08:52]** There is no word for the image of the query, but we will just call it the query.

**[2:08:52 – 2:09:03]** Let's say that the query already lives in this space, and the document should be mapped there and should produce some kind of a key.

**[2:09:03 – 2:09:15]** And here we take our axis, let's say we take x1, and we produce from it queries, keys, and values.

**[2:09:15 – 2:09:27]** So with x1, we multiply it by a matrix called w cube, and as a result, we get the first query vector.

**[2:09:27 – 2:09:30]** This will be q1.

**[2:09:30 – 2:09:43]** Then we take all of the inputs, all of the axes, and we multiply them by the matrix w, k.

**[2:09:43 – 2:09:47]** We just put it here once, not copy it many times.

**[2:09:47 – 2:09:50]** And we get the key vectors.

**[2:09:50 – 2:09:57]** We get k1, k2, and so on, kn.

**[2:09:57 – 2:10:05]** And the whole point of self-attention is that q and k should live in the same latent space.

**[2:10:05 – 2:10:13]** So now this guy goes here, these guys also go here.

**[2:10:13 – 2:10:26]** And the similarity between q and k is just a dot product between them.

**[2:10:26 – 2:10:34]** We assume that they already live in this latent space, they have the same dimension.

**[2:10:34 – 2:10:46]** And this similarity is exactly the score that we will use as the attention of it.

**[2:10:46 – 2:10:59]** You see, q was made from x, k was also made from x, and now we look at how similar q and k are between each other.

**[2:10:59 – 2:11:15]** So out of this space, we get this sequence of attention scores, so to say, affinities.

**[2:11:15 – 2:11:32]** We get a11, which is q1 times k1, and then a12 and so on, a1n, which is q1 times kn.

**[2:11:32 – 2:11:42]** So we get this vector of attention affinities, we put it through the softmax, as usual.

**[2:11:42 – 2:11:51]** And we get, yes, sorry, also I forgot one detail, I'll get to it later.

**[2:11:51 – 2:12:00]** But we put through the softmax, we rescale first by square root of d, and then we put it through the softmax.

**[2:12:00 – 2:12:05]** So this kind of transformation, I'll explain later why we need rescaling.

**[2:12:05 – 2:12:10]** And then we get this vector of attention weights.

**[2:12:10 – 2:12:16]** So now we have, this will be like a1 and this will be alpha1.

**[2:12:16 – 2:12:23]** So this is the actual attention weights between 0 and 1, rescaled to sum up to 1.

**[2:12:23 – 2:12:35]** And they are the similarities between the first query and all the keys, right?

**[2:12:35 – 2:12:39]** Similarities rescaled back to a set of weights.

**[2:12:39 – 2:12:46]** So now we need to use the set of weights to make some kind of linear combination,

**[2:12:46 – 2:12:48]** to make a convex combination of something.

**[2:12:48 – 2:12:56]** Well, of what? Of another set of vectors.

**[2:12:56 – 2:12:58]** Here is the thing.

**[2:12:58 – 2:13:10]** So now we again take all of the axes and we multiply them by yet another matrix,

**[2:13:10 – 2:13:20]** weight matrix WV, and we get vectors that we call values.

**[2:13:20 – 2:13:33]** So the green ones are values, the blue ones are keys, and the red ones are queries.

**[2:13:33 – 2:13:47]** And now we take all of these values and we multiply them with the dot product.

**[2:13:47 – 2:13:51]** We multiply them, we add them up with the coefficients alpha.

**[2:13:51 – 2:13:57]** So this is what this is.

**[2:13:57 – 2:14:02]** What's the dot product? How do I write this, right?

**[2:14:02 – 2:14:05]** Anyway, dot product.

**[2:14:05 – 2:14:08]** So the output is, let's call it z1.

**[2:14:08 – 2:14:18]** It's the sum of alpha1i times vi, okay?

**[2:14:18 – 2:14:26]** And that's it. That's the basic idea of self-attention.

**[2:14:26 – 2:14:32]** And of course, I only drew one query, but it then gets repeated.

**[2:14:32 – 2:14:37]** So we take x2, we multiply it by wq, we get q2.

**[2:14:37 – 2:14:40]** It also gets mapped here, blah, blah, blah.

**[2:14:40 – 2:14:46]** And as the output, we get z2, which is the sum of alpha 2i, again, times vi.

**[2:14:46 – 2:14:49]** And vi is our vectors, right?

**[2:14:49 – 2:14:54]** So this takes a little bit of understanding.

**[2:14:54 – 2:14:57]** Yeah, cosine similarity, right?

**[2:14:57 – 2:15:01]** So this takes a little bit of understanding to get it in your head,

**[2:15:01 – 2:15:04]** because it's all very abstract, right?

**[2:15:04 – 2:15:07]** It's just some dot products in some new space,

**[2:15:07 – 2:15:11]** and this new space is just multiplication by the weight matrices.

**[2:15:11 – 2:15:19]** Nothing too intuitive here.

**[2:15:19 – 2:15:23]** Well, I tried to give you the basic intuition for information retrieval,

**[2:15:23 – 2:15:27]** but I mean, it only goes so far.

**[2:15:27 – 2:15:31]** Still, formally, it's really, really simple, right?

**[2:15:31 – 2:15:34]** So what we do formally is we take the axis,

**[2:15:34 – 2:15:38]** we multiply them by a matrix, we get the queries.

**[2:15:38 – 2:15:42]** So in practice, of course, you would not do it step by step,

**[2:15:42 – 2:15:44]** you would do it all at once.

**[2:15:44 – 2:15:48]** So your queries are some weight matrix times x,

**[2:15:48 – 2:15:53]** or maybe the other way around, I forget which one is more common,

**[2:15:53 – 2:15:55]** maybe x times this matrix, it doesn't matter.

**[2:15:55 – 2:15:59]** And your keys are some weight matrix times x,

**[2:15:59 – 2:16:06]** and your values are some weight matrix times x, right?

**[2:16:06 – 2:16:11]** And then what do you do with these matrices?

**[2:16:11 – 2:16:14]** So if we continue the formal stuff,

**[2:16:14 – 2:16:20]** you need to get this matrix of all possible cosine similarities,

**[2:16:20 – 2:16:27]** you write all possible dot products between queries and keys.

**[2:16:27 – 2:16:29]** So if you write it in matrix forms,

**[2:16:29 – 2:16:33]** then it will be like q times k transpose.

**[2:16:33 – 2:16:46]** This will be the matrix where the ij's element will be like qi dot product by kj, right?

**[2:16:46 – 2:16:53]** And then you take this q times k transpose and you rescale, you do softmax,

**[2:16:53 – 2:16:57]** and then you multiply by the result, the vectors v.

**[2:16:57 – 2:17:12]** So the attention weights are the softmax of one of the square root of d q k transpose,

**[2:17:12 – 2:17:28]** and the actual output, dz, is softmax of one over the square root of d q k transpose times v.

**[2:17:28 – 2:17:34]** And that's the main formula that you see everywhere, right?

**[2:17:34 – 2:17:46]** This is from the original attention is all you need paper, and this is exactly what I was trying to explain to you here.

**[2:17:46 – 2:17:55]** So the intuition about these matrices, their dimensions and everything is that x is probably pretty big, pretty long.

**[2:17:55 – 2:18:04]** It's from some r to, I don't know, some capital D, and queries and keys have to live in the same space.

**[2:18:04 – 2:18:13]** We have to make dot products with them, so they both have to be living in the same smaller space, small d.

**[2:18:13 – 2:18:22]** So this matrix and this matrix are both like d times small d matrices.

**[2:18:22 – 2:18:27]** And values formally can have a different size, right?

**[2:18:27 – 2:18:31]** We never take a dot product between v and q or v and k.

**[2:18:31 – 2:18:38]** So formally it could be like d prime. In practice usually it's the same d, of course.

**[2:18:38 – 2:18:42]** But formally let me write that this is like a d times d prime matrix.

**[2:18:42 – 2:18:47]** Or sorry, the way I write it, it should be that way around.

**[2:18:47 – 2:18:55]** It should be d times capital D and this should be d prime times capital D.

**[2:18:55 – 2:19:05]** Okay, so what else can I say here?

**[2:19:05 – 2:19:08]** What else can I say here?

**[2:19:08 – 2:19:21]** I think that's it for the basic idea of self-attention we got from the beginning to the end.

**[2:19:21 – 2:19:24]** I will show you a nicer picture in a sec.

**[2:19:24 – 2:19:28]** Let me just highlight one thing.

**[2:19:28 – 2:19:33]** Sorry, I promised to explain where the square root of D comes from.

**[2:19:33 – 2:19:35]** Why the rescaling?

**[2:19:35 – 2:19:39]** Well, the rescaling goes like this.

**[2:19:39 – 2:19:48]** What we have here, what we have in this raw affinities between queries and keys

**[2:19:48 – 2:19:54]** are like dot products between vectors of length D.

**[2:19:54 – 2:20:00]** And if you think of, say, queries and keys as just random vectors,

**[2:20:00 – 2:20:05]** vectors with random numbers inside, you see that...

**[2:20:05 – 2:20:09]** What do you see? You see something, don't you?

**[2:20:09 – 2:20:16]** You see that these vectors with queries and keys inside,

**[2:20:16 – 2:20:20]** if you think of them as just random vectors,

**[2:20:20 – 2:20:28]** so let's say it's like QI is something like 0 plus or minus 1, right?

**[2:20:28 – 2:20:35]** So it's something from minus 1 to 1 on average, maybe more, maybe less,

**[2:20:35 – 2:20:39]** but more or less it has a standard deviation of 1 around 0.

**[2:20:39 – 2:20:43]** And KJ also has a standard deviation of 1 around 0.

**[2:20:43 – 2:20:45]** Then what is happening here?

**[2:20:45 – 2:20:54]** This is the sum of d batch numbers with deviation 1.

**[2:20:54 – 2:21:00]** And if you take the sum of d random variables,

**[2:21:00 – 2:21:08]** each of which can go to plus or minus 1 on average,

**[2:21:08 – 2:21:15]** then the result will have a variance on the order of give or take square root of d.

**[2:21:15 – 2:21:19]** I don't want to do probability theory now.

**[2:21:19 – 2:21:21]** It's a classical result.

**[2:21:21 – 2:21:24]** Basically, I think if you ever had a probability theory class,

**[2:21:24 – 2:21:30]** you probably know this in the form of random walks on a line.

**[2:21:30 – 2:21:33]** Like if you go from zero and you clip a coin,

**[2:21:33 – 2:21:36]** and every time you go either right or left,

**[2:21:36 – 2:21:40]** then how far from zero do you expect to be in n steps?

**[2:21:40 – 2:21:42]** And the answer is square root of n.

**[2:21:42 – 2:21:45]** So it's the exact same effect.

**[2:21:45 – 2:21:49]** And that means that if we don't do this,

**[2:21:49 – 2:21:53]** we will have big numbers over here.

**[2:21:53 – 2:21:58]** If, for example, d is something like 64,

**[2:21:58 – 2:22:00]** which I think was true for the first transformer,

**[2:22:00 – 2:22:03]** then when you add 64 numbers,

**[2:22:03 – 2:22:07]** you get numbers on the order of plus or minus 8.

**[2:22:07 – 2:22:11]** And plus or minus 8 is more or less,

**[2:22:11 – 2:22:15]** more or less means that the output of the softmax

**[2:22:15 – 2:22:18]** will be close to just one and zeros,

**[2:22:18 – 2:22:20]** close to a one-hot vector,

**[2:22:20 – 2:22:22]** which is not really what we need.

**[2:22:22 – 2:22:24]** We need it to be smoother here.

**[2:22:24 – 2:22:26]** So we smooth it back, we rescale it back

**[2:22:26 – 2:22:28]** so that we go from the square root of d

**[2:22:28 – 2:22:30]** back to give or take one.

**[2:22:30 – 2:22:33]** That's an explanation for the scaling.

**[2:22:33 – 2:22:38]** And what else I can notice right here, right now,

**[2:22:38 – 2:22:49]** is that we already see the main computational problem of transformers.

**[2:22:49 – 2:22:53]** I don't think we will have time in class to discuss this huge line of work

**[2:22:53 – 2:22:57]** that tries to avoid this, to work with it,

**[2:22:57 – 2:23:02]** but we definitely should mention the problem itself.

**[2:23:02 – 2:23:07]** Here, to compute this, you need to have this matrix.

**[2:23:07 – 2:23:11]** You need to compute this matrix.

**[2:23:11 – 2:23:14]** This matrix is an n times n matrix.

**[2:23:14 – 2:23:27]** And this is like quadratic complexity as a function of the input length,

**[2:23:27 – 2:23:30]** of the length of the input sequence.

**[2:23:30 – 2:23:34]** And that is the main computational problem of transformers,

**[2:23:34 – 2:23:40]** because it means that you cannot scale them up with respect to the input length

**[2:23:40 – 2:23:46]** unless you do some interesting tricks.

**[2:23:46 – 2:23:49]** And of course, there are a million different interesting tricks.

**[2:23:49 – 2:23:50]** It's a big field.

**[2:23:50 – 2:23:54]** But basically, if you remember like three years ago,

**[2:23:54 – 2:23:57]** when people were doing large language models,

**[2:23:57 – 2:24:00]** they would be like boasting about their context size.

**[2:24:00 – 2:24:07]** They would be saying like, "Oh, our LLM has a context size of 128,000 tokens,

**[2:24:07 – 2:24:13]** and our LLM has 512,000 tokens, and we've got a million token context window."

**[2:24:13 – 2:24:17]** I mean, this is about that.

**[2:24:17 – 2:24:22]** So it's not trivial to get to a million token context window.

**[2:24:22 – 2:24:29]** It doesn't just mean that the complexity is a million times one token.

**[2:24:29 – 2:24:33]** It means that the complexity is a million squared times one token,

**[2:24:33 – 2:24:36]** and a million squared is just too much, definitely too much.

**[2:24:36 – 2:24:40]** So you cannot do it straightforwardly as this matrix.

**[2:24:40 – 2:24:42]** You have to invent some tricks around it.

**[2:24:42 – 2:24:46]** And of course, there is a big field of science around this.

**[2:24:46 – 2:24:52]** Even right now, I think, if you go to Cloud,

**[2:24:52 – 2:24:56]** you will see that it has a separate model called Opus

**[2:24:56 – 2:24:59]** with a one million token context.

**[2:24:59 – 2:25:05]** And it's more expensive, more complicated than just straightforward Opus,

**[2:25:05 – 2:25:10]** which obviously has a smaller context size.

**[2:25:10 – 2:25:14]** So context is a difficult problem for transformers.

**[2:25:14 – 2:25:18]** But other than that, it's all here.

**[2:25:18 – 2:25:20]** This is how self-attention works.

**[2:25:20 – 2:25:25]** And I won't try to draw it on the board.

**[2:25:25 – 2:25:27]** I will show it to you on slides.

**[2:25:27 – 2:25:35]** But the next thing and another idea that we actually were discussing

**[2:25:35 – 2:25:39]** a couple of days ago, and now it all comes together.

**[2:25:39 – 2:25:48]** Another important idea here is that notice what we are doing to x's.

**[2:25:48 – 2:25:51]** Again, let's look at it from this geometric perspective.

**[2:25:51 – 2:25:55]** I think yesterday we talked about this.

**[2:25:55 – 2:26:01]** Geometrically, what we are doing is we are taking this x in a big space

**[2:26:01 – 2:26:07]** and we are projecting it to a much smaller space in two different ways.

**[2:26:07 – 2:26:10]** And these two ways give us the queries and the keys.

**[2:26:10 – 2:26:15]** Again, I can't give you like tangible intuition that you can touch,

**[2:26:15 – 2:26:19]** but mathematically what you are doing is you have a big space

**[2:26:19 – 2:26:24]** and you are looking for a good projection for the queries

**[2:26:24 – 2:26:29]** and another but the same dimensional projection for the keys.

**[2:26:29 – 2:26:34]** So like two ways of looking at the set of vectors x.

**[2:26:34 – 2:26:40]** And then there is the third projection which can have a different dimension for the various.

**[2:26:40 – 2:26:46]** So in a way it's again the same question that I asked yesterday.

**[2:26:46 – 2:26:55]** If all I do with axes with these vectors is compress them down to queries, keys and values

**[2:26:55 – 2:27:03]** and in practice like if you have, I don't know, capital D something like 256 or 512

**[2:27:03 – 2:27:08]** you would have small d something like 64 as I said

**[2:27:08 – 2:27:11]** then why do we need the long vectors at all?

**[2:27:11 – 2:27:16]** same question as we had yesterday and it's the same answer

**[2:27:16 – 2:27:22]** the answer is this is what I've just drawn to you is just one attention head

**[2:27:22 – 2:27:27]** and in practice in the transformer you will have several different attention heads

**[2:27:27 – 2:27:34]** each will have its own matrices WQ, WK, WV

**[2:27:34 – 2:27:42]** and they will produce their own kind of ways of looking at the input

**[2:27:42 – 2:27:48]** and ultimately they will produce their own output z_i

**[2:27:48 – 2:27:54]** so really there is another index in here

**[2:27:54 – 2:27:59]** let's look at the slides, I have better pictures up there

**[2:27:59 – 2:28:06]** so this is the intuition coming from self-attention

**[2:28:06 – 2:28:09]** and this is the picture that I was just drawing

**[2:28:09 – 2:28:15]** so let's walk through it again, it's the most important picture of the whole class I think

**[2:28:15 – 2:28:21]** the input is a set of vectors, each vector gets multiplied by three matrices

**[2:28:21 – 2:28:27]** wq gives you the query, wk gives you the key, wv gives you the value

**[2:28:27 – 2:28:34]** and then the queries and the keys should live in the same latent space

**[2:28:34 – 2:28:42]** you take, well, okay, set cosine similarity, I say dot product because of course nothing forces them to have like norm 1

**[2:28:42 – 2:28:46]** and we do not want to rescale by norm, it's too complicated

**[2:28:46 – 2:28:50]** so let me just stick to dot products

**[2:28:50 – 2:28:56]** we take the dot product between q and every k, we get these affinities

**[2:28:56 – 2:29:01]** then we rescale by the square root of, here it's called q, but it's square root of the dimension

**[2:29:01 – 2:29:06]** then we take the softmax and we get the actual weights, convex weights

**[2:29:06 – 2:29:13]** and we have this convex combination of the vectors v with these weights

**[2:29:13 – 2:29:27]** oh and notice by the way how we are actually looking on all input by every query

**[2:29:27 – 2:29:35]** so like every x in here is looking on every token from the input

**[2:29:35 – 2:29:41]** on every other x and on yourself as well, on x1 too

**[2:29:41 – 2:29:47]** sorry, I should probably say this explicitly here

**[2:29:47 – 2:29:52]** this is another very important property that makes transformers so cool

**[2:29:52 – 2:30:04]** and this property is if you have x1, x2, xk, blah, blah, blah, x capital L

**[2:30:04 – 2:30:11]** and let's assume that you want to like find out

**[2:30:11 – 2:30:19]** you want your x1 to influence to have some relation with xk over here

**[2:30:19 – 2:30:26]** so like this word in the input text has relevance to this word

**[2:30:26 – 2:30:33]** if you had a recurrent network this influence would have to go step by step

**[2:30:33 – 2:30:37]** through all of these intermediate vectors, right?

**[2:30:37 – 2:30:43]** so there is no path in the recurrent network that jumps over tokens

**[2:30:43 – 2:30:45]** you just go step by step

**[2:30:45 – 2:30:50]** and of course even if you have an OSTM with this memory cell

**[2:30:50 – 2:30:57]** with this constant error carousel, the highway that connects every point

**[2:30:57 – 2:31:03]** still a lot can happen as you go step by step through this sequence

**[2:31:03 – 2:31:07]** with the transformer you don't have to do that

**[2:31:07 – 2:31:12]** with the transformer you just jump in one step from here to here

**[2:31:12 – 2:31:16]** and you can actually jump to every token

**[2:31:16 – 2:31:18]** and you do jump to every token on every step

**[2:31:18 – 2:31:32]** so this is great this is like one step from every i to every j

**[2:31:32 – 2:31:39]** and this is a big plus and the cost of this is this quadratic complexity

**[2:31:39 – 2:31:47]** this is the big minus okay so a recurrent network has linear complexity

**[2:31:47 – 2:31:52]** as you add more elements to the sequence you just do more steps

**[2:31:52 – 2:32:00]** but each step has the same size has the same complexity so the current networks are linear in the input size

**[2:32:00 – 2:32:03]** transformers are quadratic in the input size it's a huge difference

**[2:32:03 – 2:32:12]** but they are then more free to notice the relations they don't care about how far it is from one topic to the other

**[2:32:12 – 2:32:21]** they just see the whole sequence at once on every layer on every step and that is great

**[2:32:21 – 2:32:28]** okay so yeah and this is the picture that i won't attempt to draw on the board

**[2:32:28 – 2:32:34]** sorry yeah please um may i ask a question sure sure uh i think i didn't really understand about the

**[2:32:34 – 2:32:47]** value space um like i understood that curie sorry i'm back i truly hope that the recording is not

**[2:32:47 – 2:32:55]** garbled after that um ob studio quit me sorry um anyway yeah please what was the question

**[2:32:55 – 2:33:06]** i'm trying to formulate it well i'm more or less understood about the key and curious part is that

**[2:33:06 – 2:33:16]** we they share the same space latent space and we uh are interested in finding the closest distance

**[2:33:16 – 2:33:26]** between them we rescale them etc but but the point i didn't really understand about the value value vector

**[2:33:26 – 2:33:36]** not that even vectors and also the space um how is it formed yeah okay i i i got the question actually

**[2:33:36 – 2:33:41]** yeah um problem is i don't have a good answer to that so i don't have a good intuition for why we

**[2:33:41 – 2:33:51]** need the values at all uh why can't it be just x that is a good yes yeah that that is a good question

**[2:33:51 – 2:33:58]** uh i guess like the superficial answer is that well i mean still every attention head is trying to

**[2:33:58 – 2:34:08]** highlight some aspect of the input and uh in terms of the values also we want to kind of um

**[2:34:08 – 2:34:21]** how to say this we want to uh highlight a specific like um um projection of of of the big vectors x

**[2:34:21 – 2:34:26]** and we want to simplify them to to highlight this thing that we are looking for with this specific

**[2:34:26 – 2:34:28]** these specific queries in these specific keys,

**[2:34:28 – 2:34:31]** but that's not really a satisfactory answer.

**[2:34:31 – 2:34:36]** I think the true answer is over here.

**[2:34:36 – 2:34:39]** And the true answer is if at the,

**[2:34:39 – 2:34:43]** so like, what does the value vector define it?

**[2:34:43 – 2:34:44]** What does the length of the value,

**[2:34:44 – 2:34:47]** where does the length of the value come in?

**[2:34:47 – 2:34:48]** What is its importance?

**[2:34:48 – 2:34:51]** The length of the value vector defines the length

**[2:34:51 – 2:34:54]** of the output, the size of the output, right?

**[2:34:54 – 2:34:59]** So your output is a combination of Vs.

**[2:34:59 – 2:35:02]** So the length of Z of the one is the same length

**[2:35:02 – 2:35:05]** as the length of V.

**[2:35:05 – 2:35:08]** And I guess it would be, it just wouldn't make sense.

**[2:35:08 – 2:35:12]** It would be too inefficient and too many weights, et cetera,

**[2:35:12 – 2:35:17]** to have many X sized Zs and then combine them together

**[2:35:18 – 2:35:22]** and compress them back down to a single X, okay?

**[2:35:22 – 2:35:27]** So I guess that's just an efficiency thing.

**[2:35:27 – 2:35:31]** So yeah, we could just use X as the document,

**[2:35:31 – 2:35:36]** but I suppose this would make this multi-head attention

**[2:35:36 – 2:35:39]** too difficult and we really want multi-head attention

**[2:35:39 – 2:35:40]** as I just explained.

**[2:35:40 – 2:35:45]** Does that make sense?

**[2:35:45 – 2:35:47]** - It's a bit confusing, but I don't think.

**[2:35:47 – 2:35:49]** - Okay, so let me go through this slide.

**[2:35:49 – 2:35:51]** Maybe it will be a bit less confusing.

**[2:35:51 – 2:35:56]** So we have actually several multiple

**[2:35:56 – 2:35:59]** of these attention heads, okay?

**[2:35:59 – 2:36:03]** We have head one, head two, head age.

**[2:36:03 – 2:36:06]** And when we have head one, head two, head age,

**[2:36:06 – 2:36:10]** every one of them gives us this set of Zs,

**[2:36:10 – 2:36:14]** the matrix Z, which is this Z

**[2:36:14 – 2:36:19]** that is in the boxed formula here, right?

**[2:36:19 – 2:36:22]** But now we have multiple such Zs

**[2:36:22 – 2:36:25]** and we need to combine them together.

**[2:36:25 – 2:36:30]** And after that, now the output of this step,

**[2:36:30 – 2:36:33]** now it has to match the input size.

**[2:36:33 – 2:36:35]** Well, it doesn't have to, but it does.

**[2:36:35 – 2:36:37]** It usually does in practice,

**[2:36:37 – 2:36:41]** just so that we can make another layer exactly like this

**[2:36:41 – 2:36:43]** and we can just copy the layers.

**[2:36:43 – 2:36:47]** So this matrix Z at the very end,

**[2:36:47 – 2:36:49]** at the top right of this,

**[2:36:49 – 2:36:52]** should have the exact same size as the input matrix X.

**[2:36:55 – 2:36:58]** But the intermediate representations,

**[2:36:58 – 2:36:59]** they are much bigger.

**[2:36:59 – 2:37:02]** So let me maybe just briefly draw it here

**[2:37:02 – 2:37:06]** since this is not that easy to understand.

**[2:37:06 – 2:37:10]** So we have this one matrix X,

**[2:37:10 – 2:37:14]** which is like a capital D times L.

**[2:37:14 – 2:37:16]** L is the number of vectors,

**[2:37:16 – 2:37:18]** D is the vector size.

**[2:37:18 – 2:37:28]** And this goes through attention head number one.

**[2:37:30 – 2:37:32]** Attention head number two, blah, blah, blah.

**[2:37:32 – 2:37:34]** Attention head number H.

**[2:37:34 – 2:37:38]** And this one gives you a matrix Z1.

**[2:37:38 – 2:37:41]** This one gives you a matrix Z2.

**[2:37:41 – 2:37:44]** This one gives you a matrix ZH.

**[2:37:44 – 2:37:54]** And these guys are, what's happening here?

**[2:37:54 – 2:38:01]** Recording in progress.

**[2:38:01 – 2:38:07]** Sorry, I don't know what's happening here today.

**[2:38:07 – 2:38:10]** Like all problems combined.

**[2:38:10 – 2:38:17]** Okay, so we have multiple, we have multiple attention heads.

**[2:38:17 – 2:38:24]** And every attention head gives you a new matrix Z, a different matrix Z.

**[2:38:24 – 2:38:26]** And now we need to merge them all together.

**[2:38:26 – 2:38:34]** So every one of these matrices is like a small d times L matrix.

**[2:38:34 – 2:38:43]** But then when you string them all together, Z1, then Z2, then ZH, you get a pretty big matrix.

**[2:38:43 – 2:38:49]** So if you just concatenate them like this, no, shouldn't, okay.

**[2:38:49 – 2:39:00]** So let's say that this is L times D, not D times L.

**[2:39:00 – 2:39:04]** Now I will concatenate properly, L times capital, yeah.

**[2:39:04 – 2:39:11]** So when I concatenate them together, I get the matrix, which is still L in terms of the rows,

**[2:39:11 – 2:39:20]** but now it's L times H times D, and H times D is probably bigger than capital D, and it's a lot.

**[2:39:20 – 2:39:27]** So what we do here in the transformer, we multiply it by another matrix of weights,

**[2:39:27 – 2:39:31]** so it's like just a feedforward layer, we mix up all the features again,

**[2:39:31 – 2:39:47]** and this feedforward layer gives us the matrix Z, so this is the matrix of size H times capital D, something like this.

**[2:39:47 – 2:40:04]** So my intuition for this is that we really, first of all, we need some variety in these Zs, we need more variety,

**[2:40:04 – 2:40:10]** not just linear combinations of the same vectors with different coefficients, but different projections of these vectors.

**[2:40:10 – 2:40:16]** This gives us more variety and more expressive power.

**[2:40:16 – 2:40:25]** And two, if we just had this small d equal to the big D, now this guy would be just infeasible to train, it would be just too big.

**[2:40:25 – 2:40:30]** So I guess this combination of two things that we wrote here.

**[2:40:30 – 2:40:36]** I understood your intuition. Thank you for drawing. It was clear.

**[2:40:36 – 2:40:50]** Thank you. All right. So what we have here is one attention head copied multiple times, several attention heads.

**[2:40:50 – 2:40:58]** They are all processed in parallel. And as the output, we get this matrix Z.

**[2:40:58 – 2:41:15]** And this, if we look at where we are now, we have explained, we have expressed exactly this one self-attention layer on the bottom left.

**[2:41:15 – 2:41:25]** This first self-attention layer from the first self-attention layer from the encoder.

**[2:41:25 – 2:41:33]** But notice that it's basically almost all that we need. So what's left?

**[2:41:33 – 2:41:38]** First, what's left is...

**[2:41:38 – 2:41:42]** Okay, so first let me go through the must self-attention in the decoder.

**[2:41:42 – 2:41:44]** And actually let's talk about the decoder.

**[2:41:44 – 2:41:50]** So we are completely done with the encoder part. That's it.

**[2:41:50 – 2:41:58]** Self-attention we've just described, then layer norm we know, feed forward just one matrix to mix up the weights we know,

**[2:41:58 – 2:42:01]** to mix up the representations we know, that's it.

**[2:42:01 – 2:42:07]** In the decoder there is more stuff to think about.

**[2:42:07 – 2:42:10]** So what is masked self-attention? What does it mean?

**[2:42:10 – 2:42:17]** Well, actually I don't even want to explain it in detail because that's a pure efficiency thing.

**[2:42:17 – 2:42:27]** So like when I draw a picture like this one where the decoder is only predicting the next token,

**[2:42:27 – 2:42:33]** there is actually masked self-attention is just self-attention. That's it.

**[2:42:33 – 2:42:38]** So we have the current state of the prefix. It's on the bottom right.

**[2:42:38 – 2:42:42]** We have the current state of the prefix. It goes into self-attention.

**[2:42:42 – 2:42:45]** It's just exactly the self-attention that we just described.

**[2:42:45 – 2:42:51]** Where the masks come in is that how do we train a language model?

**[2:42:51 – 2:42:57]** How do we train... Let me explain it briefly.

**[2:42:57 – 2:43:05]** How do we train a transformer decoder or the whole transformer with encoder and decoder?

**[2:43:05 – 2:43:10]** We have this output, right?

**[2:43:10 – 2:43:15]** So this is like the sentence that we need to produce.

**[2:43:15 – 2:43:30]** And in terms of the transformer decoder, this output sentence is like 1, 2, 3, 4, 5, 6, 7 actually different training samples.

**[2:43:30 – 2:43:47]** So the first training sample is you produce v from nothing and from the representation from the encoder.

**[2:43:47 – 2:43:54]** The second training sample is from the prefix v you are supposed to produce cat.

**[2:43:54 – 2:43:59]** The third from v cat you are supposed to produce set and so on, right?

**[2:43:59 – 2:44:05]** So it's like the decoder should be run seven times here.

**[2:44:05 – 2:44:10]** It produces six words and then it should produce like the stop talk and the talk and it's done.

**[2:44:10 – 2:44:20]** And you can do it formally, you can just do it as seven different training samples.

**[2:44:20 – 2:44:23]** But of course, it's inefficient.

**[2:44:23 – 2:44:27]** So in practice, what you do is you just you take this one sequence.

**[2:44:27 – 2:44:32]** You'll say that, OK, I'm supposed to produce.

**[2:44:32 – 2:44:39]** So I have this decoder in the transformer.

**[2:44:39 – 2:44:42]** I have all of the inputs available here.

**[2:44:42 – 2:44:44]** I have all of the outputs here.

**[2:44:44 – 2:44:49]** And then I'm supposed to have the here, cat here, blah, blah, blah.

**[2:44:49 – 2:44:54]** And this top token here.

**[2:44:54 – 2:44:56]** And this is where the masks are needed.

**[2:44:56 – 2:44:59]** Because of course, when I'm producing the word cat,

**[2:44:59 – 2:45:09]** this computational path is not supposed to look anywhere except to the word z.

**[2:45:09 – 2:45:15]** So I need to mask out all of the other tokens.

**[2:45:15 – 2:45:17]** Otherwise, it wouldn't be much of a problem.

**[2:45:17 – 2:45:20]** I just need to copy the input to the output.

**[2:45:20 – 2:45:22]** Of course, there would be nothing to do then.

**[2:45:22 – 2:45:35]** So the masked self-attention layer, what it's doing is it's blocking all of the tokens except it's called causality.

**[2:45:35 – 2:45:41]** It's called causal masks because it preserves causality.

**[2:45:41 – 2:45:50]** So token number T can only depend on positions of one zone to T minus one.

**[2:45:50 – 2:45:58]** And yeah, it's some work in terms of the programming of the implementation of the self-attention.

**[2:45:58 – 2:46:05]** So basically you need to like zero out the weights that are not supposed to be there.

**[2:46:05 – 2:46:20]** Like when the input has everything now, but when you are producing Z2, you are supposed to have this attention weight to be exactly zero and this attention weight to be exactly zero.

**[2:46:20 – 2:46:27]** And you are supposed to only look at the first token. That's what the masks do.

**[2:46:27 – 2:46:31]** So this is the mask self-attention part.

**[2:46:31 – 2:46:38]** And then the encoder-decoder attention part.

**[2:46:38 – 2:46:45]** How does this conditioning work?

**[2:46:45 – 2:47:04]** We are looking at the same self-attention layer, but now we also need to somehow have the Z inputs.

**[2:47:04 – 2:47:11]** The inputs that are produced by the encoder. Otherwise, what's the point of having an encoder?

**[2:47:11 – 2:47:18]** And it sounds like you would need to do something even more complicated.

**[2:47:18 – 2:47:23]** You would need to change something here because now there is this whole new input and stuff.

**[2:47:23 – 2:47:27]** Actually, no. Actually, it's very, very simple.

**[2:47:27 – 2:47:33]** The self-attention stays exactly the same. This picture stays exactly the same.

**[2:47:33 – 2:47:59]** There is only one difference. In encoder-decoder retention, your prefix, your X, the input from the decoder produces the queries.

**[2:47:59 – 2:48:05]** You multiply it by WQ and you get the matrix Q.

**[2:48:05 – 2:48:16]** And the keys and values are produced from the representations from the encoder.

**[2:48:16 – 2:48:27]** So W, A, W, V and you get the K and V matrices.

**[2:48:27 – 2:48:33]** No difference to this processing at all, but now the only difference is over here.

**[2:48:33 – 2:48:37]** We are not producing all three things from the same X.

**[2:48:37 – 2:48:44]** We are producing the Q thing from the X and the K and V thing from the condition.

**[2:48:44 – 2:48:50]** Notice that it doesn't break anything.

**[2:48:50 – 2:49:02]** So over here, I told you that this attention matrix is a square matrix of size L times L, N times N over here.

**[2:49:02 – 2:49:06]** Well, now it's not quadratic anymore.

**[2:49:06 – 2:49:09]** So now there is a different number of queries and keys.

**[2:49:09 – 2:49:14]** Obviously the length of the sequences will not be the same, but that's okay.

**[2:49:14 – 2:49:19]** We never assumed that we had the same number of keys and queries.

**[2:49:19 – 2:49:23]** For every query, we multiply it by all keys.

**[2:49:23 – 2:49:27]** So we get as many attention weights as there are keys.

**[2:49:27 – 2:49:32]** So the number of keys should match the number of values, naturally.

**[2:49:32 – 2:49:37]** Because then we add up values with these coefficients.

**[2:49:37 – 2:49:42]** But the queries can be completely different.

**[2:49:42 – 2:49:47]** And actually we will later when we discuss, for example, object detection with transformers.

**[2:49:47 – 2:49:53]** We will see that there are also queries and keys and values will be some very different things.

**[2:49:53 – 2:49:56]** They'll be produced from very different things.

**[2:49:56 – 2:50:03]** So it's a common idea in transformers to have queries come from one source and keys and values to come from another.

**[2:50:03 – 2:50:07]** And yeah, it dates back to the original transformer.

**[2:50:07 – 2:50:17]** In the original transformer decoder already, this is how we use the outputs of the encoder.

**[2:50:17 – 2:50:23]** Okay, so that's basically it about the architecture.

**[2:50:23 – 2:50:27]** That's it about this picture.

**[2:50:27 – 2:50:31]** Are there any questions at this point?

**[2:50:31 – 2:50:38]** Because this is, I think, the most important architecture in the world right now.

**[2:50:38 – 2:50:43]** So yeah, it's a lot to process.

**[2:50:43 – 2:50:48]** I don't expect you to internalize it right now, right from my words.

**[2:50:48 – 2:50:55]** But when you think it through once again, when you go through the pictures once more,

**[2:50:55 – 2:51:01]** and especially if you ever actually implement it, then I guess you will get an understanding.

**[2:51:01 – 2:51:04]** It's not that hard. It's just pretty abstract.

**[2:51:04 – 2:51:09]** So there is nothing tangible about what is a value vector.

**[2:51:09 – 2:51:11]** It's just a projection.

**[2:51:11 – 2:51:16]** It's just a good projection that we train for the input vectors.

**[2:51:16 – 2:51:18]** And what are these input vectors?

**[2:51:18 – 2:51:21]** Well, they are some abstract representations of the tokens.

**[2:51:21 – 2:51:26]** So there is not much intuition that I can give beyond what I already tried.

**[2:51:26 – 2:51:38]** But actually, surprisingly enough, the actual attention heads that after training will often do some very understandable,

**[2:51:38 – 2:51:45]** very interpretable, very intuitive things. Maybe if we have time, I will show you some examples later about this.

**[2:51:45 – 2:51:54]** Not too late. And there are, I guess, two more things to talk about.

**[2:51:54 – 2:52:04]** So first, let me maybe show you an example. To be honest, I have only some pretty trivial examples here.

**[2:52:04 – 2:52:11]** Pretty trivial examples. I have this... Okay, let's not go through the code.

**[2:52:11 – 2:52:17]** We have practical sessions for that. But I have this one layer and one self-attention head.

**[2:52:17 – 2:52:30]** And what it's supposed to do is it's supposed to output the matching key, so to speak, for the input.

**[2:52:30 – 2:52:39]** And if you look at the attention matrix, you see that it does...

**[2:52:39 – 2:52:47]** For this attention head, it does look in the correct spot. Basically, that's it here.

**[2:52:47 – 2:52:54]** And here is another kind of abstract example.

**[2:52:54 – 2:53:00]** It's an example to illustrate that the attention matrix,

**[2:53:00 – 2:53:06]** the matrix of attention weight doesn't have to choose a token.

**[2:53:06 – 2:53:13]** So if you look at something like this or some sample matrices like this one,

**[2:53:13 – 2:53:20]** they quite often look like a permutation matrix, right?

**[2:53:20 – 2:53:24]** They quite often look like, well, for every input we match it to some output,

**[2:53:24 – 2:53:31]** to some other input in this case, and we encode their mutual relationship right now,

**[2:53:31 – 2:53:37]** like between token number i and token number j.

**[2:53:37 – 2:53:39]** Well, it doesn't have to be this way.

**[2:53:39 – 2:53:44]** There can be more complicated sets of attention weights,

**[2:53:44 – 2:53:48]** like you can have, for example, an orientation matrix that looks like this,

**[2:53:48 – 2:53:58]** where these tokens, these queries, look at all the tokens.

**[2:53:58 – 2:54:01]** So in this example, all tokens are split into groups.

**[2:54:01 – 2:54:08]** There are four groups. They go one by one, like three tokens,

**[2:54:08 – 2:54:14]** group of three tokens, group of three tokens, then group of one token, and again group of three tokens.

**[2:54:14 – 2:54:19]** And they are supposed to look at each other uniformly.

**[2:54:19 – 2:54:22]** So that can also happen, right?

**[2:54:22 – 2:54:31]** You can have this widely distributed attention where one token just attends to all of the tokens, for example.

**[2:54:31 – 2:54:36]** We'll see probably examples of this.

**[2:54:36 – 2:54:41]** Okay, and two more things that I need to talk about.

**[2:54:41 – 2:54:48]** So first, maybe one word on tokenization.

**[2:54:48 – 2:54:56]** It's not really our subject because we are talking about computer vision and in images it will be quite different.

**[2:54:56 – 2:55:08]** But I just wanted to mention because it's a nice connection to completely different areas of computer science to coding theory and Huffman coding and stuff.

**[2:55:08 – 2:55:12]** But where do you get your dictionary from?

**[2:55:12 – 2:55:25]** It's a pretty interesting question because when I explain it to you intuitively, it makes sense to say that just a token is a word in text.

**[2:55:25 – 2:55:30]** But in reality, you can't have tokens to be equal to words because there are too many words.

**[2:55:30 – 2:55:43]** Because in a language, I mean, you can't just lemmatize everything and have all of your words lose all the grammar that would lose a lot of information.

**[2:55:43 – 2:55:48]** So different grammatical forms have to be separate words. That's one.

**[2:55:48 – 2:55:58]** And two, in reality, there are typos. And if you add typos, so again, you are not allowed to just drop everything that's not in the vocabulary

**[2:55:58 – 2:56:06]** because then many texts would not make sense and you would lose, again, a lot of information.

**[2:56:06 – 2:56:12]** But if you add all of the words with typos there, oh, my God, the dictionary will be huge.

**[2:56:12 – 2:56:15]** You will have millions of words in the English language.

**[2:56:15 – 2:56:21]** So we need something smaller. We need a smaller vocabulary.

**[2:56:21 – 2:56:26]** And, of course, we could just start with characters.

**[2:56:26 – 2:56:38]** So you could have, I mean, you could view text as not a sequence of words, but a sequence of characters.

**[2:56:38 – 2:56:45]** This is, for most languages, this is a natural way to partition the text, right?

**[2:56:45 – 2:56:49]** Also, it's a sequence of characters.

**[2:56:49 – 2:56:55]** Now, this, on the other hand, is too fine granularity, right?

**[2:56:55 – 2:57:02]** So, yeah, characters, there are a few characters, at most a couple hundred.

**[2:57:02 – 2:57:09]** Even if you count all the punctuation marks, capital letters, etc., etc., like 100, 200 at most.

**[2:57:09 – 2:57:22]** And, of course, you can train, you can have a dictionary of several hundred vectors,

**[2:57:22 – 2:57:25]** your embedding matrix of several hundred vectors.

**[2:57:25 – 2:57:33]** But now it's too little because now it means that your sequences get too long.

**[2:57:33 – 2:57:43]** So, again, remember that, for example, now a practical limit on the context size is something like a million tokens.

**[2:57:43 – 2:57:51]** And there is a big difference if it's a million words or a million letters, right?

**[2:57:51 – 2:57:55]** And, of course, you would want to be closer to a million words than a million letters.

**[2:57:55 – 2:57:59]** So how do you go in between?

**[2:57:59 – 2:58:05]** How do you choose which tokens to use, which sequences of characters to assign tokens?

**[2:58:05 – 2:58:10]** Well, it turns out there is a pretty beautiful algorithm for that.

**[2:58:10 – 2:58:14]** It's called BP, byte-pair encoding.

**[2:58:14 – 2:58:18]** And it's commonly used throughout machine learning.

**[2:58:18 – 2:58:21]** And interestingly, it has nothing to do with learning.

**[2:58:21 – 2:58:28]** It's all just Huffman coding from Shannon's information theory.

**[2:58:28 – 2:58:32]** So, how does it work?

**[2:58:32 – 2:58:39]** Well, suppose you have some kind of dataset where you have these words.

**[2:58:39 – 2:58:47]** I specifically chose words that have many similar letters and substrings.

**[2:58:47 – 2:58:50]** And here are the letters that appear in these words.

**[2:58:50 – 2:58:53]** And let's assume that these are the frequencies of the words.

**[2:58:53 – 2:58:55]** So, these are the frequencies of the letters.

**[2:58:55 – 2:59:01]** Now, suppose that I can add one more token.

**[2:59:01 – 2:59:02]** What do I do?

**[2:59:02 – 2:59:08]** Well, adding one more token means that if I start with characters,

**[2:59:08 – 2:59:13]** I can now take a pair of characters and I can call this pair a single new token.

**[2:59:13 – 2:59:17]** So, which pair do I choose?

**[2:59:17 – 2:59:20]** Well, let me list all of the pairs that actually appear.

**[2:59:20 – 2:59:24]** And let's just choose the one that appears the most.

**[2:59:24 – 2:59:30]** So, in this case, obviously, the @ appears everywhere, almost everywhere.

**[2:59:30 – 2:59:33]** So, it's very, very common, has a high frequency.

**[2:59:33 – 2:59:41]** So, let's call @ a new token, a new symbol.

**[2:59:41 – 2:59:43]** Let's call it capital Z, whatever.

**[2:59:43 – 2:59:47]** And now my words look like this, right?

**[2:59:47 – 2:59:50]** So, I replaced every @ by this Z.

**[2:59:50 – 2:59:58]** And, yeah, of course, I cannot delete A and T from the vocabulary

**[2:59:58 – 3:00:02]** because T can occur without A, for example, right?

**[3:00:02 – 3:00:08]** But still, I have reduced the length of my words.

**[3:00:08 – 3:00:11]** I have added one new token to the dictionary,

**[3:00:11 – 3:00:14]** and I have done it in the optimal way, basically.

**[3:00:14 – 3:00:17]** And then I just repeat this.

**[3:00:17 – 3:00:22]** So, now I have this new vocabulary of tokens.

**[3:00:22 – 3:00:26]** They have these new counts.

**[3:00:26 – 3:00:29]** I needed to update the counts of A and T.

**[3:00:29 – 3:00:32]** Now that's different.

**[3:00:32 – 3:00:34]** So, I have this new set of pairs.

**[3:00:34 – 3:00:36]** Also, I don't need to update the whole thing,

**[3:00:36 – 3:00:43]** but I need to update the pairs where there was an A or a T.

**[3:00:43 – 3:00:46]** And that's how we work, right?

**[3:00:46 – 3:00:50]** And then we can choose another pair of tokens

**[3:00:50 – 3:00:53]** and replace those by capital Y and so on and so forth.

**[3:00:53 – 3:00:56]** So, very simple algorithm, very straightforward.

**[3:00:56 – 3:01:03]** And the beautiful part is that you can stop it at any time.

**[3:01:03 – 3:01:09]** Yeah, absolutely. It's from that part of computer science, I agree.

**[3:01:09 – 3:01:13]** And you can stop it at any time.

**[3:01:13 – 3:01:19]** You can say, okay, so let's say I have a capacity for a vocabulary of size 100,000.

**[3:01:19 – 3:01:24]** Well, so that's way too much to have just characters

**[3:01:24 – 3:01:26]** and way too little to have complete words.

**[3:01:26 – 3:01:31]** So I just run this until I reach, I add tokens one by one,

**[3:01:31 – 3:01:35]** so I can just reach exactly 100,000 and stop.

**[3:01:35 – 3:01:38]** And if you do it, you will see that, for example, first,

**[3:01:38 – 3:01:43]** it will find common, frequent parts of words like -ed

**[3:01:43 – 3:01:46]** because it's at the end of every verb in past tense,

**[3:01:46 – 3:01:52]** or -tion because it's at the end of many nouns and so on and so forth.

**[3:01:52 – 3:01:55]** And then, of course, common words will be single tokens,

**[3:01:55 – 3:01:58]** uncommon words will be multiple tokens, and that's okay.

**[3:01:58 – 3:02:03]** So that's how tokenization works.

**[3:02:03 – 3:02:09]** And one more very interesting remark, this will be the last that I have time to say today,

**[3:02:09 – 3:02:18]** one more very interesting remark about transformers is that because they are so cool,

**[3:02:18 – 3:02:26]** because they have this wonderful ability to go from any token to any token in one step,

**[3:02:26 – 3:02:30]** this is their biggest strength.

**[3:02:30 – 3:02:35]** But it comes with a funny drawback, with a funny defect.

**[3:02:35 – 3:02:44]** Transformers lose word order, so in the recurrent network there is a very meaningful sense

**[3:02:44 – 3:02:48]** in which there are adjacent tokens and tokens that are far away,

**[3:02:48 – 3:02:53]** because between adjacent tokens you go in one step, if they are far away you go in many steps.

**[3:02:53 – 3:03:00]** Very natural, you don't need to remind the recurrent network about the word order.

**[3:03:00 – 3:03:04]** And transformers, well, it's just a matrix, right?

**[3:03:04 – 3:03:08]** If you look at this matrix of attention weights,

**[3:03:08 – 3:03:15]** it doesn't, like, just a generic matrix doesn't care if these rows are adjacent or these rows are far apart.

**[3:03:15 – 3:03:20]** There is nothing that changes because of this.

**[3:03:20 – 3:03:27]** So transformers don't care about word order, and that's a bad thing.

**[3:03:27 – 3:03:30]** We do want to keep the order, right?

**[3:03:30 – 3:03:40]** So what we actually do in practice is we add to the embeddings of the tokens,

**[3:03:40 – 3:03:45]** we add special vectors called positional encodings,

**[3:03:45 – 3:03:52]** whose only job is to encode where exactly this token is in the sequence.

**[3:03:52 – 3:03:59]** And it's kind of a topic in itself, which I don't want to go into.

**[3:03:59 – 3:04:05]** Let me just briefly hint at the main idea.

**[3:04:05 – 3:04:15]** The main idea is this: you could have an embedding that just has one hot representation,

**[3:04:15 – 3:04:19]** that here is position number one, number two, number three, number four.

**[3:04:19 – 3:04:27]** But what you actually want is you want these positional encodings to have some kind of arithmetic on them.

**[3:04:27 – 3:04:38]** So you want your positional encodings to, if you have a vector that represents position one,

**[3:04:38 – 3:04:43]** so let me maybe briefly write it here.

**[3:04:43 – 3:04:53]** If you have a vector that represents position one, e1, position two, e2 and so on,

**[3:04:53 – 3:05:06]** you want them to capture these differences, the distances between tokens.

**[3:05:06 – 3:05:16]** So you want like ei minus ej as a vector to be somehow similar to ei plus k minus ej plus k.

**[3:05:16 – 3:05:29]** So you want like if the tokens are three, if two positions are three tokens apart, you want the differences between their encodings, position encodings to be the same across the whole sequence.

**[3:05:29 – 3:05:52]** Right. And in the original transformer, they did it with this kind of approach. They did it with this, well, basically positional. What's the English word? Positional counting system. I forget.

**[3:05:52 – 3:06:02]** Like there are binary numbers, there are decimal numbers. What's the general term? So let's look at how binary numbers operate.

**[3:06:02 – 3:06:10]** you look at the binary numbers, you see that these are just binary numbers from 0 to 15,

**[3:06:10 – 3:06:17]** rote in sequence, right? So like 1 0 1 2 3 blah blah blah 15 16. And if you look at what happens

**[3:06:17 – 3:06:23]** with the actual digits, you see that the last digit just oscillates, right? 0 1 0 1. The next

**[3:06:23 – 3:06:32]** digit oscillates with twice the period 0011 0011 and so on. Now we have four zeros and four ones,

**[3:06:32 – 3:06:39]** four zeros, four ones, eight zeros, eight ones and so on. That's how binaries work. And you can do it,

**[3:06:40 – 3:06:48]** you can do like a soft version of this. You can have like sine waves in different positions of the

**[3:06:48 – 3:06:56]** encoding and you can start with sine waves that oscillate a lot with high frequency and then just

**[3:06:56 – 3:07:03]** reduce the frequency. And this will be like this positional system for counting that will give you the

**[3:07:03 – 3:07:13]** necessary properties. So this was the original approach to positional encodings and the current

**[3:07:13 – 3:07:23]** approach, I think the one they mostly use today, is called rope, rotary positional encodings. And

**[3:07:23 – 3:07:30]** rotary means that something is rotating, there is some kind of circular motion. And basically in rope

**[3:07:30 – 3:07:45]** what you do is this: you take your vector x and instead of considering its components one by one,

**[3:07:45 – 3:07:56]** you consider them in two by two. So you break x into pieces of two numbers, like two-dimensional

**[3:07:56 – 3:08:06]** vectors. Okay, so this will be x1, x2, this will be x11, x12, this will be x21, x22, and so on.

**[3:08:07 – 3:08:16]** And every two-dimensional part you can now rotate by various angles. So you cannot rotate a single

**[3:08:16 – 3:08:21]** number, it doesn't make sense, but a vector of two numbers, that's a vector on a plane, you can rotate it.

**[3:08:21 – 3:08:32]** So what the rotary encodings do, what these embeddings actually do, is they take this kind of small x

**[3:08:35 – 3:08:46]** on a plane and they multiply it by rotation matrices like this. I always forget where the minus sign is,

**[3:08:46 – 3:08:56]** maybe it's over here. And the positions are encoded as coefficients to these rotations.

**[3:08:56 – 3:09:07]** Oh sorry, let me write it again. I should have done this. Cosine k theta, sine k theta, minus sine k theta,

**[3:09:07 – 3:09:16]** cosine k theta, right? So there is like this basic angle theta and you rotate by multiples of theta,

**[3:09:16 – 3:09:23]** which gives you this perfect arithmetic by default. Because if you take a vector and you rotate it by

**[3:09:23 – 3:09:32]** k theta and then you rotate it by another L theta, then it's the same as rotating it by k plus L theta, right?

**[3:09:32 – 3:09:39]** Just obvious. So this also gives you this nice arithmetic and this kind of positional

**[3:09:39 – 3:09:46]** encodings have better properties, it seems. So I have illustrations for you here as well.

**[3:09:48 – 3:09:53]** This is the sinusoidal positional encoding and this is the the picture that I cannot draw on the board,

**[3:09:54 – 3:10:01]** but this is exactly how like this dot product between the two vectors here depends only on the

**[3:10:01 – 3:10:08]** distance between them on the offset i minus j and that is the property that we want. And rotary

**[3:10:08 – 3:10:18]** positional encodings, well here is an illustration for how they work and this is the same kind of matrix

**[3:10:18 – 3:10:24]** again showing that you have this diagonal structure which means that along each diagonal the distance

**[3:10:24 – 3:10:36]** between positions is the same and well you have the same dot product between the positional encodings.

**[3:10:36 – 3:10:43]** And I also have this illustration for why the square root of d is necessary but it's just

**[3:10:43 – 3:10:53]** a practical representation of the fact that if you don't scale you get closer and closer to one

**[3:10:53 – 3:11:05]** hot representations. You lose the entropy after the softmax. All right so let me stop here. We've

**[3:11:05 – 3:11:11]** discussed attention and self-attention and the transformer and I'm happy that I got to the end

**[3:11:11 – 3:11:27]** of the transformer architecture. Any questions? Okay then. Then thank you very much. I will try to

**[3:11:29 – 3:11:38]** I will try to produce a unified video of today's lecture. I'm pretty sure it wasn't corrupted

**[3:11:40 – 3:11:47]** completely. At some point just the BS Studio quit unexpectedly but I'm sure it's not corrupted

**[3:11:47 – 3:11:52]** completely. I'm not sure if I will be able to actually join them together. Sometimes it doesn't

**[3:11:52 – 3:12:04]** work but in any case I will make it available somehow. So thanks a lot and see you on Friday obviously

**[3:12:04 – 3:12:10]** but when the next lecture will be, we haven't yet decided. We'll talk it over. Okay see you on Friday

**[3:12:10 – 3:12:13]** and on Friday I will listen to your presentations. Bye-bye.

## Full text

Good morning, everyone. Welcome to our next class. Today is lecture day and we will discuss transformers. This is probably the single most important lecture in our class, but before we get to transformers naturally, we need to finish what we started yesterday on recurrent neural networks, then we need to discuss attention mechanisms, and then from recurrent attention, we will get to self-attention and therefore transformers. They will indeed transform the entire field of deep learning as they did 10 years ago. Yesterday we stopped at the main problems of recurrent networks. Actually, I didn't make this point yesterday, so let me make it now. The main problems of recurrent networks are exactly the same problems that you have in deep networks in general, in networks with a lot of layers like the ones we've already seen in the convolutional side of things. So, the problem is that the signal gets saturated, right? The signal, oops, sorry, looks like my, my waveform is not working, no, okay. So, the problem with deep neural networks was that as you go through the layers, and especially as gradients go through the layers, right, you start losing signal when some of the layers get saturated. So, when a layer doesn't want to train anymore, its derivatives become zero, you multiply by that zero and nothing below it trains. Well, guess what? A recurrent neural network is in a way a very, very deep network, right? So, it has, usually you think of its input as a single thing, right? But what's actually going on is when you process the input, the activations go through as many layers, actually real physical layers, neural layers, right, with trainable weights and everything, as many layers as elements in your sequence. So, any recurrent network is, by default, a very deep network. And when people talk about deep recurrent networks, what they usually mean is like several layers of processing for the recurrences. So, there are constructions like this, like this. This would be called the three-layered recurrent network, right? But in actuality, if you compare it with, or if you look at it on the level of the computational graph, any recurrent network, even one with only one level of cells, is actually a very deep network. It's as deep as the input sequence, which is probably very deep, right? So, the problem is exactly the same. As you go back with the gradients, or as you go forward with activations, strange stuff begins to happen, because you keep multiplying by this same matrix of weights, more or less. And, of course, in recurrent networks it's a little bit different, because now you have the same weight matrix for every cell, right? So, they all share the same W, and this gives us even more problems. But the vanishing gradients problem is more or less the same. So, if your W has a spectral radius under 1, then as you go from left to right with the gradients, you keep multiplying by smaller and smaller. You keep multiplying by this number which is less than 1, more or less, and your vectors, your gradients shrink, and basically they shrink to 0. And that's a bad thing. But the additional problem here is that you can notice it if you look inside your network, but from the behavior, from the graph of the loss function, you will never notice it because it's not like exploding gradients. When gradients explode, it means that just everything is a huge mess. Nothing works, right? When gradients explode, you start seeing things like numerical overflows in your code, and it's completely obvious that everything has broken down. Not so with vanishing gradients, right? So when vanishing gradients become smaller when you go from right to left, it doesn't mean that W stops training, W still trains. Why? Because it still participates in the last cells of the network, right? So even if your gradients become basically exactly zero after the second step on their way back from the loss function, even if that happens, W will still train. It will still look fine at first glance because it will still participate in here. It will still give you some signal. The gradients with respect to the weights will not be zero. You will not notice it by looking at the gradients with respect to W. Everything will be fine, but your network will make its decisions based only on the last two elements of the sequence. It will not be able to have long-term memory for the rest of the sequence. So the actual problem with vanishing gradients is like this guy's problem from this classic Nolan movie. The networks cannot have long-term memory. They cannot have this x1 influence the output at step t. So what do we do? Well, we do exactly the same thing that we already learned how to do with resnets. We add something like residual connections. And in fact, it was recurrent networks that pioneered this idea because recurrent networks simply don't work at all without this idea. And so it actually originated in the 1990s in Juergen Schmidhuber's group. And these constructions have been known for a long time, but only in like 2015 they were actually applied to deep neural networks because we didn't have so deep neural networks before. And the idea is the same. You need to have like this way for gradients to flow around multiplying them by weight matrices. So you need to have some, Schmidt-Kober sometimes called it highways, you need to have a highway for the gradient to go through. And yes, of course you will change what's happening on the highway, but not by multiplying directly by a weight matrix that could go to zero. And I will explain to you this very famous and still very important construction, LSTM, which stands for long short-term memory, kind of a strange name, but there we go. And the basic idea of LSTMs is that, yes, you do have this highway for memory to flow. So I will be drawing here one cell of the LSTM. So we are in here, and our inputs are the hidden state and the current x, and our output should be the next hidden state. So in LSTMs, the hidden state is artificially split in two. So, of course, formally it's just a single vector, but we treat two halves of this vector very differently. So I will draw them as two different vectors. One half is like this long-term memory. This is the part that will stay on the highway. This is the highway, actually. So it will stay not unchanged. We will write to memory, read from memory, etc. But this is the part that we don't want to multiply by weight matrices. This is, in terms that we already know, this is the equivalent of this path around the layers. And then there will be also, let's call it h. ht is just a regular "hidden state". It will participate in everything that happens in the LSTM. And you will see how it gets used. And actually as the output we will need to produce this vector for the next step. So C is kind of this long-term memory. And this is the correct intuition. This is like a memory cell where you write stuff, where you read stuff from. And the whole LSTM is devoted to operations with this long-term memory. And then of course we have x. So we have like x, t over here. This will also be an input for us. And what's happening inside? Well, LSTM consists of gates. This is also a pretty important concept because in many modern architectures you will see some kind of gating mechanisms. You will see some kind of gates like this. Here I will draw gates like this. Let me show it separately. There will be a gate, for example, with two inputs. I will put matrices over here. These are two inputs, x and y. And then the gate itself will look like this. And there will be a function over here, the activation function. And so the output of this gate will be like f of a times x plus b times y. And probably plus a bias term, but I will not draw the bias terms explicitly. So this is basically this one linear cell, right? So two inputs, every input gets multiplied by a matrix. This will be weight matrices. Then we add them together and we push them through an activation function. But here they will be used in many different and creative ways, these kinds of gates. So let's begin. Let's see. Our first gate will be over here. I will call it the input gate. The input gate, right? Okay, let me draw it and then I will explain what's going on here. No, sorry. Let's start with the forget gate. This will be the forget gate. Just a cleaner picture this way. So it receives as input H with the weight matrix WHF, right? H for hidden, F for forget. It also receives as input X with the weight matrix WXF. Then you go here. And then what happens is I multiply CT by the output of this gate, like component-wise. So its output is a vector, let me call it FT, and I multiply CT by FT. So let's unpack what's happening here and then the rest of the gates will work in about the same way. So what is happening here? We have this kind of linear thing that just combines H and X with some coefficients, whatever. And importantly, we pass it through a logistic sigma. We pass it through the sigma function, this function that goes from 0 to 1. And that basically converts any score to a probability. So as a result, we have this vector full of values from 0 to 1. So it's like it goes from 0 to 1 and there are several values from 0 to 1. And actually 0 and 1 not included. And then we multiply it component-wise by our memory cell. So what's going on? What's the intuition? The intuition is we want to be able to erase something from memory. How do you erase something from memory? Well, you multiply it by 0. So basically the forget gate, if the output is close to 1, it means keep it, retain the cell in memory. If the output is close to 0, that means don't keep it, erase it. And that's mostly how gates work. So in modern architectures like mixtures of experts, I don't think we all will have time to discuss those, but very often you will see some kind of a gating mechanism. And usually it means that you have some small part of your network, in this case just this linear cell, producing a control vector that will control what's happening with other stuff inside the network. So this is not like data really. This is not something that I want to treat as numbers. And of course it's still numbers, right? It's all numbers inside the neural network. But the meaning of the vector f here at the output of this gate is which memory cells to erase. It's not some additional number that I want to multiply because I care about the multiplication result. That's the point of gating here. You cannot do real logic gates because then gradients would not fall through. Logic gates are piecewise constant and you cannot train through them. But you can do some kind of continuous approximation to these kinds of gates. And here it's basically about erasing from it. And now that we have one gate clear, the rest basically follows. So next you have, let's say you have the candidate cell state. Candidate cell state. Okay, probably we'll need more space and that will come later. Candidate cell state, which will produce the new numbers to write down to memory. So this is like C prime tip. This is something that we may want to write to memory. Where do we produce them from? Well, of course, from the same inputs. So we have W, H, C, another matrix of weights, right? And we have W, X, C, another matrix of weights. Notice that for controlling gates, for gates like the forget gate, it's important that I have the sigmoid function at the end. Because I do want numbers from zero to one, I actually want them to be saturated. I want them to be either close to zero or close to one. That's the whole point. Here, not so much, right? So here, I just want to produce new numbers to store in memory. So here, this sigma cannot be exchanged for something else. It's important that it's a sigmoid. But this hyperbolic tangent, I'm just copying it from classical LSTM construction, but this is not written, set in stone. This can be modified. And so now we have C' and the question is which part of this vector I want to write to memory. And guess what? There is a gate to control that. So we have another gate which is called the input gate. Here it is. And now this one is a control gate with a sigma. And what it does is it decides which of this candidate cell, which parts of C' I want to write into memory. So I multiply C' component-wise by the output of the input gate. And then the result I write into memory. What does it mean to write something into memory that's just addition. Okay? That's it. And of course I need to do it from inputs. W-H-I-W-X-I. I need one more gate. Right. So at this point we are able to erase something from memory. And we are able to write something back to memory. So again, this plus is not really a plus. I mean, the LSTM usually does not learn to actually add stuff. It's not about this addition. It's about writing to memory. So the main mechanism is sometimes I want to erase something from memory. So I multiply by something very close to zero. I get a zero in that position of CT. And now when I add something there, it means I'm just writing to this cell. And the only remaining thing is to define this H for the next step. And here I will actually look it up because the rest is very logical. And here with me, yeah, it's a hyperbolic tangent. So now H is actually produced from the long-term memory. So it's basically kind of a copy of long-term memory. But for some reason, which I cannot really explain, it goes through a hyperbolic tangent over here. And then it's a part, and then we read the result from, and then we read it from long-term memory. But what does it mean to read? Again, it means that there will be a gate controlling which part of CT I want to write to HT. So there will be another gate, let's call it the output gate, or output, yeah, I think output. The output gate, again with the sigmoid, and you have a vector here. And this vector will decide what to read from memory for the next H. And again, WHO and WXO. That's it, that's the LSTM. So the LSTM cell is everything that's inside here, right? So this is the LSTM cell. And it looks complicated. It's not really complicated. Meaningfully, I can explain to you the intuition behind everything here. Maybe except that hyperbolic tangent. I have no idea why it's exactly that. But I can explain to you how things flow inside an LSTM. And it makes sense, right? So the beauty of this construction is that it makes perfect sense. It's like a program for memory manipulation procedures, right? There is this memory, you can delete from it, you can write to it, that's it. And also you need to decide what to write to it. So hence the candidate cell state. That's how it works. And it actually is an extremely successful construction. It's still relevant now, even though it was constructed, I think 1995 was their first paper. And by the year 2000, they already had exactly this construction. The first construction was a bit simpler. But by the year 2000 in Schmidt-Fober's group, they already had exactly this. And ever since, it just works. And when you build a recurrent network today, you will actually use LSTMs, surprisingly enough. So I don't want to spend too much time on recurrent networks. So let me be quick about what's coming next here. And the LSTM is the most important recurrent construction ever. And again, its main meaning is that it provides you with this straight line, with this highway through which the gradients will flow without any interruptions, or better to say, only with interruptions that we intend. So of course, they will be interrupted if I erase something from memory. Of course, this will stop the gradients, but that's how I want it to. But the LSTM has a big cost, and the cost is it has a lot of weights. So if you look at all of these matrices, you will see that there are a lot of matrices. In the construction that I drew here, there are eight weight matrices, and they are basically, so if like x is r d prime, and I think I said that this is d, so h and c are of length d, then like half of these matrices are like d times d matrices, and half of these matrices are d times d prime matrices. And of course you want your memory to be large. You cannot have a meaningful LSTM with like a cell of size 2. So in reality, like in practice, d is something like at least 256, maybe in small cases something like 64, in large cases something like 1000. And d prime is what it is, that's your x, probably some embedding of x, some representation, but also probably on the same kind of size level. So these are big weight matrices and for a long time it was very difficult to train LSTMs. Everybody knew that they are cool and in toy examples they were actually delivering very good results, but nobody could really train a huge LSTM. And I think it only began to be possible in like 2015 or so. But ever since, big LSTMs are indeed what people use for big recurrent networks. And for example, I think, to take an example you may have heard about, I think AlphaStar. The StarCraft playing network. It was actually a recurrent network and AlphaStar used LSTMs. Which sounds pretty strange, right? Like, how does it happen that this basically first... Okay, very smart people did it. It makes a lot of sense. But this is like the first successful attempt to build an architecture for this kind of memory manipulation stuff. And it was 25 years ago and it still stands and nobody has done better. That sounds unbelievable, right? And indeed, of course, there have been lots of attempts to do something better. So let me not draw anything new here, anything on the board. I will just walk through the slides to save time. Okay, so this is the LSTM cell that I have been drawing just now. For gate gate, input gate, candidate cell state, output gate. These are the matrices, the formulas, whatever. Yeah, so completely in its modern form, it already appeared in 2000, in the year 2000. And there have been some modifications. There have been modifications like let's add the pip holes. So one problem of the LSTM is that once you have fixed your age, all of these gates do not have access to memory. So it's like you are erasing from memory, but you cannot look inside the memory to see what you are erasing, which is pretty strange. And people added more inputs from C over here, which means even more weight matrices. And at some point, people tried to maybe lose a few of these matrices. Maybe you can do without some of the gates. Maybe you can tweak the LSTM a little bit. And it turned out that, yes, for every, like this, there was this famous paper called LSTM is Rich Space Odyssey. And basically it said, yeah, on our two examples where we could test a lot of LSTM variations, you can actually remove a whole gate and nothing much changes. And then there were even better attempts. So let us try to achieve the same goal, the goal of having memory that goes through this free highway of gradient flow. And let's keep it that way, but let's tweak the structure of the recurrent cell so that it will be more efficient. And people have been successful. So, for example, like the second very famous recurrent unit is called the GRU, Gated Recurrent Unit. Back in 2014, it was developed. And if you look at it, it's very similar to the LSTM, but it has much less, much fewer matrices. So let me just walk you through here without drawing it separately. So it still has, of course, the candidate cell state, but now it doesn't distinguish between C and H. So you only have one hidden state. And instead of updating it separately with erasing stuff and writing stuff, you do it all at once with the update gate. So basically the update gate, again, it's a control gate with a sigma at the output and it gives you numbers between zero and one. But now they are like coefficients of a convex combination. So if you look here on the right, you multiply H, the current memory state, by U. And then you add this H prime, the candidate that you proposed, times one minus U, right? So it sounds like it makes a lot of sense, right? Why do we want to erase from memory, to write something there? Why do we want to add something to memory? Because we've already erased this cell. And as I said, LSTM is not about actual addition, it's about erasing and writing back to memory. So it makes a lot of sense to combine it into one gate. And that saves like two weight matrices, right? And instead of the output gate, we have the reset gate, which does basically the same thing, only in the same cell and not in the cell as that before. It just looks at the memory and chooses which part of it should go into the candidate cell state. So GRUs look great, looks like they do exactly the same as LSTMs, only more efficiently because now you have only 6 weight matrices instead of 8 or instead of 11. If you count pip holes, you don't need pip holes now. So it's more efficient, should be better, and so on and so forth. Indeed, in like 2015, 2016, if you look in, for example, papers on natural language processing, I was actually working in the field at that point, and if you look at the papers on NLP back in 2015, they all used GRUs. They all switched to GRUs, and that was a big thing, etc., etc. And then, for some reason, which I cannot explain to you theoretically, the whole field switched back to LSTMs. So, I mentioned AlphaStar, AlphaStar, I don't remember the year, but of course, it's much later, it's like 2020 or something. And if you have a recurrent network now, probably it's more likely to be an LSTM than a GRU. Somehow, Schmidt-Huber's construction is better, and I'm sure the actual decision-making here is just empirical. You're just saying, "Oh, okay, we've tried LSTMs, we've tried GRUs, so LSTMs work better, we can bear the costs, so to speak, let's use LSTMs." But why they are better, I have no idea. What's so special about the LSTM architecture, I don't know, but it's really interesting and it's really beautiful that it stands for so long. And remember, all through the class, from time to time, I was mentioning stuff like, "Oh, and then Google came and they had lots of compute, and they ran this big neural architecture search, and now we have EfficientNet, which is better. Or now we have Swish, which is a great activation function, and then people did something else, but at the point it was the best." And so, well, of course, they tried it with recurrent cells. Of course, there is a paper from Google where they develop exactly this kind of thing. They try to make recurrent cells more efficient. And yes, on the examples on the datasets where they test their recurrent cells are better than LSTMs and GRUs. And here is an example of their cell. Of course, we won't go through it, but as you can see, it has only four weight matrices. It's kind of similar to GRU, but it's even better. It's even more efficient. And nobody has ever heard about these cells. So most probably they don't work as advertised or, I mean, they don't, I'm not saying Google is lying. I'm saying they probably work on those examples where they were developed, but they don't generalize to other situations. And for some reason LSTM is still the best. It still stands. Okay. So with this, I think I want to end our discussions of recurrent networks specifically. If there are any questions, now is a good time and I will show you an example here. Yeah. So I have some code for today, not very deep, not very difficult, but I hope more interesting codes will be in the practice session. So this is just an illustration of exploding and vanishing gradients. It's not even a real recurrent network. It just shows you that if you keep multiplying by a number less than one, you vanish. And if you keep multiplying by a number greater than one, you explode. And here is a real experiment. So this is the classic LSTM benchmark from very long ago, from Hohreiter and Schmidhuber. And it goes like this. You have an input with two components. So there are two input channels. One is just a set of numbers. It just goes to random numbers from 0 to 1. And another is a channel of zeros with exactly two ones. So like here is a sample input. The markers show, the bars show these random values that go between 0 and 1. And the stars mark the ones in the marker channel. So it's like a vector, a long stream of numbers, and two of them are highlighted. And the question is add the two highlighted numbers, give me the sum of two highlighted numbers. So it's like a perfect toy test problem for memory, right? You need to, when the marker channel tells you to, you need to memorize this value. And then when it tells to you again, you need to add this value to the one you memorized. And sure enough, LSTMs and GRUs, they both work well on this. And this is actually, since it is so simple, this is actually a good example for GRUs, not LSTMs. So here you will see that like a simple linear RNN doesn't work. It just like, it stays on the baseline, which means no training at all. LSTMs at some point get what they are asked to do and they start learning, but in like 600 steps, 600 iterations, they didn't yet train. And GRUs have trained much faster and from a much earlier point. So this is the kind of plot that you would see convincing people that GRUs are better, but this is a very easy problem, right? So that's the point for a very easy problem. Of course, a more efficient cell will be better, but probably it doesn't scale to really difficult problems. And here is another sample from the LSTM. It's the same problem, it's just I take one of the inputs, here is the input, and then I look at what is actually the contents of memory. What are the outputs of the gates and what is the current prediction of the sum that you, what is your running guess? What would be the output if your sequence stopped right now? And as you can see, a trained LSTM does some very reasonable stuff. When it sees a star, when it sees a marker, the thing that it writes to the cell actually spikes. So you write a lot of stuff here and you don't write much over here. And your cell just grows to the correct value. That's it. So if you take your running guess, then it indeed tracks the true sum and it goes to the true sum after the second sum. So it works. It's a very simple problem. But interestingly, the interesting part here is straightforward recurrent networks cannot do that. If you have just this linear cell, you simply cannot have this long-term memory that goes back and recalls it. "Oh yeah, I had that number 15 steps ago. Now I need to add it to the present number." And that's the idea behind all of these recurrent cells. Okay, so any questions about this? No questions. All right, well, with that we go to our next topic. And our next topic is probably the last time in class when I again start from a neurobiological motivation, when I again tell you about the brain and everything. But now we're in a very superficial way. Now we don't go from a bird's eye view, we don't go to the details of how neurons operate. We actually just stay on the level of how we think in general. And we are interested in the notion of attention. And if you think about attention, I hope that you are paying attention to me right now, even though I'm really not sure. But if you think about how attention works, and especially how lack of attention works, it's a really funny thing, it's really unclear how it's supposed to work. Our brain seems to work very differently in this regard from how networks that we have seen so far, artificial neural networks work. We are in the computer vision class, so think of an image. Think of looking at an image and registering some stuff, some objects that are on this image, etc. I told you that our visual cortex, the part of the brain that processes images, is kind of similar to convolutional networks, at least in spirit. They cannot really be similar in architecture, but in spirit it's like extracting local features, then combining them to better, to more global features, to semantically richer features, etc. But if I look at an image, like right now I am looking at my computer, obviously, but my field of vision is, of course, much wider than just the computer. So if something happens outside of the computer and right now I'm thinking about our lecture and I'm writing something on the board, most probably I'll miss it, right? Because I'm not paying attention to that. I'm paying attention to the board. But the stuff that's outside is still in my field of vision. So if you try to map this kind of attention thing to how neural networks work, it's really strange. So when you go with a convolution over an image of any size, you get features extracted from every part of the image, right? And then these features on the next layers, they get combined into more global features. I showed you some pictures yesterday, et cetera, et cetera. And there is no place to lose stuff there, right? If I have a huge image, okay, I will need to spend more compute, but it's not like I'm going to lose some object from there. I will still extract features from every part of the image, and they will still be combined into more global stuff. They will still have this, I don't know, tabic cat neuron up there, that will still activate on the cats. It's not like a convolutional network can just miss the cat. Completely impossible. But we do. What's the difference? The difference is an attention mechanism. And how it works is actually a pretty difficult question. There was this guy, Alexander Luria, he was a very interesting man, he had a very interesting career because it was 1930s-1940s, he lived in Italianist Russia, but still he was like a man of the world. He traveled to all the conferences, he published in all international journals and he was like one of the internationally recognized fathers of the field of neurobiology. And Alexander Luria, when he posed the main research program of neurobiology in general, he said that there are three main pillars, three main components to the field of neurobiology. And he said it's attention, memory and cognitive functions, which is basically like how we think. So to him and to the whole field of neurobiology, attention is up there on the level of memory and cognition. Well, of course, since Luria there has been a lot of progress, we kind of understand how attention works in the brain. But it's not really important for us from the computer science point of view, because in the brain attention works through memory. More or less, it works through memory. There are different types of memory in the brain. So there is this kind of working memory, which is a very short-term memory that stores just a few latest objects. Like if we were offline in class, I would be able to demonstrate. So if you give a lecture and if you ask any person, a person who is not paying attention to you at all, like this person is on their phone chatting with somebody, etc. But if you suddenly ask this person, "Tell me what I just said," even if they were not paying attention at all, they would be able to recite the last five words or so. They would say, "Oh, yeah, you were just saying blah, blah, blah," and it would be right. But if you ask what I was saying 30 seconds ago, it would be blank. So working memory is this very short-term mechanism of what's happening just now, and mostly everything goes there, but then there is this filter, which parts of this recent stuff are actually important to process further, and that's where stuff gets lost. And I won't spend more time on attention, neurobiology, etc. It's an interesting topic, but I think for us it's more important to go further. If you've never seen, so I will just recommend you one thing, if you've never seen this video where there are two teams of players passing basketballs, the team in white and the team in black, and you're supposed to count the passes of the team in white. If you haven't seen that video, please see it when I publish the slides. I can copy it here. Look at it and pass the test. It's interesting if people still fall for it, because back in the 1990s people definitely fell for it. Now I'm not so sure. Our attention mechanisms have changed a little bit. Anyway, so neurobiological words on attention actually show that even if you are looking directly at some stuff, this video shows that if you are actually even looking directly at some stuff, you still don't have to process it. It still may be lost. You still may like very early in the brain, you can decide to drop it. But also there is another thing which you probably have heard about and it's about our vision in general. And our vision also kind of doesn't process the whole field of view. You probably know that. You have this, for VL Spotlight, we have this small part of our field of vision where we can see stuff very, very clearly in high definition and then it gets blurry and blurrier, right? And we don't notice it because our gaze constantly wanders around. Even if you're looking at your computer, still you're constantly like, it's called saccadic motion, your gaze constantly shifts and you look, you get different snippets of the whole picture and then your brain just kind of constructs the whole picture from these relatively blurry components. It's like several photographs of the same scene, but the focus is on different parts. And the original motivation to add attention mechanisms to deep learning was to actually emulate this, to emulate how we see things, to emulate this blurriness in the peripheral vision. And that, of course, sounds very strange. Why on earth would you do that? Why would you make things blurry if you don't have to? In computer vision, in a convolutional network, you can just put in the whole picture. You don't need to blur anything. Why would you want to do that? In our eyes, I mean, of course, they have evolved to do stuff and maybe they didn't have the energy, the capabilities to do that. But why do we need to do this in computers? And the answer originally was to save weights, to save input size, to make it more efficient. So if you have a big image and if you can actually, instead of looking at the big image, you can actually do like three snippets of the big image where you only actually use the pixels from a few small parts of this image, and then the rest can be blurrier. What it means to be blurrier, it means there are fewer pixels, right? So the input size becomes smaller, and much smaller actually. And if you have like three glimpses and everyone is just looking at a small part of the input, then of course even the total input size will be much smaller. So originally people wanted to save processing by doing attention mechanisms. And the new thing here is that now in addition to just recognizing stuff, in addition to doing your classification problem or whatever from these blurred images, you also need to choose where you look. So you need to choose the positions of the glimpses. And these positions, they form a sequence. So this becomes a sequence problem because the next glimps, of course, can depend on what you see in the previous glimps. So your first position can be chosen somehow generally, but then your second position will depend on what you've seen in the first one. So early models of attention were recurrent. There is this field of recurrent visual attention. I won't go into details because that's not too relevant now. Now it's all very different. But more or less the point was, let's look at this picture, more or less the point was given a relatively big picture, let's walk around it and choose where to look and blur the rest. And then you can actually be more accurate while being more efficient. And there is a recurrent mechanism in choosing these subsequent glimpses. But yeah, this is outdated, you don't have to learn that. What is more relevant and more interesting is what happened with attention at the point where attention got applied to encoder-decoder mechanisms. So let me go back to the board because now I do want to explain stuff. And let me first explain to you what the problem is. So let first LSTM and now our second part for today is encoder-decoder with attention. So what is the problem that we are solving? Well, let me motivate this with machine translation. I mentioned machine translation before and it sounds like a perfect problem for recurrent encoder-decoder architectures. So you have your input, which is like, I don't know, hello world, exclamation mark. You read your input, this gives you some kind of hidden state. And then the last hidden state, or maybe the last hidden state pushed through some kind of output head, whatever, gives you this vector, let's call it z, this intermediate representation of the input sequence of the sentence. And then you take this z and you decode it into the output. I only know English and Russian, so let me write that. Privyet, comma, mir, exclamation mark, something like this, right? And probably you want to, so yeah, it probably doesn't look like this. Probably you have a hidden state over here, h prime, and z is just the input to every, to every cell. So probably the data current decoder looks like this. And when people did this, when people had the compute to train vehicle STMs, and they actually tried to apply LSTMs and GRUs with this kind of architectures to, say, machine translation, they realized that they have an unsolvable problem, at least a problem unsolvable in this kind of architecture. So, yes, this works. This defined state-of-the-art in 2014 or whatever. And this actually gives you good results with short sentences. With sentences like "hello world", it will work great. But you cannot scale it up. So here is the thing. The problem of encoder-decoder architectures like this is in the dimension of this intermediate representation Z. And the problem is you cannot have a good dimension that will be either too small or too big. If you have a Z which is too short, D is too small, then everything will train, everything will be perfect. It will run fine but it will not be able to fit a lot of meaning, a lot of information into a small Z of course. So for hello world it will work but of course I'm not talking about putting war and peace inside a single vector. But even for long sentences it will start to break down. And if you try to fix that by making Z longer, by extending Z further and further and further, then it becomes harder and harder to train. So if you have a huge or very long Z, it means that your hidden state in the LSTMs or your input to the decoder LSTMs will become longer and longer. And that means you have quadratically more weights and now you don't have enough data and enough compute to actually train them. So this is like a problem that you can't really solve inside this architecture. You can either have a good encoder-decoder LSTMs with small Zs but it won't scale up or you can have large Zs but then the training will be impossible. So in architectures like this, if you look at the graph of like, I don't know, whatever quality, I'm abstract here, but some kind of quality metric. And this is like T, the sequence length, the input-out-output sequence length. What you actually see is like it's very good while we have short sentences and then it just drops and it's very bad. So of course as sentences get longer the quality will drop, but of course you would want your graph to look like this. You would want it to drop gracefully and still work for longer sequences too. So this is what attention mechanisms for encoder-decoder recurrent networks were supposed to fix. And this is an important concept that I think is still relevant. So what is the problem with Z? Where do we get this idea for this attention mechanism from? The problem with Z is that it's only one vector for the whole input, for the whole sequence. And this is what we need to change. And in transformers also there will not be a single vector for the whole input. Because we kind of understand that sometimes we translate specific words. And when I'm writing out mir over here, I'm translating the word world. And world should be more important as the input over here than anything else. And here there is no way to express that. I just need to cram everything into this single vector. So the first step is to get rid of this assumption that everything needs to be in a single vector. So in this encoder-decoder with attention, the first thing that I do is... Okay, let me say "Hello world!" and it's still a recurrent network at the input. Let's say it's bidirectional, because of course it's bidirectional. It doesn't make sense not to read the whole sentence. But it produces outputs for every x in the input. So there is a vector, let's say z1, there is a vector z2, and there is a vector z3. So far it's easy, almost nothing has changed. Of course, if I can produce a vector at the end, I can produce it at every step. I just take the two hidden states, I push them through one feedforward layer, and there you go, here is your z. So now I have these vectors for every input word, for every token. But I can't just concatenate them all and feed them all over here. This is exactly the z is too long situation. I don't want to make them longer because that wouldn't make any sense, that this would be just the same thing restated differently. I want to have as input on every step here, I want to have one vector of this size. So how do I combine them into this single vector? And this is the attention mechanism. I do the following. I have a small network, the attention network, that receives as input. Okay, I need to draw the decoder too. So let's say that we are inside the decoder and it's got like HT prime over here. And we are writing the next word right now. And we need to find out what is the current input over here, right? So that it will write this token and will produce h prime t plus one and so on. So we are at some point in the decoding process. So the attention network receives as input a z from here and an h prime from here. So it needs to know where we are in the decoding process, of course, because the attention weights will be different for different words that I write. And then it will produce a score, A1, just a number, that shows how important this token is right now. You will see how it gets used. So it's the score for token number one at step t. So at the point characterized by this hidden state of the decoder. And then you do it for every z. So you get a2 for z2 over here. And you get a3 for z3. Then I convert this a, so let's call them the vector a, into probabilities, into a convex combination, by passing it through a softmax. You see how it all comes together. We talked about softmaxes, logistic sigmoids, etc. We talked about their properties in lecture 2 or something. And now we are using all of these properties. So it's not noticed that I'm using softmax not just as the output, but I'm also just using it to convert every time I need to convert just a set of numbers to a convex combination to something that sums to 1. And here I get something like alphas. Now they are from 0 to 1 and they sum up to 1. And that's it. These are the coefficients for my combination. So now I just do like a dot product. And Z_t here is just the sum of alpha_i times Z_i. Okay, so Z_t is not a good letter. Let's call it... I don't know. Let's call it... What other words do I have? Letters do I have U_t. So the input for the decoder at time step t is a linear combination of the representations of every token with weights determined by the separate attention network. So what this means, the intuition behind this, is that I want this to express what specific tokens I'm translating right now. So like on step 3, when I'm producing the third token, the third word, I want the word world to have a high weight over here because I'm mostly translating the word world. Well, in the context of the rest of the sentence, but mostly that. And also notice, and the last important point about this before I proceed to just show you the results and everything in discussion. The last important point is this. When I tell you these intuitions, when I tell you stuff like, "Oh, so the attention network is supposed to give you a high score for the word that we are translating right now." This is not any formal input for the network. There is no labeling in the dataset that will tell you, "Ah, now I'm translating this token, now I'm translating that token." The dataset is still the same. The dataset is a set of pairs like sentence in English, sentence in Russian. They match. They are translations of each other. And here you go, 100,000 pairs of sentences trained on that. So when I'm talking to you of intuitions like this, what I mean is we kind of want the network to work like that. And miraculously, after training, it indeed works like that. But we never explicitly train the attention network. The attention network is just this very small, tiny component. It has very few weights compared to the LSTMs. So a practical number, if I remember correctly, would be something like 2% of the weights of the whole network go to the attention mechanism. So it's a very small component compared to the rest of the network. But this very small component actually drives the results. This component is the difference between the red curve and the purple curve over here. This component actually does train to do this job of finding out which tokens we are translating right now and producing the correct weights. So it's a general principle of deep learning that we see quite often. And I think we already saw it in convolutional networks, I just didn't pull it out. The general principle that very often you just need to give the network a chance. You just need to introduce some components inside that have this potential ability to do the job that you want. And even if you have no data to train them on, even if you cannot take the attention network out of this whole thing and train it separately and then plug it back in because you don't have the inputs for this. The inputs are also changing as we train. And you don't have the outputs, you don't have the correct answers here. But still, if you just structurally give the network a chance to do it right, sometimes, not always, but sometimes it will do that. And everything will work and it will be a very nice example of a new structure inside your network. So this was what happened with encoder-decoder architectures around 2015. So in 2014, this was the state of the art. And even in late 2014, Badenow with colleagues introduced this kind of attention mechanism. So this is exactly what I was just drawing. The attention network that receives the current state of the decoder and the representation of a token from the input and it gets you a score and then you do a softmax. Yeah, here are the full formulas. And indeed, it does train to do what you want. And also, like a common feature of attention mechanisms, you will see that in transformers too. A common feature of attention mechanisms is that they also give you something to look at. They give you some attention weights when you actually draw them and look at them. They're usually very easy to interpret. For example, this is from one of the original machine translation applications. Here they're translating from French to English. La Destruction, Deletivement Signifier, blah, blah, blah. For example, French and English mostly match. Mostly it's a diagonal matrix where the high attention weight is on the diagonal. You're translating this word by word, more or less. But notice the exceptions. For example, la destruction is translated as destruction and it's two words into one. There is no article in English here. So here the attention weight is high for both la and destruction while we are writing the destruction. And here, for example, arm chemique, chemical weapons. In French the adjective goes after the noun, in English the opposite. So here the attention weight swap and you see an off diagram. I think I have examples for you here too. So here is a very simple recurrent network with attention that just learns to reverse the input. So if the input is a sequence like 3, 4, 0, 5, 7, blah, blah, blah, the output will be blah, blah, blah, 7, 5, 0, 4, 3. And of course the recurrent network can train to do the same. It's not hard. Actually, by the way, without an attention mechanism, I don't have these experiments here, but I'm pretty sure that without the attention mechanism, it would be hard. It would be very difficult because if you have just an encoder-decoder thing, if you don't have this attention mechanism, then you need to memorize the whole input sequence in order to write it down in the reverse order. So if you cannot memorize the whole input, if you don't have enough space, enough capacity in your intermediate representation to just memorize the whole input, you are screwed. You cannot do the reverse unless you remember it exactly. And with attention, you don't have to remember anything. You just train to have this reverse diagonal attention matrix. And so it's not on the diagonal because you also have special tokens like, yeah, whatever. You also have a special token here like end sequence. But anyway, there is this clear diagonal structure that basically just tells you where to look and what to copy, right? Or here is a more difficult example. I'm sorry, I'm not running them online because it takes a little bit of time to train. So just not to waste time waiting, but I will publish it and you will be able to run it yourself. So here is a slightly more difficult thing. Here is like a sorting thing. So now the input is a sequence of numbers and you need to sort them in the output. And here also you can see that at step t, we attend to the current t smallest value. So like the decoder steps are along the vertical axis, this is the source position. And on the first step, the most attention is paid to position where there is a one. On the second step, where there is a three, then to the four, then to six and so on. So you can see that indeed the attention mechanism has trained to do what it wants. And this was a big thing in 2015. And through the next couple of years, people were like exploring this stuff. And this kind of attention mechanism has a lot of benefits. Let me not waste time. I'm talking too much about this. It can do word order better. It can do some very interesting stuff like doing grammar as a foreign language. So you can sometimes fit even... Okay, let me talk about this because with Transformers it's even more relevant. So sometimes your output has some kind of complicated structure that doesn't look like a sequence. For example, if you're doing a syntax tree of your input, then your output is a tree. It's a graph, right? So it doesn't look like you should use a recurrent network to write out a graph. The graph is not a sequence, it's more complicated. But it turns out that if you just write down your tree as a string, and there are ways to represent the tree as a string, and you just treat these three strings as a language to which you translate, it works. And I think with Transformers it would work even better. In 2016 there was a very interesting paper from Google where they basically published how Google's neural machine translation system works. And I won't go into details here, but basically it was interesting to learn that Google Translate also works in the exact same way. Of course, Google being Google, it was bigger, there were some tricks, etc., etc., but basically it wasn't coder decoder with attention. And by the way, my personal experience was that around 2015, 2016, when they switched from whatever they had before to this kind of architectures, Google Translate actually became much better. I mean, I was using it all the time, better to say I wasn't, but I had a side job at the time translating research papers from Russian to English. And before about 2016, of course, I tried to use Google Translate, but it was completely hopeless. So you would spend much more time on fixing the results of Google Translate than you would on just typing the stuff from scratch. It was completely useless. And in 2016, 2015, there was a phase transition. Suddenly, sure, it was still bad. Sure, you still needed to edit it. You still do need to edit translations, even from the latest cloud of GPT. But now, it was more efficient to first do a pass with Google Translate and then fix the mistakes or the bad writing than to do everything from scratch yourself. This was the moment when machine translation actually started doing some useful work for me. The last point here is that when I'm talking about encoder-decoder architectures, usually I talk about the same kind of architecture in the encoder and the decoder. So now we were doing machine translation, it was a recurrent encoder that reads text and the recurrent decoder that writes text. It doesn't have to be this way. So you can definitely have encoder-decoder architectures where the input has one modality, one kind of network, and the output is a completely different kind of network, completely different modality. I don't even think this counts as multimodal architectures because, well, they are multimodal, but the two modalities are separate, really, because all you need from the encoder is to give you a vector representation, and then you take this vector representation and plug it into the decoder. So, for example, I mentioned at some point, I think, the captioning problem. Here is the captioning problem as it was in 2015 with a straightforward encoder-decoder thing. The encoder was a googling net that we discussed, the decoder was an LSTM, and it became much better when people added an attention mechanism. And again, this is also important and important for what will come later. Notice that you can do the exact same thing, this kind of attention highlighting specific parts of the input, even if your input is not text, even if your input is not a sequence. So if you have a picture, for example, the only difference here is that now we don't compress the whole picture to a single feature vector, like we would do if it was a straightforward encoder-to-coder. We have the same CNN, the same convolutional thing. And then I just top it a little bit short of the end, a little bit in the middle, so that I still have some geometry left. Like in this example, the input is 256 by 256, and I stop the feature extraction when I have a 14 by 14 feature map. And now I have these "pixels", elements of the feature map vectors, and I can do attention over these vectors. So now I can have an attention network that combines, that gives me coefficients to combine these 192... ...196, no, 14 by 14, 192, right? No, 196, yeah. So, this 14 by 14 different vectors, and they have this, so my coefficients will combine these 14 squared vectors. And again, it kind of works, I won't go into details, and another nice thing is that it gives you the actual attention weights. You can look at them and you can interpret them. So, we will kind of see that in transformers too, but it will be actually less clear and more complicated in transformers. But here, it's very clear, it's very straightforward, you can just see what the network is looking at right now... ...as it actually writes this piece of the output. So, a woman is throwing a frisbee in the park. Here is woman, we are writing woman, we look at the people... ...and then throwing, and we start concentrating on the throwing, and frisbee, we are concentrating on the frisbee... ...and when I write down the park, then we are not looking at the people, we are looking at the background. So that's just perfect. Okay, so I want to stop here, are there any questions at this point? You've actually covered quite a lot, starting from LSTMs... ...of the attention mechanisms, recurrent attention, and on to encoder-decoder attention. Wonderful, so let's have a break, please let's not have a half an hour break... ...because today our administration asked me to call it 1:20... ...so let's have a 15-minute break and then we'll reconvene... ...and we'll discuss the main architecture of the entire Deep Learning right now... ...for the last 10 years, the transformer break. Okay, so on to the Transformers. Transformers appeared in 2017 and was kind of... ...I mean, let me start with a brief historical remark. In 2017, when this paper appeared at the end of the year... ...I don't think, I'm pretty sure, the authors of the transformer paper... ...if the transformer paper of attention is all you need, actually understood what they were doing. So the paper is not that ambitious. We will see what its results were originally, and they are mostly about... ...here is a different way to do stuff which provides approximately the same results... ...but which is more efficient, so maybe let's switch to this more efficient way of doing basically the same. But since then, the whole field of machine learning switched to transformers, as we all know... ...and much of the rest of our class will be built on the transformers. We will use transformers in different ways. The main, I think, positive qualities that the transformer had... ...that the original paper couldn't really notice from its experiments... ...are two things. One, it turned out it proved to be very, very general... ...in the sense that the transformer is just very good... ...at noticing internal correlations within complicated data. And it doesn't really matter for the transformer whether it's text... ...or images or whatever, it just works with sequences of vectors. It doesn't care where these vectors come from. So this is a great thing. And an even more important thing is that... ...transformers prove to be extremely scalable. You can take a transformer, you can scale it up, and it works better. You can scale it further up without changing anything inside. Well, sure, there have been novelties. Sure, modern transformers... ...is slightly different from the one we had years ago, but it's mostly the same. And still you scale it up and it works better and better and better... ...and it never saturates. With our large language models, I hope I will have time to talk about that next week. With large language models, we keep going from tens of millions... ...to hundreds of millions, to billions, to hundreds of billions... ...to now trillions of parameters, and they just keep getting better. And this had never happened before. You can't scale LSTMs in the same way. Or I mean, maybe you can, but we don't have enough compute to do that... ...but the complexity grows too fast, or they saturate... ...and even if you can't train, they stop providing any benefit. And in the transformer, it kind of all came together. So what is the transformer? I will actually go through the slides first, through some of the slides first... ...because the basic structure is very similar to what we were just discussing. I don't have to redraw it, but then the main core will be the self-attention mechanism... ...and that is completely new, and that I will, of course, discuss in detail. So this is the most famous picture from the original paper... ...but I think it's pretty hard to understand, so I make my own pictures here. Here is the structure of the original transform... ...without details, without the interesting parts... ...but the general structure is actually very straightforward... ...and it's very similar to what we just had in... ...recurrent encoder-decoder with attention architectures. So it's an encoder-decoder architecture, and yes, the original transformer... ...doing machine translation. It has an encoder which consists of six identical layers. It has a decoder which consists of six identical layers. And the encoder receives text in one language. The decoder produces text in another language. Let's stay in this paradigm for now. Interesting parts here. What can we see on this picture? So first of all, the input to the actual transformer, the actual encoder layers, is not just a sequence of tokens. And we didn't discuss it in detail. I mean, text is not our thing, but it had been very common in natural language processing even ten years ago to convert one-hot representations of words, of tokens, to continuous representations that are usually called embeddings. This is, again, very, very common, very straightforward, all through deep learning. If you have a large vocabulary of different stuff that you want to input, like in this case, different words or tokens, parts of words, then you first want to convert them to dense vectors. And there is like a whole line of work in NLP on this, like work2vec, glove, fast text, different embeddings, we won't go there. But here, the embeddings are really straightforward. There is just one very interesting technical thing that I will talk to afterwards, at the end. But mostly, it's just a matrix of vectors. So for every input token, there is a vector, and we look it up, and we put it in place of this token. That's it. But importantly, it's not some external representation, it's not some work2vec that we copy here, it's an embedding layer that is trained with the rest of the network. So you train these vector representations along with the other weights. And after this embedding layer, the input sequence becomes a sequence of vectors. And all the actual transformer is doing, it's rewriting sequences of vectors into sequences of vectors. So every encoder layer will take a sequence of vectors as input and produce the same sequence of vectors. Well, I mean, a sequence of vectors of the same size as output. And that will rewrite this kind of structure for, in this case, six times. And then we get a vector for every input token. After all of this encoding, it's no longer just a representation of the token, it's now a representation of the token in the context of all the other tokens. And I mean, many times it has looked at all the other tokens, the whole sentence, the whole sequence, et cetera, et cetera. So by now, by the top here, we have these representations of smart, semantically rich representations of input tokens. And now what does the decoder do? The decoder is a language model. I hope you've heard of language models. So the decoder is producing output tokens one by one, autoregressively. So its input is what it has already written, the history of output until now. And its output is the next token. You have to run the transformer decoder as many times as the number of tokens that you want to produce. Again, this is one kind of restriction that in modern language models you need to work around in some way. There is a big science around it with speculative decoding and stuff like that, but you won't go there. Anyway, by default, it's an autoregressive thing. You produce the output token by token. And these guys, the stuff that you are actually translating... Sorry, I don't really understand this. Can you see my cursor? You can't, right? Yeah, okay, so pointing with the mouse doesn't really work. Alright, so the stuff that is at the output of the encoder on top left here, it's getting used in the decoder on every layer, on every step of the way. And of course we will discuss how exactly. But this high level structure is very similar to what we just saw, right? Decoder and there is no separate attention network here, the attention will be hidden inside the encoder and the decoder. So if you look inside an encoder layer in the decoder layer, you will see that the encoder layer, actually I think you see, yeah I have it here. So the encoder layer is what, it's a self-attention layer, then layer normalization, then interestingly a feed-forward layer, a fully connected layer, then another layer norm and that's it. So of course the interesting part, the part we are going to discuss in detail is self-attention, right, the self-attention is the first layer here. But the rest also uses these components that we have been discussing, right, so it's not, we are not discussing ancient history, everything that, all the ideas that I'm telling you are actually being used right now. For example, here we see a residual connection that goes around the self-attention layer, right, and it lands, actually I forget in front or afterwards, but near this layer normalization layer, which is a kind of batch norm, right, so you discussed it with Alex in practice, layer norm is like batch norm, but not across the mini-batch, but across all of the outputs of the current layer. So transformers are big, and then transformers, oops, what happened, sorry. Recording in progress. Yeah, I apologize, I'm not sure what happened, but somehow I got disconnected from Zoom. The internet works, I hope you can see. Yeah, so the, where did I stop? Yeah, so the encoder layer uses this layer norm at the output of self-attention, and layer norm, as you discussed with Alex, just averages out the gradients, keeps the loss landscape smooth, keeps it under control in terms of the absolute values of outputs, etc. And here, transformers are big, so we cannot really rely on batch norm, because probably there is no batch, probably only one copy of the transformer fits into our memory, and we have only one instance, so we use layer norm. And then, interestingly, there is just a feedforward layer, and it's actually very important. It has a lot of weights. If you look at it, it takes up quite a big fraction of the entire weights of the transformer. And there is nothing to say about it, it's just rearranging the features, mixing together the features in every vector separately, as you can see, it's applied to every Z' individually, and then there is another layer, and that's the encoder layer. In the decoder, you also have self-attention. It's exactly the same as the self-attention here, except for the word masked, but we'll get there. There's also a feed-forward layer, also layer norms after everything, and the only difference is this encoder-decoder attention layer. The outputs of the encoder, these vector representations, they should go somewhere, right? They should be doing something, and they go here. And when we get there, I'll explain what exactly they do. And then after the decoder has, after we've gone through the decoder, then of course we have to do some classification. So there is a linear layer that goes to a softmax layer, and the softmax produces probabilities, and then you sample the next token with these probabilities. So again, as you can see, it's exactly a logistic regression at the end, so it all kind of comes together. All right, so this is the general structure, and on this picture there should be absolutely nothing new to you, except, of course, the self-attention stuff. So what is self-attention? What exactly? How do we understand it? Where does it come from? Item number three for today, self-attention. Well, to actually discuss self-attention, I need to take a step back and I need to talk to you, surprisingly, about information retrieval, which is not the subject of our class, but turns out to be very relevant. So how does search work in deep learning? How does information retrieval work when you have neural networks? Well, basically it works like this. You have the queries, query one, query two, and you have documents. Document one, document two, document three, document four. And in usual information retrieval, what you would do, you would establish a similarity. You need to establish some kind of similarity between queries and documents. This kind of similarity will be called relevance and you will train it to be the relevance. So it should be higher when this document is relevant to this query. This is how search generally works, whatever it is. But when you have deep learning, when you have these neural networks that can process any kinds of input and that can train to process long texts, large images, etc. What you usually do is this. You get documents through an encoder, and the documents will become vectors. You get queries through their own encoder, so they become vectors too. And the idea is that all of these vectors should live in the same space. So even though encoders are different, they cannot be the same because documents can be images, for example. So they are different, but they should produce vectors in the same latent space. So documents get mapped over here, and then you map your query over here, and you are supposed to train the whole system so that the relevant documents will be close, the representations of relevant documents will be close to the representations of the queries. So then, inside this latent space, you will be able to just take nearest neighbors, and these nearest neighbors will be a good answer to the search query. So I was drawing this, but I think I have a picture about it. So you have a query, you have a document, documents go through their own encoders, and then the whole point of it is so that in the latent space, you actually have the structure that relevant documents will be near the images of the queries. There is a whole field of study about how to do that. It's obviously a very big subfield of learning, and we could have a whole class on information retrieval, maybe you will, so I won't go into more details. But what we need now is this basic intuition that different stuff gets mapped to the same latent space, and in that latent space we are just looking for nearest neighbors. And since you can do it linearly, as a linear space, basically the similarity here between the query and the document can be thought of as just the dot product of the corresponding vectors. So I encode the document and I multiply it by the encoding of the query. That's it, okay? And this approach has lots of advantages for information retrieval. You can just store the vectors, you don't have to think about anything else. It's fast to do it in the low dimensional space, blah, blah, blah. And self-attention, interestingly enough, draws on this intuition, but since it's self-attention, it applies these ideas to the same set of vectors that are both queries and documents. So here is how it works. Here is how it works. So we begin with a set of vectors. As I said, every layer of the transformer gets just a sequence of vectors as input. So we have this, putting down here, x1, x2, and so on, xn. We have these vector inputs. Now I want to make this kind of query document thing. In information retrieval, the terminology is inherited from classical information retrieval. You would sometimes call these images of documents, the representation of documents, you would call the keys. In classical retrieval, the query would not need to be encoded, it would be just the query. There is no word for the image of the query, but we will just call it the query. Let's say that the query already lives in this space, and the document should be mapped there and should produce some kind of a key. And here we take our axis, let's say we take x1, and we produce from it queries, keys, and values. So with x1, we multiply it by a matrix called w cube, and as a result, we get the first query vector. This will be q1. Then we take all of the inputs, all of the axes, and we multiply them by the matrix w, k. We just put it here once, not copy it many times. And we get the key vectors. We get k1, k2, and so on, kn. And the whole point of self-attention is that q and k should live in the same latent space. So now this guy goes here, these guys also go here. And the similarity between q and k is just a dot product between them. We assume that they already live in this latent space, they have the same dimension. And this similarity is exactly the score that we will use as the attention of it. You see, q was made from x, k was also made from x, and now we look at how similar q and k are between each other. So out of this space, we get this sequence of attention scores, so to say, affinities. We get a11, which is q1 times k1, and then a12 and so on, a1n, which is q1 times kn. So we get this vector of attention affinities, we put it through the softmax, as usual. And we get, yes, sorry, also I forgot one detail, I'll get to it later. But we put through the softmax, we rescale first by square root of d, and then we put it through the softmax. So this kind of transformation, I'll explain later why we need rescaling. And then we get this vector of attention weights. So now we have, this will be like a1 and this will be alpha1. So this is the actual attention weights between 0 and 1, rescaled to sum up to 1. And they are the similarities between the first query and all the keys, right? Similarities rescaled back to a set of weights. So now we need to use the set of weights to make some kind of linear combination, to make a convex combination of something. Well, of what? Of another set of vectors. Here is the thing. So now we again take all of the axes and we multiply them by yet another matrix, weight matrix WV, and we get vectors that we call values. So the green ones are values, the blue ones are keys, and the red ones are queries. And now we take all of these values and we multiply them with the dot product. We multiply them, we add them up with the coefficients alpha. So this is what this is. What's the dot product? How do I write this, right? Anyway, dot product. So the output is, let's call it z1. It's the sum of alpha1i times vi, okay? And that's it. That's the basic idea of self-attention. And of course, I only drew one query, but it then gets repeated. So we take x2, we multiply it by wq, we get q2. It also gets mapped here, blah, blah, blah. And as the output, we get z2, which is the sum of alpha 2i, again, times vi. And vi is our vectors, right? So this takes a little bit of understanding. Yeah, cosine similarity, right? So this takes a little bit of understanding to get it in your head, because it's all very abstract, right? It's just some dot products in some new space, and this new space is just multiplication by the weight matrices. Nothing too intuitive here. Well, I tried to give you the basic intuition for information retrieval, but I mean, it only goes so far. Still, formally, it's really, really simple, right? So what we do formally is we take the axis, we multiply them by a matrix, we get the queries. So in practice, of course, you would not do it step by step, you would do it all at once. So your queries are some weight matrix times x, or maybe the other way around, I forget which one is more common, maybe x times this matrix, it doesn't matter. And your keys are some weight matrix times x, and your values are some weight matrix times x, right? And then what do you do with these matrices? So if we continue the formal stuff, you need to get this matrix of all possible cosine similarities, you write all possible dot products between queries and keys. So if you write it in matrix forms, then it will be like q times k transpose. This will be the matrix where the ij's element will be like qi dot product by kj, right? And then you take this q times k transpose and you rescale, you do softmax, and then you multiply by the result, the vectors v. So the attention weights are the softmax of one of the square root of d q k transpose, and the actual output, dz, is softmax of one over the square root of d q k transpose times v. And that's the main formula that you see everywhere, right? This is from the original attention is all you need paper, and this is exactly what I was trying to explain to you here. So the intuition about these matrices, their dimensions and everything is that x is probably pretty big, pretty long. It's from some r to, I don't know, some capital D, and queries and keys have to live in the same space. We have to make dot products with them, so they both have to be living in the same smaller space, small d. So this matrix and this matrix are both like d times small d matrices. And values formally can have a different size, right? We never take a dot product between v and q or v and k. So formally it could be like d prime. In practice usually it's the same d, of course. But formally let me write that this is like a d times d prime matrix. Or sorry, the way I write it, it should be that way around. It should be d times capital D and this should be d prime times capital D. Okay, so what else can I say here? What else can I say here? I think that's it for the basic idea of self-attention we got from the beginning to the end. I will show you a nicer picture in a sec. Let me just highlight one thing. Sorry, I promised to explain where the square root of D comes from. Why the rescaling? Well, the rescaling goes like this. What we have here, what we have in this raw affinities between queries and keys are like dot products between vectors of length D. And if you think of, say, queries and keys as just random vectors, vectors with random numbers inside, you see that... What do you see? You see something, don't you? You see that these vectors with queries and keys inside, if you think of them as just random vectors, so let's say it's like QI is something like 0 plus or minus 1, right? So it's something from minus 1 to 1 on average, maybe more, maybe less, but more or less it has a standard deviation of 1 around 0. And KJ also has a standard deviation of 1 around 0. Then what is happening here? This is the sum of d batch numbers with deviation 1. And if you take the sum of d random variables, each of which can go to plus or minus 1 on average, then the result will have a variance on the order of give or take square root of d. I don't want to do probability theory now. It's a classical result. Basically, I think if you ever had a probability theory class, you probably know this in the form of random walks on a line. Like if you go from zero and you clip a coin, and every time you go either right or left, then how far from zero do you expect to be in n steps? And the answer is square root of n. So it's the exact same effect. And that means that if we don't do this, we will have big numbers over here. If, for example, d is something like 64, which I think was true for the first transformer, then when you add 64 numbers, you get numbers on the order of plus or minus 8. And plus or minus 8 is more or less, more or less means that the output of the softmax will be close to just one and zeros, close to a one-hot vector, which is not really what we need. We need it to be smoother here. So we smooth it back, we rescale it back so that we go from the square root of d back to give or take one. That's an explanation for the scaling. And what else I can notice right here, right now, is that we already see the main computational problem of transformers. I don't think we will have time in class to discuss this huge line of work that tries to avoid this, to work with it, but we definitely should mention the problem itself. Here, to compute this, you need to have this matrix. You need to compute this matrix. This matrix is an n times n matrix. And this is like quadratic complexity as a function of the input length, of the length of the input sequence. And that is the main computational problem of transformers, because it means that you cannot scale them up with respect to the input length unless you do some interesting tricks. And of course, there are a million different interesting tricks. It's a big field. But basically, if you remember like three years ago, when people were doing large language models, they would be like boasting about their context size. They would be saying like, "Oh, our LLM has a context size of 128,000 tokens, and our LLM has 512,000 tokens, and we've got a million token context window." I mean, this is about that. So it's not trivial to get to a million token context window. It doesn't just mean that the complexity is a million times one token. It means that the complexity is a million squared times one token, and a million squared is just too much, definitely too much. So you cannot do it straightforwardly as this matrix. You have to invent some tricks around it. And of course, there is a big field of science around this. Even right now, I think, if you go to Cloud, you will see that it has a separate model called Opus with a one million token context. And it's more expensive, more complicated than just straightforward Opus, which obviously has a smaller context size. So context is a difficult problem for transformers. But other than that, it's all here. This is how self-attention works. And I won't try to draw it on the board. I will show it to you on slides. But the next thing and another idea that we actually were discussing a couple of days ago, and now it all comes together. Another important idea here is that notice what we are doing to x's. Again, let's look at it from this geometric perspective. I think yesterday we talked about this. Geometrically, what we are doing is we are taking this x in a big space and we are projecting it to a much smaller space in two different ways. And these two ways give us the queries and the keys. Again, I can't give you like tangible intuition that you can touch, but mathematically what you are doing is you have a big space and you are looking for a good projection for the queries and another but the same dimensional projection for the keys. So like two ways of looking at the set of vectors x. And then there is the third projection which can have a different dimension for the various. So in a way it's again the same question that I asked yesterday. If all I do with axes with these vectors is compress them down to queries, keys and values and in practice like if you have, I don't know, capital D something like 256 or 512 you would have small d something like 64 as I said then why do we need the long vectors at all? same question as we had yesterday and it's the same answer the answer is this is what I've just drawn to you is just one attention head and in practice in the transformer you will have several different attention heads each will have its own matrices WQ, WK, WV and they will produce their own kind of ways of looking at the input and ultimately they will produce their own output z_i so really there is another index in here let's look at the slides, I have better pictures up there so this is the intuition coming from self-attention and this is the picture that I was just drawing so let's walk through it again, it's the most important picture of the whole class I think the input is a set of vectors, each vector gets multiplied by three matrices wq gives you the query, wk gives you the key, wv gives you the value and then the queries and the keys should live in the same latent space you take, well, okay, set cosine similarity, I say dot product because of course nothing forces them to have like norm 1 and we do not want to rescale by norm, it's too complicated so let me just stick to dot products we take the dot product between q and every k, we get these affinities then we rescale by the square root of, here it's called q, but it's square root of the dimension then we take the softmax and we get the actual weights, convex weights and we have this convex combination of the vectors v with these weights oh and notice by the way how we are actually looking on all input by every query so like every x in here is looking on every token from the input on every other x and on yourself as well, on x1 too sorry, I should probably say this explicitly here this is another very important property that makes transformers so cool and this property is if you have x1, x2, xk, blah, blah, blah, x capital L and let's assume that you want to like find out you want your x1 to influence to have some relation with xk over here so like this word in the input text has relevance to this word if you had a recurrent network this influence would have to go step by step through all of these intermediate vectors, right? so there is no path in the recurrent network that jumps over tokens you just go step by step and of course even if you have an OSTM with this memory cell with this constant error carousel, the highway that connects every point still a lot can happen as you go step by step through this sequence with the transformer you don't have to do that with the transformer you just jump in one step from here to here and you can actually jump to every token and you do jump to every token on every step so this is great this is like one step from every i to every j and this is a big plus and the cost of this is this quadratic complexity this is the big minus okay so a recurrent network has linear complexity as you add more elements to the sequence you just do more steps but each step has the same size has the same complexity so the current networks are linear in the input size transformers are quadratic in the input size it's a huge difference but they are then more free to notice the relations they don't care about how far it is from one topic to the other they just see the whole sequence at once on every layer on every step and that is great okay so yeah and this is the picture that i won't attempt to draw on the board sorry yeah please um may i ask a question sure sure uh i think i didn't really understand about the value space um like i understood that curie sorry i'm back i truly hope that the recording is not garbled after that um ob studio quit me sorry um anyway yeah please what was the question i'm trying to formulate it well i'm more or less understood about the key and curious part is that we they share the same space latent space and we uh are interested in finding the closest distance between them we rescale them etc but but the point i didn't really understand about the value value vector not that even vectors and also the space um how is it formed yeah okay i i i got the question actually yeah um problem is i don't have a good answer to that so i don't have a good intuition for why we need the values at all uh why can't it be just x that is a good yes yeah that that is a good question uh i guess like the superficial answer is that well i mean still every attention head is trying to highlight some aspect of the input and uh in terms of the values also we want to kind of um how to say this we want to uh highlight a specific like um um projection of of of the big vectors x and we want to simplify them to to highlight this thing that we are looking for with this specific these specific queries in these specific keys, but that's not really a satisfactory answer. I think the true answer is over here. And the true answer is if at the, so like, what does the value vector define it? What does the length of the value, where does the length of the value come in? What is its importance? The length of the value vector defines the length of the output, the size of the output, right? So your output is a combination of Vs. So the length of Z of the one is the same length as the length of V. And I guess it would be, it just wouldn't make sense. It would be too inefficient and too many weights, et cetera, to have many X sized Zs and then combine them together and compress them back down to a single X, okay? So I guess that's just an efficiency thing. So yeah, we could just use X as the document, but I suppose this would make this multi-head attention too difficult and we really want multi-head attention as I just explained. Does that make sense? - It's a bit confusing, but I don't think. - Okay, so let me go through this slide. Maybe it will be a bit less confusing. So we have actually several multiple of these attention heads, okay? We have head one, head two, head age. And when we have head one, head two, head age, every one of them gives us this set of Zs, the matrix Z, which is this Z that is in the boxed formula here, right? But now we have multiple such Zs and we need to combine them together. And after that, now the output of this step, now it has to match the input size. Well, it doesn't have to, but it does. It usually does in practice, just so that we can make another layer exactly like this and we can just copy the layers. So this matrix Z at the very end, at the top right of this, should have the exact same size as the input matrix X. But the intermediate representations, they are much bigger. So let me maybe just briefly draw it here since this is not that easy to understand. So we have this one matrix X, which is like a capital D times L. L is the number of vectors, D is the vector size. And this goes through attention head number one. Attention head number two, blah, blah, blah. Attention head number H. And this one gives you a matrix Z1. This one gives you a matrix Z2. This one gives you a matrix ZH. And these guys are, what's happening here? Recording in progress. Sorry, I don't know what's happening here today. Like all problems combined. Okay, so we have multiple, we have multiple attention heads. And every attention head gives you a new matrix Z, a different matrix Z. And now we need to merge them all together. So every one of these matrices is like a small d times L matrix. But then when you string them all together, Z1, then Z2, then ZH, you get a pretty big matrix. So if you just concatenate them like this, no, shouldn't, okay. So let's say that this is L times D, not D times L. Now I will concatenate properly, L times capital, yeah. So when I concatenate them together, I get the matrix, which is still L in terms of the rows, but now it's L times H times D, and H times D is probably bigger than capital D, and it's a lot. So what we do here in the transformer, we multiply it by another matrix of weights, so it's like just a feedforward layer, we mix up all the features again, and this feedforward layer gives us the matrix Z, so this is the matrix of size H times capital D, something like this. So my intuition for this is that we really, first of all, we need some variety in these Zs, we need more variety, not just linear combinations of the same vectors with different coefficients, but different projections of these vectors. This gives us more variety and more expressive power. And two, if we just had this small d equal to the big D, now this guy would be just infeasible to train, it would be just too big. So I guess this combination of two things that we wrote here. I understood your intuition. Thank you for drawing. It was clear. Thank you. All right. So what we have here is one attention head copied multiple times, several attention heads. They are all processed in parallel. And as the output, we get this matrix Z. And this, if we look at where we are now, we have explained, we have expressed exactly this one self-attention layer on the bottom left. This first self-attention layer from the first self-attention layer from the encoder. But notice that it's basically almost all that we need. So what's left? First, what's left is... Okay, so first let me go through the must self-attention in the decoder. And actually let's talk about the decoder. So we are completely done with the encoder part. That's it. Self-attention we've just described, then layer norm we know, feed forward just one matrix to mix up the weights we know, to mix up the representations we know, that's it. In the decoder there is more stuff to think about. So what is masked self-attention? What does it mean? Well, actually I don't even want to explain it in detail because that's a pure efficiency thing. So like when I draw a picture like this one where the decoder is only predicting the next token, there is actually masked self-attention is just self-attention. That's it. So we have the current state of the prefix. It's on the bottom right. We have the current state of the prefix. It goes into self-attention. It's just exactly the self-attention that we just described. Where the masks come in is that how do we train a language model? How do we train... Let me explain it briefly. How do we train a transformer decoder or the whole transformer with encoder and decoder? We have this output, right? So this is like the sentence that we need to produce. And in terms of the transformer decoder, this output sentence is like 1, 2, 3, 4, 5, 6, 7 actually different training samples. So the first training sample is you produce v from nothing and from the representation from the encoder. The second training sample is from the prefix v you are supposed to produce cat. The third from v cat you are supposed to produce set and so on, right? So it's like the decoder should be run seven times here. It produces six words and then it should produce like the stop talk and the talk and it's done. And you can do it formally, you can just do it as seven different training samples. But of course, it's inefficient. So in practice, what you do is you just you take this one sequence. You'll say that, OK, I'm supposed to produce. So I have this decoder in the transformer. I have all of the inputs available here. I have all of the outputs here. And then I'm supposed to have the here, cat here, blah, blah, blah. And this top token here. And this is where the masks are needed. Because of course, when I'm producing the word cat, this computational path is not supposed to look anywhere except to the word z. So I need to mask out all of the other tokens. Otherwise, it wouldn't be much of a problem. I just need to copy the input to the output. Of course, there would be nothing to do then. So the masked self-attention layer, what it's doing is it's blocking all of the tokens except it's called causality. It's called causal masks because it preserves causality. So token number T can only depend on positions of one zone to T minus one. And yeah, it's some work in terms of the programming of the implementation of the self-attention. So basically you need to like zero out the weights that are not supposed to be there. Like when the input has everything now, but when you are producing Z2, you are supposed to have this attention weight to be exactly zero and this attention weight to be exactly zero. And you are supposed to only look at the first token. That's what the masks do. So this is the mask self-attention part. And then the encoder-decoder attention part. How does this conditioning work? We are looking at the same self-attention layer, but now we also need to somehow have the Z inputs. The inputs that are produced by the encoder. Otherwise, what's the point of having an encoder? And it sounds like you would need to do something even more complicated. You would need to change something here because now there is this whole new input and stuff. Actually, no. Actually, it's very, very simple. The self-attention stays exactly the same. This picture stays exactly the same. There is only one difference. In encoder-decoder retention, your prefix, your X, the input from the decoder produces the queries. You multiply it by WQ and you get the matrix Q. And the keys and values are produced from the representations from the encoder. So W, A, W, V and you get the K and V matrices. No difference to this processing at all, but now the only difference is over here. We are not producing all three things from the same X. We are producing the Q thing from the X and the K and V thing from the condition. Notice that it doesn't break anything. So over here, I told you that this attention matrix is a square matrix of size L times L, N times N over here. Well, now it's not quadratic anymore. So now there is a different number of queries and keys. Obviously the length of the sequences will not be the same, but that's okay. We never assumed that we had the same number of keys and queries. For every query, we multiply it by all keys. So we get as many attention weights as there are keys. So the number of keys should match the number of values, naturally. Because then we add up values with these coefficients. But the queries can be completely different. And actually we will later when we discuss, for example, object detection with transformers. We will see that there are also queries and keys and values will be some very different things. They'll be produced from very different things. So it's a common idea in transformers to have queries come from one source and keys and values to come from another. And yeah, it dates back to the original transformer. In the original transformer decoder already, this is how we use the outputs of the encoder. Okay, so that's basically it about the architecture. That's it about this picture. Are there any questions at this point? Because this is, I think, the most important architecture in the world right now. So yeah, it's a lot to process. I don't expect you to internalize it right now, right from my words. But when you think it through once again, when you go through the pictures once more, and especially if you ever actually implement it, then I guess you will get an understanding. It's not that hard. It's just pretty abstract. So there is nothing tangible about what is a value vector. It's just a projection. It's just a good projection that we train for the input vectors. And what are these input vectors? Well, they are some abstract representations of the tokens. So there is not much intuition that I can give beyond what I already tried. But actually, surprisingly enough, the actual attention heads that after training will often do some very understandable, very interpretable, very intuitive things. Maybe if we have time, I will show you some examples later about this. Not too late. And there are, I guess, two more things to talk about. So first, let me maybe show you an example. To be honest, I have only some pretty trivial examples here. Pretty trivial examples. I have this... Okay, let's not go through the code. We have practical sessions for that. But I have this one layer and one self-attention head. And what it's supposed to do is it's supposed to output the matching key, so to speak, for the input. And if you look at the attention matrix, you see that it does... For this attention head, it does look in the correct spot. Basically, that's it here. And here is another kind of abstract example. It's an example to illustrate that the attention matrix, the matrix of attention weight doesn't have to choose a token. So if you look at something like this or some sample matrices like this one, they quite often look like a permutation matrix, right? They quite often look like, well, for every input we match it to some output, to some other input in this case, and we encode their mutual relationship right now, like between token number i and token number j. Well, it doesn't have to be this way. There can be more complicated sets of attention weights, like you can have, for example, an orientation matrix that looks like this, where these tokens, these queries, look at all the tokens. So in this example, all tokens are split into groups. There are four groups. They go one by one, like three tokens, group of three tokens, group of three tokens, then group of one token, and again group of three tokens. And they are supposed to look at each other uniformly. So that can also happen, right? You can have this widely distributed attention where one token just attends to all of the tokens, for example. We'll see probably examples of this. Okay, and two more things that I need to talk about. So first, maybe one word on tokenization. It's not really our subject because we are talking about computer vision and in images it will be quite different. But I just wanted to mention because it's a nice connection to completely different areas of computer science to coding theory and Huffman coding and stuff. But where do you get your dictionary from? It's a pretty interesting question because when I explain it to you intuitively, it makes sense to say that just a token is a word in text. But in reality, you can't have tokens to be equal to words because there are too many words. Because in a language, I mean, you can't just lemmatize everything and have all of your words lose all the grammar that would lose a lot of information. So different grammatical forms have to be separate words. That's one. And two, in reality, there are typos. And if you add typos, so again, you are not allowed to just drop everything that's not in the vocabulary because then many texts would not make sense and you would lose, again, a lot of information. But if you add all of the words with typos there, oh, my God, the dictionary will be huge. You will have millions of words in the English language. So we need something smaller. We need a smaller vocabulary. And, of course, we could just start with characters. So you could have, I mean, you could view text as not a sequence of words, but a sequence of characters. This is, for most languages, this is a natural way to partition the text, right? Also, it's a sequence of characters. Now, this, on the other hand, is too fine granularity, right? So, yeah, characters, there are a few characters, at most a couple hundred. Even if you count all the punctuation marks, capital letters, etc., etc., like 100, 200 at most. And, of course, you can train, you can have a dictionary of several hundred vectors, your embedding matrix of several hundred vectors. But now it's too little because now it means that your sequences get too long. So, again, remember that, for example, now a practical limit on the context size is something like a million tokens. And there is a big difference if it's a million words or a million letters, right? And, of course, you would want to be closer to a million words than a million letters. So how do you go in between? How do you choose which tokens to use, which sequences of characters to assign tokens? Well, it turns out there is a pretty beautiful algorithm for that. It's called BP, byte-pair encoding. And it's commonly used throughout machine learning. And interestingly, it has nothing to do with learning. It's all just Huffman coding from Shannon's information theory. So, how does it work? Well, suppose you have some kind of dataset where you have these words. I specifically chose words that have many similar letters and substrings. And here are the letters that appear in these words. And let's assume that these are the frequencies of the words. So, these are the frequencies of the letters. Now, suppose that I can add one more token. What do I do? Well, adding one more token means that if I start with characters, I can now take a pair of characters and I can call this pair a single new token. So, which pair do I choose? Well, let me list all of the pairs that actually appear. And let's just choose the one that appears the most. So, in this case, obviously, the @ appears everywhere, almost everywhere. So, it's very, very common, has a high frequency. So, let's call @ a new token, a new symbol. Let's call it capital Z, whatever. And now my words look like this, right? So, I replaced every @ by this Z. And, yeah, of course, I cannot delete A and T from the vocabulary because T can occur without A, for example, right? But still, I have reduced the length of my words. I have added one new token to the dictionary, and I have done it in the optimal way, basically. And then I just repeat this. So, now I have this new vocabulary of tokens. They have these new counts. I needed to update the counts of A and T. Now that's different. So, I have this new set of pairs. Also, I don't need to update the whole thing, but I need to update the pairs where there was an A or a T. And that's how we work, right? And then we can choose another pair of tokens and replace those by capital Y and so on and so forth. So, very simple algorithm, very straightforward. And the beautiful part is that you can stop it at any time. Yeah, absolutely. It's from that part of computer science, I agree. And you can stop it at any time. You can say, okay, so let's say I have a capacity for a vocabulary of size 100,000. Well, so that's way too much to have just characters and way too little to have complete words. So I just run this until I reach, I add tokens one by one, so I can just reach exactly 100,000 and stop. And if you do it, you will see that, for example, first, it will find common, frequent parts of words like -ed because it's at the end of every verb in past tense, or -tion because it's at the end of many nouns and so on and so forth. And then, of course, common words will be single tokens, uncommon words will be multiple tokens, and that's okay. So that's how tokenization works. And one more very interesting remark, this will be the last that I have time to say today, one more very interesting remark about transformers is that because they are so cool, because they have this wonderful ability to go from any token to any token in one step, this is their biggest strength. But it comes with a funny drawback, with a funny defect. Transformers lose word order, so in the recurrent network there is a very meaningful sense in which there are adjacent tokens and tokens that are far away, because between adjacent tokens you go in one step, if they are far away you go in many steps. Very natural, you don't need to remind the recurrent network about the word order. And transformers, well, it's just a matrix, right? If you look at this matrix of attention weights, it doesn't, like, just a generic matrix doesn't care if these rows are adjacent or these rows are far apart. There is nothing that changes because of this. So transformers don't care about word order, and that's a bad thing. We do want to keep the order, right? So what we actually do in practice is we add to the embeddings of the tokens, we add special vectors called positional encodings, whose only job is to encode where exactly this token is in the sequence. And it's kind of a topic in itself, which I don't want to go into. Let me just briefly hint at the main idea. The main idea is this: you could have an embedding that just has one hot representation, that here is position number one, number two, number three, number four. But what you actually want is you want these positional encodings to have some kind of arithmetic on them. So you want your positional encodings to, if you have a vector that represents position one, so let me maybe briefly write it here. If you have a vector that represents position one, e1, position two, e2 and so on, you want them to capture these differences, the distances between tokens. So you want like ei minus ej as a vector to be somehow similar to ei plus k minus ej plus k. So you want like if the tokens are three, if two positions are three tokens apart, you want the differences between their encodings, position encodings to be the same across the whole sequence. Right. And in the original transformer, they did it with this kind of approach. They did it with this, well, basically positional. What's the English word? Positional counting system. I forget. Like there are binary numbers, there are decimal numbers. What's the general term? So let's look at how binary numbers operate. you look at the binary numbers, you see that these are just binary numbers from 0 to 15, rote in sequence, right? So like 1 0 1 2 3 blah blah blah 15 16. And if you look at what happens with the actual digits, you see that the last digit just oscillates, right? 0 1 0 1. The next digit oscillates with twice the period 0011 0011 and so on. Now we have four zeros and four ones, four zeros, four ones, eight zeros, eight ones and so on. That's how binaries work. And you can do it, you can do like a soft version of this. You can have like sine waves in different positions of the encoding and you can start with sine waves that oscillate a lot with high frequency and then just reduce the frequency. And this will be like this positional system for counting that will give you the necessary properties. So this was the original approach to positional encodings and the current approach, I think the one they mostly use today, is called rope, rotary positional encodings. And rotary means that something is rotating, there is some kind of circular motion. And basically in rope what you do is this: you take your vector x and instead of considering its components one by one, you consider them in two by two. So you break x into pieces of two numbers, like two-dimensional vectors. Okay, so this will be x1, x2, this will be x11, x12, this will be x21, x22, and so on. And every two-dimensional part you can now rotate by various angles. So you cannot rotate a single number, it doesn't make sense, but a vector of two numbers, that's a vector on a plane, you can rotate it. So what the rotary encodings do, what these embeddings actually do, is they take this kind of small x on a plane and they multiply it by rotation matrices like this. I always forget where the minus sign is, maybe it's over here. And the positions are encoded as coefficients to these rotations. Oh sorry, let me write it again. I should have done this. Cosine k theta, sine k theta, minus sine k theta, cosine k theta, right? So there is like this basic angle theta and you rotate by multiples of theta, which gives you this perfect arithmetic by default. Because if you take a vector and you rotate it by k theta and then you rotate it by another L theta, then it's the same as rotating it by k plus L theta, right? Just obvious. So this also gives you this nice arithmetic and this kind of positional encodings have better properties, it seems. So I have illustrations for you here as well. This is the sinusoidal positional encoding and this is the the picture that I cannot draw on the board, but this is exactly how like this dot product between the two vectors here depends only on the distance between them on the offset i minus j and that is the property that we want. And rotary positional encodings, well here is an illustration for how they work and this is the same kind of matrix again showing that you have this diagonal structure which means that along each diagonal the distance between positions is the same and well you have the same dot product between the positional encodings. And I also have this illustration for why the square root of d is necessary but it's just a practical representation of the fact that if you don't scale you get closer and closer to one hot representations. You lose the entropy after the softmax. All right so let me stop here. We've discussed attention and self-attention and the transformer and I'm happy that I got to the end of the transformer architecture. Any questions? Okay then. Then thank you very much. I will try to I will try to produce a unified video of today's lecture. I'm pretty sure it wasn't corrupted completely. At some point just the BS Studio quit unexpectedly but I'm sure it's not corrupted completely. I'm not sure if I will be able to actually join them together. Sometimes it doesn't work but in any case I will make it available somehow. So thanks a lot and see you on Friday obviously but when the next lecture will be, we haven't yet decided. We'll talk it over. Okay see you on Friday and on Friday I will listen to your presentations. Bye-bye.
