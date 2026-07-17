# Transcript — google_stt

- **Provider:** google_stt
- **Language:** en-US
- **Audio duration:** 1:40:15
- **Segments:** 740
- **model:** latest_long
- **use_enhanced:** True
- **latency_sec:** 853.92

## Segments

**[00:11 – 00:12]** Okay. Hello everyone.

**[00:13 – 00:15]** And welcome back.

**[00:16 – 00:18]** I'm happy to continue our

**[00:19 – 00:22]** Discussions about declaring.

**[00:23 – 00:29]** And specifically on this last week, we finally turned from something general. I mean,

**[00:31 – 00:42]** it usually, it usually happens every year that we started teaching a course called computerization but actually

**[00:43 – 00:54]** It turns out that you always need to start with something like declaring Basics and the actual computer vision gets bumped to the end of the class. But anyway

**[00:55 – 01:00]** we are here and over the last two weeks, we have discussed

**[01:02 – 01:18]** We have build up, actually why the array of architecture's a set of tools to solve various problems? And finally, we begin to apply them specifically to pictures. Well, we already talked about pictures and the contacts of cnns.

**[01:19 – 01:21]** But we haven't yet.

**[01:22 – 01:42]** Talked about pictures in the context of Transformers. If I understand correctly, Alex already explained to you, the ability the vision, Transformer in practice sessions, so I won't be spending too much time on it and our like main plan for today, our main

**[01:44 – 01:50]** Content will be a specific.

**[01:51 – 02:04]** General but specific problem and computer vision. Specifically object detection and object detection has one of the most interesting problems in computer vision and

**[02:05 – 02:08]** Object detection, as actually.

**[02:11 – 02:15]** one of the hardest in a way, because it's quite

**[02:17 – 02:28]** Unusual. It has an unusual structure of the outputs, compared to say, segmentation which we won't discuss an actress, but maybe Alex will in practice.

**[02:28 – 02:44]** and there's a lot of talk about and also Transformers actually come in very in interestingly and very differently in object detection actually, as you

**[02:45 – 02:51]** as we discussed, I think, usually the Transformer

**[02:52 – 03:17]** just goes in replaces some part of the architecture and served as a better feature extractor, and that's it. And there is nothing like conceptually changing in the architecture. Quite often, for example, in segmentation, if you discuss it with Alex, he will tell you about the unit architecture, which is from, you know, 2015 or something.

**[03:18 – 03:30]** But modern segmentation still uses unit. Only instead of conversational layers inside. It uses some kind of self-attention base layers and of course there's a lot of

**[03:31 – 03:49]** The, there's a lot of new stuff happening, but basically the unit did not get obsolete because the Transformer appeared in object detection. It's a little bit different and we'll see how it works. So anyway,

**[03:50 – 03:57]** If you are, first on Transformers, for pictures Mission Transformers.

**[03:58 – 04:15]** Ah, let me not spend time at all on visual bird. Visual bird was one of the first moralist successful approaches to handling pictures is Transformers. And let me just tell you the setting the problem setting for for visual bird.

**[04:17 – 04:37]** It was for captioning mostly and it worked like this. You've had your text and you had like object queries, like you had tokens that represented specific objects found on the picture.

**[04:38 – 04:42]** So, to use visual bird, you would have to solve for object detection first.

**[04:43 – 04:58]** And then you would plug in this subsets of the image. This rectangles we'll discuss it an object detection. Distracting angles that correspond to specific options on the input image and

**[05:01 – 05:01]** Then.

**[05:05 – 05:07]** Pass them through some.

**[05:08 – 05:14]** Simple embedding layer, get a vector features and then off you go with Transformer.

**[05:14 – 05:15]** and,

**[05:17 – 05:22]** the point of this picture for us is that for the Transformer as you can see here,

**[05:24 – 05:51]** Like it really I won't say it doesn't matter, but it really matters little whether the input came from text or from images or from whatever. As long as it's a sequence of vectors, the Transformer is not, is an architecture that is great. And at finding various, you know, internal correlations between this vectors finding structure inside everything like that.

**[05:52 – 05:54]** So it is no wonder that.

**[05:55 – 06:01]** at some point, people just straightforwardly applied Transformers to

**[06:03 – 06:36]** images. And again, Alex, talk to you about the architecture, I want waste time, but like the most interesting, the most striking feature of the vision, Transformer architecture of the vat is just how simple it is, right? It's, I mean, you don't need to do anything, there is absolutely no change in the Transformer architecture because now the input is an image.

**[06:37 – 07:16]** And in fact, you might think that when you cut a picture into patches, these patches do not really correspond to the Natural. One-dimensional sequence, right? Well, I mean, you fix some sequins but like HSN pages in this sequence will not be necessarily anywhere close on the image right. For example, if you go rolls first, then you put the first three purchase they are indeed neighbors. And then after the third one, you go back to the right to the left part of the image. And these two pages are nowhere near

**[07:18 – 07:36]** So it is tempting to say that. Well an image is not really a sequence, right? And image is a two-dimensional structure. We need some something new something interesting, at least some change in the position and coins that we just discussed last time, right?

**[07:38 – 07:49]** In order to fix the right, we need some change in the positional concerns to tell the Transformer that it is actually.

**[07:51 – 08:23]** That it is actually and a 2G structure, right? Again, it will not care if it's an image or what, it's just a vector of features for the Transformer, but at least the positions should be somehow marked. Well, it turns out no. And in the original vat paper, there's an appendix, where they show that. Oh, yeah, sure. We tried. Lots of several ideas on how to do this position, according to none of them helped. Basically, you just treated as a sequence that's fine.

**[08:24 – 08:27]** Just use standard position on recordings from text Transformers.

**[08:29 – 08:31]** And the it.

**[08:32 – 08:34]** Kind of revolutionized.

**[08:35 – 08:47]** Image processing, revolutionized everything. Oh computer vision and everything else dealing with images because again a Transformer is just better.

**[08:48 – 09:16]** It extracts, better features, more semantically, rich. And you can in many, many applications, you can just say it, take out your convolutional network plugin, the vat, just reuse, the same stuff that you have. On top of this feature extractor, and it will be better. And there were, like, 100s of papers to exactly this after 2020.

**[09:18 – 09:40]** Ah, and there is only one problem. There is only one problem that is hard to solve for Transformers. It's like the main problem, the main computational problem of Transformers, which I mentioned when we discussed the architecture itself, the problem is the vat and then you Transformer has quadratic complexity

**[09:41 – 09:44]** Right? So we discussed that.

**[09:46 – 10:04]** We discussed that in the Transformer there is this Matrix of attention weights, right? And it's a token by token Matrix. So it's a matrix of size L times, L where l,

**[10:05 – 10:06]** Is the input size.

**[10:08 – 10:14]** And the trailer to go around this. So the VA it means that the vht

**[10:14 – 10:17]** Has complexity quadratic.

**[10:18 – 10:26]** In the number of pages, right? So every page becomes a token at the input of the vat,

**[10:28 – 10:32]** So if you have, I don't know, height age and tweets w.

**[10:33 – 10:45]** And let's say you have, I don't know, K times k h, then there will be that many pages.

**[10:47 – 10:53]** Vertically times that many pages for horizontally and this will be square.

**[10:53 – 10:56]** Right? So the size of the great Square.

**[10:58 – 11:23]** And this is a bit problem. It's applications, at least because it means that you cannot really people try it with other architectures, but you cannot really have the VIP go down to the level of individual pixels, right? If you have a million pixels input, oh fell. A million square, this too much, even for Modern Hardware, or whatever.

**[11:24 – 11:28]** So you have to have patches and you have to have relatively big pages.

**[11:29 – 11:34]** and if you have relatively big page, as it means that you can't really

**[11:38 – 11:38]** Means that you can really.

**[11:40 – 11:41]** um,

**[11:44 – 11:46]** figure out the small details of your image.

**[11:47 – 11:51]** so, if you are doing for example, object detection through the vat, whatever, that would mean,

**[11:52 – 12:27]** And you want to find a cat in the same image and if the cat is small, maybe it's far away and it's completely inside one page or even the part of one page or maybe it's on the boundary between two pages and you know, none of them really is dominated by the subject then I guess it will be very hard because every page will get flat and to a single vector and stuff will get lost along this way.

**[12:29 – 12:51]** So so it's really and like that there's really no correct size for the 80s so just like we just asked with the attention mechanisms it, it's either to be in which case you're losing detail or it's too small and which case you just can train it and can run it because it's too heavy.

**[12:52 – 13:03]** Ah, so what people did, there were a lot of approaches. I want to discuss one of them specifically

**[13:04 – 13:04]** The.

**[13:05 – 13:24]** Swin Transformer, the swin Transformer because it's one of the most popular. So today, if you open up some computer vision, application probably will see, either vat or swin, some version of spin or vhts your back.

**[13:26 – 13:31]** And the students Transformer. So the screen stands for shifted windows.

**[13:32 – 13:32]** and,

**[13:33 – 13:36]** Here is the thing. So as I said,

**[13:37 – 13:38]** The.

**[13:42 – 14:21]** A complexity grows as the square of the number of pages, right? So a natural way to say from this would be to break down the image into parts and then cut up the parts into pages, right? So for example, this here I would, let's say do a 2 by 2 grid like this, right? And then I would just take this guy which has only three by three grid and here I would have complexity like nine squared. And here, I will have six squared 6, squared, 9 squared, right? And if you had it all up, it'll be a couple hundred but

**[14:23 – 14:41]** The original complexity was like 25 squared, which, of course, much more, right? So if you, if you have square complexity and you cut up into smaller pieces, your save a lot and it basically, this Square becomes linear because now it's the square. Only in the size of this small part.

**[14:42 – 14:45]** so, it's very natural to have this kind of

**[14:47 – 14:49]** Hierarchical structure.

**[14:50 – 14:50]** where,

**[14:51 – 14:58]** First, if you have a large image of the input first you cut it up into small pieces, relatively small business, like a former for great.

**[14:59 – 15:04]** then you process every every part here with the vat,

**[15:04 – 15:52]** Then you combine them and again you process with another player, Vital Certificate layers. And then, finally, you combine those somehow won't go into details. How, exactly. And process now globally. The whole image also with vit layers, right? So in this case, on this picture, every vit layer, every Transformer layer deals with 16 tokens at the input right? On the 4, by 4 great. But in three steps we go from what from 16 by 16, image to 4 by 4 mesh, wishes and compressed and features, or a single vector, or whatever.

**[15:53 – 15:55]** So that's that's the basic idea.

**[15:56 – 15:59]** And why is it called shifted windows?

**[16:00 – 16:01]** it's called shifted in those, because

**[16:04 – 16:04]** Well.

**[16:05 – 16:21]** There is this problem that we will discuss an object detection too. The problem that when you look inside these small parts of the input image very often,

**[16:22 – 16:33]** It would help you greatly very often, you would be very happy to have a more Global context of what's happening in the image.

**[16:34 – 16:42]** Like, I don't know. You see, I can't draw it but, you know, you see a small part of some kind of

**[16:43 – 16:44]** Surface.

**[16:45 – 17:22]** And on the surface, there is some kind of vehicle, right? And it's small, that's the whole problem. So it's hard to distinguish exactly what this vehicle is. So if, if you know that the context is a highway and it's like a road with cars and it's a car. If you know that the context is, I don't know what Lagoon of oversee, then it's about, right? Two very different classes. You can't really distinguish without Global context and this in this actually happens all the time. It sounds like a contrived example, but actually a global context is necessary quite of

**[17:23 – 17:33]** So you would like these guys down here to have a way to get information about what's happening in the rest of the image.

**[17:34 – 17:43]** And shifted Windows. Does it this way? Very interesting, very cool trick. I think the trick is between self-attention layers,

**[17:44 – 17:45]** You shift the windows?

**[17:46 – 17:46]** so,

**[17:49 – 17:50]** You would have.

**[17:52 – 17:56]** Liked on one layer. I want to draw it a little bit.

**[17:57 – 18:02]** larger than on the example, because the example I think

**[18:02 – 18:07]** the picture from the paper is a little bit misleading, so you have

**[18:08 – 18:10]** A great like this.

**[18:11 – 18:13]** and then, on the next layer,

**[18:14 – 18:16]** you will have a great like this.

**[18:17 – 18:18]** Okay.

**[18:19 – 18:22]** so, it will shift like half of the

**[18:23 – 18:26]** Size of the page of the page.

**[18:27 – 18:27]** and,

**[18:29 – 18:34]** It will still be the same kind of Transformer. It will still have the same.

**[18:36 – 18:36]** Size of input.

**[18:37 – 18:40]** but now it will shift to

**[18:41 – 18:46]** different subsets of features, so like different parts of the image and

**[18:47 – 18:49]** notice that if I do it several times,

**[18:50 – 18:52]** after every layer like this, say, then

**[18:53 – 18:57]** this will expand the receptor field of my pages, so

**[18:58 – 19:09]** If I was sitting over here, right, and I saw this part of the image, then after I go out here and then come back again.

**[19:10 – 19:17]** Now the same Transformer but in two layers up, we already be looking at this part of the image.

**[19:18 – 19:27]** Right, because it has collected actually even more because like this guy will be looking at here. So, okay, so we will be looking at this part of the image. Sorry.

**[19:34 – 19:42]** Because the purple grid has been looking on like this part.

**[19:44 – 19:58]** Right, this, this Square. This, this, this this Transformer has been looking at the orange square. And when you go back, you collect all of this neighboring. Hsnt purple.

**[19:58 – 19:59]** Squares.

**[20:00 – 20:01]** Right. So

**[20:02 – 20:04]** this is how it works.

**[20:06 – 20:06]** and,

**[20:08 – 20:14]** This is how it works. And the like that there is a lot of

**[20:16 – 20:17]** Unclean. And

**[20:20 – 21:20]** Easy to miss Implement stuff about around the edges and this is what this picture shows. Basically, if you shift your grid, the ages will not fit anymore, right? This, this small parts at the near the edge of the image will not be full squares anymore. So what they actually do, they like roll up the image in the Taurus and they say, okay, so now this guy over here is goes together with this guy and this guy over here, the direct angle goes together with this track and they did the small square at the Corner's, also all go together as a single. And so, this doesn't really matter all that much, because it's only about the HS, but so it's a lot of hassle. Once I saw an implementation, I don't think

**[21:20 – 21:29]** Have here. But I saw an implementation of a 3D screen Transformer where you do the same stuff but with like, cubes instead of

**[21:31 – 21:42]** Squares. And it was the most convoluted piece of code I've ever seen. There were like, lots and lots of hard-coded, shifts and constants and it was very difficult to understand.

**[21:44 – 21:44]** So,

**[21:46 – 21:47]** Okay. But anyway.

**[21:48 – 21:49]** So, the screen Transformer.

**[21:50 – 21:57]** Won't discuss. I won't discuss the exact architecture, but the same Transformer and the vat.

**[21:58 – 22:11]** Both can serve as good backbones, right? So what is a backbone? It's a tool, a part of the network, the largest part of part of the network that does feature extraction.

**[22:12 – 22:16]** And what would it do? Feature extraction for

**[22:17 – 22:28]** Well, by default the V8 is trained on something, like classification, you know, your fish are extraction. You see where

**[22:31 – 22:47]** You do a feature extraction, you see where the you, you collect the features into a single Vector at the end and you do your stuff about the reasoning about the image as a whole about.

