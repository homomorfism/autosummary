# Transcript — whisper_cpp

- **Provider:** whisper_cpp
- **Language:** en
- **Audio duration:** 3:29:30
- **Segments:** 2129
- **model:** ggml-large-v3-turbo.bin
- **vad:** True
- **beam_size:** 5
- **entropy_thold:** 2.8
- **latency_sec:** 1235.13

## Segments

**[00:12 – 00:28]** Hello, everyone. It is very nice to meet you here. Well, virtually, remotely, but still meet you here at Harborspace. My name is Sergei Nikolenka, and I will be talking to you about machine learning.

**[00:28 – 00:51]** And, yeah, the class is named very specifically computer vision in neural networks, but to be honest, usually it so happens that it kind of becomes just a general introductory class to deep learning, which, judging by the two responses I had, we will also do this time,

**[00:51 – 01:07]** because it sounds like many of you have not had real experience with deep learning specifically, so we will start from the very beginning and then work our way up.

**[01:07 – 01:18]** There will be computer vision, of course, I mean, we have to give some examples, and since the class is about computer vision, why not give computer vision examples?

**[01:18 – 01:34]** But we will start from the beginning and we will try to build the cathedral of modern artificial intelligence from the ground up as best as we can.

**[01:34 – 01:40]** But let me begin today with a brief introduction to machine learning in general.

**[01:40 – 01:48]** Okay, so I don't think we will get to neural networks today. I hope we'll get there tomorrow.

**[01:48 – 02:00]** And finally, I got to be the host, so I can now spotlight. That's all I needed. Thank you.

**[02:00 – 02:09]** So let's begin by talking about where artificial intelligence is, how we got there.

**[02:09 – 02:24]** And today I want to maybe, for some of you it will be a reminder, for some of you it will be new material, but I want to discuss the most fundamental stuff of machine learning.

**[02:24 – 02:33]** Like, what is it based on? What is the basic machinery that everything runs on?

**[02:33 – 02:38]** And it turns out that that basic machinery is basically probability theory.

**[02:38 – 02:42]** So for those of you who liked your statistics courses, rejoice.

**[02:42 – 02:50]** And we will see how it all relates to learning, to training, et cetera, et cetera.

**[02:50 – 02:55]** So anyway, let me start with a brief intro.

**[02:55 – 02:58]** Anyway, we live in some very interesting times.

**[02:58 – 03:08]** And usually when I start a new class on machine learning, I have been teaching for almost 20 years.

**[03:08 – 03:11]** Yeah, almost 20 years I have been teaching machine learning.

**[03:11 – 03:18]** And when I start a new class, I usually start with like this historical overview, right?

**[03:18 – 03:21]** And traditionally I would begin with a picture like this one.

**[03:21 – 03:25]** It's just a random timeline of the internet, nothing special about this one.

**[03:25 – 03:37]** But, you know, I would talk about and I will talk a little bit today about how AI as a field has progressed starting from its beginnings in the 1950s.

**[03:37 – 03:47]** In the 1960s, the AI winter of 1970s, then we go to the 80s when neural networks reappear,

**[03:47 – 03:53]** then we go to the 90s and 2000s with probabilistic models,

**[03:53 – 04:00]** and then we go to the revolution of deep learning that defines artificial intelligence today.

**[04:00 – 04:08]** So that's all well and good, and if you look at AI from this standpoint,

**[04:08 – 04:11]** you see a regular field of science.

**[04:11 – 04:19]** And even if you dig deeper into some specific part of AI, for example, generative AI or whatever,

**[04:19 – 04:30]** you see some pretty reasonable timeline if you look at timelines from before the year 2022.

**[04:30 – 04:35]** But recently something has changed, right?

**[04:35 – 04:49]** Recently, AI has started to progress in some completely unexpectedly fast way, right?

**[04:49 – 05:00]** So this is a timeline I made a couple of years ago, three years ago in the summer of 2023.

**[05:00 – 05:04]** And it was about the spring of 2023.

**[05:04 – 05:09]** If you recall, that was the time when ChatGPT just appeared.

**[05:09 – 05:15]** It appeared in the late '22, but it was not really popular for a little bit.

**[05:15 – 05:19]** And then suddenly it blew up.

**[05:19 – 05:26]** And then in the spring of 2023, everything started appearing all at once, right?

**[05:26 – 05:35]** I will not go through the whole timeline here, it doesn't matter now, but look at March 14th, 2023.

**[05:35 – 05:43]** That was like...

**[05:43 – 05:48]** That was...

**[05:48 – 05:58]** Okay, sorry, we have a technical question, which I think I need to address.

**[05:58 – 06:11]** Can you see the presentation? Some people say it's not...

**[06:11 – 06:16]** The presentation is visible, but text on it is not created.

**[06:16 – 06:20]** Let me check.

**[06:20 – 06:32]** I don't want to switch to sharing the presentation because I will then need to go to the blackboard and stuff like that.

**[06:32 – 06:41]** I'm in HD. Let's do what you suggested.

**[06:41 – 06:48]** Let me post the presentation for you.

**[06:48 – 07:06]** It will take a long time to get it to Google Classroom because I'm not logged in there, but I'll send it in chat right here.

**[07:06 – 07:25]** So anyway, the spring of 2023 was like this sudden outburst of everything AI-related and specifically LLM-related.

**[07:25 – 07:54]** Okay, I send the presentation, it says it's uploaded. And if you look at, for example, March 14th here, you see that on the exact same day Google announced that it would be integrating LLMs into its workspace. It wasn't called Gemini at that point, but some LLM Google did announce.

**[07:54 – 08:11]** A small startup that recently split off of OpenAI announced that it would be producing its own family of LLMs plot, which we all know and love now.

**[08:12 – 08:28]** But both pieces of news were completely overshadowed by OpenAI, which came out and said that we are, well, not yet releasing, but we are announcing GPT-4, the next step in this development of LLMs at that point.

**[08:28 – 08:39]** And when I made this picture three years ago, I called it the Spring of Artificial Intelligence.

**[08:40 – 08:56]** And I mean, at that point, three years ago, it was completely possible that this would all still be, you know, in line with some regular development of regular science, right?

**[08:56 – 09:04]** So sometimes you have a breakthrough. When you have a breakthrough in that, in 2023, that was ChetGPT.

**[09:05 – 09:10]** So LLM started to work. And when you have a breakthrough, you know, researchers go there.

**[09:10 – 09:17]** They fill in this new space with their research. And then the field needs a new breakthrough, right?

**[09:17 – 09:32]** So scientific progress usually goes by these big steps. When somebody discovers a new direction, then it's very quick for a while, and then it slows down back again.

**[09:34 – 09:38]** So back then it was still possible that it would go like this, but of course it didn't.

**[09:39 – 09:42]** And the rate of progress has not slowed down since 2023.

**[09:42 – 09:52]** We are still getting news basically every week, and we are getting big news every month in the field of AI.

**[09:53 – 09:58]** It's not slowing down, on the contrary, it looks like it's speeding up, right?

**[09:58 – 10:14]** It looks like currently the Frontier Labs, the OpenAI and Anthropic, they already are using their own models to make their own models better, right?

**[10:14 – 10:23]** So it's not yet the fully closed loop of recursive self-improvement that everybody is talking about, but I think we're getting there, right?

**[10:23 – 10:27]** And if we do get there, then who knows what's going to happen, right?

**[10:29 – 10:39]** And so we live in some very, very interesting times, and I want to stress here, because by now it's actually already not obvious to people,

**[10:39 – 10:47]** but I want to stress here that it was completely unexpected, and very, very few people predicted this.

**[10:47 – 10:53]** So I recently came across this nice example.

**[10:53 – 10:57]** This is a book from 2018, less than 10 years ago, right?

**[10:57 – 11:00]** So the deep learning was already here.

**[11:00 – 11:03]** We already had, I don't know, LSTMs.

**[11:03 – 11:05]** We actually already had Transformers, right?

**[11:05 – 11:07]** In 2018, we already had the Transformers.

**[11:08 – 11:16]** And the author of this book asked several prominent researchers, when do they expect human-level artificial intelligence?

**[11:17 – 11:23]** And the closest was none other than Ray Kurzweil, which you would expect.

**[11:23 – 11:25]** And he predicted it in 2029.

**[11:26 – 11:28]** And that was the nearest prediction.

**[11:28 – 11:39]** So less than 10 years ago, most researchers would place human-level intelligence somewhere around 50 years from now.

**[11:42 – 11:43]** Things have changed, right?

**[11:43 – 11:45]** And this rate of progress keeps accelerating.

**[11:46 – 11:54]** So in this class, I hope, we will actually go all the way to the modern LLMs.

**[11:54 – 11:55]** Naturally, not in full details.

**[11:56 – 11:58]** We cannot do it in full detail in three weeks.

**[11:58 – 12:06]** But we will start from the foundations of artificial intelligence, from the foundations of deep learning specifically, of how neural networks work.

**[12:06 – 12:12]** And then we will discuss the main classes of architectures of neural networks.

**[12:13 – 12:24]** And ultimately, of course, we'll get to transformers, we'll get to language modeling, we'll get to the GPTs and clouds of today.

**[12:25 – 12:29]** But let's start at the very beginning, right?

**[12:29 – 12:36]** So I will still allow myself this guilty pleasure of doing a historical survey.

**[12:37 – 12:40]** Artificial intelligence is a very old idea.

**[12:41 – 12:55]** So artificial intelligence, I mean, in a way, according to almost every religious tradition in the world, we are artificial intelligence, right?

**[12:55 – 13:03]** Because we were made in some traditions out of clay, in some traditions out of some less pleasant substances.

**[13:03 – 13:12]** But in any case, we have been made by God and whatever the name of the God is, right?

**[13:12 – 13:24]** And we have been created with our souls, with our intelligence, and so we are AIs, according to the religions of the world, right?

**[13:24 – 13:33]** More modern kind of artificial intelligence ideas can be found in, actually, Greek mythology,

**[13:33 – 13:43]** where, of course, Wells, but Hephaestus would create android robots for himself, and there were several.

**[13:43 – 13:47]** The most famous was this giant humanoid robot named Talos,

**[13:47 – 13:55]** and that's actually a pretty funny story, and it relates to the field of air as well.

**[13:55 – 14:06]** Hephaestus ultimately gave Talos, or I think it was Zeus who took Talos from Hephaestus

**[14:06 – 14:15]** and gave it to the king of Crete, I think, and on the island of Crete

**[14:15 – 14:21]** the job of Talos was to basically protect the borders, right?

**[14:21 – 14:30]** So Talos would run around the perimeter of the island, and when Talos saw enemy ships approaching

**[14:30 – 14:37]** it would take giant rocks and it would throw the giant rocks to the enemy ships.

**[14:37 – 14:40]** That was his job.

**[14:40 – 14:53]** What is interesting about this, in my opinion, is how things have played out to be in terms of what's difficult and what's easy, right?

**[14:53 – 15:01]** So the ancient Greeks were already starting to be pretty good at throwing big rocks to great distances.

**[15:01 – 15:03]** They already had catapults, right?

**[15:03 – 15:12]** And then they were not very accurate, but then we got, you know, trebuchets and then guns and then rocket launchers, whatever.

**[15:12 – 15:23]** So we are pretty good at hurling destruction to great distances with great accuracy, actually.

**[15:23 – 15:33]** But the more difficult part it turned out to be was to actually recognize enemy ships, right?

**[15:33 – 15:45]** So already, I don't know, 400 years ago, you could have a big gun that would be pretty accurate in sinking the ship.

**[15:45 – 15:52]** But how would you automatically recognize, first, that there is a ship on the horizon,

**[15:52 – 15:57]** and second, that the ship is an enemy ship and not a friendly one, right?

**[15:57 – 16:05]** So that's a computer vision problem, and that proved to be more difficult for humanity to automate

**[16:05 – 16:11]** than the rock-throwing part, which is, I think, pretty interesting.

**[16:11 – 16:17]** Similarly, okay, so there was AI in many different traditions.

**[16:17 – 16:22]** In the Judean tradition, for example, there was this notion of a golem,

**[16:22 – 16:27]** and some wise rabbis could create golems.

**[16:27 – 16:34]** Okay, so that didn't play out as the Judaic tradition predicted.

**[16:34 – 16:39]** In there, there was a big difference between speech recognition

**[16:39 – 16:42]** and speech synthesis as an AI task.

**[16:42 – 16:45]** So a golem can actually understand you.

**[16:45 – 16:46]** It can understand commands.

**[16:46 – 16:50]** It will fulfill the commands of the rabbi who created it.

**[16:50 – 16:54]** It will know human language, but it will never speak.

**[16:54 – 17:00]** In the Judaic tradition, understanding was okay for man-made constructs,

**[17:00 – 17:03]** but to actually speak, you had to have a soul.

**[17:03 – 17:09]** And of course, even a very wise rabbi cannot create a new soul.

**[17:09 – 17:13]** So that didn't play out as expected.

**[17:13 – 17:19]** And that was why Thomas Aquinas was the famous philosopher

**[17:19 – 17:22]** and the pupil of Albertus Magnus, the famous alchemist.

**[17:22 – 17:29]** So Thomas Aquinas was very, very upset when his teacher, Albertus Magnus,

**[17:29 – 17:32]** actually created an artificial speaking head.

**[17:32 – 17:35]** And of course, we don't know what it actually was.

**[17:35 – 17:38]** One hypothesis is that it works something like this.

**[17:38 – 17:44]** So it was just a device for transporting sound from a different room

**[17:44 – 17:49]** and somebody would actually speak through the pipe.

**[17:49 – 17:54]** We don't really know, but what we do know is that Thomas Aquinas got very upset

**[17:54 – 17:57]** and actually smashed the whole thing to pieces.

**[17:57 – 18:02]** Then in the Middle Ages, I won't go into details here,

**[18:02 – 18:07]** but you probably know there were lots of very inventive automata,

**[18:07 – 18:13]** early robots, which are not quite robots in the modern sense,

**[18:13 – 18:18]** but human figures that can do some simple task automatically,

**[18:18 – 18:22]** particularly like poor water or something like that.

**[18:22 – 18:25]** And they were pretty inventive, but they were purely mechanical,

**[18:25 – 18:27]** not very interesting, of course, for us.

**[18:27 – 18:34]** What I do want to mention are these automata by Pierre Jacquetreau.

**[18:34 – 18:37]** He was a Swiss watchmaker,

**[18:37 – 18:43]** and actually the Jacquetreau watches you can still buy,

**[18:43 – 18:47]** although they are very, very expensive, but it's an existing brand.

**[18:47 – 18:58]** And his hobby on the site was making very intricate human-like dolls

**[18:58 – 19:05]** that would do very fine things with their hands,

**[19:05 – 19:09]** and that would actually do something interesting by themselves.

**[19:09 – 19:14]** And there was this draftsman,

**[19:14 – 19:18]** a doll that would actually draw several different pictures,

**[19:18 – 19:23]** but what is really interesting, what I wanted to highlight was this guy,

**[19:23 – 19:27]** the calligrapher, and the calligrapher is very similar to the draftsman

**[19:27 – 19:35]** because he also is using a quill to write on a piece of paper,

**[19:35 – 19:41]** but you could actually program the calligrapher to write what you want.

**[19:41 – 19:46]** There was like this, I don't know, a system of levers or something on the back

**[19:46 – 19:52]** that you could switch some of the levers and you would write different letters.

**[19:52 – 20:03]** To my knowledge, that was the first actually programmable device

**[20:03 – 20:13]** before Jacquard's looms that are usually quoted as the pioneers of programming

**[20:13 – 20:21]** that invented punch cards, etc. But that was before. That's interesting.

**[20:21 – 20:25]** But of course, this is not AI as we understand it now.

**[20:25 – 20:37]** So there was no programming to speak of. There was no math AI that would be AI related.

**[20:37 – 20:42]** Actually, I don't want to talk too much about this guy, Ramon Lowell.

**[20:42 – 20:47]** But I mean, I usually mention him in Harborspace because he is Catalan.

**[20:47 – 21:06]** But basically, he was an early logician and if you stretch definitions a lot, you can actually say that he did something that would later be related to AI, but not really.

**[21:06 – 21:11]** When did AI actually appear as a science?

**[21:11 – 21:21]** There are several starting points and usually, well basically there are two starting points that I will quote.

**[21:21 – 21:31]** One is the 1943 paper on the mathematical models of neural activity that we will get to later when we discuss deep learning.

**[21:31 – 21:40]** And the other is the 1950 paper of Alan Turing, the Turing test, which I hope you have all heard about.

**[21:40 – 21:48]** So Turing was a very smart guy and he was like really a genius.

**[21:48 – 21:54]** He did a lot of total breakthroughs in the field of computer science.

**[21:54 – 22:00]** And in particular, he basically invented artificial intelligence.

**[22:00 – 22:10]** And the first question, of course, that a person thinking about this stuff seriously encounters is:

**[22:10 – 22:15]** Can you do an artificial intelligence? Can machines think?

**[22:15 – 22:22]** And this is the subject of Turing's essay of 1950, which I definitely recommend you read.

**[22:22 – 22:27]** Because, you know, old research papers are usually very hard to read.

**[22:27 – 22:32]** They use strange notation. They are cumbersome. It doesn't make sense.

**[22:32 – 22:38]** A modern textbook would be much better, would explain stuff much better.

**[22:38 – 22:42]** But in this case, Turing was a genius, right?

**[22:42 – 22:49]** So his essays, they are not so much research papers as philosophical discussions about stuff.

**[22:49 – 22:51]** And they are still very interesting.

**[22:51 – 22:56]** So I definitely recommend you read the essays of Turing.

**[22:56 – 23:03]** And specifically, the Turing test was in this essay on Computing Machinery and Intelligence, it was called.

**[23:03 – 23:22]** And the Turing test itself is very interesting in how it survived for so long and why it survived for so long.

**[23:22 – 23:25]** So you've all heard about the Turing test.

**[23:25 – 23:35]** There is a judge, the judge is chatting in writing with an unknown entity or with two unknown entities.

**[23:35 – 23:40]** And then one of the entities is a human, the other entity is a computer.

**[23:40 – 23:47]** And basically the judge needs to recognize which was the human and which was the computer.

**[23:47 – 23:51]** So there are a couple of interesting points here.

**[23:51 – 24:00]** First, note that it doesn't make any sense to run the Turing test once.

**[24:00 – 24:14]** So the Turing test actually kind of grew out of Turing's foundational work on computer science, on algorithms, theory of algorithms and randomized algorithms.

**[24:14 – 24:26]** So the Turing test definitely wouldn't tell you anything if it was just one run of the experiment.

**[24:26 – 24:33]** Because, of course, the judge can always just flip a coin with probability one half.

**[24:33 – 24:34]** It will be right.

**[24:34 – 24:40]** So when does a machine, when does a computer program pass the Turing test?

**[24:40 – 24:44]** Not when it fools the judge once. It wouldn't make any sense.

**[24:44 – 24:57]** But when it consistently makes it impossible for the judge to recognize the program with any probability significantly different from one half.

**[24:57 – 25:04]** So right from the start, it's an interesting remark that we get to the realm of probability theory,

**[25:04 – 25:11]** we get to the realm of randomized algorithms, et cetera. We'll talk more about that later.

**[25:11 – 25:19]** Okay, so now the main part. Then I go for the fun remark, but now the main part.

**[25:19 – 25:29]** The main part about the Turing test is, unlike all other tests of artificial intelligence, and I will give an example,

**[25:29 – 25:37]** unlike all other tests, the Turing test has actually survived for a very long time.

**[25:37 – 25:43]** So I think I have a slide on this. Yeah. So formally, the Turing test was actually passed just a year ago.

**[25:43 – 25:54]** Okay. Of course, once you had stuff like GPT-4, nobody really doubted that GPT-4 could pass the Turing test in the original formulation,

**[25:54 – 26:02]** like in a five or 10-minute chat. But, you know, it was non-trivial to actually run the test,

**[26:02 – 26:11]** because, of course, if you're talking with a frontier model these days and you just ask it, well, are you an AI?

**[26:11 – 26:20]** The model will tell you, oh, yeah, sure, I'm a language model. So somehow you would need the model to stay in character, right?

**[26:20 – 26:25]** And it's easier to do with small ones, but small ones would not fool anyone.

**[26:25 – 26:33]** So there were some problems with actually running the Turing test, but once people did, of course, the models passed.

**[26:33 – 26:42]** But it's very recent news. It's 2025. And the original Turing test was in 1950.

**[26:42 – 26:56]** And that is very cool and very surprising in AI because, to be honest, AI as a field has a very long history of moving the goalposts.

**[26:56 – 27:09]** So, for example, that's the example that I want to give. In the 1970s, there was this guy, Alan Newell. We'll meet him later.

**[27:09 – 27:25]** And he wrote a very nice paper, like, what is the state of AI now and where are we going? Like this position paper that would define how the field of AI should develop.

**[27:25 – 27:37]** And at the end, he wrote, well, okay, we have the Turing test, but of course, the Turing test is not really actionable. In the 1970s, it wasn't.

**[27:37 – 27:46]** Of course, you cannot expect AI models to pass the Turing test. And there can be no progress on the Turing test, right?

**[27:46 – 27:54]** So it's not like you can fool 5% of the judges, then 10% of the judges, then 20% of the judges. It doesn't work like that.

**[27:54 – 28:08]** Either you fool humans or you don't. And so he wrote, okay, we need some kind of other tests that would be numerical.

**[28:08 – 28:21]** In the sense that you could actually measure the result, but also that would actually reflect something inherently important about intelligence.

**[28:21 – 28:30]** So if the machine passes, it means that we actually are making progress towards general artificial intelligence.

**[28:30 – 28:37]** Sounds very reasonable. But what is his example? His example was, let's take chess.

**[28:37 – 28:46]** And he actually argued for Page that, well, chess is a very nice candidate because it's numerical.

**[28:46 – 28:51]** You can play against each other, play against humans, to have an ELO rating.

**[28:51 – 28:54]** It's measurable. That's completely true.

**[28:54 – 29:04]** But on the other hand, and chess is easy to program in the sense that it's a finite game with fixed rules, blah, blah, blah.

**[29:04 – 29:10]** But on the other hand, chess is such a human game.

**[29:10 – 29:16]** You have to understand the flow of attack and defense on the chessboard.

**[29:16 – 29:25]** You have to maybe have a model of the other person's mind and understand what the other person is thinking about

**[29:25 – 29:32]** when he's making this move so that you can predict his intentions and maybe subvert them, et cetera, et cetera.

**[29:32 – 29:39]** So he was making this very plausible-sounding argument that chess is a good middle ground.

**[29:39 – 29:48]** And then, as you all know, in 1997, Deep Blue beat Kasparov.

**[29:48 – 29:53]** And I think the last match where humans had a chance was 2001.

**[29:53 – 29:58]** Vladimir Kramnik had a few matches against the best computers of the time,

**[29:58 – 30:02]** and he actually almost won at some point.

**[30:02 – 30:07]** I think he missed a mate and won very famously at one of the games.

**[30:07 – 30:13]** But after that, it was completely hopeless, right?

**[30:13 – 30:18]** So after 2001, there was no question who is better at chess.

**[30:18 – 30:27]** And by now, or even by 2010, 2015, there was even nothing humans could help with.

**[30:27 – 30:36]** So for a while, there was this field of centaur chess where a human with the help of a computer would play better than just a computer.

**[30:36 – 30:39]** But that is also a thing of the past.

**[30:39 – 30:51]** But did the AI researchers in 1997 or 2001, did they say, "Oh, okay, so we have the AGI now, the test has been passed"?

**[30:51 – 30:54]** Of course not, right?

**[30:54 – 30:59]** But what we all said collectively as a field was, "Oh, okay, so you beat chess."

**[30:59 – 31:01]** Well, chess doesn't count.

**[31:01 – 31:03]** Chess is too easy.

**[31:03 – 31:13]** Chess is, you know, you can just do a tree search and the tree search already gets you halfway to the best players.

**[31:13 – 31:14]** It doesn't count.

**[31:14 – 31:18]** Let's take Go, the game of Go, much better.

**[31:18 – 31:28]** It's still finite, it's still combinatorial, but you can never do a search tree in Go because there are too many possibilities.

**[31:28 – 31:30]** The branching factor is too big.

**[31:30 – 31:32]** That's true.

**[31:32 – 31:36]** You cannot have a meaningful complete search tree in Go.

**[31:36 – 31:43]** In chess you have like 10 reasonable moves at most, in Go you have 50 to 100 reasonable moves.

**[31:43 – 31:46]** So it's completely impossible to do the depth search.

**[31:46 – 31:51]** But AlphaGo happened, right?

**[31:51 – 31:53]** And then AlphaZero happened.

**[31:53 – 32:00]** And of course in Go computers in 2016-17 also became hopelessly better than humans.

**[32:00 – 32:05]** Well, did humans say now AlphaZero is the AGI?

**[32:05 – 32:06]** Of course not.

**[32:06 – 32:08]** Humans said well Go doesn't count.

**[32:08 – 32:15]** And that's the history of AI in a way and people still do that.

**[32:15 – 32:22]** People still say for some reason that LLMs don't count and they try to invent reasons why LLMs don't count.

**[32:22 – 32:27]** But the Turing test actually stood this test of time.

**[32:27 – 32:31]** So there was no moment in the 1980s when somebody would say,

**[32:31 – 32:35]** "Oh, I passed the Turing test with a stupid script, so it doesn't count."

**[32:35 – 32:37]** No, that didn't happen. Why?

**[32:37 – 32:45]** So my main point here, because what is the Turing test really about?

**[32:45 – 32:50]** Yes, it's about natural language processing in a big part.

**[32:50 – 32:55]** So it's about being able to talk in a natural language to a human in writing.

**[32:55 – 32:59]** But not only about that, right?

**[32:59 – 33:06]** The point of the Turing test is that when you have a freeform chat as opposed to a chess game,

**[33:06 – 33:12]** as opposed to question answering or whatever, you can talk about anything, right?

**[33:12 – 33:22]** You can actually, I don't know, you can introduce computer vision or at least 3D modeling into the Turing test.

**[33:22 – 33:27]** You can say, "Oh, hey, look, we are talking on the computer, right?

**[33:27 – 33:31]** So can you tell me what's on your desk?

**[33:31 – 33:35]** What's in front of you? What's on the left? What's on the right? What do you see? What's in the room?

**[33:35 – 33:38]** Can you please walk out of the room, describe what you see and then come back?"

**[33:38 – 33:42]** And yeah, sure, you have no way to check if that's true.

**[33:42 – 33:45]** But to actually make this picture consistent,

**[33:45 – 33:50]** the entity on the other side would need to kind of understand the 3D world.

**[33:50 – 33:59]** And natural language is complete in the sense that you can talk about anything.

**[33:59 – 34:04]** So why am I spending so much time on this?

**[34:04 – 34:11]** Because in a way, this is exactly the reason why modern LLMs are so great.

**[34:11 – 34:18]** So all that modern LLMs basically are trained to do,

**[34:18 – 34:20]** I think we'll get there at the end of the class,

**[34:20 – 34:23]** and I will explain it to you in more detail.

**[34:23 – 34:26]** But the base LLMs, what they are actually learning to do

**[34:26 – 34:29]** is just predict the next token in text.

**[34:29 – 34:31]** What is a language model?

**[34:31 – 34:36]** A language model is a machine that predicts the next word,

**[34:36 – 34:39]** the next token in natural language.

**[34:39 – 34:41]** That's it.

**[34:41 – 34:47]** But to predict the next token, you need to understand a lot of stuff.

**[34:47 – 34:52]** Not only do you need to understand how language works,

**[34:52 – 34:56]** so this will get you partly there, part of the way there.

**[34:56 – 35:01]** But then, after you understand how language works itself,

**[35:01 – 35:04]** you need to understand how the world works.

**[35:04 – 35:10]** So if the text says theorem, blah, blah, blah, proof, dot,

**[35:10 – 35:14]** and that you are supposed to predict the next token,

**[35:14 – 35:18]** well, maybe you need to prove the theorem first.

**[35:18 – 35:24]** And if the text says, I've been to Paris last month,

**[35:24 – 35:29]** and I visited the museum,

**[35:29 – 35:34]** and then you need to predict the next world,

**[35:34 – 35:38]** well, now you have to understand which museums are in Paris.

**[35:38 – 35:44]** So natural language includes everything.

**[35:44 – 35:46]** Well, maybe not exactly everything.

**[35:46 – 35:48]** It doesn't include stuff like robotics, for example.

**[35:48 – 35:50]** So robotics is a very different field

**[35:50 – 35:56]** because there is no huge set of books on,

**[35:56 – 36:04]** I don't know, what is the angle that you need to rotate your joints

**[36:04 – 36:07]** in order to pick up a cup from the table.

**[36:07 – 36:11]** So this you need to understand from other sources.

**[36:11 – 36:17]** But natural language is a great source of information for virtually everything.

**[36:17 – 36:22]** And that's the reason why LLMs keep surprising us.

**[36:22 – 36:27]** They keep getting this, uncovering these new capabilities

**[36:27 – 36:33]** that actually mostly come simply from predicting the next words in text.

**[36:33 – 36:37]** All right, I'm spending too much time on the Turing test.

**[36:37 – 36:42]** Sorry, one last point, a funny point on the Turing test, I hope.

**[36:42 – 36:49]** So if you look at the Turing test, at this competition where the machine is supposed to talk like a human,

**[36:49 – 36:53]** you notice immediately that it is completely, totally unfair.

**[36:53 – 36:57]** It's completely unfair to the computers.

**[36:57 – 37:02]** First of all, imagine the reverse Turing test.

**[37:02 – 37:07]** Imagine that we are checking in text,

**[37:07 – 37:12]** and I, a human, am trying to pass for a computer in this dialogue.

**[37:12 – 37:17]** How would you uncover that I am a human?

**[37:17 – 37:19]** What would be the question?

**[37:19 – 37:32]** What could you ask me so that you would immediately know that I am not a computer

**[37:32 – 37:35]** and I would have no way to pass for one?

**[37:35 – 37:48]** Can you give me an example of lemon pine?

**[37:48 – 37:53]** Why would it distinguish humans from computers?

**[37:53 – 38:01]** If you would give me this information, I would immediately understand that you are an LLM.

**[38:01 – 38:05]** Why?

**[38:05 – 38:13]** Actually, I don't know why, but if you have, for example, some assistance,

**[38:13 – 38:18]** if you need some help and you can ask, for example, some McDonald's chatbot

**[38:18 – 38:24]** and give me an example of lemon pine or give me some program in Python,

**[38:24 – 38:28]** I would immediately understand that you are an LLM, you are not a real person.

**[38:28 – 38:33]** No, wait, but I mean, imagine the reverse Turing test.

**[38:33 – 38:39]** So like I'm talking to you in chat and I'm a person, that's me,

**[38:39 – 38:42]** but I'm trying to pose as a computer, right?

**[38:42 – 38:46]** So I'm trying to convince you that I am a computer.

**[38:46 – 38:56]** What would you ask so that you immediately would realize that I am not a computer?

**[38:56 – 39:02]** It is worth trying like a math problem, a very complicated one.

**[39:02 – 39:11]** Yeah, for example, sure. So if you ask me what's, I don't know, 37 to the power of 23, I have no idea, right?

**[39:11 – 39:16]** And it would take me a long time to figure it out. For a computer, it's trivial, right?

**[39:16 – 39:24]** So we would never pass the reverse Turing test, we humans, right?

**[39:24 – 39:32]** Even for the computers of the 1950s, we would not pass. But that's okay.

**[39:32 – 39:37]** So this is, of course, inherently unfair, but ultimately we do want...

**[39:37 – 39:42]** The whole purpose is to teach computers to be like humans, not to teach humans to be like computers.

**[39:42 – 39:50]** So that's okay. But there is also one more subtle unfairness in the Turing test,

**[39:50 – 39:56]** which is, well, the computer needs to pose as a human.

**[39:56 – 40:02]** The computer needs to represent itself as somebody else.

**[40:02 – 40:05]** The human doesn't need to do that, the human just needs to be himself.

**[40:05 – 40:09]** That's unfair too, right?

**[40:09 – 40:12]** So the original Turing test, if you read the essay,

**[40:12 – 40:16]** the original Turing test was actually formulated as follows.

**[40:16 – 40:19]** It should be a judge, a human judge,

**[40:19 – 40:24]** trying to distinguish between a computer posing as a woman

**[40:24 – 40:28]** and a man posing as a woman,

**[40:28 – 40:31]** so that everybody would need to play somebody else

**[40:31 – 40:40]** and would need to walk in the shoes of as different a person as you can.

**[40:40 – 40:47]** And you can understand why this little detail got lost in the history of the Turing test,

**[40:47 – 40:51]** but it was there. I think it's also pretty fine.

**[40:51 – 40:54]** All right, so that was the Turing test.

**[40:54 – 40:57]** But that's kind of on the negative side,

**[40:57 – 41:06]** in the sense that, of course, in the 1950s, there was no way to pass the Turing test, not even to be close.

**[41:06 – 41:11]** But it kind of got people thinking.

**[41:11 – 41:23]** And the actual positive field of AI as a science, when you actually try to build stuff, emerged in 1956.

**[41:23 – 41:29]** It was the so-called Dartmouth workshop at Dartmouth, obviously.

**[41:29 – 41:34]** And it was organized by these four very famous researchers.

**[41:34 – 41:41]** John McCarthy was the early programming languages guy, he invented Lisp.

**[41:41 – 41:47]** Marvin Minsky was the guru of neural networks.

**[41:47 – 41:51]** I hope you all know Claude Shannon, the author of information theory.

**[41:51 – 41:56]** And Nathaniel Rochester, I keep forgetting what he did, but he built some computer at IBM.

