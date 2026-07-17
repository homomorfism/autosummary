# Transcript — whisper_cpp

- **Provider:** whisper_cpp
- **Language:** en
- **Audio duration:** 1:40:15
- **Segments:** 996
- **model:** ggml-large-v3-turbo.bin
- **vad:** True
- **beam_size:** 5
- **entropy_thold:** 2.8
- **latency_sec:** 811.95

## Segments

**[00:11 – 00:29]** Okay. Hello everyone and welcome back. I'm happy to continue our discussions about deep learning. And specifically on this last week, we finally turned from something general.

**[00:29 – 00:53]** I mean, it usually happens every year that we start teaching a course called computer vision, but actually it turns out that you always need to start with something like deep learning basics and the actual computer vision gets bumped to the end of the class.

**[00:53 – 01:12]** But anyway, we are here and over the last two weeks, we have discussed, we have built up actually a wide array of architectures, a set of tools to solve various problems.

**[01:12 – 01:16]** And finally, we begin to apply them specifically to pictures.

**[01:16 – 01:25]** Well, we already talked about pictures in the context of CNNs, but we haven't yet talked about pictures in the context of Transformers.

**[01:26 – 01:39]** If I understand correctly, Alex already explained to you the VIT, the Vision Transformer, in practice sessions, so I won't be spending too much time on it.

**[01:39 – 01:56]** And our main plan for today, our main content will be a specific general but specific problem in computer vision, specifically object detection.

**[01:56 – 02:19]** And object detection is one of the most interesting problems in computer vision, and object detection is actually one of the hardest, in a way, because it's quite unusual.

**[02:19 – 02:29]** It has an unusual structure of the outputs compared to, say, segmentation, which we won't discuss in lectures, but maybe Alex will in practice.

**[02:29 – 02:43]** And there's a lot to talk about, and also transformers actually come in very interestingly and very differently in object detection.

**[02:43 – 03:00]** Actually, as we discussed, I think, usually the transformer just goes in, replaces some part of the architecture, and serves as a better feature extractor, and that's it.

**[03:00 – 03:07]** And there is nothing conceptually changing in the architecture quite often.

**[03:07 – 03:18]** For example, in segmentation, if you discuss it with Alex, he will tell you about the UNET architecture, which is from 2015 or something.

**[03:18 – 03:29]** But modern segmentation still uses UNET, only instead of convolutional layers inside, it uses some kind of self-attention based layers.

**[03:29 – 03:43]** There's a lot of new stuff happening, but basically the UNET did not get obsolete because the transformer appeared.

**[03:43 – 03:48]** In object detection, it's a little bit different, and we'll see how it works.

**[03:48 – 03:58]** So anyway, a few words, first on transformers for pictures, vision transformers.

**[03:58 – 04:02]** Let me not spend time at all on Visual Bird.

**[04:02 – 04:09]** Visual Bird was one of the first more or less successful approaches to handling pictures with transformers.

**[04:09 – 04:15]** And let me just tell you the setting, the problem setting for Visual Bird.

**[04:15 – 04:22]** It was for captioning mostly, and it worked like this.

**[04:22 – 04:37]** You had your text and you had object queries, like you had tokens that represented specific objects found on the picture.

**[04:37 – 04:42]** So to use Visual Bird, you would have to solve object detection first.

**[04:42 – 04:49]** And then you would plug in these subsets of the image, these rectangles.

**[04:49 – 04:58]** We'll discuss it in object detection, these rectangles that correspond to specific objects on the input image.

**[04:58 – 05:15]** And then pass them through some simple embedding layer, get a vector of features, and then off you go with the transformer.

**[05:15 – 05:35]** And the point of this picture for us is that for the transformer, as you can see here, it really, I won't say it doesn't matter, but it really matters little whether the input came from text or from images or from whatever.

**[05:35 – 05:50]** As long as it's a sequence of vectors, the transformer is an architecture that is great at finding various internal correlations between these vectors, finding structure inside, everything like that.

**[05:50 – 06:04]** So it is no wonder that at some point people just straightforwardly applied transformers to images.

**[06:04 – 06:22]** And again, Alex talked to you about this architecture, I won't waste time on it, but the most interesting, the most striking feature of the vision transformer architecture of the VIT is just how simple it is.

**[06:22 – 06:36]** I mean, you don't need to do anything. There is absolutely no change in the transformer architecture because now the input is an image.

**[06:36 – 06:51]** And in fact, you might think that when you cut a picture into patches, these patches do not really correspond to a natural one-dimensional sequence.

**[06:51 – 07:02]** Well, I mean, you fix some sequence, but adjacent patches in this sequence will not be necessarily anywhere close on the image.

**[07:02 – 07:09]** For example, if you go rows first, then you put the first three patches, they are indeed neighbors.

**[07:09 – 07:17]** And then after the third one, you go back to the left part of the image, and these two patches are nowhere near.

**[07:17 – 07:25]** So it is tempting to say that, well, an image is not really a sequence.

**[07:25 – 07:28]** An image has a two-dimensional structure.

**[07:28 – 07:34]** We need something new, something interesting, at least some change in the positional encodings

**[07:34 – 07:41]** that we discussed last time, in order to fix that.

**[07:41 – 07:47]** We need some change in the positional encodings to tell the transformer

**[07:47 – 07:56]** that it is actually a 2D structure.

**[07:56 – 08:02]** Again, it will not care if it's an image or what, it's just a vector of features for the transformer,

**[08:02 – 08:07]** but at least the positions should be somehow marked.

**[08:07 – 08:09]** Well, it turns out, no.

**[08:09 – 08:13]** In the original VIT paper, there's an appendix where they show that,

**[08:13 – 08:20]** "Oh yeah, sure, we tried several ideas on how to do these positional recordings and none of them help.

**[08:20 – 08:23]** Basically, you just treat it as a sequence, it's fine.

**[08:23 – 08:29]** Just use standard positional recordings from text transformers."

**[08:29 – 08:38]** And VIT kind of revolutionized image processing,

**[08:38 – 08:45]** revolutionized everything, well, computer vision and everything else dealing with images,

**[08:45 – 08:48]** because, again, a transformer is just better.

**[08:48 – 08:54]** It extracts better features, more semantically rich.

**[08:54 – 08:58]** In many, many applications, you can just, as I said,

**[08:58 – 09:02]** take out your convolutional network, plug in the VIT,

**[09:02 – 09:09]** just reuse the same stuff that you have on top of this feature extractor,

**[09:09 – 09:11]** and it will be better.

**[09:11 – 09:19]** And there were hundreds of papers that do exactly this after 2020.

**[09:19 – 09:22]** And there is only one problem.

**[09:22 – 09:27]** There is only one problem that is hard to solve for transformers.

**[09:27 – 09:31]** It's the main problem, the main computational problem of transformers,

**[09:31 – 09:35]** which I mentioned when we discussed the architecture itself.

**[09:35 – 09:41]** The problem is the VIT and any transformer has quadratic complexity.

**[09:41 – 09:55]** We discussed that in the transformer there is this matrix of attention weights.

**[09:55 – 09:58]** It's a token by token matrix.

**[09:58 – 10:06]** It's a matrix of size L times L, where L is the input size.

**[10:06 – 10:09]** It's really hard to go around this.

**[10:09 – 10:20]** It means that the VIT has complexity quadratic in the number of patches.

**[10:20 – 10:27]** Every patch becomes a token at the input of the VIT.

**[10:27 – 10:53]** If you have height h and width w, and let's say you have k times k patch, then there will be that many patches vertically times that many patches horizontally, and this will be squared.

**[10:53 – 11:15]** So the size of the grid is squared. And this is a big problem, in some applications at least, because it means that you cannot really, people try it with other architectures, but you cannot really have the VIT go down to the level of individual pixels.

**[11:15 – 11:28]** If you have a million pixels as input, a million squared is too much, even for modern hardware or whatever. So you have to have patches and you have to have relatively big patches.

**[11:28 – 11:46]** And if you have relatively big patches, it means that you can't really figure out the small details of your image.

**[11:46 – 12:16]** So if you are doing, for example, object detection to the VIT, whatever that would mean, and you want to find a cat in this image, and if the cat is small, maybe it's far away and it's completely inside one page or even the part of one page, or maybe it's on the boundary between two patches and none of them really is dominated by this object.

**[12:16 – 12:29]** Then I guess it will be very hard, because every patch will get flattened to a single vector and stuff will get lost along this way.

**[12:29 – 12:39]** So there's really no correct size for the VIT.

**[12:39 – 12:47]** Just like we discussed with the attention mechanisms, it's either too big, in which case you're losing detail,

**[12:47 – 12:53]** or it's too small, in which case you just can't train it and can't run it because it's too heavy.

**[12:53 – 12:59]** So what people did, there were a lot of approaches.

**[12:59 – 13:08]** I want to discuss one of them, specifically the Swin Transformer.

**[13:08 – 13:12]** The Swin Transformer, because it's one of the most popular.

**[13:12 – 13:21]** Today, if you open up some computer vision application, probably you will see either VIT or Swin.

**[13:21 – 13:26]** Some version of Swin or VIT as your backbone.

**[13:26 – 13:32]** And the Swin Transformer, so the Swin stands for shifted windows.

**[13:32 – 13:35]** And here is the thing.

**[13:35 – 13:46]** So as I said, the complexity grows as the square of the number of patches.

**[13:46 – 13:57]** So a natural way to save from this would be to break down the image into parts and then cut up the parts into patches.

**[13:57 – 14:05]** So for example, this here, I would, let's say, do a 2x2 grid like this.

**[14:05 – 14:13]** And then I would just take this guy, which has only a 3x3 grid, and here I would have complexity like 9^2.

**[14:13 – 14:18]** And here I will have 6^2, 6^2, 9^2.

**[14:18 – 14:21]** And if you add it all up, it will be a couple hundred.

**[14:21 – 14:28]** But the original complexity was like 25^2, which is, of course, much more.

**[14:28 – 14:34]** So if you have square complexity and you cut up into smaller pieces, you save a lot.

**[14:34 – 14:40]** And basically the square becomes linear because now it's the square only in the size of this small part.

**[14:40 – 14:53]** So it's very natural to have this kind of hierarchical structure where, first, if you have a large image at the input,

**[14:53 – 14:58]** first you cut it up into small pieces, relatively small pieces, like a 4x4 grid.

**[14:58 – 15:03]** Then you process every part here with VIT.

**[15:03 – 15:12]** Then you combine them and again you process with another set of VIT layers.

**[15:12 – 15:18]** Then finally you combine those somehow, I won't go into details how exactly,

**[15:18 – 15:25]** and process now globally the whole image also with VIT layers.

**[15:25 – 15:31]** So in this case, on this picture, every VIT layer, every transformer layer,

**[15:31 – 15:38]** deals with 16 tokens at the input, only 4x4 grids.

**[15:38 – 15:48]** But in three steps, we go from 16x16 image to 4x4 image,

**[15:48 – 15:53]** which is then compressed into features or a single vector or whatever.

**[15:53 – 15:56]** So that's the basic idea.

**[15:56 – 16:00]** And why is it called shifted windows?

**[16:00 – 16:06]** It's called shifted windows because, well, there is this problem

**[16:06 – 16:09]** that we will discuss in object detection too.

**[16:09 – 16:20]** The problem that when you look inside these small parts of the input image,

**[16:20 – 16:25]** very often it would help you greatly.

**[16:25 – 16:32]** Very often you would be very happy to have a more global context

**[16:32 – 16:34]** of what's happening in the image.

**[16:34 – 16:37]** Like, I don't know, you see, I can't draw it,

**[16:37 – 16:44]** but you see a small part of some kind of surface,

**[16:44 – 16:49]** and on the surface there is some kind of vehicle, right?

**[16:49 – 16:52]** And it's small, that's the whole problem,

**[16:52 – 16:55]** so it's hard to distinguish exactly what this vehicle is.

**[16:55 – 16:58]** So if you know that the context is a highway,

**[16:58 – 17:02]** and it's like a road with cars, then it's a car.

**[17:02 – 17:08]** If you know that the context is, I don't know, a lagoon of a sea,

**[17:08 – 17:10]** then it's a boat.

**[17:10 – 17:12]** Two very different classes.

**[17:12 – 17:16]** You can't really distinguish without global context.

**[17:16 – 17:18]** And this actually happens all the time.

**[17:18 – 17:20]** It sounds like a contrived example,

**[17:20 – 17:24]** but actually global context is necessary quite often.

**[17:24 – 17:28]** So you would like these guys down here

**[17:28 – 17:33]** to have a way to get information about what's happening in the rest of the image.

**[17:33 – 17:36]** And ShiftedWindows does it this way.

**[17:36 – 17:38]** Very interesting, very cool trick, I think.

**[17:38 – 17:46]** The trick is between self-attention layers, you shift the windows.

**[17:46 – 17:54]** So you would have on one layer,

**[17:54 – 18:00]** I want to draw it a little bit larger than on the example,

**[18:00 – 18:05]** because the picture from the paper is a little bit misleading.

**[18:05 – 18:11]** So you have a grid like this.

**[18:11 – 18:18]** And then on the next layer, you will have a grid like this.

**[18:18 – 18:25]** So it will shift like half of the size of the patch,

**[18:25 – 18:32]** and it will still be the same kind of transformer.

**[18:32 – 18:36]** It will still have the same size of input,

**[18:36 – 18:44]** but now it will shift to different subsets of features,

**[18:44 – 18:46]** so like different parts of the image.

**[18:46 – 18:51]** And notice that if I do it several times after every layer like they say,

**[18:51 – 18:56]** then this will expand the receptive field of my patches.

**[18:56 – 19:05]** So if I was sitting over here and I saw this part of the image,

**[19:05 – 19:09]** then after I go out here and then come back again,

**[19:09 – 19:17]** now the same transformer but in two layers up will already be looking at this part of the image,

**[19:17 – 19:21]** because it has collected actually even more,

**[19:21 – 19:24]** because this guy will be looking at here,

**[19:24 – 19:31]** so we will be looking at this part of the image,

**[19:31 – 19:43]** because the purple grid has been looking on this part,

**[19:43 – 19:51]** this transformer layer has been looking at the orange square,

**[19:51 – 19:59]** and when you go back you collect all of these neighboring adjacent purple squares.

**[19:59 – 20:10]** So this is how it works,

**[20:10 – 20:26]** and there's a lot of unclean and easy to mis-implement stuff around the edges,

**[20:26 – 20:28]** and this is what this picture shows.

**[20:28 – 20:33]** Basically, if you shift your grid, the edges will not fit anymore.

**[20:33 – 20:44]** These small parts near the edges of the image will not be full squares anymore.

**[20:44 – 20:57]** So what they actually do, they roll up the image in the torus, and they say, okay, so now this guy over here goes together with this guy.

**[20:57 – 21:08]** And this guy over here, the rectangle goes together with this rectangle, and the small squares at the corners also all go together as a single end.

**[21:08 – 21:16]** So this doesn't really matter all that much because it's only about the edges, but still, it's a lot of hassle.

**[21:16 – 21:32]** Once I saw an implementation, I don't think I have it here, but I saw an implementation of a 3D SWIN transformer where you do the same stuff, but with cubes instead of squares.

**[21:32 – 21:43]** And it was the most convoluted piece of code I've ever seen. There were lots and lots of hard-coded shifts and constants, and it was very difficult to understand.

**[21:43 – 22:02]** But anyway, the SWIN transformer, I won't discuss the exact architecture, but the SWIN transformer and the VIT both can serve as good backbones.

**[22:02 – 22:12]** So what is a backbone? It's a tool, part of the network, the largest part of the network that does feature extraction.

**[22:12 – 22:22]** And what would it do feature extraction for? Well, by default, the VIT is trained on something like classification.

**[22:22 – 22:41]** You do your feature extraction, you see where you collect the features into a single vector at the end,

**[22:41 – 22:49]** and you do your stuff about the reasoning, about the image as a whole, about it globally.

**[22:49 – 22:55]** But what we are discussing today, and our main content for today...

**[22:55 – 22:59]** Okay, it's been 20 minutes. Good. I think we are good on time.

