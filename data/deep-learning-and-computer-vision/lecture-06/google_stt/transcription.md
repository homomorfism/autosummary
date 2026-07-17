# Transcript — google_stt

- **Provider:** google_stt
- **Language:** en-US
- **Audio duration:** 3:12:14
- **Segments:** 1336
- **model:** latest_long
- **use_enhanced:** True
- **latency_sec:** 1634.98

## Segments

**[00:00 – 00:02]** Good morning, everyone.

**[00:03 – 00:09]** Welcome to our next class and today's lecture day and we will discuss

**[00:10 – 00:11]** Transformers.

**[00:12 – 00:17]** This is probably the most the single most important lecture.

**[00:18 – 00:20]** in our class, but

**[00:22 – 00:31]** Before we get the Transformers nature, we need to finish what we started yesterday. The current neural networks and we need to discuss

**[00:32 – 00:49]** Attention mechanisms and then from recurrent attention we will get to self-attention and therefore Transformers and they will indeed transformed the entire field of the appearing as they did and 10 years ago.

**[00:50 – 01:04]** So yesterday we stopped at, let me see here, I don't but okay yesterday we stopped at the main problems of the current Networks.

**[01:04 – 01:06]** and actually,

**[01:08 – 01:12]** They, I didn't make this point here, so let me make it now.

**[01:14 – 01:32]** The, the main problems of recurrent networks are exactly the same problems that you have in deep networks in general, in networks with a lot of layers, like the ones we've already seen in converting in the conventional side of things.

**[01:33 – 01:33]** so,

**[01:36 – 01:43]** The problem is that the signal gets saturated, right? The signal, oops, sorry.

**[01:44 – 01:45]** Looks like my.

**[02:07 – 02:08]** so, they

**[02:09 – 02:20]** The problem like with deep neural networks, was that as you go through the layers and the specialist created go through the layers, right? You

**[02:22 – 02:35]** Start losing signal when some of the layers gets saturated. So when a layer doesn't want to train anymore it's derivative becomes 0 multiplied by that 0 and nothing below it trains.

**[02:36 – 02:55]** Well, guess what? Eric current neuron network is in a way. A very, very deep Network, right? So it has usually you think of its input as a single thing, right? But what's actually going on is when you process

**[02:56 – 02:57]** The input.

**[02:58 – 03:10]** The activations go through as many layers, actually real physical layers, neural layers, right? The trainable, it's and everything, as many layers as

**[03:11 – 03:12]** Elements in your sequence.

**[03:13 – 03:41]** So any recurrent network is like by default a very deep Network. And when people when people talk about deep recurrent networks, what they what they usually mean is like several layers of processing for the recurrences. So there are constructions like this. Like like this, this would be called a three layered recurrent Network, right? But

**[03:42 – 04:03]** In a charity, if you compare it with, or if you look at or on the level of the computational graph, any recurrent Network, even one, with only one level of cells is actually a very deep Network. It's as deep as the input sequence, which is probably right? So

**[04:05 – 04:46]** So the problem was exactly the same as you go back with the gradients or as you go forward to the activations strange stuff begins to happen because you keep multiplying by this same Matrix of weights more or less and of course in recurrent networks it's a little bit different because now you have the same weight Matrix for every cell, right? So the old share the same W and this brings us, this gives us a little more problems, but the vanishing gradients problem is more or less the same. So if your W has a spectral radius under one then

**[04:47 – 05:03]** As you go from left to right with the gradients you keep multiplying by smaller and smaller. You keep multiplying. By this number, we just list and one more or less and your vectors, your gradients think. And basically addition to 0

**[05:04 – 05:08]** And that's a big thing. And that but

**[05:09 – 05:12]** the like, the additional problem here is that

**[05:14 – 05:28]** you can notice that if you look inside your net or but from the behavior from like the graph of the loss function, you will never know. Notice it because it's not like exploding rate. When gradients explode, it means that

**[05:29 – 05:46]** Yeah, just everything is a huge mess. Nothing works right. When gradients explode you you start seeing things like numerical overflows in in your in your code and it's completely obvious that everything has broken down.

**[05:47 – 05:53]** Not so with Vanishing gradients, right? So when Vanishing gradients become

**[05:54 – 06:00]** Smaller. When you go from right to left what the search, it doesn't mean the W stop straining.

**[06:02 – 06:32]** So trains, why? Because it still participates in the last cells of the network, right? So even if your gradients become, like basically exactly zero after the second step on their way, back from those function, even if that happens, W will still train. It will still look fine at first glance because it will still participate in here.

**[06:32 – 06:34]** It will still give you some signal.

**[06:35 – 06:56]** The gradients with respect to the weight will not be zero. You will notice it by looking at the gradients with respect to W, everything will be fine, but your network will make its decisions based on the last two elements of the sequence, it will not be able to have long term memory for the rest of the seconds.

**[06:57 – 07:10]** So the actual problem with Vanishing gradients is like these guys problem from this classic Nolan movie. The networks cannot have long-term memory, they cannot have

**[07:10 – 07:22]** They cannot have this. X1 influence the output. That's step t.

**[07:24 – 07:34]** So what do we do? Well, we do exactly the same thing that we already learned how to do. With residents. We add something like residual connections.

**[07:35 – 07:46]** And in fact it was recorded networks that by nearly said. Yeah, because recurrent Network simply don't work at all without this idea and

**[07:47 – 07:50]** So, it actually originated with in the 1990s.

**[07:52 – 07:57]** In Oregon Schmidt, Cooper's group over.

**[07:58 – 08:11]** And this constructions have been known for a long time, but only in like 2015, they were actually applied to deep neural networks, because we didn't have so deep neural networks before.

**[08:12 – 08:17]** Um, and the idea is the same. You need to have like this.

**[08:19 – 08:33]** Way for gradients to flow around, multiplying them by weight matrices. So you need to have some Smith covers sometimes code at highways, you need to have a highway for the gradient to go through.

**[08:34 – 08:35]** and,

**[08:36 – 08:46]** Yes, of course, you will change what's happening on the highway but not by multiplying directly by a weight Matrix that could go to 0.

**[08:48 – 08:58]** And I will explain to you this very famous and still very important Construction. Lstm

**[08:59 – 09:03]** Which stands for long short-term memory.

**[09:04 – 09:25]** Kind of a strange name, but there we go. And the basic idea for this James is that? Yeah, yes, you do have this highway for memory to flow. So I will be drawing here one cell of the listing. So, like we are in here.

**[09:26 – 09:31]** And our inputs are the hidden State, and the current X.

**[09:32 – 09:37]** And our output should be the next hidden state, right?

**[09:38 – 09:44]** so in Palestinians, the hidden state is like artificial split into

**[09:45 – 09:54]** So of course formerly it's just a single Vector but we treat two halves of this Vector very differently so I will I will draw them as two different vectors.

**[09:55 – 09:57]** One half.

**[09:57 – 09:58]** Is.

**[09:59 – 09:59]** like,

**[10:01 – 10:03]** This long-term memory.

**[10:04 – 10:07]** This is the part that will stay.

**[10:09 – 10:12]** On the highway. This is the highway action so it will stay.

**[10:13 – 10:20]** not unchanged, we will write memory from memory Etc but this is the part that

**[10:22 – 10:32]** We don't want to multiply by weight matrices. This is like in terms that we already know this is the equivalent of this path.

**[10:33 – 10:35]** Path around the layers, right?

**[10:38 – 11:01]** And then there will be also, let's call it h, h. T a, it's just a regular quote, unquote hidden state, it will participate in everything that happens in the lstm and you will see how it gets used. And actually as the output, we will need to produce this Vector for the next step.

**[11:03 – 11:20]** So, C is kind of this long term memory and this is the correct integration. This is like a memory cell where you write stuff where you read stuff from. And like, the whole list cm is devoted to operations with this long term memory.

**[11:22 – 11:29]** And then of course we have X so we have like XP over here. This will be in first

**[11:30 – 11:32]** And what's happening inside? Well,

**[11:34 – 11:49]** Let's see, I'm consists of gates. This is also a pretty important concept because in many modern architectures, you will see some kind of gating mechanisms, you will see some kind of gates like this here, I will draw Gates

**[11:51 – 11:52]** Like this.

**[11:53 – 12:10]** Let me show it separately so there will be like this, there will be a gate for example with two inputs. I will put matrices over here. These are two inputs X and Y and then the gate itself.

**[12:11 – 12:33]** Will look like this and there will be a function over here, the activation function. And so, the output of this gate will be like f of a times X plus b times y, okay, and probably plus biased, but I will not throw the biceps explicit.

**[12:35 – 12:45]** So this is basically this one linear sell, right? So we inputs every input gets multiplied by a matrix. This will be weight matrices.

**[12:46 – 12:51]** Then we add them together and people post and throw an activation function.

**[12:52 – 12:58]** But here they will be used in a different in many different and creative ways. This kinds of gates

**[12:59 – 13:06]** So let's begin, let's see. Our first gate will be over here.

**[13:08 – 13:13]** I will call it the input gate.

**[13:18 – 13:19]** The input gate, right?

**[13:21 – 13:25]** Okay, let me draw it and then I will explain what's going on here.

**[13:30 – 13:34]** No, sorry, let's let's start with the forget gate.

**[13:34 – 13:36]** So this will be the forget gate.

**[13:38 – 13:40]** Just cleaner Picture This Way.

**[13:40 – 13:46]** So it receives this input H with the weight Matrix w

**[13:47 – 13:51]** H f right? H for hidden f for forget.

**[13:52 – 13:55]** It also receives input X.

**[13:56 – 14:02]** With the weight Matrix, double w x f, then you go here and then what happens?

**[14:04 – 14:06]** is I, multiply

**[14:09 – 14:22]** The out I'm multiply c t by the output of this gate like component wise. So its output is a vector, let me call it f t

**[14:24 – 14:28]** 50 and I multiply CT by ft.

**[14:28 – 14:58]** So let's unpack what's happening here. And then the rest of the gates will work in about the same way. So what is happening here we have this kind of linear thing that just combines H and x with some coefficients, whatever. And importantly, we pass it through a logistics equipment, we pass it through this Sigma function, this function that goes from 0 to 1 and that basically converts any score to the probability.

**[15:00 – 15:06]** So as a result, we have this Vector full of various from 0 to 1

**[15:06 – 15:12]** So it's right. It goes from 0 to 1 and there are several ways from 0.

**[15:13 – 15:15]** And actually, as a 0 and 1, not include.

**[15:17 – 15:29]** So and then we multiply it component Wise by our memory cell. So what's going on? What's the intuition? The intuition is we want to be able to erase something from memory.

**[15:30 – 15:51]** How do how do you erase something from memory? Well, you multiply it by 0, right? So basically, they forget gate, if the output is close to one. It means keep it retain the cell and memory. If the output is close to zero, that means don't keep it erase it, right?

**[15:52 – 15:54]** And that's like,

**[15:55 – 15:57]** Mostly how gates work.

**[15:58 – 16:12]** so in like modern architectures like mixtures of experts and don't think, we will have time to discuss those but very often, you will see some kind of engaging mechanism and usually it means that

**[16:13 – 16:53]** You have some small part of your network. In this case, just this line yourself producing a controller that will control what's happening with other stuff inside the network. So this is not like data, really, this is not something that I want to treat as numbers and the course it's your numbers, right? It's phone numbers inside in your network but the meaning of the vector F here at the output of this gate is which memory cells to erase. It's not some additional number that I want to multiply because I care about the multiplication result.

**[16:54 – 17:09]** That's the point of getting here. You, you cannot do like real logic gates because then gradients would not follow through right? Logic? Gates are piecewise constant and, you know, you cannot train through them but you can do.

**[17:11 – 17:18]** Some kind of continuous approximation to this kinds of gates and here, it's basically about the racing from it.

**[17:18 – 17:33]** Okay. And now that we have one gate, clear, the rest basically Falls. So next, you have next we have let's say you have the candy bit sales state

**[17:34 – 17:36]** And they sell state.

**[17:39 – 17:48]** Okay, probably don't need more space and that will come. Later can, it's all state we will

**[17:49 – 18:00]** Produce the new numbers to write down to memory, right? So this is like C Prime tip. This is something that we may want to write the memory.

**[18:01 – 18:34]** Uh, where do we produce them from? Of course, from the same inputs so we have w h c another Matrix of weights, right? And we have w x c and other Matrix of rates notice that for control controlling gates for Gates. Like the forget gate, it's important that they have the sigmoid function at the end because I do want numbers from 0 to 1 actually want them to be saturated. I want them to be either close to 0 close to one, that's the whole point.

**[18:35 – 19:01]** Here, not so much. Right? So here I just want to produce new numbers to store in memory. So here like this Sigma cannot be exchanged for something else. It's important that it's a sigma but this hyperbolic tension time, just copying it from classical HDM construction but this this is not written set and stone, this can be modified.

**[19:02 – 19:04]** and,

**[19:05 – 19:11]** So now we have C Prime. And the question is, which part of this Vector? I want to write to memory

**[19:12 – 19:18]** And guess what? There is a get to control that. So we have another gate which is called the input gate.

**[19:20 – 19:21]** Here it is.

**[19:23 – 19:26]** And now this one is a control gate with the sigma.

**[19:31 – 19:42]** And what it does is it decides which of these candidate sell we, which parts of cprime, I want to write into memory.

**[19:43 – 19:48]** So I multiply C Prime component Wise by the output of the input gate.

**[19:48 – 19:55]** And then there is a result I write into my memory. What does it mean to write something into memory? That's just addition like this.

**[19:56 – 19:57]** okay, that's

**[19:58 – 20:01]** and of course, I need to

**[20:02 – 20:05]** do it from inputs.

**[20:06 – 20:07]** w h, i

**[20:08 – 20:09]** w.

**[20:10 – 20:10]** X.

**[20:12 – 20:14]** I need one more gate.

**[20:21 – 20:39]** All right, so at this point we have, we are able to erase something from them and we are able to write something back to memory, right? So again, this plus is like, not really plus, I mean, they always TM usually does not learn to actually,

**[20:40 – 21:01]** Add stuff. It's not about this Edition, it's about writing to memory. So the main mechanism is sometimes I want to erase something from memory. So I multiply by something, very close to 0. I get a 0 in that position of CT and now when I add something there, it means I'm just writing to this. So,

**[21:02 – 21:08]** and the only remaining thing is to Define this H for the next step,

**[21:09 – 21:22]** And here I will actually look at them because the rest is very logical. And here, let me, yeah, it's hyperbolic tangent. So now, i h t plus one is actually

**[21:23 – 21:33]** Produced from the long term memory. So it's basically kind of a copy of long-term memory but

**[21:34 – 21:54]** For some reason, which I cannot really explain, it goes through hyperbolic functions over here and then and then it's a part and then we read the result from and then we read it from memory. But what does it mean to read again? It means that there will be a gate controlling, which part of CT. I want to write to HD.

**[21:55 – 22:03]** All right, so there will be another gate. Let's call it the output gate or output. Yeah, I think output.

**[22:04 – 22:05]** The output gate.

**[22:09 – 22:11]** Again, with the sigmoid.

**[22:12 – 22:12]** and you have,

**[22:13 – 22:21]** A vector here. And this Vector will decide what to read from memory for the next h.

**[22:23 – 22:24]** And again.

**[22:25 – 22:27]** W h, o.

**[22:28 – 22:29]** and,

**[22:30 – 22:32]** WX.

**[22:32 – 22:34]** That's it. Let's say.

**[22:35 – 22:45]** So, the lstm cell is everything that's in here, right? So this, this, this this is, this is the lstm cell

**[22:51 – 22:52]** and,

**[22:54 – 22:54]** It looks.

**[22:55 – 23:09]** Complicated. It's not really complicated like meaningful. I cannot explain to you the intuition behind like everything here. Maybe it's at that hyperbolic tangent. I have no idea why it's exactly that but

**[23:10 – 23:39]** I can explain to you like how things flow inside is inside an ostm and it makes sense, right? So the beauty of this construction is that it makes perfect sense. It's like a program for memory manipulation procedures. Right? There is this memory you can delete from it, you can write to it. That's it. And also you need to on the first, you need to decide what to write to it. So hence the candidate Health state

**[23:42 – 23:44]** That's how it works. And

**[23:45 – 23:46]** It actually.

**[23:47 – 23:47]** Is.

**[23:48 – 24:15]** An extremely successful construction. It's still relevant now, even though it was like constructed, I think 1995 was their first paper. And by the year 2000, they already had exactly this construction. The first construction was a bit simpler but by the year 2000, instrument covers group, they already had exactly this and ever since it just works,

**[24:17 – 24:25]** And when you build their current Network today, you will actually use the stamps surprisingly enough.

**[24:26 – 24:37]** All right, so, I don't want to spend too much time on recurrent networks. So, let me like be quick about what's coming next here. And

**[24:38 – 24:49]** the last time is the most important recurrent construction ever again. Its main meaning, is that it provides you with this straight line with this highway,

**[24:50 – 25:05]** Through which the gradients will flow without any interruptions or better to say, only with interruptions that we intend. So of course, there will be interrupted if I erase something from memory. Of course, this will stop the gradients, but that's that's how I want to.

**[25:08 – 25:08]** and,

**[25:10 – 25:14]** Yeah, and but the list here has a bit cost.

**[25:15 – 25:18]** And the cost is it has a lot of weights.

**[25:18 – 25:28]** So, if you look at all of this waitresses, you will see that they are a lot of waitresses. Right? There are in the construction that I

**[25:30 – 25:33]** drew here. There are eight waitresses.

**[25:34 – 25:52]** And they are basically. So if I X is our deprived and I think I said that this is D, so h&c are offend D. Then like half of this Matrix is are like d times D, major interests.

**[25:53 – 25:56]** And half of this matrices are D times. D Prime matrices.

**[25:58 – 26:01]** And of course you want your memory to be.

**[26:02 – 26:42]** Large you cannot have a meaningful STM with like you know, self size 2. So in reality like in practice the is something like at least to 56, maybe in small cases, something like 64 and large cases, and like a 1000 and depressed. What it is. That's your ex probably some impeding of X some representation but it's also probably on the same kind of size level. So, this are big weight matrices. And for a long time it was very difficult to train those students and

**[26:44 – 27:01]** Like everybody knew that they are cool. And in to examples, they were actually delivering very good results. But nobody could really trained a few hours here and I think it only began to be possible in like

**[27:02 – 27:10]** 200015 or so, but ever since because James are in the what what people use for

**[27:12 – 27:22]** For bigger current networks. And for example, I think to take an example, you may have heard about, I think Alpha star

**[27:23 – 27:36]** Alpha star, the Starcraft playing Network, it was actually a recurrent Network and alphastar used lstms.

**[27:37 – 27:39]** Which sounds?

**[27:40 – 27:43]** Pretty strange, right? Like

**[27:44 – 28:07]** How, how does it happen that this basically first? Okay, very smart people did it. It makes a lot of sense, but this is like the first successful attempt to build an architecture for this kind of memory manipulation stuff and it was 25 years ago and it still stands in, nobody has done better.

**[28:08 – 28:10]** That sounds unbelievable, right?

**[28:12 – 28:20]** And indeed, of course, there have been lots of attempts to do something better. So let me. Well let me not throw

**[28:22 – 28:49]** Anything new here, anything on the board? I will just walk through the slides to save time. But okay so this is this is the lstm cell that I have been growing just now forget get input gate and it's all straight output gate. These are the matrices, the formulas whatever. Yeah. So completely and its modern form. It already appeared in 2000 in the years of 1000 and

**[28:50 – 29:22]** There have been some modifications. There have been modifications, like let's add the people's. So, let's allow so like one problem of the lstm is that once you have fixed your age, all of this case do not have access to memory. So it's like you are erasing from memory, but you cannot look inside the memory to see, which are amazing, which is pretty strange. And people added like more inputs from C over here, which means even more matrices, right?

**[29:23 – 29:24]** More weight matrices.

**[29:25 – 29:32]** And at some point people try to maybe lose a few of these matrixes Maybe.

**[29:33 – 29:34]** Mmm.

**[29:35 – 30:07]** Maybe you can do without some of the gates, maybe you can like tweak their listing him a little bit and it turned out that yes for every like this. There was this famous paper called the htms respect. So it is him and basically said yeah, on our two examples where we could test a lot of illustration. You can actually like remove a whole gate and nothing much changes

**[30:09 – 30:09]** and then,

**[30:10 – 30:11]** there were

**[30:12 – 30:20]** Even better attempts. So why do we need to like so,

**[30:21 – 30:29]** Let us try to achieve the same goal. The goal of having memory that goes through this.

**[30:31 – 30:35]** How to say memory that goes through this?

**[30:37 – 30:51]** Pretty Highway of gradient flow, and let's keep it that way. But let's tweak this structure of their current cells, so that it will be more efficient.

**[30:52 – 31:19]** And people have been successful. So, for example, like the second, very famous recurrent unit is called the gru gated recurrent unit back in 2014, it was developed and if you look at it, it's very similar to the lstm but it has much less much fewer matrices. So what let me just walk you through here without drawing a separately so it still has of course the candidates well state.

**[31:20 – 31:28]** But now it doesn't distinguish between C and age, so you only have one hidden state.

**[31:28 – 31:32]** and in Stereo updating it separately with

**[31:33 – 31:39]** Erasing stuff and writing stuff. You do it all at once with the update gate.

**[31:40 – 31:49]** So basically the updated again, it's it's a control gate with the sigma at the output and it gives you numbers between 0 and 1.

**[31:50 – 32:01]** But now they are like coefficients of a convex combination. So if you look here on the right, you multiply H, the current memory state by you.

**[32:02 – 32:04]** and then you add

**[32:04 – 32:55]** These this H Prime the candidate from the that you proposed times 1 minus you, right? So it sounds like it makes a lot of sense. Right. Why do we want? Do we want to erase from memory to write something there? Why do we want to add something to memory? Because people already erased itself? And as I said, ostm is not about actual Edition, it's about racing and writing back to memory. So it makes a lot of sense to combine it into one game. And that's a that saves back to waitresses, right? And instead of the output gate, we have the reset gate, which does basically the same thing only in the same cell. And in the cell step, before it just looks at the memory and chooses, which part of it should go into the candidates hosted.

**[32:56 – 32:58]** So Gru's.

**[32:59 – 33:17]** Look great. Looks like they do exactly the same as a stms. Only more efficiently because now you have only six waitresses instead of eight or instead of 11. If you count people you don't need people now so it's more efficient.

**[33:18 – 33:20]** Should be better and so on and so forth.

**[33:21 – 33:42]** And indeed in like 2015 thousand sixteen if you look and for example papers and natural language processing, I was actually working in the field at that point and if you look at the papers on NLP, back in 2015, they all use chariots. They all switched the chair use and that was a big thing, etc. Etc.

**[33:44 – 33:44]** and then,

**[33:46 – 34:04]** for some reason, we cannot explain to you theoretically the whole field switched back to stems. So I mentioned Alpha star. How fast are? I don't remember the year, but of course, it's much later. It's like 2020. And if you have a current Network now,

**[34:05 – 34:08]** Probably it's more likely to be an lstm energy area.

**[34:09 – 34:27]** Somehow Schmidt, Cooper's construction is better and I'm sure the actual like decision making here is just, empirical, you're just saying, oh, okay. We've tried a list James. We've tried Jerry. So it's James for better. We can wear the costs, so, to speak with you. So, let's chips.

**[34:28 – 35:11]** Are, but why they are better? I have no idea. So like, what's what's so special about the lstm architecture? I don't know. But it's really interesting and it's really beautiful that it stands for so long. And remember all through the class, I was from time to time. I was mentioning stuff like, oh and then Google came and they had lots of compute and they ran this big neural architecture search. And now we have efficient net, which is better. Or now we have swoosh which is a great activation function and then people did something else. But at the point it was the best. And so

**[35:12 – 35:27]** Well, of course, they tried it with the current cells. Of course, there is a paper from Google, where they develop, exactly, this kind of thing, they tried to make recurrent cells more efficient.

**[35:28 – 35:33]** And yes, on the examples on the data sets where they test.

**[35:34 – 35:42]** Their occurrence cells, are better than lstms and Jerry use. And here is an example of their cell.

**[35:43 – 35:54]** Of course, we won't go through it. But as you can see, it has only four weight matrices. It's kind of similar to jru but it's even better. It's even more efficient.

**[35:57 – 35:59]** And nobody has ever heard about this sells.

**[36:00 – 36:18]** So most probably they don't work as advertised or I mean they don't I mean I'm not saying Google is lying. I'm saying they probably work on those examples where they were developed by the dungeon generalize to other situations and for some reason istream is still the best. It's still it's still stands.

**[36:20 – 36:20]** Okay.

**[36:22 – 36:22]** so,

**[36:24 – 36:28]** With this, I think I want to end.

**[36:29 – 36:32]** Our discussion of recurrent networks specifically.

**[36:34 – 36:37]** If there are any questions now is a good time. I will.

**[36:37 – 36:39]** Show you an example here.

**[36:41 – 37:15]** Um, yeah, so I have some, some code for today, not very deep, not very difficult, but I hope more interesting code will be in the practice session. So, this is just an illustration that of exploding convention gradients. It's, I mean, it's not even a real recurrent Network, it's just shows you that if you keep multiplying by a number less than one urination, if you keep multiplying by a number greater than one, you explode.

**[37:16 – 37:19]** And here is the real experiment.

**[37:20 – 37:20]** So,

**[37:21 – 37:35]** This is the classic lstm Benchmark from very long ago from right transmit Huber and it goes like this. You have an input of with two components.

**[37:36 – 37:45]** So they are like two input channels. One is just a set of numbers. It just goes just random numbers from 0 to 1.

**[37:46 – 37:48]** And another is a channel of zeros.

**[37:49 – 37:51]** With exactly two ones.

**[37:52 – 38:13]** So like here is a sample input, the markers show. The bars show, this random values that go between 0 and 1 and the Stars Mark the ones in in the market channel. So it's like a vector alone, stream of numbers and two of them are highlighted.

**[38:14 – 38:20]** And the question is at the two highlighted numbers? Give me the sum of two highlighted numbers.

**[38:21 – 38:21]** so,

**[38:22 – 38:29]** It's like a perfect toy test problem for memory, right? You need to when when they

**[38:30 – 38:42]** when the market Channel tells you to, you need to memorize this value and then when it tells you again, you need to add this value to MoneyGram price.

**[38:43 – 39:03]** And sure enough, let's DMS and Jerry use they both work well on this. And this is actually since it is so simple. This is actually a good example for junior used. Not always teams. So here, you will see that like a simple linear and doesn't work.