**[41:56 – 41:59]** A very early and very famous computer.

**[41:59 – 42:11]** And the 1956 workshop had what I think, I always like to quote it because I think it was the most ambitious grant proposal in history.

**[42:11 – 42:13]** And it went like this.

**[42:13 – 42:21]** We propose a two-month study of artificial intelligence by 10 people in the summer, blah, blah, blah.

**[42:21 – 42:32]** We will attempt to find how to make machines use natural languages, find abstractions and concepts, solve problems now reserved for humans, and improve themselves.

**[42:32 – 42:34]** That's machine learning, right?

**[42:34 – 42:43]** We think significant advancement in one or more of these problems is possible if a carefully selected group of scientists works on it for a summer.

**[42:43 – 43:05]** Okay, and they were funded, they got together, they did conduct the workshop, but this grant proposal, of course they didn't actually do anything, they didn't actually solve any of these problems, but they kind of understood how difficult they were.

**[43:05 – 43:11]** But still, the 1950s and the early 1960s was a period of very high expectations.

**[43:11 – 43:26]** It was the golden age of science fiction. Everybody was expecting androids to walk, in a few years was expecting androids to walk around to bring you coffee, to talk to you in human language etc.

**[43:26 – 43:40]** That was the time when science fiction was expected to become alive very soon.

**[43:40 – 43:48]** What people actually did, the actual progress was of course very limited, but it was still very good progress.

**[43:48 – 43:58]** So for example there was this logic theories program, which I will not talk about in detail, but it was a theorem prover back in the day.

**[43:58 – 44:04]** It was thought that the important part was to teach AI logic, to teach AI math.

**[44:04 – 44:11]** Now we kind of understand that it doesn't work that way, but it was a very good prover for its time.

**[44:11 – 44:28]** It actually successfully reproved a lot of the fundamentals of mathematics, and it kind of also fueled these early high expectations.

**[44:28 – 44:43]** And there were some other examples, it doesn't matter, but basically what happened in the early 1960s, the optimism didn't work out.

**[44:43 – 44:56]** But the primary example of why people were disillusioned in AI in the 1960s was a failed project on machine translation.

**[44:56 – 45:11]** So people actually expected in the 1950s that they would write a program that would translate from Russian to English, if you believe it or not, and that it would work.

**[45:11 – 45:17]** And of course, it was completely beyond the abilities of computer science at that point.

**[45:17 – 45:26]** So in 1961 or 62, there was this big report that said, well, OK, so machine translation basically doesn't work.

**[45:26 – 45:33]** We need a lot more research. Let's regroup. And then, you know, the government got disillusioned.

**[45:33 – 45:41]** They stopped giving out grants for AI. And when you don't give out grants for research, researchers move to other fields.

**[45:41 – 45:50]** So ultimately, what we had in the 1970s is now known as the AI winter.

**[45:50 – 45:56]** And the AI winter means that there were very few people actually working on AI, on artificial intelligence.

**[45:56 – 46:06]** It was believed to be kind of too hard, impossible and inaccessible with current techniques, which was true in the 1970s.

**[46:06 – 46:11]** So it's not like people were wrong. The only thing that actually was happening were experts.

**[46:11 – 46:32]** And expert systems, they are kind of also AI, but they are a very specific kind of AI when you try to perform probabilistic reasoning on small snippets of domain knowledge, so to speak.

**[46:32 – 46:49]** So, for example, the main example is probably mycin, which was a 1970s system for diagnostics, medical diagnostics, based on blood tests.

**[46:50 – 46:54]** And what is a blood test? What are the results of a blood test?

**[46:54 – 47:09]** It's basically a big table of 50 numbers, right? You have red blood cells, white blood cells, hemoglobin, iron, whatever, all sorts of chemicals found in the blood.

**[47:10 – 47:19]** And an experienced doctor, an experienced physician can look at the blood test and say, oh, it's that disease. Oh, it's this disease.

**[47:19 – 47:27]** So that's the diagnostic problem. But however experienced the physician is, however experienced the patient is,

**[47:27 – 47:40]** I don't know, whether he's a genius diagnosed like Dr. House, it actually is completely impossible for a human to just sit down

**[47:40 – 47:46]** and write a function of 50 variables that would just give you the diagnosis. Human brains don't work like that.

**[47:46 – 47:58]** Even if you kind of know what to look for, et cetera, what you can actually formulate is not a general unifying function of everything,

**[47:59 – 48:09]** but you can formulate some local heuristics, like if the red blood cell count is high and the iron is low, then it's that,

**[48:09 – 48:16]** and if the alcohol content is 20%, then it's this, and so on and so forth.

**[48:17 – 48:25]** So you can ask doctors to give you this kind of local heuristics rules.

**[48:26 – 48:30]** And then the AI question, so you do not question the rules.

**[48:30 – 48:37]** The rules are given to you from a trusted source, so to speak.

**[48:37 – 48:41]** But the AI question is, how do you combine the rules?

**[48:41 – 48:46]** So now you are given a new blood test, and there are all sorts of problems.

**[48:46 – 48:51]** So like, okay, you have like 450 rules, and 20 of them kind of apply.

**[48:52 – 48:54]** But also, they don't apply.

**[48:55 – 49:00]** They kind of apply, because the rule is, again, not a mathematical function.

**[49:01 – 49:02]** A human doctor cannot do that.

**[49:02 – 49:10]** The rule is something like, if the red blood cell count is high, and what does high mean mathematically?

**[49:11 – 49:15]** Well, this high is definitely high.

**[49:16 – 49:18]** This high is definitely not high.

**[49:18 – 49:19]** But what about this?

**[49:19 – 49:20]** What's in the middle?

**[49:21 – 49:22]** Where is the threshold?

**[49:22 – 49:23]** Probably there is no threshold.

**[49:24 – 49:25]** Probably it's a continuous function.

**[49:25 – 49:31]** So there are all sorts of difficulties here, and that's what people were doing in the 1970s.

**[49:31 – 49:33]** I won't spend time on that, because that's not our subject.

**[49:33 – 49:35]** Definitely.

**[49:35 – 49:41]** And then what actually happened, so let me skip almost to the present, what actually happened

**[49:41 – 49:47]** was in the 1980s, people again got back to neural networks.

**[49:51 – 50:01]** In the 1980s, you already had convolutional networks and recurrent networks and multilayered

**[50:01 – 50:10]** net, deep networks, so basically you could have deep learning in the 1980s, 1990s, but

**[50:10 – 50:13]** you didn't, mostly for technological reasons.

**[50:14 – 50:19]** So people already kind of realized that neural networks are cool, but they didn't really

**[50:19 – 50:23]** work because there was not enough data and not enough compute to make them work.

**[50:24 – 50:24]** You needed more.

**[50:25 – 50:31]** And it all came together in the middle of the 2000s, so to say.

**[50:31 – 50:40]** So in 2005, 2006, 2007, several different labs, specifically Jeffrey Hinton's lab and Joshua Benja's lab,

**[50:40 – 50:44]** they actually kick-started this deep learning revolution.

**[50:45 – 50:46]** And that's when everything came together.

**[50:47 – 50:54]** So by that time, due to the internet, due to increased computational capabilities,

**[50:55 – 50:59]** you already had enough data to make neural networks work.

**[51:00 – 51:05]** And you also started to have enough compute.

**[51:06 – 51:12]** You started to have enough computational power to train large enough neural networks.

**[51:12 – 51:18]** And the final step was actually going from CPUs to GPUs.

**[51:18 – 51:22]** So we'll discuss it later when we discuss neural networks, actually.

**[51:23 – 51:30]** But it's kind of obvious that if you look at neural networks,

**[51:30 – 51:33]** that everything you do there is highly parallelizable.

**[51:33 – 51:39]** And it was a very natural idea when GPUs actually appeared in Webcom,

**[51:39 – 51:42]** and it was a very natural idea to switch from CPUs,

**[51:42 – 51:50]** which are like a few very fast cores, like four cores, four gigahertz each,

**[51:50 – 51:55]** switch to GPUs, which are much slower, but with hundreds and thousands, of cores.

**[51:56 – 52:05]** And that gave you this final boost that made deep learning actually work.

**[52:05 – 52:09]** And starting from the late 2000s,

**[52:10 – 52:16]** deep learning has, neural networks have been going from subfield of subfield to machine learning,

**[52:16 – 52:23]** and they have been setting state-of-the-art in a lot of different fields.

**[52:23 – 52:24]** So we'll discuss that later.

**[52:26 – 52:31]** And now, let me end the historical part here.

**[52:31 – 52:35]** And now, about what machine learning actually is.

**[52:36 – 52:42]** So how do you define what it means to learn?

**[52:42 – 52:44]** So what is learning?

**[52:45 – 52:51]** And we will get to a much more technical definition a bit later.

**[52:52 – 52:57]** But if you open some old textbook from the 1990s,

**[52:57 – 53:00]** you could find a definition like this.

**[53:00 – 53:04]** So like a computer program learns with accumulating experience

**[53:04 – 53:08]** regarding a class of tasks T and the performance measure P

**[53:08 – 53:11]** if its performance on these tasks improves it against your experience.

**[53:11 – 53:13]** So it doesn't say much.

**[53:13 – 53:14]** It sounds very trivial.

**[53:15 – 53:20]** But so what is, I think, important here on this slide

**[53:20 – 53:22]** is that when we are talking about learning,

**[53:23 – 53:26]** we have to have a performance measure, right?

**[53:27 – 53:30]** So we have to have some kind of number that goes up or down

**[53:30 – 53:32]** whenever it needs to go.

**[53:32 – 53:36]** So because if we don't, then we will never understand

**[53:36 – 53:38]** did we learn something or not, right?

**[53:38 – 53:44]** So in a way, the half of deep learning

**[53:44 – 53:47]** is about inventing the loss functions.

**[53:48 – 53:50]** It's about inventing these objectives.

**[53:51 – 53:54]** What is the number that we want to get down?

**[53:55 – 53:59]** How do we define the error so that when we minimize this error,

**[54:00 – 54:01]** we actually get what we want?

**[54:02 – 54:06]** Sometimes it's very easy, but sometimes it's kind of non-trivial.

**[54:06 – 54:09]** Sometimes it's part of the science.

**[54:09 – 54:13]** So this is the conclusion from this.

**[54:15 – 54:22]** And also, I think you have all seen at some previous class

**[54:22 – 54:23]** or somewhere in your life,

**[54:23 – 54:31]** you have seen this main taxonomy of machine learning problems.

**[54:31 – 54:34]** Let me go through it still.

**[54:35 – 54:39]** We will not talk too much about it later in class,

**[54:39 – 54:44]** because we will mostly exclusively be in here,

**[54:44 – 54:46]** in the supervised learning part.

**[54:46 – 54:49]** But let me just mention

**[54:49 – 54:52]** what kinds of machine learning problems there are.

**[54:52 – 54:58]** So technically, machine learning problems

**[54:58 – 55:01]** are divided into supervised learning, unsupervised learning,

**[55:01 – 55:04]** and reinforcement learning.

**[55:04 – 55:09]** And supervised learning is what we intuitively think of

**[55:09 – 55:12]** when we think of machine learning,

**[55:12 – 55:15]** like I need to build a classifier

**[55:15 – 55:19]** that distinguishes cats from dogs on a picture.

**[55:19 – 55:24]** So how do I build a classifier that distinguishes cats from dogs?

**[55:24 – 55:27]** I get a dataset of pictures,

**[55:27 – 55:30]** and for every picture I mark whether it's a cat or a dog,

**[55:30 – 55:34]** and then I train a classifier to distinguish between them.

**[55:34 – 55:44]** So I think it's a good time to actually start doodling on the board.

**[55:44 – 55:51]** So in supervised learning, there is the whole machine learning,

**[55:51 – 56:02]** and in supervised learning, you have...

**[56:02 – 56:08]** One sec, I'll make it a little more comfortable, so I can write better.

**[56:08 – 56:19]** So in supervised learning, the dataset consists of pairs of X and Y, right?

**[56:19 – 56:27]** So for example, X is the input, and Y is the output that you want to get.

**[56:27 – 56:36]** And your machine learning model is actually a machine.

**[56:36 – 56:40]** It's, let's say, a black box for now. We'll get there later.

**[56:40 – 56:48]** But it's a machine that takes the input and produces some function of the input

**[56:48 – 56:54]** that is supposed to look like the output, right?

**[56:54 – 57:02]** So we are trying to convert the input into the output.

**[57:02 – 57:07]** For example, if we are doing simple classification, simple binary classification,

**[57:07 – 57:13]** so there are cats and dogs here, then probably f of x is like a number from 0 to 1.

**[57:13 – 57:19]** And if it's close to 1, then we say it's a cat. If it's close to 0, then we say it's a dog.

**[57:19 – 57:24]** So it's kind of supposed to be the probability of a cat.

**[57:24 – 57:31]** But notice that it's the probability of a cat for a given picture, right?

**[57:31 – 57:39]** So it's the probability of a cat given x. And that's the whole point of supervised learning.

**[57:39 – 57:45]** So the point of supervised learning, mathematically speaking, is to learn whatever that means.

**[57:45 – 57:51]** We'll get there much later, but it's to learn the conditional distribution p of y given x.

**[57:51 – 57:59]** So we are always assuming that we will have the input.

**[57:59 – 58:07]** The classifier that distinguishes cats from dogs cannot draw you a new cat picture.

**[58:07 – 58:09]** It's not supposed to.

**[58:09 – 58:13]** It always presumes that you have a picture at the input.

**[58:13 – 58:16]** And then with this picture, you do stuff.

**[58:16 – 58:20]** So computer vision works like that, right?

**[58:20 – 58:27]** In computer vision, you always assume that you have a picture at the input.

**[58:27 – 58:38]** Well, maybe a set of pictures, maybe a video or whatever, but you have some high dimensional, very complicated input.

**[58:38 – 58:46]** And you're supposed to break this input down into the answers to the questions that you're interested in.

**[58:46 – 58:48]** And it's not necessarily a classification.

**[58:48 – 58:51]** There may be more interesting problems like object detection, like segmentation.

**[58:51 – 58:55]** We'll talk about those in class since we are doing computer vision here.

**[58:55 – 59:05]** But overall, you are trying to take a complicated input and convert it to some relatively simple output.

**[59:05 – 59:07]** So that's what supervised learning is about.

**[59:07 – 59:15]** And when you collect a dataset for supervised learning, you always need to have the correct answers.

**[59:15 – 59:26]** Sometimes, and in computer vision, unfortunately very often, it means that you need to have some very complicated labeling.

**[59:26 – 59:29]** And labeling is very difficult and expensive.

**[59:29 – 59:40]** So we'll talk about that when we get there, but for classification, it's not that expensive, but for things like segmentation, proper labeling is extremely expensive.

**[59:40 – 59:50]** So we will need to somehow, you know, do with relatively small datasets.

**[59:50 – 59:53]** But that's only the first part, right?

**[59:53 – 59:57]** There is also unsupervised learning.

**[59:57 – 1:00:09]** So there is this other field where there is no why, there is no correct answer.

**[1:00:09 – 1:00:19]** The dataset is just a set of something, and the big question is what are you supposed to do with it, right?

**[1:00:19 – 1:00:28]** Okay, so now we have a dataset of pictures, but the pictures, the images, they are not labeled in any way.

**[1:00:28 – 1:00:34]** So what are we even trying to do? What is the goal here?

**[1:00:34 – 1:00:47]** It actually turns out that you still can have a meaningful goal and you can still do stuff that will be very, very useful for downstream problems like classification, etc.

**[1:00:47 – 1:00:59]** And usually what unsupervised learning is doing is something called, let's call it dimensionality reduction.

**[1:00:59 – 1:01:14]** So reducing the size of X, compressing it so that on the one hand you compress X down to something.

**[1:01:14 – 1:01:25]** I still have a black box, but now the output is not some small known thing, but the output is, let's say, a vector of numbers.

**[1:01:25 – 1:01:47]** And X is still, let's say, a picture, but now the goal is not to classify X immediately, but the goal is to compress X down from its original size.

**[1:01:47 – 1:02:03]** And we will actually, I think we will talk about this more, but images are big, right? And if you think of images as sets of numbers, they are pretty big sets of numbers, right?

**[1:02:03 – 1:02:34]** So, like, how many numbers, I have a question to you, how many numbers are there in a one megapixel photo? One megapixel is how many pixels? No, come on, don't try to compute.

**[1:02:34 – 1:02:43]** Naive guess, like, 1000 square or something like that?

**[1:02:43 – 1:03:02]** Well, almost, right? So, a megapixel is not a million pixels, unfortunately, it's 1024 squared, right? So it's a power of 2. But whatever, okay? It's close to a million. And how many numbers is that?

**[1:03:02 – 1:03:42]** Like, if I take an image of one megapixel, and I say that, okay, I want to view it as a set of numbers, what is the dimension? How many numbers are there? How many numbers in a pixel? Come on, guys, you're in for a computer vision.

**[1:03:42 – 1:03:53]** Three numbers, right. Right. There are three numbers in a pixel. So a one megapixel photo, which is not that large, is 3 million numbers, approximately, right?

**[1:03:53 – 1:04:09]** Right. So if you think about this space of possible images, it's a huge space. It has a huge dimension. Nothing works in that dimension. Right.

**[1:04:09 – 1:04:18]** So it's it. And if you think about, like, what is the structure of the set of images in that space?

**[1:04:18 – 1:04:24]** Well, we, collective humanity, have absolutely no idea. Right.

**[1:04:24 – 1:04:28]** So it's very, very difficult. We have no idea how to how to describe this.

**[1:04:28 – 1:04:37]** So it's some very complicated manifold in this in the huge space of dimension 3 million.

**[1:04:37 – 1:04:52]** Right. So like imagine we can't imagine, but think of this set of like real photographs among all possible pixel values in dimension 3 million.

**[1:04:52 – 1:04:58]** What is the structure of this set? Right. This is completely incomprehensible.

**[1:04:58 – 1:05:01]** I can only say that it's an open set. Right.

**[1:05:01 – 1:05:12]** Because if you have a real photo and you move every pixel by a very, very tiny amount, nothing changes. Right.

**[1:05:12 – 1:05:22]** So it's still a real photo. But what actually distinguishes real photos from random noise, we have no idea. Right.

**[1:05:22 – 1:05:29]** And we have no idea what is the geometric structure of this manifold. It's probably extremely complicated.

**[1:05:29 – 1:05:34]** So what is unsupervised learning trying to do here?

**[1:05:34 – 1:05:44]** It's trying to map this extremely complicated manifold of real images to dimension much smaller.

**[1:05:44 – 1:05:53]** Let's say, I don't know, 500. That's just a number out of nowhere.

**[1:05:53 – 1:06:05]** It doesn't mean anything, but basically to project this huge space of images down to a more manageable, still large, but more manageable space,

**[1:06:05 – 1:06:16]** where hopefully it will be more comprehensible, easier to work with manifold.

**[1:06:16 – 1:06:21]** So that's usually the idea of unsupervised learning.

**[1:06:21 – 1:06:29]** So you want to do what in machine learning is called feature extraction.

**[1:06:29 – 1:06:37]** You want feature extraction or representation learning.

**[1:06:37 – 1:06:45]** You want to map a big object like an image to a much smaller object like a vector of numbers,

**[1:06:45 – 1:06:50]** but you want to do it in a way that would not lose important stuff.

**[1:06:50 – 1:06:56]** So you can't just take the first 100 pixels from here. That's not going to work.

**[1:06:56 – 1:07:08]** You want to map it in such a way that you actually are able to answer interesting questions in this space of these, in the small space.

**[1:07:08 – 1:07:17]** For example, in this manifold of real images, you still will be able to distinguish cats from dogs.

**[1:07:17 – 1:07:28]** Cats are here, and dogs are here, and now, all of a sudden, in this space, in this 500-dimensional space,

**[1:07:28 – 1:07:34]** there is actually a hyperplane, a linear surface separating cats from dogs.

**[1:07:34 – 1:07:37]** And it's very easy to separate cats from dogs over there.

**[1:07:37 – 1:07:48]** Over here, dogs are this part, and cats are this part, and there is absolutely no way to disentangle.

**[1:07:48 – 1:07:52]** Sorry.

**[1:07:52 – 1:07:56]** So this is the point usually of unsupervised learning.

**[1:07:56 – 1:08:02]** Compress down, make it more manageable,

**[1:08:02 – 1:08:07]** and hope that in this more manageable little space,

**[1:08:07 – 1:08:16]** you actually can have relatively simple machine learning models doing the stuff that you actually want.

**[1:08:16 – 1:08:21]** So this kind of compression is never the end goal, right?

**[1:08:21 – 1:08:24]** We don't want these vectors by themselves.

**[1:08:24 – 1:08:27]** We want them for some ultimate purpose.

**[1:08:27 – 1:08:31]** But the thing is, we don't fix this purpose in unsupervised learning.

**[1:08:31 – 1:08:34]** We don't know. Maybe we'll use it for that, maybe we'll use it for this.

**[1:08:34 – 1:08:38]** Right now, we just want to get good features.

**[1:08:38 – 1:08:41]** How do we do that?

**[1:08:41 – 1:08:44]** Well, actually, there is a pretty simple answer,

**[1:08:44 – 1:08:48]** which is very common in deep learning specifically.

**[1:08:48 – 1:08:53]** So while we are talking about this, let me tell you.

**[1:08:53 – 1:08:57]** So, of course, we cannot have a dataset with the correct Zs.

**[1:08:57 – 1:08:59]** There are no correct Zs.

**[1:08:59 – 1:09:01]** We have no idea what is the correct representation

**[1:09:01 – 1:09:05]** in this low-dimensional space.

**[1:09:05 – 1:09:09]** So how do we verify that this black box

**[1:09:09 – 1:09:11]** is doing anything meaningful?

**[1:09:11 – 1:09:14]** How do we...

**[1:09:14 – 1:09:17]** So here we have, in supervised learning,

**[1:09:17 – 1:09:20]** we have a dataset with axis and y's,

**[1:09:20 – 1:09:22]** and we can just run the black box

**[1:09:22 – 1:09:26]** through the examples that we have

**[1:09:26 – 1:09:29]** and check that we get correct answers.

**[1:09:29 – 1:09:32]** Over here, there are no correct answers.

**[1:09:32 – 1:09:36]** But we cannot, as we will see soon,

**[1:09:36 – 1:09:39]** we cannot train a neural network without a loss function.

**[1:09:39 – 1:09:42]** We cannot train a neural network without some kind of goal,

**[1:09:42 – 1:09:46]** specific numerical goal that we want to optimize.

**[1:09:46 – 1:09:49]** So what would be the goal here?

**[1:09:49 – 1:09:53]** And there can be different answers,

**[1:09:53 – 1:09:56]** but in deep learning one very common idea

**[1:09:56 – 1:10:00]** is to do a thing called an autoencoder,

**[1:10:00 – 1:10:05]** which works like this.

**[1:10:05 – 1:10:07]** So I have this big thing, x.

**[1:10:07 – 1:10:13]** I get it through my neural network.

**[1:10:13 – 1:10:15]** Okay, that doesn't matter if it's a neural network,

**[1:10:15 – 1:10:17]** through my first machine learning model,

**[1:10:17 – 1:10:20]** which is called the encoder.

**[1:10:20 – 1:10:24]** And I get the vector z.

**[1:10:24 – 1:10:27]** But let's not stop there.

**[1:10:27 – 1:10:32]** Let's say, okay, so how do I verify that compression is good?

**[1:10:32 – 1:10:37]** Well, compression should, first of all, compress down to a smaller size.

**[1:10:37 – 1:10:39]** Here, it's by definition.

**[1:10:39 – 1:10:42]** I choose the size of z myself.

**[1:10:42 – 1:10:47]** But what does it mean to compress something and not just pick random numbers?

**[1:10:47 – 1:10:50]** It means that from the compressed object,

**[1:10:50 – 1:10:54]** I can reconstruct back the original.

**[1:10:54 – 1:10:56]** That's the whole point.

**[1:10:56 – 1:11:02]** It wouldn't be a very good archive tool

**[1:11:02 – 1:11:08]** It would produce just random bits and you would have no way to recover the files.

**[1:11:08 – 1:11:15]** So the whole point is to compress down in such a way that you can decompress back.

**[1:11:15 – 1:11:19]** So we add the decompressor.

**[1:11:19 – 1:11:21]** We add the decoder part,

**[1:11:21 – 1:11:29]** which takes the z and tries to restore the original image.

**[1:11:29 – 1:11:32]** Let's say it's x hat.

**[1:11:32 – 1:11:36]** So x is the input and x hat is the final output.

**[1:11:36 – 1:11:41]** So the decoder is probably also a neural network.

**[1:11:41 – 1:11:44]** The decoder is also a complicated neural network.

**[1:11:44 – 1:11:46]** It's like a generative model.

**[1:11:46 – 1:11:50]** It takes in something that looks like random noise, just numbers,

**[1:11:50 – 1:11:53]** and should produce a beautiful cat picture.

**[1:11:53 – 1:11:57]** So it does make our task more difficult, sure.

**[1:11:57 – 1:12:03]** But now we have a very easy way to say what we are looking for.

**[1:12:03 – 1:12:06]** So now we know exactly what the loss function should be,

**[1:12:06 – 1:12:13]** because the result should be just, you know, similar to the input.

**[1:12:13 – 1:12:14]** That's it.

**[1:12:14 – 1:12:21]** And you can define loss function basically like x hat minus x squared,

**[1:12:21 – 1:12:24]** like just the squared deviation in the pixels.

**[1:12:24 – 1:12:30]** That's a very common loss function in autoencoders.

**[1:12:30 – 1:12:37]** So this kind of idea, compress then decompress back,

**[1:12:37 – 1:12:42]** we will encounter it in class a couple of times.

**[1:12:42 – 1:12:46]** And it's a very natural thing to do in unsupervised learning.

**[1:12:46 – 1:12:55]** So when you are just trying to make sense of your inputs,

**[1:12:55 – 1:13:01]** of your data set, what is your goal?

**[1:13:01 – 1:13:03]** You are trying to find structure inside.

**[1:13:03 – 1:13:05]** What does it mean to find structure?

**[1:13:05 – 1:13:11]** Well, actually, in reality, it usually means to project down to a smaller space

**[1:13:11 – 1:13:16]** where you can see this structure more clearly.

**[1:13:16 – 1:13:22]** And if you've heard of unsupervised learning before,

**[1:13:22 – 1:13:29]** you probably heard about the example that was characteristic,

**[1:13:29 – 1:13:33]** that was the central example of unsupervised learning for a long time.

**[1:13:33 – 1:13:37]** I think now autoencoders and dimensionality reduction in general are more important,

**[1:13:37 – 1:13:44]** but for a long time the main example of unsupervised learning was clustering.

**[1:13:44 – 1:13:50]** Clustering, we won't talk about it much, out of scope for us,

**[1:13:50 – 1:13:55]** but clustering is this problem, you probably have an intuitive understanding of it,

**[1:13:55 – 1:14:00]** when you have some points, some objects,

**[1:14:00 – 1:14:05]** and your task is to split them into groups, clusters,

**[1:14:05 – 1:14:11]** so that points inside a cluster are similar to each other, are close to each other,

**[1:14:11 – 1:14:16]** and points across different clusters are different.

**[1:14:16 – 1:14:25]** The only thing I want to say about clustering is that you can view it as the extreme form of dimensionality reduction.

**[1:14:25 – 1:14:44]** So clustering means also taking a large object and compressing it down to Z in a smaller space,

**[1:14:44 – 1:14:48]** but now the dimension of this space is zero.

**[1:14:48 – 1:15:00]** So we are compressing each point to the label of its cluster, and there is just a finite set of different labels.

**[1:15:00 – 1:15:04]** And you can view it like that, and it's a very natural view of clustering.

**[1:15:04 – 1:15:16]** You compress down to a discrete finite set of points, and then you do it in such a way that decompression is as faithful as possible still.

**[1:15:16 – 1:15:24]** So the whole point of clustering is that you kind of want to replace all points in the cluster by its center or by the cluster label.

**[1:15:24 – 1:15:29]** And then you will be able to deconstruct the points as best you can.

**[1:15:29 – 1:15:36]** And yeah, okay, again, I'm spending too much time on supervised learning, but it's useful, I think.

**[1:15:36 – 1:15:44]** And if in supervised learning we were learning the distribution p of y given x,

**[1:15:44 – 1:15:53]** in unsupervised learning we are just trying to learn p of x, there is no y.

**[1:15:53 – 1:16:00]** And how does it map to this autoencoder or to the clustering picture or whatever?

**[1:16:00 – 1:16:03]** What does it mean to learn the distribution?

**[1:16:03 – 1:16:11]** Well, here in the autoencoder part it would probably mean to learn to sample from the distribution.

**[1:16:11 – 1:16:29]** So here you would say that z is kind of like random noise and the decoder converts the random noise into x that is supposed to be from the distribution of cat pictures.

**[1:16:29 – 1:16:40]** So I don't think we'll get to this kind of analysis in class, but again, useful to keep in mind.

**[1:16:40 – 1:16:50]** In supervised learning, we always have an x, we always have the input. In unsupervised learning, we are trying to describe the x itself.

**[1:16:50 – 1:17:01]** And very often, it means that we are actually learning a generative model that can produce new samples of x's.

**[1:17:01 – 1:17:06]** In the case of pictures, that can draw new pictures.

**[1:17:06 – 1:17:20]** And finally, there is the third guy, which we will not talk about at all, which is called reinforcement learning.

**[1:17:20 – 1:17:29]** Unfortunately, I cannot make this class about everything, so let me skip reinforcement learning.

**[1:17:29 – 1:17:40]** Let me just say a few words. Reinforcement learning is the subfield of machine learning where there is no dataset in the beginning.

**[1:17:40 – 1:17:58]** Instead of the dataset, you have your model being an agent in an environment, and the dataset is ultimately the experience of living in this environment.

**[1:17:58 – 1:18:09]** For example, if you are learning to play chess, then your agent does not have a dataset of correct moves.

**[1:18:09 – 1:18:21]** And it does not have a dataset of all possible positions from chess games and trying to compress them down like an unsupervised learning.

**[1:18:21 – 1:18:36]** So what your model is probably doing is it's playing chess against itself or against earlier versions of itself or against other models or whatever, and learning to play as it goes from the signal of who won.

**[1:18:36 – 1:18:53]** So that's how reinforcement learning works. You live in your environment, you get rewards that are, in the case of chess it's simple, the reward is who won.

**[1:18:53 – 1:19:14]** In robotics the reward may be more complicated but whatever, you get rewards from the environment and ultimately you learn to maximize these rewards.

**[1:19:14 – 1:19:22]** So you learn to behave, you learn a policy for behaving in the environment such that the reward gets maximized.

**[1:19:22 – 1:19:33]** Actually it's a pretty different topic. It has some pretty different approaches from supervised and unsupervised learning, so we will not be talking about it in class.

**[1:19:33 – 1:19:39]** I hope you will have a separate class on RL at some point. It's a very beautiful field.

**[1:19:39 – 1:19:49]** All right, so we discussed this. I think we'll skip these practical things like cross-validation and stuff.

**[1:19:49 – 1:19:55]** Maybe someone will talk to you about this in the practical part.

**[1:19:55 – 1:20:00]** Yeah, dimensionality reduction.

**[1:20:00 – 1:20:09]** All right, so I think now is a good time to have a break.

**[1:20:09 – 1:20:13]** We have come to the end of the intro part.

**[1:20:13 – 1:20:22]** Sorry, I should have started with this. I forgot to talk to you about the class itself and its structure.

**[1:20:22 – 1:20:34]** Basically, unfortunately, I'm not able to come to Barcelona this year, so I'm teaching online.

**[1:20:34 – 1:20:41]** And my colleague Alex Davidov will be with you offline on campus.

**[1:20:41 – 1:20:49]** I will be delivering lectures, and it's not what I would advise to do.

**[1:20:49 – 1:20:54]** But for logistical reasons, we will have a lot of lectures at the start.

**[1:20:54 – 1:21:00]** So we will have three days of lectures today, tomorrow and Wednesday.

**[1:21:00 – 1:21:12]** And I hope we will make some good progress and have a good start

**[1:21:12 – 1:21:18]** so that Alex will have something to work with when he begins on Thursday.

**[1:21:18 – 1:21:27]** And then I think we will mostly alternate like this, like two lectures, two practical sessions and so on.

**[1:21:27 – 1:21:29]** And ultimately we will even it out.

**[1:21:29 – 1:21:36]** I will be mostly awake next week and then I'll come back for the final lecture.

**[1:21:36 – 1:21:40]** Okay, so let's have a break.

**[1:21:40 – 1:21:46]** Are there any questions about the first part or the structure or whatever?

**[1:21:46 – 1:21:48]** How long a break do you need?

**[1:21:48 – 1:21:52]** Like offline it's usually half an hour, but maybe online we don't need that much.

**[1:21:52 – 1:22:01]** How long would you wait? 15 minutes, okay?

**[1:22:01 – 1:22:16]** Okay, so let's say 15 to 20 minutes and it's 11, sorry, 10 for you, 10:35.

**[1:22:16 – 1:22:21]** So on 10:50, 10:55, let's continue.

**[1:22:21 – 1:44:02]** Okay, break.

**[1:44:02 – 1:44:08]** Continue.

**[1:44:08 – 1:44:17]** All right, so in the first part, while you're getting back, I'll do a quick recap.

**[1:44:17 – 1:44:33]** In the first part, we discussed the history of artificial intelligence, how it all came to be, the early ideas like the Turing test, etc.

**[1:44:33 – 1:44:54]** And specifically, on point specifically, something actually useful for our machine learning class, we discussed the main and the most common taxonomy of machine learning problems.