**[22:59 – 23:06]** And what we are discussing today is a different kind of application,

**[23:06 – 23:13]** and a different kind of problem that will require us to look inside the image

**[23:13 – 23:20]** and to actually map our answers to specific pixels, which is always more difficult.

**[23:20 – 23:27]** So, I'll skip the perceiver. I don't have time for that.

**[23:27 – 23:34]** So, our main target, our main topic for today is object detection.

**[23:34 – 23:38]** Now, what is object detection? What's the problem?

**[23:38 – 23:44]** Well, okay, I don't have a slide on that, so let me just go to the board.

**[23:44 – 23:51]** And at first, let me discuss the problem setting because there's a lot to discuss.

**[23:51 – 23:58]** My first point was transformers for feature extraction from images.

**[23:58 – 24:05]** And our second point is what is object detection?

**[24:05 – 24:10]** Well, what is object detection informally?

**[24:10 – 24:15]** I hope you all kind of have an idea.

**[24:15 – 24:23]** So there is a big image like this and there is a cat inside, right?

**[24:23 – 24:28]** And maybe there's not only a cat inside, maybe there is something else.

**[24:28 – 24:31]** Maybe it's a big thing with a lot of objects.

**[24:31 – 24:37]** So the object detection problem goes like this.

**[24:37 – 24:41]** Given this image and given, let's say, the cat class.

**[24:41 – 24:48]** I also should specify what exactly I need to find.

**[24:48 – 24:54]** Find the cat and not only say that there is a cat.

**[24:54 – 25:01]** Give me the confidence, the probability that there is a cat, like the usual classification.

**[25:01 – 25:10]** But also to draw a rectangle around the cat to specify exactly where,

**[25:10 – 25:15]** and in terms of these rectangular positions, not down to individual pixels, that would be segmentation,

**[25:15 – 25:21]** but down to this rectangle, specify where exactly you found this cat.

**[25:21 – 25:33]** So this rectangle is called the bounding box, usually abbreviated to B box in documentation and papers.

**[25:33 – 25:44]** And then you can have many different classes, maybe in addition to a cat, on this image there is a dog somewhere.

**[25:44 – 25:52]** Let me draw a dog, I'm not sure, but at least let me make some different ears for the dog.

**[25:52 – 25:57]** Okay, so that's kind of a dog.

**[25:57 – 26:01]** And there is a dog, and I also want to recognize the dog,

**[26:01 – 26:08]** and I also want to draw a rectangle around the dog and also specify its bounding box.

**[26:08 – 26:14]** And the bounding boxes can overlap, of course, images can be anywhere,

**[26:14 – 26:18]** the objects themselves can overlap with each other,

**[26:18 – 26:25]** or they can just overlap in the empty parts of the rectangles, whatever, anything goes.

**[26:25 – 26:46]** The point is, for every object that I'm looking for, I need to output the class label and this bounding box.

**[26:46 – 26:53]** So how do you formalize a bounding box? It's a rectangle, you need to specify its coordinates.

**[26:53 – 27:02]** So usually people do it like this, they have X and Y for the bottom left corner or any corner that's...

**[27:02 – 27:06]** Interesting for you. And then the width and the height of directing, right?

**[27:06 – 27:11]** This rectangle is defined by four numbers.

**[27:11 – 27:16]** And so here is the interesting part now.

**[27:16 – 27:27]** I hope the idea of the problem is clear. I hope it's clear what we are trying to do here.

**[27:27 – 27:33]** But it's becoming less and less clear how exactly to do it, right?

**[27:33 – 27:40]** How would I define a neural network solving object detection?

**[27:40 – 27:44]** Let's not speak about architectures now, whatever is the network.

**[27:44 – 27:49]** But what is its input and what is its output?

**[27:49 – 27:57]** As input, obviously, I take the picture, I put it into my neural network.

**[27:57 – 28:00]** And now what is the output?

**[28:00 – 28:05]** Well, a picture can have multiple objects, right?

**[28:05 – 28:10]** If I assume that there is only one object, it's called object localization,

**[28:10 – 28:12]** and it's a much easier problem.

**[28:12 – 28:18]** So I need to have a way to output multiple objects, right?

**[28:18 – 28:25]** Like object one, two, three, and maybe more, maybe a lot more.

**[28:25 – 28:28]** Who knows, right?

**[28:28 – 28:35]** Then for every object, I need to have its class.

**[28:35 – 28:41]** So the class label as usual for classification in the form of a probability distribution.

**[28:41 – 28:48]** So this will be like the distribution on classes as always in classification.

**[28:48 – 28:52]** And then I need to specify the bounding books.

**[28:52 – 29:07]** So four numbers: x, y, w, h, and so on for every object.

**[29:07 – 29:11]** And here is the first tricky part.

**[29:11 – 29:18]** I cannot have a neural network with variable number of outputs.

**[29:18 – 29:21]** It kind of doesn't make any sense.

**[29:21 – 29:31]** So I need to fix the number of outputs from a neural network.

**[29:31 – 29:39]** I know how many outputs exactly I have per object.

**[29:39 – 29:46]** So per object I have the number of classes for their probabilities,

**[29:46 – 29:50]** and then four numbers for the bounding box.

**[29:50 – 29:56]** So if I know how many objects I have, I know how many outputs I want.

**[29:56 – 29:59]** But I don't know how many objects I have, right?

**[29:59 – 30:03]** On the picture there might be one cat, two cats, three cats,

**[30:03 – 30:05]** four cats and two dogs, whatever.

**[30:05 – 30:06]** I don't know.

**[30:06 – 30:10]** There may be hundreds of objects and I just don't know it in advance.

**[30:10 – 30:16]** So what's the answer to that?

**[30:16 – 30:23]** How do I solve the problem that I can't really have an open list at the output of a network?

**[30:23 – 30:27]** And I can't because at the output of a network there should be neurons with weights

**[30:27 – 30:35]** and I cannot have a variable number of neurons because I need to have this number of weights

**[30:35 – 30:38]** and I need to train them, right?

**[30:38 – 30:43]** So for this question the output, the answer is pretty trivial.

**[30:43 – 30:53]** For this question the answer is well, okay, let's fix some maximal number of objects that we want to recognize

**[30:53 – 30:57]** and let's just have this many outputs.

**[30:57 – 31:02]** This begs another question, right?

**[31:02 – 31:04]** This begs another question.

**[31:04 – 31:09]** Now what happens if there are fewer objects?

**[31:09 – 31:15]** What happens if I am recognizing 10 different objects but the picture only has a cat and a dog

**[31:15 – 31:20]** so like two objects and the rest is irrelevant.

**[31:20 – 31:21]** They are not my classes.

**[31:21 – 31:31]** Well, in this case, I need to have a way to specify that some outputs don't count, right?

**[31:31 – 31:39]** I need a way to specify that, okay, so object number one is real, object number two is real.

**[31:39 – 31:43]** The rest, they are not real.

**[31:43 – 31:46]** And usually it's done exactly like I said.

**[31:46 – 31:54]** So usually it's done by inserting, by adding another output, which I would call the confidence.

**[31:54 – 32:06]** So for every output, you would have something like, okay, here is how sure I am that there is an object here.

**[32:06 – 32:10]** And it's usually a probability, right? So from zero to one.

**[32:10 – 32:14]** Here is how sure I am that there is an object here.

**[32:14 – 32:23]** And if it is there, then here is its class label and here is its bounding box.

**[32:23 – 32:42]** So if I have only two objects, then sure, I would like the confidences for these objects to go to one

**[32:42 – 32:55]** and the confidences for all other objects to go to zero.

**[32:55 – 33:07]** So, okay, but this is also only the beginning.

**[33:07 – 33:12]** We still have a lot of unclear things here.

**[33:12 – 33:20]** We still have a lot of interesting questions left.

**[33:20 – 33:25]** So we defined what should be the output of the neural network.

**[33:25 – 33:30]** But this is only the first step and it's an intermediate step.

**[33:30 – 33:36]** What I really want to define, what we really need to define for this to work is a loss function.

**[33:36 – 33:46]** So what would be a loss function for this kind of output?

**[33:46 – 33:49]** What would be the loss?

**[33:49 – 34:03]** I have this picture and I have the ground truth, which are these two objects.

**[34:03 – 34:10]** So this is like y1, y2. For y1 I know it's a cat, I know where it is, I know it's bounding box.

**[34:10 – 34:14]** For y2 I know it's a dog, I know it's bounding box.

**[34:14 – 34:21]** How do I compare this to the output of the neural network?

**[34:21 – 34:30]** What should I optimize? Well, kind of, again, non-trivial.

**[34:30 – 34:35]** Why non-trivial? Because I can't just say, well, object number one should be this cat,

**[34:35 – 34:39]** object number two should be this box, this dog, and that's it.

**[34:39 – 34:45]** Because the neural network doesn't and shouldn't have any idea

**[34:45 – 34:49]** of some kind of ordering of the objects, right?

**[34:49 – 34:52]** It doesn't make any sense. They don't come ordered.

**[34:52 – 34:55]** I just want to recognize the objects on the image.

**[34:55 – 34:59]** I don't know if the cat is number one and the dog is number two.

**[34:59 – 35:05]** And also, if I have confidences like here, and if I have a big list of possible objects,

**[35:05 – 35:12]** then I don't want to require the neural network to, in addition, sort them by confidence or something.

**[35:12 – 35:15]** That would be difficult and completely unnecessary.

**[35:15 – 35:22]** I just want this cat to be somewhere inside, and this dog to be somewhere inside,

**[35:22 – 35:29]** and the rest, the other outputs to have low confidence, right?

**[35:29 – 35:39]** So what we actually are looking at is we need to find a matching between the ground truth,

**[35:39 – 35:48]** the ground truth, the answer, and the predictions of the neural network.

**[35:48 – 35:53]** So it's called an assignment problem, right?

**[35:53 – 35:57]** We need to assign elements of these two sets to each other.

**[35:57 – 36:02]** I can pad this with no object to k,

**[36:02 – 36:10]** and then I need to assign elements of these sets to each other to minimize some kind of cost.

**[36:14 – 36:20]** Okay. Here, I suppose you will discuss it in practical sessions,

**[36:20 – 36:24]** there will be something like the Hungarian algorithm

**[36:24 – 36:30]** that actually produces this bipartite matching,

**[36:30 – 36:34]** one-to-one matching between predictions and ground truth

**[36:34 – 36:41]** in a way that actually assigns the ground truth box to the best predictor.

**[36:41 – 36:46]** But that's also not enough, right?

**[36:46 – 36:54]** So what is the loss function then?

**[36:54 – 37:06]** Well, the loss function, and here I won't go into full formal details

**[37:06 – 37:08]** because they can differ.

**[37:08 – 37:14]** There can be different ideas and different weights and whatever.

**[37:14 – 37:18]** But the loss is composed of two things, right?

**[37:18 – 37:21]** The classification loss of three things, sorry.

**[37:21 – 37:27]** The confidence loss from, like, if there is an object, the confidence should go to one.

**[37:27 – 37:32]** If there is not an object, the confidence should go to zero.

**[37:32 – 37:34]** That's one part.

**[37:34 – 37:36]** And that's pretty easy, right?

**[37:36 – 37:42]** It's like just the log confidence minus log confidence or something.

**[37:42 – 37:45]** Then there is the classification loss.

**[37:45 – 37:50]** So if there is an object, let me put it this way.

**[37:50 – 37:55]** If there is no object, then we don't care what the class label says.

**[37:55 – 38:00]** Because if there is no object, then it's just random stuff.

**[38:00 – 38:03]** If there is an object, then we care.

**[38:03 – 38:13]** And then it's probably just a cross-entropy between these two probability distributions, right?

**[38:13 – 38:18]** And then there should be the bounding box loss.

**[38:18 – 38:24]** So these numbers should represent the correct rectangle.

**[38:24 – 38:28]** And of course, they won't in practice.

**[38:28 – 38:34]** And again, it only matters if you have an object.

**[38:34 – 38:41]** But if you do have an object, what is the loss for the bounding box?

**[38:41 – 38:54]** You can do it with some straightforward loss like x minus x predicted squared plus so on plus h minus h predicted squared.

**[38:54 – 39:01]** Or not squared or maybe the same, but like absolute values for an L1 loss or whatever.

**[39:01 – 39:21]** But problems with this coordinate based losses, one common problem is that you will get very different contributions into this loss for large objects and for small objects.

**[39:21 – 39:25]** So, okay, in our example, I have two large objects.

**[39:25 – 39:42]** But anyway, if I have like this ground truth box for the cat and my predicted box is like this, well, it's pretty good, right?

**[39:42 – 39:54]** It's pretty good, but we have quite a lot of distance here, so I will need to move the bottom left corner down here and then up here.

**[39:54 – 40:00]** And the width and height, I don't know how to draw it, but they also need to be updated, to be adjusted.

**[40:00 – 40:09]** But if I have a very small object like this, and as we will see, small objects are the most interesting case for object detection.

**[40:09 – 40:24]** This is what's difficult. Then, for the same kind of loss, my bounding box will be completely different.

**[40:24 – 40:29]** So here, they overlap a lot when they are large.

**[40:29 – 40:37]** And here, for the same loss, for the same differences in width, height, x and y, they will not overlap at all.

**[40:37 – 40:45]** So, not really intuitive, right? I don't really want this to make identical contributions.

**[40:45 – 40:51]** I want this to be a bad thing and this to be an almost perfect thing, right?

**[40:51 – 40:56]** So, how do I fix that?

**[40:56 – 41:01]** Well, the answer is, I don't want to get my...

**[41:01 – 41:09]** I mean, some approaches to object detection, including some of the ones that we will discuss today, say,

**[41:09 – 41:13]** "Well, alright, what can we do? Let's still use something like that."

**[41:13 – 41:18]** Like the original YOLO uses a loss function like that.

**[41:18 – 41:28]** But these days, usually, people do some kind of a loss based on what is called the intersection over union metric.

**[41:28 – 41:40]** So, the IOU of two areas on a plane, in this case two boxes, is precisely what it says:

**[41:40 – 41:49]** intersection over union, the area of their intersection divided by the area of their union.

**[41:49 – 41:56]** So, in this case, I take this guy, and I divide it by this guy.

**[41:56 – 42:04]** And I get something like, I don't know, 0.6, 0.7, I guess, in this case, which is a pretty good idea.

**[42:04 – 42:08]** In this case, I get exactly zero.

**[42:08 – 42:32]** So this is the default metric for measuring goodness of match between bounding boxes and predicted boxes.

**[42:32 – 42:48]** And it only has one more problem. I won't go into more detail formally, but it has only one problem in that now if the boxes don't overlap, the IOU, as I said, is exactly zero.

**[42:48 – 43:10]** And notice that the IOU is actually differentiable. It's not piecewise constant. You can pass gradients through it. If you slightly tweak, if you push this bounding box a little bit to some size, you will get a small change in the IOU.

**[43:10 – 43:28]** So the gradients make sense. But the gradients stop making sense when the numerator becomes zero. And this is a bad thing again, because when I look at these two bounding boxes, I do want to be able to say that I want to move it here.

**[43:28 – 43:41]** But from the point of view of the IOU, if I move it in the right direction a little bit, it's no difference than if I moved it in the other direction a little bit. It will still be zero and the gradients don't help.

**[43:41 – 43:53]** So, in effect, there are additional metrics, something like the generalized IOU, which I'm not even sure I remember correctly the formula, so I won't try to reproduce it.

**[43:53 – 44:11]** But basically, they make use of this bounding box, and they involve something like what is the percentage of this common bounding box,

**[44:11 – 44:24]** not covered by these two boxes, something like this. So now if you move in the right direction, then this joint bounding box shrinks and the percentage becomes larger.

**[44:24 – 44:34]** So this would be a good thing. And I think that's it for the loss function.

**[44:34 – 44:45]** So we have discussed the main components, the main usual components of the loss function, but there is one more little thing.

**[44:45 – 44:54]** There is a more little thing that happens when you apply the neural network.

**[44:54 – 45:02]** So now I guess I talked through everything that happens when you train the neural network, but what happens when you apply it?

