# Transcript — google_stt

- **Provider:** google_stt
- **Language:** en-US
- **Audio duration:** 3:19:09
- **Segments:** 1404
- **model:** latest_long
- **use_enhanced:** True
- **latency_sec:** 1651.1

## Segments

**[00:11 – 00:13]** Good morning everyone. Welcome

**[00:14 – 00:16]** to the second day of our class and

**[00:17 – 00:25]** I suppose, I hope the first day was interesting today, we will definitely started deep learning although I do have

**[00:26 – 00:35]** A few things to tell you before that but then at least in the second half of the start talking about neural networks, no way around that.

**[00:36 – 00:37]** so,

**[00:38 – 01:06]** to get the technical organizational stuff out of the way. I sent a message to Google Classroom. I hope you've seen it. I made a webpage secret webpage with which probably we are now suppose to link to externally, but and that's just for you. I made a web page with all class materials K-pop loading videos,

**[01:08 – 01:09]** flights board.

**[01:11 – 01:13]** So, I hope you like it.

**[01:14 – 01:15]** and with that,

**[01:16 – 01:16]** let's continue.

**[01:18 – 01:40]** Yesterday, we talked about the general idea of what learning is of how we can formalize and understand what it means. For say, machine learning model to actually learn something and we framed it in

**[01:43 – 01:55]** In the probabilistic by Asian framework and basically it was like most of yesterday's discussion or Central round the base roll.

**[01:55 – 01:57]** Around this.

**[01:57 – 02:03]** Famous formula which is the most important formula in the entire machine learning.

**[02:04 – 02:06]** But yesterday.

**[02:07 – 02:08]** we talked about,

**[02:11 – 02:29]** A very simple example, we were just talking about the coin toss and I actually want this introduction to go to the linear models because they are very directly relevant to what we do in deep learning and what neural networks actually do. So

**[02:30 – 02:31]** Let me.

**[02:32 – 02:42]** Apologies, but let me continue with this probabilistic introduction still, I hope it's important. Well, I'm sure it's important, but I hope it's interesting for you.

**[02:43 – 02:55]** So we discussed the bistro yesterday and just as a quick reminder, the main idea of this formula is that

**[02:57 – 03:32]** Is to answer the question of how should we update our beliefs when we learn new information and we get new evidence, right? So in a more General more general terms D would be not specifically dataset for machine learning, but it would be just any kind of evidence and fate would be like our beliefs, our hypotheses about the underlying process or whatever. And then when we get new evidence, we update what we

**[03:33 – 03:51]** What we believe, right? And that's in a way, how life works, right? That's, that's how our brains are supposed to work. No, not always. They work. Exactly in this way. And of course, we don't consciously do any calculations like this, but the general lessons is exactly this.

**[03:52 – 03:56]** And we discussed three.

**[03:57 – 04:50]** Main problems of machine learning where the optimization tasks come from. So, you can start with the likelihood and end right there and just maximize the likelihood that doesn't make any use of Asian inference. So, it's non-bias and Method. But still if you have lots of data or if your model is already very complicated and a prior distribution would make it completely unfeasible though? I can't imagine why still? You can just maximize the like, then you can multiply the likelihood by the posterior will see by the prayer. Will see, very specific examples of that today. In real world, real life models. Not just point us

**[04:51 – 05:04]** And then maximize the result, which will be proportional to the posterior distribution, right? That's that's what we discussed last time and we discussed the coin torsion example in great detail.

**[05:04 – 05:13]** And maybe. Yeah, in the third problem would be the predictive distribution, which I don't think we'll get to today. So let that stay at the level of the coin toast.

**[05:14 – 05:59]** And we discussed the going to as an example in great detail yesterday. So we kind of went through the all of this problems went through the notion of likelihood prior posterior with it. All means completely finished the simplest case of a uniform prior and then discussed what the more informative more reasonable prior would be like, if I do want to have a bell shaped curve and how do I choose among them? And the answer was the one that's convenient, which has, which may sound like an unsatisfactory answer. But there you go. It's it's about, it's our choice. It's about our beliefs. So actually in

**[06:01 – 06:21]** More involved cases like linear regression. That we will discuss. Now, the reasoning is exactly the same. You chose the prior not due to some principled trees, and like, you understand it, for these process, the prior should be this, but you choose your prior.

**[06:24 – 06:30]** Either for convenience or because it leads to desirable properties. We will we will see how it works.

**[06:31 – 06:32]** and,

**[06:36 – 06:36]** The.

**[06:38 – 07:22]** Another thing that I wanted to mention here, I will I will not spend much time on like real world examples or anything, but I do want to mention some kind of, you know, philosophical underpinning of all this, right? And I mentioned yesterday, that if you open an old book and probability Theory, a very good book, but an old book and probably Theory, you will see probability introduced, like, well, there is this infinitely repeatable experiment, we do the experiment, we get some results, and then we divide the results, the number of outcomes that we are interested in by the number of total experiments and that ratio tends to the probability

**[07:23 – 07:32]** that is completely correct when applicable it's completely correct. And for the coin toss, it's exactly how we Define probability.

**[07:33 – 07:33]** but,

**[07:34 – 08:00]** In real life and the special in machine learning. That's why I'm talking about this. We usually want to reason about the probability of events that are definitely not repeatable experiments, right? So, for example, if your bookmaker, you need to predict the probability of, to set the probability of Spain winning the FIFA World Cup this year.

**[08:01 – 08:13]** And there will be only one World Cup and no it's not the repeatable experiment based on previous World Cups because obviously the teams were completely different. Everything was completely different

**[08:14 – 08:24]** or we even might want to set probabilities for events. That already happened that all are already said but we just don't know the answer.

**[08:27 – 08:27]** and,

**[08:28 – 08:30]** In this kind of cases.

**[08:30 – 08:56]** It makes no sense to talk about experiments repeated to Infinity, right? For example, there is a hypothesis and not sure about the current status, but last time I checked, it was a hypothesis that the Odyssey by Homer was not created by the same Homer as they had, but was written by a woman for you to some electric analysis of the text. And it's a hypothesis, we don't know. But

**[08:57 – 09:08]** It makes sense for us to want to assign probabilities to hypothesis like this, right? Although there is only one, what is and it was written by somebody thousands of years ago and

**[09:09 – 09:12]** the answer is already set but we just don't know it.

**[09:13 – 09:13]** so,

**[09:15 – 09:29]** The point is in real life probabilities are often not limits of ratios of experiments, but they are degrees of belief. They are representations of our uncertainty

**[09:30 – 09:37]** and this is actually a very useful, I think framing to think about probability and the Very

**[09:38 – 09:44]** useful way to understand what what we are doing. We are not

**[09:45 – 09:54]** actually, well, when you do machine learning, for example, when we use this, with the real data set and a real model we are not

**[09:55 – 09:58]** Getting some kind of.

**[09:59 – 10:24]** Logical conclusion, right? We are updating our beliefs. And if we have a good data, set, a large enough data set, then our beliefs can become much more. Certain we can become, I don't know the confidence. Intervals May shrink, we can become more sure in the hypothesis that we are evaluating

**[10:25 – 10:37]** But we will never be completely sure right? Especially in machine learning, when it's all about noisy data sets are the thing is? We are

**[10:38 – 10:46]** Combined, we are combining all of the evidence to understand something about the model model parameters. In this case,

**[10:47 – 11:07]** But there is always a probability distribution. And this is a point that often gets lost for people because what you actually do in reality, and Let Me Maybe immediately so that, you understand in advance where we are driving with this. Let Me Maybe immediately

**[11:09 – 11:13]** get you the general notion of what we are doing today. So,

**[11:14 – 11:15]** We are.

**[11:16 – 12:05]** Using this identity and we are reasoning by the best role but what we are actually doing, for example, in deep learning practice all the time is we compose a loss function, right? So we compose a loss function. Like log P of D given theta plus log P of theta and actually take minus because the loss function you want to minimize not maximize but in practice this is the loss function for your neural network, right? We will see how it works specifically today. And then you minimize it with respect to Theta, with respect to the neural network parameters and you get the map, right?

**[12:06 – 12:10]** So Theta map is the arc mean of these.

**[12:12 – 12:15]** The maximum upper stereotypical hypothesis, right? So it's the arc Max

**[12:16 – 12:18]** of P of fate and giving the

**[12:19 – 12:25]** and very often people when they think about deep learning about neural networks, they kind of

**[12:26 – 12:32]** Stop here and the process desktop here and then they say, oh now we know Theta.

**[12:33 – 12:38]** Now, we got, we got our model checkpoint. Here are the weights here are the true weights.

**[12:40 – 12:40]** That is.

**[12:41 – 12:53]** An oversimplification, right? So yes, in practice very often, we will do exactly this. And we will use Theta as a point estimate, but it's very helpful to

**[12:54 – 13:02]** Remember that Fatima is just a point estimate, right? It's just the maximum of a whole distribution.

**[13:03 – 13:22]** And in deep learning with huge neural networks Etc, we usually cannot do that. But if we could, it would be very helpful. Usually to actually at least sample, several different points from this distribution and see how that translates into different predictions.

**[13:23 – 13:30]** Actually, sometimes you see this in deep learning because as well, right? So,

**[13:31 – 13:37]** All of this Machinery is about degrees of belief. It's about our uncertainty.

**[13:38 – 13:48]** Our original uncertainty captured in P of theta and then reduced by D by the data that we get. And ultimately,

**[13:49 – 14:03]** our new uncertainty capture it in P of theta given d, right? So, we know something about the parameter, set cannot be that we know, absolutely nothing. Well, sometimes it can, but still be. We need to express it in the distribution then.

**[14:06 – 14:19]** We get new information we update and we have some new belief about data, but it's it's a distribution, it's an uncertain belief. It's never a just a single point. This this is what I wanted to say here.

**[14:22 – 14:22]** and,

**[14:24 – 14:28]** yeah, and also I usually go through some

**[14:29 – 14:41]** Relatively straightforward examples of applying the Bass Pro. Let's maybe let's try it with you. So here is a very standard, like trick question from probability Theory.

**[14:44 – 14:52]** I personally have two kids. Let's say my acquaintance has two kids, but I've never met them. I don't know, their names, I don't know, their generals.

**[14:52 – 14:54]** And let's assume that.

**[14:55 – 15:09]** Every baby is either a boy or a girl with probabilities one-half and the first baby is independent from the second so they're just there. Each of them is a Fair coin to us in terms of whether it's a boy and or a girl.

**[15:10 – 15:20]** And then I go to this person and ask. Hey, do you have any voice like, among the two children that you have? Are there any boys? And he says, yes,

**[15:22 – 15:25]** in this setting, what is the probability that he has a girl?

**[15:35 – 15:35]** How many?

**[15:36 – 15:39]** How did you arrive in this?

**[15:45 – 15:46]** You know.

**[15:56 – 15:59]** Any other ideas?

**[16:05 – 16:08]** So what what's the probability of space here? Like what are the possible outcomes?

**[16:15 – 16:17]** Mmm, also not quite true.

**[16:23 – 16:41]** Okay, yeah, this, this is a straightforward precaution, but yeah, it would usually fall into the trick unless, you know it. So the, the person has two children, right? So it's like, child number one and child number two, right?

**[16:42 – 16:48]** For every child, there are two possibilities two options, right? So, how many options are in total?

**[16:52 – 17:03]** For exactly. So we have like a boy boy boy girl girl boy and girl girl. Right? So there are four possibilities and

**[17:04 – 17:15]** In the prior before I get any information there, completely, right? So we get one fourth for this one force. For this one, fourth, for this one for this, right?

**[17:16 – 17:24]** So now when I asked, do you have any boys and he answers? Yes. What information do I get? How does this table change?

**[17:30 – 17:37]** Yeah, precisely. So now the last line cannot happen.

**[17:39 – 17:43]** But the restore can happen, and the answer is not distinguish between, right?

**[17:44 – 17:58]** So as a result, I now have three options, they are still equal and probability but now I have three options and no two of them.

**[17:59 – 18:00]** Have a girl, right?

**[18:01 – 18:03]** So, the probability is actually the thirds.

**[18:04 – 18:12]** And if you want formerly, then you just need to compute P of, you know, there is a girl. Give them that.

**[18:14 – 18:37]** Give them the there is a boy, right? So it's like the probability of these two scenarios and if or FM divided by the total probability of that there is a boy of m m f or FM and that comes to the thirds, right? So formerly it's like

**[18:39 – 18:44]** Two quarters divided by 3/4. If you go straight to my definition,

**[18:46 – 18:47]** all right.

**[18:48 – 18:57]** But here is the second question now, I've met one of his kids, so it's separate question. I didn't ask the first one so I don't know that.

**[19:00 – 19:01]** and,

**[19:02 – 19:05]** Now, I've met one of his kids and it's a boy.

**[19:06 – 19:14]** So now I know that one of the kids is about and I've met this, this boy, what is the probability that the other one is a girl.

**[19:16 – 19:22]** Yeah. And now it's one half, right? So now if when I meet

**[19:23 – 19:34]** Some one of his children then it means that. Now, it doesn't matter if it's number one or number two, but it means that I kind of fix the value of one of these columns.

**[19:34 – 19:46]** So now, I eliminate not one, but two lines, for example. Number one is a boy, which means that now only two outcomes remain, and they are equal, etc. Etc.

**[19:48 – 19:48]** so,

**[19:50 – 20:16]** It, this is an easy trick question but it's already shows how in probability Theory and bias. And recently like this, notice that, although we didn't really use the BIOS, theorem it's actually the same kind of reasoning. We get some prior beliefs that everything is equally probable. That's our original assumptions. And then we get evidence, and then we update our beliefs based on this evidence, right?

**[20:18 – 20:44]** And but there are also a couple of more interesting examples. Let's discuss them with you to since the first one I think went well this are again very well known for this fallacy may have heard about them but they are very instructive in like the pitfalls but potential pitfalls of the best role. So let's okay. Here is the Satan a murder has happened.

**[20:45 – 20:48]** And we are in the court of law are in about the murder.

**[20:49 – 21:04]** So there is some blood left on the crime scene and we know 100%. So don't think about that assumption. We know for certain this is the Killer's plot. Okay. So this is probably one you don't need to question that.

**[21:05 – 21:19]** And it's so happens that the blood type is quite rare. Like, let's let's assume it was a time before DNA tests. So we cannot like directly check which person it is but it's a rare blood type.

**[21:19 – 21:26]** And only 1% of the population, only 1% of people actually have that blood type.

**[21:27 – 21:28]** And it just so happens.

**[21:29 – 21:34]** That the defendant the guy who is being accused of the murder.

**[21:35 – 21:36]** So has this what type?

**[21:37 – 21:37]** Right.

**[21:38 – 21:38]** so,

**[21:39 – 21:41]** the prosecutor comes out and says, well,

**[21:42 – 21:46]** The chance that the defendant would have this blood type of, he was innocent is only one percent.

**[21:47 – 21:49]** So, with probability 199%, he is guilty.

**[21:52 – 21:54]** Is the prosecutor correct? This.

**[21:55 – 22:01]** I suppose the question on the slide tells you that he is not, but what's the mistake?

**[22:03 – 22:04]** What's the problem with this kind of reason?

**[22:30 – 22:34]** I think it's the specific way. How the like

**[22:35 – 22:38]** The statement has been proposed here, maybe.

**[22:39 – 22:39]** like,

**[22:40 – 23:15]** Is equating the probability of like having the blood type like given innocence versus probability of actually being in Northern given the blood type something that. Exactly. Yeah. You nailed it. Exactly. So this is this is a classic mistake that happens all the time in real life you see people to make it all the time and because our brains are not really wired by Evolution to do probabilistic reasoning, especially with numbers. And yes, you your answer was completely entirely correct with repeated for everyone. So we have

**[23:16 – 23:24]** So what are we actually trying to do in the court of law? Yeah. Trying to establish like P of guilty.

**[23:25 – 23:26]** Given the evidence.

**[23:27 – 23:28]** All right.

**[23:28 – 23:36]** And if it's very, very high, then we can be convicted, right? It's probably never going to be exactly one, but if it's very high, then we can make the person

**[23:36 – 23:38]** Are.

**[23:39 – 23:43]** And so the prosecutor makes a conclusion. Exactly about this.

**[23:44 – 23:49]** So here's a final point, the 99% is about P of guilty.

**[23:50 – 23:53]** Given the blood type.

**[23:54 – 23:54]** Right.

**[23:55 – 23:57]** But what he starts with

**[23:58 – 24:05]** is not P of you of innocent. Given the blood type, it's the other way around. It's p of blood type.

**[24:06 – 24:08]** Given that the person is.

**[24:10 – 24:10]** Right.

**[24:11 – 24:15]** And yeah, so when the prosecutor

**[24:16 – 24:24]** Estimates this probability is completely, correct, right. So like one, it doesn't matter, like almost everyone is so we can say that this is also 1%. That's fine.

**[24:26 – 24:27]** but then,

**[24:28 – 24:32]** The prosecutor says. Well, all right. So this equals to one minus this.

**[24:33 – 24:43]** And now this conclusion is completely wrong, of course, right? So the prosecutor equates like P of a given B.

**[24:44 – 24:45]** with P of B given a

**[24:46 – 24:53]** in a way. And that is, of course, not right. When I write it like this, it's obvious that it's wrong, but when it's stated in the words,

**[24:54 – 24:58]** Yeah, people you missed missed this kind of mistakes all the time.

**[24:59 – 25:14]** And what would be the actual formula? Of course, it would be the best rule, right? So in actuality, like, P of blood, okay? Let's do it. The other way, around P of incentive given blood.

**[25:15 – 25:24]** Would be like P of blood given innocent times P of innocent divided by P of what.

**[25:25 – 25:26]** Right. And

**[25:27 – 26:03]** Of course, these priors this prior and this evidence probability could completely changed things, so I'm not going to try to invent any numbers. It doesn't make sense for this example, but for example, suppose that there are two possible suspects and it just so happens that both of them have right. If that happens then of course the blood types tells us nothing right? It does not help us distinguish between them and the probability remains to be one half but the prosecutors

**[26:04 – 26:06]** A reasoning would be.

**[26:07 – 26:10]** Would not change in this case.

**[26:10 – 26:21]** So, the prosecutor would now make like the obviously absurd conclusion. That both of the suspects are guilty, each with probability, 99% issues, of course, from

**[26:24 – 26:27]** Okay, so this is the prosecutor's mistake.

**[26:27 – 26:46]** And then the defense attorney comes out and comes on the. What's the word understand? Yeah. And the defense attorney says well. Okay, so first, he explains what the mistake of the prosecutor was and then he says, well, okay, let me offer my own calculation. There are a million people living in the city.

**[26:47 – 26:55]** and yeah, of course, having this rare blood type Narrows and down from a million to only about 10,000,

**[26:56 – 27:16]** Right. And that is correct. So all the blood type tells us is that the defendant is guilty with probability like 0.01%. So, yes, sure, it's kind of evidence but it's very, very weak and it's definitely not any kind of proof. Let's just not admitted to evidence at all.

**[27:19 – 27:24]** It's also doesn't sound right, right. So what's, what's the defense attorney's mistake?

**[27:34 – 27:58]** I mean is mistake is like probably stating that everybody who has the blood type is equally likely to be the killers. So so, basically not even focusing on why the defendants there in the first place. Yeah, exactly. So in this case it's not really some deep mistake and probabilistic reasoning, it's just the mistake and the Assumption, right? So yeah, it would be true but he says if

**[27:59 – 28:07]** Everyone of these 10,000 people including I don't know people who are sleeping at the time and babies and everybody in the city.

**[28:08 – 28:17]** Would actually have an equal chance of committing this murder, but that's obviously not true in real life. So they defendant is there for some reason right? Yes. So yes you're completely right?

**[28:18 – 28:22]** And yeah, and these kinds of mistakes.

**[28:23 – 28:24]** Happen all the time.

**[28:25 – 28:47]** And there there was a very famous case which you might have heard about the case of OJ Simpson, he was a very successful football player, American football player in the 1980s. And then he had well here he had some very difficult relationships so to speak with his wife,

**[28:48 – 28:50]** And ultimately, the wife was found to be killed.

**[28:52 – 29:00]** And OJ Simpson was straight from her. It was like one of the most publicized Trials of the 1990s.

**[29:01 – 29:29]** And it was a long trial. There were lots of, there was lots of evidence, lots of discussions, will not go into that, but there was one specific point that exactly matches our discussion on the BIOS. And at some point, the attorney of ocean. Sorry, the evidence was that OJ Simpson. Already had a history of violence with his wife. Basically, he bit her up a few times before.

**[29:30 – 29:30]** and,

**[29:31 – 29:51]** The prosecutors, they proved this. This was true and they kind of submitted it to the jury as not reproof, of course, but there's evidence that OJ Simpson can actually go to far in another episode and the wife can get killed

**[29:53 – 30:13]** Ah, so the attorney came up came out and said well, okay, my defense. My client is a very bad person. I do not dispute that. It's, it's it's, it's very bad to be happy for your wife and definitely, he shouldn't be doing that. But we are at a murder trial.

**[30:14 – 30:25]** And as for the murders there is a statistic that says well only one of 2500 women subject to domestic violence actually get killed.

**[30:27 – 30:30]** And he concluded that this is Irrelevant for the murder.

**[30:31 – 30:33]** Right. So

**[30:35 – 30:48]** And what, what I mean, it's of course, it's the defense attorney's job to make arguments like this even if they're copiously wrong. But what what's the, what's what's really interesting about this is that the court actually agreed

**[30:49 – 31:04]** So the court in this very famous, very public, OJ Simpson's case agreed that this is a good reason to say that the Mystic violence has no relevance to the murder and, you know, like they do it. The jury was instructed to District guard, the seventh blah.

**[31:05 – 31:16]** Um, but of course, this is exactly the same kind of mistake, right? So, in reality what,

**[31:17 – 31:25]** They were supposed to be evaluating was P. Okay, so let me start with the statistic, the statistic was

**[31:26 – 31:32]** What is the probability of murdered given a history of violence?

**[31:33 – 31:38]** And okay, the statistic was correct. So that was like one hour 2500 that's that's true.

**[31:39 – 31:43]** but that's completely not what was

**[31:44 – 31:52]** being what we what people are trying to establish, right? So this kind of statistic starts from

**[31:54 – 31:54]** The.

**[31:55 – 32:08]** Point in time when nobody is murdered, right? It's starts from from the point where everybody is alive and well, and then evaluates How likely it is to be murdered. But

**[32:09 – 32:11]** The court case, I remember case.

**[32:12 – 32:22]** Argus in the opposite direction, right? So what we actually want to know is what is the probability of being murdered by your husband?

**[32:24 – 32:46]** Sorry about this Glory topic. But you know, this is still the most famous case of this of this policy given that the murder was has already happened and there was a history of domestic violence. Right. So, of course, the, the main thing is that the murder has already happened. And we are just trying to establish who did it.

**[32:46 – 32:54]** so the vast majority of this case of this 25,000 cases in the vast, majority of them, nobody got murdered

**[32:54 – 33:00]** so they don't matter, right? They don't, they're not included into this conditional probability.

**[33:02 – 33:20]** And if you actually take the exact same statistics, here is the punchline. If you actually take the exact same statistics, that was available at the time and you compute the correct probability from it, is you estimate the correct probability? It will come. I may be slightly mistaken but it will come to something like seven or eight.

**[33:22 – 33:30]** So like among the women who were the history of the Mystic violence in the vast majority of cases,

**[33:31 – 33:32]** The husband did it.

**[33:33 – 33:34]** and,

**[33:35 – 33:41]** Uh, so of course, if evidence was presented in the correct way it would look completely different, right?

**[33:41 – 33:42]** so,

**[33:43 – 34:17]** This is just an illustration that people do make mistakes like this, and it's probably just a good habit in life to actually understand what exactly you're trying to estimate. What is I mean in life? All that we do everything that we do to make decisions is estimate various conditional. Probabilities if I do this, what is the probability of my preferred outcome? And if I do that, what is the risk of this and that and it's

**[34:18 – 34:26]** It's it's it's a good habit to actually explicitly understand. What exactly is the probability that you're evaluating even?

**[34:27 – 34:49]** If you cannot really value it, right? So in real life, we don't have this kind of Statistics. We can run the numbers, of course. But if you at least qualitatively understand what is the direction that you're trying to predict, what is on the left of the vertical bar, and what is on the right of the vertical bar? Thanks become more clear and in many cases,

**[34:51 – 34:56]** Okay, so that was the leftover that I wanted to mention.

**[34:57 – 34:58]** and now,

**[34:59 – 35:38]** We proceed to our first real example and now this I will make two examples today linear regression and logistic regression. We will not discuss them and too many details but I do want to discuss them because they are directly relevant to what's happening in neural networks. That's like the simplest possible. Neural network is a linear model like this neural network consisting of one perceptron and it's not only that, you know, it's the simplest model and modern neural networks are completely different. No linear regression. Logistic regression is still directly relevant. What's happening in them. I will explain why.

**[35:39 – 35:40]** so,

**[35:42 – 35:57]** I hope that you all have some kind of intuition about what linear regression is, maybe you don't, maybe you can remember the formulas. That's fine. Maybe you don't, I don't know maybe you never studied it like systematically, but

**[35:58 – 36:02]** This will be our Point number two, linear regression.

**[36:05 – 36:21]** But at least you have this, you know, General picture in your mind that a linear regression is a problem like this. You have X over here if you have the target variable y over here, there are some data points like this.

**[36:22 – 36:27]** and you make an assumption, you say the data points are probably

**[36:28 – 36:30]** In a linear dependence between X and Y.

**[36:32 – 36:40]** But we don't know the dependence and there is noise so they are not exactly on the same straight line. They are close to straightly

**[36:41 – 36:46]** Right? And they the problem of linear regression is to find the straight line.

**[36:47 – 36:50]** basically, this is the intuition that

**[36:52 – 36:53]** I hope you'll understand.

**[36:54 – 37:07]** So, if I write it down as a formula, I mean, obviously can only draw you two-dimensional pictures. So X will be one dimensional what I draw. But in reality, of course, we are usually talking about

**[37:10 – 37:13]** Single way. So the target variable is a number.

**[37:14 – 37:18]** Or less always. But this number is

**[37:19 – 37:36]** Not just w0 plus W1 times x but there are many axis, right? So in reality x is a vector. Usually and there are and we model y as a linear combination of excess.

**[37:38 – 37:41]** okay, so before I even begin,

**[37:42 – 37:47]** talking about it in detail, one, very simple, remark that will help us make things easier.

**[37:49 – 37:54]** I will actually skip the intercept.

**[37:55 – 38:14]** So I will actually write y as just W Times X and this, this means transposition and this means just scale or the product of the vector W. And that's so like that W1 WD times X1 XD.

**[38:15 – 38:18]** Why, why can't I escape the interest?

**[38:19 – 38:25]** Why can I forget about double zero? Like in practice, it's not 0 right here. It's not 0.

**[38:38 – 38:41]** Yeah, precise. Okay. It's good that you know, the stuff

**[38:43 – 39:06]** I to be able to skip the intercept. I just add one more Dimension. I had a fictional Dimension. Let's say x0 is just one like you said, it's a new feature, a constant feature. And then I take my Vector X and I map it to like one and then X like a vector, which is one dimension longer.

**[39:07 – 39:10]** and now, suddenly

**[39:12 – 39:36]** When I do a linear function when I do it direct product. In this Vector, I get the intercepts for free, right? So this is a standard trade, that's that's why we don't need to always add this double zero here which would make the formulas, much more. Oh, it won't make it more complicated but would make much more cumbersome.

**[39:37 – 39:39]** Okay.

**[39:40 – 39:40]** so,

**[39:42 – 39:46]** why should be similar to a linear function of excess?

**[39:47 – 39:57]** And maybe, you know, I mean again if you ever studied any linear regression, probably have an idea. How do we Define this being near to

**[39:58 – 40:05]** What what, what is what do we mean by this approximation?

**[40:07 – 40:11]** What are we actually? How do we formalize linear regression user?

**[40:14 – 40:16]** You minimize the.

**[40:17 – 40:22]** engineering measurements between the actual various and

**[40:22 – 40:23]** prediction of

**[40:24 – 40:27]** Yeah. And what is the most common error?

**[40:34 – 40:52]** Yeah, exactly. So the standard way to do linear regression and again, notice I haven't yet read on any probabilities will get, there is okay. So what does it mean that I want you to be such that? Why is approximated by W Times X? It means that

**[40:53 – 41:00]** my predictions. So, here are the excess, right? The access in the data set.

**[41:02 – 41:03]** and,

**[41:04 – 41:18]** My prediction in this access are points on the straight line, right? So this this is what my model creates. This is W Times X and over here and

**[41:20 – 41:24]** What does it mean that the straight line is closed? It means that these distances are small.

**[41:24 – 41:27]** right, it means that I want

**[41:29 – 41:34]** the total sum of these distances to be as small as possible makes sense.

**[41:36 – 41:38]** And usually, like you said,

**[41:39 – 42:03]** The loss function in linear regression is defined. So I said that I wanted this to be small, but I didn't hear Define what exactly what is the exact number that I want to be small. And usually it's exactly the square distance, right? So usually, it's the sum of Y, minus, double y and x minus W Times X and squared.