**[1:44:54 – 1:45:08]** This distinction between supervised learning and supervised learning and reinforcement learning. And in the second part today, I want to talk about what learning actually means.

**[1:45:08 – 1:45:23]** And I have always understood it and I recommend you to understand it through the Bayesian perspective, through the probabilistic perspective. I will explain what I mean.

**[1:45:23 – 1:45:50]** But first of all, like for those of you who have had, I don't know, probability theory classes in your universities or in hardware space, you're probably kind of not very happy to hear that machine learning is pure probability theory from start to finish.

**[1:45:50 – 1:46:11]** Because usually when I say probability theory to my students, they get a little bit scared because a probability theory class is usually some very involved, difficult mathematical stuff about measure theory.

**[1:46:11 – 1:46:23]** You start with the sigma algebra of measurable Borel sets in the Euclidean space and then you introduce your probability as a measure.

**[1:46:23 – 1:46:35]** And then what the expectation is is already pretty difficult and what the conditional expectation is is extremely difficult and it's all some abstract theorems, etc.

**[1:46:35 – 1:46:43]** We won't need any of that stuff. I'm not saying forget it, don't forget it if you know it, but we won't need any of that.

**[1:46:43 – 1:46:55]** We'll need, you know, there is a saying I think by Cervantes that education is what remains after you've forgotten everything you were taught.

**[1:46:55 – 1:47:07]** So this is exactly this kind of thing. What we will need in probability theory is the intuition that remains after you forget all about the theorems

**[1:47:07 – 1:47:16]** and you actually, you know, you actually get this basic intuition of what probability is about.

**[1:47:16 – 1:47:20]** So what is it about? It's about random variables, right?

**[1:47:20 – 1:47:35]** And random variables, there are discrete random variables, like coin tosses, like coin tosses or, I should have prepared.

**[1:47:35 – 1:47:39]** So coin tosses and die rolls and stuff like that.

**[1:47:39 – 1:47:45]** And if you have a discrete set of...

**[1:47:45 – 1:47:47]** If you have a discrete set of...

**[1:47:47 – 1:47:50]** No, I don't. We'll improvise.

**[1:47:50 – 1:47:58]** And if you have a discrete set of outcomes, then the probabilities of these outcomes should sum to one.

**[1:47:58 – 1:48:02]** And that's your probability, right? That's your random variable.

**[1:48:02 – 1:48:11]** And then you can have continuous random variables where instead of probabilities of outcomes,

**[1:48:11 – 1:48:13]** you have the density function, right?

**[1:48:13 – 1:48:17]** And at this point, if you've had a probability theory class, you will tell me,

**[1:48:17 – 1:48:22]** "Oh, wait, but not every probability has a density, right?

**[1:48:22 – 1:48:28]** And many probabilities, including important ones, cannot be characterized by the density,

**[1:48:28 – 1:48:32]** and therefore, you need measure theory, blah, blah, blah." Forget about that.

**[1:48:32 – 1:48:39]** In machine learning, we only deal with kind of standard and easy probabilities.

**[1:48:39 – 1:48:46]** So everything that we will ever discuss will, of course, have a density.

**[1:48:46 – 1:48:54]** And in that case, the summing to one means taking an integral, right?

**[1:48:54 – 1:48:59]** An integral over the probability space.

**[1:48:59 – 1:49:03]** And again, there will be no exotic probability spaces here.

**[1:49:03 – 1:49:10]** Only the real line, r to some power, only the Euclidean space.

**[1:49:10 – 1:49:18]** And the things that we actually need in machine learning are these basic intuitions

**[1:49:18 – 1:49:21]** and the very basic definitions of probability theory, right?

**[1:49:21 – 1:49:31]** So now I really do hope that on this slide there is nothing new for you.

**[1:49:31 – 1:49:38]** If there is, I recommend you to repeat your probability basics a little bit

**[1:49:38 – 1:49:41]** because we will be using some of that.

**[1:49:41 – 1:49:45]** But okay, I will just go through this very quickly.

**[1:49:45 – 1:49:52]** If you have two events, two random variables, they can happen at the same time.

**[1:49:52 – 1:49:58]** Then you can define the joint probability, p of x, y.

**[1:49:58 – 1:50:08]** Actually, let me switch to the board. It will be better to explain it more interactively.

**[1:50:08 – 1:50:20]** There are random variables characterized by their probability mass functions, p of x if they are discrete.

**[1:50:20 – 1:50:26]** So just what is the probability of every outcome on a die from 1 to 6?

**[1:50:26 – 1:50:33]** Or by density functions like, I don't know, maybe it's concentrated from 0 to 1.

**[1:50:33 – 1:50:46]** We'll have an example like this today. Then it's some function whose integral is supposed to be equal to 1.

**[1:50:46 – 1:50:57]** And this is the density function for a random variable that samples you a number from 0 to 1.

**[1:50:57 – 1:51:05]** And if you have two random variables, then you can have their joint probability, p .

**[1:51:05 – 1:51:14]** So p is something like p equals to something and y equals to something else.

**[1:51:14 – 1:51:21]** So if you have your joint probability and you want to get only the marginal,

**[1:51:21 – 1:51:25]** it's called the marginal probability, the probability of one of the x and y's,

**[1:51:25 – 1:51:29]** then you need to kind of sum this over y.

**[1:51:29 – 1:51:35]** That's not a very formal way to write it, but I hope you understand what I mean.

**[1:51:35 – 1:51:40]** So if you have p equals a and equals to something else,

**[1:51:40 – 1:51:45]** and you want to get what is the probability of just p of x equals a,

**[1:51:45 – 1:51:49]** you need to sum over all possible values of y.

**[1:51:49 – 1:51:51]** Kind of makes sense.

**[1:51:51 – 1:51:58]** And from the joint probability, we get the notion of conditional probability.

**[1:51:58 – 1:52:01]** This is the most important notion for machine learning.

**[1:52:01 – 1:52:05]** So what is conditional probability?

**[1:52:05 – 1:52:08]** Conditional probability, p of x given y, right,

**[1:52:08 – 1:52:15]** is the probability that x, let's say, is equal to something,

**[1:52:15 – 1:52:18]** given that we know the value of y, right?

**[1:52:18 – 1:52:24]** And formally, it's very easy to define.

**[1:52:24 – 1:52:30]** Formally, just we take the joint probability, p of x, y,

**[1:52:30 – 1:52:35]** and we decompose it into p of x given y times p of y.

**[1:52:35 – 1:52:39]** I think this formula has some name, like full probability formula,

**[1:52:39 – 1:52:41]** or something like that, I keep forgetting.

**[1:52:41 – 1:52:48]** Doesn't matter, but the point is, this is the definition of conditional probability.

**[1:52:48 – 1:52:57]** So p of x given y is defined as p of x, y divided by p of y, right?

**[1:52:57 – 1:53:05]** And we'll have a lot of conditional probabilities later today and tomorrow, probably.

**[1:53:05 – 1:53:11]** And if you look at this definition, if you look at this decomposition of the joint probability

**[1:53:11 – 1:53:18]** into the marginal and the conditional, then you notice that you can do it both ways, right?

**[1:53:18 – 1:53:22]** You can start with y, like we did here.

**[1:53:22 – 1:53:29]** I mean, okay, one way to read this formula is how do you sample x and y?

**[1:53:29 – 1:53:32]** Well, you can start with y.

**[1:53:32 – 1:53:38]** You can sample y first from its own distribution, and then you already know what y is,

**[1:53:38 – 1:53:43]** and you need to sample x given this value of y.

**[1:53:43 – 1:53:45]** Or you can start with x.

**[1:53:45 – 1:53:51]** You can first sample x and then sample y given x.

**[1:53:51 – 1:53:53]** You can view it this way.

**[1:53:53 – 1:53:57]** But it's still, I mean, formally, it's still the definition of conditional probability,

**[1:53:57 – 1:54:00]** just the definition of p of y given x.

**[1:54:00 – 1:54:06]** But if you combine these formulas, you see that they amount to the same thing, to the joint p of x, y.

**[1:54:06 – 1:54:15]** And this is where you get the most important formula in the whole world,

**[1:54:15 – 1:54:20]** definitely in the whole machine learning, but I think it's wider than that.

**[1:54:20 – 1:54:35]** And that formula is, well, p of y given x is p of x given y times p of y divided by p of x, right?

**[1:54:35 – 1:54:41]** This is the base rule or base formula.

**[1:54:41 – 1:54:49]** And the way we present it now, it's completely trivial, right?

**[1:54:49 – 1:54:54]** It directly basically follows in one line from the definition of conditional probability.

**[1:54:54 – 1:55:05]** But in effect, philosophically, that's basically how reasoning works.

**[1:55:05 – 1:55:14]** Our actual real reasoning, not logical derivations where there are no probabilities and all facts are known for sure.

**[1:55:14 – 1:55:17]** In real life, we seldom know facts for sure, right?

**[1:55:17 – 1:55:23]** In real life, it's all about balancing the probabilities and weighing in the evidence.

**[1:55:23 – 1:55:30]** And the base formula underlies how you account for evidence,

**[1:55:30 – 1:55:34]** how you actually take something into account.

**[1:55:34 – 1:55:38]** We will definitely discuss it more.

**[1:55:38 – 1:55:42]** But before we do that, one last thing.

**[1:55:42 – 1:55:47]** There is also this very important notion of independence.

**[1:55:47 – 1:55:53]** And basically two random variables are independent

**[1:55:53 – 1:55:58]** if P , their joint probability, joint density,

**[1:55:58 – 1:56:01]** is equal to P times P .

**[1:56:01 – 1:56:08]** So if P decomposes into the products of individual densities

**[1:56:08 – 1:56:11]** or individual probabilities.

**[1:56:11 – 1:56:16]** In this case, the conditional is trivial, right?

**[1:56:16 – 1:56:23]** So basically the same thing you can say P given Y is equal to just P .

**[1:56:23 – 1:56:25]** The conditional is trivial.

**[1:56:25 – 1:56:31]** It means that P does not depend on the value of Y.

**[1:56:31 – 1:56:33]** That's why it's called independence.

**[1:56:33 – 1:56:36]** So two variables are independent,

**[1:56:36 – 1:56:39]** which basically means that you can sample them separately.

**[1:56:39 – 1:56:46]** You'll get the same result, like two coins that you toss in a row.

**[1:56:46 – 1:57:11]** And let's get back to the bias formula. And let me actually just first restate it in a slightly different notation, and then we'll discuss it. So let's call it the main formula of machine learning.

**[1:57:11 – 1:57:29]** And let me write it like this. p of theta given d equals p of d given theta times p of theta divided by p of d. Okay. It's the same formula, right? I just changed the notation.

**[1:57:29 – 1:58:00]** But I hope you kind of now understand what this notation is supposed to represent. So now d is the data. d is the data set, right? And theta are the model parameters. Theta is what we actually want to learn.

**[1:58:00 – 1:58:14]** So if we are talking about a neural network, we want to learn the weights, right? And notice that it's not the exact value of the weights. It's a whole distribution of weights. So we will get back to that.

**[1:58:14 – 1:58:30]** But for now, let's just say theta is the model parameters. Theta is the weights of a linear regression. That's going to be our first serious example. Or theta is the weights of a neural network. Or theta is just the probability of the coin that we are trying to learn.

**[1:58:30 – 1:58:58]** So let's say we have a... Okay, here is my coin. It has two sides. And I can toss it and I can get some results. And the data will be the set of outcomes, the set of results of what I'm getting from the coin tosses. And the parameters will be just the probability of getting heads, right?

**[1:58:58 – 1:59:12]** So the whole point of machine learning is to understand, to learn the model parameters from the data, right?

**[1:59:13 – 1:59:22]** So we have a set of outcomes for some stochastic process, for some random process where there is some inherent randomness.

**[1:59:23 – 1:59:30]** And we want to understand what was governing this process, what were the parameters that went into this process.

**[1:59:30 – 1:59:34]** This is the whole idea of machine learning. Everything else is basically commentary.

**[1:59:35 – 1:59:43]** And the biased theorem is the main tool for this. Why? What is so special about this?

**[1:59:43 – 1:59:47]** So let's discuss what we have in this formula.

**[1:59:48 – 1:59:52]** On the left, I have P of theta given D.

**[1:59:52 – 1:59:58]** P of theta given D is called the posterior probability or the posterior distribution.

**[2:00:01 – 2:00:08]** Posterior means after the fact, a posteriori, after evidence has been included.

**[2:00:09 – 2:00:12]** And that's what it says, right?

**[2:00:12 – 2:00:13]** So it's very, very intuitive.

**[2:00:14 – 2:00:20]** I get some data and I want to understand what I now think about theta,

**[2:00:21 – 2:00:28]** how my understanding of theta has changed given data after I have taken the data set into account.

**[2:00:28 – 2:00:30]** That's the posterior distribution.

**[2:00:30 – 2:00:34]** I want to, I want to, this is my goal in learning, right?

**[2:00:34 – 2:00:36]** So, okay, the final goal will be doing predictions.

**[2:00:36 – 2:00:37]** We'll get to that later.

**[2:00:37 – 2:00:42]** But like the intermediate goal is learning what I can about theta from D.

**[2:00:44 – 2:00:45]** Okay.

**[2:00:46 – 2:00:53]** And usually there is no way to get to this distribution directly without going through this formula.

**[2:00:54 – 2:00:56]** So how do we get to this distribution?

**[2:00:58 – 2:01:03]** Well, the bias rule tells us that it's the product of two things, basically.

**[2:01:03 – 2:01:13]** It's the product of P of D given theta, which is called the likelihood.

**[2:01:16 – 2:01:18]** So what is P of D given theta?

**[2:01:19 – 2:01:31]** It's the probability or usually the density of getting a specific data set given the parameters,

**[2:01:31 – 2:01:32]** given the model parameters.

**[2:01:33 – 2:01:36]** I'll make a coin tossing example in a second.

**[2:01:36 – 2:01:36]** It will be clear.

**[2:01:36 – 2:01:43]** But basically, when you define a model in machine learning, you usually define the likelihood.

**[2:01:44 – 2:01:45]** This is the easy part.

**[2:01:45 – 2:01:51]** The likelihood is what you get from just listing your assumptions and writing them down as formulas.

**[2:01:53 – 2:01:58]** And the main point of the Bayes rule is that the likelihood is not enough.

**[2:01:59 – 2:02:08]** You also need the third part, this guy, which is called the prior distribution or just the prior.

**[2:02:10 – 2:02:15]** The prior is just P of theta without any D, right?

**[2:02:15 – 2:02:35]** And what does it mean, philosophically speaking, it means what were we thinking about theta in advance before we started getting data, before we started getting D, right?

**[2:02:35 – 2:02:37]** So P of theta without any D.

**[2:02:40 – 2:02:44]** And I will make an extensive example in a minute.

**[2:02:44 – 2:03:05]** So the bias formula basically tells you if you want to get the posterior distribution, if you want to incorporate D into your thinking of theta, you need to take what you thought about theta before and multiply it by the likelihood of D.

**[2:03:05 – 2:03:20]** So for example, for example, oh, sorry, I wanted to say I didn't talk about the denominator, but I forgot to say that I didn't talk about it.

**[2:03:20 – 2:03:30]** So the denominator, indeed, I didn't talk about it, it's usually called the full probability or the evidence probability, something like that.

**[2:03:31 – 2:03:38]** And mostly P of D is not really important for us in machine learning.

**[2:03:38 – 2:03:41]** Why? Because it doesn't have any theta.

**[2:03:42 – 2:03:49]** So in machine learning, P of D is usually completely inaccessible by itself.

**[2:03:50 – 2:03:56]** So instead of writing the full bias rule, actually, usually we use it like this.

**[2:03:56 – 2:04:02]** P of theta given D is proportional to P of D given theta times P of theta.

**[2:04:03 – 2:04:05]** This means proportional.

**[2:04:07 – 2:04:09]** And what does proportional mean in this case?

**[2:04:09 – 2:04:14]** It means that, well, P of theta given D should be a probability distribution.

**[2:04:14 – 2:04:16]** So it should integrate to one.

**[2:04:17 – 2:04:22]** So almost always, actually completely always, I know no exceptions,

**[2:04:23 – 2:04:29]** P of D, the only way to compute P of D is to make it a normalizing constant for the numerator.

**[2:04:30 – 2:04:37]** So P of D is always just this, okay?

**[2:04:38 – 2:04:43]** And in some special cases, you might be interested in P of D, yes?

**[2:04:43 – 2:04:49]** But usually what you do is, what you do in machine learning and deep learning,

**[2:04:49 – 2:04:55]** usually you are just interested in, let's suppose, maximizing this with respect to theta.

**[2:04:55 – 2:04:59]** And if you maximize this, it's the same as maximizing this.

**[2:05:00 – 2:05:02]** And you don't care about the constant, right?

**[2:05:03 – 2:05:05]** So we'll get to that a bit later.

**[2:05:06 – 2:05:10]** So the denominator is complicated, but usually not really necessary.

**[2:05:10 – 2:05:12]** So we won't talk about that too much.

**[2:05:13 – 2:05:15]** Okay, now example.

**[2:05:16 – 2:05:20]** Let's learn a coin toss, okay?

**[2:05:20 – 2:05:24]** Here is a coin, or what passes for one.

**[2:05:25 – 2:05:25]** It has two sides.

**[2:05:26 – 2:05:27]** And I can toss it.

**[2:05:27 – 2:05:32]** So, how many parameters does a coin have?

**[2:05:33 – 2:05:34]** What is the size of the vector theta?

**[2:05:35 – 2:05:36]** Can you tell me?

**[2:05:45 – 2:06:00]** How many numbers do we need to define a coin with two sides?

**[2:06:12 – 2:06:25]** Okay, maybe I'm not asking the question clearly enough.

**[2:06:25 – 2:06:31]** So, a coin is a stochastic process, right?

**[2:06:31 – 2:06:33]** It's a random variable.

**[2:06:34 – 2:06:38]** I toss it, I get either heads or tails with some probabilities.

**[2:06:38 – 2:06:41]** So, how many numbers do I need to define these probabilities?

**[2:06:42 – 2:06:42]** How many parameters?

**[2:06:48 – 2:06:55]** What are the parameters for a coin?

**[2:06:56 – 2:07:01]** What probabilities do you need to fully understand a coin toss?

**[2:07:03 – 2:07:09]** Maybe just one, like the probability of one outcome?

**[2:07:10 – 2:07:11]** Yeah, precisely, of course.

**[2:07:12 – 2:07:14]** So, a coin has just one parameter.

**[2:07:15 – 2:07:15]** Very easy.

**[2:07:16 – 2:07:18]** The simplest example we can think of.

**[2:07:18 – 2:07:20]** So, let's say theta is the probability of heads.

**[2:07:20 – 2:07:26]** Okay, then the probability of tails will be what?

**[2:07:32 – 2:07:34]** 1 minus theta, precisely.

**[2:07:35 – 2:07:39]** And this is our first example,

**[2:07:39 – 2:07:45]** our first illustration of this probabilistic view of machine learning.

**[2:07:46 – 2:07:51]** And now you can start seeing why the likelihood is very natural.

**[2:07:52 – 2:07:53]** So, what is the likelihood now?

**[2:07:54 – 2:07:59]** The likelihood is this, is P of D given theta, likelihood.

**[2:07:59 – 2:08:00]** What is D?

**[2:08:01 – 2:08:02]** D is the data.

**[2:08:03 – 2:08:04]** So, it's the sequence of outcomes.

**[2:08:06 – 2:08:10]** D is like, I've been tossing this coin several times,

**[2:08:10 – 2:08:17]** and I got like heads, tails, heads, heads, heads, tails, tails, whatever.

**[2:08:18 – 2:08:18]** Okay?

**[2:08:20 – 2:08:28]** So, P of D given theta is very easy to define.

**[2:08:29 – 2:08:32]** It directly follows from just the model itself.

**[2:08:32 – 2:08:37]** I just need one additional assumption, which is, by the way, very important.

**[2:08:37 – 2:08:41]** It's true throughout the whole machine learning in every model, it works.

**[2:08:42 – 2:08:46]** I need an assumption of conditional independence.

**[2:08:47 – 2:08:48]** We didn't talk about that, right?

**[2:08:48 – 2:08:55]** So, independence is like this, and conditional independence is when, let's say,

**[2:08:55 – 2:09:01]** X and Y are conditionally independent given Z if this holds, right?

**[2:09:01 – 2:09:05]** So, this is conditional independence, conditional.

**[2:09:07 – 2:09:16]** So, we need the assumption that different data points are conditionally independent given the parameters.

**[2:09:16 – 2:09:21]** And again, it sounds very complicated, very messy, but it's very natural.

**[2:09:21 – 2:09:28]** So, like, if I already know what is the probability of heads, then different coin tosses are independent.

**[2:09:29 – 2:09:34]** I toss the coin again, and again, I get the same probability of heads.

**[2:09:34 – 2:09:36]** That's the basic assumption, right?

**[2:09:37 – 2:09:51]** So, in this case, it means that P of D given theta is decomposed into P of, like, D1 given theta times P of D2 given theta, blah, blah, blah, times P of Dn given theta.

**[2:09:53 – 2:09:56]** And what is P of D1, D2, blah, blah, blah, given theta?

**[2:09:57 – 2:10:03]** It's the probability of one outcome, of one sample in the data set.

**[2:10:03 – 2:10:09]** One sample in the data set is one coin toss, either heads or tails.

**[2:10:11 – 2:10:16]** So this is our P of small d given theta, right?

**[2:10:16 – 2:10:24]** Actually, to make it formally correct, let me just put theta here from the very beginning.

**[2:10:24 – 2:10:26]** Why not, right?

**[2:10:26 – 2:10:30]** So this is like theta is the probability of heads.

**[2:10:30 – 2:10:34]** So what is the probability of heads given that theta is the probability of heads?

**[2:10:34 – 2:10:34]** It's theta.

**[2:10:35 – 2:10:39]** What is the probability of tails given that the probability of heads is theta?

**[2:10:39 – 2:10:41]** It's one minus theta, right?

**[2:10:42 – 2:10:51]** So over here, every one of these small d's is either heads or tails, right?

**[2:10:52 – 2:10:57]** And, okay, let's work through an example.

**[2:10:57 – 2:10:59]** So let's say that this is my data set.

**[2:11:00 – 2:11:05]** So d is heads, tails, heads, heads, heads, tails, tails.

**[2:11:05 – 2:11:09]** What is p of d given theta then?

**[2:11:09 – 2:11:10]** Can you tell me?

**[2:11:18 – 2:11:24]** The actual number?

**[2:11:24 – 2:11:26]** Well, not the number, the formula.

**[2:11:27 – 2:11:32]** The probability of heads given theta multiplied by

**[2:11:32 – 2:11:38]** the probability of tails given theta and so on.

**[2:11:38 – 2:11:39]** And so on.

**[2:11:39 – 2:11:39]** Okay.

**[2:11:40 – 2:11:42]** And what is it?

**[2:11:45 – 2:11:48]** We know what is the probability of heads and tails.

**[2:11:48 – 2:11:55]** It is theta to the power of number of heads that you perceived.

**[2:11:55 – 2:11:56]** Okay.

**[2:11:56 – 2:11:57]** Let's say 4.

**[2:11:58 – 2:12:01]** 1 minus theta to the power of...

**[2:12:01 – 2:12:04]** Number of tails.

**[2:12:04 – 2:12:06]** Number of tails or n minus number of heads.

**[2:12:07 – 2:12:07]** Right.

**[2:12:07 – 2:12:07]** Right.

**[2:12:08 – 2:12:08]** Exactly.

**[2:12:08 – 2:12:12]** So, and this is the likelihood.

**[2:12:13 – 2:12:13]** Okay.

**[2:12:15 – 2:12:19]** So, this is basically always the case in machine learning.

**[2:12:20 – 2:12:21]** The likelihood is easy.

**[2:12:22 – 2:12:22]** The likelihood is...

**[2:12:23 – 2:12:24]** Well, okay, maybe it's not easy.

**[2:12:25 – 2:12:26]** It may be a very difficult, complicated formula.

**[2:12:27 – 2:12:30]** But the likelihood is like our model itself.

**[2:12:31 – 2:12:37]** When I say we define a machine learning model, usually what it means is we define the likelihood.

**[2:12:37 – 2:12:43]** We define the assumptions that let us write down this kind of formula.

**[2:12:45 – 2:12:47]** So for the coin, what were the assumptions?

**[2:12:47 – 2:12:51]** There was the assumption, well, not the assumption, the model of the process.

**[2:12:52 – 2:12:53]** There are two outcomes.

**[2:12:53 – 2:12:55]** They are mutually exclusive.

**[2:12:56 – 2:12:58]** One of them has probability theta.

**[2:12:58 – 2:13:02]** The other correspondingly has probability 1 minus theta.

**[2:13:02 – 2:13:08]** And this basic assumption that they are conditionally independent given theta, which is always the case in machine learning.

**[2:13:08 – 2:13:14]** So this is the likelihood of a coin for you.

**[2:13:14 – 2:13:18]** And what do we want to do with that in machine learning?

**[2:13:19 – 2:13:22]** Well, there are several things we can do.

**[2:13:22 – 2:13:28]** But while we only have the likelihood, the only thing we can do with the likelihood is try to maximize it.

**[2:13:29 – 2:13:39]** So the first type of optimization problems that arise is the first type of tasks that we solve in machine learning

**[2:13:39 – 2:13:45]** is finding the maximum likelihood hypothesis.

**[2:13:48 – 2:13:56]** Like theta ML, let's say, is the theta that maximizes P of D given theta.

**[2:13:58 – 2:13:58]** Right.

**[2:14:00 – 2:14:02]** Okay.

**[2:14:02 – 2:14:04]** Let's do it for the coin.

**[2:14:06 – 2:14:07]** Okay.

**[2:14:07 – 2:14:10]** So let's maybe not work with the specific numbers 4 and 3.

**[2:14:10 – 2:14:11]** It doesn't make much sense.

**[2:14:11 – 2:14:23]** Let's say, in general, we have our data set is N heads and M tails, right?

**[2:14:23 – 2:14:28]** So we have P of D given theta, just like you said, you already said it.

**[2:14:28 – 2:14:35]** It's theta to the power number of heads and 1 minus theta to the power number of tails.

**[2:14:36 – 2:14:40]** So how do you maximize it with respect to theta?

**[2:14:41 – 2:14:45]** How do you maximize stuff?

**[2:14:55 – 2:15:03]** Yeah, it sounds very difficult, but okay, in this case, it's going to be pretty easy.

**[2:15:03 – 2:15:08]** So let's take the derivative, okay, D likelihood over D theta.

**[2:15:09 – 2:15:10]** Can you tell me the derivative?

**[2:15:18 – 2:15:22]** Come on, guys, you can do it.

**[2:15:23 – 2:15:24]** Derivative of a polynomial.

**[2:15:25 – 2:15:41]** Let me try N multiplied by theta N minus 1 minus theta N power N.

**[2:15:42 – 2:15:43]** You forgot.

**[2:15:43 – 2:15:48]** Yeah, yeah, yeah.

**[2:15:48 – 2:15:54]** Right, so first the derivative of the first factor, right, times the second factor, then?

**[2:15:55 – 2:15:58]** Minus theta N power N.

**[2:15:59 – 2:16:00]** Oh, sorry.

**[2:16:00 – 2:16:01]** Y minus.

**[2:16:02 – 2:16:03]** Yeah, you're right, you're right.

**[2:16:03 – 2:16:06]** And 1 minus theta N minus 1.

**[2:16:06 – 2:16:08]** Okay, did you forget anything else?

**[2:16:08 – 2:16:09]** Or did I forget it?

**[2:16:10 – 2:16:10]** You said it.

**[2:16:12 – 2:16:13]** What's missing?

**[2:16:16 – 2:16:17]** M, yeah.

**[2:16:19 – 2:16:20]** Okay.

**[2:16:21 – 2:16:24]** Okay, and now we equate it to 0, right?

**[2:16:24 – 2:16:29]** So, let's not waste time on asking you to collect the terms.

**[2:16:29 – 2:16:31]** That's too easy for you.

**[2:16:31 – 2:16:36]** So, we can put this outside the brackets, right?

**[2:16:36 – 2:16:42]** And in the brackets, we have N times 1 minus theta minus M times theta.

**[2:16:43 – 2:16:46]** And that is equal to 0.

**[2:16:47 – 2:16:54]** So, in here, we have like N minus N plus M times theta.

**[2:16:54 – 2:16:57]** Okay.

**[2:16:59 – 2:17:12]** And here, and then we get the roots of this equation, which are theta equals 0, theta equals 1, and also theta equals N divided by N plus M.

**[2:17:14 – 2:17:14]** Okay.

**[2:17:14 – 2:17:18]** So, the first question, it's an easy question.

**[2:17:19 – 2:17:22]** The first easy question is, what's wrong with 0 and 1?

**[2:17:23 – 2:17:25]** What's wrong with 0 and 1?

**[2:17:25 – 2:17:26]** Why is it not the maximum?

**[2:17:29 – 2:17:38]** This is like obvious solutions.

**[2:17:41 – 2:17:44]** Why can't obvious solutions be correct?

**[2:17:45 – 2:17:51]** It could be correct, but if we have only tails and only heads.

**[2:17:51 – 2:17:52]** Well, yeah, okay, sure.

**[2:17:52 – 2:17:54]** But in this case, let's say we have both.

**[2:17:55 – 2:17:59]** When we talked about how we are finding other solutions,

**[2:18:00 – 2:18:02]** I said to check second-order conditions.

**[2:18:02 – 2:18:06]** If we do it, we'll find out that it is actually minimums and perfect solutions.

**[2:18:06 – 2:18:07]** Yeah, that's true.

**[2:18:08 – 2:18:09]** That's true.

**[2:18:09 – 2:18:11]** Let's not check the second-order conditions.

**[2:18:11 – 2:18:12]** That's too much work.

**[2:18:12 – 2:18:19]** Let's just cheat our way through it and notice that theta equals zero and theta equals

**[2:18:19 – 2:18:22]** to one give you zero likelihood, right?

**[2:18:23 – 2:18:27]** And if they give you zero likelihood, then obviously it's not the maximum because in

**[2:18:27 – 2:18:29]** between you get positive likelihood.

**[2:18:29 – 2:18:33]** So that's obviously minimum, not maximum.

**[2:18:33 – 2:18:34]** It doesn't count.

**[2:18:35 – 2:18:39]** And this leaves us this guy, right?

**[2:18:39 – 2:18:43]** So we got our first result about the coin, hooray.

**[2:18:43 – 2:18:49]** We have the maximum likelihood hypothesis, which is n divided by n plus m.

**[2:18:51 – 2:18:52]** Okay, so far so good.

**[2:18:53 – 2:18:58]** And this is probably what, I don't know, your first class on probability theory would tell.

**[2:18:59 – 2:19:03]** If you have a coin, you want to learn its parameter, you toss the coin,

**[2:19:04 – 2:19:08]** you divide the number of heads by the number of experiments of coin tosses,

**[2:19:08 – 2:19:11]** and you get your estimate for the probability.

**[2:19:11 – 2:19:13]** Completely correct.

**[2:19:13 – 2:19:14]** This is the maximum likelihood hypothesis.

**[2:19:16 – 2:19:27]** Again, if you recall your probability classes, you will know that in many cases,

**[2:19:29 – 2:19:34]** or at least in, I mean, I think in modern textbooks, they do it already differently,

**[2:19:35 – 2:19:40]** but in old textbooks like Feller on probability, some classical textbooks,

**[2:19:40 – 2:19:44]** you would get probability kind of introduced in this way.

**[2:19:44 – 2:19:50]** You would get probability introduced as, well, there is a system that gives you a random result,

**[2:19:50 – 2:19:56]** and then you run it infinitely many times, and you get some outcomes.

**[2:19:57 – 2:20:01]** You count how many outcomes you have, you divide by the total number of outcomes,

**[2:20:02 – 2:20:06]** and as the total number gets to infinity, this fraction gets to the probability.

**[2:20:07 – 2:20:13]** And that's kind of the definition of probability from some standpoint.

**[2:20:13 – 2:20:17]** And, of course, for a coin, it works perfectly.

**[2:20:17 – 2:20:19]** There is no catch here.

**[2:20:19 – 2:20:24]** Indeed, if you keep tossing the coin and you keep getting results,

**[2:20:24 – 2:20:27]** this fraction will not oscillate between 0 and 1.

**[2:20:27 – 2:20:30]** It will converge to the probability of heads.

**[2:20:31 – 2:20:33]** Everything is completely true.

**[2:20:35 – 2:20:36]** But here is a question.

**[2:20:37 – 2:20:40]** Here is a more interesting question for you.

**[2:20:41 – 2:20:42]** So let's say this is a coin.

**[2:20:43 – 2:20:44]** It has two sides.

**[2:20:44 – 2:20:47]** I can toss it and let's say...

**[2:20:47 – 2:20:50]** Okay, I was showing to you something, but let's forget about it.

**[2:20:50 – 2:20:53]** Let's say this is the first time I tossed this coin ever.

**[2:20:53 – 2:20:56]** I just took it out of my purse.

**[2:20:57 – 2:21:00]** That's the first time I ever encountered this coin.

**[2:21:01 – 2:21:02]** And let's say I toss it.

**[2:21:02 – 2:21:03]** Let's do it.

**[2:21:06 – 2:21:07]** Okay, I got tails.

**[2:21:08 – 2:21:13]** So at this point, what is my data set?

**[2:21:14 – 2:21:18]** My data set is just tails.

**[2:21:19 – 2:21:22]** What is my likelihood function?