**[45:02 – 45:13]** And notice that so far I haven't said a single word about how it actually works, what's inside the neural network, what's going on.

**[45:13 – 45:21]** I'm just talking about the loss function, and this is pretty common in difficult problems and non-standard problems.

**[45:21 – 45:27]** The architectures will come and go, but the loss functions are like a separate object.

**[45:27 – 45:32]** They don't care what the architecture is as long as you can pass the gradients through.

**[45:32 – 45:37]** And they deserve a separate discussion and they evolve separately.

**[45:37 – 45:41]** There is a line of work that tries to optimize the losses.

**[45:41 – 45:46]** And a separate line of work, maybe in the same papers, but it's completely detached.

**[45:46 – 45:49]** You can optimize them independently.

**[45:49 – 45:53]** The architecture and the losses.

**[45:53 – 46:04]** Okay, so I finished talking about the losses, but what about the application?

**[46:04 – 46:07]** What about the inference of this neural network?

**[46:07 – 46:09]** What's the problem there?

**[46:09 – 46:13]** There are two problems.

**[46:13 – 46:22]** And again, I won't go into too many details, but a little bit I have to mention.

**[46:22 – 46:27]** So here is a picture and here is a cat on this picture.

**[46:27 – 46:30]** And the cat is very happy.

**[46:30 – 46:36]** And I want to recognize this cat, right?

**[46:36 – 46:45]** Actually, it concerns the loss function too. Sorry.

**[46:45 – 46:51]** But yeah, it concerns the training time too. Sorry.

**[46:51 – 46:54]** We did not quite finish with the training.

**[46:54 – 46:57]** Because here is the thing.

**[46:57 – 47:03]** Yes, I can get you the best possible assignment

**[47:03 – 47:07]** between the ground truth objects and the objects that I predict.

**[47:07 – 47:11]** But even after I get the best possible assignment,

**[47:11 – 47:16]** I still need to decide which parts, which predictions are actual objects

**[47:16 – 47:18]** and which predictions don't count.

**[47:18 – 47:27]** So suppose that in this case I get a bounding box like this, right?

**[47:27 – 47:33]** So this bounding box is kind of maybe about this cat.

**[47:33 – 47:36]** It looks like it's about this cat.

**[47:36 – 47:40]** So when I look at the bounding box like this, I want to say,

**[47:40 – 47:47]** well, almost right, but you need to shift your bounding box over here, right?

**[47:47 – 47:54]** And you need to put the class labels so that it's a cat.

**[47:54 – 48:00]** So in this case, for this gray bounding box, I want to say,

**[48:00 – 48:04]** well, I want to make you into the cat bounding box.

**[48:04 – 48:13]** And then if I have a bounding box like this, for example,

**[48:13 – 48:19]** it also kind of overlaps with the cat, right?

**[48:19 – 48:23]** But most probably it's about something else.

**[48:23 – 48:26]** And even without looking at the rest of the picture,

**[48:26 – 48:30]** even without looking at its class probabilities,

**[48:30 – 48:32]** probably it's not about the cat.

**[48:32 – 48:38]** And probably if there is no ground truth over here,

**[48:38 – 48:41]** if there are no other objects in here,

**[48:41 – 48:45]** then probably for the light blue box, I don't want...

**[48:45 – 48:49]** So for the gray box, I want it to become the cat box,

**[48:49 – 48:53]** and I want its confidence to go to one.

**[48:53 – 48:58]** For this box, well, it never had much in common with the cat.

**[48:58 – 49:02]** I don't want to bring it over here, it doesn't sound right.

**[49:02 – 49:04]** I just want its confidence to go to zero.

**[49:04 – 49:06]** It's just a spurious bounding box,

**[49:06 – 49:11]** and there will always be lots and lots of outputs

**[49:11 – 49:14]** where the confidence should go to zero.

**[49:14 – 49:18]** Because, again, remember that there are a lot of outputs,

**[49:18 – 49:21]** many boxes, like the maximum possible number of objects,

**[49:21 – 49:24]** and in reality, there will be two or three on a given picture,

**[49:24 – 49:29]** and most of the outputs should have confidence to go to zero.

**[49:29 – 49:34]** So here, too, I need to distinguish between these two cases.

**[49:34 – 49:40]** Either I want to count this box to become the cat,

**[49:40 – 49:43]** or I just want to say, okay, this is a bad, bad box,

**[49:43 – 49:46]** and let's just forget about it.

**[49:46 – 49:52]** Well, again, in practice, it's done with an IOU threshold.

**[49:52 – 50:02]** So you just pick a number, like one half or something,

**[50:02 – 50:06]** and if the overlap is larger than one half,

**[50:06 – 50:10]** then you count this output as the ground truth.

**[50:10 – 50:20]** And if the output is less, then you don't count.

**[50:20 – 50:24]** So this is easy, but still also need to mention.

**[50:24 – 50:29]** And finally, I guess Alex will talk more about this in practice.

**[50:29 – 50:34]** Finally, there is this effect that when you have an object,

**[50:34 – 50:37]** like a clear object that's easy to recognize,

**[50:37 – 50:40]** and you run this image through a neural network

**[50:40 – 50:47]** that has a possibility to distinguish dozens or hundreds of objects,

**[50:47 – 50:54]** most probably, not one, but a lot of them will stick to this cat.

**[50:54 – 50:59]** So you will have a bounding box about this cat like this,

**[50:59 – 51:04]** and you will have another bounding box about this cat like this,

**[51:04 – 51:08]** and you will have another bounding box about this cat like this,

**[51:08 – 51:12]** and there will be a dozen of those.

**[51:12 – 51:16]** Of course, you don't need to repeat the same object 12 times.

**[51:16 – 51:21]** I guess the standard way to cope with it

**[51:21 – 51:24]** is an algorithm called non-maximal suppression,

**[51:24 – 51:26]** and let me just leave it at that.

**[51:26 – 51:28]** It doesn't matter for training.

**[51:28 – 51:32]** For training, we just do the best matching, and that's it.

**[51:32 – 51:36]** For actual inference, you need to do this non-maximal suppression

**[51:36 – 51:41]** to pick the best possible bounding box,

**[51:41 – 51:44]** because now you don't know what the ground truth is,

**[51:44 – 51:48]** and you need to somehow combine all of these hypotheses into a single box.

**[51:48 – 51:55]** But overall, that's it for the problem setting.

**[51:55 – 52:01]** So notice that I haven't yet said anything about how to actually solve this problem.

**[52:01 – 52:07]** I haven't said anything about what's inside the neural network

**[52:07 – 52:12]** and how do we produce all of these wonderful outputs.

**[52:12 – 52:15]** Well, let's say a few words about it.

**[52:15 – 52:20]** So what kind of words? What can we say?

**[52:20 – 52:28]** Well, I won't, of course, go back in history before deep learning.

**[52:28 – 52:31]** We are doing deep learning after all.

**[52:31 – 52:38]** I will go 10 years back to 2014,

**[52:38 – 52:42]** when there was like this first approach,

**[52:42 – 52:47]** kind of after AlexNet revolutionized image processing,

**[52:47 – 52:51]** people tried to apply deep learning everywhere for images,

**[52:51 – 52:56]** and finally they got to object detection.

**[52:56 – 53:03]** And the first successful attempt was called RCNN,

**[53:03 – 53:06]** which stands for region-based CNN.

**[53:06 – 53:12]** And Ross Gershuk is one of the best known researchers

**[53:12 – 53:14]** in object detection.

**[53:14 – 53:19]** And here is how his original approach worked a long time ago.

**[53:19 – 53:25]** Well, first of all, it used an external algorithm

**[53:25 – 53:28]** called selective search, I won't go into details,

**[53:28 – 53:31]** to produce candidate bounding boxes.

**[53:31 – 53:36]** So you put your image through some algorithm,

**[53:36 – 53:40]** and it gives you candidate bounding boxes.

**[53:40 – 53:43]** But this algorithm doesn't know the classes.

**[53:43 – 53:45]** It doesn't care about the classes.

**[53:45 – 53:49]** It just finds distinctive objects on the photo.

**[53:49 – 53:50]** That's it.

**[53:50 – 53:53]** So if you want to recognize cows,

**[53:53 – 53:56]** you will still get this post over here

**[53:56 – 53:59]** and the clout and the ear of a cow and whatever.

**[53:59 – 54:02]** So you will get hundreds of candidates

**[54:02 – 54:04]** and only a few actual boxes.

**[54:04 – 54:05]** So what next?

**[54:05 – 54:11]** Then they take every one of these boxes

**[54:11 – 54:13]** and treat them separately

**[54:13 – 54:17]** and pass every one of these boxes through a neural network.

**[54:17 – 54:21]** In this case, a CNN trained on ImageNet.

**[54:21 – 54:23]** So this is the backbone.

**[54:23 – 54:28]** And this CNN will tell you what class of object it is.

**[54:28 – 54:32]** It sounds very straightforward.

**[54:32 – 54:38]** Of course, this doesn't answer the most interesting questions.

**[54:38 – 54:43]** So first, a technical remark.

**[54:43 – 54:49]** To actually put a bounding box through a CNN pre-trained on ImageNet,

**[54:49 – 54:50]** you need to make it square.

**[54:50 – 54:56]** The CNN pre-trained on ImageNet expects 256 by 256 square photo.

**[54:56 – 55:03]** So what they actually did was they took this box and actually warped it,

**[55:03 – 55:07]** just compressed it so that it would become square,

**[55:07 – 55:10]** just artificially geometrically compressed.

**[55:10 – 55:11]** And it actually worked.

**[55:11 – 55:18]** I mean, obviously for this post over here, it would make it very, very different, right?

**[55:18 – 55:23]** But still, it was the best solution at the time.

**[55:23 – 55:30]** And then also another problem was that the CNN, the backbone,

**[55:30 – 55:36]** will not tell you whether there is an object or not, right?

**[55:36 – 55:41]** A CNN trained on ImageNet presumes that there is an object and just classifies it.

**[55:41 – 55:47]** If you give it some bad bounding box, it's just a sky with some clouds.

**[55:47 – 55:53]** I don't know if ImageNet has the class cloud, maybe it does.

**[55:53 – 55:58]** If it does, then hopefully it will be recognized as a cloud.

**[55:58 – 56:03]** But if not, it will be just some distribution over classes.

**[56:03 – 56:09]** There is no confidence in the outputs of a classification network.

**[56:09 – 56:40]** So they actually also had to have a third step here, another step that takes the outputs of this CNN and modifies them and passes them through a completely different model, a model on top of that, that would actually further classify based on these probabilities, like whether it's a real object or not.

**[56:40 – 56:59]** It was very fragile. It still was the best approach at the time, which shows just how cool deep learning is, but it was, of course, very fragile and it was hopelessly slow, hopelessly slow.

**[56:59 – 57:22]** It was like a minute per image on a GPU. But all of the ideas are already in this original RCNN architecture. At least all of the ideas of this one approach to object detection that is called two-stage object detection.

**[57:22 – 57:54]** So I actually used to have very detailed lectures on object detection that would go through dozens of different architectures. I will not do that with you. We don't have time. And they became less relevant as time goes by. So we will jump to Transformers in a little bit. But I do want to discuss the RCNN family because in a way it's still relevant. And it's still relevant.

**[57:54 – 58:12]** It explains in these simple examples. It still explains the main ideas. So what are the main ideas in this basic RCNN? The main idea is use your backbone to extract features from a specific part of the input.

**[58:20 – 58:47]** And where do these candidate bounding boxes come from? Well, in this case, they come from an external algorithm. Later we will see they will come from the network itself. But still, you first get a set of candidates.

**[58:47 – 58:57]** And then you process every candidate through a CNN, you extract the features, and then you see what's inside there and what you want to do.

**[58:57 – 59:16]** So this is the idea of two-stage object detection. First, produce a relatively small set of candidate bounding boxes, then process every bounding box in a way.

**[59:16 – 59:24]** But of course, processing every bounding box completely independently is, again, hopelessly slow.

**[59:24 – 59:37]** So this picture has the real numbers. To get good coverage of the actual objects, of the actual bounding boxes, we need to extract 2,000 region proposals.

**[59:37 – 59:44]** So where do these 47 seconds come from? They come from running the same network.

**[59:44 – 59:56]** The network is very fast, actually, but you have to run it like 2,000 times and then run a model on top of its results to actually get something, right?

**[59:57 – 59:59]** So this is, of course, hopelessly slow.

**[59:59 – 1:00:14]** So the next step in what was called faster CNN, the next step was to, and this is an important idea, was to process the whole image only once.

**[1:00:16 – 1:00:30]** And then extract features from the feature tensor, take parts of the feature tensor, rather than reprocess everything from pixels.

**[1:00:30 – 1:00:33]** Makes perfect sense, right?

**[1:00:33 – 1:00:41]** So you have this, I won't waste time on trying to redraw this on the board, let me just talk through the slide.

**[1:00:41 – 1:00:47]** So you have this long convolutional network or long transformer network or whatever.

**[1:00:48 – 1:00:53]** And, okay, no, transformers don't work like that, but you have this long convolutional network.

**[1:00:54 – 1:01:01]** And as we go through the convolutional network, as we discussed, you gradually lose the geometry.

**[1:01:01 – 1:01:05]** And if you want to keep some of the geometry, you stop it a bit earlier.

**[1:01:05 – 1:01:09]** We did this for attention mechanisms before.

**[1:01:10 – 1:01:13]** So the same idea here.

**[1:01:13 – 1:01:19]** You pass your big picture through the CNN only once.

**[1:01:21 – 1:01:25]** But you stop a little bit short of the goal.

**[1:01:25 – 1:01:28]** So you get this feature tensor that still has geometry.

**[1:01:28 – 1:01:33]** Then you take your candidate bounding boxes.

**[1:01:34 – 1:01:38]** And faster CNN, they are still produced by an external tool, by an external algorithm.

**[1:01:39 – 1:01:42]** These bounding boxes.

**[1:01:42 – 1:01:50]** And when you have some geometry on the feature tensor,

**[1:01:50 – 1:01:58]** it's not a problem to find out which features correspond to which pixels of the original image.

**[1:01:58 – 1:02:00]** You just have this correspondence.

**[1:02:00 – 1:02:03]** So when you have a bounding box, you can project it.

**[1:02:03 – 1:02:06]** It's called ROI projection, region of interest projection.

**[1:02:07 – 1:02:10]** ROI is a very common abbreviation in object detection.

**[1:02:10 – 1:02:12]** It stands for region of interest.

**[1:02:13 – 1:02:15]** You have this ROI projection.

**[1:02:16 – 1:02:17]** It's not a trainable thing.

**[1:02:17 – 1:02:20]** It's just which features look at these pixels.

**[1:02:21 – 1:02:29]** And now you have the same bounding box, only rougher, and inside the feature tensor.

**[1:02:30 – 1:02:37]** And then you take this bounding box and you put it through an object detection head.

**[1:02:37 – 1:02:47]** An object detection head that has basically a classifier for the classes and the bounding box regressor for the bounding box itself.

**[1:02:47 – 1:02:48]** So I didn't mention it before.

**[1:02:48 – 1:02:50]** Let me mention it here.

**[1:02:51 – 1:03:13]** Usually, even if you have candidates already in terms of pixels like here, you still want to have a bounding box regression at the output because maybe the network will want to shift this bounding box a little bit and it will be useful.

**[1:03:13 – 1:03:19]** So the network might decide, oh, okay, so this is about the cat, but I need to shift it a few pixels to the left.

**[1:03:20 – 1:03:25]** And yeah, that actually happens and you can train it because you have the ground truth, so it's a good thing.

**[1:03:25 – 1:03:27]** The bounding box regression is always here.

**[1:03:29 – 1:03:37]** One detail about this is that, okay, so now I run the big convolutional network only once.

**[1:03:37 – 1:03:44]** And for every bounding box, I actually run only this small head.

**[1:03:44 – 1:03:50]** I want to say classification head, no, small detection head with a classifier and a regressor.

**[1:03:50 – 1:03:54]** So this is already like orders of magnitude faster.

**[1:03:55 – 1:04:08]** One technical problem is that, again, I don't know, I need somehow to fix the size of the input for this guy here.