**[22:49 – 22:50]** ah, but

**[22:51 – 23:21]** what we are discussing today and our main content for today? It's been 20 minutes good. I think we are a little time and what what we are discussing today is a different kind of application, and a different kind of problem that will require us to look inside the image. And to actually map our answers, the specific pixels which is always more difficult, right?

**[23:23 – 23:26]** So I'll skip the perceiver. I don't have time for that.

**[23:27 – 23:28]** so,

**[23:29 – 23:33]** Our main targets, are our main topic for today, is object detection.

**[23:34 – 23:37]** What is object detection? What's what? What's the problem?

**[23:38 – 23:38]** Well.

**[23:40 – 23:47]** Okay, I don't have a slide that's so let me just go to the board. And the first, let me discuss.

**[23:48 – 23:53]** The problem setting because there's a lot to discuss. So my first point was

**[23:54 – 24:01]** Transformers for feature, extraction from images and our second point is what is object detection?

**[24:05 – 24:06]** Um, well.

**[24:07 – 24:18]** What is object detection in Formula? I hope you all kind of have an idea. So there is a big image, like this.

**[24:20 – 24:23]** And there is a cat inside, right?

**[24:24 – 24:32]** And maybe there's not only a cat inside, maybe there is something else. Maybe it's a big thing with a lot of objects.

**[24:33 – 24:33]** so,

**[24:34 – 24:35]** the object detection problem.

**[24:36 – 24:48]** Goes like this, given the same image and give, and let's say the cat class, like, I also should specify what exactly. I'm, I need to find

**[24:50 – 24:51]** find the cat.

**[24:52 – 25:02]** And not only say that there is a cat. Like give me the confidence they probability that there is a kid like usual classification. But also

**[25:03 – 25:05]** To draw a rectangle around the kit.

**[25:07 – 25:20]** To specify exactly where and in terms of this rectangular positions, not down to individual pixels, that would be segmentation. But down to this rectangle, specify where exactly you found this cat,

**[25:21 – 25:24]** So, this rectangle is called the bounding box.

**[25:27 – 25:32]** Usually abbreviated to beatbox in documentation and papers.

**[25:33 – 25:33]** and,

**[25:35 – 25:44]** Then you can have many different classes. Maybe in addition to a cat on the same image, there is a dock somewhere.

**[25:45 – 25:51]** Can I draw a dog? I'm not sure. But at least let me make different years for the look.

**[25:52 – 25:52]** and,

**[25:53 – 25:56]** okay, so that's kind of looks

**[25:57 – 26:26]** and there is a dog and I also want to recognize the dog and I also want to draw a rectangle around the dock and also specifies bounding box and they can they bounding boxes can overlap? Of course, images can be anywhere, they can the objects themselves can can overlap with each other or they can just overlap in the empty parts of the rectangles. Whatever. Anything anything goes. The point is

**[26:26 – 26:28]** for every

**[26:30 – 26:34]** object that I'm looking for. I need to Output.

**[26:36 – 26:41]** Potential output. I need to Output the class label and

**[26:44 – 26:45]** this bounding box.

**[26:46 – 27:08]** So how do you formalize a bounding box? It's a rectangle. You need to specify its coordinates. So usually people do it like this, they have like X and Y for the bottom left corner or any Corner, that's interesting for you. And then the width and the height of directing, right? This rectangle is defined by four numbers.

**[27:10 – 27:12]** and so, here is

**[27:13 – 27:14]** the interesting part now,

**[27:17 – 27:17]** I hope.

**[27:18 – 27:23]** The idea of the problem was clear. I hope it's clear how

**[27:24 – 27:25]** What we are trying to do here?

**[27:26 – 27:38]** But it's becoming less and less clear. How exactly to do it, right? So like, how would they Define the neural network solving object detection?

**[27:40 – 27:49]** Even let's, let's not speak about architectures. Now, whatever, whatever is not work, but what is what what is its input and what is itself?

**[27:50 – 27:53]** Here's input. Obviously, I take the picture.

**[27:54 – 27:56]** I put it into my neural network.

**[27:57 – 27:58]** And now what is the output?

**[28:00 – 28:00]** Well.

**[28:01 – 28:12]** A picture can have multiple objects, right? If I assume that there is only one object, it's called object localization and it's a much easier problem.

**[28:12 – 28:12]** so,

**[28:13 – 28:16]** I need to have a way to Output multiple objects.

**[28:17 – 28:21]** Right. Like object. One, two, three.

**[28:22 – 28:26]** And maybe maybe more, maybe a lot more nose.

**[28:27 – 28:48]** Right then for every object, I need to have its class. So the class label as usual for classification in the form of a probability distribution. So this will be like the Distribution on classes and as an as always in classification.

**[28:50 – 28:58]** And then I need to specify the bounding box. So four numbers x, y w, h and so on for every

**[29:02 – 29:03]** for every

**[29:04 – 29:05]** object.

**[29:08 – 29:10]** And here is the first.

**[29:11 – 29:12]** Tricky part.

**[29:14 – 29:18]** I cannot have a neural network with variable number of outputs.

**[29:19 – 29:19]** Right.

**[29:20 – 29:22]** Kind of doesn't make any sense.

**[29:24 – 29:24]** So,

**[29:26 – 29:31]** I need to fix the number of outputs from my neural network.

**[29:32 – 29:53]** I know how many outputs exactly I have like per object, right? So per option I have the number of classes for their probabilities and then for numbers for the bounding box. So if I know how many objects I have,

**[29:54 – 30:09]** I know how many outputs I want, but I don't know how many options right on a picture. There might be one cat. Okay. Three cats, four, cats, and two dogs forever. I don't know, maybe 100 of objects and I I just don't know it and once,

**[30:10 – 30:11]** so,

**[30:12 – 30:36]** Uh what's what's the the answer to that? How do I solve the problem that I can't really have like an open list at the output of a network? And they can't because the output of a network there should be neurons with weights and I cannot have a variable number of humans because I need to have this number of weights and they need to train them, right?

**[30:37 – 30:38]** so,

**[30:40 – 30:56]** For this question, they are output. The answer is pretty trivial for this question. The answer is well, okay, let's fix some maximum number of options that we want to recognize and let's just have the this menu.

**[30:59 – 31:04]** This makes another question, right? This back's another question.

**[31:05 – 31:17]** Now, what happens? If there are fewer objects, what happens if I'm recognizing 10 different objects? But the picture only has a cat and the dogs. So, like two objects and the rest

**[31:19 – 31:21]** is irrelevant that they're not my classes.

**[31:22 – 31:24]** Well, in this case.

**[31:26 – 31:28]** I need to have a way to specify that, like,

**[31:30 – 31:39]** Some outputs. Don't count, right? I need a way to specify that, okay? So object number one is real object. Number two is real, the rest.

**[31:40 – 31:41]** They are not real.

**[31:43 – 31:51]** And usually it's done. Exactly. Like I said, so usually it's done by inserting by adding another output.

**[31:52 – 31:54]** Which I would call the confidence.

**[31:55 – 32:09]** So for every output you would have something like, okay, here is how sure I am that. There is an object here and it's usually probably right? So from 0 to 1,

**[32:11 – 32:13]** Here is how sure I am the there is an object here.

**[32:14 – 32:14]** and,

**[32:16 – 32:21]** If it is there then here is its cost label. And here is his phone books.

**[32:22 – 32:25]** so if I have only two objects then,

**[32:28 – 32:33]** Sure, if I have on the two objects, then sure.

**[32:35 – 32:44]** AI. I would like the confidence as for this objects to go to one and the confidence is for a lot of objects to go.

**[32:44 – 32:46]** To go to the room.

**[32:57 – 32:57]** So,

**[33:04 – 33:04]** Okay.

**[33:06 – 33:20]** But this is so under the beginning, we still have a lot of unclear things here. We still have a lot of like, interesting questions left.

**[33:21 – 33:21]** so,

**[33:22 – 33:26]** We Define what should be the output of the neural network?

**[33:26 – 33:37]** But this is only the first step and it's intermediate step. What I really want to Define what we really need to Define for the work. It's a lost function, right?

**[33:38 – 33:38]** So,

**[33:41 – 33:43]** What would be a loss function?

**[33:44 – 33:46]** For this kind of output.

**[33:47 – 33:53]** What would be the host? Like I have this picture and I have

**[33:54 – 33:56]** The, the ground truth.

**[33:59 – 34:13]** The ground truth, which are like these two objects, right? So this is like y 1, Y 2 for y1 and I know it's a cat. I know where it is now. It's bounding box for white so I know it's a dog. I know it's bounding box.

**[34:13 – 34:15]** How do I?

**[34:17 – 34:19]** Compare this.

**[34:20 – 34:22]** To the output of the neural network. What should I optimize?

**[34:24 – 34:25]** Well.

**[34:27 – 34:39]** Kind of again, known female. Why not travel because I can't just say, well object. Number one should be this cat object. Number two, should be this box, the token. That's it.

**[34:40 – 34:58]** Because the neural network doesn't and shouldn't have any idea of some kind of ordering of the objects, right? It doesn't make any sense. They don't come ordered. I just want to recognize the objects on the image. I don't know if the cat is number one, and the dog is number two.

**[34:59 – 35:15]** And also if I have confidence is like like here and if I have a big list of possible objects then I don't want to require the neural network to in addition, sort them by confidence or something that would be difficult and completely unnecessary.

**[35:17 – 35:24]** I just want this cat to be somewhere inside in this talk to be somewhere inside and the rest.

**[35:25 – 35:28]** The other outputs to have low conscious.

**[35:29 – 35:29]** Right.

**[35:30 – 35:33]** so, what we actually are looking at

**[35:34 – 35:41]** is we need to find a matching between the ground trolls, the answer and

**[35:42 – 35:45]** The.

**[35:46 – 35:54]** Predictions of the neural network, so it's kind of it's called an assignment problem, right. We need to assign.

**[35:55 – 35:57]** Elements of these two sets to each other.

**[35:58 – 36:09]** I can like pair this with no object to okay. And then I need to assign elements of this sets to each other. The minimize some kind of cost.

**[36:13 – 36:13]** um, and

**[36:15 – 36:25]** okay, here I I suppose he will discuss it in Practical sessions, there will be something like different area and algorithm that actually

**[36:27 – 36:37]** produces this bipartite matching one-to-one matching, between predictions and ground truths in a way that actually assigns

**[36:39 – 36:42]** The ground truth box to the best predictor.

**[36:44 – 36:47]** But that's all not enough, right? So what is

**[36:48 – 36:50]** like, the next

**[36:51 – 36:54]** What is the lowest function then?

**[36:55 – 36:56]** Well.

**[36:58 – 36:59]** The loss function.

**[37:00 – 37:14]** The Lost function. And here I am. I I want to go into full formal details because they can differ, there can be different ideas and different ways and whatever. But

**[37:15 – 37:16]** The loss.

**[37:16 – 37:35]** Is composed of two things, right? The classification was three things. Sorry the confidence was from like if there is an object, the confidence should go to one. If there is not an object, the confidence. Go to 0. That's one part. And that's pretty, right?

**[37:36 – 37:41]** It's like just the lock probably log. Confident minus low confidence or something.

**[37:42 – 37:42]** Then.

**[37:43 – 37:48]** There is the classification loss. So if there is an object,

**[37:48 – 37:58]** let me put it this way like if there is no object then we don't care what the class label says because if there is no object and it's just random stuff,

**[37:59 – 38:06]** If there is an object, then we care and then it's probably just cross entropy.

**[38:07 – 38:11]** Between these two probabilities distributions.

**[38:11 – 38:12]** Right.

**[38:13 – 38:16]** And then there should be.

**[38:17 – 38:28]** The bounding box loss. So these numbers should represent the correct rectangle and of course they won't in practice and

**[38:30 – 38:34]** Again, it only matters if you have an object.

**[38:34 – 38:39]** But if you do have an object, what is the laws for the bounding box?

**[38:42 – 38:54]** You can do it with some straightforward laws like x minus X predicted squared plus so on plus h minus H predicted

**[38:55 – 39:01]** Or not squared, or maybe the same but like absolute values for for an L1 loss or whatever.

**[39:03 – 39:04]** but,

**[39:05 – 39:08]** Problems with this coordinate based losses.

**[39:09 – 39:11]** One, common problem is that?

**[39:13 – 39:21]** you will get a very different contributions into this loss for large objects and for small objects

**[39:22 – 39:23]** so,

**[39:24 – 39:28]** okay, in our example I have two large objects but anyway if I have

**[39:28 – 39:30]** Like this ground truth box.

**[39:32 – 39:33]** For the cap.

**[39:34 – 39:37]** And my predicted box is like this.

**[39:40 – 39:44]** Well, it's pretty good, right? It's pretty good. But we have

**[39:46 – 40:00]** Quite a lot of distance here so I will need to move the bottom left corner down here and then up here and the bits and height and how to draw it. But they also need to be updated to be adjusted.

**[40:02 – 40:10]** And, but if I have a very small object like this, and as we will see a small objects are the most interesting case for object detection. This is what's difficult.

**[40:11 – 40:12]** and then,

**[40:14 – 40:16]** For the same kind of loss.

**[40:16 – 40:17]** My.

**[40:19 – 40:35]** Bounding box will be completely different, right? So here the overlap, a lot when they are large and here for the same loss for the same difference in width height X and Y.

**[40:36 – 40:52]** They will not overlap at all. So not really into it, right? I don't really want these to make identical contributions. I want this to be a bad thing, and this to be an almost perfect thing, right? So,

**[40:55 – 40:56]** how do I fix that?

**[40:56 – 40:58]** Well, the answer is.

**[40:58 – 41:03]** I don't want to get my, I mean, this some

**[41:04 – 41:28]** Some approaches object detection including some of the ones that we will discuss today, say well. All right, what can we do? Let's still use something like that. Like the original yellow uses. I lost function like that and but this is usually people do some kind of a loss based on what is called the intersection of reunion metric.

**[41:29 – 41:31]** So, the IOU of two.

**[41:34 – 41:39]** Two areas on a plane. In this case, two boxes is

**[41:40 – 41:49]** Precisely what it says intersection over unit over Union. The area of their Intex. Intersection divided by the area of their Union.

**[41:50 – 41:56]** So in this case, I take this guy and I divide it by this guy.

**[41:57 – 42:04]** And I get something like, kind of 0.6 0.7 I guess, in this case, which has a pretty good area.

**[42:06 – 42:08]** In this case, I get exactly zero.

**[42:08 – 42:08]** Right.

**[42:09 – 42:11]** so,

**[42:14 – 42:15]** so, this is

**[42:16 – 42:17]** The default.

**[42:19 – 42:25]** Metric for measuring like goodness of match between.

**[42:28 – 42:44]** Bounding boxes and predicted boxes and it only has one more problem. I want to go into more detail formerly but it also, it has on the one problem in that. Now, if the boxes don't overlap,

**[42:44 – 42:47]** The IU, as I said this exactly 0.

**[42:48 – 42:48]** and,

**[42:50 – 43:03]** Notice that the IU is actually differentiable. It's not a piecewise constant, you can pass gradients through it. If you slightly tweak, if you push this

**[43:04 – 43:16]** Bounding box a little bit to some size. You will get a small change in there. So, the gradients makes sense but the gradient stop making sense when the numerator becomes 0.

