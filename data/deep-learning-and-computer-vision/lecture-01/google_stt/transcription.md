# Transcript — google_stt

- **Provider:** google_stt
- **Language:** en-US
- **Audio duration:** 3:29:30
- **Segments:** 1499
- **model:** latest_long
- **use_enhanced:** True
- **latency_sec:** 1742.57

## Segments

**[00:12 – 00:31]** Hello everyone. It is very nice to meet you here. Virtually remotely, but still meet you here at Harbor space. My name is Regina kohen and I will be talking to you about machine learning and yeah, the the class is called his name.

**[00:32 – 00:34]** Very specifically.

**[00:35 – 01:06]** Computer vision in neural networks. But to be honest, usually it's so happens that it kind of becomes just a general introductory class to declaring, which, judging by the tourists I had, we will also do this time because it's, it sounds like you have many of you have not had real experience with deep learning specifically. So we will start from the very beginning and then work our way up.

**[01:08 – 01:10]** There will be computer vision, of course.

**[01:11 – 01:25]** I mean I we have to give some examples and since the classes about computer vision, why not give computer vision examples but we will yeah, start from the beginning and we will try to you know, build the

**[01:26 – 01:30]** Cathedral of modern artificial intelligence from the ground up.

**[01:31 – 01:33]** As best as we can.

**[01:34 – 01:45]** So but let me begin today with a brief introduction to machine learning in general. Okay? So I don't think we will get to neural networks today.

**[01:46 – 01:48]** I hope we'll get there tomorrow.

**[01:49 – 01:55]** And finally, I got to be a host, the host. So I can now spotlight

**[01:56 – 01:58]** That's all I need it.

**[01:59 – 02:00]** Thank you.

**[02:01 – 02:12]** so let's begin by talking about, we are artificial intelligence is how we got there and today I want to maybe

**[02:12 – 02:17]** for some of you, it will be a reminder for some of you it will be new material, but

**[02:19 – 02:27]** I want to discuss like the most fundamental stuff of machine learning. Like what is it based on? What

**[02:28 – 02:50]** What is the basic Machinery that everything runs on? And it turns out that that basic Machinery is basically probability Theory. So for those of you who collect your statistics courses rejoice and we will, we will see how it all relates to to learning to training etc, etc.

**[02:50 – 02:54]** So anyway, let me start with a brief intro.

**[02:54 – 03:01]** Anyway, we live in some very interesting times. And usually, when I start a new class on machine learning,

**[03:04 – 03:37]** I have been teaching for what almost 20 years. Yeah, almost 20 years, I've been teaching learning and when I started in your class I usually start with like this historic all overview, right? And traditionally, I would begin with the picture like this one. It's just the random time line of the internet. Nothing special about this one. But, you know, I would talk about and they will talk a little bit today about how AI as a field as progressed starting from its beginning in the 1950s, then.

**[03:39 – 04:00]** 196 is the eye winter of 1970s then we go to the 80s and when neural networks reappear then we go to the 90s and 2000s with the probabilistic models and then we go to the revolution of deep learning that defines artificial intelligence today.

**[04:00 – 04:10]** So that's all well and good. And if you look at AI from this standpoint, you see like you know, a regular field of sense.

**[04:12 – 04:26]** And even if you dig deeper into some specific part of a, for example, January or whatever, you say some pretty reasonable time line. If you look at a time line from

**[04:27 – 04:29]** Before the year 2022.

**[04:31 – 04:42]** But recently, something has changed. Right recently? AI has started to progress in some

**[04:43 – 05:21]** A completely unexpectedly fast way, right? So this is a timeline. I made a couple of years ago, three years ago in the summer of 2023 and it was about the spring of 2023. If you recall, that was the time when GPT just appeared, it appeared in the late 22 but it was like not really popular for a little bit and then suddenly it blew up and then

**[05:22 – 05:37]** In the spring of 2023, like everything started appearing out once, right? I will not go through the whole time line here. It doesn't matter now, but like look at March 14th. March 14th. 2023. That was like.

**[05:42 – 05:44]** that, that was

**[05:46 – 05:48]** Yeah.

**[05:49 – 05:50]** Okay.

**[05:52 – 06:03]** Okay, so sorry technical question which I think I need to address. So can you see the presentation? Because some people say it's

**[06:04 – 06:05]** It's not.

**[06:10 – 06:19]** Let me check the presentations, but text on it. Not clear. Hmm, let me check so

**[06:21 – 06:22]** I mean.

**[06:22 – 06:25]** I, I don't want to switch to

**[06:27 – 06:32]** Sharing the presentation because I will then need to you know, go to the Blackboard and stuff like that.

**[06:32 – 06:34]** I'm gonna HD.

**[06:35 – 06:36]** All right, let's

**[06:38 – 06:46]** Okay, so let's let's do what you suggested. Let me post the presentation for you.

**[06:49 – 06:49]** It will be.

**[06:51 – 06:54]** So, it will be.

**[06:56 – 07:00]** It will take a long time to, to get it.

**[07:02 – 07:08]** To Google Classroom because I'm not in there but I will send it in chat right here, okay.

**[07:08 – 07:09]** so anyway,

**[07:10 – 07:18]** the spring it's already. So anyway, the spring of 2023 was

**[07:19 – 07:29]** Oh like this sudden Outburst of everything I related and specifically llm related. Okay, I send the presentation. It says, it's uploaded.

**[07:31 – 08:04]** And if you look at, for example, March 14th, here you see that on the exact same day. Alright. Google announced that it would be integrating llms into its workspace. It wasn't called Gemini at that point, but some of them Google didn't announce anthropic a small startup that recently, split off of Open. AI announced that it would be producing its own family of llms.

**[08:08 – 08:11]** Thought which we will know and love now.

**[08:11 – 08:28]** And but it was, but both pieces of news for completely overshadowed by opening AI, which came out and said that we are well, not yet releasing but we are announcing GPS for like the next step in this development of elements, at that point.

**[08:28 – 08:30]** and when I,

**[08:31 – 08:33]** Made this picture.

**[08:34 – 08:46]** three years ago, I called it the spring artificial intelligence and I mean, at that point three years ago it was completely possible that

**[08:47 – 08:49]** This would all.

**[08:50 – 09:32]** Still be, you know, in line with some regular development of regular science, right? So sometimes you have a breakthrough when you have a breakthrough in that in 2023, that was changed it. So, llm starts at work on, 200 have a breakthrough, you know, researchers go there. They feel in this new space with their research and then the field needs new brakes, right? So kind of progress goes by these scientific progress. Usually goes by this big steps when somebody discovers New Direction, then, it it's very quick for a while. And then it's closed down back again.

**[09:34 – 09:42]** So back then it was still possible if it would go like this but of course, it didn't and the rate of progress has not slowed down since 2023.

**[09:43 – 09:48]** we are still getting use basically every week and

**[09:49 – 09:52]** We are getting big news every month and in the field of AI.

**[09:53 – 09:59]** It's not slowing down on the contrary. It looks like it's spinning up, right? That looks like currently.

**[10:02 – 10:02]** The.

**[10:03 – 10:27]** Frontier Labs, the openai and anthropic they already are using their own models to make their own models better, right? So it's not yet the fully closed loop of recursive. Self-improvement that everybody was talking about, but I think we're getting there, right? And if we do get there, then, who knows what's gonna happen, right?

**[10:28 – 10:55]** And so we believe in some very, very interesting times. And I want to stress here because by now it's actually already not not obvious to people but I want to stress here that it was completely unexpected and very, very few people predicted this. So I recently came across this nice example. This is a book from 2018.

**[10:55 – 11:07]** Less than 10 years ago, right? So the Deep learning was already here. We already had, I don't know. Lstm reaction already had Transformers right? In 2018, we already had the Transformer.

**[11:08 – 11:16]** And the author of this book asked several prominent researchers went to the expect human-level. Artificial intelligence

**[11:17 – 11:25]** And the closest was none other than Ray quartz file, which you would expect and he predicted it in 2029.

**[11:26 – 11:31]** And that was the nearest prediction so less than 10 years ago.

**[11:33 – 11:39]** Most researchers would Place human level intelligence somewhere around, you know, 50 years from now.

**[11:41 – 11:45]** Things have changed, right? And this rate of progress keeps accelerate

**[11:46 – 11:49]** so, in this class, I hope we will actually

**[11:50 – 12:09]** Go all the way to the Motorola's nature, not unfold details. We cannot do it in full detail and rates, but we will start from the foundations of our traditional intelligence from the foundations of deep learning specifically of how neural networks work. And then we will discuss the main

**[12:10 – 12:17]** Classes of architectures of neural networks. And ultimately, of course, we'll get the Transformers, we'll get to

**[12:18 – 12:24]** Language modeling will get to the gpts and clothes of of today.

**[12:25 – 12:25]** but,

**[12:26 – 12:32]** Let's start at the very beginning, right? So I will still allow myself this

**[12:33 – 12:36]** guilty pleasure of doing a historical survey.

**[12:38 – 12:46]** Artificial intelligence is a very old idea, okay? So artificial intelligence, I mean, in a way,

**[12:48 – 13:22]** According to almost every religious tradition in the world. We are artificial intelligence, right? Because we were made in some traditions out of clay in some traditions out of some less lessons substances. But in any case we have been made by God and whatever the name of the god is, right? And we have been created with our souls with our intelligence. And so we are AI is according to the relations of the world, right?

**[13:23 – 13:25]** A more more modern.

**[13:26 – 13:37]** Kind of artificial. Intelligence ideas, can can be found in actually, Greek mythology, where, of course, whales but Hephaestus would

**[13:38 – 13:55]** Create like Android robots for himself and there were several, but the most famous was this gentle humanoid robot named Dallas. And that's actually pretty fine story. And that relates to how we view it relates to the field of as well.

**[13:58 – 14:04]** The Festus ultimately gave Talos or I think it was useful. It's

**[14:04 – 14:10]** took tiles from her Festus and gave it to to the king of Crete. I think

**[14:11 – 14:12]** and,

**[14:13 – 14:15]** on the island on the island of Crete, they

**[14:16 – 14:25]** Job of towers was to basically protect the borders, right? So tell us what would run around the perimeter of the island.

**[14:26 – 14:30]** and when tell us, so any ships approaching,

**[14:31 – 14:39]** It would take giant rocks and it would throw the giant frogs to the animation. That was his job.

**[14:40 – 15:15]** Um, what is interesting about this in my opinion is how things have how things have played out to be in terms of what's difficult and what's easy, right? So the ancient Greeks were already starting to be pretty good. At throwing big rocks to Great distances. They already had catapults, right? And then they were not very accurate, but then we got, you know, tribal Shades and then guns and then, whatever rocket launchers, whatever. So we are pretty good at hurling.

**[15:17 – 15:24]** Destruction to be distorted, with great accuracy, actually.

**[15:24 – 15:25]** but,

**[15:26 – 15:27]** The more difficult part.

**[15:28 – 15:33]** It turned out to be was to actually recognize any ships, right? So

**[15:35 – 15:38]** already, I don't know, for 400 years ago, you could have

**[15:40 – 16:06]** You could have a big and that would be pretty accurate and thinking the ship. But how would you automatically recognize first? The there is a ship on the horizon and second that the shape is here is an enemy ship and not a friendly one, right? So that's a computer vision problem and it that proved to be more difficult for Humanity to automate then.

**[16:07 – 16:09]** The Rock throwing part.

**[16:09 – 16:10]** Yes, I think pretty interesting.

**[16:13 – 17:08]** Similarly, okay, so there was AI in many different Traditions. There were the integrity and tradition. For example, there was this notion of a Golem and some wise rabbis could create golems and there. Okay? So that that didn't play out as the trajectory tradition predicted in there. There was a big difference between speech recognition and speech synthesis S&A task. So, a goal and can actually understand here. It can understand commands, it will fulfill the commands of the rabbi who created it. It will know human language, but it will never speak. So in today traditional it was like an understanding was okay for man-made constructs. But, you know, to actually speak, you had to have a soul. And of course, even the way device, Rabbi cannot create a new soul.

**[17:09 – 17:09]** So,

**[17:10 – 17:12]** so that that didn't play out as expected.

**[17:13 – 17:57]** And that was why Thomas Aquinas was the famous philosopher and the pupil of albertus Magnus the famous Alchemist. So, Thomas Aquinas was very, very upset. When his teacher albertus, Magnus actually created an artificial speaking head. And, of course, we don't know what it actually was, one hypothesis, is that it works, something like this. So it was just, you know, sound a device for transporting sound from a different room and somebody would actually speak through through the pipe. But you know, we don't really know. But what we do know is that Thomas Aquinas got very upset and actually smashed the whole thing to pieces

**[17:58 – 18:21]** Then in the Middle Ages, I won't go into details here. But you probably know there were like lots of very inventive automata, early robots, which are not quite robots in the modern sense but like, you know, human figures that can do some simple tasks automatically like poor water or something like that.

**[18:22 – 18:33]** And they were pretty inventive but they were purely mechanical not very interesting. Of course, for us what I do want to mention artists Automotive by Pierre.

**[18:34 – 18:40]** Ah, he was a Swiss watchmaker and actually the jacket row.

**[18:42 – 18:48]** Watches you can still buy. Although they are very, very expensive but it's an existing brand and

**[18:50 – 19:01]** He is like hobby on the side was making very intricate human-like dolls that would do very fine.

**[19:03 – 19:08]** Things with their hands and you know, that would actually do something interesting by themselves.

**[19:09 – 19:36]** And there was this draft Mano that would actually draw several different pictures. But what is really interesting? What I wanted to highlight was this guy, the calligrapher and the calligrapher is very similar to the draftsman because here so is using a whale to to write on a piece of paper. But

**[19:37 – 19:53]** you could actually program the calligrapher to write what you want. There was like this, I don't know a sister of Labor's or something. On the back that you would actually know you would change. You could switch some of the levers and he would write different letters.

**[19:53 – 19:59]** That, that was to my knowledge. That was the first actually programmable.

**[20:01 – 20:19]** Device right before Shakira's looms that are usually quoted as the pioneers of, you know, programming and that invented, Punch Cards Etc. But that was before, that's interesting.

**[20:21 – 20:33]** But of course, this is not AI as we understand it now, right? So there was no programming or to speak of there was no math.

**[20:34 – 21:04]** AI. That would be, I really related. And actually, I don't want to talk to much about this guy Ramen Lowe, but I mean, I usually mentioned him in Harbor space, because he's Catalan. But basically, he was an early education and you can, you know, kind of if you stretched definitions a lot, you can actually, you know, say that he did something that would later be related to AI but not really.

**[21:07 – 21:10]** Um, when when did they actually appear as a science?

**[21:14 – 21:38]** There are several starting points and usually well, basically there are two starting points that I will quote one is the 1943 paper on the mathematical models of neural activity that we will get to later when we discuss different and the other is the 1950 paper of volunteering, right? The Turing test, which I hope you have heard about.

**[21:40 – 21:40]** so,

**[21:43 – 21:48]** During was a very smart day and he was like, really genius. He did a lot of

**[21:51 – 22:10]** total breakthroughs in the field of computer science and in particular he basically invented artificial intelligence and the first question of course they had a person thinking about this stuff seriously encounters is

**[22:12 – 22:14]** Can you do an artificial intelligence like can machines think?

**[22:15 – 22:38]** And this is, this is the subject of Turing session of 1950, which I definitely recommend you read because, you know, old old research, papers are usually very hard to read. They use strange notation. They are cumbersome. It doesn't make sense. A modern textbook would be much much better would explain stuff much better but

**[22:39 – 22:55]** In this case during closet genius, right? So here's essays there, not really research. They're not so much research papers like philosophical discussions about stuff and they are still very interesting. So I definitely recommend you read the essays of hearing

**[22:56 – 23:03]** And specifically, the Turing test was in the sea on Computing, machinery. And intelligence. It was called and

**[23:06 – 23:07]** The hearing test itself.

**[23:08 – 23:10]** is very

**[23:12 – 23:13]** interesting in that.

**[23:14 – 23:42]** Like how it survived for so long, and how, and why, it's so long, right? So, you all heard about the during tests, right? So there is a church, the church is chatting in writing with an unknown entity, or with two unknown entities. And then one of the entities is a human, the other entities a computer. And basically the judge needs to

**[23:43 – 23:53]** A recognized, which was the human and, which was the computer, right? So, there are a couple of interesting points here. First note that

**[23:55 – 24:20]** It doesn't make any sense to run the Turing test once, right? So the Turing test actually kind of grew out of turing's foundational. Work on computer science on algorithms, theory of algorithms and randomized occurs. So the Turing test definitely, like, wouldn't tell you anything. If it was just one,

**[24:23 – 24:32]** If it was just one run of the experiment because of course, the judge can always just flip a coin with probability one half.

**[24:32 – 24:58]** It will be. Alright, alright, so when does a machine, when does a computer program pass, the Turing test? Not when it falls to church, once in a sense, but when it consistently makes it impossible for the church to recognize the program with any probability significantly different from one half, right? So,

**[24:59 – 25:10]** Right from the start. It's an interesting. Remark that we, we get to the realm of probability Theory. We get to the realm of randomized, algorithms, Etc. We'll talk more about that later.

**[25:12 – 25:16]** The other Intel. Okay, so now the main part

**[25:17 – 25:22]** Then I go for the founder mark. But now the main part, the main part about the Turing test is

**[25:24 – 25:36]** Unlike all other tests of artificial intelligence and I will give an example, unlike a lot of tests that you can test has actually survived for a very long time.

**[25:37 – 25:43]** So I think I have a slide on this. Yeah, so formerly the hearing test was actually passed just a year ago.

**[25:43 – 26:15]** Okay, of course, once you have stuff like gpt-4, nobody really doubted the gp4, could pass the Turing test in the original formulation, like they can fight for 10 minute chat. But you know, it was not trivial to actually run the test because of course if you're talking with a Frontier Model these days and you just ask it, well are you an AI? The model will tell you. Oh yeah, sure. I'm a language model.

**[26:16 – 26:37]** So somehow you would you would need the model to stay in character, right? And it's easier to do with small ones but small ones would not fall anyone. So okay, so there were some problems with actually writing the Turing test but once people did, of course, of course, the models passed, but it's very recent news. It's 2025 and

**[26:38 – 26:41]** The original Turing, test was a 1950.

**[26:42 – 26:42]** and that's

**[26:43 – 26:56]** And that is very cool and very surprising in AI because to be honest, AI as a health is has a very long history of moving. The goal posts.

**[26:56 – 27:24]** So, for example, the example that I want to give in 19 in the 1970s, there was this guy, Ellen Newell will meet him later. And here wrote a very nice paper. Like, what is the state of AI now and where are we going like this position paper? That would you know, Define where where how the filter

**[27:26 – 27:26]** and,

**[27:27 – 27:56]** Here at the end, he wrote well, okay. Did we have the hearing test? But of course, the Turing test is not really actionable in the 1970s. It wasn't, of course, you cannot expect AI models to pass the Turing test and there is no, there can be no progress on the Turing test, right? So it's not like you can full 5% of the judges than 10% of the judges than 20% of the judges doesn't work like that. Either you full humans or you don't

**[27:57 – 27:58]** and,

**[28:00 – 28:03]** So Harold. Okay, we need some kind of

**[28:05 – 28:08]** other tests, it will be

**[28:09 – 28:18]** Numerical in the sense that you could actually measure the result but also that will actually reflect something inherently.

**[28:20 – 28:30]** Important about intelligence. So like if the machine passes, it means that we actually are making progress towards artificial general. Artificial intelligence

**[28:31 – 28:36]** Sounds. But what is his example? His example was let's take

**[28:37 – 28:38]** Chess.

**[28:38 – 29:38]** And he actually argued for like, a page that well, chess is a very nice candidate because it's numerical, you can do, like, you can, you can play against each other play against humans to have an ill or rating. It's, it's measurable, that's completely true. But on the other hand and Chassis is easy to program in the sense that it's a finite game with, you know, fixed rules blah blah. But on the other hand, chess is such a human game. You have to, you know, understand the flow of attack and defense on the chairs or to have to maybe real have a model of the other person's mind and understand what the other person thinking about when he's making this move. So that you can predict presentations and maybe subvert them etc etc. So he was making this very plausible sounding argument. That chess is a

**[29:38 – 29:40]** Is a good middle ground.

**[29:41 – 29:47]** and then as you all know in 1997 deep, blue bit Casper off,

**[29:48 – 30:08]** And I think the last match where humans had a chance was 2001. Vladimir kramnik had a few matches against the best computers of the time and he actually like almost one at some point. I think he missed the maiden one, very famously at one of the games but

**[30:09 – 30:10]** but after that,

**[30:11 – 30:38]** It was completely hopeless. Alright, so after like 2001 there was no question who is better chess and by now or even buy, you know, 2010 to 2015 there was even nothing humans could help with, right. So for a while, there was this field of sand tower chess, where a human with the help of a computer would play better than just a computer, but that is also a thing of the past.

**[30:39 – 30:49]** But did they AI researchers in 1997 or 2001? Did they say? Oh okay, so we have the hi now.

**[30:50 – 30:51]** The test has been passed.

**[30:52 – 31:00]** Of course not right. What what we all said? Collectively is a felt was oh, okay. So you bitches well chest doesn't count

**[31:02 – 31:02]** Chest is too easy.

**[31:03 – 31:14]** Chess is, you know, you can just do a research and the research already gets you halfway to the best players doesn't count.

**[31:15 – 31:16]** Let's take go.

**[31:17 – 31:30]** The game of Go much better. You cannot really. I mean, it's still finite, it's still combinatorial, but you can never do a search train go because there are too many possibilities. The branch in factor is to be

**[31:31 – 31:46]** that's true. You cannot have a meaningful complete search stream go. It's like when in chess you have like 10 reasonable moves at most and going we have 50 to 100 reasonable moves. So it's completely impossible to do the depth search.

**[31:48 – 31:48]** but,

**[31:49 – 31:59]** Alphago happened, right? And then Alpha 0 happened and of course in though computers in 2000, 16 17 also became hopelessly veteran here.

**[32:00 – 32:05]** Well, did humans say now Alpha zero is the age? I

**[32:06 – 32:27]** Of course, not humans said, well go that's count and, and that is, and that's the history of a in a way and people still do that. People still say for some reason that llms don't count and they try to invent reasons, why Helen's don't count. But the hearing test actually stood the test of time

**[32:28 – 32:41]** So there was no moment in the 1980s. When somebody would say, oh, I passed the Turing test with a stupid script, so it doesn't count. No, they didn't happen. Why? So my main point here because

**[32:42 – 32:54]** What is the Turing test really about? It's about yes it's about natural language processing in a big part so it's about being able to talk in a natural language to a human in writing.

**[32:55 – 33:01]** But not only about that, right? The point of the hearing test is that

**[33:02 – 33:28]** When you have a free-form chat as a post to a chess game as a post to question answering or whatever you can talk about anything, right? You can you can actually, I don't know. You can introduce computer vision or at least 3D modeling into the Turing test. You can say, oh, hey, look, we are talking on the computer, right? So can you

**[33:29 – 33:44]** Tell me, what's on your desk, what, what's in front of you? What's on the left, what's on the right? What do you see, what's in the room? Can you please walk out of their own? Describe what you see? And then come back, and yeah, sure, you have no, no way to check of that true. But to actually make this picture consistent,

**[33:45 – 33:56]** The Entity on the other side would need to kind of understand the 3D World, right? And natural language is complete. In the sense that

**[33:56 – 33:57]** You can talk about anything.

**[33:58 – 33:59]** Right.

**[34:00 – 34:00]** so,

**[34:02 – 34:04]** Why am I spending so much time on this? Because

**[34:05 – 34:12]** in a way, this is exactly the reason why modern llms are so great. Right? So,

**[34:14 – 34:32]** All that modern llms basically are trained to do. I think we'll get there at the end of the class and I will explain it to you in more detail but the base of the lamps for they are actually learning to do is just predict the next token and text. Right. What is a language model? Language model is a

**[34:33 – 34:39]** Is a machine that predicts the next word, the next token in natural language.

**[34:40 – 34:40]** That's it.

**[34:41 – 34:41]** but,

**[34:42 – 34:43]** To predict the next token.

**[34:44 – 35:10]** You need to understand a lot of stuff, right? You don't not only do you need to understand how language works, but then you, so this, this will get you partly their part of the way there. But then, after you, understand how language Works itself in it to understand how the world works, right? So if you say, if the text says, theorem blah, blah proof, no.

**[35:11 – 35:14]** And that you are supposed to predict the next token. Well,

**[35:15 – 35:29]** maybe you need to prove the theorem first, right? And if the text says, I've been to Paris last month and I visited, I visited the museum.

**[35:30 – 35:38]** And then you need to predict the next word. Well, now you have to understand which museums are in Paris, right? So,

**[35:40 – 35:40]** it's

**[35:42 – 36:17]** Natural language includes everything. Well, maybe not exactly everything like it doesn't include stuff like robotics for example. So robotics is a very different field because there is no huge set of books on. I don't know. What is the angle that you need to? Rotate your joints in order to pick up a cup from the table, right? So this this you need to understand from other sources, but nature language is a great source of information for virtually everything.

**[36:18 – 36:33]** And and that's the reason why llms keeps surprise us. They keep getting this uncovering, this new capabilities that actually mostly come simply from predicting the next word and in text.

**[36:35 – 36:42]** All right. Thanks so much time on the Turing, test. Sorry. One, last point, a finite appointments during tests, I hope.

**[36:42 – 36:54]** So if you look at the hearing test, at this competition where the machine is supposed to talk like a human, you know, it has immediately that it is completely totally unfair.

**[36:55 – 36:57]** It's completely unfair to the computers.

**[36:58 – 37:02]** First of all, Imaging, the reverse during tests.

**[37:02 – 37:12]** Imagine that we are changing in text and I a human. I'm trying to pass for a computer in this dialogue.

**[37:13 – 37:18]** How would you uncover that I'm a human. What would be the question?

**[37:28 – 37:34]** What could you ask me so that you would immediately know that I'm not a computer and I would have no way to pass for one.

**[37:42 – 37:45]** Can you give me example of lemon pie?

**[37:50 – 37:52]** Yeah. So why would it distinguish him from computers?

**[37:53 – 37:58]** If you would give me this information, I would imagine actually

**[37:59 – 38:01]** Understand it, your llm.

**[38:02 – 38:02]** Why?

**[38:07 – 38:08]** actually, I don't know why, but

**[38:08 – 38:09]** why?

**[38:10 – 38:18]** If you, for example, some assistance, if you need some help and you can ask, for example, to McDonald's chatbot.

**[38:20 – 38:28]** Give me example of 115 or give me some program in Python, I would mean in the center your llm, you're not a real person.

**[38:29 – 38:45]** No way. But I mean, imagine the reverse human there were hearing tests, like I'm talking to you in chat and I am a person. It's me, but I'm trying to post as a computer, right? So I'm trying to convince you that I am a computer.

**[38:46 – 38:51]** Hmm. What would you ask? So that you immediately would realize that I'm not a computer.

**[38:56 – 39:02]** It was trying. Oh my God, very complicated one.

**[39:03 – 39:14]** Yeah, for example, sure. So, if you ask me what's, I don't know. 37 to the power of 23. I have no idea, right? And it would take me a long time to figure it out.

**[39:14 – 39:17]** For a computer is Trivial, right? So,

**[39:21 – 39:27]** So we would never pass the reverse during tests we humans, right? Even for the computers of the 1950s, we would not.

**[39:28 – 39:28]** but,

**[39:30 – 39:43]** But that's okay. So this is, of course, like inherently unfair But ultimately, you know, we do want the whole purpose is to teach computers to be like, humans. Not to teach humans to be like so, okay, that that's okay.

**[39:44 – 39:51]** but there is also one like more subtle unfairness in the hearing test, which is well,

**[39:53 – 40:01]** the computer needs to pose as a human. The computer needs to, you know, represent itself for somebody else.

**[40:02 – 40:05]** The human doesn't need to do that. The human just needs to be himself.

**[40:06 – 40:06]** that's,

**[40:07 – 40:24]** Unfair too, right? So they originally hearing test, if you read the essay, The Originals hearing test was actually formulated as follows. It should be a church. A German church, trying to distinguish between a computer posing as a woman.

**[40:25 – 40:27]** And the man posing as a woman.

**[40:28 – 40:31]** So that like everybody would need to play somebody else.

**[40:32 – 40:39]** And we need to to walk and in the show. So, you know, so some as a different person as you can.

**[40:41 – 40:50]** And you can understand why this little detail got lost in the, in the history of the hearing test. But but it was there, I think it's also pretty fine.

**[40:51 – 40:53]** All right, so that was this hearing test.

**[40:54 – 41:34]** But that's kind of on the negative side in the sense that of course in the 1950s, there was no way to pass the Turing test not able to to be closed and but it kind of got people thinking and the actual like positive field of AI as a science, when you actually tried to build stuff emerged in 1956, it was so called Dark Wolf workshop at Dartmouth, obviously. And it was organized by these four very famous researchers.

**[41:35 – 41:46]** John McCarthy was the early programming language which is a guy invented list. Marvin Minsky was the guru of neural networks.

**[41:47 – 41:58]** I hope you all know, Cloud Shannon, the author of information Theory, and the senior Rochester. I keep forgetting what he did, but he builds some computer at IBM. I'm very early and very famous computer.

**[41:59 – 42:02]** And the 1956.

**[42:03 – 42:18]** Workshop. Had what I think I always liked the quote it because I think it was the most ambitious Grant proposal in history. And in the 20th like this we propose a two-month study of artificial intelligence by 10 people.

**[42:19 – 42:20]** In the summer, blah blah.

**[42:22 – 42:42]** We will attempt to find how to make machines use natural and, which is find extraction of Concepts solve problems. Now, reserved from humans and the cells. This machine learning, right? We think significant advancement in one or more of these problems as possible. If a careful is select a group of scientists works on it for a summer.

**[42:43 – 42:48]** Okay, and they were founded. They got together, they did

**[42:52 – 42:52]** Conduct the workshop.

**[42:54 – 42:54]** and,

**[42:55 – 43:11]** But this this grant proposal of course they didn't actually do anything like they didn't actually solve any of these problems but they kind of understood how difficult they were, but still the 1950s and their relationships was a period of very high expectations.