**[39:04 – 39:10]** It just like it it stays on the Baseline, which means no no training at all.

**[39:13 – 39:14]** Lstms.

**[39:14 – 39:46]** At some point, get what they are asked to do and they start learning, but in like 600 steps, they 630 iterations. They didn't yet, trained and Gru's have trained much faster and from, from a much earlier point. So this is the kind of plot that you would see convincing people that your user better. But this is a very easy problem, right? So, that's the point for a very easy problem. Of course, a more efficient,

**[39:48 – 39:49]** Cell will be better.

**[39:50 – 39:54]** But probably doesn't scale to really difficult problems.

**[39:56 – 40:01]** And yeah, and here is another sample from the, from the lstm.

**[40:02 – 40:13]** It's the same problem. It's just I take one of the inputs here, is the input. And then I look at what is actually the contents of memory.

**[40:14 – 40:27]** What are the outputs of the gates? And what is the current projection of the sum that you what is like, you're running? Guess what? What would be the output if your sequence stop right now?

**[40:29 – 40:31]** and as you can see it, rained lstm

**[40:32 – 40:51]** That's some very reasonable stuff. So it when it sees a star when it says a marker, the thing that it writes to the cell actually spikes. So, you write a lot of stuff here and you don't write much over here and your cell just

**[40:52 – 41:04]** Grows to the correct value. That's it. So if you take your running, guess then it indeed tracks. The true sum, and it goes to the truth after the second time.

**[41:05 – 41:14]** So it works. It's a very simple problem, but they but interesting there and this the interesting part here is

**[41:16 – 41:18]** Straightforward. Recurrent networks. Cannot do that.

**[41:19 – 41:34]** They, if you have just this linear, sell you simply cannot have this long-term memory that goes back and recalls at, oh, yeah, I had that number 15 Steps ago. Now I need to edit the present.

**[41:36 – 41:40]** And that's that that's the idea behind all of this current cells.

**[41:41 – 41:43]** Okay, so any questions about this?

**[41:49 – 41:50]** All right.

**[41:51 – 41:54]** well, with that, we go to our next topic and

**[41:56 – 42:03]** our next topic is probably the last time in class, when I again,

**[42:04 – 42:25]** Start from a neurobiological motivation when I again, tell you about the brain and everything. But now in a very superficial way, now we don't go from from a bird's eye view. We don't go to the details of how neurons operate we actually just stay on the level of, you know, how we think in general.

**[42:26 – 42:48]** And we are interested in the notion of attention and if you think about attention, like, I hope that you are paying attention to me right now even though I didn't really not sure. But, you know, if, but if you think about how how attention works and especially how lack of attention works,

**[42:48 – 43:05]** It's it's really funny thing. It's really unclear, how it's supposed to work. It's it's very like our brain seems to work very differently from in this regard, from how networks that we have seen so far official on your own networks work.

**[43:06 – 43:07]** so, like

**[43:08 – 43:15]** think of okay, we are in the computer vision class, so think of an image

**[43:15 – 43:26]** Think of looking at an image and, you know, registering some stuff some objects that are on the same as etc. Etc.

**[43:27 – 43:29]** I told you that.

**[43:30 – 43:30]** Our.

**[43:33 – 43:48]** Our visual cortex, the part of the brain. That processes images is kind of similar to convolutional networks at least in spirit. Like they cannot really be similar in architecture but in spirit it's it's like extracting local features then combining them to

**[43:51 – 43:56]** better to more Global features to semantically richer features Etc.

**[43:58 – 43:58]** and,

**[44:00 – 44:15]** But if I look at an image like right now, I am looking in my computer obviously, but my field of vision is, of course, much wider than just a computer. So if something happens,

**[44:16 – 44:22]** The outside of the computer and right now, I'm like thinking about our lecture and I'm writing something on the board.

**[44:23 – 44:26]** Most probably I'll miss it, right? Because I'm not paying attention to that.

**[44:27 – 44:30]** and paying attention to the board and but

**[44:31 – 44:35]** the stuff that's outside is still in my field of vision.

**[44:36 – 44:43]** So if you try to map this kind of attention thing to how neural networks work,

**[44:44 – 44:46]** It's, it's really strange. So

**[44:48 – 44:50]** when, when you go with a convolution over,

**[44:51 – 44:52]** An image.

**[44:52 – 44:58]** Of any size you get features extracted from every part of the image, right?

**[44:59 – 45:00]** and,

**[45:02 – 45:38]** Then this feature on next layers, they get combined into more Global features and showed you some some pictures yesterday. It's etc. Etc. And there is no place to lose stuff there, right. If I have a future image, okay? I will need to spend more compute, but it's not like I'm gonna lose some object from there. I will still extract features from every part of the image and they will still become binding or Global stuff and I will still have this. I don't know. Take the cat neuron up there that will steal. Activator on the cats. It's not like a conventional Network can just missed the cat.

**[45:38 – 45:40]** Completely impossible.

**[45:40 – 45:41]** But we do.

**[45:42 – 45:45]** What's the difference? The difference is an attention mechanism.

**[45:46 – 45:52]** And how it works is, actually a pretty difficult question. There was this guy Alexander Lurie?

**[45:54 – 46:22]** He was a very interesting man, very if you had a very interesting career because it was the 1930s 1940s, he lived in Sterling structure but still he was like a man of the world. He traveled to all the conferences he published in all of an international journals and he was like one of the international recognized fathers of the field of neurobiology

**[46:23 – 46:24]** and,

**[46:25 – 46:35]** Alexandra when he posted the main research program of neurobiology and general. He said that there is like three

**[46:38 – 46:40]** There, there's like three.

**[46:44 – 46:57]** Three, three, three, three, three, three, three, three three. Sorry, there are three main pillars. Three main components to the field of neurobiology and she said it's attention memory and cognitive functions which is basically like how we think.

**[46:58 – 46:58]** so,

**[46:59 – 47:03]** To him. And to the whole field of neurobiology attention is up there.

**[47:04 – 47:08]** And the level of memory and cognition.

**[47:09 – 47:25]** Well, of course, since Laurie, there has been a lot of progress, we kind of understand how attention works in the brain, but it's not really important for us from the computer science point of view, because in the brain attention works for memory more or less, it works for memory.

**[47:27 – 47:27]** There is.

**[47:31 – 47:42]** There are different types of memory in the brain. So there is this kind of working memory, which is very short term memory that stores, just a few latest objects.

**[47:43 – 48:18]** Like if we were offline in class, I would be able to demonstrate. So if you if you give a lecture and if you ask any person a personal who is not paying attention to you at all like this person is on on their phone chat with somebody Etc. But if you asked if you suddenly asked this person, tell me what they just said even if they were not paying attention at all they would be able to recite the last five words or so they would say oh yeah, you were just saying what it would be, right?

**[48:19 – 48:33]** But if you ask what I was saying 30 seconds ago it would be a blank right? So like working memory, is this very short-term mechanism of what's happening just now and mostly everything goes there?

**[48:34 – 48:36]** But then there is this.

**[48:37 – 48:56]** But then there is this filter, this filter of what goes to be processed in more, like, which parts of this recent stuff are actually important to process further and that's where stuff gets lost.

**[48:57 – 48:58]** So yeah.

**[49:00 – 49:00]** and,

**[49:02 – 49:52]** I won't spend more time on attention neurobiology Etc. It's an interesting topic but I think it's for us it's it's more important to go further if you've never seen. So I will just recommend you one thing. If you've never seen this video, where there are two teams of players, passing basketballs play a team on White and the team and black and you're supposed to count the passes of the team and white. If you haven't seen that video, please see it when I publish the slice. Okay, I can copy it here. Yeah, look at the test. It's interesting if people still fall for it because back in the 1990s, people definitely fell for it now. I'm not so sure, the our attention mechanisms have changed a little bit

**[49:54 – 49:55]** Anyway.

**[49:56 – 49:58]** So attention mechanism. So

**[49:59 – 50:02]** neurobiological works on attention.

**[50:04 – 50:04]** Actually.

**[50:06 – 50:17]** Show that even if you're looking directly at some stuff, this, this video shows that if you're actually even looking directly at some stuff, you are still.

**[50:20 – 50:24]** You are still not really.

**[50:26 – 50:34]** You still don't have the process. It it still may be lost. You still may like very early in the brain. You can decide to drop it.

**[50:35 – 51:00]** But also there is another thing we should probably have heard about and our it's it's about our vision in general. And our vision also kind of doesn't process the whole field of view. He probably know that you have this for real Spotlight. We have this small part of our field of vision where we look

**[51:01 – 51:18]** Well, where we can see stuff, very, very clearly in high definition and then it gets blurring and blurry, right? And we don't notice it because our guests constantly wanders around. Even if you're looking at your computer, still your constantly like

**[51:20 – 51:28]** it's called security motion your case constantly shifts and you look you get different Snippets of the whole picture and then your brain just kind of

**[51:29 – 51:43]** Constructs the whole picture from this small, from these relatively blurry components. So, like it's like different, several photographs of the same scene, but the focus is on different parts.

**[51:45 – 51:59]** Ah, and the original motivation to add attention, mechanisms to deploying was to, actually emulate this, to emulate how we see things to emulate this blurriness in the peripheral vision.

**[52:01 – 52:15]** And then of course sounds very strange. Why the Refuge you do that? Why would you make things blurry? If you don't have to in computer vision and conventional Network? You can just put in the whole picture. You don't need to blur anything. Why would you want to do that?

**[52:16 – 52:28]** In our eyes. I mean of course they have a wolf to to do stuff and maybe they didn't have the energy, the capabilities to that. But why do we need to compute computers?

**[52:29 – 52:40]** And the answer originally was to, to save weight to save input size to make it more efficient. So if you have a big image,

**[52:42 – 52:58]** And if you can actually instead of looking at the big image and you can actually do like three Snippets of the Big Image where you only actually use the pixels from a small small. If you small parts of the same image,

**[52:59 – 53:05]** Ah, and then the rest can be blurrier what it means to be blurrier. It means there are fewer pixels.

**[53:06 – 53:19]** Right? So the input size becomes smaller and much smaller actually. And if you have like three glimpses and everyone is just looking at a small part of the input, then of course, even the total input size will be much smaller.

**[53:21 – 53:46]** So originally people wanted to save processing by doing attention mechanisms. And the new thing here is that now you in addition to just recognizing stuff in addition to doing your classification problem, or whatever, from this blur images, you also need to choose where you look,

**[53:47 – 53:50]** So, you need to choose the positions of the glutes.

**[53:51 – 53:51]** and,

**[53:52 – 53:59]** these positions have and this positions,

**[53:59 – 54:00]** they form a sequence.

**[54:01 – 54:02]** Right.

**[54:02 – 54:21]** So this becomes a sequence problem because the next glimpse of course, can depend on what you see in the previous groups, right? So first, you okay, your first position can be chosen somehow generally, but then your second position will depend on what you've seen in the first one, right?

**[54:23 – 54:28]** So, early models of attention were current, there is this field of recurrent visual attention.

**[54:29 – 54:37]** I won't go into details because that's not too relevant now now it's all very different but

**[54:38 – 55:07]** More or less. The point was, you know, let's look at this picture more or less. The point was given a relatively big picture. Let's walk around it and choose where to look and blur the rest. And then you can actually be more accurate while being more efficient. And there is a recurrent mechanism in choosing this subsequently but yeah, this this is our date, you know, have to learn that.

**[55:09 – 55:14]** What is more relevant and more interesting?

**[55:16 – 55:18]** As what happened with attention.

**[55:19 – 55:23]** at the point where attention,

**[55:24 – 55:27]** Go to apply it to encoder decoder mechanisms.

**[55:28 – 55:39]** So let me yeah, let me first. Okay, so let me go back to the board because now I do want to explain stuff and let me first.

**[55:40 – 55:41]** Explain to you.

**[55:42 – 55:45]** What the problem is. So

**[55:46 – 55:48]** Let's first lstm.

**[55:49 – 55:51]** And now our second.

**[55:52 – 55:55]** Part for today is encoder.

**[55:57 – 55:57]** Decoder.

**[55:59 – 56:00]** With attention.

**[56:05 – 56:10]** So what what is the problem that we are solving well?

**[56:12 – 56:31]** Let's Okay, let me motivate this with machine translation. We, I mentioned machine translation before and it sounds like a perfect problem for recurrent encoder decoder, architectures. So you have your input which is like Hello World.

**[56:34 – 56:38]** Exclamation marks, okay. You read.

**[56:40 – 56:40]** Your input.

**[56:44 – 56:45]** This gives you some kind of

**[56:48 – 56:53]** hidden State and then the last hidden state, or maybe the last hidden state.

**[56:53 – 57:01]** Pushed through some kind of output head. Whatever gives you this vector.

**[57:01 – 57:10]** Let's go with Z, this intermediate representation of the inputs of the input. Sequence of this sentence,

**[57:12 – 57:14]** And then you take this Z.

**[57:15 – 57:16]** and,

**[57:16 – 57:19]** You decode it into.

**[57:20 – 57:24]** The output down, you know, English and Russian. So let me write it premium.

**[57:26 – 57:27]** Comma.

**[57:30 – 57:30]** Here.

**[57:34 – 57:36]** Exclamation mark, something like this, right?

**[57:38 – 57:50]** And and probably want to so yeah so probably doesn't look like this. Probably you have a hidden State over here H. Prime and Z is just the input to every

**[57:52 – 57:57]** To every cell. So probably the recurrence decoder looks like this.

**[57:57 – 58:02]** and when people did this, when people,

**[58:03 – 58:12]** had the compute to train vehicles and they actually try to apply list James engineer used to, with this kind of

**[58:14 – 58:18]** Architectures to say machine translation.

**[58:20 – 58:20]** They?

**[58:22 – 58:24]** Realized that they have.

**[58:25 – 58:30]** An unsolvable problem or at least an a problem unsolvable in this kind of architecture.

**[58:31 – 58:31]** So,

**[58:32 – 58:32]** Yes.

**[58:33 – 58:38]** This works, this defined state of the art in 2013 or whatever.

**[58:40 – 58:43]** And this actually gives you.

**[58:46 – 58:53]** Good results, with short sentences, a sentences like Hello World, it will work. Great.

**[58:55 – 58:57]** But you cannot scale it up.

**[58:58 – 59:01]** So, here is the thing.

**[59:01 – 59:06]** the main problem of of encoder decoder architecture is like this,

**[59:06 – 59:08]** Is in the dimension.

**[59:09 – 59:13]** Of this intermediate representation Z.

**[59:15 – 59:20]** and the problem is, you cannot have a good Dimension, it will be either to smaller to be

**[59:21 – 59:24]** if you have a c which is too short,

**[59:25 – 59:50]** He is too small. Then everything will trade, everything will be perfect, it will run fine, but you will not be able to fit a lot of meaning, a lot of information into a small Z of course. So for hello world, it will work. But of course I'm not talking about putting War and Peace inside a single Vector, but even for a long sentences, it will start to break down.

**[59:52 – 1:00:05]** And if you try to fix that by making the longer by extending the further and further and further, then it becomes harder and harder to train, right? So if you have a long day,

**[1:00:06 – 1:00:12]** It means that you're hidden state in the stems or your input to the decoder unless jams.

**[1:00:13 – 1:00:14]** Will become longer and longer.

**[1:00:16 – 1:00:20]** And that means you have quadratically more weights.

**[1:00:20 – 1:00:25]** And now, you don't have enough data and enough compute to actually train them.

**[1:00:26 – 1:00:26]** so,

**[1:00:28 – 1:00:44]** This is like a problem that you can't really solve inside this architecture. You can have either. You can either train. You can either have a good encoder decoder.

**[1:00:44 – 1:00:46]** It was to him with.

**[1:00:46 – 1:00:56]** Small disease or but but it won't scale up or you can have a large Seas, but then the training will be impossible.

**[1:00:57 – 1:01:00]** so in, in architectures like this,

**[1:01:01 – 1:01:07]** If you look at the graph of like, I don't know, whatever quality.

**[1:01:07 – 1:01:15]** I'm abstract here but some kind of quality metric and this is like tea, the sequence length.

**[1:01:16 – 1:01:27]** The input outputs in sequence length. What you actually see is like, it's very good while we have short sentences and then it just drops and it's very bad.

**[1:01:28 – 1:01:32]** And what you would want ideally. So of course, as

**[1:01:33 – 1:01:46]** Sentences get longer. You will need the quality will drop? But of course, you would want your graph to look like this, right? You would want it to to drop gracefully and still work for longer sequences.

**[1:01:49 – 1:01:58]** So this is what attention mechanisms for in order to order the current networks for suppose to fix.

**[1:01:59 – 1:02:02]** And this is an important concept that I think is still relevant.

**[1:02:03 – 1:02:07]** So, what is the problem with zip?

**[1:02:08 – 1:02:13]** Like where do we get this idea for this attention mechanism from the problem? We see

**[1:02:14 – 1:02:16]** Is that it's only one vector.

**[1:02:18 – 1:02:20]** For the whole input for the whole sequence.

**[1:02:22 – 1:02:23]** And this is what we need to change.

**[1:02:24 – 1:02:29]** And in Transformers also, there will not be a single Vector for the whole input.

**[1:02:30 – 1:02:30]** because,

**[1:02:32 – 1:02:58]** We kind of understand that sometimes we translate like specific words and when I am writing out here over here, I'm translating the word world and World should be more important as the input over here. Then it anything else? And here, there is no way to express that. I just need to cram everything into this single vector.

**[1:03:00 – 1:03:01]** so, the first step,

**[1:03:02 – 1:03:07]** Is to get rid of this assumption that everything needs to be in a single letter.

**[1:03:08 – 1:03:13]** So in this encoder decoder with attention, the first thing that I do,

**[1:03:14 – 1:03:15]** As.

**[1:03:16 – 1:03:18]** Okay, let me say hello world.

**[1:03:20 – 1:03:21]** Exclamation mark.

**[1:03:23 – 1:03:34]** And it's still a recurrent Network at the input. Let's say it's be directional because of course, it's be directional. It doesn't make sense, not to read the whole sentence.

**[1:03:36 – 1:03:41]** but it produces outputs for every

**[1:03:42 – 1:03:44]** X in the input.

**[1:03:44 – 1:03:47]** So there is a vector, let's say Z1.

**[1:03:48 – 1:03:51]** There is a vector Z2.

**[1:03:52 – 1:03:54]** And there is a vector Z3.

**[1:03:57 – 1:04:14]** So far it it's easier. Almost nothing has changed. Of course, if I can produce a vector at the end, I can produce it at every step. I just take the two hidden States. I push them through like one one layer of one.

**[1:04:15 – 1:04:18]** It Forward later in. There you go. Here is your zip.

**[1:04:19 – 1:04:25]** so, now I have this vectors for every input word for every turkey,

**[1:04:26 – 1:04:37]** But I can't just concatenate them all and feed them all over here. This is exactly. The Z is too long situation.

**[1:04:37 – 1:04:42]** I want to, I don't want to make them

**[1:04:46 – 1:04:46]** I don't.

**[1:04:47 – 1:05:04]** Yeah, I don't want to make them longer because that would make any sense that this will be just the same thing with stated differently. I want to have as input on every step here. I want to have one vector of this size.

**[1:05:06 – 1:05:10]** So how do I combine them into this single vector? And this is the attention mechanism.

**[1:05:13 – 1:05:14]** I do the following.

**[1:05:15 – 1:05:15]** I have.

**[1:05:16 – 1:05:19]** A small Network, the attention Network.

**[1:05:24 – 1:05:55]** That receives as input to the decoder to. So let's say, let's say that we are in the decoder and it's got like HT Prime over here. And we are writing the next word right now and we need to find out what is the current input over here, right? So that it will write the stocking and will produce H. Prime tip was one and so we are at some point in the decoding process.

**[1:05:56 – 1:05:59]** It. So the attention Network receives as input.

**[1:06:00 – 1:06:02]** Is from here.

**[1:06:06 – 1:06:06]** and,

**[1:06:08 – 1:06:10]** An H Prime from here.

**[1:06:11 – 1:06:28]** So it needs to, it needs to know where we are in the decoding process, of course, because the attention weight will be different for different words that I write. And then it will produce a score A1.

**[1:06:28 – 1:06:29]** Just a number.

**[1:06:30 – 1:06:30]** Four.

**[1:06:32 – 1:06:47]** That shows like how important this token is right now, okay? Like you will see how it gets used, so it's the score for token. Number one,

**[1:06:48 – 1:07:00]** At step T. So it at the point where in the point characterized by this hidden state of the decoder and then you do it for every

**[1:07:02 – 1:07:02]** See.

**[1:07:03 – 1:07:03]** so, you get

**[1:07:08 – 1:07:12]** So you get like a 2 for Z2 over here.

**[1:07:14 – 1:07:17]** And you get A3 for these three.

**[1:07:22 – 1:07:23]** Then.

**[1:07:24 – 1:07:28]** I convert this Ace. So let's call them the vector. A

**[1:07:29 – 1:07:37]** I can convert this a into probability Center. Convex combination, by passing it through a softmax.

**[1:07:38 – 1:08:04]** You see how it all comes together? We are we talked about soft Maxes, Logistics, sigmoid Etc. We talked about their properties and lecture or something, and now we are using all these properties. So it's not noticed that I'm using software's. Not just as the output but I am. So just using it to convert. Every time I need to convert just a set of numbers to convex combination to something that sounds to one.

**[1:08:05 – 1:08:08]** So and here I get something like Alphas.

**[1:08:09 – 1:08:10]** Now, they are.

**[1:08:11 – 1:08:13]** From 0 to 1 and they sum up to one.

**[1:08:14 – 1:08:22]** And that's it. These are the, these are the coefficients.

**[1:08:23 – 1:08:24]** For my combination.

**[1:08:25 – 1:08:31]** So now I just do like a DOT product and ZT here.

**[1:08:34 – 1:08:44]** Ziti here is just the sum of alpha, I times the I okay. So ZT is not a good letter. Let's call it.

**[1:08:45 – 1:08:45]** I don't know.

**[1:08:47 – 1:08:47]** Let's call it.

**[1:08:52 – 1:08:59]** What afterwards do I have letters that I have YouTube? Okay, so the input for for the

**[1:09:00 – 1:09:17]** the so the input for the decoder at time at time step, T is a linear combination of the representations of every token with weeds determined by the separate attention Network.

**[1:09:19 – 1:09:23]** So what this means, like they intuition behind this day.

**[1:09:26 – 1:09:29]** The motivation is that I want.

**[1:09:30 – 1:09:31]** this to

**[1:09:34 – 1:09:46]** A to express what specific tokens. I am translating right now, so like on step three. When I'm producing the third token, the third word I want.

**[1:09:47 – 1:09:50]** The word world to have a high weight over here.

**[1:09:52 – 1:09:57]** because I mostly translating the word world, well, in the context of the rest of the sentence, but mostly that

**[1:09:58 – 1:10:12]** And also notice and this the last important point about this before I proceed to just show a show to show you the results and everything in discussion. The last important point is this

**[1:10:12 – 1:10:23]** When I tell you this intuitions when I tell you stuff like oh, so the attention network is supposed to give you a high score for the word that we are translating right now.

**[1:10:24 – 1:10:26]** This is not.

**[1:10:27 – 1:10:29]** Any formal input for the network?

**[1:10:30 – 1:10:47]** There is no labeling in the data set that will tell you. Now I'm translating this talking now, I'm Translating that this, they, the data set is still the same. The data set is a set of pairs, like sentence in English sentence in Russian.

**[1:10:48 – 1:10:56]** They they match. They are translations of each other and here you go. 100,000 pairs of sentences trained on that.

**[1:10:57 – 1:10:57]** so,

**[1:11:00 – 1:11:02]** when I'm talking to you of intuitions, like this,

**[1:11:04 – 1:11:08]** What I mean, is we kind of want the network to work to work like that.

**[1:11:09 – 1:11:19]** And miraculously after trading it indeed works like that but we never explicitly trained trained the attention Network.

**[1:11:20 – 1:11:40]** The attention network is just this very small tiny component. It has very few weights compared to the listings. So, a practical number. If I remember correctly, would be something like 2% of the weights of the whole network goat, the attention mechanism. So it's a very small component compared to the rest of the network.

**[1:11:42 – 1:11:43]** but,

**[1:11:44 – 1:11:47]** This very small component, actually.

**[1:11:48 – 1:11:54]** Drives the results. This component is the difference between the red curve and the purple performer here.

**[1:11:54 – 1:12:00]** this component actually does trained to do this job of finding out, which

**[1:12:02 – 1:12:29]** A finding out which tokens we are translating right now and producing the correct weights. So it's a general principle of deep learning that we see quite often and I think we already saw it in convolutional networks, I just didn't call it out General principle. That very often, you just need to keep the network a chance.

**[1:12:30 – 1:12:31]** Right. You just need to

**[1:12:33 – 1:12:37]** Introduce some components inside that have.

**[1:12:38 – 1:12:40]** These potential ability.

**[1:12:41 – 1:12:42]** To do the job that you want.

**[1:12:43 – 1:12:59]** And even if you have no data to train them, even if you cannot take the attention Network out of this whole thing and train it separately and then plug it back in because oh, you don't have the inputs for these, right? Inputs are also changing as we train.

**[1:13:01 – 1:13:05]** And you don't have the Outpost. You don't have the correct answers here.

**[1:13:06 – 1:13:25]** But still, if you just structurally give the network a chance to do it right with sometimes not always but sometimes it will do that and everything will work and it will be like a very nice example of new structure inside of that.

**[1:13:27 – 1:13:35]** So this was what happened with encoder decoder. Architectures around 24 15.

**[1:13:36 – 1:13:39]** So in 2014, this was the state of the art.

**[1:13:39 – 1:14:07]** And in, okay, even in late 2014, but I don't know, let's call it introduced this kind of attention mechanism. So this this is exactly what I was just drawing, right? The attention Network that receives the current state of the decoder and the representation of a token from the input, and it gets you a score and then you do a softmax etc.

**[1:14:08 – 1:14:14]** Yeah, cheers. Here are the formulas and indeed and indeed

**[1:14:15 – 1:15:15]** It does trained to to do what you want. And also like a common feature of attention mechanisms, we will see that in Transformers 2. A common feature of attention mechanism says that they also give you something to look at. They give you some this attention weights when you actually draw them. And look at them there, probably usually very easy to interpret. So for example, this is from one of the original machine translation applications here. Here, they're translating from French to English. So, the instructions, if you have, for example, French and English mostly match mostly, it's a diagonal matrix where the high attention weight is on the deck and all your translation. This word by word, more or less. But notice the