**[42:04 – 42:08]** And standard linear regression, minimizes this with respect to W, right?

**[42:09 – 42:11]** Well, here here is a question.

**[42:12 – 42:12]** Why?

**[42:14 – 42:15]** Where does this come from?

**[42:16 – 42:18]** If you know, you can speak up and tell.

**[42:21 – 42:22]** or if you have an idea, why

**[42:23 – 42:56]** So, obviously, I do want this distance to be as small as possible. That's that's right. Obviously, I do want, I don't, I cannot just add up distances as they are because they have science, right? So I don't, I don't want this to be symmetric. I don't I don't want like, the straight line to go just to positive Infinity because then everything will have like negative Infinity errors, right? So I do want it to be symmetric. So that's part of the job that the square is doing sure.

**[42:57 – 43:02]** But the same job could be done by million otherwise in a million other ways, right?

**[43:02 – 43:09]** I could have said, okay, why don't I add up the absolute value of this? There is

**[43:10 – 43:14]** why don't I add up for this value to how to degree 4?

**[43:15 – 43:21]** Why don't I adopt e to the power of the absolute value of this?

**[43:22 – 43:26]** And I mean there, I mean, there are infinitely. Many

**[43:27 – 43:36]** Monotone functions that are symmetric, symmetric and monotone in the distance. And if I actually start minimizing all of this thing's,

**[43:36 – 43:39]** I will get different results, right?

**[43:40 – 43:41]** The W will be different.

**[43:44 – 43:50]** So why do people choose squares often? Why is it the most common loss function?

**[43:53 – 44:05]** Things because of the Fulfillment of the government of theorem, maybe like the blue property. Exactly. Okay. So I I see that you already have the background for this so I'll make it quick.

**[44:07 – 44:16]** just like if everybody, if everybody has the same answer, we can just skip it if if you want to hear and

**[44:17 – 44:18]** I can explain.

**[44:19 – 44:31]** So okay, so the reason for this reason for the square actually comes from the probabilistic assumptions that we're making and let's frame linear regression.

**[44:32 – 44:44]** As a machine learning model in the sense that we are developing, right? So in this case Theta is the W, of course, so the model parameters are the weights, that's that's clear.

**[44:45 – 44:47]** Data.

**[44:47 – 44:51]** Are they excess and wise? That that's also pretty clear.

**[44:55 – 45:06]** But how do we Define the likelihood? So to define the model? We need to define the likelihood. The likelihood is p of D given Theta, right?

**[45:07 – 45:30]** The first thing that we do is we make the same assumption that we make. Always in machine learning, that keeps true throughout all of the machine learning models. We say that all of the data points are conditionally independent. Sorry, not X. Why are conditionally independent given the parameters, right? Sorry,

**[45:35 – 45:52]** And also, since we are doing supervised learning, we always have an X and the X, we are not modeling the expert on the modeling the way, right? So the X always goes on the right hand side here. So this is what you provide learning actually means. It means that we have an input that goes here.

**[45:52 – 45:55]** And then we are modeling the output that goes here.

**[45:56 – 45:58]** Okay, so

**[45:59 – 46:04]** The this part is straightforward. This, this is our first assumption, we always make it.

**[46:05 – 46:11]** But then comes the interesting part. So what is this distribution here?

**[46:12 – 46:16]** It's actually the distribution of the points that we see.

**[46:17 – 46:20]** Given our model and the X-ray, we measure.

**[46:21 – 46:22]** so, for example,

**[46:23 – 46:28]** At X3, we have our model predicting, this point.

**[46:29 – 46:32]** But what we need to Define is not just a single point.

**[46:32 – 46:44]** Right. So our second assumption will be linearity. Alright. Our second assumption will be that the most probable point the center of this distribution is in fact, W times x.

**[46:45 – 46:47]** But to actually do learning.

**[46:49 – 47:05]** We have to define a whole distribution around this point. Probably looks something like this, right? So it should decrease. I mean, I wanted it to be symmetrical. So let's assume it's magical and I wanted it to decrease to both sides.

**[47:06 – 47:10]** Right. So what it would mean it would mean that

**[47:12 – 47:18]** A larger distances from our model are largely distances from the straight line are less probable.

**[47:19 – 47:32]** So, if I want to find the most probable line, the maximum likelihood line, for example, then, of course, I want, this is just abysmal. So, I want this points to, I want the noise to be a small as possible. The total noise here,

**[47:34 – 47:40]** And the specific form of those function will follow from the choice of distribution.

**[47:41 – 47:50]** So yeah, I want it to be asymmetric. I wanted to be kind of bell-shaped, but as we discussed yesterday, there are lots of milkshake curves, right? So we want to pick a specific distribution here.

**[47:52 – 47:56]** And now comes around. It's this was all the setup for your answer.

**[47:58 – 48:05]** What is the most nature of distribution? That what is the default distribution that you use in a situation like this?

**[48:06 – 48:14]** Actually, it's the girls, it's normal distribution. And why? Because of the central limit theorem actually

**[48:16 – 48:16]** so,

**[48:18 – 48:26]** What does if you don't know if you haven't had probability theory, if you don't know, Central limit theorems, no matter, we won't really use it. I'm just explaining where it comes from

**[48:28 – 48:28]** so,

**[48:29 – 48:36]** What does the central limit theorem? Tell us the basic one, it says that whatever is the distribution.

**[48:37 – 48:50]** If you average it out sufficiently if you have a child, sufficiently more copies of this distribution or if you add them up, sufficiently many times. What you get is a gaussian you converge to a ghost.

**[48:51 – 49:04]** Right? So what this means in practice is that if you have a process, some kind of physical process or whatever where there are many small sources of noise.

**[49:04 – 49:06]** That all come together.

**[49:07 – 49:08]** And all add up.

**[49:09 – 49:11]** there is, although probably because

**[49:12 – 49:13]** Or close to ghosts.

**[49:13 – 49:24]** So if you don't know like in high school physics, if you're doing experiment like your rolling the ball down slow and then it comes to a certain distance.

**[49:24 – 49:41]** Then as the ball rolls, there are billions of small impacts on the ball right Professionals in the plane, the ball is imperfect. There's wind or whatever, and every one of these imperfections is definitely not ghosts.

**[49:42 – 49:47]** Everyone of them. Make some small impotent specially Direction, actually, probably

**[49:48 – 49:49]** but when you add them all together,

**[49:51 – 49:54]** it's a ghost because there are a lot of them.

**[49:55 – 50:03]** So it I mean there is a theorem there is math behind it but let's just limit here. So when you average out loads of

**[50:04 – 50:18]** Small nudges that go in opposite in different directions. What you get is more or less goes, unless there is some systemic bias inside like if all of your niches are in the same direction and of course you don't get to goes but that's different.

**[50:21 – 50:24]** So the so this is why.

**[50:26 – 50:26]** This.

**[50:30 – 50:38]** Noise this error in linear. Regression is indeed most natural to model with ghosts.

**[50:38 – 51:00]** With normal distribution and that's why the normal distribution is called normal. And that's why it's so so important, right? So, if you just look at its shape with the density here, you wouldn't understand why it's it holds us. Such a special place. Well, it's special because of the central limit theorem because everything converges to goes and away,

**[51:01 – 51:04]** and so if we do this assumption here,

**[51:05 – 51:07]** P of sorry, not P, but

**[51:08 – 51:35]** That was an already normal distribution of Y and around W Times, xn with some variance Sigma squared, it's a one-dimensional gaussian. We're talking about viands right now. This will be our. So, this was the first assumption. This is our second assumption that the center is linear function. That's the linear linear regression. And this is the third assumption that the noise is goes,

**[51:36 – 51:36]** Okay.

**[51:37 – 51:39]** There is a fourth but we'll get back. We'll get there.

**[51:40 – 51:43]** so, what is the

**[51:44 – 52:01]** Let me write down the density of the ghosts and it's one over square. Root of 2 pi is squared times e to the power. Minus 1 over 2 Sigma squared times, Y, and minus W Times X and squared and that's it, okay?

**[52:02 – 52:02]** so,

**[52:03 – 52:04]** Looks pretty complicated.

**[52:06 – 52:08]** What do you do next?

**[52:09 – 52:19]** Next are our first job is to maximize the thing, right? So we want to, let's say, I want to get the maximum likelihood hypothesis on the weights.

**[52:20 – 52:22]** I need to take the likelihood and I need to maximize.

**[52:24 – 52:24]** How do you?

**[52:25 – 52:35]** Always inevitably, do it in practice the very first trick that is always supplied and it's usually like understood without even explicitly writing it down.

**[52:37 – 52:38]** In machine learning.

**[52:40 – 52:46]** The likelihood is always as we discussed a big product of stuff.

**[52:46 – 52:55]** Right, so it's a product overall data points and there are lots of data points and we multiply the likelihoods of data points all together.

**[52:56 – 53:01]** So when you have a big big product, what you always want to do is take the logarithm.

**[53:02 – 53:16]** Right? So you want to convert the product to sum? Because if you keep multiplying small numbers like probabilities, it will be very difficult numerically, right? So the first step is always to take the locks

**[53:17 – 53:24]** So, look pod, even W and now this formula is the sum over n.

**[53:25 – 53:29]** This is what minus 1/2 times look.

**[53:29 – 53:46]** 2 by Sigma squared, I'll leave it at that. Minus 1 over 2 Sigma squared Y and I'm going to now this is a constant that goes out of the sum. So it's minus n over to

**[53:47 – 53:52]** Look to Pi Sigma squared. This can also go out of the sum

**[53:53 – 53:55]** and inside the sum, we have

**[53:56 – 54:00]** Wire minus W Times, xn squared.

**[54:00 – 54:01]** Okay.

**[54:02 – 54:08]** And now our problem, our equation is, I want to maximize this with respect to w.

**[54:10 – 54:18]** There is a minus sign here. So if I just look at this sum, this one doesn't have any WS. So this one is irrelevant. It's a constant.

**[54:19 – 54:20]** And the W is in here.

**[54:21 – 54:25]** And there is a minus sign. So what I do is this sum is I actually want to minimize it.

**[54:26 – 54:26]** Right.

**[54:27 – 54:28]** That's it.

**[54:29 – 54:38]** There you go that's the motivation behind having a sum of squares specifically squares and not. Absolute value is not exponents. Not anything.

**[54:40 – 54:45]** The story of course, does not stop here. It's not at the beginning.

**[54:48 – 55:01]** Okay. Oh yeah, and one more thing, I, I promise to go back to the fourth, assumption. So, there is a force assumption which is kind of hidden over here. And the fourth assumption is that

**[55:02 – 55:02]** The variance.

**[55:03 – 55:04]** Is the same.

**[55:05 – 55:10]** Over the whole data set, right in statistics. It's called

**[55:11 – 55:15]** There is a difficult word, homoscedasticity I think.

**[55:16 – 55:25]** so, if you have a homeless Scholastic process, it means that the noise variance is constant across the whole process and it's

**[55:26 – 55:35]** It's the assumption that allows us to actually take the sigma and get it out of the summon, not care about the same.

**[55:36 – 56:23]** And that can be violated and practices, right? So in practice it's quite possible that you can have points that go like this. There is a good first their dance and then they become more noisy for example. And you still want to have a single straight line that goes that describes all of these points. I have. But yeah if something like that happens, then you need to modify the last function you need to actually explicitly notice this which is not very well and then understand what it tells you about those. So this is by the way, one of the most direct reasons why you actually want to understand this probabilistic approach because it's

**[56:24 – 56:34]** It may seem at First Once that. Okay, so we explained why squares, but it doesn't change anything right. We are still minimizing the sum of spares, right?

**[56:35 – 56:47]** But the point is not to, it's not only so like, why do we want to understand stuff? We want to understand stuff in order to notice when it stops working.

**[56:49 – 57:01]** We understand, we want to understand the assumptions behind the sum of squares. So that when they are violated, when we are not in this situation, we actually know it's not

**[57:02 – 57:14]** for example, when our variance is change in the middle of the process. Or, for example, when we have reasons to build that all of the noise is only in a single Direction,

**[57:14 – 57:22]** Right. So now you want to have an estimate noise distribution and its distribution. That's only on the positive part of the line.

**[57:22 – 57:34]** Also, there are variations of linear regression like this too. Of course, it's not like it to do any new math here, but you need to know, notice this and to apply the correct math, right?

**[57:38 – 57:38]** Um, okay.

**[57:39 – 57:45]** So this is our first step and we compute the sum of squares and blah.

**[57:46 – 57:49]** but of course, we want to apply

**[57:50 – 57:55]** Our bias and story, right? So we want to say, hmm.

**[57:57 – 58:05]** What I am actually interested in is not P of D given W but it's p of w d.

**[58:06 – 58:06]** Right.

**[58:08 – 58:08]** Which means?

**[58:09 – 58:14]** That I need to have a prayer, right? What does

**[58:15 – 58:17]** A prior look like for linear regression.

**[58:18 – 58:27]** Well, it's a more complicated thing and again as soon as we get to something like bass and inference something like prior distributions.

**[58:28 – 58:41]** Well, the probability Theory becomes a bit Messier. Like in coins, we had a very simple discrete likely Hood, just to outcomes but then as soon as we went to the prior and posterior,

**[58:42 – 58:58]** Distributions became continuous. There was no way around that here, everything is continuous, but from the single one dimensional clean house and now we need to go to a multi-dimensional distribution. Right. So now there are several different ways and we want to have a distribution on them.

**[59:00 – 59:16]** But before we chose before we choose it what is going to happen with our optimization problem? Like if I now want to maximize the posterior distribution, what does it actually mean in terms of the numerical problem that I'm solving?

**[59:17 – 59:35]** Well, to be honest, it changes quite little. So what we are basically saying and this is also true, I can entire machine learning where basically, saying like a proportional means that there is a constant, which doesn't matter right from maximization. And then we have this look

**[59:36 – 59:41]** Like likelihood, which we already had before and then there is the lock prior.

**[59:43 – 59:46]** So basically, I want to maximize this case together.

**[59:47 – 59:48]** Right.

**[59:49 – 59:50]** And the lock prior.

**[59:52 – 1:00:02]** You probably in some previous classes, you probably have seen already all of this look prior stuff and you usually call them regularizers.

**[1:00:03 – 1:00:04]** Right. So regularization

**[1:00:05 – 1:00:06]** Is actually.

**[1:00:07 – 1:00:12]** The process of putting a prior on the parameters of your model.

**[1:00:13 – 1:00:27]** So what is the difference between this terms and practice differences that the regularizer does not depend on the data, right? So it's the part of the loss function. That is only about the weights only about the model parameters and not about the dataset.

**[1:00:29 – 1:00:30]** and,

**[1:00:32 – 1:00:45]** So formally, it's a it's our prior beliefs. It's what we think about the ways of our linear regression before.

**[1:00:46 – 1:00:47]** We start getting the data.

**[1:00:50 – 1:00:51]** and at this point,

**[1:00:52 – 1:00:53]** It may sound.

**[1:00:55 – 1:00:56]** Quite strange.

**[1:00:57 – 1:01:14]** Because if for a coin, we did have an intuition, like a real life intuition that coins are approximately fair, right? So for a coin that they take out of my pocket, obviously, I do have some kind of Prior beliefs that are actually quite strong

**[1:01:15 – 1:01:17]** For linear regression. Seems like we don't

**[1:01:18 – 1:01:23]** Right. So for linear regression, it seems like the regular eraser shouldn't be doing anything.

**[1:01:24 – 1:01:36]** A what's like, how do I prefer? One slope of this straight line to another slope. I don't know if I don't have any data, they all are the same for me or at least they should be right.

**[1:01:38 – 1:01:38]** Well.

**[1:01:39 – 1:01:41]** Here is how it actually works.

**[1:01:42 – 1:01:42]** so,

**[1:01:45 – 1:01:54]** To make a good illustration. I won't go to the multi-dimensional case, but I will make like a multi-dimensional regression out of a one-dimension progress.

**[1:01:55 – 1:02:16]** So an example that I always give and that I think is illustrates this. The best is let's extract some additional features from ads. Okay? So this is all so an important discussion and so on, right? So how do people usually apply simple models like linear regression?

**[1:02:18 – 1:02:25]** well, they have their access their original inputs and sometimes

**[1:02:26 – 1:02:36]** it so happens that you can just treat excess as numbers and do a linear regression and your output is W Times X and everybody's happy

**[1:02:37 – 1:02:43]** but more often than not, you before you go to learn the weights,

**[1:02:44 – 1:02:48]** you actually extract some kind of features from X.

**[1:02:49 – 1:02:50]** Sometimes.

**[1:02:51 – 1:03:01]** And then you get some, you know, fear of X Firefox and then you do the linear regression and the output is W Times 5x, okay?

**[1:03:01 – 1:03:19]** So sometimes feature extraction is about reducing the content. Like if you want to do linear regression on images then obviously it makes no sense to the linear regression on the pixels right. If first one to extract some semantically rich features and then the linear regression

**[1:03:20 – 1:03:33]** Sometimes it's the opposite. Sometimes X is very simple and you want to just describe a more complicated dependency between X and Y and you need to extract additional features.

**[1:03:34 – 1:03:35]** So this is an example like that.

**[1:03:36 – 1:03:40]** and suppose that

**[1:03:41 – 1:03:46]** I have one dimensional regression. So there is only one X. There is only one way.

**[1:03:47 – 1:03:51]** Ah, but when I look at my points.

**[1:03:54 – 1:03:55]** I kind of realized.

**[1:03:56 – 1:03:59]** That they're definitely not linear.

**[1:03:59 – 1:04:03]** Right. I realized that they don't look like a straight line at all.

**[1:04:04 – 1:04:07]** But they kind of look like a parabola.

**[1:04:08 – 1:04:10]** They kind of look like a quadratic function.

**[1:04:11 – 1:04:12]** So,

**[1:04:13 – 1:04:15]** Here is a question. Can I use linear regression?

**[1:04:16 – 1:04:26]** To actually learn a parabola here to learn something like w0 plus W 1 times X Plus W2 times x squared.

**[1:04:30 – 1:04:34]** Yes, if we make a feature, yeah.

**[1:04:35 – 1:04:36]** Precisely. So,

**[1:04:38 – 1:04:53]** The three billionaire regression of only give you this, but we already know that we can add more features it in a trivial way. Now, let's do it in the history will be. So let's go from X to this feature Vector One X x squared.

**[1:04:55 – 1:04:58]** And then you multiply and then you do just linear regression.

**[1:04:59 – 1:05:16]** Right? And when you do linear regression on this, what you are actually minimizing, what is your loss function, it's the sum of Y and minus What minus? Well, w0, plus W1 times X plus W, 2 times x squared,

**[1:05:17 – 1:05:20]** There we go, right? So you are actually fitting a parable.

**[1:05:22 – 1:05:29]** And actually this discussion is extremely relevant to deep learning. Because what is the

**[1:05:30 – 1:05:38]** the thing that deep learning is doing what? What are the neural networks always doing? They are learning good feature, extractors

**[1:05:38 – 1:05:44]** that's the whole like the whole Revolution. So before declaring worked

**[1:05:45 – 1:05:53]** What we would usually do is machine Learners. We would try to invent this feature extraction, part by hand or from some other.

**[1:05:55 – 1:06:04]** For some other reasons, right? And then we would run relatively simple models on this features of course not necessarily linear regression but relatively simple models.

**[1:06:06 – 1:06:13]** What neural networks do is they make feature extraction apart of the model.

**[1:06:14 – 1:06:17]** so now, the feature extraction also has weights

**[1:06:18 – 1:06:21]** And how does a neural network actually look?

**[1:06:23 – 1:06:33]** Let's say I have an image at the input. Then there are like lots of layers that do different interesting stuff, blah blah. But then at the end of this layers,

**[1:06:34 – 1:06:39]** we have actually a vector of numbers that goes into the final layer.

**[1:06:40 – 1:06:48]** And the final layer, depending on what problem you are solving. If it's, if you're predicting a number, it's usually a linearly

**[1:06:49 – 1:06:58]** So if, if you're output is supposed to be a number, not the classification problem. Then the last layer is probably linear. Almost always, I don't know any exceptions.

**[1:07:00 – 1:07:03]** What this means is that.

**[1:07:05 – 1:07:06]** This part of the network.

**[1:07:07 – 1:07:12]** Is doing feature extraction for the last linear. Regression layer.

**[1:07:14 – 1:07:22]** The last layer is actually linear regression but not on the pixels of the input, not on the X but on the features extracted from X.

**[1:07:22 – 1:07:33]** And of course, the hard part is learning the previously layers. The last layer is kind of easy and we are now doing these stuff of course, but it's, it's there.

**[1:07:34 – 1:07:35]** so, any

**[1:07:36 – 1:07:40]** Basically, any big complicated neural network that predicts a number?

**[1:07:41 – 1:07:43]** Almost always ends with a linear regression.

**[1:07:45 – 1:07:49]** Any complicated neural network that does specification?

**[1:07:50 – 1:07:53]** And with a logistic regression, we'll get there later.

**[1:07:54 – 1:07:55]** so, the rest of the network,

**[1:07:56 – 1:08:05]** Is extracting features for this last final layer. That that's that's the connection that's why this linear models are still very, very low for deep learning as well.

**[1:08:08 – 1:08:11]** All right, so back to linear regression.

**[1:08:14 – 1:08:17]** Yeah, and at this point, I think I want to make an example of this.

**[1:08:19 – 1:08:20]** Let me see.

**[1:08:22 – 1:08:23]** Let me see.

**[1:08:24 – 1:08:25]** There we go. Yeah.

**[1:08:27 – 1:08:28]** so, I put some more

**[1:08:32 – 1:08:35]** Stuff here. But yeah for now,

**[1:08:36 – 1:08:41]** Okay, we're getting there. Yeah for now.

**[1:08:43 – 1:08:43]** let's,

**[1:08:46 – 1:08:48]** Okay, yeah, there we go.

**[1:08:51 – 1:08:53]** So, let me show you.

**[1:08:56 – 1:08:58]** A polynomial, regression problem.

**[1:08:59 – 1:09:10]** I have the true function, the original function, which is actually not polynomial. So we will we don't expect to capture this function exactly. It's it's a sign for sine wave.

**[1:09:12 – 1:09:12]** but,

**[1:09:13 – 1:09:15]** I take one period of this sine wave.

**[1:09:16 – 1:09:23]** And they put the points around this one period of the same wave. Okay. So the stars are the points.

**[1:09:24 – 1:09:31]** They horizontal line is X. There is only one dimension here and the vertical line is why the workplace is why

**[1:09:32 – 1:09:34]** so, when you look at this Stars,

**[1:09:35 – 1:09:40]** You kind of immediately realize that they are not linear, right?

**[1:09:41 – 1:09:43]** And if you actually fit linear regression,

**[1:09:44 – 1:09:51]** you get a straight line. Of course, you get some line. Sure, but the air is very high, right? So obviously not describing this points. Well,

**[1:09:53 – 1:09:54]** so,

**[1:09:55 – 1:09:59]** first question to you, what do you think is the proper degree of the polynomial?

**[1:10:00 – 1:10:03]** What would be a good degree of the polynomial?

**[1:10:05 – 1:10:08]** I can't put the sine wave here, but I can do it in.

**[1:10:19 – 1:10:25]** You please. Repeat the question. Yeah. What would be a good degree of the polynomial to fit this points?

**[1:10:26 – 1:10:28]** So the straight line degree one doesn't work.

**[1:10:29 – 1:10:30]** What, what would work?

**[1:10:33 – 1:10:35]** I think the degree of free.

**[1:10:36 – 1:11:10]** Yeah, exactly. Yeah. So a parabola probably also doesn't capture this, right? So it's a little better, but not much, but if you go to the degree 3, then yeah, the third degree program has this, to one minimum, one maximum can have. And we kind of already made can match one period of the sine of, right? So if I train a third degree, put an email, they sew their four.

**[1:11:12 – 1:11:24]** A four weight including the intercept. Then it's already a pretty good fit and if I compute their second thing I have here, but if a computer there, they will be fine.

**[1:11:25 – 1:11:31]** But what happens if I keep increasing the degree?

**[1:11:32 – 1:11:48]** So, if I increase it to four or five, I don't think much will happen. I think they have a look approximately the same. So if you look at the degree foreign degree 5 curves, they are slightly better but it's basically the same stuff.

**[1:11:49 – 1:11:51]** When do you think it's gonna break?

**[1:11:52 – 1:11:55]** Or is it gonna break or can I increase the degree?

**[1:11:56 – 1:11:57]** Indefinitely.

**[1:12:00 – 1:12:00]** Maybe.

**[1:12:04 – 1:12:06]** Okay, they're not 25.

**[1:12:06 – 1:12:08]** What do you need to know answer this?

**[1:12:17 – 1:12:19]** What do we need to know to us? Yeah.

**[1:12:24 – 1:12:30]** Like okay, we will make a number of points.

**[1:12:32 – 1:12:52]** It goes to each point. It will break. Yeah, sure. So, yeah, of course, we cannot predict in advance, when exactly, it's going to be start to be bad, but we definitely know when it's certainly going to be read. And here I have one, two, three, four, five, six, seven, eight, nine, ten, eleven points. So for 11 points,

**[1:12:52 – 1:12:55]** if I do a polynomial of degree 10,

**[1:12:56 – 1:13:00]** a polynomial of degree 10 can just pass through all of this points. Exactly right.

**[1:13:01 – 1:13:05]** So let me keep the third degree and add the Grid 10.

**[1:13:06 – 1:13:09]** And this is what and interpolation polynomial looks like.

**[1:13:11 – 1:13:14]** So, it passes through every point. Exactly.

**[1:13:15 – 1:13:16]** Which is great.

**[1:13:17 – 1:13:18]** but,

**[1:13:19 – 1:13:21]** So they Training Center is exactly zero.

**[1:13:22 – 1:13:39]** But the test sets there is huge, right? It's completely useful for predicting. It has this very strange Peaks on the left on the right. Even some in the middle a little bit. So it's it's definitely a very bad model much worse than the orange curve, right?

**[1:13:40 – 1:13:54]** And that's in details as you write in chat. That's the classical picture of overheating. So we have too many parameters. And in this case of course it's quite obvious that we have too many parameters and

**[1:13:55 – 1:14:07]** What do we do? Like how do we notice this overheating? If we can't just look at the picture right in real life, there would be a high-dimensional input and we wouldn't be able to just look at the picture. How do we know what you said?

**[1:14:08 – 1:14:30]** Well, in this specific case, it's very easy to say just don't do this, right? So this is of course, it's a generic case. This is a very simple example and you can say, well obviously we have 11 points, we don't want to degree the polynomial of degree 10. That's easy. You don't need any Theory to understand this.

**[1:14:31 – 1:14:31]** but,

**[1:14:33 – 1:14:49]** In real life, we usually cannot avoid this completely. So in this simple example, where I have a one dimensional X and I choose the degree myself. Sure, I can just look at the pictures and pictures. That's why I'm showing to you because the pictures make it obvious

**[1:14:50 – 1:15:07]** But in real life, what's gonna happen is actually this and I'm answering this, on asked, question of how can this happen and practice with linear regression? And the answer is basically this what would actually happen to you when you do linear regression, you have your data set.

**[1:15:08 – 1:15:12]** And you have in your dataset points of the greedy.

**[1:15:13 – 1:15:23]** So it's not one thing and one dimension one nothing but will ever happen I mentioned one is easy, but you have points of Dimension d

**[1:15:24 – 1:15:26]** and you are trying to

**[1:15:28 – 1:15:29]** Do linear regression?

**[1:15:30 – 1:15:36]** And your failing? Okay. So if linear regression works like this perfect, you don't need anything else, but

**[1:15:37 – 1:15:43]** you're failing you can see that the relationship is not really linear. You want some something else you want something more?

**[1:15:43 – 1:15:44]** right

**[1:15:45 – 1:15:51]** So this doesn't work and you don't you make the next step. What is the next step? Let's do it.

**[1:15:53 – 1:16:09]** But unlike the one dimensional case where the code rating depends. It just adds one more feature and you control it very friendly you go to degrees 38 one more feature go to degree for you at one more feature. So you'll choose the number of features explicitly basic.

**[1:16:11 – 1:16:14]** If you have a multi-dimensional vector doesn't work like that anymore.

**[1:16:14 – 1:16:23]** Right. So if you go from X of the greedy of Dimension this area of lengthy to a quadratic.

**[1:16:24 – 1:16:25]** Feature vector.

**[1:16:26 – 1:16:36]** What you actually get is something like 1 x 1 x d. The next one squared, x 1, x 2, x 1, x 3, and all the way to XD squared, right?

**[1:16:37 – 1:16:47]** So the actual number of features is something like, maybe I'm missing some plus or minus 1 but something like this, something on the order of this squared.

**[1:16:48 – 1:16:48]** Right.

**[1:16:51 – 1:16:52]** Which is.

**[1:16:53 – 1:17:00]** quite a bit in the sense that now, if I start with the vector of size, 100