**[43:11 – 43:40]** It was the Golden Age of Science Fiction. Everybody was, you know, expecting Androids to walk in a few years was expecting Androids to walk around to bring you coffee to talk to you. In human language, etc. Etc. That was like that was the time when science fiction was starting to what was expected to to become a life very soon.

**[43:42 – 44:04]** What people actually did the actual progress was, of course, very limited, but it was still very good progress. So, for example, there was this logic theorist program, which I will not talk about in detail but it was a fair improver back in the day. It was thought that the important part was to teach AI launcher to teach a math.

**[44:05 – 44:28]** Now we kind of understand that it doesn't work that way, but it was a very good proverb for its time, it's actually successfully reproved. A lot of fundamental, a lot of the fundamentals of mathematics and it kind of oh, this early high expectations,

**[44:28 – 44:34]** And there were some other examples doesn't matter. But basically what happened in the early 1960s,

**[44:36 – 44:38]** The optimism didn't work out.

**[44:38 – 44:41]** Okay. So and

**[44:42 – 44:56]** Sorry, I don't have it on the slide but like the the main example, the primary example why people was very disillusioned in AI in the 1960s was a fail permit on machine translation.

**[44:57 – 45:09]** Okay, so people actually expected in the 1950s that they would write a program that would translate from English, from Russian to English, believe it or not.

**[45:11 – 45:12]** And that it would work.

**[45:13 – 45:49]** And of course it was completely beyond the ability of computer science at that point. So in 1961 or 62, there was this big report that said well okay, so machine translation basically doesn't work, we need a lot more research. Let's regroup and then, you know, the government, got the solution, they stopped, giving out grant for AI. And when you don't give out, grants for research, researchers move to other fields. So ultimately what we had in the 1970s is now known as the AI winter.

**[45:50 – 46:21]** And there I will enter means that there were very few people actually working on AI on artificial intelligence. It was believed to be kind of too hard impossible and inaccessible with current techniques which was true in the 1970s. So it's not like people are wrong. The only thing that actually was happening were expert systems and expert systems. They're kind of also AI, but there was a very specific kind of and you try to

**[46:23 – 46:27]** When you try to perform probabilistic reasoning on.

**[46:29 – 46:41]** A small Snippets of the main knowledge so to speak. So for example, okay, so the main example is probably my sin which was 1976 system.

**[46:42 – 46:49]** For this for Diagnostics, Medical Diagnostics based on what tests.

**[46:49 – 47:09]** And like, what is a blood test? What are the results of a blood test? It's basically a big table of 15 numbers, right? You have red blood cells, white blood cells hemoglobin. I don't know what was iron, whatever. All sorts of chemicals found in the blood.

**[47:10 – 47:10]** and,

**[47:12 – 47:22]** An experienced doctor and experienced physician can look at the blood test and say, oh, is that this is, oh, is this disease, right? So that's the diagnostic problem, but

**[47:23 – 47:36]** However, experienced The Physician is however I don't know whether he is a genius diagnosed like Dr. House it actually

**[47:37 – 47:54]** Complete is completely impossible for a human to just sit down and write, you know, a function of 50 variables that would just give you the diagnosis. Human brains. Don't work like that. Even if you kind of know what to look for, ETC. What you can actually, formulate is not a

**[47:55 – 48:17]** General unifying function of everything but you can formulate some local, heuristics. Like if the red blood cell count is high and the iron is low then it's that and if they don't know alcohol content is 20% and its this and so on and so forth. So

**[48:20 – 48:24]** you can ask doctors to give you this kind of local heuristics rules.

**[48:26 – 48:50]** And then the AI question. So you do not question the rules, the rules are like given to you from from a trusted source so to speak. But the AI question is, how do you combine the rules? So now you are given a new blood test and there are all sorts of problems. Like, okay, you have like 450 rules and 20 of them, kind of apply.

**[48:52 – 49:10]** But also they don't like apply. They kind of apply because the rule is again, not a mathematical function, a human doctor cannot do that the role. A role is something like if the red blood cell count is high and what does hi mean? Medically.

**[49:11 – 49:12]** Well.

**[49:13 – 49:34]** This like this high is definitely high, this highest definitely not high. But what about this? What's in the Middle? Where is the trash hole? Probably, there is no fresh will probably, it's a continuous function. So there are all sorts of difficulties here and that's what people were doing in the 197 just I won't spend time on that because that's not our subject definitely.

**[49:34 – 49:35]** and,

**[49:36 – 49:55]** And then what actually happened. So let me skip almost to the present. What actually happened was in the 1980s. People, again, got back to neural networks. That was the in the 1980s you already had.

**[49:57 – 50:13]** Convolutional networks and recurrent networks, and multi-layered net deep networks. So, basically, you could have deep learning in the 1980s 1990s but he didn't mostly for technological reasons.

**[50:14 – 50:17]** so people already kind of realized in neural networks are cool, but

**[50:18 – 50:27]** they didn't really work because there was not enough date and not enough compute to make them work, you need more and it all came together. And

**[50:28 – 50:41]** The middle of the 2000s. So to say, so in 2005 to 2006 to 2007, several different Labs, specifically Jeffrey, hinton's lab, and Joshua been just left. They actually

**[50:42 – 50:48]** kickstarted this deep learning Revolution and that's when everything came together. So by that time,

**[50:49 – 50:59]** Due to the internet due to, you know, increased computational capabilities. You already had enough data to make neural networks work.

**[51:00 – 51:00]** and,

**[51:02 – 51:24]** You already you also started to have enough compute, we started to have enough computational power to train, large enough, neural networks. And like the final step was actually going from CPUs to gpus. So we'll, we'll discuss it later when we discuss neural networks actually, but

**[51:25 – 51:58]** It's kind of obvious that if you look at neural networks that everything you do, there is highly parallelizable and it was a very natural idea when gpus actually appeared. And it was a very natural idea to switch from CPUs, which are like a few very fast course. Like four course, four gigahertz each switch to gpus, which are much slower but with hundreds and thousands of cores and that that gave you like this.

**[52:01 – 52:24]** Final boost that made deep learning actually work and starting from the late 2000s. Deep learning has neural networks have been by going from subfield of subfield to machine learning and they have been setting state of the art in a lot of different fields. So we'll discuss that later.

**[52:26 – 52:27]** and now,

**[52:29 – 52:36]** Let me and the historical part here and now about what machine learning actually is. So

**[52:39 – 52:44]** how do you define what it means to learn, right? So what is learning?

**[52:45 – 52:46]** And I will.

**[52:47 – 52:52]** we will get to a much more technical definition a bit later, but

**[52:53 – 53:15]** If you open some old textbook from the 1990s, you could find the definition of like this. So, like a computer program, learns with accumulating experience regarding a class of tasks. T, and the performance measure P is performance on this task, improves it against your experience. So it doesn't say much, it sounds very trivial, but

**[53:16 – 53:22]** Here. So what this, I think important here on this slide is that when we are talking about learning

**[53:23 – 53:24]** We have to have.

**[53:25 – 53:40]** A performance measure, right? So we have to have some kind of number that goes up or down whenever it needs to go. Because if we don't, then we will never understand. Did we learn something or not? Right. So in a way,

**[53:42 – 54:01]** They have half of deep learning is about inventing the loss functions. It's about inventing this objectives. What is the number that we want to get down? What how do we Define the error? So that when we minimize the server, we actually get what we want.

**[54:02 – 54:12]** Right? Sometimes it's very easy but sometimes it's kind of non-trivial and sometimes as part of part of the science and this, this is the conclusion from this.

**[54:14 – 54:15]** and,

**[54:17 – 54:24]** Also, I think you have all seen at some previous class or somewhere in your life, you have seen this.

**[54:26 – 54:31]** Main like, taxonomy of machine learning problems. Let me

**[54:32 – 54:51]** A go through it. Still, we will not talk too much about it later in class because we will mostly exclusively. We will be in here in the supervised learning part. But let me just mention what kinds of functional learning problems. There are

**[54:52 – 54:52]** so,

**[54:55 – 55:02]** technically machine learning problems are divided into supervised learning unsupervised, learning and reinforcement learning.

**[55:03 – 55:35]** And supervised learning is what we intuitively think of when we think of Machinery, like I need to build a classifier the distinguishes cats from dogs on a picture, right? So how do I build the classifier and distinguishes case from dogs? I get a data set of pictures and for every picture I Mark with, or it's a cat or a dog and then I trained a classifier to distinguish between them, right? So I think it's a good.

**[55:36 – 55:40]** It's a good time to actually start.

**[55:41 – 55:43]** Doodling, on the board.

**[55:44 – 55:44]** so,

**[55:46 – 55:47]** In supervised learning.

**[55:48 – 55:50]** Okay, there is the whole machine learning.

**[55:51 – 55:53]** and in supervised learning,

**[55:57 – 55:58]** You have.

**[56:01 – 56:03]** Yeah, one sec. I'll be

**[56:03 – 56:06]** I'll make a little more comfortable. So I

**[56:07 – 56:07]** Write better.

**[56:08 – 56:11]** So, in supervised learning the data set.

**[56:12 – 56:16]** Consists of pairs of X and Y.

**[56:18 – 56:27]** Right. So, for example. So X is the input. And why is the output that you want to get?

**[56:28 – 56:31]** And your machine learning model.

**[56:32 – 56:44]** Is actually a machine. It's let's say a black box for now, will get there later but it's it's a machine that takes the input.

**[56:45 – 56:49]** And produces some function of the input that is supposed.

**[56:50 – 56:52]** To look like the output.

**[56:53 – 56:57]** Right? So we are trying to make the input.

**[56:58 – 57:23]** The interim, we are trying to convert the input into the output for example if we are doing Simple, classification, simple, binary classification. So there are cats and dogs here then. Probably a f of x is like a number from 0 to 1 and if it's close to 1 then we say it's a cat, if it's close to 0 then we say it's a dog so it's kind of its supposed to be the probability of a cap.

**[57:23 – 57:28]** But notice that it's the probability of a cat.

**[57:29 – 57:33]** For a given picture, right? So it's the probability of a cat given X.

**[57:35 – 57:38]** And that's the whole point of supervised learning.

**[57:39 – 57:52]** So the point of view provides learning amazingly speaking is to learn, whatever that means, we'll get there much later, but it's to learn the conditional distribution. P of Y given X.

**[57:53 – 57:56]** so, we are always assuming

**[57:57 – 57:59]** that we will have the input.

**[58:00 – 58:08]** The classifier, the distinguishes gets from dogs, cannot draw you and you get picture. It's not supposed to

**[58:09 – 58:17]** It always presumes that you have a picture at the input and then with this picture, you do stuff.

**[58:18 – 58:34]** So computer vision works like that right in computer vision, you always assume that you have a picture of the input. Well maybe a set of pictures maybe video whatever but you have some high dimensional very complicated.

**[58:35 – 58:36]** Input.

**[58:37 – 59:07]** And you're supposed to, you know, break the input down and to some answers into the answers to the questions that you're interested in. And it's not necessarily specification. There may be more interesting problems. Like object detection. We'll talk about those in class since since we are doing computer vision here. But overall, you are trying to take a complicated input and convert it to some relatively simple out. So that's what you provide learning is about.

**[59:08 – 59:15]** And you, and when you collect the data set for supervised learning, you always need to have the correct answers.

**[59:16 – 59:26]** So sometimes and the computer vision, unfortunately, very often, it means that you need to have some very complicated labeling.

**[59:26 – 59:30]** All right, and labeling is very difficult and expensive.

**[59:30 – 59:45]** So we'll talk about that when we get there, but for for classification, it's not that expensive. But for things like segmentation proper labeling is extremely expensive. So we need to, we will need to somehow, you know,

**[59:47 – 59:50]** do with relatively small data sets.

**[59:51 – 59:55]** But that's only the first part, right there is all. So

**[59:59 – 1:00:01]** So there is this other field.

**[1:00:03 – 1:00:03]** where,

**[1:00:04 – 1:00:05]** There is no why?

**[1:00:06 – 1:00:08]** There is no correct answer.

**[1:00:10 – 1:00:13]** The data set is just a set of something.

**[1:00:16 – 1:00:19]** And the big question is, what are you supposed to do with it, right? So,

**[1:00:20 – 1:00:25]** okay, so now we have a data set of pictures but the pictures, the image is

**[1:00:27 – 1:00:34]** They're not labeled in any way. So what, what are we even trying to do? What, what is the goal here?

**[1:00:35 – 1:00:45]** Actually turns out that you still can have a meaningful go and you can still do the stuff that will be very, very useful for Downstream problems. Like classification, Etc.

**[1:00:46 – 1:00:52]** ah, and usually what answers is doing is

**[1:00:54 – 1:00:55]** Something called.

**[1:00:56 – 1:01:03]** Let's call it dimensionality reduction. So reducing the size.

**[1:01:04 – 1:01:05]** Of x.

**[1:01:06 – 1:01:07]** Compressing it.

**[1:01:08 – 1:01:19]** So that on the one hand you can press X down to something. I still have a black box but now the output is not

**[1:01:20 – 1:01:28]** Some small known thing, but the output is, let's say a vector of numbers, right? And X is still

**[1:01:29 – 1:01:30]** Let's say a picture.

**[1:01:32 – 1:01:33]** but,

**[1:01:35 – 1:01:37]** now, the goal is not to

**[1:01:40 – 1:01:47]** Classify executed him. But the goal is to compress X down from its original size.

**[1:01:48 – 1:02:10]** And we will, actually, I think we will talk about this more. But images are big, right? And if you think think of images, as sets of numbers, they're pretty big sets of numbers, right? So like how many numbers question to you, how many numbers are there in a one megapixel photo?

**[1:02:10 – 1:02:11]** It's one megapixel.

**[1:02:12 – 1:02:13]** Is how many pixels?

**[1:02:32 – 1:02:35]** No. Come on. Don't try to compute gas.

**[1:02:39 – 1:02:40]** Yeah.

**[1:02:43 – 1:02:47]** Well, almost right. So

**[1:02:48 – 1:03:02]** Megapixel is not a million pixels and for functional. It's one 100024 square right? So it's a power of two but what, whatever. Okay, it's it's close to a million and how many numbers is that?

**[1:03:06 – 1:03:09]** like, if I take an image of one megapixel,

**[1:03:10 – 1:03:16]** And I say that, okay, I want to view it as a set of numbers. What is the damage? How many numbers are there?

**[1:03:35 – 1:03:36]** How many numbers in a pixel.

**[1:03:40 – 1:03:52]** Come on, guys, you're in for a computer vision. Number three numbers, right? Right, there are three numbers in a pixel. So a one megapixel photo, which is not that large is 3 million numbers approximately.

**[1:03:53 – 1:03:53]** Right.

**[1:03:54 – 1:04:00]** So if you think about this space of possible images,

**[1:04:02 – 1:04:03]** it's a huge space.

**[1:04:04 – 1:04:06]** It has a huge dimension.

**[1:04:06 – 1:04:18]** Nothing works in that damage, right? So it's it. And if you think about like, what is the structure of the set of images in that space?

**[1:04:20 – 1:04:21]** Well, we

**[1:04:22 – 1:04:29]** Collective Humanity. Have absolutely no idea, right? So, it's very, very difficult. We have no idea how to how to describe this. So,

**[1:04:31 – 1:04:48]** It's some very complicated manifold in this in a huge space of Dimension. 3 million, right? So like imagine, we can't imagine, but think of this set of like real photographs,

**[1:04:49 – 1:05:06]** Among all possible pixel values in dimension, 3 million. What is the structure of this set, right? This this is completely incomprehensible. I can only say that it's an open set, right? Because if you have, if you have a real photo and you

**[1:05:07 – 1:05:26]** and you move every pixel by a very, very tiny amount. Nothing changes, right? So it's still a real photo, but what actually distinguishes, real photos from from random noise, we have no idea, right? And we have no idea what is the geometric structure of this menu?

**[1:05:27 – 1:05:29]** It's probably extremely complicated.

**[1:05:31 – 1:05:40]** So what is ANSI provided in trying to do here? It's trying to map this extremely complicated manifold of Freelancers.

**[1:05:40 – 1:05:42]** To dimension.

**[1:05:44 – 1:05:48]** Much smaller. Let's say, I don't know. 500 that's just a number out of

**[1:05:51 – 1:06:06]** Okay, once we are out of nowhere doesn't mean anything. But basically to project this huge space of images down to a more manageable, still large but more manageable space where hopefully,

**[1:06:07 – 1:06:08]** It will be.

**[1:06:09 – 1:06:14]** More comprehensible either to work with manifold, right?

**[1:06:17 – 1:06:22]** So that that's usually the idea of once you provide learning, right? So you want to

**[1:06:24 – 1:06:36]** To do what in machine learning is called feature extraction. You want to feature extraction or representation learning, representational learning?

**[1:06:36 – 1:06:59]** You want to map a bit object, like a name image to a small, much smaller object, like vector of numbers, but you want to do it in a way that would not lose important stuff, right? So you can just take the first one, 100 pixels from here, that that's not gonna work. You want to map it and such a way that

**[1:07:00 – 1:07:08]** You actually, you know, are able to answer interesting questions in this space of these in the small space.

**[1:07:09 – 1:07:17]** For example, in the main fall of real images, you see will be able to distinguish cats from dogs.

**[1:07:18 – 1:07:43]** So like cats are here and dogs are here. And now all of a sudden in this space, in in these 500 dimensional space, there is actually like a linear hyperplane, the linear surface separating, cats from dogs and it's very easy to separate kids from dogs over there over here. Like dogs are this part and cats are this part?

**[1:07:44 – 1:07:49]** And there is absolutely no way to disentangle. Okay, right.

**[1:07:51 – 1:07:52]** so,

**[1:07:53 – 1:08:15]** Point usually a fancy provides learning, compressed down, make it more manageable and hope that in this more manageable little space. You actually can have a relatively, same simple, machine learning models, doing the stuff that you actually want.

**[1:08:16 – 1:08:36]** So like this kind of compression is never the end go, right? You don't want this vectors by the cells. We want them for some ultimate purpose and but the thing is, we are not, we don't we don't fix this purpose and answer and we don't know, maybe we'll use it for that. Maybe we'll use it for this right now. We just want to get good features.

**[1:08:39 – 1:08:43]** How do we do that? Well actually, there is a pretty simple answer.

**[1:08:45 – 1:09:04]** Which is very common in deep learning specifically. So while we are talking about this, let me let me tell you. So of course, we cannot have a data set with the correct disease, right? There are no correct this. We have no idea. What is the correct representation in this low dimensional space.

**[1:09:05 – 1:09:11]** So, how do we verify that this Black Box is doing anything meaningful?

**[1:09:12 – 1:09:29]** How do we, what? So here we have in supervised learning, we have a data set is accessing wise and we can just run the Black Box through the examples that we have and check that we got. We get correct answers, is it?

**[1:09:30 – 1:09:32]** Over here. There are no correct answers.

**[1:09:33 – 1:09:46]** But we cannot as we will see. So we cannot train a neural network without a loss functions, right? We cannot train in your own network without some kind of goal specific numerical goal that we want to optimize

**[1:09:48 – 1:09:49]** So what would be the goal here?

**[1:09:50 – 1:09:50]** and,

**[1:09:51 – 1:10:00]** There can be different answers but in deep learning one. Very common idea is to do a thing called an autoencoder.

**[1:10:03 – 1:10:06]** Which works like this. So I have this big thing.

**[1:10:08 – 1:10:08]** X.

**[1:10:10 – 1:10:19]** I get it through my neural network, okay, that doesn't matter if it's in your own network. Through my first machine learning model, which is called the encoder

**[1:10:20 – 1:10:21]** and I get,

**[1:10:22 – 1:10:22]** The vector Z.

**[1:10:25 – 1:10:31]** But let's not stop there, let's say, okay, so how do I verify that compression is good?

**[1:10:32 – 1:10:41]** Well, compression should. First of all, compress down to a smaller size. Here, it's by definition, I choose the size of the myself.

**[1:10:42 – 1:10:42]** but,

**[1:10:43 – 1:10:52]** What does it mean to compress something? And not just pick random numbers? It means that from the compressed object I can reconstruct back to the original.

**[1:10:54 – 1:11:14]** That's, that's the whole point. Like it wouldn't be, it wouldn't be a very good archive tool it. If it would produce just random bits and you would have no way to recover the files, right? So the whole point is to compress down in such a way that you can decompress back

**[1:11:15 – 1:11:20]** So we add the decompressor, right? We add the decoder part.

**[1:11:22 – 1:11:24]** Which takes the Z.

**[1:11:24 – 1:11:26]** And tries to restore.

**[1:11:27 – 1:11:28]** The original image.

**[1:11:30 – 1:11:32]** Let's say it's X hat.

**[1:11:32 – 1:11:37]** So, X is the input. And X hat is the final output.

**[1:11:38 – 1:11:59]** So the decoder is probably also in your own network. The decoder is also a complicated neural network, right? It's like a generative model takes in something like that. Looks like random noise just number and should produce a beautiful cat picture, right? So it does make our task more difficult. Sure, but now,

**[1:12:00 – 1:12:11]** We have a very easy way to say what we are looking for, right? So now we know exactly what was function, should be because the result should be just, you know,

**[1:12:12 – 1:12:31]** Similar to the input, that's it. And you can Define what's function basically like X head, minus x squared like just a square deviation in the pixels. That's okay. That's a very common loss function and in ordering colors. So,

**[1:12:32 – 1:13:15]** Uh and so this kind of idea compressed and then decompress back, we will encounter it in class A couple of times and it's it's a very natural thing to do in unsupervised learning. So when you when you are just trying to make sense of of your inputs of your data set, how do you what is your goal? You're trying to find structure inside what does it mean to find structure? Well, actually in reality, it usually means to project down to a smaller space where you can see the structure more clear, right?

**[1:13:18 – 1:13:18]** and,

**[1:13:20 – 1:13:22]** if you've heard the fancy provides during before,

**[1:13:23 – 1:13:23]** You.

**[1:13:24 – 1:13:42]** Probably heard about the like the example that was characteristic that was decentral, example of fancy provided for a long time. I think now, what encoders in the nationality reduction in general are more important but for a long time. They the main example of a fancy learning was clustering.

**[1:13:44 – 1:14:02]** A clustering. We we want we want to talk about that much out of scope for us. But clustering is this problem. You probably have like an intuitive understanding of it. When you have some points, some objects, right? And your task is to

**[1:14:04 – 1:14:15]** Split them into groups clusters, so that points inside the cluster are similar to each other close to each other and points across different pastors, a different right?

**[1:14:16 – 1:14:25]** so, the only thing I want to say about clustering is that, it's exactly, you can view it as the extreme form of dimensionality reduction,

**[1:14:26 – 1:14:31]** So, it's clustering clustering.

**[1:14:33 – 1:14:34]** Is all. So,

**[1:14:35 – 1:14:47]** Means also taking a large object and compressing it down to Z in a smaller space. But now the dimension of the space is 0

**[1:14:48 – 1:14:50]** okay, so we are compressing

**[1:14:52 – 1:15:00]** we are compressing each point to the label of its cluster and there is like just a finite state of the different labels

**[1:15:00 – 1:15:28]** And you can view it like that, and it's a very natural view of clustering. You you can press down to a discrete finite set of points and then if you do it in such a way that decompression is as faithful as possible, still, right? So the whole point of clustering is that you kind of want to replace all points in the cluster, by its Center, or by the cluster label, and then you will be able to deconstruct the points as best you can.

**[1:15:30 – 1:15:37]** and yeah, okay again explaining too much time on super wrestler in but yeah it's it's useful I think and

**[1:15:38 – 1:15:44]** If in supervised learning, we were learning the distribution people. Why even X

**[1:15:45 – 1:16:11]** In unsupervised learning, we are just trying to learn pox there is no why, right? So and how does it map to this Auto encoder or to the classroom picture or whatever? What does it mean to learn the distribution? Well here in the auto encoder part, it would probably mean to learn to sample from the distribution.

**[1:16:12 – 1:16:17]** So here you would say that D is kind of like random noise.

**[1:16:19 – 1:16:25]** And the decoder. Converts the random noise into X that

**[1:16:26 – 1:16:31]** Is supposed to be from the distribution of get pictures, right? So,

**[1:16:32 – 1:16:39]** I don't think we'll get to this kind of analysis and plus, but again, useful to keep in mind. So,

**[1:16:41 – 1:17:00]** in supervised learning, we always have an X, we always have the input in answer, you provide learning, and we are trying to describe the exit itself. And very often, it means that we are actually learning a generative model that can produce new samples of access.

**[1:17:01 – 1:17:04]** In the case of pictures that can draw new pictures.

**[1:17:06 – 1:17:06]** Okay.

**[1:17:07 – 1:17:09]** And finally, there is the third guy.

**[1:17:10 – 1:17:12]** Which we will not talk about at all.

**[1:17:12 – 1:17:14]** We just called reinforcement learning.

**[1:17:19 – 1:17:34]** And yeah, I think, I mean, unfortunately, I cannot make this class about everything. So, let me skip praying, forcement learning, but basically, it's let me just say, if you were reinforcement, learning is the

**[1:17:35 – 1:17:39]** The sap field of machine learning where there is no data set in the beginning.

**[1:17:40 – 1:17:44]** so, instead of the data set you have your model,

**[1:17:46 – 1:17:50]** B being like an agent in an environment.

**[1:17:51 – 1:17:51]** and,

**[1:17:52 – 1:17:58]** The data set is ultimately the experience of living in this environment.

**[1:17:58 – 1:18:08]** So, for example, if you're learning to play chess, then your agent is just does not have a data set of correct moves.

**[1:18:09 – 1:18:25]** And it is not just trying to, it does not have a data set of all possible positions from chess games and trying to compress them down, like an answer provides learning. Know what's your agent? What what's your model is probably doing? Is it's playing?

**[1:18:26 – 1:18:36]** chess against itself, for against earlier, versions of itself for against other models, or whatever and learning to place it goes from the signal of Juan

**[1:18:37 – 1:18:44]** Right? So that that's how reinforcement learning works. You leave in your environment, you get

**[1:18:46 – 1:19:00]** A rewards that are in the case of Chess, it's simple. That award is who won in robotics, the reward, maybe more complicated but whatever you get rewards from the environment,

**[1:19:01 – 1:19:02]** and ultimately,

**[1:19:03 – 1:19:04]** You.

**[1:19:06 – 1:19:37]** Get rewards from the environment and ultimately you learn to maximize this rewards so there are you learn to behave? You learn a policy for behaving and environment. So such that the report gets maximized actually. It's a pretty different topic. It has some pretty different approaches from supervised and answering. So we will not be talking about it and in class I hope you will have a separate class and RL at some point. It's it's a very beautiful field.

**[1:19:38 – 1:19:42]** All right, so we discussed this.

**[1:19:43 – 1:19:55]** I don't, I think we'll skip this practical things like, cross validation and stuff. Maybe someone will talk to you about this and in the Practical part,

**[1:19:56 – 1:19:58]** Yet, I mention it reduction.

**[1:19:59 – 1:20:01]** Um, all right.

**[1:20:03 – 1:20:03]** so,

**[1:20:04 – 1:20:05]** I think.

**[1:20:06 – 1:20:06]** Now.

**[1:20:08 – 1:20:09]** Is a good time to have a break.

**[1:20:10 – 1:20:21]** We have come to the end of the intro part. Oh, yeah. And sorry. I should have started with this. I forgot to talk to you about the the class itself and a structure.

**[1:20:24 – 1:20:40]** Basically, unfortunately, I'm not able to come to Barcelona this year. So, I'm teaching online, and my colleague, Alex Davidoff will be with you offline at on campus.

**[1:20:41 – 1:20:44]** I will be delivering lectures and

**[1:20:46 – 1:20:53]** it's it's not what I would advise to do. But for logistical reasons we will have a lot of lectures at the start.

**[1:20:54 – 1:20:59]** So we will have three days of lectures today, tomorrow, and Wednesday.

**[1:21:00 – 1:21:03]** and I hope we will make some good progress and

**[1:21:05 – 1:21:05]** Get to.

**[1:21:09 – 1:21:18]** And and and have a good start so that Alex will will have something to work with when she begins on Thursday.

**[1:21:19 – 1:21:34]** Ah and then I think we will mostly alternate like this, like two lectures, to practical sessions and so on. And ultimately we will even it out. So I will be mostly await next week and then then I'll come back for for the final picture.

**[1:21:35 – 1:21:36]** Okay.

**[1:21:37 – 1:21:38]** so,

**[1:21:40 – 1:21:44]** Let's have a break. Are there any questions about the first part or the structure or whatever?

**[1:21:46 – 1:21:52]** How long a break do you need like offline? It's usually have an hour but maybe online hit that much.

**[1:21:53 – 1:21:56]** How long would you like 15 minutes? Okay.

**[1:22:08 – 1:22:22]** Okay, so let's say 15 to 20 minutes and it's 11, sorry, 10 for you write 1035. So on 10:50, then 55, let's continue. Okay, right.

**[1:25:19 – 1:25:20]** oh,

**[1:35:24 – 1:35:26]** You.

**[1:43:59 – 1:43:59]** All right.

**[1:44:01 – 1:44:02]** Let's continue.

**[1:44:06 – 1:44:20]** In the first part while you're getting back, I'll do a quick recap in the first part. We discussed.

**[1:44:21 – 1:44:32]** The history of artificial intelligence, highway to, you know, came to to be the earlier ideas like the Turing test Etc.

**[1:44:34 – 1:44:34]** and,

**[1:44:37 – 1:44:37]** Specifically.

**[1:44:39 – 1:45:00]** On point specifically, something actually useful for our machine learning class. We discussed the main and like the most common taxonomy of machine learning problems, right? This distinction between supervised learning Concepts learning Country, and

**[1:45:02 – 1:45:08]** In the second part. Today, I want to talk about what learning actually means.

**[1:45:09 – 1:45:09]** and,

**[1:45:12 – 1:45:23]** I have always understood it and the recommend you to understand it through the biasm perspective, through the probabilistic perspective. I will explain what I mean.

**[1:45:24 – 1:45:26]** but first of all,