**[43:17 – 43:17]** Right.

**[43:18 – 43:27]** And this is a bad thing again because I when I look at this to bounding boxes I do want to be able to say that I want to move it here.

**[43:28 – 43:40]** But from the point of view of the view, if I move it in the right direction a little bit, it's no different than if I moved it in the direction a little bit, it will still be 0. And the gradients don't have

**[43:40 – 44:03]** So in effect they are like additional metrics. Something like the general lifestyle. You which I am not even sure I remember correctly. The formula. So I won't try to reproduce it but basically they make use of these Bounty box and they do something like, they involve something like

**[44:06 – 44:16]** What is the percentage of this common bounding box? Not covered by these two boxes? Something like this. So now if you move in the right direction, then

**[44:18 – 44:26]** This joint bounding box shrinks and the percentage becomes larger, so this would be a good thing.

**[44:31 – 44:39]** And I think that's it for the loss function. So we have discussed the main components, the main usual components of the was function

**[44:40 – 44:46]** But there is one more little thing. One more little thing.

**[44:48 – 44:49]** That happens.

**[44:50 – 44:59]** When you apply in your network. So now, I guess, I I talked through everything that happens when you train your own network.

**[45:00 – 45:04]** but what happens when you apply it and notice that so far I haven't said,

**[45:05 – 45:07]** A single word about.

**[45:08 – 45:34]** How it actually works. What's inside in your own network? What, what's going on? I'm just talking about those function. This is pretty common and difficult problems in non-standard problems, the architectures will come and go, but those functions are like a separate option. They don't care what the architecture is. As long as you can pass the gradients through and they deserve separate discussion and they both

**[45:35 – 45:47]** Separately. There is a line of work that tries to optimize the losses and the separate line of work maybe in the same papers but it's completely agitated right? You can optimize them independently.

**[45:48 – 45:51]** And the architecture in the losses.

**[45:52 – 45:54]** So, okay. So

**[45:55 – 46:08]** Finished talking about the losses. But what about the, what about the application? What about the inference of this neural network? What's the problem there?

**[46:09 – 46:09]** Well.

**[46:11 – 46:13]** The there is there are two problems.

**[46:14 – 46:19]** and again, I don't I won't go into too many details but a little bit

**[46:20 – 46:22]** I have to mention.

**[46:23 – 46:27]** So, here is a picture and here is a cat on the specter.

**[46:28 – 46:29]** And the cat.

**[46:30 – 46:30]** Is very happy.

**[46:33 – 46:35]** And I want to recognize this kid.

**[46:35 – 46:36]** Right.

**[46:36 – 46:37]** so,

**[46:40 – 46:40]** Make sure.

**[46:42 – 46:46]** Oh yeah, actually. It concerns the loss function too sorry. But

**[46:47 – 46:57]** Uh yeah, it concerns the training time too. Sorry, we did not quite finish that with the training because here is the thing.

**[46:58 – 47:07]** Yes I can. I can get you the best possible assignment between the ground truth objects and the objects that I project.

**[47:08 – 47:12]** But even after I get the best possible assignment, I still need to decide.

**[47:13 – 47:18]** Which parts, which predictions are actual objects and which predictions don't count.

**[47:19 – 47:22]** so suppose that in this case,

**[47:23 – 47:24]** I get a bounding box like this.

**[47:26 – 47:27]** Right.

**[47:28 – 47:36]** So this bounding box is kind of maybe about this cat. It looks like it's about this kid.

**[47:36 – 47:38]** so, when I look at the bounding box like this,

**[47:39 – 47:40]** I want to say, well,

**[47:41 – 47:42]** Almost right.

**[47:43 – 47:46]** But you need to shift your bounding box over here.

**[47:47 – 47:47]** Right.

**[47:48 – 47:54]** And you need to put the class labels so that it's a cat.

**[47:55 – 48:05]** So in this case, for this gray bounding box, I want to say well I want to make you into into the campground in box.

**[48:08 – 48:13]** It. And then if I have a bounding box like this, for example,

**[48:16 – 48:23]** It also kind of overlaps with the cat, right? But most probably it's about something else.

**[48:24 – 48:32]** And even without looking at the rest of the picture, without looking at its class probabilities, probably, it's not about the cat.

**[48:33 – 48:44]** And probably if it's if there is no ground truth over here, if there are no other objects in here then probably for the light blue box.

**[48:45 – 48:52]** I don't want. So for the gray box, I want to become the cat box and they would want it confidence to go to one.

**[48:53 – 49:28]** For this box. Well, it never had much in common with the cat. I don't want to bring it over here. It's it's it doesn't sound right. I just wanted to go to zero and it's just a serious bounding box and there will always be lots and lots of outputs with where the confidence showed zero because again remember that there are a lot of outputs many boxes like the maximum possible number of objects and then reality there will be like two or three on a given picture and most of the outputs should have confidence go to 0.

**[49:30 – 49:31]** So here too.

**[49:33 – 49:46]** I need to distinguish between these two cases either. I want to count this box for to become the cat or I just want to say okay this is a bad bad box. And let's let's let's just forget about.

**[49:48 – 49:54]** well, again in practice, it's done with an IU threshold, so

**[49:55 – 49:57]** you just,

**[49:58 – 50:15]** pick a number like one half or something and if they overlap is larger than one half, then you count, this output is the ground truth and if they output is less than

**[50:16 – 50:40]** If they overlap is less than you don't. So this is easy but still also need to mention. And finally, I guess I will talk more about this in practice finally. There is this effect that when you have an object like clear object, that's easy to recognize and you run the same image through in your own network.

**[50:41 – 50:59]** Ah, that has a possibility to distinguish those dozens or hundreds of objects, most probably not one, but a lot of them will stick to this kit. So you will have like a bounding Box about this cat like this.

**[51:00 – 51:10]** And you will have another bounding Box about this cat like this. And you will have another bounding Box about this cat like this. And there will be like those of those.

**[51:13 – 51:18]** of course, you don't need to repeat the same object of times, I guess the

**[51:19 – 51:48]** And the standard way to, to cope with it is an algorithm called non maximum suppression, and let me just leave it at that. It doesn't matter for training for training. We just do the best matching and that's it for actual inference. You need to do this on maximal, suppression to pick the best possible bounding box because now, you don't know what the ground truth is. And you need to somehow combine, all of this hypothesis into a single box.

**[51:50 – 52:01]** But overall, that's it for the problem. Satan. Right, so notice that I haven't yet said anything about how to actually solve this problem.

**[52:02 – 52:10]** I haven't said anything about what's inside the neural network and how do we produce all of this wonderful outputs?

**[52:12 – 52:12]** Well.

**[52:13 – 52:16]** let's say a few words about it, so,

**[52:18 – 52:20]** What kind of words, what can we say?

**[52:21 – 52:22]** Well.

**[52:24 – 52:33]** I want, of course go back in history before the learning where we are doing preparing after all. I will go.

**[52:36 – 52:42]** 10 years back to 2014 when there was like this first approach,

**[52:44 – 52:48]** Kind of after Alex net, revolutionized image processing. People tried to

**[52:49 – 52:52]** Apply deep learning everywhere for images. And

**[52:53 – 52:56]** Finally, they go to object detection.

**[52:58 – 53:05]** And the first successful attempt was called rcnn, which stands for region based and then

**[53:06 – 53:19]** And roskear is one of the best known researchers in object detection and here is how his original approach worked a long time ago.

**[53:20 – 53:30]** well, first of all, it used an external algorithm called selective search, I won't go into details to produce candidate bounding boxes,

**[53:31 – 53:35]** so, you put your image through some algorithm

**[53:37 – 53:45]** Some external algorithm and it gives you candidate bounding boxes but the algorithm doesn't know the classes. It doesn't care about the classes.

**[53:46 – 53:50]** It just finds distinctive objects on the photo. That's

**[53:51 – 54:01]** So if you want to recognize cows, it will still get this post over here and the cloud and the ear of a cow and whatever. So it will get 1 0 0.

**[54:06 – 54:17]** So what next then they take every one of these boxes and treat them separately and pass every one of these boxes through in your own network.

**[54:18 – 54:23]** In this case you see an entrance on image net. So this is the backbone.

**[54:24 – 54:25]** And this CNN will tell you.

**[54:26 – 54:28]** Like what class of object it is.

**[54:30 – 54:30]** Sounds.

**[54:31 – 54:32]** Very straightforward.

**[54:34 – 54:34]** Of course.

**[54:35 – 54:38]** This doesn't answer. The most interesting questions.

**[54:38 – 54:39]** so,

**[54:40 – 54:55]** Well, okay. So first a technical remark to actually put a bounding box through a CNN pre-trained an image and that you need to make it Square. The CNN pretrained on image, net expects the 56 by 2:56 square foot.

**[54:56 – 54:56]** so,

**[54:58 – 55:03]** what they actually did was they took this box and actually warped it just, you know,

**[55:04 – 55:09]** Compressed it so that it would it would become Square. Just artificially geometrically compressed.

**[55:10 – 55:22]** And that actually worked. I mean, obviously, for this post over here, it would make it very, very different, right? But still, it was the best solution on the time.

**[55:23 – 55:24]** And then all. So,

**[55:25 – 55:32]** Another problem was that the CNN they the backbone will not tell you.

**[55:33 – 55:35]** Whether there is an object or not.

**[55:36 – 55:42]** Right. I see an entry image, that presumes that there is an object and just classified.

**[55:43 – 55:47]** If you give it some bad bounding box, that's just you know, a sky with some clouds.

**[55:50 – 56:08]** And I don't know if image that has the class Cloud, maybe it does, if it does, then hopefully it will be recognized as a cloud. But if not, it will be just some some distribution of our classes, there's no confidence in the outputs of a classification Network.

**[56:10 – 56:19]** So they actually also had to have a third step here. Another step that takes the outputs of this CNN.

**[56:20 – 56:35]** and modifies them and they and passes them through a completely different model, a model on top of that, that will actually

**[56:36 – 56:42]** Further classify based on this probabilities like whether it's a real object or not, it was very fragile.

**[56:43 – 56:55]** It still was the best approach at the time which shows just how cool declaring case but it was, of course, Very French and it was hopelessly slow.

**[56:57 – 56:58]** Hopelessly slow.

**[57:00 – 57:06]** It, it was like a minute per image on a GPU.

**[57:09 – 57:10]** But all of the ideas.

**[57:11 – 57:18]** Are already in this original version and an architecture. At least all of the ideas of this one of this.

**[57:18 – 57:23]** One approach to object detection. That is called two stage object detection. So

**[57:25 – 57:52]** I actually I used to have like very detailed lectures. An object detection. That would go through those of different architectures. I will not do that with you. We don't have time and they became less relevant as time goes by. So we will jump to Transformers in a little bit, but I do want to discuss their CNN family, because in a way, it's so long.

**[57:53 – 58:11]** And it's still explains in this simple example, let's say explains the main idea. So what are the main ideas in this basic Carson and the main idea is use your backbone to extract features from a specific part.

**[58:12 – 58:12]** Of the input.

**[58:13 – 58:13]** Right.

**[58:14 – 58:15]** and,

**[58:20 – 58:23]** From specific part of the input. And

**[58:31 – 58:44]** sorry. Yeah. And where do this candidate bounding boxes? Come from? Well, in this case they come from an external others from later. We will see they will come from the network itself but still you first

**[58:45 – 58:54]** Get a set of candidates and then you process every candidate through a scene and you extract the features. And then you see what's inside there and

**[58:55 – 59:06]** What you want to do, right? So this is the idea of two stage, two stage object detection. First produce candidate.

**[59:08 – 59:15]** A relatively small set of candidate bounding boxes, then process, everybody knows in the way.

**[59:17 – 59:37]** But of course, processing every bounding box completely independently is again hopelessly slow. So this picture has the real numbers to get like good coverage of the actual objects of the actual bank and boxes. We need to extract like 2000 region, proposals.

**[59:38 – 59:49]** Uh so where do this? 47 seconds? Come from. They come from running the same network. The network is very fast actually but you have to run it like 2000 times.

**[59:50 – 59:53]** And then run a model on top of its results.

**[59:54 – 59:59]** To actually get something, right? So this is of course, hopelessly slow.

**[1:00:00 – 1:00:04]** so the next step in what was called faster CNN,

**[1:00:04 – 1:00:14]** The Next Step was to and this is this is an important idea was to process the whole image on the ones.

**[1:00:16 – 1:00:16]** and then,

**[1:00:20 – 1:00:30]** Extract features from from the feature tensor, take parts of the feature tender are rather than reprocess everything from pixels.

**[1:00:31 – 1:00:34]** Makes perfect sense. Right? So you have this

**[1:00:36 – 1:00:48]** I want wait time on trying to redraw this on the board. Let me just talk. Talk through the slide. So you have this long convolutional Network, or Transformer Network or whatever and

**[1:00:49 – 1:00:53]** keynote Transformers don't work like that, but if you have this long convolutional Network,

**[1:00:53 – 1:00:58]** and as we go through the convolutional network as we discussed,

**[1:00:59 – 1:01:01]** You gradually lose the geometry.

**[1:01:02 – 1:01:09]** And if you want to keep some of the geometry, stop it a bit earlier. We did this in attention mechanism for attention mechanisms before

**[1:01:10 – 1:01:12]** So, the same idea here.

**[1:01:14 – 1:01:16]** You pass your big picture.

**[1:01:17 – 1:01:19]** Through the CNN, on only ones.

**[1:01:20 – 1:01:20]** You get.

**[1:01:22 – 1:01:28]** But in, but you stop a little bit short of the goal. So you get this feature tensor that still has geometry.

**[1:01:29 – 1:01:38]** Then you take your candidate bounding boxes and faster and they're still produced by an external tool and external algorithm.

**[1:01:40 – 1:01:42]** this bounding boxes, and

**[1:01:46 – 1:01:47]** when you have,

**[1:01:48 – 1:01:50]** Some geometry on the feature tensor.

**[1:01:51 – 1:02:12]** It's not a problem to find out like which features correspond to which pixels of the original image. You just have this correspondence. So when you have a bounding box you can project. That's called Rory, projection region of Interest projection row, Roi is a very common abbreviation and object detection, it stands for each of Interest.

**[1:02:12 – 1:02:22]** Um you have this Roi projection, it's not a trainable thing. It's just which features look at these pixels. And now you have

**[1:02:23 – 1:02:30]** The same bounding box, only rougher and inside the feature tensor, okay?

**[1:02:30 – 1:02:33]** and then you take this mounting box and you put it through

**[1:02:36 – 1:02:37]** an object detection head.

**[1:02:38 – 1:02:54]** An object detection head that has basically a classifier for the classes and the bounding box regressor for the bounding box itself. So I didn't mention it before, let me mention it here, usually even even if you have

**[1:02:56 – 1:02:57]** Candidates already.

**[1:02:58 – 1:03:07]** in terms of pixels like here, you still want to have a bounding box regression at the output because maybe the network will

**[1:03:09 – 1:03:26]** Want to shift this bounding box a little bit, maybe and it will be useful. So the network might decide. Oh. Okay. So this is about can't but I need to shift it, a few pics of the left. And yeah, that actually happens and you can train it because you have the brown truth. So it's a good thing, the bound box regression is always here.

**[1:03:28 – 1:03:32]** A one detail about this.