**[1:04:08 – 1:04:19]** So my bounding boxes will come in different sizes and they will map to parts of the feature tensor of different sizes too.

**[1:04:20 – 1:04:25]** And I need the input to this head, detection head, to be always the same.

**[1:04:26 – 1:04:27]** What do I do?

**[1:04:28 – 1:04:32]** Well, I insert what is called a region of interest pooling layer.

**[1:04:33 – 1:04:39]** And also a pretty straightforward idea, but pretty cool.

**[1:04:40 – 1:04:43]** Let me draw it over here.

**[1:04:44 – 1:04:46]** Straightforward but cool idea.

**[1:04:47 – 1:04:52]** I have, let's say, this is the feature tensor, right?

**[1:04:52 – 1:04:57]** And I have a bounding box in the feature tensor that goes, let's say, like this.

**[1:04:57 – 1:05:07]** So, it's a 3x5, 5x3 tensor.

**[1:05:09 – 1:05:12]** Don't care what the depth is, I will not cut the depth.

**[1:05:12 – 1:05:26]** But it's 3x5 and my detection head wants to have as input a 2x2 tensor, let's say.

**[1:05:27 – 1:05:28]** So, what do I do?

**[1:05:29 – 1:05:36]** I do pooling, but I do, like, pooling not with a fixed window size,

**[1:05:36 – 1:05:39]** but pooling with a fixed output size.

**[1:05:40 – 1:05:45]** So, in this case, I will see, I know that I expect my output to be 2x2,

**[1:05:45 – 1:05:59]** and I will just cut it up as evenly as possible to have 2x2 windows.

**[1:06:00 – 1:06:05]** So, of course, it will not be exact, because these are integer numbers,

**[1:06:05 – 1:06:07]** but as close as possible.

**[1:06:07 – 1:06:12]** And then I will pool the features in these four windows.

**[1:06:12 – 1:06:15]** So this is called region of interest pooling.

**[1:06:16 – 1:06:24]** That's, I guess, the one cool idea that I wanted to mention for faster CNN.

**[1:06:27 – 1:06:33]** And not just for faster CNN, it will be used everywhere, starting from faster CNN.

**[1:06:35 – 1:06:41]** So this was already orders of magnitude faster,

**[1:06:41 – 1:06:50]** and the remaining bottleneck, now the slowest part of this pipeline,

**[1:06:51 – 1:06:53]** was not in the network at all.

**[1:06:54 – 1:06:59]** Now the slowest part was actually this external algorithm that we didn't want to discuss

**[1:06:59 – 1:07:03]** that produced the candidate boxes.

**[1:07:07 – 1:07:19]** And therefore, in the next iteration, in the next idea that we need to understand,

**[1:07:19 – 1:07:24]** that underlies what is called faster CNN, very creative naming.

**[1:07:24 – 1:07:28]** We have this line from RCNN to faster CNN to faster RCNN.

**[1:07:30 – 1:07:38]** And faster RCNN, it still counts as two-stage detection,

**[1:07:38 – 1:07:41]** because we still will produce the proposals separately,

**[1:07:42 – 1:07:46]** and then we will score them and match them and everything.

**[1:07:47 – 1:07:56]** But now I will make the proposals by a separate part of the network,

**[1:07:56 – 1:08:00]** the region proposal network, that is inside the architecture.

**[1:08:01 – 1:08:03]** So, again, we don't have time.

**[1:08:04 – 1:08:06]** I won't discuss how this RPN actually works,

**[1:08:07 – 1:08:09]** the region proposal network, how it actually works.

**[1:08:09 – 1:08:13]** But the point is, it works on the same feature map,

**[1:08:14 – 1:08:20]** and it's a separate network that goes with a sliding window over this feature map.

**[1:08:21 – 1:08:23]** The feature map has already lost most of the geometry,

**[1:08:24 – 1:08:26]** so now you can afford to just go with a sliding window.

**[1:08:27 – 1:08:34]** And basically just finds which boxes make sense on the level of this feature map.

**[1:08:35 – 1:08:40]** And it outputs a few top boxes, maybe some hundreds of top boxes,

**[1:08:41 – 1:08:43]** and then the rest is the same.

**[1:08:43 – 1:08:46]** So still we do this region of interest pooling,

**[1:08:46 – 1:08:47]** still we go to the detection head,

**[1:08:48 – 1:08:50]** still we cut out the features, everything else is the same.

**[1:08:51 – 1:08:53]** But now the proposals come from inside the network.

**[1:08:53 – 1:09:00]** And faster R-CNN actually became the standard approach

**[1:09:00 – 1:09:02]** up until Transformers changed everything.

**[1:09:03 – 1:09:04]** It was not in 2017.

**[1:09:04 – 1:09:06]** It was much later after VIT and everything.

**[1:09:06 – 1:09:10]** But for quite a few years,

**[1:09:10 – 1:09:15]** faster R-CNN was like the standard way to do object detection

**[1:09:15 – 1:09:16]** when you have time.

**[1:09:17 – 1:09:19]** So two-stage detection,

**[1:09:20 – 1:09:22]** even if it's all in the same architecture,

**[1:09:22 – 1:09:23]** is pretty slow.

**[1:09:23 – 1:09:28]** And you still have...

**[1:09:29 – 1:09:34]** And it shines if you give it a very smart,

**[1:09:35 – 1:09:36]** very complicated backbone,

**[1:09:36 – 1:09:38]** if you use a good network.

**[1:09:39 – 1:09:43]** So, of course, CNN's progressed,

**[1:09:43 – 1:09:45]** you know, from ResNets,

**[1:09:45 – 1:09:49]** from VGGs to ResNets to EfficientNets, ultimately.

**[1:09:50 – 1:09:53]** And when you see an architecture like this,

**[1:09:53 – 1:09:58]** you can just plug in a different backbone here.

**[1:09:58 – 1:10:00]** You don't have to change anything over here.

**[1:10:00 – 1:10:04]** And you will get a better object detector, okay?

**[1:10:04 – 1:10:08]** So notice how our discussion has shifted

**[1:10:08 – 1:10:12]** from architectures to meta architectures.

**[1:10:13 – 1:10:19]** You have now this global idea of a neural network

**[1:10:19 – 1:10:22]** that extracts features and then does the region proposal

**[1:10:22 – 1:10:23]** and then everything.

**[1:10:23 – 1:10:27]** And the top part, the heads, are more or less fixed.

**[1:10:28 – 1:10:31]** But for the bottom part, you can substitute whatever.

**[1:10:32 – 1:10:39]** And whenever a new feature extractor comes out

**[1:10:39 – 1:10:42]** that works better, you get better object detection for free.

**[1:10:43 – 1:10:44]** That's how it's always worked.

**[1:10:46 – 1:10:47]** Okay.

**[1:10:47 – 1:10:52]** At the same time, I still want to get to transformer-based detection,

**[1:10:52 – 1:10:54]** so I will speed up a little bit.

**[1:10:54 – 1:10:58]** At the same time, there was a separate line of work

**[1:10:58 – 1:11:04]** called one-stage object detection where you do it in one path.

**[1:11:05 – 1:11:07]** And what is the difference?

**[1:11:07 – 1:11:10]** What's the difference between one-stage and two-stage detectors?

**[1:11:10 – 1:11:13]** The difference is, in one-stage detection,

**[1:11:14 – 1:11:20]** you do only one path of the network through the image,

**[1:11:20 – 1:11:24]** and there is no separate stage.

**[1:11:24 – 1:11:26]** I mean, here it's also a part of the network.

**[1:11:26 – 1:11:27]** It's a fine distinction.

**[1:11:28 – 1:11:32]** But here, there is a stage where you have your proposals,

**[1:11:33 – 1:11:37]** then you rank them, you choose the top proposals,

**[1:11:37 – 1:11:41]** and for the top proposals, you do some heavy stuff over here.

**[1:11:41 – 1:11:44]** In one stage of object detection,

**[1:11:45 – 1:11:50]** you just go over all of the possible proposals,

**[1:11:51 – 1:11:55]** which means that maybe there will be fewer of them

**[1:11:55 – 1:12:00]** because you can't go over all possible rectangles

**[1:12:00 – 1:12:02]** inside an image in terms of pixels.

**[1:12:02 – 1:12:03]** That would be too much.

**[1:12:03 – 1:12:05]** That would be like number of pixels squared,

**[1:12:06 – 1:12:07]** completely invisible.

**[1:12:09 – 1:12:14]** But maybe you can go over reasonable candidates

**[1:12:14 – 1:12:17]** for bounding boxes at some level of granularity.

**[1:12:17 – 1:12:25]** And yeah, that is best exemplified by the YOLO family.

**[1:12:26 – 1:12:30]** Let me maybe not discuss the original YOLO.

**[1:12:30 – 1:12:31]** It's kind of irrelevant,

**[1:12:32 – 1:12:35]** although it's quite beautiful in its ideas

**[1:12:35 – 1:12:38]** and the loss function we already discussed.

**[1:12:38 – 1:12:42]** But anyway, maybe not relevant now.

**[1:12:44 – 1:12:47]** And then, oh, all right.

**[1:12:48 – 1:12:48]** Yeah, sorry.

**[1:12:50 – 1:12:53]** Yeah, no, sorry about that.

**[1:12:54 – 1:12:56]** I thought I would have slides about YOLO v2

**[1:12:56 – 1:12:58]** and YOLO v3 and everything.

**[1:12:58 – 1:12:59]** Yeah, I decided to skip them,

**[1:12:59 – 1:13:02]** but forgot that I took out the slides.

**[1:13:03 – 1:13:07]** So after, so the YOLO family basically,

**[1:13:08 – 1:13:12]** okay, so let me maybe show you this picture anyway.

**[1:13:12 – 1:13:14]** The YOLO family goes like this.

**[1:13:15 – 1:13:17]** You have a single neural architecture

**[1:13:17 – 1:13:19]** that starts with an image,

**[1:13:20 – 1:13:23]** goes over lots of candidates in parallel

**[1:13:23 – 1:13:32]** and outputs the results for all of these candidates

**[1:13:32 – 1:13:34]** and then you can rank them

**[1:13:34 – 1:13:36]** and just take the top however many you need.

**[1:13:36 – 1:13:39]** So there was the original YOLO,

**[1:13:39 – 1:13:43]** then YOLO v2, YOLO 9000 that had a lot of classes

**[1:13:43 – 1:13:54]** and also pretty interesting techniques like the hierarchical softmax.

**[1:13:55 – 1:13:56]** Also a very interesting idea.

**[1:13:56 – 1:13:58]** Unfortunately, we don't have time to discuss it.

**[1:13:58 – 1:14:01]** Then there was YOLO v3 and everything.

**[1:14:01 – 1:14:08]** And basically, as you go through these architectures,

**[1:14:09 – 1:14:17]** the basic architectures change a lot in many small ways.

**[1:14:18 – 1:14:22]** I mean, there is rarely one big idea

**[1:14:22 – 1:14:25]** that you need to actually,

**[1:14:27 – 1:14:30]** that you can just understand.

**[1:14:30 – 1:14:32]** And that's the huge step.

**[1:14:32 – 1:14:35]** So usually, it's like 10 different little tweaks.

**[1:14:36 – 1:14:39]** Every tweak gives you like plus 2% to the accuracy

**[1:14:39 – 1:14:41]** to whatever metric you're using.

**[1:14:41 – 1:14:43]** Also a very interesting discussion

**[1:14:43 – 1:14:44]** of what are the metrics in object detection.

**[1:14:44 – 1:14:49]** But anyway, everyone gives you like plus 1%, plus 2%.

**[1:14:49 – 1:14:52]** And then as a result, when you combine all of them,

**[1:14:52 – 1:14:54]** you get like plus 15% to the result.

**[1:14:54 – 1:14:55]** And that's a huge leap forward.

**[1:14:56 – 1:14:59]** So in a way, it's a lot of small things.

**[1:14:59 – 1:15:03]** But let me mention just one more thing

**[1:15:03 – 1:15:06]** about object detection before we go on to transformers.

**[1:15:07 – 1:15:14]** So what is the main problem of object detection,

**[1:15:14 – 1:15:18]** both classical, both contemporary and whatever,

**[1:15:19 – 1:15:21]** with neural networks, with classical algorithms?

**[1:15:22 – 1:15:27]** The problem is always about detecting small objects.

**[1:15:27 – 1:15:32]** That's always the hardest and sometimes even impossible.

**[1:15:32 – 1:15:36]** So if I have a cat over here,

**[1:15:36 – 1:15:39]** and this cat takes up a quarter of the image,

**[1:15:41 – 1:15:43]** mostly any object detection algorithm,

**[1:15:44 – 1:15:47]** any object detection architecture will recognize it fine.

**[1:15:48 – 1:15:49]** That will be okay.

**[1:15:50 – 1:15:53]** Starting from the original FasterCNN

**[1:15:53 – 1:15:55]** and YOLO v2, it will be fine.

**[1:15:55 – 1:16:00]** But if there is also like a small cat in the distance over here,

**[1:16:01 – 1:16:09]** then we are again at this crucial trade-off,

**[1:16:09 – 1:16:12]** crucial dilemma that we cannot really resolve.

**[1:16:12 – 1:16:14]** And we see it again.

**[1:16:14 – 1:16:16]** We return to the same thing again.

**[1:16:17 – 1:16:20]** We need to fix a level of granularity.

**[1:16:20 – 1:16:23]** So in terms of FasterCNN,

**[1:16:23 – 1:16:26]** you go through your CNN,

**[1:16:26 – 1:16:28]** you extract features,

**[1:16:28 – 1:16:31]** and then at some point you stop, right?

**[1:16:32 – 1:16:33]** And you need to decide

**[1:16:33 – 1:16:35]** at which point do you stop.

**[1:16:36 – 1:16:38]** If you stop too late,

**[1:16:38 – 1:16:41]** it means that you have lost a lot of the geometry.

**[1:16:42 – 1:16:44]** Your feature grid,

**[1:16:44 – 1:16:46]** if you map it back to the original pixels,

**[1:16:46 – 1:16:49]** maybe looks something like this, right?

**[1:16:49 – 1:16:52]** And now this small cat

**[1:16:52 – 1:16:56]** lives completely inside one feature vector

**[1:16:56 – 1:16:59]** and it doesn't even define it entirely.

**[1:16:59 – 1:17:02]** So you are losing this cat.

**[1:17:02 – 1:17:04]** You will never recognize this object

**[1:17:04 – 1:17:06]** that is completely inside one feature vector.

**[1:17:07 – 1:17:09]** It's just this information has been lost

**[1:17:09 – 1:17:11]** along the way to here.

**[1:17:12 – 1:17:14]** On the other hand,

**[1:17:14 – 1:17:16]** if you stop too early,

**[1:17:18 – 1:17:22]** so now, yes, we have a fine grid here

**[1:17:22 – 1:17:24]** and we can recognize this cat,

**[1:17:24 – 1:17:26]** but now it becomes infeasible

**[1:17:26 – 1:17:28]** because everything that happens

**[1:17:28 – 1:17:29]** with this guy over here

**[1:17:29 – 1:17:32]** involves some kind of,

**[1:17:32 – 1:17:35]** you know, going over all of these features

**[1:17:35 – 1:17:37]** with all possible candidates

**[1:17:37 – 1:17:39]** for bounding boxes and stuff like that.

**[1:17:39 – 1:17:41]** So just like you can't do it

**[1:17:41 – 1:17:42]** on the pixels themselves,

**[1:17:42 – 1:17:43]** you probably can't do it

**[1:17:43 – 1:17:44]** on this too fine grid.

**[1:17:45 – 1:17:47]** So this would be great,

**[1:17:47 – 1:17:50]** but it's kind of infeasible.

**[1:17:51 – 1:17:53]** And even if it was feasible,

**[1:17:53 – 1:17:56]** so again, I don't have time

**[1:17:56 – 1:17:57]** to go into details,

**[1:17:57 – 1:17:57]** but you could say,

**[1:17:57 – 1:18:00]** oh, okay, but what if I just look

**[1:18:00 – 1:18:01]** for small objects

**[1:18:01 – 1:18:03]** if I have this fine grid?