**[1:45:27 – 1:46:27]** Like for those of you who have had, I don't know probability Theory classes in your University is over in Harbor space. You're probably kind of not very happy to hear that. Machine learning is pure probability Theory from start to finish because usually when, when I say probability Theory to my students, they get a little bit scared because a probability Theory class is some, usually, some very involved, difficult mathematical stuff about measure theory about, you know, you start with the sigma algebra of measurable, burial sets on in the euclidean space and then you're introduced your probabilities and measure and then you, and then what the expectation is is

**[1:46:27 – 1:46:35]** Already pretty difficult. And what the conditional expectation is extremely difficult and, you know, it's it's awesome abstract theorem Etc.

**[1:46:36 – 1:46:54]** We won't need any of that stuff. I'm not saying forget it. Don't forget if you know it but we want any of that. We need, you know, as there is a saying, I think by one, is it in, education is what remains after forgotten. Everything you thought

**[1:46:54 – 1:47:09]** So this this is exactly this kind of thing. What we will need in probability theory is the intuition that remains, after you forget all about the theorems and you actually

**[1:47:11 – 1:47:26]** You know, you you actually get this basic intuition of what probabilities about, so what is it about? It's about random variables, right? And random variables. There are discrete random variables like coin tosses.

**[1:47:28 – 1:47:30]** I like pointers or

**[1:47:31 – 1:48:07]** should have prepared coin tosses, and die rolls and stuff like that. And if you have just created set of, if you have a great set of William price, and if you have a discrete set of outcomes, then the probability of this outcomes should sum to one and that's your probability, right? That's your invariable. And then, you can have continuously in the variables where they

**[1:48:08 – 1:48:35]** It instead of probabilities of outcomes, you have the density function, right? And at this point, if you had a probability Theory class, he will tell me, oh, wait, but not every probability has a density, right? And maybe probabilities, including important ones, are cannot be characterized by the density and therefore, you need measure Theory. Blah, I forget about that machine learning. We only deal with kind of standard and

**[1:48:36 – 1:48:55]** Easy probabilities. So everything that we will ever discuss will, of course, have a density. And in that case, the timing to one means taking an intro, right? Taking an integral over the

**[1:48:58 – 1:49:10]** probability space. And again, there will be no exotic probability spaces here. Only the real line art of some power on the eclipse.

**[1:49:12 – 1:49:40]** Um, and the things that we actually need in machine learning card is basic intuitions and the base the very basic definitions of probability Theory, right? So you can have and okay. So now what I really do, hope that on this slide there is nothing new for you. If there is I recommend, you know, repeater probability Basics a little bit because we will be using some of that.

**[1:49:40 – 1:49:44]** But okay, I'll just go through this very quickly.

**[1:49:45 – 1:49:52]** If you have two events, two random variables, they can happen at the same time.

**[1:49:54 – 1:50:01]** Then you can Define The Joint probability, right? The effects. Why should let me switch?

**[1:50:02 – 1:50:08]** Better to explain it more interactively, right? So

**[1:50:10 – 1:50:10]** The.

**[1:50:11 – 1:50:42]** Ah, okay. So there are random variables characterized by their probability Mass functions. P of x if they are discreet. So, like, just what is the probability of every outcome on the die from 1, to 6, or by density functions. Like, I don't know, maybe it's concentrated from 0 to 1. We'll have an example like this today, then it's some function. Whose integral is supposed to be

**[1:50:45 – 1:50:46]** Equal to 1.

**[1:50:47 – 1:50:56]** And this is the density function for a random variable that samples you a number from 0 to 1, right?

**[1:50:58 – 1:51:13]** And if you have two random variables and you can have their joint probability of XY. So P of XY is something like P of x equals to something and why equals to something else.

**[1:51:14 – 1:51:30]** Right? So if you have your joint probability and you want to get on the marginal, it's called the marginal probability of the probability of one of the X and y's, then you need to kind of sum this over. Why?

**[1:51:30 – 1:51:34]** It's not a very formal way to write about.

**[1:51:34 – 1:51:50]** I hope you understand what I mean. So if you have like, P of x equals, a, and equals to something else and you want to get, what is the probability of just povert equals a you need to sum over all possible values of Y, kind of makes sense.

**[1:51:51 – 1:51:53]** and from The Joint probability,

**[1:51:56 – 1:52:01]** we get the notion of conditional probability. This is the most important notion for machine learning.

**[1:52:02 – 1:52:04]** So what is conditional probability?

**[1:52:05 – 1:52:17]** Conditional probability P of x given why? Right? Is the probability that X let's say is equal to something. Given that we know the value of y.

**[1:52:18 – 1:52:18]** Right.

**[1:52:20 – 1:52:20]** and,

**[1:52:22 – 1:52:25]** Formerly, it's very easy to Define. Formulate, just

**[1:52:28 – 1:52:54]** With the joint probability of XY and we decompose it into P of x given y times P of Y that this formula has some name like four probability for something like that. I keep forget, it doesn't matter. But the point is, this is the definition of conditional probability. So P of x given Y, is defined as P of X Y, divided by P of Y.

**[1:52:55 – 1:52:56]** All right.

**[1:52:57 – 1:53:04]** And we'll have a lot of conditional probabilities later today and tomorrow. Probably.

**[1:53:06 – 1:53:28]** And if you look at this definition, if you look at this decomposition of the joint, probability into the marginal in the conditional, then, you know, just that you can do it both ways, right? You can start with why? Like we did here first. We, I mean, okay. One way to read this formula is how do you sample X and Y?

**[1:53:30 – 1:53:41]** Well, you can start with why you can sample wife first from its own distribution. And then you already know what, why is, and you need to sample X. Even this very

**[1:53:43 – 1:53:43]** Or.

**[1:53:44 – 1:53:50]** You can start with X, you can first sample, X, and then sample. Why give an X

**[1:53:51 – 1:53:52]** You can hear this way.

**[1:53:53 – 1:53:59]** But it's still I'm a formerly. It's still the definition of conditional probability, just the definition of pure white given next.

**[1:54:00 – 1:54:06]** But if you combine this formula's, you see that like this they amount to the same thing to the Joint. Poxy.

**[1:54:07 – 1:54:18]** And this is where you get like the most important formula in the whole world, definitely in the whole machine learning. But I think it's wider than that.

**[1:54:19 – 1:54:23]** and that formula is well P of

**[1:54:24 – 1:54:29]** Y given X is p of x given y times P of Y.

**[1:54:31 – 1:54:33]** Divided by P of x.

**[1:54:34 – 1:54:38]** Right. This is the best bass roll.

**[1:54:38 – 1:54:40]** Or base formula.

**[1:54:41 – 1:54:42]** and,

**[1:54:43 – 1:54:55]** The way we presented. Now it's completely trivial, right? It's just directly basically follows in one line from the definition of conditional probability, but like,

**[1:54:56 – 1:55:00]** In effect philosophical. Um, that's

**[1:55:01 – 1:55:04]** Basically, how reasoning works?

**[1:55:05 – 1:55:23]** Our actual real reasoning, not logical derivations, where there are no probabilities and all facts are known for sure. In real life, we sell them know facts for sure, right? In real life, it's all about balancing, the probabilities and weighing in the evidence

**[1:55:24 – 1:55:30]** And this is like the database formula underlies, how you account for evidence.

**[1:55:31 – 1:55:34]** How you actually, you know, take something into account.

**[1:55:35 – 1:55:37]** We will definitely discuss it more.

**[1:55:38 – 1:55:47]** But before we do that, one last thing, there is also this very important notion of Independence.

**[1:55:48 – 1:56:01]** And basically two random variables are independent. If P of X Y, their joint. Probably joined entity. Is it will appear effects times Poe for

**[1:56:02 – 1:56:09]** so, if P of X Y, decomposes into the products of individuals or individual probabilities,

**[1:56:11 – 1:56:26]** In this case, there is the conditional Australia, right? So, basically, the same thing, you can say, pox given Y is equal to just pay of X, right? The conditional Australia. It means that

**[1:56:27 – 1:56:40]** P of x p of X does not depend on the value of why, right? That, that's why it's called Independents. So to wearables are in development, which basically means that you can sample them separately,

**[1:56:41 – 1:56:46]** You'll get the same result like two coins that you toast in a row.

**[1:56:50 – 1:56:50]** and,

**[1:56:53 – 1:56:56]** Let's get back to the bias formula and let me actually.

**[1:56:58 – 1:57:00]** Just first be stated in.

**[1:57:01 – 1:57:04]** Slightly different notation and then we'll discuss it.

**[1:57:05 – 1:57:11]** So, let's let's call it the main formula of machine learning.

**[1:57:12 – 1:57:15]** And let me write it like this P of theta given d.

**[1:57:16 – 1:57:22]** Equals P of D, given Theta times P of theta.

**[1:57:23 – 1:57:29]** Divided by P of D. Okay. It's the same formula, right? I just changed The annotation.

**[1:57:30 – 1:57:35]** But I hope you kind of now and understand what this notation.

**[1:57:37 – 1:57:43]** It's supposed to represent. So now D is the data.

**[1:57:43 – 1:57:45]** These data set.

**[1:57:46 – 1:57:46]** Right.

**[1:57:49 – 1:57:50]** And Theta.

**[1:57:51 – 1:57:52]** Are the model parameters?

**[1:57:55 – 1:57:56]** Theta.

**[1:57:58 – 1:58:00]** Is what we actually want to learn.

**[1:58:00 – 1:58:24]** So for if we are talking about a neural network, we want to learn the weights, right? And notice that it's not the exact value of the way. It's, it's a whole distribution of it, so it's, we will get back to that. But for now, let's just say Theta is the model parameters Theta is the way it's a linear regression. That's going to be our first serious example or Theta is

**[1:58:25 – 1:58:38]** The weight. So when you're all Network or Theta is just the probability of the coin that we are trying to learn. So let's say we have okay, here is my point, it has to say and

**[1:58:39 – 1:58:44]** I can toss it and I can get some results.

**[1:58:45 – 1:58:46]** and,

**[1:58:48 – 1:59:01]** The data will be the set of outcomes, the set of results of what I'm getting from the coin tosses and the parameters will be just a probability of getting heads, right? So the whole point of machine learning,

**[1:59:01 – 1:59:02]** Is to.

**[1:59:04 – 1:59:10]** understand to learn the model parameters from

**[1:59:11 – 1:59:22]** the data, right? So we have a set of outcomes for some stochastic process, for some random process where there is some inherent randomness.

**[1:59:23 – 1:59:24]** And we want to understand.

**[1:59:26 – 1:59:34]** What was governing this process? What are the parameters that went into this process? This is the whole idea of machine learning, everything else is basically commentary.

**[1:59:35 – 1:59:39]** And the biased theory is the main tool.

**[1:59:40 – 1:59:47]** For this. Why? What is so special about this? So let's let's discuss what we have in this formula.

**[1:59:48 – 1:59:49]** On the left.

**[1:59:50 – 1:59:51]** I have P of Fate again.

**[1:59:53 – 1:59:58]** D is called the posterior probability or the posterior distribution.

**[2:00:00 – 2:00:02]** Posterior means.

**[2:00:02 – 2:00:08]** After the fact upper stereo, after evidence has been included.

**[2:00:09 – 2:00:09]** and,

**[2:00:10 – 2:00:42]** That's what it says, right. So it's very, very intuitive. I get some data and I want to understand what I now think about Theta. How my understanding of theta has changed given data. After I have taken the data set into account, that's the posterior distribution. I want to I want to this is my goal in learning, right? So, okay, the final goal will be doing predictions. We'll get to that later. But the intermediate though, is learning what I can about, Theta from the

**[2:00:45 – 2:00:45]** Okay.

**[2:00:47 – 2:00:53]** And usually there is no way to to get to this distribution directly without going through this formula.

**[2:00:54 – 2:00:56]** So how do we get to this distribution?

**[2:00:58 – 2:01:03]** Well, the best role tells us that it's the product of two things, basically.

**[2:01:04 – 2:01:05]** it's the product of

**[2:01:07 – 2:01:08]** P of D given Theta.

**[2:01:10 – 2:01:10]** Which is.

**[2:01:12 – 2:01:13]** Called the likelihood.

**[2:01:15 – 2:01:18]** So, what is p of D given Theta?

**[2:01:18 – 2:01:20]** It's the

**[2:01:21 – 2:01:22]** um,

**[2:01:23 – 2:01:29]** it's the probability or that usually the density of getting a specific data set.

**[2:01:30 – 2:01:44]** Given the parameters given the model parameters, I'll make a coin tossing example. In a second, it will be clear, but basically, when you define a model in machine learning, you usually Define the likelihood. This is the easy part.

**[2:01:45 – 2:01:51]** The likelihood is what you get from just, you know, listing your assumptions and writing them down as formulas.

**[2:01:53 – 2:02:02]** And the main point of the best rule is that the likelihood is not enough. You also need the third part, this guy,

**[2:02:03 – 2:02:05]** we just called the prior distribution.

**[2:02:07 – 2:02:08]** Or just the prior.

**[2:02:09 – 2:02:12]** The prior is.

**[2:02:13 – 2:02:21]** Just be often without any d. Right? And what does it mean for Social Security and means what were we thinking about Theta?

**[2:02:22 – 2:02:23]** In advance.

**[2:02:24 – 2:02:28]** before we start to get before we started,

**[2:02:30 – 2:02:31]** Getting.

**[2:02:33 – 2:02:38]** D, right? So PPO Theta. Without any d.

**[2:02:40 – 2:02:44]** And I will make an extensive example in a minute. So,

**[2:02:47 – 2:02:53]** the bias formula basically tells you if you want to get the posterior distribution, if you want to

**[2:02:54 – 2:02:58]** Incorporate D into your thinking of theta.

**[2:02:59 – 2:03:00]** You need to take.

**[2:03:00 – 2:03:05]** what you thought about it before and multiply it by the likelihood of the

**[2:03:06 – 2:03:07]** so, for example,

**[2:03:08 – 2:03:11]** For example. Oh sorry. I

**[2:03:13 – 2:03:32]** I wanted to say, I didn't talk about the denominator but I forgot to say that I didn't talk about it so they did not nominate her in data. I didn't talk about it. It's usually called the full probability or the evidence probability, or something like that. And

**[2:03:33 – 2:03:41]** Mostly of this is not really important for us in machine learning, why? Because it doesn't have any fades.

**[2:03:42 – 2:03:45]** okay, so in machine learning are

**[2:03:46 – 2:03:49]** P of D is usually completely inaccessible by itself.

**[2:03:50 – 2:04:02]** So in stead of writing, the full bias row actually, usually be used like this P of theta given D is proportional to P of D, given Theta times P of theta.

**[2:04:03 – 2:04:05]** so, this means proportional,

**[2:04:06 – 2:04:16]** And what does proportional mean? In this case, it means that well, P of theta given is should be probability distribution, right? So, it should integrate to one.

**[2:04:17 – 2:04:17]** So,

**[2:04:18 – 2:04:32]** Almost always actually completely always. I know. No exceptions, P of D. They only way to compute P of D is to make it a normalizing constant for the numerator. So P of D is always just this.

**[2:04:37 – 2:04:42]** Okay? And in some special cases you might be interested in puberty.

**[2:04:43 – 2:05:02]** Yes. But usually what you do is what you doing, machine learning deep learning. Usually you're just interested in, let's suppose maximize in this with respect to Theta, and if you maximize this, it's the same as maximize on this and you don't care about the constant, right?

**[2:05:03 – 2:05:12]** So we'll get to that a bit later so the denominator is is complicated but usually not really necessary. So we want to talk about that too much.

**[2:05:12 – 2:05:15]** Okay, now example.

**[2:05:16 – 2:05:20]** Let's learn a coin to us. Okay.

**[2:05:21 – 2:05:25]** Here is a coin or what passes for one. It has two sides.

**[2:05:26 – 2:05:27]** And I can toss it.

**[2:05:28 – 2:05:31]** So how many parameters does a coin have?

**[2:05:32 – 2:05:34]** What is the size of the vector Theta?

**[2:05:35 – 2:05:36]** Can you tell me?

**[2:05:54 – 2:05:56]** How many numbers do you need to?

**[2:05:57 – 2:06:00]** Define a coin with to say, it's

**[2:06:20 – 2:06:25]** Okay, maybe I'm not asking the question clearly enough. So

**[2:06:27 – 2:06:28]** Bitcoin is a

**[2:06:30 – 2:06:33]** stochastic process, right? It's it's random variable.

**[2:06:34 – 2:06:38]** I toss it, I get either heads or tails with some probabilities.

**[2:06:39 – 2:06:42]** So how many numbers do I need to Define this probabilities? How many parameters?

**[2:06:54 – 2:07:01]** What are the parameters for a coin? What what probabilities do you need to fully understand the contest?

**[2:07:04 – 2:07:04]** Maybe just

**[2:07:09 – 2:07:21]** Yeah precisely, of course. So in a coin has just one parameter very, very easy. The simplest example, we can think of. So let's say Theta is the probability of heads, okay?

**[2:07:22 – 2:07:25]** Then the probability of Tails will be what?

**[2:07:30 – 2:07:34]** minus 8 says,

**[2:07:35 – 2:07:46]** and this is our first example, our first illustration of this probabilistic view of machine learning and

**[2:07:47 – 2:07:51]** Now you can start seeing why the likelihood is very natural.

**[2:07:52 – 2:07:53]** So what is the likelihood now?

**[2:07:54 – 2:08:04]** The likelihood is this is p of D given Theta. Like what is d? D is the data. So it's the sequence of outcomes.

**[2:08:06 – 2:08:15]** D is like I've been tossing this coin several times. And I got like, heads, Tails, heads heads Heads, tails,

**[2:08:16 – 2:08:18]** Tails, whatever. Okay.

**[2:08:19 – 2:08:20]** so,

**[2:08:23 – 2:08:25]** P of D given Theta.

**[2:08:26 – 2:08:32]** Is very easy to Define it directly follows from from just the model itself.

**[2:08:33 – 2:09:02]** I just need one additional assumption, which is by the way, very important. It's true throughout the whole machine learning and every model, it's it works. I need an assumption of conditional Independence, which didn't talk about that, right? So Independence is like this and conditional Independence is when, let's say excellent, why are conditionally independent given Z if this holds, right? So this is conditional Independence.

**[2:09:04 – 2:09:07]** A conditional Independence.

**[2:09:09 – 2:09:25]** So we need the assumption that different data points are conditionally independent, given the parameters and again, sounds very complicated, very messy, but it's very natural. So like if I already know what is the probability of heads,

**[2:09:25 – 2:09:28]** Then different pointers are independent.

**[2:09:29 – 2:09:36]** I post the coin again and again, I get the same probability of heads. That's the basic assumption, right?

**[2:09:37 – 2:09:38]** so,

**[2:09:38 – 2:09:51]** in this case, it means that P of D given Theta is decomposed and to P of like D1 given Theta times P of D2, even Theta bla bla times P of D and giving

**[2:09:53 – 2:09:56]** and what is p of D12, blah blah given Theta.

**[2:09:57 – 2:10:03]** It's the probability of one outcome of one sample and data set.

**[2:10:04 – 2:10:09]** One sample on the data set is one point us. Either heads or tails,

**[2:10:10 – 2:10:24]** So this is our P of small D given fate, right? Actually to make it formerly correct. Let me just put Faith here from the very beginning. Why not?

**[2:10:26 – 2:10:41]** All right, so this is like Theta is the probability of head. So what is the probability of heads? Given the data is the probability of heads, it stated. What is the probability of tails? Even that the probability of heads is Theta? It's 1 minus 8, right?

**[2:10:44 – 2:10:45]** So, over here.

**[2:10:46 – 2:10:49]** Everyone of this mod is either head or tails?

**[2:10:50 – 2:10:50]** Right.

**[2:10:52 – 2:10:52]** and,

**[2:10:54 – 2:10:58]** Okay, let's let's work through an example. So let's say that, this is my data set.

**[2:10:59 – 2:11:04]** So D is heads, Tails, heads heads Heads, Tails, tails.

**[2:11:06 – 2:11:08]** What is p of D given Theta? And

**[2:11:10 – 2:11:10]** Can you tell me?

**[2:11:22 – 2:11:23]** The actual number.

**[2:11:25 – 2:11:26]** Well, not the number the formula.

**[2:11:28 – 2:11:34]** the probably have had even data multiplied by the probability of

**[2:11:34 – 2:11:42]** Tails, even their own and so on. Okay. And what is it?

**[2:11:45 – 2:11:50]** like we know, what is the probability of heads and tails to the power of

**[2:11:51 – 2:11:52]** number of,

**[2:11:54 – 2:11:57]** Heads that you. Okay, let's say four.

**[2:11:58 – 2:12:00]** one minus Delta to the power of

**[2:12:03 – 2:12:12]** Number of Tails number of trails or n minus number of heads. Right? Right, exactly. So the and this is the likelihood,

**[2:12:13 – 2:12:13]** Okay.

**[2:12:15 – 2:12:30]** So, this is basically always the case and machine learning. The likelihood is easy. The likelihood is well, okay, maybe it's not easy. It may be very difficult complicated for me, but the likelihood is like our model itself.

**[2:12:30 – 2:12:37]** We when when I say we Define emotional learning model, usually what it means is we Define like

**[2:12:38 – 2:12:43]** we Define the assumptions that let us write down. This kind of formula.

**[2:12:45 – 2:12:55]** So for the coin, what were the assumptions there was the Assumption? Well the Assumption like the model of the process there are two outcomes they are usually exclusive.

**[2:12:56 – 2:13:08]** One of them has probability Theta. The other correspondingly has probability 1 minus Theta and this basic assumption that their conditional independent given Theta, which is always the case in machinery.

**[2:13:10 – 2:13:10]** so,

**[2:13:11 – 2:13:14]** This is this is the likelihood of a coin for you, okay?

**[2:13:15 – 2:13:17]** And what do we want to do with it?

**[2:13:18 – 2:13:18]** In machine learning.

**[2:13:19 – 2:13:28]** Well, there are some things we can do but while we only have the likelihood, the only thing we can do is the likelihood is try to maximize.

**[2:13:28 – 2:13:33]** okay, so the first like type of

**[2:13:34 – 2:13:40]** optimization problems that arises the first type of tasks that we sold from generating is

**[2:13:43 – 2:13:45]** finding the maximum likelihood hypothesis.

**[2:13:47 – 2:13:56]** Like fate ml, let's say is Theta that maximizes P of D given Theta.

**[2:13:58 – 2:13:58]** Right.

**[2:14:01 – 2:14:01]** Okay.

**[2:14:02 – 2:14:04]** Let's do it for the coin.

**[2:14:05 – 2:14:18]** Okay, so let's maybe not work with the specific numbers, four and three, it doesn't make much sense. Let's say in general, we have our data set is and

**[2:14:19 – 2:14:20]** Hats.

**[2:14:20 – 2:14:22]** And M tails.

**[2:14:23 – 2:14:36]** Right? So we have P of D given Theta. Just like you said, you already said it. It's fated to the number to the power number of heads and 1, minus Theta to the power number of Tails, okay?

**[2:14:37 – 2:14:40]** So, how do you maximize it with respect to Theta?

**[2:14:44 – 2:14:45]** How do maximize stuff?

**[2:14:53 – 2:14:54]** And you.

**[2:14:59 – 2:15:10]** Yeah, it sounds very difficult, but okay, in this case it's gonna be pretty easy. So let's take the derivative. Okay, the likelihood over Theta, can you tell me there is a

**[2:15:21 – 2:15:24]** Man guys, you can do it for a polynomial.

**[2:15:32 – 2:15:34]** Let me try and

**[2:15:42 – 2:15:43]** Here, you forgot.

**[2:15:45 – 2:15:46]** Yeah. Yeah.

**[2:15:47 – 2:15:54]** alright, so first the derivative of the first Factor right times the second Factor, then

**[2:15:55 – 2:15:58]** Minus that in our n.

**[2:15:59 – 2:16:00]** And oh, sorry.

**[2:16:02 – 2:16:10]** Hey, you're right. You're right. And one minus that and minus 1. Okay. Did you forget anything else or did I forget it and you said it.

**[2:16:12 – 2:16:13]** What's missing?

**[2:16:16 – 2:16:17]** M. Yeah.

**[2:16:19 – 2:16:20]** Oh, okay.

**[2:16:21 – 2:16:24]** Okay, and now we created this 0.

**[2:16:25 – 2:16:43]** Right. So let's not waste time and asking you to collect the terms. That's too easy for you. So we can put this out at the brackets, right? And in the brackets we have and times one minus 8 minus M times the time, right? Yeah.

**[2:16:44 – 2:16:46]** And that is equal to 0.

**[2:16:47 – 2:16:50]** So in here, we have like an

**[2:16:50 – 2:16:54]** - and plus M times Theta.

**[2:16:57 – 2:16:57]** Okay.

**[2:16:59 – 2:17:05]** And here and then we get the roots of this equation, which are theta equals 0.

**[2:17:06 – 2:17:07]** Theta equals 1.

**[2:17:09 – 2:17:12]** And also theta equals n divided by n possum.

**[2:17:14 – 2:17:22]** Okay. So the first question, it's, it's an easy equation. The first is equation is what, what's wrong with 0 and 1?

**[2:17:24 – 2:17:26]** What's wrong with zero and one? Why is it not the maximum?

**[2:17:37 – 2:17:38]** This is like, all the solutions.

**[2:17:42 – 2:17:44]** Why can't obvious Solutions be correct?

**[2:17:46 – 2:17:57]** It could be correct, but if you have only tails and only have oh yeah, okay, sure. But in this case, let's say we have both how we are finding

**[2:17:58 – 2:18:28]** That's the solutions. I said the check secondary condition. If you do it, you'll find out. Then it is actually a minimums and yeah, that's true. That's true. Let's not check the second order conditions, that's too much work. Let's just cheat our way through it. And notice that theta equals 0 and theta, equals to 1 give you zero likelihood, right? And if they give you zero likelihood, then obviously it's not the maximum because in between you get positive like

**[2:18:29 – 2:18:34]** So that's obviously minimum maximum doesn't count.

**[2:18:36 – 2:18:39]** And this leaves us this guy, right?

**[2:18:40 – 2:18:49]** So we got our first result about the coin, right? We have the maximum likelihood hypothesis which is and divided by n plus I'm

**[2:18:50 – 2:19:06]** Okay, so far so good and this is probably what, I don't know. Your first class on probability Theory would tell if you have a coin, you want to learn as parameter you toast the coin, you divide, the number of heads by number of experiments.

**[2:19:08 – 2:19:10]** Of coin tosses and you get your estimate for the probability.

**[2:19:12 – 2:19:14]** Completely correct. This is the maximum likelihood hypothesis.

**[2:19:16 – 2:19:22]** and again, if you recall, your probability classes, you will know that like

**[2:19:24 – 2:20:06]** In many cases, or at least, I mean, I think in modern textbooks, they do it already differently. But in all textbooks, like failure on probabilities some classical textbooks, you would get probability kind of introduced in this way. You would get probability introduced as well. There is a system that gives you a random result and then you run it infinitely many times and you get some outcomes, you count, how many outcomes you have you divide by the total number of outcomes and asked the total number gets to Infinity this fraction gets to the probability.

**[2:20:07 – 2:20:13]** And that's kind of the definition of probability from from some standpoint.

**[2:20:14 – 2:20:32]** And of course for a coin at all works. Perfectly there is no catch here. Indeed, if you keep talking the coin and you keep getting results, this fraction will not oscillate between 0 and 1. It will converge to the probability of heads. Everything is completely true.

**[2:20:34 – 2:20:39]** Ah, but here is a question. Here is a more interesting question for you.

**[2:20:40 – 2:21:03]** So let's say this is a coin, it has two sides. I can toss it and let's say okay I was showing to you something but let's forget about it let's say this is the first time I post this coin ever, I just took it out of my purse that's that's the first time I ever encountered this time and let's say I toss it. Let's do it.

**[2:21:06 – 2:21:07]** Okay, I got tails.

**[2:21:09 – 2:21:10]** so, at this point,

**[2:21:11 – 2:21:13]** What is my data set?

**[2:21:14 – 2:21:15]** My data set.

**[2:21:16 – 2:21:18]** Is just Tales.

**[2:21:19 – 2:21:20]** What is my?

**[2:21:21 – 2:21:22]** Likelihood function.

**[2:21:24 – 2:21:27]** My likelihood function is one minus Theta.

**[2:21:28 – 2:21:28]** Right.

**[2:21:30 – 2:21:37]** What is the maximum. Likelihood hypothesis for this? Where is this function? Maximized.

**[2:21:40 – 2:22:06]** Well, there is a first of all there is an interesting formal problem here and that. Oh now I just have a linear function. It gets it goes to Infinity. There is I mean there is no maximum no, minimum basically, if I just look at it formally and forget that it's a coin Theta. Ml should be like negative Infinity.

**[2:22:07 – 2:22:07]** Right.

**[2:22:11 – 2:22:12]** In a way, it's true.

**[2:22:13 – 2:22:27]** In a way, it's true. This formula in the electrical function. Indeed, does not care. That 80s is a coin data is a probability, right? So there is nothing in this function that says oh data should be from 0 to 1, right?

**[2:22:28 – 2:22:32]** So we have to kind of introduce it, impose it as a constraint.

**[2:22:32 – 2:22:43]** So far kind of arbitrary. But okay, let's do that. Let's do that. Let's say we know that our fate is a probability so it should be between 0 and 1.

**[2:22:44 – 2:22:47]** Then what is the maximum likelihood hypothesis between 0 and 1?

**[2:22:48 – 2:22:48]** Tell me.

**[2:22:57 – 2:22:59]** If we make it zero, right? Yeah.

**[2:23:00 – 2:23:04]** So now, the maximum likelihood hypothesis is exactly 0.

**[2:23:06 – 2:23:15]** The math checks out? It's correct. I mean, it's a very hard to make a mistake here, but what does it actually mean? Like, what's my conclusion? What did I learn?

**[2:23:16 – 2:23:20]** I took a coin, let's say it's a real coin. I took out of pocket.

**[2:23:21 – 2:23:24]** And I toasted once I got tails.

**[2:23:25 – 2:23:31]** And now my conclusion is that I will keep getting Tails. Always

**[2:23:33 – 2:23:34]** that doesn't make any sense.