**[1:03:32 – 1:03:37]** Is that? Okay, so now I run the big convolutional Network only once

**[1:03:38 – 1:03:50]** And for every bounding box I actually run. Only this small head I want to say classification head no small detection head with a classifier and regression.

**[1:03:51 – 1:03:54]** So this is already like orders of magnitude faster.

**[1:03:55 – 1:03:56]** One, technical problem, is that?

**[1:03:57 – 1:03:57]** Again.

**[1:03:58 – 1:04:04]** I don't know. I I need somehow to fix the size.

**[1:04:05 – 1:04:08]** Of the input for this guy here.

**[1:04:09 – 1:04:09]** So,

**[1:04:10 – 1:04:13]** my bounding boxes will come in different sizes.

**[1:04:14 – 1:04:19]** And they will map to parts of the feature tensor of different size, too.

**[1:04:20 – 1:04:25]** And I need the input to this head. It actually had to be always the same.

**[1:04:26 – 1:04:27]** What do I do?

**[1:04:28 – 1:04:32]** Well, I insert what is called tradition of Interest pulling Claire

**[1:04:33 – 1:04:43]** and also a pretty straightforward idea, but pretty cool. Let me draw it over here.

**[1:04:44 – 1:04:46]** Straightforward. But cool idea.

**[1:04:47 – 1:04:52]** I have, let's say this is the feature tensor, right?

**[1:04:52 – 1:04:57]** And I have a bounding box. In the feature to enter that goes, let's say like this.

**[1:04:59 – 1:05:07]** So it's a three by five five by three tensor.

**[1:05:09 – 1:05:17]** Don't care what the depth is. I will not cut the depth but it's three by five and my detection had

**[1:05:20 – 1:05:22]** once to have as input,

**[1:05:23 – 1:05:26]** A 2 by 2 tensor. Let's say.

**[1:05:27 – 1:05:28]** So what do I do?

**[1:05:29 – 1:05:34]** I do pouring, but I do like falling not with a fixed.

**[1:05:35 – 1:05:39]** Windows size but pulling with the fixed output size,

**[1:05:40 – 1:05:51]** So in this case, I will see. I know that I expect my output to be two by two and I will just cut it up as evenly as possible to

**[1:05:52 – 1:06:16]** To read the to have two by two windows. So of course it will not be exact because these are integer numbers but as close as possible and then I will pull the features in this for Windows, okay? So this, this is called region of Interest pulling. That's I guess

**[1:06:18 – 1:06:24]** the one cool idea that I wanted to mention for faster and

**[1:06:27 – 1:06:33]** not just for fastest RC and it will be used everywhere, starting from faster and

**[1:06:34 – 1:06:35]** so,

**[1:06:38 – 1:06:41]** So, this was already orders of magnitude faster.

**[1:06:42 – 1:06:42]** and,

**[1:06:45 – 1:06:50]** The remaining bottleneck. Now the slowest part of this pipeline.

**[1:06:51 – 1:06:53]** Was not in the network at all.

**[1:06:54 – 1:07:01]** now, the slowest part was actually this external Elder in the, we didn't want to discuss that produced the

**[1:07:02 – 1:07:04]** Candidate boxes.

**[1:07:05 – 1:07:06]** Okay.

**[1:07:07 – 1:07:08]** and,

**[1:07:13 – 1:07:13]** therefore,

**[1:07:14 – 1:07:28]** In the next iteration in the next idea that we need to to understand that underlies. What is called faster rcnn, very creative naming. We have this line from Arson, and to faster and to faster and

**[1:07:32 – 1:07:34]** Faster. CNN.

**[1:07:35 – 1:07:41]** It's still counts as two stage detection because we still will produce the proposal separately.

**[1:07:43 – 1:07:46]** And then we will score them and match them and everything.

**[1:07:46 – 1:07:48]** But now,

**[1:07:51 – 1:07:53]** I will make the proposals.

**[1:07:54 – 1:08:00]** By a separate part of the network, the region proposal Network that is inside the architecture.

**[1:08:01 – 1:08:13]** So again, we don't have time. I want discuss how this RPM actually works. The region proposal Network, how it actually works, but the point is it works on the same feature map.

**[1:08:14 – 1:08:20]** And it's a separate Network that goes with a sliding window over this feature map.

**[1:08:20 – 1:08:34]** The feature map map has already lost most of the geometry. So now you can afford to just go with the sliding window and basically just find which boxes make sense on the level of this feature map.

**[1:08:34 – 1:08:36]** And it outputs.

**[1:08:37 – 1:08:40]** A few top boxes, maybe some hundreds of top boxes.

**[1:08:42 – 1:08:53]** And then the rest is the same. So still with this creation of Interest, pulling still, we go to the detection, head still be cut out the features, everything else is the same, but now the proposals come from inside the network.

**[1:08:54 – 1:08:56]** And faster. And then actually,

**[1:08:58 – 1:09:06]** Became like the standard approach up until Transformers change everything but it's not in 2017. It was much later after the 18th and everything, but

**[1:09:08 – 1:09:16]** For quite a few years faster and was like the standard way to do object detection when you have time.

**[1:09:17 – 1:09:23]** So two stage detection, even if it's all in the same Market lecture is preacher slow.

**[1:09:24 – 1:09:24]** and,

**[1:09:27 – 1:09:38]** You still have and like it shines, if you give it a very smart, very complicated backbone. If you use a good Network,

**[1:09:39 – 1:09:41]** so, of course,

**[1:09:42 – 1:09:53]** CNN's progress, you know, from resnet from from VHS, to resnet to efficient Nets, ultimately. And when you see an architectural like this,

**[1:09:54 – 1:09:54]** you can just,

**[1:09:56 – 1:10:30]** Plug in a different backbone here. You don't have to change anything over here, and you will get a better object detector, okay? So notice how how our discussion has shifted from like architectures, too Meta, Meta, architectures. You have now, this Global idea of a new Roman networks, that extracts features. And then that's the region proposal and everything. And the top part, the heads are more or less fixed but for the bottom part you can substitute whatever.

**[1:10:31 – 1:10:32]** and,

**[1:10:34 – 1:10:44]** They are like whenever a new feature extractor, comes out that works better. You get better option of detection for free. Let's that's how it's always worked.

**[1:10:46 – 1:10:48]** Okay, at the same time.

**[1:10:49 – 1:10:55]** I still want to get the Transformer based detection so I will speed up a little bit at the same time.

**[1:10:56 – 1:11:04]** There was a separate line of work called one stage object detection, where you do it in one pass.

**[1:11:05 – 1:11:15]** And what is the difference? What's the difference between one stage in two stage detectors? The difference is, in one stage detection, you go,

**[1:11:16 – 1:11:32]** You don't only want pass of the network through the image and there is no like separate stage. I mean here, it's also a part of the network. It's, it's a fine distinction. But Here There is a stage where you like have your proposals

**[1:11:33 – 1:11:41]** Then you rank them. You choose the top proposals. And for the top proposals, you do some heavy stuff over here.

**[1:11:43 – 1:11:46]** In one stage object detection, you just go over.

**[1:11:47 – 1:12:07]** All of the possible proposals, which means that maybe they will not be, maybe there will be fewer of them, because you can't go over possible. Rectangles inside an image. In terms of pixels, bit too much, that would be like number of pixels squared completely invisible.

**[1:12:09 – 1:12:12]** It. But maybe you can go over like

**[1:12:13 – 1:12:17]** reasonable candidates for bounding boxes at some level of granularity.

**[1:12:18 – 1:12:42]** And yeah, that's what that is. Best exemplified by the YOLO family. Let Me Maybe not discuss the original yellow, it's kind of irrelevant. Although it's it's it's it's quite beautiful and its ideas and those function already discussed. But anyway, maybe not relevant. Now.

**[1:12:45 – 1:12:48]** And then oh, all right. Yeah sorry.

**[1:12:50 – 1:13:02]** Yeah. So sorry about that. I thought I would have flights about the only two and he'll be three and everything. Yeah I decided to skip them but forgot that I took out the lights.

**[1:13:02 – 1:13:03]** so,

**[1:13:04 – 1:13:19]** After so the yo family basically okay so let me show you okay this picture anyway the yellow family goes like this. You have a single neural architecture that starts with the image.

**[1:13:20 – 1:13:23]** It goes over. Lots of candidates in parallel.

**[1:13:24 – 1:13:26]** and outputs the

**[1:13:29 – 1:13:36]** results for all of these candidates and then you can rank them and just take the top however many unit.

**[1:13:37 – 1:13:46]** So there was the original yellow and yellow V2. YOLO 9000 that had a lot of classes. And also pretty interesting techniques, like,

**[1:13:47 – 1:13:50]** techniques, like the

**[1:13:51 – 1:14:01]** Hierarchical softmax also very interesting idea and for you don't have time to discuss it. Then there was able to be three and everything and

**[1:14:03 – 1:14:08]** basically, like as you go through this architectures,

**[1:14:12 – 1:14:14]** The basic architectures. Change a lot.

**[1:14:16 – 1:14:24]** in many small ways and I mean, there is rarely one big idea that you need to actually

**[1:14:27 – 1:14:59]** Ah, that you can just understand. And that that's the huge step. So usually, it's like 10 different little tweaks, every tweak gives you like plus 2% to the accuracy to whatever metric you're using. Also a very interesting discussion, what are the metrics of an object detection? But anyway, everyone gives you like plus plus 1% plus 2%. And then as a result, when you combine all of them, you get like plus 15% to the result and that's a huge leap forward. So in a way, it's a lot of small things.

**[1:15:00 – 1:15:06]** But let me mention just one more thing about object detection, before we go on to Transformers.

**[1:15:07 – 1:15:07]** So,

**[1:15:10 – 1:15:21]** What is the main problem of object detection? Both classical both contemporary, and whatever in with neural networks, with classical replacement.

**[1:15:22 – 1:15:39]** The problem is always about detecting small objects, that's like, always the hardest and sometimes, even impossible. So if I have like a cat over here and this can't take up like a quarter of the image.

**[1:15:41 – 1:15:55]** Mostly any object detection algorithm or any object detection architecture will recognize it fine, that, that will be. Okay, starting from 1905, the original faster, CNN, and yolov2, it will be fine.

**[1:15:56 – 1:16:00]** But if there is also like a small cat in the distance over here,

**[1:16:01 – 1:16:03]** then we are again.

**[1:16:04 – 1:16:30]** This crucial trade of crucial dilemma that we cannot really resolve and we see it again, we return to the same thing. Again, we need to to fix a level of granularity. So in terms of faster and you go through your CNN, you extract features, and then, at some point, you stop.

**[1:16:31 – 1:16:35]** Right? And you need to decide at which point do you stop?

**[1:16:37 – 1:16:48]** If you stop to late, it means that you have lost a lot of the geometry, your feature grid. If you map it back to the original pixels, maybe looks something like this.

**[1:16:49 – 1:16:59]** Right? And now this small kit leaves completely inside one feature vector, and it doesn't even Define entirely. So,

**[1:17:00 – 1:17:11]** You are losing this cat, you will never recognize this object that is completely inside. One feature Vector, it's just this information has been lost along the way to here.

**[1:17:12 – 1:17:16]** on the other hand, if you stop too early,

**[1:17:18 – 1:17:49]** So now yes we can we have a fine grid here and we can recognize this cat but now it becomes infeasible because everything that happens with this guy over here, involves some kind of, you know, going over all of this features with all possible candidates for bounding boxes and stuff like that. So just like you can do it on the pixels and sales you probably can't do it on this two fine grid so this would be great but it's kind of invisible.

**[1:17:51 – 1:18:03]** And if it was feasible, so again, I don't have time to go into details but you could say, oh, okay. But what if I just look for small objects if I have this fine, right?

**[1:18:05 – 1:18:15]** Well this, you can do it becomes feasible. If you don't need to go over like all possible objects on the fine but only on the small one. Then again this quadratic complexity disappears.

**[1:18:16 – 1:18:21]** And now, what you can do is you can do something like multi-stage.

**[1:18:23 – 1:18:24]** Object detection.

**[1:18:25 – 1:18:29]** Where you have let me now. Draw it vertically. You have your image.

**[1:18:30 – 1:18:36]** you go through the first level through the first kind of

**[1:18:38 – 1:18:49]** set of layers. This is the first part of the scene and and here, you have still a fine grid but not very semantically rich.

**[1:18:50 – 1:19:00]** And here you can actually go ahead and do your region proposal on that work and then get your bounding boxes.

**[1:19:00 – 1:19:02]** For the smaller objects, right?

**[1:19:04 – 1:19:06]** Then you do another.

**[1:19:08 – 1:19:13]** Few layers of the CNN and you have like more Global set of features.

**[1:19:14 – 1:19:22]** And then you do another part of the CNN and you have the most Global set of features and so you have like this three different, okay?

**[1:19:23 – 1:19:25]** I have like this 3 different scale.

**[1:19:26 – 1:19:27]** at which

**[1:19:28 – 1:19:29]** you are doing object detection.

**[1:19:31 – 1:19:42]** And another different scale like this. So now this guy will detect large objects. This guy medium and these guys small

**[1:19:43 – 1:20:00]** and you can basically do it. But and notice that it's not that expensive, it's more expensive, of course but not prohibitively with just one small detail and the one small detail is that

**[1:20:03 – 1:20:05]** as I told you in the beginning.

**[1:20:06 – 1:20:17]** When you are recognizing small objects, you really want to have Global contacts. You want to understand what the image is about. It will help a lot smaller objects are really hard to recognize because the only

**[1:20:18 – 1:20:28]** Take up a few pixels. And like, if I showed you this crop with a few pixels, we humans wouldn't be able to recognize them too. We would need the contacts of the Holy

**[1:20:30 – 1:20:30]** so,

**[1:20:31 – 1:20:37]** One of the most, fruitful ideas after this faster. And, you know, was

**[1:20:38 – 1:20:42]** What is called an fpn feature pyramid Network.

**[1:20:45 – 1:20:48]** and the idea of a feature pyramid is,

**[1:20:49 – 1:21:00]** to do this past bottom up to detect large objects, just like I said, but for detecting medium objects to also

**[1:21:00 – 1:21:03]** Copy here and view somehow.

**[1:21:06 – 1:21:08]** Features from a more global scale.

**[1:21:10 – 1:21:17]** And then also from here, to copy and fuse features for the finer scale.

**[1:21:18 – 1:21:28]** So in this way, you are not increasing your work too much. It's okay. It's just a couple more layers over here for the fusion, that's it.

**[1:21:29 – 1:21:36]** But now you give the network an opportunity to actually capture this Global context.

**[1:21:37 – 1:21:41]** So, fpn was a very influential idea. Still is

**[1:21:42 – 1:21:58]** And again, we don't have time to go into details, but I could give you a big, big, big survey of what different stuff people did with this idea. And with the idea of multi-scale, multi-stage, option detection,

**[1:21:59 – 1:22:22]** And then particular in the CNN's, we talk about the efficient net family of architectures where they would use, neural architecture search to search for the most efficient architectures. And here, there is a parallel efficient debt.

**[1:22:22 – 1:22:30]** Family of architectures where they actually searched for the optimal way to do this.

**[1:22:30 – 1:22:36]** so like you still you fix your backbone for feature extraction to be efficient at