**[1:17:01 – 1:17:07]** And I go to accelerating dependency. I immediately get not 200 features.

**[1:17:07 – 1:17:13]** Not even 500 features, but I get what 5,000 features about approximately.

**[1:17:17 – 1:17:22]** And of course, when you go from 100 features to 5000 features, overheating can happen.

**[1:17:24 – 1:17:24]** All right.

**[1:17:25 – 1:17:38]** So this is the actual mechanism like, of course, in dimension one, it's it's it's always easy. But in high Dimensions there is no middle ground. You can't go to degrees 3/5, right?

**[1:17:40 – 1:17:43]** so, and actually, like,

**[1:17:44 – 1:17:53]** when you look at all of these features, you understand, of course in your head that you don't need all of them, of course, of course, you don't need all of them.

**[1:17:54 – 1:18:12]** You only need some of these quadratically dependencies. So like in reality what matters is, maybe like the relation, the dependency, the connection between X1 and X3 and then maybe XD squared and then maybe something else in the middle and that's it. And the rest could be 0.

**[1:18:13 – 1:18:29]** But the point is, you don't know in advance which ones that's the whole point of learning, right. And you need to figure out which of this interactions matter, they're called interactions and statistics. When you get this features like X1, X3, we each of these interactions matter.

**[1:18:30 – 1:18:30]** and,

**[1:18:32 – 1:18:35]** You can't do it when you if you don't start with them, all right?

**[1:18:36 – 1:18:45]** So overheating is kind of inherent in machine learning. You can not avoid it, even for linear regression, let alone something complicated like neural networks.

**[1:18:47 – 1:18:48]** So, getting back here.

**[1:18:50 – 1:18:57]** How could be notice that something bad is happening? If we cannot just look at the picture, how can we know just over it?

**[1:18:59 – 1:19:01]** There is a simple principle dancer.

**[1:19:02 – 1:19:15]** A principled answer would be so let's do a test set or to be more precise, validation set. Let's set aside a part of the points. Let's measure the validation set error.

**[1:19:16 – 1:19:24]** And when the validation Center starts to grow, we stop that's the standard procedures, standard procedure and machine learning.

**[1:19:25 – 1:19:25]** but,

**[1:19:27 – 1:19:30]** And if you can do it, it's fine.

**[1:19:31 – 1:19:32]** but,

**[1:19:33 – 1:19:35]** Again, in this example.

**[1:19:36 – 1:19:37]** You can't really do it.

**[1:19:38 – 1:19:53]** So well, I mean maybe okay. Maybe you can imagine like, aiding this quadratic terms one by one and you know but then he would need to kind of go through all of them and then go through all of them. Again probably would be impractical.

**[1:19:54 – 1:20:00]** but if you know of them at once, you just get overheating, you get this High test center and what do you do, you know,

**[1:20:02 – 1:20:06]** There is no continuous process that you can just stop at some point.

**[1:20:08 – 1:20:08]** So,

**[1:20:10 – 1:20:16]** How else, what is another symptom of overheating Happening Here?

**[1:20:16 – 1:20:20]** How else is? It could at work.

**[1:20:21 – 1:20:21]** Well.

**[1:20:22 – 1:20:28]** Here, I output them over here. You can also look at the coefficients.

**[1:20:29 – 1:20:39]** And this sounds a little bit counterintuitive, but we are getting back to to the stuff that we actually, that is actually useful for us now.

**[1:20:41 – 1:20:46]** If you look at the coefficients of this polynomials, let me a lot of them.

**[1:20:49 – 1:20:57]** So the plot is now completely unreadable. But let's look over here. If you look at the coefficients of this polynomials,

**[1:20:58 – 1:21:02]** You will know just that as the degree, is the degree increases.

**[1:21:03 – 1:21:04]** The coefficient grow.

**[1:21:06 – 1:21:16]** But they grow kind of in a bounded way and then when overfeeding starts to happen in this case, it's only the equals to 10, but it could happen a bit before.

**[1:21:18 – 1:21:23]** You see a sudden jump in the question. So you see if coefficients like plus or minus 50.

**[1:21:25 – 1:21:29]** and at this point, you can notice that

**[1:21:30 – 1:21:31]** and you can say, well,

**[1:21:32 – 1:21:38]** so this this is the tricky part here. This is the not really formal part. You can say, well,

**[1:21:39 – 1:21:52]** I have like 10 points, 11 points that and the x is always about one. So it's from negative one, one and a half to positive 2.

**[1:21:53 – 1:21:56]** And the Y is from minus to plus one.

**[1:21:57 – 1:22:01]** And this points are described by a model with coefficients, like 50.

**[1:22:02 – 1:22:04]** That doesn't sound possible to me.

**[1:22:04 – 1:22:05]** Okay.

**[1:22:06 – 1:22:06]** so,

**[1:22:07 – 1:22:10]** This is the intuitive reading of this.

**[1:22:12 – 1:22:21]** And the formation of this would be my prior belief about the coefficients is that they should actually be relatively small.

**[1:22:22 – 1:22:29]** They should for this data set. They should be on the order of plus or minus one, or maybe two, but definitely not 50.

**[1:22:30 – 1:22:30]** Right.

**[1:22:32 – 1:22:32]** and,

**[1:22:33 – 1:22:37]** You know, think about this way, maybe this picture also find very helpful. So

**[1:22:38 – 1:22:55]** Ah when you do a standard, linear regression, you have this two-dimension. If you have one dimensional X and standard linear regression, you have two dimensions of Weights. So you have the two-dimensional space of weights to choose from

**[1:22:55 – 1:22:56]** Right.

**[1:22:56 – 1:23:01]** And then you go to quadratic regression, you get a three-dimensional space of weights.

**[1:23:02 – 1:23:10]** Which is now it's not a mathematical term but we just kind of larger. You have a larger variety of models to choose from.

**[1:23:11 – 1:23:15]** I can make it precise, but we won't have time in class to make it precise.

**[1:23:16 – 1:23:22]** And then you go to Dimension 4, you get even more different models. There are much more.

**[1:23:24 – 1:23:27]** Polynomials of degree 4th and there are problems of degree 2.

**[1:23:28 – 1:23:38]** because I'm a degree for include Polymers of the Creator and then some and what if so models of degree 4 can

**[1:23:40 – 1:23:41]** Explain can.

**[1:23:42 – 1:23:43]** Approximate.

**[1:23:44 – 1:23:52]** More data sets, many more different dependencies between points then polynomial degree.

**[1:23:53 – 1:23:56]** So you get this much larger set of ways to choose from.

**[1:23:57 – 1:24:00]** and then you go up to degree 10 and

**[1:24:01 – 1:24:06]** At some point. This variety becomes too much, right? And this gets you to overheating.

**[1:24:07 – 1:24:25]** So, one way to reduce the variety would be to go back and the dimension. But if you cannot afford that like in this multi-dimensional example, if you can't just do a smaller set of features, then what you could do is you could try to limit this variety inside the big space.

**[1:24:26 – 1:24:46]** So you could say, okay I have to stick with the 11th but at least let me look for Solutions inside like near zero. At least let me constrain the vectors in the National Space. So I kind of again intuitively I kind of want to

**[1:24:47 – 1:24:49]** Constrain the variety of the models.

**[1:24:51 – 1:24:55]** And that's what regularization does. And that's what that's what priority distributions do.

**[1:24:56 – 1:24:57]** so, in this case,

**[1:24:58 – 1:25:06]** in the case, what we actually do here, how can this hold this problem?

**[1:25:07 – 1:25:15]** It would be, we need to add a prior distribution. That would tell me that the weights are relatively small,

**[1:25:16 – 1:25:20]** So what does it mean? It means that P of w.

**[1:25:21 – 1:25:22]** should be like,

**[1:25:24 – 1:25:32]** Somewhere around zero concentrated somewhere around 0, probably we don't want to completely exclude anything we want.

**[1:25:32 – 1:25:40]** All the address to have some non-zero density, but we want it to be concentrated around zero and then just go.

**[1:25:42 – 1:25:46]** Just reduce and another Direction and all and all directions, right?

**[1:25:47 – 1:25:50]** and what kind of a distribution could that be

**[1:25:51 – 1:25:58]** Well, the obvious answer, it could be a ghost, right? So you could say, okay let's say the P of w.

**[1:25:59 – 1:26:04]** is a gaussian centered around zero, we sum

**[1:26:07 – 1:26:27]** Covariance Matrix. And since it's a prior distribution and I don't distinguish between different weights. I see no reason to have anything but the identity Matrix here. So I don't, I don't in advance, I don't know which way it's will be dependent with which so let me let the prior be independent.

**[1:26:28 – 1:26:56]** Ah, and then I don't want to actually go into in this class. I don't want to go into the density of multidimensional goals and Etc. If, if you're interested, I I do teach classes like this personally in Russian, but there are quite a few Russian speakers among you. You can watch on my website, some other classes where I spent like a whole semester on this kind of stuff, but let me just say that

**[1:26:57 – 1:27:08]** from from this P of w, the log P of w will be some constant minus one over two Sigma 0 squared times.

**[1:27:08 – 1:27:14]** The norm of the vector, W Times the sum of wi squared.

**[1:27:15 – 1:27:16]** Right.

**[1:27:17 – 1:27:21]** and then, if I add this prior to

**[1:27:22 – 1:27:42]** My likelihood which is already fixed. This is part of the model. Then what they actually get is something is a lost function that looks like this some of our end why and minus W Times X and squared that's the likelihood part. And let's okay, let's put one over Sigma square root here.

**[1:27:43 – 1:27:43]** Plus.

**[1:27:44 – 1:27:48]** 1 over Sigma, zero squared, the prior variance.

**[1:27:49 – 1:27:52]** Times this sum of squares of the W's.

**[1:27:53 – 1:27:54]** And I want to minimize this.

**[1:27:55 – 1:28:00]** So again constants don't really matter so I can put this signal over here.

**[1:28:01 – 1:28:02]** Cancel the 2.

**[1:28:02 – 1:28:03]** and,

**[1:28:04 – 1:28:04]** What I get.

**[1:28:05 – 1:28:06]** Is exactly.

**[1:28:07 – 1:28:09]** The sum of squares with.

**[1:28:10 – 1:28:14]** What is often called and L2 regular eraser.

**[1:28:15 – 1:28:17]** L2 means.

**[1:28:18 – 1:28:19]** Regular eraser.

**[1:28:20 – 1:28:30]** The regularizer is often the norm of the vector of way and Norm of the vector of weights, and then the L2 Norm in the L2 space is sum of squares. The equation.

**[1:28:31 – 1:28:33]** So that's an L2 regularizer.

**[1:28:36 – 1:28:43]** And then I can use this regular, I can fix the problems. So if let me see if I have

**[1:28:44 – 1:28:52]** Let me see if I have. Yeah, we'll skip the local features time for that.

**[1:28:54 – 1:28:54]** Yeah.

**[1:28:56 – 1:28:58]** Yeah, I do have it. Okay. So

**[1:29:00 – 1:29:05]** so, first of all, before I show that before I show, regularization, let me say that,

**[1:29:07 – 1:29:18]** This kind of overheating and regularization everything is dependent on the data set also, right? So no, it is how when we went to degree 10, we got

**[1:29:19 – 1:29:39]** severe over fitting only because we had exactly 11 points, right? If we just add more points, a degree and polynomial will be fine, that's kind of obvious, but I wanted to mention it, right? So, if I have 100 points, not 10, then of course a degree 10 polynomial will not be severe or fit.

**[1:29:41 – 1:29:43]** And that's for regularization.

**[1:29:46 – 1:30:02]** As regularization here is the data set. Here is the original function with no, no regularization. It's the interpolation polynomial and Alpha is basically this equation this guy over here.

**[1:30:05 – 1:30:05]** so,

**[1:30:06 – 1:30:08]** ASI, increase Alpha.

**[1:30:09 – 1:30:15]** It will become more important, right? So it will, it will be

**[1:30:17 – 1:30:25]** The shape of this curve, the shape of this polynomial will be determined more and more by the regularizer and less by the actual Training Center.

**[1:30:26 – 1:30:37]** So if I have this kind of small regularizer, like 1 over 1,000 then, you can see that actually actually, it's already pretty strong. Okay, let me let me make it even bigger.

**[1:30:38 – 1:31:22]** In this case. Yeah. So the absolute value of the coefficients are already kind of reduced but you still see this some of this local extremes at the yeah in this. Yeah as you can. Okay here is another illustration. Obviously I do the points at random every time so for this specific set of friends and points even a very small regularization is enough. So actually we it would take a lot to straighten out this guy's on on the extreme but the other special features are kind of already straight up.

**[1:31:22 – 1:31:26]** Yeah, but okay. So let's let's make the regularizer even smaller.

**[1:31:27 – 1:31:29]** Yeah. So at some point, you can see that.

**[1:31:31 – 1:31:32]** It gradually.

**[1:31:33 – 1:31:36]** Irons out this overfitting.

**[1:31:37 – 1:31:41]** and I already showed that with some

**[1:31:42 – 1:32:03]** Good value of alpha. You can get a very good curve over here. Let's see if I can even straighten out the sides. I'm not sure I can, but yeah, I can make this effect smaller. At least. Okay. Here I strange that straighten it out on the left but not on the right. So, yeah, as I keep increasing the regularizer,

**[1:32:04 – 1:32:10]** Remove this one and keep increasing this one. As I increase the regular eraser. Okay, so this is a good craft now.

**[1:32:12 – 1:32:29]** I will see that the degree 10 polynomial, it's still great and it's properly degree. And if you look at the coefficients, yes, they become closer to 0 but they're not like everything is 0, except the first three know, they are still meaningful over here. For example

**[1:32:30 – 1:32:32]** So it's still a great example.

**[1:32:33 – 1:32:41]** Ah but now it behaves much better, right? So we are kind of got rid of the regularizer of the overfeeding by regularization.

**[1:32:41 – 1:33:01]** But then, of course you can overdo it. So if you go to something like 10, you will get like a curve that a degree 10 polynomial. It doesn't care about the points in at all right. It only cares about the regularizer and in this case, of course, it's also a bit model. So as with all things in life, there is a trade-off.

**[1:33:03 – 1:33:06]** Okay. And what else did I want to say here?

**[1:33:08 – 1:33:08]** Was that?

**[1:33:09 – 1:33:15]** again, I don't want to go into the math here and probably able to have to skip the base and part here, but

**[1:33:17 – 1:33:18]** I don't want to mention that.

**[1:33:20 – 1:33:40]** If you look so the L2 regularizer the gaussian prior is indeed special for linear regression. So as we discussed yesterday with this, conjugate priors with the prior in the form of the likelihood blah blah, blah. You can know just that here. Also,

**[1:33:41 – 1:33:41]** Here. Also,

**[1:33:44 – 1:33:46]** She also what sorry.

**[1:33:50 – 1:34:07]** Here. Also the shape of the gaussian regularizer matches the shape of the gaussian likelihood. It's a quadratic function of w, right? So of course, it's convenient to add two quadratic functions of w. Also get the quadratic function of w and to get the ghosts and again

**[1:34:07 – 1:34:20]** So this is the conjugate prior and you can go from gaussian to gaussian in the space of Weights. Let's let's not go into my my first turn to that discussion but

**[1:34:22 – 1:34:27]** linear regression also gives us a good example that you don't necessarily have to do that.

**[1:34:27 – 1:34:32]** So here, you can have very good reasons to choose different regular erasers

**[1:34:34 – 1:34:36]** very good reasons like

**[1:34:37 – 1:34:46]** So one other common regularizer for many models and for it for neural Nets as well, would be an L1 regular race.

**[1:34:47 – 1:34:52]** So let's start from this. So what if instead of adding sum of squares

**[1:34:53 – 1:34:54]** I would add.

**[1:34:56 – 1:34:58]** The sum of absolute values here.

**[1:34:59 – 1:34:59]** So,

**[1:35:00 – 1:35:03]** Notice that there is a difference here, there is an asymmetry.

**[1:35:04 – 1:35:06]** The error.

**[1:35:06 – 1:35:07]** The noise.

**[1:35:08 – 1:35:33]** Is a property of our model. It's I mean yeah we kind of choose it but we are supposed to choose it correctly. There is a right answer in the wrong answer here. Like what is the actual noise in the actual process that we got the data with that would be the perfect? Correct answer. There is some kind of underlying truth here. Probably it's not exactly goes and probably it's an approximation but

**[1:35:34 – 1:35:41]** There is a way in which there is the correct. Answer to the question of what is the what is the right likelihood?

**[1:35:42 – 1:35:45]** But there is no correct. Answer to the question. What is the right prior?

**[1:35:46 – 1:35:48]** It's completely our choice.

**[1:35:49 – 1:35:52]** We choose the prior to match whatever we want.

**[1:35:53 – 1:35:54]** and,

**[1:35:55 – 1:35:58]** We might want to choose something else.

**[1:35:59 – 1:36:01]** So, this is L1 regularization.

**[1:36:03 – 1:36:14]** And so they you may also encounter this terms. The linear regression with L1 regularization is called the loss or regression

**[1:36:15 – 1:36:18]** a last Saw is actually an acronym for

**[1:36:19 – 1:36:27]** Something like least average inch. I forget never comes up. And this is called the rich regression.

**[1:36:28 – 1:36:32]** Rich is not an acronym, it's this reach the calcium.

**[1:36:35 – 1:36:36]** But anyway,

**[1:36:36 – 1:36:40]** You might want to choose a non-conjugated prayer because it has Better Properties.

**[1:36:41 – 1:36:53]** So I have it here. So, let me let me show this property to you, they don't have time to discuss, why? But this, let's let's see the how it works.

**[1:36:54 – 1:36:54]** So,

**[1:36:56 – 1:37:25]** If you look at the same kind of regularization way but we still lost sorry creation with the L1 regularizer, not the rich regression. Not the author regularizer. You will see that. It all is like a pretty good curve. It's still it doesn't overheat. It goes very own and probably we need some kind of lower weight here. Yeah, okay so now this looks a lot like the best Rich regression that we got right? So the curve is approximately the same

**[1:37:26 – 1:37:36]** But if you look at the actual coefficients, you will see something very different. You will see that, like many of the coefficients have gone to exactly zero.

**[1:37:37 – 1:37:40]** And some are clearly, like, on their way to exactly zero.

**[1:37:42 – 1:37:52]** With which regression they were all decreasing more or less isotropically. So, to speak, right? There were all decreasing together, getting closer to 0.

**[1:37:53 – 1:38:00]** maybe not with exactly the same speed but they were all non-zero when we checked

**[1:38:02 – 1:38:02]** here.

**[1:38:03 – 1:38:09]** Some coefficients become exactly zero or very close to zero and you can send them exactly to zero. That's will change.

**[1:38:10 – 1:38:18]** And sometimes that are that desirable property, right? So sometimes you might want to have sparsity in the results.

**[1:38:21 – 1:38:23]** so, why this is

**[1:38:24 – 1:38:29]** This is what we would call a sparsity inducing regular race.

**[1:38:33 – 1:38:43]** And for example, I think it would be a better fit for our question over here. Right? So if I get a lot of different features and I need to choose out of them then

**[1:38:44 – 1:38:56]** It instead of some arbitrary setting, the threshold and you know picking which small number is better than another small number. Why not? Choose a different way of regularization to set some of them executive zero.

**[1:38:57 – 1:39:04]** Okay, so this is our choice. This this is this is an hour hand.

**[1:39:05 – 1:39:39]** Okay, so we need to have a break by now, but so let me summarize I discuss linear regression. We didn't go into the actual base and inference, it doesn't much matter for for the rest of our class. So it's okay, that we skip it, but I did want to highlight two important points. First linear regression is relevant to any kind of complicated neural networks still and we will see it in an architecture.

**[1:39:40 – 1:39:41]** But most importantly,

**[1:39:43 – 1:39:54]** all of this probabilistic machine and all of these discussions about likelihoods priors probabilistic assumptions how they all come together.

**[1:39:55 – 1:39:59]** What they are actually doing for us in deep learning.

**[1:40:00 – 1:40:03]** Is they are giving us the loss functions.

**[1:40:04 – 1:40:04]** Okay.

**[1:40:05 – 1:40:12]** so notice that when I write the general formula like this,

**[1:40:15 – 1:40:25]** It doesn't matter what the model is, right? It's just about, okay, so this is too general form, this is about everything, but when I write even a formula like this,

**[1:40:27 – 1:40:29]** Okay, the model is only over here.

**[1:40:30 – 1:40:45]** Right. And this is the noise distribution, but the linear model is only over here. And of course, I can change. If I keep the noise distribution, Goshen, I can change the model to something else.

**[1:40:46 – 1:40:50]** so if I was, I I can do any

**[1:40:52 – 1:40:54]** Kind of function over here.

**[1:40:55 – 1:41:12]** And maybe it will be more difficult to optimize. It will not be quite right, okay. It will be like completely different thing in terms of in practice but I still get the same kind of loss function, Square deviation and I still get the same kind of regularizer if I want.

**[1:41:13 – 1:41:23]** And this is still a very common loss function, whatever the model is, right? And this may be a neural network.

**[1:41:24 – 1:41:37]** Maybe a very complex neural network. It may be anything that we will discuss later in class, but then it gets plugged in to the loss function. That comes from some probabilistic assumptions that we make.

**[1:41:38 – 1:41:40]** That that's my point in the first part.

**[1:41:42 – 1:41:43]** Okay, any questions?

**[1:41:49 – 1:41:50]** Okay good.

**[1:41:50 – 1:42:12]** So let's have a break over here and then I will briefly discuss. Logistic regression will not go into the same kind of detail, but it's really important to get this, the soft Max function, right? So, we will discuss the main Assumption of the softmax and then finally, we'll get in your own networks. I promise break.

**[1:55:14 – 1:55:21]** Here.

**[2:00:56 – 2:00:58]** You.

**[2:02:23 – 2:02:24]** For me.

**[2:03:20 – 2:03:22]** Okay, let's continue.

**[2:03:23 – 2:03:26]** So we just discussed, linear regression before the brake.

**[2:03:28 – 2:03:34]** While you are gettering back, let me go through the slides to see what they missed.

**[2:03:35 – 2:03:42]** A linear regression sum of squares, the gaussian noise hypothesis.

**[2:03:43 – 2:04:00]** Blah, blah. You can get a posterior distribution, to get the predictive distribution. We didn't get there, unfortunately, by using regularization, we didn't derive this formula. No matter, this would be interesting, but I think it's time for us to move on.

**[2:04:01 – 2:04:04]** And yeah, and our next point.

**[2:04:05 – 2:04:07]** Is classification.

**[2:04:08 – 2:04:10]** Which is probably even more important.

**[2:04:11 – 2:04:14]** For deep learning for neural networks, then.

**[2:04:16 – 2:04:19]** Linear regression and predicting numbers.

**[2:04:20 – 2:04:22]** so how our third one point,

**[2:04:24 – 2:04:26]** Is the logistic regression.

**[2:04:27 – 2:04:37]** I'll try to be quick about it, but I do want to get the general idea across so

**[2:04:38 – 2:04:40]** suppose that we are sold in a classification problem.

**[2:04:41 – 2:04:56]** So what is specification like you have you want to distinguish cats from dogs? And if you are in a lower dimensional space, you can visualize it as trying to get separated decision surface between

**[2:04:57 – 2:04:59]** Two or more sets of points.

**[2:05:01 – 2:05:13]** The difference between logistic the difference between classification and regression is in the nature of Y, right? It's in the nature of the target variable.

**[2:05:14 – 2:05:23]** So it's still classification. Of course is still supervised learning. We still have a data set. That looks like this.

**[2:05:24 – 2:05:30]** But now for linear regression, why and was a number. But now I am is like a class label.

**[2:05:31 – 2:05:32]** Right. So it's

**[2:05:34 – 2:05:41]** Just, it just create variable with the finite set of values. It's one of several classes that we want to listen.

**[2:05:43 – 2:05:49]** So what does it mean for us for constructing, the model for building the likelihood for everything like that?

**[2:05:50 – 2:05:53]** It means that since we're not predicting a number,

**[2:05:55 – 2:05:55]** what?

**[2:05:57 – 2:06:01]** I mean, okay, not just since we're not predict number.

**[2:06:03 – 2:06:05]** it means that in most cases,

**[2:06:07 – 2:06:12]** even though we are not predicting a number, we still do want to have a number of the output.

**[2:06:13 – 2:06:15]** So, what is?

**[2:06:15 – 2:06:23]** Kind of bad about discrete Target variables and that will, we will come back to that in deep learning as well.

**[2:06:24 – 2:06:52]** The bad thing about the discrete Target variable. So let's say that I'm doing like a simple threshold rule for classifying and they have like one class is the 0 and then affects exceeds some threshold. Then I start to Output one, right? So this is like the simplest classifier possible, one dimension, one input to classes and they chose by threshold.

**[2:06:54 – 2:06:58]** What's the problem with this function? If it was my output,

**[2:07:00 – 2:07:02]** The problem is that.

**[2:07:02 – 2:07:03]** This function.

**[2:07:04 – 2:07:13]** Since its best ways constant, right? It has no derivatives, I mean does have derivatives, but it's derivative through 0.

**[2:07:14 – 2:07:24]** So what this actually means is that if so if this is just X and this is and the thing that I'm learning is on the A and that it's fine.

**[2:07:25 – 2:07:41]** But what if they input is actually some kind of as it, always happens in real life in neural networks and everywhere. What if the input is some kind of function of X with some weights? Some model some feature extractors Etc.

**[2:07:42 – 2:07:48]** If that happens then we don't know what to do with this feature structure, we don't know how to train it.

**[2:07:49 – 2:07:59]** Because you can take the gradients and we will be taking gradients in Dearing. And but if you take the gradient of this function,

**[2:08:00 – 2:08:01]** it's always zero.

**[2:08:02 – 2:08:05]** It's, it doesn't give us any any information at all.

**[2:08:06 – 2:08:20]** And you can understand that intuitively is supposed that I take the weights W and I take them a little bit I change them slightly then the input to this fresh hold will move a little bit.

**[2:08:22 – 2:08:24]** Did it move in the right direction or in the wrong direction?

**[2:08:25 – 2:08:33]** By looking at the output we have, absolutely, no idea. There are output, does not change, it does not change, it does not change, it does not change and suddenly changes.

**[2:08:34 – 2:08:37]** That's not something that we can actually trade through.

**[2:08:40 – 2:08:49]** um, so what we actually want and both for this practical reason and also for conceptual reasons like

**[2:08:52 – 2:09:07]** Both for this practical reason and for conceptual reasons like we also want to estimate our uncertainty. We want to evaluate how sure we are, what we actually want to have the output of a classifier.

**[2:09:08 – 2:09:14]** Is not just the class label but a probability distribution, of course.

**[2:09:15 – 2:09:22]** So let's start with two classes if I only have C1 and C2. What I actually

**[2:09:23 – 2:09:25]** Get some dogs, right?

**[2:09:26 – 2:09:32]** What they actually want to have? The output is p of C1 given X.

**[2:09:33 – 2:09:34]** Okay.

**[2:09:35 – 2:09:36]** if you want to give an X,

**[2:09:37 – 2:09:40]** That is for a new point.

**[2:09:41 – 2:09:42]** I want to evaluate.

**[2:09:43 – 2:09:49]** How likely it is that it belongs to to the first class as a second?

**[2:09:52 – 2:10:17]** And where, where does the logistic regression appear? What's, what's the reasoning behind it? Well, actually, it's, it's pretty, it's pretty straightforward or I mean, we could make it more complicated, but it's not a straightforward reasoning. Behind logistic regression, looks like this. So, let's assume that I want a linear model.

**[2:10:18 – 2:10:28]** So I do want to have a linear Model A linear separating surface. I do want something that includes W Times X and that's how X should appear in their

**[2:10:33 – 2:10:34]** you know, question.

**[2:10:34 – 2:10:41]** I also got an also got a window that's at internet's unstable.

**[2:10:42 – 2:10:44]** Did it fix itself? Is it okay? Now.

**[2:10:54 – 2:10:55]** Want to.

**[2:10:57 – 2:11:02]** Sometimes yeah, yeah, it's right in case.

**[2:11:04 – 2:11:04]** Unintelligible.

**[2:11:05 – 2:11:06]** Uh-huh.

**[2:11:06 – 2:11:12]** Okay, so okay if it's better now then just keep me informed if anything changes.

**[2:11:14 – 2:11:20]** Okay. So anyway, suppose I want PFC one given X

**[2:11:20 – 2:11:22]** And I wanted to be.

**[2:11:24 – 2:11:32]** To be derived from like a linear function of the features. So I want the access the inputs to have.

**[2:11:32 – 2:11:35]** A linear to go through linear function.

**[2:11:36 – 2:11:36]** so,

**[2:11:38 – 2:11:38]** Can I?

**[2:11:39 – 2:11:45]** Take this probability and the proximate like I did and linear regression with a linear function of the inputs.

**[2:11:47 – 2:11:59]** Kind of obviously not right, because the probability chair is a number between 0 and 1. And if they approximated with the linear function, of course, it will go to Infinity at one and the other end everywhere.

**[2:12:01 – 2:12:07]** So it's not a good idea to operate to model probabilities by linear functions, right?