**[1:15:15 – 1:15:21]** Exemptions right? So for example, a lot of restaurants here is translated as destruction.

**[1:15:22 – 1:15:22]** and,

**[1:15:23 – 1:15:35]** It's two words into one. There is an article in English here. So here the attention rate is high for both wine districts. You know why we are right in the destruction, right?

**[1:15:36 – 1:15:52]** And here, for example, arm comic, chemical weapons in French, the adjective goes after the noun in English, the opposite. So here the attention weights Swap and you see an opening

**[1:15:53 – 1:15:54]** I think I have.

**[1:15:56 – 1:16:25]** I have examples for you here too. So okay, so here here is a very simple recurrent network with attention that just learns to reverse the input. So, if the input is sequence by 34057, blah blah, the output will be blah, blah 75 043, right? And of course, the recurrent Network can train to do the same. It's it's not hard.

**[1:16:26 – 1:17:08]** Actually, by the way, without an attention mechanism. I don't have this experiments here, but I'm pretty sure that without the attention mechanism, it would be hard. It would be very difficult. Because if you don't, if you have just encoder decoder thing, if you don't have this attention mechanism, then you need to memorize the whole input sequence in order to write it down in the reverse order, right? So if you cannot memorize, the whole input, if you don't have enough space enough capacity in your intermediate representation to just memorize the whole input your screwed, you cannot do the reverse unless you remember it. Exactly.

**[1:17:09 – 1:17:10]** and,

**[1:17:12 – 1:17:27]** With attention, you don't have to remember anything. You just trained to have this of reversed and of reverse the economy Matrix and so it it's not on the diagonal because you have a special tokens like

**[1:17:28 – 1:18:24]** Um yeah, whatever you also have a special token here like and sequence but anyway, there is this clear diagonal structure that basically just tells you where to look and what to copy, right? Or here is a more difficult example. I'm sorry, I'm not running them online because it takes a little bit of time to train so just not to waste time waiting but I will probably certainly you will be able to run it yourself. So here is a slightly more difficult thing. Here is like a sorting thing. So now the input is a sequence of numbers and you need to sort them in the output. And here also you will see you can see that at step T, we attend to the current

**[1:18:24 – 1:18:49]** Teeth. Small Australia. So like the decoder, steps are along the vertical excess and this is the source position. And on the first step, the most attention is paid to position. Where there is a one on the Second Step where there is a three then to the four and six. And so

**[1:18:50 – 1:18:56]** So you can see that indeed the attention mechanism has trained to do with it once.

**[1:18:58 – 1:19:54]** And this was a big thing in 2015. And through the next couple of years, people were like, exploring this stuff and this kind of attention mechanism has a lot of benefits. Let me not waste time or talking to my sham about this. It can do work order better. It can do some very interesting stuff like calm, doing grammar as a foreign language so you can sometimes fit even. And yeah, okay, let me talk about this because we Transformers at 7 more. I want. So sometimes your output has some kind of complicated structure that doesn't look like a sequence. For example, if you're doing a syntax tree of your input, then your output is a tree. It's a graph, right?

**[1:19:55 – 1:19:56]** so,

**[1:20:04 – 1:20:04]** You.

**[1:20:04 – 1:20:12]** It doesn't look like you should use a recurrent Network to write out a graph. The graph is not a sequence, it's more complicated.

**[1:20:13 – 1:20:22]** But it turns out that if you just write down, your tree is a string and there are ways to represent the trees a string and you just treat this.

**[1:20:23 – 1:20:26]** three strings as a language to which you translate

**[1:20:27 – 1:20:31]** it works and I think with Transformers it would work even better.

**[1:20:32 – 1:20:41]** In 2016. There was a very interesting paper from Google where they basically published how they are.

**[1:20:42 – 1:21:02]** Google's neural machine translation system works and I won't go into details here but basically it was interesting to learn that Google transfer it all works in the exact same way it of course Google being Google. It was bigger. There was some tricks etc etc but basically it was in order to order with attention

**[1:21:03 – 1:21:07]** and by the way, my personal experience was that

**[1:21:08 – 1:21:11]** Around 2015 to 2016.

**[1:21:11 – 1:21:17]** When they switched from whatever they had before to this kind of architectures.

**[1:21:19 – 1:21:24]** Google translate actually became much better.

**[1:21:24 – 1:21:27]** I mean I was using all the time.

**[1:21:28 – 1:21:36]** All better to say, I wasn't but I had a side job at the time translating like research papers from Russian to English.

**[1:21:37 – 1:21:53]** And before about 2016, of course, I tried to use Google Translate but it was completely hopeless. So you would spend much more time on fixing the results of Google translate, then you wouldn't just typing the stuff from scratch.

**[1:21:54 – 1:21:55]** It was completely useless.

**[1:21:58 – 1:22:12]** And in 2016 2050 and there was a phase transition. Suddenly sure. It was still bad. Sure. You still needed to edit it. You still doing it to edit translation 7 from the latest quote and GT but

**[1:22:14 – 1:22:21]** now it was more efficient to First, do a pass with Google translate and then fix the mistakes or they

**[1:22:23 – 1:22:26]** you know, but writing then,

**[1:22:26 – 1:22:35]** To do everything from scratch yourself. This, this was the moment when machine translation actually started doing some useful work for me,

**[1:22:36 – 1:22:55]** Um, and yeah. Okay, so let me skip that. And the last Point here, is that when I'm talking about in order to the other architectures, usually, I talk about like the same kind of architecture and the encoder and the decoder.

**[1:22:56 – 1:23:03]** So now we are doing machine translation. It was a recurrent encoder that reads text and the current recorder the right steps.

**[1:23:04 – 1:23:38]** Doesn't have to be this way, right? So you can definitely have encoder decoder, architectures. Where the input has one modality and one kind of network in the output is a completely different kind of network, completely different models. I don't even think this count as multiple model architecture, is because well, they are multimodal. But the two modalities are separate really because all you need from the encoder is to give you a vector representation and then you take this Vector presentation and plug it into the decoder.

**[1:23:39 – 1:23:51]** so, for example, I mentioned at some point, I think the captioning problem here is the captioning problem as it wasn't 2015, with a straightforward and quarter, decoder thing,

**[1:23:51 – 1:23:55]** Um, they encoder was a googlenet that we discussed.

**[1:23:56 – 1:23:58]** The decoder was an lstm.

**[1:23:59 – 1:24:26]** And it became much better when people edit an attention mechanism. And again, this, this is also important and important for what will come later? Notice that you can do the exact same thing. This kind of attention highlighting specific parts of the input. Even if you're input is not text, even if your input is not a sequence. So if you have a picture for example,

**[1:24:28 – 1:24:36]** the only difference here is that now we don't compress the whole picture to a single feature vector.

**[1:24:37 – 1:24:40]** Like we would do if it was a straightforward little political order.

**[1:24:41 – 1:24:42]** We have the same.

**[1:24:43 – 1:24:49]** CM the same convolutional thing. And then I just

**[1:24:50 – 1:24:57]** Stopped it a little bit short of the little bit in the middle so that I still have some geometry left.

**[1:24:58 – 1:25:08]** Like in this example, the input is not the 56 by 2506 and they stopped the feature extraction when I have a 14 by 14 feature.

**[1:25:10 – 1:25:13]** And now I have this quote, unquote pixels.

**[1:25:14 – 1:25:16]** Elements of the feature map vectors.

**[1:25:17 – 1:25:29]** And I can do a tension over this vectors. So, now I can have an attention Network that combines, that gives me coefficients to combine these.

**[1:25:30 – 1:25:32]** 192.

**[1:25:33 – 1:25:38]** 96 right? No wait.

**[1:25:39 – 1:25:40]** For my fortune.

**[1:25:41 – 1:25:44]** 193 right? No.

**[1:25:45 – 1:25:46]** Let's just, yeah.

**[1:25:48 – 1:25:50]** so this Fortune by 4 chain,

**[1:25:53 – 1:25:59]** Different vectors and they have this. So my coefficients will combine this Fortune squared vectors.

**[1:26:00 – 1:26:57]** And again, it kind of works. I won't go into details and another nice thing. Nice thing is that it gives you the actual attention weights. You can look at them and you can interpret them. So, we will kind of see that in Transformers still, but it will be actually less clear and more complicated and Transformers. But here it's very clear, it's very straightforward. You can just see what the network is looking at right now as it actually write this piece of the output. So it a woman throwing a frisbee in the park. Here is woman, we are writing woman. We look at the people and then throwing and we start concentrating on the throwing and freeze beware concentrated on the face. Be and when when I ride down the park then they are not looking at the people we are looking at the background so that's that's just perfect.

**[1:26:58 – 1:26:58]** Okay.

**[1:27:00 – 1:27:08]** So I want to stop here. Are there any questions at this point? You actually covered quite a lot.

**[1:27:09 – 1:27:13]** It's in promo sgms from the attention mechanisms required attention and

**[1:27:14 – 1:27:17]** Onto encoder decoder attention.

**[1:27:20 – 1:27:26]** Wonderful. So let's have a break please. Let's not have a half an hour break because today

**[1:27:27 – 1:27:42]** Our Administration asked me to, to have a call. It what? One 20. So let's have a 15 minute break and then we'll reconvene and we'll discuss.

**[1:27:43 – 1:27:46]** we'll discuss the main architecture of

**[1:27:47 – 1:27:52]** The entire deep learning right now. For the last 10 years, the Transformer

**[1:27:53 – 1:27:53]** Right.

**[1:46:14 – 1:46:15]** Okay.

**[1:46:16 – 1:46:17]** so,

**[1:46:18 – 1:46:19]** On to the Transformer's.

**[1:46:22 – 1:46:22]** Well.

**[1:46:26 – 1:46:30]** Here. Yep. So

**[1:46:32 – 1:46:35]** Transformers appeared in 2017.

**[1:46:36 – 1:46:36]** and,

**[1:46:38 – 1:46:39]** It was.

**[1:46:40 – 1:46:40]** kind of,

**[1:46:42 – 1:46:49]** I mean, let me start with the brief historical remarks. So in 2017, when this paper appeared, at the end of the year,

**[1:46:51 – 1:46:55]** I don't think I'm pretty sure the the authors.

**[1:46:56 – 1:47:01]** Of the Transformer, paper of attention is all you need actually understood what they were doing.

**[1:47:02 – 1:47:12]** so the paper is not that ambitious, we will see what its results were originally and they are mostly about like

**[1:47:13 – 1:47:27]** Here is a different way to do stuff which provides approximately the same results, but which is more efficient. Maybe let's switch to this more efficient way of doing, basically the same

**[1:47:29 – 1:47:30]** but,

**[1:47:31 – 1:47:32]** Since then.

**[1:47:32 – 1:47:46]** The whole field of machine learning switch to Transformers, as we all know and much of the rest of our class will be billed on the Transformers. So we will use Transformers in different ways.

**[1:47:47 – 1:47:48]** so,

**[1:47:50 – 1:47:52]** The main, I think.

**[1:47:54 – 1:48:02]** Positive qualities that the Transformer had that the original paper didn't really couldn't really notice it from from its experiments.

**[1:48:03 – 1:48:31]** Are two things, one it turned out that proved to be very, very general. In the sense that the Transformer is just very good at noticing internal correlations within complicated data, right? And it doesn't really matter for the Transformer with, or its text or images or whatever. It just works with sequences of vectors.

**[1:48:32 – 1:48:34]** And it doesn't care where?

**[1:48:36 – 1:48:48]** This vectors come from. So this is a great thing. And even more important thing is that Transformers proved to be extremely

**[1:48:51 – 1:48:53]** scalable.

**[1:48:54 – 1:49:53]** You can take it Transformer, you can scale it up, and it works better. You can scale it further up without changing anything inside. Well, sure there have been Novelties. Sure, modern Transformers are slightly different from the one we had 10 years ago, but it's mostly the same and still your scale. What happened? That works better and better and better and never situates with our large language models. I hope I will have time to talk about that next week with large language models. We keep going from like tens of millions of millions of billions 200 billions to now trillions of parameters and they just keep getting better and this has had never happened before. You can't scale lstms in the same way or I mean maybe you can but we don't have enough compute to do that, but I think the complexity grows so fast or they say

**[1:49:54 – 1:50:03]** Trade. And they even if you can't train them, they stopped providing any benefit. And in the Transformer it kind of all came together.

**[1:50:04 – 1:50:42]** So what is the Transformer? I will actually go through the slides first through some of the slides first because the basic structure is very similar to what we were. Just discussing. It doesn't, I don't have to redraw it but then the main core will be the self-attention mechanism and that is completely new. And that I will, of course you discuss in detail. So this is the most famous picture from the original paper but I think it's pretty hard to understand. So I make my own pictures here and here is the structure of the original transform.

**[1:50:43 – 1:50:51]** Without details, without the interesting Parts. But the general structure is actually very

**[1:50:52 – 1:51:06]** Straightforward. And it's very similar to what we just had in recurrent and others attention architecture. So it's important architecture and yes, the original Transformer was

**[1:51:07 – 1:51:08]** doing machine translation.

**[1:51:11 – 1:51:32]** It has an encoder which consists of six, identical layers, it has a decoder, which consists of 6%, clears and the encoder receives text in one language. The decoder produces text in another one. Let's let's say in this Paradigm for now.

**[1:51:35 – 1:51:47]** Are interesting Parts here. What can we see on this picture? So first of all, the input to the actual Transformer, the actual and quadrant layers is not just the sequence of tokens.

**[1:51:48 – 1:51:52]** And we didn't discuss it in detail. I mean text is not our thing, but

**[1:51:54 – 1:51:55]** it's

**[1:51:56 – 1:52:03]** it had been very common in natural language processing. Even 10 years ago to convert.

**[1:52:06 – 1:52:13]** One hot representation of words of tokens to continuous representations, that are usually call them bearings.

**[1:52:14 – 1:52:29]** This is again, very, very common, very straightforward, all through deep learning if you have a large vocabulary of different stuff that you want to import. Like, in this case, different words or tokens parts of words,

**[1:52:31 – 1:52:31]** Then.

**[1:52:35 – 1:52:35]** and then,

**[1:52:37 – 1:53:31]** Then sorry, then you first want to convert them to dense vectors and there is like a whole line of work and an opium on this like word to their glove fast, text different embeddings, we won't go there, but here the embeds are really straightforward. There is just one very interesting technical thing that I will talk to afterwards in the end, but mostly it's just, you know, a matrix of vectors. So for every input token, there is a vector. And we look at up and we put it in place of this talk, that's it. And, but importantly, it's not some external representation. It's not some work to act that we copy here. It's an embedding player that is trained with the rest of the network. So you train this Vector representation. So along with the other ways,

**[1:53:33 – 1:53:38]** And after this embedding player, the input sequence becomes a sequence of actors.

**[1:53:39 – 1:53:42]** And all the actual Transformers doing.

**[1:53:43 – 1:53:45]** It's rewriting.

**[1:53:46 – 1:53:52]** Sequences of vectors into sequences of vectors. So every encoder layer will take

**[1:53:53 – 1:53:56]** a sequence of vectors as input and produce.

**[1:53:57 – 1:54:04]** The same sequence of vectors. Well, I mean, sequence of vectors from the same size as our output.

**[1:54:05 – 1:54:15]** And that will. And that will rewrite this kind of structure for in this case, 6 times. And then we get a vector for every input token.

**[1:54:16 – 1:54:40]** After all of this encoding, it's no longer just representation of the token. It's now representation of the token in the context of all the other tokens. And I mean, it has many times it has looked at all the other tokens at the whole sentence. The whole sequence, Etc. So by now, by the top, here we have this representation of smart. Semantic acceleration, presentations of inputs.

**[1:54:41 – 1:54:42]** And now what does the decoder do?

**[1:54:43 – 1:54:44]** The decoder.

**[1:54:45 – 1:54:56]** Is a language model. I hope you heard of language models. So the decoder is producing output tokens one by one.

**[1:54:57 – 1:55:14]** Out the aggressively, right? So it's input is what it has already written by the history of input until now and its output is the next token.

**[1:55:14 – 1:55:36]** Right? So after the decoder so you have to run the Transformer decoder as many times as the number of tokens that you want to produce. And this is one kind of restriction that in modern language models you need to work around and wait, there there is

**[1:55:38 – 1:55:48]** A big signs around. It speculative decoding and stuff like that, but you want to go there anyway, by default, it's not regressive thing. You produce the output torque converter

**[1:55:49 – 1:55:51]** and,

**[1:55:52 – 1:55:55]** these guys, the stuff that you are actually translating,

**[1:55:57 – 1:56:00]** Sorry, I don't really understand this. Can you see

**[1:56:02 – 1:56:03]** My cursor.

**[1:56:04 – 1:56:06]** You can't write.

**[1:56:08 – 1:56:19]** Yeah. Okay, so pointing with the mouse, doesn't really work. All right, so the stuff that is at the output of the encoder on top left here. It's

**[1:56:22 – 1:56:30]** It's getting used in the decoder on every layer on every step of the way. And of course, we will discuss how exactly

**[1:56:32 – 1:56:33]** But this.

**[1:56:33 – 1:56:50]** This high level, this high level structure is very similar to what we just saw right and coder the coder and not, there is no separate attention Network here. The attention will be hidden inside the encoder and the decoder.

**[1:56:52 – 1:56:54]** so, if you look inside,

**[1:56:55 – 1:57:00]** and quarter layer in the D quarter layer, you will see the

**[1:57:01 – 1:57:11]** The end quarter layer actually, I think. Okay, yeah, I have here. So the end code layer is what it's a self-attention layer.

**[1:57:12 – 1:57:23]** Then layer normally Asian. Then interestingly, If It Forward layer a fully connected layer, then another layer norm and that's it.

**[1:57:24 – 1:57:31]** So of course, the interesting part, the part we are going to discuss in detail, is self-attention, right? The self-attention is the first layer here.

**[1:57:33 – 1:57:54]** But the rest also uses this components that we have been discussing, right? So it's not we are not discussing ancient history. Everything that all the ideas that I'm telling you are actually being used right now. For example here we see a residual connection that goes around the self-attention layer right?

**[1:57:55 – 1:58:21]** And it lands actually, I forget in front or afterwards, but near this layer normally layer, we is a kind of batch Norm, right? So you just discussed it with Alex and practice layer Norm is like bitch Norm but not across the meaning, which but across all of the outputs of the current player. So Transformers a big and then Transformers

**[1:58:22 – 1:58:23]** Oops.

**[1:58:27 – 1:58:27]** Sorry.

**[1:58:30 – 1:58:32]** Recording in progress.

**[1:58:33 – 1:58:40]** Yeah, I want to chase. I'm not sure what happened but somehow I got disconnected from Zoom.

**[1:58:40 – 1:58:41]** um,

**[1:58:42 – 1:58:42]** You know.

**[1:58:44 – 1:58:46]** The internet works. I hope you can see.

**[1:58:50 – 1:58:50]** Ya.

**[1:58:51 – 1:58:51]** so,

**[1:58:53 – 1:59:27]** So the where did this stop? Yeah, there the end. So the encoder layer uses, this layer Norm at the output of self-attention and layer Norm as you discussed with Alex just averages out. Gradients keeps the Lost landscape. Smooth keeps it under control. In terms of the absolute value of output Etc. And here Transformers are big so we cannot really

**[1:59:29 – 1:59:32]** We cannot really rely on.

**[1:59:34 – 1:59:44]** Bachelor because the probably there is no bitch, probably only one copy of the Transformer fits into our memory and we have on the one instance. So we use later.

**[1:59:45 – 2:00:18]** And then interestingly, there is just a feed-forward layer and it's actually a very important that it has a lot of Weights. If you look at it, it takes up quite a lot of the quite quite, a big fraction of the entire weights of the Transformer. And there is nothing to say about it. It's just, you know, rearranging the features mixing together the features in every Vector separately. As you can see, it's applied to every Z Prime individual, and then there is another layer, and that's the encoder layer.

**[2:00:20 – 2:00:23]** In the decoder. You also have self-attention.

**[2:00:24 – 2:00:45]** It's exactly the same as a self-attention here, except for the word mosque, but we'll get there. There is also, if it Forward layer, all. So, layer Norms are after everything. And the only difference is this in quarter decoder, attention layers. So the outputs of the encoder, this Vector representations, they

**[2:00:46 – 2:00:52]** Should go somewhere, right? They should be doing something and they go here. And when we get there, I'll explain what exactly

**[2:00:54 – 2:00:56]** and then, after the decoder has,

**[2:00:58 – 2:01:19]** After we've gone through the decoder, then, of course, we have to do some classification. So, there is a linear layer that goes to a soft matte layer and the softmax produces probabilities, and then you sample, the next token of this probabilities. So, again, as you can see, it's exactly the logistic regression at the end, so it all kind of comes together.

**[2:01:20 – 2:01:28]** All right, so this is the general structure. And on this picture, there should be absolutely nothing new to

**[2:01:29 – 2:01:29]** Except.

**[2:01:30 – 2:01:32]** Of course, the self-attention stuff.

**[2:01:33 – 2:01:41]** So what is self-attention? What exactly how do we understand it? Where does it come from?

**[2:01:44 – 2:01:45]** It number three for today.

**[2:01:46 – 2:01:47]** So touch.

**[2:01:49 – 2:01:50]** Well.

**[2:01:51 – 2:01:53]** Actually discuss self attention.

**[2:01:54 – 2:01:59]** I need to take a step back and I need to talk to you, surprisingly.

**[2:02:00 – 2:02:02]** About information retrieval.

**[2:02:05 – 2:02:10]** Which is not the subject of our class but turns out to be made around.

**[2:02:11 – 2:02:21]** So how does search work in deep learning? How does information retrieval work when you have neural networks?

**[2:02:23 – 2:02:24]** Basically, it works like this.

**[2:02:26 – 2:02:28]** You have say, queries.

**[2:02:30 – 2:02:32]** Very one, very two.

**[2:02:33 – 2:02:34]** And you have documents.

**[2:02:36 – 2:02:37]** Okay, one.

**[2:02:38 – 2:02:40]** Document 2 document 3.

**[2:02:41 – 2:02:42]** document for

**[2:02:44 – 2:02:48]** And in usual information, retrieval what you would do?

**[2:02:49 – 2:02:50]** You would.

**[2:02:52 – 2:03:05]** Establish a similarity. You need to establish some kind of similarity between queries and documents. This kind of similarity will be called relevance and you will train it to be the relevance, right? So,

**[2:03:07 – 2:03:12]** It should be higher when this document is relevant to this query.

**[2:03:12 – 2:03:16]** This is how search generally Works. What whatever is

**[2:03:17 – 2:03:28]** But when you have the bearing, when you have this neural networks, that can process any kinds of input, and that can train to process long texts, large, images, Etc.

**[2:03:29 – 2:03:31]** What he usually do is this.

**[2:03:32 – 2:03:33]** You.

**[2:03:34 – 2:03:35]** Get.

**[2:03:38 – 2:03:39]** Documents.

**[2:03:40 – 2:03:41]** Rowan encoder.

**[2:03:42 – 2:03:45]** And the documents will become vectors.

**[2:03:46 – 2:03:49]** You get queries through their own encoder.

**[2:03:50 – 2:03:52]** So they become vectors to.

**[2:03:54 – 2:03:55]** And the idea.

**[2:03:57 – 2:04:02]** Is that all of this vectors should leave in the same space?

**[2:04:03 – 2:04:05]** so even though in quarters are different,

**[2:04:06 – 2:04:15]** they cannot be the same because documents can be images for example. So there are different at first but they should produce vectors in the same latent space.

**[2:04:16 – 2:04:20]** So like documents get my apps over here.

**[2:04:24 – 2:04:27]** And then you may have your query over here.

**[2:04:28 – 2:04:29]** and,

**[2:04:30 – 2:04:32]** You are supposed to train the whole system.

**[2:04:34 – 2:04:43]** So that the relevant documents will be closed, they representations of relevant. Documents will be closed to the representations of the queries.

**[2:04:44 – 2:04:47]** So like then, inside this latent space.

**[2:04:48 – 2:04:55]** You will be able to just you know take nearest Neighbors in, this nearest neighbors will be a good answer to the search query.

**[2:04:56 – 2:04:56]** Okay.

**[2:04:57 – 2:05:02]** So I was drawing this but I think I have a picture about. Yeah.

**[2:05:04 – 2:05:06]** so, you have

**[2:05:07 – 2:05:16]** a query, you have a document documents, go through their own, encoders queries, go through their own orders and then like

**[2:05:17 – 2:05:25]** the whole point of it is so that in the latent space in the late in space, you actually

**[2:05:26 – 2:05:26]** Have.

**[2:05:28 – 2:05:38]** This structure that relevant documents will be near the images of the queries, okay? There is a whole

**[2:05:39 – 2:05:43]** field of study about how to do that. It's obviously very very

**[2:05:45 – 2:05:49]** Big Assumption of.

**[2:05:51 – 2:06:02]** Learning and we could have a whole class on information retrievable maybe you will. So I won't, I won't go into more details but what we need now is this basic intuition that

**[2:06:03 – 2:06:25]** Different stuff gets mapped to the same latent space and in that latent space. We are just looking for nearest neighbors and since it's, since you can do it linearly as a linear space, basically this, the similarity here between the query and the document,

**[2:06:28 – 2:06:30]** is can be thought of as just, the

**[2:06:31 – 2:06:56]** Dot product of the corresponding vectors. So like I encode the document and I multiply it by the encoding of the query, that's it. Okay, and this approach has lots of advantages for information retrieval. You can just store the vectors. You don't have to think about anything else. It's fast to do it in the low dimensional space blah blah, very good.

**[2:06:58 – 2:07:03]** And so attention. Interestingly enough drawers on this intuition?

**[2:07:04 – 2:07:11]** But since itself attention, it applies this ideas to like the same set of vectors that are both.

**[2:07:12 – 2:07:14]** The are both queries and documents.

**[2:07:17 – 2:07:18]** Here is how it works.

**[2:07:23 – 2:07:24]** Here is how it works.

**[2:07:36 – 2:07:36]** Okay.

**[2:07:38 – 2:07:43]** Here is how it works. Here is how it works. So we begin

**[2:07:44 – 2:07:45]** With.

**[2:07:46 – 2:07:54]** A set of vectors. As I said, every layer of the Transformer gets just a sequence of vectors as input.

**[2:07:54 – 2:07:56]** So, we have this.

**[2:07:57 – 2:07:59]** One.

**[2:08:01 – 2:08:03]** X2 and so on.

**[2:08:05 – 2:08:12]** X. And okay we have this vectors Vector inputs.