**[1:22:37 – 1:23:07]** but then you search for the best way to like do this post-processing more or less because you can do a lot of stuff here. You can go down and then again up and then again down or you can go skip layers or whatever. It's it's not that expensive and you are allowed to experiment here so they experimented and there was also a step forward over here. But anyway, I really need to switch to Transformers so at this point

**[1:23:08 – 1:23:09]** We've discussed.

**[1:23:11 – 1:23:12]** So to speak.

**[1:23:13 – 1:23:20]** Classical object detection. I call it classical here but you know, it's

**[1:23:23 – 1:23:31]** It's already deployed and usually when people say classical, they mean something before the learning. Well, you know, anyway.

**[1:23:34 – 1:23:38]** and then Transformers appeared and then the VIP happened

**[1:23:39 – 1:23:42]** And suddenly, there was this question. There was this idea.

**[1:23:44 – 1:23:44]** Of how?

**[1:23:46 – 1:23:48]** Can be applied Transformers to object detection.

**[1:23:49 – 1:23:55]** And can we make a text actually easier because everything that I told you,

**[1:23:56 – 1:24:00]** it all makes sense and that's like a lot of ideas that

**[1:24:02 – 1:24:11]** Make logical sense and that work. And that constitute, this big field of research for object detection and everything.

**[1:24:13 – 1:24:13]** but,

**[1:24:14 – 1:24:16]** What did the Transformer teach us?

**[1:24:17 – 1:24:18]** As the humanity.

**[1:24:19 – 1:24:38]** The Transformer, what was that in deep learning canola architectures? Very often, maybe you can get away with just taking one. Excellent architectural at the Transformer and just throwing everything to, to the Transformer and plating at sorted out.

**[1:24:39 – 1:24:42]** Can we use the Transformer to sort out object detection?

**[1:24:44 – 1:24:50]** Well, it turns out we can and it's a very interesting approach or actually a very interesting family of approaches

**[1:24:51 – 1:24:53]** so, the first

**[1:24:54 – 1:25:12]** The first idea, the first architecture that starts at this direction is called debtor detection, Transformer, and I think Alex will have a practice session on that or its neighbors.

**[1:25:13 – 1:25:15]** And basically,

**[1:25:17 – 1:25:18]** what what does it do?

**[1:25:20 – 1:25:20]** so,

**[1:25:23 – 1:25:26]** Quite yeah.

**[1:25:26 – 1:25:28]** This, I wanted this picture.

**[1:25:29 – 1:25:31]** So what what exactly does that do?

**[1:25:32 – 1:25:36]** So first, by the way, it still uses a CNN.

**[1:25:37 – 1:25:42]** Pretty interesting. So the Transformer is not used to extract features from the from the image.

**[1:25:43 – 1:25:52]** They set the famous fish are extracted by the backbone. And anyway, he used the CNN to extract the features. You had positional coordinates as usual.

**[1:25:53 – 1:26:01]** And now you get your inputs to the Transformer encoder, right? So it's a sequence of vectors 0.

**[1:26:02 – 1:26:08]** And here is the basic idea. The encoder doesn't do detection at all.

**[1:26:09 – 1:26:15]** the encoder just extracts, features it you know, mixes up all of this vectors

**[1:26:17 – 1:26:31]** In some very convoluted way like Transformers usually do and basically it will train together with the rest to make the features. Most suitable for object detection.

**[1:26:32 – 1:26:43]** The interesting part happens in the D quarter, so this is like a full-scale Transformer. It's not Birthright GPT, it's an encoder, decoder architecture. And in the D quarter,

**[1:26:46 – 1:27:09]** we have you remember, right? And the Transformer decoder you have this encoder decoder attention where the query is come from the decoder from the prefix that it already rolled in if it was a language model and the keys and values come from the other part, from from, from the vectors produced by the encoder.

**[1:27:10 – 1:27:11]** Well here.

**[1:27:12 – 1:27:27]** There is no autoregressive generation. There is a set of what is called object queries. They are just vectors that are trained together with everything else or maybe even just random vectors that are fixed. And

**[1:27:28 – 1:27:28]** Then.

**[1:27:30 – 1:27:33]** You put them through this decoding decoder layers.

**[1:27:35 – 1:27:36]** with the

**[1:27:37 – 1:27:41]** Cross attention from the encoder also.

**[1:27:43 – 1:27:47]** Like informing them. So they the information comes from here. The image comes from here.

**[1:27:48 – 1:27:50]** and then,

**[1:27:51 – 1:27:59]** You take every one of the vectors here in the output and you treated like the input for the plate for the detection help.

**[1:28:00 – 1:28:11]** So here you have like small feet forward Network. Like the usual detection had that does confidence specification and bounding box regression.

**[1:28:12 – 1:28:13]** and,

**[1:28:14 – 1:28:20]** The input to this textual head is this transformed object query.

**[1:28:21 – 1:28:26]** So, how many objects do I recognize? As many as the object queries?

**[1:28:27 – 1:28:30]** So again, we need to fix this number, this doesn't change.

**[1:28:31 – 1:28:34]** But other than that, no, just how it's like this. Very

**[1:28:36 – 1:28:40]** Different but also very straightforward idea.

**[1:28:42 – 1:28:58]** So a backbone Maps, the input, the features, then we just flatten the grid here. This set of image features will have within the height, but we forget about it we just put converted to a single vectors.

**[1:28:58 – 1:29:06]** At positioning, of course and then go through this encoder decoder, Transformer architecture.

**[1:29:08 – 1:29:08]** and,

**[1:29:09 – 1:29:10]** An object query.

**[1:29:13 – 1:29:13]** Is.

**[1:29:14 – 1:29:19]** Like this placeholder, right? It's like a slot for a possible object.

**[1:29:20 – 1:29:27]** so it kind of I mean, when you look at how that are actually works

**[1:29:28 – 1:29:48]** Object queries tend to kind of like specialized so you will have an object. Where is that looks? Like I don't know for small objects in the middle of the image or large show objects on the left side of the image, something like that. They probably won't specialize in classes, but they will specialize in locations.

**[1:29:49 – 1:29:56]** And yeah, and of course, most of them will just say No Object. They will drive confidence to zero because

**[1:29:57 – 1:30:06]** You need to have a large number of queries, like 100. And in fact, images will have usually much fewer objects.

**[1:30:08 – 1:30:08]** so,

**[1:30:11 – 1:30:12]** What is also kind of interesting?

**[1:30:14 – 1:30:18]** What is also kind of interesting is that in better?

**[1:30:19 – 1:30:20]** You don't need.

**[1:30:21 – 1:30:23]** Tricks like non maximum suppression.

**[1:30:24 – 1:30:25]** Because the Aquarius.

**[1:30:26 – 1:30:36]** Talk to each other. They exchange information in this Transformer decoder. And when they exchange information, they

**[1:30:37 – 1:30:37]** kind of,

**[1:30:40 – 1:30:49]** This specialized again. So there are won't be as the output of that they're probably hopefully won't be.

**[1:30:50 – 1:31:04]** A huge number, but to those and almost identical squares around the seagull. There will be just one square because they object various learned to specialize in to not repeat each other.

**[1:31:06 – 1:31:10]** um, but then again, of course there are

**[1:31:12 – 1:31:23]** There are problems here too. I'm running out of time, but I will mention a few more architectures. One problem is the same that I already mentioned, it's the problem of scale.

**[1:31:24 – 1:31:29]** so, as shown here, the data

**[1:31:31 – 1:31:50]** Works on a single scale so you see. I put the CNN through a backbone and I used this features and that's it. There is no way for the rest of this architecture to like recover the small options that got lost in this transition. No, they got lost.

**[1:31:52 – 1:31:54]** so, the smaller objects will probably be

**[1:31:55 – 1:31:56]** Not very good.

**[1:32:00 – 1:32:01]** Yeah.

**[1:32:02 – 1:32:15]** Go. Okay. Oh yeah. Here are examples of that work in. You, you can actually visualize the attention heads, the self-attention that those inside.

**[1:32:17 – 1:32:27]** ah that that goes on inside the decoder and you can actually see that yes indeed object had specialized object, very specialized objects

**[1:32:30 – 1:32:40]** Yeah, so and back to to the scale problem. The next idea that the next modification was called deformable debtor.

**[1:32:40 – 1:32:42]** And the formidable data.

**[1:32:43 – 1:32:44]** Is as follows.

**[1:32:45 – 1:33:05]** So, first of all, you can run at several different scales. So here this is, this part will will be solving the scale problem in the same way as we discussed by riding on different scales on different like separately for small objects and barish objects.

**[1:33:06 – 1:33:08]** But what is?

**[1:33:09 – 1:33:14]** Like even most like what is most interesting here.

**[1:33:16 – 1:33:16]** Is that?

**[1:33:19 – 1:33:22]** The formal letter uses, what is called deformable attention.

**[1:33:24 – 1:33:36]** so, if you look at what actually that are attend to, what is what where where does it spend its attention weights,

**[1:33:37 – 1:33:38]** You will see that.

**[1:33:40 – 1:33:54]** The most important object, the pixels are the pixels and object boundaries. So if you look the decoder attention is localized on the boundaries of of the objects.

**[1:33:55 – 1:34:16]** And basically in that, ER, once you have a tension like this you've already separated the objects and you now already kind of the rest of the job is to just classify it and maybe draw a better bounding box that's it but mostly attention. Radio separates the objectives. You see in different attention heads.

**[1:34:17 – 1:34:19]** So it's a natural idea.

**[1:34:20 – 1:34:31]** To try to avoid this quadratic complexity of the Transformer, which does not let you just work on on small scale on the fine. Great, right.

**[1:34:33 – 1:34:50]** A natural idea would be to avoid it by just looking, not on every pixel, not on every feature Vector, but looking on small subset of them and also like, you don't know in advance what the subset will be.

**[1:34:51 – 1:35:04]** so again, I probably don't have time to explain in detail, but the basic idea is this like you have your attention head and it looks at

**[1:35:06 – 1:35:07]** several other tokens.

**[1:35:09 – 1:35:24]** At several other position, not actually, not tokens, but positions on the image and collects features from this position of the image, and the locations of this positions are also trained as part of training the whole thing.

**[1:35:24 – 1:35:31]** So yeah, that there are some technical difficulties here. I won't go into the details but basically it works like this.

**[1:35:32 – 1:35:33]** and,

**[1:35:36 – 1:35:36]** In this way.

**[1:35:37 – 1:35:39]** You can actually afford.

**[1:35:40 – 1:35:43]** To have the smallest scale feature map in the Transformer as well.

**[1:35:44 – 1:35:49]** So, the problem with the small scale approach would be the Transformer.

**[1:35:52 – 1:36:04]** You need to attend to every other token and if you have a fine grid, this could create a complexity will kill you. Well, how do we deal with complexity? Which is reduced, in this case, produce our attention,

**[1:36:05 – 1:36:09]** To a small subset of the input tokens.

**[1:36:11 – 1:36:12]** Then.

**[1:36:14 – 1:36:16]** The next set of ideas here.

**[1:36:16 – 1:36:20]** Is to work with the object various themselves.

**[1:36:21 – 1:36:21]** So,

**[1:36:24 – 1:36:40]** Again, I said that they tend to specialize and if you look at what however, this was produced and have time to explain but like this on average, where are the box is predicted by the object queries? They in fact, they do kind of

**[1:36:42 – 1:36:45]** Separate all over the input, which is which is great.

**[1:36:47 – 1:36:47]** but,

**[1:36:49 – 1:36:50]** this kind of

**[1:36:50 – 1:36:52]** learning happens, very slowly.

**[1:36:53 – 1:36:54]** Not really stable.

**[1:36:55 – 1:36:55]** and,

**[1:36:56 – 1:37:04]** A good question is and the next question, the next reasonable. Question is like, can we improve this? Because to be honest

**[1:37:04 – 1:37:06]** This picture does not look like.

**[1:37:08 – 1:37:22]** It would be difficult to produce just right from the start. Why don't we just take a great or sample random points and help better produce better object queries

**[1:37:23 – 1:37:24]** And indeed.

**[1:37:24 – 1:37:39]** The Next Step. Again, I have to wrap up but I want to mention it. Debt or dynamic Anchor Box, that are it actually uses anchors. It uses this object queries that are not just

**[1:37:40 – 1:37:48]** abstract vectors that will somehow over 100 of epochs of training move away and learn to

**[1:37:48 – 1:37:53]** predict different stuff, but they're just Bounty boxes.

**[1:37:53 – 1:37:58]** They have the meaning of x y, h and W therefore numbers. And that's

**[1:37:59 – 1:37:59]** so,

**[1:38:00 – 1:38:02]** when you have,

**[1:38:03 – 1:38:04]** this kind of

**[1:38:06 – 1:38:35]** Thing you can actually, first of all, you can initialize them in a smart way, so they are kind of separate from the beginning. And then you have this very clear, semantics of what's going on between layers, and you can actually refine them in a smart way that don't have time to explain here. So but as a result, you get better object, queries better anchors there called in less time.

**[1:38:37 – 1:38:53]** Ah, and yeah, I guess I will have to skip this. I don't have to skip this, the best object detectors right now are dino and their modification. And this modifications that I know DND letter and

**[1:38:54 – 1:39:10]** yeah, whatever the formidable that turns on and so forth. I I left in the big server on Transformer, based object detection but unfortunately we don't have time to discuss them but yeah, let me stop here.

**[1:39:12 – 1:39:13]** All of this.

**[1:39:14 – 1:39:28]** Things, all of these different architectures, they share this basic idea of their original data. That the query is the objects. The bounding boxes are queries to a Transformer decoder.

**[1:39:29 – 1:39:31]** And the Transformer decoder.

**[1:39:32 – 1:39:32]** Will.

**[1:39:35 – 1:39:39]** Fill them with content, according to the image.

**[1:39:40 – 1:39:40]** and then,

**[1:39:41 – 1:39:46]** Again, there is a big science about it, lots of results, lots of lots of lots of different architectures.

**[1:39:47 – 1:39:54]** Okay, so sorry. I ran a little bit over time, but we only have three lectures left and

**[1:39:55 – 1:40:01]** Tomorrow will be something completely different. We'll go to more generative stuff.

**[1:40:02 – 1:40:03]** So, any questions?

**[1:40:08 – 1:40:14]** Okay, in that case, thank you. I'll make it available and see you tomorrow.

## Full text