**[2:21:22 – 2:21:28]** My likelihood function is 1 minus theta, right?

**[2:21:30 – 2:21:33]** What is the maximum likelihood hypothesis for this?

**[2:21:34 – 2:21:37]** Where is this function maximized?

**[2:21:41 – 2:21:49]** Well, there is a, first of all, there is an interesting formal problem here in that,

**[2:21:49 – 2:21:51]** well, now I just have a linear function.

**[2:21:51 – 2:21:53]** It goes to infinity.

**[2:21:54 – 2:21:58]** There is, I mean, there is no maximum, no minimum.

**[2:21:58 – 2:22:03]** Basically, if I just look at it formally and forget that it's a coin,

**[2:22:04 – 2:22:07]** theta ML should be like negative infinity, right?

**[2:22:09 – 2:22:12]** In a way, it's true.

**[2:22:14 – 2:22:14]** In a way, it's true.

**[2:22:15 – 2:22:20]** This formula and the likelihood function indeed does not care that theta is a coin,

**[2:22:20 – 2:22:22]** that theta is a probability, right?

**[2:22:22 – 2:22:27]** So there is nothing in this function that says, oh, theta should be from zero to one, right?

**[2:22:27 – 2:22:32]** So we have to kind of introduce it, impose it as a constraint.

**[2:22:32 – 2:22:35]** So far, kind of arbitrary, but okay, let's do that.

**[2:22:36 – 2:22:37]** Let's do that.

**[2:22:37 – 2:22:43]** Let's say we know that our theta is a probability, so it should be between zero and one.

**[2:22:44 – 2:22:47]** Then what is the maximum likelihood hypothesis between zero and one?

**[2:22:48 – 2:22:48]** Tell me.

**[2:22:52 – 2:22:59]** If we make it zero, right?

**[2:22:59 – 2:22:59]** Yeah.

**[2:23:00 – 2:23:04]** So now the maximum likelihood hypothesis is exactly zero.

**[2:23:06 – 2:23:07]** The math checks out.

**[2:23:07 – 2:23:08]** It's correct.

**[2:23:08 – 2:23:10]** I mean, it's very hard to make a mistake here.

**[2:23:10 – 2:23:12]** But what does it actually mean?

**[2:23:13 – 2:23:14]** Like, what's my conclusion?

**[2:23:14 – 2:23:15]** What did I learn?

**[2:23:16 – 2:23:17]** I took a coin.

**[2:23:18 – 2:23:20]** Let's say it's a real coin I took out of pocket.

**[2:23:21 – 2:23:23]** And I tossed it once.

**[2:23:24 – 2:23:24]** I got tails.

**[2:23:25 – 2:23:31]** And now my conclusion is that I will keep getting tails always.

**[2:23:32 – 2:23:36]** That doesn't make any sense, right?

**[2:23:36 – 2:23:39]** I mean, even if I didn't know about coins,

**[2:23:40 – 2:23:45]** like, I kind of have this intuition that coins are approximately fair, right?

**[2:23:46 – 2:23:48]** So theta should be something like one half.

**[2:23:48 – 2:23:49]** Probably not exactly.

**[2:23:49 – 2:23:51]** There is nothing exact in this world.

**[2:23:51 – 2:23:53]** Something nearby, right?

**[2:23:54 – 2:23:56]** But even if I did not have this intuition,

**[2:23:56 – 2:23:58]** if I didn't know anything about coins,

**[2:23:58 – 2:24:01]** still, I mean, come on, I have two options,

**[2:24:02 – 2:24:03]** and I made one experiment.

**[2:24:04 – 2:24:07]** Obviously, I will get one of the options, right?

**[2:24:07 – 2:24:08]** There is no other way.

**[2:24:09 – 2:24:10]** So, like, after one experiment,

**[2:24:10 – 2:24:14]** my maximum likelihood hypothesis will always be either zero or one,

**[2:24:15 – 2:24:16]** depending on what I got,

**[2:24:17 – 2:24:21]** which means that I should always conclude

**[2:24:21 – 2:24:23]** that I will keep getting just one result.

**[2:24:23 – 2:24:26]** That doesn't sound correct.

**[2:24:28 – 2:24:32]** That doesn't sound like a conclusion that we should actually make, right?

**[2:24:33 – 2:24:35]** So what's missing?

**[2:24:35 – 2:24:35]** What's wrong?

**[2:24:36 – 2:24:38]** What do you think is wrong here?

**[2:24:40 – 2:24:41]** The math is correct.

**[2:24:41 – 2:24:43]** It's indeed the maximum likelihood hypothesis.

**[2:24:44 – 2:24:45]** But it's not the...

**[2:24:45 – 2:24:46]** More experiments are needed?

**[2:24:47 – 2:24:48]** More experiments are needed.

**[2:24:48 – 2:24:49]** Good.

**[2:24:49 – 2:24:50]** Yes.

**[2:24:50 – 2:24:55]** Of course, if I want to, like, make a more precise estimate of theta,

**[2:24:55 – 2:24:57]** I will need more experiments.

**[2:24:57 – 2:24:57]** That is correct.

**[2:24:57 – 2:25:00]** And, again, your statistics classes will probably tell you

**[2:25:00 – 2:25:02]** how many experiments you need.

**[2:25:03 – 2:25:03]** Right.

**[2:25:04 – 2:25:06]** But here is the thing.

**[2:25:06 – 2:25:07]** Here is the important thing.

**[2:25:09 – 2:25:13]** There is, as I said before I started talking about this example,

**[2:25:13 – 2:25:15]** that there is no difference in the limit.

**[2:25:16 – 2:25:20]** So in the limit, the maximum likelihood hypothesis

**[2:25:20 – 2:25:23]** will get to the true value of theta

**[2:25:23 – 2:25:26]** as n and m go to infinity,

**[2:25:26 – 2:25:28]** and everything will check out,

**[2:25:28 – 2:25:31]** and all that I am telling you right now will not matter.

**[2:25:32 – 2:25:39]** So if we have this possibly infinite series of experiments

**[2:25:39 – 2:25:42]** if we can just toss the coin again and again,

**[2:25:43 – 2:25:44]** there is no problem,

**[2:25:45 – 2:25:46]** and we don't need to have this discussion.

**[2:25:46 – 2:25:47]** That's fine.

**[2:25:48 – 2:25:51]** But the thing is, in practice,

**[2:25:51 – 2:25:53]** we do not live in this limit.

**[2:25:54 – 2:25:57]** In practice, when we are talking about machine learning,

**[2:25:58 – 2:26:01]** we start with some data set, right?

**[2:26:01 – 2:26:04]** We have as much data as we have,

**[2:26:05 – 2:26:06]** and usually in machine learning,

**[2:26:06 – 2:26:09]** there is no easy way to get more data.

**[2:26:10 – 2:26:13]** If there was, then a lot of problems would be much easier.

**[2:26:14 – 2:26:17]** So in machine learning,

**[2:26:17 – 2:26:21]** we have our D,

**[2:26:21 – 2:26:24]** and we cannot really change it, right?

**[2:26:25 – 2:26:27]** And I mean, okay, in practice,

**[2:26:27 – 2:26:31]** maybe we can do some project to get additional data, yes,

**[2:26:31 – 2:26:34]** but when we are actually doing machine learning,

**[2:26:34 – 2:26:37]** when we do the data processing part,

**[2:26:37 – 2:26:39]** we have to assume that this is the data set that we are given.

**[2:26:40 – 2:26:43]** And even more importantly here,

**[2:26:44 – 2:26:46]** in practice, in real life,

**[2:26:48 – 2:26:53]** we will never get quite enough data.

**[2:26:53 – 2:26:55]** This is an important point.

**[2:26:55 – 2:26:56]** I want to make it here.

**[2:26:57 – 2:27:00]** Like suppose that I have,

**[2:27:00 – 2:27:03]** so if I just have a coin in this example

**[2:27:03 – 2:27:07]** and I have this ability to collect more data,

**[2:27:08 – 2:27:11]** then sure, I can toss it once, twice,

**[2:27:11 – 2:27:13]** 10 times, 20 times, 50 times.

**[2:27:13 – 2:27:14]** And after I've tossed it 50 times,

**[2:27:15 – 2:27:22]** I can be pretty sure in my results about the coin.

**[2:27:22 – 2:27:24]** Like the confidence interval will be quite small,

**[2:27:24 – 2:27:25]** et cetera, et cetera.

**[2:27:26 – 2:27:27]** Statistics will tell you.

**[2:27:28 – 2:27:32]** But that's not what happens with real-world problems.

**[2:27:33 – 2:27:36]** So, for example,

**[2:27:37 – 2:27:42]** suppose that you are building a language model.

**[2:27:43 – 2:27:45]** That sounds like a very difficult example,

**[2:27:45 – 2:27:47]** but in fact, it's one of the simplest

**[2:27:47 – 2:27:49]** and nearest to our intuition.

**[2:27:50 – 2:27:52]** Suppose that we are building a language model.

**[2:27:52 – 2:27:54]** So it's a model that has some kind of text.

**[2:27:55 – 2:27:57]** Then there is this black box,

**[2:27:57 – 2:28:00]** and then it produces the next token,

**[2:28:00 – 2:28:03]** the next word in this text, right?

**[2:28:05 – 2:28:08]** Suppose that I am OpenAI

**[2:28:08 – 2:28:14]** and the transformer has been introduced quite recently,

**[2:28:14 – 2:28:15]** and here I am.

**[2:28:16 – 2:28:18]** I just made my very first GPT model,

**[2:28:18 – 2:28:21]** which is like half of a transformer, right?

**[2:28:21 – 2:28:25]** So I train it on some text data set.

**[2:28:25 – 2:28:27]** I get some pretty good language model.

**[2:28:30 – 2:28:32]** Then what do I do next?

**[2:28:32 – 2:28:36]** I say, well, all right, so let's see how this scales up.

**[2:28:37 – 2:28:38]** Maybe I can get more data.

**[2:28:39 – 2:28:41]** And indeed, compared to the first GPT,

**[2:28:42 – 2:28:44]** how it was trained, it's easy to get more data.

**[2:28:45 – 2:28:46]** Let's just scrape it off the internet.

**[2:28:47 – 2:28:49]** Let's get some more texts, okay?

**[2:28:49 – 2:28:52]** So I extend my data set,

**[2:28:52 – 2:28:57]** and now I have like lots of additional data sets,

**[2:28:57 – 2:28:58]** and I have lots of text.

**[2:28:58 – 2:29:02]** I have a huge other data set.

**[2:29:04 – 2:29:06]** When I have this huge data set

**[2:29:06 – 2:29:08]** that's like orders of magnitude larger

**[2:29:08 – 2:29:10]** than the one used here,

**[2:29:11 – 2:29:15]** it maybe indeed means

**[2:29:15 – 2:29:19]** that now I don't care about this Bayesian stuff.

**[2:29:19 – 2:29:21]** I don't care about this effect.

**[2:29:21 – 2:29:23]** I can go back and I can train my GPT

**[2:29:23 – 2:29:24]** on this huge data set,

**[2:29:24 – 2:29:27]** and it will be like almost in the limit.

**[2:29:27 – 2:29:28]** It will be fine.

**[2:29:29 – 2:29:31]** But that's not what happens, right?

**[2:29:31 – 2:29:33]** It's not like I collect more data

**[2:29:33 – 2:29:37]** to go back to my GPT model

**[2:29:37 – 2:29:39]** and train it even better a little bit.

**[2:29:40 – 2:29:40]** No.

**[2:29:41 – 2:29:43]** When I collect orders of magnitude more data,

**[2:29:44 – 2:29:47]** I go to a larger model, right?

**[2:29:47 – 2:29:52]** I go to GPT-2 that has more parameters.

**[2:29:54 – 2:29:56]** So GPT had that many parameters,

**[2:29:56 – 2:29:58]** actually, I forget how many.

**[2:29:58 – 2:30:01]** And GPT-2 had like an order of magnitude more.

**[2:30:01 – 2:30:04]** It had something like 150 million parameters

**[2:30:04 – 2:30:05]** in GPT-1, I don't remember.

**[2:30:08 – 2:30:10]** So in actual practice,

**[2:30:10 – 2:30:13]** when you are solving a difficult task

**[2:30:13 – 2:30:14]** like predicting the next token

**[2:30:14 – 2:30:18]** or identifying cats and dogs and images or whatever,

**[2:30:19 – 2:30:21]** you never have enough data.

**[2:30:21 – 2:30:22]** It's impossible.

**[2:30:23 – 2:30:26]** Because whenever you have enough data for your model,

**[2:30:27 – 2:30:29]** in practice, it means that your model is too weak.

**[2:30:30 – 2:30:33]** It means that you should switch to a bigger model

**[2:30:33 – 2:30:36]** for which you now don't have enough data.

**[2:30:37 – 2:30:39]** But it still will work better.

**[2:30:41 – 2:30:45]** So I know I haven't proven that formally to you.

**[2:30:45 – 2:30:48]** And maybe if we have time,

**[2:30:48 – 2:30:50]** maybe we'll discuss scaling loss and stuff like that.

**[2:30:50 – 2:30:55]** But the point is, in machine learning,

**[2:30:55 – 2:31:00]** unless you have some very specific, very simple,

**[2:31:00 – 2:31:03]** very well-defined problem, like let's learn a coin toss

**[2:31:03 – 2:31:09]** or let's learn linear regression, right?

**[2:31:09 – 2:31:17]** So you have points and you want to represent them

**[2:31:17 – 2:31:20]** with the linear dependence, right?

**[2:31:20 – 2:31:21]** That's linear regression.

**[2:31:22 – 2:31:26]** You can maybe get more data for this linear law.

**[2:31:27 – 2:31:29]** You can get additional points.

**[2:31:30 – 2:31:33]** But unless you have like some very good reason

**[2:31:33 – 2:31:38]** to know that this is going to be definitely linear,

**[2:31:38 – 2:31:40]** unless it's, I don't know, a law of physics

**[2:31:40 – 2:31:42]** and it's supposed to be linear

**[2:31:42 – 2:31:44]** and you're just getting more data for it.

**[2:31:44 – 2:31:47]** So unless you are in some very special situation,

**[2:31:48 – 2:31:49]** if you have significantly more data,

**[2:31:49 – 2:31:52]** it will be better to go to a larger model,

**[2:31:52 – 2:31:54]** I don't know, from linear to polynomial, for example.

**[2:31:55 – 2:31:57]** And it will be a better fit,

**[2:31:57 – 2:32:00]** it will not overfit since you have more data, etc.

**[2:32:00 – 2:32:02]** We'll discuss it when we get to linear regression.

**[2:32:04 – 2:32:07]** So usually in machine learning,

**[2:32:07 – 2:32:10]** we operate on the frontier of what's possible.

**[2:32:11 – 2:32:13]** So the data is usually fixed.

**[2:32:13 – 2:32:15]** We can change the model,

**[2:32:15 – 2:32:18]** we can select the model, it's in our hands.

**[2:32:18 – 2:32:21]** And usually you want to choose a model

**[2:32:21 – 2:32:25]** in such a way that it's barely enough data to train.

**[2:32:25 – 2:32:29]** So we are always in practice in a situation

**[2:32:29 – 2:32:32]** where data is scarce, where it's not enough.

**[2:32:33 – 2:32:35]** So your answer is correct.

**[2:32:35 – 2:32:37]** Indeed, one toss is not enough

**[2:32:37 – 2:32:41]** to learn the probability of a coin toss.

**[2:32:42 – 2:32:45]** But let's say that's all we have.

**[2:32:45 – 2:32:48]** What can we say about the coin still?

**[2:32:49 – 2:32:54]** And definitely it shouldn't be this, right?

**[2:32:54 – 2:32:56]** So maybe we can give up and say,

**[2:32:56 – 2:32:57]** okay, we can say nothing,

**[2:32:58 – 2:33:00]** but we definitely shouldn't be concluding

**[2:33:00 – 2:33:03]** that from now on,

**[2:33:03 – 2:33:05]** the coin will always lend tails.

**[2:33:06 – 2:33:07]** That's definitely wrong.

**[2:33:08 – 2:33:10]** So what's missing?

**[2:33:11 – 2:33:12]** What else is missing?

**[2:33:12 – 2:33:17]** What is the component

**[2:33:17 – 2:33:19]** that will get us from this zero?

**[2:33:20 – 2:33:21]** What is the component

**[2:33:21 – 2:33:23]** that will allow us to say that,

**[2:33:24 – 2:33:26]** oh, okay, so the maximum likelihood hypothesis is this,

**[2:33:27 – 2:33:35]** but actually maybe one data point

**[2:33:35 – 2:33:37]** is not enough to really shift

**[2:33:37 – 2:33:40]** my beliefs about the coin.

**[2:33:40 – 2:33:44]** Well, the missing piece,

**[2:33:45 – 2:33:48]** the missing part here is my beliefs.

**[2:33:50 – 2:33:54]** And if you go back to the best row here,

**[2:33:54 – 2:33:57]** you will see that we have only talked

**[2:33:57 – 2:34:00]** about the likelihood, right?

**[2:34:00 – 2:34:02]** And what we actually want

**[2:34:02 – 2:34:06]** is the posterior distribution over here.

**[2:34:08 – 2:34:10]** And to get from the likelihood to the posterior,

**[2:34:10 – 2:34:12]** so like the posterior in this case,

**[2:34:12 – 2:34:13]** what does it mean?

**[2:34:13 – 2:34:16]** What is its tangible meaning?

**[2:34:16 – 2:34:18]** It's what do I think,

**[2:34:19 – 2:34:22]** what is my belief about the probability of heads

**[2:34:22 – 2:34:26]** after I got my data point,

**[2:34:27 – 2:34:30]** after I've tossed it once and got tails, okay?

**[2:34:30 – 2:34:34]** And the likelihood is how likely it was to get tails,

**[2:34:34 – 2:34:36]** given data.

**[2:34:36 – 2:34:39]** And to get to the posterior,

**[2:34:39 – 2:34:42]** the missing piece is the prior, right?

**[2:34:42 – 2:34:46]** So it's what did I believe about the coin?

**[2:34:47 – 2:34:49]** What did I think about theta

**[2:34:49 – 2:34:52]** before I started even tossing it,

**[2:34:52 – 2:34:54]** before any data came in?

**[2:34:55 – 2:34:56]** That's the missing piece.

**[2:34:57 – 2:34:58]** And in this case, it's pretty important.

**[2:34:58 – 2:35:04]** So let's think we will be able to complete this example.

**[2:35:05 – 2:35:08]** So let's go to the second part of this example,

**[2:35:10 – 2:35:11]** to the prior distribution.

**[2:35:14 – 2:35:18]** Prior distribution, P of theta for the coin toss.

**[2:35:19 – 2:35:21]** What does it mean?

**[2:35:21 – 2:35:22]** What kind of object is it?

**[2:35:22 – 2:35:25]** Well, here is the thing.

**[2:35:26 – 2:35:31]** P of theta is a distribution on the parameters.

**[2:35:32 – 2:35:34]** In this case, on one parameter, right?

**[2:35:35 – 2:35:39]** So that's why, unfortunately, in machine learning,

**[2:35:39 – 2:35:44]** you cannot limit yourself to discrete probability theory.

**[2:35:44 – 2:35:46]** So even when we are tossing a coin,

**[2:35:47 – 2:35:51]** it looks like the most discrete probabilistic object imaginable,

**[2:35:51 – 2:35:54]** only two outcomes, only one probability, et cetera.

**[2:35:54 – 2:35:57]** Still, as soon as we do learning,

**[2:35:58 – 2:36:00]** we get a continuous distribution.

**[2:36:01 – 2:36:03]** So P of theta is a continuous distribution.

**[2:36:03 – 2:36:07]** It's a distribution on the probabilities, right?

**[2:36:07 – 2:36:14]** So let's try to plot something.

**[2:36:16 – 2:36:16]** This is theta.

**[2:36:17 – 2:36:19]** This will be P of theta.

**[2:36:19 – 2:36:24]** And the first property that we definitely need to have

**[2:36:24 – 2:36:28]** is that theta is a probability, right?

**[2:36:28 – 2:36:33]** So the first very firm belief about theta

**[2:36:33 – 2:36:36]** is that it should be between 0 and 1, right?

**[2:36:37 – 2:36:40]** So whatever I think about the coin,

**[2:36:40 – 2:36:42]** whatever I think about its heads or tails probability,

**[2:36:43 – 2:36:46]** I can definitely be sure that theta cannot be negative.

**[2:36:47 – 2:36:48]** So P of theta is 0 over here.

**[2:36:49 – 2:36:51]** And theta cannot be larger than 1.

**[2:36:52 – 2:36:53]** So P of theta is 0 over here.

**[2:36:55 – 2:36:56]** This is P of theta.

**[2:36:58 – 2:37:03]** So by the way, this is the answer

**[2:37:03 – 2:37:09]** to why theta ML is not negative infinity over here.

**[2:37:10 – 2:37:13]** And the answer is theta ML is negative infinity.

**[2:37:13 – 2:37:18]** And that's fine, because then we will take this.

**[2:37:19 – 2:37:23]** So if I have only, so if D is just one tail,

**[2:37:23 – 2:37:28]** then my P of D given theta is 1 minus theta, right?

**[2:37:29 – 2:37:33]** And it's like this straight line over here.

**[2:37:36 – 2:37:42]** So this is, sorry, I'm not good at drawing.

**[2:37:43 – 2:37:46]** I'll do what I can, then I'll show you some nice plots.

**[2:37:47 – 2:37:55]** So this is P of D given theta, and yes, it does go to infinity, definitely.

**[2:37:55 – 2:37:58]** On the left and on the right, and since we want to maximize,

**[2:37:59 – 2:38:01]** it goes to plus infinity over here.

**[2:38:02 – 2:38:09]** But we will multiply this straight line by something which is 0

**[2:38:09 – 2:38:12]** on the left of 0 and on the right of 1.

**[2:38:13 – 2:38:17]** So after we multiply, let's start with the obvious,

**[2:38:17 – 2:38:18]** let's start with the uniform distribution.

**[2:38:19 – 2:38:24]** It's not the uniform distribution, it's just 1 on the interval from 0 to 1.

**[2:38:25 – 2:38:28]** Oh, sorry, the interval is wrong.

**[2:38:29 – 2:38:31]** 1 is here, right?

**[2:38:32 – 2:38:36]** So if we start with the uniform distribution,

**[2:38:37 – 2:38:43]** then after I multiply this P of theta by this straight line,

**[2:38:43 – 2:38:45]** and this is the bias rule here, right?

**[2:38:45 – 2:38:54]** So P of theta given D is proportional to P of theta times P of D given theta.

**[2:38:54 – 2:38:55]** You remember.

**[2:38:55 – 2:39:01]** So what I'm doing is I'm taking P of D given theta, the green straight line.

**[2:39:01 – 2:39:07]** I am taking P of theta, which is this piecewise constant thing,

**[2:39:07 – 2:39:11]** the uniform distribution, the red one, and I am multiplying them.

**[2:39:11 – 2:39:12]** What do I get?

**[2:39:12 – 2:39:14]** I get 0 over here.

**[2:39:15 – 2:39:16]** Then I jump to 1.

**[2:39:16 – 2:39:22]** Then I go along this straight line, and then I get 0 again, right?

**[2:39:23 – 2:39:26]** These two lines are easy to multiply.

**[2:39:27 – 2:39:30]** This is not yet P of theta given D.

**[2:39:30 – 2:39:31]** Why not?

**[2:39:31 – 2:39:32]** Can you tell me why not?

**[2:39:38 – 2:39:42]** Why is the light blue line still not P of theta given D?

**[2:39:46 – 2:39:47]** The denominator?

**[2:39:47 – 2:39:49]** Yeah, the denominator is still missing,

**[2:39:50 – 2:39:53]** and here is an illustration to what I was telling you before.

**[2:39:54 – 2:39:58]** We don't want to get the denominator as some fact

**[2:39:58 – 2:40:00]** about the coin that we want to prove, right?

**[2:40:00 – 2:40:02]** It's just a normalizing constant.

**[2:40:02 – 2:40:05]** So I know that this area is supposed to be 1.

**[2:40:05 – 2:40:07]** Right now, it's not 1.

**[2:40:07 – 2:40:08]** Right now, it's what?

**[2:40:09 – 2:40:13]** What is this area?

**[2:40:19 – 2:40:24]** 1 and 1 half?

**[2:40:25 – 2:40:26]** 1 and 1 half, yeah, sure.

**[2:40:26 – 2:40:29]** It's half of a square of area 1.

**[2:40:29 – 2:40:30]** Right.

**[2:40:30 – 2:40:32]** So it's 1 and 1 half,

**[2:40:33 – 2:40:36]** and so it means that to get the actual distribution,

**[2:40:36 – 2:40:37]** I need to multiply it by 2.

**[2:40:37 – 2:40:38]** That's it.

**[2:40:38 – 2:40:42]** So the actual distribution is 0 here,

**[2:40:42 – 2:40:45]** and, like, twice larger over here.

**[2:40:46 – 2:40:48]** So, yeah, it will span two pages.

**[2:40:49 – 2:40:50]** I hope that's...

**[2:40:50 – 2:40:57]** So this guy is P of theta given D, right?

**[2:40:59 – 2:41:05]** And notice that we didn't actually change much

**[2:41:05 – 2:41:07]** in terms of maximization.

**[2:41:08 – 2:41:08]** Oh, yeah.

**[2:41:10 – 2:41:12]** So, yeah, this is P of...

**[2:41:12 – 2:41:15]** Okay, sorry, we'll get there in a sec.

**[2:41:15 – 2:41:17]** I forgot to say one thing.

**[2:41:17 – 2:41:19]** So, this is P of theta given D

**[2:41:19 – 2:41:25]** for the uniform prior distribution over here, okay?

**[2:41:26 – 2:41:29]** The first remark is,

**[2:41:30 – 2:41:36]** well, the uniform prior is not quite...

**[2:41:36 – 2:41:40]** Sorry, what's the word?

**[2:41:40 – 2:41:42]** The uniform prior is not quite

**[2:41:42 – 2:41:45]** what I really think about coins, right?

**[2:41:45 – 2:41:48]** So, let me draw a separate picture.

**[2:41:49 – 2:41:52]** The uniform prior means that,

**[2:41:52 – 2:41:56]** well, I don't know anything

**[2:41:56 – 2:41:59]** about the probability of heads.

**[2:42:00 – 2:42:02]** So, it could be 0, could be 1,

**[2:42:02 – 2:42:03]** could be 1.5, could be 1.3.

**[2:42:03 – 2:42:04]** It's all equal to me.

**[2:42:07 – 2:42:09]** But in reality, when I take a coin,

**[2:42:09 – 2:42:10]** like a real coin,

**[2:42:10 – 2:42:13]** or even this pseudo coin

**[2:42:13 – 2:42:17]** that is the coaster for my cup of coffee,

**[2:42:18 – 2:42:23]** I kind of expect that it's approximately fair, right?

**[2:42:23 – 2:42:25]** So, in real life,

**[2:42:25 – 2:42:27]** obviously, it's not exactly one-half

**[2:42:27 – 2:42:28]** because it's a physical object,

**[2:42:28 – 2:42:29]** it has imperfections,

**[2:42:30 – 2:42:32]** but in real life,

**[2:42:32 – 2:42:36]** I kind of expect that the probability is close to one-half.

**[2:42:37 – 2:42:41]** So, my actual prior distribution looks,

**[2:42:42 – 2:42:45]** okay, it's still exactly zero on the left and on the right,

**[2:42:45 – 2:42:47]** that's for sure, that's by definition,

**[2:42:47 – 2:42:49]** that's a mathematical fact, not my opinion.

**[2:42:50 – 2:42:54]** But in between, it's probably something like this, right?

**[2:42:54 – 2:42:58]** So, it's probably some bell-shaped curve,

**[2:42:58 – 2:43:03]** that says, well, I think it's approximately fair,

**[2:43:04 – 2:43:07]** maybe not exactly, but it's near one half.

**[2:43:09 – 2:43:12]** That's about where my intuition stops, really.

**[2:43:12 – 2:43:16]** So, I cannot define this curve mathematically, right?

**[2:43:16 – 2:43:18]** Our brains don't work in this way.

**[2:43:18 – 2:43:21]** I can just say that, okay, it's approximately fair,

**[2:43:21 – 2:43:22]** I'm pretty sure of that,

**[2:43:22 – 2:43:28]** but so this should be a pretty high and peaky distribution,

**[2:43:28 – 2:43:31]** but what exactly is the shape of this distribution,

**[2:43:31 – 2:43:32]** I don't know, right?

**[2:43:32 – 2:43:36]** This cannot be a part of my personal intuition.

**[2:43:37 – 2:43:40]** But anyway, we'll get back here,

**[2:43:40 – 2:43:43]** but let's first finish with the uniform thing.

**[2:43:43 – 2:43:49]** So still, let's begin with this not quite realistic uniform prior,

**[2:43:50 – 2:43:51]** not quite realistic for coins,

**[2:43:51 – 2:43:55]** but in other situations, it's a perfectly good prior

**[2:43:55 – 2:43:57]** because it basically just means I don't know anything.

**[2:43:58 – 2:44:00]** So in many situations, it's very reasonable.

**[2:44:00 – 2:44:03]** If it's a new machine learning problem,

**[2:44:04 – 2:44:04]** it has a parameter.

**[2:44:05 – 2:44:06]** I don't know anything about this parameter,

**[2:44:07 – 2:44:09]** but I know it's, let's say, I know it's a probability,

**[2:44:10 – 2:44:11]** so it's from zero to one.

**[2:44:11 – 2:44:14]** A uniform distribution is a great first step, okay?

**[2:44:15 – 2:44:16]** So in many situations,

**[2:44:17 – 2:44:20]** having a uniform P of theta is perfectly reasonable.

**[2:44:20 – 2:44:24]** So I take this uniform P of theta,

**[2:44:24 – 2:44:30]** I multiply it by my likelihood, one minus theta,

**[2:44:30 – 2:44:32]** and I get this pointy triangle,

**[2:44:33 – 2:44:35]** and this pointy triangle,

**[2:44:35 – 2:44:36]** so let me write it down,

**[2:44:37 – 2:44:39]** like P of theta given D,

**[2:44:39 – 2:44:42]** in my case, P of theta given a single tail,

**[2:44:44 – 2:44:49]** it's like 2 times 1 minus theta,

**[2:44:49 – 2:44:52]** if theta is from 0 to 1,

**[2:44:52 – 2:44:55]** and it's 0 otherwise, right?

**[2:44:55 – 2:44:57]** So formally we get this.

**[2:44:59 – 2:45:02]** And the next question,

**[2:45:03 – 2:45:05]** let's go back to the bias rule.

**[2:45:06 – 2:45:10]** We had our first question is,

**[2:45:10 – 2:45:12]** let's maximize the likelihood,

**[2:45:15 – 2:45:16]** our second question,

**[2:45:16 – 2:45:18]** and usually a better one,

**[2:45:18 – 2:45:21]** is let's maximize the posterior

**[2:45:21 – 2:45:23]** with respect to theta.

**[2:45:24 – 2:45:26]** So now that we have a posterior distribution,

**[2:45:27 – 2:45:29]** we can ask what is the,

**[2:45:29 – 2:45:33]** it's called the maximum a posteriori hypothesis.

**[2:45:34 – 2:45:39]** What's the theta that maximizes

**[2:45:39 – 2:45:41]** P of theta given D?

**[2:45:45 – 2:45:46]** And in this case,

**[2:45:46 – 2:45:48]** there is no difference really, right?

**[2:45:48 – 2:45:50]** So if I have a uniform prior,

**[2:45:51 – 2:45:53]** the only thing that I actually did,

**[2:45:53 – 2:45:55]** like formally what I actually did,

**[2:45:55 – 2:46:00]** was I took care of these degenerate solutions, right?

**[2:46:00 – 2:46:03]** So now my prior does say that

**[2:46:03 – 2:46:05]** theta should be between 0 and 1.

**[2:46:06 – 2:46:07]** That's a good thing.

**[2:46:09 – 2:46:12]** But otherwise, I didn't change the shape of the likelihood.

**[2:46:13 – 2:46:14]** I am multiplying it by 1.

**[2:46:15 – 2:46:16]** And then I am renormalizing,

**[2:46:16 – 2:46:17]** but that's just a constant.

**[2:46:18 – 2:46:19]** So the maximum will not change.

**[2:46:20 – 2:46:22]** The maximum will be at the same point, right?

**[2:46:22 – 2:46:36]** So theta, in this case, theta MAP is still N over N plus M, okay?

**[2:46:37 – 2:46:44]** And this sounds like a lot of complicated math.

**[2:46:44 – 2:46:46]** Well, maybe not that complicated,

**[2:46:46 – 2:46:48]** but a lot of math for nothing, right?

**[2:46:48 – 2:46:53]** So we went from maximum likelihood to maximum aposteriori,

**[2:46:54 – 2:46:56]** and we didn't change anything.

**[2:46:56 – 2:46:57]** The answer is the same.

**[2:46:59 – 2:47:02]** Well, that's because our prior was uniform,

**[2:47:03 – 2:47:06]** but even for a uniform prior, something has changed

**[2:47:06 – 2:47:14]** because I have one point left to make in this specific example,

**[2:47:14 – 2:47:15]** then we'll go to the priors.

**[2:47:16 – 2:47:17]** I hope we still have time.

**[2:47:18 – 2:47:26]** In this example, for example,

**[2:47:26 – 2:47:28]** in the example of a coin toss,

**[2:47:28 – 2:47:31]** and this is also a very important concept in machine learning.

**[2:47:32 – 2:47:36]** Today is like this very abstract and introductory lecture.