**[2:08:13 – 2:08:15]** Now, I want to make

**[2:08:17 – 2:08:18]** this kind of

**[2:08:19 – 2:08:39]** Query document thing. So in information retrieval, it terminology is inherited from like classical information retrieval. You would sometimes call this image from documents, the representation of documents, you would call the keys.

**[2:08:40 – 2:09:01]** Okay, In classical retrieval, the query would not need to be encoded. It would be just aquarius. So there is no word for the image of the query, but okay, we will just call it the query. So let's, let's, let's say that the query already lives in this space and the document should be mapped there and should produce some kind of a key.

**[2:09:04 – 2:09:14]** And here we take our access, let's say we take X1 and we produce from it queries keys and values.

**[2:09:15 – 2:09:20]** So, with X1, we multiply it by a matrix called WQ.

**[2:09:22 – 2:09:26]** And as a result, we get the first query vector.

**[2:09:27 – 2:09:29]** This will be q1.

**[2:09:29 – 2:09:30]** Okay.

**[2:09:31 – 2:09:32]** Then.

**[2:09:32 – 2:09:33]** We take.

**[2:09:34 – 2:09:36]** All of the inputs.

**[2:09:37 – 2:09:38]** All of the excess.

**[2:09:39 – 2:09:52]** And we multiply them by The Matrix WK. Just put it here, once not copy it many times and we get the key. Vectors we get K1.

**[2:09:53 – 2:09:54]** A K2.

**[2:09:55 – 2:09:57]** And so on. Okay. And

**[2:09:59 – 2:10:03]** And the whole point of self-attention is that q and K.

**[2:10:03 – 2:10:05]** Should live in the same latent space.

**[2:10:06 – 2:10:09]** So now, this guy goes here.

**[2:10:11 – 2:10:13]** These guys also go here.

**[2:10:17 – 2:10:18]** and the

**[2:10:21 – 2:10:22]** similarity.

**[2:10:22 – 2:10:23]** Between.

**[2:10:24 – 2:10:32]** Q and K. It's just a DOT product between them. It's we assume that they already live in the slate and space. They are they they have

**[2:10:33 – 2:10:35]** the same Dimension are and

**[2:10:37 – 2:10:38]** this similarity.

**[2:10:39 – 2:10:44]** Is exactly the score that we will use. This is the attention of it.

**[2:10:45 – 2:10:45]** so,

**[2:10:47 – 2:11:00]** You see queue was made from X. Hey what's my also made from X and now we look at like how similar q and Care between each other.

**[2:11:01 – 2:11:08]** so, out of this space, we get like this sequence of

**[2:11:10 – 2:11:32]** Ah, attention scores. So to say affinities, right? We get like a one one, which is q1 times K1 as well and then a12 and so on a one and which is q1 times km

**[2:11:33 – 2:11:35]** Right. So we get this.

**[2:11:37 – 2:11:42]** Vector of attention Affinity as we put it through the softmax as usual.

**[2:11:43 – 2:11:44]** and we get,

**[2:11:45 – 2:11:47]** Yes, sorry. Also

**[2:11:48 – 2:11:56]** I forgot one one detail I'll get to it later but we put through the softmax we scale first by square root of d.

**[2:11:57 – 2:12:06]** And then we put it through the software. So this kind of transformation. I'll explain later. Why? Why? We need risk scaling? And then we get this

**[2:12:07 – 2:12:08]** Vector of

**[2:12:09 – 2:12:25]** attention weights. So now we have this this will be like a one in. This will be awful one. So this is the actual potential weights between 0 and 1 rescale to sum up to one and

**[2:12:26 – 2:12:34]** They are the similarities between the first query, the first query and all the keys.

**[2:12:35 – 2:12:39]** Right, similarities, rescaled back to a set of weights.

**[2:12:41 – 2:12:48]** So now we need to use the set of weights to make some kind of linear combination to make a complex combination of something.

**[2:12:49 – 2:12:49]** Well.

**[2:12:50 – 2:12:50]** Of what?

**[2:12:54 – 2:12:56]** Of another set of vectors.

**[2:12:57 – 2:12:59]** Here is the thing. So,

**[2:13:01 – 2:13:04]** now we again, take all of the excess,

**[2:13:08 – 2:13:12]** And we multiply them by yet another Matrix. Wait Matrix WV

**[2:13:13 – 2:13:14]** and we get,

**[2:13:18 – 2:13:20]** Vectors that we call values.

**[2:13:20 – 2:13:23]** We want to be in values.

**[2:13:24 – 2:13:30]** So the green ones are really use the blue ones are keys and the red ones are queries.

**[2:13:34 – 2:13:34]** and now,

**[2:13:36 – 2:13:38]** We take all of these videos.

**[2:13:41 – 2:13:44]** Am we multiply them?

**[2:13:46 – 2:13:51]** With the dot product, we multiply them, we add them up with the coefficient self.

**[2:13:53 – 2:13:55]** so, this is what

**[2:13:56 – 2:14:04]** This is what's the dot product? How do I like this, right? Maybe Anyway, dot product.

**[2:14:04 – 2:14:07]** So the output is how it's called Z1.

**[2:14:08 – 2:14:14]** It's the sum of Alpha One. I times V.

**[2:14:18 – 2:14:18]** Okay.

**[2:14:21 – 2:14:22]** And that's it.

**[2:14:23 – 2:14:25]** That's the basic idea of attention.

**[2:14:26 – 2:14:47]** And of course, I only Drew one query but it then gets repeated. So we take X2 we multiply it by WQ. We get Q2 it also gets my here. Blah blah blah and test the output begins it to which is the sum of two I again times V. So and we answered

**[2:14:49 – 2:14:53]** Right. So this takes a little bit of understanding.

**[2:14:55 – 2:14:57]** Here cosine similarity. Yeah. Right.

**[2:14:57 – 2:15:14]** So this takes a little bit of understanding to get it in your head because it's all very abstract, right? It's just some dot products and some new space. In this new space is just multiplication by the weight matrices. There is nothing like to

**[2:15:17 – 2:15:19]** nothing too intuitive here.

**[2:15:20 – 2:15:27]** Well, I tried to give you the basic intuition for information retrieval, but I mean, it only goes so far still.

**[2:15:28 – 2:15:48]** Formerly. It's really, really simple. All right. So what we do for formerly is we take the excess from multiply them by double by by matrix forget aquarius. So in practice, of course you would not do it, step by step. You would do it all at once. So like, your Aquarius are some weight Matrix times x.

**[2:15:49 – 2:16:08]** Or maybe the other way around. If I forget, which one is more, commonly extends? This metrics doesn't matter and your keys are some weight Matrix times and here waiting videos. Okay. Are some weight Matrix times x, right? And then

**[2:16:09 – 2:16:18]** What do you do with this Matrix is so if we continue the formal stuff, you need to get this Matrix of all possible.

**[2:16:20 – 2:16:26]** Cosine similarities. You write all possible dot products between queries and keys.

**[2:16:27 – 2:16:44]** So if you write it in Matrix forms, then it will be like Q times K transpose. This will be the Matrix where the ij's element will be like UI dot product by KJ.

**[2:16:45 – 2:16:45]** Wright.

**[2:16:46 – 2:16:56]** And then you take this queue times K transpose and your risk scale. You do so softmax and then you multiply by the result.

**[2:16:56 – 2:16:57]** The vector speed.

**[2:16:58 – 2:17:01]** So, the attention weights.

**[2:17:03 – 2:17:04]** Are.

**[2:17:04 – 2:17:06]** The softmax.

**[2:17:07 – 2:17:11]** Of one of the square root of G Q transpose.

**[2:17:12 – 2:17:15]** And the actual output disease.

**[2:17:16 – 2:17:19]** Is what software?

**[2:17:22 – 2:17:29]** Of 1 over the square root of d q. K transpose, times V.

**[2:17:30 – 2:17:39]** And that's the main formula that you see everywhere, right? This this is from the original attention, is all you need paper and this is exactly

**[2:17:40 – 2:17:42]** what I was trying to explain to you here.

**[2:17:43 – 2:17:43]** so,

**[2:17:45 – 2:17:54]** The intuition about the this Matrix is there dimensions and everything, is that adds is probably pretty big.

**[2:17:54 – 2:18:12]** Pretty long. It's from some art to, I don't know, some capital G, and queries and keys have to live in the same space. We have to make dot products with them, so they both have to be lifting in the same smaller space.

**[2:18:13 – 2:18:13]** Small d.

**[2:18:14 – 2:18:42]** So this Matrix and this Matrix are both like gay times, small D matrices and really was formerly. Can have a different size, right? We never take a DOT product between V and Q or V and K. So formerly, it could be like deep Prime in practice. Usually it's the same deal of course, but formerly. Let me write that. This is like a d times D, Prime Matrix.

**[2:18:43 – 2:18:47]** It or sorry, the way the way I write. It should be that way around.

**[2:18:48 – 2:18:49]** Could be.

**[2:18:50 – 2:18:54]** A g times capital D and this should be deprived. Thanks.

**[2:18:58 – 2:18:58]** Okay.

**[2:19:01 – 2:19:05]** So what else can I say here?

**[2:19:06 – 2:19:08]** Tells can I see here?

**[2:19:13 – 2:19:19]** I think that's it for the basic idea of potential. We got from the beginning to the end.

**[2:19:20 – 2:19:26]** I will show you a nice picture in a sec. Let me just highlight one thing.

**[2:19:27 – 2:19:38]** So yeah, okay sorry. I promise to explain where the square root of decomp from why. Why the risk? Well, the risk scaling goes like this.

**[2:19:42 – 2:19:44]** What we have here, what we have in this Raw

**[2:19:46 – 2:19:54]** Affinities between queries and kiss, like, dot products between vectors of entity.

**[2:19:55 – 2:20:02]** Right? And if you think of say queries in case, it's just random vectors vectors with random numbers inside.

**[2:20:03 – 2:20:04]** You see that?

**[2:20:06 – 2:20:07]** What do you?

**[2:20:08 – 2:20:15]** Say something. Don't you see that this vectors with queries in case inside?

**[2:20:16 – 2:20:16]** Hmm.

**[2:20:17 – 2:20:32]** If you think of them, it's just random vectors. So like if let's say it's like Qi is something like zero plus or minus 1, right? So it's something from minus one to one.

**[2:20:33 – 2:20:39]** On their average, maybe more, maybe less, but more or less. It has like a standard deviation of one around here.

**[2:20:40 – 2:20:45]** And KJ also has a standard deviation of one around 0. Then, what is happening here?

**[2:20:46 – 2:20:50]** This is the sum of d.

**[2:20:50 – 2:20:51]** Much.

**[2:20:53 – 2:20:54]** Number is deviation.

**[2:20:55 – 2:20:55]** One.

**[2:20:56 – 2:21:04]** and if you take the sum of the random variables, Each of, which can go to plus or minus one,

**[2:21:05 – 2:21:15]** A approximately on average then the result will have a variance on the order of give or take square root of d.

**[2:21:16 – 2:21:42]** I don't want to do probability Theory now, it's it's a classical result, basically, I think if you ever had a probability of theory class, you probably know this in the form of random walks on the line. Like if you go from zero and you flip a coin and every time you go either right or left and how far from 0 do you expect to be in N steps? And the answer is square. Root of him.

**[2:21:43 – 2:21:50]** so it's it's the exact same effect, and that means that if we don't do this,

**[2:21:51 – 2:22:07]** We will have like big numbers over here. We will, if for example, D is something like 64 which I think was true for the first Transformer. Then when you add 64 numbers, you get numbers on the order of like plus or minus 8.

**[2:22:08 – 2:22:20]** And plus for minus 8 is more or less, more or less means that the output of the softmax will be closed to just one zeroes close to one hot vector.

**[2:22:21 – 2:22:33]** Which is not really what we need. We needed to be smoother here. So we smooth it back. We rescale it back so that we go from the square root of D back to give or take one. That's, that's an explanation for the scaling.

**[2:22:34 – 2:22:39]** And what else? I can notice right here, right now is that

**[2:22:41 – 2:23:01]** we already see the main computational problem of Transformers. I don't think we will have time in class to discuss this huge line of work that tries to, to avoid this to work with it, but we definitely should mention the problem itself.

**[2:23:03 – 2:23:14]** Here to compute this, you need to have this Matrix, you need to compute this Matrix, and this Matrix is an end times and Matrix.

**[2:23:15 – 2:23:18]** And this is like, quadratic complexity.

**[2:23:22 – 2:23:29]** Or create a complexity as a function of the input length of the length of the input sequence.

**[2:23:31 – 2:24:13]** And that is the main computational problem of Transformers because it means that you cannot scale them up with respect to the inputs to the input length unless you unless you do some interesting tricks. And of course there are a million different interesting tricks. It's it's a big field. But basically, if you remember like three years ago when people were doing large language models, they would be like boasting about their contact size. They would be saying like, oh our llm has a contact size of 128,000 tokens and our LM has 500 12,000 tokens. And we have got a million token contacts with

**[2:24:15 – 2:24:45]** I mean, this is about that. So it's it's not trivial to get to a million token contacts window. It doesn't just mean that your, it doesn't mean that the complexity is a million times. One token. It means the complexity is a million square times 1 token and the million square is just too much definitely so you cannot do it straightforwardly as this Matrix you have to invent some tricks around it and of course there is a big field of science around this.

**[2:24:46 – 2:25:00]** ah even right now, I think if you go to to Cloud you will see that it has a separate model called Opus with a 1, million token context and it's

**[2:25:01 – 2:25:08]** More expensive more complicated than just straightforward opposed, which obviously has a smaller content size, right?

**[2:25:11 – 2:25:14]** So contacts is is a difficult problem for Transformers.

**[2:25:15 – 2:25:17]** But other than that,

**[2:25:18 – 2:25:21]** it's all here. This is how self-attention works.

**[2:25:22 – 2:25:29]** And I won't try to draw it on the board. I will show you it to you on site but the next

**[2:25:31 – 2:25:46]** the next thing and another idea that we actually were discussing a couple of days ago and now it all comes together. Another important idea here is that notice what we are doing to assess

**[2:25:48 – 2:26:00]** Again, let's look at it from this geometric perspective. I think yesterday they were talking about this geometric, the geometry geometrically, what we are doing is we are taking this X in a big space.

**[2:26:01 – 2:26:04]** And we are projecting it to a much smaller space.

**[2:26:05 – 2:26:09]** In two different ways in these two ways. Give us the queries in the case.

**[2:26:10 – 2:26:19]** So again, I can't give you like tangible intuition that you can touch. But mathematically what you are doing is you have a big space.

**[2:26:20 – 2:26:30]** And you're looking for a good projection for the queries and another, but the same dimensional projection for the case.

**[2:26:30 – 2:26:34]** So, like two ways of looking at the set of vectors X.

**[2:26:35 – 2:26:39]** and then there is the third projection, which can have a different dimension for the various

**[2:26:40 – 2:27:11]** So in a way, it's again the same question that I asked yesterday, if all I do is assess, this vectors is compressed and down to query skin values. And in practice like if you have no capital D, something like 2:56 or 512, it would have small D, something like 64. As I said, then why do you need the long factors at all?

**[2:27:12 – 2:27:21]** Same question as we had yesterday and it's the same answer. The answer is, this is what I've just drawn to. You is just one attention head.

**[2:27:22 – 2:27:50]** And in a fair in practice, in a Transformer, you will have several different attention. Heads, each will have its own Matrix, matrices wqwk WV, and they will produce their own, kind of ways, of looking at the input and ultimately, they will produce their own output zi. So, really there is another in the index in here.

**[2:27:51 – 2:27:52]** Okay.

**[2:27:53 – 2:27:56]** Let's look at this slide. I have

**[2:27:57 – 2:27:58]** better pictures up there.

**[2:28:00 – 2:28:05]** So this is the intuition coming from self-attention.

**[2:28:06 – 2:28:13]** And this is the picture that I was just drawing. So let's, let's walk through it again. It's the most important picture of the whole class, I think.

**[2:28:15 – 2:28:17]** The input is a set of vectors.

**[2:28:18 – 2:28:27]** Each Vector gets multiplied by three, matrices WQ, gives you the query WK gives you the key, WV gives you the value.

**[2:28:28 – 2:28:34]** And then the queries, and the case should live in the same latent space.

**[2:28:34 – 2:29:12]** You take well okay set, cosine similarity as I do product because of course, nothing forces them to have like normal one and we do not want to rescale by enormous to complicate it. So let me just stick to that products, we take the dot product between q and every K. We get this definitive then we scale by the square root of K here is called q but it's square root with the dimension. Then we take the softmax and we get the actual weights, convex weights and we have this products combination of the vectors V. We these weights.

**[2:29:13 – 2:29:13]** Okay.

**[2:29:14 – 2:29:22]** So oh and notice by the way, how we are actually looking on all input.

**[2:29:23 – 2:29:33]** By every query. So, like every X in here is looking on every

**[2:29:34 – 2:29:55]** token from the input on every other X and on yourself on a cell as well on Xbox one too. So this. Yes. So sorry I should probably say this explicitly here. This is another very important property that makes Transformers so cool. And this property is

**[2:29:56 – 2:30:04]** Here, if you have X1 X2 X K, blah, blah, x capital l.

**[2:30:06 – 2:30:19]** And let's assume that you want to like find out, you want your X1 to influence to have some relation with X scale over here.

**[2:30:20 – 2:30:24]** So like this word in the input, text has relevance to this work.

**[2:30:26 – 2:30:28]** To have the current Network.

**[2:30:29 – 2:30:35]** This influence would have to go step by step through all of this intermediate vectors.

**[2:30:36 – 2:30:44]** Right? So, there is no path in their current Network that jumps over tokens. You just go step by step.

**[2:30:46 – 2:30:46]** and of course,

**[2:30:47 – 2:30:51]** even if you have an hasta with this memory cell with this,

**[2:30:53 – 2:31:03]** Constant error, Carousel, the highway that connects every Point. Still a lot can happen as you go step by step through this sequence.

**[2:31:04 – 2:31:05]** With the Transformer.

**[2:31:06 – 2:31:18]** You don't have to do. That is the Transformer. You just jump in one step from here to here. And you can actually jump to every token and you do jump to every token and every step.

**[2:31:19 – 2:31:24]** So this is great. This is like one

**[2:31:25 – 2:31:25]** step.

**[2:31:26 – 2:31:27]** From.

**[2:31:29 – 2:31:33]** Every eye to every J. And this is a big plus

**[2:31:34 – 2:31:37]** And the cost of this is this quadratic complexity.

**[2:31:39 – 2:31:46]** This is the big minus, okay. So at a current network has linear complexity.

**[2:31:47 – 2:32:02]** As you add more elements to the sequence, you just do more steps but each step has the same size as the same complexity. So the current that works are linear in the input. Size Transformers, work with content, it's a huge difference.

**[2:32:03 – 2:32:18]** But they are then more free to notice the relations and they don't care about how far it is from one talking to the other. They just see the whole sequence at once on every layer on every step, and that is great.

**[2:32:20 – 2:32:21]** um,

**[2:32:22 – 2:32:35]** Okay, so yeah. And this is the picture that I wanted to draw on the board. Yeah, please ask a question. I think it's in really understand about the value of space.

**[2:32:38 – 2:32:40]** Like I understood that theory.

**[2:32:43 – 2:32:44]** Sorry, I'm back. I

**[2:32:45 – 2:32:48]** truly hope that the recording is not garbled after that. I'm

**[2:32:50 – 2:32:51]** OBS Studio. Creating

**[2:32:53 – 2:32:55]** Anyway yeah please. What was the question?

**[2:32:57 – 2:33:00]** I'm Transformer related well.

**[2:33:01 – 2:33:09]** I'm more or less, understood about the key and curious part is that we they shared the same space and space.

**[2:33:10 – 2:33:16]** And the way we are interested in finding the closest distance.

**[2:33:17 – 2:33:18]** Between them.

**[2:33:19 – 2:33:37]** We're scared him, Etc. But but the point, I didn't really understand about the value value Vector. Not that even doctors and also the space. How is it formed? Yeah. Okay I I got the question actually. Yeah, I'm

**[2:33:38 – 2:33:46]** Problem is I don't have a good answer to that, so I don't have a good intuition for why we need the values at all, why can't it be just X?

**[2:33:47 – 2:34:07]** That is a good question. Yeah, that is a good question. I guess like The Superficial answer is that. Well I mean still every attention had is trying to highlight some aspect of the input and in terms of the values all so we want to kind of

**[2:34:10 – 2:34:12]** how to say this, we want to

**[2:34:13 – 2:34:57]** highlight a specific like projection of the big vectors X and we want to simplify them to to highlight this thing that we are looking for with this specific queries and this specific case. But that's not really a satisfactory answer. I think the true answer is over here and the answer is if so, like what does the value of vector Define it? What does the length of the very? Where does the length of the value come in? What is it important? The Links of the value of vector defines the length of the output, the size of the output, right? So your output is a combination of these.

**[2:34:58 – 2:35:03]** So, the length of Z of the one is the same length as the length of V.

**[2:35:05 – 2:35:21]** And I guess it would be it would just wouldn't make sense. It would be too inefficient and too much too many weights, Etc to have many X sized these and then combine them together and compress them back down to a single X. Okay?

**[2:35:22 – 2:35:26]** So I guess that's just an efficiency thing.

**[2:35:26 – 2:35:31]** so yeah, we could just use x as the document, but

**[2:35:32 – 2:35:39]** I, I suppose this would make this multi-head attention to difficult and we really want multi-headed attention as I just explained.

**[2:35:40 – 2:35:41]** Does that make sense?

**[2:35:44 – 2:36:01]** It's a bit confusing. Okay. So let me go through this slide. Maybe it'll be a bit less confusing. So we have actually several multiple of this attention heads, okay, we have had one had two headache

**[2:36:02 – 2:36:21]** and when we have had one had to finish every one of them gives us the set of these, The Matrix Z, which is these, that is in the boxed formula here, right? But now we have multiple Sciences

**[2:36:21 – 2:36:23]** And we need to combine them together.

**[2:36:24 – 2:36:43]** And after that, now the the output of this step. Now it has to make the input size. Well, it's not doesn't have to but it does it usually, it doesn't practice, just so that we can make another layer exactly like this. We can just copy the layers. So,

**[2:36:44 – 2:36:48]** This Matrix Z at the very end at the top right of this.

**[2:36:49 – 2:36:53]** Should have the exact same size as the input Matrix X, okay?

**[2:36:54 – 2:37:17]** But the intermediate representations they are much better. So let me maybe just briefly throw it here since this is not. Not that easy to understand. So we have this one Matrix X which is like capital D times, L is the number of vectors is the vector size.

**[2:37:18 – 2:37:23]** And this goes through attention head.

**[2:37:25 – 2:37:25]** Number.

**[2:37:26 – 2:37:26]** At.

**[2:37:27 – 2:37:34]** Number one. Okay, attention had number two, blah blah. Attention. Hit number H.

**[2:37:35 – 2:37:45]** And this one gives you a matrix Z1. This one gives you Matrix Z2, this one gives you Matrix CH and these guys are

**[2:37:49 – 2:37:50]** What's Happening Here?

**[2:38:00 – 2:38:01]** Recording in progress.

**[2:38:04 – 2:38:14]** Sorry, I don't know what's happening here today? Like all problems combined. Okay, so we have multiple

**[2:38:15 – 2:38:20]** we have multiple attention heads and every attention had gives you

**[2:38:21 – 2:38:40]** And you may Matrix z a different Matrix you see, and now we need to merge the mold together. So, everyone of this Matrix is like a small details element Matrix, but then when you string them all together, the one then Z2, then zh

**[2:38:41 – 2:38:42]** You get a pretty big Matrix.

**[2:38:44 – 2:38:51]** So if you just communicating them like this. No, I should. Okay. So let's say that this is

**[2:38:53 – 2:38:54]** L times d.

**[2:38:54 – 2:38:56]** Naught, L times.

**[2:38:57 – 2:38:58]** Not D times out.

**[2:39:00 – 2:39:13]** Now I will concatenate properly all types Capital. Yeah, so when I concatenate them together I get the Matrix which is still l in terms of the roles but now it's l times. H times d.

**[2:39:14 – 2:39:19]** And H times D is probably bigger than capital D and it's it's a lot.

**[2:39:20 – 2:39:31]** So what we do here in a Transformer, we multiply it by another Matrix of Weights so it's like just the feet forward layer, we mix up all the features again.

**[2:39:32 – 2:39:40]** And this fit forward layer gives us the Matrix Z. So this this is the Matrix of size. What?

**[2:39:41 – 2:39:47]** HD times Capitol building something like this. Okay. So

**[2:39:48 – 2:39:50]** My intuition for this is that.

**[2:39:52 – 2:39:59]** We really, first of all, we need some variety in.

**[2:40:00 – 2:40:24]** Disease, we need more variety. Not just linear combinations of the same vectors with different coefficients, but different projections of this vectors this this gives us more variety and more expressive power and two. If we just had this small G equal to the Big D, now, this guy would be just invisible to train would be just to be

**[2:40:25 – 2:40:28]** So I guess this combination of two things that we want here.

**[2:40:29 – 2:40:29]** Okay.

**[2:40:30 – 2:40:37]** I understood your intuition. Okay, thank you for trying. It was clear. Thank you.

**[2:40:39 – 2:40:40]** All right.

**[2:40:41 – 2:40:42]** So, what we have here?

**[2:40:43 – 2:40:44]** Is.

**[2:40:45 – 2:40:48]** One attention had copied multiple times.

**[2:40:49 – 2:40:57]** They wrote attention heads, they are all processed in parallel. And as the output we gave we get this Matrix C.

**[2:40:58 – 2:41:03]** and this this if we, yeah, if we look at

**[2:41:04 – 2:41:18]** Where where we are now, we have explained, we have expressed exactly this one, self-attention layer on the bottom left. This first self-attention layer from the

**[2:41:20 – 2:41:23]** The first self-attention layer from the encoder.

**[2:41:25 – 2:41:28]** But notice that it's basically almost all that we need.

**[2:41:30 – 2:41:31]** So, what's left?

**[2:41:32 – 2:41:36]** first, what's left is

**[2:41:39 – 2:41:45]** Okay, so first let me go through The Masks of attention in the decoder. And actually, let's, let's talk about the decoder. So we have

**[2:41:46 – 2:41:49]** completely, we are completely done with the encoder part.

**[2:41:50 – 2:41:50]** That's it.

**[2:41:51 – 2:42:01]** So potentially just described then layer normally know fit forward, just one Matrix to mix up the weights, know it makes up their presentations, we know that's it.