Okay. Hello everyone. And welcome back. I'm happy to continue our Discussions about declaring. And specifically on this last week, we finally turned from something general. I mean, it usually, it usually happens every year that we started teaching a course called computerization but actually It turns out that you always need to start with something like declaring Basics and the actual computer vision gets bumped to the end of the class. But anyway we are here and over the last two weeks, we have discussed We have build up, actually why the array of architecture's a set of tools to solve various problems? And finally, we begin to apply them specifically to pictures. Well, we already talked about pictures and the contacts of cnns. But we haven't yet. Talked about pictures in the context of Transformers. If I understand correctly, Alex already explained to you, the ability the vision, Transformer in practice sessions, so I won't be spending too much time on it and our like main plan for today, our main Content will be a specific. General but specific problem and computer vision. Specifically object detection and object detection has one of the most interesting problems in computer vision and Object detection, as actually. one of the hardest in a way, because it's quite Unusual. It has an unusual structure of the outputs, compared to say, segmentation which we won't discuss an actress, but maybe Alex will in practice. and there's a lot of talk about and also Transformers actually come in very in interestingly and very differently in object detection actually, as you as we discussed, I think, usually the Transformer just goes in replaces some part of the architecture and served as a better feature extractor, and that's it. And there is nothing like conceptually changing in the architecture. Quite often, for example, in segmentation, if you discuss it with Alex, he will tell you about the unit architecture, which is from, you know, 2015 or something. But modern segmentation still uses unit. Only instead of conversational layers inside. It uses some kind of self-attention base layers and of course there's a lot of The, there's a lot of new stuff happening, but basically the unit did not get obsolete because the Transformer appeared in object detection. It's a little bit different and we'll see how it works. So anyway, If you are, first on Transformers, for pictures Mission Transformers. Ah, let me not spend time at all on visual bird. Visual bird was one of the first moralist successful approaches to handling pictures is Transformers. And let me just tell you the setting the problem setting for for visual bird. It was for captioning mostly and it worked like this. You've had your text and you had like object queries, like you had tokens that represented specific objects found on the picture. So, to use visual bird, you would have to solve for object detection first. And then you would plug in this subsets of the image. This rectangles we'll discuss it an object detection. Distracting angles that correspond to specific options on the input image and Then. Pass them through some. Simple embedding layer, get a vector features and then off you go with Transformer. and, the point of this picture for us is that for the Transformer as you can see here, Like it really I won't say it doesn't matter, but it really matters little whether the input came from text or from images or from whatever. As long as it's a sequence of vectors, the Transformer is not, is an architecture that is great. And at finding various, you know, internal correlations between this vectors finding structure inside everything like that. So it is no wonder that. at some point, people just straightforwardly applied Transformers to images. And again, Alex, talk to you about the architecture, I want waste time, but like the most interesting, the most striking feature of the vision, Transformer architecture of the vat is just how simple it is, right? It's, I mean, you don't need to do anything, there is absolutely no change in the Transformer architecture because now the input is an image. And in fact, you might think that when you cut a picture into patches, these patches do not really correspond to the Natural. One-dimensional sequence, right? Well, I mean, you fix some sequins but like HSN pages in this sequence will not be necessarily anywhere close on the image right. For example, if you go rolls first, then you put the first three purchase they are indeed neighbors. And then after the third one, you go back to the right to the left part of the image. And these two pages are nowhere near So it is tempting to say that. Well an image is not really a sequence, right? And image is a two-dimensional structure. We need some something new something interesting, at least some change in the position and coins that we just discussed last time, right? In order to fix the right, we need some change in the positional concerns to tell the Transformer that it is actually. That it is actually and a 2G structure, right? Again, it will not care if it's an image or what, it's just a vector of features for the Transformer, but at least the positions should be somehow marked. Well, it turns out no. And in the original vat paper, there's an appendix, where they show that. Oh, yeah, sure. We tried. Lots of several ideas on how to do this position, according to none of them helped. Basically, you just treated as a sequence that's fine. Just use standard position on recordings from text Transformers. And the it. Kind of revolutionized. Image processing, revolutionized everything. Oh computer vision and everything else dealing with images because again a Transformer is just better. It extracts, better features, more semantically, rich. And you can in many, many applications, you can just say it, take out your convolutional network plugin, the vat, just reuse, the same stuff that you have. On top of this feature extractor, and it will be better. And there were, like, 100s of papers to exactly this after 2020. Ah, and there is only one problem. There is only one problem that is hard to solve for Transformers. It's like the main problem, the main computational problem of Transformers, which I mentioned when we discussed the architecture itself, the problem is the vat and then you Transformer has quadratic complexity Right? So we discussed that. We discussed that in the Transformer there is this Matrix of attention weights, right? And it's a token by token Matrix. So it's a matrix of size L times, L where l, Is the input size. And the trailer to go around this. So the VA it means that the vht Has complexity quadratic. In the number of pages, right? So every page becomes a token at the input of the vat, So if you have, I don't know, height age and tweets w. And let's say you have, I don't know, K times k h, then there will be that many pages. Vertically times that many pages for horizontally and this will be square. Right? So the size of the great Square. And this is a bit problem. It's applications, at least because it means that you cannot really people try it with other architectures, but you cannot really have the VIP go down to the level of individual pixels, right? If you have a million pixels input, oh fell. A million square, this too much, even for Modern Hardware, or whatever. So you have to have patches and you have to have relatively big pages. and if you have relatively big page, as it means that you can't really Means that you can really. um, figure out the small details of your image. so, if you are doing for example, object detection through the vat, whatever, that would mean, And you want to find a cat in the same image and if the cat is small, maybe it's far away and it's completely inside one page or even the part of one page or maybe it's on the boundary between two pages and you know, none of them really is dominated by the subject then I guess it will be very hard because every page will get flat and to a single vector and stuff will get lost along this way. So so it's really and like that there's really no correct size for the 80s so just like we just asked with the attention mechanisms it, it's either to be in which case you're losing detail or it's too small and which case you just can train it and can run it because it's too heavy. Ah, so what people did, there were a lot of approaches. I want to discuss one of them specifically The. Swin Transformer, the swin Transformer because it's one of the most popular. So today, if you open up some computer vision, application probably will see, either vat or swin, some version of spin or vhts your back. And the students Transformer. So the screen stands for shifted windows. and, Here is the thing. So as I said, The. A complexity grows as the square of the number of pages, right? So a natural way to say from this would be to break down the image into parts and then cut up the parts into pages, right? So for example, this here I would, let's say do a 2 by 2 grid like this, right? And then I would just take this guy which has only three by three grid and here I would have complexity like nine squared. And here, I will have six squared 6, squared, 9 squared, right? And if you had it all up, it'll be a couple hundred but The original complexity was like 25 squared, which, of course, much more, right? So if you, if you have square complexity and you cut up into smaller pieces, your save a lot and it basically, this Square becomes linear because now it's the square. Only in the size of this small part. so, it's very natural to have this kind of Hierarchical structure. where, First, if you have a large image of the input first you cut it up into small pieces, relatively small business, like a former for great. then you process every every part here with the vat, Then you combine them and again you process with another player, Vital Certificate layers. And then, finally, you combine those somehow won't go into details. How, exactly. And process now globally. The whole image also with vit layers, right? So in this case, on this picture, every vit layer, every Transformer layer deals with 16 tokens at the input right? On the 4, by 4 great. But in three steps we go from what from 16 by 16, image to 4 by 4 mesh, wishes and compressed and features, or a single vector, or whatever. So that's that's the basic idea. And why is it called shifted windows? it's called shifted in those, because Well. There is this problem that we will discuss an object detection too. The problem that when you look inside these small parts of the input image very often, It would help you greatly very often, you would be very happy to have a more Global context of what's happening in the image. Like, I don't know. You see, I can't draw it but, you know, you see a small part of some kind of Surface. And on the surface, there is some kind of vehicle, right? And it's small, that's the whole problem. So it's hard to distinguish exactly what this vehicle is. So if, if you know that the context is a highway and it's like a road with cars and it's a car. If you know that the context is, I don't know what Lagoon of oversee, then it's about, right? Two very different classes. You can't really distinguish without Global context and this in this actually happens all the time. It sounds like a contrived example, but actually a global context is necessary quite of So you would like these guys down here to have a way to get information about what's happening in the rest of the image. And shifted Windows. Does it this way? Very interesting, very cool trick. I think the trick is between self-attention layers, You shift the windows? so, You would have. Liked on one layer. I want to draw it a little bit. larger than on the example, because the example I think the picture from the paper is a little bit misleading, so you have A great like this. and then, on the next layer, you will have a great like this. Okay. so, it will shift like half of the Size of the page of the page. and, It will still be the same kind of Transformer. It will still have the same. Size of input. but now it will shift to different subsets of features, so like different parts of the image and notice that if I do it several times, after every layer like this, say, then this will expand the receptor field of my pages, so If I was sitting over here, right, and I saw this part of the image, then after I go out here and then come back again. Now the same Transformer but in two layers up, we already be looking at this part of the image. Right, because it has collected actually even more because like this guy will be looking at here. So, okay, so we will be looking at this part of the image. Sorry. Because the purple grid has been looking on like this part. Right, this, this Square. This, this, this this Transformer has been looking at the orange square. And when you go back, you collect all of this neighboring. Hsnt purple. Squares. Right. So this is how it works. and, This is how it works. And the like that there is a lot of Unclean. And Easy to miss Implement stuff about around the edges and this is what this picture shows. Basically, if you shift your grid, the ages will not fit anymore, right? This, this small parts at the near the edge of the image will not be full squares anymore. So what they actually do, they like roll up the image in the Taurus and they say, okay, so now this guy over here is goes together with this guy and this guy over here, the direct angle goes together with this track and they did the small square at the Corner's, also all go together as a single. And so, this doesn't really matter all that much, because it's only about the HS, but so it's a lot of hassle. Once I saw an implementation, I don't think Have here. But I saw an implementation of a 3D screen Transformer where you do the same stuff but with like, cubes instead of Squares. And it was the most convoluted piece of code I've ever seen. There were like, lots and lots of hard-coded, shifts and constants and it was very difficult to understand. So, Okay. But anyway. So, the screen Transformer. Won't discuss. I won't discuss the exact architecture, but the same Transformer and the vat. Both can serve as good backbones, right? So what is a backbone? It's a tool, a part of the network, the largest part of part of the network that does feature extraction. And what would it do? Feature extraction for Well, by default the V8 is trained on something, like classification, you know, your fish are extraction. You see where You do a feature extraction, you see where the you, you collect the features into a single Vector at the end and you do your stuff about the reasoning about the image as a whole about. ah, but what we are discussing today and our main content for today? It's been 20 minutes good. I think we are a little time and what what we are discussing today is a different kind of application, and a different kind of problem that will require us to look inside the image. And to actually map our answers, the specific pixels which is always more difficult, right? So I'll skip the perceiver. I don't have time for that. so, Our main targets, are our main topic for today, is object detection. What is object detection? What's what? What's the problem? Well. Okay, I don't have a slide that's so let me just go to the board. And the first, let me discuss. The problem setting because there's a lot to discuss. So my first point was Transformers for feature, extraction from images and our second point is what is object detection? Um, well. What is object detection in Formula? I hope you all kind of have an idea. So there is a big image, like this. And there is a cat inside, right? And maybe there's not only a cat inside, maybe there is something else. Maybe it's a big thing with a lot of objects. so, the object detection problem. Goes like this, given the same image and give, and let's say the cat class, like, I also should specify what exactly. I'm, I need to find find the cat. And not only say that there is a cat. Like give me the confidence they probability that there is a kid like usual classification. But also To draw a rectangle around the kit. To specify exactly where and in terms of this rectangular positions, not down to individual pixels, that would be segmentation. But down to this rectangle, specify where exactly you found this cat, So, this rectangle is called the bounding box. Usually abbreviated to beatbox in documentation and papers. and, Then you can have many different classes. Maybe in addition to a cat on the same image, there is a dock somewhere. Can I draw a dog? I'm not sure. But at least let me make different years for the look. and, okay, so that's kind of looks and there is a dog and I also want to recognize the dog and I also want to draw a rectangle around the dock and also specifies bounding box and they can they bounding boxes can overlap? Of course, images can be anywhere, they can the objects themselves can can overlap with each other or they can just overlap in the empty parts of the rectangles. Whatever. Anything anything goes. The point is for every object that I'm looking for. I need to Output. Potential output. I need to Output the class label and this bounding box. So how do you formalize a bounding box? It's a rectangle. You need to specify its coordinates. So usually people do it like this, they have like X and Y for the bottom left corner or any Corner, that's interesting for you. And then the width and the height of directing, right? This rectangle is defined by four numbers. and so, here is the interesting part now, I hope. The idea of the problem was clear. I hope it's clear how What we are trying to do here? But it's becoming less and less clear. How exactly to do it, right? So like, how would they Define the neural network solving object detection? Even let's, let's not speak about architectures. Now, whatever, whatever is not work, but what is what what is its input and what is itself? Here's input. Obviously, I take the picture. I put it into my neural network. And now what is the output? Well. A picture can have multiple objects, right? If I assume that there is only one object, it's called object localization and it's a much easier problem. so, I need to have a way to Output multiple objects. Right. Like object. One, two, three. And maybe maybe more, maybe a lot more nose. Right then for every object, I need to have its class. So the class label as usual for classification in the form of a probability distribution. So this will be like the Distribution on classes and as an as always in classification. And then I need to specify the bounding box. So four numbers x, y w, h and so on for every for every object. And here is the first. Tricky part. I cannot have a neural network with variable number of outputs. Right. Kind of doesn't make any sense. So, I need to fix the number of outputs from my neural network. I know how many outputs exactly I have like per object, right? So per option I have the number of classes for their probabilities and then for numbers for the bounding box. So if I know how many objects I have, I know how many outputs I want, but I don't know how many options right on a picture. There might be one cat. Okay. Three cats, four, cats, and two dogs forever. I don't know, maybe 100 of objects and I I just don't know it and once, so, Uh what's what's the the answer to that? How do I solve the problem that I can't really have like an open list at the output of a network? And they can't because the output of a network there should be neurons with weights and I cannot have a variable number of humans because I need to have this number of weights and they need to train them, right? so, For this question, they are output. The answer is pretty trivial for this question. The answer is well, okay, let's fix some maximum number of options that we want to recognize and let's just have the this menu. This makes another question, right? This back's another question. Now, what happens? If there are fewer objects, what happens if I'm recognizing 10 different objects? But the picture only has a cat and the dogs. So, like two objects and the rest is irrelevant that they're not my classes. Well, in this case. I need to have a way to specify that, like, Some outputs. Don't count, right? I need a way to specify that, okay? So object number one is real object. Number two is real, the rest. They are not real. And usually it's done. Exactly. Like I said, so usually it's done by inserting by adding another output. Which I would call the confidence. So for every output you would have something like, okay, here is how sure I am that. There is an object here and it's usually probably right? So from 0 to 1, Here is how sure I am the there is an object here. and, If it is there then here is its cost label. And here is his phone books. so if I have only two objects then, Sure, if I have on the two objects, then sure. AI. I would like the confidence as for this objects to go to one and the confidence is for a lot of objects to go. To go to the room. So, Okay. But this is so under the beginning, we still have a lot of unclear things here. We still have a lot of like, interesting questions left. so, We Define what should be the output of the neural network? But this is only the first step and it's intermediate step. What I really want to Define what we really need to Define for the work. It's a lost function, right? So, What would be a loss function? For this kind of output. What would be the host? Like I have this picture and I have The, the ground truth. The ground truth, which are like these two objects, right? So this is like y 1, Y 2 for y1 and I know it's a cat. I know where it is now. It's bounding box for white so I know it's a dog. I know it's bounding box. How do I? Compare this. To the output of the neural network. What should I optimize? Well. Kind of again, known female. Why not travel because I can't just say, well object. Number one should be this cat object. Number two, should be this box, the token. That's it. Because the neural network doesn't and shouldn't have any idea of some kind of ordering of the objects, right? It doesn't make any sense. They don't come ordered. I just want to recognize the objects on the image. I don't know if the cat is number one, and the dog is number two. And also if I have confidence is like like here and if I have a big list of possible objects then I don't want to require the neural network to in addition, sort them by confidence or something that would be difficult and completely unnecessary. I just want this cat to be somewhere inside in this talk to be somewhere inside and the rest. The other outputs to have low conscious. Right. so, what we actually are looking at is we need to find a matching between the ground trolls, the answer and The. Predictions of the neural network, so it's kind of it's called an assignment problem, right. We need to assign. Elements of these two sets to each other. I can like pair this with no object to okay. And then I need to assign elements of this sets to each other. The minimize some kind of cost. um, and okay, here I I suppose he will discuss it in Practical sessions, there will be something like different area and algorithm that actually produces this bipartite matching one-to-one matching, between predictions and ground truths in a way that actually assigns The ground truth box to the best predictor. But that's all not enough, right? So what is like, the next What is the lowest function then? Well. The loss function. The Lost function. And here I am. I I want to go into full formal details because they can differ, there can be different ideas and different ways and whatever. But The loss. Is composed of two things, right? The classification was three things. Sorry the confidence was from like if there is an object, the confidence should go to one. If there is not an object, the confidence. Go to 0. That's one part. And that's pretty, right? It's like just the lock probably log. Confident minus low confidence or something. Then. There is the classification loss. So if there is an object, let me put it this way like if there is no object then we don't care what the class label says because if there is no object and it's just random stuff, If there is an object, then we care and then it's probably just cross entropy. Between these two probabilities distributions. Right. And then there should be. The bounding box loss. So these numbers should represent the correct rectangle and of course they won't in practice and Again, it only matters if you have an object. But if you do have an object, what is the laws for the bounding box? You can do it with some straightforward laws like x minus X predicted squared plus so on plus h minus H predicted Or not squared, or maybe the same but like absolute values for for an L1 loss or whatever. but, Problems with this coordinate based losses. One, common problem is that? you will get a very different contributions into this loss for large objects and for small objects so, okay, in our example I have two large objects but anyway if I have Like this ground truth box. For the cap. And my predicted box is like this. Well, it's pretty good, right? It's pretty good. But we have Quite a lot of distance here so I will need to move the bottom left corner down here and then up here and the bits and height and how to draw it. But they also need to be updated to be adjusted. And, but if I have a very small object like this, and as we will see a small objects are the most interesting case for object detection. This is what's difficult. and then, For the same kind of loss. My. Bounding box will be completely different, right? So here the overlap, a lot when they are large and here for the same loss for the same difference in width height X and Y. They will not overlap at all. So not really into it, right? I don't really want these to make identical contributions. I want this to be a bad thing, and this to be an almost perfect thing, right? So, how do I fix that? Well, the answer is. I don't want to get my, I mean, this some Some approaches object detection including some of the ones that we will discuss today, say well. All right, what can we do? Let's still use something like that. Like the original yellow uses. I lost function like that and but this is usually people do some kind of a loss based on what is called the intersection of reunion metric. So, the IOU of two. Two areas on a plane. In this case, two boxes is Precisely what it says intersection over unit over Union. The area of their Intex. Intersection divided by the area of their Union. So in this case, I take this guy and I divide it by this guy. And I get something like, kind of 0.6 0.7 I guess, in this case, which has a pretty good area. In this case, I get exactly zero. Right. so, so, this is The default. Metric for measuring like goodness of match between. Bounding boxes and predicted boxes and it only has one more problem. I want to go into more detail formerly but it also, it has on the one problem in that. Now, if the boxes don't overlap, The IU, as I said this exactly 0. and, Notice that the IU is actually differentiable. It's not a piecewise constant, you can pass gradients through it. If you slightly tweak, if you push this Bounding box a little bit to some size. You will get a small change in there. So, the gradients makes sense but the gradient stop making sense when the numerator becomes 0. Right. And this is a bad thing again because I when I look at this to bounding boxes I do want to be able to say that I want to move it here. But from the point of view of the view, if I move it in the right direction a little bit, it's no different than if I moved it in the direction a little bit, it will still be 0. And the gradients don't have So in effect they are like additional metrics. Something like the general lifestyle. You which I am not even sure I remember correctly. The formula. So I won't try to reproduce it but basically they make use of these Bounty box and they do something like, they involve something like What is the percentage of this common bounding box? Not covered by these two boxes? Something like this. So now if you move in the right direction, then This joint bounding box shrinks and the percentage becomes larger, so this would be a good thing. And I think that's it for the loss function. So we have discussed the main components, the main usual components of the was function But there is one more little thing. One more little thing. That happens. When you apply in your network. So now, I guess, I I talked through everything that happens when you train your own network. but what happens when you apply it and notice that so far I haven't said, A single word about. How it actually works. What's inside in your own network? What, what's going on? I'm just talking about those function. This is pretty common and difficult problems in non-standard problems, the architectures will come and go, but those functions are like a separate option. They don't care what the architecture is. As long as you can pass the gradients through and they deserve separate discussion and they both Separately. There is a line of work that tries to optimize the losses and the separate line of work maybe in the same papers but it's completely agitated right? You can optimize them independently. And the architecture in the losses. So, okay. So Finished talking about the losses. But what about the, what about the application? What about the inference of this neural network? What's the problem there? Well. The there is there are two problems. and again, I don't I won't go into too many details but a little bit I have to mention. So, here is a picture and here is a cat on the specter. And the cat. Is very happy. And I want to recognize this kid. Right. so, Make sure. Oh yeah, actually. It concerns the loss function too sorry. But Uh yeah, it concerns the training time too. Sorry, we did not quite finish that with the training because here is the thing. Yes I can. I can get you the best possible assignment between the ground truth objects and the objects that I project. But even after I get the best possible assignment, I still need to decide. Which parts, which predictions are actual objects and which predictions don't count. so suppose that in this case, I get a bounding box like this. Right. So this bounding box is kind of maybe about this cat. It looks like it's about this kid. so, when I look at the bounding box like this, I want to say, well, Almost right. But you need to shift your bounding box over here. Right. And you need to put the class labels so that it's a cat. So in this case, for this gray bounding box, I want to say well I want to make you into into the campground in box. It. And then if I have a bounding box like this, for example, It also kind of overlaps with the cat, right? But most probably it's about something else. And even without looking at the rest of the picture, without looking at its class probabilities, probably, it's not about the cat. And probably if it's if there is no ground truth over here, if there are no other objects in here then probably for the light blue box. I don't want. So for the gray box, I want to become the cat box and they would want it confidence to go to one. For this box. Well, it never had much in common with the cat. I don't want to bring it over here. It's it's it doesn't sound right. I just wanted to go to zero and it's just a serious bounding box and there will always be lots and lots of outputs with where the confidence showed zero because again remember that there are a lot of outputs many boxes like the maximum possible number of objects and then reality there will be like two or three on a given picture and most of the outputs should have confidence go to 0. So here too. I need to distinguish between these two cases either. I want to count this box for to become the cat or I just want to say okay this is a bad bad box. And let's let's let's just forget about. well, again in practice, it's done with an IU threshold, so you just, pick a number like one half or something and if they overlap is larger than one half, then you count, this output is the ground truth and if they output is less than If they overlap is less than you don't. So this is easy but still also need to mention. And finally, I guess I will talk more about this in practice finally. There is this effect that when you have an object like clear object, that's easy to recognize and you run the same image through in your own network. Ah, that has a possibility to distinguish those dozens or hundreds of objects, most probably not one, but a lot of them will stick to this kit. So you will have like a bounding Box about this cat like this. And you will have another bounding Box about this cat like this. And you will have another bounding Box about this cat like this. And there will be like those of those. of course, you don't need to repeat the same object of times, I guess the And the standard way to, to cope with it is an algorithm called non maximum suppression, and let me just leave it at that. It doesn't matter for training for training. We just do the best matching and that's it for actual inference. You need to do this on maximal, suppression to pick the best possible bounding box because now, you don't know what the ground truth is. And you need to somehow combine, all of this hypothesis into a single box. But overall, that's it for the problem. Satan. Right, so notice that I haven't yet said anything about how to actually solve this problem. I haven't said anything about what's inside the neural network and how do we produce all of this wonderful outputs? Well. let's say a few words about it, so, What kind of words, what can we say? Well. I want, of course go back in history before the learning where we are doing preparing after all. I will go. 10 years back to 2014 when there was like this first approach, Kind of after Alex net, revolutionized image processing. People tried to Apply deep learning everywhere for images. And Finally, they go to object detection. And the first successful attempt was called rcnn, which stands for region based and then And roskear is one of the best known researchers in object detection and here is how his original approach worked a long time ago. well, first of all, it used an external algorithm called selective search, I won't go into details to produce candidate bounding boxes, so, you put your image through some algorithm Some external algorithm and it gives you candidate bounding boxes but the algorithm doesn't know the classes. It doesn't care about the classes. It just finds distinctive objects on the photo. That's So if you want to recognize cows, it will still get this post over here and the cloud and the ear of a cow and whatever. So it will get 1 0 0. So what next then they take every one of these boxes and treat them separately and pass every one of these boxes through in your own network. In this case you see an entrance on image net. So this is the backbone. And this CNN will tell you. Like what class of object it is. Sounds. Very straightforward. Of course. This doesn't answer. The most interesting questions. so, Well, okay. So first a technical remark to actually put a bounding box through a CNN pre-trained an image and that you need to make it Square. The CNN pretrained on image, net expects the 56 by 2:56 square foot. so, what they actually did was they took this box and actually warped it just, you know, Compressed it so that it would it would become Square. Just artificially geometrically compressed. And that actually worked. I mean, obviously, for this post over here, it would make it very, very different, right? But still, it was the best solution on the time. And then all. So, Another problem was that the CNN they the backbone will not tell you. Whether there is an object or not. Right. I see an entry image, that presumes that there is an object and just classified. If you give it some bad bounding box, that's just you know, a sky with some clouds. And I don't know if image that has the class Cloud, maybe it does, if it does, then hopefully it will be recognized as a cloud. But if not, it will be just some some distribution of our classes, there's no confidence in the outputs of a classification Network. So they actually also had to have a third step here. Another step that takes the outputs of this CNN. and modifies them and they and passes them through a completely different model, a model on top of that, that will actually Further classify based on this probabilities like whether it's a real object or not, it was very fragile. It still was the best approach at the time which shows just how cool declaring case but it was, of course, Very French and it was hopelessly slow. Hopelessly slow. It, it was like a minute per image on a GPU. But all of the ideas. Are already in this original version and an architecture. At least all of the ideas of this one of this. One approach to object detection. That is called two stage object detection. So I actually I used to have like very detailed lectures. An object detection. That would go through those of different architectures. I will not do that with you. We don't have time and they became less relevant as time goes by. So we will jump to Transformers in a little bit, but I do want to discuss their CNN family, because in a way, it's so long. And it's still explains in this simple example, let's say explains the main idea. So what are the main ideas in this basic Carson and the main idea is use your backbone to extract features from a specific part. Of the input. Right. and, From specific part of the input. And sorry. Yeah. And where do this candidate bounding boxes? Come from? Well, in this case they come from an external others from later. We will see they will come from the network itself but still you first Get a set of candidates and then you process every candidate through a scene and you extract the features. And then you see what's inside there and What you want to do, right? So this is the idea of two stage, two stage object detection. First produce candidate. A relatively small set of candidate bounding boxes, then process, everybody knows in the way. But of course, processing every bounding box completely independently is again hopelessly slow. So this picture has the real numbers to get like good coverage of the actual objects of the actual bank and boxes. We need to extract like 2000 region, proposals. Uh so where do this? 47 seconds? Come from. They come from running the same network. The network is very fast actually but you have to run it like 2000 times. And then run a model on top of its results. To actually get something, right? So this is of course, hopelessly slow. so the next step in what was called faster CNN, The Next Step was to and this is this is an important idea was to process the whole image on the ones. and then, Extract features from from the feature tensor, take parts of the feature tender are rather than reprocess everything from pixels. Makes perfect sense. Right? So you have this I want wait time on trying to redraw this on the board. Let me just talk. Talk through the slide. So you have this long convolutional Network, or Transformer Network or whatever and keynote Transformers don't work like that, but if you have this long convolutional Network, and as we go through the convolutional network as we discussed, You gradually lose the geometry. And if you want to keep some of the geometry, stop it a bit earlier. We did this in attention mechanism for attention mechanisms before So, the same idea here. You pass your big picture. Through the CNN, on only ones. You get. But in, but you stop a little bit short of the goal. So you get this feature tensor that still has geometry. Then you take your candidate bounding boxes and faster and they're still produced by an external tool and external algorithm. this bounding boxes, and when you have, Some geometry on the feature tensor. It's not a problem to find out like which features correspond to which pixels of the original image. You just have this correspondence. So when you have a bounding box you can project. That's called Rory, projection region of Interest projection row, Roi is a very common abbreviation and object detection, it stands for each of Interest. Um you have this Roi projection, it's not a trainable thing. It's just which features look at these pixels. And now you have The same bounding box, only rougher and inside the feature tensor, okay? and then you take this mounting box and you put it through an object detection head. An object detection head that has basically a classifier for the classes and the bounding box regressor for the bounding box itself. So I didn't mention it before, let me mention it here, usually even even if you have Candidates already. in terms of pixels like here, you still want to have a bounding box regression at the output because maybe the network will Want to shift this bounding box a little bit, maybe and it will be useful. So the network might decide. Oh. Okay. So this is about can't but I need to shift it, a few pics of the left. And yeah, that actually happens and you can train it because you have the brown truth. So it's a good thing, the bound box regression is always here. A one detail about this. Is that? Okay, so now I run the big convolutional Network only once And for every bounding box I actually run. Only this small head I want to say classification head no small detection head with a classifier and regression. So this is already like orders of magnitude faster. One, technical problem, is that? Again. I don't know. I I need somehow to fix the size. Of the input for this guy here. So, my bounding boxes will come in different sizes. And they will map to parts of the feature tensor of different size, too. And I need the input to this head. It actually had to be always the same. What do I do? Well, I insert what is called tradition of Interest pulling Claire and also a pretty straightforward idea, but pretty cool. Let me draw it over here. Straightforward. But cool idea. I have, let's say this is the feature tensor, right? And I have a bounding box. In the feature to enter that goes, let's say like this. So it's a three by five five by three tensor. Don't care what the depth is. I will not cut the depth but it's three by five and my detection had once to have as input, A 2 by 2 tensor. Let's say. So what do I do? I do pouring, but I do like falling not with a fixed. Windows size but pulling with the fixed output size, So in this case, I will see. I know that I expect my output to be two by two and I will just cut it up as evenly as possible to To read the to have two by two windows. So of course it will not be exact because these are integer numbers but as close as possible and then I will pull the features in this for Windows, okay? So this, this is called region of Interest pulling. That's I guess the one cool idea that I wanted to mention for faster and not just for fastest RC and it will be used everywhere, starting from faster and so, So, this was already orders of magnitude faster. and, The remaining bottleneck. Now the slowest part of this pipeline. Was not in the network at all. now, the slowest part was actually this external Elder in the, we didn't want to discuss that produced the Candidate boxes. Okay. and, therefore, In the next iteration in the next idea that we need to to understand that underlies. What is called faster rcnn, very creative naming. We have this line from Arson, and to faster and to faster and Faster. CNN. It's still counts as two stage detection because we still will produce the proposal separately. And then we will score them and match them and everything. But now, I will make the proposals. By a separate part of the network, the region proposal Network that is inside the architecture. So again, we don't have time. I want discuss how this RPM actually works. The region proposal Network, how it actually works, but the point is it works on the same feature map. And it's a separate Network that goes with a sliding window over this feature map. The feature map map has already lost most of the geometry. So now you can afford to just go with the sliding window and basically just find which boxes make sense on the level of this feature map. And it outputs. A few top boxes, maybe some hundreds of top boxes. And then the rest is the same. So still with this creation of Interest, pulling still, we go to the detection, head still be cut out the features, everything else is the same, but now the proposals come from inside the network. And faster. And then actually, Became like the standard approach up until Transformers change everything but it's not in 2017. It was much later after the 18th and everything, but For quite a few years faster and was like the standard way to do object detection when you have time. So two stage detection, even if it's all in the same Market lecture is preacher slow. and, You still have and like it shines, if you give it a very smart, very complicated backbone. If you use a good Network, so, of course, CNN's progress, you know, from resnet from from VHS, to resnet to efficient Nets, ultimately. And when you see an architectural like this, you can just, Plug in a different backbone here. You don't have to change anything over here, and you will get a better object detector, okay? So notice how how our discussion has shifted from like architectures, too Meta, Meta, architectures. You have now, this Global idea of a new Roman networks, that extracts features. And then that's the region proposal and everything. And the top part, the heads are more or less fixed but for the bottom part you can substitute whatever. and, They are like whenever a new feature extractor, comes out that works better. You get better option of detection for free. Let's that's how it's always worked. Okay, at the same time. I still want to get the Transformer based detection so I will speed up a little bit at the same time. There was a separate line of work called one stage object detection, where you do it in one pass. And what is the difference? What's the difference between one stage in two stage detectors? The difference is, in one stage detection, you go, You don't only want pass of the network through the image and there is no like separate stage. I mean here, it's also a part of the network. It's, it's a fine distinction. But Here There is a stage where you like have your proposals Then you rank them. You choose the top proposals. And for the top proposals, you do some heavy stuff over here. In one stage object detection, you just go over. All of the possible proposals, which means that maybe they will not be, maybe there will be fewer of them, because you can't go over possible. Rectangles inside an image. In terms of pixels, bit too much, that would be like number of pixels squared completely invisible. It. But maybe you can go over like reasonable candidates for bounding boxes at some level of granularity. And yeah, that's what that is. Best exemplified by the YOLO family. Let Me Maybe not discuss the original yellow, it's kind of irrelevant. Although it's it's it's it's quite beautiful and its ideas and those function already discussed. But anyway, maybe not relevant. Now. And then oh, all right. Yeah sorry. Yeah. So sorry about that. I thought I would have flights about the only two and he'll be three and everything. Yeah I decided to skip them but forgot that I took out the lights. so, After so the yo family basically okay so let me show you okay this picture anyway the yellow family goes like this. You have a single neural architecture that starts with the image. It goes over. Lots of candidates in parallel. and outputs the results for all of these candidates and then you can rank them and just take the top however many unit. So there was the original yellow and yellow V2. YOLO 9000 that had a lot of classes. And also pretty interesting techniques, like, techniques, like the Hierarchical softmax also very interesting idea and for you don't have time to discuss it. Then there was able to be three and everything and basically, like as you go through this architectures, The basic architectures. Change a lot. in many small ways and I mean, there is rarely one big idea that you need to actually Ah, that you can just understand. And that that's the huge step. So usually, it's like 10 different little tweaks, every tweak gives you like plus 2% to the accuracy to whatever metric you're using. Also a very interesting discussion, what are the metrics of an object detection? But anyway, everyone gives you like plus plus 1% plus 2%. And then as a result, when you combine all of them, you get like plus 15% to the result and that's a huge leap forward. So in a way, it's a lot of small things. But let me mention just one more thing about object detection, before we go on to Transformers. So, What is the main problem of object detection? Both classical both contemporary, and whatever in with neural networks, with classical replacement. The problem is always about detecting small objects, that's like, always the hardest and sometimes, even impossible. So if I have like a cat over here and this can't take up like a quarter of the image. Mostly any object detection algorithm or any object detection architecture will recognize it fine, that, that will be. Okay, starting from 1905, the original faster, CNN, and yolov2, it will be fine. But if there is also like a small cat in the distance over here, then we are again. This crucial trade of crucial dilemma that we cannot really resolve and we see it again, we return to the same thing. Again, we need to to fix a level of granularity. So in terms of faster and you go through your CNN, you extract features, and then, at some point, you stop. Right? And you need to decide at which point do you stop? If you stop to late, it means that you have lost a lot of the geometry, your feature grid. If you map it back to the original pixels, maybe looks something like this. Right? And now this small kit leaves completely inside one feature vector, and it doesn't even Define entirely. So, You are losing this cat, you will never recognize this object that is completely inside. One feature Vector, it's just this information has been lost along the way to here. on the other hand, if you stop too early, So now yes we can we have a fine grid here and we can recognize this cat but now it becomes infeasible because everything that happens with this guy over here, involves some kind of, you know, going over all of this features with all possible candidates for bounding boxes and stuff like that. So just like you can do it on the pixels and sales you probably can't do it on this two fine grid so this would be great but it's kind of invisible. And if it was feasible, so again, I don't have time to go into details but you could say, oh, okay. But what if I just look for small objects if I have this fine, right? Well this, you can do it becomes feasible. If you don't need to go over like all possible objects on the fine but only on the small one. Then again this quadratic complexity disappears. And now, what you can do is you can do something like multi-stage. Object detection. Where you have let me now. Draw it vertically. You have your image. you go through the first level through the first kind of set of layers. This is the first part of the scene and and here, you have still a fine grid but not very semantically rich. And here you can actually go ahead and do your region proposal on that work and then get your bounding boxes. For the smaller objects, right? Then you do another. Few layers of the CNN and you have like more Global set of features. And then you do another part of the CNN and you have the most Global set of features and so you have like this three different, okay? I have like this 3 different scale. at which you are doing object detection. And another different scale like this. So now this guy will detect large objects. This guy medium and these guys small and you can basically do it. But and notice that it's not that expensive, it's more expensive, of course but not prohibitively with just one small detail and the one small detail is that as I told you in the beginning. When you are recognizing small objects, you really want to have Global contacts. You want to understand what the image is about. It will help a lot smaller objects are really hard to recognize because the only Take up a few pixels. And like, if I showed you this crop with a few pixels, we humans wouldn't be able to recognize them too. We would need the contacts of the Holy so, One of the most, fruitful ideas after this faster. And, you know, was What is called an fpn feature pyramid Network. and the idea of a feature pyramid is, to do this past bottom up to detect large objects, just like I said, but for detecting medium objects to also Copy here and view somehow. Features from a more global scale. And then also from here, to copy and fuse features for the finer scale. So in this way, you are not increasing your work too much. It's okay. It's just a couple more layers over here for the fusion, that's it. But now you give the network an opportunity to actually capture this Global context. So, fpn was a very influential idea. Still is And again, we don't have time to go into details, but I could give you a big, big, big survey of what different stuff people did with this idea. And with the idea of multi-scale, multi-stage, option detection, And then particular in the CNN's, we talk about the efficient net family of architectures where they would use, neural architecture search to search for the most efficient architectures. And here, there is a parallel efficient debt. Family of architectures where they actually searched for the optimal way to do this. so like you still you fix your backbone for feature extraction to be efficient at but then you search for the best way to like do this post-processing more or less because you can do a lot of stuff here. You can go down and then again up and then again down or you can go skip layers or whatever. It's it's not that expensive and you are allowed to experiment here so they experimented and there was also a step forward over here. But anyway, I really need to switch to Transformers so at this point We've discussed. So to speak. Classical object detection. I call it classical here but you know, it's It's already deployed and usually when people say classical, they mean something before the learning. Well, you know, anyway. and then Transformers appeared and then the VIP happened And suddenly, there was this question. There was this idea. Of how? Can be applied Transformers to object detection. And can we make a text actually easier because everything that I told you, it all makes sense and that's like a lot of ideas that Make logical sense and that work. And that constitute, this big field of research for object detection and everything. but, What did the Transformer teach us? As the humanity. The Transformer, what was that in deep learning canola architectures? Very often, maybe you can get away with just taking one. Excellent architectural at the Transformer and just throwing everything to, to the Transformer and plating at sorted out. Can we use the Transformer to sort out object detection? Well, it turns out we can and it's a very interesting approach or actually a very interesting family of approaches so, the first The first idea, the first architecture that starts at this direction is called debtor detection, Transformer, and I think Alex will have a practice session on that or its neighbors. And basically, what what does it do? so, Quite yeah. This, I wanted this picture. So what what exactly does that do? So first, by the way, it still uses a CNN. Pretty interesting. So the Transformer is not used to extract features from the from the image. They set the famous fish are extracted by the backbone. And anyway, he used the CNN to extract the features. You had positional coordinates as usual. And now you get your inputs to the Transformer encoder, right? So it's a sequence of vectors 0. And here is the basic idea. The encoder doesn't do detection at all. the encoder just extracts, features it you know, mixes up all of this vectors In some very convoluted way like Transformers usually do and basically it will train together with the rest to make the features. Most suitable for object detection. The interesting part happens in the D quarter, so this is like a full-scale Transformer. It's not Birthright GPT, it's an encoder, decoder architecture. And in the D quarter, we have you remember, right? And the Transformer decoder you have this encoder decoder attention where the query is come from the decoder from the prefix that it already rolled in if it was a language model and the keys and values come from the other part, from from, from the vectors produced by the encoder. Well here. There is no autoregressive generation. There is a set of what is called object queries. They are just vectors that are trained together with everything else or maybe even just random vectors that are fixed. And Then. You put them through this decoding decoder layers. with the Cross attention from the encoder also. Like informing them. So they the information comes from here. The image comes from here. and then, You take every one of the vectors here in the output and you treated like the input for the plate for the detection help. So here you have like small feet forward Network. Like the usual detection had that does confidence specification and bounding box regression. and, The input to this textual head is this transformed object query. So, how many objects do I recognize? As many as the object queries? So again, we need to fix this number, this doesn't change. But other than that, no, just how it's like this. Very Different but also very straightforward idea. So a backbone Maps, the input, the features, then we just flatten the grid here. This set of image features will have within the height, but we forget about it we just put converted to a single vectors. At positioning, of course and then go through this encoder decoder, Transformer architecture. and, An object query. Is. Like this placeholder, right? It's like a slot for a possible object. so it kind of I mean, when you look at how that are actually works Object queries tend to kind of like specialized so you will have an object. Where is that looks? Like I don't know for small objects in the middle of the image or large show objects on the left side of the image, something like that. They probably won't specialize in classes, but they will specialize in locations. And yeah, and of course, most of them will just say No Object. They will drive confidence to zero because You need to have a large number of queries, like 100. And in fact, images will have usually much fewer objects. so, What is also kind of interesting? What is also kind of interesting is that in better? You don't need. Tricks like non maximum suppression. Because the Aquarius. Talk to each other. They exchange information in this Transformer decoder. And when they exchange information, they kind of, This specialized again. So there are won't be as the output of that they're probably hopefully won't be. A huge number, but to those and almost identical squares around the seagull. There will be just one square because they object various learned to specialize in to not repeat each other. um, but then again, of course there are There are problems here too. I'm running out of time, but I will mention a few more architectures. One problem is the same that I already mentioned, it's the problem of scale. so, as shown here, the data Works on a single scale so you see. I put the CNN through a backbone and I used this features and that's it. There is no way for the rest of this architecture to like recover the small options that got lost in this transition. No, they got lost. so, the smaller objects will probably be Not very good. Yeah. Go. Okay. Oh yeah. Here are examples of that work in. You, you can actually visualize the attention heads, the self-attention that those inside. ah that that goes on inside the decoder and you can actually see that yes indeed object had specialized object, very specialized objects Yeah, so and back to to the scale problem. The next idea that the next modification was called deformable debtor. And the formidable data. Is as follows. So, first of all, you can run at several different scales. So here this is, this part will will be solving the scale problem in the same way as we discussed by riding on different scales on different like separately for small objects and barish objects. But what is? Like even most like what is most interesting here. Is that? The formal letter uses, what is called deformable attention. so, if you look at what actually that are attend to, what is what where where does it spend its attention weights, You will see that. The most important object, the pixels are the pixels and object boundaries. So if you look the decoder attention is localized on the boundaries of of the objects. And basically in that, ER, once you have a tension like this you've already separated the objects and you now already kind of the rest of the job is to just classify it and maybe draw a better bounding box that's it but mostly attention. Radio separates the objectives. You see in different attention heads. So it's a natural idea. To try to avoid this quadratic complexity of the Transformer, which does not let you just work on on small scale on the fine. Great, right. A natural idea would be to avoid it by just looking, not on every pixel, not on every feature Vector, but looking on small subset of them and also like, you don't know in advance what the subset will be. so again, I probably don't have time to explain in detail, but the basic idea is this like you have your attention head and it looks at several other tokens. At several other position, not actually, not tokens, but positions on the image and collects features from this position of the image, and the locations of this positions are also trained as part of training the whole thing. So yeah, that there are some technical difficulties here. I won't go into the details but basically it works like this. and, In this way. You can actually afford. To have the smallest scale feature map in the Transformer as well. So, the problem with the small scale approach would be the Transformer. You need to attend to every other token and if you have a fine grid, this could create a complexity will kill you. Well, how do we deal with complexity? Which is reduced, in this case, produce our attention, To a small subset of the input tokens. Then. The next set of ideas here. Is to work with the object various themselves. So, Again, I said that they tend to specialize and if you look at what however, this was produced and have time to explain but like this on average, where are the box is predicted by the object queries? They in fact, they do kind of Separate all over the input, which is which is great. but, this kind of learning happens, very slowly. Not really stable. and, A good question is and the next question, the next reasonable. Question is like, can we improve this? Because to be honest This picture does not look like. It would be difficult to produce just right from the start. Why don't we just take a great or sample random points and help better produce better object queries And indeed. The Next Step. Again, I have to wrap up but I want to mention it. Debt or dynamic Anchor Box, that are it actually uses anchors. It uses this object queries that are not just abstract vectors that will somehow over 100 of epochs of training move away and learn to predict different stuff, but they're just Bounty boxes. They have the meaning of x y, h and W therefore numbers. And that's so, when you have, this kind of Thing you can actually, first of all, you can initialize them in a smart way, so they are kind of separate from the beginning. And then you have this very clear, semantics of what's going on between layers, and you can actually refine them in a smart way that don't have time to explain here. So but as a result, you get better object, queries better anchors there called in less time. Ah, and yeah, I guess I will have to skip this. I don't have to skip this, the best object detectors right now are dino and their modification. And this modifications that I know DND letter and yeah, whatever the formidable that turns on and so forth. I I left in the big server on Transformer, based object detection but unfortunately we don't have time to discuss them but yeah, let me stop here. All of this. Things, all of these different architectures, they share this basic idea of their original data. That the query is the objects. The bounding boxes are queries to a Transformer decoder. And the Transformer decoder. Will. Fill them with content, according to the image. and then, Again, there is a big science about it, lots of results, lots of lots of lots of different architectures. Okay, so sorry. I ran a little bit over time, but we only have three lectures left and Tomorrow will be something completely different. We'll go to more generative stuff. So, any questions? Okay, in that case, thank you. I'll make it available and see you tomorrow.