**[2:23:35 – 2:23:36]** Right.

**[2:23:37 – 2:23:40]** I mean, even if I didn't know about coins like

**[2:23:41 – 2:24:03]** I kind of have this intuition that coins are approximately fair, right? So say, it should be something like one half. Probably not, exactly. There is nothing. Exactly in this world but something nearby. Right. But even if I did not have this situation, if I didn't know anything about coins still I mean come on. I have two options and I made one experiment.

**[2:24:04 – 2:24:14]** Obviously, we'll get one of the options, right, there is no other way. So like after one experiment, my maximum leg would hypothesis will always be either zero or one.

**[2:24:15 – 2:24:16]** Depending on what I got.

**[2:24:18 – 2:24:23]** Which means that I should always conclude that, I will keep getting just one result.

**[2:24:24 – 2:24:25]** It doesn't sound.

**[2:24:26 – 2:24:26]** Correct.

**[2:24:27 – 2:24:31]** It doesn't sound like a conclusion that we should actually make.

**[2:24:32 – 2:24:32]** Right.

**[2:24:34 – 2:24:35]** So, what's missing what's wrong?

**[2:24:37 – 2:24:38]** What do you think is wrong here?

**[2:24:40 – 2:24:46]** The math is correct. It's in the maximum like hypothesis but it's not needed.

**[2:24:47 – 2:25:03]** More experiments. Turning it good? Yes. Of course if I want to like make fate a more make more precise estimate of the I will need more experiments. That is correct. And again your statistic classes will probably tell you how many experiments you need, right?

**[2:25:05 – 2:25:05]** But here's the thing.

**[2:25:06 – 2:25:07]** Here is the important thing.

**[2:25:08 – 2:25:10]** There is.

**[2:25:10 – 2:25:15]** As I said before, I started talking about, this example, there is no difference in the limit.

**[2:25:16 – 2:25:31]** So, in the limit, the maximum likelihood hypothesis will get to the true value of theta as n and M, go to infinity and everything will check out and all the time, telling you right now will not matter.

**[2:25:32 – 2:25:34]** so, if we have this,

**[2:25:36 – 2:25:47]** Possibly infinite series of experiments if we can just toss the coin again and again there is no problem and we don't need to have this discussion. That's fine.

**[2:25:48 – 2:25:53]** but thing is in practice, we do not live in the limit,

**[2:25:54 – 2:26:09]** In practice, when we are talking about machine learning, we start with some data set, right? We have as much data as we have. And usually, in machine learning, there is no easy way to to get more date.

**[2:26:10 – 2:26:15]** If there was then, a lot of problems would be much easier, right? So,

**[2:26:16 – 2:26:21]** in machine learning, we are weak, we have our d,

**[2:26:22 – 2:26:39]** And we cannot really change it, right? And I mean okay in practice maybe we can do some project to get additional data. Yes. But when we are actually doing machine learning when we do the data processing part, we have to assume that this is the data set that we're giving.

**[2:26:40 – 2:26:40]** and,

**[2:26:41 – 2:26:43]** Even more importantly here.

**[2:26:44 – 2:26:46]** In practice in real life.

**[2:26:48 – 2:26:57]** We will never get quite enough data. This is an important point. I want to make it here like

**[2:26:58 – 2:27:03]** Suppose that I have. So if I just have a coin in this example,

**[2:27:04 – 2:27:07]** And I have this ability to collect more data.

**[2:27:08 – 2:27:15]** Then sure I can toast it once twice, 10 times, 20 times, 50 times. And after I have toasted 50 times, secondly,

**[2:27:16 – 2:27:26]** after I have toasted 50 times, I can be pretty sure in my results about the coin. Like the confidence interval will be quite small, etc, etc. Statistics will tell you

**[2:27:28 – 2:27:33]** But that's not what happens with real world problems, you know?

**[2:27:34 – 2:27:35]** so,

**[2:27:36 – 2:27:40]** For example, suppose that you are building.

**[2:27:41 – 2:27:42]** A language model.

**[2:27:43 – 2:28:03]** That sounds like a very difficult example but in fact it's one of the simplest near nearest store intuition suppose that we are building a language model so it's a model that has some kind of text. Then there is this black box and then it produces the next token. The next word in this text right?

**[2:28:05 – 2:28:06]** a suppose that

**[2:28:07 – 2:28:09]** I am open Ai and

**[2:28:11 – 2:28:20]** the Transformer has been introduced quite recently. And here I am, I just made my very first GPT model which is like half of a Transformers.

**[2:28:20 – 2:28:21]** Right.

**[2:28:22 – 2:28:27]** So I trained it on some Text data set. I get some pretty good language model.

**[2:28:29 – 2:28:30]** Then.

**[2:28:31 – 2:28:38]** What do I do next? I say well, all right, so let's see how this scales up. Maybe I can get more data.

**[2:28:39 – 2:28:48]** And indeed compared to the first GPT how it was trained. It's easy to get more data, let's just scrape it off the internet. Let's get some more tips. Okay?

**[2:28:49 – 2:29:02]** So, I extend my data set and now I have like, lots of additional data sets and they have lots of text. I have a huge other dates,

**[2:29:03 – 2:29:10]** When I have this huge data set, that's like quarters of magnitude larger than the one used here.

**[2:29:12 – 2:29:14]** It may be indeed means.

**[2:29:15 – 2:29:28]** That now I don't care about this by Asian stuff, I don't care about this effect. I can go back and I can train my GPT on this huge data set and it will be like almost in The Limited will be fine.

**[2:29:29 – 2:29:30]** But that's not what happens, right?

**[2:29:31 – 2:29:33]** It's not like, I collect more data.

**[2:29:34 – 2:29:39]** To go back to my GPT model and train. It even better a little bit.

**[2:29:40 – 2:29:46]** Know when I collect orders of magnitude more data, I go to a larger model.

**[2:29:46 – 2:29:49]** Right. I go to GPT, too.

**[2:29:50 – 2:29:52]** That has more parameters.

**[2:29:53 – 2:30:05]** So GPD had that many parameters actually forget how many and gpt2 had like an order of magnitude more. It had something like 150 million parameters in GT1, I don't remember.

**[2:30:08 – 2:30:18]** So, in actual practice, when you are solving a difficult task, like predicting the next talk or identifying cats and dogs and images or whatever.

**[2:30:19 – 2:30:21]** You never have enough data?

**[2:30:22 – 2:30:26]** It's impossible. Because whenever you have enough data for your model,

**[2:30:27 – 2:30:29]** In practice, it means that your model is too weak.

**[2:30:30 – 2:30:33]** It means that you should switch to a bigger model.

**[2:30:34 – 2:30:36]** For which you now don't have enough data.

**[2:30:37 – 2:30:50]** But it's still will work better. Okay, so I know I haven't proven that formerly to you. And maybe if we have time, maybe we'll discuss scaling clothes and stuff like that, but

**[2:30:51 – 2:30:55]** The point is in machine learning.

**[2:30:56 – 2:31:08]** Unless you have some very specific, very simple, very well-defined problem, like let's learn a coin toss or let's learn. Linear regression

**[2:31:09 – 2:31:10]** Right. So you have like points.

**[2:31:11 – 2:31:26]** And you want to Define to express to represent them with a linear dependence, right? That's linear regression. You can maybe get more data for this linear law.

**[2:31:27 – 2:31:28]** You can get additional points.

**[2:31:29 – 2:31:54]** But unless you have like some very good reason to know that this is going to be definitely linear unless I don't know physics and its supposed to be linear and you're just getting more data for it. So unless you're in some very special situation, if you have significantly more dated, it will be better to go to a large or model. I don't know from linear to polynomial for example.

**[2:31:55 – 2:32:02]** And to it will be a better fit, it will not overfit since you have more data Etc. It will discuss it when we get to linear regression.

**[2:32:03 – 2:32:04]** so,

**[2:32:05 – 2:32:12]** Usually in machine learning we operate like on the frontier of what's possible, so the date is usually fixed.

**[2:32:14 – 2:32:19]** We can change the model. We can we can see the model. It's it's an hour hand and usually

**[2:32:20 – 2:32:25]** You want to choose a model in such a way that, like, it's barely enough data to train it.

**[2:32:26 – 2:32:32]** So we are always in practice in a situation where data is scarce, where it's not in enough.

**[2:32:33 – 2:32:40]** So your answer is correct, indeed. One toss is not enough to learn probability of a coin to us.

**[2:32:41 – 2:32:43]** but,

**[2:32:43 – 2:32:48]** Let's say that's all we have. What can we say about the coin still?

**[2:32:49 – 2:33:07]** And definitely it shouldn't be this right? So maybe we can give up and say okay we can say nothing but we definitely shouldn't be concluding that not from now on the coin will always win Tails. That's definitely wrong.

**[2:33:08 – 2:33:10]** So, what's missing?

**[2:33:11 – 2:33:12]** What else is missing? Like, what is?

**[2:33:15 – 2:33:17]** What is the component that will?

**[2:33:18 – 2:33:30]** Get us from this 0. What is the component that will allow us to say that? Or okay, so the maximum electronic hypothesis is this but actually, maybe I

**[2:33:33 – 2:33:40]** Like one data point is not enough to really shift my, my beliefs, about the coin.

**[2:33:41 – 2:33:42]** Well.

**[2:33:42 – 2:33:46]** The missing is the missing part here.

**[2:33:47 – 2:33:48]** Is my beliefs.

**[2:33:50 – 2:33:51]** and if you go back,

**[2:33:52 – 2:33:53]** To the best from here.

**[2:33:54 – 2:33:58]** It will see that we have only talked about the likelihood.

**[2:33:59 – 2:33:59]** Right.

**[2:34:01 – 2:34:02]** And what we actually want.

**[2:34:03 – 2:34:04]** Is the posterior distribution.

**[2:34:06 – 2:34:06]** Over here.

**[2:34:08 – 2:34:18]** And to get from the likelihood to the posterior. So like the posterior, in this case, what does it mean? What is it tangible? Meaning it's, what do I think?

**[2:34:19 – 2:34:22]** What is my belief about the probability of heads?

**[2:34:23 – 2:34:24]** After.

**[2:34:25 – 2:34:29]** I got my data point after I've tested once and got Tales.

**[2:34:30 – 2:34:30]** Okay.

**[2:34:31 – 2:34:36]** And the likelihood is How likely it was to get Tails given Theta.

**[2:34:37 – 2:34:54]** And to get to the posterior, the missing piece is the prior, right? It's what did I believe about the coin? What did I think about Theta before I started even tossing it before any data came in?

**[2:34:55 – 2:34:56]** That's a missing piece.

**[2:34:56 – 2:35:00]** And in this case is pretty important. So um, let's

**[2:35:01 – 2:35:04]** think we will be able to complete this example.

**[2:35:06 – 2:35:08]** So, let's go to the second part of this example.

**[2:35:09 – 2:35:11]** To the prior distribution.

**[2:35:14 – 2:35:16]** Prior distribution. Pierre Theta.

**[2:35:17 – 2:35:18]** For the coin toss.

**[2:35:20 – 2:35:22]** What does it mean? What kind of object is it?

**[2:35:23 – 2:35:25]** Well, here is the thing.

**[2:35:27 – 2:35:28]** He of fate.

**[2:35:29 – 2:35:33]** It's a distribution on the parameters. In this case on one parameter.

**[2:35:34 – 2:35:34]** Right.

**[2:35:35 – 2:35:37]** So that's why, unfortunately.

**[2:35:38 – 2:35:55]** In machine learning, you can never, you cannot limit yourself to discrete probability Theory. So even when we are tossing a coin, it looks like the most discreet probabilistic object to mentionable only two outcomes, only one probability Etc. So

**[2:35:56 – 2:35:57]** as soon as we do learning,

**[2:35:58 – 2:36:05]** we get a continuous distribution. So P of theta is a continuous distribution. It's a distribution on the probabilities.

**[2:36:06 – 2:36:06]** Right.

**[2:36:08 – 2:36:09]** so,

**[2:36:12 – 2:36:12]** let's,

**[2:36:13 – 2:36:14]** Try to plot something.

**[2:36:15 – 2:36:16]** Like, this is Fatima.

**[2:36:17 – 2:36:18]** This will be of.

**[2:36:19 – 2:36:20]** and,

**[2:36:20 – 2:36:30]** The first property that we definitely need to have, is that fate is a probability, right? So the first very

**[2:36:31 – 2:36:35]** firm belief about Theta is that it should be between 0 and 1.

**[2:36:36 – 2:36:36]** Right.

**[2:36:37 – 2:36:48]** So what ever I think about the coin, whatever, I think about its heads or tails probability, I can definitely be sure that Theta cannot be negative. So pay is 0 over here.

**[2:36:49 – 2:36:53]** And Theta cannot be larger than one. So P of theta is zero over here.

**[2:36:54 – 2:36:56]** This is p of 8.

**[2:36:59 – 2:37:01]** So, by the way, this

**[2:37:02 – 2:37:05]** Is the answer to why?

**[2:37:07 – 2:37:09]** Theta, ml is not negative Infinity over here.

**[2:37:10 – 2:37:14]** And the answer is Theta. Ml is negative infinity and that's fine.

**[2:37:15 – 2:37:32]** Because then we will take this. So in if I have only. So if D is just one tail, then my P of D given Theta is one minus Theta, right? And it's like this straight line over here.

**[2:37:34 – 2:37:34]** Right.

**[2:37:35 – 2:37:36]** So this this is

**[2:37:39 – 2:37:39]** sorry.

**[2:37:41 – 2:37:42]** I'm not good at drawing.

**[2:37:43 – 2:37:46]** I'll do what I can then I'll show you some nice plots.

**[2:37:49 – 2:37:51]** So, this is p of D given Theta.

**[2:37:52 – 2:38:01]** And yes, it does. Go to Infinity, definitely on the left and on the right. And since we want to maximize goes to Infinity of the plus infinity over here.

**[2:38:02 – 2:38:03]** but,

**[2:38:03 – 2:38:06]** We will multiply this straight line.

**[2:38:06 – 2:38:12]** By something which is 0 on the left of zero and on the right one.

**[2:38:13 – 2:38:28]** So after we multiply, all right, let's start with the obvious. Let's start with the uniform distribution. So, the uniform distribution is just one on on the intro from 0 to 1. Oh, sorry, the intro is wrong.

**[2:38:30 – 2:38:35]** One is here, right? So if we start with the uniform distribution,

**[2:38:38 – 2:38:55]** Then after I, multiply this P of theta by this straight line and this is the best from here, right? So P of Fate to give and D is proportional to P of theta times, P of D given fate. You remember,

**[2:38:56 – 2:39:14]** So what I'm doing is I'm taking P of D. Given Theta, the green straight line I am taking P of theta which is this piecewise constant thing. You need the uniform distribution, the right one and I'm multiplying them. What do I get? I get zero over here.

**[2:39:15 – 2:39:16]** And then, I jumped to one.

**[2:39:17 – 2:39:19]** Then I go along this straight line.

**[2:39:20 – 2:39:22]** And then I get zero again, right?

**[2:39:23 – 2:39:30]** That's these two lines are easy to multiply. This is not yet. Pure Faith, given d.

**[2:39:30 – 2:39:32]** Why not? Can you tell me why not?

**[2:39:37 – 2:39:41]** Why is the light blue line? It's not still not pay of it.

**[2:39:46 – 2:39:53]** Yeah, the denominator is still missing and here is an illustration to what I was telling you before.

**[2:39:55 – 2:40:05]** We don't want to get the denominator as some fact about the coin that we want to prove, right? It's just a normalizing constant so I know that this area is supposed to be one.

**[2:40:05 – 2:40:08]** right now, it's not one right now, right now, it's what

**[2:40:12 – 2:40:12]** What is this area?

**[2:40:18 – 2:40:18]** Oh,

**[2:40:24 – 2:40:31]** Yeah, sure it's half of a square, very one, right? So it's one half

**[2:40:32 – 2:40:45]** And so it means that to get the actual distribution, I need to multiply it by two, that's it. So the actual distribution is zero here, zero here and like twice larger over here.

**[2:40:46 – 2:40:49]** So yeah, it will spend two pages. I hope that's

**[2:40:51 – 2:40:56]** Okay, so this guy is p of theta given d.

**[2:40:57 – 2:40:57]** Right.

**[2:41:00 – 2:41:07]** And notice that we didn't actually change much in terms of maximization.

**[2:41:08 – 2:41:08]** Oh,

**[2:41:10 – 2:41:24]** so yeah, this is pure. Okay. So we'll get, we'll get there in a sec. Forgot to say one thing. So this is p of theta given D. Four, the uniform prior distribution over here.

**[2:41:25 – 2:41:25]** Okay.

**[2:41:26 – 2:41:28]** The first remark is.

**[2:41:29 – 2:41:30]** Well.

**[2:41:31 – 2:41:33]** The uniform prayer is not quite.

**[2:41:37 – 2:41:44]** Sorry, what's the word? The uniform prior is not quite what they really think about coins.

**[2:41:44 – 2:41:53]** All right, so let me draw a separate picture. The uniform prior means that well

**[2:41:54 – 2:41:59]** I don't know anything about the probability of the of heads.

**[2:42:00 – 2:42:04]** So it could be zero could be one could be one half could be 1/3, it's all equal to me.

**[2:42:06 – 2:42:17]** But in reality when I take a coin like a real coin or even this pseudo coin that that is the coaster from my cup of course.

**[2:42:19 – 2:42:22]** I kind of expect that it's like approximately Fair.

**[2:42:23 – 2:42:36]** Right. So in real life obviously it's not exactly one half because it's a physical object, has some Perfections. But in real life, I kind of expect that the probability is closed to have

**[2:42:37 – 2:42:53]** So my actual prior program prior distribution, looks okay, it's still exactly zero on the left and on the right. That's for sure. That's by definition. That's mathematical fact. Not my opinion but in between it's probably something like this.

**[2:42:54 – 2:42:54]** Right.

**[2:42:55 – 2:42:59]** so, it's probably some bell-shaped curve that says, well,

**[2:43:00 – 2:43:07]** It's, I think it's approximately Fair, maybe not exactly but it's near 1/2.

**[2:43:09 – 2:43:36]** That's about where my intuition stops really. So I cannot Define this curve. Mathematically write our brains don't work in this way. I just, I can just say that, okay, it's approximately fair, I'm pretty sure of that. But so this should be pretty like high and peaky distribution. But what exactly is the shape of this distribution? I don't know, right? This this cannot be a part of my personal intuition.

**[2:43:37 – 2:44:06]** But anyway, we'll get, we'll get back here. But let's first finish with the uniform thing. So still let's begin with this, not quite realistic uniform, prior not quite realistic for coins. But for other another situations, it's a perfectly good prior because it basically just means I don't know anything. So it made a situations, it's very reasonable. If it's a new machine, learning problem, it has a parameter. I don't know anything about this parameter.

**[2:44:07 – 2:44:13]** But I know it's let's say, I know it's a probability. So it's from 0 to 1. Only from distribution is a great first step.

**[2:44:14 – 2:44:20]** Okay, so in many situations having a uniform, pair of faith is perfectly reasonable.

**[2:44:22 – 2:44:26]** so, I take this uniform P of theta, I multiply it by my

**[2:44:28 – 2:44:45]** Likelihood 1 minus Theta and they get this pointed triangle and this point a triangle. So let me write it down like P of Fate a given D. In my case P of 8 to give even a single tail. It's like

**[2:44:46 – 2:44:54]** Two times. One minus 8, if Theta is from 0 to 1 and 0, otherwise

**[2:44:55 – 2:44:56]** Right. So formally we get this.

**[2:44:58 – 2:44:59]** and,

**[2:45:01 – 2:45:08]** The next question. Let's, let's go back to the best. Roll the head. Our first

**[2:45:09 – 2:45:12]** question is, let's maximize the likelihood.

**[2:45:14 – 2:45:21]** Our second question and usually a better one is, let's maximize the posterior.

**[2:45:22 – 2:45:29]** With respect to Faith. So now that we have a posterior distribution, we can ask, what is the

**[2:45:30 – 2:45:33]** it's called the maximum upper stereo hypothesis.

**[2:45:34 – 2:45:36]** What's the Theta?

**[2:45:37 – 2:45:41]** That maximizes P of theta given d.

**[2:45:45 – 2:46:04]** And in this case there is no difference, really, right? So if I have a uniform prior, the only thing that I actually did like former leevote actually did was, I took care of this the general Solutions, right? So now my my prior does say that the should be between 0 and 1.

**[2:46:05 – 2:46:07]** That that's that's a good thing.

**[2:46:08 – 2:46:19]** But otherwise, I didn't change the shape of the likelihood. I multiplying it by one and then I am renormalized, but that's just a constant. So the maximum will not change.

**[2:46:20 – 2:46:24]** The maximum will be at the same point, right? So Theta,

**[2:46:25 – 2:46:27]** in this case,

**[2:46:29 – 2:46:34]** the map is still and Over N Plus

**[2:46:35 – 2:46:36]** Okay.

**[2:46:38 – 2:46:38]** and,

**[2:46:40 – 2:46:57]** This sounds like a lot of complicated math. Maybe not that complicated but a lot of mess for nothing. Right? So we went from Maximum likelihood to maximum up a stereo and we we didn't change anything. The answer is the same.

**[2:46:59 – 2:47:00]** well, that's because

**[2:47:01 – 2:47:17]** Our prayer was uniform but even for a uniform prayer. Something has changed because I have one point left to make this specific example. Then we'll go to the prayers. I hope they still have time.

**[2:47:20 – 2:47:20]** In this.

**[2:47:24 – 2:47:42]** In this example, for example, in the example of a coin toss and this is a very awesome, very important conception learning. Today is like this very abstract and introductory lecture apologize. I have to begin with something like this. We will we'll get on your own networks, literally tomorrow.

**[2:47:42 – 2:47:43]** But anyway,

**[2:47:45 – 2:47:46]** In this.

**[2:47:47 – 2:47:47]** Example.

**[2:47:48 – 2:48:03]** What is the end goal of this whole thing? Like, let's say that this is an actual machine learning problem. Let's say that. It's I mean it's not but let's say that it's something like distinguishing cats from dogs or something, right? So

**[2:48:05 – 2:48:08]** when I am learning the parameters of

**[2:48:09 – 2:48:10]** A machine learning model.

**[2:48:12 – 2:48:16]** What am I really interested in? What is my final goal? This is a very important point.

**[2:48:18 – 2:48:18]** So far.

**[2:48:19 – 2:48:21]** We have been talking about.

**[2:48:23 – 2:48:25]** Learning something about Theta.

**[2:48:26 – 2:48:36]** So we try to get them ml maximum likelihood. Now we did the prior and now we are getting data MP maximum Australia.

**[2:48:37 – 2:48:38]** But that's about Theta.

**[2:48:39 – 2:48:56]** So if you if I mapped this discussion to neural networks, it would say. All right so I have an old networks, hey taste, the vector of its weights of the parameters, right? And then I do my learning and here is so fat amount. They may be are like checkpoints of the weights.

**[2:48:57 – 2:49:00]** They are this state of the neural network.

**[2:49:02 – 2:49:12]** But when I phrase it like this, it becomes clear that that's not the final goal of the process, right? If I am training, a neural network to distinguish case from dogs,

**[2:49:13 – 2:49:14]** I don't care what the weights are.

**[2:49:15 – 2:49:24]** Right? I mean I do want to get them but I want to get them as a, an intermediate step for the goal. And the goal is this English gets from those.

**[2:49:25 – 2:49:26]** Right. So

**[2:49:27 – 2:49:31]** What we are actually supposed to do, and this is the third part here.

**[2:49:32 – 2:49:41]** And this is true. Both in machine learning can generally in life, actually, what we are actually supposed to do is to make predictions,

**[2:49:42 – 2:49:43]** Right.

**[2:49:44 – 2:49:44]** so,

**[2:49:48 – 2:49:53]** Like philosophically speaking. What does it mean to understand something? Well, it means that you can predict

**[2:49:54 – 2:49:58]** What's going to happen with it? And you can be right. More often than chance.

**[2:50:02 – 2:50:06]** It's I mean, if you haven't thought about this, it's a pretty deep ideas. So

**[2:50:08 – 2:50:20]** understanding something doesn't mean, rephrasing it in different words, it means phrasing in such a way that you can operate analyze it and get to

**[2:50:21 – 2:50:23]** predicting some stuff that you didn't know.

**[2:50:24 – 2:50:26]** in such a way that it actually,

**[2:50:27 – 2:50:29]** Conforms to rare it, right?

**[2:50:31 – 2:50:47]** And here also in this very simple case even here. I mean in the case of a coin everything is very simple, very small and very close to each other. So there may seem there is no difference. So okay, so what's the difference between

**[2:50:49 – 2:51:00]** Predicting heads or tails and learning the probability of heads or tails. It's the same thing. If I get Theta, more than one half, I will predict heads if I get paid less than what I have a projectiles. Isn't that true?

**[2:51:02 – 2:51:02]** Still.

**[2:51:04 – 2:51:13]** There is a difference, very interesting but there is and the predictive distribution, and this case, what is it? It's like the probability of heads.

**[2:51:14 – 2:51:15]** Given the date.

**[2:51:17 – 2:51:19]** It's not in the best for me.

**[2:51:19 – 2:51:20]** It's the next step.

**[2:51:21 – 2:51:25]** Let me I don't have space here. I think.

**[2:51:26 – 2:51:29]** Yeah, let let me write it.

**[2:51:31 – 2:51:43]** Formally separately. So I have the bias roll B of Faith. A given D is p of D, given Theta times P of theta divided by P of D, but the predictive distribution.

**[2:51:46 – 2:51:50]** Is the distribution of the next outcome.

**[2:51:50 – 2:51:58]** Of the next X or the next y, given X in our learning problem. Like what's, okay? So I have this data.

**[2:51:59 – 2:52:03]** What's the probability that this picture is a kid for example.

**[2:52:06 – 2:52:07]** X given d.

**[2:52:08 – 2:52:14]** And P of x given D does not contain Theta at all.

**[2:52:14 – 2:52:16]** I don't care about Theta here.

**[2:52:16 – 2:52:19]** I care about the next prediction solving the problem.

**[2:52:20 – 2:52:21]** but,

**[2:52:22 – 2:52:38]** It's so happens that I can't get to this distribution other than introduce it, right? So the only way to actually compute this is to say, ah, okay, so I don't know about P of x given D, but maybe I know something about P of X and Theta giving d

**[2:52:38 – 2:52:40]** Here is this?

**[2:52:41 – 2:52:49]** Joint joint probability. And here is this marginalization process, right? We are integrating the Gen probability to get pure effects.

**[2:52:50 – 2:52:57]** And now for this joint probability, yes, we can actually reduce it to what we know. So it's p of

**[2:52:58 – 2:53:05]** x given Theta and D times P of theta given d e Theta.

**[2:53:08 – 2:53:12]** And now P of Faith, a given D is our posterior.

**[2:53:13 – 2:53:34]** Right and pox giving well, we have to recall our assumption, we had this assumption which always holds that data points are in the independent. If you have, if you know the parameters, if you know, the full model so here all. So, if I already know the full model, then did not matter.

**[2:53:34 – 2:53:46]** Right? If I already know what is the probability of heads, then it doesn't matter what further the results of the coin in the past, if I know the probability, it will stay the same.

**[2:53:46 – 2:53:54]** So here, the first part is just P of x given fate. It's the likelihood of the single point.

**[2:53:58 – 2:54:00]** Um, and that's it. So this is the predictive distribution.

**[2:54:01 – 2:54:09]** And in this case, even for this uniform prior, it will be different from just predicting zero.

**[2:54:10 – 2:54:24]** That that's the interesting part. So P of has given D. In our case is p of heads, given Theta times P of theta given d d Theta, right? And it's like,

**[2:54:25 – 2:54:27]** What is p of heads given d?

**[2:54:28 – 2:54:37]** Well just fate, right? It's the probability of heads given that the probability of headset that's like a foot of one. Was it difficult?

**[2:54:39 – 2:54:48]** And people that give and give, we actually, I think we didn't write it completely but we did write the likelihood, right? So this this is it.

**[2:54:49 – 2:54:50]** and,

**[2:54:51 – 2:54:53]** P of Fate a given d.

**[2:54:56 – 2:54:57]** Of Fate to give and D.

**[2:54:58 – 2:55:11]** Is proportional to P of D given Theta times P of theta. So it's proportional to like Theta to the end. One minus Theta to the M on 01.

**[2:55:12 – 2:55:26]** And 0 everywhere else, right? So we take the likelihood we multiply it by the uniform prior which basically just zeros everything outside here and does nothing inside here.

**[2:55:26 – 2:55:29]** And we get the posterior distribution.

**[2:55:30 – 2:55:41]** So it's Theta times Theta to the M1 minus Theta to the m divided. Let's let's keep it like this P of D. If

**[2:55:42 – 2:55:44]** And what is p of d.

**[2:55:45 – 2:55:56]** P of D is just the normalizing constant for this. It's the integral from 0 to 1. Oh and the integral is from 0 to 1 because elsewhere it's 0.

**[2:55:56 – 2:56:04]** So P of D is the integral from 0 to 1 of theta to the and times. One minus Theta to the MD Theta.

**[2:56:05 – 2:56:12]** And here we get integral from 0 to 1 Theta 2 to the End. Plus one. There is this extra Theta here.

**[2:56:13 – 2:56:16]** Times 1 minus Theta to the MD Theta.

**[2:56:17 – 2:56:38]** And I want to the math, it doesn't matter for us. We will never come back to it, but if you had a Calculus class, you probably recognize this is the beta function and you can express it as factorials and then all of the factorials will cancel out, blah, blah. I don't want to teach you about beta functions if you don't already know and if you do it kind of fish.

**[2:56:39 – 2:56:43]** Ah, but the result here will be n plus 1.

**[2:56:44 – 2:56:47]** Divided by n, plus M, plus 2.

**[2:56:49 – 2:56:52]** So there is this extra stuff here.

**[2:56:54 – 2:56:58]** this is called this formula is called the LaPlace

**[2:57:00 – 2:57:01]** or rule of succession.

**[2:57:04 – 2:57:16]** Lapia persimmon LaPlace was one of the original founders of probability theory that was one of the original results of the whole field. But whatever doesn't matter. The point is