**[2:47:36 – 2:47:37]** I apologize.

**[2:47:37 – 2:47:39]** I have to begin with something like this.

**[2:47:39 – 2:47:42]** We'll get to neural networks literally tomorrow.

**[2:47:43 – 2:47:47]** But anyway, in this example,

**[2:47:48 – 2:47:51]** what is the end goal of this whole thing?

**[2:47:53 – 2:47:56]** Let's say that this is an actual machine learning problem.

**[2:47:56 – 2:47:58]** Let's say that it's, I mean, it's not,

**[2:47:58 – 2:48:02]** but let's say that it's something like distinguishing cats from dogs or something.

**[2:48:03 – 2:48:11]** So when I am learning the parameters of a machine learning model,

**[2:48:11 – 2:48:13]** what am I really interested in?

**[2:48:13 – 2:48:15]** What is my final goal?

**[2:48:15 – 2:48:16]** This is a very important point.

**[2:48:17 – 2:48:24]** So far, we have been talking about learning something about Theta.

**[2:48:25 – 2:48:31]** So we tried getting Theta ML, maximum likelihood.

**[2:48:31 – 2:48:36]** Now we added the prior, and now we are getting Theta MAP, maximum a posteriori.

**[2:48:37 – 2:48:38]** But that's about Theta.

**[2:48:39 – 2:48:44]** So if I map this discussion to neural networks, it would say,

**[2:48:44 – 2:48:49]** all right, so I have a neural network, Theta is the vector of its weights of the parameters, right?

**[2:48:49 – 2:48:56]** And then I do my learning, and here is, so Theta ML and Theta MAP are like checkpoints of the weights.

**[2:48:58 – 2:49:00]** They are the states of the neural network.

**[2:49:02 – 2:49:09]** But when I phrase it like this, it becomes clear that that's not the final goal of the process, right?

**[2:49:09 – 2:49:16]** If I am training a neural network to distinguish cats from dogs, I don't care what the weights are, right?

**[2:49:16 – 2:49:25]** I mean, I do want to get them, but I want to get them as an intermediate step for the goal, and the goal is distinguish cats from dogs, right?

**[2:49:26 – 2:49:38]** So what we are actually supposed to do, and this is the third part here, and this is true both in machine learning and generally in life, actually.

**[2:49:38 – 2:49:43]** What we are actually supposed to do is to make predictions, right?

**[2:49:44 – 2:49:51]** So, like, philosophically speaking, what does it mean to understand something?

**[2:49:52 – 2:49:58]** Well, it means that you can predict what's going to happen with it, and you can be right more often than chance.

**[2:50:01 – 2:50:06]** It's, I mean, if you haven't thought about this, it's a pretty deep idea.

**[2:50:07 – 2:50:12]** So understanding something doesn't mean rephrasing it in different words.

**[2:50:13 – 2:50:28]** It means phrasing in such a way that you can operationalize it and get to predicting some stuff that you didn't know in such a way that it actually conforms to reality.

**[2:50:30 – 2:50:45]** And here also, in this very simple case, even here, I mean, in the case of a coin, everything is very simple, very small, and very close to each other, so there may seem that there is no difference.

**[2:50:45 – 2:50:53]** So, okay, so what's the difference between predicting heads or tails and learning the probability of heads or tails?

**[2:50:53 – 2:50:54]** It's the same thing.

**[2:50:54 – 2:50:57]** If I get theta more than one half, I will predict heads.

**[2:50:57 – 2:50:59]** If I get theta less than one half, I will predict tails.

**[2:51:00 – 2:51:00]** Isn't that true?

**[2:51:02 – 2:51:05]** Still, there is a difference.

**[2:51:06 – 2:51:07]** Very interesting, but there is.

**[2:51:08 – 2:51:11]** And the predictive distribution in this case, what is it?

**[2:51:11 – 2:51:15]** It's like the probability of heads given the data.

**[2:51:15 – 2:51:19]** It's not in the biased formula.

**[2:51:19 – 2:51:20]** It's the next step.

**[2:51:22 – 2:51:25]** Let me, I don't have space here, I think.

**[2:51:27 – 2:51:33]** Yeah, let me write it formally separately.

**[2:51:33 – 2:51:41]** So I have the biased rule, P of theta given D is P of D given theta times P of theta divided by P of D.

**[2:51:41 – 2:51:55]** But the predictive distribution is the distribution of the next outcome, of the next X or the next Y given X in our learning problem.

**[2:51:55 – 2:52:03]** Like what's, okay, so I have this data, what's the probability that this picture is a cat, for example?

**[2:52:06 – 2:52:07]** X given D.

**[2:52:09 – 2:52:14]** And P of X given D does not contain theta at all.

**[2:52:14 – 2:52:16]** I don't care about theta here.

**[2:52:16 – 2:52:19]** I care about the next prediction, solving the problem.

**[2:52:21 – 2:52:26]** But it so happens that I can't get to this distribution other than introduce theta, right?

**[2:52:26 – 2:52:33]** So the only way to actually compute this is to say, ah, okay, so I don't know about P of X given D,

**[2:52:34 – 2:52:38]** but maybe I know something about P of X and theta given D.

**[2:52:38 – 2:52:42]** And here is this joint probability.

**[2:52:43 – 2:52:46]** And here is this marginalization process, right?

**[2:52:46 – 2:52:49]** We are integrating the joint probability to get P of X.

**[2:52:50 – 2:52:55]** And now for this joint probability, yes, we can actually reduce it to what we know.

**[2:52:55 – 2:53:05]** So it's P of X given theta and D times P of theta given D, D theta.

**[2:53:06 – 2:53:14]** And now P of theta given D is our posterior, right?

**[2:53:14 – 2:53:19]** And P of X given theta and D, well, we have to recall our assumption.

**[2:53:19 – 2:53:29]** We had this assumption which always holds that data points are independent if you know the parameters, if you know the full model.

**[2:53:30 – 2:53:35]** So here also, if I already know the full model, then D doesn't matter, right?

**[2:53:35 – 2:53:43]** If I already know what is the probability of heads, then it doesn't matter what were the results of the coin in the past.

**[2:53:43 – 2:53:46]** If I know the probability, it will stay the same.

**[2:53:46 – 2:53:51]** So here, the first part is just P of X given theta.

**[2:53:51 – 2:53:54]** It's the likelihood of this single point.

**[2:53:57 – 2:53:59]** And that's it.

**[2:53:59 – 2:54:00]** So this is the predictive distribution.

**[2:54:00 – 2:54:09]** And in this case, even for this uniform prior, it will be different from just predicting zero.

**[2:54:10 – 2:54:11]** That's the interesting part.

**[2:54:11 – 2:54:22]** So P of heads given D, in our case, is P of heads given theta times P of theta given D, D theta, right?

**[2:54:22 – 2:54:27]** And it's like, what is P of heads given D?

**[2:54:28 – 2:54:30]** Well, just theta, right?

**[2:54:31 – 2:54:35]** It's the probability of heads given that the probability of heads is theta.

**[2:54:35 – 2:54:38]** That's the likelihood of one positive outcome.

**[2:54:39 – 2:54:47]** And P of theta given D, we actually, I think we didn't write it completely, but we did write the likelihood, right?

**[2:54:47 – 2:54:48]** So this is it.

**[2:54:48 – 2:55:03]** And P of theta given D is proportional to P of D given theta times P of theta.

**[2:55:04 – 2:55:15]** So it's proportional to like theta to the n 1 minus theta to the m on 0, 1 and 0 everywhere else, right?

**[2:55:15 – 2:55:26]** So we take the likelihood, we multiply it by the uniform prior, which basically just zeros everything outside here and does nothing inside here.

**[2:55:27 – 2:55:29]** And we get the posterior distribution.

**[2:55:30 – 2:55:41]** So it's theta times theta to the n 1 minus theta to the m divided, let's keep it like this, p of d, d theta.

**[2:55:41 – 2:55:44]** And what is p of d?

**[2:55:45 – 2:55:49]** p of d is just the normalizing constant for this.

**[2:55:50 – 2:55:52]** It's the integral from 0 to 1.

**[2:55:52 – 2:55:56]** Oh, and the integral is from 0 to 1 because elsewhere it's 0.

**[2:55:56 – 2:56:04]** So p of d is the integral from 0 to 1 of theta to the n times 1 minus theta to the m d theta.

**[2:56:04 – 2:56:10]** And here we get integral from 0 to 1, theta to the n plus 1.

**[2:56:10 – 2:56:12]** There is this extra theta here.

**[2:56:12 – 2:56:15]** Times 1 minus theta to the m d theta.

**[2:56:17 – 2:56:19]** And I won't do the math.

**[2:56:19 – 2:56:20]** It doesn't matter for us.

**[2:56:20 – 2:56:22]** We will never come back to it.

**[2:56:22 – 2:56:28]** But if you had a calculus class, you probably recognize this is the beta function.

**[2:56:28 – 2:56:31]** And you can express it as factorials.

**[2:56:31 – 2:56:34]** And then all of the factorials will cancel out, blah, blah, blah.

**[2:56:34 – 2:56:37]** I don't want to teach you about beta functions if you don't already know.

**[2:56:37 – 2:56:38]** And if you do, it's kind of easy.

**[2:56:39 – 2:56:47]** But the result here will be n plus 1 divided by n plus m plus 2.

**[2:56:48 – 2:56:52]** So there is this extra stuff here.

**[2:56:54 – 2:57:01]** This formula is called the Laplace's rule of succession.

**[2:57:06 – 2:57:10]** Pierre-Simon Laplace was one of the original founders of probability theory.

**[2:57:10 – 2:57:13]** That was one of the original results of the whole field.

**[2:57:13 – 2:57:15]** But whatever, it doesn't matter.

**[2:57:16 – 2:57:21]** The point is what the predictive distribution does, in fact.

**[2:57:21 – 2:57:25]** So if you look at this from a different perspective,

**[2:57:25 – 2:57:34]** it's the expectation over the posterior of this likelihood, right?

**[2:57:35 – 2:57:37]** Just by definition, what is the expectation?

**[2:57:37 – 2:57:41]** It's the integral, the function times the density, d theta.

**[2:57:41 – 2:57:47]** So this is like the likelihood averaged over the posterior distribution.

**[2:57:50 – 2:57:53]** And what does it mean in our case?

**[2:57:54 – 2:57:59]** Well, in our case, it means that we average over this purple distribution here.

**[2:58:00 – 2:58:02]** And yes, its maximum is at zero.

**[2:58:04 – 2:58:05]** This is the theta map.

**[2:58:06 – 2:58:09]** But its maximum is on this one side of it.

**[2:58:10 – 2:58:14]** And in fact, there is this whole triangle, right?

**[2:58:14 – 2:58:24]** So when you average over this distribution, you don't just get what you would get if you plugged in zero.

**[2:58:24 – 2:58:26]** You get something in between.

**[2:58:26 – 2:58:28]** Like it's not one, the average is not one half.

**[2:58:29 – 2:58:31]** The average here is like one third.

**[2:58:31 – 2:58:34]** But it's not zero either, right?

**[2:58:35 – 2:58:44]** So you average your likelihood over the whole posterior distribution,

**[2:58:45 – 2:58:48]** over all possibilities for the model parameters.

**[2:58:48 – 2:58:51]** And yeah, that's a lot to digest.

**[2:58:51 – 2:58:56]** But I hope that this coin tossing example is easy enough

**[2:58:56 – 2:58:59]** that we actually understand what's going on.

**[2:58:59 – 2:59:01]** Are there any questions at this point?

**[2:59:01 – 2:59:08]** I think there has been a lot of new information so far.

**[2:59:14 – 2:59:16]** Okay, okay.

**[2:59:17 – 2:59:19]** Yeah, I love the emojis.

**[2:59:20 – 2:59:21]** All right.

**[2:59:21 – 2:59:27]** So at this point, even on this very simple example of the coin toss,

**[2:59:27 – 2:59:31]** I have just one, I think, last comment left,

**[2:59:31 – 2:59:33]** and then I will show you a couple of plots,

**[2:59:33 – 2:59:35]** and then we'll end for today.

**[2:59:36 – 2:59:47]** So this kind of thing is what machine learning is actually about.

**[2:59:49 – 2:59:54]** So when you define a model, like when you...

**[2:59:54 – 2:59:55]** Sorry, where was it? Here.

**[2:59:56 – 3:00:01]** When you define a model, like I want to distinguish cats from dogs,

**[3:00:01 – 3:00:05]** what you actually are doing is you define a loss function.

**[3:00:07 – 3:00:11]** And the loss function is actually, almost always,

**[3:00:13 – 3:00:17]** either the log likelihood that you want to maximize,

**[3:00:18 – 3:00:21]** well, the negative log likelihood because for the losses you want to minimize,

**[3:00:22 – 3:00:23]** but it's the same thing.

**[3:00:24 – 3:00:30]** Or, even more often, it's the negative log posterior, which is...

**[3:00:30 – 3:00:35]** So if I write it in logarithms, I will see that, like,

**[3:00:35 – 3:00:46]** the log posterior is just the log likelihood plus the log prior plus a constant, right?

**[3:00:46 – 3:00:47]** That's what proportional is.

**[3:00:48 – 3:00:51]** So, again, in terms of the optimization, it doesn't matter,

**[3:00:51 – 3:00:59]** but it does matter in the sense that we are aiding the log prior, too.

**[3:00:59 – 3:01:02]** And the log prior is the regularizer.

**[3:01:02 – 3:01:03]** We didn't discuss it.

**[3:01:03 – 3:01:07]** We'll discuss it tomorrow where the regularization comes in.

**[3:01:07 – 3:01:13]** But regularization means putting a prior on the modal parameters.

**[3:01:14 – 3:01:20]** So introducing your own beliefs of what the prior actually was.

**[3:01:24 – 3:01:25]** Okay.

**[3:01:27 – 3:01:34]** And yeah, and I think I have to discuss one last point here.

**[3:01:34 – 3:01:39]** So this was all, the specific formulas that I wrote

**[3:01:39 – 3:01:41]** were only about the uniform prior.

**[3:01:41 – 3:01:46]** And as I said, it's not the prior that I actually have in mind

**[3:01:46 – 3:01:48]** when I'm talking about the coin, right?

**[3:01:48 – 3:01:51]** So for a real coin, it's some bell-shaped curve.

**[3:01:51 – 3:01:53]** I'm pretty sure it's close to one half.

**[3:01:55 – 3:02:00]** So of course, I want to plug in a more realistic prior here

**[3:02:00 – 3:02:01]** if I want to learn the Quintos.

**[3:02:02 – 3:02:05]** But to plug it in, I need to define it, right?

**[3:02:06 – 3:02:09]** So the question, let's say it's,

**[3:02:10 – 3:02:16]** what is the more realistic prior for the coin?

**[3:02:16 – 3:02:19]** And what is the most natural prior for a coin?

**[3:02:20 – 3:02:25]** What is, how do I define P of theta?

**[3:02:27 – 3:02:29]** Okay, and here the answer may surprise you.

**[3:02:30 – 3:02:32]** If you never thought about it before,

**[3:02:32 – 3:02:33]** the answer may surprise you

**[3:02:33 – 3:02:37]** because it sounds kind of lazy, but it's true.

**[3:02:38 – 3:02:43]** So the prior is a distribution on theta.

**[3:02:44 – 3:02:47]** We know that it should be zero here, zero here.

**[3:02:47 – 3:02:48]** No question about that.

**[3:02:48 – 3:02:50]** But what is the shape inside?

**[3:02:50 – 3:02:54]** My intuition says that it should be something like this.

**[3:02:55 – 3:02:58]** But there are millions and billions and, you know,

**[3:02:58 – 3:03:03]** a space with continual dimension

**[3:03:03 – 3:03:06]** of how many different functions look like this, right?

**[3:03:06 – 3:03:09]** So how do I choose a specific function?

**[3:03:09 – 3:03:13]** What will be this family of probability distributions

**[3:03:13 – 3:03:15]** that I plug in for p of theta?

**[3:03:16 – 3:03:19]** Do you know any distributions that look like this?

**[3:03:19 – 3:03:20]** Can you suggest some?

**[3:03:23 – 3:03:25]** Normal distribution.

**[3:03:25 – 3:03:27]** Normal, sounds good.

**[3:03:27 – 3:03:28]** On the surface.

**[3:03:29 – 3:03:34]** So with normal, you will have a problem right from the outset

**[3:03:34 – 3:03:38]** because the normal distribution will not go to zero, right?

**[3:03:38 – 3:03:41]** So the normal distribution is never exactly zero.

**[3:03:41 – 3:03:45]** It will be like something depending on the variance

**[3:03:45 – 3:03:46]** and then it will go down

**[3:03:46 – 3:03:50]** and then it will have some tails on both sides, right?

**[3:03:50 – 3:03:51]** So there will be tails.

**[3:03:53 – 3:03:55]** But okay, let's cut off the tails.

**[3:03:55 – 3:03:56]** We can do that.

**[3:03:56 – 3:03:59]** We can truncate normal distribution on the left and on the right.

**[3:03:59 – 3:04:01]** And we renormalize a little bit.

**[3:04:01 – 3:04:02]** It becomes a bit higher.

**[3:04:02 – 3:04:05]** But it's still like the normal bell curve over here.

**[3:04:07 – 3:04:08]** What happens next?

**[3:04:09 – 3:04:12]** So I need to write down the normal distribution.

**[3:04:12 – 3:04:13]** What is my P of theta?

**[3:04:14 – 3:04:17]** Well, it's 0 outside of 0, 1.

**[3:04:17 – 3:04:21]** And here it's some constant, which I cannot compute, of course.

**[3:04:22 – 3:04:25]** Times what?

**[3:04:25 – 3:04:30]** Times e to the power minus 1 over 2 sigma squared.

**[3:04:31 – 3:04:36]** Theta minus 1 half squared on 0, 1.

**[3:04:36 – 3:04:38]** Right?

**[3:04:38 – 3:04:41]** That's the density of the normal distribution.

**[3:04:42 – 3:04:43]** Okay.

**[3:04:43 – 3:04:44]** So far, not so scary.

**[3:04:45 – 3:04:46]** But what happens next?

**[3:04:46 – 3:04:52]** Next, I need to multiply P of theta times P of D given theta.

**[3:04:54 – 3:05:03]** And that's going to be, okay, inside 0, 1, it's going to be like C times this exponent

**[3:05:03 – 3:05:09]** times theta to the n times 1 minus theta to the n.

**[3:05:09 – 3:05:13]** That's my posterior distribution, the shape of the posterior.

**[3:05:14 – 3:05:17]** And then I need to maximize it.

**[3:05:17 – 3:05:18]** So I need to take derivatives.

**[3:05:19 – 3:05:22]** It sounds like it doesn't fit, right?

**[3:05:22 – 3:05:25]** So we probably can do it numerically, of course.

**[3:05:25 – 3:05:27]** I mean, it's a coin, it's dimension one.

**[3:05:27 – 3:05:29]** Of course we can do it numerically.

**[3:05:29 – 3:05:35]** But it sounds like some pretty inconvenient distribution for acquaintance.

**[3:05:36 – 3:05:38]** And what exactly is inconvenient?

**[3:05:38 – 3:05:45]** What is inconvenient is that the shape of the prior does not match the shape of the likelihood.

**[3:05:46 – 3:05:50]** The prior is an exponent, and the likelihood is a polynomial.

**[3:05:50 – 3:05:53]** And we multiply one by the other, we don't get anything meaningful.

**[3:05:54 – 3:05:55]** We get exponent times polynomial.

**[3:05:58 – 3:06:02]** So here is the secret here.

**[3:06:03 – 3:06:05]** I just want a bell-shaped curve.

**[3:06:06 – 3:06:12]** My intuition doesn't tell me if it's normal or student's T or whatever.

**[3:06:13 – 3:06:19]** So how we actually choose is we choose by convenience.

**[3:06:20 – 3:06:26]** We choose the shape of the prior that matches the shape of the likelihood,

**[3:06:26 – 3:06:29]** so that this multiplication becomes easy.

**[3:06:31 – 3:06:34]** And that, formerly it would be called the conjugate prior.

**[3:06:34 – 3:06:35]** Let's not get there.

**[3:06:35 – 3:06:37]** I will just give you an example, and we'll be done with it.

**[3:06:38 – 3:06:41]** So what would be easy to multiply?

**[3:06:41 – 3:06:43]** So the likelihood we cannot change.

**[3:06:43 – 3:06:48]** The likelihood is given by the process, by the thing that we are describing.

**[3:06:48 – 3:06:49]** So in this case, it's a coin.

**[3:06:50 – 3:06:52]** It has two sides, one parameter.

**[3:06:52 – 3:06:53]** So this formula is fixed.

**[3:06:54 – 3:06:55]** We cannot change the likelihood.

**[3:06:56 – 3:06:58]** But we can change the prior.

**[3:06:59 – 3:07:03]** And what would be easy to multiply by a polynomial like this?

**[3:07:05 – 3:07:10]** This is the likelihood.

**[3:07:10 – 3:07:15]** How should a prior look like so that it's easier to multiply by this?

**[3:07:27 – 3:07:30]** Okay, you're probably wondering exactly how easy.

**[3:07:30 – 3:07:32]** I didn't define that.

**[3:07:32 – 3:07:43]** But like, okay, so the prior, the easiest way, the easiest function to multiply by a thing like this would be another thing like this.

**[3:07:44 – 3:07:45]** Isn't that true?

**[3:07:46 – 3:07:53]** So let's say the prior is something like theta to the power of alpha, formerly alpha minus 1.

**[3:07:53 – 3:07:55]** That's just for formal reasons.

**[3:07:55 – 3:07:56]** Don't pay attention.

**[3:07:56 – 3:08:00]** Times 1 minus theta to the power of beta minus 1.

**[3:08:01 – 3:08:05]** And times a constant and the constant is a beta function, blah, blah, blah.

**[3:08:05 – 3:08:06]** Let's not get there.

**[3:08:06 – 3:08:13]** But as a result, I will get theta to the power alpha plus n minus 1.

**[3:08:13 – 3:08:19]** And I will get 1 minus theta to the power beta plus m minus 1.

**[3:08:20 – 3:08:22]** So the multiplication becomes trivial.

**[3:08:23 – 3:08:32]** But what is actually important is not that it's easy, but that the posterior again looks exactly like the prior.

**[3:08:32 – 3:08:40]** So the prior is what is called the beta distribution with parameters alpha and beta.

**[3:08:41 – 3:08:53]** And after I multiply by likelihood with n heads and n tails, I get the posterior, which is again a beta distribution.

**[3:08:54 – 3:08:58]** But with parameters alpha plus n and beta plus n.

**[3:08:59 – 3:09:03]** So when that happens, we call it the conjugate prior.

**[3:09:04 – 3:09:06]** You don't have to memorize that.

**[3:09:06 – 3:09:16]** But the point is now this calculation by the bias rule becomes trivial.

**[3:09:17 – 3:09:19]** I don't need to even think about the formulas.

**[3:09:20 – 3:09:21]** I just did it once.

**[3:09:21 – 3:09:23]** It's just adding up the exponents.

**[3:09:23 – 3:09:24]** That's it.

**[3:09:24 – 3:09:24]** Right.

**[3:09:26 – 3:09:39]** And now I can easily go from prior to posterior for any n and them.

**[3:09:40 – 3:09:41]** I don't need to do any new math.

**[3:09:41 – 3:09:43]** I don't need to run any numerical algorithms.

**[3:09:44 – 3:09:47]** I just plug it into this very simple formula where it's just addition.

**[3:09:49 – 3:09:55]** And the only thing that I need to check is that indeed this kind of prior can express what I want.

**[3:09:56 – 3:09:56]** Right.

**[3:09:56 – 3:09:59]** So that I can get a bell-shaped curve out of it.

**[3:09:59 – 3:10:02]** And yeah, I can get a bell-shaped curve out of it.

**[3:10:02 – 3:10:08]** So if I have, like, theta to the power 10 and 1 minus theta to the power 10,

**[3:10:08 – 3:10:14]** if the exponents are the same, then I will get a big peak at one half.

**[3:10:14 – 3:10:21]** So at this point, let me just show it to you in practice.

**[3:10:26 – 3:10:29]** Yeah, let me just show you the betas.

**[3:10:30 – 3:10:35]** So here is the family of the beta distributions.

**[3:10:38 – 3:10:43]** The uniform distribution is also beta, beta with parameters one and one.

**[3:10:43 – 3:10:49]** So it's theta to the power of one minus one and one minus theta to the power of one minus one.

**[3:10:49 – 3:10:50]** So it's just uniform.

**[3:10:51 – 3:11:02]** And then as the alpha and beta increase, I get like this more and more pointy distributions.

**[3:11:02 – 3:11:03]** The variance decreases.

**[3:11:05 – 3:11:09]** And if alpha and beta are equal, then I get the maximum at one half.

**[3:11:09 – 3:11:16]** In general, I get the maximum at alpha divided by alpha plus beta, just like the coin, just like the max-like.

**[3:11:16 – 3:11:21]** So the beta family does include what I want.

**[3:11:22 – 3:11:27]** It also includes a lot of other nice distributions that I can probably get as posteriors.

**[3:11:28 – 3:11:32]** And what does the actual Bayesian inference look like?

**[3:11:32 – 3:11:34]** Well, it looks something like this.

**[3:11:34 – 3:11:44]** So let's first begin with our example like we did in the lecture.

**[3:11:45 – 3:11:48]** So here is the prior, it's uniform.

**[3:11:49 – 3:11:54]** The likelihood for one tails is the orange line.

**[3:11:55 – 3:12:00]** And then I multiply it by the prior, and then I renormalize,

**[3:12:01 – 3:12:03]** and I get the posterior, which is the green line.

**[3:12:04 – 3:12:06]** So this is what I drew on the board.

**[3:12:08 – 3:12:10]** What if my prior was different?

**[3:12:10 – 3:12:16]** What if my prior had parameters like 2 and 2?

**[3:12:16 – 3:12:21]** So 1 and 1 gives you theta to power 0, 1 minus theta to power 0.

**[3:12:21 – 3:12:26]** 2 and 2 give you theta to power 1 times 1 minus theta to power 1.

**[3:12:26 – 3:12:29]** So it's a parabola like this, right?

**[3:12:30 – 3:12:36]** This is the prior, and when I multiply this prior by the same likelihood,

**[3:12:37 – 3:12:39]** I still tossed it once, I got one tails.

**[3:12:40 – 3:12:44]** Well, now it's a cubic curve, and it shifted to the left a little bit,

**[3:12:44 – 3:12:46]** and its maximum is at one third.

**[3:12:47 – 3:12:48]** Makes sense, right?

**[3:12:49 – 3:12:54]** And then I can continue like this.

**[3:12:54 – 3:13:01]** I can become more and more sure a priori that the coin was fair,

**[3:13:02 – 3:13:09]** and I will get like this more and more picky priors around one half,

**[3:13:10 – 3:13:16]** and the more convinced I am in advance that the coin was fair,

**[3:13:17 – 3:13:19]** the less this one experiment will matter.

**[3:13:21 – 3:13:31]** So if I was already very sure that the coin is kind of fair, like 50-50, the parameter is 50-50,

**[3:13:32 – 3:13:38]** then this one result of tails will not change anything.

**[3:13:39 – 3:13:41]** The posterior looks just like the prior.

**[3:13:42 – 3:13:49]** But of course, if I keep tossing it and I keep getting tails, it matters more.

**[3:13:50 – 3:13:55]** So 10 tails will shift my posterior to the left.

**[3:13:56 – 3:13:59]** This is the likelihood for 10 tails in a row.

**[3:13:59 – 3:14:04]** And if I get, I don't know, 100 tails, then I will probably shift it quite a lot.

**[3:14:04 – 3:14:18]** But still, the prior matters a lot to how much evidence I need to actually move my beliefs.

**[3:14:22 – 3:14:22]** Okay.

**[3:14:23 – 3:14:24]** Yeah.

**[3:14:25 – 3:14:27]** And since we are here, let me also show you this.

**[3:14:28 – 3:14:39]** So how it might actually work is what is another...

**[3:14:40 – 3:14:43]** like nice property of the conjugate priors?

**[3:14:43 – 3:14:49]** What is another nice property of a situation where your posterior looks just like the prior?

**[3:14:50 – 3:14:57]** Another nice property is that now you can reuse this posterior as the prior for the next experiment.

**[3:14:58 – 3:15:01]** So now I can do like sequential updating.

**[3:15:02 – 3:15:10]** I can say, well, all right, so here is my original uniform distribution.

**[3:15:11 – 3:15:14]** Then I tossed the coin once and I got heads.

**[3:15:14 – 3:15:20]** So the orange straight line is the posterior after one coin toss.

**[3:15:20 – 3:15:25]** Then I tossed it another one time and I got a tail.

**[3:15:25 – 3:15:30]** So now this parabola is my posterior after two coin tosses.

**[3:15:30 – 3:15:35]** And when I toss it three more times, I don't have to go to the beginning.

**[3:15:35 – 3:15:40]** I can say, all right, so now I have this parabola after two coin tosses.

**[3:15:41 – 3:15:45]** Let me just multiply that by the likelihood of the next three.

**[3:15:45 – 3:15:48]** Like one heads and two tails, I think in this case.

**[3:15:49 – 3:15:51]** And this is the result.

**[3:15:51 – 3:15:51]** And so on.

**[3:15:52 – 3:16:00]** So I can forget about the previous dataset, just take the posterior and plug it in as the prior for the next update.

**[3:16:01 – 3:16:06]** So it can work like this.

**[3:16:06 – 3:16:22]** I start with p of theta, then from a dataset I get p of theta given d, and then I get another dataset, more data.

**[3:16:23 – 3:16:28]** And I want to go to p of theta given d and d prime, right?

**[3:16:28 – 3:16:32]** I want to unite all of the data and use all of the data.

**[3:16:33 – 3:16:38]** And basically, if I have a conjugate prior like this, I can just say, all right, so I did the math here.

**[3:16:39 – 3:16:41]** I can forget about this part.

**[3:16:41 – 3:16:48]** Now, this is my new prior, this is my new data set, and I get to the posterior, and of course, formally nothing changes.

**[3:16:48 – 3:16:54]** So, it's the same bias rule, only it's d on the right in every probability.

**[3:16:54 – 3:16:55]** It doesn't matter.

**[3:16:57 – 3:17:02]** But if I didn't have a conjugate prior, then it would just be very difficult to do.

**[3:17:02 – 3:17:08]** So, it would be easier to just start from here and do the whole computation with d and d prime.

**[3:17:08 – 3:17:13]** But if I do have a conjugate prior, then I can use it.

**[3:17:14 – 3:17:33]** And maybe one final thing to show, here is a coin toss that I, a sequence of coin tosses and the sequence of probability of heads that I have learned.

**[3:17:33 – 3:17:38]** And the probabilities of heads change as I go.

**[3:17:39 – 3:17:43]** And the blue line is the maximum likelihood hypothesis.

**[3:17:44 – 3:17:46]** And the orange line is the Laplace's rule.

**[3:17:47 – 3:17:54]** So it's this smoothed out n plus 1 over n plus m plus 2, the predictive distribution, the predictive probability.

**[3:17:55 – 3:17:59]** And as you can see, it's just as we expect, right?

**[3:17:59 – 3:18:06]** So in the beginning, the Laplace's rule is less extreme than the maximum likelihood.

**[3:18:06 – 3:18:14]** So after one toss, this is either 1 or 0, and this is either 1 third or 2 thirds, so much closer to 1 half.

**[3:18:15 – 3:18:23]** And it will, like, moderate these extremes of the max likelihood, but then after, like, 50 tosses, they're in distinguishing.

**[3:18:24 – 3:18:28]** So one converges to the other, and they both converge to the true probability.

**[3:18:29 – 3:18:35]** And we can do other random experiments here.

**[3:18:35 – 3:18:36]** It's, of course, the same.

**[3:18:41 – 3:18:44]** So, okay, so let's summarize.

**[3:18:44 – 3:18:46]** I think I'm already over time here.

**[3:18:47 – 3:18:58]** What we did today, this is Thomas Baez, the Reverend Thomas Baez from 1760-something.

**[3:18:59 – 3:19:04]** So, but actually, yeah, there is a famous story that this portrait is actually fake.

**[3:19:04 – 3:19:07]** It's not Thomas Baez, and nobody knows who that is.

**[3:19:07 – 3:19:09]** Okay, you can read it.

**[3:19:09 – 3:19:17]** Anyway, so we discussed the Baez theorem and how it is used in machine learning.

**[3:19:18 – 3:19:28]** We discussed the most important, not just the most important, we discussed basically the only problems that we are solving in machine learning.

**[3:19:29 – 3:19:30]** Like, what does it mean to learn something?

**[3:19:31 – 3:19:39]** Well, it means to say something about the parameters of the model, and you can just maximize the likelihood.

**[3:19:39 – 3:19:52]** But as we have seen today, it probably usually makes more sense to get the full posterior distribution if you can, and then maybe maximize it if you have to.

**[3:19:53 – 3:19:58]** And, yeah, tossing a coin, blah, blah, blah.

**[3:19:58 – 3:20:00]** Yeah, this is what we discussed.

**[3:20:00 – 3:20:04]** I will get to a couple more examples tomorrow.

**[3:20:04 – 3:20:08]** Conjugate priors we discussed.

**[3:20:08 – 3:20:11]** This is the beta family.

**[3:20:11 – 3:20:14]** Yeah, I think this is it.

**[3:20:14 – 3:20:16]** This is the Laplace's rule.

**[3:20:16 – 3:20:21]** You can read it up on the slides if you want.

**[3:20:21 – 3:20:22]** Where is the predictor?

**[3:20:22 – 3:20:24]** Yeah, yeah, for example, here.