**[2:12:08 – 2:12:10]** What can I do instead? Well?

**[2:12:11 – 2:12:16]** I can use the best theorem here of X, you know, see one.

**[2:12:17 – 2:12:21]** BBC, One P of X, right?

**[2:12:24 – 2:12:33]** And then I can expand this. Since I only have two outcomes to classes, it's pretty easy. You can just say the pox

**[2:12:34 – 2:12:39]** Is one possible numerator, plus the other possible numerator.

**[2:12:40 – 2:12:40]** Right.

**[2:12:41 – 2:12:48]** Now, I have a lot of different things in here and I only want to model one thing. So let me

**[2:12:49 – 2:12:56]** Divide by the numerator and I get one over one plus P of x given c, 2, c, 2.

**[2:12:57 – 2:13:02]** Divided by P of x given C1 times P of c 1.

**[2:13:02 – 2:13:03]** Okay.

**[2:13:04 – 2:13:05]** so, this thing,

**[2:13:07 – 2:13:14]** You can view it as P of C2, given x divided by P of C1. Given X is the same thing.

**[2:13:16 – 2:13:19]** And this thing is known as the odds.

**[2:13:20 – 2:13:22]** Right. So the odds are

**[2:13:23 – 2:13:42]** Oh, like when you say in real life, when you say, I give you 50 to 1 oats, what does 50 to 1 minute creates this ratio, right? It's the ratio of the probability of a sign. For one outcome divided by the probability of the other. That's that's what it means to give thoughts.

**[2:13:44 – 2:13:56]** Ah, and as I just said, odds can be like 50 to 1 or 1 to 50, right? So odds are not constrained by one. They are ratio of two probabilities, so they go they can go to Infinity.

**[2:13:58 – 2:14:02]** But does it make sense to model them as a linear function?

**[2:14:04 – 2:14:05]** Well again, not really.

**[2:14:06 – 2:14:20]** Because even though they can go to Infinity, they still cannot be negative, right? It's ratio of two probabilities and the linear function will be negative somewhere, but half of the space. It will be angry.

**[2:14:21 – 2:14:21]** so,

**[2:14:22 – 2:14:34]** this is also not a nature thing to model with the linear function, but we are getting there. Just one small step left. We have a positive quantity, and we want to model it, somehow linearly

**[2:14:35 – 2:14:50]** What is the transformation that we need? Oh, we can take the lock, right? So, if you take the lock of some of some of something that goes from 0 to Infinity, not including zero, then now you get something to goals from negative.

**[2:14:52 – 2:15:00]** so then we go to this, e, to the power, it's customary to put the minus sign here, it doesn't really matter, but

**[2:15:00 – 2:15:07]** Usually people do. So now the fraction flips the ratio flips

**[2:15:09 – 2:15:11]** POC to

**[2:15:12 – 2:15:14]** so, this guy

**[2:15:15 – 2:15:17]** is called the logos.

**[2:15:19 – 2:15:20]** The logarithm of the odds.

**[2:15:21 – 2:15:44]** And now, this indeed does make sense to model with a linear function because now it's a quantity that goes from negative Infinity to infinity and it has exactly the properties that we want at negative Infinity, go to 0, the probability goes to 0 at positive Infinity, the probability goes to 1 and in between at 120 increase.

**[2:15:46 – 2:15:51]** So logistic regression is exactly as well.

**[2:15:52 – 2:15:58]** Which is a regression is the model where you say that P of C1 given X.

**[2:15:59 – 2:16:05]** Is 10 over 1 plus e to the power, minus a linear function of x.

**[2:16:08 – 2:16:12]** This function is called the logistic sigmoid.

**[2:16:14 – 2:16:22]** so Sigma of a is like 1 over 1 plus, e, to the power minus a and it's this

**[2:16:23 – 2:16:30]** It's a sigma function, right? So it goes from negative Infinity to Infinity. It goes through one. Half at zero,

**[2:16:32 – 2:16:36]** And it asymptotically goes to one or on the right into the 0 in the left.

**[2:16:38 – 2:16:40]** It's an important function machine learning.

**[2:16:41 – 2:16:56]** Then we get, what is p of C2? Given X. Well, unfortunately, it's a bit more complicated because it's one minus Sigma of W Times X, right? So, if I try to do like,

**[2:16:59 – 2:16:59]** The.

**[2:17:01 – 2:17:04]** Likelihood of data set for logistic regression.

**[2:17:05 – 2:17:42]** Again, I I do a product of P of YNS, given W and X sense, but then it will be a product of like sometimes it's Sigma and sometimes it's one minus Sigma and then it's Sigma and then at Sigma and then it's 1 minus segment. So on, right? So it's a bit more complicated, it's more complicated function than the linear regression. We cannot get it's not quadratic of course anymore and we cannot do it in closed form but we can be something like gradient descent or second order methods. In this case also can be used.

**[2:17:43 – 2:17:50]** We can actually optimize the likelihood. We can add prayers and do it in a regularized way and so forth.

**[2:17:50 – 2:17:51]** so, this is

**[2:17:52 – 2:18:04]** This is actually a linear model in machine. Learning institutes. A linear model, is something that that is a function of this. It doesn't have to be linear all the way, but X is

**[2:18:05 – 2:18:09]** Occur in there in a linear combination.

**[2:18:10 – 2:18:16]** And it's a very natural linear model for classification. For binary classification.

**[2:18:18 – 2:18:24]** How do we make it more than binary? How do we make? How do we insert several classes here?

**[2:18:25 – 2:18:37]** Well here I was just modeling while one quantity and if I have like basically going to us, if I have only two classes, then sure I only need to model one probability.

**[2:18:39 – 2:18:43]** But if I have several classes, you want to see k?

**[2:18:44 – 2:18:46]** Then now it's not enough.

**[2:18:47 – 2:19:03]** To model, it's not enough to have only one vector W. That is multiplied by X. Because from one number, I will not get K. Minus one different numbers, right? And I need game -20 different numbers to model. This diro between Kate classes,

**[2:19:04 – 2:19:13]** So instead now I basically say that okay well I will not model a single logo for between two classes. I will just

**[2:19:16 – 2:19:21]** Say this. So P of C Small key given X.

**[2:19:22 – 2:19:36]** Just like this, it's p of C Smalls. He's okay divided by the sum overall classes, right? B u c s p o, x x given c s.

**[2:19:37 – 2:19:42]** Ah, and let me just again, take the logs so I can also have negative numbers.

**[2:19:44 – 2:19:47]** So, e to the power of this.

**[2:19:50 – 2:19:55]** Divided by the sum of e, to the power of the same but about class s.

**[2:19:56 – 2:20:03]** And then, let me just say that. Now I'm modeling every exponent here with its own linear function,

**[2:20:03 – 2:20:08]** So, I'm saying that like WK times x.

**[2:20:09 – 2:20:14]** Should be like P of c k times P of x given c k.

**[2:20:16 – 2:20:52]** No notice that. It doesn't quite work as I wrote it because they did the thing on the right cannot be negative. They just said it's a bad thing but to be honest it doesn't matter. So when you get negative numbers from some of the scores this are usually cool scores or affinities or something like that. So it's like a measure of how like a plus K is but not the probability just a number, right? So when you get Negative scores, you can just

**[2:20:55 – 2:21:30]** Cancel, out the negative parts. So if you have like, e to the power, minus 2 divided by e to the power 1 plus, e to the power, minus 1 plus, e to the power minus 2, the same, then you can just take e to the power minus 2 and cancel it out, right? So, and everything becomes non-negative right now, it's e to the power 0, e to the power of 3 plus E1 plus e 0, that's it, right? So you can always in this formula you don't, it doesn't matter if sometimes you get negative because you can always send a baseline like this and it just cancels out.

**[2:21:32 – 2:21:33]** And that's it.

**[2:21:34 – 2:21:59]** So this is how you do multi-class classification and this thing now it's a vector function, right? So now it's a function that Maps the vector a to another Vector full of this guys. So like the case coordinate is it to the power, a k divided by the sum of e to the power, a s.

**[2:22:00 – 2:22:01]** Right normalized.

**[2:22:02 – 2:22:03]** Normalized exponents.

**[2:22:05 – 2:22:07]** Ah, and this is called the softmax function.

**[2:22:08 – 2:22:09]** so, the softmax

**[2:22:11 – 2:22:11]** Of.

**[2:22:12 – 2:22:24]** Okay, let me write it again. A1 and A2. AK is another vector. And at the case spot, we have e to the power AK normalized so that it becomes a vector of probabilities.

**[2:22:26 – 2:22:47]** That's it. That's the softmax are why is it called the softmax? Because the exponents have this tendency to, you know, exaggerate the differences. Like if you have one of the ace, one of the arguments to be significantly larger than the others.

**[2:22:48 – 2:23:01]** Then what you get is a result, will the basically probability one for this guy and probability about your of the others. So, we are kind of taking the maximum of, of the arguments.

**[2:23:02 – 2:23:13]** But we are doing it in a soft way with as a continuous function, that is never exactly zero. That you can take your relatives of that allows for gradients, gradient descent Etc.

**[2:23:14 – 2:23:18]** so that's a soft version of taking the arc, Max

**[2:23:22 – 2:23:36]** Okay, and I won't go into more details about logistic regression. Not exactly our subject, but this part is important because again, this is the last layer of almost every neural networks.

**[2:23:37 – 2:23:38]** if you have,

**[2:23:39 – 2:23:42]** if you have, I don't know GPT file.

**[2:23:43 – 2:23:59]** Which is an insanely complicated model. I have no idea how exactly it works because nobody tells us, but if you have Jupiter 5 and it's a language model and its supposed to produce the next door. Can right now then, what is the last layer of gp35 frame. Sure.

**[2:24:00 – 2:24:09]** The last layer is this, after all of this internal Machinery, which is very complicated. We get LA or of scores.

**[2:24:11 – 2:24:14]** For every tokens for every token.

**[2:24:15 – 2:24:17]** And then they go through the software.

**[2:24:19 – 2:24:24]** And the softmax turns them into the probabilities of tokens.

**[2:24:25 – 2:24:47]** That's that's that's how it always works at the end because it's completely hopeless to try to to produce probabilities like immediately. It's, it's not how when neural networks work, it's not how linear functions work, it's not how anything Works. What you do is you produce some kind of scores and then you

**[2:24:48 – 2:24:51]** turn them into probabilities with the software.

**[2:24:52 – 2:25:01]** And yeah, sure. It's also very common. Now, I cannot watch for gb5, but it's also very common that the layer between the before this is linear,

**[2:25:01 – 2:25:07]** so we get an exact logistic regression at the end of your

**[2:25:08 – 2:25:16]** So we get to some features when we do a linear layer, that gets so this lead. So okay.

**[2:25:18 – 2:25:26]** Let me explain because I will I don't think I will explain it later and now it's a good spot. So we have some input.

**[2:25:28 – 2:25:32]** it goes through the neural network and then,

**[2:25:32 – 2:25:46]** Let's say we get to the final feature Vector, right? The final like semantically reach, very intricate extracted features and whether it's a cat or a dog is already somewhere inside.

**[2:25:46 – 2:25:55]** Somewhere in this feature. So it says so pretty explicitly, but we are still not sure where and we are not sure how to to get, right? So,

**[2:25:56 – 2:25:59]** What how do we do it? How do we

**[2:25:59 – 2:26:04]** What is the simplest way to process? This already extracted features. Well,

**[2:26:06 – 2:26:15]** I could just do a softmax and assume their scores, but they're not scores and there's probably the wrong number of them, right? So there are

**[2:26:16 – 2:26:22]** There is some some number of classes and here I have just extracted features that express my picture.

**[2:26:23 – 2:26:27]** Why should the numbers match? No reason, right? So the number of features can be different.

**[2:26:28 – 2:26:30]** So I do weight Matrix.

**[2:26:31 – 2:26:37]** I multiply W Times C and the wait Matrix so let's say this is dimension d.

**[2:26:37 – 2:26:45]** And this is dimension. Okay? Like number of classes so w is of Dimension D times k.

**[2:26:45 – 2:26:49]** And then W Times C becomes the vector. Of course.

**[2:26:50 – 2:26:51]** and now,

**[2:26:52 – 2:26:54]** I go through softmax.

**[2:26:56 – 2:26:56]** and I get,

**[2:26:57 – 2:26:59]** A vector of probability.

**[2:27:00 – 2:27:03]** Vector of probabilities for all the classes that I have.

**[2:27:04 – 2:27:09]** And this is my output and the loss function now.

**[2:27:10 – 2:27:18]** Will be defined on these probabilities. So the there may be some variation here but usually the loss function is just

**[2:27:19 – 2:27:24]** The well, it's a fancy name. It's the cross entropy between the output and the

**[2:27:28 – 2:27:32]** Output and the target. But if you are doing classification, the target.

**[2:27:34 – 2:27:40]** Looks like a one-hot vector with one one at the correct class.

**[2:27:41 – 2:27:58]** And 0s on the other classes, right? So, and the cross entry here, when we get there, I will write it in more detail, but the cross entry before this kind of Target will be basically, just saying that I want to have the probability of the correct question to be larger.

**[2:27:59 – 2:28:06]** So like the Lost function will be something like the negative. Look P of the correct class.

**[2:28:07 – 2:28:12]** And I want this to be blowers accordingly.

**[2:28:14 – 2:28:18]** Um and that's it. That's how classification Works in deep learning.

**[2:28:18 – 2:28:18]** Okay.

**[2:28:20 – 2:28:27]** So the interesting stuff happens over here. Of course, that's what we are going to be discussing for the rest of the class.

**[2:28:27 – 2:28:32]** But at the end, almost inevitably happens, something like this.

**[2:28:32 – 2:28:43]** So at the end if you're doing classification you want a vector of probabilities at the output. Can you get a vector of probabilities directly? Probably not,

**[2:28:44 – 2:28:58]** What you can get is a vector of scores Affinity like numbers that can be arbitrary, but that reflect how well, they input matches one of the classes and then you can convert them that that's how the stuff first.

**[2:29:00 – 2:29:01]** Okay.

**[2:29:02 – 2:29:06]** Any questions about logistic regression? I didn't go into much detail.

**[2:29:10 – 2:29:10]** All right, then.

**[2:29:11 – 2:29:12]** Then.

**[2:29:14 – 2:29:15]** For the rest of this lecture.

**[2:29:16 – 2:29:17]** Let's concentrate.

**[2:29:18 – 2:29:20]** On neural networks.

**[2:29:20 – 2:29:21]** and actually,

**[2:29:25 – 2:29:25]** Have.

**[2:29:27 – 2:29:29]** Yeah, yeah. I don't have

**[2:29:30 – 2:29:43]** I don't have illustrations for classification called but that's fine that it wouldn't show you anything anyway. It would be just a linear surface between two classes or three classes, but what's the point?

**[2:29:44 – 2:30:05]** Yeah, so we discussed logistic regression. This is what Logistics Sigma, it looks like. Then we get logistic regression. This is the softmax function. This is what we model for the softmax etc, etc. And logistic regression even though it's very

**[2:30:06 – 2:30:08]** It's a very simple model.

**[2:30:10 – 2:30:18]** It's a linear model like one step from from linear regression. So linear regression is just linear. This one is linear plus Sigma on top.

**[2:30:19 – 2:30:27]** But already for logistic regression. We cannot really hope to get the closed form solution.

**[2:30:28 – 2:30:31]** So we didn't discuss it for.

**[2:30:32 – 2:30:45]** Linear regression but because it really doesn't pertain to the parent. But when you're optimizing quadratic functional like this, you can just write down the answer.

**[2:30:46 – 2:31:10]** It will be maybe not that easy to actually Implement because it will be like the inverse of some huge huge Matrix. And in practice you would be like solving the system of linear equations with some approximate techniques, iterative approximate techniques. And I mean, it's it's a whole science but theoretically, you can just write down the answer. You can write down the formula.

**[2:31:11 – 2:31:14]** And it's a system of linear equations, after you take the green.

**[2:31:15 – 2:31:16]** Here.

**[2:31:18 – 2:31:19]** It's already not.

**[2:31:20 – 2:31:28]** Right? So if you look at a big product, okay? And you take a look and then if you have a big sum of logs of things like this, and things like this,

**[2:31:29 – 2:31:34]** There is no clothes phone search, right? So the only thing we can do is

**[2:31:35 – 2:31:40]** try to do it with some iterative optimization algorithm.

**[2:31:41 – 2:31:49]** And the main iterative optimization now Christmas, that we will be discussing tomorrow in great detail as of course, gradient descent.

**[2:31:49 – 2:31:49]** so,

**[2:31:51 – 2:32:00]** In in logistic regression, you can actually do a second order method, but in neural networks, you can't afford to discuss that as well.

**[2:32:01 – 2:32:24]** And we have to restrict ourselves to variations of gradient descent gradient sentence. When you start somewhere and you go in the direction where the loss function is really is being reduced most quickly and that is the direction opposite to the gradient of the gradient is the direction of where it grows most weightless. Well the opposite is where it

**[2:32:26 – 2:32:26]** decreases mostly

**[2:32:28 – 2:32:31]** and then you keep going until you

**[2:32:32 – 2:32:42]** find the local minimum. There can be many local minimum in real life in neural networks, Etc. And we'll discuss that in detail but not for

**[2:32:44 – 2:32:45]** not for logistic regression.

**[2:32:46 – 2:32:46]** All right.

**[2:32:48 – 2:32:48]** so, with that,

**[2:32:49 – 2:32:55]** Let me move on to some last May the medical far less mathematical topic but I hope also pretty interesting.

**[2:32:56 – 2:33:12]** And that is an introduction to keep learning, right? I will again, try to make it quick and painless I don't want to go into too many historical details or anything, but there are a few things that I want to highlight.

**[2:33:13 – 2:33:17]** a few things in the motivations, if you thinks in the

**[2:33:21 – 2:33:23]** Like how neural networks evolved.

**[2:33:24 – 2:33:25]** and then, we'll just

**[2:33:26 – 2:33:29]** Go to the main meat of our class, that will be probably tomorrow.

**[2:33:30 – 2:33:30]** so,

**[2:33:33 – 2:33:45]** Neural networks. Artificial neural networks are called artificial because there are natural neural networks right. There are neural networks in our brains and in the brains of other living beings.

**[2:33:47 – 2:33:47]** and,

**[2:33:48 – 2:33:50]** Of course, a very natural.

**[2:33:53 – 2:33:59]** Motivation for for a scientist would be well, I want to build a thinking machine.

**[2:34:00 – 2:34:05]** There already are thinking machines in the world. I have a proof of concept right here.

**[2:34:06 – 2:34:15]** So let me study how the thinking machine in here works, and let's try to emulate it in a computer, why not? It's all information process.

**[2:34:17 – 2:34:21]** and when you begin to study how the human brain works, it's actually

**[2:34:23 – 2:34:37]** it actually gives you some pretty important insights. So sorry my picture. Now this is not an artifact Defense. Net Connection for some reason, it is down. Simple lot. But anyway,

**[2:34:40 – 2:34:48]** Probably you have you probably have heard at some point, how neurons work? What a neuron is. So our brain consists of neurons

**[2:34:48 – 2:34:57]** Biologists will tell you that there are different kinds of neurons. There are slight differences but for our from our computational perspective, they're basically all the same

**[2:34:58 – 2:35:00]** and they work like this.

**[2:35:01 – 2:35:11]** they have this processing part, the Soma the actual like mid center of the cell and then it has all sorts of

**[2:35:14 – 2:35:14]** tentacles.

**[2:35:15 – 2:35:30]** All sorts of little things, going out of the cell and connecting to other things. Right. And there are two kinds of tendrils, I guess the better word would be. There are two kinds of this.

**[2:35:33 – 2:35:33]** Growth.

**[2:35:35 – 2:35:44]** There are the rights which are relatively short and which attach to the outputs of other neurons.

**[2:35:44 – 2:35:46]** And they provide inputs.

**[2:35:47 – 2:35:56]** So from the there are many, there is for every neuron and the dendrites get inputs for this neuron.

**[2:35:57 – 2:35:58]** Okay.

**[2:35:58 – 2:36:00]** And then, there is one.

**[2:36:01 – 2:36:08]** special part one, special tentacles of the neuron, which is called the Axon

**[2:36:08 – 2:36:29]** and the excellent can be very long. There is a neuron, there is a neuron in your spinal cord. That goes all the way to your toe, right? To every one of your toes. Actually, there are separate neurons. So they can be like up to a meter length or something. And the point is the

**[2:36:30 – 2:36:37]** Axon is the output computationally everywhere. Has lots of inputs, several thousands on average.

**[2:36:37 – 2:36:39]** And one output.

**[2:36:40 – 2:36:40]** Okay.

**[2:36:41 – 2:36:44]** So far, so good, pretty straightforward.

**[2:36:46 – 2:36:59]** Now what is interesting about this and this is a purely like computational very surface like inside but it's already pretty interesting in the brain.

**[2:37:01 – 2:37:06]** So first of all, how does a neuron work like physical? How does it say something else?

**[2:37:07 – 2:37:16]** It would be pretty difficult for a biological thing for a biological mechanism to read out numbers.

**[2:37:18 – 2:37:28]** so like it would be pretty difficult for the dendrites to capture like the exact amplitude of an electrical signal and then

**[2:37:30 – 2:37:40]** Process inside the neuron that from this input. I got a 2.5 and from that input. I got negative 1.46 that, that's not how biology works.

**[2:37:41 – 2:38:08]** Biologically, it's much easier, and faster and more reliable to just capture bits individual events. Like, is there a spike or is there not a spike? So, neurons work actually. Inspects they do not, or almost do not much late, the amplitude of their signals. So the spike. Yeah, I didn't tell a spike is the electrical signal that the neuron sends out through its Axon

**[2:38:09 – 2:38:18]** So the neuron always fires spikes along its actions and the other neurons who are attached to, they pick up the signals.

**[2:38:20 – 2:38:31]** And the spikes are more or less the same. I think there is some variation but it's not, it's not consequential. There are more or less the same. What changes is the frequency of the specs?

**[2:38:32 – 2:38:44]** So if the neuron is relaxed is not excited, then it turns out spikes with frequency like 10% 20%, something like this.

**[2:38:44 – 2:38:48]** When it gets really excited, really activated.

**[2:38:48 – 2:38:53]** It starts sending out spikes with the frequency of like 200 Specs.

**[2:38:53 – 2:39:00]** okay, so there is a big range and when a neuron sends out spikes,

**[2:39:01 – 2:39:16]** More often, it means. It's it's more excited. So now there is actually numerical value. It can be more excited or less excited. It's not binary. But every spike is the same and it's just transmitting basically one bit, but a different controls.

**[2:39:18 – 2:39:19]** and,

**[2:39:20 – 2:39:23]** the interesting point about this is that

**[2:39:24 – 2:39:26]** we have lots.

**[2:39:26 – 2:39:38]** Lots and lots of neurons. I think artificial neural network still haven't reached the sheer number of neurons of the human brain or maybe have just reached that, I'm not sure. So,

**[2:39:40 – 2:39:44]** In the human brain have like 100 billion.

**[2:39:45 – 2:39:50]** Um no, okay, yeah, yeah right we have like a hundred billion neurons.

**[2:39:52 – 2:40:20]** And every neuron. So you know that there are neural networks with 100 billion and trillion weights, right. But the way it is not in Europe, the weight for in a bio in the biological brain is on the connection between the neurons. Right? So the weight is attached is like the ways are in the synopsis. In this connections where a dendrite of one neuron takes to the extent of another

**[2:40:21 – 2:40:43]** And yes there are weights there so the it really in some way, it's likely in your combination, not really? But like so there are connections that get reinforced. There are connections that get inhibited, there can be negative ways, they're all sorts of things. So there are indeed weights at the synopsis that are learned that are trained in human, right?

**[2:40:44 – 2:40:49]** and that's how we think, that's how we learn stuff, but the point is

**[2:40:50 – 2:41:05]** How many weights are there in the human brain? How many parameters well have like 100 billion neurons and if each one on average has several thousands of 7,000 Senators. So if you multiply you get something like

**[2:41:06 – 2:41:20]** What's the quintillion or a bit less than a continued of, of synapses of Weights that are being trained in our brain? That's a huge amount. I think artificial neural networks have not yet reached that

**[2:41:21 – 2:41:21]** but,

**[2:41:22 – 2:41:24]** On the other hand.

**[2:41:25 – 2:41:27]** It's extremely slow.

**[2:41:27 – 2:41:28]** Right.

**[2:41:28 – 2:41:34]** so, I just told you that our brain is a computer that operates on the

**[2:41:36 – 2:41:38]** frequency of

**[2:41:39 – 2:41:42]** 10 to a couple hundred Hertz.

**[2:41:43 – 2:41:51]** Right. A couple of hundreds signals per second, not megahertz, not kilohertz, just hurts.

**[2:41:52 – 2:42:04]** And so the brain is very, very slow as a computer if you were talking about like, clock speeds, but it's huge in terms of the number of connections.

**[2:42:06 – 2:42:08]** And what this actually means.

**[2:42:09 – 2:42:10]** Is.

**[2:42:11 – 2:42:21]** The brain always performs highly parallel computations but cannot perform a long. Sequential computation simply doesn't have time.

**[2:42:22 – 2:42:42]** So for example, we recognize a phase, recognizing faces, a difficult task in computer vision, it's a difficult task, but we recognize a face in like a couple 100 milliseconds, right? And that's like the full cycle of, between the time when I show you the phrase and the time, when you press a button to, you know,

**[2:42:44 – 2:42:59]** to record that you have recognized the face. So it's the full cycle of feature extraction decision making motor command to the finger everything and it all fits into like two or three hundred milliseconds.

**[2:43:00 – 2:43:21]** So, what this actually means is that this is an actual picture of how it goes through the brain, maybe we will get back to this picture when we discussion, but maybe not. And what the section means is that the brain cannot have like a loop for I from one to 1000.

**[2:43:22 – 2:43:24]** It doesn't have time to do.

**[2:43:25 – 2:43:31]** It only has time for like 10 or 15 sequential steps of computation.

**[2:43:32 – 2:43:40]** And then it has to get out the answer out. Otherwise, you are already being written by land, right? And

**[2:43:41 – 2:43:42]** so,

**[2:43:43 – 2:43:46]** It's the cognitions are not sequential.

**[2:43:47 – 2:43:53]** But they are very, very highly parallel. So when you're, when we recognizing, if it's like half of our brain lights up.

**[2:43:54 – 2:44:03]** But half of our blade brain lights up, but it lights up in like 10 steps sequential. And then we have to give the answer.

**[2:44:07 – 2:44:15]** In a way, this is a this is the property of a brain of the brain that we actually keep in artificial neural networks. So

**[2:44:17 – 2:44:20]** we will just discuss how to make your own networks, really, really deep.

**[2:44:20 – 2:44:28]** We build discuss networks with 100s of layers and I will tell you that you can go to thousands just doesn't make sense.

**[2:44:30 – 2:44:42]** And yeah, it doesn't make sense. So in actually our current artificial neural networks, okay, maybe they know they have more than 10 or 20 layers, maybe they have 100, but not much more than that.

**[2:44:42 – 2:45:10]** So we don't we don't know how to make use of tens of thousands of layers in the neural network and let's say the proverbial GPT 5 is probably very very wide. It's probably like a mixture of experts that have been trained to the different things, blah blah, but in terms of the number of layers of sequential computations it's probably like a few dozen. Maybe a couple hundred not more. I'm pretty sure.

**[2:45:13 – 2:45:18]** so this kind of white blood cell thing, we will keep

**[2:45:20 – 2:45:34]** And the main, but the main part of the motivation, is not, of course, in the architecture, we will see that the architecture cannot be the architectural cannot be the same. It's by definition kind of very different, but

**[2:45:37 – 2:45:38]** The.

**[2:45:40 – 2:45:41]** but,

**[2:45:43 – 2:46:00]** What we actually want to get from like what is the Department of of the motivation that we actually want to reproduce in computers is how versatile? How adaptive

**[2:46:01 – 2:46:03]** How elastic our brain is.

**[2:46:04 – 2:46:13]** So, we can learn on very few examples and we can learn some, very, very complicated stuff on very small data samples, right?

**[2:46:14 – 2:46:17]** We can adapt new data sources.

**[2:46:17 – 2:46:28]** There are experiments like this one where you can actually like you know learn to see with your tongue or something. This this is called neuroplasticity and this was a fun experiment.

**[2:46:30 – 2:46:50]** You do you make a small plate of electrodes? And it's the tongue just because the tongue is sensitive and a connection, really distinguish between a lot of electrodes on the tongue, but it doesn't matter. You just put it somewhere on you and then you send to the electrodes a signal from a camera picture for it.

**[2:46:51 – 2:46:52]** And then you just walk around.

**[2:46:53 – 2:46:56]** And you feel a slight tingling from the electricity?

**[2:46:56 – 2:47:02]** and then you stop feeling it, of course very soon because the brain and ups and stops noticing it but

**[2:47:03 – 2:47:14]** In if in a few days of working around this camera, your brain starts to know just that there is an actual correlation between what you see and what the stinging looks like.