**[2:57:18 – 2:57:21]** what the predictive distribution does, in fact,

**[2:57:22 – 2:57:29]** so if you look at this from a different perspective, it's the expectation over the posterior

**[2:57:31 – 2:57:32]** of this, like,

**[2:57:34 – 2:57:34]** Right.

**[2:57:35 – 2:57:47]** Just by definition. What is the expectation? It's integral the function times the density defect. So this is like the likelihood average over the posterior distribution.

**[2:57:50 – 2:57:50]** and,

**[2:57:51 – 2:57:59]** What does it mean in our case? Well, in our case, it means that we average over this purple distribution here.

**[2:58:00 – 2:58:02]** And yes, its maximum is at zero.

**[2:58:04 – 2:58:05]** This is the Theta map.

**[2:58:06 – 2:58:09]** But its maximum is on this one side of it.

**[2:58:10 – 2:58:11]** And then fact,

**[2:58:12 – 2:58:14]** there is this whole triangle, right?

**[2:58:15 – 2:58:18]** so, when you average over this

**[2:58:19 – 2:58:36]** Distribution. You don't just get what you would get. If you plugged in zero, you get something in between like it's not the average is not one half and they ever hear is like one third, but it's not 0 either, right? So you average your

**[2:58:39 – 2:58:42]** Likelihood over the whole.

**[2:58:43 – 2:58:48]** Posterior distribution over all possibilities for the model parameters.

**[2:58:49 – 2:58:58]** And yeah, that's that's a lot to digest. But I hope that this coin. Tossing example, is easy enough, that we actually understand what's going on.

**[2:58:59 – 2:59:02]** There any questions at this point? I think I

**[2:59:03 – 2:59:04]** Diamond. I've kind of

**[2:59:05 – 2:59:08]** I think that has been a lot of new information, so,

**[2:59:14 – 2:59:15]** Okay.

**[2:59:16 – 2:59:21]** Okay. Yeah, I love the the Emojis. All right, so

**[2:59:23 – 2:59:36]** At this point even on this. Very simple, example, of the coin. Does I have just one? I think last comment left and then I will show you a couple of thoughts and then we'll, and for today. So,

**[2:59:39 – 2:59:40]** This.

**[2:59:41 – 2:59:42]** Kind of thing.

**[2:59:43 – 2:59:43]** Is.

**[2:59:45 – 2:59:47]** What machine learning is actually about.

**[2:59:48 – 2:59:49]** So,

**[2:59:50 – 2:59:58]** when you define a model, like, when you sorry, where was here, when you define a model like

**[2:59:59 – 3:00:03]** I want to distinguish guests from dogs. What you actually are doing is

**[3:00:04 – 3:00:05]** You define a lost function.

**[3:00:06 – 3:00:09]** And the lost function is actually.

**[3:00:10 – 3:00:11]** Almost always.

**[3:00:12 – 3:00:13]** Either.

**[3:00:14 – 3:00:17]** The log likelihood that you want to maximize?

**[3:00:18 – 3:00:24]** well, the negative because for the losses you want to minimize but it's the same thing or

**[3:00:25 – 3:00:28]** Even more often, it's the negative log posterior.

**[3:00:29 – 3:00:41]** which is so if I write it in logarithms I will see that like the log posterior is just the look likelihood Plus

**[3:00:42 – 3:00:47]** The log prior plus a constant, right? That's what proportional means.

**[3:00:48 – 3:00:53]** so again, in terms of the optimization that doesn't matter, but if

**[3:00:54 – 3:01:13]** It does matter in the sense that we are reading the look, prior to, and the log, prior is the regularizer. We didn't discuss it. We don't discuss it tomorrow where the regularization comes in, but regularization means putting a prior on the model parameters,

**[3:01:14 – 3:01:16]** so introducing your own beliefs.

**[3:01:18 – 3:01:20]** Of what the prior action was.

**[3:01:24 – 3:01:25]** Okay.

**[3:01:26 – 3:01:34]** And yeah, and I think I, I have to, I have to discuss one last Point here. So,

**[3:01:36 – 3:01:41]** This was all the specific formulas that I wrote were only about the uniform prayer.

**[3:01:42 – 3:01:53]** And as I said it's not the prior that I actually have in mind when I'm talking about the coin, right? So for a real coin, it's some bell-shaped curve. I'm pretty sure it's close to one half.

**[3:01:55 – 3:01:55]** so,

**[3:01:57 – 3:02:02]** Of course, I want to plug in a more realistic prayer here. If I want to learn the quintus,

**[3:02:02 – 3:02:14]** But the plug it in, I need to Define it, right? So the question let's say it's what is a, the more realistic prior?

**[3:02:15 – 3:02:19]** For the coin. And what is the most nature prayer for a queen?

**[3:02:20 – 3:02:20]** What is?

**[3:02:21 – 3:02:22]** How do I?

**[3:02:23 – 3:02:25]** Define p of theta.

**[3:02:26 – 3:02:27]** Okay.

**[3:02:28 – 3:02:29]** And here, the answer may surprise you.

**[3:02:30 – 3:02:38]** If you never thought about it before, the answer is surprise you because it sounds kind of lazy but it's true. So,

**[3:02:40 – 3:02:42]** The prior is a distribution.

**[3:02:43 – 3:02:44]** On Theta.

**[3:02:44 – 3:02:50]** We know that it should be 0 here. 0 here. Now question about that. But what is the shape inside?

**[3:02:51 – 3:02:54]** My intuition says that it should be something like this.

**[3:02:55 – 3:03:05]** But there are millions and billions and you know, space with continual dimension of how many different functions look like this, right?

**[3:03:07 – 3:03:15]** So how do I choose a specific function? What what will be the family of probability distributions that I plug in for p of faith?

**[3:03:16 – 3:03:18]** Do you know any distributions that look like this?

**[3:03:19 – 3:03:20]** Can you suggest?

**[3:03:24 – 3:03:28]** Normal distribution, normal. Sounds good on the surface.

**[3:03:28 – 3:03:51]** So with normal, you will have a problem right from the outside because the normal distribution will not go to 0, right? So the normal distribution is never exactly. It will be like something depending on the variance and then it will go down and then it will have some tails on the ball sets, right? So there will be tails.

**[3:03:52 – 3:04:05]** But okay, let's cut off the tails. We can do that. We can truncate normal distribution on the left and on the right. Then we renormalize a little bit, it becomes a bit higher, but it's still like normal. Just the normal bell curve over here.

**[3:04:07 – 3:04:08]** What happens next?

**[3:04:09 – 3:04:30]** So I need to write down the normal distribution. What is my P of theta? Well, it's zero outside of 01 and here. It's some constant which I cannot compute. Of course, times times what times, e to the power minus 1 over 2 Sigma squared,

**[3:04:31 – 3:04:33]** Theta, minus 1/2 squared.

**[3:04:35 – 3:04:36]** On the 01.

**[3:04:37 – 3:04:37]** Right.

**[3:04:38 – 3:04:40]** That's the density of the normal distribution.

**[3:04:42 – 3:04:52]** Okay, so far. Not so scary but what happens next. Next, I need to multiply P of theta times P of D given Theta.

**[3:04:54 – 3:05:03]** And that's gonna be okay. Inside zero one is going to be like c times this exponent.

**[3:05:04 – 3:05:13]** Times Theta to the N times. 1 minus Theta to them. That's my posterior distribution, the shape of the posterior.

**[3:05:14 – 3:05:18]** And then I need to put maximize it. So I need to take derivative

**[3:05:20 – 3:05:31]** It sounds like it doesn't fit, right? So we probably can do it numerically. Of course. It's I mean it's it's a coin. It's dimensional one. Of course we can do it numerically but it sounds like

**[3:05:32 – 3:05:35]** some pretty inconvenient distribution for acquaintance.

**[3:05:35 – 3:05:42]** And what is it? What exactly isn't convenient? What is inconvenient is that the shape of the prior

**[3:05:42 – 3:05:45]** Does not match the shape of the likelihood.

**[3:05:46 – 3:05:55]** The prior is an exponent and the likelihood is a polynomial and we multiply one by the other, we don't get anything meaningful, we get exponent times, putting them.

**[3:05:58 – 3:06:12]** So here here is the secret here. I just want about shift curve into my intuition doesn't tell me if it's normal or students t, or or whatever.

**[3:06:13 – 3:06:15]** So, how we actually choose?

**[3:06:16 – 3:06:19]** Is we choose by convenience?

**[3:06:20 – 3:06:22]** We choose the shape of the prior.

**[3:06:23 – 3:06:29]** That matches the shape of the likelihood, so that these multiplication becomes easy.

**[3:06:31 – 3:06:55]** And that the former it would be called the conjugate prior. Let's not get there. I will just give you an example and we'll be done with it. So what would be easy to multiply? So the likelihood we cannot change. The likelihood is given by the process by the thing that we are describing. So, in this case, it's a coin. Has two sides. One parameter. So this formula is fixed. We cannot change the like

**[3:06:57 – 3:07:02]** But we can change the prior and what would be easy to multiply by polynomial like this.

**[3:07:09 – 3:07:10]** This is the electrical.

**[3:07:11 – 3:07:15]** How should the prior look like? So that it's easier to multiply by this.

**[3:07:26 – 3:07:43]** Okay, probably, you're probably wondering exactly how easy I didn't Define that. But okay. So the prior, the easiest way, this is function to multiply by basing like this would be another thing like this.

**[3:07:44 – 3:07:50]** Isn't that true? So let's say the prior is something like Theta to the power of alpha.

**[3:07:51 – 3:08:00]** Formerly Alpha minus 1 that's just for formal reason. Don't pay attention times 1, minus Theta to the power beta minus 1.

**[3:08:02 – 3:08:06]** Times a constant. And the constant is a beta function. Blah blah. Let's not get there but

**[3:08:08 – 3:08:12]** As a result, I will get Theta to the power. Alpha plus n minus 1.

**[3:08:14 – 3:08:19]** And I will get 1 minus 8 to the power beta plus M minus one.

**[3:08:20 – 3:08:32]** so, the multiplication becomes trivial, but what is actually important is, not that it's easy, but that the posterior again looks exactly like the prayer

**[3:08:34 – 3:08:40]** so the prior is, what is called the beta distribution with parameters of and beta,

**[3:08:42 – 3:08:47]** And after I multiply by likelihood with and heads on them tails.

**[3:08:48 – 3:08:53]** I get the posterior which is again a beta distribution.

**[3:08:54 – 3:08:58]** but with parameters Alpha plus n and beta Plus

**[3:08:59 – 3:09:00]** Okay.

**[3:09:00 – 3:09:11]** So when that happens we call it the conjugate prior you don't have to memorize that. But the point is now this calculation by the

**[3:09:13 – 3:09:24]** bias for row becomes trivial. I don't need to even think about the formulas. I just did it once. It's just adding up the exponents, that's it, right?

**[3:09:25 – 3:09:26]** and,

**[3:09:30 – 3:09:30]** Now.

**[3:09:32 – 3:09:47]** I can easily go from prior to posterior for any and them, I don't need to do any new method. I don't need to run any numerical algorithms. I just plug it into this. Very simple formula where it's just initial

**[3:09:48 – 3:10:17]** And the only thing that I need to check is that indeed, this kind of Prior can express what I want, right? So that I can get a bell shaped curve out of it and here I can get a bullshit profile to it. So if I have a fated to the power 10 and 1, minus Theta to the power 10, if the exponents are the same, then I will get a big at one half. So this point let me just show it to you.

**[3:10:17 – 3:10:19]** um, in

**[3:10:20 – 3:10:21]** practice.

**[3:10:27 – 3:10:29]** Yeah, let me just show you the bettas.

**[3:10:30 – 3:10:30]** So,

**[3:10:32 – 3:10:37]** Here is the family of the beta distributions. The

**[3:10:38 – 3:10:54]** The the uniform distribution is also a bit with parameters 1 and 1. So like one it's fated to the power 1 minus 1 and 1 minus 8 to the power 1 minus 1. So it's just uniform. And then as the bait, the elephant bathing increase

**[3:10:56 – 3:11:00]** I get like this more and more pointy.

**[3:11:01 – 3:11:03]** Distributions, the variance decreases.

**[3:11:04 – 3:11:16]** And if Alpha and beta are equal, then I get the maximum at one half in general. Like I get the maximum at Alpha divided by Alpha plus beta just like the coin just like the max like

**[3:11:17 – 3:11:26]** So the beta frame it does include what I want. It also includes a lot of other nice distributions that I can probably get as posterior.

**[3:11:28 – 3:11:28]** and,

**[3:11:29 – 3:11:35]** What does the actual bias and inference look like, well, it looks something like this. So let's

**[3:11:36 – 3:11:39]** let's have, let's first begin with our

**[3:11:40 – 3:11:42]** our example, like we did.

**[3:11:44 – 3:11:48]** In the lecture. So here is the prior it's uniform.

**[3:11:49 – 3:11:54]** The likelihood for one tails is the orange line.

**[3:11:55 – 3:12:03]** And then I multiply it by the posterior, which by the prior. Sorry. And then I normalize and I get the posterior, which is the green line.

**[3:12:04 – 3:12:06]** Okay, so this is what the Drew on the board.

**[3:12:08 – 3:12:10]** What if my prior was different?

**[3:12:11 – 3:12:17]** What if my prior had parameters? Like, two and two, so one and one gives you

**[3:12:18 – 3:12:31]** The power zero. One minus, the power is 0 2 and 2, give you the power 1 times, 1 minus, the power one. So it's a parable like this, right? This, this is the prior.

**[3:12:33 – 3:12:39]** and when I multiply this prior by the same likelihood, I still toasted once I got one tails,

**[3:12:40 – 3:12:46]** Well, now it's a cubic curve and the shifted to the left a little bit and its maximum is at one third.

**[3:12:46 – 3:12:48]** Makes sense, right?

**[3:12:49 – 3:12:50]** And then I can.

**[3:12:51 – 3:12:56]** I can continue like this. I can become more and more sure.

**[3:12:57 – 3:13:01]** A pre-order that the coin was fair.

**[3:13:02 – 3:13:09]** And I will get like this more and more peaky priors around one half.

**[3:13:10 – 3:13:10]** and,

**[3:13:11 – 3:13:22]** The more convinced I am in advance that the coin was fair. The last, this one experience will matter. One experiment, will matter.

**[3:13:22 – 3:13:27]** So if I was already very sure that the coin is kind of fair.

**[3:13:28 – 3:13:31]** Like 50/50 the parameters, 50, 50.

**[3:13:32 – 3:13:32]** Then.

**[3:13:35 – 3:13:41]** This one result of Tails will not change anything. The posterior looks just like the prayer.

**[3:13:42 – 3:13:46]** but of course, if I keep talking it and I keep getting tails

**[3:13:48 – 3:13:49]** It matters more.

**[3:13:50 – 3:14:06]** So 10 Trails will shift my posterior to the left. This is the likelihood for 10 tails in a row and if I get, I don't know, 100 Tails. Then I will probably shift it quite a lot, right? But still

**[3:14:09 – 3:14:18]** The prior matters a lot to how much evidence I need to actually move my beliefs.

**[3:14:21 – 3:14:22]** Okay.

**[3:14:24 – 3:14:28]** Yeah, and since we are here, let me know show you this. So,

**[3:14:32 – 3:14:34]** How it actually, how it might actually work.

**[3:14:35 – 3:14:35]** Is.

**[3:14:38 – 3:14:57]** What is another like? Nice property of the conjugate priors. What is another? Nice property of a situation where you're posterior? Looks just like the prior and other nice properties that. Now, you can reuse. This posterior is the prior for the next experiment.

**[3:14:58 – 3:15:04]** So now I can do like sequential update I can say well all right. So here is my

**[3:15:06 – 3:15:12]** Here is my original uniform distribution, then I tossed the coil once.

**[3:15:13 – 3:15:20]** And I got heads. So the orange straight line is the posterior after one pointers.

**[3:15:20 – 3:15:22]** Then I tested another

**[3:15:23 – 3:15:30]** one time and I got a tail. So now this Parabola is my posterior after 2.06.

**[3:15:30 – 3:15:40]** And when I toss it three more times, I don't have to go to the beginning. I can say, all right, so now I have this Parabola after 2.06

**[3:15:41 – 3:15:48]** Let me just multiply that, by the likelihood of the next three. Like, one heads and two tails, I think in this case,

**[3:15:49 – 3:16:00]** And this is there is a result. And so so I can like forget about the previous data set. Just take the posterior and plug it in as the prior for the next update.

**[3:16:01 – 3:16:02]** So I, it can work.

**[3:16:04 – 3:16:09]** It can work like this, I start with P of Fatima.

**[3:16:12 – 3:16:13]** Then.

**[3:16:14 – 3:16:17]** From a dataset. I get paid a d.

**[3:16:18 – 3:16:19]** and then,

**[3:16:20 – 3:16:22]** I get another dataset more data.

**[3:16:23 – 3:16:32]** And I want to go to P of Faith, a given D and D Prime, right? I want to unite all of the data and use all of the data.

**[3:16:33 – 3:16:38]** And basically, if I have a conjugate prior like this, I can just say, all right, so I did the math here.

**[3:16:39 – 3:16:55]** I can forget about this part. Now, this is my new prior. This is my new data set and I get to the posterior and of course formerly nothing changes. So it's the same by a stroll, only its deal on the right. And every and every probability doesn't doesn't matter.

**[3:16:58 – 3:17:08]** But if I didn't have a conjugate, president would just be very difficult to do. So, it would be easier to just start from here and do the whole computation with the and the prime.

**[3:17:08 – 3:17:12]** But if I do have a conjugate prior, then I can use it.

**[3:17:14 – 3:17:33]** And maybe one final. Yeah. Maybe one final thing to show here is here is a coin toss that I did a sequence of coin tosses in the sequence of probability of heads that I have learned.

**[3:17:34 – 3:17:38]** And the probability of heads change as I go.

**[3:17:39 – 3:17:46]** And the blue line is the maximum likelihood hypothesis and the orange line is the LaPlace is roll.

**[3:17:47 – 3:17:54]** So it's this small out and plus one over n plus n, plus 2, the predictive distribution, the predictive probability.

**[3:17:55 – 3:18:14]** And as you can see it's just as we expect, right? So in the beginning, they LaPlace is row is less extreme than the maximum likelihood. So after one toss, this is either one or zero and this is either one through two thirds, so much closer to one half.

**[3:18:15 – 3:18:23]** And that will like moderate this extreme of the max likelihood, but then, after like 50 tosses, they're in distinguishable.

**[3:18:24 – 3:18:28]** so one converges to the other and they both converge to the true probability,

**[3:18:29 – 3:18:31]** and we can, we can do other

**[3:18:33 – 3:18:35]** Random experiments here. It's of course.

**[3:18:41 – 3:18:46]** So okay, so let's let's summarize I think I'm already over time here.

**[3:18:48 – 3:18:49]** What we did today?

**[3:18:50 – 3:18:54]** this is Thomas bias, the Reverend Thomas Bass from

**[3:18:55 – 3:19:09]** 1760 something. So but actually yeah there there is a famous story that this portrait is actually fake. It's not Thomas bass and nobody knows who that is, okay? You can read them.

**[3:19:09 – 3:19:12]** anyway, so

**[3:19:13 – 3:19:17]** we discussed the best theorem in and how it is used in machine learning.

**[3:19:18 – 3:19:19]** We discussed.

**[3:19:20 – 3:19:26]** the most important, not just the most important because basically, the only problems that we

**[3:19:27 – 3:19:35]** Are solving in machine learning. Like, what does it mean to learn something? Well, it means to say something about the parameters of the model.

**[3:19:37 – 3:19:44]** and you can just maximize the likelihood, but as we have seen today, it's probably probably usually makes more sense to

**[3:19:45 – 3:19:48]** Get the full posterior distribution, if you can.

**[3:19:50 – 3:19:52]** and then maybe maximize it if you have to

**[3:19:53 – 3:19:55]** And yes.

**[3:19:58 – 3:20:03]** This is what we discussed. I will get to a couple more examples tomorrow.

**[3:20:04 – 3:20:06]** A conjugate prior. So we discussed

**[3:20:07 – 3:20:13]** This is the beta family here. I think this is it.

**[3:20:14 – 3:20:20]** This is the laplace's role. You can read it up on the slides. If you want you want to

**[3:20:20 – 3:20:31]** What, where is the predictive here? Yeah, for example here and the last problem, the most difficult problem is to get the predictive distribution is to get

**[3:20:33 – 3:20:47]** The next, the distribution of the next element of the data set predict the next coin pose, given what the data Setters is still in a regardless of the specific way of fate.

**[3:20:48 – 3:20:50]** Which means you have to average overstate.

**[3:20:51 – 3:20:53]** And we did it.

**[3:20:55 – 3:20:57]** with the example of the coin, we

**[3:20:58 – 3:20:59]** hopefully.

**[3:21:00 – 3:21:18]** When through the whole example, I skipped a couple of Minor Details that don't affect and they machine learning understanding. But overall, we've completed the cuantos example, naturally. You can also extend it to

**[3:21:20 – 3:21:28]** Die rolling to several different outcomes. It will be exactly the same. Maybe we'll talk about it tomorrow, but at this point, I think,

**[3:21:30 – 3:21:31]** I will stop here.

**[3:21:32 – 3:21:33]** Are there any questions?

**[3:21:38 – 3:21:40]** Yeah, I have a question. Can you remind please?

**[3:21:43 – 3:21:52]** Yeah, maximum likelihood and plus rule is activation of Prior multiplied by likelihood and

**[3:21:53 – 3:22:03]** Okay, so LaPlace role is the predictive distribution. So let's let me repeat it again because this is really important. So you have the

**[3:22:05 – 3:22:06]** Best role, right?

**[3:22:08 – 3:22:12]** The bias role connects the likelihood, the prior, and the posterior.

**[3:22:13 – 3:22:17]** The model itself is usually the likelihood.

**[3:22:18 – 3:22:23]** And you can maximize the likelihood directly and you get the maximum likelihood hypothesis.

**[3:22:24 – 3:22:25]** if you add the prior,

**[3:22:26 – 3:22:27]** You get the posterior.

**[3:22:29 – 3:22:34]** And you can maximize the posterior and you get the maximum aposteriori hypothesis.

**[3:22:36 – 3:22:48]** But what you really want, it's just that often it's impractical to get often, you can't get it. But what you really want is the predictive distribution, the next x given d,

**[3:22:49 – 3:22:54]** And that is and there is no way to compute it, usually except like this.

**[3:22:57 – 3:23:01]** Right. So like the expectation over the posterior.

**[3:23:03 – 3:23:05]** Of this next.

**[3:23:05 – 3:23:06]** Item. Like,

**[3:23:08 – 3:23:12]** Okay, and the LaPlace is role was about this.

**[3:23:13 – 3:23:14]** So the LaPlace roll.

**[3:23:18 – 3:23:20]** Said that P of heads.

**[3:23:21 – 3:23:23]** Give an end and then given d.

**[3:23:24 – 3:23:31]** Is and plus one divided by n plus, n plus 2. If you have a uniform prior,

**[3:23:32 – 3:23:43]** While let's say, Theta ml was given us and over n. + m, and Theta, Mae people's also give us and divided by n plus him.

**[3:23:44 – 3:23:45]** It's all for the uniform.

**[3:23:49 – 3:23:49]** Okay.

**[3:23:51 – 3:23:52]** Okay, thank you.

**[3:23:55 – 3:24:03]** Our questions. Sorry, yeah another question. Sure. Okay, first of all about the same topic so

**[3:24:05 – 3:24:17]** For example, in economics and financial econometrics where you use time series, it is very common. Well, every time you build a model to predict the next

**[3:24:18 – 3:24:20]** How they say? Yeah.

**[3:24:23 – 3:24:36]** Inputs from the previous period. So it is a very common problem. Why is it such a problem here, is the difference between time series and on ordered observations, like here, or is it a different?

**[3:24:37 – 3:24:40]** Of languages by yourself approaches.

**[3:24:41 – 3:25:12]** There is no difference. I mean, it's just a different problem setting but you will still need to convert it to your previous layering. Probably right? So, in reality I mean, yeah, maybe your time serious goes to negative Infinity but in reality doesn't right. So in reality you will have your data set. Sorry, your data set in Time, series analysis will still look like players of access and wise

**[3:25:13 – 3:25:33]** And how do you define the excess? Well, that depends on your model of course. So maybe you do a sliding window, right? So maybe you say, okay, I look at the previous so many tips and I predict the next tick based on this fixed context.

**[3:25:34 – 3:25:36]** Then your access this.

**[3:25:37 – 3:25:42]** Or you can say, well, let me do, I don't know, recurrent neural network.

**[3:25:43 – 3:26:13]** If I have a current neural network, then it means that what my recurrent cell is doing is it's getting my current X and the hidden State age and we are predicting. Let's say, okay actually, we are outputting the next hidden state, but we are also, let's say, predicting this, why over here, right? So we will talk about recurrent networks when we get there. But here all. So you compress your contacts down to this state Vector page,

**[3:26:14 – 3:26:15]** and this is your input and you want to

**[3:26:16 – 3:26:19]** and, and then you get your

**[3:26:20 – 3:26:22]** Own and so on. So,

**[3:26:23 – 3:26:55]** I don't feel. There is any difference specifically. So yeah, time series sometimes are a little bit special but I think not an econometrics. I think they're special. When they're, when they're like really really long, I can sound analysis. When you have like, millions and millions of ticks and you don't want to treat them as a single. Not just at times serious, maybe you want to do, you know, Fourier transforms look at the Spectra Etc and it becomes a different sense. But I think in econometrics, it's just your professor.

**[3:26:59 – 3:27:00]** The question about.

**[3:27:02 – 3:27:03]** Notebooks that you.

**[3:27:13 – 3:27:14]** This one.

**[3:27:15 – 3:27:15]** Yes. So

**[3:27:16 – 3:27:22]** For example, and equals 5, sorry, no problem.

**[3:27:24 – 3:27:26]** Yeah, and it cost to five.

**[3:27:28 – 3:27:31]** so, we can use the

**[3:27:34 – 3:28:00]** How do I say our our prior component is the result that we go to previous step. Yeah. So is there a difference in results? Now, go in step by step or that's just using five observations from our initial. Yeah, that's the same. Exactly the same as the whole point here. So of course, for a coin, I mean, it doesn't matter. You are not saving anything. Going straight from the beginning is just as easy.

**[3:28:01 – 3:28:24]** But if you had like a big data set and you could compress it down to to the posterior distribution, maybe now you can forget about the data set, that's maybe a good thing. You need to to go over it again. I mean for a coin yeah you're not saving anything because for a coin the data set reduces to two numbers. So it's it's not like you can be more efficient here.

**[3:28:27 – 3:28:48]** And can you upload these sure sure there's no yeah, absolutely. So what I will do, what I always do is I will make web page for the class for you and it will have the videos, it will have the boards. It will have a notebooks

**[3:28:49 – 3:29:01]** And it will be unfortunately a secret webpage for the herbal space University, so I'm not allowed to post it in public, but I will send you the link in Google classroom or whatever.

**[3:29:01 – 3:29:14]** Also, if it's convenient for you, we can make a telegram chat for the class. I think we don't have one but it would be really convenient for me. But if if that's not good for you, then Google Classroom is fine too.

**[3:29:17 – 3:29:20]** Okay, so thank you. And

**[3:29:21 – 3:29:26]** See you tomorrow judging by your questions. I think you did learn something new today.

**[3:29:27 – 3:29:30]** Thank you tomorrow. Thank you.

## Full text