**[3:20:24 – 3:20:28]** And the last problem, the most difficult problem,

**[3:20:28 – 3:20:31]** is to get the predictive distribution,

**[3:20:31 – 3:20:34]** is to get the next,

**[3:20:34 – 3:20:38]** the distribution of the next element of the data set,

**[3:20:38 – 3:20:41]** predict the next coin toss,

**[3:20:41 – 3:20:43]** given what the data set is telling us,

**[3:20:43 – 3:20:48]** regardless of the specific value of theta,

**[3:20:48 – 3:20:51]** which means you have to average over theta.

**[3:20:51 – 3:20:58]** And we did it with the example of the coin.

**[3:20:59 – 3:21:03]** Hopefully went through this whole example.

**[3:21:03 – 3:21:06]** I skipped a couple of minor details

**[3:21:06 – 3:21:11]** that don't affect the machine learning understanding.

**[3:21:11 – 3:21:16]** But overall, we've completed the coin toss example.

**[3:21:16 – 3:21:21]** Naturally, you can also extend it to die rolling

**[3:21:21 – 3:21:23]** to several different outcomes.

**[3:21:23 – 3:21:25]** It will be exactly the same.

**[3:21:25 – 3:21:27]** Maybe we'll talk about it tomorrow.

**[3:21:27 – 3:21:32]** But at this point, I think I will stop here.

**[3:21:32 – 3:21:37]** Are there any questions?

**[3:21:37 – 3:21:39]** - Yeah, I have a question.

**[3:21:39 – 3:21:47]** Can you remind, please, maximum likelihood and Laplace rule.

**[3:21:47 – 3:21:53]** Laplace rule is the optimization of prior multiplied by likelihood

**[3:21:53 – 3:21:55]** and maximum likelihood also.

**[3:21:55 – 3:21:58]** - So Laplace rule is the predictive distribution.

**[3:21:58 – 3:22:02]** So let me repeat it again because this is really important.

**[3:22:02 – 3:22:09]** So you have the bias rule, right?

**[3:22:09 – 3:22:12]** The bias rule connects the likelihood, the prior,

**[3:22:12 – 3:22:14]** and the posterior.

**[3:22:14 – 3:22:18]** The model itself is usually the likelihood

**[3:22:18 – 3:22:21]** and you can maximize the likelihood directly

**[3:22:21 – 3:22:24]** and you get the maximum likelihood hypothesis.

**[3:22:24 – 3:22:29]** If you add the prior, you get the posterior

**[3:22:29 – 3:22:32]** and you can maximize the posterior

**[3:22:32 – 3:22:36]** and you get the maximum a posteriori hypothesis.

**[3:22:36 – 3:22:39]** But what you really want,

**[3:22:39 – 3:22:41]** it's just that often it's impractical to get,

**[3:22:41 – 3:22:42]** often you can't get it,

**[3:22:42 – 3:22:47]** but what you really want is the predictive distribution.

**[3:22:47 – 3:22:49]** The next x given d.

**[3:22:49 – 3:22:54]** And there is no way to compute it usually,

**[3:22:54 – 3:22:58]** except like this, right?

**[3:22:58 – 3:23:03]** So like the expectation over the posterior

**[3:23:03 – 3:23:09]** of this next item likelihood, okay?

**[3:23:09 – 3:23:13]** And the Laplace's rule was about this.

**[3:23:13 – 3:23:22]** So the Laplace's rule said that P of heads given n and them,

**[3:23:23 – 3:23:30]** given D is n plus one divided by n plus m plus two,

**[3:23:30 – 3:23:32]** if you have a uniform prior.

**[3:23:32 – 3:23:39]** While let's say theta ML was given us n over n plus m,

**[3:23:39 – 3:23:44]** and theta MAP was also given us n divided by n plus m.

**[3:23:44 – 3:23:49]** This is all for the uniform prior.

**[3:23:49 – 3:23:57]** Okay, more questions?

**[3:23:57 – 3:23:58]** - Sorry, yeah, another question.

**[3:23:58 – 3:24:01]** - Sure.

**[3:24:01 – 3:24:03]** - Okay, first of all, about the same topic.

**[3:24:03 – 3:24:10]** So, for example, in econometrics and financial econometrics

**[3:24:10 – 3:24:13]** where we use time series, it is very common.

**[3:24:13 – 3:24:18]** Well, every time we build the model to predict the next,

**[3:24:19 – 3:24:20]** how do I say?

**[3:24:20 – 3:24:21]** - Yeah.

**[3:24:21 – 3:24:26]** - Out of value based on inputs from the previous period.

**[3:24:26 – 3:24:27]** So it is a very common problem.

**[3:24:27 – 3:24:28]** - Sure.

**[3:24:28 – 3:24:29]** - Why is it such a problem here?

**[3:24:29 – 3:24:32]** Is it the difference between time series

**[3:24:32 – 3:24:35]** and unordered observations like here?

**[3:24:35 – 3:24:42]** Or is it the difference of frequentist versus bias approaches?

**[3:24:42 – 3:24:43]** - There is no difference.

**[3:24:43 – 3:24:46]** I mean, it's just a different problem setting,

**[3:24:46 – 3:24:48]** but you will still need to convert it

**[3:24:48 – 3:24:51]** to supervised learning probably, right?

**[3:24:51 – 3:24:57]** So in reality, I mean, yeah, maybe formally your time series

**[3:24:57 – 3:25:01]** goes to negative infinity, but in reality, it doesn't, right?

**[3:25:01 – 3:25:06]** So in reality, you will have your data set, sorry,

**[3:25:06 – 3:25:13]** your data set in time series analysis will still look like pairs of Xs and Ys.

**[3:25:13 – 3:25:16]** And how do you define the Xs?

**[3:25:16 – 3:25:18]** Well, that depends on your model, of course.

**[3:25:18 – 3:25:22]** So maybe you do a sliding window, right?

**[3:25:22 – 3:25:27]** So maybe you say, okay, I look at the previous, so many ticks,

**[3:25:27 – 3:25:35]** and I predict the next tick based on this fixed context.

**[3:25:35 – 3:25:39]** Then your X is this, or you can say, well,

**[3:25:39 – 3:25:43]** let me do, I don't know, a recurrent neural network.

**[3:25:43 – 3:25:45]** If I have a recurrent neural network,

**[3:25:45 – 3:25:50]** then it means that what my recurrent cell is doing

**[3:25:50 – 3:25:55]** is it's getting my current X and the hidden state H.

**[3:25:55 – 3:25:57]** And we are predicting, let's say, okay,

**[3:25:57 – 3:25:59]** actually we are outputting the next hidden state,

**[3:25:59 – 3:26:04]** but we are also, let's say, predicting this Y over here, right?

**[3:26:04 – 3:26:06]** So we will talk about recurrent neural networks

**[3:26:06 – 3:26:09]** when we get there, but here also, you

**[3:26:09 – 3:26:14]** compress your context down to this state vector H,

**[3:26:14 – 3:26:16]** and this is your input and you want to,

**[3:26:16 – 3:26:22]** and then you get your output, and so on.

**[3:26:22 – 3:26:26]** So I don't feel there is any difference specifically.

**[3:26:26 – 3:26:30]** So yeah, time series sometimes are a little bit special,

**[3:26:30 – 3:26:32]** but I think not in econometrics.

**[3:26:32 – 3:26:36]** I think they're special when they're really, really long,

**[3:26:36 – 3:26:41]** like in sound analysis, when you have millions and millions of ticks,

**[3:26:41 – 3:26:45]** you don't want to treat them as just a time series,

**[3:26:45 – 3:26:48]** maybe you want to do Fourier transforms,

**[3:26:48 – 3:26:50]** look at the spectra, etc.

**[3:26:50 – 3:26:52]** And then it becomes a different science.

**[3:26:52 – 3:26:59]** But I think in econometrics, it's just supervised learning.

**[3:26:59 – 3:27:05]** - Another question about the notebook that you showed.

**[3:27:05 – 3:27:13]** So the second-to-last graph, can you show it again, Grace?

**[3:27:13 – 3:27:15]** - This one? - Yes.

**[3:27:15 – 3:27:22]** So, for example, when n equals to five, sorry.

**[3:27:22 – 3:27:24]** - No problem.

**[3:27:24 – 3:27:28]** Yeah, when n equals to five.

**[3:27:28 – 3:27:36]** - So we can reduce the, how do I say,

**[3:27:36 – 3:27:41]** our prior component is the result that we got on previous step.

**[3:27:41 – 3:27:44]** - Yeah. - So is there a difference

**[3:27:44 – 3:27:46]** in the result going step by step?

**[3:27:46 – 3:27:49]** - No. - Or just using five observations

**[3:27:49 – 3:27:51]** from our initial expectation, which is the same?

**[3:27:51 – 3:27:53]** Exactly the same, that's the whole point, yeah.

**[3:27:53 – 3:27:56]** So, of course, for a coin, I mean, it doesn't matter.

**[3:27:56 – 3:27:58]** You're not saving anything.

**[3:27:58 – 3:28:02]** Going straight from the beginning is just as easy.

**[3:28:02 – 3:28:04]** But if you had like a big data set

**[3:28:04 – 3:28:10]** and you could compress it down to the posterior distribution,

**[3:28:10 – 3:28:12]** maybe now you can forget about the data set.

**[3:28:12 – 3:28:13]** That's maybe a good thing.

**[3:28:13 – 3:28:16]** You don't need to go over it again.

**[3:28:16 – 3:28:18]** I mean, for a coin, yeah, you're not saving anything

**[3:28:18 – 3:28:21]** because for a coin, the data set reduces to two numbers.

**[3:28:21 – 3:28:34]** numbers so it's it's not like you can be more efficient here yeah absolutely so

**[3:28:34 – 3:28:41]** what I will do what I always do is I will make a web page for the class or you

**[3:28:41 – 3:28:49]** and it will have the videos it will have the boards it will have the notebooks

**[3:28:49 – 3:28:57]** um and it will be unfortunately a secret web page for the harbour space university so I am not allowed

**[3:28:57 – 3:29:03]** to post it in public but I will send you the link in google classroom also if it's convenient for you

**[3:29:03 – 3:29:09]** we can make a telegram chat for the class I think we don't have one but it it would be really convenient

**[3:29:09 – 3:29:19]** for me but if if that's not good for you then google classroom is fine too okay so thank you

**[3:29:19 – 3:29:27]** and see you tomorrow judging by your questions I think you did learn something new today thank you

**[3:29:27 – 3:29:30]** see you tomorrow thank you

## Full text