**[2:47:16 – 2:47:26]** And there have been experiments that like after a couple of weeks of working around with this stuff, you can actually close your eyes and see through this.

**[2:47:27 – 2:47:34]** Through you through this electroplate. Maybe not read books, but like at least walk around that not bump into a wall station.

**[2:47:35 – 2:47:35]** So,

**[2:47:39 – 2:47:59]** And for example, you probably have heard of neuroplasticity examples. Like when somebody I know has a stroke and part of the brain stops working, sometimes it's too much over damage and the person never recovers, but sometimes they recover sometimes other parts of the brain.

**[2:48:00 – 2:48:11]** Take on the functions that were previously done by this now, missing part and that's, that's all. So, something that our brain can do, so, in a way,

**[2:48:13 – 2:48:38]** This kind of experiments. Tell us that the brain. Yes, it does. Have I predetermined areas predetermined by the ocean? Like, yes, we have our visual cortex is back there in the occipital. Lobe of the brain. Our frontal cortex is to usually doing the reasoning decision-making. Yes,

**[2:48:38 – 2:48:46]** But it's kind of incidental, so yeah, sure it will be this way, but the neurons are still the same.

**[2:48:47 – 2:48:48]** and,

**[2:48:50 – 2:48:58]** They there is some kind of a single learning algorithm inside the human brain that can be applied to all of these sorts of different situations.

**[2:48:59 – 2:49:04]** There is there are no neurons in the brain that have evolved to distinguish cats from dogs.

**[2:49:04 – 2:49:06]** This is a learned thing, of course.

**[2:49:07 – 2:49:27]** And there are no neurons in the brain that are like from birth regionally evolved to already distinguish and understand the 3D structure of the world around us computer vision suppose to do now. That's that, that's that cannot buried in the chains. There is not enough information that you just to write it down.

**[2:49:29 – 2:49:35]** This is all learned. This is all learned from scratch and this is learned with very high efficiency and the early stages of our life.

**[2:49:36 – 2:49:43]** So, we do want to have it in computers, right? That was the original motivation for neural networks, and

**[2:49:44 – 2:49:45]** As we will see.

**[2:49:48 – 2:49:56]** yeah, as we will see, we in artificial neural networks, we do keep this

**[2:49:57 – 2:50:01]** A general idea which is known as connectionism.

**[2:50:02 – 2:50:15]** Connectionism. Is this philosophical part mathematical idea that if you connect a lot of simple things together the huge composition of very simple. Things becomes very complicated and can do very interesting stuff.

**[2:50:16 – 2:50:46]** That. That's as simple as it gets and it's true. Right. There are lots of mathematical results about this. Like how you can approximate anything with a polynomial and approximately anything with like two layers of one University functions. You there are lots of, here's number of results about it. And neural networks are kind of based on this idea. You take very simple things. You put them together and you get a very complicated thing like a face recognition system.

**[2:50:48 – 2:50:49]** but in the way,

**[2:50:50 – 2:51:00]** That's and yeah. And another thing where artificial neural networks are really, really similar to the human brain is the structure of a single neuron

**[2:51:01 – 2:51:05]** We will come back to it, just right now and later.

**[2:51:06 – 2:51:25]** We will see the so. Okay, let's come to it right now. No point in leaving it for the future. So how does what does a neuron look like an artificial neural? Like this most basic building block of neural networks

**[2:51:26 – 2:51:30]** Well, it has some inputs that's One X to x n.

**[2:51:31 – 2:51:41]** It looks just like the linear models that we discussed just now, that's in part. That's why I'm discussing always discussing them. Then you multiply them.

**[2:51:42 – 2:52:01]** By the way, of this neuron and you get W Times X, you get this linear combination of inputs, with with the weights, the weights will be trained during learning of the network, but then you also need to have a nonlinear function before you can get to the output.

**[2:52:03 – 2:52:04]** Why. Because

**[2:52:05 – 2:52:19]** if you, if you're new ones were doing just linear regression, if you're neurons or did not have an nonlinear function, which is called the activation function, then there would be no point to

**[2:52:20 – 2:52:36]** There would be no point to have a network because, you know, composition of linear functions is linear again. Now, if I have a huge Network full of linear neurons, it's basically just one neuron applied to the hole. There is no difference.

**[2:52:37 – 2:52:37]** so,

**[2:52:39 – 2:52:42]** with linear functions, I will not get more complicated things.

**[2:52:43 – 2:53:00]** But as soon as I have any kind of non-linearity, we will just discuss. Just now what kind of non-linearity is there are and there are very simple ones. As soon as I have any kind of nonlinearities, even something like real, which is just two linear functions strained together.

**[2:53:02 – 2:53:16]** It starts to work and there is a big field of math that shows that any kind of a linearity is enough to approximate anything. It doesn't really matter in practice for us in practice, for what matters is that it works?

**[2:53:16 – 2:53:17]** so,

**[2:53:19 – 2:53:23]** as soon as we have any sort of nonlinearity it,

**[2:53:24 – 2:53:40]** Starts compositions of this simple neurons. Begin to approximate whatever but whatever you want it. Which still lives open the question of how to approximate how to find the way. It's how to train will discuss that. What? But basically, as soon as we have an nonlinear, we can

**[2:53:42 – 2:53:46]** and interestingly enough, this kind of

**[2:53:48 – 2:53:53]** Model for a single. Artificial neuron has been with us since 1943.

**[2:53:54 – 2:54:04]** since before the Turing test since before, the Dartmouth seminar, before the word artificial intelligence for any scientific meaning

**[2:54:06 – 2:54:20]** Already in 1943 Warren McCulloch and Walter pits wrote a paper which was called logical calculus of nervous activity. So it was actually they were approaching it from from the perspective of mathematical logic.

**[2:54:21 – 2:54:35]** but they had to have the they wanted to have a mathematical model of the human brain and in particular mathematical model of a single neuron and it was basically already this

**[2:54:36 – 2:54:42]** So even in 1943, we started off with this model of the neuron and bear still with it.

**[2:54:43 – 2:54:59]** So yes, there are parts of modern neural networks that are that cannot be directly explained by this neurons. So, there are like attention mechanisms. We get Transformers, We will see some functions that have weights, but that are not quite like this.

**[2:55:00 – 2:55:04]** But mostly most neural networks are still.

**[2:55:04 – 2:55:05]** Composed.

**[2:55:06 – 2:55:09]** From your instance like this and even Transformers have a lot of neurons like this.

**[2:55:10 – 2:55:12]** So, this is still the basic building block.

**[2:55:13 – 2:55:38]** It was first implemented in practice by Frank rosenblatt in 1958. I think I have pictures. Yep. Very romantic time. And to be in computer science, that's what the computer looked like back in the days in 1950s and this. So this is Frank Ross and what, like learning training perceptron.

**[2:55:39 – 2:55:48]** Right. And but it did work. So it was I think it was the first actual honest machine learning model implemented in practice.

**[2:55:49 – 2:55:55]** And it actually did some pretty amazing things eventually, so it learned to recognize letters.

**[2:55:59 – 2:56:02]** And of course, it's not real computer vision. They were not.

**[2:56:03 – 2:56:40]** And they were letters in a specific font photographed from a specific point. And of course this was much simpler problem that then real OCR, of course, but still it was extremely amazing for the time and when this perceptron appeared, well, I always show this New York Times quote, maybe maybe it's, let's not well on it right now. But basically, at that point, everybody decided that well, the hard part is done.

**[2:56:41 – 2:56:56]** So I recommend you read it, the hard part is done and we know how to make computers learn and now it's only a couple of years before they can walk talk see right, reproduced himself and be conscious of their existence.

**[2:56:57 – 2:57:12]** So, as we know, it took little bit more than that. This early optimism was not really warranted, but, but still is the same principles, right? We still inherit a lot from this early. Neural network ideas,

**[2:57:14 – 2:57:15]** Okay.

**[2:57:17 – 2:57:26]** How do I want here? Yeah, and then as I told you yesterday, the AI winter happened so then people

**[2:57:27 – 2:57:28]** somehow got

**[2:57:30 – 2:57:44]** convinced that machine learning doesn't really work. And in particular, by the way, they got convinced that neural networks don't work.

**[2:57:45 – 2:58:01]** And there were some practical reasons which are true, but there was also a very strange theoretical reason for that somehow convinced a lot of people that neural networks are worthless and the theoretical reason is this? What? Whatever.

**[2:58:04 – 2:58:06]** Whatever activation function you have.

**[2:58:07 – 2:58:13]** If you have and this is an important point. So let me make it whatever activation function you have.

**[2:58:14 – 2:58:16]** Whatever, whatever is the age?

**[2:58:17 – 2:58:23]** Still, the inputs go to H through a linear combination, right?

**[2:58:24 – 2:58:32]** so, if you think about it as like a model doing classification, then

**[2:58:32 – 2:58:34]** You are still.

**[2:58:35 – 2:58:39]** Drawing a linear separating surface between the clauses.

**[2:58:40 – 2:58:42]** so, there is

**[2:58:43 – 2:58:59]** So if if you have wage of W Times X and you have some decision roll afterwards, like if it's more than 0 then plus one if it's less than 0 and plus two, then the surface will be this.

**[2:59:00 – 2:59:00]** Right.

**[2:59:01 – 2:59:07]** This is the decision. Surface on one hand, on one. On one side, you have C1 and there is a C2.

**[2:59:08 – 2:59:14]** Which is the same thing as saying. Well, let me just see where H reaches 0 and now it's a linear surface.

**[2:59:15 – 2:59:31]** Right? So the non-linearity does not give you nonlinear separating surfaces, nonlinearity just gives you the ability to build networks but by itself it it's still lifts the class linear, of course.

**[2:59:32 – 2:59:33]** and for some reason,

**[2:59:34 – 2:59:55]** People look at this and say well okay so it means that one person cannot separate a lot. Cannot solve a lot of problems. There are many problems which are, which do not have linear separating surface like the solar function. If you have the orange class over here and you have the blue cross over here and over here, then, of course, there is no.

**[2:59:56 – 2:59:59]** Straight line. That separates them? Well, sure.

**[3:00:00 – 3:00:04]** This, these are linearly inseparable classes.

**[3:00:04 – 3:00:14]** But for some reason, people thought this that this was like an argument against perceptrons and against neural networks.

**[3:00:14 – 3:00:19]** Which was kind of strange, I'm still not sure how there is an actually worked.

**[3:00:19 – 3:00:28]** But of course, the correct answer is sure you cannot do or you cannot do not linearly and separable.

**[3:00:31 – 3:00:38]** Task with a single perceptron but you can do it with a network of perception problems, right? And

**[3:00:39 – 3:00:43]** the idea of a neural network, the idea of taking this kind of

**[3:00:46 – 3:00:55]** Neurons and putting them together in layers and Computing. The final result of a composition of several such neurons.

**[3:00:56 – 3:01:16]** It's also very old and that actually goes back to the same element during he was a smart guy. And he already in 1948 before the Turing test, he already had the paper which I don't recommend it, it's very hard to read today, but he already had the paper where he suggested actually deep neural networks.

**[3:01:17 – 3:01:22]** Like real deep neural networks, compositions of layers of neurons.

**[3:01:23 – 3:01:24]** and,

**[3:01:26 – 3:01:29]** They the question was, how do we train it?

**[3:01:31 – 3:01:39]** The answer was pretty straightforward. I think we'll discuss it in detail tomorrow. According along with all of the gradient descent variations that we have today.

**[3:01:40 – 3:01:45]** But the answer is, of course, well you learn by gradient descent.

**[3:01:45 – 3:02:02]** And to do gradient descent. The only thing you need to be able to do is to take the gradients, take the derivatives and how to take the derivatives through the computational graph? Well, I bet propagation, I think you've heard about it probably should already know it. Maybe it will.

**[3:02:02 – 3:02:04]** Cut through it quickly tomorrow.

**[3:02:05 – 3:02:12]** So it's it's not a very deep idea. Back propagation is just a general for computing probabilities.

**[3:02:12 – 3:02:22]** and therefore, it's hard to say who discovered it because it was kind of discovered and dependently, a lot of times, but by this 1970s,

**[3:02:23 – 3:02:38]** It was already kind of well known and understood that you can use back propagation to to go through through the layers and to update the weights of a composition of simple functions.

**[3:02:39 – 3:02:49]** Um, and already in the late 1970s in the first half of the 1980s you already had.

**[3:02:51 – 3:02:55]** The idea of deep neural networks and they already started to appear.

**[3:02:56 – 3:03:11]** And by the second half of the 1980s, you already had convolutional networks. You already had recurrent networks. You didn't have Transformers yet that had wait, but you already had a lot of architectural ideas that

**[3:03:12 – 3:03:20]** Would actually be the iteration is still relevant and that if you could just scale them up, they would work quite amazing. You will actually

**[3:03:21 – 3:03:23]** so, if you take a network,

**[3:03:24 – 3:03:26]** say convolutional network is and then

**[3:03:26 – 3:03:42]** From the early 1990s from late 1980s and you just mechanical scale it up and you train it on Modern Hardware, on Modern data sets. It's gonna work pretty well. So of course, it will be burst and the networks we have today, of course, but if people had this kind of

**[3:03:44 – 3:03:55]** Results back on the nine, back in 1992, they would never be discouraged from neural networks. That would definitely be state of their back on the time.

**[3:03:56 – 3:03:59]** but unfortunately, neural networks require

**[3:04:00 – 3:04:16]** A certain scale to work so to speak, right? So if you have a very small neural network and the small data set, then probably the result will be worse. Then if you actually just think about the problem and do some more specialized model,

**[3:04:18 – 3:04:19]** For this problem.

**[3:04:20 – 3:04:22]** So, by the early 1990s,

**[3:04:24 – 3:04:24]** Since.

**[3:04:25 – 3:04:39]** People did not have the ability to scale up. They did not have the compute. They did not have the data. Basically the consensus, in the research Community was like this. Neural networks are the second best way of doing just about anything.

**[3:04:40 – 3:04:55]** So the place of neural networks was that there are very Universal you can do anything within your own network indeed, but it will be worse. Then if you just think about the specific problem, you have and create a model for this specific problem,

**[3:04:56 – 3:05:13]** So in the 1990s and there's the thousands neural networks were kind of Forgotten again. It was the Heyday of probabilistic models of graphical, probabilistic models, etc, etc. Very interesting still relevant very important, but out of scope for us.

**[3:05:14 – 3:05:37]** Ah and there were just a few groups who pushed and pushed on neural networks. There was an electron who was doing the image processing with cnns. There were Jeffrey hinton's group and Joshua benches group and they continued working. They continued believing in the neural networks and finally they were proved to be right.

**[3:05:37 – 3:05:44]** Okay, so the Deep learning Revolution happened in the middle of 2000 and 2006.

**[3:05:45 – 3:05:58]** 1,007 and I won't discuss in detail. What exactly was like there in Innovation because it's irrelevant by now it's it's it's absolute. But

**[3:06:00 – 3:06:01]** The specific.

**[3:06:02 – 3:06:23]** The technical Innovation. Wishes are still, of course, relevant was that they moved from CPUs to gpus. So again it's not much of an idea to notice that the stuff we're doing in your own network is easy to parallelize. Of course, it's easy to parallel. It's a huge number of neurons and not very deep computation, just like in the brain.

**[3:06:24 – 3:06:39]** But only in our Century only in the early 2000s. There was actually Hardwear widely available on the market gaming gpus that will actually implement this parallel process.

**[3:06:40 – 3:06:47]** So before that CPUs were still the best, we had, right? And as soon as gpus became good enough,

**[3:06:47 – 3:07:00]** People specifically the guys at hinton's group moved computations, to gpus that gave a boost of about another 10x 20x inefficiency.

**[3:07:01 – 3:07:20]** And that was enough that was enough to put neural networks from not working to work and starting from the late 2000s. Neural networks have been kind of revolutionizing one field of machine learning after not. Actually the first field was speech recognition.

**[3:07:21 – 3:07:39]** Speech processing. Deep, neural networks, had some very good surface and very good feature, extractors in the late in about 1010. So basically it was this original Deep neural networks patient and Benji that made Siri possible.

**[3:07:40 – 3:07:50]** Syria appeared in what found 11, I think the first version and it was, of course, would be impossible on classical speech, recognition, wouldn't work well enough to be useful

**[3:07:52 – 3:08:10]** Ah, and then, so we will not talk about speech recognition in this class, but we will talk definitely about image processing and the image recognition and computerization. So there the revolution happened around, 2011 to 2012 with alexnet, we will discuss how it's not in detail when we come to.

**[3:08:11 – 3:08:12]** and,

**[3:08:13 – 3:08:18]** let those and then everywhere, then with recurrent Networks,

**[3:08:19 – 3:08:21]** deep learning got into.

**[3:08:23 – 3:08:27]** Got into natural language processing.

**[3:08:28 – 3:08:50]** So by 2014-15, people were doing machine translation with neural networks and stuff like that. There's neural networks, and then in 2017, everything changed again, 2017, we had the Transformer and that transformed literally the whole industry. Again, we are still living in the age of Transformers, so to speak.

**[3:08:51 – 3:09:00]** So, I think I don't have time to go to bed props right now. This was a quick historical overview and

**[3:09:02 – 3:09:06]** It will will do the optimization part tomorrow. Any questions.

**[3:09:08 – 3:09:08]** Yep.

**[3:09:14 – 3:09:23]** So neural network but just I think I just didn't it. Sure was going on there. Yeah, sure.

**[3:09:24 – 3:09:27]** Yeah, sure, no problem. So

**[3:09:29 – 3:09:32]** suppose that I'm doing a neural network that is supposed to do classification.

**[3:09:33 – 3:09:40]** So at the output I want to have a lot of function like this and I want to have like a vector of probabilities for classes.

**[3:09:42 – 3:09:43]** Where do I get a vector of probabilities?

**[3:09:44 – 3:09:44]** Well.

**[3:09:45 – 3:10:00]** If I just do some neural layers, some Elementary functions and big compositions, I will not get a vector of need numbers from 0 to 1 that sum up to one, right? What I will get is a vector of scores

**[3:10:01 – 3:10:04]** That then will need to be converted to probabilities.

**[3:10:05 – 3:10:07]** By the softmax function, that's part one.

**[3:10:08 – 3:10:28]** But also, I mean, for some networks this will be the actual output and this may not happen. But usually, of course, it's still happens. So usually after like the main part of the neural network, what what it does is it extracts? Some kind of features from the input.

**[3:10:29 – 3:10:36]** and this features are a vector or a higher dimensional tensor doesn't matter at this point but it's it's

**[3:10:37 – 3:10:39]** A set of numbers. Let's say of safety.

**[3:10:40 – 3:10:40]** Right.

**[3:10:42 – 3:10:47]** And we want to convert it to a set of numbers of size case.

**[3:10:47 – 3:11:01]** That that's the only point that I was making here. So how can you do it? Well, for example, with just a linear transformation. So very often when neural networks look classification, very often like the last layer is actually just logistic regression.

**[3:11:03 – 3:11:04]** this is,

**[3:11:05 – 3:11:08]** Literally straightforward villages to regression.

**[3:11:09 – 3:11:16]** But not on the input, but on the features extracted by all the rest of the network and that's that's the very important difference.

**[3:11:30 – 3:11:39]** And probably I mean, linear regression. It's kind of uncommon to have many outputs so probably would be equal to one but not necessarily have several

**[3:11:41 – 3:11:43]** Just, you know, they were explained that before.

**[3:11:45 – 3:11:50]** And also want to say thank you for the lecturer. It was very interesting. Okay. It was very

**[3:11:52 – 3:11:52]** honestly, the prior

**[3:11:53 – 3:12:04]** like biasing Theory. Imagine that regularization is bios because I read a lot of information, I Was preparing for interview and I

**[3:12:05 – 3:12:08]** Literally couldn't find. I haven't seen that before.

**[3:12:09 – 3:12:12]** Well, if yeah, if

**[3:12:14 – 3:12:36]** If you looked for it, you should be able to find it because, of course, it's, it's like an in the foundation of the machine learning, but I'm really happy that you find it. Interesting. I'm always a little bit worried about this introductory part because, you know, some people just want to get to programming pytorch. But I think that foundations are important and I'm really happy that if you feel that way,

**[3:12:39 – 3:12:42]** Thank you. Thank you. All right. Thanks a lot guys.

**[3:12:52 – 3:12:52]** In general.

**[3:12:55 – 3:12:56]** You can.

**[3:12:58 – 3:13:04]** okay, previously, since this is you would use like measures like r-squared adjusted or

**[3:13:07 – 3:13:14]** like criterias, I don't remember like a formation criteria and some other measures that pioneers.

**[3:13:14 – 3:13:18]** Adding extra variables to the model.

**[3:13:21 – 3:13:25]** Yes, this was rich Russian and also doing this.

**[3:13:26 – 3:13:37]** Not quite so yeah, that there is a difference here. That is a little bit that made the little bit made them clear by my example,

**[3:13:38 – 3:13:48]** And I apologize for that, but it's still very instructive for example, so I still give it. But yes, that's a great question and there is an important difference. So when we talk of regularization

**[3:13:49 – 3:13:52]** We kind of have already fixed the model.

**[3:13:54 – 3:14:07]** So in the case of linear regression, I can have L2 regularizer. I can have one regularizer, I can have any kind of Prior over here, but the likelihood is already fixed.

**[3:14:08 – 3:14:14]** And what it means that the likelihood is fixed in particular. It means that the size of this Vector is also fixed.

**[3:14:16 – 3:14:23]** So when I change regularizers, I don't change the model structure, I don't change the number of parameters,

**[3:14:25 – 3:14:32]** it might look like that in my example, because as I went from between degrees of the polynomials, I was changing number of parameters.

**[3:14:33 – 3:14:41]** You're right. It was a little bit confusing in this regard, but regularization usually does not do that. Regularization deals with the values of this parameters.

**[3:14:42 – 3:15:02]** And the stuff that you mentioned and this are great keywords that are so talk about and in classes when I have time. But not in this class, we go to Japan. But things like okay, you can information Criterion. They buy Asian information criteria and stuff like that. They pertain to what is called Model selection.

**[3:15:04 – 3:15:20]** Right. And model selection basically, means I can model my data set and several different ways I can have linear regression, have code rates, regression cubic regression, local, gaussian regression, whatever,

**[3:15:22 – 3:15:26]** Ah, and then I need to choose between them. How do I choose between them? Well,

**[3:15:27 – 3:15:30]** What is what is this Choice? Like what am I trying to estimate?

**[3:15:31 – 3:15:42]** Its deceptively simple. I want to estimate. What is the likelihood? What is the probability of having model? Number k for my data set.

**[3:15:44 – 3:15:44]** and,

**[3:15:46 – 3:15:50]** How, where do I get this probability from?

**[3:15:51 – 3:15:52]** Well, of course, I get it from the best role.

**[3:15:53 – 3:15:58]** So of course, I get it from from something like this poem K times P of D given MK.

**[3:16:00 – 3:16:10]** Here. And notice that here. M is not a specific set of Weights. Here I am, is the whole model. So like one M could be like linear regression.

**[3:16:11 – 3:16:14]** And another M could be like, quadratic regression.

**[3:16:14 – 3:16:18]** So, it's a whole, the whole model, not specific weight.

**[3:16:20 – 3:16:32]** But still the best role is the same and it's still tells you well. Okay. If I don't have any reasons to prefer one model to another, then let's assume this is uniform and I just compare of given them, okay?

**[3:16:33 – 3:16:37]** Where is that P of T? Given MK and our formulas. Well,

**[3:16:38 – 3:16:42]** Let's go back to our Bistro.

**[3:16:43 – 3:16:45]** View of theta.

**[3:16:46 – 3:16:54]** Put more space here because I need P of theta. P of D. Given. Say sorry.

**[3:16:56 – 3:17:00]** P of D given Theta divided by P of d.

**[3:17:01 – 3:17:28]** And here P often these formula. As I wrote it we didn't have you know the contacts and the chance to go. This one metal level up but you can go one metal level up. They the formulas I wrote it was about one model like we are talking about linear regression and we are dealing with the parameters that obey this baby shower and you do in France from the parameters. So like everything happens in a model.

**[3:17:30 – 3:17:32]** Sorry, not the bar.

**[3:17:34 – 3:17:34]** Right.

**[3:17:35 – 3:17:42]** You can you can add the model. Here doesn't change the formula. It's still works.

**[3:17:43 – 3:17:44]** so,

**[3:17:45 – 3:17:55]** What do you compare the models by? How do you choose between quadratic and cubic features or between different versions of the model Etc? Well

**[3:17:56 – 3:17:57]** By this guy over here.

**[3:17:59 – 3:18:03]** The denominator. So this this is exactly this quantity.

**[3:18:04 – 3:18:05]** They denominator in the base rule.

**[3:18:06 – 3:18:08]** The normalizing constant.

**[3:18:09 – 3:18:16]** And everything that this information criteria do they are basically approximations to compute this.

**[3:18:17 – 3:18:25]** And then there is a lot of methods. It's very beautiful and interesting, approximation loads to say about it, but basically, it's an approximation to compute this

**[3:18:26 – 3:18:35]** So model selection is about trying to estimate this, normalizing constant, and choose the model with the largest normalizing constant.

**[3:18:36 – 3:18:42]** but in the model, then we will have a whole distribution of parameters and

**[3:18:43 – 3:18:52]** So there are two levels there is the level of selecting the model, and then inside the model, there is the level of actually learning the parameters.

**[3:18:56 – 3:18:57]** The answer question.

**[3:18:59 – 3:19:00]** Yeah, thank you.

**[3:19:01 – 3:19:03]** Okay, thanks guys.

**[3:19:04 – 3:19:08]** And see you tomorrow. Finally, for some actual neural networks. Bye.

## Full text