Hello everyone. It is very nice to meet you here. Virtually remotely, but still meet you here at Harbor space. My name is Regina kohen and I will be talking to you about machine learning and yeah, the the class is called his name. Very specifically. Computer vision in neural networks. But to be honest, usually it's so happens that it kind of becomes just a general introductory class to declaring, which, judging by the tourists I had, we will also do this time because it's, it sounds like you have many of you have not had real experience with deep learning specifically. So we will start from the very beginning and then work our way up. There will be computer vision, of course. I mean I we have to give some examples and since the classes about computer vision, why not give computer vision examples but we will yeah, start from the beginning and we will try to you know, build the Cathedral of modern artificial intelligence from the ground up. As best as we can. So but let me begin today with a brief introduction to machine learning in general. Okay? So I don't think we will get to neural networks today. I hope we'll get there tomorrow. And finally, I got to be a host, the host. So I can now spotlight That's all I need it. Thank you. so let's begin by talking about, we are artificial intelligence is how we got there and today I want to maybe for some of you, it will be a reminder for some of you it will be new material, but I want to discuss like the most fundamental stuff of machine learning. Like what is it based on? What What is the basic Machinery that everything runs on? And it turns out that that basic Machinery is basically probability Theory. So for those of you who collect your statistics courses rejoice and we will, we will see how it all relates to to learning to training etc, etc. So anyway, let me start with a brief intro. Anyway, we live in some very interesting times. And usually, when I start a new class on machine learning, I have been teaching for what almost 20 years. Yeah, almost 20 years, I've been teaching learning and when I started in your class I usually start with like this historic all overview, right? And traditionally, I would begin with the picture like this one. It's just the random time line of the internet. Nothing special about this one. But, you know, I would talk about and they will talk a little bit today about how AI as a field as progressed starting from its beginning in the 1950s, then. 196 is the eye winter of 1970s then we go to the 80s and when neural networks reappear then we go to the 90s and 2000s with the probabilistic models and then we go to the revolution of deep learning that defines artificial intelligence today. So that's all well and good. And if you look at AI from this standpoint, you see like you know, a regular field of sense. And even if you dig deeper into some specific part of a, for example, January or whatever, you say some pretty reasonable time line. If you look at a time line from Before the year 2022. But recently, something has changed. Right recently? AI has started to progress in some A completely unexpectedly fast way, right? So this is a timeline. I made a couple of years ago, three years ago in the summer of 2023 and it was about the spring of 2023. If you recall, that was the time when GPT just appeared, it appeared in the late 22 but it was like not really popular for a little bit and then suddenly it blew up and then In the spring of 2023, like everything started appearing out once, right? I will not go through the whole time line here. It doesn't matter now, but like look at March 14th. March 14th. 2023. That was like. that, that was Yeah. Okay. Okay, so sorry technical question which I think I need to address. So can you see the presentation? Because some people say it's It's not. Let me check the presentations, but text on it. Not clear. Hmm, let me check so I mean. I, I don't want to switch to Sharing the presentation because I will then need to you know, go to the Blackboard and stuff like that. I'm gonna HD. All right, let's Okay, so let's let's do what you suggested. Let me post the presentation for you. It will be. So, it will be. It will take a long time to, to get it. To Google Classroom because I'm not in there but I will send it in chat right here, okay. so anyway, the spring it's already. So anyway, the spring of 2023 was Oh like this sudden Outburst of everything I related and specifically llm related. Okay, I send the presentation. It says, it's uploaded. And if you look at, for example, March 14th, here you see that on the exact same day. Alright. Google announced that it would be integrating llms into its workspace. It wasn't called Gemini at that point, but some of them Google didn't announce anthropic a small startup that recently, split off of Open. AI announced that it would be producing its own family of llms. Thought which we will know and love now. And but it was, but both pieces of news for completely overshadowed by opening AI, which came out and said that we are well, not yet releasing but we are announcing GPS for like the next step in this development of elements, at that point. and when I, Made this picture. three years ago, I called it the spring artificial intelligence and I mean, at that point three years ago it was completely possible that This would all. Still be, you know, in line with some regular development of regular science, right? So sometimes you have a breakthrough when you have a breakthrough in that in 2023, that was changed it. So, llm starts at work on, 200 have a breakthrough, you know, researchers go there. They feel in this new space with their research and then the field needs new brakes, right? So kind of progress goes by these scientific progress. Usually goes by this big steps when somebody discovers New Direction, then, it it's very quick for a while. And then it's closed down back again. So back then it was still possible if it would go like this but of course, it didn't and the rate of progress has not slowed down since 2023. we are still getting use basically every week and We are getting big news every month and in the field of AI. It's not slowing down on the contrary. It looks like it's spinning up, right? That looks like currently. The. Frontier Labs, the openai and anthropic they already are using their own models to make their own models better, right? So it's not yet the fully closed loop of recursive. Self-improvement that everybody was talking about, but I think we're getting there, right? And if we do get there, then, who knows what's gonna happen, right? And so we believe in some very, very interesting times. And I want to stress here because by now it's actually already not not obvious to people but I want to stress here that it was completely unexpected and very, very few people predicted this. So I recently came across this nice example. This is a book from 2018. Less than 10 years ago, right? So the Deep learning was already here. We already had, I don't know. Lstm reaction already had Transformers right? In 2018, we already had the Transformer. And the author of this book asked several prominent researchers went to the expect human-level. Artificial intelligence And the closest was none other than Ray quartz file, which you would expect and he predicted it in 2029. And that was the nearest prediction so less than 10 years ago. Most researchers would Place human level intelligence somewhere around, you know, 50 years from now. Things have changed, right? And this rate of progress keeps accelerate so, in this class, I hope we will actually Go all the way to the Motorola's nature, not unfold details. We cannot do it in full detail and rates, but we will start from the foundations of our traditional intelligence from the foundations of deep learning specifically of how neural networks work. And then we will discuss the main Classes of architectures of neural networks. And ultimately, of course, we'll get the Transformers, we'll get to Language modeling will get to the gpts and clothes of of today. but, Let's start at the very beginning, right? So I will still allow myself this guilty pleasure of doing a historical survey. Artificial intelligence is a very old idea, okay? So artificial intelligence, I mean, in a way, According to almost every religious tradition in the world. We are artificial intelligence, right? Because we were made in some traditions out of clay in some traditions out of some less lessons substances. But in any case we have been made by God and whatever the name of the god is, right? And we have been created with our souls with our intelligence. And so we are AI is according to the relations of the world, right? A more more modern. Kind of artificial. Intelligence ideas, can can be found in actually, Greek mythology, where, of course, whales but Hephaestus would Create like Android robots for himself and there were several, but the most famous was this gentle humanoid robot named Dallas. And that's actually pretty fine story. And that relates to how we view it relates to the field of as well. The Festus ultimately gave Talos or I think it was useful. It's took tiles from her Festus and gave it to to the king of Crete. I think and, on the island on the island of Crete, they Job of towers was to basically protect the borders, right? So tell us what would run around the perimeter of the island. and when tell us, so any ships approaching, It would take giant rocks and it would throw the giant frogs to the animation. That was his job. Um, what is interesting about this in my opinion is how things have how things have played out to be in terms of what's difficult and what's easy, right? So the ancient Greeks were already starting to be pretty good. At throwing big rocks to Great distances. They already had catapults, right? And then they were not very accurate, but then we got, you know, tribal Shades and then guns and then, whatever rocket launchers, whatever. So we are pretty good at hurling. Destruction to be distorted, with great accuracy, actually. but, The more difficult part. It turned out to be was to actually recognize any ships, right? So already, I don't know, for 400 years ago, you could have You could have a big and that would be pretty accurate and thinking the ship. But how would you automatically recognize first? The there is a ship on the horizon and second that the shape is here is an enemy ship and not a friendly one, right? So that's a computer vision problem and it that proved to be more difficult for Humanity to automate then. The Rock throwing part. Yes, I think pretty interesting. Similarly, okay, so there was AI in many different Traditions. There were the integrity and tradition. For example, there was this notion of a Golem and some wise rabbis could create golems and there. Okay? So that that didn't play out as the trajectory tradition predicted in there. There was a big difference between speech recognition and speech synthesis S&A task. So, a goal and can actually understand here. It can understand commands, it will fulfill the commands of the rabbi who created it. It will know human language, but it will never speak. So in today traditional it was like an understanding was okay for man-made constructs. But, you know, to actually speak, you had to have a soul. And of course, even the way device, Rabbi cannot create a new soul. So, so that that didn't play out as expected. And that was why Thomas Aquinas was the famous philosopher and the pupil of albertus Magnus the famous Alchemist. So, Thomas Aquinas was very, very upset. When his teacher albertus, Magnus actually created an artificial speaking head. And, of course, we don't know what it actually was, one hypothesis, is that it works, something like this. So it was just, you know, sound a device for transporting sound from a different room and somebody would actually speak through through the pipe. But you know, we don't really know. But what we do know is that Thomas Aquinas got very upset and actually smashed the whole thing to pieces Then in the Middle Ages, I won't go into details here. But you probably know there were like lots of very inventive automata, early robots, which are not quite robots in the modern sense but like, you know, human figures that can do some simple tasks automatically like poor water or something like that. And they were pretty inventive but they were purely mechanical not very interesting. Of course, for us what I do want to mention artists Automotive by Pierre. Ah, he was a Swiss watchmaker and actually the jacket row. Watches you can still buy. Although they are very, very expensive but it's an existing brand and He is like hobby on the side was making very intricate human-like dolls that would do very fine. Things with their hands and you know, that would actually do something interesting by themselves. And there was this draft Mano that would actually draw several different pictures. But what is really interesting? What I wanted to highlight was this guy, the calligrapher and the calligrapher is very similar to the draftsman because here so is using a whale to to write on a piece of paper. But you could actually program the calligrapher to write what you want. There was like this, I don't know a sister of Labor's or something. On the back that you would actually know you would change. You could switch some of the levers and he would write different letters. That, that was to my knowledge. That was the first actually programmable. Device right before Shakira's looms that are usually quoted as the pioneers of, you know, programming and that invented, Punch Cards Etc. But that was before, that's interesting. But of course, this is not AI as we understand it now, right? So there was no programming or to speak of there was no math. AI. That would be, I really related. And actually, I don't want to talk to much about this guy Ramen Lowe, but I mean, I usually mentioned him in Harbor space, because he's Catalan. But basically, he was an early education and you can, you know, kind of if you stretched definitions a lot, you can actually, you know, say that he did something that would later be related to AI but not really. Um, when when did they actually appear as a science? There are several starting points and usually well, basically there are two starting points that I will quote one is the 1943 paper on the mathematical models of neural activity that we will get to later when we discuss different and the other is the 1950 paper of volunteering, right? The Turing test, which I hope you have heard about. so, During was a very smart day and he was like, really genius. He did a lot of total breakthroughs in the field of computer science and in particular he basically invented artificial intelligence and the first question of course they had a person thinking about this stuff seriously encounters is Can you do an artificial intelligence like can machines think? And this is, this is the subject of Turing session of 1950, which I definitely recommend you read because, you know, old old research, papers are usually very hard to read. They use strange notation. They are cumbersome. It doesn't make sense. A modern textbook would be much much better would explain stuff much better but In this case during closet genius, right? So here's essays there, not really research. They're not so much research papers like philosophical discussions about stuff and they are still very interesting. So I definitely recommend you read the essays of hearing And specifically, the Turing test was in the sea on Computing, machinery. And intelligence. It was called and The hearing test itself. is very interesting in that. Like how it survived for so long, and how, and why, it's so long, right? So, you all heard about the during tests, right? So there is a church, the church is chatting in writing with an unknown entity, or with two unknown entities. And then one of the entities is a human, the other entities a computer. And basically the judge needs to A recognized, which was the human and, which was the computer, right? So, there are a couple of interesting points here. First note that It doesn't make any sense to run the Turing test once, right? So the Turing test actually kind of grew out of turing's foundational. Work on computer science on algorithms, theory of algorithms and randomized occurs. So the Turing test definitely, like, wouldn't tell you anything. If it was just one, If it was just one run of the experiment because of course, the judge can always just flip a coin with probability one half. It will be. Alright, alright, so when does a machine, when does a computer program pass, the Turing test? Not when it falls to church, once in a sense, but when it consistently makes it impossible for the church to recognize the program with any probability significantly different from one half, right? So, Right from the start. It's an interesting. Remark that we, we get to the realm of probability Theory. We get to the realm of randomized, algorithms, Etc. We'll talk more about that later. The other Intel. Okay, so now the main part Then I go for the founder mark. But now the main part, the main part about the Turing test is Unlike all other tests of artificial intelligence and I will give an example, unlike a lot of tests that you can test has actually survived for a very long time. So I think I have a slide on this. Yeah, so formerly the hearing test was actually passed just a year ago. Okay, of course, once you have stuff like gpt-4, nobody really doubted the gp4, could pass the Turing test in the original formulation, like they can fight for 10 minute chat. But you know, it was not trivial to actually run the test because of course if you're talking with a Frontier Model these days and you just ask it, well are you an AI? The model will tell you. Oh yeah, sure. I'm a language model. So somehow you would you would need the model to stay in character, right? And it's easier to do with small ones but small ones would not fall anyone. So okay, so there were some problems with actually writing the Turing test but once people did, of course, of course, the models passed, but it's very recent news. It's 2025 and The original Turing, test was a 1950. and that's And that is very cool and very surprising in AI because to be honest, AI as a health is has a very long history of moving. The goal posts. So, for example, the example that I want to give in 19 in the 1970s, there was this guy, Ellen Newell will meet him later. And here wrote a very nice paper. Like, what is the state of AI now and where are we going like this position paper? That would you know, Define where where how the filter and, Here at the end, he wrote well, okay. Did we have the hearing test? But of course, the Turing test is not really actionable in the 1970s. It wasn't, of course, you cannot expect AI models to pass the Turing test and there is no, there can be no progress on the Turing test, right? So it's not like you can full 5% of the judges than 10% of the judges than 20% of the judges doesn't work like that. Either you full humans or you don't and, So Harold. Okay, we need some kind of other tests, it will be Numerical in the sense that you could actually measure the result but also that will actually reflect something inherently. Important about intelligence. So like if the machine passes, it means that we actually are making progress towards artificial general. Artificial intelligence Sounds. But what is his example? His example was let's take Chess. And he actually argued for like, a page that well, chess is a very nice candidate because it's numerical, you can do, like, you can, you can play against each other play against humans to have an ill or rating. It's, it's measurable, that's completely true. But on the other hand and Chassis is easy to program in the sense that it's a finite game with, you know, fixed rules blah blah. But on the other hand, chess is such a human game. You have to, you know, understand the flow of attack and defense on the chairs or to have to maybe real have a model of the other person's mind and understand what the other person thinking about when he's making this move. So that you can predict presentations and maybe subvert them etc etc. So he was making this very plausible sounding argument. That chess is a Is a good middle ground. and then as you all know in 1997 deep, blue bit Casper off, And I think the last match where humans had a chance was 2001. Vladimir kramnik had a few matches against the best computers of the time and he actually like almost one at some point. I think he missed the maiden one, very famously at one of the games but but after that, It was completely hopeless. Alright, so after like 2001 there was no question who is better chess and by now or even buy, you know, 2010 to 2015 there was even nothing humans could help with, right. So for a while, there was this field of sand tower chess, where a human with the help of a computer would play better than just a computer, but that is also a thing of the past. But did they AI researchers in 1997 or 2001? Did they say? Oh okay, so we have the hi now. The test has been passed. Of course not right. What what we all said? Collectively is a felt was oh, okay. So you bitches well chest doesn't count Chest is too easy. Chess is, you know, you can just do a research and the research already gets you halfway to the best players doesn't count. Let's take go. The game of Go much better. You cannot really. I mean, it's still finite, it's still combinatorial, but you can never do a search train go because there are too many possibilities. The branch in factor is to be that's true. You cannot have a meaningful complete search stream go. It's like when in chess you have like 10 reasonable moves at most and going we have 50 to 100 reasonable moves. So it's completely impossible to do the depth search. but, Alphago happened, right? And then Alpha 0 happened and of course in though computers in 2000, 16 17 also became hopelessly veteran here. Well, did humans say now Alpha zero is the age? I Of course, not humans said, well go that's count and, and that is, and that's the history of a in a way and people still do that. People still say for some reason that llms don't count and they try to invent reasons, why Helen's don't count. But the hearing test actually stood the test of time So there was no moment in the 1980s. When somebody would say, oh, I passed the Turing test with a stupid script, so it doesn't count. No, they didn't happen. Why? So my main point here because What is the Turing test really about? It's about yes it's about natural language processing in a big part so it's about being able to talk in a natural language to a human in writing. But not only about that, right? The point of the hearing test is that When you have a free-form chat as a post to a chess game as a post to question answering or whatever you can talk about anything, right? You can you can actually, I don't know. You can introduce computer vision or at least 3D modeling into the Turing test. You can say, oh, hey, look, we are talking on the computer, right? So can you Tell me, what's on your desk, what, what's in front of you? What's on the left, what's on the right? What do you see, what's in the room? Can you please walk out of their own? Describe what you see? And then come back, and yeah, sure, you have no, no way to check of that true. But to actually make this picture consistent, The Entity on the other side would need to kind of understand the 3D World, right? And natural language is complete. In the sense that You can talk about anything. Right. so, Why am I spending so much time on this? Because in a way, this is exactly the reason why modern llms are so great. Right? So, All that modern llms basically are trained to do. I think we'll get there at the end of the class and I will explain it to you in more detail but the base of the lamps for they are actually learning to do is just predict the next token and text. Right. What is a language model? Language model is a Is a machine that predicts the next word, the next token in natural language. That's it. but, To predict the next token. You need to understand a lot of stuff, right? You don't not only do you need to understand how language works, but then you, so this, this will get you partly their part of the way there. But then, after you, understand how language Works itself in it to understand how the world works, right? So if you say, if the text says, theorem blah, blah proof, no. And that you are supposed to predict the next token. Well, maybe you need to prove the theorem first, right? And if the text says, I've been to Paris last month and I visited, I visited the museum. And then you need to predict the next word. Well, now you have to understand which museums are in Paris, right? So, it's Natural language includes everything. Well, maybe not exactly everything like it doesn't include stuff like robotics for example. So robotics is a very different field because there is no huge set of books on. I don't know. What is the angle that you need to? Rotate your joints in order to pick up a cup from the table, right? So this this you need to understand from other sources, but nature language is a great source of information for virtually everything. And and that's the reason why llms keeps surprise us. They keep getting this uncovering, this new capabilities that actually mostly come simply from predicting the next word and in text. All right. Thanks so much time on the Turing, test. Sorry. One, last point, a finite appointments during tests, I hope. So if you look at the hearing test, at this competition where the machine is supposed to talk like a human, you know, it has immediately that it is completely totally unfair. It's completely unfair to the computers. First of all, Imaging, the reverse during tests. Imagine that we are changing in text and I a human. I'm trying to pass for a computer in this dialogue. How would you uncover that I'm a human. What would be the question? What could you ask me so that you would immediately know that I'm not a computer and I would have no way to pass for one. Can you give me example of lemon pie? Yeah. So why would it distinguish him from computers? If you would give me this information, I would imagine actually Understand it, your llm. Why? actually, I don't know why, but why? If you, for example, some assistance, if you need some help and you can ask, for example, to McDonald's chatbot. Give me example of 115 or give me some program in Python, I would mean in the center your llm, you're not a real person. No way. But I mean, imagine the reverse human there were hearing tests, like I'm talking to you in chat and I am a person. It's me, but I'm trying to post as a computer, right? So I'm trying to convince you that I am a computer. Hmm. What would you ask? So that you immediately would realize that I'm not a computer. It was trying. Oh my God, very complicated one. Yeah, for example, sure. So, if you ask me what's, I don't know. 37 to the power of 23. I have no idea, right? And it would take me a long time to figure it out. For a computer is Trivial, right? So, So we would never pass the reverse during tests we humans, right? Even for the computers of the 1950s, we would not. but, But that's okay. So this is, of course, like inherently unfair But ultimately, you know, we do want the whole purpose is to teach computers to be like, humans. Not to teach humans to be like so, okay, that that's okay. but there is also one like more subtle unfairness in the hearing test, which is well, the computer needs to pose as a human. The computer needs to, you know, represent itself for somebody else. The human doesn't need to do that. The human just needs to be himself. that's, Unfair too, right? So they originally hearing test, if you read the essay, The Originals hearing test was actually formulated as follows. It should be a church. A German church, trying to distinguish between a computer posing as a woman. And the man posing as a woman. So that like everybody would need to play somebody else. And we need to to walk and in the show. So, you know, so some as a different person as you can. And you can understand why this little detail got lost in the, in the history of the hearing test. But but it was there, I think it's also pretty fine. All right, so that was this hearing test. But that's kind of on the negative side in the sense that of course in the 1950s, there was no way to pass the Turing test not able to to be closed and but it kind of got people thinking and the actual like positive field of AI as a science, when you actually tried to build stuff emerged in 1956, it was so called Dark Wolf workshop at Dartmouth, obviously. And it was organized by these four very famous researchers. John McCarthy was the early programming language which is a guy invented list. Marvin Minsky was the guru of neural networks. I hope you all know, Cloud Shannon, the author of information Theory, and the senior Rochester. I keep forgetting what he did, but he builds some computer at IBM. I'm very early and very famous computer. And the 1956. Workshop. Had what I think I always liked the quote it because I think it was the most ambitious Grant proposal in history. And in the 20th like this we propose a two-month study of artificial intelligence by 10 people. In the summer, blah blah. We will attempt to find how to make machines use natural and, which is find extraction of Concepts solve problems. Now, reserved from humans and the cells. This machine learning, right? We think significant advancement in one or more of these problems as possible. If a careful is select a group of scientists works on it for a summer. Okay, and they were founded. They got together, they did Conduct the workshop. and, But this this grant proposal of course they didn't actually do anything like they didn't actually solve any of these problems but they kind of understood how difficult they were, but still the 1950s and their relationships was a period of very high expectations. It was the Golden Age of Science Fiction. Everybody was, you know, expecting Androids to walk in a few years was expecting Androids to walk around to bring you coffee to talk to you. In human language, etc. Etc. That was like that was the time when science fiction was starting to what was expected to to become a life very soon. What people actually did the actual progress was, of course, very limited, but it was still very good progress. So, for example, there was this logic theorist program, which I will not talk about in detail but it was a fair improver back in the day. It was thought that the important part was to teach AI launcher to teach a math. Now we kind of understand that it doesn't work that way, but it was a very good proverb for its time, it's actually successfully reproved. A lot of fundamental, a lot of the fundamentals of mathematics and it kind of oh, this early high expectations, And there were some other examples doesn't matter. But basically what happened in the early 1960s, The optimism didn't work out. Okay. So and Sorry, I don't have it on the slide but like the the main example, the primary example why people was very disillusioned in AI in the 1960s was a fail permit on machine translation. Okay, so people actually expected in the 1950s that they would write a program that would translate from English, from Russian to English, believe it or not. And that it would work. And of course it was completely beyond the ability of computer science at that point. So in 1961 or 62, there was this big report that said well okay, so machine translation basically doesn't work, we need a lot more research. Let's regroup and then, you know, the government, got the solution, they stopped, giving out grant for AI. And when you don't give out, grants for research, researchers move to other fields. So ultimately what we had in the 1970s is now known as the AI winter. And there I will enter means that there were very few people actually working on AI on artificial intelligence. It was believed to be kind of too hard impossible and inaccessible with current techniques which was true in the 1970s. So it's not like people are wrong. The only thing that actually was happening were expert systems and expert systems. They're kind of also AI, but there was a very specific kind of and you try to When you try to perform probabilistic reasoning on. A small Snippets of the main knowledge so to speak. So for example, okay, so the main example is probably my sin which was 1976 system. For this for Diagnostics, Medical Diagnostics based on what tests. And like, what is a blood test? What are the results of a blood test? It's basically a big table of 15 numbers, right? You have red blood cells, white blood cells hemoglobin. I don't know what was iron, whatever. All sorts of chemicals found in the blood. and, An experienced doctor and experienced physician can look at the blood test and say, oh, is that this is, oh, is this disease, right? So that's the diagnostic problem, but However, experienced The Physician is however I don't know whether he is a genius diagnosed like Dr. House it actually Complete is completely impossible for a human to just sit down and write, you know, a function of 50 variables that would just give you the diagnosis. Human brains. Don't work like that. Even if you kind of know what to look for, ETC. What you can actually, formulate is not a General unifying function of everything but you can formulate some local, heuristics. Like if the red blood cell count is high and the iron is low then it's that and if they don't know alcohol content is 20% and its this and so on and so forth. So you can ask doctors to give you this kind of local heuristics rules. And then the AI question. So you do not question the rules, the rules are like given to you from from a trusted source so to speak. But the AI question is, how do you combine the rules? So now you are given a new blood test and there are all sorts of problems. Like, okay, you have like 450 rules and 20 of them, kind of apply. But also they don't like apply. They kind of apply because the rule is again, not a mathematical function, a human doctor cannot do that the role. A role is something like if the red blood cell count is high and what does hi mean? Medically. Well. This like this high is definitely high, this highest definitely not high. But what about this? What's in the Middle? Where is the trash hole? Probably, there is no fresh will probably, it's a continuous function. So there are all sorts of difficulties here and that's what people were doing in the 197 just I won't spend time on that because that's not our subject definitely. and, And then what actually happened. So let me skip almost to the present. What actually happened was in the 1980s. People, again, got back to neural networks. That was the in the 1980s you already had. Convolutional networks and recurrent networks, and multi-layered net deep networks. So, basically, you could have deep learning in the 1980s 1990s but he didn't mostly for technological reasons. so people already kind of realized in neural networks are cool, but they didn't really work because there was not enough date and not enough compute to make them work, you need more and it all came together. And The middle of the 2000s. So to say, so in 2005 to 2006 to 2007, several different Labs, specifically Jeffrey, hinton's lab, and Joshua been just left. They actually kickstarted this deep learning Revolution and that's when everything came together. So by that time, Due to the internet due to, you know, increased computational capabilities. You already had enough data to make neural networks work. and, You already you also started to have enough compute, we started to have enough computational power to train, large enough, neural networks. And like the final step was actually going from CPUs to gpus. So we'll, we'll discuss it later when we discuss neural networks actually, but It's kind of obvious that if you look at neural networks that everything you do, there is highly parallelizable and it was a very natural idea when gpus actually appeared. And it was a very natural idea to switch from CPUs, which are like a few very fast course. Like four course, four gigahertz each switch to gpus, which are much slower but with hundreds and thousands of cores and that that gave you like this. Final boost that made deep learning actually work and starting from the late 2000s. Deep learning has neural networks have been by going from subfield of subfield to machine learning and they have been setting state of the art in a lot of different fields. So we'll discuss that later. and now, Let me and the historical part here and now about what machine learning actually is. So how do you define what it means to learn, right? So what is learning? And I will. we will get to a much more technical definition a bit later, but If you open some old textbook from the 1990s, you could find the definition of like this. So, like a computer program, learns with accumulating experience regarding a class of tasks. T, and the performance measure P is performance on this task, improves it against your experience. So it doesn't say much, it sounds very trivial, but Here. So what this, I think important here on this slide is that when we are talking about learning We have to have. A performance measure, right? So we have to have some kind of number that goes up or down whenever it needs to go. Because if we don't, then we will never understand. Did we learn something or not? Right. So in a way, They have half of deep learning is about inventing the loss functions. It's about inventing this objectives. What is the number that we want to get down? What how do we Define the error? So that when we minimize the server, we actually get what we want. Right? Sometimes it's very easy but sometimes it's kind of non-trivial and sometimes as part of part of the science and this, this is the conclusion from this. and, Also, I think you have all seen at some previous class or somewhere in your life, you have seen this. Main like, taxonomy of machine learning problems. Let me A go through it. Still, we will not talk too much about it later in class because we will mostly exclusively. We will be in here in the supervised learning part. But let me just mention what kinds of functional learning problems. There are so, technically machine learning problems are divided into supervised learning unsupervised, learning and reinforcement learning. And supervised learning is what we intuitively think of when we think of Machinery, like I need to build a classifier the distinguishes cats from dogs on a picture, right? So how do I build the classifier and distinguishes case from dogs? I get a data set of pictures and for every picture I Mark with, or it's a cat or a dog and then I trained a classifier to distinguish between them, right? So I think it's a good. It's a good time to actually start. Doodling, on the board. so, In supervised learning. Okay, there is the whole machine learning. and in supervised learning, You have. Yeah, one sec. I'll be I'll make a little more comfortable. So I Write better. So, in supervised learning the data set. Consists of pairs of X and Y. Right. So, for example. So X is the input. And why is the output that you want to get? And your machine learning model. Is actually a machine. It's let's say a black box for now, will get there later but it's it's a machine that takes the input. And produces some function of the input that is supposed. To look like the output. Right? So we are trying to make the input. The interim, we are trying to convert the input into the output for example if we are doing Simple, classification, simple, binary classification. So there are cats and dogs here then. Probably a f of x is like a number from 0 to 1 and if it's close to 1 then we say it's a cat, if it's close to 0 then we say it's a dog so it's kind of its supposed to be the probability of a cap. But notice that it's the probability of a cat. For a given picture, right? So it's the probability of a cat given X. And that's the whole point of supervised learning. So the point of view provides learning amazingly speaking is to learn, whatever that means, we'll get there much later, but it's to learn the conditional distribution. P of Y given X. so, we are always assuming that we will have the input. The classifier, the distinguishes gets from dogs, cannot draw you and you get picture. It's not supposed to It always presumes that you have a picture at the input and then with this picture, you do stuff. So computer vision works like that right in computer vision, you always assume that you have a picture of the input. Well maybe a set of pictures maybe video whatever but you have some high dimensional very complicated. Input. And you're supposed to, you know, break the input down and to some answers into the answers to the questions that you're interested in. And it's not necessarily specification. There may be more interesting problems. Like object detection. We'll talk about those in class since since we are doing computer vision here. But overall, you are trying to take a complicated input and convert it to some relatively simple out. So that's what you provide learning is about. And you, and when you collect the data set for supervised learning, you always need to have the correct answers. So sometimes and the computer vision, unfortunately, very often, it means that you need to have some very complicated labeling. All right, and labeling is very difficult and expensive. So we'll talk about that when we get there, but for for classification, it's not that expensive. But for things like segmentation proper labeling is extremely expensive. So we need to, we will need to somehow, you know, do with relatively small data sets. But that's only the first part, right there is all. So So there is this other field. where, There is no why? There is no correct answer. The data set is just a set of something. And the big question is, what are you supposed to do with it, right? So, okay, so now we have a data set of pictures but the pictures, the image is They're not labeled in any way. So what, what are we even trying to do? What, what is the goal here? Actually turns out that you still can have a meaningful go and you can still do the stuff that will be very, very useful for Downstream problems. Like classification, Etc. ah, and usually what answers is doing is Something called. Let's call it dimensionality reduction. So reducing the size. Of x. Compressing it. So that on the one hand you can press X down to something. I still have a black box but now the output is not Some small known thing, but the output is, let's say a vector of numbers, right? And X is still Let's say a picture. but, now, the goal is not to Classify executed him. But the goal is to compress X down from its original size. And we will, actually, I think we will talk about this more. But images are big, right? And if you think think of images, as sets of numbers, they're pretty big sets of numbers, right? So like how many numbers question to you, how many numbers are there in a one megapixel photo? It's one megapixel. Is how many pixels? No. Come on. Don't try to compute gas. Yeah. Well, almost right. So Megapixel is not a million pixels and for functional. It's one 100024 square right? So it's a power of two but what, whatever. Okay, it's it's close to a million and how many numbers is that? like, if I take an image of one megapixel, And I say that, okay, I want to view it as a set of numbers. What is the damage? How many numbers are there? How many numbers in a pixel. Come on, guys, you're in for a computer vision. Number three numbers, right? Right, there are three numbers in a pixel. So a one megapixel photo, which is not that large is 3 million numbers approximately. Right. So if you think about this space of possible images, it's a huge space. It has a huge dimension. Nothing works in that damage, right? So it's it. And if you think about like, what is the structure of the set of images in that space? Well, we Collective Humanity. Have absolutely no idea, right? So, it's very, very difficult. We have no idea how to how to describe this. So, It's some very complicated manifold in this in a huge space of Dimension. 3 million, right? So like imagine, we can't imagine, but think of this set of like real photographs, Among all possible pixel values in dimension, 3 million. What is the structure of this set, right? This this is completely incomprehensible. I can only say that it's an open set, right? Because if you have, if you have a real photo and you and you move every pixel by a very, very tiny amount. Nothing changes, right? So it's still a real photo, but what actually distinguishes, real photos from from random noise, we have no idea, right? And we have no idea what is the geometric structure of this menu? It's probably extremely complicated. So what is ANSI provided in trying to do here? It's trying to map this extremely complicated manifold of Freelancers. To dimension. Much smaller. Let's say, I don't know. 500 that's just a number out of Okay, once we are out of nowhere doesn't mean anything. But basically to project this huge space of images down to a more manageable, still large but more manageable space where hopefully, It will be. More comprehensible either to work with manifold, right? So that that's usually the idea of once you provide learning, right? So you want to To do what in machine learning is called feature extraction. You want to feature extraction or representation learning, representational learning? You want to map a bit object, like a name image to a small, much smaller object, like vector of numbers, but you want to do it in a way that would not lose important stuff, right? So you can just take the first one, 100 pixels from here, that that's not gonna work. You want to map it and such a way that You actually, you know, are able to answer interesting questions in this space of these in the small space. For example, in the main fall of real images, you see will be able to distinguish cats from dogs. So like cats are here and dogs are here. And now all of a sudden in this space, in in these 500 dimensional space, there is actually like a linear hyperplane, the linear surface separating, cats from dogs and it's very easy to separate kids from dogs over there over here. Like dogs are this part and cats are this part? And there is absolutely no way to disentangle. Okay, right. so, Point usually a fancy provides learning, compressed down, make it more manageable and hope that in this more manageable little space. You actually can have a relatively, same simple, machine learning models, doing the stuff that you actually want. So like this kind of compression is never the end go, right? You don't want this vectors by the cells. We want them for some ultimate purpose and but the thing is, we are not, we don't we don't fix this purpose and answer and we don't know, maybe we'll use it for that. Maybe we'll use it for this right now. We just want to get good features. How do we do that? Well actually, there is a pretty simple answer. Which is very common in deep learning specifically. So while we are talking about this, let me let me tell you. So of course, we cannot have a data set with the correct disease, right? There are no correct this. We have no idea. What is the correct representation in this low dimensional space. So, how do we verify that this Black Box is doing anything meaningful? How do we, what? So here we have in supervised learning, we have a data set is accessing wise and we can just run the Black Box through the examples that we have and check that we got. We get correct answers, is it? Over here. There are no correct answers. But we cannot as we will see. So we cannot train a neural network without a loss functions, right? We cannot train in your own network without some kind of goal specific numerical goal that we want to optimize So what would be the goal here? and, There can be different answers but in deep learning one. Very common idea is to do a thing called an autoencoder. Which works like this. So I have this big thing. X. I get it through my neural network, okay, that doesn't matter if it's in your own network. Through my first machine learning model, which is called the encoder and I get, The vector Z. But let's not stop there, let's say, okay, so how do I verify that compression is good? Well, compression should. First of all, compress down to a smaller size. Here, it's by definition, I choose the size of the myself. but, What does it mean to compress something? And not just pick random numbers? It means that from the compressed object I can reconstruct back to the original. That's, that's the whole point. Like it wouldn't be, it wouldn't be a very good archive tool it. If it would produce just random bits and you would have no way to recover the files, right? So the whole point is to compress down in such a way that you can decompress back So we add the decompressor, right? We add the decoder part. Which takes the Z. And tries to restore. The original image. Let's say it's X hat. So, X is the input. And X hat is the final output. So the decoder is probably also in your own network. The decoder is also a complicated neural network, right? It's like a generative model takes in something like that. Looks like random noise just number and should produce a beautiful cat picture, right? So it does make our task more difficult. Sure, but now, We have a very easy way to say what we are looking for, right? So now we know exactly what was function, should be because the result should be just, you know, Similar to the input, that's it. And you can Define what's function basically like X head, minus x squared like just a square deviation in the pixels. That's okay. That's a very common loss function and in ordering colors. So, Uh and so this kind of idea compressed and then decompress back, we will encounter it in class A couple of times and it's it's a very natural thing to do in unsupervised learning. So when you when you are just trying to make sense of of your inputs of your data set, how do you what is your goal? You're trying to find structure inside what does it mean to find structure? Well, actually in reality, it usually means to project down to a smaller space where you can see the structure more clear, right? and, if you've heard the fancy provides during before, You. Probably heard about the like the example that was characteristic that was decentral, example of fancy provided for a long time. I think now, what encoders in the nationality reduction in general are more important but for a long time. They the main example of a fancy learning was clustering. A clustering. We we want we want to talk about that much out of scope for us. But clustering is this problem. You probably have like an intuitive understanding of it. When you have some points, some objects, right? And your task is to Split them into groups clusters, so that points inside the cluster are similar to each other close to each other and points across different pastors, a different right? so, the only thing I want to say about clustering is that, it's exactly, you can view it as the extreme form of dimensionality reduction, So, it's clustering clustering. Is all. So, Means also taking a large object and compressing it down to Z in a smaller space. But now the dimension of the space is 0 okay, so we are compressing we are compressing each point to the label of its cluster and there is like just a finite state of the different labels And you can view it like that, and it's a very natural view of clustering. You you can press down to a discrete finite set of points and then if you do it in such a way that decompression is as faithful as possible, still, right? So the whole point of clustering is that you kind of want to replace all points in the cluster, by its Center, or by the cluster label, and then you will be able to deconstruct the points as best you can. and yeah, okay again explaining too much time on super wrestler in but yeah it's it's useful I think and If in supervised learning, we were learning the distribution people. Why even X In unsupervised learning, we are just trying to learn pox there is no why, right? So and how does it map to this Auto encoder or to the classroom picture or whatever? What does it mean to learn the distribution? Well here in the auto encoder part, it would probably mean to learn to sample from the distribution. So here you would say that D is kind of like random noise. And the decoder. Converts the random noise into X that Is supposed to be from the distribution of get pictures, right? So, I don't think we'll get to this kind of analysis and plus, but again, useful to keep in mind. So, in supervised learning, we always have an X, we always have the input in answer, you provide learning, and we are trying to describe the exit itself. And very often, it means that we are actually learning a generative model that can produce new samples of access. In the case of pictures that can draw new pictures. Okay. And finally, there is the third guy. Which we will not talk about at all. We just called reinforcement learning. And yeah, I think, I mean, unfortunately, I cannot make this class about everything. So, let me skip praying, forcement learning, but basically, it's let me just say, if you were reinforcement, learning is the The sap field of machine learning where there is no data set in the beginning. so, instead of the data set you have your model, B being like an agent in an environment. and, The data set is ultimately the experience of living in this environment. So, for example, if you're learning to play chess, then your agent is just does not have a data set of correct moves. And it is not just trying to, it does not have a data set of all possible positions from chess games and trying to compress them down, like an answer provides learning. Know what's your agent? What what's your model is probably doing? Is it's playing? chess against itself, for against earlier, versions of itself for against other models, or whatever and learning to place it goes from the signal of Juan Right? So that that's how reinforcement learning works. You leave in your environment, you get A rewards that are in the case of Chess, it's simple. That award is who won in robotics, the reward, maybe more complicated but whatever you get rewards from the environment, and ultimately, You. Get rewards from the environment and ultimately you learn to maximize this rewards so there are you learn to behave? You learn a policy for behaving and environment. So such that the report gets maximized actually. It's a pretty different topic. It has some pretty different approaches from supervised and answering. So we will not be talking about it and in class I hope you will have a separate class and RL at some point. It's it's a very beautiful field. All right, so we discussed this. I don't, I think we'll skip this practical things like, cross validation and stuff. Maybe someone will talk to you about this and in the Practical part, Yet, I mention it reduction. Um, all right. so, I think. Now. Is a good time to have a break. We have come to the end of the intro part. Oh, yeah. And sorry. I should have started with this. I forgot to talk to you about the the class itself and a structure. Basically, unfortunately, I'm not able to come to Barcelona this year. So, I'm teaching online, and my colleague, Alex Davidoff will be with you offline at on campus. I will be delivering lectures and it's it's not what I would advise to do. But for logistical reasons we will have a lot of lectures at the start. So we will have three days of lectures today, tomorrow, and Wednesday. and I hope we will make some good progress and Get to. And and and have a good start so that Alex will will have something to work with when she begins on Thursday. Ah and then I think we will mostly alternate like this, like two lectures, to practical sessions and so on. And ultimately we will even it out. So I will be mostly await next week and then then I'll come back for for the final picture. Okay. so, Let's have a break. Are there any questions about the first part or the structure or whatever? How long a break do you need like offline? It's usually have an hour but maybe online hit that much. How long would you like 15 minutes? Okay. Okay, so let's say 15 to 20 minutes and it's 11, sorry, 10 for you write 1035. So on 10:50, then 55, let's continue. Okay, right. oh, You. All right. Let's continue. In the first part while you're getting back, I'll do a quick recap in the first part. We discussed. The history of artificial intelligence, highway to, you know, came to to be the earlier ideas like the Turing test Etc. and, Specifically. On point specifically, something actually useful for our machine learning class. We discussed the main and like the most common taxonomy of machine learning problems, right? This distinction between supervised learning Concepts learning Country, and In the second part. Today, I want to talk about what learning actually means. and, I have always understood it and the recommend you to understand it through the biasm perspective, through the probabilistic perspective. I will explain what I mean. but first of all, Like for those of you who have had, I don't know probability Theory classes in your University is over in Harbor space. You're probably kind of not very happy to hear that. Machine learning is pure probability Theory from start to finish because usually when, when I say probability Theory to my students, they get a little bit scared because a probability Theory class is some, usually, some very involved, difficult mathematical stuff about measure theory about, you know, you start with the sigma algebra of measurable, burial sets on in the euclidean space and then you're introduced your probabilities and measure and then you, and then what the expectation is is Already pretty difficult. And what the conditional expectation is extremely difficult and, you know, it's it's awesome abstract theorem Etc. We won't need any of that stuff. I'm not saying forget it. Don't forget if you know it but we want any of that. We need, you know, as there is a saying, I think by one, is it in, education is what remains after forgotten. Everything you thought So this this is exactly this kind of thing. What we will need in probability theory is the intuition that remains, after you forget all about the theorems and you actually You know, you you actually get this basic intuition of what probabilities about, so what is it about? It's about random variables, right? And random variables. There are discrete random variables like coin tosses. I like pointers or should have prepared coin tosses, and die rolls and stuff like that. And if you have just created set of, if you have a great set of William price, and if you have a discrete set of outcomes, then the probability of this outcomes should sum to one and that's your probability, right? That's your invariable. And then, you can have continuously in the variables where they It instead of probabilities of outcomes, you have the density function, right? And at this point, if you had a probability Theory class, he will tell me, oh, wait, but not every probability has a density, right? And maybe probabilities, including important ones, are cannot be characterized by the density and therefore, you need measure Theory. Blah, I forget about that machine learning. We only deal with kind of standard and Easy probabilities. So everything that we will ever discuss will, of course, have a density. And in that case, the timing to one means taking an intro, right? Taking an integral over the probability space. And again, there will be no exotic probability spaces here. Only the real line art of some power on the eclipse. Um, and the things that we actually need in machine learning card is basic intuitions and the base the very basic definitions of probability Theory, right? So you can have and okay. So now what I really do, hope that on this slide there is nothing new for you. If there is I recommend, you know, repeater probability Basics a little bit because we will be using some of that. But okay, I'll just go through this very quickly. If you have two events, two random variables, they can happen at the same time. Then you can Define The Joint probability, right? The effects. Why should let me switch? Better to explain it more interactively, right? So The. Ah, okay. So there are random variables characterized by their probability Mass functions. P of x if they are discreet. So, like, just what is the probability of every outcome on the die from 1, to 6, or by density functions. Like, I don't know, maybe it's concentrated from 0 to 1. We'll have an example like this today, then it's some function. Whose integral is supposed to be Equal to 1. And this is the density function for a random variable that samples you a number from 0 to 1, right? And if you have two random variables and you can have their joint probability of XY. So P of XY is something like P of x equals to something and why equals to something else. Right? So if you have your joint probability and you want to get on the marginal, it's called the marginal probability of the probability of one of the X and y's, then you need to kind of sum this over. Why? It's not a very formal way to write about. I hope you understand what I mean. So if you have like, P of x equals, a, and equals to something else and you want to get, what is the probability of just povert equals a you need to sum over all possible values of Y, kind of makes sense. and from The Joint probability, we get the notion of conditional probability. This is the most important notion for machine learning. So what is conditional probability? Conditional probability P of x given why? Right? Is the probability that X let's say is equal to something. Given that we know the value of y. Right. and, Formerly, it's very easy to Define. Formulate, just With the joint probability of XY and we decompose it into P of x given y times P of Y that this formula has some name like four probability for something like that. I keep forget, it doesn't matter. But the point is, this is the definition of conditional probability. So P of x given Y, is defined as P of X Y, divided by P of Y. All right. And we'll have a lot of conditional probabilities later today and tomorrow. Probably. And if you look at this definition, if you look at this decomposition of the joint, probability into the marginal in the conditional, then, you know, just that you can do it both ways, right? You can start with why? Like we did here first. We, I mean, okay. One way to read this formula is how do you sample X and Y? Well, you can start with why you can sample wife first from its own distribution. And then you already know what, why is, and you need to sample X. Even this very Or. You can start with X, you can first sample, X, and then sample. Why give an X You can hear this way. But it's still I'm a formerly. It's still the definition of conditional probability, just the definition of pure white given next. But if you combine this formula's, you see that like this they amount to the same thing to the Joint. Poxy. And this is where you get like the most important formula in the whole world, definitely in the whole machine learning. But I think it's wider than that. and that formula is well P of Y given X is p of x given y times P of Y. Divided by P of x. Right. This is the best bass roll. Or base formula. and, The way we presented. Now it's completely trivial, right? It's just directly basically follows in one line from the definition of conditional probability, but like, In effect philosophical. Um, that's Basically, how reasoning works? Our actual real reasoning, not logical derivations, where there are no probabilities and all facts are known for sure. In real life, we sell them know facts for sure, right? In real life, it's all about balancing, the probabilities and weighing in the evidence And this is like the database formula underlies, how you account for evidence. How you actually, you know, take something into account. We will definitely discuss it more. But before we do that, one last thing, there is also this very important notion of Independence. And basically two random variables are independent. If P of X Y, their joint. Probably joined entity. Is it will appear effects times Poe for so, if P of X Y, decomposes into the products of individuals or individual probabilities, In this case, there is the conditional Australia, right? So, basically, the same thing, you can say, pox given Y is equal to just pay of X, right? The conditional Australia. It means that P of x p of X does not depend on the value of why, right? That, that's why it's called Independents. So to wearables are in development, which basically means that you can sample them separately, You'll get the same result like two coins that you toast in a row. and, Let's get back to the bias formula and let me actually. Just first be stated in. Slightly different notation and then we'll discuss it. So, let's let's call it the main formula of machine learning. And let me write it like this P of theta given d. Equals P of D, given Theta times P of theta. Divided by P of D. Okay. It's the same formula, right? I just changed The annotation. But I hope you kind of now and understand what this notation. It's supposed to represent. So now D is the data. These data set. Right. And Theta. Are the model parameters? Theta. Is what we actually want to learn. So for if we are talking about a neural network, we want to learn the weights, right? And notice that it's not the exact value of the way. It's, it's a whole distribution of it, so it's, we will get back to that. But for now, let's just say Theta is the model parameters Theta is the way it's a linear regression. That's going to be our first serious example or Theta is The weight. So when you're all Network or Theta is just the probability of the coin that we are trying to learn. So let's say we have okay, here is my point, it has to say and I can toss it and I can get some results. and, The data will be the set of outcomes, the set of results of what I'm getting from the coin tosses and the parameters will be just a probability of getting heads, right? So the whole point of machine learning, Is to. understand to learn the model parameters from the data, right? So we have a set of outcomes for some stochastic process, for some random process where there is some inherent randomness. And we want to understand. What was governing this process? What are the parameters that went into this process? This is the whole idea of machine learning, everything else is basically commentary. And the biased theory is the main tool. For this. Why? What is so special about this? So let's let's discuss what we have in this formula. On the left. I have P of Fate again. D is called the posterior probability or the posterior distribution. Posterior means. After the fact upper stereo, after evidence has been included. and, That's what it says, right. So it's very, very intuitive. I get some data and I want to understand what I now think about Theta. How my understanding of theta has changed given data. After I have taken the data set into account, that's the posterior distribution. I want to I want to this is my goal in learning, right? So, okay, the final goal will be doing predictions. We'll get to that later. But the intermediate though, is learning what I can about, Theta from the Okay. And usually there is no way to to get to this distribution directly without going through this formula. So how do we get to this distribution? Well, the best role tells us that it's the product of two things, basically. it's the product of P of D given Theta. Which is. Called the likelihood. So, what is p of D given Theta? It's the um, it's the probability or that usually the density of getting a specific data set. Given the parameters given the model parameters, I'll make a coin tossing example. In a second, it will be clear, but basically, when you define a model in machine learning, you usually Define the likelihood. This is the easy part. The likelihood is what you get from just, you know, listing your assumptions and writing them down as formulas. And the main point of the best rule is that the likelihood is not enough. You also need the third part, this guy, we just called the prior distribution. Or just the prior. The prior is. Just be often without any d. Right? And what does it mean for Social Security and means what were we thinking about Theta? In advance. before we start to get before we started, Getting. D, right? So PPO Theta. Without any d. And I will make an extensive example in a minute. So, the bias formula basically tells you if you want to get the posterior distribution, if you want to Incorporate D into your thinking of theta. You need to take. what you thought about it before and multiply it by the likelihood of the so, for example, For example. Oh sorry. I I wanted to say, I didn't talk about the denominator but I forgot to say that I didn't talk about it so they did not nominate her in data. I didn't talk about it. It's usually called the full probability or the evidence probability, or something like that. And Mostly of this is not really important for us in machine learning, why? Because it doesn't have any fades. okay, so in machine learning are P of D is usually completely inaccessible by itself. So in stead of writing, the full bias row actually, usually be used like this P of theta given D is proportional to P of D, given Theta times P of theta. so, this means proportional, And what does proportional mean? In this case, it means that well, P of theta given is should be probability distribution, right? So, it should integrate to one. So, Almost always actually completely always. I know. No exceptions, P of D. They only way to compute P of D is to make it a normalizing constant for the numerator. So P of D is always just this. Okay? And in some special cases you might be interested in puberty. Yes. But usually what you do is what you doing, machine learning deep learning. Usually you're just interested in, let's suppose maximize in this with respect to Theta, and if you maximize this, it's the same as maximize on this and you don't care about the constant, right? So we'll get to that a bit later so the denominator is is complicated but usually not really necessary. So we want to talk about that too much. Okay, now example. Let's learn a coin to us. Okay. Here is a coin or what passes for one. It has two sides. And I can toss it. So how many parameters does a coin have? What is the size of the vector Theta? Can you tell me? How many numbers do you need to? Define a coin with to say, it's Okay, maybe I'm not asking the question clearly enough. So Bitcoin is a stochastic process, right? It's it's random variable. I toss it, I get either heads or tails with some probabilities. So how many numbers do I need to Define this probabilities? How many parameters? What are the parameters for a coin? What what probabilities do you need to fully understand the contest? Maybe just Yeah precisely, of course. So in a coin has just one parameter very, very easy. The simplest example, we can think of. So let's say Theta is the probability of heads, okay? Then the probability of Tails will be what? minus 8 says, and this is our first example, our first illustration of this probabilistic view of machine learning and Now you can start seeing why the likelihood is very natural. So what is the likelihood now? The likelihood is this is p of D given Theta. Like what is d? D is the data. So it's the sequence of outcomes. D is like I've been tossing this coin several times. And I got like, heads, Tails, heads heads Heads, tails, Tails, whatever. Okay. so, P of D given Theta. Is very easy to Define it directly follows from from just the model itself. I just need one additional assumption, which is by the way, very important. It's true throughout the whole machine learning and every model, it's it works. I need an assumption of conditional Independence, which didn't talk about that, right? So Independence is like this and conditional Independence is when, let's say excellent, why are conditionally independent given Z if this holds, right? So this is conditional Independence. A conditional Independence. So we need the assumption that different data points are conditionally independent, given the parameters and again, sounds very complicated, very messy, but it's very natural. So like if I already know what is the probability of heads, Then different pointers are independent. I post the coin again and again, I get the same probability of heads. That's the basic assumption, right? so, in this case, it means that P of D given Theta is decomposed and to P of like D1 given Theta times P of D2, even Theta bla bla times P of D and giving and what is p of D12, blah blah given Theta. It's the probability of one outcome of one sample and data set. One sample on the data set is one point us. Either heads or tails, So this is our P of small D given fate, right? Actually to make it formerly correct. Let me just put Faith here from the very beginning. Why not? All right, so this is like Theta is the probability of head. So what is the probability of heads? Given the data is the probability of heads, it stated. What is the probability of tails? Even that the probability of heads is Theta? It's 1 minus 8, right? So, over here. Everyone of this mod is either head or tails? Right. and, Okay, let's let's work through an example. So let's say that, this is my data set. So D is heads, Tails, heads heads Heads, Tails, tails. What is p of D given Theta? And Can you tell me? The actual number. Well, not the number the formula. the probably have had even data multiplied by the probability of Tails, even their own and so on. Okay. And what is it? like we know, what is the probability of heads and tails to the power of number of, Heads that you. Okay, let's say four. one minus Delta to the power of Number of Tails number of trails or n minus number of heads. Right? Right, exactly. So the and this is the likelihood, Okay. So, this is basically always the case and machine learning. The likelihood is easy. The likelihood is well, okay, maybe it's not easy. It may be very difficult complicated for me, but the likelihood is like our model itself. We when when I say we Define emotional learning model, usually what it means is we Define like we Define the assumptions that let us write down. This kind of formula. So for the coin, what were the assumptions there was the Assumption? Well the Assumption like the model of the process there are two outcomes they are usually exclusive. One of them has probability Theta. The other correspondingly has probability 1 minus Theta and this basic assumption that their conditional independent given Theta, which is always the case in machinery. so, This is this is the likelihood of a coin for you, okay? And what do we want to do with it? In machine learning. Well, there are some things we can do but while we only have the likelihood, the only thing we can do is the likelihood is try to maximize. okay, so the first like type of optimization problems that arises the first type of tasks that we sold from generating is finding the maximum likelihood hypothesis. Like fate ml, let's say is Theta that maximizes P of D given Theta. Right. Okay. Let's do it for the coin. Okay, so let's maybe not work with the specific numbers, four and three, it doesn't make much sense. Let's say in general, we have our data set is and Hats. And M tails. Right? So we have P of D given Theta. Just like you said, you already said it. It's fated to the number to the power number of heads and 1, minus Theta to the power number of Tails, okay? So, how do you maximize it with respect to Theta? How do maximize stuff? And you. Yeah, it sounds very difficult, but okay, in this case it's gonna be pretty easy. So let's take the derivative. Okay, the likelihood over Theta, can you tell me there is a Man guys, you can do it for a polynomial. Let me try and Here, you forgot. Yeah. Yeah. alright, so first the derivative of the first Factor right times the second Factor, then Minus that in our n. And oh, sorry. Hey, you're right. You're right. And one minus that and minus 1. Okay. Did you forget anything else or did I forget it and you said it. What's missing? M. Yeah. Oh, okay. Okay, and now we created this 0. Right. So let's not waste time and asking you to collect the terms. That's too easy for you. So we can put this out at the brackets, right? And in the brackets we have and times one minus 8 minus M times the time, right? Yeah. And that is equal to 0. So in here, we have like an - and plus M times Theta. Okay. And here and then we get the roots of this equation, which are theta equals 0. Theta equals 1. And also theta equals n divided by n possum. Okay. So the first question, it's, it's an easy equation. The first is equation is what, what's wrong with 0 and 1? What's wrong with zero and one? Why is it not the maximum? This is like, all the solutions. Why can't obvious Solutions be correct? It could be correct, but if you have only tails and only have oh yeah, okay, sure. But in this case, let's say we have both how we are finding That's the solutions. I said the check secondary condition. If you do it, you'll find out. Then it is actually a minimums and yeah, that's true. That's true. Let's not check the second order conditions, that's too much work. Let's just cheat our way through it. And notice that theta equals 0 and theta, equals to 1 give you zero likelihood, right? And if they give you zero likelihood, then obviously it's not the maximum because in between you get positive like So that's obviously minimum maximum doesn't count. And this leaves us this guy, right? So we got our first result about the coin, right? We have the maximum likelihood hypothesis which is and divided by n plus I'm Okay, so far so good and this is probably what, I don't know. Your first class on probability Theory would tell if you have a coin, you want to learn as parameter you toast the coin, you divide, the number of heads by number of experiments. Of coin tosses and you get your estimate for the probability. Completely correct. This is the maximum likelihood hypothesis. and again, if you recall, your probability classes, you will know that like In many cases, or at least, I mean, I think in modern textbooks, they do it already differently. But in all textbooks, like failure on probabilities some classical textbooks, you would get probability kind of introduced in this way. You would get probability introduced as well. There is a system that gives you a random result and then you run it infinitely many times and you get some outcomes, you count, how many outcomes you have you divide by the total number of outcomes and asked the total number gets to Infinity this fraction gets to the probability. And that's kind of the definition of probability from from some standpoint. And of course for a coin at all works. Perfectly there is no catch here. Indeed, if you keep talking the coin and you keep getting results, this fraction will not oscillate between 0 and 1. It will converge to the probability of heads. Everything is completely true. Ah, but here is a question. Here is a more interesting question for you. So let's say this is a coin, it has two sides. I can toss it and let's say okay I was showing to you something but let's forget about it let's say this is the first time I post this coin ever, I just took it out of my purse that's that's the first time I ever encountered this time and let's say I toss it. Let's do it. Okay, I got tails. so, at this point, What is my data set? My data set. Is just Tales. What is my? Likelihood function. My likelihood function is one minus Theta. Right. What is the maximum. Likelihood hypothesis for this? Where is this function? Maximized. Well, there is a first of all there is an interesting formal problem here and that. Oh now I just have a linear function. It gets it goes to Infinity. There is I mean there is no maximum no, minimum basically, if I just look at it formally and forget that it's a coin Theta. Ml should be like negative Infinity. Right. In a way, it's true. In a way, it's true. This formula in the electrical function. Indeed, does not care. That 80s is a coin data is a probability, right? So there is nothing in this function that says oh data should be from 0 to 1, right? So we have to kind of introduce it, impose it as a constraint. So far kind of arbitrary. But okay, let's do that. Let's do that. Let's say we know that our fate is a probability so it should be between 0 and 1. Then what is the maximum likelihood hypothesis between 0 and 1? Tell me. If we make it zero, right? Yeah. So now, the maximum likelihood hypothesis is exactly 0. The math checks out? It's correct. I mean, it's a very hard to make a mistake here, but what does it actually mean? Like, what's my conclusion? What did I learn? I took a coin, let's say it's a real coin. I took out of pocket. And I toasted once I got tails. And now my conclusion is that I will keep getting Tails. Always that doesn't make any sense. Right. I mean, even if I didn't know about coins like I kind of have this intuition that coins are approximately fair, right? So say, it should be something like one half. Probably not, exactly. There is nothing. Exactly in this world but something nearby. Right. But even if I did not have this situation, if I didn't know anything about coins still I mean come on. I have two options and I made one experiment. Obviously, we'll get one of the options, right, there is no other way. So like after one experiment, my maximum leg would hypothesis will always be either zero or one. Depending on what I got. Which means that I should always conclude that, I will keep getting just one result. It doesn't sound. Correct. It doesn't sound like a conclusion that we should actually make. Right. So, what's missing what's wrong? What do you think is wrong here? The math is correct. It's in the maximum like hypothesis but it's not needed. More experiments. Turning it good? Yes. Of course if I want to like make fate a more make more precise estimate of the I will need more experiments. That is correct. And again your statistic classes will probably tell you how many experiments you need, right? But here's the thing. Here is the important thing. There is. As I said before, I started talking about, this example, there is no difference in the limit. So, in the limit, the maximum likelihood hypothesis will get to the true value of theta as n and M, go to infinity and everything will check out and all the time, telling you right now will not matter. so, if we have this, Possibly infinite series of experiments if we can just toss the coin again and again there is no problem and we don't need to have this discussion. That's fine. but thing is in practice, we do not live in the limit, In practice, when we are talking about machine learning, we start with some data set, right? We have as much data as we have. And usually, in machine learning, there is no easy way to to get more date. If there was then, a lot of problems would be much easier, right? So, in machine learning, we are weak, we have our d, And we cannot really change it, right? And I mean okay in practice maybe we can do some project to get additional data. Yes. But when we are actually doing machine learning when we do the data processing part, we have to assume that this is the data set that we're giving. and, Even more importantly here. In practice in real life. We will never get quite enough data. This is an important point. I want to make it here like Suppose that I have. So if I just have a coin in this example, And I have this ability to collect more data. Then sure I can toast it once twice, 10 times, 20 times, 50 times. And after I have toasted 50 times, secondly, after I have toasted 50 times, I can be pretty sure in my results about the coin. Like the confidence interval will be quite small, etc, etc. Statistics will tell you But that's not what happens with real world problems, you know? so, For example, suppose that you are building. A language model. That sounds like a very difficult example but in fact it's one of the simplest near nearest store intuition suppose that we are building a language model so it's a model that has some kind of text. Then there is this black box and then it produces the next token. The next word in this text right? a suppose that I am open Ai and the Transformer has been introduced quite recently. And here I am, I just made my very first GPT model which is like half of a Transformers. Right. So I trained it on some Text data set. I get some pretty good language model. Then. What do I do next? I say well, all right, so let's see how this scales up. Maybe I can get more data. And indeed compared to the first GPT how it was trained. It's easy to get more data, let's just scrape it off the internet. Let's get some more tips. Okay? So, I extend my data set and now I have like, lots of additional data sets and they have lots of text. I have a huge other dates, When I have this huge data set, that's like quarters of magnitude larger than the one used here. It may be indeed means. That now I don't care about this by Asian stuff, I don't care about this effect. I can go back and I can train my GPT on this huge data set and it will be like almost in The Limited will be fine. But that's not what happens, right? It's not like, I collect more data. To go back to my GPT model and train. It even better a little bit. Know when I collect orders of magnitude more data, I go to a larger model. Right. I go to GPT, too. That has more parameters. So GPD had that many parameters actually forget how many and gpt2 had like an order of magnitude more. It had something like 150 million parameters in GT1, I don't remember. So, in actual practice, when you are solving a difficult task, like predicting the next talk or identifying cats and dogs and images or whatever. You never have enough data? It's impossible. Because whenever you have enough data for your model, In practice, it means that your model is too weak. It means that you should switch to a bigger model. For which you now don't have enough data. But it's still will work better. Okay, so I know I haven't proven that formerly to you. And maybe if we have time, maybe we'll discuss scaling clothes and stuff like that, but The point is in machine learning. Unless you have some very specific, very simple, very well-defined problem, like let's learn a coin toss or let's learn. Linear regression Right. So you have like points. And you want to Define to express to represent them with a linear dependence, right? That's linear regression. You can maybe get more data for this linear law. You can get additional points. But unless you have like some very good reason to know that this is going to be definitely linear unless I don't know physics and its supposed to be linear and you're just getting more data for it. So unless you're in some very special situation, if you have significantly more dated, it will be better to go to a large or model. I don't know from linear to polynomial for example. And to it will be a better fit, it will not overfit since you have more data Etc. It will discuss it when we get to linear regression. so, Usually in machine learning we operate like on the frontier of what's possible, so the date is usually fixed. We can change the model. We can we can see the model. It's it's an hour hand and usually You want to choose a model in such a way that, like, it's barely enough data to train it. So we are always in practice in a situation where data is scarce, where it's not in enough. So your answer is correct, indeed. One toss is not enough to learn probability of a coin to us. but, Let's say that's all we have. What can we say about the coin still? And definitely it shouldn't be this right? So maybe we can give up and say okay we can say nothing but we definitely shouldn't be concluding that not from now on the coin will always win Tails. That's definitely wrong. So, what's missing? What else is missing? Like, what is? What is the component that will? Get us from this 0. What is the component that will allow us to say that? Or okay, so the maximum electronic hypothesis is this but actually, maybe I Like one data point is not enough to really shift my, my beliefs, about the coin. Well. The missing is the missing part here. Is my beliefs. and if you go back, To the best from here. It will see that we have only talked about the likelihood. Right. And what we actually want. Is the posterior distribution. Over here. And to get from the likelihood to the posterior. So like the posterior, in this case, what does it mean? What is it tangible? Meaning it's, what do I think? What is my belief about the probability of heads? After. I got my data point after I've tested once and got Tales. Okay. And the likelihood is How likely it was to get Tails given Theta. And to get to the posterior, the missing piece is the prior, right? It's what did I believe about the coin? What did I think about Theta before I started even tossing it before any data came in? That's a missing piece. And in this case is pretty important. So um, let's think we will be able to complete this example. So, let's go to the second part of this example. To the prior distribution. Prior distribution. Pierre Theta. For the coin toss. What does it mean? What kind of object is it? Well, here is the thing. He of fate. It's a distribution on the parameters. In this case on one parameter. Right. So that's why, unfortunately. In machine learning, you can never, you cannot limit yourself to discrete probability Theory. So even when we are tossing a coin, it looks like the most discreet probabilistic object to mentionable only two outcomes, only one probability Etc. So as soon as we do learning, we get a continuous distribution. So P of theta is a continuous distribution. It's a distribution on the probabilities. Right. so, let's, Try to plot something. Like, this is Fatima. This will be of. and, The first property that we definitely need to have, is that fate is a probability, right? So the first very firm belief about Theta is that it should be between 0 and 1. Right. So what ever I think about the coin, whatever, I think about its heads or tails probability, I can definitely be sure that Theta cannot be negative. So pay is 0 over here. And Theta cannot be larger than one. So P of theta is zero over here. This is p of 8. So, by the way, this Is the answer to why? Theta, ml is not negative Infinity over here. And the answer is Theta. Ml is negative infinity and that's fine. Because then we will take this. So in if I have only. So if D is just one tail, then my P of D given Theta is one minus Theta, right? And it's like this straight line over here. Right. So this this is sorry. I'm not good at drawing. I'll do what I can then I'll show you some nice plots. So, this is p of D given Theta. And yes, it does. Go to Infinity, definitely on the left and on the right. And since we want to maximize goes to Infinity of the plus infinity over here. but, We will multiply this straight line. By something which is 0 on the left of zero and on the right one. So after we multiply, all right, let's start with the obvious. Let's start with the uniform distribution. So, the uniform distribution is just one on on the intro from 0 to 1. Oh, sorry, the intro is wrong. One is here, right? So if we start with the uniform distribution, Then after I, multiply this P of theta by this straight line and this is the best from here, right? So P of Fate to give and D is proportional to P of theta times, P of D given fate. You remember, So what I'm doing is I'm taking P of D. Given Theta, the green straight line I am taking P of theta which is this piecewise constant thing. You need the uniform distribution, the right one and I'm multiplying them. What do I get? I get zero over here. And then, I jumped to one. Then I go along this straight line. And then I get zero again, right? That's these two lines are easy to multiply. This is not yet. Pure Faith, given d. Why not? Can you tell me why not? Why is the light blue line? It's not still not pay of it. Yeah, the denominator is still missing and here is an illustration to what I was telling you before. We don't want to get the denominator as some fact about the coin that we want to prove, right? It's just a normalizing constant so I know that this area is supposed to be one. right now, it's not one right now, right now, it's what What is this area? Oh, Yeah, sure it's half of a square, very one, right? So it's one half And so it means that to get the actual distribution, I need to multiply it by two, that's it. So the actual distribution is zero here, zero here and like twice larger over here. So yeah, it will spend two pages. I hope that's Okay, so this guy is p of theta given d. Right. And notice that we didn't actually change much in terms of maximization. Oh, so yeah, this is pure. Okay. So we'll get, we'll get there in a sec. Forgot to say one thing. So this is p of theta given D. Four, the uniform prior distribution over here. Okay. The first remark is. Well. The uniform prayer is not quite. Sorry, what's the word? The uniform prior is not quite what they really think about coins. All right, so let me draw a separate picture. The uniform prior means that well I don't know anything about the probability of the of heads. So it could be zero could be one could be one half could be 1/3, it's all equal to me. But in reality when I take a coin like a real coin or even this pseudo coin that that is the coaster from my cup of course. I kind of expect that it's like approximately Fair. Right. So in real life obviously it's not exactly one half because it's a physical object, has some Perfections. But in real life, I kind of expect that the probability is closed to have So my actual prior program prior distribution, looks okay, it's still exactly zero on the left and on the right. That's for sure. That's by definition. That's mathematical fact. Not my opinion but in between it's probably something like this. Right. so, it's probably some bell-shaped curve that says, well, It's, I think it's approximately Fair, maybe not exactly but it's near 1/2. That's about where my intuition stops really. So I cannot Define this curve. Mathematically write our brains don't work in this way. I just, I can just say that, okay, it's approximately fair, I'm pretty sure of that. But so this should be pretty like high and peaky distribution. But what exactly is the shape of this distribution? I don't know, right? This this cannot be a part of my personal intuition. But anyway, we'll get, we'll get back here. But let's first finish with the uniform thing. So still let's begin with this, not quite realistic uniform, prior not quite realistic for coins. But for other another situations, it's a perfectly good prior because it basically just means I don't know anything. So it made a situations, it's very reasonable. If it's a new machine, learning problem, it has a parameter. I don't know anything about this parameter. But I know it's let's say, I know it's a probability. So it's from 0 to 1. Only from distribution is a great first step. Okay, so in many situations having a uniform, pair of faith is perfectly reasonable. so, I take this uniform P of theta, I multiply it by my Likelihood 1 minus Theta and they get this pointed triangle and this point a triangle. So let me write it down like P of Fate a given D. In my case P of 8 to give even a single tail. It's like Two times. One minus 8, if Theta is from 0 to 1 and 0, otherwise Right. So formally we get this. and, The next question. Let's, let's go back to the best. Roll the head. Our first question is, let's maximize the likelihood. Our second question and usually a better one is, let's maximize the posterior. With respect to Faith. So now that we have a posterior distribution, we can ask, what is the it's called the maximum upper stereo hypothesis. What's the Theta? That maximizes P of theta given d. And in this case there is no difference, really, right? So if I have a uniform prior, the only thing that I actually did like former leevote actually did was, I took care of this the general Solutions, right? So now my my prior does say that the should be between 0 and 1. That that's that's a good thing. But otherwise, I didn't change the shape of the likelihood. I multiplying it by one and then I am renormalized, but that's just a constant. So the maximum will not change. The maximum will be at the same point, right? So Theta, in this case, the map is still and Over N Plus Okay. and, This sounds like a lot of complicated math. Maybe not that complicated but a lot of mess for nothing. Right? So we went from Maximum likelihood to maximum up a stereo and we we didn't change anything. The answer is the same. well, that's because Our prayer was uniform but even for a uniform prayer. Something has changed because I have one point left to make this specific example. Then we'll go to the prayers. I hope they still have time. In this. In this example, for example, in the example of a coin toss and this is a very awesome, very important conception learning. Today is like this very abstract and introductory lecture apologize. I have to begin with something like this. We will we'll get on your own networks, literally tomorrow. But anyway, In this. Example. What is the end goal of this whole thing? Like, let's say that this is an actual machine learning problem. Let's say that. It's I mean it's not but let's say that it's something like distinguishing cats from dogs or something, right? So when I am learning the parameters of A machine learning model. What am I really interested in? What is my final goal? This is a very important point. So far. We have been talking about. Learning something about Theta. So we try to get them ml maximum likelihood. Now we did the prior and now we are getting data MP maximum Australia. But that's about Theta. So if you if I mapped this discussion to neural networks, it would say. All right so I have an old networks, hey taste, the vector of its weights of the parameters, right? And then I do my learning and here is so fat amount. They may be are like checkpoints of the weights. They are this state of the neural network. But when I phrase it like this, it becomes clear that that's not the final goal of the process, right? If I am training, a neural network to distinguish case from dogs, I don't care what the weights are. Right? I mean I do want to get them but I want to get them as a, an intermediate step for the goal. And the goal is this English gets from those. Right. So What we are actually supposed to do, and this is the third part here. And this is true. Both in machine learning can generally in life, actually, what we are actually supposed to do is to make predictions, Right. so, Like philosophically speaking. What does it mean to understand something? Well, it means that you can predict What's going to happen with it? And you can be right. More often than chance. It's I mean, if you haven't thought about this, it's a pretty deep ideas. So understanding something doesn't mean, rephrasing it in different words, it means phrasing in such a way that you can operate analyze it and get to predicting some stuff that you didn't know. in such a way that it actually, Conforms to rare it, right? And here also in this very simple case even here. I mean in the case of a coin everything is very simple, very small and very close to each other. So there may seem there is no difference. So okay, so what's the difference between Predicting heads or tails and learning the probability of heads or tails. It's the same thing. If I get Theta, more than one half, I will predict heads if I get paid less than what I have a projectiles. Isn't that true? Still. There is a difference, very interesting but there is and the predictive distribution, and this case, what is it? It's like the probability of heads. Given the date. It's not in the best for me. It's the next step. Let me I don't have space here. I think. Yeah, let let me write it. Formally separately. So I have the bias roll B of Faith. A given D is p of D, given Theta times P of theta divided by P of D, but the predictive distribution. Is the distribution of the next outcome. Of the next X or the next y, given X in our learning problem. Like what's, okay? So I have this data. What's the probability that this picture is a kid for example. X given d. And P of x given D does not contain Theta at all. I don't care about Theta here. I care about the next prediction solving the problem. but, It's so happens that I can't get to this distribution other than introduce it, right? So the only way to actually compute this is to say, ah, okay, so I don't know about P of x given D, but maybe I know something about P of X and Theta giving d Here is this? Joint joint probability. And here is this marginalization process, right? We are integrating the Gen probability to get pure effects. And now for this joint probability, yes, we can actually reduce it to what we know. So it's p of x given Theta and D times P of theta given d e Theta. And now P of Faith, a given D is our posterior. Right and pox giving well, we have to recall our assumption, we had this assumption which always holds that data points are in the independent. If you have, if you know the parameters, if you know, the full model so here all. So, if I already know the full model, then did not matter. Right? If I already know what is the probability of heads, then it doesn't matter what further the results of the coin in the past, if I know the probability, it will stay the same. So here, the first part is just P of x given fate. It's the likelihood of the single point. Um, and that's it. So this is the predictive distribution. And in this case, even for this uniform prior, it will be different from just predicting zero. That that's the interesting part. So P of has given D. In our case is p of heads, given Theta times P of theta given d d Theta, right? And it's like, What is p of heads given d? Well just fate, right? It's the probability of heads given that the probability of headset that's like a foot of one. Was it difficult? And people that give and give, we actually, I think we didn't write it completely but we did write the likelihood, right? So this this is it. and, P of Fate a given d. Of Fate to give and D. Is proportional to P of D given Theta times P of theta. So it's proportional to like Theta to the end. One minus Theta to the M on 01. And 0 everywhere else, right? So we take the likelihood we multiply it by the uniform prior which basically just zeros everything outside here and does nothing inside here. And we get the posterior distribution. So it's Theta times Theta to the M1 minus Theta to the m divided. Let's let's keep it like this P of D. If And what is p of d. P of D is just the normalizing constant for this. It's the integral from 0 to 1. Oh and the integral is from 0 to 1 because elsewhere it's 0. So P of D is the integral from 0 to 1 of theta to the and times. One minus Theta to the MD Theta. And here we get integral from 0 to 1 Theta 2 to the End. Plus one. There is this extra Theta here. Times 1 minus Theta to the MD Theta. And I want to the math, it doesn't matter for us. We will never come back to it, but if you had a Calculus class, you probably recognize this is the beta function and you can express it as factorials and then all of the factorials will cancel out, blah, blah. I don't want to teach you about beta functions if you don't already know and if you do it kind of fish. Ah, but the result here will be n plus 1. Divided by n, plus M, plus 2. So there is this extra stuff here. this is called this formula is called the LaPlace or rule of succession. Lapia persimmon LaPlace was one of the original founders of probability theory that was one of the original results of the whole field. But whatever doesn't matter. The point is what the predictive distribution does, in fact, so if you look at this from a different perspective, it's the expectation over the posterior of this, like, Right. Just by definition. What is the expectation? It's integral the function times the density defect. So this is like the likelihood average over the posterior distribution. and, What does it mean in our case? Well, in our case, it means that we average over this purple distribution here. And yes, its maximum is at zero. This is the Theta map. But its maximum is on this one side of it. And then fact, there is this whole triangle, right? so, when you average over this Distribution. You don't just get what you would get. If you plugged in zero, you get something in between like it's not the average is not one half and they ever hear is like one third, but it's not 0 either, right? So you average your Likelihood over the whole. Posterior distribution over all possibilities for the model parameters. And yeah, that's that's a lot to digest. But I hope that this coin. Tossing example, is easy enough, that we actually understand what's going on. There any questions at this point? I think I Diamond. I've kind of I think that has been a lot of new information, so, Okay. Okay. Yeah, I love the the Emojis. All right, so At this point even on this. Very simple, example, of the coin. Does I have just one? I think last comment left and then I will show you a couple of thoughts and then we'll, and for today. So, This. Kind of thing. Is. What machine learning is actually about. So, when you define a model, like, when you sorry, where was here, when you define a model like I want to distinguish guests from dogs. What you actually are doing is You define a lost function. And the lost function is actually. Almost always. Either. The log likelihood that you want to maximize? well, the negative because for the losses you want to minimize but it's the same thing or Even more often, it's the negative log posterior. which is so if I write it in logarithms I will see that like the log posterior is just the look likelihood Plus The log prior plus a constant, right? That's what proportional means. so again, in terms of the optimization that doesn't matter, but if It does matter in the sense that we are reading the look, prior to, and the log, prior is the regularizer. We didn't discuss it. We don't discuss it tomorrow where the regularization comes in, but regularization means putting a prior on the model parameters, so introducing your own beliefs. Of what the prior action was. Okay. And yeah, and I think I, I have to, I have to discuss one last Point here. So, This was all the specific formulas that I wrote were only about the uniform prayer. And as I said it's not the prior that I actually have in mind when I'm talking about the coin, right? So for a real coin, it's some bell-shaped curve. I'm pretty sure it's close to one half. so, Of course, I want to plug in a more realistic prayer here. If I want to learn the quintus, But the plug it in, I need to Define it, right? So the question let's say it's what is a, the more realistic prior? For the coin. And what is the most nature prayer for a queen? What is? How do I? Define p of theta. Okay. And here, the answer may surprise you. If you never thought about it before, the answer is surprise you because it sounds kind of lazy but it's true. So, The prior is a distribution. On Theta. We know that it should be 0 here. 0 here. Now question about that. But what is the shape inside? My intuition says that it should be something like this. But there are millions and billions and you know, space with continual dimension of how many different functions look like this, right? So how do I choose a specific function? What what will be the family of probability distributions that I plug in for p of faith? Do you know any distributions that look like this? Can you suggest? Normal distribution, normal. Sounds good on the surface. So with normal, you will have a problem right from the outside because the normal distribution will not go to 0, right? So the normal distribution is never exactly. It will be like something depending on the variance and then it will go down and then it will have some tails on the ball sets, right? So there will be tails. But okay, let's cut off the tails. We can do that. We can truncate normal distribution on the left and on the right. Then we renormalize a little bit, it becomes a bit higher, but it's still like normal. Just the normal bell curve over here. What happens next? So I need to write down the normal distribution. What is my P of theta? Well, it's zero outside of 01 and here. It's some constant which I cannot compute. Of course, times times what times, e to the power minus 1 over 2 Sigma squared, Theta, minus 1/2 squared. On the 01. Right. That's the density of the normal distribution. Okay, so far. Not so scary but what happens next. Next, I need to multiply P of theta times P of D given Theta. And that's gonna be okay. Inside zero one is going to be like c times this exponent. Times Theta to the N times. 1 minus Theta to them. That's my posterior distribution, the shape of the posterior. And then I need to put maximize it. So I need to take derivative It sounds like it doesn't fit, right? So we probably can do it numerically. Of course. It's I mean it's it's a coin. It's dimensional one. Of course we can do it numerically but it sounds like some pretty inconvenient distribution for acquaintance. And what is it? What exactly isn't convenient? What is inconvenient is that the shape of the prior Does not match the shape of the likelihood. The prior is an exponent and the likelihood is a polynomial and we multiply one by the other, we don't get anything meaningful, we get exponent times, putting them. So here here is the secret here. I just want about shift curve into my intuition doesn't tell me if it's normal or students t, or or whatever. So, how we actually choose? Is we choose by convenience? We choose the shape of the prior. That matches the shape of the likelihood, so that these multiplication becomes easy. And that the former it would be called the conjugate prior. Let's not get there. I will just give you an example and we'll be done with it. So what would be easy to multiply? So the likelihood we cannot change. The likelihood is given by the process by the thing that we are describing. So, in this case, it's a coin. Has two sides. One parameter. So this formula is fixed. We cannot change the like But we can change the prior and what would be easy to multiply by polynomial like this. This is the electrical. How should the prior look like? So that it's easier to multiply by this. Okay, probably, you're probably wondering exactly how easy I didn't Define that. But okay. So the prior, the easiest way, this is function to multiply by basing like this would be another thing like this. Isn't that true? So let's say the prior is something like Theta to the power of alpha. Formerly Alpha minus 1 that's just for formal reason. Don't pay attention times 1, minus Theta to the power beta minus 1. Times a constant. And the constant is a beta function. Blah blah. Let's not get there but As a result, I will get Theta to the power. Alpha plus n minus 1. And I will get 1 minus 8 to the power beta plus M minus one. so, the multiplication becomes trivial, but what is actually important is, not that it's easy, but that the posterior again looks exactly like the prayer so the prior is, what is called the beta distribution with parameters of and beta, And after I multiply by likelihood with and heads on them tails. I get the posterior which is again a beta distribution. but with parameters Alpha plus n and beta Plus Okay. So when that happens we call it the conjugate prior you don't have to memorize that. But the point is now this calculation by the bias for row becomes trivial. I don't need to even think about the formulas. I just did it once. It's just adding up the exponents, that's it, right? and, Now. I can easily go from prior to posterior for any and them, I don't need to do any new method. I don't need to run any numerical algorithms. I just plug it into this. Very simple formula where it's just initial And the only thing that I need to check is that indeed, this kind of Prior can express what I want, right? So that I can get a bell shaped curve out of it and here I can get a bullshit profile to it. So if I have a fated to the power 10 and 1, minus Theta to the power 10, if the exponents are the same, then I will get a big at one half. So this point let me just show it to you. um, in practice. Yeah, let me just show you the bettas. So, Here is the family of the beta distributions. The The the uniform distribution is also a bit with parameters 1 and 1. So like one it's fated to the power 1 minus 1 and 1 minus 8 to the power 1 minus 1. So it's just uniform. And then as the bait, the elephant bathing increase I get like this more and more pointy. Distributions, the variance decreases. And if Alpha and beta are equal, then I get the maximum at one half in general. Like I get the maximum at Alpha divided by Alpha plus beta just like the coin just like the max like So the beta frame it does include what I want. It also includes a lot of other nice distributions that I can probably get as posterior. and, What does the actual bias and inference look like, well, it looks something like this. So let's let's have, let's first begin with our our example, like we did. In the lecture. So here is the prior it's uniform. The likelihood for one tails is the orange line. And then I multiply it by the posterior, which by the prior. Sorry. And then I normalize and I get the posterior, which is the green line. Okay, so this is what the Drew on the board. What if my prior was different? What if my prior had parameters? Like, two and two, so one and one gives you The power zero. One minus, the power is 0 2 and 2, give you the power 1 times, 1 minus, the power one. So it's a parable like this, right? This, this is the prior. and when I multiply this prior by the same likelihood, I still toasted once I got one tails, Well, now it's a cubic curve and the shifted to the left a little bit and its maximum is at one third. Makes sense, right? And then I can. I can continue like this. I can become more and more sure. A pre-order that the coin was fair. And I will get like this more and more peaky priors around one half. and, The more convinced I am in advance that the coin was fair. The last, this one experience will matter. One experiment, will matter. So if I was already very sure that the coin is kind of fair. Like 50/50 the parameters, 50, 50. Then. This one result of Tails will not change anything. The posterior looks just like the prayer. but of course, if I keep talking it and I keep getting tails It matters more. So 10 Trails will shift my posterior to the left. This is the likelihood for 10 tails in a row and if I get, I don't know, 100 Tails. Then I will probably shift it quite a lot, right? But still The prior matters a lot to how much evidence I need to actually move my beliefs. Okay. Yeah, and since we are here, let me know show you this. So, How it actually, how it might actually work. Is. What is another like? Nice property of the conjugate priors. What is another? Nice property of a situation where you're posterior? Looks just like the prior and other nice properties that. Now, you can reuse. This posterior is the prior for the next experiment. So now I can do like sequential update I can say well all right. So here is my Here is my original uniform distribution, then I tossed the coil once. And I got heads. So the orange straight line is the posterior after one pointers. Then I tested another one time and I got a tail. So now this Parabola is my posterior after 2.06. And when I toss it three more times, I don't have to go to the beginning. I can say, all right, so now I have this Parabola after 2.06 Let me just multiply that, by the likelihood of the next three. Like, one heads and two tails, I think in this case, And this is there is a result. And so so I can like forget about the previous data set. Just take the posterior and plug it in as the prior for the next update. So I, it can work. It can work like this, I start with P of Fatima. Then. From a dataset. I get paid a d. and then, I get another dataset more data. And I want to go to P of Faith, a given D and D Prime, right? I want to unite all of the data and use all of the data. And basically, if I have a conjugate prior like this, I can just say, all right, so I did the math here. I can forget about this part. Now, this is my new prior. This is my new data set and I get to the posterior and of course formerly nothing changes. So it's the same by a stroll, only its deal on the right. And every and every probability doesn't doesn't matter. But if I didn't have a conjugate, president would just be very difficult to do. So, it would be easier to just start from here and do the whole computation with the and the prime. But if I do have a conjugate prior, then I can use it. And maybe one final. Yeah. Maybe one final thing to show here is here is a coin toss that I did a sequence of coin tosses in the sequence of probability of heads that I have learned. And the probability of heads change as I go. And the blue line is the maximum likelihood hypothesis and the orange line is the LaPlace is roll. So it's this small out and plus one over n plus n, plus 2, the predictive distribution, the predictive probability. And as you can see it's just as we expect, right? So in the beginning, they LaPlace is row is less extreme than the maximum likelihood. So after one toss, this is either one or zero and this is either one through two thirds, so much closer to one half. And that will like moderate this extreme of the max likelihood, but then, after like 50 tosses, they're in distinguishable. so one converges to the other and they both converge to the true probability, and we can, we can do other Random experiments here. It's of course. So okay, so let's let's summarize I think I'm already over time here. What we did today? this is Thomas bias, the Reverend Thomas Bass from 1760 something. So but actually yeah there there is a famous story that this portrait is actually fake. It's not Thomas bass and nobody knows who that is, okay? You can read them. anyway, so we discussed the best theorem in and how it is used in machine learning. We discussed. the most important, not just the most important because basically, the only problems that we Are solving in machine learning. Like, what does it mean to learn something? Well, it means to say something about the parameters of the model. and you can just maximize the likelihood, but as we have seen today, it's probably probably usually makes more sense to Get the full posterior distribution, if you can. and then maybe maximize it if you have to And yes. This is what we discussed. I will get to a couple more examples tomorrow. A conjugate prior. So we discussed This is the beta family here. I think this is it. This is the laplace's role. You can read it up on the slides. If you want you want to What, where is the predictive here? Yeah, for example here and the last problem, the most difficult problem is to get the predictive distribution is to get The next, the distribution of the next element of the data set predict the next coin pose, given what the data Setters is still in a regardless of the specific way of fate. Which means you have to average overstate. And we did it. with the example of the coin, we hopefully. When through the whole example, I skipped a couple of Minor Details that don't affect and they machine learning understanding. But overall, we've completed the cuantos example, naturally. You can also extend it to Die rolling to several different outcomes. It will be exactly the same. Maybe we'll talk about it tomorrow, but at this point, I think, I will stop here. Are there any questions? Yeah, I have a question. Can you remind please? Yeah, maximum likelihood and plus rule is activation of Prior multiplied by likelihood and Okay, so LaPlace role is the predictive distribution. So let's let me repeat it again because this is really important. So you have the Best role, right? The bias role connects the likelihood, the prior, and the posterior. The model itself is usually the likelihood. And you can maximize the likelihood directly and you get the maximum likelihood hypothesis. if you add the prior, You get the posterior. And you can maximize the posterior and you get the maximum aposteriori hypothesis. But what you really want, it's just that often it's impractical to get often, you can't get it. But what you really want is the predictive distribution, the next x given d, And that is and there is no way to compute it, usually except like this. Right. So like the expectation over the posterior. Of this next. Item. Like, Okay, and the LaPlace is role was about this. So the LaPlace roll. Said that P of heads. Give an end and then given d. Is and plus one divided by n plus, n plus 2. If you have a uniform prior, While let's say, Theta ml was given us and over n. + m, and Theta, Mae people's also give us and divided by n plus him. It's all for the uniform. Okay. Okay, thank you. Our questions. Sorry, yeah another question. Sure. Okay, first of all about the same topic so For example, in economics and financial econometrics where you use time series, it is very common. Well, every time you build a model to predict the next How they say? Yeah. Inputs from the previous period. So it is a very common problem. Why is it such a problem here, is the difference between time series and on ordered observations, like here, or is it a different? Of languages by yourself approaches. There is no difference. I mean, it's just a different problem setting but you will still need to convert it to your previous layering. Probably right? So, in reality I mean, yeah, maybe your time serious goes to negative Infinity but in reality doesn't right. So in reality you will have your data set. Sorry, your data set in Time, series analysis will still look like players of access and wise And how do you define the excess? Well, that depends on your model of course. So maybe you do a sliding window, right? So maybe you say, okay, I look at the previous so many tips and I predict the next tick based on this fixed context. Then your access this. Or you can say, well, let me do, I don't know, recurrent neural network. If I have a current neural network, then it means that what my recurrent cell is doing is it's getting my current X and the hidden State age and we are predicting. Let's say, okay actually, we are outputting the next hidden state, but we are also, let's say, predicting this, why over here, right? So we will talk about recurrent networks when we get there. But here all. So you compress your contacts down to this state Vector page, and this is your input and you want to and, and then you get your Own and so on. So, I don't feel. There is any difference specifically. So yeah, time series sometimes are a little bit special but I think not an econometrics. I think they're special. When they're, when they're like really really long, I can sound analysis. When you have like, millions and millions of ticks and you don't want to treat them as a single. Not just at times serious, maybe you want to do, you know, Fourier transforms look at the Spectra Etc and it becomes a different sense. But I think in econometrics, it's just your professor. The question about. Notebooks that you. This one. Yes. So For example, and equals 5, sorry, no problem. Yeah, and it cost to five. so, we can use the How do I say our our prior component is the result that we go to previous step. Yeah. So is there a difference in results? Now, go in step by step or that's just using five observations from our initial. Yeah, that's the same. Exactly the same as the whole point here. So of course, for a coin, I mean, it doesn't matter. You are not saving anything. Going straight from the beginning is just as easy. But if you had like a big data set and you could compress it down to to the posterior distribution, maybe now you can forget about the data set, that's maybe a good thing. You need to to go over it again. I mean for a coin yeah you're not saving anything because for a coin the data set reduces to two numbers. So it's it's not like you can be more efficient here. And can you upload these sure sure there's no yeah, absolutely. So what I will do, what I always do is I will make web page for the class for you and it will have the videos, it will have the boards. It will have a notebooks And it will be unfortunately a secret webpage for the herbal space University, so I'm not allowed to post it in public, but I will send you the link in Google classroom or whatever. Also, if it's convenient for you, we can make a telegram chat for the class. I think we don't have one but it would be really convenient for me. But if if that's not good for you, then Google Classroom is fine too. Okay, so thank you. And See you tomorrow judging by your questions. I think you did learn something new today. Thank you tomorrow. Thank you.