**[1:18:03 – 1:18:07]** Well, this you can do.

**[1:18:07 – 1:18:08]** Now it becomes feasible

**[1:18:08 – 1:18:10]** if you don't need to go over

**[1:18:10 – 1:18:11]** like all possible objects

**[1:18:11 – 1:18:12]** on the fine grid,

**[1:18:12 – 1:18:13]** but only on the small one.

**[1:18:13 – 1:18:13]** Then again,

**[1:18:13 – 1:18:15]** this quadratic complexity disappears.

**[1:18:16 – 1:18:18]** And now what you can do

**[1:18:18 – 1:18:19]** is you can do something

**[1:18:19 – 1:18:24]** like multi-stage object detection

**[1:18:24 – 1:18:26]** where you have,

**[1:18:26 – 1:18:28]** let me now draw it vertically,

**[1:18:28 – 1:18:29]** you have your image,

**[1:18:30 – 1:18:32]** you go through the first level,

**[1:18:34 – 1:18:36]** through the first kind of

**[1:18:36 – 1:18:40]** set of layers.

**[1:18:40 – 1:18:42]** This is the first part of the CNN.

**[1:18:43 – 1:18:45]** And here you have still a fine grid,

**[1:18:46 – 1:18:49]** but not very semantically rich.

**[1:18:49 – 1:18:53]** And here you can actually go ahead

**[1:18:53 – 1:18:57]** and do your region proposal network

**[1:18:57 – 1:19:00]** and then get your bounding boxes

**[1:19:00 – 1:19:02]** for the small objects.

**[1:19:02 – 1:19:09]** Then you do another few layers of the CNN

**[1:19:09 – 1:19:13]** and you have a more global set of features.

**[1:19:14 – 1:19:17]** And then you do another part of the CNN

**[1:19:17 – 1:19:19]** and you have the most global set of features.

**[1:19:19 – 1:19:25]** And so you have these three different scales

**[1:19:25 – 1:19:29]** at which you are doing object detection

**[1:19:29 – 1:19:34]** and another different scale like this.

**[1:19:34 – 1:19:39]** So now this guy will detect large objects,

**[1:19:39 – 1:19:42]** this guy medium, and this guy small.

**[1:19:43 – 1:19:45]** And you can basically do it.

**[1:19:46 – 1:19:50]** But notice that it's not that expensive.

**[1:19:50 – 1:19:53]** It's more expensive, of course, but not prohibitively

**[1:19:53 – 1:19:58]** with just one small detail.

**[1:19:58 – 1:20:00]** And the one small detail is that,

**[1:20:01 – 1:20:05]** as I told you in the beginning,

**[1:20:06 – 1:20:08]** when you are recognizing small objects,

**[1:20:09 – 1:20:11]** you really want to have global context.

**[1:20:11 – 1:20:13]** You want to understand what the image is about.

**[1:20:13 – 1:20:14]** It will help a lot.

**[1:20:15 – 1:20:17]** Small objects are really hard to recognize

**[1:20:17 – 1:20:20]** because they only take up a few pixels.

**[1:20:20 – 1:20:22]** And like if I showed you this crop with a few pixels,

**[1:20:23 – 1:20:25]** we humans wouldn't be able to recognize them too.

**[1:20:26 – 1:20:28]** We would need the context of the whole image.

**[1:20:30 – 1:20:33]** So one of the most fruitful ideas

**[1:20:33 – 1:20:36]** after this faster CNN deals

**[1:20:36 – 1:20:41]** was what is called an FPN,

**[1:20:41 – 1:20:43]** feature pyramid network.

**[1:20:45 – 1:20:48]** And the idea of a feature pyramid

**[1:20:48 – 1:20:51]** is to do this path bottom-up

**[1:20:51 – 1:20:55]** to detect large objects, just like I said,

**[1:20:56 – 1:20:58]** but for detecting medium objects

**[1:20:58 – 1:21:03]** to also copy here and fuse somehow

**[1:21:03 – 1:21:08]** features from a more global scale.

**[1:21:09 – 1:21:12]** And then also from here to copy and fuse

**[1:21:12 – 1:21:17]** features for the finer scale.

**[1:21:17 – 1:21:19]** So in this way,

**[1:21:20 – 1:21:23]** you are not increasing your work too much.

**[1:21:24 – 1:21:26]** It's okay, it's just a couple more layers

**[1:21:26 – 1:21:28]** over here for the fusion, that's it.

**[1:21:29 – 1:21:33]** But now you give the network an opportunity

**[1:21:33 – 1:21:36]** to actually capture this global context.

**[1:21:37 – 1:21:41]** So FPN was a very influential idea, still is.

**[1:21:42 – 1:21:46]** And again, we don't have time to go into details,

**[1:21:46 – 1:21:49]** but I could give you a big, big, big survey

**[1:21:49 – 1:21:53]** of what different stuff people did with this idea

**[1:21:53 – 1:21:56]** and with the idea of multi-scale,

**[1:21:56 – 1:21:58]** multi-stage object detection.

**[1:21:59 – 1:22:04]** And in particular, in the CNNs,

**[1:22:04 – 1:22:10]** we talk about the efficient net family of architectures

**[1:22:10 – 1:22:15]** where they would use neural architecture search

**[1:22:15 – 1:22:18]** to search for the most efficient architectures.

**[1:22:18 – 1:22:24]** And here there is a parallel efficient net family of architectures

**[1:22:24 – 1:22:30]** where they actually search for the optimal way to do this.

**[1:22:31 – 1:22:36]** So you fix your backbone for feature extraction to be efficient net,

**[1:22:36 – 1:22:44]** but then you search for the best way to do this post-processing more or less.

**[1:22:44 – 1:22:46]** Because you can do a lot of stuff here.

**[1:22:46 – 1:22:49]** You can go down and then again up and then again down,

**[1:22:50 – 1:22:52]** or you can go skip layers or whatever.

**[1:22:52 – 1:22:56]** It's not that expensive and you are allowed to experiment here.

**[1:22:57 – 1:23:01]** So they experimented and there was also a step forward over here.

**[1:23:01 – 1:23:05]** But anyway, I really need to switch to transformers.

**[1:23:06 – 1:23:15]** So at this point, we've discussed, so to speak, classical object detection.

**[1:23:16 – 1:23:25]** I call it classical here, but it's already deep learning.

**[1:23:25 – 1:23:29]** And usually when people say classical, they mean something before deep learning.

**[1:23:30 – 1:23:38]** Anyway, and then transformers appeared and then the VIT happened.

**[1:23:39 – 1:23:48]** And suddenly there was this question, there was this idea of how can we apply transformers to object detection?

**[1:23:50 – 1:23:52]** And can we make it actually easier?

**[1:23:53 – 1:23:58]** Because everything that I told you, it all makes sense.

**[1:23:58 – 1:24:11]** And it's like a lot of ideas that make logical sense and that work and that constitutes this big field of research for object detection and everything.

**[1:24:13 – 1:24:18]** But what did the transformer teach us, us, the humanity?

**[1:24:19 – 1:24:38]** The transformer taught us that in deep learning and neural architectures, very often, maybe you can get away with just taking one excellent architecture like the transformer and just throwing everything to the transformer and letting it sort it out.

**[1:24:39 – 1:24:42]** Can we use the transformer to sort out object detection?

**[1:24:42 – 1:24:50]** Well, it turns out we can, and it's a very interesting approach, or actually a very interesting family of approaches.

**[1:24:52 – 1:25:12]** So the first idea, the first architecture that started this direction is called DETR, Detection Transformer, and I think Alex will have a practice session on DETR or its neighbors.

**[1:25:14 – 1:25:18]** And basically, what does it do?

**[1:25:20 – 1:25:23]** So, wait a sec.

**[1:25:26 – 1:25:28]** Yeah, I wanted this picture.

**[1:25:29 – 1:25:31]** So what exactly does DETR do?

**[1:25:32 – 1:25:38]** So first, by the way, it still uses a CNN, pretty interestingly.

**[1:25:38 – 1:25:42]** So the Transformer is not used to extract features from the image.

**[1:25:43 – 1:25:46]** The set of image features are extracted by the backbone CNN.

**[1:25:46 – 1:25:50]** But anyway, you use the CNN to extract the features.

**[1:25:51 – 1:25:59]** You add positional encodings as usual, and now you get your inputs to the Transformer encoder, right?

**[1:25:59 – 1:26:01]** So it's a sequence of vectors as usual.

**[1:26:03 – 1:26:05]** And here is the basic idea.

**[1:26:05 – 1:26:08]** The encoder doesn't do detection at all.

**[1:26:09 – 1:26:12]** The encoder just extracts features.

**[1:26:12 – 1:26:22]** It mixes up all of these vectors in some very convoluted way like Transformers usually do.

**[1:26:23 – 1:26:31]** And basically it will train together with the rest to make the features most suitable for object detection.

**[1:26:32 – 1:26:34]** The interesting part happens in the decoder.

**[1:26:35 – 1:26:37]** So this is like a full-scale transformer.

**[1:26:37 – 1:26:38]** It's not BERT or GPT.

**[1:26:39 – 1:26:40]** It's an encoder-decoder architecture.

**[1:26:41 – 1:26:48]** And in the decoder we have, you remember, right?

**[1:26:48 – 1:26:56]** In the transformer decoder you have this encoder-decoder attention where the queries come from the decoder,

**[1:26:56 – 1:27:01]** from the prefix that it already wrote, if it was a language model.

**[1:27:01 – 1:27:09]** And the keys and values come from the encoder part, from the vectors produced by the encoder.

**[1:27:09 – 1:27:18]** Well, here, there is no autoregressive generation, there is a set of what is called object queries.

**[1:27:18 – 1:27:29]** They are just vectors that are trained together with everything else, or maybe even just random vectors that are fixed.

**[1:27:29 – 1:27:45]** And you put them through these decoder layers, with the cross-attention from the encoder also informing them.

**[1:27:45 – 1:27:50]** So the information comes from here, the image comes from here.

**[1:27:50 – 1:28:00]** And then you take every one of the vectors here in the output and you treat it like the input for the detection head.

**[1:28:00 – 1:28:13]** So here you have small feed-forward network, like the usual detection head that does confidence classification and bounding box regression.

**[1:28:13 – 1:28:22]** And the input to this detection head is this transformed object query.

**[1:28:22 – 1:28:24]** So how many objects do I recognize?

**[1:28:24 – 1:28:27]** As many as the object queries.

**[1:28:27 – 1:28:29]** So again, we need to fix this number.

**[1:28:29 – 1:28:31]** This doesn't change.

**[1:28:31 – 1:28:42]** But other than that, notice how it's like this very different, but also very straightforward idea.

**[1:28:42 – 1:28:46]** So a backbone maps the input to features.

**[1:28:46 – 1:28:50]** Then we just flatten the grid here.

**[1:28:50 – 1:28:55]** This set of image features will have a width and a height, but we forget about it.

**[1:28:55 – 1:28:59]** We just convert it to asynchronous vectors.

**[1:28:59 – 1:29:01]** Add positional encodings, of course.

**[1:29:01 – 1:29:08]** And then go through this encoder, decoder, transformer architecture.

**[1:29:08 – 1:29:17]** And an object query is like this placeholder, right?

**[1:29:17 – 1:29:21]** It's like a slot for a possible object.

**[1:29:21 – 1:29:30]** So it kind of, I mean, when you look at how data actually works, object queries tend to

**[1:29:30 – 1:29:32]** kind of like specialize.

**[1:29:32 – 1:29:37]** So you will have an object query that looks like, I don't know, for small objects in the

**[1:29:37 – 1:29:43]** middle of the image or large objects on the left side of the image, something like that.

**[1:29:43 – 1:29:50]** They probably won't specialize in classes, but they will specialize in locations.

**[1:29:50 – 1:29:54]** And of course, most of them will just say no object.

**[1:29:54 – 1:30:00]** They will drive confidence to zero because you need to have a large number of queries,

**[1:30:00 – 1:30:10]** like 100, and in fact, images will have usually much fewer objects.

**[1:30:10 – 1:30:23]** What is also kind of interesting is that in dator, you don't need tricks like non-maximal suppression,

**[1:30:23 – 1:30:28]** because the queries talk to each other.

**[1:30:28 – 1:30:33]** They exchange information in this transformer decoder.

**[1:30:33 – 1:30:43]** And when they exchange information, they kind of specialize again.

**[1:30:43 – 1:30:48]** So there won't be, as the output of dator, there probably, hopefully,

**[1:30:48 – 1:30:58]** won't be a huge number, like two dozen almost identical squares around this seagull.

**[1:30:58 – 1:31:00]** There will be just one square,

**[1:31:00 – 1:31:04]** because the object queries learn to specialize and to not repeat each other.

**[1:31:07 – 1:31:14]** But then again, of course, there are problems here, too.

**[1:31:14 – 1:31:18]** I'm running out of time, but I will mention a few more architectures.

**[1:31:19 – 1:31:22]** One problem is the same that I already mentioned.

**[1:31:22 – 1:31:24]** It's the problem of scale.

**[1:31:24 – 1:31:33]** So as shown here, the data works on a single scale.

**[1:31:33 – 1:31:39]** So you see, I put the CNN through a backbone and I use these features and that's it.

**[1:31:39 – 1:31:50]** There is no way for the rest of this architecture to recover the small objects that got lost in this transition.

**[1:31:50 – 1:31:51]** No, they got lost.

**[1:31:51 – 1:32:01]** So the small objects will probably be not very good.

**[1:32:01 – 1:32:13]** Yeah, so here are examples that are working and you can actually visualize the attention heads,

**[1:32:13 – 1:32:25]** the self-attention that goes on inside the decoder and you can actually see that yes, indeed, object heads,

**[1:32:25 – 1:32:27]** object very specialized objects.

**[1:32:31 – 1:32:41]** And back to the scale problem, the next idea, the next modification was called deformable data,

**[1:32:41 – 1:32:44]** and deformable data is as follows.

**[1:32:45 – 1:32:51]** So first of all, you can run at several different scales.

**[1:32:51 – 1:32:57]** So here this part will be solving the scale problem in the same way as we discussed,

**[1:32:57 – 1:33:05]** by running on different scales, separately for small objects and large objects.

**[1:33:05 – 1:33:23]** But what is most interesting here is that deformable data uses what is called deformable attention.

**[1:33:23 – 1:33:36]** So if you look at what actually data attempts to, where does it spend its attention weights?

**[1:33:36 – 1:33:46]** You will see that the most important pixels are the pixels on object boundaries.

**[1:33:46 – 1:33:54]** So if you look, the decoder attention is localized on the boundaries of the objects.

**[1:33:54 – 1:34:00]** And basically in data, once you have attention like this, you've already separated the objects.

**[1:34:00 – 1:34:09]** And the rest of the job is to just classify them and maybe draw a better bounding box.

**[1:34:09 – 1:34:09]** That's it.

**[1:34:09 – 1:34:16]** But mostly attention already separates the objects, as you see, in different attention heads.

**[1:34:16 – 1:34:25]** So it's a natural idea to try to avoid this quadratic complexity of the transformer,

**[1:34:25 – 1:34:32]** which doesn't let you just work on a small scale, on the fine grid, right?

**[1:34:32 – 1:34:43]** A natural idea would be to avoid it by just looking not on every pixel, not on every feature vector,

**[1:34:43 – 1:34:45]** but looking on a small subset of them.

**[1:34:45 – 1:34:51]** And also, you don't know in advance what the subset will be.

**[1:34:51 – 1:34:56]** So again, I probably don't have time to explain in detail,

**[1:34:56 – 1:35:01]** but the basic idea is this: you have your attention head,

**[1:35:01 – 1:35:13]** and it looks at several other positions on the image,

**[1:35:13 – 1:35:16]** and collects features from these positions of the image.

**[1:35:17 – 1:35:24]** And the locations of these positions are also trained as part of training the whole thing.

**[1:35:24 – 1:35:29]** So yeah, there are some technical difficulties here, I won't go into the details,

**[1:35:29 – 1:35:33]** but basically it works like this.

**[1:35:33 – 1:35:44]** And in this way, you can actually afford to have this multi-scale feature map in the transformer as well.