Hello, everyone. It is very nice to meet you here. Well, virtually, remotely, but still meet you here at Harborspace. My name is Sergei Nikolenka, and I will be talking to you about machine learning. And, yeah, the class is named very specifically computer vision in neural networks, but to be honest, usually it so happens that it kind of becomes just a general introductory class to deep learning, which, judging by the two responses I had, we will also do this time, because it sounds like many of you have not had real experience with deep learning specifically, so we will start from the very beginning and then work our way up. There will be computer vision, of course, I mean, we have to give some examples, and since the class is about computer vision, why not give computer vision examples? But we will start from the beginning and we will try to build the cathedral of modern artificial intelligence from the ground up as best as we can. But let me begin today with a brief introduction to machine learning in general. Okay, so I don't think we will get to neural networks today. I hope we'll get there tomorrow. And finally, I got to be the host, so I can now spotlight. That's all I needed. Thank you. So let's begin by talking about where artificial intelligence is, how we got there. And today I want to maybe, for some of you it will be a reminder, for some of you it will be new material, but I want to discuss the most fundamental stuff of machine learning. Like, what is it based on? What is the basic machinery that everything runs on? And it turns out that that basic machinery is basically probability theory. So for those of you who liked your statistics courses, rejoice. And we will see how it all relates to learning, to training, et cetera, et cetera. So anyway, let me start with a brief intro. Anyway, we live in some very interesting times. And usually when I start a new class on machine learning, I have been teaching for almost 20 years. Yeah, almost 20 years I have been teaching machine learning. And when I start a new class, I usually start with like this historical overview, right? And traditionally I would begin with a picture like this one. It's just a random timeline of the internet, nothing special about this one. But, you know, I would talk about and I will talk a little bit today about how AI as a field has progressed starting from its beginnings in the 1950s. In the 1960s, the AI winter of 1970s, then we go to the 80s when neural networks reappear, then we go to the 90s and 2000s with probabilistic models, and then we go to the revolution of deep learning that defines artificial intelligence today. So that's all well and good, and if you look at AI from this standpoint, you see a regular field of science. And even if you dig deeper into some specific part of AI, for example, generative AI or whatever, you see some pretty reasonable timeline if you look at timelines from before the year 2022. But recently something has changed, right? Recently, AI has started to progress in some completely unexpectedly fast way, right? So this is a timeline I made a couple of years ago, three years ago in the summer of 2023. And it was about the spring of 2023. If you recall, that was the time when ChatGPT just appeared. It appeared in the late '22, but it was not really popular for a little bit. And then suddenly it blew up. And then in the spring of 2023, everything started appearing all at once, right? I will not go through the whole timeline here, it doesn't matter now, but look at March 14th, 2023. That was like... That was... Okay, sorry, we have a technical question, which I think I need to address. Can you see the presentation? Some people say it's not... The presentation is visible, but text on it is not created. Let me check. I don't want to switch to sharing the presentation because I will then need to go to the blackboard and stuff like that. I'm in HD. Let's do what you suggested. Let me post the presentation for you. It will take a long time to get it to Google Classroom because I'm not logged in there, but I'll send it in chat right here. So anyway, the spring of 2023 was like this sudden outburst of everything AI-related and specifically LLM-related. Okay, I send the presentation, it says it's uploaded. And if you look at, for example, March 14th here, you see that on the exact same day Google announced that it would be integrating LLMs into its workspace. It wasn't called Gemini at that point, but some LLM Google did announce. A small startup that recently split off of OpenAI announced that it would be producing its own family of LLMs plot, which we all know and love now. But both pieces of news were completely overshadowed by OpenAI, which came out and said that we are, well, not yet releasing, but we are announcing GPT-4, the next step in this development of LLMs at that point. And when I made this picture three years ago, I called it the Spring of Artificial Intelligence. And I mean, at that point, three years ago, it was completely possible that this would all still be, you know, in line with some regular development of regular science, right? So sometimes you have a breakthrough. When you have a breakthrough in that, in 2023, that was ChetGPT. So LLM started to work. And when you have a breakthrough, you know, researchers go there. They fill in this new space with their research. And then the field needs a new breakthrough, right? So scientific progress usually goes by these big steps. When somebody discovers a new direction, then it's very quick for a while, and then it slows down back again. So back then it was still possible that it would go like this, but of course it didn't. And the rate of progress has not slowed down since 2023. We are still getting news basically every week, and we are getting big news every month in the field of AI. It's not slowing down, on the contrary, it looks like it's speeding up, right? It looks like currently the Frontier Labs, the OpenAI and Anthropic, they already are using their own models to make their own models better, right? So it's not yet the fully closed loop of recursive self-improvement that everybody is talking about, but I think we're getting there, right? And if we do get there, then who knows what's going to happen, right? And so we live in some very, very interesting times, and I want to stress here, because by now it's actually already not obvious to people, but I want to stress here that it was completely unexpected, and very, very few people predicted this. So I recently came across this nice example. This is a book from 2018, less than 10 years ago, right? So the deep learning was already here. We already had, I don't know, LSTMs. We actually already had Transformers, right? In 2018, we already had the Transformers. And the author of this book asked several prominent researchers, when do they expect human-level artificial intelligence? And the closest was none other than Ray Kurzweil, which you would expect. And he predicted it in 2029. And that was the nearest prediction. So less than 10 years ago, most researchers would place human-level intelligence somewhere around 50 years from now. Things have changed, right? And this rate of progress keeps accelerating. So in this class, I hope, we will actually go all the way to the modern LLMs. Naturally, not in full details. We cannot do it in full detail in three weeks. But we will start from the foundations of artificial intelligence, from the foundations of deep learning specifically, of how neural networks work. And then we will discuss the main classes of architectures of neural networks. And ultimately, of course, we'll get to transformers, we'll get to language modeling, we'll get to the GPTs and clouds of today. But let's start at the very beginning, right? So I will still allow myself this guilty pleasure of doing a historical survey. Artificial intelligence is a very old idea. So artificial intelligence, I mean, in a way, according to almost every religious tradition in the world, we are artificial intelligence, right? Because we were made in some traditions out of clay, in some traditions out of some less pleasant substances. But in any case, we have been made by God and whatever the name of the God is, right? And we have been created with our souls, with our intelligence, and so we are AIs, according to the religions of the world, right? More modern kind of artificial intelligence ideas can be found in, actually, Greek mythology, where, of course, Wells, but Hephaestus would create android robots for himself, and there were several. The most famous was this giant humanoid robot named Talos, and that's actually a pretty funny story, and it relates to the field of air as well. Hephaestus ultimately gave Talos, or I think it was Zeus who took Talos from Hephaestus and gave it to the king of Crete, I think, and on the island of Crete the job of Talos was to basically protect the borders, right? So Talos would run around the perimeter of the island, and when Talos saw enemy ships approaching it would take giant rocks and it would throw the giant rocks to the enemy ships. That was his job. What is interesting about this, in my opinion, is how things have played out to be in terms of what's difficult and what's easy, right? So the ancient Greeks were already starting to be pretty good at throwing big rocks to great distances. They already had catapults, right? And then they were not very accurate, but then we got, you know, trebuchets and then guns and then rocket launchers, whatever. So we are pretty good at hurling destruction to great distances with great accuracy, actually. But the more difficult part it turned out to be was to actually recognize enemy ships, right? So already, I don't know, 400 years ago, you could have a big gun that would be pretty accurate in sinking the ship. But how would you automatically recognize, first, that there is a ship on the horizon, and second, that the ship is an enemy ship and not a friendly one, right? So that's a computer vision problem, and that proved to be more difficult for humanity to automate than the rock-throwing part, which is, I think, pretty interesting. Similarly, okay, so there was AI in many different traditions. In the Judean tradition, for example, there was this notion of a golem, and some wise rabbis could create golems. Okay, so that didn't play out as the Judaic tradition predicted. In there, there was a big difference between speech recognition and speech synthesis as an AI task. So a golem can actually understand you. It can understand commands. It will fulfill the commands of the rabbi who created it. It will know human language, but it will never speak. In the Judaic tradition, understanding was okay for man-made constructs, but to actually speak, you had to have a soul. And of course, even a very wise rabbi cannot create a new soul. So that didn't play out as expected. And that was why Thomas Aquinas was the famous philosopher and the pupil of Albertus Magnus, the famous alchemist. So Thomas Aquinas was very, very upset when his teacher, Albertus Magnus, actually created an artificial speaking head. And of course, we don't know what it actually was. One hypothesis is that it works something like this. So it was just a device for transporting sound from a different room and somebody would actually speak through the pipe. We don't really know, but what we do know is that Thomas Aquinas got very upset and actually smashed the whole thing to pieces. Then in the Middle Ages, I won't go into details here, but you probably know there were lots of very inventive automata, early robots, which are not quite robots in the modern sense, but human figures that can do some simple task automatically, particularly like poor water or something like that. And they were pretty inventive, but they were purely mechanical, not very interesting, of course, for us. What I do want to mention are these automata by Pierre Jacquetreau. He was a Swiss watchmaker, and actually the Jacquetreau watches you can still buy, although they are very, very expensive, but it's an existing brand. And his hobby on the site was making very intricate human-like dolls that would do very fine things with their hands, and that would actually do something interesting by themselves. And there was this draftsman, a doll that would actually draw several different pictures, but what is really interesting, what I wanted to highlight was this guy, the calligrapher, and the calligrapher is very similar to the draftsman because he also is using a quill to write on a piece of paper, but you could actually program the calligrapher to write what you want. There was like this, I don't know, a system of levers or something on the back that you could switch some of the levers and you would write different letters. To my knowledge, that was the first actually programmable device before Jacquard's looms that are usually quoted as the pioneers of programming that invented punch cards, etc. But that was before. That's interesting. But of course, this is not AI as we understand it now. So there was no programming to speak of. There was no math AI that would be AI related. Actually, I don't want to talk too much about this guy, Ramon Lowell. But I mean, I usually mention him in Harborspace because he is Catalan. But basically, he was an early logician and if you stretch definitions a lot, you can actually say that he did something that would later be related to AI, but not really. When did AI actually appear as a science? There are several starting points and usually, well basically there are two starting points that I will quote. One is the 1943 paper on the mathematical models of neural activity that we will get to later when we discuss deep learning. And the other is the 1950 paper of Alan Turing, the Turing test, which I hope you have all heard about. So Turing was a very smart guy and he was like really a genius. He did a lot of total breakthroughs in the field of computer science. And in particular, he basically invented artificial intelligence. And the first question, of course, that a person thinking about this stuff seriously encounters is: Can you do an artificial intelligence? Can machines think? And this is the subject of Turing's essay of 1950, which I definitely recommend you read. Because, you know, old research papers are usually very hard to read. They use strange notation. They are cumbersome. It doesn't make sense. A modern textbook would be much better, would explain stuff much better. But in this case, Turing was a genius, right? So his essays, they are not so much research papers as philosophical discussions about stuff. And they are still very interesting. So I definitely recommend you read the essays of Turing. And specifically, the Turing test was in this essay on Computing Machinery and Intelligence, it was called. And the Turing test itself is very interesting in how it survived for so long and why it survived for so long. So you've all heard about the Turing test. There is a judge, the judge is chatting in writing with an unknown entity or with two unknown entities. And then one of the entities is a human, the other entity is a computer. And basically the judge needs to recognize which was the human and which was the computer. So there are a couple of interesting points here. First, note that it doesn't make any sense to run the Turing test once. So the Turing test actually kind of grew out of Turing's foundational work on computer science, on algorithms, theory of algorithms and randomized algorithms. So the Turing test definitely wouldn't tell you anything if it was just one run of the experiment. Because, of course, the judge can always just flip a coin with probability one half. It will be right. So when does a machine, when does a computer program pass the Turing test? Not when it fools the judge once. It wouldn't make any sense. But when it consistently makes it impossible for the judge to recognize the program with any probability significantly different from one half. So right from the start, it's an interesting remark that we get to the realm of probability theory, we get to the realm of randomized algorithms, et cetera. We'll talk more about that later. Okay, so now the main part. Then I go for the fun remark, but now the main part. The main part about the Turing test is, unlike all other tests of artificial intelligence, and I will give an example, unlike all other tests, the Turing test has actually survived for a very long time. So I think I have a slide on this. Yeah. So formally, the Turing test was actually passed just a year ago. Okay. Of course, once you had stuff like GPT-4, nobody really doubted that GPT-4 could pass the Turing test in the original formulation, like in a five or 10-minute chat. But, you know, it was non-trivial to actually run the test, because, of course, if you're talking with a frontier model these days and you just ask it, well, are you an AI? The model will tell you, oh, yeah, sure, I'm a language model. So somehow you would need the model to stay in character, right? And it's easier to do with small ones, but small ones would not fool anyone. So there were some problems with actually running the Turing test, but once people did, of course, the models passed. But it's very recent news. It's 2025. And the original Turing test was in 1950. And that is very cool and very surprising in AI because, to be honest, AI as a field has a very long history of moving the goalposts. So, for example, that's the example that I want to give. In the 1970s, there was this guy, Alan Newell. We'll meet him later. And he wrote a very nice paper, like, what is the state of AI now and where are we going? Like this position paper that would define how the field of AI should develop. And at the end, he wrote, well, okay, we have the Turing test, but of course, the Turing test is not really actionable. In the 1970s, it wasn't. Of course, you cannot expect AI models to pass the Turing test. And there can be no progress on the Turing test, right? So it's not like you can fool 5% of the judges, then 10% of the judges, then 20% of the judges. It doesn't work like that. Either you fool humans or you don't. And so he wrote, okay, we need some kind of other tests that would be numerical. In the sense that you could actually measure the result, but also that would actually reflect something inherently important about intelligence. So if the machine passes, it means that we actually are making progress towards general artificial intelligence. Sounds very reasonable. But what is his example? His example was, let's take chess. And he actually argued for Page that, well, chess is a very nice candidate because it's numerical. You can play against each other, play against humans, to have an ELO rating. It's measurable. That's completely true. But on the other hand, and chess is easy to program in the sense that it's a finite game with fixed rules, blah, blah, blah. But on the other hand, chess is such a human game. You have to understand the flow of attack and defense on the chessboard. You have to maybe have a model of the other person's mind and understand what the other person is thinking about when he's making this move so that you can predict his intentions and maybe subvert them, et cetera, et cetera. So he was making this very plausible-sounding argument that chess is a good middle ground. And then, as you all know, in 1997, Deep Blue beat Kasparov. And I think the last match where humans had a chance was 2001. Vladimir Kramnik had a few matches against the best computers of the time, and he actually almost won at some point. I think he missed a mate and won very famously at one of the games. But after that, it was completely hopeless, right? So after 2001, there was no question who is better at chess. And by now, or even by 2010, 2015, there was even nothing humans could help with. So for a while, there was this field of centaur chess where a human with the help of a computer would play better than just a computer. But that is also a thing of the past. But did the AI researchers in 1997 or 2001, did they say, "Oh, okay, so we have the AGI now, the test has been passed"? Of course not, right? But what we all said collectively as a field was, "Oh, okay, so you beat chess." Well, chess doesn't count. Chess is too easy. Chess is, you know, you can just do a tree search and the tree search already gets you halfway to the best players. It doesn't count. Let's take Go, the game of Go, much better. It's still finite, it's still combinatorial, but you can never do a search tree in Go because there are too many possibilities. The branching factor is too big. That's true. You cannot have a meaningful complete search tree in Go. In chess you have like 10 reasonable moves at most, in Go you have 50 to 100 reasonable moves. So it's completely impossible to do the depth search. But AlphaGo happened, right? And then AlphaZero happened. And of course in Go computers in 2016-17 also became hopelessly better than humans. Well, did humans say now AlphaZero is the AGI? Of course not. Humans said well Go doesn't count. And that's the history of AI in a way and people still do that. People still say for some reason that LLMs don't count and they try to invent reasons why LLMs don't count. But the Turing test actually stood this test of time. So there was no moment in the 1980s when somebody would say, "Oh, I passed the Turing test with a stupid script, so it doesn't count." No, that didn't happen. Why? So my main point here, because what is the Turing test really about? Yes, it's about natural language processing in a big part. So it's about being able to talk in a natural language to a human in writing. But not only about that, right? The point of the Turing test is that when you have a freeform chat as opposed to a chess game, as opposed to question answering or whatever, you can talk about anything, right? You can actually, I don't know, you can introduce computer vision or at least 3D modeling into the Turing test. You can say, "Oh, hey, look, we are talking on the computer, right? So can you tell me what's on your desk? What's in front of you? What's on the left? What's on the right? What do you see? What's in the room? Can you please walk out of the room, describe what you see and then come back?" And yeah, sure, you have no way to check if that's true. But to actually make this picture consistent, the entity on the other side would need to kind of understand the 3D world. And natural language is complete in the sense that you can talk about anything. So why am I spending so much time on this? Because in a way, this is exactly the reason why modern LLMs are so great. So all that modern LLMs basically are trained to do, I think we'll get there at the end of the class, and I will explain it to you in more detail. But the base LLMs, what they are actually learning to do is just predict the next token in text. What is a language model? A language model is a machine that predicts the next word, the next token in natural language. That's it. But to predict the next token, you need to understand a lot of stuff. Not only do you need to understand how language works, so this will get you partly there, part of the way there. But then, after you understand how language works itself, you need to understand how the world works. So if the text says theorem, blah, blah, blah, proof, dot, and that you are supposed to predict the next token, well, maybe you need to prove the theorem first. And if the text says, I've been to Paris last month, and I visited the museum, and then you need to predict the next world, well, now you have to understand which museums are in Paris. So natural language includes everything. Well, maybe not exactly everything. It doesn't include stuff like robotics, for example. So robotics is a very different field because there is no huge set of books on, I don't know, what is the angle that you need to rotate your joints in order to pick up a cup from the table. So this you need to understand from other sources. But natural language is a great source of information for virtually everything. And that's the reason why LLMs keep surprising us. They keep getting this, uncovering these new capabilities that actually mostly come simply from predicting the next words in text. All right, I'm spending too much time on the Turing test. Sorry, one last point, a funny point on the Turing test, I hope. So if you look at the Turing test, at this competition where the machine is supposed to talk like a human, you notice immediately that it is completely, totally unfair. It's completely unfair to the computers. First of all, imagine the reverse Turing test. Imagine that we are checking in text, and I, a human, am trying to pass for a computer in this dialogue. How would you uncover that I am a human? What would be the question? What could you ask me so that you would immediately know that I am not a computer and I would have no way to pass for one? Can you give me an example of lemon pine? Why would it distinguish humans from computers? If you would give me this information, I would immediately understand that you are an LLM. Why? Actually, I don't know why, but if you have, for example, some assistance, if you need some help and you can ask, for example, some McDonald's chatbot and give me an example of lemon pine or give me some program in Python, I would immediately understand that you are an LLM, you are not a real person. No, wait, but I mean, imagine the reverse Turing test. So like I'm talking to you in chat and I'm a person, that's me, but I'm trying to pose as a computer, right? So I'm trying to convince you that I am a computer. What would you ask so that you immediately would realize that I am not a computer? It is worth trying like a math problem, a very complicated one. Yeah, for example, sure. So if you ask me what's, I don't know, 37 to the power of 23, I have no idea, right? And it would take me a long time to figure it out. For a computer, it's trivial, right? So we would never pass the reverse Turing test, we humans, right? Even for the computers of the 1950s, we would not pass. But that's okay. So this is, of course, inherently unfair, but ultimately we do want... The whole purpose is to teach computers to be like humans, not to teach humans to be like computers. So that's okay. But there is also one more subtle unfairness in the Turing test, which is, well, the computer needs to pose as a human. The computer needs to represent itself as somebody else. The human doesn't need to do that, the human just needs to be himself. That's unfair too, right? So the original Turing test, if you read the essay, the original Turing test was actually formulated as follows. It should be a judge, a human judge, trying to distinguish between a computer posing as a woman and a man posing as a woman, so that everybody would need to play somebody else and would need to walk in the shoes of as different a person as you can. And you can understand why this little detail got lost in the history of the Turing test, but it was there. I think it's also pretty fine. All right, so that was the Turing test. But that's kind of on the negative side, in the sense that, of course, in the 1950s, there was no way to pass the Turing test, not even to be close. But it kind of got people thinking. And the actual positive field of AI as a science, when you actually try to build stuff, emerged in 1956. It was the so-called Dartmouth workshop at Dartmouth, obviously. And it was organized by these four very famous researchers. John McCarthy was the early programming languages guy, he invented Lisp. Marvin Minsky was the guru of neural networks. I hope you all know Claude Shannon, the author of information theory. And Nathaniel Rochester, I keep forgetting what he did, but he built some computer at IBM. A very early and very famous computer. And the 1956 workshop had what I think, I always like to quote it because I think it was the most ambitious grant proposal in history. And it went like this. We propose a two-month study of artificial intelligence by 10 people in the summer, blah, blah, blah. We will attempt to find how to make machines use natural languages, find abstractions and concepts, solve problems now reserved for humans, and improve themselves. That's machine learning, right? We think significant advancement in one or more of these problems is possible if a carefully selected group of scientists works on it for a summer. Okay, and they were funded, they got together, they did conduct the workshop, but this grant proposal, of course they didn't actually do anything, they didn't actually solve any of these problems, but they kind of understood how difficult they were. But still, the 1950s and the early 1960s was a period of very high expectations. It was the golden age of science fiction. Everybody was expecting androids to walk, in a few years was expecting androids to walk around to bring you coffee, to talk to you in human language etc. That was the time when science fiction was expected to become alive very soon. What people actually did, the actual progress was of course very limited, but it was still very good progress. So for example there was this logic theories program, which I will not talk about in detail, but it was a theorem prover back in the day. It was thought that the important part was to teach AI logic, to teach AI math. Now we kind of understand that it doesn't work that way, but it was a very good prover for its time. It actually successfully reproved a lot of the fundamentals of mathematics, and it kind of also fueled these early high expectations. And there were some other examples, it doesn't matter, but basically what happened in the early 1960s, the optimism didn't work out. But the primary example of why people were disillusioned in AI in the 1960s was a failed project on machine translation. So people actually expected in the 1950s that they would write a program that would translate from Russian to English, if you believe it or not, and that it would work. And of course, it was completely beyond the abilities of computer science at that point. So in 1961 or 62, there was this big report that said, well, OK, so machine translation basically doesn't work. We need a lot more research. Let's regroup. And then, you know, the government got disillusioned. They stopped giving out grants for AI. And when you don't give out grants for research, researchers move to other fields. So ultimately, what we had in the 1970s is now known as the AI winter. And the AI winter means that there were very few people actually working on AI, on artificial intelligence. It was believed to be kind of too hard, impossible and inaccessible with current techniques, which was true in the 1970s. So it's not like people were wrong. The only thing that actually was happening were experts. And expert systems, they are kind of also AI, but they are a very specific kind of AI when you try to perform probabilistic reasoning on small snippets of domain knowledge, so to speak. So, for example, the main example is probably mycin, which was a 1970s system for diagnostics, medical diagnostics, based on blood tests. And what is a blood test? What are the results of a blood test? It's basically a big table of 50 numbers, right? You have red blood cells, white blood cells, hemoglobin, iron, whatever, all sorts of chemicals found in the blood. And an experienced doctor, an experienced physician can look at the blood test and say, oh, it's that disease. Oh, it's this disease. So that's the diagnostic problem. But however experienced the physician is, however experienced the patient is, I don't know, whether he's a genius diagnosed like Dr. House, it actually is completely impossible for a human to just sit down and write a function of 50 variables that would just give you the diagnosis. Human brains don't work like that. Even if you kind of know what to look for, et cetera, what you can actually formulate is not a general unifying function of everything, but you can formulate some local heuristics, like if the red blood cell count is high and the iron is low, then it's that, and if the alcohol content is 20%, then it's this, and so on and so forth. So you can ask doctors to give you this kind of local heuristics rules. And then the AI question, so you do not question the rules. The rules are given to you from a trusted source, so to speak. But the AI question is, how do you combine the rules? So now you are given a new blood test, and there are all sorts of problems. So like, okay, you have like 450 rules, and 20 of them kind of apply. But also, they don't apply. They kind of apply, because the rule is, again, not a mathematical function. A human doctor cannot do that. The rule is something like, if the red blood cell count is high, and what does high mean mathematically? Well, this high is definitely high. This high is definitely not high. But what about this? What's in the middle? Where is the threshold? Probably there is no threshold. Probably it's a continuous function. So there are all sorts of difficulties here, and that's what people were doing in the 1970s. I won't spend time on that, because that's not our subject. Definitely. And then what actually happened, so let me skip almost to the present, what actually happened was in the 1980s, people again got back to neural networks. In the 1980s, you already had convolutional networks and recurrent networks and multilayered net, deep networks, so basically you could have deep learning in the 1980s, 1990s, but you didn't, mostly for technological reasons. So people already kind of realized that neural networks are cool, but they didn't really work because there was not enough data and not enough compute to make them work. You needed more. And it all came together in the middle of the 2000s, so to say. So in 2005, 2006, 2007, several different labs, specifically Jeffrey Hinton's lab and Joshua Benja's lab, they actually kick-started this deep learning revolution. And that's when everything came together. So by that time, due to the internet, due to increased computational capabilities, you already had enough data to make neural networks work. And you also started to have enough compute. You started to have enough computational power to train large enough neural networks. And the final step was actually going from CPUs to GPUs. So we'll discuss it later when we discuss neural networks, actually. But it's kind of obvious that if you look at neural networks, that everything you do there is highly parallelizable. And it was a very natural idea when GPUs actually appeared in Webcom, and it was a very natural idea to switch from CPUs, which are like a few very fast cores, like four cores, four gigahertz each, switch to GPUs, which are much slower, but with hundreds and thousands, of cores. And that gave you this final boost that made deep learning actually work. And starting from the late 2000s, deep learning has, neural networks have been going from subfield of subfield to machine learning, and they have been setting state-of-the-art in a lot of different fields. So we'll discuss that later. And now, let me end the historical part here. And now, about what machine learning actually is. So how do you define what it means to learn? So what is learning? And we will get to a much more technical definition a bit later. But if you open some old textbook from the 1990s, you could find a definition like this. So like a computer program learns with accumulating experience regarding a class of tasks T and the performance measure P if its performance on these tasks improves it against your experience. So it doesn't say much. It sounds very trivial. But so what is, I think, important here on this slide is that when we are talking about learning, we have to have a performance measure, right? So we have to have some kind of number that goes up or down whenever it needs to go. So because if we don't, then we will never understand did we learn something or not, right? So in a way, the half of deep learning is about inventing the loss functions. It's about inventing these objectives. What is the number that we want to get down? How do we define the error so that when we minimize this error, we actually get what we want? Sometimes it's very easy, but sometimes it's kind of non-trivial. Sometimes it's part of the science. So this is the conclusion from this. And also, I think you have all seen at some previous class or somewhere in your life, you have seen this main taxonomy of machine learning problems. Let me go through it still. We will not talk too much about it later in class, because we will mostly exclusively be in here, in the supervised learning part. But let me just mention what kinds of machine learning problems there are. So technically, machine learning problems are divided into supervised learning, unsupervised learning, and reinforcement learning. And supervised learning is what we intuitively think of when we think of machine learning, like I need to build a classifier that distinguishes cats from dogs on a picture. So how do I build a classifier that distinguishes cats from dogs? I get a dataset of pictures, and for every picture I mark whether it's a cat or a dog, and then I train a classifier to distinguish between them. So I think it's a good time to actually start doodling on the board. So in supervised learning, there is the whole machine learning, and in supervised learning, you have... One sec, I'll make it a little more comfortable, so I can write better. So in supervised learning, the dataset consists of pairs of X and Y, right? So for example, X is the input, and Y is the output that you want to get. And your machine learning model is actually a machine. It's, let's say, a black box for now. We'll get there later. But it's a machine that takes the input and produces some function of the input that is supposed to look like the output, right? So we are trying to convert the input into the output. For example, if we are doing simple classification, simple binary classification, so there are cats and dogs here, then probably f of x is like a number from 0 to 1. And if it's close to 1, then we say it's a cat. If it's close to 0, then we say it's a dog. So it's kind of supposed to be the probability of a cat. But notice that it's the probability of a cat for a given picture, right? So it's the probability of a cat given x. And that's the whole point of supervised learning. So the point of supervised learning, mathematically speaking, is to learn whatever that means. We'll get there much later, but it's to learn the conditional distribution p of y given x. So we are always assuming that we will have the input. The classifier that distinguishes cats from dogs cannot draw you a new cat picture. It's not supposed to. It always presumes that you have a picture at the input. And then with this picture, you do stuff. So computer vision works like that, right? In computer vision, you always assume that you have a picture at the input. Well, maybe a set of pictures, maybe a video or whatever, but you have some high dimensional, very complicated input. And you're supposed to break this input down into the answers to the questions that you're interested in. And it's not necessarily a classification. There may be more interesting problems like object detection, like segmentation. We'll talk about those in class since we are doing computer vision here. But overall, you are trying to take a complicated input and convert it to some relatively simple output. So that's what supervised learning is about. And when you collect a dataset for supervised learning, you always need to have the correct answers. Sometimes, and in computer vision, unfortunately very often, it means that you need to have some very complicated labeling. And labeling is very difficult and expensive. So we'll talk about that when we get there, but for classification, it's not that expensive, but for things like segmentation, proper labeling is extremely expensive. So we will need to somehow, you know, do with relatively small datasets. But that's only the first part, right? There is also unsupervised learning. So there is this other field where there is no why, there is no correct answer. The dataset is just a set of something, and the big question is what are you supposed to do with it, right? Okay, so now we have a dataset of pictures, but the pictures, the images, they are not labeled in any way. So what are we even trying to do? What is the goal here? It actually turns out that you still can have a meaningful goal and you can still do stuff that will be very, very useful for downstream problems like classification, etc. And usually what unsupervised learning is doing is something called, let's call it dimensionality reduction. So reducing the size of X, compressing it so that on the one hand you compress X down to something. I still have a black box, but now the output is not some small known thing, but the output is, let's say, a vector of numbers. And X is still, let's say, a picture, but now the goal is not to classify X immediately, but the goal is to compress X down from its original size. And we will actually, I think we will talk about this more, but images are big, right? And if you think of images as sets of numbers, they are pretty big sets of numbers, right? So, like, how many numbers, I have a question to you, how many numbers are there in a one megapixel photo? One megapixel is how many pixels? No, come on, don't try to compute. Naive guess, like, 1000 square or something like that? Well, almost, right? So, a megapixel is not a million pixels, unfortunately, it's 1024 squared, right? So it's a power of 2. But whatever, okay? It's close to a million. And how many numbers is that? Like, if I take an image of one megapixel, and I say that, okay, I want to view it as a set of numbers, what is the dimension? How many numbers are there? How many numbers in a pixel? Come on, guys, you're in for a computer vision. Three numbers, right. Right. There are three numbers in a pixel. So a one megapixel photo, which is not that large, is 3 million numbers, approximately, right? Right. So if you think about this space of possible images, it's a huge space. It has a huge dimension. Nothing works in that dimension. Right. So it's it. And if you think about, like, what is the structure of the set of images in that space? Well, we, collective humanity, have absolutely no idea. Right. So it's very, very difficult. We have no idea how to how to describe this. So it's some very complicated manifold in this in the huge space of dimension 3 million. Right. So like imagine we can't imagine, but think of this set of like real photographs among all possible pixel values in dimension 3 million. What is the structure of this set? Right. This is completely incomprehensible. I can only say that it's an open set. Right. Because if you have a real photo and you move every pixel by a very, very tiny amount, nothing changes. Right. So it's still a real photo. But what actually distinguishes real photos from random noise, we have no idea. Right. And we have no idea what is the geometric structure of this manifold. It's probably extremely complicated. So what is unsupervised learning trying to do here? It's trying to map this extremely complicated manifold of real images to dimension much smaller. Let's say, I don't know, 500. That's just a number out of nowhere. It doesn't mean anything, but basically to project this huge space of images down to a more manageable, still large, but more manageable space, where hopefully it will be more comprehensible, easier to work with manifold. So that's usually the idea of unsupervised learning. So you want to do what in machine learning is called feature extraction. You want feature extraction or representation learning. You want to map a big object like an image to a much smaller object like a vector of numbers, but you want to do it in a way that would not lose important stuff. So you can't just take the first 100 pixels from here. That's not going to work. You want to map it in such a way that you actually are able to answer interesting questions in this space of these, in the small space. For example, in this manifold of real images, you still will be able to distinguish cats from dogs. Cats are here, and dogs are here, and now, all of a sudden, in this space, in this 500-dimensional space, there is actually a hyperplane, a linear surface separating cats from dogs. And it's very easy to separate cats from dogs over there. Over here, dogs are this part, and cats are this part, and there is absolutely no way to disentangle. Sorry. So this is the point usually of unsupervised learning. Compress down, make it more manageable, and hope that in this more manageable little space, you actually can have relatively simple machine learning models doing the stuff that you actually want. So this kind of compression is never the end goal, right? We don't want these vectors by themselves. We want them for some ultimate purpose. But the thing is, we don't fix this purpose in unsupervised learning. We don't know. Maybe we'll use it for that, maybe we'll use it for this. Right now, we just want to get good features. How do we do that? Well, actually, there is a pretty simple answer, which is very common in deep learning specifically. So while we are talking about this, let me tell you. So, of course, we cannot have a dataset with the correct Zs. There are no correct Zs. We have no idea what is the correct representation in this low-dimensional space. So how do we verify that this black box is doing anything meaningful? How do we... So here we have, in supervised learning, we have a dataset with axis and y's, and we can just run the black box through the examples that we have and check that we get correct answers. Over here, there are no correct answers. But we cannot, as we will see soon, we cannot train a neural network without a loss function. We cannot train a neural network without some kind of goal, specific numerical goal that we want to optimize. So what would be the goal here? And there can be different answers, but in deep learning one very common idea is to do a thing called an autoencoder, which works like this. So I have this big thing, x. I get it through my neural network. Okay, that doesn't matter if it's a neural network, through my first machine learning model, which is called the encoder. And I get the vector z. But let's not stop there. Let's say, okay, so how do I verify that compression is good? Well, compression should, first of all, compress down to a smaller size. Here, it's by definition. I choose the size of z myself. But what does it mean to compress something and not just pick random numbers? It means that from the compressed object, I can reconstruct back the original. That's the whole point. It wouldn't be a very good archive tool It would produce just random bits and you would have no way to recover the files. So the whole point is to compress down in such a way that you can decompress back. So we add the decompressor. We add the decoder part, which takes the z and tries to restore the original image. Let's say it's x hat. So x is the input and x hat is the final output. So the decoder is probably also a neural network. The decoder is also a complicated neural network. It's like a generative model. It takes in something that looks like random noise, just numbers, and should produce a beautiful cat picture. So it does make our task more difficult, sure. But now we have a very easy way to say what we are looking for. So now we know exactly what the loss function should be, because the result should be just, you know, similar to the input. That's it. And you can define loss function basically like x hat minus x squared, like just the squared deviation in the pixels. That's a very common loss function in autoencoders. So this kind of idea, compress then decompress back, we will encounter it in class a couple of times. And it's a very natural thing to do in unsupervised learning. So when you are just trying to make sense of your inputs, of your data set, what is your goal? You are trying to find structure inside. What does it mean to find structure? Well, actually, in reality, it usually means to project down to a smaller space where you can see this structure more clearly. And if you've heard of unsupervised learning before, you probably heard about the example that was characteristic, that was the central example of unsupervised learning for a long time. I think now autoencoders and dimensionality reduction in general are more important, but for a long time the main example of unsupervised learning was clustering. Clustering, we won't talk about it much, out of scope for us, but clustering is this problem, you probably have an intuitive understanding of it, when you have some points, some objects, and your task is to split them into groups, clusters, so that points inside a cluster are similar to each other, are close to each other, and points across different clusters are different. The only thing I want to say about clustering is that you can view it as the extreme form of dimensionality reduction. So clustering means also taking a large object and compressing it down to Z in a smaller space, but now the dimension of this space is zero. So we are compressing each point to the label of its cluster, and there is just a finite set of different labels. And you can view it like that, and it's a very natural view of clustering. You compress down to a discrete finite set of points, and then you do it in such a way that decompression is as faithful as possible still. So the whole point of clustering is that you kind of want to replace all points in the cluster by its center or by the cluster label. And then you will be able to deconstruct the points as best you can. And yeah, okay, again, I'm spending too much time on supervised learning, but it's useful, I think. And if in supervised learning we were learning the distribution p of y given x, in unsupervised learning we are just trying to learn p of x, there is no y. And how does it map to this autoencoder or to the clustering picture or whatever? What does it mean to learn the distribution? Well, here in the autoencoder part it would probably mean to learn to sample from the distribution. So here you would say that z is kind of like random noise and the decoder converts the random noise into x that is supposed to be from the distribution of cat pictures. So I don't think we'll get to this kind of analysis in class, but again, useful to keep in mind. In supervised learning, we always have an x, we always have the input. In unsupervised learning, we are trying to describe the x itself. And very often, it means that we are actually learning a generative model that can produce new samples of x's. In the case of pictures, that can draw new pictures. And finally, there is the third guy, which we will not talk about at all, which is called reinforcement learning. Unfortunately, I cannot make this class about everything, so let me skip reinforcement learning. Let me just say a few words. Reinforcement learning is the subfield of machine learning where there is no dataset in the beginning. Instead of the dataset, you have your model being an agent in an environment, and the dataset is ultimately the experience of living in this environment. For example, if you are learning to play chess, then your agent does not have a dataset of correct moves. And it does not have a dataset of all possible positions from chess games and trying to compress them down like an unsupervised learning. So what your model is probably doing is it's playing chess against itself or against earlier versions of itself or against other models or whatever, and learning to play as it goes from the signal of who won. So that's how reinforcement learning works. You live in your environment, you get rewards that are, in the case of chess it's simple, the reward is who won. In robotics the reward may be more complicated but whatever, you get rewards from the environment and ultimately you learn to maximize these rewards. So you learn to behave, you learn a policy for behaving in the environment such that the reward gets maximized. Actually it's a pretty different topic. It has some pretty different approaches from supervised and unsupervised learning, so we will not be talking about it in class. I hope you will have a separate class on RL at some point. It's a very beautiful field. All right, so we discussed this. I think we'll skip these practical things like cross-validation and stuff. Maybe someone will talk to you about this in the practical part. Yeah, dimensionality reduction. All right, so I think now is a good time to have a break. We have come to the end of the intro part. Sorry, I should have started with this. I forgot to talk to you about the class itself and its structure. Basically, unfortunately, I'm not able to come to Barcelona this year, so I'm teaching online. And my colleague Alex Davidov will be with you offline on campus. I will be delivering lectures, and it's not what I would advise to do. But for logistical reasons, we will have a lot of lectures at the start. So we will have three days of lectures today, tomorrow and Wednesday. And I hope we will make some good progress and have a good start so that Alex will have something to work with when he begins on Thursday. And then I think we will mostly alternate like this, like two lectures, two practical sessions and so on. And ultimately we will even it out. I will be mostly awake next week and then I'll come back for the final lecture. Okay, so let's have a break. Are there any questions about the first part or the structure or whatever? How long a break do you need? Like offline it's usually half an hour, but maybe online we don't need that much. How long would you wait? 15 minutes, okay? Okay, so let's say 15 to 20 minutes and it's 11, sorry, 10 for you, 10:35. So on 10:50, 10:55, let's continue. Okay, break. Continue. All right, so in the first part, while you're getting back, I'll do a quick recap. In the first part, we discussed the history of artificial intelligence, how it all came to be, the early ideas like the Turing test, etc. And specifically, on point specifically, something actually useful for our machine learning class, we discussed the main and the most common taxonomy of machine learning problems. This distinction between supervised learning and supervised learning and reinforcement learning. And in the second part today, I want to talk about what learning actually means. And I have always understood it and I recommend you to understand it through the Bayesian perspective, through the probabilistic perspective. I will explain what I mean. But first of all, like for those of you who have had, I don't know, probability theory classes in your universities or in hardware space, you're probably kind of not very happy to hear that machine learning is pure probability theory from start to finish. Because usually when I say probability theory to my students, they get a little bit scared because a probability theory class is usually some very involved, difficult mathematical stuff about measure theory. You start with the sigma algebra of measurable Borel sets in the Euclidean space and then you introduce your probability as a measure. And then what the expectation is is already pretty difficult and what the conditional expectation is is extremely difficult and it's all some abstract theorems, etc. We won't need any of that stuff. I'm not saying forget it, don't forget it if you know it, but we won't need any of that. We'll need, you know, there is a saying I think by Cervantes that education is what remains after you've forgotten everything you were taught. So this is exactly this kind of thing. What we will need in probability theory is the intuition that remains after you forget all about the theorems and you actually, you know, you actually get this basic intuition of what probability is about. So what is it about? It's about random variables, right? And random variables, there are discrete random variables, like coin tosses, like coin tosses or, I should have prepared. So coin tosses and die rolls and stuff like that. And if you have a discrete set of... If you have a discrete set of... No, I don't. We'll improvise. And if you have a discrete set of outcomes, then the probabilities of these outcomes should sum to one. And that's your probability, right? That's your random variable. And then you can have continuous random variables where instead of probabilities of outcomes, you have the density function, right? And at this point, if you've had a probability theory class, you will tell me, "Oh, wait, but not every probability has a density, right? And many probabilities, including important ones, cannot be characterized by the density, and therefore, you need measure theory, blah, blah, blah." Forget about that. In machine learning, we only deal with kind of standard and easy probabilities. So everything that we will ever discuss will, of course, have a density. And in that case, the summing to one means taking an integral, right? An integral over the probability space. And again, there will be no exotic probability spaces here. Only the real line, r to some power, only the Euclidean space. And the things that we actually need in machine learning are these basic intuitions and the very basic definitions of probability theory, right? So now I really do hope that on this slide there is nothing new for you. If there is, I recommend you to repeat your probability basics a little bit because we will be using some of that. But okay, I will just go through this very quickly. If you have two events, two random variables, they can happen at the same time. Then you can define the joint probability, p of x, y. Actually, let me switch to the board. It will be better to explain it more interactively. There are random variables characterized by their probability mass functions, p of x if they are discrete. So just what is the probability of every outcome on a die from 1 to 6? Or by density functions like, I don't know, maybe it's concentrated from 0 to 1. We'll have an example like this today. Then it's some function whose integral is supposed to be equal to 1. And this is the density function for a random variable that samples you a number from 0 to 1. And if you have two random variables, then you can have their joint probability, p . So p is something like p equals to something and y equals to something else. So if you have your joint probability and you want to get only the marginal, it's called the marginal probability, the probability of one of the x and y's, then you need to kind of sum this over y. That's not a very formal way to write it, but I hope you understand what I mean. So if you have p equals a and equals to something else, and you want to get what is the probability of just p of x equals a, you need to sum over all possible values of y. Kind of makes sense. And from the joint probability, we get the notion of conditional probability. This is the most important notion for machine learning. So what is conditional probability? Conditional probability, p of x given y, right, is the probability that x, let's say, is equal to something, given that we know the value of y, right? And formally, it's very easy to define. Formally, just we take the joint probability, p of x, y, and we decompose it into p of x given y times p of y. I think this formula has some name, like full probability formula, or something like that, I keep forgetting. Doesn't matter, but the point is, this is the definition of conditional probability. So p of x given y is defined as p of x, y divided by p of y, right? And we'll have a lot of conditional probabilities later today and tomorrow, probably. And if you look at this definition, if you look at this decomposition of the joint probability into the marginal and the conditional, then you notice that you can do it both ways, right? You can start with y, like we did here. I mean, okay, one way to read this formula is how do you sample x and y? Well, you can start with y. You can sample y first from its own distribution, and then you already know what y is, and you need to sample x given this value of y. Or you can start with x. You can first sample x and then sample y given x. You can view it this way. But it's still, I mean, formally, it's still the definition of conditional probability, just the definition of p of y given x. But if you combine these formulas, you see that they amount to the same thing, to the joint p of x, y. And this is where you get the most important formula in the whole world, definitely in the whole machine learning, but I think it's wider than that. And that formula is, well, p of y given x is p of x given y times p of y divided by p of x, right? This is the base rule or base formula. And the way we present it now, it's completely trivial, right? It directly basically follows in one line from the definition of conditional probability. But in effect, philosophically, that's basically how reasoning works. Our actual real reasoning, not logical derivations where there are no probabilities and all facts are known for sure. In real life, we seldom know facts for sure, right? In real life, it's all about balancing the probabilities and weighing in the evidence. And the base formula underlies how you account for evidence, how you actually take something into account. We will definitely discuss it more. But before we do that, one last thing. There is also this very important notion of independence. And basically two random variables are independent if P , their joint probability, joint density, is equal to P times P . So if P decomposes into the products of individual densities or individual probabilities. In this case, the conditional is trivial, right? So basically the same thing you can say P given Y is equal to just P . The conditional is trivial. It means that P does not depend on the value of Y. That's why it's called independence. So two variables are independent, which basically means that you can sample them separately. You'll get the same result, like two coins that you toss in a row. And let's get back to the bias formula. And let me actually just first restate it in a slightly different notation, and then we'll discuss it. So let's call it the main formula of machine learning. And let me write it like this. p of theta given d equals p of d given theta times p of theta divided by p of d. Okay. It's the same formula, right? I just changed the notation. But I hope you kind of now understand what this notation is supposed to represent. So now d is the data. d is the data set, right? And theta are the model parameters. Theta is what we actually want to learn. So if we are talking about a neural network, we want to learn the weights, right? And notice that it's not the exact value of the weights. It's a whole distribution of weights. So we will get back to that. But for now, let's just say theta is the model parameters. Theta is the weights of a linear regression. That's going to be our first serious example. Or theta is the weights of a neural network. Or theta is just the probability of the coin that we are trying to learn. So let's say we have a... Okay, here is my coin. It has two sides. And I can toss it and I can get some results. And the data will be the set of outcomes, the set of results of what I'm getting from the coin tosses. And the parameters will be just the probability of getting heads, right? So the whole point of machine learning is to understand, to learn the model parameters from the data, right? So we have a set of outcomes for some stochastic process, for some random process where there is some inherent randomness. And we want to understand what was governing this process, what were the parameters that went into this process. This is the whole idea of machine learning. Everything else is basically commentary. And the biased theorem is the main tool for this. Why? What is so special about this? So let's discuss what we have in this formula. On the left, I have P of theta given D. P of theta given D is called the posterior probability or the posterior distribution. Posterior means after the fact, a posteriori, after evidence has been included. And that's what it says, right? So it's very, very intuitive. I get some data and I want to understand what I now think about theta, how my understanding of theta has changed given data after I have taken the data set into account. That's the posterior distribution. I want to, I want to, this is my goal in learning, right? So, okay, the final goal will be doing predictions. We'll get to that later. But like the intermediate goal is learning what I can about theta from D. Okay. And usually there is no way to get to this distribution directly without going through this formula. So how do we get to this distribution? Well, the bias rule tells us that it's the product of two things, basically. It's the product of P of D given theta, which is called the likelihood. So what is P of D given theta? It's the probability or usually the density of getting a specific data set given the parameters, given the model parameters. I'll make a coin tossing example in a second. It will be clear. But basically, when you define a model in machine learning, you usually define the likelihood. This is the easy part. The likelihood is what you get from just listing your assumptions and writing them down as formulas. And the main point of the Bayes rule is that the likelihood is not enough. You also need the third part, this guy, which is called the prior distribution or just the prior. The prior is just P of theta without any D, right? And what does it mean, philosophically speaking, it means what were we thinking about theta in advance before we started getting data, before we started getting D, right? So P of theta without any D. And I will make an extensive example in a minute. So the bias formula basically tells you if you want to get the posterior distribution, if you want to incorporate D into your thinking of theta, you need to take what you thought about theta before and multiply it by the likelihood of D. So for example, for example, oh, sorry, I wanted to say I didn't talk about the denominator, but I forgot to say that I didn't talk about it. So the denominator, indeed, I didn't talk about it, it's usually called the full probability or the evidence probability, something like that. And mostly P of D is not really important for us in machine learning. Why? Because it doesn't have any theta. So in machine learning, P of D is usually completely inaccessible by itself. So instead of writing the full bias rule, actually, usually we use it like this. P of theta given D is proportional to P of D given theta times P of theta. This means proportional. And what does proportional mean in this case? It means that, well, P of theta given D should be a probability distribution. So it should integrate to one. So almost always, actually completely always, I know no exceptions, P of D, the only way to compute P of D is to make it a normalizing constant for the numerator. So P of D is always just this, okay? And in some special cases, you might be interested in P of D, yes? But usually what you do is, what you do in machine learning and deep learning, usually you are just interested in, let's suppose, maximizing this with respect to theta. And if you maximize this, it's the same as maximizing this. And you don't care about the constant, right? So we'll get to that a bit later. So the denominator is complicated, but usually not really necessary. So we won't talk about that too much. Okay, now example. Let's learn a coin toss, okay? Here is a coin, or what passes for one. It has two sides. And I can toss it. So, how many parameters does a coin have? What is the size of the vector theta? Can you tell me? How many numbers do we need to define a coin with two sides? Okay, maybe I'm not asking the question clearly enough. So, a coin is a stochastic process, right? It's a random variable. I toss it, I get either heads or tails with some probabilities. So, how many numbers do I need to define these probabilities? How many parameters? What are the parameters for a coin? What probabilities do you need to fully understand a coin toss? Maybe just one, like the probability of one outcome? Yeah, precisely, of course. So, a coin has just one parameter. Very easy. The simplest example we can think of. So, let's say theta is the probability of heads. Okay, then the probability of tails will be what? 1 minus theta, precisely. And this is our first example, our first illustration of this probabilistic view of machine learning. And now you can start seeing why the likelihood is very natural. So, what is the likelihood now? The likelihood is this, is P of D given theta, likelihood. What is D? D is the data. So, it's the sequence of outcomes. D is like, I've been tossing this coin several times, and I got like heads, tails, heads, heads, heads, tails, tails, whatever. Okay? So, P of D given theta is very easy to define. It directly follows from just the model itself. I just need one additional assumption, which is, by the way, very important. It's true throughout the whole machine learning in every model, it works. I need an assumption of conditional independence. We didn't talk about that, right? So, independence is like this, and conditional independence is when, let's say, X and Y are conditionally independent given Z if this holds, right? So, this is conditional independence, conditional. So, we need the assumption that different data points are conditionally independent given the parameters. And again, it sounds very complicated, very messy, but it's very natural. So, like, if I already know what is the probability of heads, then different coin tosses are independent. I toss the coin again, and again, I get the same probability of heads. That's the basic assumption, right? So, in this case, it means that P of D given theta is decomposed into P of, like, D1 given theta times P of D2 given theta, blah, blah, blah, times P of Dn given theta. And what is P of D1, D2, blah, blah, blah, given theta? It's the probability of one outcome, of one sample in the data set. One sample in the data set is one coin toss, either heads or tails. So this is our P of small d given theta, right? Actually, to make it formally correct, let me just put theta here from the very beginning. Why not, right? So this is like theta is the probability of heads. So what is the probability of heads given that theta is the probability of heads? It's theta. What is the probability of tails given that the probability of heads is theta? It's one minus theta, right? So over here, every one of these small d's is either heads or tails, right? And, okay, let's work through an example. So let's say that this is my data set. So d is heads, tails, heads, heads, heads, tails, tails. What is p of d given theta then? Can you tell me? The actual number? Well, not the number, the formula. The probability of heads given theta multiplied by the probability of tails given theta and so on. And so on. Okay. And what is it? We know what is the probability of heads and tails. It is theta to the power of number of heads that you perceived. Okay. Let's say 4. 1 minus theta to the power of... Number of tails. Number of tails or n minus number of heads. Right. Right. Exactly. So, and this is the likelihood. Okay. So, this is basically always the case in machine learning. The likelihood is easy. The likelihood is... Well, okay, maybe it's not easy. It may be a very difficult, complicated formula. But the likelihood is like our model itself. When I say we define a machine learning model, usually what it means is we define the likelihood. We define the assumptions that let us write down this kind of formula. So for the coin, what were the assumptions? There was the assumption, well, not the assumption, the model of the process. There are two outcomes. They are mutually exclusive. One of them has probability theta. The other correspondingly has probability 1 minus theta. And this basic assumption that they are conditionally independent given theta, which is always the case in machine learning. So this is the likelihood of a coin for you. And what do we want to do with that in machine learning? Well, there are several things we can do. But while we only have the likelihood, the only thing we can do with the likelihood is try to maximize it. So the first type of optimization problems that arise is the first type of tasks that we solve in machine learning is finding the maximum likelihood hypothesis. Like theta ML, let's say, is the theta that maximizes P of D given theta. Right. Okay. Let's do it for the coin. Okay. So let's maybe not work with the specific numbers 4 and 3. It doesn't make much sense. Let's say, in general, we have our data set is N heads and M tails, right? So we have P of D given theta, just like you said, you already said it. It's theta to the power number of heads and 1 minus theta to the power number of tails. So how do you maximize it with respect to theta? How do you maximize stuff? Yeah, it sounds very difficult, but okay, in this case, it's going to be pretty easy. So let's take the derivative, okay, D likelihood over D theta. Can you tell me the derivative? Come on, guys, you can do it. Derivative of a polynomial. Let me try N multiplied by theta N minus 1 minus theta N power N. You forgot. Yeah, yeah, yeah. Right, so first the derivative of the first factor, right, times the second factor, then? Minus theta N power N. Oh, sorry. Y minus. Yeah, you're right, you're right. And 1 minus theta N minus 1. Okay, did you forget anything else? Or did I forget it? You said it. What's missing? M, yeah. Okay. Okay, and now we equate it to 0, right? So, let's not waste time on asking you to collect the terms. That's too easy for you. So, we can put this outside the brackets, right? And in the brackets, we have N times 1 minus theta minus M times theta. And that is equal to 0. So, in here, we have like N minus N plus M times theta. Okay. And here, and then we get the roots of this equation, which are theta equals 0, theta equals 1, and also theta equals N divided by N plus M. Okay. So, the first question, it's an easy question. The first easy question is, what's wrong with 0 and 1? What's wrong with 0 and 1? Why is it not the maximum? This is like obvious solutions. Why can't obvious solutions be correct? It could be correct, but if we have only tails and only heads. Well, yeah, okay, sure. But in this case, let's say we have both. When we talked about how we are finding other solutions, I said to check second-order conditions. If we do it, we'll find out that it is actually minimums and perfect solutions. Yeah, that's true. That's true. Let's not check the second-order conditions. That's too much work. Let's just cheat our way through it and notice that theta equals zero and theta equals to one give you zero likelihood, right? And if they give you zero likelihood, then obviously it's not the maximum because in between you get positive likelihood. So that's obviously minimum, not maximum. It doesn't count. And this leaves us this guy, right? So we got our first result about the coin, hooray. We have the maximum likelihood hypothesis, which is n divided by n plus m. Okay, so far so good. And this is probably what, I don't know, your first class on probability theory would tell. If you have a coin, you want to learn its parameter, you toss the coin, you divide the number of heads by the number of experiments of coin tosses, and you get your estimate for the probability. Completely correct. This is the maximum likelihood hypothesis. Again, if you recall your probability classes, you will know that in many cases, or at least in, I mean, I think in modern textbooks, they do it already differently, but in old textbooks like Feller on probability, some classical textbooks, you would get probability kind of introduced in this way. You would get probability introduced as, well, there is a system that gives you a random result, and then you run it infinitely many times, and you get some outcomes. You count how many outcomes you have, you divide by the total number of outcomes, and as the total number gets to infinity, this fraction gets to the probability. And that's kind of the definition of probability from some standpoint. And, of course, for a coin, it works perfectly. There is no catch here. Indeed, if you keep tossing the coin and you keep getting results, this fraction will not oscillate between 0 and 1. It will converge to the probability of heads. Everything is completely true. But here is a question. Here is a more interesting question for you. So let's say this is a coin. It has two sides. I can toss it and let's say... Okay, I was showing to you something, but let's forget about it. Let's say this is the first time I tossed this coin ever. I just took it out of my purse. That's the first time I ever encountered this coin. And let's say I toss it. Let's do it. Okay, I got tails. So at this point, what is my data set? My data set is just tails. What is my likelihood function? My likelihood function is 1 minus theta, right? What is the maximum likelihood hypothesis for this? Where is this function maximized? Well, there is a, first of all, there is an interesting formal problem here in that, well, now I just have a linear function. It goes to infinity. There is, I mean, there is no maximum, no minimum. Basically, if I just look at it formally and forget that it's a coin, theta ML should be like negative infinity, right? In a way, it's true. In a way, it's true. This formula and the likelihood function indeed does not care that theta is a coin, that theta is a probability, right? So there is nothing in this function that says, oh, theta should be from zero to one, right? So we have to kind of introduce it, impose it as a constraint. So far, kind of arbitrary, but okay, let's do that. Let's do that. Let's say we know that our theta is a probability, so it should be between zero and one. Then what is the maximum likelihood hypothesis between zero and one? Tell me. If we make it zero, right? Yeah. So now the maximum likelihood hypothesis is exactly zero. The math checks out. It's correct. I mean, it's very hard to make a mistake here. But what does it actually mean? Like, what's my conclusion? What did I learn? I took a coin. Let's say it's a real coin I took out of pocket. And I tossed it once. I got tails. And now my conclusion is that I will keep getting tails always. That doesn't make any sense, right? I mean, even if I didn't know about coins, like, I kind of have this intuition that coins are approximately fair, right? So theta should be something like one half. Probably not exactly. There is nothing exact in this world. Something nearby, right? But even if I did not have this intuition, if I didn't know anything about coins, still, I mean, come on, I have two options, and I made one experiment. Obviously, I will get one of the options, right? There is no other way. So, like, after one experiment, my maximum likelihood hypothesis will always be either zero or one, depending on what I got, which means that I should always conclude that I will keep getting just one result. That doesn't sound correct. That doesn't sound like a conclusion that we should actually make, right? So what's missing? What's wrong? What do you think is wrong here? The math is correct. It's indeed the maximum likelihood hypothesis. But it's not the... More experiments are needed? More experiments are needed. Good. Yes. Of course, if I want to, like, make a more precise estimate of theta, I will need more experiments. That is correct. And, again, your statistics classes will probably tell you how many experiments you need. Right. But here is the thing. Here is the important thing. There is, as I said before I started talking about this example, that there is no difference in the limit. So in the limit, the maximum likelihood hypothesis will get to the true value of theta as n and m go to infinity, and everything will check out, and all that I am telling you right now will not matter. So if we have this possibly infinite series of experiments if we can just toss the coin again and again, there is no problem, and we don't need to have this discussion. That's fine. But the thing is, in practice, we do not live in this limit. In practice, when we are talking about machine learning, we start with some data set, right? We have as much data as we have, and usually in machine learning, there is no easy way to get more data. If there was, then a lot of problems would be much easier. So in machine learning, we have our D, and we cannot really change it, right? And I mean, okay, in practice, maybe we can do some project to get additional data, yes, but when we are actually doing machine learning, when we do the data processing part, we have to assume that this is the data set that we are given. And even more importantly here, in practice, in real life, we will never get quite enough data. This is an important point. I want to make it here. Like suppose that I have, so if I just have a coin in this example and I have this ability to collect more data, then sure, I can toss it once, twice, 10 times, 20 times, 50 times. And after I've tossed it 50 times, I can be pretty sure in my results about the coin. Like the confidence interval will be quite small, et cetera, et cetera. Statistics will tell you. But that's not what happens with real-world problems. So, for example, suppose that you are building a language model. That sounds like a very difficult example, but in fact, it's one of the simplest and nearest to our intuition. Suppose that we are building a language model. So it's a model that has some kind of text. Then there is this black box, and then it produces the next token, the next word in this text, right? Suppose that I am OpenAI and the transformer has been introduced quite recently, and here I am. I just made my very first GPT model, which is like half of a transformer, right? So I train it on some text data set. I get some pretty good language model. Then what do I do next? I say, well, all right, so let's see how this scales up. Maybe I can get more data. And indeed, compared to the first GPT, how it was trained, it's easy to get more data. Let's just scrape it off the internet. Let's get some more texts, okay? So I extend my data set, and now I have like lots of additional data sets, and I have lots of text. I have a huge other data set. When I have this huge data set that's like orders of magnitude larger than the one used here, it maybe indeed means that now I don't care about this Bayesian stuff. I don't care about this effect. I can go back and I can train my GPT on this huge data set, and it will be like almost in the limit. It will be fine. But that's not what happens, right? It's not like I collect more data to go back to my GPT model and train it even better a little bit. No. When I collect orders of magnitude more data, I go to a larger model, right? I go to GPT-2 that has more parameters. So GPT had that many parameters, actually, I forget how many. And GPT-2 had like an order of magnitude more. It had something like 150 million parameters in GPT-1, I don't remember. So in actual practice, when you are solving a difficult task like predicting the next token or identifying cats and dogs and images or whatever, you never have enough data. It's impossible. Because whenever you have enough data for your model, in practice, it means that your model is too weak. It means that you should switch to a bigger model for which you now don't have enough data. But it still will work better. So I know I haven't proven that formally to you. And maybe if we have time, maybe we'll discuss scaling loss and stuff like that. But the point is, in machine learning, unless you have some very specific, very simple, very well-defined problem, like let's learn a coin toss or let's learn linear regression, right? So you have points and you want to represent them with the linear dependence, right? That's linear regression. You can maybe get more data for this linear law. You can get additional points. But unless you have like some very good reason to know that this is going to be definitely linear, unless it's, I don't know, a law of physics and it's supposed to be linear and you're just getting more data for it. So unless you are in some very special situation, if you have significantly more data, it will be better to go to a larger model, I don't know, from linear to polynomial, for example. And it will be a better fit, it will not overfit since you have more data, etc. We'll discuss it when we get to linear regression. So usually in machine learning, we operate on the frontier of what's possible. So the data is usually fixed. We can change the model, we can select the model, it's in our hands. And usually you want to choose a model in such a way that it's barely enough data to train. So we are always in practice in a situation where data is scarce, where it's not enough. So your answer is correct. Indeed, one toss is not enough to learn the probability of a coin toss. But let's say that's all we have. What can we say about the coin still? And definitely it shouldn't be this, right? So maybe we can give up and say, okay, we can say nothing, but we definitely shouldn't be concluding that from now on, the coin will always lend tails. That's definitely wrong. So what's missing? What else is missing? What is the component that will get us from this zero? What is the component that will allow us to say that, oh, okay, so the maximum likelihood hypothesis is this, but actually maybe one data point is not enough to really shift my beliefs about the coin. Well, the missing piece, the missing part here is my beliefs. And if you go back to the best row here, you will see that we have only talked about the likelihood, right? And what we actually want is the posterior distribution over here. And to get from the likelihood to the posterior, so like the posterior in this case, what does it mean? What is its tangible meaning? It's what do I think, what is my belief about the probability of heads after I got my data point, after I've tossed it once and got tails, okay? And the likelihood is how likely it was to get tails, given data. And to get to the posterior, the missing piece is the prior, right? So it's what did I believe about the coin? What did I think about theta before I started even tossing it, before any data came in? That's the missing piece. And in this case, it's pretty important. So let's think we will be able to complete this example. So let's go to the second part of this example, to the prior distribution. Prior distribution, P of theta for the coin toss. What does it mean? What kind of object is it? Well, here is the thing. P of theta is a distribution on the parameters. In this case, on one parameter, right? So that's why, unfortunately, in machine learning, you cannot limit yourself to discrete probability theory. So even when we are tossing a coin, it looks like the most discrete probabilistic object imaginable, only two outcomes, only one probability, et cetera. Still, as soon as we do learning, we get a continuous distribution. So P of theta is a continuous distribution. It's a distribution on the probabilities, right? So let's try to plot something. This is theta. This will be P of theta. And the first property that we definitely need to have is that theta is a probability, right? So the first very firm belief about theta is that it should be between 0 and 1, right? So whatever I think about the coin, whatever I think about its heads or tails probability, I can definitely be sure that theta cannot be negative. So P of theta is 0 over here. And theta cannot be larger than 1. So P of theta is 0 over here. This is P of theta. So by the way, this is the answer to why theta ML is not negative infinity over here. And the answer is theta ML is negative infinity. And that's fine, because then we will take this. So if I have only, so if D is just one tail, then my P of D given theta is 1 minus theta, right? And it's like this straight line over here. So this is, sorry, I'm not good at drawing. I'll do what I can, then I'll show you some nice plots. So this is P of D given theta, and yes, it does go to infinity, definitely. On the left and on the right, and since we want to maximize, it goes to plus infinity over here. But we will multiply this straight line by something which is 0 on the left of 0 and on the right of 1. So after we multiply, let's start with the obvious, let's start with the uniform distribution. It's not the uniform distribution, it's just 1 on the interval from 0 to 1. Oh, sorry, the interval is wrong. 1 is here, right? So if we start with the uniform distribution, then after I multiply this P of theta by this straight line, and this is the bias rule here, right? So P of theta given D is proportional to P of theta times P of D given theta. You remember. So what I'm doing is I'm taking P of D given theta, the green straight line. I am taking P of theta, which is this piecewise constant thing, the uniform distribution, the red one, and I am multiplying them. What do I get? I get 0 over here. Then I jump to 1. Then I go along this straight line, and then I get 0 again, right? These two lines are easy to multiply. This is not yet P of theta given D. Why not? Can you tell me why not? Why is the light blue line still not P of theta given D? The denominator? Yeah, the denominator is still missing, and here is an illustration to what I was telling you before. We don't want to get the denominator as some fact about the coin that we want to prove, right? It's just a normalizing constant. So I know that this area is supposed to be 1. Right now, it's not 1. Right now, it's what? What is this area? 1 and 1 half? 1 and 1 half, yeah, sure. It's half of a square of area 1. Right. So it's 1 and 1 half, and so it means that to get the actual distribution, I need to multiply it by 2. That's it. So the actual distribution is 0 here, and, like, twice larger over here. So, yeah, it will span two pages. I hope that's... So this guy is P of theta given D, right? And notice that we didn't actually change much in terms of maximization. Oh, yeah. So, yeah, this is P of... Okay, sorry, we'll get there in a sec. I forgot to say one thing. So, this is P of theta given D for the uniform prior distribution over here, okay? The first remark is, well, the uniform prior is not quite... Sorry, what's the word? The uniform prior is not quite what I really think about coins, right? So, let me draw a separate picture. The uniform prior means that, well, I don't know anything about the probability of heads. So, it could be 0, could be 1, could be 1.5, could be 1.3. It's all equal to me. But in reality, when I take a coin, like a real coin, or even this pseudo coin that is the coaster for my cup of coffee, I kind of expect that it's approximately fair, right? So, in real life, obviously, it's not exactly one-half because it's a physical object, it has imperfections, but in real life, I kind of expect that the probability is close to one-half. So, my actual prior distribution looks, okay, it's still exactly zero on the left and on the right, that's for sure, that's by definition, that's a mathematical fact, not my opinion. But in between, it's probably something like this, right? So, it's probably some bell-shaped curve, that says, well, I think it's approximately fair, maybe not exactly, but it's near one half. That's about where my intuition stops, really. So, I cannot define this curve mathematically, right? Our brains don't work in this way. I can just say that, okay, it's approximately fair, I'm pretty sure of that, but so this should be a pretty high and peaky distribution, but what exactly is the shape of this distribution, I don't know, right? This cannot be a part of my personal intuition. But anyway, we'll get back here, but let's first finish with the uniform thing. So still, let's begin with this not quite realistic uniform prior, not quite realistic for coins, but in other situations, it's a perfectly good prior because it basically just means I don't know anything. So in many situations, it's very reasonable. If it's a new machine learning problem, it has a parameter. I don't know anything about this parameter, but I know it's, let's say, I know it's a probability, so it's from zero to one. A uniform distribution is a great first step, okay? So in many situations, having a uniform P of theta is perfectly reasonable. So I take this uniform P of theta, I multiply it by my likelihood, one minus theta, and I get this pointy triangle, and this pointy triangle, so let me write it down, like P of theta given D, in my case, P of theta given a single tail, it's like 2 times 1 minus theta, if theta is from 0 to 1, and it's 0 otherwise, right? So formally we get this. And the next question, let's go back to the bias rule. We had our first question is, let's maximize the likelihood, our second question, and usually a better one, is let's maximize the posterior with respect to theta. So now that we have a posterior distribution, we can ask what is the, it's called the maximum a posteriori hypothesis. What's the theta that maximizes P of theta given D? And in this case, there is no difference really, right? So if I have a uniform prior, the only thing that I actually did, like formally what I actually did, was I took care of these degenerate solutions, right? So now my prior does say that theta should be between 0 and 1. That's a good thing. But otherwise, I didn't change the shape of the likelihood. I am multiplying it by 1. And then I am renormalizing, but that's just a constant. So the maximum will not change. The maximum will be at the same point, right? So theta, in this case, theta MAP is still N over N plus M, okay? And this sounds like a lot of complicated math. Well, maybe not that complicated, but a lot of math for nothing, right? So we went from maximum likelihood to maximum aposteriori, and we didn't change anything. The answer is the same. Well, that's because our prior was uniform, but even for a uniform prior, something has changed because I have one point left to make in this specific example, then we'll go to the priors. I hope we still have time. In this example, for example, in the example of a coin toss, and this is also a very important concept in machine learning. Today is like this very abstract and introductory lecture. I apologize. I have to begin with something like this. We'll get to neural networks literally tomorrow. But anyway, in this example, what is the end goal of this whole thing? Let's say that this is an actual machine learning problem. Let's say that it's, I mean, it's not, but let's say that it's something like distinguishing cats from dogs or something. So when I am learning the parameters of a machine learning model, what am I really interested in? What is my final goal? This is a very important point. So far, we have been talking about learning something about Theta. So we tried getting Theta ML, maximum likelihood. Now we added the prior, and now we are getting Theta MAP, maximum a posteriori. But that's about Theta. So if I map this discussion to neural networks, it would say, all right, so I have a neural network, Theta is the vector of its weights of the parameters, right? And then I do my learning, and here is, so Theta ML and Theta MAP are like checkpoints of the weights. They are the states of the neural network. But when I phrase it like this, it becomes clear that that's not the final goal of the process, right? If I am training a neural network to distinguish cats from dogs, I don't care what the weights are, right? I mean, I do want to get them, but I want to get them as an intermediate step for the goal, and the goal is distinguish cats from dogs, right? So what we are actually supposed to do, and this is the third part here, and this is true both in machine learning and generally in life, actually. What we are actually supposed to do is to make predictions, right? So, like, philosophically speaking, what does it mean to understand something? Well, it means that you can predict what's going to happen with it, and you can be right more often than chance. It's, I mean, if you haven't thought about this, it's a pretty deep idea. So understanding something doesn't mean rephrasing it in different words. It means phrasing in such a way that you can operationalize it and get to predicting some stuff that you didn't know in such a way that it actually conforms to reality. And here also, in this very simple case, even here, I mean, in the case of a coin, everything is very simple, very small, and very close to each other, so there may seem that there is no difference. So, okay, so what's the difference between predicting heads or tails and learning the probability of heads or tails? It's the same thing. If I get theta more than one half, I will predict heads. If I get theta less than one half, I will predict tails. Isn't that true? Still, there is a difference. Very interesting, but there is. And the predictive distribution in this case, what is it? It's like the probability of heads given the data. It's not in the biased formula. It's the next step. Let me, I don't have space here, I think. Yeah, let me write it formally separately. So I have the biased rule, P of theta given D is P of D given theta times P of theta divided by P of D. But the predictive distribution is the distribution of the next outcome, of the next X or the next Y given X in our learning problem. Like what's, okay, so I have this data, what's the probability that this picture is a cat, for example? X given D. And P of X given D does not contain theta at all. I don't care about theta here. I care about the next prediction, solving the problem. But it so happens that I can't get to this distribution other than introduce theta, right? So the only way to actually compute this is to say, ah, okay, so I don't know about P of X given D, but maybe I know something about P of X and theta given D. And here is this joint probability. And here is this marginalization process, right? We are integrating the joint probability to get P of X. And now for this joint probability, yes, we can actually reduce it to what we know. So it's P of X given theta and D times P of theta given D, D theta. And now P of theta given D is our posterior, right? And P of X given theta and D, well, we have to recall our assumption. We had this assumption which always holds that data points are independent if you know the parameters, if you know the full model. So here also, if I already know the full model, then D doesn't matter, right? If I already know what is the probability of heads, then it doesn't matter what were the results of the coin in the past. If I know the probability, it will stay the same. So here, the first part is just P of X given theta. It's the likelihood of this single point. And that's it. So this is the predictive distribution. And in this case, even for this uniform prior, it will be different from just predicting zero. That's the interesting part. So P of heads given D, in our case, is P of heads given theta times P of theta given D, D theta, right? And it's like, what is P of heads given D? Well, just theta, right? It's the probability of heads given that the probability of heads is theta. That's the likelihood of one positive outcome. And P of theta given D, we actually, I think we didn't write it completely, but we did write the likelihood, right? So this is it. And P of theta given D is proportional to P of D given theta times P of theta. So it's proportional to like theta to the n 1 minus theta to the m on 0, 1 and 0 everywhere else, right? So we take the likelihood, we multiply it by the uniform prior, which basically just zeros everything outside here and does nothing inside here. And we get the posterior distribution. So it's theta times theta to the n 1 minus theta to the m divided, let's keep it like this, p of d, d theta. And what is p of d? p of d is just the normalizing constant for this. It's the integral from 0 to 1. Oh, and the integral is from 0 to 1 because elsewhere it's 0. So p of d is the integral from 0 to 1 of theta to the n times 1 minus theta to the m d theta. And here we get integral from 0 to 1, theta to the n plus 1. There is this extra theta here. Times 1 minus theta to the m d theta. And I won't do the math. It doesn't matter for us. We will never come back to it. But if you had a calculus class, you probably recognize this is the beta function. And you can express it as factorials. And then all of the factorials will cancel out, blah, blah, blah. I don't want to teach you about beta functions if you don't already know. And if you do, it's kind of easy. But the result here will be n plus 1 divided by n plus m plus 2. So there is this extra stuff here. This formula is called the Laplace's rule of succession. Pierre-Simon Laplace was one of the original founders of probability theory. That was one of the original results of the whole field. But whatever, it doesn't matter. The point is what the predictive distribution does, in fact. So if you look at this from a different perspective, it's the expectation over the posterior of this likelihood, right? Just by definition, what is the expectation? It's the integral, the function times the density, d theta. So this is like the likelihood averaged over the posterior distribution. And what does it mean in our case? Well, in our case, it means that we average over this purple distribution here. And yes, its maximum is at zero. This is the theta map. But its maximum is on this one side of it. And in fact, there is this whole triangle, right? So when you average over this distribution, you don't just get what you would get if you plugged in zero. You get something in between. Like it's not one, the average is not one half. The average here is like one third. But it's not zero either, right? So you average your likelihood over the whole posterior distribution, over all possibilities for the model parameters. And yeah, that's a lot to digest. But I hope that this coin tossing example is easy enough that we actually understand what's going on. Are there any questions at this point? I think there has been a lot of new information so far. Okay, okay. Yeah, I love the emojis. All right. So at this point, even on this very simple example of the coin toss, I have just one, I think, last comment left, and then I will show you a couple of plots, and then we'll end for today. So this kind of thing is what machine learning is actually about. So when you define a model, like when you... Sorry, where was it? Here. When you define a model, like I want to distinguish cats from dogs, what you actually are doing is you define a loss function. And the loss function is actually, almost always, either the log likelihood that you want to maximize, well, the negative log likelihood because for the losses you want to minimize, but it's the same thing. Or, even more often, it's the negative log posterior, which is... So if I write it in logarithms, I will see that, like, the log posterior is just the log likelihood plus the log prior plus a constant, right? That's what proportional is. So, again, in terms of the optimization, it doesn't matter, but it does matter in the sense that we are aiding the log prior, too. And the log prior is the regularizer. We didn't discuss it. We'll discuss it tomorrow where the regularization comes in. But regularization means putting a prior on the modal parameters. So introducing your own beliefs of what the prior actually was. Okay. And yeah, and I think I have to discuss one last point here. So this was all, the specific formulas that I wrote were only about the uniform prior. And as I said, it's not the prior that I actually have in mind when I'm talking about the coin, right? So for a real coin, it's some bell-shaped curve. I'm pretty sure it's close to one half. So of course, I want to plug in a more realistic prior here if I want to learn the Quintos. But to plug it in, I need to define it, right? So the question, let's say it's, what is the more realistic prior for the coin? And what is the most natural prior for a coin? What is, how do I define P of theta? Okay, and here the answer may surprise you. If you never thought about it before, the answer may surprise you because it sounds kind of lazy, but it's true. So the prior is a distribution on theta. We know that it should be zero here, zero here. No question about that. But what is the shape inside? My intuition says that it should be something like this. But there are millions and billions and, you know, a space with continual dimension of how many different functions look like this, right? So how do I choose a specific function? What will be this family of probability distributions that I plug in for p of theta? Do you know any distributions that look like this? Can you suggest some? Normal distribution. Normal, sounds good. On the surface. So with normal, you will have a problem right from the outset because the normal distribution will not go to zero, right? So the normal distribution is never exactly zero. It will be like something depending on the variance and then it will go down and then it will have some tails on both sides, right? So there will be tails. But okay, let's cut off the tails. We can do that. We can truncate normal distribution on the left and on the right. And we renormalize a little bit. It becomes a bit higher. But it's still like the normal bell curve over here. What happens next? So I need to write down the normal distribution. What is my P of theta? Well, it's 0 outside of 0, 1. And here it's some constant, which I cannot compute, of course. Times what? Times e to the power minus 1 over 2 sigma squared. Theta minus 1 half squared on 0, 1. Right? That's the density of the normal distribution. Okay. So far, not so scary. But what happens next? Next, I need to multiply P of theta times P of D given theta. And that's going to be, okay, inside 0, 1, it's going to be like C times this exponent times theta to the n times 1 minus theta to the n. That's my posterior distribution, the shape of the posterior. And then I need to maximize it. So I need to take derivatives. It sounds like it doesn't fit, right? So we probably can do it numerically, of course. I mean, it's a coin, it's dimension one. Of course we can do it numerically. But it sounds like some pretty inconvenient distribution for acquaintance. And what exactly is inconvenient? What is inconvenient is that the shape of the prior does not match the shape of the likelihood. The prior is an exponent, and the likelihood is a polynomial. And we multiply one by the other, we don't get anything meaningful. We get exponent times polynomial. So here is the secret here. I just want a bell-shaped curve. My intuition doesn't tell me if it's normal or student's T or whatever. So how we actually choose is we choose by convenience. We choose the shape of the prior that matches the shape of the likelihood, so that this multiplication becomes easy. And that, formerly it would be called the conjugate prior. Let's not get there. I will just give you an example, and we'll be done with it. So what would be easy to multiply? So the likelihood we cannot change. The likelihood is given by the process, by the thing that we are describing. So in this case, it's a coin. It has two sides, one parameter. So this formula is fixed. We cannot change the likelihood. But we can change the prior. And what would be easy to multiply by a polynomial like this? This is the likelihood. How should a prior look like so that it's easier to multiply by this? Okay, you're probably wondering exactly how easy. I didn't define that. But like, okay, so the prior, the easiest way, the easiest function to multiply by a thing like this would be another thing like this. Isn't that true? So let's say the prior is something like theta to the power of alpha, formerly alpha minus 1. That's just for formal reasons. Don't pay attention. Times 1 minus theta to the power of beta minus 1. And times a constant and the constant is a beta function, blah, blah, blah. Let's not get there. But as a result, I will get theta to the power alpha plus n minus 1. And I will get 1 minus theta to the power beta plus m minus 1. So the multiplication becomes trivial. But what is actually important is not that it's easy, but that the posterior again looks exactly like the prior. So the prior is what is called the beta distribution with parameters alpha and beta. And after I multiply by likelihood with n heads and n tails, I get the posterior, which is again a beta distribution. But with parameters alpha plus n and beta plus n. So when that happens, we call it the conjugate prior. You don't have to memorize that. But the point is now this calculation by the bias rule becomes trivial. I don't need to even think about the formulas. I just did it once. It's just adding up the exponents. That's it. Right. And now I can easily go from prior to posterior for any n and them. I don't need to do any new math. I don't need to run any numerical algorithms. I just plug it into this very simple formula where it's just addition. And the only thing that I need to check is that indeed this kind of prior can express what I want. Right. So that I can get a bell-shaped curve out of it. And yeah, I can get a bell-shaped curve out of it. So if I have, like, theta to the power 10 and 1 minus theta to the power 10, if the exponents are the same, then I will get a big peak at one half. So at this point, let me just show it to you in practice. Yeah, let me just show you the betas. So here is the family of the beta distributions. The uniform distribution is also beta, beta with parameters one and one. So it's theta to the power of one minus one and one minus theta to the power of one minus one. So it's just uniform. And then as the alpha and beta increase, I get like this more and more pointy distributions. The variance decreases. And if alpha and beta are equal, then I get the maximum at one half. In general, I get the maximum at alpha divided by alpha plus beta, just like the coin, just like the max-like. So the beta family does include what I want. It also includes a lot of other nice distributions that I can probably get as posteriors. And what does the actual Bayesian inference look like? Well, it looks something like this. So let's first begin with our example like we did in the lecture. So here is the prior, it's uniform. The likelihood for one tails is the orange line. And then I multiply it by the prior, and then I renormalize, and I get the posterior, which is the green line. So this is what I drew on the board. What if my prior was different? What if my prior had parameters like 2 and 2? So 1 and 1 gives you theta to power 0, 1 minus theta to power 0. 2 and 2 give you theta to power 1 times 1 minus theta to power 1. So it's a parabola like this, right? This is the prior, and when I multiply this prior by the same likelihood, I still tossed it once, I got one tails. Well, now it's a cubic curve, and it shifted to the left a little bit, and its maximum is at one third. Makes sense, right? And then I can continue like this. I can become more and more sure a priori that the coin was fair, and I will get like this more and more picky priors around one half, and the more convinced I am in advance that the coin was fair, the less this one experiment will matter. So if I was already very sure that the coin is kind of fair, like 50-50, the parameter is 50-50, then this one result of tails will not change anything. The posterior looks just like the prior. But of course, if I keep tossing it and I keep getting tails, it matters more. So 10 tails will shift my posterior to the left. This is the likelihood for 10 tails in a row. And if I get, I don't know, 100 tails, then I will probably shift it quite a lot. But still, the prior matters a lot to how much evidence I need to actually move my beliefs. Okay. Yeah. And since we are here, let me also show you this. So how it might actually work is what is another... like nice property of the conjugate priors? What is another nice property of a situation where your posterior looks just like the prior? Another nice property is that now you can reuse this posterior as the prior for the next experiment. So now I can do like sequential updating. I can say, well, all right, so here is my original uniform distribution. Then I tossed the coin once and I got heads. So the orange straight line is the posterior after one coin toss. Then I tossed it another one time and I got a tail. So now this parabola is my posterior after two coin tosses. And when I toss it three more times, I don't have to go to the beginning. I can say, all right, so now I have this parabola after two coin tosses. Let me just multiply that by the likelihood of the next three. Like one heads and two tails, I think in this case. And this is the result. And so on. So I can forget about the previous dataset, just take the posterior and plug it in as the prior for the next update. So it can work like this. I start with p of theta, then from a dataset I get p of theta given d, and then I get another dataset, more data. And I want to go to p of theta given d and d prime, right? I want to unite all of the data and use all of the data. And basically, if I have a conjugate prior like this, I can just say, all right, so I did the math here. I can forget about this part. Now, this is my new prior, this is my new data set, and I get to the posterior, and of course, formally nothing changes. So, it's the same bias rule, only it's d on the right in every probability. It doesn't matter. But if I didn't have a conjugate prior, then it would just be very difficult to do. So, it would be easier to just start from here and do the whole computation with d and d prime. But if I do have a conjugate prior, then I can use it. And maybe one final thing to show, here is a coin toss that I, a sequence of coin tosses and the sequence of probability of heads that I have learned. And the probabilities of heads change as I go. And the blue line is the maximum likelihood hypothesis. And the orange line is the Laplace's rule. So it's this smoothed out n plus 1 over n plus m plus 2, the predictive distribution, the predictive probability. And as you can see, it's just as we expect, right? So in the beginning, the Laplace's rule is less extreme than the maximum likelihood. So after one toss, this is either 1 or 0, and this is either 1 third or 2 thirds, so much closer to 1 half. And it will, like, moderate these extremes of the max likelihood, but then after, like, 50 tosses, they're in distinguishing. So one converges to the other, and they both converge to the true probability. And we can do other random experiments here. It's, of course, the same. So, okay, so let's summarize. I think I'm already over time here. What we did today, this is Thomas Baez, the Reverend Thomas Baez from 1760-something. So, but actually, yeah, there is a famous story that this portrait is actually fake. It's not Thomas Baez, and nobody knows who that is. Okay, you can read it. Anyway, so we discussed the Baez theorem and how it is used in machine learning. We discussed the most important, not just the most important, we discussed basically the only problems that we are solving in machine learning. Like, what does it mean to learn something? Well, it means to say something about the parameters of the model, and you can just maximize the likelihood. But as we have seen today, it probably usually makes more sense to get the full posterior distribution if you can, and then maybe maximize it if you have to. And, yeah, tossing a coin, blah, blah, blah. Yeah, this is what we discussed. I will get to a couple more examples tomorrow. Conjugate priors we discussed. This is the beta family. Yeah, I think this is it. This is the Laplace's rule. You can read it up on the slides if you want. Where is the predictor? Yeah, yeah, for example, here. And the last problem, the most difficult problem, is to get the predictive distribution, is to get the next, the distribution of the next element of the data set, predict the next coin toss, given what the data set is telling us, regardless of the specific value of theta, which means you have to average over theta. And we did it with the example of the coin. Hopefully went through this whole example. I skipped a couple of minor details that don't affect the machine learning understanding. But overall, we've completed the coin toss example. Naturally, you can also extend it to die rolling to several different outcomes. It will be exactly the same. Maybe we'll talk about it tomorrow. But at this point, I think I will stop here. Are there any questions? - Yeah, I have a question. Can you remind, please, maximum likelihood and Laplace rule. Laplace rule is the optimization of prior multiplied by likelihood and maximum likelihood also. - So Laplace rule is the predictive distribution. So let me repeat it again because this is really important. So you have the bias rule, right? The bias rule connects the likelihood, the prior, and the posterior. The model itself is usually the likelihood and you can maximize the likelihood directly and you get the maximum likelihood hypothesis. If you add the prior, you get the posterior and you can maximize the posterior and you get the maximum a posteriori hypothesis. But what you really want, it's just that often it's impractical to get, often you can't get it, but what you really want is the predictive distribution. The next x given d. And there is no way to compute it usually, except like this, right? So like the expectation over the posterior of this next item likelihood, okay? And the Laplace's rule was about this. So the Laplace's rule said that P of heads given n and them, given D is n plus one divided by n plus m plus two, if you have a uniform prior. While let's say theta ML was given us n over n plus m, and theta MAP was also given us n divided by n plus m. This is all for the uniform prior. Okay, more questions? - Sorry, yeah, another question. - Sure. - Okay, first of all, about the same topic. So, for example, in econometrics and financial econometrics where we use time series, it is very common. Well, every time we build the model to predict the next, how do I say? - Yeah. - Out of value based on inputs from the previous period. So it is a very common problem. - Sure. - Why is it such a problem here? Is it the difference between time series and unordered observations like here? Or is it the difference of frequentist versus bias approaches? - There is no difference. I mean, it's just a different problem setting, but you will still need to convert it to supervised learning probably, right? So in reality, I mean, yeah, maybe formally your time series goes to negative infinity, but in reality, it doesn't, right? So in reality, you will have your data set, sorry, your data set in time series analysis will still look like pairs of Xs and Ys. And how do you define the Xs? Well, that depends on your model, of course. So maybe you do a sliding window, right? So maybe you say, okay, I look at the previous, so many ticks, and I predict the next tick based on this fixed context. Then your X is this, or you can say, well, let me do, I don't know, a recurrent neural network. If I have a recurrent neural network, then it means that what my recurrent cell is doing is it's getting my current X and the hidden state H. And we are predicting, let's say, okay, actually we are outputting the next hidden state, but we are also, let's say, predicting this Y over here, right? So we will talk about recurrent neural networks when we get there, but here also, you compress your context down to this state vector H, and this is your input and you want to, and then you get your output, and so on. So I don't feel there is any difference specifically. So yeah, time series sometimes are a little bit special, but I think not in econometrics. I think they're special when they're really, really long, like in sound analysis, when you have millions and millions of ticks, you don't want to treat them as just a time series, maybe you want to do Fourier transforms, look at the spectra, etc. And then it becomes a different science. But I think in econometrics, it's just supervised learning. - Another question about the notebook that you showed. So the second-to-last graph, can you show it again, Grace? - This one? - Yes. So, for example, when n equals to five, sorry. - No problem. Yeah, when n equals to five. - So we can reduce the, how do I say, our prior component is the result that we got on previous step. - Yeah. - So is there a difference in the result going step by step? - No. - Or just using five observations from our initial expectation, which is the same? Exactly the same, that's the whole point, yeah. So, of course, for a coin, I mean, it doesn't matter. You're not saving anything. Going straight from the beginning is just as easy. But if you had like a big data set and you could compress it down to the posterior distribution, maybe now you can forget about the data set. That's maybe a good thing. You don't need to go over it again. I mean, for a coin, yeah, you're not saving anything because for a coin, the data set reduces to two numbers. numbers so it's it's not like you can be more efficient here yeah absolutely so what I will do what I always do is I will make a web page for the class or you and it will have the videos it will have the boards it will have the notebooks um and it will be unfortunately a secret web page for the harbour space university so I am not allowed to post it in public but I will send you the link in google classroom also if it's convenient for you we can make a telegram chat for the class I think we don't have one but it it would be really convenient for me but if if that's not good for you then google classroom is fine too okay so thank you and see you tomorrow judging by your questions I think you did learn something new today thank you see you tomorrow thank you