**[2:42:02 – 2:42:11]** In the decoder. There are there is more stuff to think about. So what is masks self-attention? What does it mean?

**[2:42:12 – 2:42:17]** Well actually, I don't able to explain it in detail because that's a pure efficiency thing.

**[2:42:18 – 2:42:18]** so,

**[2:42:20 – 2:42:20]** like,

**[2:42:21 – 2:42:27]** When I draw a picture like this one, where the decoder is only predicting the next token.

**[2:42:28 – 2:42:32]** There is actually a mask, self-attention is just self-attention.

**[2:42:32 – 2:42:45]** That's it. So we have the current state of the prefix, it's on the bottom, right? We have the current state of the prefix it goes into self-attention. It's just exactly the self-attention to be just described

**[2:42:46 – 2:42:48]** where the masks come in is that

**[2:42:49 – 2:42:53]** How do we train a language model? How do we train?

**[2:42:55 – 2:43:10]** Let me explain it. Briefly, how do we train a Transformer decoder, or the whole Transformer, with encoder and decoder? We have this output

**[2:43:12 – 2:43:14]** Right. So this is like the sentence that we need to produce.

**[2:43:15 – 2:43:17]** and, in terms of the,

**[2:43:18 – 2:43:20]** Transformer decoder.

**[2:43:20 – 2:43:30]** This output sentence is like one to three, four, five, six, different seven, actually different training samples.

**[2:43:31 – 2:43:31]** so,

**[2:43:34 – 2:44:09]** The yes. So the first training sample is, you produce the from nothing from nothing and from the representation, from the encoder, the second training sample is from the prefix. The you're supposed to produce cat, the third from the cat, your supposed to produce set and so on, right? So it's like the end, the decoder should be run, seven times here, it produces six words and then it should produce like the stop talking, the token. It's done.

**[2:44:11 – 2:44:12]** and,

**[2:44:14 – 2:44:21]** You can do it formerly. You can just do it as seven different training samples.

**[2:44:22 – 2:44:28]** But of course it's inefficient. So in practice what you do is you just, you take this one sequence,

**[2:44:28 – 2:44:42]** You say that? Okay, I'm supposed to produce. So I have this, I have this decoder in the Transformer. I have all of the inputs available here.

**[2:44:43 – 2:44:52]** I have all of the outputs here and then I'm supposed to have the here cat here, blah, blah, blah, and like this top token here,

**[2:44:53 – 2:44:59]** And this is where the masks are needed. Because, of course, when I'm producing the word cat,

**[2:45:00 – 2:45:09]** This like computational path is not supposed to look anywhere except to the word Z.

**[2:45:10 – 2:45:10]** Right.

**[2:45:11 – 2:45:22]** So, I need to mask out all of the other tokens, otherwise it wouldn't be much of a problem, right? They just need to copy the input to the output. Of course, there would be nothing to do that.

**[2:45:23 – 2:45:30]** So the mask self-attention layer, what it's doing is, it's blocking all of the tokens except

**[2:45:32 – 2:45:36]** It's called causality, it's called Coastal masks.

**[2:45:37 – 2:46:26]** Ah because it preserves causality, right? So token number T can only depend on positions of one. So I want to T minus 1, right? And yeah, it's it. Some work in terms of the programming of the implementation of the self-attention. So basically you need to like zero out the way that are not supposed to be there like when the input has everything now, but when you are producing the two you are supposed to have this attention to be exactly zero in this attention, wait to be exactly 0 and you're supposed to only look at the first token. That's that's what the masks, that's it.

**[2:46:28 – 2:46:33]** So this is the master of attention part. And then they

**[2:46:34 – 2:46:36]** Encoded attention part.

**[2:46:37 – 2:46:50]** So there was a, how do, how does this conditioning work? We are from the, we are looking at the

**[2:46:52 – 2:46:54]** Ah, encoder.

**[2:46:55 – 2:47:22]** Sorry, we are looking at the at the same self-attention layer, but now we also need to somehow have the Z inputs have to the inputs that are produced by the encoder. Otherwise. What's the point of having encoder, right? And it sounds like it's, it would you would need to do something more, even more complicated. You would need to change something here because now there is this whole new input that stuff.

**[2:47:24 – 2:47:30]** Actually no actually. It's very, very simple. The self-attention stays exactly the same.

**[2:47:30 – 2:47:36]** all this picture stays exactly the same, there is only one difference so in

**[2:47:39 – 2:47:40]** In a quarter, decoder attention.

**[2:47:42 – 2:47:43]** Quarter.

**[2:47:44 – 2:47:45]** The quarter attention.

**[2:47:48 – 2:47:50]** Your prefix.

**[2:47:51 – 2:47:56]** Your ex the input from from the decoder.

**[2:47:58 – 2:48:00]** Produces the queries.

**[2:48:01 – 2:48:08]** You multiply by WQ and you get the Matrix Cube and the key isn't really use.

**[2:48:09 – 2:48:11]** Are produced by the.

**[2:48:12 – 2:48:16]** From the representations, from the encoder.

**[2:48:17 – 2:48:18]** So w.

**[2:48:20 – 2:48:45]** Okay WV and you get the K and V matrices. Okay. So no difference to this processing at all but now we have like the only difference is over. Here we are not producing all three things from the same X. We are producing the queue thing from the X and the K. And we think from some from the condition

**[2:48:46 – 2:48:49]** notice that it doesn't break anything.

**[2:48:50 – 2:48:56]** so over here, I told you that this attention Matrix is

**[2:48:56 – 2:49:02]** A square Matrix of size L times, L and times. And this over here.

**[2:49:03 – 2:49:12]** Well, now it's not quadratic anymore. So now there is a different number of queries and keys. Obviously the lengths of the sequences will not be the same.

**[2:49:12 – 2:49:18]** But that's okay, right? Whenever whenever assume that we had the same number of kissing queries

**[2:49:18 – 2:49:27]** For every query, we multiply it by all keys. So we get as many attention weights as there are keys.

**[2:49:28 – 2:49:36]** So the number of keys should match the number of values nature because then we add up values with this coefficients.

**[2:49:37 – 2:49:37]** but,

**[2:49:39 – 2:50:03]** The queries can be completely different and actually we will later when we discuss for example, object detection with Transformers, We will see that they're also queries and keys and various will be some very different things will be produced from very different things. So it's a common idea in Transformers to have queries come from one source and keys and values to come from another.

**[2:50:03 – 2:50:17]** And yeah, it dates back to the original Transformer and in the original Transformer, decoder, already. This is how we use the outputs of the encoder.

**[2:50:19 – 2:50:23]** Okay, so that's basically eat about the architecture.

**[2:50:24 – 2:50:26]** That's it about this picture.

**[2:50:27 – 2:50:28]** There are.

**[2:50:29 – 2:50:30]** Okay, any questions at this point?

**[2:50:31 – 2:50:33]** Because this is, I think.

**[2:50:34 – 2:50:38]** The most important architecture in the world, right?

**[2:50:41 – 2:50:58]** Um, so yeah, it's a lot the process. I don't expect you to like internalized it right now, right? Right from my words. But when you think it through once again, when you go through the pictures once more, and especially if you ever actually implemented,

**[2:50:59 – 2:51:09]** Then I guess you will get an understanding. It's not that hard. It's just pretty abstract. So there is nothing tangible about what is a value of vector.

**[2:51:10 – 2:51:34]** It's just a projection. It's just a good projection that we train for the input vectors and what are this input vectors? Well there are some abstract representations of the tokens so there is not much intuition that I can give beyond what I already tried but actually surprisingly enough, the actual like a potential heads that after training.

**[2:51:35 – 2:51:46]** We often do some very understandable, very interpretable very into things. Maybe if we have time I will show you some examples later about this not today.

**[2:51:48 – 2:51:57]** Um, and there are I guess, two more things to talk about. So first, let me maybe show you

**[2:51:58 – 2:52:02]** An example, to be honest, I have only some pretty trivial examples here.

**[2:52:06 – 2:52:31]** Pretty trivial examples. I have this. Let's not go through the code, we have practical sessions for that, but I have this like one layer and one self-attention head and what it's supposed to do is its supposed to Output the matching key so to speak right for the input. So and

**[2:52:32 – 2:52:53]** If you look at the attention Matrix you you see that it does like for this attention had it does look to the in the in the correct spot. Basically that's it here. And here is another kind of abstract example

**[2:52:55 – 2:53:03]** What happened? Like it's an example to illustrate that the attention Matrix, The Matrix of attention weight does not have to

**[2:53:05 – 2:53:06]** choose a token.

**[2:53:07 – 2:53:14]** so, if you look at something like this, or some sample Matrix is like this one, the

**[2:53:15 – 2:53:37]** Quite often look like a permutation Matrix, right? They're quite often look like. Well for every input, we matched to some output to some other input in this case, and we encode their Mutual relationship right now. Between input number token, number I and token number J.

**[2:53:38 – 2:53:49]** Well, it doesn't have to be this way. There can be more complicated sets of attention weights like you can have for example Plantation Matrix. It looks like this where

**[2:53:51 – 2:54:01]** These tokens these queries. Look at like the older tokens. So in this example, all totals are split into groups.

**[2:54:02 – 2:54:18]** There are four groups they go one by one. Like three tokens group of three tokens group of three tokens, then one group of one token and again group of Traders. And they are supposed to look at each other uniformly.

**[2:54:19 – 2:54:34]** So that can also happen. Okay? You can have like this widely distributed attention where one token just attends to all of the tokens for example we'll see probably examples of this.

**[2:54:37 – 2:54:38]** Um, okay. And

**[2:54:39 – 2:54:41]** two more things that I need to talk about.

**[2:54:42 – 2:54:43]** so first

**[2:54:44 – 2:55:11]** Maybe one word on tokenization, it's not really our subject because we are talking about computer vision. And in images, it will be quite different. But I just wanted to mention because it's it's a nice connection to completely different areas of computer science to like coding Theory and Huffman coding and stuff. But like where do you get your dictionary from?

**[2:55:12 – 2:55:24]** It's a pretty interesting question. Because when I explain it to you intuitively, it makes sense to say that I just talking is a word and text

**[2:55:25 – 2:55:30]** but in reality, you can't have tokens to be able to work because there are too many words

**[2:55:31 – 2:55:31]** because,

**[2:55:33 – 2:55:51]** In a language. I mean you you can't just let my everything and have all of your words loose all the grammar that would lose a lot of information. So different grammatical forms have to be separate words that's one and two in reality there are typos

**[2:55:51 – 2:56:00]** and if you add diapers, so, again, you are not allowed to just drop everything that's not in the vocabulary because then

**[2:56:01 – 2:56:15]** Many texts would not make sense and you would lose again. A lot of information, but if you add all of the words with typos there, oh my God, the dictionary will be huge. You will have millions of words in the English language.

**[2:56:17 – 2:56:17]** so,

**[2:56:19 – 2:56:22]** We need something smaller. We need a smaller vocabulary.

**[2:56:22 – 2:56:26]** But and of course we could just start with characters.

**[2:56:27 – 2:56:47]** So you could have, I mean, you you could have a, you could view text as not, a sequence of words. But the sequence of characters, this is for most language is, this is a natural way to partition the text, right? Also. It's a sequence of characters.

**[2:56:48 – 2:56:51]** but now, this on the other hand is

**[2:56:52 – 2:57:00]** To find granularity, right? So yeah, character. There are few characters at most a couple hundred

**[2:57:01 – 2:57:09]** Even if you count old punctuation marks capital letters, etc, etc. Like 100 to 200 most at most

**[2:57:10 – 2:57:14]** And of course you can train. You can have

**[2:57:16 – 2:57:25]** A dictionary of 100. Vectors your embedding Matrix of several hundred vectors, but

**[2:57:26 – 2:57:32]** Now, it's too little because now it means that your sequences get too long.

**[2:57:33 – 2:57:34]** So again.

**[2:57:36 – 2:57:55]** Remember that, for example, now like a practical limit on the contact side or something like a million tokens and if there is a big difference if it's a million words or a million letters, right? And of course you would want to be closer to million words in the middle of letters.

**[2:57:56 – 2:57:57]** How do you go?

**[2:57:57 – 2:58:10]** In between. How do you choose which tokens to use which sequences of characters to assign characters? It turns out there is a pretty beautiful algorithm for that.

**[2:58:12 – 2:58:28]** It's called BP by parenting and it's commonly used throughout machine learning and interestingly it has nothing to do with learning. It's it's all just Huffman coding from like Shannon's information Theory.

**[2:58:29 – 2:58:56]** So let's how does it work? Well suppose you have some kind of data set where you have this words, I specifically chose words that are that have many similar letters of substrings and here are the letters that appear in this world. So let's assume that these are there, the frequencies of the word. So, these are the frequencies of the letters.

**[2:58:57 – 2:59:03]** Now. Okay, suppose that I want to as a can add one more token. What do I do? Well,

**[2:59:05 – 2:59:13]** Aid in one more talking means that if I start with characters, I can now take a pair of characters, so they can call this pair a single newtek.

**[2:59:14 – 2:59:16]** So, which pair do I choose?

**[2:59:17 – 2:59:20]** Well, let me list all of the pairs that actually appear.

**[2:59:21 – 2:59:23]** Let's just choose the one that appears the most.

**[2:59:24 – 2:59:26]** in this case, obviously the at

**[2:59:27 – 2:59:28]** appears everywhere.

**[2:59:29 – 2:59:36]** Almost everywhere. So it's very, very common has a high frequency. So let's call it and you

**[2:59:39 – 2:59:50]** Talking a new symbol. Let's go capital, Z whatever. And now my words look like this, right? So I replaced every at by this Z,

**[2:59:52 – 3:00:22]** And yeah of course the I cannot delete a and t from the vocabulary because like T can occur without a for example. Right. But still I have reduced the length of my words, I have added one, new token to the dictionary and I have done it in the in the optimal way. Basic script. And then you just repeat this. So now I, I have this new vocabulary of tokens.

**[3:00:23 – 3:00:25]** They have this new account.

**[3:00:26 – 3:00:30]** I needed to update the counts of a and t.

**[3:00:30 – 3:00:40]** Now, there's different. So I have this new set of pairs. Also, I don't need to update the whole thing, but I need to update the pairs where there was an A, or a t.

**[3:00:42 – 3:00:44]** and,

**[3:00:45 – 3:01:00]** And that's how I work, right? And then we can choose another pair of tokens and replace those by Capital One and so forth. So very simple, very straightforward. And the beauty, the beautiful part is that you can stop it.

**[3:01:01 – 3:01:02]** At any time.

**[3:01:03 – 3:01:11]** You can. Yeah, yeah, absolutely. It's it's, it's from that that part of computer science, I agree, and you can stop at any time.

**[3:01:12 – 3:01:18]** you can say, Okay, so let's say I have a capacity for a vocabulary of size 100,000

**[3:01:19 – 3:01:20]** Well.

**[3:01:20 – 3:01:34]** So, that's way too much to have just characters and wait a little, to have complete words. So I just run this until I reach. I add tokens one by one so I can just reach exactly 100,000 and stop.

**[3:01:35 – 3:02:00]** And if you do it, you will see that. For example, first it will find like common frequent parts of words like Ed because it's at the end of everywhere and past tense or should I O N. Because it's a end of many nonsense, it's all so forth. And then of course, common words will be single tokens on common words will be moved multiple times and that's okay. So let's how to organization works.

**[3:02:02 – 3:02:13]** And one more very interesting remarks this will be the last that I have time to say today. One more very interesting remark about Transformers.

**[3:02:14 – 3:02:15]** Is that?

**[3:02:15 – 3:02:18]** Because they are so cool.

**[3:02:18 – 3:02:26]** Because they have this wonderful ability to go from any token to any token in one step.

**[3:02:27 – 3:02:30]** This is their biggest strength.

**[3:02:30 – 3:02:39]** But that comes with the final drawback with the finding defect Transformers loose word order.

**[3:02:40 – 3:02:58]** So in the current Network there is a very meaningful sense in which there are Hsu tokens and tokens that are far away because between a Json tokens you go in one step. If they are far away you go in many steps very natural. You don't need to remind the current Network about the word order.

**[3:02:59 – 3:03:18]** Transformers. Well, it's just a matrix, right? If you look at this Matrix of attention weights, it doesn't like just a generic Matrix, does not care. If these rules are in chess, or this rows are far apart. There is nothing that changes because of this,

**[3:03:20 – 3:03:20]** so,

**[3:03:22 – 3:03:25]** Transformers don't care about word order.

**[3:03:26 – 3:03:33]** And that's a bad thing. We don't want to keep the order, right? So what we actually do

**[3:03:34 – 3:03:40]** In practice, is we add to the embeddings of the tokens.

**[3:03:41 – 3:03:52]** We add special vectors called positional encodings that whose only job is to encode where exactly this token is in the sequence.

**[3:03:54 – 3:04:04]** And it's kind of a topic in itself, which I don't want to go into. Let me just briefly hinted the main idea.

**[3:04:05 – 3:04:07]** The main idea is this.

**[3:04:09 – 3:04:36]** Like you could have been embedding that just has like one hot representation that here is position. Number one, number two, number three, number four, but what you actually want is you want this position, according to have some kind of arithmetic on them. So you want your positional according to like if you have a vector represents position, one

**[3:04:37 – 3:04:39]** okay, so let me maybe

**[3:04:40 – 3:04:47]** briefly write it here if you have a vector that represents position 1.

**[3:04:48 – 3:04:52]** E 1 position 2 e 2, and so on.

**[3:04:52 – 3:04:54]** You want?

**[3:04:55 – 3:04:58]** them to capture this, like,

**[3:05:00 – 3:05:16]** Differences the distances between tokens. So you want like EI minus EJ as a vector to be somehow similar to e. I plus came, minus E J plus k

**[3:05:17 – 3:05:28]** So we want like if the tokens are three, if two positions are three tokens apart, you want the difference between their according to position, according to be the same across the whole sequence.

**[3:05:29 – 3:05:29]** Right.

**[3:05:30 – 3:05:34]** And in the original Transformer, they did it with this kind of approach.

**[3:05:35 – 3:05:38]** They did it with these.

**[3:05:40 – 3:06:05]** Ah, know basically positional what's the English word positional counting system? I forget like there are binary numbers, there are decimal numbers, what's the general term? So let's look at how binary numbers operate. If you look at the binary numbers, you see that?

**[3:06:07 – 3:06:14]** These are just binary numbers from 0 to 15 Road in sequence, right? So like one zero one, two, three blah, blah, 15 16.

**[3:06:15 – 3:06:34]** And if you look at what happens with the actual digits, you see that the last digit just oscillates right there are 101. The next Stitch also relates with twice, the period, the 0011001, and so on. Now we have four zeros and four ones for zeros for once 808 ones and so on,

**[3:06:35 – 3:06:37]** that's that's how binaries for

**[3:06:38 – 3:06:51]** and you can do it. You can do like a soft version of this. You can have like sine waves in different positions of the accordion and you can start with

**[3:06:52 – 3:06:57]** Sine waves with the oscillator, a lot with high frequency and then just reduce the frequency.

**[3:06:57 – 3:07:05]** And this will be like this positional system for counting that will give you the necessary properties.

**[3:07:07 – 3:07:18]** So this was the original approach to positional Coatings and the current approach. I think the one they mostly used today is called rope

**[3:07:20 – 3:07:20]** Rotary.

**[3:07:21 – 3:07:22]** Positional encodings.

**[3:07:23 – 3:07:32]** And rotary means that something is rotating. There is some kind of circular motion. And basically in raw put you do is this your

**[3:07:34 – 3:07:37]** you take your vector.

**[3:07:38 – 3:07:44]** Okay, so let's say take a vector X and in the state of considering its components one by one.

**[3:07:45 – 3:07:47]** You can see there them in.

**[3:07:48 – 3:07:49]** two ways to

**[3:07:51 – 3:08:10]** so you you break X into PCS of two numbers like two-dimensional vectors. Okay so this will be x 1 x 2. This will be X11 X12, this will be x 2, 1, x 2 2, and so on. And every two-dimensional part.

**[3:08:10 – 3:08:21]** You wrote, you can now rotate by various angles so you cannot rotate a single number, doesn't make sense. But a vector of two numbers. That's a vector on a plane. You can rotate it.

**[3:08:22 – 3:08:22]** so,

**[3:08:23 – 3:08:32]** what the rotary encoding do what this embedding section do is they take this kind of small packs of

**[3:08:34 – 3:08:35]** On a plane.

**[3:08:36 – 3:08:40]** And they multiply it by rotation matrices like this.

**[3:08:43 – 3:08:46]** I always forget where the minus sign is, maybe it's over here.

**[3:08:49 – 3:08:55]** And the positions are encoded as a coefficients to this rotation's.

**[3:08:56 – 3:08:58]** So sorry, let me write it again.

**[3:08:59 – 3:09:02]** I should have done this cosine. Okay, Theta.

**[3:09:03 – 3:09:07]** Sine Kate Theta? Minus sine K Theta?

**[3:09:08 – 3:09:16]** Cosine cave, right? So there is like this basic angle Theta and you rotate by multiple of theta.

**[3:09:17 – 3:09:33]** Which gives you this perfect arithmetic by default because if you take a vector and you rotate by K Theta and then you rotated by another elevator, then it's the same as rotating it by K plus sulfate, right? Just obvious

**[3:09:33 – 3:09:42]** So this also gives you this nice arithmetic and this kind of positional encodings have Better Properties. It seems.

**[3:09:43 – 3:09:46]** So, I have illustrations for you here as well.

**[3:09:47 – 3:10:06]** This is the sinusoidal, positional, encoding condition. This is the picture that I cannot draw on the board but this is the exactly how like this dot product between the two vectors here, depends only on the distance between them on the offset. I minus J. And that is the property that we want.

**[3:10:07 – 3:10:14]** And rotary positional coins. Well, here is an illustration for how they work.

**[3:10:15 – 3:10:17]** And this is the same kind of Matrix.

**[3:10:18 – 3:10:27]** again, showing that you have this diagonal structure, which means that along each diagonal distance between positions is the same and,

**[3:10:30 – 3:10:57]** You have the same dot product between the positional credits and I oh yeah. And I also have this illustration for why the square root of this necessary but it's just you know, practical representation of the fact that yeah if you don't scale, you get closer and closer to one hot representation, you lose the entropy after the softmax

**[3:10:58 – 3:11:00]** Um, all right.

**[3:11:01 – 3:11:01]** so,

**[3:11:02 – 3:11:13]** Let me stop here. We've discussed attention, and self-attention and the Transformer and I'm happy that I got to the end of the Transformer architecture.

**[3:11:14 – 3:11:14]** Any questions?

**[3:11:22 – 3:11:23]** okay, then

**[3:11:23 – 3:11:56]** then, thank you very much. I will try to. I will try to produce a unified video of this lecture. I'm I'm pretty sure it was not corrupted. Completely at some point, just not be a studio, quit unexpectedly, but I am sure it's not corrupted completely. I'm not sure if it will be able to actually join them together, sometimes it doesn't work. But in any case I will make it available somehow

**[3:11:56 – 3:11:59]** so, thanks a lot and

**[3:12:00 – 3:12:01]** see you.

**[3:12:02 – 3:12:08]** well, see you on Friday, but when next lecture will be, we have it decided, Well, talking about,

**[3:12:09 – 3:12:14]** Okay, so you're on Friday and Friday. I will listen to your presentations. Bye bye.

## Full text