**[1:35:44 – 1:35:50]** So the problem with this multi-scale approach would be that in the transformer,

**[1:35:51 – 1:35:54]** you need to attend to every other token.

**[1:35:54 – 1:35:58]** And if you have a fine grid, this quadratic complexity will kill you.

**[1:35:58 – 1:36:01]** Well, how do we deal with quadratic complexity?

**[1:36:01 – 1:36:09]** We just reduce, in this case, we reduce our attention to a small subset of the input tokens.

**[1:36:12 – 1:36:21]** Then the next set of ideas here is to work with the object queries themselves.

**[1:36:21 – 1:36:26]** So, again, I said that they tend to specialize.

**[1:36:26 – 1:36:31]** And if you look at however this was produced, I don't have time to explain,

**[1:36:31 – 1:36:39]** but on average, where are the boxes predicted by the object queries?

**[1:36:39 – 1:36:46]** In fact, they do kind of separate all over the input, which is great.

**[1:36:46 – 1:36:54]** But this kind of learning happens very slowly, not really stable.

**[1:36:54 – 1:37:02]** And a good question is, and the next reasonable question is, can we improve this?

**[1:37:02 – 1:37:12]** Because to be honest, this picture doesn't look like it would be difficult to produce just right from the start.

**[1:37:12 – 1:37:22]** Why don't we just take a grid or sample random points and help data produce better object queries?

**[1:37:22 – 1:37:29]** And indeed, the next step, again, I have to wrap up, but I want to mention it.

**[1:37:29 – 1:37:51]** The depth data or dynamic anchor box data, it actually uses anchors, it uses these object queries that are not just abstract vectors that will somehow over hundreds of epochs of training move away and learn to predict different stuff.

**[1:37:51 – 1:37:53]** But they're just bounding boxes.

**[1:37:53 – 1:37:59]** They have the meaning of X, Y, H and W, there are four numbers and that's it.

**[1:37:59 – 1:38:14]** So, when you have this kind of thing, you can actually, first of all, you can initialize them in a smart way so they are kind of separate from the beginning.

**[1:38:14 – 1:38:25]** And then you have this very clear semantics of what's going on between layers and you can actually refine them in a smarter way.

**[1:38:25 – 1:38:28]** I don't have time to explain here.

**[1:38:28 – 1:38:38]** As a result, you get better object queries, better anchors, as they are called, in less time.

**[1:38:38 – 1:38:43]** And yeah, I guess I will have to skip this, I will have to skip this.

**[1:38:43 – 1:39:00]** The best object detectors right now are dyno and their modifications, dyno, dendator and whatever, deformable data and so on and so forth.

**[1:39:00 – 1:39:08]** I left in the big survey on transformer based object detection, but unfortunately we don't have time to discuss them.

**[1:39:08 – 1:39:10]** But yeah, let me stop here.

**[1:39:10 – 1:39:33]** All of these things, all of these different architectures, they share this basic idea of the original data that the queries, the objects, the bounding boxes are queries to a transformer decoder and the transformer decoder will

**[1:39:33 – 1:39:40]** fill them with content according to the image.

**[1:39:40 – 1:39:47]** And then again, there's a big science about it, lots of results, lots of different architectures.

**[1:39:47 – 1:39:59]** Okay, so sorry, I ran a little bit over time, but we only have three lectures left and tomorrow will be something completely different.

**[1:39:59 – 1:40:02]** We'll go to more generative stuff.

**[1:40:02 – 1:40:09]** So any questions?

**[1:40:09 – 1:40:14]** In this case, thank you, I'll make it available and see you tomorrow.

## Full text