Good morning everyone. Welcome to the second day of our class and I suppose, I hope the first day was interesting today, we will definitely started deep learning although I do have A few things to tell you before that but then at least in the second half of the start talking about neural networks, no way around that. so, to get the technical organizational stuff out of the way. I sent a message to Google Classroom. I hope you've seen it. I made a webpage secret webpage with which probably we are now suppose to link to externally, but and that's just for you. I made a web page with all class materials K-pop loading videos, flights board. So, I hope you like it. and with that, let's continue. Yesterday, we talked about the general idea of what learning is of how we can formalize and understand what it means. For say, machine learning model to actually learn something and we framed it in In the probabilistic by Asian framework and basically it was like most of yesterday's discussion or Central round the base roll. Around this. Famous formula which is the most important formula in the entire machine learning. But yesterday. we talked about, A very simple example, we were just talking about the coin toss and I actually want this introduction to go to the linear models because they are very directly relevant to what we do in deep learning and what neural networks actually do. So Let me. Apologies, but let me continue with this probabilistic introduction still, I hope it's important. Well, I'm sure it's important, but I hope it's interesting for you. So we discussed the bistro yesterday and just as a quick reminder, the main idea of this formula is that Is to answer the question of how should we update our beliefs when we learn new information and we get new evidence, right? So in a more General more general terms D would be not specifically dataset for machine learning, but it would be just any kind of evidence and fate would be like our beliefs, our hypotheses about the underlying process or whatever. And then when we get new evidence, we update what we What we believe, right? And that's in a way, how life works, right? That's, that's how our brains are supposed to work. No, not always. They work. Exactly in this way. And of course, we don't consciously do any calculations like this, but the general lessons is exactly this. And we discussed three. Main problems of machine learning where the optimization tasks come from. So, you can start with the likelihood and end right there and just maximize the likelihood that doesn't make any use of Asian inference. So, it's non-bias and Method. But still if you have lots of data or if your model is already very complicated and a prior distribution would make it completely unfeasible though? I can't imagine why still? You can just maximize the like, then you can multiply the likelihood by the posterior will see by the prayer. Will see, very specific examples of that today. In real world, real life models. Not just point us And then maximize the result, which will be proportional to the posterior distribution, right? That's that's what we discussed last time and we discussed the coin torsion example in great detail. And maybe. Yeah, in the third problem would be the predictive distribution, which I don't think we'll get to today. So let that stay at the level of the coin toast. And we discussed the going to as an example in great detail yesterday. So we kind of went through the all of this problems went through the notion of likelihood prior posterior with it. All means completely finished the simplest case of a uniform prior and then discussed what the more informative more reasonable prior would be like, if I do want to have a bell shaped curve and how do I choose among them? And the answer was the one that's convenient, which has, which may sound like an unsatisfactory answer. But there you go. It's it's about, it's our choice. It's about our beliefs. So actually in More involved cases like linear regression. That we will discuss. Now, the reasoning is exactly the same. You chose the prior not due to some principled trees, and like, you understand it, for these process, the prior should be this, but you choose your prior. Either for convenience or because it leads to desirable properties. We will we will see how it works. and, The. Another thing that I wanted to mention here, I will I will not spend much time on like real world examples or anything, but I do want to mention some kind of, you know, philosophical underpinning of all this, right? And I mentioned yesterday, that if you open an old book and probability Theory, a very good book, but an old book and probably Theory, you will see probability introduced, like, well, there is this infinitely repeatable experiment, we do the experiment, we get some results, and then we divide the results, the number of outcomes that we are interested in by the number of total experiments and that ratio tends to the probability that is completely correct when applicable it's completely correct. And for the coin toss, it's exactly how we Define probability. but, In real life and the special in machine learning. That's why I'm talking about this. We usually want to reason about the probability of events that are definitely not repeatable experiments, right? So, for example, if your bookmaker, you need to predict the probability of, to set the probability of Spain winning the FIFA World Cup this year. And there will be only one World Cup and no it's not the repeatable experiment based on previous World Cups because obviously the teams were completely different. Everything was completely different or we even might want to set probabilities for events. That already happened that all are already said but we just don't know the answer. and, In this kind of cases. It makes no sense to talk about experiments repeated to Infinity, right? For example, there is a hypothesis and not sure about the current status, but last time I checked, it was a hypothesis that the Odyssey by Homer was not created by the same Homer as they had, but was written by a woman for you to some electric analysis of the text. And it's a hypothesis, we don't know. But It makes sense for us to want to assign probabilities to hypothesis like this, right? Although there is only one, what is and it was written by somebody thousands of years ago and the answer is already set but we just don't know it. so, The point is in real life probabilities are often not limits of ratios of experiments, but they are degrees of belief. They are representations of our uncertainty and this is actually a very useful, I think framing to think about probability and the Very useful way to understand what what we are doing. We are not actually, well, when you do machine learning, for example, when we use this, with the real data set and a real model we are not Getting some kind of. Logical conclusion, right? We are updating our beliefs. And if we have a good data, set, a large enough data set, then our beliefs can become much more. Certain we can become, I don't know the confidence. Intervals May shrink, we can become more sure in the hypothesis that we are evaluating But we will never be completely sure right? Especially in machine learning, when it's all about noisy data sets are the thing is? We are Combined, we are combining all of the evidence to understand something about the model model parameters. In this case, But there is always a probability distribution. And this is a point that often gets lost for people because what you actually do in reality, and Let Me Maybe immediately so that, you understand in advance where we are driving with this. Let Me Maybe immediately get you the general notion of what we are doing today. So, We are. Using this identity and we are reasoning by the best role but what we are actually doing, for example, in deep learning practice all the time is we compose a loss function, right? So we compose a loss function. Like log P of D given theta plus log P of theta and actually take minus because the loss function you want to minimize not maximize but in practice this is the loss function for your neural network, right? We will see how it works specifically today. And then you minimize it with respect to Theta, with respect to the neural network parameters and you get the map, right? So Theta map is the arc mean of these. The maximum upper stereotypical hypothesis, right? So it's the arc Max of P of fate and giving the and very often people when they think about deep learning about neural networks, they kind of Stop here and the process desktop here and then they say, oh now we know Theta. Now, we got, we got our model checkpoint. Here are the weights here are the true weights. That is. An oversimplification, right? So yes, in practice very often, we will do exactly this. And we will use Theta as a point estimate, but it's very helpful to Remember that Fatima is just a point estimate, right? It's just the maximum of a whole distribution. And in deep learning with huge neural networks Etc, we usually cannot do that. But if we could, it would be very helpful. Usually to actually at least sample, several different points from this distribution and see how that translates into different predictions. Actually, sometimes you see this in deep learning because as well, right? So, All of this Machinery is about degrees of belief. It's about our uncertainty. Our original uncertainty captured in P of theta and then reduced by D by the data that we get. And ultimately, our new uncertainty capture it in P of theta given d, right? So, we know something about the parameter, set cannot be that we know, absolutely nothing. Well, sometimes it can, but still be. We need to express it in the distribution then. We get new information we update and we have some new belief about data, but it's it's a distribution, it's an uncertain belief. It's never a just a single point. This this is what I wanted to say here. and, yeah, and also I usually go through some Relatively straightforward examples of applying the Bass Pro. Let's maybe let's try it with you. So here is a very standard, like trick question from probability Theory. I personally have two kids. Let's say my acquaintance has two kids, but I've never met them. I don't know, their names, I don't know, their generals. And let's assume that. Every baby is either a boy or a girl with probabilities one-half and the first baby is independent from the second so they're just there. Each of them is a Fair coin to us in terms of whether it's a boy and or a girl. And then I go to this person and ask. Hey, do you have any voice like, among the two children that you have? Are there any boys? And he says, yes, in this setting, what is the probability that he has a girl? How many? How did you arrive in this? You know. Any other ideas? So what what's the probability of space here? Like what are the possible outcomes? Mmm, also not quite true. Okay, yeah, this, this is a straightforward precaution, but yeah, it would usually fall into the trick unless, you know it. So the, the person has two children, right? So it's like, child number one and child number two, right? For every child, there are two possibilities two options, right? So, how many options are in total? For exactly. So we have like a boy boy boy girl girl boy and girl girl. Right? So there are four possibilities and In the prior before I get any information there, completely, right? So we get one fourth for this one force. For this one, fourth, for this one for this, right? So now when I asked, do you have any boys and he answers? Yes. What information do I get? How does this table change? Yeah, precisely. So now the last line cannot happen. But the restore can happen, and the answer is not distinguish between, right? So as a result, I now have three options, they are still equal and probability but now I have three options and no two of them. Have a girl, right? So, the probability is actually the thirds. And if you want formerly, then you just need to compute P of, you know, there is a girl. Give them that. Give them the there is a boy, right? So it's like the probability of these two scenarios and if or FM divided by the total probability of that there is a boy of m m f or FM and that comes to the thirds, right? So formerly it's like Two quarters divided by 3/4. If you go straight to my definition, all right. But here is the second question now, I've met one of his kids, so it's separate question. I didn't ask the first one so I don't know that. and, Now, I've met one of his kids and it's a boy. So now I know that one of the kids is about and I've met this, this boy, what is the probability that the other one is a girl. Yeah. And now it's one half, right? So now if when I meet Some one of his children then it means that. Now, it doesn't matter if it's number one or number two, but it means that I kind of fix the value of one of these columns. So now, I eliminate not one, but two lines, for example. Number one is a boy, which means that now only two outcomes remain, and they are equal, etc. Etc. so, It, this is an easy trick question but it's already shows how in probability Theory and bias. And recently like this, notice that, although we didn't really use the BIOS, theorem it's actually the same kind of reasoning. We get some prior beliefs that everything is equally probable. That's our original assumptions. And then we get evidence, and then we update our beliefs based on this evidence, right? And but there are also a couple of more interesting examples. Let's discuss them with you to since the first one I think went well this are again very well known for this fallacy may have heard about them but they are very instructive in like the pitfalls but potential pitfalls of the best role. So let's okay. Here is the Satan a murder has happened. And we are in the court of law are in about the murder. So there is some blood left on the crime scene and we know 100%. So don't think about that assumption. We know for certain this is the Killer's plot. Okay. So this is probably one you don't need to question that. And it's so happens that the blood type is quite rare. Like, let's let's assume it was a time before DNA tests. So we cannot like directly check which person it is but it's a rare blood type. And only 1% of the population, only 1% of people actually have that blood type. And it just so happens. That the defendant the guy who is being accused of the murder. So has this what type? Right. so, the prosecutor comes out and says, well, The chance that the defendant would have this blood type of, he was innocent is only one percent. So, with probability 199%, he is guilty. Is the prosecutor correct? This. I suppose the question on the slide tells you that he is not, but what's the mistake? What's the problem with this kind of reason? I think it's the specific way. How the like The statement has been proposed here, maybe. like, Is equating the probability of like having the blood type like given innocence versus probability of actually being in Northern given the blood type something that. Exactly. Yeah. You nailed it. Exactly. So this is this is a classic mistake that happens all the time in real life you see people to make it all the time and because our brains are not really wired by Evolution to do probabilistic reasoning, especially with numbers. And yes, you your answer was completely entirely correct with repeated for everyone. So we have So what are we actually trying to do in the court of law? Yeah. Trying to establish like P of guilty. Given the evidence. All right. And if it's very, very high, then we can be convicted, right? It's probably never going to be exactly one, but if it's very high, then we can make the person Are. And so the prosecutor makes a conclusion. Exactly about this. So here's a final point, the 99% is about P of guilty. Given the blood type. Right. But what he starts with is not P of you of innocent. Given the blood type, it's the other way around. It's p of blood type. Given that the person is. Right. And yeah, so when the prosecutor Estimates this probability is completely, correct, right. So like one, it doesn't matter, like almost everyone is so we can say that this is also 1%. That's fine. but then, The prosecutor says. Well, all right. So this equals to one minus this. And now this conclusion is completely wrong, of course, right? So the prosecutor equates like P of a given B. with P of B given a in a way. And that is, of course, not right. When I write it like this, it's obvious that it's wrong, but when it's stated in the words, Yeah, people you missed missed this kind of mistakes all the time. And what would be the actual formula? Of course, it would be the best rule, right? So in actuality, like, P of blood, okay? Let's do it. The other way, around P of incentive given blood. Would be like P of blood given innocent times P of innocent divided by P of what. Right. And Of course, these priors this prior and this evidence probability could completely changed things, so I'm not going to try to invent any numbers. It doesn't make sense for this example, but for example, suppose that there are two possible suspects and it just so happens that both of them have right. If that happens then of course the blood types tells us nothing right? It does not help us distinguish between them and the probability remains to be one half but the prosecutors A reasoning would be. Would not change in this case. So, the prosecutor would now make like the obviously absurd conclusion. That both of the suspects are guilty, each with probability, 99% issues, of course, from Okay, so this is the prosecutor's mistake. And then the defense attorney comes out and comes on the. What's the word understand? Yeah. And the defense attorney says well. Okay, so first, he explains what the mistake of the prosecutor was and then he says, well, okay, let me offer my own calculation. There are a million people living in the city. and yeah, of course, having this rare blood type Narrows and down from a million to only about 10,000, Right. And that is correct. So all the blood type tells us is that the defendant is guilty with probability like 0.01%. So, yes, sure, it's kind of evidence but it's very, very weak and it's definitely not any kind of proof. Let's just not admitted to evidence at all. It's also doesn't sound right, right. So what's, what's the defense attorney's mistake? I mean is mistake is like probably stating that everybody who has the blood type is equally likely to be the killers. So so, basically not even focusing on why the defendants there in the first place. Yeah, exactly. So in this case it's not really some deep mistake and probabilistic reasoning, it's just the mistake and the Assumption, right? So yeah, it would be true but he says if Everyone of these 10,000 people including I don't know people who are sleeping at the time and babies and everybody in the city. Would actually have an equal chance of committing this murder, but that's obviously not true in real life. So they defendant is there for some reason right? Yes. So yes you're completely right? And yeah, and these kinds of mistakes. Happen all the time. And there there was a very famous case which you might have heard about the case of OJ Simpson, he was a very successful football player, American football player in the 1980s. And then he had well here he had some very difficult relationships so to speak with his wife, And ultimately, the wife was found to be killed. And OJ Simpson was straight from her. It was like one of the most publicized Trials of the 1990s. And it was a long trial. There were lots of, there was lots of evidence, lots of discussions, will not go into that, but there was one specific point that exactly matches our discussion on the BIOS. And at some point, the attorney of ocean. Sorry, the evidence was that OJ Simpson. Already had a history of violence with his wife. Basically, he bit her up a few times before. and, The prosecutors, they proved this. This was true and they kind of submitted it to the jury as not reproof, of course, but there's evidence that OJ Simpson can actually go to far in another episode and the wife can get killed Ah, so the attorney came up came out and said well, okay, my defense. My client is a very bad person. I do not dispute that. It's, it's it's, it's very bad to be happy for your wife and definitely, he shouldn't be doing that. But we are at a murder trial. And as for the murders there is a statistic that says well only one of 2500 women subject to domestic violence actually get killed. And he concluded that this is Irrelevant for the murder. Right. So And what, what I mean, it's of course, it's the defense attorney's job to make arguments like this even if they're copiously wrong. But what what's the, what's what's really interesting about this is that the court actually agreed So the court in this very famous, very public, OJ Simpson's case agreed that this is a good reason to say that the Mystic violence has no relevance to the murder and, you know, like they do it. The jury was instructed to District guard, the seventh blah. Um, but of course, this is exactly the same kind of mistake, right? So, in reality what, They were supposed to be evaluating was P. Okay, so let me start with the statistic, the statistic was What is the probability of murdered given a history of violence? And okay, the statistic was correct. So that was like one hour 2500 that's that's true. but that's completely not what was being what we what people are trying to establish, right? So this kind of statistic starts from The. Point in time when nobody is murdered, right? It's starts from from the point where everybody is alive and well, and then evaluates How likely it is to be murdered. But The court case, I remember case. Argus in the opposite direction, right? So what we actually want to know is what is the probability of being murdered by your husband? Sorry about this Glory topic. But you know, this is still the most famous case of this of this policy given that the murder was has already happened and there was a history of domestic violence. Right. So, of course, the, the main thing is that the murder has already happened. And we are just trying to establish who did it. so the vast majority of this case of this 25,000 cases in the vast, majority of them, nobody got murdered so they don't matter, right? They don't, they're not included into this conditional probability. And if you actually take the exact same statistics, here is the punchline. If you actually take the exact same statistics, that was available at the time and you compute the correct probability from it, is you estimate the correct probability? It will come. I may be slightly mistaken but it will come to something like seven or eight. So like among the women who were the history of the Mystic violence in the vast majority of cases, The husband did it. and, Uh, so of course, if evidence was presented in the correct way it would look completely different, right? so, This is just an illustration that people do make mistakes like this, and it's probably just a good habit in life to actually understand what exactly you're trying to estimate. What is I mean in life? All that we do everything that we do to make decisions is estimate various conditional. Probabilities if I do this, what is the probability of my preferred outcome? And if I do that, what is the risk of this and that and it's It's it's it's a good habit to actually explicitly understand. What exactly is the probability that you're evaluating even? If you cannot really value it, right? So in real life, we don't have this kind of Statistics. We can run the numbers, of course. But if you at least qualitatively understand what is the direction that you're trying to predict, what is on the left of the vertical bar, and what is on the right of the vertical bar? Thanks become more clear and in many cases, Okay, so that was the leftover that I wanted to mention. and now, We proceed to our first real example and now this I will make two examples today linear regression and logistic regression. We will not discuss them and too many details but I do want to discuss them because they are directly relevant to what's happening in neural networks. That's like the simplest possible. Neural network is a linear model like this neural network consisting of one perceptron and it's not only that, you know, it's the simplest model and modern neural networks are completely different. No linear regression. Logistic regression is still directly relevant. What's happening in them. I will explain why. so, I hope that you all have some kind of intuition about what linear regression is, maybe you don't, maybe you can remember the formulas. That's fine. Maybe you don't, I don't know maybe you never studied it like systematically, but This will be our Point number two, linear regression. But at least you have this, you know, General picture in your mind that a linear regression is a problem like this. You have X over here if you have the target variable y over here, there are some data points like this. and you make an assumption, you say the data points are probably In a linear dependence between X and Y. But we don't know the dependence and there is noise so they are not exactly on the same straight line. They are close to straightly Right? And they the problem of linear regression is to find the straight line. basically, this is the intuition that I hope you'll understand. So, if I write it down as a formula, I mean, obviously can only draw you two-dimensional pictures. So X will be one dimensional what I draw. But in reality, of course, we are usually talking about Single way. So the target variable is a number. Or less always. But this number is Not just w0 plus W1 times x but there are many axis, right? So in reality x is a vector. Usually and there are and we model y as a linear combination of excess. okay, so before I even begin, talking about it in detail, one, very simple, remark that will help us make things easier. I will actually skip the intercept. So I will actually write y as just W Times X and this, this means transposition and this means just scale or the product of the vector W. And that's so like that W1 WD times X1 XD. Why, why can't I escape the interest? Why can I forget about double zero? Like in practice, it's not 0 right here. It's not 0. Yeah, precise. Okay. It's good that you know, the stuff I to be able to skip the intercept. I just add one more Dimension. I had a fictional Dimension. Let's say x0 is just one like you said, it's a new feature, a constant feature. And then I take my Vector X and I map it to like one and then X like a vector, which is one dimension longer. and now, suddenly When I do a linear function when I do it direct product. In this Vector, I get the intercepts for free, right? So this is a standard trade, that's that's why we don't need to always add this double zero here which would make the formulas, much more. Oh, it won't make it more complicated but would make much more cumbersome. Okay. so, why should be similar to a linear function of excess? And maybe, you know, I mean again if you ever studied any linear regression, probably have an idea. How do we Define this being near to What what, what is what do we mean by this approximation? What are we actually? How do we formalize linear regression user? You minimize the. engineering measurements between the actual various and prediction of Yeah. And what is the most common error? Yeah, exactly. So the standard way to do linear regression and again, notice I haven't yet read on any probabilities will get, there is okay. So what does it mean that I want you to be such that? Why is approximated by W Times X? It means that my predictions. So, here are the excess, right? The access in the data set. and, My prediction in this access are points on the straight line, right? So this this is what my model creates. This is W Times X and over here and What does it mean that the straight line is closed? It means that these distances are small. right, it means that I want the total sum of these distances to be as small as possible makes sense. And usually, like you said, The loss function in linear regression is defined. So I said that I wanted this to be small, but I didn't hear Define what exactly what is the exact number that I want to be small. And usually it's exactly the square distance, right? So usually, it's the sum of Y, minus, double y and x minus W Times X and squared. And standard linear regression, minimizes this with respect to W, right? Well, here here is a question. Why? Where does this come from? If you know, you can speak up and tell. or if you have an idea, why So, obviously, I do want this distance to be as small as possible. That's that's right. Obviously, I do want, I don't, I cannot just add up distances as they are because they have science, right? So I don't, I don't want this to be symmetric. I don't I don't want like, the straight line to go just to positive Infinity because then everything will have like negative Infinity errors, right? So I do want it to be symmetric. So that's part of the job that the square is doing sure. But the same job could be done by million otherwise in a million other ways, right? I could have said, okay, why don't I add up the absolute value of this? There is why don't I add up for this value to how to degree 4? Why don't I adopt e to the power of the absolute value of this? And I mean there, I mean, there are infinitely. Many Monotone functions that are symmetric, symmetric and monotone in the distance. And if I actually start minimizing all of this thing's, I will get different results, right? The W will be different. So why do people choose squares often? Why is it the most common loss function? Things because of the Fulfillment of the government of theorem, maybe like the blue property. Exactly. Okay. So I I see that you already have the background for this so I'll make it quick. just like if everybody, if everybody has the same answer, we can just skip it if if you want to hear and I can explain. So okay, so the reason for this reason for the square actually comes from the probabilistic assumptions that we're making and let's frame linear regression. As a machine learning model in the sense that we are developing, right? So in this case Theta is the W, of course, so the model parameters are the weights, that's that's clear. Data. Are they excess and wise? That that's also pretty clear. But how do we Define the likelihood? So to define the model? We need to define the likelihood. The likelihood is p of D given Theta, right? The first thing that we do is we make the same assumption that we make. Always in machine learning, that keeps true throughout all of the machine learning models. We say that all of the data points are conditionally independent. Sorry, not X. Why are conditionally independent given the parameters, right? Sorry, And also, since we are doing supervised learning, we always have an X and the X, we are not modeling the expert on the modeling the way, right? So the X always goes on the right hand side here. So this is what you provide learning actually means. It means that we have an input that goes here. And then we are modeling the output that goes here. Okay, so The this part is straightforward. This, this is our first assumption, we always make it. But then comes the interesting part. So what is this distribution here? It's actually the distribution of the points that we see. Given our model and the X-ray, we measure. so, for example, At X3, we have our model predicting, this point. But what we need to Define is not just a single point. Right. So our second assumption will be linearity. Alright. Our second assumption will be that the most probable point the center of this distribution is in fact, W times x. But to actually do learning. We have to define a whole distribution around this point. Probably looks something like this, right? So it should decrease. I mean, I wanted it to be symmetrical. So let's assume it's magical and I wanted it to decrease to both sides. Right. So what it would mean it would mean that A larger distances from our model are largely distances from the straight line are less probable. So, if I want to find the most probable line, the maximum likelihood line, for example, then, of course, I want, this is just abysmal. So, I want this points to, I want the noise to be a small as possible. The total noise here, And the specific form of those function will follow from the choice of distribution. So yeah, I want it to be asymmetric. I wanted to be kind of bell-shaped, but as we discussed yesterday, there are lots of milkshake curves, right? So we want to pick a specific distribution here. And now comes around. It's this was all the setup for your answer. What is the most nature of distribution? That what is the default distribution that you use in a situation like this? Actually, it's the girls, it's normal distribution. And why? Because of the central limit theorem actually so, What does if you don't know if you haven't had probability theory, if you don't know, Central limit theorems, no matter, we won't really use it. I'm just explaining where it comes from so, What does the central limit theorem? Tell us the basic one, it says that whatever is the distribution. If you average it out sufficiently if you have a child, sufficiently more copies of this distribution or if you add them up, sufficiently many times. What you get is a gaussian you converge to a ghost. Right? So what this means in practice is that if you have a process, some kind of physical process or whatever where there are many small sources of noise. That all come together. And all add up. there is, although probably because Or close to ghosts. So if you don't know like in high school physics, if you're doing experiment like your rolling the ball down slow and then it comes to a certain distance. Then as the ball rolls, there are billions of small impacts on the ball right Professionals in the plane, the ball is imperfect. There's wind or whatever, and every one of these imperfections is definitely not ghosts. Everyone of them. Make some small impotent specially Direction, actually, probably but when you add them all together, it's a ghost because there are a lot of them. So it I mean there is a theorem there is math behind it but let's just limit here. So when you average out loads of Small nudges that go in opposite in different directions. What you get is more or less goes, unless there is some systemic bias inside like if all of your niches are in the same direction and of course you don't get to goes but that's different. So the so this is why. This. Noise this error in linear. Regression is indeed most natural to model with ghosts. With normal distribution and that's why the normal distribution is called normal. And that's why it's so so important, right? So, if you just look at its shape with the density here, you wouldn't understand why it's it holds us. Such a special place. Well, it's special because of the central limit theorem because everything converges to goes and away, and so if we do this assumption here, P of sorry, not P, but That was an already normal distribution of Y and around W Times, xn with some variance Sigma squared, it's a one-dimensional gaussian. We're talking about viands right now. This will be our. So, this was the first assumption. This is our second assumption that the center is linear function. That's the linear linear regression. And this is the third assumption that the noise is goes, Okay. There is a fourth but we'll get back. We'll get there. so, what is the Let me write down the density of the ghosts and it's one over square. Root of 2 pi is squared times e to the power. Minus 1 over 2 Sigma squared times, Y, and minus W Times X and squared and that's it, okay? so, Looks pretty complicated. What do you do next? Next are our first job is to maximize the thing, right? So we want to, let's say, I want to get the maximum likelihood hypothesis on the weights. I need to take the likelihood and I need to maximize. How do you? Always inevitably, do it in practice the very first trick that is always supplied and it's usually like understood without even explicitly writing it down. In machine learning. The likelihood is always as we discussed a big product of stuff. Right, so it's a product overall data points and there are lots of data points and we multiply the likelihoods of data points all together. So when you have a big big product, what you always want to do is take the logarithm. Right? So you want to convert the product to sum? Because if you keep multiplying small numbers like probabilities, it will be very difficult numerically, right? So the first step is always to take the locks So, look pod, even W and now this formula is the sum over n. This is what minus 1/2 times look. 2 by Sigma squared, I'll leave it at that. Minus 1 over 2 Sigma squared Y and I'm going to now this is a constant that goes out of the sum. So it's minus n over to Look to Pi Sigma squared. This can also go out of the sum and inside the sum, we have Wire minus W Times, xn squared. Okay. And now our problem, our equation is, I want to maximize this with respect to w. There is a minus sign here. So if I just look at this sum, this one doesn't have any WS. So this one is irrelevant. It's a constant. And the W is in here. And there is a minus sign. So what I do is this sum is I actually want to minimize it. Right. That's it. There you go that's the motivation behind having a sum of squares specifically squares and not. Absolute value is not exponents. Not anything. The story of course, does not stop here. It's not at the beginning. Okay. Oh yeah, and one more thing, I, I promise to go back to the fourth, assumption. So, there is a force assumption which is kind of hidden over here. And the fourth assumption is that The variance. Is the same. Over the whole data set, right in statistics. It's called There is a difficult word, homoscedasticity I think. so, if you have a homeless Scholastic process, it means that the noise variance is constant across the whole process and it's It's the assumption that allows us to actually take the sigma and get it out of the summon, not care about the same. And that can be violated and practices, right? So in practice it's quite possible that you can have points that go like this. There is a good first their dance and then they become more noisy for example. And you still want to have a single straight line that goes that describes all of these points. I have. But yeah if something like that happens, then you need to modify the last function you need to actually explicitly notice this which is not very well and then understand what it tells you about those. So this is by the way, one of the most direct reasons why you actually want to understand this probabilistic approach because it's It may seem at First Once that. Okay, so we explained why squares, but it doesn't change anything right. We are still minimizing the sum of spares, right? But the point is not to, it's not only so like, why do we want to understand stuff? We want to understand stuff in order to notice when it stops working. We understand, we want to understand the assumptions behind the sum of squares. So that when they are violated, when we are not in this situation, we actually know it's not for example, when our variance is change in the middle of the process. Or, for example, when we have reasons to build that all of the noise is only in a single Direction, Right. So now you want to have an estimate noise distribution and its distribution. That's only on the positive part of the line. Also, there are variations of linear regression like this too. Of course, it's not like it to do any new math here, but you need to know, notice this and to apply the correct math, right? Um, okay. So this is our first step and we compute the sum of squares and blah. but of course, we want to apply Our bias and story, right? So we want to say, hmm. What I am actually interested in is not P of D given W but it's p of w d. Right. Which means? That I need to have a prayer, right? What does A prior look like for linear regression. Well, it's a more complicated thing and again as soon as we get to something like bass and inference something like prior distributions. Well, the probability Theory becomes a bit Messier. Like in coins, we had a very simple discrete likely Hood, just to outcomes but then as soon as we went to the prior and posterior, Distributions became continuous. There was no way around that here, everything is continuous, but from the single one dimensional clean house and now we need to go to a multi-dimensional distribution. Right. So now there are several different ways and we want to have a distribution on them. But before we chose before we choose it what is going to happen with our optimization problem? Like if I now want to maximize the posterior distribution, what does it actually mean in terms of the numerical problem that I'm solving? Well, to be honest, it changes quite little. So what we are basically saying and this is also true, I can entire machine learning where basically, saying like a proportional means that there is a constant, which doesn't matter right from maximization. And then we have this look Like likelihood, which we already had before and then there is the lock prior. So basically, I want to maximize this case together. Right. And the lock prior. You probably in some previous classes, you probably have seen already all of this look prior stuff and you usually call them regularizers. Right. So regularization Is actually. The process of putting a prior on the parameters of your model. So what is the difference between this terms and practice differences that the regularizer does not depend on the data, right? So it's the part of the loss function. That is only about the weights only about the model parameters and not about the dataset. and, So formally, it's a it's our prior beliefs. It's what we think about the ways of our linear regression before. We start getting the data. and at this point, It may sound. Quite strange. Because if for a coin, we did have an intuition, like a real life intuition that coins are approximately fair, right? So for a coin that they take out of my pocket, obviously, I do have some kind of Prior beliefs that are actually quite strong For linear regression. Seems like we don't Right. So for linear regression, it seems like the regular eraser shouldn't be doing anything. A what's like, how do I prefer? One slope of this straight line to another slope. I don't know if I don't have any data, they all are the same for me or at least they should be right. Well. Here is how it actually works. so, To make a good illustration. I won't go to the multi-dimensional case, but I will make like a multi-dimensional regression out of a one-dimension progress. So an example that I always give and that I think is illustrates this. The best is let's extract some additional features from ads. Okay? So this is all so an important discussion and so on, right? So how do people usually apply simple models like linear regression? well, they have their access their original inputs and sometimes it so happens that you can just treat excess as numbers and do a linear regression and your output is W Times X and everybody's happy but more often than not, you before you go to learn the weights, you actually extract some kind of features from X. Sometimes. And then you get some, you know, fear of X Firefox and then you do the linear regression and the output is W Times 5x, okay? So sometimes feature extraction is about reducing the content. Like if you want to do linear regression on images then obviously it makes no sense to the linear regression on the pixels right. If first one to extract some semantically rich features and then the linear regression Sometimes it's the opposite. Sometimes X is very simple and you want to just describe a more complicated dependency between X and Y and you need to extract additional features. So this is an example like that. and suppose that I have one dimensional regression. So there is only one X. There is only one way. Ah, but when I look at my points. I kind of realized. That they're definitely not linear. Right. I realized that they don't look like a straight line at all. But they kind of look like a parabola. They kind of look like a quadratic function. So, Here is a question. Can I use linear regression? To actually learn a parabola here to learn something like w0 plus W 1 times X Plus W2 times x squared. Yes, if we make a feature, yeah. Precisely. So, The three billionaire regression of only give you this, but we already know that we can add more features it in a trivial way. Now, let's do it in the history will be. So let's go from X to this feature Vector One X x squared. And then you multiply and then you do just linear regression. Right? And when you do linear regression on this, what you are actually minimizing, what is your loss function, it's the sum of Y and minus What minus? Well, w0, plus W1 times X plus W, 2 times x squared, There we go, right? So you are actually fitting a parable. And actually this discussion is extremely relevant to deep learning. Because what is the the thing that deep learning is doing what? What are the neural networks always doing? They are learning good feature, extractors that's the whole like the whole Revolution. So before declaring worked What we would usually do is machine Learners. We would try to invent this feature extraction, part by hand or from some other. For some other reasons, right? And then we would run relatively simple models on this features of course not necessarily linear regression but relatively simple models. What neural networks do is they make feature extraction apart of the model. so now, the feature extraction also has weights And how does a neural network actually look? Let's say I have an image at the input. Then there are like lots of layers that do different interesting stuff, blah blah. But then at the end of this layers, we have actually a vector of numbers that goes into the final layer. And the final layer, depending on what problem you are solving. If it's, if you're predicting a number, it's usually a linearly So if, if you're output is supposed to be a number, not the classification problem. Then the last layer is probably linear. Almost always, I don't know any exceptions. What this means is that. This part of the network. Is doing feature extraction for the last linear. Regression layer. The last layer is actually linear regression but not on the pixels of the input, not on the X but on the features extracted from X. And of course, the hard part is learning the previously layers. The last layer is kind of easy and we are now doing these stuff of course, but it's, it's there. so, any Basically, any big complicated neural network that predicts a number? Almost always ends with a linear regression. Any complicated neural network that does specification? And with a logistic regression, we'll get there later. so, the rest of the network, Is extracting features for this last final layer. That that's that's the connection that's why this linear models are still very, very low for deep learning as well. All right, so back to linear regression. Yeah, and at this point, I think I want to make an example of this. Let me see. Let me see. There we go. Yeah. so, I put some more Stuff here. But yeah for now, Okay, we're getting there. Yeah for now. let's, Okay, yeah, there we go. So, let me show you. A polynomial, regression problem. I have the true function, the original function, which is actually not polynomial. So we will we don't expect to capture this function exactly. It's it's a sign for sine wave. but, I take one period of this sine wave. And they put the points around this one period of the same wave. Okay. So the stars are the points. They horizontal line is X. There is only one dimension here and the vertical line is why the workplace is why so, when you look at this Stars, You kind of immediately realize that they are not linear, right? And if you actually fit linear regression, you get a straight line. Of course, you get some line. Sure, but the air is very high, right? So obviously not describing this points. Well, so, first question to you, what do you think is the proper degree of the polynomial? What would be a good degree of the polynomial? I can't put the sine wave here, but I can do it in. You please. Repeat the question. Yeah. What would be a good degree of the polynomial to fit this points? So the straight line degree one doesn't work. What, what would work? I think the degree of free. Yeah, exactly. Yeah. So a parabola probably also doesn't capture this, right? So it's a little better, but not much, but if you go to the degree 3, then yeah, the third degree program has this, to one minimum, one maximum can have. And we kind of already made can match one period of the sine of, right? So if I train a third degree, put an email, they sew their four. A four weight including the intercept. Then it's already a pretty good fit and if I compute their second thing I have here, but if a computer there, they will be fine. But what happens if I keep increasing the degree? So, if I increase it to four or five, I don't think much will happen. I think they have a look approximately the same. So if you look at the degree foreign degree 5 curves, they are slightly better but it's basically the same stuff. When do you think it's gonna break? Or is it gonna break or can I increase the degree? Indefinitely. Maybe. Okay, they're not 25. What do you need to know answer this? What do we need to know to us? Yeah. Like okay, we will make a number of points. It goes to each point. It will break. Yeah, sure. So, yeah, of course, we cannot predict in advance, when exactly, it's going to be start to be bad, but we definitely know when it's certainly going to be read. And here I have one, two, three, four, five, six, seven, eight, nine, ten, eleven points. So for 11 points, if I do a polynomial of degree 10, a polynomial of degree 10 can just pass through all of this points. Exactly right. So let me keep the third degree and add the Grid 10. And this is what and interpolation polynomial looks like. So, it passes through every point. Exactly. Which is great. but, So they Training Center is exactly zero. But the test sets there is huge, right? It's completely useful for predicting. It has this very strange Peaks on the left on the right. Even some in the middle a little bit. So it's it's definitely a very bad model much worse than the orange curve, right? And that's in details as you write in chat. That's the classical picture of overheating. So we have too many parameters. And in this case of course it's quite obvious that we have too many parameters and What do we do? Like how do we notice this overheating? If we can't just look at the picture right in real life, there would be a high-dimensional input and we wouldn't be able to just look at the picture. How do we know what you said? Well, in this specific case, it's very easy to say just don't do this, right? So this is of course, it's a generic case. This is a very simple example and you can say, well obviously we have 11 points, we don't want to degree the polynomial of degree 10. That's easy. You don't need any Theory to understand this. but, In real life, we usually cannot avoid this completely. So in this simple example, where I have a one dimensional X and I choose the degree myself. Sure, I can just look at the pictures and pictures. That's why I'm showing to you because the pictures make it obvious But in real life, what's gonna happen is actually this and I'm answering this, on asked, question of how can this happen and practice with linear regression? And the answer is basically this what would actually happen to you when you do linear regression, you have your data set. And you have in your dataset points of the greedy. So it's not one thing and one dimension one nothing but will ever happen I mentioned one is easy, but you have points of Dimension d and you are trying to Do linear regression? And your failing? Okay. So if linear regression works like this perfect, you don't need anything else, but you're failing you can see that the relationship is not really linear. You want some something else you want something more? right So this doesn't work and you don't you make the next step. What is the next step? Let's do it. But unlike the one dimensional case where the code rating depends. It just adds one more feature and you control it very friendly you go to degrees 38 one more feature go to degree for you at one more feature. So you'll choose the number of features explicitly basic. If you have a multi-dimensional vector doesn't work like that anymore. Right. So if you go from X of the greedy of Dimension this area of lengthy to a quadratic. Feature vector. What you actually get is something like 1 x 1 x d. The next one squared, x 1, x 2, x 1, x 3, and all the way to XD squared, right? So the actual number of features is something like, maybe I'm missing some plus or minus 1 but something like this, something on the order of this squared. Right. Which is. quite a bit in the sense that now, if I start with the vector of size, 100 And I go to accelerating dependency. I immediately get not 200 features. Not even 500 features, but I get what 5,000 features about approximately. And of course, when you go from 100 features to 5000 features, overheating can happen. All right. So this is the actual mechanism like, of course, in dimension one, it's it's it's always easy. But in high Dimensions there is no middle ground. You can't go to degrees 3/5, right? so, and actually, like, when you look at all of these features, you understand, of course in your head that you don't need all of them, of course, of course, you don't need all of them. You only need some of these quadratically dependencies. So like in reality what matters is, maybe like the relation, the dependency, the connection between X1 and X3 and then maybe XD squared and then maybe something else in the middle and that's it. And the rest could be 0. But the point is, you don't know in advance which ones that's the whole point of learning, right. And you need to figure out which of this interactions matter, they're called interactions and statistics. When you get this features like X1, X3, we each of these interactions matter. and, You can't do it when you if you don't start with them, all right? So overheating is kind of inherent in machine learning. You can not avoid it, even for linear regression, let alone something complicated like neural networks. So, getting back here. How could be notice that something bad is happening? If we cannot just look at the picture, how can we know just over it? There is a simple principle dancer. A principled answer would be so let's do a test set or to be more precise, validation set. Let's set aside a part of the points. Let's measure the validation set error. And when the validation Center starts to grow, we stop that's the standard procedures, standard procedure and machine learning. but, And if you can do it, it's fine. but, Again, in this example. You can't really do it. So well, I mean maybe okay. Maybe you can imagine like, aiding this quadratic terms one by one and you know but then he would need to kind of go through all of them and then go through all of them. Again probably would be impractical. but if you know of them at once, you just get overheating, you get this High test center and what do you do, you know, There is no continuous process that you can just stop at some point. So, How else, what is another symptom of overheating Happening Here? How else is? It could at work. Well. Here, I output them over here. You can also look at the coefficients. And this sounds a little bit counterintuitive, but we are getting back to to the stuff that we actually, that is actually useful for us now. If you look at the coefficients of this polynomials, let me a lot of them. So the plot is now completely unreadable. But let's look over here. If you look at the coefficients of this polynomials, You will know just that as the degree, is the degree increases. The coefficient grow. But they grow kind of in a bounded way and then when overfeeding starts to happen in this case, it's only the equals to 10, but it could happen a bit before. You see a sudden jump in the question. So you see if coefficients like plus or minus 50. and at this point, you can notice that and you can say, well, so this this is the tricky part here. This is the not really formal part. You can say, well, I have like 10 points, 11 points that and the x is always about one. So it's from negative one, one and a half to positive 2. And the Y is from minus to plus one. And this points are described by a model with coefficients, like 50. That doesn't sound possible to me. Okay. so, This is the intuitive reading of this. And the formation of this would be my prior belief about the coefficients is that they should actually be relatively small. They should for this data set. They should be on the order of plus or minus one, or maybe two, but definitely not 50. Right. and, You know, think about this way, maybe this picture also find very helpful. So Ah when you do a standard, linear regression, you have this two-dimension. If you have one dimensional X and standard linear regression, you have two dimensions of Weights. So you have the two-dimensional space of weights to choose from Right. And then you go to quadratic regression, you get a three-dimensional space of weights. Which is now it's not a mathematical term but we just kind of larger. You have a larger variety of models to choose from. I can make it precise, but we won't have time in class to make it precise. And then you go to Dimension 4, you get even more different models. There are much more. Polynomials of degree 4th and there are problems of degree 2. because I'm a degree for include Polymers of the Creator and then some and what if so models of degree 4 can Explain can. Approximate. More data sets, many more different dependencies between points then polynomial degree. So you get this much larger set of ways to choose from. and then you go up to degree 10 and At some point. This variety becomes too much, right? And this gets you to overheating. So, one way to reduce the variety would be to go back and the dimension. But if you cannot afford that like in this multi-dimensional example, if you can't just do a smaller set of features, then what you could do is you could try to limit this variety inside the big space. So you could say, okay I have to stick with the 11th but at least let me look for Solutions inside like near zero. At least let me constrain the vectors in the National Space. So I kind of again intuitively I kind of want to Constrain the variety of the models. And that's what regularization does. And that's what that's what priority distributions do. so, in this case, in the case, what we actually do here, how can this hold this problem? It would be, we need to add a prior distribution. That would tell me that the weights are relatively small, So what does it mean? It means that P of w. should be like, Somewhere around zero concentrated somewhere around 0, probably we don't want to completely exclude anything we want. All the address to have some non-zero density, but we want it to be concentrated around zero and then just go. Just reduce and another Direction and all and all directions, right? and what kind of a distribution could that be Well, the obvious answer, it could be a ghost, right? So you could say, okay let's say the P of w. is a gaussian centered around zero, we sum Covariance Matrix. And since it's a prior distribution and I don't distinguish between different weights. I see no reason to have anything but the identity Matrix here. So I don't, I don't in advance, I don't know which way it's will be dependent with which so let me let the prior be independent. Ah, and then I don't want to actually go into in this class. I don't want to go into the density of multidimensional goals and Etc. If, if you're interested, I I do teach classes like this personally in Russian, but there are quite a few Russian speakers among you. You can watch on my website, some other classes where I spent like a whole semester on this kind of stuff, but let me just say that from from this P of w, the log P of w will be some constant minus one over two Sigma 0 squared times. The norm of the vector, W Times the sum of wi squared. Right. and then, if I add this prior to My likelihood which is already fixed. This is part of the model. Then what they actually get is something is a lost function that looks like this some of our end why and minus W Times X and squared that's the likelihood part. And let's okay, let's put one over Sigma square root here. Plus. 1 over Sigma, zero squared, the prior variance. Times this sum of squares of the W's. And I want to minimize this. So again constants don't really matter so I can put this signal over here. Cancel the 2. and, What I get. Is exactly. The sum of squares with. What is often called and L2 regular eraser. L2 means. Regular eraser. The regularizer is often the norm of the vector of way and Norm of the vector of weights, and then the L2 Norm in the L2 space is sum of squares. The equation. So that's an L2 regularizer. And then I can use this regular, I can fix the problems. So if let me see if I have Let me see if I have. Yeah, we'll skip the local features time for that. Yeah. Yeah, I do have it. Okay. So so, first of all, before I show that before I show, regularization, let me say that, This kind of overheating and regularization everything is dependent on the data set also, right? So no, it is how when we went to degree 10, we got severe over fitting only because we had exactly 11 points, right? If we just add more points, a degree and polynomial will be fine, that's kind of obvious, but I wanted to mention it, right? So, if I have 100 points, not 10, then of course a degree 10 polynomial will not be severe or fit. And that's for regularization. As regularization here is the data set. Here is the original function with no, no regularization. It's the interpolation polynomial and Alpha is basically this equation this guy over here. so, ASI, increase Alpha. It will become more important, right? So it will, it will be The shape of this curve, the shape of this polynomial will be determined more and more by the regularizer and less by the actual Training Center. So if I have this kind of small regularizer, like 1 over 1,000 then, you can see that actually actually, it's already pretty strong. Okay, let me let me make it even bigger. In this case. Yeah. So the absolute value of the coefficients are already kind of reduced but you still see this some of this local extremes at the yeah in this. Yeah as you can. Okay here is another illustration. Obviously I do the points at random every time so for this specific set of friends and points even a very small regularization is enough. So actually we it would take a lot to straighten out this guy's on on the extreme but the other special features are kind of already straight up. Yeah, but okay. So let's let's make the regularizer even smaller. Yeah. So at some point, you can see that. It gradually. Irons out this overfitting. and I already showed that with some Good value of alpha. You can get a very good curve over here. Let's see if I can even straighten out the sides. I'm not sure I can, but yeah, I can make this effect smaller. At least. Okay. Here I strange that straighten it out on the left but not on the right. So, yeah, as I keep increasing the regularizer, Remove this one and keep increasing this one. As I increase the regular eraser. Okay, so this is a good craft now. I will see that the degree 10 polynomial, it's still great and it's properly degree. And if you look at the coefficients, yes, they become closer to 0 but they're not like everything is 0, except the first three know, they are still meaningful over here. For example So it's still a great example. Ah but now it behaves much better, right? So we are kind of got rid of the regularizer of the overfeeding by regularization. But then, of course you can overdo it. So if you go to something like 10, you will get like a curve that a degree 10 polynomial. It doesn't care about the points in at all right. It only cares about the regularizer and in this case, of course, it's also a bit model. So as with all things in life, there is a trade-off. Okay. And what else did I want to say here? Was that? again, I don't want to go into the math here and probably able to have to skip the base and part here, but I don't want to mention that. If you look so the L2 regularizer the gaussian prior is indeed special for linear regression. So as we discussed yesterday with this, conjugate priors with the prior in the form of the likelihood blah blah, blah. You can know just that here. Also, Here. Also, She also what sorry. Here. Also the shape of the gaussian regularizer matches the shape of the gaussian likelihood. It's a quadratic function of w, right? So of course, it's convenient to add two quadratic functions of w. Also get the quadratic function of w and to get the ghosts and again So this is the conjugate prior and you can go from gaussian to gaussian in the space of Weights. Let's let's not go into my my first turn to that discussion but linear regression also gives us a good example that you don't necessarily have to do that. So here, you can have very good reasons to choose different regular erasers very good reasons like So one other common regularizer for many models and for it for neural Nets as well, would be an L1 regular race. So let's start from this. So what if instead of adding sum of squares I would add. The sum of absolute values here. So, Notice that there is a difference here, there is an asymmetry. The error. The noise. Is a property of our model. It's I mean yeah we kind of choose it but we are supposed to choose it correctly. There is a right answer in the wrong answer here. Like what is the actual noise in the actual process that we got the data with that would be the perfect? Correct answer. There is some kind of underlying truth here. Probably it's not exactly goes and probably it's an approximation but There is a way in which there is the correct. Answer to the question of what is the what is the right likelihood? But there is no correct. Answer to the question. What is the right prior? It's completely our choice. We choose the prior to match whatever we want. and, We might want to choose something else. So, this is L1 regularization. And so they you may also encounter this terms. The linear regression with L1 regularization is called the loss or regression a last Saw is actually an acronym for Something like least average inch. I forget never comes up. And this is called the rich regression. Rich is not an acronym, it's this reach the calcium. But anyway, You might want to choose a non-conjugated prayer because it has Better Properties. So I have it here. So, let me let me show this property to you, they don't have time to discuss, why? But this, let's let's see the how it works. So, If you look at the same kind of regularization way but we still lost sorry creation with the L1 regularizer, not the rich regression. Not the author regularizer. You will see that. It all is like a pretty good curve. It's still it doesn't overheat. It goes very own and probably we need some kind of lower weight here. Yeah, okay so now this looks a lot like the best Rich regression that we got right? So the curve is approximately the same But if you look at the actual coefficients, you will see something very different. You will see that, like many of the coefficients have gone to exactly zero. And some are clearly, like, on their way to exactly zero. With which regression they were all decreasing more or less isotropically. So, to speak, right? There were all decreasing together, getting closer to 0. maybe not with exactly the same speed but they were all non-zero when we checked here. Some coefficients become exactly zero or very close to zero and you can send them exactly to zero. That's will change. And sometimes that are that desirable property, right? So sometimes you might want to have sparsity in the results. so, why this is This is what we would call a sparsity inducing regular race. And for example, I think it would be a better fit for our question over here. Right? So if I get a lot of different features and I need to choose out of them then It instead of some arbitrary setting, the threshold and you know picking which small number is better than another small number. Why not? Choose a different way of regularization to set some of them executive zero. Okay, so this is our choice. This this is this is an hour hand. Okay, so we need to have a break by now, but so let me summarize I discuss linear regression. We didn't go into the actual base and inference, it doesn't much matter for for the rest of our class. So it's okay, that we skip it, but I did want to highlight two important points. First linear regression is relevant to any kind of complicated neural networks still and we will see it in an architecture. But most importantly, all of this probabilistic machine and all of these discussions about likelihoods priors probabilistic assumptions how they all come together. What they are actually doing for us in deep learning. Is they are giving us the loss functions. Okay. so notice that when I write the general formula like this, It doesn't matter what the model is, right? It's just about, okay, so this is too general form, this is about everything, but when I write even a formula like this, Okay, the model is only over here. Right. And this is the noise distribution, but the linear model is only over here. And of course, I can change. If I keep the noise distribution, Goshen, I can change the model to something else. so if I was, I I can do any Kind of function over here. And maybe it will be more difficult to optimize. It will not be quite right, okay. It will be like completely different thing in terms of in practice but I still get the same kind of loss function, Square deviation and I still get the same kind of regularizer if I want. And this is still a very common loss function, whatever the model is, right? And this may be a neural network. Maybe a very complex neural network. It may be anything that we will discuss later in class, but then it gets plugged in to the loss function. That comes from some probabilistic assumptions that we make. That that's my point in the first part. Okay, any questions? Okay good. So let's have a break over here and then I will briefly discuss. Logistic regression will not go into the same kind of detail, but it's really important to get this, the soft Max function, right? So, we will discuss the main Assumption of the softmax and then finally, we'll get in your own networks. I promise break. Here. You. For me. Okay, let's continue. So we just discussed, linear regression before the brake. While you are gettering back, let me go through the slides to see what they missed. A linear regression sum of squares, the gaussian noise hypothesis. Blah, blah. You can get a posterior distribution, to get the predictive distribution. We didn't get there, unfortunately, by using regularization, we didn't derive this formula. No matter, this would be interesting, but I think it's time for us to move on. And yeah, and our next point. Is classification. Which is probably even more important. For deep learning for neural networks, then. Linear regression and predicting numbers. so how our third one point, Is the logistic regression. I'll try to be quick about it, but I do want to get the general idea across so suppose that we are sold in a classification problem. So what is specification like you have you want to distinguish cats from dogs? And if you are in a lower dimensional space, you can visualize it as trying to get separated decision surface between Two or more sets of points. The difference between logistic the difference between classification and regression is in the nature of Y, right? It's in the nature of the target variable. So it's still classification. Of course is still supervised learning. We still have a data set. That looks like this. But now for linear regression, why and was a number. But now I am is like a class label. Right. So it's Just, it just create variable with the finite set of values. It's one of several classes that we want to listen. So what does it mean for us for constructing, the model for building the likelihood for everything like that? It means that since we're not predicting a number, what? I mean, okay, not just since we're not predict number. it means that in most cases, even though we are not predicting a number, we still do want to have a number of the output. So, what is? Kind of bad about discrete Target variables and that will, we will come back to that in deep learning as well. The bad thing about the discrete Target variable. So let's say that I'm doing like a simple threshold rule for classifying and they have like one class is the 0 and then affects exceeds some threshold. Then I start to Output one, right? So this is like the simplest classifier possible, one dimension, one input to classes and they chose by threshold. What's the problem with this function? If it was my output, The problem is that. This function. Since its best ways constant, right? It has no derivatives, I mean does have derivatives, but it's derivative through 0. So what this actually means is that if so if this is just X and this is and the thing that I'm learning is on the A and that it's fine. But what if they input is actually some kind of as it, always happens in real life in neural networks and everywhere. What if the input is some kind of function of X with some weights? Some model some feature extractors Etc. If that happens then we don't know what to do with this feature structure, we don't know how to train it. Because you can take the gradients and we will be taking gradients in Dearing. And but if you take the gradient of this function, it's always zero. It's, it doesn't give us any any information at all. And you can understand that intuitively is supposed that I take the weights W and I take them a little bit I change them slightly then the input to this fresh hold will move a little bit. Did it move in the right direction or in the wrong direction? By looking at the output we have, absolutely, no idea. There are output, does not change, it does not change, it does not change, it does not change and suddenly changes. That's not something that we can actually trade through. um, so what we actually want and both for this practical reason and also for conceptual reasons like Both for this practical reason and for conceptual reasons like we also want to estimate our uncertainty. We want to evaluate how sure we are, what we actually want to have the output of a classifier. Is not just the class label but a probability distribution, of course. So let's start with two classes if I only have C1 and C2. What I actually Get some dogs, right? What they actually want to have? The output is p of C1 given X. Okay. if you want to give an X, That is for a new point. I want to evaluate. How likely it is that it belongs to to the first class as a second? And where, where does the logistic regression appear? What's, what's the reasoning behind it? Well, actually, it's, it's pretty, it's pretty straightforward or I mean, we could make it more complicated, but it's not a straightforward reasoning. Behind logistic regression, looks like this. So, let's assume that I want a linear model. So I do want to have a linear Model A linear separating surface. I do want something that includes W Times X and that's how X should appear in their you know, question. I also got an also got a window that's at internet's unstable. Did it fix itself? Is it okay? Now. Want to. Sometimes yeah, yeah, it's right in case. Unintelligible. Uh-huh. Okay, so okay if it's better now then just keep me informed if anything changes. Okay. So anyway, suppose I want PFC one given X And I wanted to be. To be derived from like a linear function of the features. So I want the access the inputs to have. A linear to go through linear function. so, Can I? Take this probability and the proximate like I did and linear regression with a linear function of the inputs. Kind of obviously not right, because the probability chair is a number between 0 and 1. And if they approximated with the linear function, of course, it will go to Infinity at one and the other end everywhere. So it's not a good idea to operate to model probabilities by linear functions, right? What can I do instead? Well? I can use the best theorem here of X, you know, see one. BBC, One P of X, right? And then I can expand this. Since I only have two outcomes to classes, it's pretty easy. You can just say the pox Is one possible numerator, plus the other possible numerator. Right. Now, I have a lot of different things in here and I only want to model one thing. So let me Divide by the numerator and I get one over one plus P of x given c, 2, c, 2. Divided by P of x given C1 times P of c 1. Okay. so, this thing, You can view it as P of C2, given x divided by P of C1. Given X is the same thing. And this thing is known as the odds. Right. So the odds are Oh, like when you say in real life, when you say, I give you 50 to 1 oats, what does 50 to 1 minute creates this ratio, right? It's the ratio of the probability of a sign. For one outcome divided by the probability of the other. That's that's what it means to give thoughts. Ah, and as I just said, odds can be like 50 to 1 or 1 to 50, right? So odds are not constrained by one. They are ratio of two probabilities, so they go they can go to Infinity. But does it make sense to model them as a linear function? Well again, not really. Because even though they can go to Infinity, they still cannot be negative, right? It's ratio of two probabilities and the linear function will be negative somewhere, but half of the space. It will be angry. so, this is also not a nature thing to model with the linear function, but we are getting there. Just one small step left. We have a positive quantity, and we want to model it, somehow linearly What is the transformation that we need? Oh, we can take the lock, right? So, if you take the lock of some of some of something that goes from 0 to Infinity, not including zero, then now you get something to goals from negative. so then we go to this, e, to the power, it's customary to put the minus sign here, it doesn't really matter, but Usually people do. So now the fraction flips the ratio flips POC to so, this guy is called the logos. The logarithm of the odds. And now, this indeed does make sense to model with a linear function because now it's a quantity that goes from negative Infinity to infinity and it has exactly the properties that we want at negative Infinity, go to 0, the probability goes to 0 at positive Infinity, the probability goes to 1 and in between at 120 increase. So logistic regression is exactly as well. Which is a regression is the model where you say that P of C1 given X. Is 10 over 1 plus e to the power, minus a linear function of x. This function is called the logistic sigmoid. so Sigma of a is like 1 over 1 plus, e, to the power minus a and it's this It's a sigma function, right? So it goes from negative Infinity to Infinity. It goes through one. Half at zero, And it asymptotically goes to one or on the right into the 0 in the left. It's an important function machine learning. Then we get, what is p of C2? Given X. Well, unfortunately, it's a bit more complicated because it's one minus Sigma of W Times X, right? So, if I try to do like, The. Likelihood of data set for logistic regression. Again, I I do a product of P of YNS, given W and X sense, but then it will be a product of like sometimes it's Sigma and sometimes it's one minus Sigma and then it's Sigma and then at Sigma and then it's 1 minus segment. So on, right? So it's a bit more complicated, it's more complicated function than the linear regression. We cannot get it's not quadratic of course anymore and we cannot do it in closed form but we can be something like gradient descent or second order methods. In this case also can be used. We can actually optimize the likelihood. We can add prayers and do it in a regularized way and so forth. so, this is This is actually a linear model in machine. Learning institutes. A linear model, is something that that is a function of this. It doesn't have to be linear all the way, but X is Occur in there in a linear combination. And it's a very natural linear model for classification. For binary classification. How do we make it more than binary? How do we make? How do we insert several classes here? Well here I was just modeling while one quantity and if I have like basically going to us, if I have only two classes, then sure I only need to model one probability. But if I have several classes, you want to see k? Then now it's not enough. To model, it's not enough to have only one vector W. That is multiplied by X. Because from one number, I will not get K. Minus one different numbers, right? And I need game -20 different numbers to model. This diro between Kate classes, So instead now I basically say that okay well I will not model a single logo for between two classes. I will just Say this. So P of C Small key given X. Just like this, it's p of C Smalls. He's okay divided by the sum overall classes, right? B u c s p o, x x given c s. Ah, and let me just again, take the logs so I can also have negative numbers. So, e to the power of this. Divided by the sum of e, to the power of the same but about class s. And then, let me just say that. Now I'm modeling every exponent here with its own linear function, So, I'm saying that like WK times x. Should be like P of c k times P of x given c k. No notice that. It doesn't quite work as I wrote it because they did the thing on the right cannot be negative. They just said it's a bad thing but to be honest it doesn't matter. So when you get negative numbers from some of the scores this are usually cool scores or affinities or something like that. So it's like a measure of how like a plus K is but not the probability just a number, right? So when you get Negative scores, you can just Cancel, out the negative parts. So if you have like, e to the power, minus 2 divided by e to the power 1 plus, e to the power, minus 1 plus, e to the power minus 2, the same, then you can just take e to the power minus 2 and cancel it out, right? So, and everything becomes non-negative right now, it's e to the power 0, e to the power of 3 plus E1 plus e 0, that's it, right? So you can always in this formula you don't, it doesn't matter if sometimes you get negative because you can always send a baseline like this and it just cancels out. And that's it. So this is how you do multi-class classification and this thing now it's a vector function, right? So now it's a function that Maps the vector a to another Vector full of this guys. So like the case coordinate is it to the power, a k divided by the sum of e to the power, a s. Right normalized. Normalized exponents. Ah, and this is called the softmax function. so, the softmax Of. Okay, let me write it again. A1 and A2. AK is another vector. And at the case spot, we have e to the power AK normalized so that it becomes a vector of probabilities. That's it. That's the softmax are why is it called the softmax? Because the exponents have this tendency to, you know, exaggerate the differences. Like if you have one of the ace, one of the arguments to be significantly larger than the others. Then what you get is a result, will the basically probability one for this guy and probability about your of the others. So, we are kind of taking the maximum of, of the arguments. But we are doing it in a soft way with as a continuous function, that is never exactly zero. That you can take your relatives of that allows for gradients, gradient descent Etc. so that's a soft version of taking the arc, Max Okay, and I won't go into more details about logistic regression. Not exactly our subject, but this part is important because again, this is the last layer of almost every neural networks. if you have, if you have, I don't know GPT file. Which is an insanely complicated model. I have no idea how exactly it works because nobody tells us, but if you have Jupiter 5 and it's a language model and its supposed to produce the next door. Can right now then, what is the last layer of gp35 frame. Sure. The last layer is this, after all of this internal Machinery, which is very complicated. We get LA or of scores. For every tokens for every token. And then they go through the software. And the softmax turns them into the probabilities of tokens. That's that's that's how it always works at the end because it's completely hopeless to try to to produce probabilities like immediately. It's, it's not how when neural networks work, it's not how linear functions work, it's not how anything Works. What you do is you produce some kind of scores and then you turn them into probabilities with the software. And yeah, sure. It's also very common. Now, I cannot watch for gb5, but it's also very common that the layer between the before this is linear, so we get an exact logistic regression at the end of your So we get to some features when we do a linear layer, that gets so this lead. So okay. Let me explain because I will I don't think I will explain it later and now it's a good spot. So we have some input. it goes through the neural network and then, Let's say we get to the final feature Vector, right? The final like semantically reach, very intricate extracted features and whether it's a cat or a dog is already somewhere inside. Somewhere in this feature. So it says so pretty explicitly, but we are still not sure where and we are not sure how to to get, right? So, What how do we do it? How do we What is the simplest way to process? This already extracted features. Well, I could just do a softmax and assume their scores, but they're not scores and there's probably the wrong number of them, right? So there are There is some some number of classes and here I have just extracted features that express my picture. Why should the numbers match? No reason, right? So the number of features can be different. So I do weight Matrix. I multiply W Times C and the wait Matrix so let's say this is dimension d. And this is dimension. Okay? Like number of classes so w is of Dimension D times k. And then W Times C becomes the vector. Of course. and now, I go through softmax. and I get, A vector of probability. Vector of probabilities for all the classes that I have. And this is my output and the loss function now. Will be defined on these probabilities. So the there may be some variation here but usually the loss function is just The well, it's a fancy name. It's the cross entropy between the output and the Output and the target. But if you are doing classification, the target. Looks like a one-hot vector with one one at the correct class. And 0s on the other classes, right? So, and the cross entry here, when we get there, I will write it in more detail, but the cross entry before this kind of Target will be basically, just saying that I want to have the probability of the correct question to be larger. So like the Lost function will be something like the negative. Look P of the correct class. And I want this to be blowers accordingly. Um and that's it. That's how classification Works in deep learning. Okay. So the interesting stuff happens over here. Of course, that's what we are going to be discussing for the rest of the class. But at the end, almost inevitably happens, something like this. So at the end if you're doing classification you want a vector of probabilities at the output. Can you get a vector of probabilities directly? Probably not, What you can get is a vector of scores Affinity like numbers that can be arbitrary, but that reflect how well, they input matches one of the classes and then you can convert them that that's how the stuff first. Okay. Any questions about logistic regression? I didn't go into much detail. All right, then. Then. For the rest of this lecture. Let's concentrate. On neural networks. and actually, Have. Yeah, yeah. I don't have I don't have illustrations for classification called but that's fine that it wouldn't show you anything anyway. It would be just a linear surface between two classes or three classes, but what's the point? Yeah, so we discussed logistic regression. This is what Logistics Sigma, it looks like. Then we get logistic regression. This is the softmax function. This is what we model for the softmax etc, etc. And logistic regression even though it's very It's a very simple model. It's a linear model like one step from from linear regression. So linear regression is just linear. This one is linear plus Sigma on top. But already for logistic regression. We cannot really hope to get the closed form solution. So we didn't discuss it for. Linear regression but because it really doesn't pertain to the parent. But when you're optimizing quadratic functional like this, you can just write down the answer. It will be maybe not that easy to actually Implement because it will be like the inverse of some huge huge Matrix. And in practice you would be like solving the system of linear equations with some approximate techniques, iterative approximate techniques. And I mean, it's it's a whole science but theoretically, you can just write down the answer. You can write down the formula. And it's a system of linear equations, after you take the green. Here. It's already not. Right? So if you look at a big product, okay? And you take a look and then if you have a big sum of logs of things like this, and things like this, There is no clothes phone search, right? So the only thing we can do is try to do it with some iterative optimization algorithm. And the main iterative optimization now Christmas, that we will be discussing tomorrow in great detail as of course, gradient descent. so, In in logistic regression, you can actually do a second order method, but in neural networks, you can't afford to discuss that as well. And we have to restrict ourselves to variations of gradient descent gradient sentence. When you start somewhere and you go in the direction where the loss function is really is being reduced most quickly and that is the direction opposite to the gradient of the gradient is the direction of where it grows most weightless. Well the opposite is where it decreases mostly and then you keep going until you find the local minimum. There can be many local minimum in real life in neural networks, Etc. And we'll discuss that in detail but not for not for logistic regression. All right. so, with that, Let me move on to some last May the medical far less mathematical topic but I hope also pretty interesting. And that is an introduction to keep learning, right? I will again, try to make it quick and painless I don't want to go into too many historical details or anything, but there are a few things that I want to highlight. a few things in the motivations, if you thinks in the Like how neural networks evolved. and then, we'll just Go to the main meat of our class, that will be probably tomorrow. so, Neural networks. Artificial neural networks are called artificial because there are natural neural networks right. There are neural networks in our brains and in the brains of other living beings. and, Of course, a very natural. Motivation for for a scientist would be well, I want to build a thinking machine. There already are thinking machines in the world. I have a proof of concept right here. So let me study how the thinking machine in here works, and let's try to emulate it in a computer, why not? It's all information process. and when you begin to study how the human brain works, it's actually it actually gives you some pretty important insights. So sorry my picture. Now this is not an artifact Defense. Net Connection for some reason, it is down. Simple lot. But anyway, Probably you have you probably have heard at some point, how neurons work? What a neuron is. So our brain consists of neurons Biologists will tell you that there are different kinds of neurons. There are slight differences but for our from our computational perspective, they're basically all the same and they work like this. they have this processing part, the Soma the actual like mid center of the cell and then it has all sorts of tentacles. All sorts of little things, going out of the cell and connecting to other things. Right. And there are two kinds of tendrils, I guess the better word would be. There are two kinds of this. Growth. There are the rights which are relatively short and which attach to the outputs of other neurons. And they provide inputs. So from the there are many, there is for every neuron and the dendrites get inputs for this neuron. Okay. And then, there is one. special part one, special tentacles of the neuron, which is called the Axon and the excellent can be very long. There is a neuron, there is a neuron in your spinal cord. That goes all the way to your toe, right? To every one of your toes. Actually, there are separate neurons. So they can be like up to a meter length or something. And the point is the Axon is the output computationally everywhere. Has lots of inputs, several thousands on average. And one output. Okay. So far, so good, pretty straightforward. Now what is interesting about this and this is a purely like computational very surface like inside but it's already pretty interesting in the brain. So first of all, how does a neuron work like physical? How does it say something else? It would be pretty difficult for a biological thing for a biological mechanism to read out numbers. so like it would be pretty difficult for the dendrites to capture like the exact amplitude of an electrical signal and then Process inside the neuron that from this input. I got a 2.5 and from that input. I got negative 1.46 that, that's not how biology works. Biologically, it's much easier, and faster and more reliable to just capture bits individual events. Like, is there a spike or is there not a spike? So, neurons work actually. Inspects they do not, or almost do not much late, the amplitude of their signals. So the spike. Yeah, I didn't tell a spike is the electrical signal that the neuron sends out through its Axon So the neuron always fires spikes along its actions and the other neurons who are attached to, they pick up the signals. And the spikes are more or less the same. I think there is some variation but it's not, it's not consequential. There are more or less the same. What changes is the frequency of the specs? So if the neuron is relaxed is not excited, then it turns out spikes with frequency like 10% 20%, something like this. When it gets really excited, really activated. It starts sending out spikes with the frequency of like 200 Specs. okay, so there is a big range and when a neuron sends out spikes, More often, it means. It's it's more excited. So now there is actually numerical value. It can be more excited or less excited. It's not binary. But every spike is the same and it's just transmitting basically one bit, but a different controls. and, the interesting point about this is that we have lots. Lots and lots of neurons. I think artificial neural network still haven't reached the sheer number of neurons of the human brain or maybe have just reached that, I'm not sure. So, In the human brain have like 100 billion. Um no, okay, yeah, yeah right we have like a hundred billion neurons. And every neuron. So you know that there are neural networks with 100 billion and trillion weights, right. But the way it is not in Europe, the weight for in a bio in the biological brain is on the connection between the neurons. Right? So the weight is attached is like the ways are in the synopsis. In this connections where a dendrite of one neuron takes to the extent of another And yes there are weights there so the it really in some way, it's likely in your combination, not really? But like so there are connections that get reinforced. There are connections that get inhibited, there can be negative ways, they're all sorts of things. So there are indeed weights at the synopsis that are learned that are trained in human, right? and that's how we think, that's how we learn stuff, but the point is How many weights are there in the human brain? How many parameters well have like 100 billion neurons and if each one on average has several thousands of 7,000 Senators. So if you multiply you get something like What's the quintillion or a bit less than a continued of, of synapses of Weights that are being trained in our brain? That's a huge amount. I think artificial neural networks have not yet reached that but, On the other hand. It's extremely slow. Right. so, I just told you that our brain is a computer that operates on the frequency of 10 to a couple hundred Hertz. Right. A couple of hundreds signals per second, not megahertz, not kilohertz, just hurts. And so the brain is very, very slow as a computer if you were talking about like, clock speeds, but it's huge in terms of the number of connections. And what this actually means. Is. The brain always performs highly parallel computations but cannot perform a long. Sequential computation simply doesn't have time. So for example, we recognize a phase, recognizing faces, a difficult task in computer vision, it's a difficult task, but we recognize a face in like a couple 100 milliseconds, right? And that's like the full cycle of, between the time when I show you the phrase and the time, when you press a button to, you know, to record that you have recognized the face. So it's the full cycle of feature extraction decision making motor command to the finger everything and it all fits into like two or three hundred milliseconds. So, what this actually means is that this is an actual picture of how it goes through the brain, maybe we will get back to this picture when we discussion, but maybe not. And what the section means is that the brain cannot have like a loop for I from one to 1000. It doesn't have time to do. It only has time for like 10 or 15 sequential steps of computation. And then it has to get out the answer out. Otherwise, you are already being written by land, right? And so, It's the cognitions are not sequential. But they are very, very highly parallel. So when you're, when we recognizing, if it's like half of our brain lights up. But half of our blade brain lights up, but it lights up in like 10 steps sequential. And then we have to give the answer. In a way, this is a this is the property of a brain of the brain that we actually keep in artificial neural networks. So we will just discuss how to make your own networks, really, really deep. We build discuss networks with 100s of layers and I will tell you that you can go to thousands just doesn't make sense. And yeah, it doesn't make sense. So in actually our current artificial neural networks, okay, maybe they know they have more than 10 or 20 layers, maybe they have 100, but not much more than that. So we don't we don't know how to make use of tens of thousands of layers in the neural network and let's say the proverbial GPT 5 is probably very very wide. It's probably like a mixture of experts that have been trained to the different things, blah blah, but in terms of the number of layers of sequential computations it's probably like a few dozen. Maybe a couple hundred not more. I'm pretty sure. so this kind of white blood cell thing, we will keep And the main, but the main part of the motivation, is not, of course, in the architecture, we will see that the architecture cannot be the architectural cannot be the same. It's by definition kind of very different, but The. but, What we actually want to get from like what is the Department of of the motivation that we actually want to reproduce in computers is how versatile? How adaptive How elastic our brain is. So, we can learn on very few examples and we can learn some, very, very complicated stuff on very small data samples, right? We can adapt new data sources. There are experiments like this one where you can actually like you know learn to see with your tongue or something. This this is called neuroplasticity and this was a fun experiment. You do you make a small plate of electrodes? And it's the tongue just because the tongue is sensitive and a connection, really distinguish between a lot of electrodes on the tongue, but it doesn't matter. You just put it somewhere on you and then you send to the electrodes a signal from a camera picture for it. And then you just walk around. And you feel a slight tingling from the electricity? and then you stop feeling it, of course very soon because the brain and ups and stops noticing it but In if in a few days of working around this camera, your brain starts to know just that there is an actual correlation between what you see and what the stinging looks like. And there have been experiments that like after a couple of weeks of working around with this stuff, you can actually close your eyes and see through this. Through you through this electroplate. Maybe not read books, but like at least walk around that not bump into a wall station. So, And for example, you probably have heard of neuroplasticity examples. Like when somebody I know has a stroke and part of the brain stops working, sometimes it's too much over damage and the person never recovers, but sometimes they recover sometimes other parts of the brain. Take on the functions that were previously done by this now, missing part and that's, that's all. So, something that our brain can do, so, in a way, This kind of experiments. Tell us that the brain. Yes, it does. Have I predetermined areas predetermined by the ocean? Like, yes, we have our visual cortex is back there in the occipital. Lobe of the brain. Our frontal cortex is to usually doing the reasoning decision-making. Yes, But it's kind of incidental, so yeah, sure it will be this way, but the neurons are still the same. and, They there is some kind of a single learning algorithm inside the human brain that can be applied to all of these sorts of different situations. There is there are no neurons in the brain that have evolved to distinguish cats from dogs. This is a learned thing, of course. And there are no neurons in the brain that are like from birth regionally evolved to already distinguish and understand the 3D structure of the world around us computer vision suppose to do now. That's that, that's that cannot buried in the chains. There is not enough information that you just to write it down. This is all learned. This is all learned from scratch and this is learned with very high efficiency and the early stages of our life. So, we do want to have it in computers, right? That was the original motivation for neural networks, and As we will see. yeah, as we will see, we in artificial neural networks, we do keep this A general idea which is known as connectionism. Connectionism. Is this philosophical part mathematical idea that if you connect a lot of simple things together the huge composition of very simple. Things becomes very complicated and can do very interesting stuff. That. That's as simple as it gets and it's true. Right. There are lots of mathematical results about this. Like how you can approximate anything with a polynomial and approximately anything with like two layers of one University functions. You there are lots of, here's number of results about it. And neural networks are kind of based on this idea. You take very simple things. You put them together and you get a very complicated thing like a face recognition system. but in the way, That's and yeah. And another thing where artificial neural networks are really, really similar to the human brain is the structure of a single neuron We will come back to it, just right now and later. We will see the so. Okay, let's come to it right now. No point in leaving it for the future. So how does what does a neuron look like an artificial neural? Like this most basic building block of neural networks Well, it has some inputs that's One X to x n. It looks just like the linear models that we discussed just now, that's in part. That's why I'm discussing always discussing them. Then you multiply them. By the way, of this neuron and you get W Times X, you get this linear combination of inputs, with with the weights, the weights will be trained during learning of the network, but then you also need to have a nonlinear function before you can get to the output. Why. Because if you, if you're new ones were doing just linear regression, if you're neurons or did not have an nonlinear function, which is called the activation function, then there would be no point to There would be no point to have a network because, you know, composition of linear functions is linear again. Now, if I have a huge Network full of linear neurons, it's basically just one neuron applied to the hole. There is no difference. so, with linear functions, I will not get more complicated things. But as soon as I have any kind of non-linearity, we will just discuss. Just now what kind of non-linearity is there are and there are very simple ones. As soon as I have any kind of nonlinearities, even something like real, which is just two linear functions strained together. It starts to work and there is a big field of math that shows that any kind of a linearity is enough to approximate anything. It doesn't really matter in practice for us in practice, for what matters is that it works? so, as soon as we have any sort of nonlinearity it, Starts compositions of this simple neurons. Begin to approximate whatever but whatever you want it. Which still lives open the question of how to approximate how to find the way. It's how to train will discuss that. What? But basically, as soon as we have an nonlinear, we can and interestingly enough, this kind of Model for a single. Artificial neuron has been with us since 1943. since before the Turing test since before, the Dartmouth seminar, before the word artificial intelligence for any scientific meaning Already in 1943 Warren McCulloch and Walter pits wrote a paper which was called logical calculus of nervous activity. So it was actually they were approaching it from from the perspective of mathematical logic. but they had to have the they wanted to have a mathematical model of the human brain and in particular mathematical model of a single neuron and it was basically already this So even in 1943, we started off with this model of the neuron and bear still with it. So yes, there are parts of modern neural networks that are that cannot be directly explained by this neurons. So, there are like attention mechanisms. We get Transformers, We will see some functions that have weights, but that are not quite like this. But mostly most neural networks are still. Composed. From your instance like this and even Transformers have a lot of neurons like this. So, this is still the basic building block. It was first implemented in practice by Frank rosenblatt in 1958. I think I have pictures. Yep. Very romantic time. And to be in computer science, that's what the computer looked like back in the days in 1950s and this. So this is Frank Ross and what, like learning training perceptron. Right. And but it did work. So it was I think it was the first actual honest machine learning model implemented in practice. And it actually did some pretty amazing things eventually, so it learned to recognize letters. And of course, it's not real computer vision. They were not. And they were letters in a specific font photographed from a specific point. And of course this was much simpler problem that then real OCR, of course, but still it was extremely amazing for the time and when this perceptron appeared, well, I always show this New York Times quote, maybe maybe it's, let's not well on it right now. But basically, at that point, everybody decided that well, the hard part is done. So I recommend you read it, the hard part is done and we know how to make computers learn and now it's only a couple of years before they can walk talk see right, reproduced himself and be conscious of their existence. So, as we know, it took little bit more than that. This early optimism was not really warranted, but, but still is the same principles, right? We still inherit a lot from this early. Neural network ideas, Okay. How do I want here? Yeah, and then as I told you yesterday, the AI winter happened so then people somehow got convinced that machine learning doesn't really work. And in particular, by the way, they got convinced that neural networks don't work. And there were some practical reasons which are true, but there was also a very strange theoretical reason for that somehow convinced a lot of people that neural networks are worthless and the theoretical reason is this? What? Whatever. Whatever activation function you have. If you have and this is an important point. So let me make it whatever activation function you have. Whatever, whatever is the age? Still, the inputs go to H through a linear combination, right? so, if you think about it as like a model doing classification, then You are still. Drawing a linear separating surface between the clauses. so, there is So if if you have wage of W Times X and you have some decision roll afterwards, like if it's more than 0 then plus one if it's less than 0 and plus two, then the surface will be this. Right. This is the decision. Surface on one hand, on one. On one side, you have C1 and there is a C2. Which is the same thing as saying. Well, let me just see where H reaches 0 and now it's a linear surface. Right? So the non-linearity does not give you nonlinear separating surfaces, nonlinearity just gives you the ability to build networks but by itself it it's still lifts the class linear, of course. and for some reason, People look at this and say well okay so it means that one person cannot separate a lot. Cannot solve a lot of problems. There are many problems which are, which do not have linear separating surface like the solar function. If you have the orange class over here and you have the blue cross over here and over here, then, of course, there is no. Straight line. That separates them? Well, sure. This, these are linearly inseparable classes. But for some reason, people thought this that this was like an argument against perceptrons and against neural networks. Which was kind of strange, I'm still not sure how there is an actually worked. But of course, the correct answer is sure you cannot do or you cannot do not linearly and separable. Task with a single perceptron but you can do it with a network of perception problems, right? And the idea of a neural network, the idea of taking this kind of Neurons and putting them together in layers and Computing. The final result of a composition of several such neurons. It's also very old and that actually goes back to the same element during he was a smart guy. And he already in 1948 before the Turing test, he already had the paper which I don't recommend it, it's very hard to read today, but he already had the paper where he suggested actually deep neural networks. Like real deep neural networks, compositions of layers of neurons. and, They the question was, how do we train it? The answer was pretty straightforward. I think we'll discuss it in detail tomorrow. According along with all of the gradient descent variations that we have today. But the answer is, of course, well you learn by gradient descent. And to do gradient descent. The only thing you need to be able to do is to take the gradients, take the derivatives and how to take the derivatives through the computational graph? Well, I bet propagation, I think you've heard about it probably should already know it. Maybe it will. Cut through it quickly tomorrow. So it's it's not a very deep idea. Back propagation is just a general for computing probabilities. and therefore, it's hard to say who discovered it because it was kind of discovered and dependently, a lot of times, but by this 1970s, It was already kind of well known and understood that you can use back propagation to to go through through the layers and to update the weights of a composition of simple functions. Um, and already in the late 1970s in the first half of the 1980s you already had. The idea of deep neural networks and they already started to appear. And by the second half of the 1980s, you already had convolutional networks. You already had recurrent networks. You didn't have Transformers yet that had wait, but you already had a lot of architectural ideas that Would actually be the iteration is still relevant and that if you could just scale them up, they would work quite amazing. You will actually so, if you take a network, say convolutional network is and then From the early 1990s from late 1980s and you just mechanical scale it up and you train it on Modern Hardware, on Modern data sets. It's gonna work pretty well. So of course, it will be burst and the networks we have today, of course, but if people had this kind of Results back on the nine, back in 1992, they would never be discouraged from neural networks. That would definitely be state of their back on the time. but unfortunately, neural networks require A certain scale to work so to speak, right? So if you have a very small neural network and the small data set, then probably the result will be worse. Then if you actually just think about the problem and do some more specialized model, For this problem. So, by the early 1990s, Since. People did not have the ability to scale up. They did not have the compute. They did not have the data. Basically the consensus, in the research Community was like this. Neural networks are the second best way of doing just about anything. So the place of neural networks was that there are very Universal you can do anything within your own network indeed, but it will be worse. Then if you just think about the specific problem, you have and create a model for this specific problem, So in the 1990s and there's the thousands neural networks were kind of Forgotten again. It was the Heyday of probabilistic models of graphical, probabilistic models, etc, etc. Very interesting still relevant very important, but out of scope for us. Ah and there were just a few groups who pushed and pushed on neural networks. There was an electron who was doing the image processing with cnns. There were Jeffrey hinton's group and Joshua benches group and they continued working. They continued believing in the neural networks and finally they were proved to be right. Okay, so the Deep learning Revolution happened in the middle of 2000 and 2006. 1,007 and I won't discuss in detail. What exactly was like there in Innovation because it's irrelevant by now it's it's it's absolute. But The specific. The technical Innovation. Wishes are still, of course, relevant was that they moved from CPUs to gpus. So again it's not much of an idea to notice that the stuff we're doing in your own network is easy to parallelize. Of course, it's easy to parallel. It's a huge number of neurons and not very deep computation, just like in the brain. But only in our Century only in the early 2000s. There was actually Hardwear widely available on the market gaming gpus that will actually implement this parallel process. So before that CPUs were still the best, we had, right? And as soon as gpus became good enough, People specifically the guys at hinton's group moved computations, to gpus that gave a boost of about another 10x 20x inefficiency. And that was enough that was enough to put neural networks from not working to work and starting from the late 2000s. Neural networks have been kind of revolutionizing one field of machine learning after not. Actually the first field was speech recognition. Speech processing. Deep, neural networks, had some very good surface and very good feature, extractors in the late in about 1010. So basically it was this original Deep neural networks patient and Benji that made Siri possible. Syria appeared in what found 11, I think the first version and it was, of course, would be impossible on classical speech, recognition, wouldn't work well enough to be useful Ah, and then, so we will not talk about speech recognition in this class, but we will talk definitely about image processing and the image recognition and computerization. So there the revolution happened around, 2011 to 2012 with alexnet, we will discuss how it's not in detail when we come to. and, let those and then everywhere, then with recurrent Networks, deep learning got into. Got into natural language processing. So by 2014-15, people were doing machine translation with neural networks and stuff like that. There's neural networks, and then in 2017, everything changed again, 2017, we had the Transformer and that transformed literally the whole industry. Again, we are still living in the age of Transformers, so to speak. So, I think I don't have time to go to bed props right now. This was a quick historical overview and It will will do the optimization part tomorrow. Any questions. Yep. So neural network but just I think I just didn't it. Sure was going on there. Yeah, sure. Yeah, sure, no problem. So suppose that I'm doing a neural network that is supposed to do classification. So at the output I want to have a lot of function like this and I want to have like a vector of probabilities for classes. Where do I get a vector of probabilities? Well. If I just do some neural layers, some Elementary functions and big compositions, I will not get a vector of need numbers from 0 to 1 that sum up to one, right? What I will get is a vector of scores That then will need to be converted to probabilities. By the softmax function, that's part one. But also, I mean, for some networks this will be the actual output and this may not happen. But usually, of course, it's still happens. So usually after like the main part of the neural network, what what it does is it extracts? Some kind of features from the input. and this features are a vector or a higher dimensional tensor doesn't matter at this point but it's it's A set of numbers. Let's say of safety. Right. And we want to convert it to a set of numbers of size case. That that's the only point that I was making here. So how can you do it? Well, for example, with just a linear transformation. So very often when neural networks look classification, very often like the last layer is actually just logistic regression. this is, Literally straightforward villages to regression. But not on the input, but on the features extracted by all the rest of the network and that's that's the very important difference. And probably I mean, linear regression. It's kind of uncommon to have many outputs so probably would be equal to one but not necessarily have several Just, you know, they were explained that before. And also want to say thank you for the lecturer. It was very interesting. Okay. It was very honestly, the prior like biasing Theory. Imagine that regularization is bios because I read a lot of information, I Was preparing for interview and I Literally couldn't find. I haven't seen that before. Well, if yeah, if If you looked for it, you should be able to find it because, of course, it's, it's like an in the foundation of the machine learning, but I'm really happy that you find it. Interesting. I'm always a little bit worried about this introductory part because, you know, some people just want to get to programming pytorch. But I think that foundations are important and I'm really happy that if you feel that way, Thank you. Thank you. All right. Thanks a lot guys. In general. You can. okay, previously, since this is you would use like measures like r-squared adjusted or like criterias, I don't remember like a formation criteria and some other measures that pioneers. Adding extra variables to the model. Yes, this was rich Russian and also doing this. Not quite so yeah, that there is a difference here. That is a little bit that made the little bit made them clear by my example, And I apologize for that, but it's still very instructive for example, so I still give it. But yes, that's a great question and there is an important difference. So when we talk of regularization We kind of have already fixed the model. So in the case of linear regression, I can have L2 regularizer. I can have one regularizer, I can have any kind of Prior over here, but the likelihood is already fixed. And what it means that the likelihood is fixed in particular. It means that the size of this Vector is also fixed. So when I change regularizers, I don't change the model structure, I don't change the number of parameters, it might look like that in my example, because as I went from between degrees of the polynomials, I was changing number of parameters. You're right. It was a little bit confusing in this regard, but regularization usually does not do that. Regularization deals with the values of this parameters. And the stuff that you mentioned and this are great keywords that are so talk about and in classes when I have time. But not in this class, we go to Japan. But things like okay, you can information Criterion. They buy Asian information criteria and stuff like that. They pertain to what is called Model selection. Right. And model selection basically, means I can model my data set and several different ways I can have linear regression, have code rates, regression cubic regression, local, gaussian regression, whatever, Ah, and then I need to choose between them. How do I choose between them? Well, What is what is this Choice? Like what am I trying to estimate? Its deceptively simple. I want to estimate. What is the likelihood? What is the probability of having model? Number k for my data set. and, How, where do I get this probability from? Well, of course, I get it from the best role. So of course, I get it from from something like this poem K times P of D given MK. Here. And notice that here. M is not a specific set of Weights. Here I am, is the whole model. So like one M could be like linear regression. And another M could be like, quadratic regression. So, it's a whole, the whole model, not specific weight. But still the best role is the same and it's still tells you well. Okay. If I don't have any reasons to prefer one model to another, then let's assume this is uniform and I just compare of given them, okay? Where is that P of T? Given MK and our formulas. Well, Let's go back to our Bistro. View of theta. Put more space here because I need P of theta. P of D. Given. Say sorry. P of D given Theta divided by P of d. And here P often these formula. As I wrote it we didn't have you know the contacts and the chance to go. This one metal level up but you can go one metal level up. They the formulas I wrote it was about one model like we are talking about linear regression and we are dealing with the parameters that obey this baby shower and you do in France from the parameters. So like everything happens in a model. Sorry, not the bar. Right. You can you can add the model. Here doesn't change the formula. It's still works. so, What do you compare the models by? How do you choose between quadratic and cubic features or between different versions of the model Etc? Well By this guy over here. The denominator. So this this is exactly this quantity. They denominator in the base rule. The normalizing constant. And everything that this information criteria do they are basically approximations to compute this. And then there is a lot of methods. It's very beautiful and interesting, approximation loads to say about it, but basically, it's an approximation to compute this So model selection is about trying to estimate this, normalizing constant, and choose the model with the largest normalizing constant. but in the model, then we will have a whole distribution of parameters and So there are two levels there is the level of selecting the model, and then inside the model, there is the level of actually learning the parameters. The answer question. Yeah, thank you. Okay, thanks guys. And see you tomorrow. Finally, for some actual neural networks. Bye.