Good morning, everyone. Welcome to our next class and today's lecture day and we will discuss Transformers. This is probably the most the single most important lecture. in our class, but Before we get the Transformers nature, we need to finish what we started yesterday. The current neural networks and we need to discuss Attention mechanisms and then from recurrent attention we will get to self-attention and therefore Transformers and they will indeed transformed the entire field of the appearing as they did and 10 years ago. So yesterday we stopped at, let me see here, I don't but okay yesterday we stopped at the main problems of the current Networks. and actually, They, I didn't make this point here, so let me make it now. The, the main problems of recurrent networks are exactly the same problems that you have in deep networks in general, in networks with a lot of layers, like the ones we've already seen in converting in the conventional side of things. so, The problem is that the signal gets saturated, right? The signal, oops, sorry. Looks like my. so, they The problem like with deep neural networks, was that as you go through the layers and the specialist created go through the layers, right? You Start losing signal when some of the layers gets saturated. So when a layer doesn't want to train anymore it's derivative becomes 0 multiplied by that 0 and nothing below it trains. Well, guess what? Eric current neuron network is in a way. A very, very deep Network, right? So it has usually you think of its input as a single thing, right? But what's actually going on is when you process The input. The activations go through as many layers, actually real physical layers, neural layers, right? The trainable, it's and everything, as many layers as Elements in your sequence. So any recurrent network is like by default a very deep Network. And when people when people talk about deep recurrent networks, what they what they usually mean is like several layers of processing for the recurrences. So there are constructions like this. Like like this, this would be called a three layered recurrent Network, right? But In a charity, if you compare it with, or if you look at or on the level of the computational graph, any recurrent Network, even one, with only one level of cells is actually a very deep Network. It's as deep as the input sequence, which is probably right? So So the problem was exactly the same as you go back with the gradients or as you go forward to the activations strange stuff begins to happen because you keep multiplying by this same Matrix of weights more or less and of course in recurrent networks it's a little bit different because now you have the same weight Matrix for every cell, right? So the old share the same W and this brings us, this gives us a little more problems, but the vanishing gradients problem is more or less the same. So if your W has a spectral radius under one then As you go from left to right with the gradients you keep multiplying by smaller and smaller. You keep multiplying. By this number, we just list and one more or less and your vectors, your gradients think. And basically addition to 0 And that's a big thing. And that but the like, the additional problem here is that you can notice that if you look inside your net or but from the behavior from like the graph of the loss function, you will never know. Notice it because it's not like exploding rate. When gradients explode, it means that Yeah, just everything is a huge mess. Nothing works right. When gradients explode you you start seeing things like numerical overflows in in your in your code and it's completely obvious that everything has broken down. Not so with Vanishing gradients, right? So when Vanishing gradients become Smaller. When you go from right to left what the search, it doesn't mean the W stop straining. So trains, why? Because it still participates in the last cells of the network, right? So even if your gradients become, like basically exactly zero after the second step on their way, back from those function, even if that happens, W will still train. It will still look fine at first glance because it will still participate in here. It will still give you some signal. The gradients with respect to the weight will not be zero. You will notice it by looking at the gradients with respect to W, everything will be fine, but your network will make its decisions based on the last two elements of the sequence, it will not be able to have long term memory for the rest of the seconds. So the actual problem with Vanishing gradients is like these guys problem from this classic Nolan movie. The networks cannot have long-term memory, they cannot have They cannot have this. X1 influence the output. That's step t. So what do we do? Well, we do exactly the same thing that we already learned how to do. With residents. We add something like residual connections. And in fact it was recorded networks that by nearly said. Yeah, because recurrent Network simply don't work at all without this idea and So, it actually originated with in the 1990s. In Oregon Schmidt, Cooper's group over. And this constructions have been known for a long time, but only in like 2015, they were actually applied to deep neural networks, because we didn't have so deep neural networks before. Um, and the idea is the same. You need to have like this. Way for gradients to flow around, multiplying them by weight matrices. So you need to have some Smith covers sometimes code at highways, you need to have a highway for the gradient to go through. and, Yes, of course, you will change what's happening on the highway but not by multiplying directly by a weight Matrix that could go to 0. And I will explain to you this very famous and still very important Construction. Lstm Which stands for long short-term memory. Kind of a strange name, but there we go. And the basic idea for this James is that? Yeah, yes, you do have this highway for memory to flow. So I will be drawing here one cell of the listing. So, like we are in here. And our inputs are the hidden State, and the current X. And our output should be the next hidden state, right? so in Palestinians, the hidden state is like artificial split into So of course formerly it's just a single Vector but we treat two halves of this Vector very differently so I will I will draw them as two different vectors. One half. Is. like, This long-term memory. This is the part that will stay. On the highway. This is the highway action so it will stay. not unchanged, we will write memory from memory Etc but this is the part that We don't want to multiply by weight matrices. This is like in terms that we already know this is the equivalent of this path. Path around the layers, right? And then there will be also, let's call it h, h. T a, it's just a regular quote, unquote hidden state, it will participate in everything that happens in the lstm and you will see how it gets used. And actually as the output, we will need to produce this Vector for the next step. So, C is kind of this long term memory and this is the correct integration. This is like a memory cell where you write stuff where you read stuff from. And like, the whole list cm is devoted to operations with this long term memory. And then of course we have X so we have like XP over here. This will be in first And what's happening inside? Well, Let's see, I'm consists of gates. This is also a pretty important concept because in many modern architectures, you will see some kind of gating mechanisms, you will see some kind of gates like this here, I will draw Gates Like this. Let me show it separately so there will be like this, there will be a gate for example with two inputs. I will put matrices over here. These are two inputs X and Y and then the gate itself. Will look like this and there will be a function over here, the activation function. And so, the output of this gate will be like f of a times X plus b times y, okay, and probably plus biased, but I will not throw the biceps explicit. So this is basically this one linear sell, right? So we inputs every input gets multiplied by a matrix. This will be weight matrices. Then we add them together and people post and throw an activation function. But here they will be used in a different in many different and creative ways. This kinds of gates So let's begin, let's see. Our first gate will be over here. I will call it the input gate. The input gate, right? Okay, let me draw it and then I will explain what's going on here. No, sorry, let's let's start with the forget gate. So this will be the forget gate. Just cleaner Picture This Way. So it receives this input H with the weight Matrix w H f right? H for hidden f for forget. It also receives input X. With the weight Matrix, double w x f, then you go here and then what happens? is I, multiply The out I'm multiply c t by the output of this gate like component wise. So its output is a vector, let me call it f t 50 and I multiply CT by ft. So let's unpack what's happening here. And then the rest of the gates will work in about the same way. So what is happening here we have this kind of linear thing that just combines H and x with some coefficients, whatever. And importantly, we pass it through a logistics equipment, we pass it through this Sigma function, this function that goes from 0 to 1 and that basically converts any score to the probability. So as a result, we have this Vector full of various from 0 to 1 So it's right. It goes from 0 to 1 and there are several ways from 0. And actually, as a 0 and 1, not include. So and then we multiply it component Wise by our memory cell. So what's going on? What's the intuition? The intuition is we want to be able to erase something from memory. How do how do you erase something from memory? Well, you multiply it by 0, right? So basically, they forget gate, if the output is close to one. It means keep it retain the cell and memory. If the output is close to zero, that means don't keep it erase it, right? And that's like, Mostly how gates work. so in like modern architectures like mixtures of experts and don't think, we will have time to discuss those but very often, you will see some kind of engaging mechanism and usually it means that You have some small part of your network. In this case, just this line yourself producing a controller that will control what's happening with other stuff inside the network. So this is not like data, really, this is not something that I want to treat as numbers and the course it's your numbers, right? It's phone numbers inside in your network but the meaning of the vector F here at the output of this gate is which memory cells to erase. It's not some additional number that I want to multiply because I care about the multiplication result. That's the point of getting here. You, you cannot do like real logic gates because then gradients would not follow through right? Logic? Gates are piecewise constant and, you know, you cannot train through them but you can do. Some kind of continuous approximation to this kinds of gates and here, it's basically about the racing from it. Okay. And now that we have one gate, clear, the rest basically Falls. So next, you have next we have let's say you have the candy bit sales state And they sell state. Okay, probably don't need more space and that will come. Later can, it's all state we will Produce the new numbers to write down to memory, right? So this is like C Prime tip. This is something that we may want to write the memory. Uh, where do we produce them from? Of course, from the same inputs so we have w h c another Matrix of weights, right? And we have w x c and other Matrix of rates notice that for control controlling gates for Gates. Like the forget gate, it's important that they have the sigmoid function at the end because I do want numbers from 0 to 1 actually want them to be saturated. I want them to be either close to 0 close to one, that's the whole point. Here, not so much. Right? So here I just want to produce new numbers to store in memory. So here like this Sigma cannot be exchanged for something else. It's important that it's a sigma but this hyperbolic tension time, just copying it from classical HDM construction but this this is not written set and stone, this can be modified. and, So now we have C Prime. And the question is, which part of this Vector? I want to write to memory And guess what? There is a get to control that. So we have another gate which is called the input gate. Here it is. And now this one is a control gate with the sigma. And what it does is it decides which of these candidate sell we, which parts of cprime, I want to write into memory. So I multiply C Prime component Wise by the output of the input gate. And then there is a result I write into my memory. What does it mean to write something into memory? That's just addition like this. okay, that's and of course, I need to do it from inputs. w h, i w. X. I need one more gate. All right, so at this point we have, we are able to erase something from them and we are able to write something back to memory, right? So again, this plus is like, not really plus, I mean, they always TM usually does not learn to actually, Add stuff. It's not about this Edition, it's about writing to memory. So the main mechanism is sometimes I want to erase something from memory. So I multiply by something, very close to 0. I get a 0 in that position of CT and now when I add something there, it means I'm just writing to this. So, and the only remaining thing is to Define this H for the next step, And here I will actually look at them because the rest is very logical. And here, let me, yeah, it's hyperbolic tangent. So now, i h t plus one is actually Produced from the long term memory. So it's basically kind of a copy of long-term memory but For some reason, which I cannot really explain, it goes through hyperbolic functions over here and then and then it's a part and then we read the result from and then we read it from memory. But what does it mean to read again? It means that there will be a gate controlling, which part of CT. I want to write to HD. All right, so there will be another gate. Let's call it the output gate or output. Yeah, I think output. The output gate. Again, with the sigmoid. and you have, A vector here. And this Vector will decide what to read from memory for the next h. And again. W h, o. and, WX. That's it. Let's say. So, the lstm cell is everything that's in here, right? So this, this, this this is, this is the lstm cell and, It looks. Complicated. It's not really complicated like meaningful. I cannot explain to you the intuition behind like everything here. Maybe it's at that hyperbolic tangent. I have no idea why it's exactly that but I can explain to you like how things flow inside is inside an ostm and it makes sense, right? So the beauty of this construction is that it makes perfect sense. It's like a program for memory manipulation procedures. Right? There is this memory you can delete from it, you can write to it. That's it. And also you need to on the first, you need to decide what to write to it. So hence the candidate Health state That's how it works. And It actually. Is. An extremely successful construction. It's still relevant now, even though it was like constructed, I think 1995 was their first paper. And by the year 2000, they already had exactly this construction. The first construction was a bit simpler but by the year 2000, instrument covers group, they already had exactly this and ever since it just works, And when you build their current Network today, you will actually use the stamps surprisingly enough. All right, so, I don't want to spend too much time on recurrent networks. So, let me like be quick about what's coming next here. And the last time is the most important recurrent construction ever again. Its main meaning, is that it provides you with this straight line with this highway, Through which the gradients will flow without any interruptions or better to say, only with interruptions that we intend. So of course, there will be interrupted if I erase something from memory. Of course, this will stop the gradients, but that's that's how I want to. and, Yeah, and but the list here has a bit cost. And the cost is it has a lot of weights. So, if you look at all of this waitresses, you will see that they are a lot of waitresses. Right? There are in the construction that I drew here. There are eight waitresses. And they are basically. So if I X is our deprived and I think I said that this is D, so h&c are offend D. Then like half of this Matrix is are like d times D, major interests. And half of this matrices are D times. D Prime matrices. And of course you want your memory to be. Large you cannot have a meaningful STM with like you know, self size 2. So in reality like in practice the is something like at least to 56, maybe in small cases, something like 64 and large cases, and like a 1000 and depressed. What it is. That's your ex probably some impeding of X some representation but it's also probably on the same kind of size level. So, this are big weight matrices. And for a long time it was very difficult to train those students and Like everybody knew that they are cool. And in to examples, they were actually delivering very good results. But nobody could really trained a few hours here and I think it only began to be possible in like 200015 or so, but ever since because James are in the what what people use for For bigger current networks. And for example, I think to take an example, you may have heard about, I think Alpha star Alpha star, the Starcraft playing Network, it was actually a recurrent Network and alphastar used lstms. Which sounds? Pretty strange, right? Like How, how does it happen that this basically first? Okay, very smart people did it. It makes a lot of sense, but this is like the first successful attempt to build an architecture for this kind of memory manipulation stuff and it was 25 years ago and it still stands in, nobody has done better. That sounds unbelievable, right? And indeed, of course, there have been lots of attempts to do something better. So let me. Well let me not throw Anything new here, anything on the board? I will just walk through the slides to save time. But okay so this is this is the lstm cell that I have been growing just now forget get input gate and it's all straight output gate. These are the matrices, the formulas whatever. Yeah. So completely and its modern form. It already appeared in 2000 in the years of 1000 and There have been some modifications. There have been modifications, like let's add the people's. So, let's allow so like one problem of the lstm is that once you have fixed your age, all of this case do not have access to memory. So it's like you are erasing from memory, but you cannot look inside the memory to see, which are amazing, which is pretty strange. And people added like more inputs from C over here, which means even more matrices, right? More weight matrices. And at some point people try to maybe lose a few of these matrixes Maybe. Mmm. Maybe you can do without some of the gates, maybe you can like tweak their listing him a little bit and it turned out that yes for every like this. There was this famous paper called the htms respect. So it is him and basically said yeah, on our two examples where we could test a lot of illustration. You can actually like remove a whole gate and nothing much changes and then, there were Even better attempts. So why do we need to like so, Let us try to achieve the same goal. The goal of having memory that goes through this. How to say memory that goes through this? Pretty Highway of gradient flow, and let's keep it that way. But let's tweak this structure of their current cells, so that it will be more efficient. And people have been successful. So, for example, like the second, very famous recurrent unit is called the gru gated recurrent unit back in 2014, it was developed and if you look at it, it's very similar to the lstm but it has much less much fewer matrices. So what let me just walk you through here without drawing a separately so it still has of course the candidates well state. But now it doesn't distinguish between C and age, so you only have one hidden state. and in Stereo updating it separately with Erasing stuff and writing stuff. You do it all at once with the update gate. So basically the updated again, it's it's a control gate with the sigma at the output and it gives you numbers between 0 and 1. But now they are like coefficients of a convex combination. So if you look here on the right, you multiply H, the current memory state by you. and then you add These this H Prime the candidate from the that you proposed times 1 minus you, right? So it sounds like it makes a lot of sense. Right. Why do we want? Do we want to erase from memory to write something there? Why do we want to add something to memory? Because people already erased itself? And as I said, ostm is not about actual Edition, it's about racing and writing back to memory. So it makes a lot of sense to combine it into one game. And that's a that saves back to waitresses, right? And instead of the output gate, we have the reset gate, which does basically the same thing only in the same cell. And in the cell step, before it just looks at the memory and chooses, which part of it should go into the candidates hosted. So Gru's. Look great. Looks like they do exactly the same as a stms. Only more efficiently because now you have only six waitresses instead of eight or instead of 11. If you count people you don't need people now so it's more efficient. Should be better and so on and so forth. And indeed in like 2015 thousand sixteen if you look and for example papers and natural language processing, I was actually working in the field at that point and if you look at the papers on NLP, back in 2015, they all use chariots. They all switched the chair use and that was a big thing, etc. Etc. and then, for some reason, we cannot explain to you theoretically the whole field switched back to stems. So I mentioned Alpha star. How fast are? I don't remember the year, but of course, it's much later. It's like 2020. And if you have a current Network now, Probably it's more likely to be an lstm energy area. Somehow Schmidt, Cooper's construction is better and I'm sure the actual like decision making here is just, empirical, you're just saying, oh, okay. We've tried a list James. We've tried Jerry. So it's James for better. We can wear the costs, so, to speak with you. So, let's chips. Are, but why they are better? I have no idea. So like, what's what's so special about the lstm architecture? I don't know. But it's really interesting and it's really beautiful that it stands for so long. And remember all through the class, I was from time to time. I was mentioning stuff like, oh and then Google came and they had lots of compute and they ran this big neural architecture search. And now we have efficient net, which is better. Or now we have swoosh which is a great activation function and then people did something else. But at the point it was the best. And so Well, of course, they tried it with the current cells. Of course, there is a paper from Google, where they develop, exactly, this kind of thing, they tried to make recurrent cells more efficient. And yes, on the examples on the data sets where they test. Their occurrence cells, are better than lstms and Jerry use. And here is an example of their cell. Of course, we won't go through it. But as you can see, it has only four weight matrices. It's kind of similar to jru but it's even better. It's even more efficient. And nobody has ever heard about this sells. So most probably they don't work as advertised or I mean they don't I mean I'm not saying Google is lying. I'm saying they probably work on those examples where they were developed by the dungeon generalize to other situations and for some reason istream is still the best. It's still it's still stands. Okay. so, With this, I think I want to end. Our discussion of recurrent networks specifically. If there are any questions now is a good time. I will. Show you an example here. Um, yeah, so I have some, some code for today, not very deep, not very difficult, but I hope more interesting code will be in the practice session. So, this is just an illustration that of exploding convention gradients. It's, I mean, it's not even a real recurrent Network, it's just shows you that if you keep multiplying by a number less than one urination, if you keep multiplying by a number greater than one, you explode. And here is the real experiment. So, This is the classic lstm Benchmark from very long ago from right transmit Huber and it goes like this. You have an input of with two components. So they are like two input channels. One is just a set of numbers. It just goes just random numbers from 0 to 1. And another is a channel of zeros. With exactly two ones. So like here is a sample input, the markers show. The bars show, this random values that go between 0 and 1 and the Stars Mark the ones in in the market channel. So it's like a vector alone, stream of numbers and two of them are highlighted. And the question is at the two highlighted numbers? Give me the sum of two highlighted numbers. so, It's like a perfect toy test problem for memory, right? You need to when when they when the market Channel tells you to, you need to memorize this value and then when it tells you again, you need to add this value to MoneyGram price. And sure enough, let's DMS and Jerry use they both work well on this. And this is actually since it is so simple. This is actually a good example for junior used. Not always teams. So here, you will see that like a simple linear and doesn't work. It just like it it stays on the Baseline, which means no no training at all. Lstms. At some point, get what they are asked to do and they start learning, but in like 600 steps, they 630 iterations. They didn't yet, trained and Gru's have trained much faster and from, from a much earlier point. So this is the kind of plot that you would see convincing people that your user better. But this is a very easy problem, right? So, that's the point for a very easy problem. Of course, a more efficient, Cell will be better. But probably doesn't scale to really difficult problems. And yeah, and here is another sample from the, from the lstm. It's the same problem. It's just I take one of the inputs here, is the input. And then I look at what is actually the contents of memory. What are the outputs of the gates? And what is the current projection of the sum that you what is like, you're running? Guess what? What would be the output if your sequence stop right now? and as you can see it, rained lstm That's some very reasonable stuff. So it when it sees a star when it says a marker, the thing that it writes to the cell actually spikes. So, you write a lot of stuff here and you don't write much over here and your cell just Grows to the correct value. That's it. So if you take your running, guess then it indeed tracks. The true sum, and it goes to the truth after the second time. So it works. It's a very simple problem, but they but interesting there and this the interesting part here is Straightforward. Recurrent networks. Cannot do that. They, if you have just this linear, sell you simply cannot have this long-term memory that goes back and recalls at, oh, yeah, I had that number 15 Steps ago. Now I need to edit the present. And that's that that's the idea behind all of this current cells. Okay, so any questions about this? All right. well, with that, we go to our next topic and our next topic is probably the last time in class, when I again, Start from a neurobiological motivation when I again, tell you about the brain and everything. But now in a very superficial way, now we don't go from from a bird's eye view. We don't go to the details of how neurons operate we actually just stay on the level of, you know, how we think in general. And we are interested in the notion of attention and if you think about attention, like, I hope that you are paying attention to me right now even though I didn't really not sure. But, you know, if, but if you think about how how attention works and especially how lack of attention works, It's it's really funny thing. It's really unclear, how it's supposed to work. It's it's very like our brain seems to work very differently from in this regard, from how networks that we have seen so far official on your own networks work. so, like think of okay, we are in the computer vision class, so think of an image Think of looking at an image and, you know, registering some stuff some objects that are on the same as etc. Etc. I told you that. Our. Our visual cortex, the part of the brain. That processes images is kind of similar to convolutional networks at least in spirit. Like they cannot really be similar in architecture but in spirit it's it's like extracting local features then combining them to better to more Global features to semantically richer features Etc. and, But if I look at an image like right now, I am looking in my computer obviously, but my field of vision is, of course, much wider than just a computer. So if something happens, The outside of the computer and right now, I'm like thinking about our lecture and I'm writing something on the board. Most probably I'll miss it, right? Because I'm not paying attention to that. and paying attention to the board and but the stuff that's outside is still in my field of vision. So if you try to map this kind of attention thing to how neural networks work, It's, it's really strange. So when, when you go with a convolution over, An image. Of any size you get features extracted from every part of the image, right? and, Then this feature on next layers, they get combined into more Global features and showed you some some pictures yesterday. It's etc. Etc. And there is no place to lose stuff there, right. If I have a future image, okay? I will need to spend more compute, but it's not like I'm gonna lose some object from there. I will still extract features from every part of the image and they will still become binding or Global stuff and I will still have this. I don't know. Take the cat neuron up there that will steal. Activator on the cats. It's not like a conventional Network can just missed the cat. Completely impossible. But we do. What's the difference? The difference is an attention mechanism. And how it works is, actually a pretty difficult question. There was this guy Alexander Lurie? He was a very interesting man, very if you had a very interesting career because it was the 1930s 1940s, he lived in Sterling structure but still he was like a man of the world. He traveled to all the conferences he published in all of an international journals and he was like one of the international recognized fathers of the field of neurobiology and, Alexandra when he posted the main research program of neurobiology and general. He said that there is like three There, there's like three. Three, three, three, three, three, three, three, three three. Sorry, there are three main pillars. Three main components to the field of neurobiology and she said it's attention memory and cognitive functions which is basically like how we think. so, To him. And to the whole field of neurobiology attention is up there. And the level of memory and cognition. Well, of course, since Laurie, there has been a lot of progress, we kind of understand how attention works in the brain, but it's not really important for us from the computer science point of view, because in the brain attention works for memory more or less, it works for memory. There is. There are different types of memory in the brain. So there is this kind of working memory, which is very short term memory that stores, just a few latest objects. Like if we were offline in class, I would be able to demonstrate. So if you if you give a lecture and if you ask any person a personal who is not paying attention to you at all like this person is on on their phone chat with somebody Etc. But if you asked if you suddenly asked this person, tell me what they just said even if they were not paying attention at all they would be able to recite the last five words or so they would say oh yeah, you were just saying what it would be, right? But if you ask what I was saying 30 seconds ago it would be a blank right? So like working memory, is this very short-term mechanism of what's happening just now and mostly everything goes there? But then there is this. But then there is this filter, this filter of what goes to be processed in more, like, which parts of this recent stuff are actually important to process further and that's where stuff gets lost. So yeah. and, I won't spend more time on attention neurobiology Etc. It's an interesting topic but I think it's for us it's it's more important to go further if you've never seen. So I will just recommend you one thing. If you've never seen this video, where there are two teams of players, passing basketballs play a team on White and the team and black and you're supposed to count the passes of the team and white. If you haven't seen that video, please see it when I publish the slice. Okay, I can copy it here. Yeah, look at the test. It's interesting if people still fall for it because back in the 1990s, people definitely fell for it now. I'm not so sure, the our attention mechanisms have changed a little bit Anyway. So attention mechanism. So neurobiological works on attention. Actually. Show that even if you're looking directly at some stuff, this, this video shows that if you're actually even looking directly at some stuff, you are still. You are still not really. You still don't have the process. It it still may be lost. You still may like very early in the brain. You can decide to drop it. But also there is another thing we should probably have heard about and our it's it's about our vision in general. And our vision also kind of doesn't process the whole field of view. He probably know that you have this for real Spotlight. We have this small part of our field of vision where we look Well, where we can see stuff, very, very clearly in high definition and then it gets blurring and blurry, right? And we don't notice it because our guests constantly wanders around. Even if you're looking at your computer, still your constantly like it's called security motion your case constantly shifts and you look you get different Snippets of the whole picture and then your brain just kind of Constructs the whole picture from this small, from these relatively blurry components. So, like it's like different, several photographs of the same scene, but the focus is on different parts. Ah, and the original motivation to add attention, mechanisms to deploying was to, actually emulate this, to emulate how we see things to emulate this blurriness in the peripheral vision. And then of course sounds very strange. Why the Refuge you do that? Why would you make things blurry? If you don't have to in computer vision and conventional Network? You can just put in the whole picture. You don't need to blur anything. Why would you want to do that? In our eyes. I mean of course they have a wolf to to do stuff and maybe they didn't have the energy, the capabilities to that. But why do we need to compute computers? And the answer originally was to, to save weight to save input size to make it more efficient. So if you have a big image, And if you can actually instead of looking at the big image and you can actually do like three Snippets of the Big Image where you only actually use the pixels from a small small. If you small parts of the same image, Ah, and then the rest can be blurrier what it means to be blurrier. It means there are fewer pixels. Right? So the input size becomes smaller and much smaller actually. And if you have like three glimpses and everyone is just looking at a small part of the input, then of course, even the total input size will be much smaller. So originally people wanted to save processing by doing attention mechanisms. And the new thing here is that now you in addition to just recognizing stuff in addition to doing your classification problem, or whatever, from this blur images, you also need to choose where you look, So, you need to choose the positions of the glutes. and, these positions have and this positions, they form a sequence. Right. So this becomes a sequence problem because the next glimpse of course, can depend on what you see in the previous groups, right? So first, you okay, your first position can be chosen somehow generally, but then your second position will depend on what you've seen in the first one, right? So, early models of attention were current, there is this field of recurrent visual attention. I won't go into details because that's not too relevant now now it's all very different but More or less. The point was, you know, let's look at this picture more or less. The point was given a relatively big picture. Let's walk around it and choose where to look and blur the rest. And then you can actually be more accurate while being more efficient. And there is a recurrent mechanism in choosing this subsequently but yeah, this this is our date, you know, have to learn that. What is more relevant and more interesting? As what happened with attention. at the point where attention, Go to apply it to encoder decoder mechanisms. So let me yeah, let me first. Okay, so let me go back to the board because now I do want to explain stuff and let me first. Explain to you. What the problem is. So Let's first lstm. And now our second. Part for today is encoder. Decoder. With attention. So what what is the problem that we are solving well? Let's Okay, let me motivate this with machine translation. We, I mentioned machine translation before and it sounds like a perfect problem for recurrent encoder decoder, architectures. So you have your input which is like Hello World. Exclamation marks, okay. You read. Your input. This gives you some kind of hidden State and then the last hidden state, or maybe the last hidden state. Pushed through some kind of output head. Whatever gives you this vector. Let's go with Z, this intermediate representation of the inputs of the input. Sequence of this sentence, And then you take this Z. and, You decode it into. The output down, you know, English and Russian. So let me write it premium. Comma. Here. Exclamation mark, something like this, right? And and probably want to so yeah so probably doesn't look like this. Probably you have a hidden State over here H. Prime and Z is just the input to every To every cell. So probably the recurrence decoder looks like this. and when people did this, when people, had the compute to train vehicles and they actually try to apply list James engineer used to, with this kind of Architectures to say machine translation. They? Realized that they have. An unsolvable problem or at least an a problem unsolvable in this kind of architecture. So, Yes. This works, this defined state of the art in 2013 or whatever. And this actually gives you. Good results, with short sentences, a sentences like Hello World, it will work. Great. But you cannot scale it up. So, here is the thing. the main problem of of encoder decoder architecture is like this, Is in the dimension. Of this intermediate representation Z. and the problem is, you cannot have a good Dimension, it will be either to smaller to be if you have a c which is too short, He is too small. Then everything will trade, everything will be perfect, it will run fine, but you will not be able to fit a lot of meaning, a lot of information into a small Z of course. So for hello world, it will work. But of course I'm not talking about putting War and Peace inside a single Vector, but even for a long sentences, it will start to break down. And if you try to fix that by making the longer by extending the further and further and further, then it becomes harder and harder to train, right? So if you have a long day, It means that you're hidden state in the stems or your input to the decoder unless jams. Will become longer and longer. And that means you have quadratically more weights. And now, you don't have enough data and enough compute to actually train them. so, This is like a problem that you can't really solve inside this architecture. You can have either. You can either train. You can either have a good encoder decoder. It was to him with. Small disease or but but it won't scale up or you can have a large Seas, but then the training will be impossible. so in, in architectures like this, If you look at the graph of like, I don't know, whatever quality. I'm abstract here but some kind of quality metric and this is like tea, the sequence length. The input outputs in sequence length. What you actually see is like, it's very good while we have short sentences and then it just drops and it's very bad. And what you would want ideally. So of course, as Sentences get longer. You will need the quality will drop? But of course, you would want your graph to look like this, right? You would want it to to drop gracefully and still work for longer sequences. So this is what attention mechanisms for in order to order the current networks for suppose to fix. And this is an important concept that I think is still relevant. So, what is the problem with zip? Like where do we get this idea for this attention mechanism from the problem? We see Is that it's only one vector. For the whole input for the whole sequence. And this is what we need to change. And in Transformers also, there will not be a single Vector for the whole input. because, We kind of understand that sometimes we translate like specific words and when I am writing out here over here, I'm translating the word world and World should be more important as the input over here. Then it anything else? And here, there is no way to express that. I just need to cram everything into this single vector. so, the first step, Is to get rid of this assumption that everything needs to be in a single letter. So in this encoder decoder with attention, the first thing that I do, As. Okay, let me say hello world. Exclamation mark. And it's still a recurrent Network at the input. Let's say it's be directional because of course, it's be directional. It doesn't make sense, not to read the whole sentence. but it produces outputs for every X in the input. So there is a vector, let's say Z1. There is a vector Z2. And there is a vector Z3. So far it it's easier. Almost nothing has changed. Of course, if I can produce a vector at the end, I can produce it at every step. I just take the two hidden States. I push them through like one one layer of one. It Forward later in. There you go. Here is your zip. so, now I have this vectors for every input word for every turkey, But I can't just concatenate them all and feed them all over here. This is exactly. The Z is too long situation. I want to, I don't want to make them I don't. Yeah, I don't want to make them longer because that would make any sense that this will be just the same thing with stated differently. I want to have as input on every step here. I want to have one vector of this size. So how do I combine them into this single vector? And this is the attention mechanism. I do the following. I have. A small Network, the attention Network. That receives as input to the decoder to. So let's say, let's say that we are in the decoder and it's got like HT Prime over here. And we are writing the next word right now and we need to find out what is the current input over here, right? So that it will write the stocking and will produce H. Prime tip was one and so we are at some point in the decoding process. It. So the attention Network receives as input. Is from here. and, An H Prime from here. So it needs to, it needs to know where we are in the decoding process, of course, because the attention weight will be different for different words that I write. And then it will produce a score A1. Just a number. Four. That shows like how important this token is right now, okay? Like you will see how it gets used, so it's the score for token. Number one, At step T. So it at the point where in the point characterized by this hidden state of the decoder and then you do it for every See. so, you get So you get like a 2 for Z2 over here. And you get A3 for these three. Then. I convert this Ace. So let's call them the vector. A I can convert this a into probability Center. Convex combination, by passing it through a softmax. You see how it all comes together? We are we talked about soft Maxes, Logistics, sigmoid Etc. We talked about their properties and lecture or something, and now we are using all these properties. So it's not noticed that I'm using software's. Not just as the output but I am. So just using it to convert. Every time I need to convert just a set of numbers to convex combination to something that sounds to one. So and here I get something like Alphas. Now, they are. From 0 to 1 and they sum up to one. And that's it. These are the, these are the coefficients. For my combination. So now I just do like a DOT product and ZT here. Ziti here is just the sum of alpha, I times the I okay. So ZT is not a good letter. Let's call it. I don't know. Let's call it. What afterwards do I have letters that I have YouTube? Okay, so the input for for the the so the input for the decoder at time at time step, T is a linear combination of the representations of every token with weeds determined by the separate attention Network. So what this means, like they intuition behind this day. The motivation is that I want. this to A to express what specific tokens. I am translating right now, so like on step three. When I'm producing the third token, the third word I want. The word world to have a high weight over here. because I mostly translating the word world, well, in the context of the rest of the sentence, but mostly that And also notice and this the last important point about this before I proceed to just show a show to show you the results and everything in discussion. The last important point is this When I tell you this intuitions when I tell you stuff like oh, so the attention network is supposed to give you a high score for the word that we are translating right now. This is not. Any formal input for the network? There is no labeling in the data set that will tell you. Now I'm translating this talking now, I'm Translating that this, they, the data set is still the same. The data set is a set of pairs, like sentence in English sentence in Russian. They they match. They are translations of each other and here you go. 100,000 pairs of sentences trained on that. so, when I'm talking to you of intuitions, like this, What I mean, is we kind of want the network to work to work like that. And miraculously after trading it indeed works like that but we never explicitly trained trained the attention Network. The attention network is just this very small tiny component. It has very few weights compared to the listings. So, a practical number. If I remember correctly, would be something like 2% of the weights of the whole network goat, the attention mechanism. So it's a very small component compared to the rest of the network. but, This very small component, actually. Drives the results. This component is the difference between the red curve and the purple performer here. this component actually does trained to do this job of finding out, which A finding out which tokens we are translating right now and producing the correct weights. So it's a general principle of deep learning that we see quite often and I think we already saw it in convolutional networks, I just didn't call it out General principle. That very often, you just need to keep the network a chance. Right. You just need to Introduce some components inside that have. These potential ability. To do the job that you want. And even if you have no data to train them, even if you cannot take the attention Network out of this whole thing and train it separately and then plug it back in because oh, you don't have the inputs for these, right? Inputs are also changing as we train. And you don't have the Outpost. You don't have the correct answers here. But still, if you just structurally give the network a chance to do it right with sometimes not always but sometimes it will do that and everything will work and it will be like a very nice example of new structure inside of that. So this was what happened with encoder decoder. Architectures around 24 15. So in 2014, this was the state of the art. And in, okay, even in late 2014, but I don't know, let's call it introduced this kind of attention mechanism. So this this is exactly what I was just drawing, right? The attention Network that receives the current state of the decoder and the representation of a token from the input, and it gets you a score and then you do a softmax etc. Yeah, cheers. Here are the formulas and indeed and indeed It does trained to to do what you want. And also like a common feature of attention mechanisms, we will see that in Transformers 2. A common feature of attention mechanism says that they also give you something to look at. They give you some this attention weights when you actually draw them. And look at them there, probably usually very easy to interpret. So for example, this is from one of the original machine translation applications here. Here, they're translating from French to English. So, the instructions, if you have, for example, French and English mostly match mostly, it's a diagonal matrix where the high attention weight is on the deck and all your translation. This word by word, more or less. But notice the Exemptions right? So for example, a lot of restaurants here is translated as destruction. and, It's two words into one. There is an article in English here. So here the attention rate is high for both wine districts. You know why we are right in the destruction, right? And here, for example, arm comic, chemical weapons in French, the adjective goes after the noun in English, the opposite. So here the attention weights Swap and you see an opening I think I have. I have examples for you here too. So okay, so here here is a very simple recurrent network with attention that just learns to reverse the input. So, if the input is sequence by 34057, blah blah, the output will be blah, blah 75 043, right? And of course, the recurrent Network can train to do the same. It's it's not hard. Actually, by the way, without an attention mechanism. I don't have this experiments here, but I'm pretty sure that without the attention mechanism, it would be hard. It would be very difficult. Because if you don't, if you have just encoder decoder thing, if you don't have this attention mechanism, then you need to memorize the whole input sequence in order to write it down in the reverse order, right? So if you cannot memorize, the whole input, if you don't have enough space enough capacity in your intermediate representation to just memorize the whole input your screwed, you cannot do the reverse unless you remember it. Exactly. and, With attention, you don't have to remember anything. You just trained to have this of reversed and of reverse the economy Matrix and so it it's not on the diagonal because you have a special tokens like Um yeah, whatever you also have a special token here like and sequence but anyway, there is this clear diagonal structure that basically just tells you where to look and what to copy, right? Or here is a more difficult example. I'm sorry, I'm not running them online because it takes a little bit of time to train so just not to waste time waiting but I will probably certainly you will be able to run it yourself. So here is a slightly more difficult thing. Here is like a sorting thing. So now the input is a sequence of numbers and you need to sort them in the output. And here also you will see you can see that at step T, we attend to the current Teeth. Small Australia. So like the decoder, steps are along the vertical excess and this is the source position. And on the first step, the most attention is paid to position. Where there is a one on the Second Step where there is a three then to the four and six. And so So you can see that indeed the attention mechanism has trained to do with it once. And this was a big thing in 2015. And through the next couple of years, people were like, exploring this stuff and this kind of attention mechanism has a lot of benefits. Let me not waste time or talking to my sham about this. It can do work order better. It can do some very interesting stuff like calm, doing grammar as a foreign language so you can sometimes fit even. And yeah, okay, let me talk about this because we Transformers at 7 more. I want. So sometimes your output has some kind of complicated structure that doesn't look like a sequence. For example, if you're doing a syntax tree of your input, then your output is a tree. It's a graph, right? so, You. It doesn't look like you should use a recurrent Network to write out a graph. The graph is not a sequence, it's more complicated. But it turns out that if you just write down, your tree is a string and there are ways to represent the trees a string and you just treat this. three strings as a language to which you translate it works and I think with Transformers it would work even better. In 2016. There was a very interesting paper from Google where they basically published how they are. Google's neural machine translation system works and I won't go into details here but basically it was interesting to learn that Google transfer it all works in the exact same way it of course Google being Google. It was bigger. There was some tricks etc etc but basically it was in order to order with attention and by the way, my personal experience was that Around 2015 to 2016. When they switched from whatever they had before to this kind of architectures. Google translate actually became much better. I mean I was using all the time. All better to say, I wasn't but I had a side job at the time translating like research papers from Russian to English. And before about 2016, of course, I tried to use Google Translate but it was completely hopeless. So you would spend much more time on fixing the results of Google translate, then you wouldn't just typing the stuff from scratch. It was completely useless. And in 2016 2050 and there was a phase transition. Suddenly sure. It was still bad. Sure. You still needed to edit it. You still doing it to edit translation 7 from the latest quote and GT but now it was more efficient to First, do a pass with Google translate and then fix the mistakes or they you know, but writing then, To do everything from scratch yourself. This, this was the moment when machine translation actually started doing some useful work for me, Um, and yeah. Okay, so let me skip that. And the last Point here, is that when I'm talking about in order to the other architectures, usually, I talk about like the same kind of architecture and the encoder and the decoder. So now we are doing machine translation. It was a recurrent encoder that reads text and the current recorder the right steps. Doesn't have to be this way, right? So you can definitely have encoder decoder, architectures. Where the input has one modality and one kind of network in the output is a completely different kind of network, completely different models. I don't even think this count as multiple model architecture, is because well, they are multimodal. But the two modalities are separate really because all you need from the encoder is to give you a vector representation and then you take this Vector presentation and plug it into the decoder. so, for example, I mentioned at some point, I think the captioning problem here is the captioning problem as it wasn't 2015, with a straightforward and quarter, decoder thing, Um, they encoder was a googlenet that we discussed. The decoder was an lstm. And it became much better when people edit an attention mechanism. And again, this, this is also important and important for what will come later? Notice that you can do the exact same thing. This kind of attention highlighting specific parts of the input. Even if you're input is not text, even if your input is not a sequence. So if you have a picture for example, the only difference here is that now we don't compress the whole picture to a single feature vector. Like we would do if it was a straightforward little political order. We have the same. CM the same convolutional thing. And then I just Stopped it a little bit short of the little bit in the middle so that I still have some geometry left. Like in this example, the input is not the 56 by 2506 and they stopped the feature extraction when I have a 14 by 14 feature. And now I have this quote, unquote pixels. Elements of the feature map vectors. And I can do a tension over this vectors. So, now I can have an attention Network that combines, that gives me coefficients to combine these. 192. 96 right? No wait. For my fortune. 193 right? No. Let's just, yeah. so this Fortune by 4 chain, Different vectors and they have this. So my coefficients will combine this Fortune squared vectors. And again, it kind of works. I won't go into details and another nice thing. Nice thing is that it gives you the actual attention weights. You can look at them and you can interpret them. So, we will kind of see that in Transformers still, but it will be actually less clear and more complicated and Transformers. But here it's very clear, it's very straightforward. You can just see what the network is looking at right now as it actually write this piece of the output. So it a woman throwing a frisbee in the park. Here is woman, we are writing woman. We look at the people and then throwing and we start concentrating on the throwing and freeze beware concentrated on the face. Be and when when I ride down the park then they are not looking at the people we are looking at the background so that's that's just perfect. Okay. So I want to stop here. Are there any questions at this point? You actually covered quite a lot. It's in promo sgms from the attention mechanisms required attention and Onto encoder decoder attention. Wonderful. So let's have a break please. Let's not have a half an hour break because today Our Administration asked me to, to have a call. It what? One 20. So let's have a 15 minute break and then we'll reconvene and we'll discuss. we'll discuss the main architecture of The entire deep learning right now. For the last 10 years, the Transformer Right. Okay. so, On to the Transformer's. Well. Here. Yep. So Transformers appeared in 2017. and, It was. kind of, I mean, let me start with the brief historical remarks. So in 2017, when this paper appeared, at the end of the year, I don't think I'm pretty sure the the authors. Of the Transformer, paper of attention is all you need actually understood what they were doing. so the paper is not that ambitious, we will see what its results were originally and they are mostly about like Here is a different way to do stuff which provides approximately the same results, but which is more efficient. Maybe let's switch to this more efficient way of doing, basically the same but, Since then. The whole field of machine learning switch to Transformers, as we all know and much of the rest of our class will be billed on the Transformers. So we will use Transformers in different ways. so, The main, I think. Positive qualities that the Transformer had that the original paper didn't really couldn't really notice it from from its experiments. Are two things, one it turned out that proved to be very, very general. In the sense that the Transformer is just very good at noticing internal correlations within complicated data, right? And it doesn't really matter for the Transformer with, or its text or images or whatever. It just works with sequences of vectors. And it doesn't care where? This vectors come from. So this is a great thing. And even more important thing is that Transformers proved to be extremely scalable. You can take it Transformer, you can scale it up, and it works better. You can scale it further up without changing anything inside. Well, sure there have been Novelties. Sure, modern Transformers are slightly different from the one we had 10 years ago, but it's mostly the same and still your scale. What happened? That works better and better and better and never situates with our large language models. I hope I will have time to talk about that next week with large language models. We keep going from like tens of millions of millions of billions 200 billions to now trillions of parameters and they just keep getting better and this has had never happened before. You can't scale lstms in the same way or I mean maybe you can but we don't have enough compute to do that, but I think the complexity grows so fast or they say Trade. And they even if you can't train them, they stopped providing any benefit. And in the Transformer it kind of all came together. So what is the Transformer? I will actually go through the slides first through some of the slides first because the basic structure is very similar to what we were. Just discussing. It doesn't, I don't have to redraw it but then the main core will be the self-attention mechanism and that is completely new. And that I will, of course you discuss in detail. So this is the most famous picture from the original paper but I think it's pretty hard to understand. So I make my own pictures here and here is the structure of the original transform. Without details, without the interesting Parts. But the general structure is actually very Straightforward. And it's very similar to what we just had in recurrent and others attention architecture. So it's important architecture and yes, the original Transformer was doing machine translation. It has an encoder which consists of six, identical layers, it has a decoder, which consists of 6%, clears and the encoder receives text in one language. The decoder produces text in another one. Let's let's say in this Paradigm for now. Are interesting Parts here. What can we see on this picture? So first of all, the input to the actual Transformer, the actual and quadrant layers is not just the sequence of tokens. And we didn't discuss it in detail. I mean text is not our thing, but it's it had been very common in natural language processing. Even 10 years ago to convert. One hot representation of words of tokens to continuous representations, that are usually call them bearings. This is again, very, very common, very straightforward, all through deep learning if you have a large vocabulary of different stuff that you want to import. Like, in this case, different words or tokens parts of words, Then. and then, Then sorry, then you first want to convert them to dense vectors and there is like a whole line of work and an opium on this like word to their glove fast, text different embeddings, we won't go there, but here the embeds are really straightforward. There is just one very interesting technical thing that I will talk to afterwards in the end, but mostly it's just, you know, a matrix of vectors. So for every input token, there is a vector. And we look at up and we put it in place of this talk, that's it. And, but importantly, it's not some external representation. It's not some work to act that we copy here. It's an embedding player that is trained with the rest of the network. So you train this Vector representation. So along with the other ways, And after this embedding player, the input sequence becomes a sequence of actors. And all the actual Transformers doing. It's rewriting. Sequences of vectors into sequences of vectors. So every encoder layer will take a sequence of vectors as input and produce. The same sequence of vectors. Well, I mean, sequence of vectors from the same size as our output. And that will. And that will rewrite this kind of structure for in this case, 6 times. And then we get a vector for every input token. After all of this encoding, it's no longer just representation of the token. It's now representation of the token in the context of all the other tokens. And I mean, it has many times it has looked at all the other tokens at the whole sentence. The whole sequence, Etc. So by now, by the top, here we have this representation of smart. Semantic acceleration, presentations of inputs. And now what does the decoder do? The decoder. Is a language model. I hope you heard of language models. So the decoder is producing output tokens one by one. Out the aggressively, right? So it's input is what it has already written by the history of input until now and its output is the next token. Right? So after the decoder so you have to run the Transformer decoder as many times as the number of tokens that you want to produce. And this is one kind of restriction that in modern language models you need to work around and wait, there there is A big signs around. It speculative decoding and stuff like that, but you want to go there anyway, by default, it's not regressive thing. You produce the output torque converter and, these guys, the stuff that you are actually translating, Sorry, I don't really understand this. Can you see My cursor. You can't write. Yeah. Okay, so pointing with the mouse, doesn't really work. All right, so the stuff that is at the output of the encoder on top left here. It's It's getting used in the decoder on every layer on every step of the way. And of course, we will discuss how exactly But this. This high level, this high level structure is very similar to what we just saw right and coder the coder and not, there is no separate attention Network here. The attention will be hidden inside the encoder and the decoder. so, if you look inside, and quarter layer in the D quarter layer, you will see the The end quarter layer actually, I think. Okay, yeah, I have here. So the end code layer is what it's a self-attention layer. Then layer normally Asian. Then interestingly, If It Forward layer a fully connected layer, then another layer norm and that's it. So of course, the interesting part, the part we are going to discuss in detail, is self-attention, right? The self-attention is the first layer here. But the rest also uses this components that we have been discussing, right? So it's not we are not discussing ancient history. Everything that all the ideas that I'm telling you are actually being used right now. For example here we see a residual connection that goes around the self-attention layer right? And it lands actually, I forget in front or afterwards, but near this layer normally layer, we is a kind of batch Norm, right? So you just discussed it with Alex and practice layer Norm is like bitch Norm but not across the meaning, which but across all of the outputs of the current player. So Transformers a big and then Transformers Oops. Sorry. Recording in progress. Yeah, I want to chase. I'm not sure what happened but somehow I got disconnected from Zoom. um, You know. The internet works. I hope you can see. Ya. so, So the where did this stop? Yeah, there the end. So the encoder layer uses, this layer Norm at the output of self-attention and layer Norm as you discussed with Alex just averages out. Gradients keeps the Lost landscape. Smooth keeps it under control. In terms of the absolute value of output Etc. And here Transformers are big so we cannot really We cannot really rely on. Bachelor because the probably there is no bitch, probably only one copy of the Transformer fits into our memory and we have on the one instance. So we use later. And then interestingly, there is just a feed-forward layer and it's actually a very important that it has a lot of Weights. If you look at it, it takes up quite a lot of the quite quite, a big fraction of the entire weights of the Transformer. And there is nothing to say about it. It's just, you know, rearranging the features mixing together the features in every Vector separately. As you can see, it's applied to every Z Prime individual, and then there is another layer, and that's the encoder layer. In the decoder. You also have self-attention. It's exactly the same as a self-attention here, except for the word mosque, but we'll get there. There is also, if it Forward layer, all. So, layer Norms are after everything. And the only difference is this in quarter decoder, attention layers. So the outputs of the encoder, this Vector representations, they Should go somewhere, right? They should be doing something and they go here. And when we get there, I'll explain what exactly and then, after the decoder has, After we've gone through the decoder, then, of course, we have to do some classification. So, there is a linear layer that goes to a soft matte layer and the softmax produces probabilities, and then you sample, the next token of this probabilities. So, again, as you can see, it's exactly the logistic regression at the end, so it all kind of comes together. All right, so this is the general structure. And on this picture, there should be absolutely nothing new to Except. Of course, the self-attention stuff. So what is self-attention? What exactly how do we understand it? Where does it come from? It number three for today. So touch. Well. Actually discuss self attention. I need to take a step back and I need to talk to you, surprisingly. About information retrieval. Which is not the subject of our class but turns out to be made around. So how does search work in deep learning? How does information retrieval work when you have neural networks? Basically, it works like this. You have say, queries. Very one, very two. And you have documents. Okay, one. Document 2 document 3. document for And in usual information, retrieval what you would do? You would. Establish a similarity. You need to establish some kind of similarity between queries and documents. This kind of similarity will be called relevance and you will train it to be the relevance, right? So, It should be higher when this document is relevant to this query. This is how search generally Works. What whatever is But when you have the bearing, when you have this neural networks, that can process any kinds of input, and that can train to process long texts, large, images, Etc. What he usually do is this. You. Get. Documents. Rowan encoder. And the documents will become vectors. You get queries through their own encoder. So they become vectors to. And the idea. Is that all of this vectors should leave in the same space? so even though in quarters are different, they cannot be the same because documents can be images for example. So there are different at first but they should produce vectors in the same latent space. So like documents get my apps over here. And then you may have your query over here. and, You are supposed to train the whole system. So that the relevant documents will be closed, they representations of relevant. Documents will be closed to the representations of the queries. So like then, inside this latent space. You will be able to just you know take nearest Neighbors in, this nearest neighbors will be a good answer to the search query. Okay. So I was drawing this but I think I have a picture about. Yeah. so, you have a query, you have a document documents, go through their own, encoders queries, go through their own orders and then like the whole point of it is so that in the latent space in the late in space, you actually Have. This structure that relevant documents will be near the images of the queries, okay? There is a whole field of study about how to do that. It's obviously very very Big Assumption of. Learning and we could have a whole class on information retrievable maybe you will. So I won't, I won't go into more details but what we need now is this basic intuition that Different stuff gets mapped to the same latent space and in that latent space. We are just looking for nearest neighbors and since it's, since you can do it linearly as a linear space, basically this, the similarity here between the query and the document, is can be thought of as just, the Dot product of the corresponding vectors. So like I encode the document and I multiply it by the encoding of the query, that's it. Okay, and this approach has lots of advantages for information retrieval. You can just store the vectors. You don't have to think about anything else. It's fast to do it in the low dimensional space blah blah, very good. And so attention. Interestingly enough drawers on this intuition? But since itself attention, it applies this ideas to like the same set of vectors that are both. The are both queries and documents. Here is how it works. Here is how it works. Okay. Here is how it works. Here is how it works. So we begin With. A set of vectors. As I said, every layer of the Transformer gets just a sequence of vectors as input. So, we have this. One. X2 and so on. X. And okay we have this vectors Vector inputs. Now, I want to make this kind of Query document thing. So in information retrieval, it terminology is inherited from like classical information retrieval. You would sometimes call this image from documents, the representation of documents, you would call the keys. Okay, In classical retrieval, the query would not need to be encoded. It would be just aquarius. So there is no word for the image of the query, but okay, we will just call it the query. So let's, let's, let's say that the query already lives in this space and the document should be mapped there and should produce some kind of a key. And here we take our access, let's say we take X1 and we produce from it queries keys and values. So, with X1, we multiply it by a matrix called WQ. And as a result, we get the first query vector. This will be q1. Okay. Then. We take. All of the inputs. All of the excess. And we multiply them by The Matrix WK. Just put it here, once not copy it many times and we get the key. Vectors we get K1. A K2. And so on. Okay. And And the whole point of self-attention is that q and K. Should live in the same latent space. So now, this guy goes here. These guys also go here. and the similarity. Between. Q and K. It's just a DOT product between them. It's we assume that they already live in the slate and space. They are they they have the same Dimension are and this similarity. Is exactly the score that we will use. This is the attention of it. so, You see queue was made from X. Hey what's my also made from X and now we look at like how similar q and Care between each other. so, out of this space, we get like this sequence of Ah, attention scores. So to say affinities, right? We get like a one one, which is q1 times K1 as well and then a12 and so on a one and which is q1 times km Right. So we get this. Vector of attention Affinity as we put it through the softmax as usual. and we get, Yes, sorry. Also I forgot one one detail I'll get to it later but we put through the softmax we scale first by square root of d. And then we put it through the software. So this kind of transformation. I'll explain later. Why? Why? We need risk scaling? And then we get this Vector of attention weights. So now we have this this will be like a one in. This will be awful one. So this is the actual potential weights between 0 and 1 rescale to sum up to one and They are the similarities between the first query, the first query and all the keys. Right, similarities, rescaled back to a set of weights. So now we need to use the set of weights to make some kind of linear combination to make a complex combination of something. Well. Of what? Of another set of vectors. Here is the thing. So, now we again, take all of the excess, And we multiply them by yet another Matrix. Wait Matrix WV and we get, Vectors that we call values. We want to be in values. So the green ones are really use the blue ones are keys and the red ones are queries. and now, We take all of these videos. Am we multiply them? With the dot product, we multiply them, we add them up with the coefficient self. so, this is what This is what's the dot product? How do I like this, right? Maybe Anyway, dot product. So the output is how it's called Z1. It's the sum of Alpha One. I times V. Okay. And that's it. That's the basic idea of attention. And of course, I only Drew one query but it then gets repeated. So we take X2 we multiply it by WQ. We get Q2 it also gets my here. Blah blah blah and test the output begins it to which is the sum of two I again times V. So and we answered Right. So this takes a little bit of understanding. Here cosine similarity. Yeah. Right. So this takes a little bit of understanding to get it in your head because it's all very abstract, right? It's just some dot products and some new space. In this new space is just multiplication by the weight matrices. There is nothing like to nothing too intuitive here. Well, I tried to give you the basic intuition for information retrieval, but I mean, it only goes so far still. Formerly. It's really, really simple. All right. So what we do for formerly is we take the excess from multiply them by double by by matrix forget aquarius. So in practice, of course you would not do it, step by step. You would do it all at once. So like, your Aquarius are some weight Matrix times x. Or maybe the other way around. If I forget, which one is more, commonly extends? This metrics doesn't matter and your keys are some weight Matrix times and here waiting videos. Okay. Are some weight Matrix times x, right? And then What do you do with this Matrix is so if we continue the formal stuff, you need to get this Matrix of all possible. Cosine similarities. You write all possible dot products between queries and keys. So if you write it in Matrix forms, then it will be like Q times K transpose. This will be the Matrix where the ij's element will be like UI dot product by KJ. Wright. And then you take this queue times K transpose and your risk scale. You do so softmax and then you multiply by the result. The vector speed. So, the attention weights. Are. The softmax. Of one of the square root of G Q transpose. And the actual output disease. Is what software? Of 1 over the square root of d q. K transpose, times V. And that's the main formula that you see everywhere, right? This this is from the original attention, is all you need paper and this is exactly what I was trying to explain to you here. so, The intuition about the this Matrix is there dimensions and everything, is that adds is probably pretty big. Pretty long. It's from some art to, I don't know, some capital G, and queries and keys have to live in the same space. We have to make dot products with them, so they both have to be lifting in the same smaller space. Small d. So this Matrix and this Matrix are both like gay times, small D matrices and really was formerly. Can have a different size, right? We never take a DOT product between V and Q or V and K. So formerly, it could be like deep Prime in practice. Usually it's the same deal of course, but formerly. Let me write that. This is like a d times D, Prime Matrix. It or sorry, the way the way I write. It should be that way around. Could be. A g times capital D and this should be deprived. Thanks. Okay. So what else can I say here? Tells can I see here? I think that's it for the basic idea of potential. We got from the beginning to the end. I will show you a nice picture in a sec. Let me just highlight one thing. So yeah, okay sorry. I promise to explain where the square root of decomp from why. Why the risk? Well, the risk scaling goes like this. What we have here, what we have in this Raw Affinities between queries and kiss, like, dot products between vectors of entity. Right? And if you think of say queries in case, it's just random vectors vectors with random numbers inside. You see that? What do you? Say something. Don't you see that this vectors with queries in case inside? Hmm. If you think of them, it's just random vectors. So like if let's say it's like Qi is something like zero plus or minus 1, right? So it's something from minus one to one. On their average, maybe more, maybe less, but more or less. It has like a standard deviation of one around here. And KJ also has a standard deviation of one around 0. Then, what is happening here? This is the sum of d. Much. Number is deviation. One. and if you take the sum of the random variables, Each of, which can go to plus or minus one, A approximately on average then the result will have a variance on the order of give or take square root of d. I don't want to do probability Theory now, it's it's a classical result, basically, I think if you ever had a probability of theory class, you probably know this in the form of random walks on the line. Like if you go from zero and you flip a coin and every time you go either right or left and how far from 0 do you expect to be in N steps? And the answer is square. Root of him. so it's it's the exact same effect, and that means that if we don't do this, We will have like big numbers over here. We will, if for example, D is something like 64 which I think was true for the first Transformer. Then when you add 64 numbers, you get numbers on the order of like plus or minus 8. And plus for minus 8 is more or less, more or less means that the output of the softmax will be closed to just one zeroes close to one hot vector. Which is not really what we need. We needed to be smoother here. So we smooth it back. We rescale it back so that we go from the square root of D back to give or take one. That's, that's an explanation for the scaling. And what else? I can notice right here, right now is that we already see the main computational problem of Transformers. I don't think we will have time in class to discuss this huge line of work that tries to, to avoid this to work with it, but we definitely should mention the problem itself. Here to compute this, you need to have this Matrix, you need to compute this Matrix, and this Matrix is an end times and Matrix. And this is like, quadratic complexity. Or create a complexity as a function of the input length of the length of the input sequence. And that is the main computational problem of Transformers because it means that you cannot scale them up with respect to the inputs to the input length unless you unless you do some interesting tricks. And of course there are a million different interesting tricks. It's it's a big field. But basically, if you remember like three years ago when people were doing large language models, they would be like boasting about their contact size. They would be saying like, oh our llm has a contact size of 128,000 tokens and our LM has 500 12,000 tokens. And we have got a million token contacts with I mean, this is about that. So it's it's not trivial to get to a million token contacts window. It doesn't just mean that your, it doesn't mean that the complexity is a million times. One token. It means the complexity is a million square times 1 token and the million square is just too much definitely so you cannot do it straightforwardly as this Matrix you have to invent some tricks around it and of course there is a big field of science around this. ah even right now, I think if you go to to Cloud you will see that it has a separate model called Opus with a 1, million token context and it's More expensive more complicated than just straightforward opposed, which obviously has a smaller content size, right? So contacts is is a difficult problem for Transformers. But other than that, it's all here. This is how self-attention works. And I won't try to draw it on the board. I will show you it to you on site but the next the next thing and another idea that we actually were discussing a couple of days ago and now it all comes together. Another important idea here is that notice what we are doing to assess Again, let's look at it from this geometric perspective. I think yesterday they were talking about this geometric, the geometry geometrically, what we are doing is we are taking this X in a big space. And we are projecting it to a much smaller space. In two different ways in these two ways. Give us the queries in the case. So again, I can't give you like tangible intuition that you can touch. But mathematically what you are doing is you have a big space. And you're looking for a good projection for the queries and another, but the same dimensional projection for the case. So, like two ways of looking at the set of vectors X. and then there is the third projection, which can have a different dimension for the various So in a way, it's again the same question that I asked yesterday, if all I do is assess, this vectors is compressed and down to query skin values. And in practice like if you have no capital D, something like 2:56 or 512, it would have small D, something like 64. As I said, then why do you need the long factors at all? Same question as we had yesterday and it's the same answer. The answer is, this is what I've just drawn to. You is just one attention head. And in a fair in practice, in a Transformer, you will have several different attention. Heads, each will have its own Matrix, matrices wqwk WV, and they will produce their own, kind of ways, of looking at the input and ultimately, they will produce their own output zi. So, really there is another in the index in here. Okay. Let's look at this slide. I have better pictures up there. So this is the intuition coming from self-attention. And this is the picture that I was just drawing. So let's, let's walk through it again. It's the most important picture of the whole class, I think. The input is a set of vectors. Each Vector gets multiplied by three, matrices WQ, gives you the query WK gives you the key, WV gives you the value. And then the queries, and the case should live in the same latent space. You take well okay set, cosine similarity as I do product because of course, nothing forces them to have like normal one and we do not want to rescale by enormous to complicate it. So let me just stick to that products, we take the dot product between q and every K. We get this definitive then we scale by the square root of K here is called q but it's square root with the dimension. Then we take the softmax and we get the actual weights, convex weights and we have this products combination of the vectors V. We these weights. Okay. So oh and notice by the way, how we are actually looking on all input. By every query. So, like every X in here is looking on every token from the input on every other X and on yourself on a cell as well on Xbox one too. So this. Yes. So sorry I should probably say this explicitly here. This is another very important property that makes Transformers so cool. And this property is Here, if you have X1 X2 X K, blah, blah, x capital l. And let's assume that you want to like find out, you want your X1 to influence to have some relation with X scale over here. So like this word in the input, text has relevance to this work. To have the current Network. This influence would have to go step by step through all of this intermediate vectors. Right? So, there is no path in their current Network that jumps over tokens. You just go step by step. and of course, even if you have an hasta with this memory cell with this, Constant error, Carousel, the highway that connects every Point. Still a lot can happen as you go step by step through this sequence. With the Transformer. You don't have to do. That is the Transformer. You just jump in one step from here to here. And you can actually jump to every token and you do jump to every token and every step. So this is great. This is like one step. From. Every eye to every J. And this is a big plus And the cost of this is this quadratic complexity. This is the big minus, okay. So at a current network has linear complexity. As you add more elements to the sequence, you just do more steps but each step has the same size as the same complexity. So the current that works are linear in the input. Size Transformers, work with content, it's a huge difference. But they are then more free to notice the relations and they don't care about how far it is from one talking to the other. They just see the whole sequence at once on every layer on every step, and that is great. um, Okay, so yeah. And this is the picture that I wanted to draw on the board. Yeah, please ask a question. I think it's in really understand about the value of space. Like I understood that theory. Sorry, I'm back. I truly hope that the recording is not garbled after that. I'm OBS Studio. Creating Anyway yeah please. What was the question? I'm Transformer related well. I'm more or less, understood about the key and curious part is that we they shared the same space and space. And the way we are interested in finding the closest distance. Between them. We're scared him, Etc. But but the point, I didn't really understand about the value value Vector. Not that even doctors and also the space. How is it formed? Yeah. Okay I I got the question actually. Yeah, I'm Problem is I don't have a good answer to that, so I don't have a good intuition for why we need the values at all, why can't it be just X? That is a good question. Yeah, that is a good question. I guess like The Superficial answer is that. Well I mean still every attention had is trying to highlight some aspect of the input and in terms of the values all so we want to kind of how to say this, we want to highlight a specific like projection of the big vectors X and we want to simplify them to to highlight this thing that we are looking for with this specific queries and this specific case. But that's not really a satisfactory answer. I think the true answer is over here and the answer is if so, like what does the value of vector Define it? What does the length of the very? Where does the length of the value come in? What is it important? The Links of the value of vector defines the length of the output, the size of the output, right? So your output is a combination of these. So, the length of Z of the one is the same length as the length of V. And I guess it would be it would just wouldn't make sense. It would be too inefficient and too much too many weights, Etc to have many X sized these and then combine them together and compress them back down to a single X. Okay? So I guess that's just an efficiency thing. so yeah, we could just use x as the document, but I, I suppose this would make this multi-head attention to difficult and we really want multi-headed attention as I just explained. Does that make sense? It's a bit confusing. Okay. So let me go through this slide. Maybe it'll be a bit less confusing. So we have actually several multiple of this attention heads, okay, we have had one had two headache and when we have had one had to finish every one of them gives us the set of these, The Matrix Z, which is these, that is in the boxed formula here, right? But now we have multiple Sciences And we need to combine them together. And after that, now the the output of this step. Now it has to make the input size. Well, it's not doesn't have to but it does it usually, it doesn't practice, just so that we can make another layer exactly like this. We can just copy the layers. So, This Matrix Z at the very end at the top right of this. Should have the exact same size as the input Matrix X, okay? But the intermediate representations they are much better. So let me maybe just briefly throw it here since this is not. Not that easy to understand. So we have this one Matrix X which is like capital D times, L is the number of vectors is the vector size. And this goes through attention head. Number. At. Number one. Okay, attention had number two, blah blah. Attention. Hit number H. And this one gives you a matrix Z1. This one gives you Matrix Z2, this one gives you Matrix CH and these guys are What's Happening Here? Recording in progress. Sorry, I don't know what's happening here today? Like all problems combined. Okay, so we have multiple we have multiple attention heads and every attention had gives you And you may Matrix z a different Matrix you see, and now we need to merge the mold together. So, everyone of this Matrix is like a small details element Matrix, but then when you string them all together, the one then Z2, then zh You get a pretty big Matrix. So if you just communicating them like this. No, I should. Okay. So let's say that this is L times d. Naught, L times. Not D times out. Now I will concatenate properly all types Capital. Yeah, so when I concatenate them together I get the Matrix which is still l in terms of the roles but now it's l times. H times d. And H times D is probably bigger than capital D and it's it's a lot. So what we do here in a Transformer, we multiply it by another Matrix of Weights so it's like just the feet forward layer, we mix up all the features again. And this fit forward layer gives us the Matrix Z. So this this is the Matrix of size. What? HD times Capitol building something like this. Okay. So My intuition for this is that. We really, first of all, we need some variety in. Disease, we need more variety. Not just linear combinations of the same vectors with different coefficients, but different projections of this vectors this this gives us more variety and more expressive power and two. If we just had this small G equal to the Big D, now, this guy would be just invisible to train would be just to be So I guess this combination of two things that we want here. Okay. I understood your intuition. Okay, thank you for trying. It was clear. Thank you. All right. So, what we have here? Is. One attention had copied multiple times. They wrote attention heads, they are all processed in parallel. And as the output we gave we get this Matrix C. and this this if we, yeah, if we look at Where where we are now, we have explained, we have expressed exactly this one, self-attention layer on the bottom left. This first self-attention layer from the The first self-attention layer from the encoder. But notice that it's basically almost all that we need. So, what's left? first, what's left is Okay, so first let me go through The Masks of attention in the decoder. And actually, let's, let's talk about the decoder. So we have completely, we are completely done with the encoder part. That's it. So potentially just described then layer normally know fit forward, just one Matrix to mix up the weights, know it makes up their presentations, we know that's it. In the decoder. There are there is more stuff to think about. So what is masks self-attention? What does it mean? Well actually, I don't able to explain it in detail because that's a pure efficiency thing. so, like, When I draw a picture like this one, where the decoder is only predicting the next token. There is actually a mask, self-attention is just self-attention. That's it. So we have the current state of the prefix, it's on the bottom, right? We have the current state of the prefix it goes into self-attention. It's just exactly the self-attention to be just described where the masks come in is that How do we train a language model? How do we train? Let me explain it. Briefly, how do we train a Transformer decoder, or the whole Transformer, with encoder and decoder? We have this output Right. So this is like the sentence that we need to produce. and, in terms of the, Transformer decoder. This output sentence is like one to three, four, five, six, different seven, actually different training samples. so, The yes. So the first training sample is, you produce the from nothing from nothing and from the representation, from the encoder, the second training sample is from the prefix. The you're supposed to produce cat, the third from the cat, your supposed to produce set and so on, right? So it's like the end, the decoder should be run, seven times here, it produces six words and then it should produce like the stop talking, the token. It's done. and, You can do it formerly. You can just do it as seven different training samples. But of course it's inefficient. So in practice what you do is you just, you take this one sequence, You say that? Okay, I'm supposed to produce. So I have this, I have this decoder in the Transformer. I have all of the inputs available here. I have all of the outputs here and then I'm supposed to have the here cat here, blah, blah, blah, and like this top token here, And this is where the masks are needed. Because, of course, when I'm producing the word cat, This like computational path is not supposed to look anywhere except to the word Z. Right. So, I need to mask out all of the other tokens, otherwise it wouldn't be much of a problem, right? They just need to copy the input to the output. Of course, there would be nothing to do that. So the mask self-attention layer, what it's doing is, it's blocking all of the tokens except It's called causality, it's called Coastal masks. Ah because it preserves causality, right? So token number T can only depend on positions of one. So I want to T minus 1, right? And yeah, it's it. Some work in terms of the programming of the implementation of the self-attention. So basically you need to like zero out the way that are not supposed to be there like when the input has everything now, but when you are producing the two you are supposed to have this attention to be exactly zero in this attention, wait to be exactly 0 and you're supposed to only look at the first token. That's that's what the masks, that's it. So this is the master of attention part. And then they Encoded attention part. So there was a, how do, how does this conditioning work? We are from the, we are looking at the Ah, encoder. Sorry, we are looking at the at the same self-attention layer, but now we also need to somehow have the Z inputs have to the inputs that are produced by the encoder. Otherwise. What's the point of having encoder, right? And it sounds like it's, it would you would need to do something more, even more complicated. You would need to change something here because now there is this whole new input that stuff. Actually no actually. It's very, very simple. The self-attention stays exactly the same. all this picture stays exactly the same, there is only one difference so in In a quarter, decoder attention. Quarter. The quarter attention. Your prefix. Your ex the input from from the decoder. Produces the queries. You multiply by WQ and you get the Matrix Cube and the key isn't really use. Are produced by the. From the representations, from the encoder. So w. Okay WV and you get the K and V matrices. Okay. So no difference to this processing at all but now we have like the only difference is over. Here we are not producing all three things from the same X. We are producing the queue thing from the X and the K. And we think from some from the condition notice that it doesn't break anything. so over here, I told you that this attention Matrix is A square Matrix of size L times, L and times. And this over here. Well, now it's not quadratic anymore. So now there is a different number of queries and keys. Obviously the lengths of the sequences will not be the same. But that's okay, right? Whenever whenever assume that we had the same number of kissing queries For every query, we multiply it by all keys. So we get as many attention weights as there are keys. So the number of keys should match the number of values nature because then we add up values with this coefficients. but, The queries can be completely different and actually we will later when we discuss for example, object detection with Transformers, We will see that they're also queries and keys and various will be some very different things will be produced from very different things. So it's a common idea in Transformers to have queries come from one source and keys and values to come from another. And yeah, it dates back to the original Transformer and in the original Transformer, decoder, already. This is how we use the outputs of the encoder. Okay, so that's basically eat about the architecture. That's it about this picture. There are. Okay, any questions at this point? Because this is, I think. The most important architecture in the world, right? Um, so yeah, it's a lot the process. I don't expect you to like internalized it right now, right? Right from my words. But when you think it through once again, when you go through the pictures once more, and especially if you ever actually implemented, Then I guess you will get an understanding. It's not that hard. It's just pretty abstract. So there is nothing tangible about what is a value of vector. It's just a projection. It's just a good projection that we train for the input vectors and what are this input vectors? Well there are some abstract representations of the tokens so there is not much intuition that I can give beyond what I already tried but actually surprisingly enough, the actual like a potential heads that after training. We often do some very understandable, very interpretable very into things. Maybe if we have time I will show you some examples later about this not today. Um, and there are I guess, two more things to talk about. So first, let me maybe show you An example, to be honest, I have only some pretty trivial examples here. Pretty trivial examples. I have this. Let's not go through the code, we have practical sessions for that, but I have this like one layer and one self-attention head and what it's supposed to do is its supposed to Output the matching key so to speak right for the input. So and If you look at the attention Matrix you you see that it does like for this attention had it does look to the in the in the correct spot. Basically that's it here. And here is another kind of abstract example What happened? Like it's an example to illustrate that the attention Matrix, The Matrix of attention weight does not have to choose a token. so, if you look at something like this, or some sample Matrix is like this one, the Quite often look like a permutation Matrix, right? They're quite often look like. Well for every input, we matched to some output to some other input in this case, and we encode their Mutual relationship right now. Between input number token, number I and token number J. Well, it doesn't have to be this way. There can be more complicated sets of attention weights like you can have for example Plantation Matrix. It looks like this where These tokens these queries. Look at like the older tokens. So in this example, all totals are split into groups. There are four groups they go one by one. Like three tokens group of three tokens group of three tokens, then one group of one token and again group of Traders. And they are supposed to look at each other uniformly. So that can also happen. Okay? You can have like this widely distributed attention where one token just attends to all of the tokens for example we'll see probably examples of this. Um, okay. And two more things that I need to talk about. so first Maybe one word on tokenization, it's not really our subject because we are talking about computer vision. And in images, it will be quite different. But I just wanted to mention because it's it's a nice connection to completely different areas of computer science to like coding Theory and Huffman coding and stuff. But like where do you get your dictionary from? It's a pretty interesting question. Because when I explain it to you intuitively, it makes sense to say that I just talking is a word and text but in reality, you can't have tokens to be able to work because there are too many words because, In a language. I mean you you can't just let my everything and have all of your words loose all the grammar that would lose a lot of information. So different grammatical forms have to be separate words that's one and two in reality there are typos and if you add diapers, so, again, you are not allowed to just drop everything that's not in the vocabulary because then Many texts would not make sense and you would lose again. A lot of information, but if you add all of the words with typos there, oh my God, the dictionary will be huge. You will have millions of words in the English language. so, We need something smaller. We need a smaller vocabulary. But and of course we could just start with characters. So you could have, I mean, you you could have a, you could view text as not, a sequence of words. But the sequence of characters, this is for most language is, this is a natural way to partition the text, right? Also. It's a sequence of characters. but now, this on the other hand is To find granularity, right? So yeah, character. There are few characters at most a couple hundred Even if you count old punctuation marks capital letters, etc, etc. Like 100 to 200 most at most And of course you can train. You can have A dictionary of 100. Vectors your embedding Matrix of several hundred vectors, but Now, it's too little because now it means that your sequences get too long. So again. Remember that, for example, now like a practical limit on the contact side or something like a million tokens and if there is a big difference if it's a million words or a million letters, right? And of course you would want to be closer to million words in the middle of letters. How do you go? In between. How do you choose which tokens to use which sequences of characters to assign characters? It turns out there is a pretty beautiful algorithm for that. It's called BP by parenting and it's commonly used throughout machine learning and interestingly it has nothing to do with learning. It's it's all just Huffman coding from like Shannon's information Theory. So let's how does it work? Well suppose you have some kind of data set where you have this words, I specifically chose words that are that have many similar letters of substrings and here are the letters that appear in this world. So let's assume that these are there, the frequencies of the word. So, these are the frequencies of the letters. Now. Okay, suppose that I want to as a can add one more token. What do I do? Well, Aid in one more talking means that if I start with characters, I can now take a pair of characters, so they can call this pair a single newtek. So, which pair do I choose? Well, let me list all of the pairs that actually appear. Let's just choose the one that appears the most. in this case, obviously the at appears everywhere. Almost everywhere. So it's very, very common has a high frequency. So let's call it and you Talking a new symbol. Let's go capital, Z whatever. And now my words look like this, right? So I replaced every at by this Z, And yeah of course the I cannot delete a and t from the vocabulary because like T can occur without a for example. Right. But still I have reduced the length of my words, I have added one, new token to the dictionary and I have done it in the in the optimal way. Basic script. And then you just repeat this. So now I, I have this new vocabulary of tokens. They have this new account. I needed to update the counts of a and t. Now, there's different. So I have this new set of pairs. Also, I don't need to update the whole thing, but I need to update the pairs where there was an A, or a t. and, And that's how I work, right? And then we can choose another pair of tokens and replace those by Capital One and so forth. So very simple, very straightforward. And the beauty, the beautiful part is that you can stop it. At any time. You can. Yeah, yeah, absolutely. It's it's, it's from that that part of computer science, I agree, and you can stop at any time. you can say, Okay, so let's say I have a capacity for a vocabulary of size 100,000 Well. So, that's way too much to have just characters and wait a little, to have complete words. So I just run this until I reach. I add tokens one by one so I can just reach exactly 100,000 and stop. And if you do it, you will see that. For example, first it will find like common frequent parts of words like Ed because it's at the end of everywhere and past tense or should I O N. Because it's a end of many nonsense, it's all so forth. And then of course, common words will be single tokens on common words will be moved multiple times and that's okay. So let's how to organization works. And one more very interesting remarks this will be the last that I have time to say today. One more very interesting remark about Transformers. Is that? Because they are so cool. Because they have this wonderful ability to go from any token to any token in one step. This is their biggest strength. But that comes with the final drawback with the finding defect Transformers loose word order. So in the current Network there is a very meaningful sense in which there are Hsu tokens and tokens that are far away because between a Json tokens you go in one step. If they are far away you go in many steps very natural. You don't need to remind the current Network about the word order. Transformers. Well, it's just a matrix, right? If you look at this Matrix of attention weights, it doesn't like just a generic Matrix, does not care. If these rules are in chess, or this rows are far apart. There is nothing that changes because of this, so, Transformers don't care about word order. And that's a bad thing. We don't want to keep the order, right? So what we actually do In practice, is we add to the embeddings of the tokens. We add special vectors called positional encodings that whose only job is to encode where exactly this token is in the sequence. And it's kind of a topic in itself, which I don't want to go into. Let me just briefly hinted the main idea. The main idea is this. Like you could have been embedding that just has like one hot representation that here is position. Number one, number two, number three, number four, but what you actually want is you want this position, according to have some kind of arithmetic on them. So you want your positional according to like if you have a vector represents position, one okay, so let me maybe briefly write it here if you have a vector that represents position 1. E 1 position 2 e 2, and so on. You want? them to capture this, like, Differences the distances between tokens. So you want like EI minus EJ as a vector to be somehow similar to e. I plus came, minus E J plus k So we want like if the tokens are three, if two positions are three tokens apart, you want the difference between their according to position, according to be the same across the whole sequence. Right. And in the original Transformer, they did it with this kind of approach. They did it with these. Ah, know basically positional what's the English word positional counting system? I forget like there are binary numbers, there are decimal numbers, what's the general term? So let's look at how binary numbers operate. If you look at the binary numbers, you see that? These are just binary numbers from 0 to 15 Road in sequence, right? So like one zero one, two, three blah, blah, 15 16. And if you look at what happens with the actual digits, you see that the last digit just oscillates right there are 101. The next Stitch also relates with twice, the period, the 0011001, and so on. Now we have four zeros and four ones for zeros for once 808 ones and so on, that's that's how binaries for and you can do it. You can do like a soft version of this. You can have like sine waves in different positions of the accordion and you can start with Sine waves with the oscillator, a lot with high frequency and then just reduce the frequency. And this will be like this positional system for counting that will give you the necessary properties. So this was the original approach to positional Coatings and the current approach. I think the one they mostly used today is called rope Rotary. Positional encodings. And rotary means that something is rotating. There is some kind of circular motion. And basically in raw put you do is this your you take your vector. Okay, so let's say take a vector X and in the state of considering its components one by one. You can see there them in. two ways to so you you break X into PCS of two numbers like two-dimensional vectors. Okay so this will be x 1 x 2. This will be X11 X12, this will be x 2, 1, x 2 2, and so on. And every two-dimensional part. You wrote, you can now rotate by various angles so you cannot rotate a single number, doesn't make sense. But a vector of two numbers. That's a vector on a plane. You can rotate it. so, what the rotary encoding do what this embedding section do is they take this kind of small packs of On a plane. And they multiply it by rotation matrices like this. I always forget where the minus sign is, maybe it's over here. And the positions are encoded as a coefficients to this rotation's. So sorry, let me write it again. I should have done this cosine. Okay, Theta. Sine Kate Theta? Minus sine K Theta? Cosine cave, right? So there is like this basic angle Theta and you rotate by multiple of theta. Which gives you this perfect arithmetic by default because if you take a vector and you rotate by K Theta and then you rotated by another elevator, then it's the same as rotating it by K plus sulfate, right? Just obvious So this also gives you this nice arithmetic and this kind of positional encodings have Better Properties. It seems. So, I have illustrations for you here as well. This is the sinusoidal, positional, encoding condition. This is the picture that I cannot draw on the board but this is the exactly how like this dot product between the two vectors here, depends only on the distance between them on the offset. I minus J. And that is the property that we want. And rotary positional coins. Well, here is an illustration for how they work. And this is the same kind of Matrix. again, showing that you have this diagonal structure, which means that along each diagonal distance between positions is the same and, You have the same dot product between the positional credits and I oh yeah. And I also have this illustration for why the square root of this necessary but it's just you know, practical representation of the fact that yeah if you don't scale, you get closer and closer to one hot representation, you lose the entropy after the softmax Um, all right. so, Let me stop here. We've discussed attention, and self-attention and the Transformer and I'm happy that I got to the end of the Transformer architecture. Any questions? okay, then then, thank you very much. I will try to. I will try to produce a unified video of this lecture. I'm I'm pretty sure it was not corrupted. Completely at some point, just not be a studio, quit unexpectedly, but I am sure it's not corrupted completely. I'm not sure if it will be able to actually join them together, sometimes it doesn't work. But in any case I will make it available somehow so, thanks a lot and see you. well, see you on Friday, but when next lecture will be, we have it decided, Well, talking about, Okay, so you're on Friday and Friday. I will listen to your presentations. Bye bye.