Okay. Hello everyone and welcome back. I'm happy to continue our discussions about deep learning. And specifically on this last week, we finally turned from something general. I mean, it usually happens every year that we start teaching a course called computer vision, but actually it turns out that you always need to start with something like deep learning basics and the actual computer vision gets bumped to the end of the class. But anyway, we are here and over the last two weeks, we have discussed, we have built up actually a wide array of architectures, a set of tools to solve various problems. And finally, we begin to apply them specifically to pictures. Well, we already talked about pictures in the context of CNNs, but we haven't yet talked about pictures in the context of Transformers. If I understand correctly, Alex already explained to you the VIT, the Vision Transformer, in practice sessions, so I won't be spending too much time on it. And our main plan for today, our main content will be a specific general but specific problem in computer vision, specifically object detection. And object detection is one of the most interesting problems in computer vision, and object detection is actually one of the hardest, in a way, because it's quite unusual. It has an unusual structure of the outputs compared to, say, segmentation, which we won't discuss in lectures, but maybe Alex will in practice. And there's a lot to talk about, and also transformers actually come in very interestingly and very differently in object detection. Actually, as we discussed, I think, usually the transformer just goes in, replaces some part of the architecture, and serves as a better feature extractor, and that's it. And there is nothing conceptually changing in the architecture quite often. For example, in segmentation, if you discuss it with Alex, he will tell you about the UNET architecture, which is from 2015 or something. But modern segmentation still uses UNET, only instead of convolutional layers inside, it uses some kind of self-attention based layers. There's a lot of new stuff happening, but basically the UNET did not get obsolete because the transformer appeared. In object detection, it's a little bit different, and we'll see how it works. So anyway, a few words, first on transformers for pictures, vision transformers. Let me not spend time at all on Visual Bird. Visual Bird was one of the first more or less successful approaches to handling pictures with transformers. And let me just tell you the setting, the problem setting for Visual Bird. It was for captioning mostly, and it worked like this. You had your text and you had object queries, like you had tokens that represented specific objects found on the picture. So to use Visual Bird, you would have to solve object detection first. And then you would plug in these subsets of the image, these rectangles. We'll discuss it in object detection, these rectangles that correspond to specific objects on the input image. And then pass them through some simple embedding layer, get a vector of features, and then off you go with the transformer. And the point of this picture for us is that for the transformer, as you can see here, it really, I won't say it doesn't matter, but it really matters little whether the input came from text or from images or from whatever. As long as it's a sequence of vectors, the transformer is an architecture that is great at finding various internal correlations between these vectors, finding structure inside, everything like that. So it is no wonder that at some point people just straightforwardly applied transformers to images. And again, Alex talked to you about this architecture, I won't waste time on it, but the most interesting, the most striking feature of the vision transformer architecture of the VIT is just how simple it is. I mean, you don't need to do anything. There is absolutely no change in the transformer architecture because now the input is an image. And in fact, you might think that when you cut a picture into patches, these patches do not really correspond to a natural one-dimensional sequence. Well, I mean, you fix some sequence, but adjacent patches in this sequence will not be necessarily anywhere close on the image. For example, if you go rows first, then you put the first three patches, they are indeed neighbors. And then after the third one, you go back to the left part of the image, and these two patches are nowhere near. So it is tempting to say that, well, an image is not really a sequence. An image has a two-dimensional structure. We need something new, something interesting, at least some change in the positional encodings that we discussed last time, in order to fix that. We need some change in the positional encodings to tell the transformer that it is actually a 2D structure. Again, it will not care if it's an image or what, it's just a vector of features for the transformer, but at least the positions should be somehow marked. Well, it turns out, no. In the original VIT paper, there's an appendix where they show that, "Oh yeah, sure, we tried several ideas on how to do these positional recordings and none of them help. Basically, you just treat it as a sequence, it's fine. Just use standard positional recordings from text transformers." And VIT kind of revolutionized image processing, revolutionized everything, well, computer vision and everything else dealing with images, because, again, a transformer is just better. It extracts better features, more semantically rich. In many, many applications, you can just, as I said, take out your convolutional network, plug in the VIT, just reuse the same stuff that you have on top of this feature extractor, and it will be better. And there were hundreds of papers that do exactly this after 2020. And there is only one problem. There is only one problem that is hard to solve for transformers. It's the main problem, the main computational problem of transformers, which I mentioned when we discussed the architecture itself. The problem is the VIT and any transformer has quadratic complexity. We discussed that in the transformer there is this matrix of attention weights. It's a token by token matrix. It's a matrix of size L times L, where L is the input size. It's really hard to go around this. It means that the VIT has complexity quadratic in the number of patches. Every patch becomes a token at the input of the VIT. If you have height h and width w, and let's say you have k times k patch, then there will be that many patches vertically times that many patches horizontally, and this will be squared. So the size of the grid is squared. And this is a big problem, in some applications at least, because it means that you cannot really, people try it with other architectures, but you cannot really have the VIT go down to the level of individual pixels. If you have a million pixels as input, a million squared is too much, even for modern hardware or whatever. So you have to have patches and you have to have relatively big patches. And if you have relatively big patches, it means that you can't really figure out the small details of your image. So if you are doing, for example, object detection to the VIT, whatever that would mean, and you want to find a cat in this image, and if the cat is small, maybe it's far away and it's completely inside one page or even the part of one page, or maybe it's on the boundary between two patches and none of them really is dominated by this object. Then I guess it will be very hard, because every patch will get flattened to a single vector and stuff will get lost along this way. So there's really no correct size for the VIT. Just like we discussed with the attention mechanisms, it's either too big, in which case you're losing detail, or it's too small, in which case you just can't train it and can't run it because it's too heavy. So what people did, there were a lot of approaches. I want to discuss one of them, specifically the Swin Transformer. The Swin Transformer, because it's one of the most popular. Today, if you open up some computer vision application, probably you will see either VIT or Swin. Some version of Swin or VIT as your backbone. And the Swin Transformer, so the Swin stands for shifted windows. And here is the thing. So as I said, the complexity grows as the square of the number of patches. So a natural way to save from this would be to break down the image into parts and then cut up the parts into patches. So for example, this here, I would, let's say, do a 2x2 grid like this. And then I would just take this guy, which has only a 3x3 grid, and here I would have complexity like 9^2. And here I will have 6^2, 6^2, 9^2. And if you add it all up, it will be a couple hundred. But the original complexity was like 25^2, which is, of course, much more. So if you have square complexity and you cut up into smaller pieces, you save a lot. And basically the square becomes linear because now it's the square only in the size of this small part. So it's very natural to have this kind of hierarchical structure where, first, if you have a large image at the input, first you cut it up into small pieces, relatively small pieces, like a 4x4 grid. Then you process every part here with VIT. Then you combine them and again you process with another set of VIT layers. Then finally you combine those somehow, I won't go into details how exactly, and process now globally the whole image also with VIT layers. So in this case, on this picture, every VIT layer, every transformer layer, deals with 16 tokens at the input, only 4x4 grids. But in three steps, we go from 16x16 image to 4x4 image, which is then compressed into features or a single vector or whatever. So that's the basic idea. And why is it called shifted windows? It's called shifted windows because, well, there is this problem that we will discuss in object detection too. The problem that when you look inside these small parts of the input image, very often it would help you greatly. Very often you would be very happy to have a more global context of what's happening in the image. Like, I don't know, you see, I can't draw it, but you see a small part of some kind of surface, and on the surface there is some kind of vehicle, right? And it's small, that's the whole problem, so it's hard to distinguish exactly what this vehicle is. So if you know that the context is a highway, and it's like a road with cars, then it's a car. If you know that the context is, I don't know, a lagoon of a sea, then it's a boat. Two very different classes. You can't really distinguish without global context. And this actually happens all the time. It sounds like a contrived example, but actually global context is necessary quite often. So you would like these guys down here to have a way to get information about what's happening in the rest of the image. And ShiftedWindows does it this way. Very interesting, very cool trick, I think. The trick is between self-attention layers, you shift the windows. So you would have on one layer, I want to draw it a little bit larger than on the example, because the picture from the paper is a little bit misleading. So you have a grid like this. And then on the next layer, you will have a grid like this. So it will shift like half of the size of the patch, and it will still be the same kind of transformer. It will still have the same size of input, but now it will shift to different subsets of features, so like different parts of the image. And notice that if I do it several times after every layer like they say, then this will expand the receptive field of my patches. So if I was sitting over here and I saw this part of the image, then after I go out here and then come back again, now the same transformer but in two layers up will already be looking at this part of the image, because it has collected actually even more, because this guy will be looking at here, so we will be looking at this part of the image, because the purple grid has been looking on this part, this transformer layer has been looking at the orange square, and when you go back you collect all of these neighboring adjacent purple squares. So this is how it works, and there's a lot of unclean and easy to mis-implement stuff around the edges, and this is what this picture shows. Basically, if you shift your grid, the edges will not fit anymore. These small parts near the edges of the image will not be full squares anymore. So what they actually do, they roll up the image in the torus, and they say, okay, so now this guy over here goes together with this guy. And this guy over here, the rectangle goes together with this rectangle, and the small squares at the corners also all go together as a single end. So this doesn't really matter all that much because it's only about the edges, but still, it's a lot of hassle. Once I saw an implementation, I don't think I have it here, but I saw an implementation of a 3D SWIN transformer where you do the same stuff, but with cubes instead of squares. And it was the most convoluted piece of code I've ever seen. There were lots and lots of hard-coded shifts and constants, and it was very difficult to understand. But anyway, the SWIN transformer, I won't discuss the exact architecture, but the SWIN transformer and the VIT both can serve as good backbones. So what is a backbone? It's a tool, part of the network, the largest part of the network that does feature extraction. And what would it do feature extraction for? Well, by default, the VIT is trained on something like classification. You do your feature extraction, you see where you collect the features into a single vector at the end, and you do your stuff about the reasoning, about the image as a whole, about it globally. But what we are discussing today, and our main content for today... Okay, it's been 20 minutes. Good. I think we are good on time. And what we are discussing today is a different kind of application, and a different kind of problem that will require us to look inside the image and to actually map our answers to specific pixels, which is always more difficult. So, I'll skip the perceiver. I don't have time for that. So, our main target, our main topic for today is object detection. Now, what is object detection? What's the problem? Well, okay, I don't have a slide on that, so let me just go to the board. And at first, let me discuss the problem setting because there's a lot to discuss. My first point was transformers for feature extraction from images. And our second point is what is object detection? Well, what is object detection informally? I hope you all kind of have an idea. So there is a big image like this and there is a cat inside, right? And maybe there's not only a cat inside, maybe there is something else. Maybe it's a big thing with a lot of objects. So the object detection problem goes like this. Given this image and given, let's say, the cat class. I also should specify what exactly I need to find. Find the cat and not only say that there is a cat. Give me the confidence, the probability that there is a cat, like the usual classification. But also to draw a rectangle around the cat to specify exactly where, and in terms of these rectangular positions, not down to individual pixels, that would be segmentation, but down to this rectangle, specify where exactly you found this cat. So this rectangle is called the bounding box, usually abbreviated to B box in documentation and papers. And then you can have many different classes, maybe in addition to a cat, on this image there is a dog somewhere. Let me draw a dog, I'm not sure, but at least let me make some different ears for the dog. Okay, so that's kind of a dog. And there is a dog, and I also want to recognize the dog, and I also want to draw a rectangle around the dog and also specify its bounding box. And the bounding boxes can overlap, of course, images can be anywhere, the objects themselves can overlap with each other, or they can just overlap in the empty parts of the rectangles, whatever, anything goes. The point is, for every object that I'm looking for, I need to output the class label and this bounding box. So how do you formalize a bounding box? It's a rectangle, you need to specify its coordinates. So usually people do it like this, they have X and Y for the bottom left corner or any corner that's... Interesting for you. And then the width and the height of directing, right? This rectangle is defined by four numbers. And so here is the interesting part now. I hope the idea of the problem is clear. I hope it's clear what we are trying to do here. But it's becoming less and less clear how exactly to do it, right? How would I define a neural network solving object detection? Let's not speak about architectures now, whatever is the network. But what is its input and what is its output? As input, obviously, I take the picture, I put it into my neural network. And now what is the output? Well, a picture can have multiple objects, right? If I assume that there is only one object, it's called object localization, and it's a much easier problem. So I need to have a way to output multiple objects, right? Like object one, two, three, and maybe more, maybe a lot more. Who knows, right? Then for every object, I need to have its class. So the class label as usual for classification in the form of a probability distribution. So this will be like the distribution on classes as always in classification. And then I need to specify the bounding books. So four numbers: x, y, w, h, and so on for every object. And here is the first tricky part. I cannot have a neural network with variable number of outputs. It kind of doesn't make any sense. So I need to fix the number of outputs from a neural network. I know how many outputs exactly I have per object. So per object I have the number of classes for their probabilities, and then four numbers for the bounding box. So if I know how many objects I have, I know how many outputs I want. But I don't know how many objects I have, right? On the picture there might be one cat, two cats, three cats, four cats and two dogs, whatever. I don't know. There may be hundreds of objects and I just don't know it in advance. So what's the answer to that? How do I solve the problem that I can't really have an open list at the output of a network? And I can't because at the output of a network there should be neurons with weights and I cannot have a variable number of neurons because I need to have this number of weights and I need to train them, right? So for this question the output, the answer is pretty trivial. For this question the answer is well, okay, let's fix some maximal number of objects that we want to recognize and let's just have this many outputs. This begs another question, right? This begs another question. Now what happens if there are fewer objects? What happens if I am recognizing 10 different objects but the picture only has a cat and a dog so like two objects and the rest is irrelevant. They are not my classes. Well, in this case, I need to have a way to specify that some outputs don't count, right? I need a way to specify that, okay, so object number one is real, object number two is real. The rest, they are not real. And usually it's done exactly like I said. So usually it's done by inserting, by adding another output, which I would call the confidence. So for every output, you would have something like, okay, here is how sure I am that there is an object here. And it's usually a probability, right? So from zero to one. Here is how sure I am that there is an object here. And if it is there, then here is its class label and here is its bounding box. So if I have only two objects, then sure, I would like the confidences for these objects to go to one and the confidences for all other objects to go to zero. So, okay, but this is also only the beginning. We still have a lot of unclear things here. We still have a lot of interesting questions left. So we defined what should be the output of the neural network. But this is only the first step and it's an intermediate step. What I really want to define, what we really need to define for this to work is a loss function. So what would be a loss function for this kind of output? What would be the loss? I have this picture and I have the ground truth, which are these two objects. So this is like y1, y2. For y1 I know it's a cat, I know where it is, I know it's bounding box. For y2 I know it's a dog, I know it's bounding box. How do I compare this to the output of the neural network? What should I optimize? Well, kind of, again, non-trivial. Why non-trivial? Because I can't just say, well, object number one should be this cat, object number two should be this box, this dog, and that's it. Because the neural network doesn't and shouldn't have any idea of some kind of ordering of the objects, right? It doesn't make any sense. They don't come ordered. I just want to recognize the objects on the image. I don't know if the cat is number one and the dog is number two. And also, if I have confidences like here, and if I have a big list of possible objects, then I don't want to require the neural network to, in addition, sort them by confidence or something. That would be difficult and completely unnecessary. I just want this cat to be somewhere inside, and this dog to be somewhere inside, and the rest, the other outputs to have low confidence, right? So what we actually are looking at is we need to find a matching between the ground truth, the ground truth, the answer, and the predictions of the neural network. So it's called an assignment problem, right? We need to assign elements of these two sets to each other. I can pad this with no object to k, and then I need to assign elements of these sets to each other to minimize some kind of cost. Okay. Here, I suppose you will discuss it in practical sessions, there will be something like the Hungarian algorithm that actually produces this bipartite matching, one-to-one matching between predictions and ground truth in a way that actually assigns the ground truth box to the best predictor. But that's also not enough, right? So what is the loss function then? Well, the loss function, and here I won't go into full formal details because they can differ. There can be different ideas and different weights and whatever. But the loss is composed of two things, right? The classification loss of three things, sorry. The confidence loss from, like, if there is an object, the confidence should go to one. If there is not an object, the confidence should go to zero. That's one part. And that's pretty easy, right? It's like just the log confidence minus log confidence or something. Then there is the classification loss. So if there is an object, let me put it this way. If there is no object, then we don't care what the class label says. Because if there is no object, then it's just random stuff. If there is an object, then we care. And then it's probably just a cross-entropy between these two probability distributions, right? And then there should be the bounding box loss. So these numbers should represent the correct rectangle. And of course, they won't in practice. And again, it only matters if you have an object. But if you do have an object, what is the loss for the bounding box? You can do it with some straightforward loss like x minus x predicted squared plus so on plus h minus h predicted squared. Or not squared or maybe the same, but like absolute values for an L1 loss or whatever. But problems with this coordinate based losses, one common problem is that you will get very different contributions into this loss for large objects and for small objects. So, okay, in our example, I have two large objects. But anyway, if I have like this ground truth box for the cat and my predicted box is like this, well, it's pretty good, right? It's pretty good, but we have quite a lot of distance here, so I will need to move the bottom left corner down here and then up here. And the width and height, I don't know how to draw it, but they also need to be updated, to be adjusted. But if I have a very small object like this, and as we will see, small objects are the most interesting case for object detection. This is what's difficult. Then, for the same kind of loss, my bounding box will be completely different. So here, they overlap a lot when they are large. And here, for the same loss, for the same differences in width, height, x and y, they will not overlap at all. So, not really intuitive, right? I don't really want this to make identical contributions. I want this to be a bad thing and this to be an almost perfect thing, right? So, how do I fix that? Well, the answer is, I don't want to get my... I mean, some approaches to object detection, including some of the ones that we will discuss today, say, "Well, alright, what can we do? Let's still use something like that." Like the original YOLO uses a loss function like that. But these days, usually, people do some kind of a loss based on what is called the intersection over union metric. So, the IOU of two areas on a plane, in this case two boxes, is precisely what it says: intersection over union, the area of their intersection divided by the area of their union. So, in this case, I take this guy, and I divide it by this guy. And I get something like, I don't know, 0.6, 0.7, I guess, in this case, which is a pretty good idea. In this case, I get exactly zero. So this is the default metric for measuring goodness of match between bounding boxes and predicted boxes. And it only has one more problem. I won't go into more detail formally, but it has only one problem in that now if the boxes don't overlap, the IOU, as I said, is exactly zero. And notice that the IOU is actually differentiable. It's not piecewise constant. You can pass gradients through it. If you slightly tweak, if you push this bounding box a little bit to some size, you will get a small change in the IOU. So the gradients make sense. But the gradients stop making sense when the numerator becomes zero. And this is a bad thing again, because when I look at these two bounding boxes, I do want to be able to say that I want to move it here. But from the point of view of the IOU, if I move it in the right direction a little bit, it's no difference than if I moved it in the other direction a little bit. It will still be zero and the gradients don't help. So, in effect, there are additional metrics, something like the generalized IOU, which I'm not even sure I remember correctly the formula, so I won't try to reproduce it. But basically, they make use of this bounding box, and they involve something like what is the percentage of this common bounding box, not covered by these two boxes, something like this. So now if you move in the right direction, then this joint bounding box shrinks and the percentage becomes larger. So this would be a good thing. And I think that's it for the loss function. So we have discussed the main components, the main usual components of the loss function, but there is one more little thing. There is a more little thing that happens when you apply the neural network. So now I guess I talked through everything that happens when you train the neural network, but what happens when you apply it? And notice that so far I haven't said a single word about how it actually works, what's inside the neural network, what's going on. I'm just talking about the loss function, and this is pretty common in difficult problems and non-standard problems. The architectures will come and go, but the loss functions are like a separate object. They don't care what the architecture is as long as you can pass the gradients through. And they deserve a separate discussion and they evolve separately. There is a line of work that tries to optimize the losses. And a separate line of work, maybe in the same papers, but it's completely detached. You can optimize them independently. The architecture and the losses. Okay, so I finished talking about the losses, but what about the application? What about the inference of this neural network? What's the problem there? There are two problems. And again, I won't go into too many details, but a little bit I have to mention. So here is a picture and here is a cat on this picture. And the cat is very happy. And I want to recognize this cat, right? Actually, it concerns the loss function too. Sorry. But yeah, it concerns the training time too. Sorry. We did not quite finish with the training. Because here is the thing. Yes, I can get you the best possible assignment between the ground truth objects and the objects that I predict. But even after I get the best possible assignment, I still need to decide which parts, which predictions are actual objects and which predictions don't count. So suppose that in this case I get a bounding box like this, right? So this bounding box is kind of maybe about this cat. It looks like it's about this cat. So when I look at the bounding box like this, I want to say, well, almost right, but you need to shift your bounding box over here, right? And you need to put the class labels so that it's a cat. So in this case, for this gray bounding box, I want to say, well, I want to make you into the cat bounding box. And then if I have a bounding box like this, for example, it also kind of overlaps with the cat, right? But most probably it's about something else. And even without looking at the rest of the picture, even without looking at its class probabilities, probably it's not about the cat. And probably if there is no ground truth over here, if there are no other objects in here, then probably for the light blue box, I don't want... So for the gray box, I want it to become the cat box, and I want its confidence to go to one. For this box, well, it never had much in common with the cat. I don't want to bring it over here, it doesn't sound right. I just want its confidence to go to zero. It's just a spurious bounding box, and there will always be lots and lots of outputs where the confidence should go to zero. Because, again, remember that there are a lot of outputs, many boxes, like the maximum possible number of objects, and in reality, there will be two or three on a given picture, and most of the outputs should have confidence to go to zero. So here, too, I need to distinguish between these two cases. Either I want to count this box to become the cat, or I just want to say, okay, this is a bad, bad box, and let's just forget about it. Well, again, in practice, it's done with an IOU threshold. So you just pick a number, like one half or something, and if the overlap is larger than one half, then you count this output as the ground truth. And if the output is less, then you don't count. So this is easy, but still also need to mention. And finally, I guess Alex will talk more about this in practice. Finally, there is this effect that when you have an object, like a clear object that's easy to recognize, and you run this image through a neural network that has a possibility to distinguish dozens or hundreds of objects, most probably, not one, but a lot of them will stick to this cat. So you will have a bounding box about this cat like this, and you will have another bounding box about this cat like this, and you will have another bounding box about this cat like this, and there will be a dozen of those. Of course, you don't need to repeat the same object 12 times. I guess the standard way to cope with it is an algorithm called non-maximal suppression, and let me just leave it at that. It doesn't matter for training. For training, we just do the best matching, and that's it. For actual inference, you need to do this non-maximal suppression to pick the best possible bounding box, because now you don't know what the ground truth is, and you need to somehow combine all of these hypotheses into a single box. But overall, that's it for the problem setting. So notice that I haven't yet said anything about how to actually solve this problem. I haven't said anything about what's inside the neural network and how do we produce all of these wonderful outputs. Well, let's say a few words about it. So what kind of words? What can we say? Well, I won't, of course, go back in history before deep learning. We are doing deep learning after all. I will go 10 years back to 2014, when there was like this first approach, kind of after AlexNet revolutionized image processing, people tried to apply deep learning everywhere for images, and finally they got to object detection. And the first successful attempt was called RCNN, which stands for region-based CNN. And Ross Gershuk is one of the best known researchers in object detection. And here is how his original approach worked a long time ago. Well, first of all, it used an external algorithm called selective search, I won't go into details, to produce candidate bounding boxes. So you put your image through some algorithm, and it gives you candidate bounding boxes. But this algorithm doesn't know the classes. It doesn't care about the classes. It just finds distinctive objects on the photo. That's it. So if you want to recognize cows, you will still get this post over here and the clout and the ear of a cow and whatever. So you will get hundreds of candidates and only a few actual boxes. So what next? Then they take every one of these boxes and treat them separately and pass every one of these boxes through a neural network. In this case, a CNN trained on ImageNet. So this is the backbone. And this CNN will tell you what class of object it is. It sounds very straightforward. Of course, this doesn't answer the most interesting questions. So first, a technical remark. To actually put a bounding box through a CNN pre-trained on ImageNet, you need to make it square. The CNN pre-trained on ImageNet expects 256 by 256 square photo. So what they actually did was they took this box and actually warped it, just compressed it so that it would become square, just artificially geometrically compressed. And it actually worked. I mean, obviously for this post over here, it would make it very, very different, right? But still, it was the best solution at the time. And then also another problem was that the CNN, the backbone, will not tell you whether there is an object or not, right? A CNN trained on ImageNet presumes that there is an object and just classifies it. If you give it some bad bounding box, it's just a sky with some clouds. I don't know if ImageNet has the class cloud, maybe it does. If it does, then hopefully it will be recognized as a cloud. But if not, it will be just some distribution over classes. There is no confidence in the outputs of a classification network. So they actually also had to have a third step here, another step that takes the outputs of this CNN and modifies them and passes them through a completely different model, a model on top of that, that would actually further classify based on these probabilities, like whether it's a real object or not. It was very fragile. It still was the best approach at the time, which shows just how cool deep learning is, but it was, of course, very fragile and it was hopelessly slow, hopelessly slow. It was like a minute per image on a GPU. But all of the ideas are already in this original RCNN architecture. At least all of the ideas of this one approach to object detection that is called two-stage object detection. So I actually used to have very detailed lectures on object detection that would go through dozens of different architectures. I will not do that with you. We don't have time. And they became less relevant as time goes by. So we will jump to Transformers in a little bit. But I do want to discuss the RCNN family because in a way it's still relevant. And it's still relevant. It explains in these simple examples. It still explains the main ideas. So what are the main ideas in this basic RCNN? The main idea is use your backbone to extract features from a specific part of the input. And where do these candidate bounding boxes come from? Well, in this case, they come from an external algorithm. Later we will see they will come from the network itself. But still, you first get a set of candidates. And then you process every candidate through a CNN, you extract the features, and then you see what's inside there and what you want to do. So this is the idea of two-stage object detection. First, produce a relatively small set of candidate bounding boxes, then process every bounding box in a way. But of course, processing every bounding box completely independently is, again, hopelessly slow. So this picture has the real numbers. To get good coverage of the actual objects, of the actual bounding boxes, we need to extract 2,000 region proposals. So where do these 47 seconds come from? They come from running the same network. The network is very fast, actually, but you have to run it like 2,000 times and then run a model on top of its results to actually get something, right? So this is, of course, hopelessly slow. So the next step in what was called faster CNN, the next step was to, and this is an important idea, was to process the whole image only once. And then extract features from the feature tensor, take parts of the feature tensor, rather than reprocess everything from pixels. Makes perfect sense, right? So you have this, I won't waste time on trying to redraw this on the board, let me just talk through the slide. So you have this long convolutional network or long transformer network or whatever. And, okay, no, transformers don't work like that, but you have this long convolutional network. And as we go through the convolutional network, as we discussed, you gradually lose the geometry. And if you want to keep some of the geometry, you stop it a bit earlier. We did this for attention mechanisms before. So the same idea here. You pass your big picture through the CNN only once. But you stop a little bit short of the goal. So you get this feature tensor that still has geometry. Then you take your candidate bounding boxes. And faster CNN, they are still produced by an external tool, by an external algorithm. These bounding boxes. And when you have some geometry on the feature tensor, it's not a problem to find out which features correspond to which pixels of the original image. You just have this correspondence. So when you have a bounding box, you can project it. It's called ROI projection, region of interest projection. ROI is a very common abbreviation in object detection. It stands for region of interest. You have this ROI projection. It's not a trainable thing. It's just which features look at these pixels. And now you have the same bounding box, only rougher, and inside the feature tensor. And then you take this bounding box and you put it through an object detection head. An object detection head that has basically a classifier for the classes and the bounding box regressor for the bounding box itself. So I didn't mention it before. Let me mention it here. Usually, even if you have candidates already in terms of pixels like here, you still want to have a bounding box regression at the output because maybe the network will want to shift this bounding box a little bit and it will be useful. So the network might decide, oh, okay, so this is about the cat, but I need to shift it a few pixels to the left. And yeah, that actually happens and you can train it because you have the ground truth, so it's a good thing. The bounding box regression is always here. One detail about this is that, okay, so now I run the big convolutional network only once. And for every bounding box, I actually run only this small head. I want to say classification head, no, small detection head with a classifier and a regressor. So this is already like orders of magnitude faster. One technical problem is that, again, I don't know, I need somehow to fix the size of the input for this guy here. So my bounding boxes will come in different sizes and they will map to parts of the feature tensor of different sizes too. And I need the input to this head, detection head, to be always the same. What do I do? Well, I insert what is called a region of interest pooling layer. And also a pretty straightforward idea, but pretty cool. Let me draw it over here. Straightforward but cool idea. I have, let's say, this is the feature tensor, right? And I have a bounding box in the feature tensor that goes, let's say, like this. So, it's a 3x5, 5x3 tensor. Don't care what the depth is, I will not cut the depth. But it's 3x5 and my detection head wants to have as input a 2x2 tensor, let's say. So, what do I do? I do pooling, but I do, like, pooling not with a fixed window size, but pooling with a fixed output size. So, in this case, I will see, I know that I expect my output to be 2x2, and I will just cut it up as evenly as possible to have 2x2 windows. So, of course, it will not be exact, because these are integer numbers, but as close as possible. And then I will pool the features in these four windows. So this is called region of interest pooling. That's, I guess, the one cool idea that I wanted to mention for faster CNN. And not just for faster CNN, it will be used everywhere, starting from faster CNN. So this was already orders of magnitude faster, and the remaining bottleneck, now the slowest part of this pipeline, was not in the network at all. Now the slowest part was actually this external algorithm that we didn't want to discuss that produced the candidate boxes. And therefore, in the next iteration, in the next idea that we need to understand, that underlies what is called faster CNN, very creative naming. We have this line from RCNN to faster CNN to faster RCNN. And faster RCNN, it still counts as two-stage detection, because we still will produce the proposals separately, and then we will score them and match them and everything. But now I will make the proposals by a separate part of the network, the region proposal network, that is inside the architecture. So, again, we don't have time. I won't discuss how this RPN actually works, the region proposal network, how it actually works. But the point is, it works on the same feature map, and it's a separate network that goes with a sliding window over this feature map. The feature map has already lost most of the geometry, so now you can afford to just go with a sliding window. And basically just finds which boxes make sense on the level of this feature map. And it outputs a few top boxes, maybe some hundreds of top boxes, and then the rest is the same. So still we do this region of interest pooling, still we go to the detection head, still we cut out the features, everything else is the same. But now the proposals come from inside the network. And faster R-CNN actually became the standard approach up until Transformers changed everything. It was not in 2017. It was much later after VIT and everything. But for quite a few years, faster R-CNN was like the standard way to do object detection when you have time. So two-stage detection, even if it's all in the same architecture, is pretty slow. And you still have... And it shines if you give it a very smart, very complicated backbone, if you use a good network. So, of course, CNN's progressed, you know, from ResNets, from VGGs to ResNets to EfficientNets, ultimately. And when you see an architecture like this, you can just plug in a different backbone here. You don't have to change anything over here. And you will get a better object detector, okay? So notice how our discussion has shifted from architectures to meta architectures. You have now this global idea of a neural network that extracts features and then does the region proposal and then everything. And the top part, the heads, are more or less fixed. But for the bottom part, you can substitute whatever. And whenever a new feature extractor comes out that works better, you get better object detection for free. That's how it's always worked. Okay. At the same time, I still want to get to transformer-based detection, so I will speed up a little bit. At the same time, there was a separate line of work called one-stage object detection where you do it in one path. And what is the difference? What's the difference between one-stage and two-stage detectors? The difference is, in one-stage detection, you do only one path of the network through the image, and there is no separate stage. I mean, here it's also a part of the network. It's a fine distinction. But here, there is a stage where you have your proposals, then you rank them, you choose the top proposals, and for the top proposals, you do some heavy stuff over here. In one stage of object detection, you just go over all of the possible proposals, which means that maybe there will be fewer of them because you can't go over all possible rectangles inside an image in terms of pixels. That would be too much. That would be like number of pixels squared, completely invisible. But maybe you can go over reasonable candidates for bounding boxes at some level of granularity. And yeah, that is best exemplified by the YOLO family. Let me maybe not discuss the original YOLO. It's kind of irrelevant, although it's quite beautiful in its ideas and the loss function we already discussed. But anyway, maybe not relevant now. And then, oh, all right. Yeah, sorry. Yeah, no, sorry about that. I thought I would have slides about YOLO v2 and YOLO v3 and everything. Yeah, I decided to skip them, but forgot that I took out the slides. So after, so the YOLO family basically, okay, so let me maybe show you this picture anyway. The YOLO family goes like this. You have a single neural architecture that starts with an image, goes over lots of candidates in parallel and outputs the results for all of these candidates and then you can rank them and just take the top however many you need. So there was the original YOLO, then YOLO v2, YOLO 9000 that had a lot of classes and also pretty interesting techniques like the hierarchical softmax. Also a very interesting idea. Unfortunately, we don't have time to discuss it. Then there was YOLO v3 and everything. And basically, as you go through these architectures, the basic architectures change a lot in many small ways. I mean, there is rarely one big idea that you need to actually, that you can just understand. And that's the huge step. So usually, it's like 10 different little tweaks. Every tweak gives you like plus 2% to the accuracy to whatever metric you're using. Also a very interesting discussion of what are the metrics in object detection. But anyway, everyone gives you like plus 1%, plus 2%. And then as a result, when you combine all of them, you get like plus 15% to the result. And that's a huge leap forward. So in a way, it's a lot of small things. But let me mention just one more thing about object detection before we go on to transformers. So what is the main problem of object detection, both classical, both contemporary and whatever, with neural networks, with classical algorithms? The problem is always about detecting small objects. That's always the hardest and sometimes even impossible. So if I have a cat over here, and this cat takes up a quarter of the image, mostly any object detection algorithm, any object detection architecture will recognize it fine. That will be okay. Starting from the original FasterCNN and YOLO v2, it will be fine. But if there is also like a small cat in the distance over here, then we are again at this crucial trade-off, crucial dilemma that we cannot really resolve. And we see it again. We return to the same thing again. We need to fix a level of granularity. So in terms of FasterCNN, you go through your CNN, you extract features, and then at some point you stop, right? And you need to decide at which point do you stop. If you stop too late, it means that you have lost a lot of the geometry. Your feature grid, if you map it back to the original pixels, maybe looks something like this, right? And now this small cat lives completely inside one feature vector and it doesn't even define it entirely. So you are losing this cat. You will never recognize this object that is completely inside one feature vector. It's just this information has been lost along the way to here. On the other hand, if you stop too early, so now, yes, we have a fine grid here and we can recognize this cat, but now it becomes infeasible because everything that happens with this guy over here involves some kind of, you know, going over all of these features with all possible candidates for bounding boxes and stuff like that. So just like you can't do it on the pixels themselves, you probably can't do it on this too fine grid. So this would be great, but it's kind of infeasible. And even if it was feasible, so again, I don't have time to go into details, but you could say, oh, okay, but what if I just look for small objects if I have this fine grid? Well, this you can do. Now it becomes feasible if you don't need to go over like all possible objects on the fine grid, but only on the small one. Then again, this quadratic complexity disappears. And now what you can do is you can do something like multi-stage object detection where you have, let me now draw it vertically, you have your image, you go through the first level, through the first kind of set of layers. This is the first part of the CNN. And here you have still a fine grid, but not very semantically rich. And here you can actually go ahead and do your region proposal network and then get your bounding boxes for the small objects. Then you do another few layers of the CNN and you have a more global set of features. And then you do another part of the CNN and you have the most global set of features. And so you have these three different scales at which you are doing object detection and another different scale like this. So now this guy will detect large objects, this guy medium, and this guy small. And you can basically do it. But notice that it's not that expensive. It's more expensive, of course, but not prohibitively with just one small detail. And the one small detail is that, as I told you in the beginning, when you are recognizing small objects, you really want to have global context. You want to understand what the image is about. It will help a lot. Small objects are really hard to recognize because they only take up a few pixels. And like if I showed you this crop with a few pixels, we humans wouldn't be able to recognize them too. We would need the context of the whole image. So one of the most fruitful ideas after this faster CNN deals was what is called an FPN, feature pyramid network. And the idea of a feature pyramid is to do this path bottom-up to detect large objects, just like I said, but for detecting medium objects to also copy here and fuse somehow features from a more global scale. And then also from here to copy and fuse features for the finer scale. So in this way, you are not increasing your work too much. It's okay, it's just a couple more layers over here for the fusion, that's it. But now you give the network an opportunity to actually capture this global context. So FPN was a very influential idea, still is. And again, we don't have time to go into details, but I could give you a big, big, big survey of what different stuff people did with this idea and with the idea of multi-scale, multi-stage object detection. And in particular, in the CNNs, we talk about the efficient net family of architectures where they would use neural architecture search to search for the most efficient architectures. And here there is a parallel efficient net family of architectures where they actually search for the optimal way to do this. So you fix your backbone for feature extraction to be efficient net, but then you search for the best way to do this post-processing more or less. Because you can do a lot of stuff here. You can go down and then again up and then again down, or you can go skip layers or whatever. It's not that expensive and you are allowed to experiment here. So they experimented and there was also a step forward over here. But anyway, I really need to switch to transformers. So at this point, we've discussed, so to speak, classical object detection. I call it classical here, but it's already deep learning. And usually when people say classical, they mean something before deep learning. Anyway, and then transformers appeared and then the VIT happened. And suddenly there was this question, there was this idea of how can we apply transformers to object detection? And can we make it actually easier? Because everything that I told you, it all makes sense. And it's like a lot of ideas that make logical sense and that work and that constitutes this big field of research for object detection and everything. But what did the transformer teach us, us, the humanity? The transformer taught us that in deep learning and neural architectures, very often, maybe you can get away with just taking one excellent architecture like the transformer and just throwing everything to the transformer and letting it sort it out. Can we use the transformer to sort out object detection? Well, it turns out we can, and it's a very interesting approach, or actually a very interesting family of approaches. So the first idea, the first architecture that started this direction is called DETR, Detection Transformer, and I think Alex will have a practice session on DETR or its neighbors. And basically, what does it do? So, wait a sec. Yeah, I wanted this picture. So what exactly does DETR do? So first, by the way, it still uses a CNN, pretty interestingly. So the Transformer is not used to extract features from the image. The set of image features are extracted by the backbone CNN. But anyway, you use the CNN to extract the features. You add positional encodings as usual, and now you get your inputs to the Transformer encoder, right? So it's a sequence of vectors as usual. And here is the basic idea. The encoder doesn't do detection at all. The encoder just extracts features. It mixes up all of these vectors in some very convoluted way like Transformers usually do. And basically it will train together with the rest to make the features most suitable for object detection. The interesting part happens in the decoder. So this is like a full-scale transformer. It's not BERT or GPT. It's an encoder-decoder architecture. And in the decoder we have, you remember, right? In the transformer decoder you have this encoder-decoder attention where the queries come from the decoder, from the prefix that it already wrote, if it was a language model. And the keys and values come from the encoder part, from the vectors produced by the encoder. Well, here, there is no autoregressive generation, there is a set of what is called object queries. They are just vectors that are trained together with everything else, or maybe even just random vectors that are fixed. And you put them through these decoder layers, with the cross-attention from the encoder also informing them. So the information comes from here, the image comes from here. And then you take every one of the vectors here in the output and you treat it like the input for the detection head. So here you have small feed-forward network, like the usual detection head that does confidence classification and bounding box regression. And the input to this detection head is this transformed object query. So how many objects do I recognize? As many as the object queries. So again, we need to fix this number. This doesn't change. But other than that, notice how it's like this very different, but also very straightforward idea. So a backbone maps the input to features. Then we just flatten the grid here. This set of image features will have a width and a height, but we forget about it. We just convert it to asynchronous vectors. Add positional encodings, of course. And then go through this encoder, decoder, transformer architecture. And an object query is like this placeholder, right? It's like a slot for a possible object. So it kind of, I mean, when you look at how data actually works, object queries tend to kind of like specialize. So you will have an object query that looks like, I don't know, for small objects in the middle of the image or large objects on the left side of the image, something like that. They probably won't specialize in classes, but they will specialize in locations. And of course, most of them will just say no object. They will drive confidence to zero because you need to have a large number of queries, like 100, and in fact, images will have usually much fewer objects. What is also kind of interesting is that in dator, you don't need tricks like non-maximal suppression, because the queries talk to each other. They exchange information in this transformer decoder. And when they exchange information, they kind of specialize again. So there won't be, as the output of dator, there probably, hopefully, won't be a huge number, like two dozen almost identical squares around this seagull. There will be just one square, because the object queries learn to specialize and to not repeat each other. But then again, of course, there are problems here, too. I'm running out of time, but I will mention a few more architectures. One problem is the same that I already mentioned. It's the problem of scale. So as shown here, the data works on a single scale. So you see, I put the CNN through a backbone and I use these features and that's it. There is no way for the rest of this architecture to recover the small objects that got lost in this transition. No, they got lost. So the small objects will probably be not very good. Yeah, so here are examples that are working and you can actually visualize the attention heads, the self-attention that goes on inside the decoder and you can actually see that yes, indeed, object heads, object very specialized objects. And back to the scale problem, the next idea, the next modification was called deformable data, and deformable data is as follows. So first of all, you can run at several different scales. So here this part will be solving the scale problem in the same way as we discussed, by running on different scales, separately for small objects and large objects. But what is most interesting here is that deformable data uses what is called deformable attention. So if you look at what actually data attempts to, where does it spend its attention weights? You will see that the most important pixels are the pixels on object boundaries. So if you look, the decoder attention is localized on the boundaries of the objects. And basically in data, once you have attention like this, you've already separated the objects. And the rest of the job is to just classify them and maybe draw a better bounding box. That's it. But mostly attention already separates the objects, as you see, in different attention heads. So it's a natural idea to try to avoid this quadratic complexity of the transformer, which doesn't let you just work on a small scale, on the fine grid, right? A natural idea would be to avoid it by just looking not on every pixel, not on every feature vector, but looking on a small subset of them. And also, you don't know in advance what the subset will be. So again, I probably don't have time to explain in detail, but the basic idea is this: you have your attention head, and it looks at several other positions on the image, and collects features from these positions of the image. And the locations of these positions are also trained as part of training the whole thing. So yeah, there are some technical difficulties here, I won't go into the details, but basically it works like this. And in this way, you can actually afford to have this multi-scale feature map in the transformer as well. So the problem with this multi-scale approach would be that in the transformer, you need to attend to every other token. And if you have a fine grid, this quadratic complexity will kill you. Well, how do we deal with quadratic complexity? We just reduce, in this case, we reduce our attention to a small subset of the input tokens. Then the next set of ideas here is to work with the object queries themselves. So, again, I said that they tend to specialize. And if you look at however this was produced, I don't have time to explain, but on average, where are the boxes predicted by the object queries? In fact, they do kind of separate all over the input, which is great. But this kind of learning happens very slowly, not really stable. And a good question is, and the next reasonable question is, can we improve this? Because to be honest, this picture doesn't look like it would be difficult to produce just right from the start. Why don't we just take a grid or sample random points and help data produce better object queries? And indeed, the next step, again, I have to wrap up, but I want to mention it. The depth data or dynamic anchor box data, it actually uses anchors, it uses these object queries that are not just abstract vectors that will somehow over hundreds of epochs of training move away and learn to predict different stuff. But they're just bounding boxes. They have the meaning of X, Y, H and W, there are four numbers and that's it. So, when you have this kind of thing, you can actually, first of all, you can initialize them in a smart way so they are kind of separate from the beginning. And then you have this very clear semantics of what's going on between layers and you can actually refine them in a smarter way. I don't have time to explain here. As a result, you get better object queries, better anchors, as they are called, in less time. And yeah, I guess I will have to skip this, I will have to skip this. The best object detectors right now are dyno and their modifications, dyno, dendator and whatever, deformable data and so on and so forth. I left in the big survey on transformer based object detection, but unfortunately we don't have time to discuss them. But yeah, let me stop here. All of these things, all of these different architectures, they share this basic idea of the original data that the queries, the objects, the bounding boxes are queries to a transformer decoder and the transformer decoder will fill them with content according to the image. And then again, there's a big science about it, lots of results, lots of different architectures. Okay, so sorry, I ran a little bit over time, but we only have three lectures left and tomorrow will be something completely different. We'll go to more generative stuff. So any questions? In this case, thank you, I'll make it available and see you tomorrow.
