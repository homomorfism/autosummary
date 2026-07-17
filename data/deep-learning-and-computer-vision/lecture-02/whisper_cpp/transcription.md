# Transcript — whisper_cpp

- **Provider:** whisper_cpp
- **Language:** en
- **Audio duration:** 3:19:09
- **Segments:** 2003
- **model:** ggml-large-v3-turbo.bin
- **vad:** True
- **beam_size:** 5
- **entropy_thold:** 2.8
- **latency_sec:** 1239.1

## Segments

**[00:11 – 00:35]** Good morning, everyone. Welcome to the second day of our class. And I suppose, I hope the first day was interesting. Today we will definitely start deep learning, although I do have a few things to tell you before that. But then, at least in the second half, we'll definitely start talking about neural networks. No way around that.

**[00:39 – 01:00]** To get the technical organizational stuff out of the way, I sent a message to Google Classroom. I hope you've seen it. I made a web page, a secret web page, which probably we are not supposed to link to externally, but that's just for you.

**[01:00 – 01:13]** I made a web page with all class materials. I'll keep uploading videos, slides, words, etc. So I hope you like it.

**[01:13 – 01:37]** And with that, let's continue. Yesterday, we talked about the general idea of what learning is, of how we can formalize and understand what it means for, say, machine learning model to actually learn something.

**[01:37 – 02:03]** And we framed it in the probabilistic Bayesian framework. And basically, it was like most of yesterday's discussion was centered around the Bayesian rule, around this famous formula, which is the most important formula in the entire machine learning.

**[02:04 – 02:29]** But yesterday, we talked about a very simple example. We were just talking about the coin toss. And I actually want this introduction to go to the linear models, because they are very directly relevant to what we do in deep learning and to what neural networks actually do.

**[02:29 – 02:42]** So let me, apologies, but let me continue with this probabilistic introduction. Still, I hope it's important. Well, I'm sure it's important, but I hope it's interesting for you.

**[02:42 – 03:06]** So we discussed the base rule yesterday. And just as a quick reminder, the main idea of this formula is to answer the question of how should we update our beliefs when we learn new information, when we get new evidence.

**[03:06 – 03:27]** So in more general terms, D would be not specifically a data set for machine learning, but it would be just any kind of evidence. And theta would be like our beliefs, our hypotheses about the underlying process or whatever.

**[03:27 – 03:43]** And then when we get new evidence, we update what we believe. And that's in a way how life works. That's how our brains are supposed to work. Not always they work exactly in this way.

**[03:43 – 04:06]** And of course, we don't consciously do any calculations like this. But the general essence is exactly this. And we discussed three main problems of machine learning, where the optimization tasks come from.

**[04:06 – 04:19]** So you can start with the likelihood and end right there and just maximize the likelihood. That doesn't make any use of Bayesian inference, so it's a non-Bayesian method.

**[04:19 – 04:35]** But still, if you have lots of data or if your model is already very complicated and a prior distribution would make it completely infeasible, although I can't imagine why, still you can just maximize the likelihood.

**[04:35 – 04:52]** Then you can multiply the likelihood by the prior, we'll see very specific examples of that today in real-life models, not just the coin toss.

**[04:52 – 04:58]** And then maximize the result, which will be proportional to the posterior distribution.

**[04:58 – 05:00]** That's what we discussed last time.

**[05:00 – 05:04]** And we discussed the coin tossing example in great detail.

**[05:04 – 05:10]** And the third problem would be the predictive distribution, which I don't think we'll get to today.

**[05:10 – 05:14]** So let that stay at the level of the coin tossing.

**[05:14 – 05:19]** And we discussed the coin tossing example in great detail yesterday.

**[05:19 – 05:28]** So we kind of went through all of these problems, went through the notions of likelihood, prior, posterior,

**[05:28 – 05:36]** what it all means, completely finished the simplest case of a uniform prior,

**[05:36 – 05:42]** and then discussed what a more informative, more reasonable prior would be.

**[05:42 – 05:46]** Like if I do want to have a bell-shaped curve, then how do I choose among them?

**[05:46 – 05:49]** And the answer was, well, choose the one that's convenient,

**[05:49 – 05:53]** which may sound like an unsatisfactory answer, but there you go.

**[05:53 – 05:58]** It's our choice, it's about our beliefs.

**[05:58 – 06:08]** So actually in more involved cases like linear regression that we will discuss now,

**[06:08 – 06:10]** the reasoning is exactly the same.

**[06:10 – 06:15]** You choose the prior not due to some principled reason,

**[06:15 – 06:20]** like you understand that for this process the prior should be this,

**[06:20 – 06:28]** but you choose your prior either for convenience or because it leads to desirable properties.

**[06:28 – 06:31]** We will see how it works.

**[06:31 – 06:42]** And another thing that I wanted to mention here,

**[06:42 – 06:46]** I will not spend much time on real-world examples or anything,

**[06:46 – 06:53]** but I do want to mention some kind of philosophical underpinning of all this.

**[06:53 – 06:59]** And I mentioned yesterday that if you open an old book on probability theory,

**[06:59 – 07:02]** a very good book, but an old book on probability theory,

**[07:02 – 07:06]** you will see probability introduced like,

**[07:06 – 07:10]** well, there is this infinitely repeatable experiment,

**[07:10 – 07:13]** we do the experiment, we get some results,

**[07:13 – 07:15]** and then we divide the results,

**[07:15 – 07:19]** the number of outcomes that we are interested in by the number of total experiments,

**[07:19 – 07:22]** and that ratio tends to the probability.

**[07:22 – 07:25]** That is completely correct.

**[07:25 – 07:28]** When it's applicable, it's completely correct.

**[07:28 – 07:32]** And for the coin toss, it's exactly how we define probability.

**[07:32 – 07:38]** But in real life, and especially in machine learning,

**[07:38 – 07:40]** that's why I'm talking about this,

**[07:40 – 07:45]** we usually want to reason about the probability of events

**[07:45 – 07:49]** that are definitely not repeatable experiments, right?

**[07:49 – 07:55]** So, for example, if you're a bookmaker, you need to predict the probability,

**[07:55 – 08:00]** to set the probability of, say, Spain winning the FIFA World Cup this year.

**[08:00 – 08:05]** And there will be only one World Cup.

**[08:05 – 08:09]** And no, it's not a repeatable experiment based on previous World Cups,

**[08:09 – 08:12]** because obviously the teams were completely different,

**[08:12 – 08:14]** everything was completely different.

**[08:14 – 08:20]** Or we even might want to set probabilities for events

**[08:20 – 08:23]** that already happened, that are already set,

**[08:23 – 08:26]** but we just don't know the answer.

**[08:26 – 08:30]** And in these kind of cases,

**[08:30 – 08:35]** it makes no sense to talk about experiments repeated to infinity, right?

**[08:35 – 08:38]** For example, there is a hypothesis,

**[08:38 – 08:40]** I'm not sure about the current status,

**[08:40 – 08:42]** but once time I checked it was a hypothesis,

**[08:42 – 08:47]** that the Odyssey by Homer was not written by the same Homer as the Iliad,

**[08:47 – 08:53]** was written by a woman due to some lexicographic analysis of the text.

**[08:53 – 08:55]** And it's a hypothesis, we don't know,

**[08:55 – 09:02]** but it makes sense for us to want to assign probabilities to hypotheses like this, right?

**[09:02 – 09:04]** Although there is only one Odyssey,

**[09:04 – 09:08]** and it was written by somebody thousands of years ago,

**[09:08 – 09:13]** and the answer is already set, but we just don't know it.

**[09:13 – 09:18]** So the point is, in real life,

**[09:18 – 09:23]** probabilities are often not limits of ratios of experiments,

**[09:23 – 09:26]** but they are degrees of belief.

**[09:26 – 09:30]** They are representations of our uncertainty.

**[09:30 – 09:34]** And this is actually a very useful, I think, framing

**[09:34 – 09:36]** to think about probability,

**[09:36 – 09:43]** and a very useful way to understand what we are doing.

**[09:43 – 09:45]** We are not actually...

**[09:45 – 09:48]** When we do machine learning, for example,

**[09:48 – 09:52]** when we use this with a real dataset and a real model,

**[09:52 – 10:01]** we are not getting some kind of logical conclusion, right?

**[10:01 – 10:05]** We are updating our beliefs,

**[10:05 – 10:09]** and if we have a good dataset, a large enough dataset,

**[10:09 – 10:14]** then our beliefs can become much more certain.

**[10:14 – 10:20]** We can become... I don't know, the confidence intervals may shrink.

**[10:20 – 10:25]** We can become more sure in the hypothesis that we are evaluating,

**[10:25 – 10:29]** but we will never be completely sure, right?

**[10:29 – 10:35]** Especially in machine learning when it's all about noisy datasets.

**[10:35 – 10:42]** The thing is, we are combining all of this evidence

**[10:42 – 10:46]** to understand something about the model, model parameters in this case,

**[10:46 – 10:50]** but the result is always a probability distribution.

**[10:50 – 10:55]** And this is a point that often gets lost for people,

**[10:55 – 11:02]** because what you actually do in reality, and let me maybe immediately,

**[11:02 – 11:05]** so that you understand in advance where we are driving with this,

**[11:05 – 11:13]** let me maybe immediately get you the general notion of what we are doing today.

**[11:13 – 11:22]** So we are using this identity, and we are reasoning by the base rule,

**[11:22 – 11:27]** but what we are actually doing, for example, in deep learning practice all the time,

**[11:27 – 11:32]** is we compose a loss function, right?

**[11:32 – 11:42]** So we compose a loss function like log p of d given theta plus log p of theta,

**[11:42 – 11:48]** and actually we take a minus because the loss function you want to minimize, not maximize.

**[11:48 – 11:54]** But in practice, this is the loss function for your neural network, right?

**[11:54 – 11:56]** We'll see how it works specifically today.

**[11:56 – 12:02]** And then you minimize it with respect to theta, with respect to the neural network parameters,

**[12:02 – 12:05]** and you get theta MAP, right?

**[12:05 – 12:14]** So theta MAP is the argmin of this, the maximum posterior hypothesis, right?

**[12:14 – 12:19]** So it's the argmax of p of theta given d.

**[12:19 – 12:24]** And very often people, when they think about deep learning about neural networks,

**[12:24 – 12:30]** they kind of stop here and the process does stop here.

**[12:30 – 12:33]** And then they say, oh, now we know theta.

**[12:33 – 12:38]** Now we got our model checkpoint. Here are the weights. Here are the true weights.

**[12:38 – 12:43]** That is an oversimplification, right?

**[12:43 – 12:50]** So yes, in practice, very often we will do exactly this and we will use theta as a point estimate.

**[12:50 – 12:57]** But it's very helpful to remember that theta MAP is just a point estimate.

**[12:57 – 13:04]** It's just the maximum of a whole distribution.

**[13:04 – 13:09]** And in deep learning with huge neural networks, etc., we usually cannot do that.

**[13:09 – 13:18]** But if we could, it would be very helpful usually to actually at least sample several different points from this distribution

**[13:18 – 13:22]** and see how that translates into different predictions.

**[13:22 – 13:29]** And actually, sometimes you see this in deep learning as well.

**[13:29 – 13:34]** So all of this machinery is about degrees of belief.

**[13:34 – 13:41]** It's about our uncertainty, our original uncertainty captured in P of Theta

**[13:41 – 13:46]** and then reduced by D, by the data that we get.

**[13:46 – 13:54]** And ultimately, our new uncertainty captured in P of Theta given D, right?

**[13:54 – 13:57]** So we know something about the parameters.

**[13:57 – 13:59]** It cannot be that we know absolutely nothing.

**[13:59 – 14:03]** Well, sometimes it can, but still we need to express it in a distribution.

**[14:03 – 14:08]** Then we get new information, we update,

**[14:08 – 14:10]** and we have some new belief about Theta.

**[14:10 – 14:12]** But it's a distribution.

**[14:12 – 14:14]** It's an uncertain belief.

**[14:14 – 14:17]** It's never just a single point.

**[14:17 – 14:21]** This is what I wanted to say here.

**[14:21 – 14:31]** And also, I usually go through some relatively straightforward examples

**[14:31 – 14:33]** of applying the base rule.

**[14:33 – 14:36]** Let's try it with you.

**[14:36 – 14:43]** So here is a very standard trick question from probability theory.

**[14:43 – 14:45]** A person has two kids.

**[14:45 – 14:49]** Let's say my acquaintance has two kids, but I've never met them.

**[14:49 – 14:52]** I don't know their names. I don't know their genders.

**[14:52 – 14:57]** And let's assume that every baby is either a boy or a girl

**[14:57 – 15:03]** with probabilities one half and the first baby is independent from the second.

**[15:03 – 15:05]** So they are just there.

**[15:05 – 15:09]** Each of them is a fair coin to us in terms of whether it's a boy or a girl.

**[15:09 – 15:16]** And then I go to this person and I ask, hey, do you have any boys?

**[15:16 – 15:19]** Like among the two children that you have, are there any boys?

**[15:19 – 15:21]** And he says, yes.

**[15:21 – 15:34]** In this setting, what is the probability that he has a girl?

**[15:34 – 15:37]** How many?

**[15:37 – 15:39]** How did he arrive in this?

**[15:39 – 15:54]** Well, we know that he had at least one voice, one slot available, that can be either one or the other.

**[15:54 – 15:59]** Not quite.

**[15:59 – 16:01]** Any other ideas?

**[16:01 – 16:07]** So what's the probability space here?

**[16:07 – 16:09]** Like what are the possible outcomes?

**[16:09 – 16:17]** Also not quite true.

**[16:17 – 16:24]** Okay.

**[16:24 – 16:31]** Yeah, this is a straightforward trick question, but yeah, it would usually fall into the trick unless you know it.

**[16:31 – 16:36]** So, the person has two children, right?

**[16:37 – 16:41]** So, it's like child number one and child number two, right?

**[16:41 – 16:45]** For every child, there are two possibilities, two options, right?

**[16:46 – 16:47]** So, how many options are in total?

**[16:50 – 16:53]** Four, exactly.

**[16:53 – 17:02]** So, we have like boy, boy, boy, girl, girl, boy, and girl, girl, right?

**[17:02 – 17:03]** So, there are four possibilities.

**[17:03 – 17:09]** And in the prior, before I get any information, they're completely equal, right?

**[17:09 – 17:15]** So, we get one-fourth for this, one-fourth for this, one-fourth for this, right?

**[17:15 – 17:19]** So, now when I ask, do you have any boys?

**[17:19 – 17:20]** And he answers yes.

**[17:20 – 17:22]** What information do I get?

**[17:23 – 17:24]** How does this table change?

**[17:31 – 17:32]** Yeah, precisely.

**[17:32 – 17:40]** So, now the last line cannot happen, but the rest all can happen.

**[17:40 – 17:43]** And the answer yes does not distinguish between them, right?

**[17:44 – 17:50]** So, as a result, I now have three options.

**[17:51 – 18:00]** They are still equal in probability, but now I have three options and two of them have a girl, right?

**[18:00 – 18:03]** So, the probability is actually two-thirds.

**[18:04 – 18:17]** And if you want it formally, then you just need to compute P of, you know, there is a girl given that there is a boy, right?

**[18:17 – 18:36]** So, it's like the probability of these two scenarios, MF or FM, divided by the total probability of that there is a boy of M, M, MF or FM, and that comes to two-thirds, right?

**[18:36 – 18:44]** So, formally, it's like two quarters divided by three quarters, if you go strictly by definition.

**[18:46 – 18:50]** All right, but here is the second question.

**[18:50 – 18:57]** Now, I've met one of his kids, so it's a separate question, I didn't ask the first one, so I don't know that.

**[18:59 – 19:12]** And now I've met one of his kids, and it's a boy, so now I know that one of the kids is a boy, and I've met this boy.

**[19:12 – 19:15]** What is the probability that the other one is a girl?

**[19:16 – 19:19]** Yeah, and now it's one half, right?

**[19:19 – 19:34]** So now, when I meet one of his children, then it means that now, okay, it doesn't matter if it's number one or number two, but it means that I kind of fix the value of one of these columns.

**[19:34 – 19:39]** So now, I eliminate not one, but two lines.

**[19:39 – 19:46]** For example, number one is a boy, which means that now only two outcomes remain, and they are equal, etc., etc.

**[19:48 – 19:57]** So, this is an easy trick question, but it already shows how in probability theory and in Bayesian reasoning like this,

**[19:58 – 20:04]** notice that although we didn't really use the Bayes' theorem, it's actually the same kind of reasoning.

**[20:04 – 20:11]** We get some prior beliefs that everything is equiprobable, that's our original assumptions,

**[20:11 – 20:17]** and then we get evidence, and then we update our beliefs based on this evidence, right?

**[20:18 – 20:28]** But there are also a couple of more interesting examples, so let's discuss them with you too, since the first one, I think, went well.

**[20:29 – 20:39]** These are, again, very well-known policies, you may have heard about them, but they are very instructive in the pitfalls, potential pitfalls of the Bayes' rule.

**[20:41 – 20:48]** Here is the setting. A murder has happened, and we are in a court of law arguing about the murder.

**[20:48 – 20:58]** So there is some blood left on the crime scene, and we know 100%, so don't think about that assumption.

**[20:58 – 21:01]** We know for certain that this is the killer's blood, okay?

**[21:01 – 21:04]** So this is with probability one, you don't need to question that.

**[21:06 – 21:09]** And it so happens that the blood type is quite rare.

**[21:10 – 21:17]** Like, let's assume it was a time before DNA tests, so we cannot directly check which person it is,

**[21:17 – 21:25]** but it's a rare blood type, and only 1% of the population, only 1% of people actually have this blood type.

**[21:26 – 21:37]** And it just so happens that the defendant, the guy who is being accused of the murder, also has this blood type, right?

**[21:37 – 21:46]** So the prosecutor comes out and says, well, the chance that the defendant would have this blood type if he was innocent is only 1%,

**[21:46 – 21:50]** so with probability 99% he is guilty.

**[21:50 – 21:54]** Is the prosecutor correct in this?

**[21:55 – 22:01]** I suppose the question on the slide already tells you that he is not, but what's the mistake?

**[22:02 – 22:04]** What's the problem with this kind of reason?

**[22:27 – 22:38]** I think it's the specific way how the statement has been proposed to you, maybe?

**[22:39 – 22:49]** Is it equating the probability of having the blood type given innocence versus probability of actually being innocent given the blood type, something there?

**[22:49 – 22:52]** Exactly. You nailed it. Exactly.

**[22:53 – 22:58]** So this is a classic mistake that happens all the time in real life.

**[22:58 – 23:07]** You see people making it all the time because our brains are not really wired by evolution to do probabilistic reasoning, especially with numbers.

**[23:08 – 23:12]** And yes, your answer was completely entirely correct.

**[23:12 – 23:13]** Let me repeat it for everyone.

**[23:13 – 23:21]** And so we have, so what are we actually trying to do in the court of law?

**[23:21 – 23:28]** We are trying to establish like P of guilty given the evidence, right?

**[23:28 – 23:31]** And if it's very, very high, then we convict, right?

**[23:32 – 23:36]** It's probably never going to be exactly one, but if it's very high, then we convict the person.

**[23:37 – 23:43]** And so the prosecutor makes a conclusion exactly about this.

**[23:43 – 23:54]** So his final point, the 99%, is about P of guilty, given the blood type, right?

**[23:54 – 24:01]** But what he starts with is not P of innocent, given the blood type.

**[24:02 – 24:03]** It's the other way around.

**[24:04 – 24:11]** It's P of blood type, given that the person is innocent, right?

**[24:12 – 24:19]** And yeah, so when the prosecutor estimates this probability, he is completely correct, right?

**[24:19 – 24:23]** So like one, it doesn't matter, like almost everyone is innocent, so we can say that this

**[24:23 – 24:24]** is also 1%, that's fine.

**[24:26 – 24:32]** But then the prosecutor says, well, all right, so this equals to 1 minus this.

**[24:32 – 24:36]** And now this conclusion is completely wrong, of course, right?

**[24:36 – 24:47]** So the prosecutor equates like P of A given B with P of B given A, in a way.

**[24:47 – 24:49]** And that is, of course, not right.

**[24:49 – 24:51]** When I write it like this, it's obvious that it's wrong.

**[24:51 – 24:58]** But when it's stated in words, people miss this kind of mistakes all the time.

**[24:59 – 25:02]** And what would be the actual formula?

**[25:02 – 25:04]** Of course, it would be the bias rule, right?

**[25:04 – 25:09]** So in actuality, like P of blood...

**[25:09 – 25:11]** Okay, let's do it the other way around.

**[25:11 – 25:21]** P of innocent given blood would be like P of blood given innocent times P of innocent

**[25:22 – 25:25]** divided by P of blood, right?

**[25:25 – 25:34]** And of course, this prior and this evidence probability could completely change things.

**[25:34 – 25:38]** So I'm not going to try to invent any numbers.

**[25:38 – 25:39]** It doesn't make sense for this example.

**[25:40 – 25:46]** But for example, suppose that there are two possible suspects.

**[25:47 – 25:51]** And it just so happens that both of them have this blood type, right?

**[25:52 – 25:56]** If that happens, then of course the blood type tells us nothing, right?

**[25:57 – 26:00]** It does not help us distinguish between them and the probability remains to be one half.

**[26:01 – 26:10]** But the prosecutor's reasoning would not change in this case.

**[26:10 – 26:21]** So the prosecutor would now make the obviously absurd conclusion that both of the suspects are guilty, each with probability 99%, which is of course wrong.

**[26:23 – 26:27]** Okay, so this is the prosecutor's mistake.

**[26:28 – 26:33]** And then the defense attorney comes out and comes on the, what's the word?

**[26:34 – 26:34]** On the stand, yeah.

**[26:35 – 26:40]** And the defense attorney says, well, okay, so first he explains what the mistake of the prosecutor was.

**[26:40 – 26:44]** And then he says, well, okay, let me offer you my own calculation.

**[26:44 – 26:46]** There are a million people living in this city.

**[26:46 – 26:55]** And yeah, of course, having this rare blood type narrows it down from a million to only about 10,000.

**[26:55 – 26:58]** And that is correct.

**[26:58 – 27:06]** So all that the blood type tells us is that the defendant is guilty with probability like 0.01%.

**[27:07 – 27:11]** So yeah, sure, it's kind of evidence, but it's very, very weak evidence, right?

**[27:12 – 27:14]** It's definitely not any kind of proof.

**[27:14 – 27:17]** Let's just not admit it to evidence at all.

**[27:19 – 27:21]** This also doesn't sound right, right?

**[27:21 – 27:24]** So what's the defense attorney's mistake?

**[27:38 – 27:43]** The blood type is equally likely to be the killer, so basically not even focusing on

**[27:43 – 27:45]** why the defendant is there in the first place.

**[27:45 – 27:46]** Yeah, exactly.

**[27:46 – 27:51]** So in this case, it's not really some deep mistaken probabilistic reasoning.

**[27:51 – 27:54]** It's just the mistaken assumption, right?

**[27:55 – 28:02]** So yeah, it would be true what he says if every one of these 10,000 people, including, I don't

**[28:02 – 28:09]** know, people who are sleeping at the time and babies and everybody in the city would actually

**[28:09 – 28:11]** have an equal chance of committing this murder.

**[28:11 – 28:15]** But that's obviously not true in real life, so the defendant is there for some reason.

**[28:16 – 28:17]** Yeah, so yes, you're completely right.

**[28:18 – 28:24]** And yeah, and these kinds of mistakes happen all the time.

**[28:25 – 28:31]** And there was a very famous case, which you might have heard about, the case of O.J.

**[28:31 – 28:32]** Simpson.

**[28:32 – 28:39]** He was a very successful football player, American football player, in the 1980s.

**[28:39 – 28:47]** And then he had some very difficult relationships, so to speak, with his wife.

**[28:48 – 28:50]** And ultimately, the wife was found to be killed.

**[28:52 – 28:54]** And O.J. Simpson was tried for murder.

**[28:55 – 29:00]** It was one of the most publicized trials of the 1990s.

**[29:01 – 29:04]** And it was a long trial.

**[29:04 – 29:07]** There were lots of evidence, lots of discussions.

**[29:07 – 29:08]** We will not go into that.

**[29:08 – 29:14]** But there was one specific point that exactly matches our discussion on the bias troll.

**[29:15 – 29:26]** And at some point, the evidence was that O.J. Simpson already had a history of violence with his wife.

**[29:26 – 29:29]** So basically, he beat her up a few times before.

**[29:30 – 29:36]** And the prosecutors, they proved this.

**[29:36 – 29:37]** This was true.

**[29:38 – 29:44]** And they kind of submitted it to the jury as not direct proof, of course, but as evidence

**[29:44 – 29:52]** that O.J. Simpson can actually go too far in another episode and the wife can get killed.

**[29:54 – 30:04]** So the attorney came out and said, well, okay, my client is a very bad person.

**[30:04 – 30:05]** I do not dispute that.

**[30:06 – 30:11]** It's very bad to beat up your wife, and definitely he shouldn't be doing that.

**[30:12 – 30:18]** But we are at a murder trial, and as for the murders, there is a statistic that says,

**[30:18 – 30:25]** well, only one of 2,500 women subject to domestic violence actually get killed.

**[30:27 – 30:31]** And he concluded that this is irrelevant for the murder, right?

**[30:33 – 30:40]** So, and what, I mean, it's, of course, it's the defense attorney's job to make arguments

**[30:40 – 30:42]** like this, even if they're obviously wrong.

**[30:43 – 30:48]** But what's really interesting about this is that the court actually agreed.

**[30:49 – 30:56]** So the court in this very famous, very public O.J. Simpson's case agreed that this is a good

**[30:56 – 30:59]** reason to say that domestic violence has no relevance to the murderer.

**[30:59 – 31:04]** And, you know, like they do it, the jury was instructed to disregard this evidence, blah,

**[31:04 – 31:04]** blah, blah.

**[31:06 – 31:11]** But of course, this is exactly the same kind of mistake, right?

**[31:11 – 31:22]** So, in reality, what they were supposed to be evaluating was P...

**[31:22 – 31:24]** Okay, so let me start with the statistic.

**[31:24 – 31:32]** The statistic was, what is the probability of murdered given the history of violence?

**[31:33 – 31:35]** And, okay, the statistic was correct.

**[31:35 – 31:38]** So that was like 1 over 2,500, that's true.

**[31:38 – 31:48]** But that's completely not what people were trying to establish, right?

**[31:48 – 31:58]** So this kind of statistic starts from the point in time when nobody is murdered, right?

**[31:58 – 32:04]** It starts from the point where everybody is alive and well,

**[32:04 – 32:07]** and then evaluates how likely it is to be murdered.

**[32:07 – 32:14]** But a court case, a murder case, argues in the opposite direction, right?

**[32:14 – 32:23]** So what we actually want to know is what is the probability of being murdered by your husband?

**[32:24 – 32:31]** Sorry about this gory topic, but this is still the most famous case of this policy.

**[32:31 – 32:40]** Given that the murder has already happened and there was a history of domestic violence, right?

**[32:40 – 32:46]** So, of course, the main thing is that the murder has already happened and we are just trying to establish who did it.

**[32:47 – 32:54]** So the vast majority of these cases, of these 25,000 cases, in the vast majority of them, nobody got murdered.

**[32:54 – 32:56]** So they don't matter, right?

**[32:56 – 33:00]** They are not included into this conditional probability.

**[33:02 – 33:06]** And if you actually take the exact same statistics, here is the punchline.

**[33:06 – 33:20]** If you actually take the exact same statistics that was available at the time, and you compute the correct probability from it, you estimate the correct probability, it will come, I may be slightly mistaken, but it will come to something like 7 over 8.

**[33:21 – 33:32]** So, like, among the women who were murdered with a history of domestic violence, in the vast majority of cases, the husband did it.

**[33:35 – 33:41]** So, of course, if evidence was presented in the correct way, it would look completely different, right?

**[33:41 – 33:56]** So, this is just an illustration that people do make mistakes like this, and it's probably just a good habit in life to actually understand what exactly you're trying to estimate.

**[33:57 – 34:05]** What is, I mean, in life, all that we do, like, everything that we do to make decisions is estimate various conditional probabilities.

**[34:05 – 34:09]** Like, if I do this, what is the probability of my preferred outcome?

**[34:10 – 34:15]** And if I do that, what is the risk of this and that?

**[34:16 – 34:29]** And it's a good habit to actually explicitly understand what exactly is the probability that you're evaluating, even if you cannot really evaluate it, right?

**[34:29 – 34:32]** So in real life, we don't have this kind of statistics.

**[34:32 – 34:34]** We can't run the numbers, of course.

**[34:34 – 34:49]** But if you at least qualitatively understand what is the direction that you are trying to predict, what is on the left of the vertical bar and what is on the right of the vertical bar, things become more clear in many cases.

**[34:52 – 34:56]** Okay, so that was the leftover that I wanted to mention.

**[34:57 – 35:03]** And now we proceed to our first real example.

**[35:03 – 35:07]** And now I will make two examples today, linear regression and logistic regression.

**[35:07 – 35:18]** We will not discuss them in too many details, but I do want to discuss them because they are directly relevant to what's happening in neural networks.

**[35:18 – 35:26]** That's like the simplest possible neural network is a linear model like this, a neural network consisting of one perceptron.

**[35:27 – 35:33]** And it's not only that, you know, it's the simplest model and modern neural networks are completely different.

**[35:33 – 35:37]** No, linear regression and logistic regression are still directly relevant to what's happening in them.

**[35:37 – 35:38]** I will explain why.

**[35:39 – 35:49]** So I hope that you all have some kind of intuition about what linear regression is.

**[35:49 – 35:52]** Maybe you don't, maybe you can't remember the formulas, that's fine.

**[35:52 – 35:56]** Maybe you don't, I don't know, maybe you never studied it like systematically.

**[35:57 – 36:02]** But this will be our point number two, linear regression.

**[36:04 – 36:13]** But at least you have this, you know, general picture in your mind that a linear regression is a problem like this.

**[36:13 – 36:18]** You have x over here, you have the target variable y over here.

**[36:18 – 36:21]** There are some data points like this.

**[36:22 – 36:23]** And you make an assumption.

**[36:24 – 36:30]** You say the data points are probably in a linear dependence between x and y.

**[36:31 – 36:35]** But we don't know the dependence and there is noise.

**[36:35 – 36:38]** So they are not exactly on the same straight line.

**[36:38 – 36:41]** They are close to a straight line, right?

**[36:42 – 36:46]** And the problem of linear regression is to find the straight line.

**[36:47 – 36:53]** Basically, this is the intuition that I hope you all understand.

**[36:55 – 37:01]** So if I write it down as a formula, I mean, obviously, I can only draw you two-dimensional pictures.

**[37:02 – 37:04]** So x will be one-dimensional in what I draw.

**[37:04 – 37:11]** But in reality, of course, we are usually talking about a single y.

**[37:11 – 37:15]** So the target variable is a number, more or less always.

**[37:15 – 37:25]** But this number is not just w0 plus w1 times x, but there are many x's, right?

**[37:25 – 37:36]** So in reality, x is a vector, usually, and we model y as a linear combination of x's.

**[37:38 – 37:43]** Okay, so before I even begin talking about it in detail,

**[37:43 – 37:49]** one very simple remark that will help us make things easier.

**[37:49 – 37:55]** I will actually skip the intercept.

**[37:55 – 38:00]** So I will actually write y as just w times x,

**[38:00 – 38:04]** and this means transposition, and this means just the scalar,

**[38:04 – 38:07]** the dot product of the vectors w and x.

**[38:07 – 38:15]** So like w1, wd times x1, xd.

**[38:15 – 38:18]** Why can't I skip the intercept?

**[38:18 – 38:22]** Why can't I forget about w0?

**[38:22 – 38:24]** In practice, it's not zero, right?

**[38:24 – 38:25]** Here it's not zero.

**[38:27 – 38:39]** Yeah, precisely.

**[38:39 – 38:41]** Okay, it's good that you know all this stuff.

**[38:44 – 38:47]** To be able to skip the intercept,

**[38:47 – 38:48]** I just add one more dimension.

**[38:48 – 38:50]** I add a fictional dimension.

**[38:51 – 38:54]** Let's say x0 is just one, like you said.

**[38:54 – 38:57]** It's a new feature, a constant feature,

**[38:57 – 39:02]** and then I take my vector x and I map it to one and then x,

**[39:02 – 39:06]** like a vector which is one dimension longer.

**[39:08 – 39:15]** And now, suddenly, when I do a linear function,

**[39:15 – 39:18]** when I do a direct dot product in this vector,

**[39:18 – 39:21]** I get the intercept for free.

**[39:22 – 39:24]** So this is a standard trick.

**[39:24 – 39:30]** That's why we don't need to always add this w0 here,

**[39:30 – 39:33]** which would make the formulas much more...

**[39:33 – 39:34]** Well, it wouldn't make it more complicated,

**[39:34 – 39:36]** but it would make it much more cumbersome.

**[39:39 – 39:46]** Okay, so y should be similar to a linear function of x's.

**[39:46 – 39:49]** And maybe you know...

**[39:49 – 39:52]** I mean, again, if you ever studied any linear regression,

**[39:52 – 39:54]** you probably have an idea.

**[39:54 – 39:58]** How do we define this being near to?

**[39:58 – 40:05]** What do we mean by this approximation?

**[40:07 – 40:08]** What are we actually...

**[40:08 – 40:15]** How do we formalize linear regression use?

**[40:15 – 40:20]** You minimize the, in general, measure of patterns

**[40:20 – 40:25]** between the actual values and prediction of regression.

**[40:25 – 40:30]** Yeah, and what is the most common error?

**[40:30 – 40:33]** Patterns squared.

**[40:33 – 40:35]** Yeah, yeah, exactly.

**[40:35 – 40:38]** So the standard way to do linear regression,

**[40:38 – 40:40]** and again, notice I haven't yet written any probabilities,

**[40:40 – 40:43]** we'll get there, is...

**[40:43 – 40:47]** Okay, so what does it mean that I want W to be

**[40:47 – 40:51]** such that Y is approximated by W times X?

**[40:51 – 40:55]** It means that my predictions...

**[40:55 – 40:57]** So here are the axes, right?

**[40:57 – 41:01]** The axes in the dataset.

**[41:01 – 41:07]** And my predictions in this axis

**[41:07 – 41:10]** are points on this straight line, right?

**[41:10 – 41:13]** So this is what my model predicts.

**[41:13 – 41:17]** This is W times XN over here.

**[41:17 – 41:22]** And what does it mean that the straight line is closed?

**[41:22 – 41:25]** It means that these distances are small, right?

**[41:25 – 41:31]** It means that I want the total sum of these distances

**[41:31 – 41:33]** to be as small as possible.

**[41:33 – 41:34]** Makes sense.

**[41:34 – 41:39]** And usually, like you said,

**[41:39 – 41:44]** the loss function in linear regression is defined.

**[41:44 – 41:46]** So I said that I want the distances to be small,

**[41:46 – 41:49]** but I didn't yet define what exactly,

**[41:49 – 41:52]** what is the exact number that I want to be small.

**[41:52 – 41:54]** And usually it's exactly the square distance, right?

**[41:54 – 42:04]** So usually it's the sum of Y minus Yn minus W times Xn squared.

**[42:04 – 42:08]** And standard linear regression minimizes this with respect to W, right?

**[42:08 – 42:12]** Well, here is a question.

**[42:12 – 42:16]** Why? Where does this come from?

**[42:16 – 42:23]** If you know, you can speak up and tell, or if you have an idea why.

**[42:23 – 42:29]** So obviously I do want these distances to be as small as possible.

**[42:29 – 42:31]** That's right.

**[42:31 – 42:36]** Obviously, I cannot just add up distances as they are

**[42:36 – 42:38]** because they have signs, right?

**[42:38 – 42:41]** So I do want this to be symmetric.

**[42:41 – 42:47]** I don't want the straight line to go just to positive infinity

**[42:47 – 42:51]** because then everything will have negative infinite errors, right?

**[42:51 – 42:53]** So I do want it to be symmetric.

**[42:53 – 42:56]** So that's part of the job that the square is doing, sure.

**[42:56 – 43:03]** But the same job could be done by a million other ways, in a million other ways, right?

**[43:03 – 43:09]** I could have said, okay, why don't I add up the absolute values of this errors?

**[43:09 – 43:15]** Why don't I add up these values to degree four?

**[43:15 – 43:21]** Why don't I add up e to the power of the absolute value of this?

**[43:21 – 43:28]** And I mean, there are a million, there are infinitely many monotone functions

**[43:28 – 43:31]** that are symmetric and monotone in the distance.

**[43:31 – 43:36]** And if I actually start minimizing all of these things,

**[43:36 – 43:39]** I will get different results, right?

**[43:39 – 43:41]** The w will be different.

**[43:43 – 43:47]** So why do people choose squares so often?

**[43:47 – 43:51]** Why is it the most common loss function?

**[43:51 – 43:57]** I think it's because of the fulfillment of the Goffman computer, maybe?

**[43:57 – 43:59]** Like the blue property?

**[43:59 – 44:00]** Exactly.

**[44:00 – 44:04]** Okay, so I see that you already have the background for this,

**[44:04 – 44:05]** so I'll make it quick.

**[44:09 – 44:13]** If everybody has the same answer, we can just skip it.

**[44:13 – 44:18]** If you want to hear it, then I can explain.

**[44:22 – 44:25]** The reason for this, the reason for the square,

**[44:25 – 44:28]** actually comes from the probabilistic assumptions that we're making.

**[44:28 – 44:34]** And let's frame linear regression as a machine learning model

**[44:34 – 44:36]** in the sense that we are developing, right?

**[44:36 – 44:41]** So in this case, theta is the W, of course.

**[44:41 – 44:45]** So the model parameters are the weights, that's clear.

**[44:46 – 44:51]** Data are the Xs and Ys, that's also pretty clear.

**[44:53 – 44:58]** But how do we define the likelihood?

**[44:58 – 45:01]** So to define the model, we need to define the likelihood.

**[45:01 – 45:07]** The likelihood is P of D given theta, right?

**[45:07 – 45:11]** The first thing that we do is we make the same assumption

**[45:11 – 45:12]** that we make always in machine learning,

**[45:12 – 45:16]** that keeps true throughout all of the machine learning models.

**[45:17 – 45:22]** We say that all of the data points are conditionally independent.

**[45:23 – 45:25]** Sorry, not X, Y.

**[45:25 – 45:30]** Are conditionally independent given the parameters, right?

**[45:30 – 45:31]** Sorry, it should be W too.

**[45:34 – 45:38]** And also, since we are doing supervised learning,

**[45:38 – 45:40]** we always have an X.

**[45:40 – 45:42]** And the X, we are not modeling the X.

**[45:42 – 45:43]** We are only modeling the Y, right?

**[45:43 – 45:47]** So the X always goes on the right-hand side here.

**[45:47 – 45:50]** So this is what supervised learning actually means.

**[45:50 – 45:52]** It means that we have an input that goes here.

**[45:52 – 45:57]** And then we are modeling the output that goes here.

**[45:57 – 46:01]** Okay, so this part is straightforward.

**[46:01 – 46:03]** This is our first assumption.

**[46:03 – 46:05]** We always make it.

**[46:05 – 46:06]** But then comes the interesting part.

**[46:06 – 46:11]** So what is this distribution here?

**[46:11 – 46:16]** It's actually the distribution of the points that we see

**[46:16 – 46:20]** given our model and the x where we measure.

**[46:20 – 46:24]** So for example, at x3,

**[46:24 – 46:28]** we have our model predicting this point.

**[46:28 – 46:32]** But what we need to define is not just a single point.

**[46:32 – 46:35]** So our second assumption will be linearity.

**[46:35 – 46:40]** Our second assumption will be that the most probable point,

**[46:40 – 46:45]** the center of this distribution, is, in fact, w times x.

**[46:45 – 46:48]** But to actually do learning,

**[46:48 – 46:53]** we have to define a whole distribution around this point.

**[46:53 – 46:55]** It probably looks something like this, right?

**[46:55 – 46:59]** So it should decrease.

**[46:59 – 47:02]** I mean, I wanted it to be symmetrical,

**[47:02 – 47:03]** so let's assume it's symmetrical,

**[47:03 – 47:06]** and I wanted it to decrease to both sides, right?

**[47:06 – 47:09]** So what it would mean,

**[47:09 – 47:15]** it would mean that larger distances from our model,

**[47:15 – 47:17]** larger distances from the straight line,

**[47:17 – 47:19]** are less probable.

**[47:19 – 47:22]** So if I want to find the most probable line,

**[47:22 – 47:25]** the maximum likelihood line, for example,

**[47:25 – 47:27]** then, of course, I want these distances to be small.

**[47:27 – 47:30]** So I want these points to...

**[47:30 – 47:32]** I want the noise to be as small as possible,

**[47:32 – 47:33]** the total noise here.

**[47:33 – 47:37]** And the specific form of the loss function

**[47:37 – 47:40]** will follow from the choice of distribution.

**[47:40 – 47:42]** So yeah, I want it to be symmetric,

**[47:42 – 47:44]** I want it to be kind of bell-shaped,

**[47:44 – 47:46]** but as we discussed yesterday,

**[47:46 – 47:47]** there are lots of bell-shaped curves, right?

**[47:47 – 47:50]** So we want to pick a specific distribution here.

**[47:51 – 47:54]** And now comes your answer, right?

**[47:54 – 47:56]** So this was all the setup for your answer.

**[47:58 – 48:01]** What is the most natural distribution?

**[48:02 – 48:03]** What is the default distribution

**[48:03 – 48:06]** that you use in a situation like this?

**[48:06 – 48:08]** Actually, it's the Gaussian.

**[48:08 – 48:10]** It's the normal distribution.

**[48:10 – 48:10]** And why?

**[48:11 – 48:15]** Because of the central limit theorem actually.

**[48:16 – 48:20]** So if you don't know,

**[48:20 – 48:21]** if you haven't had probability theory,

**[48:21 – 48:23]** if you don't know central limit theorems,

**[48:23 – 48:25]** no matter if you won't really use it,

**[48:25 – 48:26]** I'm just explaining where it comes from.

**[48:28 – 48:31]** So what does the central limit theorem tell us?

**[48:32 – 48:33]** The basic one.

**[48:33 – 48:36]** It says that whatever is the distribution,

**[48:37 – 48:39]** if you average it out sufficiently,

**[48:40 – 48:44]** if you average out sufficiently more copies of this distribution

**[48:44 – 48:46]** or if you add them up sufficiently many times,

**[48:46 – 48:49]** what you get is a Gaussian.

**[48:49 – 48:52]** You converge to a Gaussian, right?

**[48:52 – 48:57]** So what this means in practice is that if you have a process,

**[48:57 – 48:59]** some kind of physical process or whatever,

**[49:00 – 49:05]** where there are many small sources of noise

**[49:05 – 49:09]** that all come together and all add up,

**[49:09 – 49:13]** the result will probably be Gaussian or close to Gaussian.

**[49:13 – 49:17]** So if you, I don't know, in high school physics,

**[49:17 – 49:22]** if you do an experiment like you're rolling the ball down a slope

**[49:22 – 49:24]** and then it comes to a certain distance,

**[49:24 – 49:27]** then as the ball rolls,

**[49:27 – 49:31]** there are billions of small impacts on the ball.

**[49:31 – 49:34]** There are imperfections in the plane,

**[49:34 – 49:37]** the ball is imperfect, there's wind or whatever,

**[49:37 – 49:42]** and every one of these imperfections is definitely not Gaussian.

**[49:42 – 49:45]** Every one of them makes some small impact

**[49:45 – 49:47]** in a specific direction, actually, probably.

**[49:47 – 49:52]** But when you add them all together, it's a Gaussian,

**[49:52 – 49:54]** because there are a lot of them.

**[49:54 – 49:58]** So, I mean, there is a theorem, there is math behind it,

**[49:58 – 50:00]** but let's just leave it here.

**[50:00 – 50:05]** So, when you average out lots of small notches

**[50:05 – 50:08]** that go in opposite, in different directions,

**[50:08 – 50:10]** what you get is more or less a Gaussian,

**[50:10 – 50:13]** unless there is some systematic bias inside.

**[50:13 – 50:16]** Like, if all of your notches are in the same direction,

**[50:16 – 50:17]** then, of course, you don't get a Gaussian.

**[50:17 – 50:22]** But that's a different story.

**[50:22 – 50:31]** So this is why this noise,

**[50:31 – 50:33]** this error in linear regression,

**[50:33 – 50:39]** is indeed most natural to model with a Gaussian,

**[50:39 – 50:40]** with a normal distribution.

**[50:40 – 50:42]** And that's why the normal distribution is called normal,

**[50:42 – 50:46]** and that's why it's also important, right?

**[50:46 – 50:49]** So if you just look at its shape, at the density,

**[50:49 – 50:53]** you wouldn't understand why it holds

**[50:53 – 50:54]** such a special place.

**[50:54 – 50:57]** Well, it's special because of the central limit theorem,

**[50:57 – 51:00]** because everything converges to a Gaussian in a way.

**[51:00 – 51:04]** And so if we do this assumption here,

**[51:04 – 51:09]** p of, sorry, not p, but Gaussian already,

**[51:09 – 51:14]** normal distribution of yn around w times xn

**[51:14 – 51:16]** with some variance sigma squared,

**[51:16 – 51:18]** it's a one-dimensional Gaussian.

**[51:18 – 51:19]** We are talking about yn, right?

**[51:21 – 51:26]** Now this will be our, so this was the first assumption,

**[51:26 – 51:27]** this is our second assumption,

**[51:27 – 51:29]** that the center is a linear function,

**[51:29 – 51:32]** that's the linear regression,

**[51:32 – 51:33]** and this is the third assumption,

**[51:33 – 51:36]** that the noise is Gauss, okay?

**[51:36 – 51:39]** There is a fourth, but we'll get there.

**[51:41 – 51:47]** So what is the, let me write down the density of the Gauss,

**[51:47 – 51:51]** and it's one over square root of two pi sigma squared

**[51:51 – 51:55]** times e to the power minus one over two sigma squared

**[51:55 – 52:02]** times yn minus w times xn squared, and that's it, okay?

**[52:02 – 52:04]** So looks pretty complicated.

**[52:06 – 52:09]** What do we do next?

**[52:09 – 52:14]** Next, our first job is to maximize the thing, right?

**[52:14 – 52:19]** So we want to, let's say I want to get the maximum likelihood hypothesis on the weights.

**[52:19 – 52:23]** I need to take the likelihood and I need to maximize.

**[52:23 – 52:28]** How do you always inevitably do it in practice?

**[52:28 – 52:34]** The very first trick that is always applied and it's usually like understood without even

**[52:34 – 52:35]** explicitly writing it down.

**[52:37 – 52:47]** In machine learning, the likelihood is always, as we discussed, a big product of stuff, right?

**[52:47 – 52:51]** So it's a product over all data points and there are lots of data points.

**[52:52 – 52:56]** And we multiply the likelihoods of data points all together.

**[52:56 – 53:02]** So when you have a big, big, big product, what you always want to do is take the logarithm, right?

**[53:02 – 53:05]** So you want to convert the product to a sum.

**[53:05 – 53:12]** Because if you keep multiplying small numbers like probabilities, it will be very difficult numerically, right?

**[53:12 – 53:16]** So the first step is always to take the logs.

**[53:16 – 53:20]** So log P of D given W.

**[53:20 – 53:25]** And now this formula is the sum over N.

**[53:25 – 53:31]** This is what minus 1/2 times log 2 pi sigma squared.

**[53:31 – 53:33]** I'll leave it to that.

**[53:33 – 53:40]** Minus 1 over 2 sigma squared Yn W times Xn squared, right?

**[53:40 – 53:44]** And now this is a constant that goes out of the sum.

**[53:44 – 53:49]** So it's minus N over 2 log 2 pi sigma squared.

**[53:49 – 53:53]** This can also go out of the sum.

**[53:53 – 54:00]** And inside the sum, we have Yn minus W times Xn squared.

**[54:00 – 54:11]** And now our problem, our equation is, I want to maximize this with respect to W.

**[54:11 – 54:12]** There is a minus sign here.

**[54:12 – 54:16]** So if I just look at this sum, this one doesn't have any Ws.

**[54:16 – 54:18]** So this one is irrelevant, it's a constant.

**[54:18 – 54:22]** And the W is in here and there is a minus sign.

**[54:22 – 54:26]** So what I do with this sum is I actually want to minimize it, right?

**[54:26 – 54:30]** That's it. There you go.

**[54:30 – 54:34]** That's the motivation behind having a sum of squares.

**[54:34 – 54:41]** Specifically squares and not absolute values, not exponents, not anything else.

**[54:41 – 54:45]** The story, of course, does not stop here. It's only the beginning.

**[54:47 – 54:51]** One sec, did I forget anything? Oh, yeah.

**[54:51 – 54:55]** And one more thing. I promised to go back to the fourth assumption.

**[54:55 – 54:58]** So there is a fourth assumption which is kind of hidden over here.

**[54:58 – 55:08]** And the fourth assumption is that the variance is the same over the whole dataset, right?

**[55:08 – 55:15]** In statistics, it's called, there is a difficult word, homoscedasticity, I think.

**[55:17 – 55:22]** So if you have a homoscedastic process, it means that the noise variance is constant across the

**[55:22 – 55:33]** whole process. And it's the assumption that allows us to actually take the sigma and get it out of the

**[55:33 – 55:39]** sum and not care about the sigma. And it can be violated in practice, right? So in practice, it's

**[55:39 – 55:46]** quite possible that you can have points that go like this. At first, they are dense, and then they

**[55:46 – 55:55]** become more noisy, for example. And you still want to have a single straight line that describes all of

**[55:55 – 56:01]** these points. It may happen. But yeah, if something like that happens, then you need to modify the loss

**[56:01 – 56:07]** function. You need to actually explicitly notice this, which is non-trivial, and then understand

**[56:07 – 56:16]** what it tells you about the loss function. So this is, by the way, one of the most direct reasons why

**[56:17 – 56:27]** you actually want to understand this probabilistic approach. Because it may seem at first glance that,

**[56:27 – 56:33]** okay, so we explained y-squares, but it doesn't change anything. We are still minimizing the sum

**[56:33 – 56:43]** of squares, right? But the point is not only, so why do we want to understand stuff? We want to

**[56:43 – 56:52]** understand stuff in order to notice when it stops working. We want to understand the assumptions

**[56:52 – 57:00]** behind the sum of squares so that when they are violated, when we are not in this situation,

**[57:00 – 57:07]** we actually notice. For example, when our variances change in the middle of the process,

**[57:07 – 57:15]** or for example, when we have reasons to believe that all of the noise is only in a single direction.

**[57:15 – 57:20]** So now you want to have an asymmetric noise distribution, a noise distribution that's only

**[57:20 – 57:26]** on the positive part of the line. Also, there are variations of linear regression like this too,

**[57:26 – 57:32]** of course. It's not like you need to do any new math here, but you need to notice this

**[57:32 – 57:44]** and to apply the correct math. Okay, so this is our first step and we compute the sum of squares and

**[57:44 – 57:54]** blah, blah, blah. But of course, we want to apply our Bayesian story, right? So we want to say,

**[57:56 – 58:09]** what I'm actually interested in is not p of d given w, but it's p of w given d, right? Which means

**[58:09 – 58:19]** that I need to have a prior, right? What does a prior look like for linear regression? Well,

**[58:19 – 58:26]** it's a more complicated thing. And again, as soon as we get to something like Bayesian inference,

**[58:26 – 58:32]** something like prior distributions, well, the probability theory becomes a bit messier.

**[58:32 – 58:38]** Like in coins, we had a very simple discrete likelihood, just two outcomes. But then as

**[58:38 – 58:44]** soon as we went to the prior and posterior, distributions became continuous. There was

**[58:44 – 58:50]** no way around that. Here, everything is continuous, but from the single one-dimensional clean Gaussian,

**[58:50 – 58:55]** now we need to go to a multi-dimensional distribution, right? So now there are several

**[58:55 – 59:03]** different weights, and we want to have a distribution on them. But before we choose it,

**[59:04 – 59:10]** what is going to happen with our optimization problem? If I now want to maximize the posterior

**[59:10 – 59:17]** distribution, what does it actually mean in terms of the numerical problem that I'm solving? Well,

**[59:17 – 59:25]** to be honest, it changes quite little. So what we are basically saying, and this is also true in

**[59:25 – 59:30]** the entire machine learning, we are basically saying that, okay, proportional means that there is a

**[59:30 – 59:37]** constant which doesn't matter, right, for maximization. And then we have this log likelihood,

**[59:37 – 59:45]** which we already had before. And then there is the log prior. So basically, I want to maximize these

**[59:45 – 59:55]** guys together, right? And the log prior, you probably, in some previous classes, you probably

**[59:55 – 1:00:03]** have seen already all of this log prior stuff. And you usually call them regularizers, right?

**[1:00:03 – 1:00:12]** So regularization is actually the process of putting a prior on the parameters of your model.

**[1:00:12 – 1:00:17]** So what is the difference between these terms in practice? The difference is that

**[1:00:17 – 1:00:22]** the regularizer does not depend on the data, right? So it's the part of the loss function

**[1:00:22 – 1:00:27]** that is only about the weights, only about the model parameters and not about the dataset.

**[1:00:29 – 1:00:40]** And so formally, it's our prior beliefs, it's what we think about the weights of

**[1:00:43 – 1:00:56]** our linear regression before we start getting the data. And at this point, it may sound quite strange

**[1:00:56 – 1:01:05]** because if for a coin we did have an intuition, like a real-life intuition that coins are

**[1:01:05 – 1:01:11]** approximately fair, right? So for a coin that I take out of my pocket, obviously I do have some kind of

**[1:01:11 – 1:01:18]** prior beliefs that are actually quite strong. For linear regression, it seems like we don't, right?

**[1:01:18 – 1:01:23]** So for linear regression, it seems like the regularizer shouldn't be doing anything.

**[1:01:26 – 1:01:33]** How do I prefer one slope of this straight line to another slope? I don't know. If I don't have any

**[1:01:33 – 1:01:36]** data, they all are the same for me, or at least they should be, right?

**[1:01:38 – 1:01:47]** Well, here is how it actually works. So to make a good illustration, I won't go to the

**[1:01:47 – 1:01:53]** multidimensional case, but I will make a multidimensional regression out of a one-dimensional

**[1:01:53 – 1:02:00]** regression. So an example that I always give and that I think illustrates this the best is

**[1:02:01 – 1:02:12]** let's extract some additional features from X. So this is also an important discussion in its own right.

**[1:02:12 – 1:02:21]** So how do people usually apply simple models like linear regression? Well, they have their axes,

**[1:02:21 – 1:02:32]** their original inputs, and sometimes it so happens that you can just treat axes as numbers and do a

**[1:02:32 – 1:02:39]** linear regression and your output is W times X and everybody's happy. But more often than not,

**[1:02:40 – 1:02:50]** before you go to learn the weights, you actually extract some kind of features from X. Sometimes,

**[1:02:51 – 1:02:58]** and then you get some, I know, Phi of X, Phi of X, and then you do the linear regression and the output

**[1:02:58 – 1:03:07]** is W times Phi of X. Okay? So sometimes feature extraction is about reducing the

**[1:03:07 – 1:03:12]** content. Like if you want to do linear regression on images, then obviously it makes no sense to do

**[1:03:12 – 1:03:18]** linear regression on the pixels, right? You first want to extract some semantically rich features and

**[1:03:18 – 1:03:25]** then do the linear regression. Sometimes it's the opposite. Sometimes X is very simple and you want

**[1:03:25 – 1:03:33]** to describe a more complicated dependency between X and Y and you need to extract additional features.

**[1:03:33 – 1:03:44]** So this is an example like that. And suppose that I have one dimensional regression.

**[1:03:44 – 1:03:55]** So there is only one X, there is only one Y. But when I look at my points, I kind of realize

**[1:03:55 – 1:04:04]** that they're definitely not linear, right? I realize that they don't look like a straight line at all,

**[1:04:04 – 1:04:11]** but they kind of look like a parabola. They kind of look like a quadratic function.

**[1:04:11 – 1:04:19]** So here is a question. Can I use linear regression to actually learn a parabola here?

**[1:04:19 – 1:04:29]** To learn something like w0 plus w1 times x plus w2 times x squared?

**[1:04:29 – 1:04:34]** Yes, if we make a feature, we're processing it.

**[1:04:34 – 1:04:41]** Yeah, precisely. So the trivial linear regression would only give you this,

**[1:04:41 – 1:04:46]** but we already know that we can add more features. We did it in a trivial way,

**[1:04:46 – 1:04:54]** now let's do it in a less trivial way. So let's go from x to this feature vector, 1x, x squared.

**[1:04:54 – 1:05:00]** And then you multiply, and then you do just linear regression, right?

**[1:05:00 – 1:05:04]** And when you do linear regression on this, what you are actually minimizing,

**[1:05:04 – 1:05:10]** what is your loss function? It's the sum of yn minus what?

**[1:05:10 – 1:05:18]** Minus, well, w0 plus w1 times x plus w2 times x squared. There we go, right?

**[1:05:18 – 1:05:26]** So you are actually feeding a parabola. And actually, this discussion is extremely relevant

**[1:05:26 – 1:05:33]** to deep learning because what is the thing that deep learning is doing? What are the neural

**[1:05:33 – 1:05:42]** networks always doing? They are learning good feature extractors. That's the whole revolution.

**[1:05:42 – 1:05:48]** So before deep learning worked, what we would usually do as machine learners, we would try to

**[1:05:48 – 1:05:58]** invent this feature extraction part by hand or for some other reasons, right? And then we would run

**[1:05:58 – 1:06:03]** relatively simple models on these features. Of course, not necessarily linear regression, but

**[1:06:03 – 1:06:13]** relatively simple models. What neural networks do is they make feature extraction a part of the

**[1:06:13 – 1:06:21]** model. So now the feature extraction also has weights. And how does a neural network actually

**[1:06:21 – 1:06:29]** look? Let's say I have an image at the input. Then there are lots of layers that do different

**[1:06:29 – 1:06:35]** interesting stuff, blah, blah, blah. But then at the end of these layers, we have actually a vector

**[1:06:35 – 1:06:43]** of numbers that goes into the final layer. And the final layer, depending on what problem you are

**[1:06:43 – 1:06:52]** solving, if you're predicting a number, it's usually a linear layer. So if your output is supposed to be

**[1:06:52 – 1:06:59]** a number, not a classification problem, then the last layer is probably linear. Almost always. I don't know any exceptions.

**[1:07:01 – 1:07:13]** What this means is that this part of the network is doing feature extraction for the last linear regression layer.

**[1:07:13 – 1:07:19]** The last layer is actually linear regression, but not on the pixels of the input, not on the X,

**[1:07:19 – 1:07:28]** but on the features extracted from X. And of course, the hard part is learning the previous layers.

**[1:07:28 – 1:07:34]** The last layer is kind of easy and we are now doing the easy stuff, of course, but it's there.

**[1:07:34 – 1:07:44]** So basically any big complicated neural network that predicts a number almost always ends with a linear regression.

**[1:07:44 – 1:07:52]** Any complicated neural network that does classification ends with a logistic regression.

**[1:07:52 – 1:07:53]** We'll get there later.

**[1:07:53 – 1:07:59]** So the rest of the network is extracting features for this last final layer.

**[1:07:59 – 1:08:01]** That's the connection.

**[1:08:01 – 1:08:05]** That's why these linear models are still very, very relevant for deep learning as well.

**[1:08:08 – 1:08:09]** All right.

**[1:08:09 – 1:08:11]** So back to linear regression.

**[1:08:12 – 1:08:17]** Yeah, and at this point, I think I want to make an example of this.

**[1:08:26 – 1:08:40]** So I put some more stuff here, but yeah, for now, we are getting there.

**[1:08:40 – 1:08:43]** Yeah, for now, let's...

**[1:08:45 – 1:08:48]** Okay, yeah, there we go.

**[1:08:50 – 1:08:58]** So let me show you a polynomial regression problem.

**[1:08:59 – 1:09:05]** I have the true function, the original function, which is actually not polynomial.

**[1:09:05 – 1:09:11]** So we don't expect to capture this function exactly. It's a sine wave.

**[1:09:11 – 1:09:20]** But I take one period of this sine wave and I put the points around this one period of the sine wave.

**[1:09:20 – 1:09:28]** Okay, so the stars are the points, the horizontal line is x, there is only one dimension here,

**[1:09:28 – 1:09:31]** and the vertical line is y, the vertical axis is y.

**[1:09:33 – 1:09:39]** So when you look at these stars, you kind of immediately realize that they are not linear.

**[1:09:40 – 1:09:47]** And if you actually fit linear regression, you get a straight line, of course, you get some line, sure,

**[1:09:47 – 1:09:53]** but the error is very high. It's obviously not describing these points well.

**[1:09:53 – 1:10:00]** So first question to you, what do you think is the proper degree of the polynomial?

**[1:10:00 – 1:10:03]** What would be a good degree of the polynomial?

**[1:10:03 – 1:10:08]** I can't put a sine wave here, but I can do a polynomial.

**[1:10:08 – 1:10:20]** Can you please repeat the question?

**[1:10:20 – 1:10:25]** Yeah, what would be a good degree of the polynomial to fit these points?

**[1:10:25 – 1:10:29]** So the straight line, degree one, doesn't work.

**[1:10:29 – 1:10:31]** What would work?

**[1:10:31 – 1:10:35]** I think the degree of three.

**[1:10:35 – 1:10:37]** Yeah, exactly, yeah.

**[1:10:37 – 1:10:41]** So a parabola probably also doesn't capture this, right?

**[1:10:43 – 1:10:45]** So it's a little better, but not much.

**[1:10:45 – 1:10:47]** But if you go to degree three, then yeah,

**[1:10:47 – 1:10:53]** the third degree polynomial has this two,

**[1:10:55 – 1:10:57]** one minimum and one maximum it can have,

**[1:10:57 – 1:11:04]** and which kind of already can match one period of the sine wave, right?

**[1:11:04 – 1:11:08]** So if I train a third degree polynomial,

**[1:11:08 – 1:11:17]** so the regression with four weights, including the intercept,

**[1:11:17 – 1:11:19]** then it's already a pretty good fit.

**[1:11:19 – 1:11:22]** And if I compute the errors, I don't think I have it here,

**[1:11:22 – 1:11:24]** but if I compute the errors, they will be fine.

**[1:11:26 – 1:11:31]** But what happens if I keep increasing the degree?

**[1:11:32 – 1:11:38]** So if I increase it to four or five, I don't think much will happen.

**[1:11:38 – 1:11:41]** I think they will look approximately the same.

**[1:11:41 – 1:11:44]** So if you look at the degree four and degree five curves,

**[1:11:44 – 1:11:48]** they are slightly better, but it's basically the same stuff.

**[1:11:50 – 1:11:52]** When do you think it's going to break?

**[1:11:52 – 1:11:53]** Or is it going to break?

**[1:11:53 – 1:11:58]** Or can I increase the degree indefinitely?

**[1:11:58 – 1:12:03]** Maybe 10 or 20 it will break.

**[1:12:03 – 1:12:06]** Okay, 10 or 20.

**[1:12:06 – 1:12:08]** What do we need to know to answer this?

**[1:12:09 – 1:12:19]** What do we need to know to answer?

**[1:12:19 – 1:12:25]** Yeah, like, okay.

**[1:12:25 – 1:12:30]** At least I know if we will make a polynomial with a number of points,

**[1:12:31 – 1:12:34]** it goes to which point it will break.

**[1:12:34 – 1:12:35]** Yeah, sure.

**[1:12:35 – 1:12:42]** So yeah, of course we cannot predict in advance when exactly it's going to start to be bad,

**[1:12:42 – 1:12:45]** but we definitely know when it's certainly going to be bad.

**[1:12:45 – 1:12:50]** And here I have 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 points.

**[1:12:50 – 1:12:55]** So for 11 points, if I do a polynomial of degree 10,

**[1:12:55 – 1:13:01]** a polynomial of degree 10 can just pass through all of these points exactly, right?

**[1:13:01 – 1:13:05]** So let me keep the third degree and add degree 10.

**[1:13:05 – 1:13:11]** And this is what an interpolation polynomial looks like.

**[1:13:11 – 1:13:16]** So it passes through every point exactly, which is great.

**[1:13:17 – 1:13:22]** But so the training set error is exactly zero,

**[1:13:22 – 1:13:25]** but the test set error is huge, right?

**[1:13:25 – 1:13:27]** It's completely useless for predicting.

**[1:13:27 – 1:13:31]** It has this very strange peaks on the left, on the right,

**[1:13:31 – 1:13:33]** even in the middle a little bit.

**[1:13:33 – 1:13:40]** So it's definitely a very bad model, much worse than the orange curve, right?

**[1:13:40 – 1:13:45]** And that's indeed, as you write in chat, that's the classical picture of overfitting.

**[1:13:45 – 1:13:49]** So we have too many parameters. And in this case, of course,

**[1:13:49 – 1:13:52]** it's quite obvious that we have too many parameters.

**[1:13:53 – 1:13:59]** And what do we do? How do we notice this overfitting

**[1:13:59 – 1:14:01]** if we can't just look at the picture, right?

**[1:14:01 – 1:14:03]** In real life, there would be a high dimensional input

**[1:14:03 – 1:14:06]** and we wouldn't be able to just look at the picture.

**[1:14:06 – 1:14:07]** How do we notice it?

**[1:14:08 – 1:14:13]** Well, in this specific case, it's very easy to say,

**[1:14:13 – 1:14:15]** just don't do this, right?

**[1:14:15 – 1:14:17]** So this is, of course, a degenerate case.

**[1:14:17 – 1:14:19]** This is a very simple example and you can say,

**[1:14:19 – 1:14:23]** well, obviously, if we have 11 points,

**[1:14:23 – 1:14:26]** we don't want the polynomial of degree 10.

**[1:14:26 – 1:14:26]** That's easy.

**[1:14:26 – 1:14:30]** You don't need any theory to understand this.

**[1:14:31 – 1:14:38]** But in real life, you usually cannot avoid this completely.

**[1:14:38 – 1:14:41]** So in this simple example where I have a one-dimensional x

**[1:14:41 – 1:14:43]** and I choose the degree myself,

**[1:14:43 – 1:14:46]** sure, I can just look at the pictures and choose.

**[1:14:46 – 1:14:49]** That's why I'm showing it to you because the pictures make it obvious.

**[1:14:49 – 1:14:54]** But in real life, what's going to happen is actually this.

**[1:14:55 – 1:14:59]** And I'm answering this unasked question of how can this happen in practice

**[1:14:59 – 1:15:00]** with linear regression?

**[1:15:01 – 1:15:02]** And the answer is basically this.

**[1:15:02 – 1:15:06]** What would actually happen to you when you do linear regression?

**[1:15:06 – 1:15:13]** You have your data set and you have in your data set points of degree d.

**[1:15:13 – 1:15:17]** So in dimension one, nothing bad will ever happen.

**[1:15:17 – 1:15:18]** Dimension one is easy.

**[1:15:18 – 1:15:29]** But you have points of dimension d and you are trying to do linear regression

**[1:15:29 – 1:15:31]** and you are failing.

**[1:15:31 – 1:15:34]** Okay, so if linear regression works like this, perfect.

**[1:15:34 – 1:15:36]** You don't need anything else.

**[1:15:36 – 1:15:37]** But you are failing.

**[1:15:37 – 1:15:40]** You can see that the relationship is not really linear.

**[1:15:40 – 1:15:42]** You want something else.

**[1:15:42 – 1:15:44]** You want something more, right?

**[1:15:45 – 1:15:48]** So this doesn't work and you make the next step.

**[1:15:48 – 1:15:50]** What is the next step?

**[1:15:50 – 1:15:52]** Let's do a quadratic dependency.

**[1:15:52 – 1:15:57]** But unlike the one-dimensional case,

**[1:15:57 – 1:16:00]** where the quadratic dependency just adds one more feature

**[1:16:00 – 1:16:02]** and you control it very finely.

**[1:16:02 – 1:16:04]** You go to degree three, you add one more feature.

**[1:16:04 – 1:16:06]** You go to degree four, you add one more feature.

**[1:16:06 – 1:16:09]** So you choose the number of features explicitly, basically.

**[1:16:09 – 1:16:12]** If you have a multi-dimensional vector,

**[1:16:12 – 1:16:15]** it doesn't work like that anymore, right?

**[1:16:15 – 1:16:21]** So if you go from x of dimension d, sorry, of length d,

**[1:16:21 – 1:16:25]** to a quadratic feature vector,

**[1:16:25 – 1:16:30]** what you actually get is something like 1, x1, xd,

**[1:16:30 – 1:16:34]** then x1 squared, x1, x2, x1, x3,

**[1:16:34 – 1:16:36]** and all the way to xd squared, right?

**[1:16:36 – 1:16:40]** So the actual number of features is something like,

**[1:16:40 – 1:16:44]** maybe I'm missing some plus or minus one,

**[1:16:44 – 1:16:45]** but something like this,

**[1:16:45 – 1:16:48]** something on the order of d squared, right?

**[1:16:50 – 1:16:56]** Which is quite bad in the sense that now,

**[1:16:56 – 1:17:00]** if I start with a vector of size 100,

**[1:17:00 – 1:17:03]** and I go to a quadratic dependency,

**[1:17:03 – 1:17:07]** I immediately get not 200 features,

**[1:17:07 – 1:17:10]** not even 500 features,

**[1:17:10 – 1:17:14]** but I get, what, 5,000 features, about approximately.

**[1:17:16 – 1:17:21]** And of course, when you go from 100 features to 5,000 features,

**[1:17:21 – 1:17:24]** overfitting can happen, right?

**[1:17:26 – 1:17:29]** So this is the actual mechanism.

**[1:17:29 – 1:17:32]** Of course, in dimension one, it's always easy,

**[1:17:32 – 1:17:35]** but in high dimensions, there is no middle ground.

**[1:17:35 – 1:17:38]** You cannot go to degrees three halves, right?

**[1:17:41 – 1:17:46]** And actually, when you look at all of these features,

**[1:17:46 – 1:17:49]** you understand, of course, in your head,

**[1:17:49 – 1:17:52]** that you don't need all of them, of course.

**[1:17:52 – 1:17:53]** Of course, you don't need all of them.

**[1:17:54 – 1:17:58]** You only need some of these quadratic dependencies.

**[1:17:58 – 1:18:02]** So in reality, what matters is maybe the relation,

**[1:18:02 – 1:18:07]** the dependency, the connection between x1 and x3,

**[1:18:07 – 1:18:09]** and then maybe xd squared,

**[1:18:09 – 1:18:10]** and then maybe something else in the middle,

**[1:18:10 – 1:18:12]** and that's it, and the rest could be zero.

**[1:18:12 – 1:18:16]** But the point is, you don't know in advance which ones.

**[1:18:16 – 1:18:18]** That's the whole point of learning, right?

**[1:18:19 – 1:18:22]** You need to figure out which of these interactions matter.

**[1:18:22 – 1:18:25]** They're called interactions in statistics when you add this.

**[1:18:25 – 1:18:28]** Features like X1 and X3.

**[1:18:28 – 1:18:30]** Which of these interactions matter?

**[1:18:30 – 1:18:36]** And you can't do it if you don't start with them all, right?

**[1:18:36 – 1:18:39]** So overfitting is kind of inherent in machine learning.

**[1:18:39 – 1:18:42]** You cannot avoid it even for linear regression,

**[1:18:42 – 1:18:46]** let alone something complicated like neural networks.

**[1:18:46 – 1:18:54]** So getting back here, how could we notice that something bad is happening

**[1:18:54 – 1:18:56]** if we cannot just look at the picture?

**[1:18:56 – 1:18:58]** How can we notice overfitting?

**[1:18:58 – 1:19:01]** There is a simple principled answer.

**[1:19:03 – 1:19:06]** A principled answer would be, so let's do a test set,

**[1:19:06 – 1:19:10]** or to be more precise, a validation set.

**[1:19:10 – 1:19:13]** Let's set aside part of the points.

**[1:19:13 – 1:19:16]** Let's measure the validation set error.

**[1:19:16 – 1:19:20]** And when the validation set error starts to grow, we stop.

**[1:19:20 – 1:19:24]** That's the standard procedure in machine learning.

**[1:19:26 – 1:19:30]** And if you can do it, it's fine.

**[1:19:32 – 1:19:38]** But again, in this example, you can't really do it.

**[1:19:38 – 1:19:45]** So, well, I mean, maybe you can imagine like adding these quadratic terms one by one.

**[1:19:47 – 1:19:52]** But then you would need to kind of go through all of them and then go through all of them again.

**[1:19:52 – 1:19:53]** Probably would be impractical.

**[1:19:54 – 1:19:57]** But if you add all of them at once, you just get overfitting.

**[1:19:57 – 1:19:59]** You get this high test set error and what do you do?

**[1:20:03 – 1:20:07]** There is no continuous process that you can just stop at some point.

**[1:20:07 – 1:20:16]** So what is another symptom of overfitting happening here?

**[1:20:16 – 1:20:20]** How else could it work?

**[1:20:20 – 1:20:26]** Well, here I output them over here.

**[1:20:27 – 1:20:29]** You can also look at the coefficients.

**[1:20:29 – 1:20:32]** And this sounds a little bit counterintuitive,

**[1:20:32 – 1:20:39]** but we are getting back to the stuff that is actually useful for us now.

**[1:20:40 – 1:20:44]** If you look at the coefficients of these polynomials,

**[1:20:44 – 1:20:46]** let me do a lot of them.

**[1:20:49 – 1:20:53]** So the plot is now completely unreadable, but let's look over here.

**[1:20:54 – 1:20:57]** If you look at the coefficients of these polynomials,

**[1:20:57 – 1:21:03]** you will notice that as the degree increases,

**[1:21:03 – 1:21:10]** the coefficients grow, but they grow kind of in a bounded way.

**[1:21:10 – 1:21:13]** And then when overfitting starts to happen,

**[1:21:13 – 1:21:15]** in this case, it's only at d equals to 10,

**[1:21:15 – 1:21:16]** but it could happen a bit before,

**[1:21:18 – 1:21:21]** you see a sudden jump in the coefficients.

**[1:21:21 – 1:21:23]** You see coefficients like plus or minus 50.

**[1:21:23 – 1:21:29]** And at this point, you can notice that.

**[1:21:29 – 1:21:31]** And you can say, well...

**[1:21:31 – 1:21:34]** So this is the tricky part here.

**[1:21:34 – 1:21:36]** This is the not really formal part.

**[1:21:37 – 1:21:42]** You can say, well, I have like 10 points, 11 points.

**[1:21:44 – 1:21:47]** And the x is always about 1.

**[1:21:47 – 1:21:52]** So it's from negative 1 and a half to positive 2.

**[1:21:53 – 1:21:56]** And the y is from minus to plus 1.

**[1:21:56 – 1:22:01]** And these points are described by a model with coefficients like 50.

**[1:22:01 – 1:22:04]** That doesn't sound plausible to me.

**[1:22:04 – 1:22:05]** Okay?

**[1:22:05 – 1:22:10]** So this is the intuitive reading of this.

**[1:22:10 – 1:22:21]** And the formal reading of this would be my prior belief about the coefficients is that they should actually be relatively small.

**[1:22:21 – 1:22:30]** They should, for this data set, they should be on the order of plus or minus 1 or maybe 2, but definitely not 50, right?

**[1:22:30 – 1:22:35]** And you can also think about it this way.

**[1:22:35 – 1:22:37]** Maybe this picture I also find very helpful.

**[1:22:37 – 1:22:52]** So when you do standard linear regression, if you have one-dimensional x and standard linear regression, you have two dimensions of weights.

**[1:22:52 – 1:22:56]** So you have this two-dimensional space of weights to choose from, right?

**[1:22:56 – 1:23:07]** And then you go to quadratic regression, you get a three-dimensional space of weights, which is, now it's not a mathematical term, but which is kind of larger.

**[1:23:07 – 1:23:14]** you have a larger variety of models to choose from. I can make it precise, but we won't have time in

**[1:23:14 – 1:23:20]** class to make it precise. And then you go to dimension 4, you get even more different models.

**[1:23:20 – 1:23:27]** There are much more polynomials of degree 4 than there are polynomials of degree 2,

**[1:23:27 – 1:23:33]** because polynomials of degree 4 include polynomials of degree 2 and then some, and a lot

**[1:23:33 – 1:23:47]** different polynomials. So models of degree 4 can explain, can approximate more data sets, many more

**[1:23:47 – 1:23:54]** different dependencies between points than polynomials of degree 2. So you get this much

**[1:23:54 – 1:24:03]** larger set of weights to choose from. And then you go up to degree 10 and at some point this variety

**[1:24:03 – 1:24:09]** becomes too much, right? And this gets you to overfitting. So one way to reduce the variety would

**[1:24:09 – 1:24:15]** be to go back in the dimension. But if you cannot afford that, like in this multidimensional example,

**[1:24:15 – 1:24:22]** if you can't just do a smaller set of features, then what you could do is you could try to limit

**[1:24:22 – 1:24:31]** this variety inside the big space. So you could say, okay, I have to stick with the 11 dimensional

**[1:24:31 – 1:24:38]** space of weights, but at least let me look for solutions inside, like near zero. At least let me

**[1:24:38 – 1:24:46]** constrain the vectors in this 11 dimensional space. So I kind of, again, intuitively, I kind of want to

**[1:24:46 – 1:24:54]** constrain the variety of the models. And that's what regularization does, and that's what prior

**[1:24:54 – 1:25:05]** distributions do. So in this case, in this case, what we actually do here, how can we solve this

**[1:25:05 – 1:25:14]** problem? It would be, we need to add a prior distribution that would tell me that the weights

**[1:25:14 – 1:25:25]** are relatively small. So what does it mean? It means that P of W should be like somewhere around

**[1:25:25 – 1:25:32]** zero, concentrated somewhere around zero. Probably we don't want to completely exclude anything. We

**[1:25:32 – 1:25:39]** want all vectors to have some non-zero density, but we want it to be concentrated around zero. And then

**[1:25:39 – 1:25:49]** just go, just reduce in other directions, in all directions, right? And what kind of a

**[1:25:49 – 1:25:55]** distribution could that be? Well, the obvious answer, it could be a Gaussian, right? So you

**[1:25:55 – 1:26:04]** could say, okay, let's say that P of W is a Gaussian centered around zero with some

**[1:26:04 – 1:26:13]** covariance matrix. And since it's a prior distribution and I don't distinguish between

**[1:26:13 – 1:26:18]** different weights, I see no reason to have anything but the identity matrix here. So

**[1:26:18 – 1:26:23]** I don't, in advance, I don't know which weights will be dependent with which. So

**[1:26:23 – 1:26:33]** let me, let the prior be independent. And then I don't want to actually go into,

**[1:26:33 – 1:26:38]** in this class, I don't want to go into the densities of multidimensional Gauss,

**[1:26:38 – 1:26:44]** et cetera. If you're interested, I do teach classes like this, fortunately,

**[1:26:44 – 1:26:48]** in Russian, but there are quite a few Russian speakers among you. You can watch on my website

**[1:26:48 – 1:26:56]** some other classes where I spent a whole semester on this kind of stuff. But let me just say that

**[1:26:56 – 1:27:08]** from this P of W, the log P of W will be some constant minus 1 over 2 sigma 0 squared times

**[1:27:08 – 1:27:21]** the norm of the vector W times the sum of W i squared, right? And then if I add this prior to

**[1:27:21 – 1:27:31]** my likelihood, which is already fixed, this is part of the model, then what I actually get is a loss

**[1:27:31 – 1:27:39]** function that looks like this. Sum over n y n minus W times x n squared. That's the likelihood part.

**[1:27:39 – 1:27:48]** And let's, okay, let's put 1 over sigma squared here, plus 1 over sigma 0 squared, the prior variance,

**[1:27:48 – 1:27:57]** times this sum of squares of W's. And I want to minimize this. So again, constants don't really

**[1:27:57 – 1:28:08]** matter. So I can put this sigma over here and cancel the 2. And what I get is exactly the sum of squares

**[1:28:08 – 1:28:21]** with what is often called an L2 regularizer. L2 means regularizer. The regularizer is often

**[1:28:21 – 1:28:30]** the norm of the vector of weights. And then the L2 norm in the L2 space is the sum of squares,

**[1:28:30 – 1:28:40]** the Euclidean norm. So that's an L2 regularizer. And then I can use this regularizer and I can fix

**[1:28:40 – 1:28:50]** the problem. So if, let me see if I have, let me see if I have, yeah, I will skip the local features.

**[1:28:50 – 1:29:01]** I don't think I have time for that. Yeah, I do have it. Okay. So first of all,

**[1:29:01 – 1:29:10]** before I show that, before I show regularization, let me say that this kind of overfitting and regularization

**[1:29:10 – 1:29:18]** and everything is dependent on the dataset also, right? So notice how when we went to degree 10,

**[1:29:18 – 1:29:27]** we got severe overfitting only because we had exactly 11 points, right? If we just add more points, a degree

**[1:29:27 – 1:29:34]** 10 polynomial will be fine. That's kind of obvious, but I wanted to mention it. So if I have 100 points, not 10,

**[1:29:34 – 1:29:43]** then of course a degree 10 polynomial will not be severe overfitting. And that's for regularization.

**[1:29:43 – 1:29:55]** Here is the data set. Here is the original function with no regularization. It's the interpolation

**[1:29:55 – 1:30:07]** polynomial. And alpha is basically this coefficient, this guy over here. So as I increase alpha,

**[1:30:07 – 1:30:19]** it will become more important, right? So it will be the shape of this curve, the shape of this

**[1:30:19 – 1:30:25]** polynomial will be determined more and more by the regularizer and less by the actual training setter.

**[1:30:25 – 1:30:33]** So if I have this kind of small regularizer, like 1/1000, then you can see that actually...

**[1:30:33 – 1:30:39]** Actually, it's already pretty strong. Okay, let me make it even weaker in this case.

**[1:30:39 – 1:30:45]** Yeah, so the absolute values of the coefficients are already kind of reduced,

**[1:30:45 – 1:30:50]** but you still see some of this local...

**[1:30:50 – 1:30:56]** ..extremes at the...

**[1:30:56 – 1:31:01]** Okay, here is another illustration.

**[1:31:01 – 1:31:03]** Obviously, I do the points at random every time,

**[1:31:03 – 1:31:07]** so for this specific set of random points,

**[1:31:07 – 1:31:10]** even a very small regularization is enough.

**[1:31:10 – 1:31:16]** So actually, it would take a lot to straighten out these guys on the extremes,

**[1:31:16 – 1:31:22]** but the other special features are kind of already straightened out.

**[1:31:22 – 1:31:26]** But okay, so let's make the regularizer even smaller.

**[1:31:26 – 1:31:36]** Yeah, so at some point, you can see that it gradually irons out this overfitting,

**[1:31:36 – 1:31:43]** and I already showed that with some good value of alpha,

**[1:31:43 – 1:31:46]** you can get a very good curve over here.

**[1:31:46 – 1:31:50]** Let's see if I can even straighten out the sides.

**[1:31:50 – 1:31:55]** I'm not sure I can, but yeah, I can make this effect smaller at least.

**[1:31:55 – 1:31:59]** Oh, okay, here. I straightened it out on the left, but not on the right.

**[1:31:59 – 1:32:06]** So yeah, as I keep increasing the regularizer, remove this one and keep increasing this one.

**[1:32:06 – 1:32:10]** As I increase the regularizer, okay, so this is a good curve now.

**[1:32:10 – 1:32:16]** I will see that the degree 10 polynomial, it's still degree 10.

**[1:32:16 – 1:32:20]** It's still degree 10. It's properly degree 10 if you look at the coefficients.

**[1:32:20 – 1:32:25]** Yes, they become closer to zero, but they are not like everything is zero except the first three.

**[1:32:25 – 1:32:29]** No, they are still meaningful over here, for example.

**[1:32:29 – 1:32:37]** So it's still a degree 10 polynomial, but now it behaves much better, right?

**[1:32:37 – 1:32:41]** So we are kind of got rid of the regularizer, of the overfitting by regularization.

**[1:32:41 – 1:32:43]** But then of course you can overdo it.

**[1:32:43 – 1:32:51]** So if you go to something like 10, you will get like a curve that a degree 10 polynomial that doesn't care about the points at all, right?

**[1:32:51 – 1:32:54]** It only cares about the regularizer.

**[1:32:54 – 1:32:57]** And in this case, of course, it's also a bad model.

**[1:32:57 – 1:33:03]** So as with all things in life, there is a trade-off.

**[1:33:03 – 1:33:04]** Okay.

**[1:33:04 – 1:33:11]** And what else did I want to say here was that, again, I don't want to go into the math here.

**[1:33:11 – 1:33:14]** And probably I will have to skip the Bayesian part here.

**[1:33:14 – 1:33:27]** But I do want to mention that if you look, so the L2 regularizer, the Gaussian prior is indeed special for linear regression.

**[1:33:27 – 1:33:36]** So as we discussed yesterday with these conjugate priors, with the prior in the form of the likelihood and blah, blah, blah.

**[1:33:36 – 1:33:57]** You can notice that here also the shape of the Gaussian regularizer matches the shape of the Gaussian likelihood.

**[1:33:57 – 1:34:00]** It's a quadratic function of W, right?

**[1:34:00 – 1:34:04]** So, of course, it's convenient to add two quadratic functions of W.

**[1:34:04 – 1:34:07]** You also get the quadratic function of W and to get the Gaussian again.

**[1:34:07 – 1:34:15]** So this is the conjugate prior, and you can go from Gaussian to Gaussian in the space of weights.

**[1:34:15 – 1:34:19]** Let's not go much further into that discussion.

**[1:34:19 – 1:34:27]** But linear regression also gives us a good example that you don't necessarily have to do that.

**[1:34:27 – 1:34:34]** So here you can have very good reasons to choose different regularizers.

**[1:34:34 – 1:34:37]** Very good reasons like...

**[1:34:37 – 1:34:46]** So one other common regularizer for many models and for neural nets as well would be an L1 regularizer.

**[1:34:46 – 1:34:49]** So let's start from this.

**[1:34:49 – 1:34:58]** So what if instead of adding a sum of squares, I would add a sum of absolute values here?

**[1:34:58 – 1:35:03]** So notice that there is a difference here, there is an asymmetry.

**[1:35:03 – 1:35:10]** The error, the noise is a property of our model.

**[1:35:10 – 1:35:16]** I mean, yeah, we kind of choose it, but we are supposed to choose it correctly.

**[1:35:16 – 1:35:19]** There is a right answer and the wrong answer here.

**[1:35:19 – 1:35:24]** Like what is the actual noise in the actual process that we got the data with?

**[1:35:24 – 1:35:26]** That would be the perfect correct answer.

**[1:35:26 – 1:35:29]** There is some kind of underlying truth here.

**[1:35:29 – 1:35:32]** Probably it's not exactly Gaussian.

**[1:35:32 – 1:35:34]** Probably it's an approximation.

**[1:35:34 – 1:35:37]** But there is a way in which...

**[1:35:37 – 1:35:40]** There is the correct answer to the question of what is the right likelihood.

**[1:35:40 – 1:35:47]** But there is no correct answer to the question of what is the right prior.

**[1:35:47 – 1:35:48]** It's completely our choice.

**[1:35:48 – 1:35:54]** We choose the prior to match whatever we want.

**[1:35:54 – 1:35:58]** And we might want to choose something else.

**[1:35:58 – 1:36:04]** So this is L1 regularization.

**[1:36:04 – 1:36:08]** And so you may also encounter these terms.

**[1:36:09 – 1:36:13]** The linear regression with L1 regularization

**[1:36:13 – 1:36:14]** is called the LASSO regression.

**[1:36:16 – 1:36:20]** LASSO is actually an acronym for something like

**[1:36:20 – 1:36:23]** least average shrinkage.

**[1:36:23 – 1:36:24]** I forget.

**[1:36:24 – 1:36:25]** It never comes up.

**[1:36:26 – 1:36:27]** And this is called the REACH regression.

**[1:36:28 – 1:36:29]** REACH is not an acronym.

**[1:36:30 – 1:36:32]** It's this REACH, the Gaussian REACH.

**[1:36:34 – 1:36:38]** But anyway, you might want to choose

**[1:36:38 – 1:36:39]** a non-conjugate prior

**[1:36:39 – 1:36:40]** because it has better properties.

**[1:36:41 – 1:36:43]** So do I have it here?

**[1:36:43 – 1:36:44]** Yeah, I do have it here.

**[1:36:44 – 1:36:47]** So let me show these properties to you.

**[1:36:47 – 1:36:50]** We don't have time to discuss why,

**[1:36:50 – 1:36:53]** but at least let's see how it works.

**[1:36:54 – 1:36:59]** So if you look at the same kind

**[1:36:59 – 1:37:01]** of regularization weight,

**[1:37:01 – 1:37:04]** but with the LASO regression,

**[1:37:04 – 1:37:05]** with the L1 regularizer,

**[1:37:06 – 1:37:07]** not the REACH regression,

**[1:37:07 – 1:37:08]** not the L2 regularizer,

**[1:37:09 – 1:37:10]** you will see that it also is

**[1:37:10 – 1:37:12]** like a pretty good curve.

**[1:37:12 – 1:37:13]** It still, it doesn't overfit.

**[1:37:13 – 1:37:14]** It goes where you want.

**[1:37:14 – 1:37:16]** Probably we need some kind of

**[1:37:16 – 1:37:18]** lower weight here.

**[1:37:18 – 1:37:19]** Yeah, okay.

**[1:37:19 – 1:37:20]** So now this looks a lot like

**[1:37:20 – 1:37:22]** the best REACH regression

**[1:37:22 – 1:37:23]** that we got, right?

**[1:37:23 – 1:37:25]** So the curve is approximately the same.

**[1:37:26 – 1:37:28]** But if you look at the actual coefficients,

**[1:37:29 – 1:37:31]** you will see something very different.

**[1:37:31 – 1:37:34]** You will see that many of the coefficients

**[1:37:34 – 1:37:36]** have gone to exactly zero

**[1:37:36 – 1:37:38]** and some are clearly like

**[1:37:38 – 1:37:40]** on their way to exactly zero.

**[1:37:40 – 1:37:43]** With rich regression,

**[1:37:44 – 1:37:46]** they were all decreasing more or less

**[1:37:46 – 1:37:49]** isotropically, so to speak, right?

**[1:37:49 – 1:37:50]** They were all decreasing together,

**[1:37:51 – 1:37:52]** getting closer to zero,

**[1:37:53 – 1:37:56]** maybe not with exactly the same speed,

**[1:37:56 – 1:38:00]** but they were all non-zero when we checked.

**[1:38:01 – 1:38:06]** Here, some coefficients become exactly zero

**[1:38:06 – 1:38:07]** or very close to zero

**[1:38:07 – 1:38:09]** and you can send them exactly to zero,

**[1:38:09 – 1:38:10]** nothing will change.

**[1:38:10 – 1:38:14]** And sometimes that's a desirable property, right?

**[1:38:14 – 1:38:19]** So sometimes you might want to have sparsity in the results.

**[1:38:21 – 1:38:27]** So like this is what we would call

**[1:38:27 – 1:38:29]** a sparsity-inducing regularizer.

**[1:38:33 – 1:38:36]** And for example, I think it would be a better fit

**[1:38:36 – 1:38:38]** for our equation over here, right?

**[1:38:38 – 1:38:41]** So if I get a lot of different features

**[1:38:41 – 1:38:42]** and I need to choose out of them,

**[1:38:43 – 1:38:48]** then instead of some arbitrary setting the threshold

**[1:38:48 – 1:38:51]** and picking which small number is better

**[1:38:51 – 1:38:52]** than another small number,

**[1:38:52 – 1:38:55]** why not choose a different way of regularization

**[1:38:55 – 1:38:58]** to set some of them exactly to the wrong, okay?

**[1:38:58 – 1:39:01]** So this is our choice.

**[1:39:01 – 1:39:04]** This is in our hands.

**[1:39:06 – 1:39:09]** Okay, so we need to have a break by now,

**[1:39:09 – 1:39:10]** but let me summarize.

**[1:39:11 – 1:39:12]** I discussed linear regression.

**[1:39:13 – 1:39:16]** We didn't go into the actual Bayesian inference.

**[1:39:17 – 1:39:21]** It doesn't much matter for the rest of our class.

**[1:39:22 – 1:39:25]** So it's okay that we skip it,

**[1:39:25 – 1:39:29]** but I did want to highlight two important points.

**[1:39:29 – 1:39:33]** First, linear regression is relevant

**[1:39:33 – 1:39:36]** to any kind of complicated neural network still,

**[1:39:37 – 1:39:39]** and we will see it in architectures.

**[1:39:40 – 1:39:41]** But most importantly,

**[1:39:42 – 1:39:46]** all of this probabilistic machinery

**[1:39:46 – 1:39:49]** and all of these discussions about likelihoods,

**[1:39:50 – 1:39:53]** priors, probabilistic assumptions,

**[1:39:53 – 1:39:54]** how they all come together,

**[1:39:55 – 1:39:59]** what they are actually doing for us in deep learning

**[1:39:59 – 1:40:04]** is they are giving us the loss functions.

**[1:40:04 – 1:40:05]** Okay?

**[1:40:05 – 1:40:12]** So notice that when I write a general formula like this,

**[1:40:14 – 1:40:17]** it doesn't matter what the model is, right?

**[1:40:18 – 1:40:19]** It's just about...

**[1:40:19 – 1:40:20]** Okay, so this is too general a formula.

**[1:40:20 – 1:40:21]** This is about everything.

**[1:40:22 – 1:40:25]** But when I write even a formula like this,

**[1:40:25 – 1:40:30]** okay, the model is only over here, right?

**[1:40:31 – 1:40:34]** And this is the noise distribution.

**[1:40:35 – 1:40:38]** But the linear model is only over here.

**[1:40:38 – 1:40:40]** And of course, I can change,

**[1:40:40 – 1:40:43]** if I keep the noise distribution Gaussian,

**[1:40:43 – 1:40:45]** I can change the model to something else.

**[1:40:47 – 1:40:48]** So if I was...

**[1:40:48 – 1:40:54]** I can do any kind of function over here,

**[1:40:55 – 1:40:58]** and maybe it will be more difficult to optimize.

**[1:40:58 – 1:40:59]** It will not be quadratic.

**[1:40:59 – 1:41:03]** It will be a completely different thing in practice.

**[1:41:04 – 1:41:08]** But I still get the same kind of loss function,

**[1:41:08 – 1:41:08]** square deviation,

**[1:41:09 – 1:41:12]** and I still get the same kind of regularizer if I want.

**[1:41:13 – 1:41:17]** And this is still a very common loss function,

**[1:41:18 – 1:41:19]** whatever the model is.

**[1:41:20 – 1:41:23]** And this may be a neural network,

**[1:41:24 – 1:41:26]** may be a very complex neural network.

**[1:41:27 – 1:41:30]** It may be anything that we will discuss later in class.

**[1:41:30 – 1:41:34]** But then it gets plugged in to a loss function

**[1:41:34 – 1:41:37]** that comes from some probabilistic assumptions that we make.

**[1:41:38 – 1:41:40]** That's my point in the first part.

**[1:41:40 – 1:41:43]** Okay, any questions?

**[1:41:46 – 1:41:50]** Okay, good.

**[1:41:50 – 1:41:53]** So let's have a break over here.

**[1:41:54 – 1:41:58]** And then I will briefly discuss logistic regression.

**[1:41:58 – 1:42:00]** We will not go into the same kind of detail,

**[1:42:00 – 1:42:03]** but it's really important to get the softmax function, right?

**[1:42:04 – 1:42:08]** So we will discuss the main assumption of the softmax.

**[1:42:08 – 1:42:10]** And then finally, we'll get the neural networks.

**[1:42:11 – 1:42:11]** I promise.

**[1:42:12 – 1:42:12]** Break.

**[1:42:13 – 2:03:22]** Okay, let's continue.

**[2:03:22 – 2:03:26]** We discussed linear regression before the break.

**[2:03:28 – 2:03:32]** We are gathering all through the slides.

**[2:03:35 – 2:03:38]** Linear regression, sum of squares,

**[2:03:39 – 2:03:44]** the Gaussian noise hypothesis, blah, blah, blah.

**[2:03:45 – 2:03:46]** We can get a posterior distribution.

**[2:03:46 – 2:03:47]** We can get the predictive distribution.

**[2:03:47 – 2:03:49]** We didn't get there, unfortunately.

**[2:03:51 – 2:03:56]** We didn't derive this formulas, no matter.

**[2:03:56 – 2:03:57]** This would be interesting,

**[2:03:58 – 2:04:00]** but I think it's time for us to move on.

**[2:04:02 – 2:04:07]** And our next point is classification,

**[2:04:07 – 2:04:10]** which is probably even more important

**[2:04:10 – 2:04:14]** for deep learning for neural networks

**[2:04:14 – 2:04:19]** than linear regression and predictive numbers.

**[2:04:20 – 2:04:26]** So our third point is the logistic regression.

**[2:04:27 – 2:04:30]** I'll try to be quick about it,

**[2:04:30 – 2:04:35]** but I do want to get the general idea across.

**[2:04:36 – 2:04:40]** So suppose that we are solving a classification problem.

**[2:04:41 – 2:04:42]** So what is classification?

**[2:04:42 – 2:04:45]** You want to distinguish cats from dogs,

**[2:04:45 – 2:04:49]** and if you are in a lower dimensional space,

**[2:04:49 – 2:04:53]** you can visualize it as trying to get

**[2:04:53 – 2:04:56]** a separating decision surface

**[2:04:56 – 2:04:59]** between two or more sets of points.

**[2:05:01 – 2:05:07]** The difference between classification and regression

**[2:05:07 – 2:05:11]** is in the nature of Y, right?

**[2:05:11 – 2:05:13]** It's in the nature of the target variable.

**[2:05:13 – 2:05:18]** So classification, of course, is still supervised learning.

**[2:05:18 – 2:05:23]** We still have a data set that looks like this.

**[2:05:23 – 2:05:27]** But now, for linear regression, YN was a number,

**[2:05:27 – 2:05:31]** but now YN is like a class label, right?

**[2:05:31 – 2:05:38]** So it's just a discrete variable with a finite set of values.

**[2:05:39 – 2:05:42]** It's one of several classes that we want to distinguish.

**[2:05:42 – 2:05:47]** So what does it mean for us for constructing the model,

**[2:05:47 – 2:05:49]** for building the likelihood, for everything like that?

**[2:05:50 – 2:05:53]** It means that since we are not predicting a number,

**[2:05:55 – 2:06:01]** what, I mean, okay, not just since we are not predicting a number,

**[2:06:03 – 2:06:10]** it means that in most cases, even though we are not predicting a number,

**[2:06:10 – 2:06:13]** we still do want to have a number at the output.

**[2:06:13 – 2:06:20]** So what is kind of bad about discrete target variables?

**[2:06:20 – 2:06:24]** And we will come back to that in deep learning as well.

**[2:06:25 – 2:06:28]** The bad thing about the discrete target variable,

**[2:06:28 – 2:06:34]** so let's say that I'm doing like a simple threshold rule for classifying

**[2:06:34 – 2:06:40]** and they have like one class is the zero and then if x exceeds some threshold,

**[2:06:41 – 2:06:43]** then I start to output one, right?

**[2:06:43 – 2:06:46]** So this is like the simplest classifier possible.

**[2:06:47 – 2:06:53]** One dimension, one input, two classes, and I choose by threshold.

**[2:06:55 – 2:07:00]** What's the problem with this function if it was my output?

**[2:07:00 – 2:07:07]** The problem is that this function, since it's piecewise constant,

**[2:07:07 – 2:07:10]** right, it has no derivatives.

**[2:07:10 – 2:07:14]** I mean, it does have derivatives, but its derivatives are zero everywhere.

**[2:07:14 – 2:07:21]** So what this actually means is that if, so if this is just x and this is,

**[2:07:21 – 2:07:25]** and the thing that I'm learning is only a, then it's fine.

**[2:07:25 – 2:07:33]** But what if the input is actually some kind of, as it always happens in real life,

**[2:07:33 – 2:07:38]** in neural networks and everywhere, what if the input is some kind of function of x with some weights,

**[2:07:38 – 2:07:42]** some model, some feature extractor, et cetera.

**[2:07:42 – 2:07:47]** If that happens, then we don't know what to do with this feature extractor.

**[2:07:47 – 2:07:49]** We don't know how to train it.

**[2:07:49 – 2:07:55]** Because we can take the gradients, and we will be taking gradients in the learning,

**[2:07:55 – 2:08:02]** but if you take the gradient of this function, it's always zero.

**[2:08:02 – 2:08:06]** It doesn't give us any information at all.

**[2:08:06 – 2:08:12]** And you can understand that intuitively as suppose that I take the weights w

**[2:08:12 – 2:08:16]** and I tweak them a little bit, I change them slightly.

**[2:08:16 – 2:08:21]** Then the input to this threshold will move a little bit.

**[2:08:21 – 2:08:25]** Did it move in the right direction or in the wrong direction?

**[2:08:25 – 2:08:28]** By looking at the output, we have absolutely no idea.

**[2:08:28 – 2:08:29]** The output does not change.

**[2:08:29 – 2:08:32]** It does not change, it does not change, it does not change,

**[2:08:32 – 2:08:34]** then suddenly it changes.

**[2:08:34 – 2:08:37]** That's not something that we can actually train through.

**[2:08:41 – 2:08:46]** So what we actually want, and both for this practical reason and also for

**[2:08:47 – 2:08:57]** conceptual reasons, like both for this practical reason and for conceptual reasons,

**[2:08:57 – 2:09:02]** like we also want to estimate our uncertainty, we want to evaluate how sure we are.

**[2:09:03 – 2:09:11]** What we actually want to have at the output of a classifier is not just the class label,

**[2:09:11 – 2:09:15]** but a probability distribution on the classes.

**[2:09:15 – 2:09:19]** So let's start with two classes.

**[2:09:19 – 2:09:32]** If I only have c1 and c2, what I actually want to have at the output is p of c1 given x.

**[2:09:32 – 2:09:36]** Okay, it's p of c1 given x.

**[2:09:38 – 2:09:40]** That is for a new point.

**[2:09:40 – 2:09:51]** I want to evaluate how likely it is that it belongs to the first class as opposed to the second.

**[2:09:51 – 2:09:58]** And where does the logistic regression appear? What's the reasoning behind it?

**[2:09:58 – 2:10:03]** Well, actually, it's pretty straightforward.

**[2:10:04 – 2:10:08]** Or, I mean, we could make it more complicated, but let's not.

**[2:10:09 – 2:10:14]** A straightforward reasoning behind the logistic regression looks like this.

**[2:10:14 – 2:10:17]** So let's assume that I want a linear model.

**[2:10:17 – 2:10:22]** So I do want to have a linear model, a linear separating surface.

**[2:10:22 – 2:10:29]** I do want something that includes w times x, and that's how x should appear in there.

**[2:10:29 – 2:10:34]** Yeah, good question.

**[2:10:34 – 2:10:41]** I also got a window that said internet is unstable.

**[2:10:41 – 2:10:43]** Did it fix itself?

**[2:10:43 – 2:10:45]** Is it okay now?

**[2:10:45 – 2:10:55]** One, two, one, two.

**[2:10:55 – 2:10:59]** Works right now, but sometimes the...

**[2:10:59 – 2:11:01]** Yeah, yeah, it's better now.

**[2:11:01 – 2:11:04]** But sometimes the writing is unintelligible.

**[2:11:06 – 2:11:13]** Okay, so, okay, if it's better now, then just keep me informed if anything changes.

**[2:11:15 – 2:11:25]** Okay, so anyway, suppose I want p and I want it to be derived

**[2:11:25 – 2:11:28]** from a linear function of the features.

**[2:11:28 – 2:11:36]** So I want the axes, the inputs to go through a linear function.

**[2:11:36 – 2:11:45]** So can I take this probability and approximate it like I did in linear regression with a linear function of the inputs?

**[2:11:45 – 2:11:48]** Kind of obviously not, right?

**[2:11:48 – 2:11:52]** Because the probability is a number between zero and one.

**[2:11:52 – 2:11:57]** And if I approximate it with a linear function, of course it will go to infinity.

**[2:11:57 – 2:12:00]** At one end, the other end, everywhere.

**[2:12:00 – 2:12:08]** So it's not a good idea to model probabilities by linear functions, right?

**[2:12:08 – 2:12:10]** What can I do instead?

**[2:12:10 – 2:12:14]** Well, I can use the base theorem.

**[2:12:14 – 2:12:21]** P of x given c1, P of c1, P of x, right?

**[2:12:23 – 2:12:26]** And then I can expand this.

**[2:12:27 – 2:12:32]** Since I only have two outcomes, two classes, it's pretty easy.

**[2:12:32 – 2:12:41]** I can just say that P of x is one possible numerator plus the other possible numerator, right?

**[2:12:41 – 2:12:47]** Now I have a lot of different things in here and I only want to model one thing.

**[2:12:47 – 2:13:04]** So let me divide by the numerator and I get 1 over 1 plus P of x given c2, P of c2 divided by P of x given c1 times P of c1, okay?

**[2:13:04 – 2:13:15]** So this thing, you can view it as P of c2 given x divided by P of c1 given x, it's the same thing.

**[2:13:15 – 2:13:20]** And this thing is known as the odds, right?

**[2:13:20 – 2:13:29]** So the odds are, well, like when you say in real life, when you say I give you 50 to 1 odds,

**[2:13:29 – 2:13:32]** what does 50 to 1 mean mathematically?

**[2:13:32 – 2:13:33]** It's this ratio, right?

**[2:13:33 – 2:13:40]** It's the ratio of the probability you assign to one outcome divided by the probability you assign to the other outcome.

**[2:13:40 – 2:13:43]** That's what it means to give odds.

**[2:13:43 – 2:13:49]** And as I just said, odds can be like 50 to 1 or 1 to 50.

**[2:13:49 – 2:13:53]** Right? So odds are not constrained by 1.

**[2:13:53 – 2:13:56]** They are ratio of two probabilities, so they can go to infinity.

**[2:13:56 – 2:14:03]** But does it make sense to model them as a linear function?

**[2:14:03 – 2:14:06]** Well, again, not really.

**[2:14:06 – 2:14:13]** Because even though they can go to infinity, they still cannot be negative.

**[2:14:13 – 2:14:16]** Right? It's a ratio of two probabilities.

**[2:14:16 – 2:14:18]** And the linear function will be negative somewhere.

**[2:14:18 – 2:14:20]** But half of the space it will be negative.

**[2:14:20 – 2:14:26]** So this is also not a natural thing to model with a linear function.

**[2:14:26 – 2:14:28]** But we are getting there.

**[2:14:28 – 2:14:30]** Just one small step left.

**[2:14:30 – 2:14:34]** We have a positive quantity and we want to model it somehow linearly.

**[2:14:35 – 2:14:37]** What is the transformation that we need?

**[2:14:37 – 2:14:41]** Well, we can take the log again, right?

**[2:14:41 – 2:14:47]** So if you take the log of something that goes from zero to infinity, not including zero,

**[2:14:47 – 2:14:51]** then now you get something that goes from negative infinity to infinity.

**[2:14:51 – 2:14:58]** So then we go to this, e to the power, it's customary to put a minus sign here.

**[2:14:58 – 2:15:01]** It doesn't really matter, but usually people do.

**[2:15:03 – 2:15:12]** So now the fraction flips, ratio flips, p of c2.

**[2:15:12 – 2:15:21]** So this guy is called the log odds, the logarithm of the odds.

**[2:15:21 – 2:15:28]** And now this indeed does make sense to model with a linear function,

**[2:15:28 – 2:15:31]** because now it's a quantity that goes from negative infinity to infinity,

**[2:15:31 – 2:15:33]** and it has exactly the properties that we want.

**[2:15:34 – 2:15:39]** At negative infinity, you go to zero, the probability goes to zero.

**[2:15:39 – 2:15:42]** At positive infinity, the probability goes to one.

**[2:15:42 – 2:15:46]** And in between, it monotonically increases.

**[2:15:46 – 2:15:51]** So logistic regression is exactly this model.

**[2:15:51 – 2:16:00]** Logistic regression is the model where you say that p of c1 given x is

**[2:16:00 – 2:16:08]** one over one plus e to the power minus a linear function of x.

**[2:16:08 – 2:16:14]** This function is called the logistic sigmoid.

**[2:16:14 – 2:16:20]** So sigma of a is like one over one plus e to the power minus a.

**[2:16:20 – 2:16:25]** And it's this, it's a sigmoid function, right?

**[2:16:25 – 2:16:28]** So it goes from negative infinity to infinity.

**[2:16:28 – 2:16:34]** It goes through one half at zero and it asymptotically

**[2:16:34 – 2:16:37]** goes to one on the right and to zero on the left.

**[2:16:37 – 2:16:42]** It's an important function in machinery.

**[2:16:42 – 2:16:46]** Then we get what is p of c2 given x.

**[2:16:46 – 2:16:48]** Well, unfortunately, it's a bit more complicated

**[2:16:48 – 2:16:53]** because it's one minus sigma of w times x, right?

**[2:16:53 – 2:17:05]** So if I try to do like the likelihood of a dataset for logistic regression,

**[2:17:05 – 2:17:11]** again, I do a product of p of y n given w and x n,

**[2:17:11 – 2:17:16]** but then it will be a product of like sometimes it's sigma

**[2:17:16 – 2:17:18]** and sometimes it's one minus sigma,

**[2:17:18 – 2:17:21]** and then it's sigma, and then it's sigma,

**[2:17:21 – 2:17:24]** and then it's one minus sigma and so on, right?

**[2:17:24 – 2:17:26]** So it's a bit more complicated.

**[2:17:26 – 2:17:29]** It's a more complicated function than the linear regression.

**[2:17:31 – 2:17:33]** It's not quadratic, of course, anymore,

**[2:17:33 – 2:17:36]** and we cannot do it in closed form,

**[2:17:36 – 2:17:39]** but we can do something like gradient descent

**[2:17:39 – 2:17:42]** or second-order methods in this case also can be used.

**[2:17:43 – 2:17:46]** We can actually optimize the likelihood.

**[2:17:46 – 2:17:49]** We can add priors and do it in a regularized way,

**[2:17:49 – 2:17:50]** and so on and so forth.

**[2:17:50 – 2:17:57]** So this is actually a linear model in machine learning and statistics.

**[2:17:57 – 2:18:01]** A linear model is something that is a function of this.

**[2:18:01 – 2:18:04]** It doesn't have to be linear all the way,

**[2:18:04 – 2:18:09]** but axes occur in there as a linear combination.

**[2:18:10 – 2:18:16]** And it's a very natural linear model for binary classification.

**[2:18:16 – 2:18:20]** How do we make it more than binary?

**[2:18:20 – 2:18:24]** How do we insert several classes here?

**[2:18:24 – 2:18:29]** Well, here I was just modeling one quantity.

**[2:18:29 – 2:18:35]** And if I have basically a coin toss, if I have only two classes, then sure,

**[2:18:35 – 2:18:37]** I only need to model one probability.

**[2:18:37 – 2:18:52]** But if I have several classes, c1, c2, ck, then now it's not enough to have only one vector, w,

**[2:18:52 – 2:18:53]** that is multiplied by x.

**[2:18:53 – 2:18:58]** Because from one number, I will not get k minus one different numbers, right?

**[2:18:58 – 2:19:03]** And I need k minus one different numbers to model this die roll between k classes.

**[2:19:03 – 2:19:12]** So instead, now I basically say that, okay, I will not model a single logout for between two classes.

**[2:19:12 – 2:19:18]** I will just, I will say this.

**[2:19:18 – 2:19:28]** So p of c small k given x, just like this, it's p of c small k, p of x given c small k,

**[2:19:28 – 2:19:31]** divided by the sum overall classes, right?

**[2:19:31 – 2:19:37]** p of c s, p of x given c s.

**[2:19:37 – 2:19:44]** And let me just, again, take the logs, so I can also have negative numbers.

**[2:19:44 – 2:19:55]** So e to the power of this divided by the sum of e to the power of the same, but about class s.

**[2:19:55 – 2:20:03]** And then let me just say that now I'm modeling every exponent here with its own linear function.

**[2:20:03 – 2:20:17]** So I'm saying that w k times x should be like p of ck times p of x given ck.

**[2:20:17 – 2:20:25]** Notice that it doesn't quite work as I wrote it because the thing on the right cannot be negative.

**[2:20:25 – 2:20:28]** They just said it's a bad thing.

**[2:20:28 – 2:20:30]** But to be honest, it doesn't matter.

**[2:20:30 – 2:20:37]** So when you get negative numbers from some of the scores,

**[2:20:37 – 2:20:41]** These are usually called scores or affinities or something like that.

**[2:20:41 – 2:20:46]** So it's like a measure of how likely class k is, but not a probability, just a number.

**[2:20:48 – 2:20:58]** So when you get negative scores, you can just cancel out the negative parts.

**[2:20:58 – 2:21:09]** So if you have e to the power minus 2 divided by e to the power 1 plus e to the power minus 1 plus e to the power minus 2, the same,

**[2:21:09 – 2:21:13]** then you can just take e to the power minus 2 and cancel it out, right?

**[2:21:13 – 2:21:15]** So and everything becomes non-negative.

**[2:21:15 – 2:21:20]** Like now it's e to the power 0, e to the power 3 plus e1 plus e0.

**[2:21:20 – 2:21:21]** That's it, right?

**[2:21:21 – 2:21:26]** So you can always, in this formula, it doesn't matter if sometimes you get negatives

**[2:21:26 – 2:21:30]** because you can always add a baseline like this and it just cancels out.

**[2:21:32 – 2:21:33]** And that's it.

**[2:21:34 – 2:21:38]** So this is how you do multi-class classification.

**[2:21:39 – 2:21:42]** And this thing, now it's a vector function, right?

**[2:21:42 – 2:21:51]** So now it's a function that maps the vector a to another vector full of these guys.

**[2:21:51 – 2:22:00]** So like the kth coordinate is e to the power ak divided by the sum of e to the power as, right?

**[2:22:01 – 2:22:03]** Normalized exponents.

**[2:22:05 – 2:22:07]** And this is called the softmax function.

**[2:22:08 – 2:22:13]** So the softmax of, okay, let me write it again.

**[2:22:13 – 2:22:17]** A1 and a2 ak is another vector.

**[2:22:18 – 2:22:25]** And at the kth spot, we have e to the power ak normalized so that it becomes a vector of probabilities.

**[2:22:26 – 2:22:26]** That's it.

**[2:22:27 – 2:22:28]** So that's the softmax.

**[2:22:29 – 2:22:31]** Why is it called the softmax?

**[2:22:31 – 2:22:38]** Because the exponents have this tendency to, you know, exaggerate the differences.

**[2:22:38 – 2:22:47]** Like if you have one of the A's, one of the arguments, to be significantly larger than the others,

**[2:22:48 – 2:22:55]** then what you get as a result will be basically probability 1 for this guy and probability about 0 for the others.

**[2:22:55 – 2:23:04]** So we are kind of taking the maximum of the arguments, but we are doing it in a soft way,

**[2:23:04 – 2:23:10]** as a continuous function that is never exactly 0, that you can take derivatives of,

**[2:23:10 – 2:23:14]** that allows for gradients, gradient descent, et cetera, et cetera.

**[2:23:14 – 2:23:22]** So that's a soft version of taking the argmax, okay?

**[2:23:22 – 2:23:28]** And I won't go into more details about logistic regression, not exactly our subject,

**[2:23:28 – 2:23:37]** but this part is important because, again, this is the last layer of almost every neural network.

**[2:23:37 – 2:23:46]** If you have, I don't know, GPT-5, which is an insanely complicated model,

**[2:23:46 – 2:23:49]** I have no idea how exactly it works because nobody tells us,

**[2:23:49 – 2:23:56]** but if you have GPT-5 and it's a language model and it's supposed to produce the next token right now,

**[2:23:56 – 2:24:00]** then what is the last layer of GPT-5, I'm sure?

**[2:24:00 – 2:24:02]** The last layer is this.

**[2:24:02 – 2:24:05]** After all of this internal machinery, which is very complicated,

**[2:24:05 – 2:24:18]** we get a layer of scores for every token and then they go through the softmax

**[2:24:18 – 2:24:25]** and the softmax turns them into the probabilities of tokens.

**[2:24:25 – 2:24:37]** That's how it always works at the end because it's completely hopeless to try to produce probabilities immediately.

**[2:24:37 – 2:24:43]** It's not how neural networks work, it's not how linear functions work, it's not how anything works.

**[2:24:43 – 2:24:52]** What you do is you produce some kind of scores and then you turn them into probabilities with the softmax.

**[2:24:52 – 2:25:01]** And yeah, sure, it's also very common, now I cannot vouch for GPT-5, but it's also very common that the layer before this is linear.

**[2:25:01 – 2:25:08]** So we get an exact logistic regression at the end of a neural network.

**[2:25:08 – 2:25:24]** So we get to some features, when we do a linear layer that gets - so okay, let me explain, because I don't think I will explain it later, and now is a good spot.

**[2:25:24 – 2:25:36]** So we have some input, it goes through the neural network, and then let's say we get to the final feature vector, right?

**[2:25:36 – 2:25:43]** To the final, like, semantically rich, very intricate extracted features.

**[2:25:43 – 2:25:47]** And whether it's a cat or a dog is already somewhere inside.

**[2:25:47 – 2:25:55]** Somewhere in these features it says so pretty explicitly, but we are still not sure where, and we are not sure how to get, right?

**[2:25:55 – 2:26:04]** So how do we do it, what is the simplest way to process these already extracted features?

**[2:26:04 – 2:26:10]** Well, I could just do a softmax and assume they are scores.

**[2:26:10 – 2:26:14]** They are not scores, and there's probably the wrong number of them, right?

**[2:26:14 – 2:26:23]** So there is some number of classes, and here I have just extracted features that express my picture.

**[2:26:23 – 2:26:26]** Why should the numbers match? No reason, right?

**[2:26:26 – 2:26:28]** So the number of features can be different.

**[2:26:28 – 2:26:31]** So I do a weight matrix.

**[2:26:31 – 2:26:38]** I multiply W times Z, and the weight matrix, so let's say this is dimension D,

**[2:26:38 – 2:26:41]** and this is dimension K, like number of classes.

**[2:26:41 – 2:26:51]** So W is of dimension D times K, and then W times Z becomes the vector of scores.

**[2:26:51 – 2:27:04]** And now I go through Softmax, and I get a vector of probabilities for all the classes that I have.

**[2:27:04 – 2:27:14]** And this is my output, and the loss function now will be defined on these probabilities.

**[2:27:14 – 2:27:19]** There may be some variation here, but usually the loss function is just the...

**[2:27:19 – 2:27:21]** Well, it's a fancy name.

**[2:27:21 – 2:27:29]** It's the cross-entropy between the output and the target.

**[2:27:29 – 2:27:44]** But if you're doing classification, the target looks like a one-hot vector with one one at the correct class and zeros on the other classes, right?

**[2:27:44 – 2:27:58]** So, and the cross-entropy, when we get there, I will write it in more detail, but the cross-entropy for this kind of target will be basically just saying that I want to have the probability of the correct class to be larger.

**[2:27:58 – 2:28:11]** So, like, the loss function will be something like the negative log P of the correct class, and I want this to be lower, according.

**[2:28:14 – 2:28:15]** And that's it.

**[2:28:16 – 2:28:19]** That's how classification works in deep learning, okay?

**[2:28:20 – 2:28:24]** So, the interesting stuff happens over here, of course.

**[2:28:24 – 2:28:27]** That's what we are going to be discussing for the rest of the class.

**[2:28:27 – 2:28:32]** But at the end, almost inevitably, happens something like this.

**[2:28:32 – 2:28:39]** So, at the end, if you are doing classification, you want a vector of probabilities at the output.

**[2:28:40 – 2:28:42]** Can you get a vector of probabilities directly?

**[2:28:42 – 2:28:43]** Probably not.

**[2:28:43 – 2:28:49]** What you can get is a vector of scores, affinities, like numbers that can be arbitrary,

**[2:28:49 – 2:28:55]** but that reflect how well the input matches one of the classes, and then you convert them to probabilities.

**[2:28:56 – 2:28:58]** That's how this stuff works.

**[2:29:00 – 2:29:04]** Okay, any questions about logistic regression?

**[2:29:04 – 2:29:06]** I didn't go into much detail.

**[2:29:10 – 2:29:10]** All right, then.

**[2:29:11 – 2:29:20]** Then, for the rest of today's lecture, let's concentrate on neural networks.

**[2:29:20 – 2:29:23]** Oh, actually, wait one second, I'll check.

**[2:29:23 – 2:29:34]** Yeah, I don't have illustrations for classification code, but that's fine.

**[2:29:34 – 2:29:37]** It wouldn't show you anything anyway.

**[2:29:37 – 2:29:41]** It would be just a linear surface between two classes, or three classes.

**[2:29:41 – 2:29:43]** What's the point?

**[2:29:45 – 2:29:47]** Yeah, so we discussed logistic regression.

**[2:29:48 – 2:29:51]** This is what a logistic sigmoid looks like.

**[2:29:52 – 2:29:55]** Then we get logistic regression.

**[2:29:55 – 2:29:57]** This is the softmax function.

**[2:29:57 – 2:30:01]** This is what we model for the softmax, etc., etc.

**[2:30:01 – 2:30:08]** And logistic regression, even though it's a very simple model,

**[2:30:09 – 2:30:13]** it's a linear model, like one step from linear regression.

**[2:30:13 – 2:30:15]** So linear regression is just linear.

**[2:30:15 – 2:30:18]** This one is linear plus a sigmoid on top.

**[2:30:19 – 2:30:22]** But already for logistic regression,

**[2:30:23 – 2:30:27]** we cannot really hope to get a closed-form solution.

**[2:30:27 – 2:30:33]** So we didn't discuss it for linear regression

**[2:30:33 – 2:30:39]** because it really doesn't pertain to deep learning.

**[2:30:39 – 2:30:43]** But when you're optimizing a quadratic function like this,

**[2:30:43 – 2:30:45]** you can just write down the answer.

**[2:30:46 – 2:30:49]** It will be maybe not that easy to actually implement

**[2:30:49 – 2:30:53]** because it will be like the inverse of some huge matrix.

**[2:30:54 – 2:30:58]** And in practice, you would be solving the system of linear equations

**[2:30:58 – 2:31:04]** with some approximate techniques, iterative approximate techniques.

**[2:31:04 – 2:31:06]** I mean, it's a whole science.

**[2:31:07 – 2:31:09]** But theoretically, you can just write down the answer.

**[2:31:09 – 2:31:10]** You can write down the formula.

**[2:31:11 – 2:31:14]** It's a system of linear equations after you take the gradient.

**[2:31:16 – 2:31:19]** Here, it's already not.

**[2:31:20 – 2:31:23]** So if you look at a big product and you take a log

**[2:31:23 – 2:31:28]** and then you have a big sum of logs of things like this and things like this,

**[2:31:28 – 2:31:30]** there is no closed-form solution.

**[2:31:31 – 2:31:40]** So the only thing we can do is try to do it with some iterative optimization algorithm.

**[2:31:42 – 2:31:47]** And the main iterative optimization algorithm that we will be discussing tomorrow in great detail

**[2:31:47 – 2:31:49]** is, of course, gradient descent.

**[2:31:49 – 2:31:56]** So in logistic regression, you can actually do a second-order method,

**[2:31:56 – 2:31:59]** but in neural networks, you can't afford to.

**[2:31:59 – 2:32:00]** We'll discuss that as well.

**[2:32:00 – 2:32:05]** And we have to restrict ourselves to variations of gradient descent.

**[2:32:06 – 2:32:08]** Gradient descent is when you start somewhere

**[2:32:08 – 2:32:17]** and you go in the direction where the loss function is being reduced most quickly.

**[2:32:18 – 2:32:20]** And that is the direction opposite to the gradient.

**[2:32:20 – 2:32:23]** So gradient is the direction where it grows most quickly.

**[2:32:23 – 2:32:26]** So the opposite is where it decreases most quickly.

**[2:32:28 – 2:32:33]** And then you keep going until you find the local minimum.

**[2:32:33 – 2:32:38]** There can be many local minima in real life, in neural networks, etc.

**[2:32:38 – 2:32:45]** And we'll discuss that in detail, but not for logistic regression.

**[2:32:46 – 2:32:47]** All right.

**[2:32:47 – 2:32:53]** So with that, let me move on to some less mathematical, far less mathematical topic,

**[2:32:53 – 2:32:55]** but I hope also pretty interesting.

**[2:32:56 – 2:33:00]** And that is an introduction to deep learning.

**[2:33:00 – 2:33:05]** I will, again, try to make it quick and painless.

**[2:33:05 – 2:33:08]** I don't want to go into too many historical details or anything.

**[2:33:09 – 2:33:13]** But there are a few things that I want to highlight.

**[2:33:13 – 2:33:23]** A few things in the motivations, a few things in the, like, how neural networks evolved.

**[2:33:23 – 2:33:28]** And then we'll just go to the main meat of our class.

**[2:33:28 – 2:33:29]** That will be probably tomorrow.

**[2:33:30 – 2:33:40]** So neural networks, artificial neural networks, are called artificial because there are natural neural networks, right?

**[2:33:40 – 2:33:45]** There are neural networks in our brains and in the brains of other living beings.

**[2:33:47 – 2:33:59]** And, of course, a very natural motivation for a scientist would be, well, I want to build a thinking machine.

**[2:34:01 – 2:34:03]** There already are thinking machines in the world.

**[2:34:03 – 2:34:05]** I have a proof of concept right here.

**[2:34:06 – 2:34:13]** So let me study how the thinking machine in here works, and let's try to emulate it in a computer.

**[2:34:13 – 2:34:14]** Why not?

**[2:34:14 – 2:34:15]** It's all information process.

**[2:34:15 – 2:34:26]** And when you begin to study how the human brain works, it actually gives you some pretty important insights.

**[2:34:27 – 2:34:29]** So, oh, sorry, my picture.

**[2:34:30 – 2:34:33]** Now, this is not an artifact of internet connection for some reason.

**[2:34:33 – 2:34:35]** It is downsampled a lot.

**[2:34:35 – 2:34:45]** But anyway, you probably have heard at some point how neurons work, what a neuron is.

**[2:34:45 – 2:34:48]** So our brain consists of neurons.

**[2:34:49 – 2:34:51]** Biologists will tell you that there are different kinds of neurons.

**[2:34:52 – 2:34:53]** There are slight differences.

**[2:34:53 – 2:34:57]** But from our computational perspective, they are basically all the same.

**[2:34:58 – 2:35:00]** And they work like this.

**[2:35:01 – 2:35:07]** They have this processing part, the soma, the actual center of the cell.

**[2:35:08 – 2:35:21]** And then it has all sorts of tentacles, all sorts of little things going out of the cell

**[2:35:21 – 2:35:22]** and connecting to other things.

**[2:35:23 – 2:35:28]** And there are two kinds of tendrils, I guess the better word would be.

**[2:35:29 – 2:35:34]** There are two kinds of this growth.

**[2:35:35 – 2:35:39]** There are dendrites, which are relatively short,

**[2:35:39 – 2:35:44]** and which attach to the outputs of other neurons,

**[2:35:44 – 2:35:46]** and they provide the inputs.

**[2:35:47 – 2:35:51]** So there are many dendrites, like thousands for every neuron,

**[2:35:52 – 2:35:57]** and the dendrites get inputs for this neuron.

**[2:35:57 – 2:36:05]** And then there is one special part, one special tentacle of the neuron,

**[2:36:06 – 2:36:08]** which is called the axon.

**[2:36:08 – 2:36:10]** And the axon can be very long.

**[2:36:10 – 2:36:17]** There is a neuron in your spinal cord that goes all the way to your toe,

**[2:36:17 – 2:36:19]** to every one of your toes, actually.

**[2:36:19 – 2:36:20]** There are separate neurons.

**[2:36:21 – 2:36:26]** So they can be up to a meter in length or something.

**[2:36:26 – 2:36:31]** And the point is, the axon is the output.

**[2:36:32 – 2:36:35]** So computationally, every neuron has lots of inputs,

**[2:36:35 – 2:36:39]** several thousands on average, and one output.

**[2:36:39 – 2:36:44]** So far, pretty straightforward.

**[2:36:45 – 2:36:47]** Now, what is interesting about this,

**[2:36:48 – 2:36:52]** and this is a purely computational,

**[2:36:52 – 2:36:56]** very surface-like insight,

**[2:36:56 – 2:36:57]** but it's already pretty interesting.

**[2:36:59 – 2:36:59]** In the brain,

**[2:37:02 – 2:37:05]** so first of all, how does a neuron work physically?

**[2:37:05 – 2:37:06]** How does it send signals?

**[2:37:08 – 2:37:13]** It would be pretty difficult for a biological thing,

**[2:37:13 – 2:37:17]** for a biological mechanism to read out numbers.

**[2:37:18 – 2:37:23]** So it would be pretty difficult for the dendrites

**[2:37:23 – 2:37:28]** to capture the exact amplitude of an electrical signal

**[2:37:28 – 2:37:31]** and then process inside the neuron

**[2:37:31 – 2:37:35]** that from this input I got a 2.5,

**[2:37:35 – 2:37:37]** and from that input I got negative 1.46.

**[2:37:38 – 2:37:40]** That's not how biology works.

**[2:37:42 – 2:37:44]** Biologically, it's much easier and faster

**[2:37:44 – 2:37:48]** and more reliable to just capture bits,

**[2:37:48 – 2:37:50]** individual events, like is there a spike

**[2:37:50 – 2:37:52]** or is there not a spike?

**[2:37:53 – 2:37:55]** So neurons work actually in spikes.

**[2:37:56 – 2:37:59]** They do not or almost do not modulate

**[2:37:59 – 2:38:01]** the amplitude of their signals.

**[2:38:02 – 2:38:03]** Was it a spike? Yeah, I didn't tell.

**[2:38:03 – 2:38:05]** A spike is the electrical signal

**[2:38:05 – 2:38:08]** that the neuron sends out through its exon.

**[2:38:09 – 2:38:14]** So the neuron always fires spikes along its exons.

**[2:38:14 – 2:38:17]** And the other neurons who are attached to it,

**[2:38:17 – 2:38:18]** they pick up the signals.

**[2:38:20 – 2:38:23]** And the spikes are more or less the same.

**[2:38:23 – 2:38:24]** I think there is some variation,

**[2:38:25 – 2:38:26]** but it's not consequential.

**[2:38:27 – 2:38:28]** They are more or less the same.

**[2:38:29 – 2:38:31]** What changes is the frequency of the spikes.

**[2:38:32 – 2:38:37]** So if the neuron is relaxed, is not excited,

**[2:38:37 – 2:38:40]** then it sends out spikes with frequency

**[2:38:40 – 2:38:44]** like 10 per second, 20 per second, something like this.

**[2:38:44 – 2:38:47]** When it gets really excited, really activated,

**[2:38:47 – 2:38:51]** it starts sending out spikes with the frequency

**[2:38:51 – 2:38:54]** of like 200 spikes per second, okay?

**[2:38:54 – 2:38:56]** So there is a big range.

**[2:38:57 – 2:39:02]** And when a neuron sends out spikes more often,

**[2:39:02 – 2:39:04]** it means it's more excited.

**[2:39:04 – 2:39:07]** So now there is actually a numerical value.

**[2:39:07 – 2:39:09]** It can be more excited or less excited.

**[2:39:09 – 2:39:09]** It's not binary.

**[2:39:10 – 2:39:12]** But every spike is the same,

**[2:39:12 – 2:39:14]** and it's just transmitting basically one bit,

**[2:39:14 – 2:39:16]** but at different intervals.

**[2:39:19 – 2:39:26]** The interesting point about this is that we have lots,

**[2:39:27 – 2:39:28]** lots and lots of neurons.

**[2:39:29 – 2:39:32]** I think artificial neural networks still haven't reached

**[2:39:32 – 2:39:35]** the sheer number of neurons of the human brain,

**[2:39:35 – 2:39:37]** or maybe have just reached it, I'm not sure.

**[2:39:38 – 2:39:45]** So in the human brain, we have like 100 billion...

**[2:39:45 – 2:39:46]** No, okay.

**[2:39:47 – 2:39:48]** Yeah, yeah, right.

**[2:39:48 – 2:39:50]** We have like 100 billion neurons,

**[2:39:50 – 2:39:54]** and every neuron...

**[2:39:54 – 2:39:56]** So you know that there are neural networks

**[2:39:56 – 2:39:58]** with 100 billion and trillion weights, right?

**[2:39:59 – 2:40:00]** But the weight is not a neuron.

**[2:40:01 – 2:40:05]** The weight in the biological brain

**[2:40:05 – 2:40:08]** is on the connection between the neurons, right?

**[2:40:09 – 2:40:15]** So the weights are in the synapses,

**[2:40:16 – 2:40:19]** in these connections where a dendrite of one neuron

**[2:40:19 – 2:40:20]** attaches to the axon of another.

**[2:40:21 – 2:40:24]** And yes, there are weights there.

**[2:40:24 – 2:40:26]** So it really, in some way,

**[2:40:26 – 2:40:28]** it's like a linear combination.

**[2:40:28 – 2:40:30]** Not really, but like.

**[2:40:30 – 2:40:33]** So there are connections that get reinforced.

**[2:40:33 – 2:40:35]** There are connections that get inhibited.

**[2:40:35 – 2:40:36]** There can be negative weights.

**[2:40:36 – 2:40:38]** There are all sorts of things.

**[2:40:38 – 2:40:40]** So there are indeed weights at the synapses

**[2:40:40 – 2:40:43]** that are learned, that are trained in the human brain.

**[2:40:44 – 2:40:45]** And that's how we think.

**[2:40:45 – 2:40:46]** That's how we learn stuff.

**[2:40:47 – 2:40:49]** But the point is,

**[2:40:49 – 2:40:52]** how many weights are there in the human brain?

**[2:40:52 – 2:40:53]** How many parameters?

**[2:40:54 – 2:40:56]** Well, we have like 100 billion neurons,

**[2:40:57 – 2:41:01]** and each one on average has several thousand synapses,

**[2:41:01 – 2:41:02]** like 7,000 synapses on average.

**[2:41:03 – 2:41:05]** So if you multiply, you get something like,

**[2:41:06 – 2:41:12]** what's the quintillion or a bit less than a quintillion of synapses,

**[2:41:13 – 2:41:15]** of weights that are being trained in our brain.

**[2:41:16 – 2:41:17]** That's a huge amount.

**[2:41:17 – 2:41:20]** I think artificial neural networks have not yet reached that.

**[2:41:20 – 2:41:28]** But on the other hand, it's extremely slow, right?

**[2:41:28 – 2:41:31]** So I just told you that our brain is a computer

**[2:41:31 – 2:41:44]** that operates on the frequency of 10 to a couple hundred hertz, right?

**[2:41:44 – 2:41:47]** A couple hundred signals per second,

**[2:41:48 – 2:41:51]** not megahertz, not kilohertz, just hertz.

**[2:41:52 – 2:41:56]** And so the brain is very, very slow as a computer,

**[2:41:57 – 2:41:59]** if you were talking about clock speeds,

**[2:41:59 – 2:42:05]** but it's huge in terms of the number of connections.

**[2:42:06 – 2:42:12]** And what this actually means is the brain

**[2:42:12 – 2:42:16]** always performs highly parallel computations,

**[2:42:16 – 2:42:19]** but cannot perform a long sequential computation.

**[2:42:20 – 2:42:21]** It simply doesn't have time.

**[2:42:21 – 2:42:25]** So for example, we recognize a face.

**[2:42:25 – 2:42:28]** Recognizing a face is a difficult task in computer vision.

**[2:42:28 – 2:42:29]** It's a difficult task.

**[2:42:29 – 2:42:32]** But we recognize a face in like a couple hundred milliseconds.

**[2:42:33 – 2:42:39]** And that's like the full cycle of between the time when I show you the face

**[2:42:39 – 2:42:48]** and the time when you press a button to record that you have recognized the face.

**[2:42:48 – 2:42:53]** So it's the full cycle of feature extraction, decision-making,

**[2:42:54 – 2:42:56]** motor command to the finger, everything.

**[2:42:56 – 2:43:00]** And it all fits into like 200 or 300 milliseconds.

**[2:43:00 – 2:43:08]** So what this actually means is that this is an actual picture of how it goes through the brain.

**[2:43:08 – 2:43:13]** Maybe we will get back to this picture when we discuss CNNs, but maybe not.

**[2:43:13 – 2:43:23]** And what this actually means is that the brain cannot have like a loop for I from 1 to 1,000.

**[2:43:23 – 2:43:26]** It doesn't have time to do it.

**[2:43:26 – 2:43:33]** It only has time for like 10 or 15 sequential steps of computation.

**[2:43:33 – 2:43:36]** And then it has to get the answer out.

**[2:43:36 – 2:43:40]** Otherwise, you are already being eaten by a lamb, right?

**[2:43:40 – 2:43:49]** And so the computations are not sequential, but they are very, very highly parallel.

**[2:43:49 – 2:43:54]** So when we are recognizing a face, it's like half of our brain lights up.

**[2:43:54 – 2:44:01]** But half of our brain lights up, but it lights up in like 10 steps, sequentially.

**[2:44:01 – 2:44:07]** And then we have to give the answer.

**[2:44:07 – 2:44:15]** In a way, this is the property of the brain that we actually keep in artificial neural networks.

**[2:44:15 – 2:44:21]** So we will discuss how to make neural networks really, really deep.

**[2:44:21 – 2:44:25]** We will discuss networks with hundreds of layers.

**[2:44:25 – 2:44:30]** And I will tell you that you can go to thousands, it just doesn't make sense.

**[2:44:30 – 2:44:33]** And yeah, it doesn't make sense.

**[2:44:33 – 2:44:43]** In actuality, our current artificial neural networks, okay, maybe they have more than 10 or 20 layers, maybe they have 100, but not much more than that.

**[2:44:43 – 2:44:49]** So we don't know how to make use of tens of thousands of layers in the neural network.

**[2:44:49 – 2:45:00]** And let's say the proverbial GPT-5 is probably very, very wide, it's probably like a mixture of experts that have been trained to do different things, blah, blah, blah.

**[2:45:00 – 2:45:13]** But in terms of the number of layers of sequential computations, it's probably like a few dozen, maybe a couple of hundred, not more, I'm pretty sure.

**[2:45:13 – 2:45:34]** So this kind of wide but shallow thing we will keep, but the main part of the motivation is not, of course, in the architecture, we will see that the architecture cannot be the same, it's by definition kind of very different.

**[2:45:34 – 2:46:03]** But what we actually want to get from, what is the part of the motivation that we actually want to reproduce in computers is how versatile, how adaptive, how elastic our brain is.

**[2:46:03 – 2:46:12]** So we can learn on very few examples and we can learn some very, very complicated stuff on very small data samples.

**[2:46:12 – 2:46:28]** We can adapt to new data sources. There are experiments like this one where you can actually learn to see with your tongue or something. This is called neuroplasticity. And this was a fun experiment.

**[2:46:28 – 2:46:41]** You make a small plate of electrodes and it's the tongue just because the tongue is sensitive and you can actually distinguish between a lot of electrodes on the tongue.

**[2:46:41 – 2:46:51]** But it doesn't matter. You just put it somewhere on you and then you send to the electrodes a signal from a camera at your forehead.

**[2:46:51 – 2:46:56]** And then you just walk around and you feel a slight tingling from the electricity.

**[2:46:56 – 2:47:01]** And then you stop feeling it, of course, very soon because the brain adapts and stops noticing it.

**[2:47:01 – 2:47:15]** But in a few days of walking around with this camera, your brain starts to notice that there is an actual correlation between what you see and what this tingling looks like.

**[2:47:15 – 2:47:29]** And there have been experiments that after a couple of weeks of walking around with this stuff, you can actually close your eyes and see through this electrode plate.

**[2:47:29 – 2:47:34]** Maybe not read books, but at least walk around and not bump into walls differently.

**[2:47:34 – 2:47:56]** And for example, you probably have heard of neuroplasticity examples like when somebody has a stroke and part of the brain stops working, sometimes it's too much of a damage and the person never recovers, but sometimes they recover.

**[2:47:56 – 2:48:09]** Sometimes other parts of the brain take on the functions that were previously done by this now missing part and that's also something that our brain can do.

**[2:48:09 – 2:48:23]** So, in a way, this kind of experiments tell us that the brain, yes, it does have predetermined areas, predetermined by evolution.

**[2:48:23 – 2:48:38]** Like, yes, we have our visual cortex is back there in the occipital lobe of the brain, our frontal cortex is usually doing the reasoning and the decision-making, yes.

**[2:48:38 – 2:48:47]** But it's kind of incidental. So, yeah, sure, it evolves to be this way, but the neurons are still the same.

**[2:48:47 – 2:48:59]** And there is some kind of a single learning algorithm inside the human brain that can be applied to all of these sorts of different situations.

**[2:48:59 – 2:49:05]** There are no neurons in the brain that have evolved to distinguish cats from dogs. This is a learned thing, of course.

**[2:49:05 – 2:49:21]** And there are no neurons in the brain that are from birth originally evolved to already distinguish, to already understand the 3D structure of the world around us, like computer vision is supposed to do.

**[2:49:21 – 2:49:27]** No, that cannot be written in the genes. There is not enough information in the genes to write it down.

**[2:49:27 – 2:49:34]** This is all learned. This is all learned from scratch. And this is learned with very high efficiency in the early stages of our life.

**[2:49:34 – 2:49:42]** So we do want to have it in computers. That was the original motivation for neural networks.

**[2:49:42 – 2:50:01]** And as we will see, in artificial neural networks, we do keep this general idea which is known as connectionism.

**[2:50:01 – 2:50:17]** Connectionism is part philosophical, part mathematical idea that if you connect a lot of simple things together, the huge composition of very simple things becomes very complicated and can do very interesting stuff.

**[2:50:17 – 2:50:31]** It's as simple as it gets and it's true, right? There are lots of mathematical results about this, like how you can approximate anything with a polynomial, you can approximate anything with two layers of univariate functions.

**[2:50:31 – 2:50:49]** There are a huge number of results about it, and neural networks are kind of based on this idea. You take very simple things, you put them together, and you get a very complicated thing like a face recognition system.

**[2:50:49 – 2:51:07]** Another thing where artificial neural networks are really, really similar to the human brain is the structure of a single neuron. We will come back to it just right now and later, and we will see that.

**[2:51:07 – 2:51:25]** So, okay, let's come to it right now. No point in leaving it for the future. So what does a neuron look like, an artificial neuron, like this most basic building block of neural networks?

**[2:51:25 – 2:51:38]** Well, it has some inputs, x1, x2, xn. It looks just like the linear models that we discussed just now. In part, that's why I'm always discussing them.

**[2:51:38 – 2:51:52]** Then you multiply them by the weights of this neuron, and you get w times x. You get this linear combination of inputs with the weights.

**[2:51:52 – 2:52:02]** The weights will be trained during learning of the network. But then you also need to have a nonlinear function before you can get to the output.

**[2:52:02 – 2:52:16]** Why? Because if your neurons were doing just linear regression, if your neurons did not have a nonlinear function, which is called the activation function,

**[2:52:16 – 2:52:29]** then there would be no point to have a network, because composition of linear functions is linear again.

**[2:52:29 – 2:52:37]** And now if I have a huge network full of linear neurons, it's basically just one neuron applied to the whole, and there is no difference.

**[2:52:37 – 2:52:42]** So with linear functions, I will not get more complicated things.

**[2:52:42 – 2:52:53]** But as soon as I have any kind of nonlinearity, we will discuss just now what kind of nonlinearities there are, and there are very simple ones.

**[2:52:53 – 2:53:04]** As soon as I have any kind of nonlinearity, even something like real, which is just two linear functions strained together, it starts to work.

**[2:53:04 – 2:53:11]** And there is a big field of math that shows that any kind of nonlinearity is enough to approximate anything.

**[2:53:11 – 2:53:16]** It doesn't really matter in practice for us. In practice, what matters is that it works.

**[2:53:16 – 2:53:29]** So as soon as we have any sort of nonlinearity, compositions of these simple neurons begin to approximate whatever you want.

**[2:53:29 – 2:53:34]** Which still leaves open the question of how to approximate, how to find the weights, how to train.

**[2:53:34 – 2:53:42]** We'll discuss that a lot. But basically, as soon as we have a nonlinear neuron, we can.

**[2:53:42 – 2:53:54]** And interestingly enough, this kind of model for a single artificial neuron has been with us since 1943.

**[2:53:54 – 2:54:05]** Since before the Turing test, since before the Dartmouth seminar, before the words artificial intelligence had any scientific meaning.

**[2:54:05 – 2:54:15]** Already in 1943, Warren McCulloch and Walter Pitts wrote a paper which was called Logical Calculus of Nervous Activity.

**[2:54:16 – 2:54:22]** So it was actually, they were approaching it from the perspective of mathematical logic.

**[2:54:22 – 2:54:28]** But they wanted to have a mathematical model of the human brain.

**[2:54:28 – 2:54:33]** And in particular, a mathematical model of a single neuron.

**[2:54:33 – 2:54:37]** And it was basically already this.

**[2:54:37 – 2:54:43]** So even in 1943, we started off with this model of the neuron and we are still with it.

**[2:54:43 – 2:54:49]** So yes, there are parts of modern neural networks that cannot be directly explained by these neurons.

**[2:54:49 – 2:54:53]** So there are like attention mechanisms when we get to transformers.

**[2:54:53 – 2:54:58]** We will see some functions that have weights, but that are not quite like this.

**[2:54:58 – 2:55:06]** But mostly, most neural networks are still composed from neurons like this.

**[2:55:06 – 2:55:09]** And even transformers have a lot of neurons like this.

**[2:55:09 – 2:55:12]** So this is still the basic building block.

**[2:55:12 – 2:55:18]** It was first implemented in practice by Frank Rosenblatt in 1958.

**[2:55:18 – 2:55:20]** I think I have pictures.

**[2:55:20 – 2:55:21]** Yep.

**[2:55:21 – 2:55:24]** Very romantic time to be in computer science.

**[2:55:24 – 2:55:28]** That's what the computer looked like back in the days, 1950s.

**[2:55:28 – 2:55:39]** And so this is Frank Rosenblatt, like, learning, training a perceptron, right?

**[2:55:39 – 2:55:41]** But it indeed worked.

**[2:55:41 – 2:55:49]** So I think it was the first actual honest machine learning model implemented in practice.

**[2:55:49 – 2:55:53]** And it actually did some pretty amazing things eventually.

**[2:55:53 – 2:55:57]** So it learned to recognize letters.

**[2:55:57 – 2:56:01]** And, of course, it's not real computer vision.

**[2:56:01 – 2:56:10]** They were letters in a specific font, photographed from a specific point.

**[2:56:10 – 2:56:16]** And, of course, this was much simpler problem than real OCR, of course.

**[2:56:16 – 2:56:19]** But still, it was extremely amazing for the time.

**[2:56:19 – 2:56:22]** And when this perceptron appeared,

**[2:56:22 – 2:56:31]** well, I always show this New York Times quote.

**[2:56:31 – 2:56:34]** Maybe let's not dwell on it right now.

**[2:56:34 – 2:56:40]** But basically, at that point, everybody decided that, well, the hard part is done.

**[2:56:40 – 2:56:42]** So I recommend you read it.

**[2:56:42 – 2:56:44]** The hard part is done.

**[2:56:44 – 2:56:48]** And we know how to make computers learn.

**[2:56:48 – 2:56:55]** And now it's only a couple of years before they can walk, talk, see, write, reproduce themselves

**[2:56:55 – 2:56:57]** and be conscious of their existence.

**[2:56:57 – 2:57:00]** So as we know, it took a little bit more than that.

**[2:57:00 – 2:57:07]** This early optimism was not really warranted, but still it's the same principles, right?

**[2:57:07 – 2:57:12]** We still inherit a lot from this early neural network ideas.

**[2:57:12 – 2:57:18]** Okay, what do I want here? Yeah.

**[2:57:18 – 2:57:24]** And then, as I told you yesterday, the AI winter happened.

**[2:57:24 – 2:57:35]** So then people somehow got convinced that machine learning doesn't really work.

**[2:57:35 – 2:57:43]** And in particular, by the way, they got convinced that neural networks don't work.

**[2:57:43 – 2:57:52]** And there were some practical reasons which were true, but there was also a very strange theoretical reason for that,

**[2:57:52 – 2:57:57]** that somehow convinced a lot of people that neural networks are worthless.

**[2:57:57 – 2:58:10]** And the theoretical reason is this: whatever activation function you have, if you have—and this is an important point, so let me make it—

**[2:58:10 – 2:58:23]** whatever activation function you have, whatever is the H, still the inputs go to H through a linear combination, right?

**[2:58:23 – 2:58:40]** So if you think about it as a model doing classification, then you are still drawing a linear separating surface between the classes.

**[2:58:40 – 2:58:56]** So there is—so if you have H times X and you have some decision rule afterwards, like if it's more than 0, then class 1, if it's less than 0, then class 2,

**[2:58:56 – 2:59:00]** then the surface will be this, right?

**[2:59:00 – 2:59:07]** This is the decision surface on one side to have C1, on the other side to have C2,

**[2:59:07 – 2:59:16]** which is the same thing as saying, well, let me just see where H reaches 0 and now it's a linear surface, right?

**[2:59:16 – 2:59:21]** So the non-linearity doesn't give you non-linear separating surfaces.

**[2:59:21 – 2:59:26]** Non-linearity just gives you the ability to build networks,

**[2:59:26 – 2:59:31]** but by itself, it still leaves the classifier linear, of course.

**[2:59:31 – 2:59:36]** And for some reason, people look at this and say, well, okay,

**[2:59:36 – 2:59:41]** so it means that one perceptron cannot solve a lot of problems.

**[2:59:41 – 2:59:47]** There are many problems which do not have a linear separating surface, like the XOR function.

**[2:59:47 – 2:59:53]** If you have the orange class over here and you have the blue class over here and over here,

**[2:59:53 – 2:59:58]** then of course there is no straight line that separates them.

**[2:59:58 – 3:00:04]** Well, sure, these are linearly inseparable classes.

**[3:00:04 – 3:00:12]** But for some reason people thought that this was like an argument against perceptrons

**[3:00:12 – 3:00:16]** and against neural networks, which was kind of strange.

**[3:00:16 – 3:00:19]** I'm still not sure how the reasoning actually worked.

**[3:00:19 – 3:00:25]** But, of course, the correct answer is, sure, you cannot do XOR,

**[3:00:25 – 3:00:33]** you cannot do a linearly inseparable task with a single perceptron,

**[3:00:33 – 3:00:38]** but you can do it with a network of perceptrons, right?

**[3:00:38 – 3:00:47]** And the idea of a neural network, the idea of taking this kind of neurons

**[3:00:47 – 3:00:56]** and putting them together in layers and computing the final result of a composition of several such neurons,

**[3:00:56 – 3:01:02]** it's also very old, and it actually goes back to the same Alan Turing.

**[3:01:02 – 3:01:08]** He was a smart guy, and he already, in 1948, before the Turing test,

**[3:01:08 – 3:01:12]** he already had a paper, which I don't recommend to read, it's very hard to read today,

**[3:01:12 – 3:01:17]** but he already had a paper where he suggested actually deep neural networks,

**[3:01:17 – 3:01:23]** like real deep neural networks, compositions of layers of neurons.

**[3:01:23 – 3:01:29]** And the question was, how do we train it?

**[3:01:29 – 3:01:34]** The answer was pretty straightforward, I think we'll discuss it in detail tomorrow,

**[3:01:34 – 3:01:39]** along with all of the gradient descent variations that we have today.

**[3:01:39 – 3:01:44]** But the answer is, of course, well, you learn by gradient descent,

**[3:01:44 – 3:01:50]** and to do gradient descent, the only thing you need to be able to do is to take the gradients,

**[3:01:50 – 3:01:55]** take the derivatives, and how do you take the derivatives through the computational graph?

**[3:01:55 – 3:01:57]** Well, by backpropagation.

**[3:01:57 – 3:01:59]** I think you've heard about it.

**[3:01:59 – 3:02:01]** Probably you should already know it.

**[3:02:01 – 3:02:04]** Maybe we'll cut through it quickly tomorrow.

**[3:02:04 – 3:02:08]** So it's not a very deep idea.

**[3:02:08 – 3:02:13]** Backpropagation is just the chain rule for computing probabilities.

**[3:02:13 – 3:02:20]** And therefore, it's hard to say who discovered it because it was kind of discovered independently a lot of times.

**[3:02:20 – 3:02:38]** But by the 1970s, it was already kind of well known and understood that you can use backpropagation to go through the layers and to update the weights of a composition of simple functions.

**[3:02:38 – 3:02:52]** And already in the late 1970s, in the first half of the 1980s, you already had the idea of deep neural networks.

**[3:02:52 – 3:02:56]** And they already started to appear.

**[3:02:56 – 3:03:01]** And by the second half of the 1980s, you already had convolutional networks.

**[3:03:01 – 3:03:03]** You already had recurrent networks.

**[3:03:03 – 3:03:06]** You didn't have transformers yet that had to wait.

**[3:03:06 – 3:03:15]** But you already had a lot of architectural ideas that are actually still relevant,

**[3:03:15 – 3:03:20]** and that if you could just scale them up, they would work quite amazingly well, actually.

**[3:03:20 – 3:03:26]** So if you take a network, say a convolutional network, a CNN,

**[3:03:26 – 3:03:31]** from the early 1990s to late 1980s, and you just mechanically scale it up,

**[3:03:31 – 3:03:34]** and you train it on modern hardware and modern datasets,

**[3:03:34 – 3:03:36]** it's going to work pretty well.

**[3:03:36 – 3:03:39]** So of course it will be worse than the networks we have today, of course.

**[3:03:39 – 3:03:48]** But if people had this kind of results back in 1990,

**[3:03:48 – 3:03:52]** they would never be discouraged from neural networks.

**[3:03:52 – 3:03:55]** That would definitely be state-of-the-art back in the time.

**[3:03:55 – 3:04:01]** But unfortunately, neural networks require a certain scale to work,

**[3:04:01 – 3:04:02]** so to speak, right?

**[3:04:02 – 3:04:06]** So if you have a very small neural network and a small dataset,

**[3:04:06 – 3:04:12]** then probably the result will be worse than if you actually just think

**[3:04:12 – 3:04:18]** about the problem and do some more specialized model for this problem.

**[3:04:18 – 3:04:27]** So by the early 1990s, since people did not have the ability to scale up,

**[3:04:27 – 3:04:31]** they did not have the compute, they did not have the data,

**[3:04:31 – 3:04:36]** basically the consensus in the research community was like this:

**[3:04:36 – 3:04:40]** neural networks are the second best way of doing just about anything.

**[3:04:40 – 3:04:44]** So the place of neural networks was that they are very universal,

**[3:04:44 – 3:04:47]** you can do anything with a neural network, indeed,

**[3:04:47 – 3:04:53]** but it will be worse than if you just think about the specific problem you have

**[3:04:53 – 3:04:55]** and create a model for this specific problem.

**[3:04:55 – 3:04:59]** So in the 1990s and early 2000s,

**[3:04:59 – 3:05:02]** neural networks were kind of forgotten again.

**[3:05:02 – 3:05:06]** It was the heyday of probabilistic models,

**[3:05:06 – 3:05:09]** of graphical probabilistic models, etc., etc.

**[3:05:09 – 3:05:14]** Very interesting, still relevant, very important, but out of scope for us.

**[3:05:14 – 3:05:20]** And there were just a few groups who pushed and pushed on neural networks.

**[3:05:20 – 3:05:24]** There was Jan LeCun who was doing image processing with CNNs.

**[3:05:24 – 3:05:28]** There were Jeffrey Hinton's group and Joshua Bench's group.

**[3:05:28 – 3:05:32]** And they continued working, they continued believing in the neural networks.

**[3:05:32 – 3:05:36]** And finally, they were proved to be right.

**[3:05:36 – 3:05:47]** Okay, so the deep learning revolution happened in the middle of the 2000s, 2006, 2007.

**[3:05:47 – 3:05:55]** And I won't discuss in detail what exactly was their innovation because it's irrelevant by now.

**[3:05:55 – 3:05:57]** It's absolute.

**[3:05:57 – 3:06:08]** But the technical innovation, which is still, of course, relevant, was that they moved from CPUs to GPUs.

**[3:06:08 – 3:06:17]** So, again, it's not much of an idea to notice that the stuff we do in neural networks is easy to parallelize.

**[3:06:17 – 3:06:19]** Of course, it's easy to parallelize.

**[3:06:19 – 3:06:23]** It's a huge number of neurons and not very deep computation, just like in the brain.

**[3:06:23 – 3:06:38]** But only in our century, only in the early 2000s, there was actually hardware widely available on the market, gaming GPUs, that would actually implement this parallel process.

**[3:06:38 – 3:06:44]** So before that, CPUs were still the best we had, right?

**[3:06:44 – 3:06:53]** And as soon as GPUs became good enough, people, specifically the guys at Hinton's group, moved computations to GPUs.

**[3:06:53 – 3:06:59]** That gave a boost of about another 10x, 20x inefficiency.

**[3:06:59 – 3:07:06]** And that was enough. That was enough to put neural networks from not working to working.

**[3:07:06 – 3:07:16]** And starting from the late 2000s, neural networks have been kind of revolutionizing one field of machine learning after another.

**[3:07:16 – 3:07:22]** Actually, the first field was speech recognition, speech processing.

**[3:07:22 – 3:07:30]** Deep neural networks served as some very good feature extractors in about 2010.

**[3:07:30 – 3:07:39]** So basically, it was these original deep neural networks by Hinton and Benji that made Siri possible.

**[3:07:39 – 3:07:43]** Siri appeared in 2011, I think, the first version.

**[3:07:43 – 3:07:48]** And it was, of course, would be impossible on classical speech recognition.

**[3:07:48 – 3:07:52]** I mean, it wouldn't work well enough to be useful.

**[3:07:52 – 3:08:02]** And then, so we will not talk about speech recognition in this class, but we will talk definitely about image processing and image recognition and computer vision.

**[3:08:02 – 3:08:27]** So there the revolution happened around 2011, 2012 with AlexNet. We will discuss AlexNet in detail when we come to it. And then everywhere. Then with recurrent networks, deep learning got into natural language processing.

**[3:08:27 – 3:08:50]** So by 2014, 15, people were doing machine translation with neural networks and stuff like that with neural networks. And then in 2017, everything changed again. In 2017, we had the transformer and that transformed literally the whole industry again. We are still living in the age of transformers, so to speak.

**[3:08:52 – 3:09:06]** So I think I don't have time to go to BecProv right now. This was a quick historical overview and we'll do the optimization part tomorrow. Any questions?

**[3:09:06 – 3:09:23]** I'm sorry. I think I skipped one of the parts you were explaining about logistic regression and you put some neural network, you put logistic regression at the end. I think I just didn't capture what was going on there.

**[3:09:23 – 3:09:43]** Yeah, sure, no problem. So suppose that I'm doing a neural network that is supposed to do classification. So at the output, I want to have a loss function like this. And I want to have like a vector of probabilities for classes. Where do I get a vector of probabilities?

**[3:09:43 – 3:09:56]** Well, if I just do some neural layers, some elementary functions, some big compositions, I will not get a vector of neat numbers from zero to one that sum up to one, right?

**[3:09:56 – 3:10:08]** What I will get is a vector of scores that then will need to be converted to probabilities by the softmax function. That's part one.

**[3:10:08 – 3:10:19]** But also, I mean, for some networks, this will be the actual output and this may not happen, but usually, of course, it still happens.

**[3:10:19 – 3:10:30]** So usually after the main part of the neural network, what it does is it extracts some kind of features from the input.

**[3:10:30 – 3:10:41]** And these features are a vector or a higher dimensional tensor, it doesn't matter at this point, but it's a set of numbers, let's say, of size d, right?

**[3:10:41 – 3:10:43]** Okay, I got it.

**[3:10:43 – 3:10:47]** And we want to convert it to a set of numbers of size k.

**[3:10:47 – 3:10:49]** That's the only point that I was making here.

**[3:10:49 – 3:10:53]** So how can you do it well, for example, with just a linear transformation?

**[3:10:53 – 3:11:01]** So very often when neural networks do classification, very often the last layer is actually just logistic regression.

**[3:11:01 – 3:11:08]** This is literally straightforwardly logistic regression.

**[3:11:08 – 3:11:14]** But not on the input, but on the features extracted by all the rest of the neural network.

**[3:11:14 – 3:11:16]** And that's the very important difference.

**[3:11:16 – 3:11:27]** If that would be not logistic regression, but linear regression, everything would be the same except for softmax part.

**[3:11:27 – 3:11:35]** And probably, I mean, in linear regression it's kind of uncommon to have many outputs.

**[3:11:35 – 3:11:37]** So probably k would be equal to 1.

**[3:11:37 – 3:11:40]** But not necessarily, you could have several outputs, of course.

**[3:11:40 – 3:11:44]** Yes, you explained that before.

**[3:11:44 – 3:11:47]** And I also want to say thank you for the lecture.

**[3:11:47 – 3:11:49]** It was very interesting.

**[3:11:49 – 3:11:56]** It was very unobvious to see the prior Bayesian theory,

**[3:11:56 – 3:12:00]** imagining that regularization is a bias.

**[3:12:00 – 3:12:02]** Because I read a lot of information,

**[3:12:02 – 3:12:04]** I was preparing for an interview,

**[3:12:04 – 3:12:06]** and I literally couldn't find it.

**[3:12:06 – 3:12:09]** I haven't seen it before.

**[3:12:09 – 3:12:11]** Maybe I haven't read it properly.

**[3:12:11 – 3:12:15]** If you looked for it, you should be able to find it.

**[3:12:15 – 3:12:20]** Of course, it's like in the foundations of all the machine learning,

**[3:12:20 – 3:12:23]** but I'm really happy that you find it interesting.

**[3:12:23 – 3:12:26]** I'm always a little bit worried about this introductory part

**[3:12:26 – 3:12:30]** because some people just want to get to programming in PyTorch.

**[3:12:30 – 3:12:33]** But I think that foundations are important,

**[3:12:33 – 3:12:36]** and I'm really happy that you feel that way too.

**[3:12:36 – 3:12:40]** Thank you.

**[3:12:40 – 3:12:41]** Thank you.

**[3:12:41 – 3:12:43]** All right. Thanks a lot, guys.

**[3:12:43 – 3:12:44]** Sure.

**[3:12:44 – 3:12:49]** In the first part of the bus, we discussed the problem of overfitting, right?

**[3:12:49 – 3:12:50]** Mm-hmm.

**[3:12:50 – 3:12:56]** So, like, in general, you can...

**[3:12:56 – 3:13:03]** Okay, previously in statistics, you would use, like, measures like R-squared-adjusted,

**[3:13:03 – 3:13:11]** or, like, criteria, I don't remember, like, Kaike information criteria

**[3:13:11 – 3:13:18]** and some other measures that punish adding extra variables to the model.

**[3:13:18 – 3:13:26]** Which is basically what rich regression and lasso do, I guess.

**[3:13:26 – 3:13:34]** Not quite. So, yeah, there is a difference here that is a little bit...

**[3:13:34 – 3:13:37]** that is a little bit made unclear by my example.

**[3:13:37 – 3:13:42]** And I apologize for that, but it's still a very instructive example, so I still give it.

**[3:13:42 – 3:13:45]** But yes, that is a great question, and there is an important difference.

**[3:13:45 – 3:13:52]** So when we talk of regularization, we kind of have already fixed the model.

**[3:13:52 – 3:14:00]** So in the case of linear regression, I can have an L2 regularizer, I can have an L1 regularizer,

**[3:14:00 – 3:14:07]** I can have any kind of prior over here, but the likelihood is already fixed.

**[3:14:07 – 3:14:11]** And what it means that the likelihood is fixed in particular,

**[3:14:11 – 3:14:14]** it means that the size of this vector is also fixed.

**[3:14:14 – 3:14:21]** So when I change regularizers, I don't change the model structure,

**[3:14:21 – 3:14:23]** I don't change the number of parameters.

**[3:14:23 – 3:14:30]** It might look like that in my example, because as I went from between degrees of the polynomials,

**[3:14:30 – 3:14:32]** I was changing the number of parameters.

**[3:14:32 – 3:14:35]** You're right, it was a little bit confusing in this regard.

**[3:14:35 – 3:14:38]** But regularization usually does not do that.

**[3:14:38 – 3:14:41]** Regularization deals with the values of these parameters.

**[3:14:41 – 3:14:47]** And the stuff that you mentioned, and these are great keywords

**[3:14:47 – 3:14:50]** that I also talk about in classes when I have time,

**[3:14:50 – 3:14:53]** but not in this class where we go to deep learning,

**[3:14:53 – 3:14:56]** but things like Akaiki information criterion,

**[3:14:56 – 3:14:59]** the Bayesian information criterion, and stuff like that,

**[3:14:59 – 3:15:02]** they pertain to what is called model selection.

**[3:15:02 – 3:15:09]** And model selection basically means I can model my data set

**[3:15:09 – 3:15:11]** in several different ways.

**[3:15:11 – 3:15:17]** I can have linear regression, I have quadratic regression, cubic regression,

**[3:15:17 – 3:15:21]** local Gaussian regression, whatever.

**[3:15:21 – 3:15:23]** And then I need to choose between them.

**[3:15:23 – 3:15:26]** How do I choose between them?

**[3:15:26 – 3:15:28]** Well, what is this choice?

**[3:15:28 – 3:15:30]** What am I trying to estimate?

**[3:15:30 – 3:15:33]** It's deceptively simple.

**[3:15:33 – 3:15:37]** I want to estimate what is the likelihood,

**[3:15:37 – 3:15:42]** what is the probability of having model number k for my data set.

**[3:15:42 – 3:15:49]** And where do I get this probability from?

**[3:15:49 – 3:15:53]** Well, of course I get it from the bias rule.

**[3:15:53 – 3:15:58]** So of course I get it from something like this, p of mk times p of d given mk.

**[3:15:58 – 3:16:05]** And notice that here m is not a specific set of weights.

**[3:16:05 – 3:16:07]** Here m is the whole model.

**[3:16:07 – 3:16:10]** So like one m could be like linear regression

**[3:16:10 – 3:16:14]** and another m could be like quadratic regression.

**[3:16:14 – 3:16:17]** So it's the whole model, not specific weights.

**[3:16:17 – 3:16:22]** But still, the bias rule is the same.

**[3:16:22 – 3:16:24]** And it still tells you, well, okay,

**[3:16:24 – 3:16:27]** if I don't have any reasons to prefer one model to another,

**[3:16:27 – 3:16:29]** then let's assume this is uniform.

**[3:16:29 – 3:16:34]** And I just compare p of d given mk.

**[3:16:34 – 3:16:37]** Where is that p of d given mk in our formulas?

**[3:16:37 – 3:16:47]** Well, let's go back to our bias rule, p of theta.

**[3:16:47 – 3:16:49]** Put more space here because I need this.

**[3:16:49 – 3:17:03]** p of theta, p of d given theta, sorry, p of d given theta divided by p of d and here p of theta given d.

**[3:17:03 – 3:17:11]** This formula, as I wrote it, we didn't have, you know, the context and the chance to go this one meta level up.

**[3:17:11 – 3:17:13]** But you can go one meta level up.

**[3:17:13 – 3:17:17]** The formula, as I wrote it, was about one model.

**[3:17:17 – 3:17:25]** Like we are talking about linear regression and we are dealing with the parameters that obey this base rule and do inference for the parameters.

**[3:17:25 – 3:17:31]** So like everything happens in a model.

**[3:17:31 – 3:17:34]** Sorry, not the bar, right?

**[3:17:34 – 3:17:44]** You can add the model here, doesn't change the formula, it still works.

**[3:17:44 – 3:17:47]** So what do you compare the models by?

**[3:17:47 – 3:17:54]** How do you choose between quadratic and cubic features or between different versions of the model, et cetera?

**[3:17:54 – 3:17:59]** Well, by this guy over here.

**[3:17:59 – 3:18:04]** The denominator, so this is exactly this quantity.

**[3:18:04 – 3:18:09]** The denominator in the base rule, the normalizing constant.

**[3:18:09 – 3:18:17]** And everything that these information criteria do, they are basically approximations to compute this.

**[3:18:17 – 3:18:21]** And then there is a lot of methods, it's a very beautiful and interesting approximation.

**[3:18:21 – 3:18:25]** Lots to say about it, but basically it's an approximation to compute this.

**[3:18:25 – 3:18:32]** So model selection is about trying to estimate this normalizing constant

**[3:18:32 – 3:18:35]** and choose the model with the largest normalizing constant.

**[3:18:35 – 3:18:42]** But inside the model, then, we will have a whole distribution of parameters, blah, blah, blah, and so on.

**[3:18:42 – 3:18:47]** So there are two levels. There is the level of selecting the model,

**[3:18:47 – 3:18:52]** and then inside the model there is the level of actually learning the parameters.

**[3:18:52 – 3:18:57]** Did I answer the question?

**[3:18:57 – 3:19:02]** Thank you.

**[3:19:02 – 3:19:08]** Okay. Thanks, guys. And see you tomorrow, finally, for some actual neural networks. Bye-bye.

## Full text

Good morning, everyone. Welcome to the second day of our class. And I suppose, I hope the first day was interesting. Today we will definitely start deep learning, although I do have a few things to tell you before that. But then, at least in the second half, we'll definitely start talking about neural networks. No way around that. To get the technical organizational stuff out of the way, I sent a message to Google Classroom. I hope you've seen it. I made a web page, a secret web page, which probably we are not supposed to link to externally, but that's just for you. I made a web page with all class materials. I'll keep uploading videos, slides, words, etc. So I hope you like it. And with that, let's continue. Yesterday, we talked about the general idea of what learning is, of how we can formalize and understand what it means for, say, machine learning model to actually learn something. And we framed it in the probabilistic Bayesian framework. And basically, it was like most of yesterday's discussion was centered around the Bayesian rule, around this famous formula, which is the most important formula in the entire machine learning. But yesterday, we talked about a very simple example. We were just talking about the coin toss. And I actually want this introduction to go to the linear models, because they are very directly relevant to what we do in deep learning and to what neural networks actually do. So let me, apologies, but let me continue with this probabilistic introduction. Still, I hope it's important. Well, I'm sure it's important, but I hope it's interesting for you. So we discussed the base rule yesterday. And just as a quick reminder, the main idea of this formula is to answer the question of how should we update our beliefs when we learn new information, when we get new evidence. So in more general terms, D would be not specifically a data set for machine learning, but it would be just any kind of evidence. And theta would be like our beliefs, our hypotheses about the underlying process or whatever. And then when we get new evidence, we update what we believe. And that's in a way how life works. That's how our brains are supposed to work. Not always they work exactly in this way. And of course, we don't consciously do any calculations like this. But the general essence is exactly this. And we discussed three main problems of machine learning, where the optimization tasks come from. So you can start with the likelihood and end right there and just maximize the likelihood. That doesn't make any use of Bayesian inference, so it's a non-Bayesian method. But still, if you have lots of data or if your model is already very complicated and a prior distribution would make it completely infeasible, although I can't imagine why, still you can just maximize the likelihood. Then you can multiply the likelihood by the prior, we'll see very specific examples of that today in real-life models, not just the coin toss. And then maximize the result, which will be proportional to the posterior distribution. That's what we discussed last time. And we discussed the coin tossing example in great detail. And the third problem would be the predictive distribution, which I don't think we'll get to today. So let that stay at the level of the coin tossing. And we discussed the coin tossing example in great detail yesterday. So we kind of went through all of these problems, went through the notions of likelihood, prior, posterior, what it all means, completely finished the simplest case of a uniform prior, and then discussed what a more informative, more reasonable prior would be. Like if I do want to have a bell-shaped curve, then how do I choose among them? And the answer was, well, choose the one that's convenient, which may sound like an unsatisfactory answer, but there you go. It's our choice, it's about our beliefs. So actually in more involved cases like linear regression that we will discuss now, the reasoning is exactly the same. You choose the prior not due to some principled reason, like you understand that for this process the prior should be this, but you choose your prior either for convenience or because it leads to desirable properties. We will see how it works. And another thing that I wanted to mention here, I will not spend much time on real-world examples or anything, but I do want to mention some kind of philosophical underpinning of all this. And I mentioned yesterday that if you open an old book on probability theory, a very good book, but an old book on probability theory, you will see probability introduced like, well, there is this infinitely repeatable experiment, we do the experiment, we get some results, and then we divide the results, the number of outcomes that we are interested in by the number of total experiments, and that ratio tends to the probability. That is completely correct. When it's applicable, it's completely correct. And for the coin toss, it's exactly how we define probability. But in real life, and especially in machine learning, that's why I'm talking about this, we usually want to reason about the probability of events that are definitely not repeatable experiments, right? So, for example, if you're a bookmaker, you need to predict the probability, to set the probability of, say, Spain winning the FIFA World Cup this year. And there will be only one World Cup. And no, it's not a repeatable experiment based on previous World Cups, because obviously the teams were completely different, everything was completely different. Or we even might want to set probabilities for events that already happened, that are already set, but we just don't know the answer. And in these kind of cases, it makes no sense to talk about experiments repeated to infinity, right? For example, there is a hypothesis, I'm not sure about the current status, but once time I checked it was a hypothesis, that the Odyssey by Homer was not written by the same Homer as the Iliad, was written by a woman due to some lexicographic analysis of the text. And it's a hypothesis, we don't know, but it makes sense for us to want to assign probabilities to hypotheses like this, right? Although there is only one Odyssey, and it was written by somebody thousands of years ago, and the answer is already set, but we just don't know it. So the point is, in real life, probabilities are often not limits of ratios of experiments, but they are degrees of belief. They are representations of our uncertainty. And this is actually a very useful, I think, framing to think about probability, and a very useful way to understand what we are doing. We are not actually... When we do machine learning, for example, when we use this with a real dataset and a real model, we are not getting some kind of logical conclusion, right? We are updating our beliefs, and if we have a good dataset, a large enough dataset, then our beliefs can become much more certain. We can become... I don't know, the confidence intervals may shrink. We can become more sure in the hypothesis that we are evaluating, but we will never be completely sure, right? Especially in machine learning when it's all about noisy datasets. The thing is, we are combining all of this evidence to understand something about the model, model parameters in this case, but the result is always a probability distribution. And this is a point that often gets lost for people, because what you actually do in reality, and let me maybe immediately, so that you understand in advance where we are driving with this, let me maybe immediately get you the general notion of what we are doing today. So we are using this identity, and we are reasoning by the base rule, but what we are actually doing, for example, in deep learning practice all the time, is we compose a loss function, right? So we compose a loss function like log p of d given theta plus log p of theta, and actually we take a minus because the loss function you want to minimize, not maximize. But in practice, this is the loss function for your neural network, right? We'll see how it works specifically today. And then you minimize it with respect to theta, with respect to the neural network parameters, and you get theta MAP, right? So theta MAP is the argmin of this, the maximum posterior hypothesis, right? So it's the argmax of p of theta given d. And very often people, when they think about deep learning about neural networks, they kind of stop here and the process does stop here. And then they say, oh, now we know theta. Now we got our model checkpoint. Here are the weights. Here are the true weights. That is an oversimplification, right? So yes, in practice, very often we will do exactly this and we will use theta as a point estimate. But it's very helpful to remember that theta MAP is just a point estimate. It's just the maximum of a whole distribution. And in deep learning with huge neural networks, etc., we usually cannot do that. But if we could, it would be very helpful usually to actually at least sample several different points from this distribution and see how that translates into different predictions. And actually, sometimes you see this in deep learning as well. So all of this machinery is about degrees of belief. It's about our uncertainty, our original uncertainty captured in P of Theta and then reduced by D, by the data that we get. And ultimately, our new uncertainty captured in P of Theta given D, right? So we know something about the parameters. It cannot be that we know absolutely nothing. Well, sometimes it can, but still we need to express it in a distribution. Then we get new information, we update, and we have some new belief about Theta. But it's a distribution. It's an uncertain belief. It's never just a single point. This is what I wanted to say here. And also, I usually go through some relatively straightforward examples of applying the base rule. Let's try it with you. So here is a very standard trick question from probability theory. A person has two kids. Let's say my acquaintance has two kids, but I've never met them. I don't know their names. I don't know their genders. And let's assume that every baby is either a boy or a girl with probabilities one half and the first baby is independent from the second. So they are just there. Each of them is a fair coin to us in terms of whether it's a boy or a girl. And then I go to this person and I ask, hey, do you have any boys? Like among the two children that you have, are there any boys? And he says, yes. In this setting, what is the probability that he has a girl? How many? How did he arrive in this? Well, we know that he had at least one voice, one slot available, that can be either one or the other. Not quite. Any other ideas? So what's the probability space here? Like what are the possible outcomes? Also not quite true. Okay. Yeah, this is a straightforward trick question, but yeah, it would usually fall into the trick unless you know it. So, the person has two children, right? So, it's like child number one and child number two, right? For every child, there are two possibilities, two options, right? So, how many options are in total? Four, exactly. So, we have like boy, boy, boy, girl, girl, boy, and girl, girl, right? So, there are four possibilities. And in the prior, before I get any information, they're completely equal, right? So, we get one-fourth for this, one-fourth for this, one-fourth for this, right? So, now when I ask, do you have any boys? And he answers yes. What information do I get? How does this table change? Yeah, precisely. So, now the last line cannot happen, but the rest all can happen. And the answer yes does not distinguish between them, right? So, as a result, I now have three options. They are still equal in probability, but now I have three options and two of them have a girl, right? So, the probability is actually two-thirds. And if you want it formally, then you just need to compute P of, you know, there is a girl given that there is a boy, right? So, it's like the probability of these two scenarios, MF or FM, divided by the total probability of that there is a boy of M, M, MF or FM, and that comes to two-thirds, right? So, formally, it's like two quarters divided by three quarters, if you go strictly by definition. All right, but here is the second question. Now, I've met one of his kids, so it's a separate question, I didn't ask the first one, so I don't know that. And now I've met one of his kids, and it's a boy, so now I know that one of the kids is a boy, and I've met this boy. What is the probability that the other one is a girl? Yeah, and now it's one half, right? So now, when I meet one of his children, then it means that now, okay, it doesn't matter if it's number one or number two, but it means that I kind of fix the value of one of these columns. So now, I eliminate not one, but two lines. For example, number one is a boy, which means that now only two outcomes remain, and they are equal, etc., etc. So, this is an easy trick question, but it already shows how in probability theory and in Bayesian reasoning like this, notice that although we didn't really use the Bayes' theorem, it's actually the same kind of reasoning. We get some prior beliefs that everything is equiprobable, that's our original assumptions, and then we get evidence, and then we update our beliefs based on this evidence, right? But there are also a couple of more interesting examples, so let's discuss them with you too, since the first one, I think, went well. These are, again, very well-known policies, you may have heard about them, but they are very instructive in the pitfalls, potential pitfalls of the Bayes' rule. Here is the setting. A murder has happened, and we are in a court of law arguing about the murder. So there is some blood left on the crime scene, and we know 100%, so don't think about that assumption. We know for certain that this is the killer's blood, okay? So this is with probability one, you don't need to question that. And it so happens that the blood type is quite rare. Like, let's assume it was a time before DNA tests, so we cannot directly check which person it is, but it's a rare blood type, and only 1% of the population, only 1% of people actually have this blood type. And it just so happens that the defendant, the guy who is being accused of the murder, also has this blood type, right? So the prosecutor comes out and says, well, the chance that the defendant would have this blood type if he was innocent is only 1%, so with probability 99% he is guilty. Is the prosecutor correct in this? I suppose the question on the slide already tells you that he is not, but what's the mistake? What's the problem with this kind of reason? I think it's the specific way how the statement has been proposed to you, maybe? Is it equating the probability of having the blood type given innocence versus probability of actually being innocent given the blood type, something there? Exactly. You nailed it. Exactly. So this is a classic mistake that happens all the time in real life. You see people making it all the time because our brains are not really wired by evolution to do probabilistic reasoning, especially with numbers. And yes, your answer was completely entirely correct. Let me repeat it for everyone. And so we have, so what are we actually trying to do in the court of law? We are trying to establish like P of guilty given the evidence, right? And if it's very, very high, then we convict, right? It's probably never going to be exactly one, but if it's very high, then we convict the person. And so the prosecutor makes a conclusion exactly about this. So his final point, the 99%, is about P of guilty, given the blood type, right? But what he starts with is not P of innocent, given the blood type. It's the other way around. It's P of blood type, given that the person is innocent, right? And yeah, so when the prosecutor estimates this probability, he is completely correct, right? So like one, it doesn't matter, like almost everyone is innocent, so we can say that this is also 1%, that's fine. But then the prosecutor says, well, all right, so this equals to 1 minus this. And now this conclusion is completely wrong, of course, right? So the prosecutor equates like P of A given B with P of B given A, in a way. And that is, of course, not right. When I write it like this, it's obvious that it's wrong. But when it's stated in words, people miss this kind of mistakes all the time. And what would be the actual formula? Of course, it would be the bias rule, right? So in actuality, like P of blood... Okay, let's do it the other way around. P of innocent given blood would be like P of blood given innocent times P of innocent divided by P of blood, right? And of course, this prior and this evidence probability could completely change things. So I'm not going to try to invent any numbers. It doesn't make sense for this example. But for example, suppose that there are two possible suspects. And it just so happens that both of them have this blood type, right? If that happens, then of course the blood type tells us nothing, right? It does not help us distinguish between them and the probability remains to be one half. But the prosecutor's reasoning would not change in this case. So the prosecutor would now make the obviously absurd conclusion that both of the suspects are guilty, each with probability 99%, which is of course wrong. Okay, so this is the prosecutor's mistake. And then the defense attorney comes out and comes on the, what's the word? On the stand, yeah. And the defense attorney says, well, okay, so first he explains what the mistake of the prosecutor was. And then he says, well, okay, let me offer you my own calculation. There are a million people living in this city. And yeah, of course, having this rare blood type narrows it down from a million to only about 10,000. And that is correct. So all that the blood type tells us is that the defendant is guilty with probability like 0.01%. So yeah, sure, it's kind of evidence, but it's very, very weak evidence, right? It's definitely not any kind of proof. Let's just not admit it to evidence at all. This also doesn't sound right, right? So what's the defense attorney's mistake? The blood type is equally likely to be the killer, so basically not even focusing on why the defendant is there in the first place. Yeah, exactly. So in this case, it's not really some deep mistaken probabilistic reasoning. It's just the mistaken assumption, right? So yeah, it would be true what he says if every one of these 10,000 people, including, I don't know, people who are sleeping at the time and babies and everybody in the city would actually have an equal chance of committing this murder. But that's obviously not true in real life, so the defendant is there for some reason. Yeah, so yes, you're completely right. And yeah, and these kinds of mistakes happen all the time. And there was a very famous case, which you might have heard about, the case of O.J. Simpson. He was a very successful football player, American football player, in the 1980s. And then he had some very difficult relationships, so to speak, with his wife. And ultimately, the wife was found to be killed. And O.J. Simpson was tried for murder. It was one of the most publicized trials of the 1990s. And it was a long trial. There were lots of evidence, lots of discussions. We will not go into that. But there was one specific point that exactly matches our discussion on the bias troll. And at some point, the evidence was that O.J. Simpson already had a history of violence with his wife. So basically, he beat her up a few times before. And the prosecutors, they proved this. This was true. And they kind of submitted it to the jury as not direct proof, of course, but as evidence that O.J. Simpson can actually go too far in another episode and the wife can get killed. So the attorney came out and said, well, okay, my client is a very bad person. I do not dispute that. It's very bad to beat up your wife, and definitely he shouldn't be doing that. But we are at a murder trial, and as for the murders, there is a statistic that says, well, only one of 2,500 women subject to domestic violence actually get killed. And he concluded that this is irrelevant for the murder, right? So, and what, I mean, it's, of course, it's the defense attorney's job to make arguments like this, even if they're obviously wrong. But what's really interesting about this is that the court actually agreed. So the court in this very famous, very public O.J. Simpson's case agreed that this is a good reason to say that domestic violence has no relevance to the murderer. And, you know, like they do it, the jury was instructed to disregard this evidence, blah, blah, blah. But of course, this is exactly the same kind of mistake, right? So, in reality, what they were supposed to be evaluating was P... Okay, so let me start with the statistic. The statistic was, what is the probability of murdered given the history of violence? And, okay, the statistic was correct. So that was like 1 over 2,500, that's true. But that's completely not what people were trying to establish, right? So this kind of statistic starts from the point in time when nobody is murdered, right? It starts from the point where everybody is alive and well, and then evaluates how likely it is to be murdered. But a court case, a murder case, argues in the opposite direction, right? So what we actually want to know is what is the probability of being murdered by your husband? Sorry about this gory topic, but this is still the most famous case of this policy. Given that the murder has already happened and there was a history of domestic violence, right? So, of course, the main thing is that the murder has already happened and we are just trying to establish who did it. So the vast majority of these cases, of these 25,000 cases, in the vast majority of them, nobody got murdered. So they don't matter, right? They are not included into this conditional probability. And if you actually take the exact same statistics, here is the punchline. If you actually take the exact same statistics that was available at the time, and you compute the correct probability from it, you estimate the correct probability, it will come, I may be slightly mistaken, but it will come to something like 7 over 8. So, like, among the women who were murdered with a history of domestic violence, in the vast majority of cases, the husband did it. So, of course, if evidence was presented in the correct way, it would look completely different, right? So, this is just an illustration that people do make mistakes like this, and it's probably just a good habit in life to actually understand what exactly you're trying to estimate. What is, I mean, in life, all that we do, like, everything that we do to make decisions is estimate various conditional probabilities. Like, if I do this, what is the probability of my preferred outcome? And if I do that, what is the risk of this and that? And it's a good habit to actually explicitly understand what exactly is the probability that you're evaluating, even if you cannot really evaluate it, right? So in real life, we don't have this kind of statistics. We can't run the numbers, of course. But if you at least qualitatively understand what is the direction that you are trying to predict, what is on the left of the vertical bar and what is on the right of the vertical bar, things become more clear in many cases. Okay, so that was the leftover that I wanted to mention. And now we proceed to our first real example. And now I will make two examples today, linear regression and logistic regression. We will not discuss them in too many details, but I do want to discuss them because they are directly relevant to what's happening in neural networks. That's like the simplest possible neural network is a linear model like this, a neural network consisting of one perceptron. And it's not only that, you know, it's the simplest model and modern neural networks are completely different. No, linear regression and logistic regression are still directly relevant to what's happening in them. I will explain why. So I hope that you all have some kind of intuition about what linear regression is. Maybe you don't, maybe you can't remember the formulas, that's fine. Maybe you don't, I don't know, maybe you never studied it like systematically. But this will be our point number two, linear regression. But at least you have this, you know, general picture in your mind that a linear regression is a problem like this. You have x over here, you have the target variable y over here. There are some data points like this. And you make an assumption. You say the data points are probably in a linear dependence between x and y. But we don't know the dependence and there is noise. So they are not exactly on the same straight line. They are close to a straight line, right? And the problem of linear regression is to find the straight line. Basically, this is the intuition that I hope you all understand. So if I write it down as a formula, I mean, obviously, I can only draw you two-dimensional pictures. So x will be one-dimensional in what I draw. But in reality, of course, we are usually talking about a single y. So the target variable is a number, more or less always. But this number is not just w0 plus w1 times x, but there are many x's, right? So in reality, x is a vector, usually, and we model y as a linear combination of x's. Okay, so before I even begin talking about it in detail, one very simple remark that will help us make things easier. I will actually skip the intercept. So I will actually write y as just w times x, and this means transposition, and this means just the scalar, the dot product of the vectors w and x. So like w1, wd times x1, xd. Why can't I skip the intercept? Why can't I forget about w0? In practice, it's not zero, right? Here it's not zero. Yeah, precisely. Okay, it's good that you know all this stuff. To be able to skip the intercept, I just add one more dimension. I add a fictional dimension. Let's say x0 is just one, like you said. It's a new feature, a constant feature, and then I take my vector x and I map it to one and then x, like a vector which is one dimension longer. And now, suddenly, when I do a linear function, when I do a direct dot product in this vector, I get the intercept for free. So this is a standard trick. That's why we don't need to always add this w0 here, which would make the formulas much more... Well, it wouldn't make it more complicated, but it would make it much more cumbersome. Okay, so y should be similar to a linear function of x's. And maybe you know... I mean, again, if you ever studied any linear regression, you probably have an idea. How do we define this being near to? What do we mean by this approximation? What are we actually... How do we formalize linear regression use? You minimize the, in general, measure of patterns between the actual values and prediction of regression. Yeah, and what is the most common error? Patterns squared. Yeah, yeah, exactly. So the standard way to do linear regression, and again, notice I haven't yet written any probabilities, we'll get there, is... Okay, so what does it mean that I want W to be such that Y is approximated by W times X? It means that my predictions... So here are the axes, right? The axes in the dataset. And my predictions in this axis are points on this straight line, right? So this is what my model predicts. This is W times XN over here. And what does it mean that the straight line is closed? It means that these distances are small, right? It means that I want the total sum of these distances to be as small as possible. Makes sense. And usually, like you said, the loss function in linear regression is defined. So I said that I want the distances to be small, but I didn't yet define what exactly, what is the exact number that I want to be small. And usually it's exactly the square distance, right? So usually it's the sum of Y minus Yn minus W times Xn squared. And standard linear regression minimizes this with respect to W, right? Well, here is a question. Why? Where does this come from? If you know, you can speak up and tell, or if you have an idea why. So obviously I do want these distances to be as small as possible. That's right. Obviously, I cannot just add up distances as they are because they have signs, right? So I do want this to be symmetric. I don't want the straight line to go just to positive infinity because then everything will have negative infinite errors, right? So I do want it to be symmetric. So that's part of the job that the square is doing, sure. But the same job could be done by a million other ways, in a million other ways, right? I could have said, okay, why don't I add up the absolute values of this errors? Why don't I add up these values to degree four? Why don't I add up e to the power of the absolute value of this? And I mean, there are a million, there are infinitely many monotone functions that are symmetric and monotone in the distance. And if I actually start minimizing all of these things, I will get different results, right? The w will be different. So why do people choose squares so often? Why is it the most common loss function? I think it's because of the fulfillment of the Goffman computer, maybe? Like the blue property? Exactly. Okay, so I see that you already have the background for this, so I'll make it quick. If everybody has the same answer, we can just skip it. If you want to hear it, then I can explain. The reason for this, the reason for the square, actually comes from the probabilistic assumptions that we're making. And let's frame linear regression as a machine learning model in the sense that we are developing, right? So in this case, theta is the W, of course. So the model parameters are the weights, that's clear. Data are the Xs and Ys, that's also pretty clear. But how do we define the likelihood? So to define the model, we need to define the likelihood. The likelihood is P of D given theta, right? The first thing that we do is we make the same assumption that we make always in machine learning, that keeps true throughout all of the machine learning models. We say that all of the data points are conditionally independent. Sorry, not X, Y. Are conditionally independent given the parameters, right? Sorry, it should be W too. And also, since we are doing supervised learning, we always have an X. And the X, we are not modeling the X. We are only modeling the Y, right? So the X always goes on the right-hand side here. So this is what supervised learning actually means. It means that we have an input that goes here. And then we are modeling the output that goes here. Okay, so this part is straightforward. This is our first assumption. We always make it. But then comes the interesting part. So what is this distribution here? It's actually the distribution of the points that we see given our model and the x where we measure. So for example, at x3, we have our model predicting this point. But what we need to define is not just a single point. So our second assumption will be linearity. Our second assumption will be that the most probable point, the center of this distribution, is, in fact, w times x. But to actually do learning, we have to define a whole distribution around this point. It probably looks something like this, right? So it should decrease. I mean, I wanted it to be symmetrical, so let's assume it's symmetrical, and I wanted it to decrease to both sides, right? So what it would mean, it would mean that larger distances from our model, larger distances from the straight line, are less probable. So if I want to find the most probable line, the maximum likelihood line, for example, then, of course, I want these distances to be small. So I want these points to... I want the noise to be as small as possible, the total noise here. And the specific form of the loss function will follow from the choice of distribution. So yeah, I want it to be symmetric, I want it to be kind of bell-shaped, but as we discussed yesterday, there are lots of bell-shaped curves, right? So we want to pick a specific distribution here. And now comes your answer, right? So this was all the setup for your answer. What is the most natural distribution? What is the default distribution that you use in a situation like this? Actually, it's the Gaussian. It's the normal distribution. And why? Because of the central limit theorem actually. So if you don't know, if you haven't had probability theory, if you don't know central limit theorems, no matter if you won't really use it, I'm just explaining where it comes from. So what does the central limit theorem tell us? The basic one. It says that whatever is the distribution, if you average it out sufficiently, if you average out sufficiently more copies of this distribution or if you add them up sufficiently many times, what you get is a Gaussian. You converge to a Gaussian, right? So what this means in practice is that if you have a process, some kind of physical process or whatever, where there are many small sources of noise that all come together and all add up, the result will probably be Gaussian or close to Gaussian. So if you, I don't know, in high school physics, if you do an experiment like you're rolling the ball down a slope and then it comes to a certain distance, then as the ball rolls, there are billions of small impacts on the ball. There are imperfections in the plane, the ball is imperfect, there's wind or whatever, and every one of these imperfections is definitely not Gaussian. Every one of them makes some small impact in a specific direction, actually, probably. But when you add them all together, it's a Gaussian, because there are a lot of them. So, I mean, there is a theorem, there is math behind it, but let's just leave it here. So, when you average out lots of small notches that go in opposite, in different directions, what you get is more or less a Gaussian, unless there is some systematic bias inside. Like, if all of your notches are in the same direction, then, of course, you don't get a Gaussian. But that's a different story. So this is why this noise, this error in linear regression, is indeed most natural to model with a Gaussian, with a normal distribution. And that's why the normal distribution is called normal, and that's why it's also important, right? So if you just look at its shape, at the density, you wouldn't understand why it holds such a special place. Well, it's special because of the central limit theorem, because everything converges to a Gaussian in a way. And so if we do this assumption here, p of, sorry, not p, but Gaussian already, normal distribution of yn around w times xn with some variance sigma squared, it's a one-dimensional Gaussian. We are talking about yn, right? Now this will be our, so this was the first assumption, this is our second assumption, that the center is a linear function, that's the linear regression, and this is the third assumption, that the noise is Gauss, okay? There is a fourth, but we'll get there. So what is the, let me write down the density of the Gauss, and it's one over square root of two pi sigma squared times e to the power minus one over two sigma squared times yn minus w times xn squared, and that's it, okay? So looks pretty complicated. What do we do next? Next, our first job is to maximize the thing, right? So we want to, let's say I want to get the maximum likelihood hypothesis on the weights. I need to take the likelihood and I need to maximize. How do you always inevitably do it in practice? The very first trick that is always applied and it's usually like understood without even explicitly writing it down. In machine learning, the likelihood is always, as we discussed, a big product of stuff, right? So it's a product over all data points and there are lots of data points. And we multiply the likelihoods of data points all together. So when you have a big, big, big product, what you always want to do is take the logarithm, right? So you want to convert the product to a sum. Because if you keep multiplying small numbers like probabilities, it will be very difficult numerically, right? So the first step is always to take the logs. So log P of D given W. And now this formula is the sum over N. This is what minus 1/2 times log 2 pi sigma squared. I'll leave it to that. Minus 1 over 2 sigma squared Yn W times Xn squared, right? And now this is a constant that goes out of the sum. So it's minus N over 2 log 2 pi sigma squared. This can also go out of the sum. And inside the sum, we have Yn minus W times Xn squared. And now our problem, our equation is, I want to maximize this with respect to W. There is a minus sign here. So if I just look at this sum, this one doesn't have any Ws. So this one is irrelevant, it's a constant. And the W is in here and there is a minus sign. So what I do with this sum is I actually want to minimize it, right? That's it. There you go. That's the motivation behind having a sum of squares. Specifically squares and not absolute values, not exponents, not anything else. The story, of course, does not stop here. It's only the beginning. One sec, did I forget anything? Oh, yeah. And one more thing. I promised to go back to the fourth assumption. So there is a fourth assumption which is kind of hidden over here. And the fourth assumption is that the variance is the same over the whole dataset, right? In statistics, it's called, there is a difficult word, homoscedasticity, I think. So if you have a homoscedastic process, it means that the noise variance is constant across the whole process. And it's the assumption that allows us to actually take the sigma and get it out of the sum and not care about the sigma. And it can be violated in practice, right? So in practice, it's quite possible that you can have points that go like this. At first, they are dense, and then they become more noisy, for example. And you still want to have a single straight line that describes all of these points. It may happen. But yeah, if something like that happens, then you need to modify the loss function. You need to actually explicitly notice this, which is non-trivial, and then understand what it tells you about the loss function. So this is, by the way, one of the most direct reasons why you actually want to understand this probabilistic approach. Because it may seem at first glance that, okay, so we explained y-squares, but it doesn't change anything. We are still minimizing the sum of squares, right? But the point is not only, so why do we want to understand stuff? We want to understand stuff in order to notice when it stops working. We want to understand the assumptions behind the sum of squares so that when they are violated, when we are not in this situation, we actually notice. For example, when our variances change in the middle of the process, or for example, when we have reasons to believe that all of the noise is only in a single direction. So now you want to have an asymmetric noise distribution, a noise distribution that's only on the positive part of the line. Also, there are variations of linear regression like this too, of course. It's not like you need to do any new math here, but you need to notice this and to apply the correct math. Okay, so this is our first step and we compute the sum of squares and blah, blah, blah. But of course, we want to apply our Bayesian story, right? So we want to say, what I'm actually interested in is not p of d given w, but it's p of w given d, right? Which means that I need to have a prior, right? What does a prior look like for linear regression? Well, it's a more complicated thing. And again, as soon as we get to something like Bayesian inference, something like prior distributions, well, the probability theory becomes a bit messier. Like in coins, we had a very simple discrete likelihood, just two outcomes. But then as soon as we went to the prior and posterior, distributions became continuous. There was no way around that. Here, everything is continuous, but from the single one-dimensional clean Gaussian, now we need to go to a multi-dimensional distribution, right? So now there are several different weights, and we want to have a distribution on them. But before we choose it, what is going to happen with our optimization problem? If I now want to maximize the posterior distribution, what does it actually mean in terms of the numerical problem that I'm solving? Well, to be honest, it changes quite little. So what we are basically saying, and this is also true in the entire machine learning, we are basically saying that, okay, proportional means that there is a constant which doesn't matter, right, for maximization. And then we have this log likelihood, which we already had before. And then there is the log prior. So basically, I want to maximize these guys together, right? And the log prior, you probably, in some previous classes, you probably have seen already all of this log prior stuff. And you usually call them regularizers, right? So regularization is actually the process of putting a prior on the parameters of your model. So what is the difference between these terms in practice? The difference is that the regularizer does not depend on the data, right? So it's the part of the loss function that is only about the weights, only about the model parameters and not about the dataset. And so formally, it's our prior beliefs, it's what we think about the weights of our linear regression before we start getting the data. And at this point, it may sound quite strange because if for a coin we did have an intuition, like a real-life intuition that coins are approximately fair, right? So for a coin that I take out of my pocket, obviously I do have some kind of prior beliefs that are actually quite strong. For linear regression, it seems like we don't, right? So for linear regression, it seems like the regularizer shouldn't be doing anything. How do I prefer one slope of this straight line to another slope? I don't know. If I don't have any data, they all are the same for me, or at least they should be, right? Well, here is how it actually works. So to make a good illustration, I won't go to the multidimensional case, but I will make a multidimensional regression out of a one-dimensional regression. So an example that I always give and that I think illustrates this the best is let's extract some additional features from X. So this is also an important discussion in its own right. So how do people usually apply simple models like linear regression? Well, they have their axes, their original inputs, and sometimes it so happens that you can just treat axes as numbers and do a linear regression and your output is W times X and everybody's happy. But more often than not, before you go to learn the weights, you actually extract some kind of features from X. Sometimes, and then you get some, I know, Phi of X, Phi of X, and then you do the linear regression and the output is W times Phi of X. Okay? So sometimes feature extraction is about reducing the content. Like if you want to do linear regression on images, then obviously it makes no sense to do linear regression on the pixels, right? You first want to extract some semantically rich features and then do the linear regression. Sometimes it's the opposite. Sometimes X is very simple and you want to describe a more complicated dependency between X and Y and you need to extract additional features. So this is an example like that. And suppose that I have one dimensional regression. So there is only one X, there is only one Y. But when I look at my points, I kind of realize that they're definitely not linear, right? I realize that they don't look like a straight line at all, but they kind of look like a parabola. They kind of look like a quadratic function. So here is a question. Can I use linear regression to actually learn a parabola here? To learn something like w0 plus w1 times x plus w2 times x squared? Yes, if we make a feature, we're processing it. Yeah, precisely. So the trivial linear regression would only give you this, but we already know that we can add more features. We did it in a trivial way, now let's do it in a less trivial way. So let's go from x to this feature vector, 1x, x squared. And then you multiply, and then you do just linear regression, right? And when you do linear regression on this, what you are actually minimizing, what is your loss function? It's the sum of yn minus what? Minus, well, w0 plus w1 times x plus w2 times x squared. There we go, right? So you are actually feeding a parabola. And actually, this discussion is extremely relevant to deep learning because what is the thing that deep learning is doing? What are the neural networks always doing? They are learning good feature extractors. That's the whole revolution. So before deep learning worked, what we would usually do as machine learners, we would try to invent this feature extraction part by hand or for some other reasons, right? And then we would run relatively simple models on these features. Of course, not necessarily linear regression, but relatively simple models. What neural networks do is they make feature extraction a part of the model. So now the feature extraction also has weights. And how does a neural network actually look? Let's say I have an image at the input. Then there are lots of layers that do different interesting stuff, blah, blah, blah. But then at the end of these layers, we have actually a vector of numbers that goes into the final layer. And the final layer, depending on what problem you are solving, if you're predicting a number, it's usually a linear layer. So if your output is supposed to be a number, not a classification problem, then the last layer is probably linear. Almost always. I don't know any exceptions. What this means is that this part of the network is doing feature extraction for the last linear regression layer. The last layer is actually linear regression, but not on the pixels of the input, not on the X, but on the features extracted from X. And of course, the hard part is learning the previous layers. The last layer is kind of easy and we are now doing the easy stuff, of course, but it's there. So basically any big complicated neural network that predicts a number almost always ends with a linear regression. Any complicated neural network that does classification ends with a logistic regression. We'll get there later. So the rest of the network is extracting features for this last final layer. That's the connection. That's why these linear models are still very, very relevant for deep learning as well. All right. So back to linear regression. Yeah, and at this point, I think I want to make an example of this. So I put some more stuff here, but yeah, for now, we are getting there. Yeah, for now, let's... Okay, yeah, there we go. So let me show you a polynomial regression problem. I have the true function, the original function, which is actually not polynomial. So we don't expect to capture this function exactly. It's a sine wave. But I take one period of this sine wave and I put the points around this one period of the sine wave. Okay, so the stars are the points, the horizontal line is x, there is only one dimension here, and the vertical line is y, the vertical axis is y. So when you look at these stars, you kind of immediately realize that they are not linear. And if you actually fit linear regression, you get a straight line, of course, you get some line, sure, but the error is very high. It's obviously not describing these points well. So first question to you, what do you think is the proper degree of the polynomial? What would be a good degree of the polynomial? I can't put a sine wave here, but I can do a polynomial. Can you please repeat the question? Yeah, what would be a good degree of the polynomial to fit these points? So the straight line, degree one, doesn't work. What would work? I think the degree of three. Yeah, exactly, yeah. So a parabola probably also doesn't capture this, right? So it's a little better, but not much. But if you go to degree three, then yeah, the third degree polynomial has this two, one minimum and one maximum it can have, and which kind of already can match one period of the sine wave, right? So if I train a third degree polynomial, so the regression with four weights, including the intercept, then it's already a pretty good fit. And if I compute the errors, I don't think I have it here, but if I compute the errors, they will be fine. But what happens if I keep increasing the degree? So if I increase it to four or five, I don't think much will happen. I think they will look approximately the same. So if you look at the degree four and degree five curves, they are slightly better, but it's basically the same stuff. When do you think it's going to break? Or is it going to break? Or can I increase the degree indefinitely? Maybe 10 or 20 it will break. Okay, 10 or 20. What do we need to know to answer this? What do we need to know to answer? Yeah, like, okay. At least I know if we will make a polynomial with a number of points, it goes to which point it will break. Yeah, sure. So yeah, of course we cannot predict in advance when exactly it's going to start to be bad, but we definitely know when it's certainly going to be bad. And here I have 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 points. So for 11 points, if I do a polynomial of degree 10, a polynomial of degree 10 can just pass through all of these points exactly, right? So let me keep the third degree and add degree 10. And this is what an interpolation polynomial looks like. So it passes through every point exactly, which is great. But so the training set error is exactly zero, but the test set error is huge, right? It's completely useless for predicting. It has this very strange peaks on the left, on the right, even in the middle a little bit. So it's definitely a very bad model, much worse than the orange curve, right? And that's indeed, as you write in chat, that's the classical picture of overfitting. So we have too many parameters. And in this case, of course, it's quite obvious that we have too many parameters. And what do we do? How do we notice this overfitting if we can't just look at the picture, right? In real life, there would be a high dimensional input and we wouldn't be able to just look at the picture. How do we notice it? Well, in this specific case, it's very easy to say, just don't do this, right? So this is, of course, a degenerate case. This is a very simple example and you can say, well, obviously, if we have 11 points, we don't want the polynomial of degree 10. That's easy. You don't need any theory to understand this. But in real life, you usually cannot avoid this completely. So in this simple example where I have a one-dimensional x and I choose the degree myself, sure, I can just look at the pictures and choose. That's why I'm showing it to you because the pictures make it obvious. But in real life, what's going to happen is actually this. And I'm answering this unasked question of how can this happen in practice with linear regression? And the answer is basically this. What would actually happen to you when you do linear regression? You have your data set and you have in your data set points of degree d. So in dimension one, nothing bad will ever happen. Dimension one is easy. But you have points of dimension d and you are trying to do linear regression and you are failing. Okay, so if linear regression works like this, perfect. You don't need anything else. But you are failing. You can see that the relationship is not really linear. You want something else. You want something more, right? So this doesn't work and you make the next step. What is the next step? Let's do a quadratic dependency. But unlike the one-dimensional case, where the quadratic dependency just adds one more feature and you control it very finely. You go to degree three, you add one more feature. You go to degree four, you add one more feature. So you choose the number of features explicitly, basically. If you have a multi-dimensional vector, it doesn't work like that anymore, right? So if you go from x of dimension d, sorry, of length d, to a quadratic feature vector, what you actually get is something like 1, x1, xd, then x1 squared, x1, x2, x1, x3, and all the way to xd squared, right? So the actual number of features is something like, maybe I'm missing some plus or minus one, but something like this, something on the order of d squared, right? Which is quite bad in the sense that now, if I start with a vector of size 100, and I go to a quadratic dependency, I immediately get not 200 features, not even 500 features, but I get, what, 5,000 features, about approximately. And of course, when you go from 100 features to 5,000 features, overfitting can happen, right? So this is the actual mechanism. Of course, in dimension one, it's always easy, but in high dimensions, there is no middle ground. You cannot go to degrees three halves, right? And actually, when you look at all of these features, you understand, of course, in your head, that you don't need all of them, of course. Of course, you don't need all of them. You only need some of these quadratic dependencies. So in reality, what matters is maybe the relation, the dependency, the connection between x1 and x3, and then maybe xd squared, and then maybe something else in the middle, and that's it, and the rest could be zero. But the point is, you don't know in advance which ones. That's the whole point of learning, right? You need to figure out which of these interactions matter. They're called interactions in statistics when you add this. Features like X1 and X3. Which of these interactions matter? And you can't do it if you don't start with them all, right? So overfitting is kind of inherent in machine learning. You cannot avoid it even for linear regression, let alone something complicated like neural networks. So getting back here, how could we notice that something bad is happening if we cannot just look at the picture? How can we notice overfitting? There is a simple principled answer. A principled answer would be, so let's do a test set, or to be more precise, a validation set. Let's set aside part of the points. Let's measure the validation set error. And when the validation set error starts to grow, we stop. That's the standard procedure in machine learning. And if you can do it, it's fine. But again, in this example, you can't really do it. So, well, I mean, maybe you can imagine like adding these quadratic terms one by one. But then you would need to kind of go through all of them and then go through all of them again. Probably would be impractical. But if you add all of them at once, you just get overfitting. You get this high test set error and what do you do? There is no continuous process that you can just stop at some point. So what is another symptom of overfitting happening here? How else could it work? Well, here I output them over here. You can also look at the coefficients. And this sounds a little bit counterintuitive, but we are getting back to the stuff that is actually useful for us now. If you look at the coefficients of these polynomials, let me do a lot of them. So the plot is now completely unreadable, but let's look over here. If you look at the coefficients of these polynomials, you will notice that as the degree increases, the coefficients grow, but they grow kind of in a bounded way. And then when overfitting starts to happen, in this case, it's only at d equals to 10, but it could happen a bit before, you see a sudden jump in the coefficients. You see coefficients like plus or minus 50. And at this point, you can notice that. And you can say, well... So this is the tricky part here. This is the not really formal part. You can say, well, I have like 10 points, 11 points. And the x is always about 1. So it's from negative 1 and a half to positive 2. And the y is from minus to plus 1. And these points are described by a model with coefficients like 50. That doesn't sound plausible to me. Okay? So this is the intuitive reading of this. And the formal reading of this would be my prior belief about the coefficients is that they should actually be relatively small. They should, for this data set, they should be on the order of plus or minus 1 or maybe 2, but definitely not 50, right? And you can also think about it this way. Maybe this picture I also find very helpful. So when you do standard linear regression, if you have one-dimensional x and standard linear regression, you have two dimensions of weights. So you have this two-dimensional space of weights to choose from, right? And then you go to quadratic regression, you get a three-dimensional space of weights, which is, now it's not a mathematical term, but which is kind of larger. you have a larger variety of models to choose from. I can make it precise, but we won't have time in class to make it precise. And then you go to dimension 4, you get even more different models. There are much more polynomials of degree 4 than there are polynomials of degree 2, because polynomials of degree 4 include polynomials of degree 2 and then some, and a lot different polynomials. So models of degree 4 can explain, can approximate more data sets, many more different dependencies between points than polynomials of degree 2. So you get this much larger set of weights to choose from. And then you go up to degree 10 and at some point this variety becomes too much, right? And this gets you to overfitting. So one way to reduce the variety would be to go back in the dimension. But if you cannot afford that, like in this multidimensional example, if you can't just do a smaller set of features, then what you could do is you could try to limit this variety inside the big space. So you could say, okay, I have to stick with the 11 dimensional space of weights, but at least let me look for solutions inside, like near zero. At least let me constrain the vectors in this 11 dimensional space. So I kind of, again, intuitively, I kind of want to constrain the variety of the models. And that's what regularization does, and that's what prior distributions do. So in this case, in this case, what we actually do here, how can we solve this problem? It would be, we need to add a prior distribution that would tell me that the weights are relatively small. So what does it mean? It means that P of W should be like somewhere around zero, concentrated somewhere around zero. Probably we don't want to completely exclude anything. We want all vectors to have some non-zero density, but we want it to be concentrated around zero. And then just go, just reduce in other directions, in all directions, right? And what kind of a distribution could that be? Well, the obvious answer, it could be a Gaussian, right? So you could say, okay, let's say that P of W is a Gaussian centered around zero with some covariance matrix. And since it's a prior distribution and I don't distinguish between different weights, I see no reason to have anything but the identity matrix here. So I don't, in advance, I don't know which weights will be dependent with which. So let me, let the prior be independent. And then I don't want to actually go into, in this class, I don't want to go into the densities of multidimensional Gauss, et cetera. If you're interested, I do teach classes like this, fortunately, in Russian, but there are quite a few Russian speakers among you. You can watch on my website some other classes where I spent a whole semester on this kind of stuff. But let me just say that from this P of W, the log P of W will be some constant minus 1 over 2 sigma 0 squared times the norm of the vector W times the sum of W i squared, right? And then if I add this prior to my likelihood, which is already fixed, this is part of the model, then what I actually get is a loss function that looks like this. Sum over n y n minus W times x n squared. That's the likelihood part. And let's, okay, let's put 1 over sigma squared here, plus 1 over sigma 0 squared, the prior variance, times this sum of squares of W's. And I want to minimize this. So again, constants don't really matter. So I can put this sigma over here and cancel the 2. And what I get is exactly the sum of squares with what is often called an L2 regularizer. L2 means regularizer. The regularizer is often the norm of the vector of weights. And then the L2 norm in the L2 space is the sum of squares, the Euclidean norm. So that's an L2 regularizer. And then I can use this regularizer and I can fix the problem. So if, let me see if I have, let me see if I have, yeah, I will skip the local features. I don't think I have time for that. Yeah, I do have it. Okay. So first of all, before I show that, before I show regularization, let me say that this kind of overfitting and regularization and everything is dependent on the dataset also, right? So notice how when we went to degree 10, we got severe overfitting only because we had exactly 11 points, right? If we just add more points, a degree 10 polynomial will be fine. That's kind of obvious, but I wanted to mention it. So if I have 100 points, not 10, then of course a degree 10 polynomial will not be severe overfitting. And that's for regularization. Here is the data set. Here is the original function with no regularization. It's the interpolation polynomial. And alpha is basically this coefficient, this guy over here. So as I increase alpha, it will become more important, right? So it will be the shape of this curve, the shape of this polynomial will be determined more and more by the regularizer and less by the actual training setter. So if I have this kind of small regularizer, like 1/1000, then you can see that actually... Actually, it's already pretty strong. Okay, let me make it even weaker in this case. Yeah, so the absolute values of the coefficients are already kind of reduced, but you still see some of this local... ..extremes at the... Okay, here is another illustration. Obviously, I do the points at random every time, so for this specific set of random points, even a very small regularization is enough. So actually, it would take a lot to straighten out these guys on the extremes, but the other special features are kind of already straightened out. But okay, so let's make the regularizer even smaller. Yeah, so at some point, you can see that it gradually irons out this overfitting, and I already showed that with some good value of alpha, you can get a very good curve over here. Let's see if I can even straighten out the sides. I'm not sure I can, but yeah, I can make this effect smaller at least. Oh, okay, here. I straightened it out on the left, but not on the right. So yeah, as I keep increasing the regularizer, remove this one and keep increasing this one. As I increase the regularizer, okay, so this is a good curve now. I will see that the degree 10 polynomial, it's still degree 10. It's still degree 10. It's properly degree 10 if you look at the coefficients. Yes, they become closer to zero, but they are not like everything is zero except the first three. No, they are still meaningful over here, for example. So it's still a degree 10 polynomial, but now it behaves much better, right? So we are kind of got rid of the regularizer, of the overfitting by regularization. But then of course you can overdo it. So if you go to something like 10, you will get like a curve that a degree 10 polynomial that doesn't care about the points at all, right? It only cares about the regularizer. And in this case, of course, it's also a bad model. So as with all things in life, there is a trade-off. Okay. And what else did I want to say here was that, again, I don't want to go into the math here. And probably I will have to skip the Bayesian part here. But I do want to mention that if you look, so the L2 regularizer, the Gaussian prior is indeed special for linear regression. So as we discussed yesterday with these conjugate priors, with the prior in the form of the likelihood and blah, blah, blah. You can notice that here also the shape of the Gaussian regularizer matches the shape of the Gaussian likelihood. It's a quadratic function of W, right? So, of course, it's convenient to add two quadratic functions of W. You also get the quadratic function of W and to get the Gaussian again. So this is the conjugate prior, and you can go from Gaussian to Gaussian in the space of weights. Let's not go much further into that discussion. But linear regression also gives us a good example that you don't necessarily have to do that. So here you can have very good reasons to choose different regularizers. Very good reasons like... So one other common regularizer for many models and for neural nets as well would be an L1 regularizer. So let's start from this. So what if instead of adding a sum of squares, I would add a sum of absolute values here? So notice that there is a difference here, there is an asymmetry. The error, the noise is a property of our model. I mean, yeah, we kind of choose it, but we are supposed to choose it correctly. There is a right answer and the wrong answer here. Like what is the actual noise in the actual process that we got the data with? That would be the perfect correct answer. There is some kind of underlying truth here. Probably it's not exactly Gaussian. Probably it's an approximation. But there is a way in which... There is the correct answer to the question of what is the right likelihood. But there is no correct answer to the question of what is the right prior. It's completely our choice. We choose the prior to match whatever we want. And we might want to choose something else. So this is L1 regularization. And so you may also encounter these terms. The linear regression with L1 regularization is called the LASSO regression. LASSO is actually an acronym for something like least average shrinkage. I forget. It never comes up. And this is called the REACH regression. REACH is not an acronym. It's this REACH, the Gaussian REACH. But anyway, you might want to choose a non-conjugate prior because it has better properties. So do I have it here? Yeah, I do have it here. So let me show these properties to you. We don't have time to discuss why, but at least let's see how it works. So if you look at the same kind of regularization weight, but with the LASO regression, with the L1 regularizer, not the REACH regression, not the L2 regularizer, you will see that it also is like a pretty good curve. It still, it doesn't overfit. It goes where you want. Probably we need some kind of lower weight here. Yeah, okay. So now this looks a lot like the best REACH regression that we got, right? So the curve is approximately the same. But if you look at the actual coefficients, you will see something very different. You will see that many of the coefficients have gone to exactly zero and some are clearly like on their way to exactly zero. With rich regression, they were all decreasing more or less isotropically, so to speak, right? They were all decreasing together, getting closer to zero, maybe not with exactly the same speed, but they were all non-zero when we checked. Here, some coefficients become exactly zero or very close to zero and you can send them exactly to zero, nothing will change. And sometimes that's a desirable property, right? So sometimes you might want to have sparsity in the results. So like this is what we would call a sparsity-inducing regularizer. And for example, I think it would be a better fit for our equation over here, right? So if I get a lot of different features and I need to choose out of them, then instead of some arbitrary setting the threshold and picking which small number is better than another small number, why not choose a different way of regularization to set some of them exactly to the wrong, okay? So this is our choice. This is in our hands. Okay, so we need to have a break by now, but let me summarize. I discussed linear regression. We didn't go into the actual Bayesian inference. It doesn't much matter for the rest of our class. So it's okay that we skip it, but I did want to highlight two important points. First, linear regression is relevant to any kind of complicated neural network still, and we will see it in architectures. But most importantly, all of this probabilistic machinery and all of these discussions about likelihoods, priors, probabilistic assumptions, how they all come together, what they are actually doing for us in deep learning is they are giving us the loss functions. Okay? So notice that when I write a general formula like this, it doesn't matter what the model is, right? It's just about... Okay, so this is too general a formula. This is about everything. But when I write even a formula like this, okay, the model is only over here, right? And this is the noise distribution. But the linear model is only over here. And of course, I can change, if I keep the noise distribution Gaussian, I can change the model to something else. So if I was... I can do any kind of function over here, and maybe it will be more difficult to optimize. It will not be quadratic. It will be a completely different thing in practice. But I still get the same kind of loss function, square deviation, and I still get the same kind of regularizer if I want. And this is still a very common loss function, whatever the model is. And this may be a neural network, may be a very complex neural network. It may be anything that we will discuss later in class. But then it gets plugged in to a loss function that comes from some probabilistic assumptions that we make. That's my point in the first part. Okay, any questions? Okay, good. So let's have a break over here. And then I will briefly discuss logistic regression. We will not go into the same kind of detail, but it's really important to get the softmax function, right? So we will discuss the main assumption of the softmax. And then finally, we'll get the neural networks. I promise. Break. Okay, let's continue. We discussed linear regression before the break. We are gathering all through the slides. Linear regression, sum of squares, the Gaussian noise hypothesis, blah, blah, blah. We can get a posterior distribution. We can get the predictive distribution. We didn't get there, unfortunately. We didn't derive this formulas, no matter. This would be interesting, but I think it's time for us to move on. And our next point is classification, which is probably even more important for deep learning for neural networks than linear regression and predictive numbers. So our third point is the logistic regression. I'll try to be quick about it, but I do want to get the general idea across. So suppose that we are solving a classification problem. So what is classification? You want to distinguish cats from dogs, and if you are in a lower dimensional space, you can visualize it as trying to get a separating decision surface between two or more sets of points. The difference between classification and regression is in the nature of Y, right? It's in the nature of the target variable. So classification, of course, is still supervised learning. We still have a data set that looks like this. But now, for linear regression, YN was a number, but now YN is like a class label, right? So it's just a discrete variable with a finite set of values. It's one of several classes that we want to distinguish. So what does it mean for us for constructing the model, for building the likelihood, for everything like that? It means that since we are not predicting a number, what, I mean, okay, not just since we are not predicting a number, it means that in most cases, even though we are not predicting a number, we still do want to have a number at the output. So what is kind of bad about discrete target variables? And we will come back to that in deep learning as well. The bad thing about the discrete target variable, so let's say that I'm doing like a simple threshold rule for classifying and they have like one class is the zero and then if x exceeds some threshold, then I start to output one, right? So this is like the simplest classifier possible. One dimension, one input, two classes, and I choose by threshold. What's the problem with this function if it was my output? The problem is that this function, since it's piecewise constant, right, it has no derivatives. I mean, it does have derivatives, but its derivatives are zero everywhere. So what this actually means is that if, so if this is just x and this is, and the thing that I'm learning is only a, then it's fine. But what if the input is actually some kind of, as it always happens in real life, in neural networks and everywhere, what if the input is some kind of function of x with some weights, some model, some feature extractor, et cetera. If that happens, then we don't know what to do with this feature extractor. We don't know how to train it. Because we can take the gradients, and we will be taking gradients in the learning, but if you take the gradient of this function, it's always zero. It doesn't give us any information at all. And you can understand that intuitively as suppose that I take the weights w and I tweak them a little bit, I change them slightly. Then the input to this threshold will move a little bit. Did it move in the right direction or in the wrong direction? By looking at the output, we have absolutely no idea. The output does not change. It does not change, it does not change, it does not change, then suddenly it changes. That's not something that we can actually train through. So what we actually want, and both for this practical reason and also for conceptual reasons, like both for this practical reason and for conceptual reasons, like we also want to estimate our uncertainty, we want to evaluate how sure we are. What we actually want to have at the output of a classifier is not just the class label, but a probability distribution on the classes. So let's start with two classes. If I only have c1 and c2, what I actually want to have at the output is p of c1 given x. Okay, it's p of c1 given x. That is for a new point. I want to evaluate how likely it is that it belongs to the first class as opposed to the second. And where does the logistic regression appear? What's the reasoning behind it? Well, actually, it's pretty straightforward. Or, I mean, we could make it more complicated, but let's not. A straightforward reasoning behind the logistic regression looks like this. So let's assume that I want a linear model. So I do want to have a linear model, a linear separating surface. I do want something that includes w times x, and that's how x should appear in there. Yeah, good question. I also got a window that said internet is unstable. Did it fix itself? Is it okay now? One, two, one, two. Works right now, but sometimes the... Yeah, yeah, it's better now. But sometimes the writing is unintelligible. Okay, so, okay, if it's better now, then just keep me informed if anything changes. Okay, so anyway, suppose I want p and I want it to be derived from a linear function of the features. So I want the axes, the inputs to go through a linear function. So can I take this probability and approximate it like I did in linear regression with a linear function of the inputs? Kind of obviously not, right? Because the probability is a number between zero and one. And if I approximate it with a linear function, of course it will go to infinity. At one end, the other end, everywhere. So it's not a good idea to model probabilities by linear functions, right? What can I do instead? Well, I can use the base theorem. P of x given c1, P of c1, P of x, right? And then I can expand this. Since I only have two outcomes, two classes, it's pretty easy. I can just say that P of x is one possible numerator plus the other possible numerator, right? Now I have a lot of different things in here and I only want to model one thing. So let me divide by the numerator and I get 1 over 1 plus P of x given c2, P of c2 divided by P of x given c1 times P of c1, okay? So this thing, you can view it as P of c2 given x divided by P of c1 given x, it's the same thing. And this thing is known as the odds, right? So the odds are, well, like when you say in real life, when you say I give you 50 to 1 odds, what does 50 to 1 mean mathematically? It's this ratio, right? It's the ratio of the probability you assign to one outcome divided by the probability you assign to the other outcome. That's what it means to give odds. And as I just said, odds can be like 50 to 1 or 1 to 50. Right? So odds are not constrained by 1. They are ratio of two probabilities, so they can go to infinity. But does it make sense to model them as a linear function? Well, again, not really. Because even though they can go to infinity, they still cannot be negative. Right? It's a ratio of two probabilities. And the linear function will be negative somewhere. But half of the space it will be negative. So this is also not a natural thing to model with a linear function. But we are getting there. Just one small step left. We have a positive quantity and we want to model it somehow linearly. What is the transformation that we need? Well, we can take the log again, right? So if you take the log of something that goes from zero to infinity, not including zero, then now you get something that goes from negative infinity to infinity. So then we go to this, e to the power, it's customary to put a minus sign here. It doesn't really matter, but usually people do. So now the fraction flips, ratio flips, p of c2. So this guy is called the log odds, the logarithm of the odds. And now this indeed does make sense to model with a linear function, because now it's a quantity that goes from negative infinity to infinity, and it has exactly the properties that we want. At negative infinity, you go to zero, the probability goes to zero. At positive infinity, the probability goes to one. And in between, it monotonically increases. So logistic regression is exactly this model. Logistic regression is the model where you say that p of c1 given x is one over one plus e to the power minus a linear function of x. This function is called the logistic sigmoid. So sigma of a is like one over one plus e to the power minus a. And it's this, it's a sigmoid function, right? So it goes from negative infinity to infinity. It goes through one half at zero and it asymptotically goes to one on the right and to zero on the left. It's an important function in machinery. Then we get what is p of c2 given x. Well, unfortunately, it's a bit more complicated because it's one minus sigma of w times x, right? So if I try to do like the likelihood of a dataset for logistic regression, again, I do a product of p of y n given w and x n, but then it will be a product of like sometimes it's sigma and sometimes it's one minus sigma, and then it's sigma, and then it's sigma, and then it's one minus sigma and so on, right? So it's a bit more complicated. It's a more complicated function than the linear regression. It's not quadratic, of course, anymore, and we cannot do it in closed form, but we can do something like gradient descent or second-order methods in this case also can be used. We can actually optimize the likelihood. We can add priors and do it in a regularized way, and so on and so forth. So this is actually a linear model in machine learning and statistics. A linear model is something that is a function of this. It doesn't have to be linear all the way, but axes occur in there as a linear combination. And it's a very natural linear model for binary classification. How do we make it more than binary? How do we insert several classes here? Well, here I was just modeling one quantity. And if I have basically a coin toss, if I have only two classes, then sure, I only need to model one probability. But if I have several classes, c1, c2, ck, then now it's not enough to have only one vector, w, that is multiplied by x. Because from one number, I will not get k minus one different numbers, right? And I need k minus one different numbers to model this die roll between k classes. So instead, now I basically say that, okay, I will not model a single logout for between two classes. I will just, I will say this. So p of c small k given x, just like this, it's p of c small k, p of x given c small k, divided by the sum overall classes, right? p of c s, p of x given c s. And let me just, again, take the logs, so I can also have negative numbers. So e to the power of this divided by the sum of e to the power of the same, but about class s. And then let me just say that now I'm modeling every exponent here with its own linear function. So I'm saying that w k times x should be like p of ck times p of x given ck. Notice that it doesn't quite work as I wrote it because the thing on the right cannot be negative. They just said it's a bad thing. But to be honest, it doesn't matter. So when you get negative numbers from some of the scores, These are usually called scores or affinities or something like that. So it's like a measure of how likely class k is, but not a probability, just a number. So when you get negative scores, you can just cancel out the negative parts. So if you have e to the power minus 2 divided by e to the power 1 plus e to the power minus 1 plus e to the power minus 2, the same, then you can just take e to the power minus 2 and cancel it out, right? So and everything becomes non-negative. Like now it's e to the power 0, e to the power 3 plus e1 plus e0. That's it, right? So you can always, in this formula, it doesn't matter if sometimes you get negatives because you can always add a baseline like this and it just cancels out. And that's it. So this is how you do multi-class classification. And this thing, now it's a vector function, right? So now it's a function that maps the vector a to another vector full of these guys. So like the kth coordinate is e to the power ak divided by the sum of e to the power as, right? Normalized exponents. And this is called the softmax function. So the softmax of, okay, let me write it again. A1 and a2 ak is another vector. And at the kth spot, we have e to the power ak normalized so that it becomes a vector of probabilities. That's it. So that's the softmax. Why is it called the softmax? Because the exponents have this tendency to, you know, exaggerate the differences. Like if you have one of the A's, one of the arguments, to be significantly larger than the others, then what you get as a result will be basically probability 1 for this guy and probability about 0 for the others. So we are kind of taking the maximum of the arguments, but we are doing it in a soft way, as a continuous function that is never exactly 0, that you can take derivatives of, that allows for gradients, gradient descent, et cetera, et cetera. So that's a soft version of taking the argmax, okay? And I won't go into more details about logistic regression, not exactly our subject, but this part is important because, again, this is the last layer of almost every neural network. If you have, I don't know, GPT-5, which is an insanely complicated model, I have no idea how exactly it works because nobody tells us, but if you have GPT-5 and it's a language model and it's supposed to produce the next token right now, then what is the last layer of GPT-5, I'm sure? The last layer is this. After all of this internal machinery, which is very complicated, we get a layer of scores for every token and then they go through the softmax and the softmax turns them into the probabilities of tokens. That's how it always works at the end because it's completely hopeless to try to produce probabilities immediately. It's not how neural networks work, it's not how linear functions work, it's not how anything works. What you do is you produce some kind of scores and then you turn them into probabilities with the softmax. And yeah, sure, it's also very common, now I cannot vouch for GPT-5, but it's also very common that the layer before this is linear. So we get an exact logistic regression at the end of a neural network. So we get to some features, when we do a linear layer that gets - so okay, let me explain, because I don't think I will explain it later, and now is a good spot. So we have some input, it goes through the neural network, and then let's say we get to the final feature vector, right? To the final, like, semantically rich, very intricate extracted features. And whether it's a cat or a dog is already somewhere inside. Somewhere in these features it says so pretty explicitly, but we are still not sure where, and we are not sure how to get, right? So how do we do it, what is the simplest way to process these already extracted features? Well, I could just do a softmax and assume they are scores. They are not scores, and there's probably the wrong number of them, right? So there is some number of classes, and here I have just extracted features that express my picture. Why should the numbers match? No reason, right? So the number of features can be different. So I do a weight matrix. I multiply W times Z, and the weight matrix, so let's say this is dimension D, and this is dimension K, like number of classes. So W is of dimension D times K, and then W times Z becomes the vector of scores. And now I go through Softmax, and I get a vector of probabilities for all the classes that I have. And this is my output, and the loss function now will be defined on these probabilities. There may be some variation here, but usually the loss function is just the... Well, it's a fancy name. It's the cross-entropy between the output and the target. But if you're doing classification, the target looks like a one-hot vector with one one at the correct class and zeros on the other classes, right? So, and the cross-entropy, when we get there, I will write it in more detail, but the cross-entropy for this kind of target will be basically just saying that I want to have the probability of the correct class to be larger. So, like, the loss function will be something like the negative log P of the correct class, and I want this to be lower, according. And that's it. That's how classification works in deep learning, okay? So, the interesting stuff happens over here, of course. That's what we are going to be discussing for the rest of the class. But at the end, almost inevitably, happens something like this. So, at the end, if you are doing classification, you want a vector of probabilities at the output. Can you get a vector of probabilities directly? Probably not. What you can get is a vector of scores, affinities, like numbers that can be arbitrary, but that reflect how well the input matches one of the classes, and then you convert them to probabilities. That's how this stuff works. Okay, any questions about logistic regression? I didn't go into much detail. All right, then. Then, for the rest of today's lecture, let's concentrate on neural networks. Oh, actually, wait one second, I'll check. Yeah, I don't have illustrations for classification code, but that's fine. It wouldn't show you anything anyway. It would be just a linear surface between two classes, or three classes. What's the point? Yeah, so we discussed logistic regression. This is what a logistic sigmoid looks like. Then we get logistic regression. This is the softmax function. This is what we model for the softmax, etc., etc. And logistic regression, even though it's a very simple model, it's a linear model, like one step from linear regression. So linear regression is just linear. This one is linear plus a sigmoid on top. But already for logistic regression, we cannot really hope to get a closed-form solution. So we didn't discuss it for linear regression because it really doesn't pertain to deep learning. But when you're optimizing a quadratic function like this, you can just write down the answer. It will be maybe not that easy to actually implement because it will be like the inverse of some huge matrix. And in practice, you would be solving the system of linear equations with some approximate techniques, iterative approximate techniques. I mean, it's a whole science. But theoretically, you can just write down the answer. You can write down the formula. It's a system of linear equations after you take the gradient. Here, it's already not. So if you look at a big product and you take a log and then you have a big sum of logs of things like this and things like this, there is no closed-form solution. So the only thing we can do is try to do it with some iterative optimization algorithm. And the main iterative optimization algorithm that we will be discussing tomorrow in great detail is, of course, gradient descent. So in logistic regression, you can actually do a second-order method, but in neural networks, you can't afford to. We'll discuss that as well. And we have to restrict ourselves to variations of gradient descent. Gradient descent is when you start somewhere and you go in the direction where the loss function is being reduced most quickly. And that is the direction opposite to the gradient. So gradient is the direction where it grows most quickly. So the opposite is where it decreases most quickly. And then you keep going until you find the local minimum. There can be many local minima in real life, in neural networks, etc. And we'll discuss that in detail, but not for logistic regression. All right. So with that, let me move on to some less mathematical, far less mathematical topic, but I hope also pretty interesting. And that is an introduction to deep learning. I will, again, try to make it quick and painless. I don't want to go into too many historical details or anything. But there are a few things that I want to highlight. A few things in the motivations, a few things in the, like, how neural networks evolved. And then we'll just go to the main meat of our class. That will be probably tomorrow. So neural networks, artificial neural networks, are called artificial because there are natural neural networks, right? There are neural networks in our brains and in the brains of other living beings. And, of course, a very natural motivation for a scientist would be, well, I want to build a thinking machine. There already are thinking machines in the world. I have a proof of concept right here. So let me study how the thinking machine in here works, and let's try to emulate it in a computer. Why not? It's all information process. And when you begin to study how the human brain works, it actually gives you some pretty important insights. So, oh, sorry, my picture. Now, this is not an artifact of internet connection for some reason. It is downsampled a lot. But anyway, you probably have heard at some point how neurons work, what a neuron is. So our brain consists of neurons. Biologists will tell you that there are different kinds of neurons. There are slight differences. But from our computational perspective, they are basically all the same. And they work like this. They have this processing part, the soma, the actual center of the cell. And then it has all sorts of tentacles, all sorts of little things going out of the cell and connecting to other things. And there are two kinds of tendrils, I guess the better word would be. There are two kinds of this growth. There are dendrites, which are relatively short, and which attach to the outputs of other neurons, and they provide the inputs. So there are many dendrites, like thousands for every neuron, and the dendrites get inputs for this neuron. And then there is one special part, one special tentacle of the neuron, which is called the axon. And the axon can be very long. There is a neuron in your spinal cord that goes all the way to your toe, to every one of your toes, actually. There are separate neurons. So they can be up to a meter in length or something. And the point is, the axon is the output. So computationally, every neuron has lots of inputs, several thousands on average, and one output. So far, pretty straightforward. Now, what is interesting about this, and this is a purely computational, very surface-like insight, but it's already pretty interesting. In the brain, so first of all, how does a neuron work physically? How does it send signals? It would be pretty difficult for a biological thing, for a biological mechanism to read out numbers. So it would be pretty difficult for the dendrites to capture the exact amplitude of an electrical signal and then process inside the neuron that from this input I got a 2.5, and from that input I got negative 1.46. That's not how biology works. Biologically, it's much easier and faster and more reliable to just capture bits, individual events, like is there a spike or is there not a spike? So neurons work actually in spikes. They do not or almost do not modulate the amplitude of their signals. Was it a spike? Yeah, I didn't tell. A spike is the electrical signal that the neuron sends out through its exon. So the neuron always fires spikes along its exons. And the other neurons who are attached to it, they pick up the signals. And the spikes are more or less the same. I think there is some variation, but it's not consequential. They are more or less the same. What changes is the frequency of the spikes. So if the neuron is relaxed, is not excited, then it sends out spikes with frequency like 10 per second, 20 per second, something like this. When it gets really excited, really activated, it starts sending out spikes with the frequency of like 200 spikes per second, okay? So there is a big range. And when a neuron sends out spikes more often, it means it's more excited. So now there is actually a numerical value. It can be more excited or less excited. It's not binary. But every spike is the same, and it's just transmitting basically one bit, but at different intervals. The interesting point about this is that we have lots, lots and lots of neurons. I think artificial neural networks still haven't reached the sheer number of neurons of the human brain, or maybe have just reached it, I'm not sure. So in the human brain, we have like 100 billion... No, okay. Yeah, yeah, right. We have like 100 billion neurons, and every neuron... So you know that there are neural networks with 100 billion and trillion weights, right? But the weight is not a neuron. The weight in the biological brain is on the connection between the neurons, right? So the weights are in the synapses, in these connections where a dendrite of one neuron attaches to the axon of another. And yes, there are weights there. So it really, in some way, it's like a linear combination. Not really, but like. So there are connections that get reinforced. There are connections that get inhibited. There can be negative weights. There are all sorts of things. So there are indeed weights at the synapses that are learned, that are trained in the human brain. And that's how we think. That's how we learn stuff. But the point is, how many weights are there in the human brain? How many parameters? Well, we have like 100 billion neurons, and each one on average has several thousand synapses, like 7,000 synapses on average. So if you multiply, you get something like, what's the quintillion or a bit less than a quintillion of synapses, of weights that are being trained in our brain. That's a huge amount. I think artificial neural networks have not yet reached that. But on the other hand, it's extremely slow, right? So I just told you that our brain is a computer that operates on the frequency of 10 to a couple hundred hertz, right? A couple hundred signals per second, not megahertz, not kilohertz, just hertz. And so the brain is very, very slow as a computer, if you were talking about clock speeds, but it's huge in terms of the number of connections. And what this actually means is the brain always performs highly parallel computations, but cannot perform a long sequential computation. It simply doesn't have time. So for example, we recognize a face. Recognizing a face is a difficult task in computer vision. It's a difficult task. But we recognize a face in like a couple hundred milliseconds. And that's like the full cycle of between the time when I show you the face and the time when you press a button to record that you have recognized the face. So it's the full cycle of feature extraction, decision-making, motor command to the finger, everything. And it all fits into like 200 or 300 milliseconds. So what this actually means is that this is an actual picture of how it goes through the brain. Maybe we will get back to this picture when we discuss CNNs, but maybe not. And what this actually means is that the brain cannot have like a loop for I from 1 to 1,000. It doesn't have time to do it. It only has time for like 10 or 15 sequential steps of computation. And then it has to get the answer out. Otherwise, you are already being eaten by a lamb, right? And so the computations are not sequential, but they are very, very highly parallel. So when we are recognizing a face, it's like half of our brain lights up. But half of our brain lights up, but it lights up in like 10 steps, sequentially. And then we have to give the answer. In a way, this is the property of the brain that we actually keep in artificial neural networks. So we will discuss how to make neural networks really, really deep. We will discuss networks with hundreds of layers. And I will tell you that you can go to thousands, it just doesn't make sense. And yeah, it doesn't make sense. In actuality, our current artificial neural networks, okay, maybe they have more than 10 or 20 layers, maybe they have 100, but not much more than that. So we don't know how to make use of tens of thousands of layers in the neural network. And let's say the proverbial GPT-5 is probably very, very wide, it's probably like a mixture of experts that have been trained to do different things, blah, blah, blah. But in terms of the number of layers of sequential computations, it's probably like a few dozen, maybe a couple of hundred, not more, I'm pretty sure. So this kind of wide but shallow thing we will keep, but the main part of the motivation is not, of course, in the architecture, we will see that the architecture cannot be the same, it's by definition kind of very different. But what we actually want to get from, what is the part of the motivation that we actually want to reproduce in computers is how versatile, how adaptive, how elastic our brain is. So we can learn on very few examples and we can learn some very, very complicated stuff on very small data samples. We can adapt to new data sources. There are experiments like this one where you can actually learn to see with your tongue or something. This is called neuroplasticity. And this was a fun experiment. You make a small plate of electrodes and it's the tongue just because the tongue is sensitive and you can actually distinguish between a lot of electrodes on the tongue. But it doesn't matter. You just put it somewhere on you and then you send to the electrodes a signal from a camera at your forehead. And then you just walk around and you feel a slight tingling from the electricity. And then you stop feeling it, of course, very soon because the brain adapts and stops noticing it. But in a few days of walking around with this camera, your brain starts to notice that there is an actual correlation between what you see and what this tingling looks like. And there have been experiments that after a couple of weeks of walking around with this stuff, you can actually close your eyes and see through this electrode plate. Maybe not read books, but at least walk around and not bump into walls differently. And for example, you probably have heard of neuroplasticity examples like when somebody has a stroke and part of the brain stops working, sometimes it's too much of a damage and the person never recovers, but sometimes they recover. Sometimes other parts of the brain take on the functions that were previously done by this now missing part and that's also something that our brain can do. So, in a way, this kind of experiments tell us that the brain, yes, it does have predetermined areas, predetermined by evolution. Like, yes, we have our visual cortex is back there in the occipital lobe of the brain, our frontal cortex is usually doing the reasoning and the decision-making, yes. But it's kind of incidental. So, yeah, sure, it evolves to be this way, but the neurons are still the same. And there is some kind of a single learning algorithm inside the human brain that can be applied to all of these sorts of different situations. There are no neurons in the brain that have evolved to distinguish cats from dogs. This is a learned thing, of course. And there are no neurons in the brain that are from birth originally evolved to already distinguish, to already understand the 3D structure of the world around us, like computer vision is supposed to do. No, that cannot be written in the genes. There is not enough information in the genes to write it down. This is all learned. This is all learned from scratch. And this is learned with very high efficiency in the early stages of our life. So we do want to have it in computers. That was the original motivation for neural networks. And as we will see, in artificial neural networks, we do keep this general idea which is known as connectionism. Connectionism is part philosophical, part mathematical idea that if you connect a lot of simple things together, the huge composition of very simple things becomes very complicated and can do very interesting stuff. It's as simple as it gets and it's true, right? There are lots of mathematical results about this, like how you can approximate anything with a polynomial, you can approximate anything with two layers of univariate functions. There are a huge number of results about it, and neural networks are kind of based on this idea. You take very simple things, you put them together, and you get a very complicated thing like a face recognition system. Another thing where artificial neural networks are really, really similar to the human brain is the structure of a single neuron. We will come back to it just right now and later, and we will see that. So, okay, let's come to it right now. No point in leaving it for the future. So what does a neuron look like, an artificial neuron, like this most basic building block of neural networks? Well, it has some inputs, x1, x2, xn. It looks just like the linear models that we discussed just now. In part, that's why I'm always discussing them. Then you multiply them by the weights of this neuron, and you get w times x. You get this linear combination of inputs with the weights. The weights will be trained during learning of the network. But then you also need to have a nonlinear function before you can get to the output. Why? Because if your neurons were doing just linear regression, if your neurons did not have a nonlinear function, which is called the activation function, then there would be no point to have a network, because composition of linear functions is linear again. And now if I have a huge network full of linear neurons, it's basically just one neuron applied to the whole, and there is no difference. So with linear functions, I will not get more complicated things. But as soon as I have any kind of nonlinearity, we will discuss just now what kind of nonlinearities there are, and there are very simple ones. As soon as I have any kind of nonlinearity, even something like real, which is just two linear functions strained together, it starts to work. And there is a big field of math that shows that any kind of nonlinearity is enough to approximate anything. It doesn't really matter in practice for us. In practice, what matters is that it works. So as soon as we have any sort of nonlinearity, compositions of these simple neurons begin to approximate whatever you want. Which still leaves open the question of how to approximate, how to find the weights, how to train. We'll discuss that a lot. But basically, as soon as we have a nonlinear neuron, we can. And interestingly enough, this kind of model for a single artificial neuron has been with us since 1943. Since before the Turing test, since before the Dartmouth seminar, before the words artificial intelligence had any scientific meaning. Already in 1943, Warren McCulloch and Walter Pitts wrote a paper which was called Logical Calculus of Nervous Activity. So it was actually, they were approaching it from the perspective of mathematical logic. But they wanted to have a mathematical model of the human brain. And in particular, a mathematical model of a single neuron. And it was basically already this. So even in 1943, we started off with this model of the neuron and we are still with it. So yes, there are parts of modern neural networks that cannot be directly explained by these neurons. So there are like attention mechanisms when we get to transformers. We will see some functions that have weights, but that are not quite like this. But mostly, most neural networks are still composed from neurons like this. And even transformers have a lot of neurons like this. So this is still the basic building block. It was first implemented in practice by Frank Rosenblatt in 1958. I think I have pictures. Yep. Very romantic time to be in computer science. That's what the computer looked like back in the days, 1950s. And so this is Frank Rosenblatt, like, learning, training a perceptron, right? But it indeed worked. So I think it was the first actual honest machine learning model implemented in practice. And it actually did some pretty amazing things eventually. So it learned to recognize letters. And, of course, it's not real computer vision. They were letters in a specific font, photographed from a specific point. And, of course, this was much simpler problem than real OCR, of course. But still, it was extremely amazing for the time. And when this perceptron appeared, well, I always show this New York Times quote. Maybe let's not dwell on it right now. But basically, at that point, everybody decided that, well, the hard part is done. So I recommend you read it. The hard part is done. And we know how to make computers learn. And now it's only a couple of years before they can walk, talk, see, write, reproduce themselves and be conscious of their existence. So as we know, it took a little bit more than that. This early optimism was not really warranted, but still it's the same principles, right? We still inherit a lot from this early neural network ideas. Okay, what do I want here? Yeah. And then, as I told you yesterday, the AI winter happened. So then people somehow got convinced that machine learning doesn't really work. And in particular, by the way, they got convinced that neural networks don't work. And there were some practical reasons which were true, but there was also a very strange theoretical reason for that, that somehow convinced a lot of people that neural networks are worthless. And the theoretical reason is this: whatever activation function you have, if you have—and this is an important point, so let me make it— whatever activation function you have, whatever is the H, still the inputs go to H through a linear combination, right? So if you think about it as a model doing classification, then you are still drawing a linear separating surface between the classes. So there is—so if you have H times X and you have some decision rule afterwards, like if it's more than 0, then class 1, if it's less than 0, then class 2, then the surface will be this, right? This is the decision surface on one side to have C1, on the other side to have C2, which is the same thing as saying, well, let me just see where H reaches 0 and now it's a linear surface, right? So the non-linearity doesn't give you non-linear separating surfaces. Non-linearity just gives you the ability to build networks, but by itself, it still leaves the classifier linear, of course. And for some reason, people look at this and say, well, okay, so it means that one perceptron cannot solve a lot of problems. There are many problems which do not have a linear separating surface, like the XOR function. If you have the orange class over here and you have the blue class over here and over here, then of course there is no straight line that separates them. Well, sure, these are linearly inseparable classes. But for some reason people thought that this was like an argument against perceptrons and against neural networks, which was kind of strange. I'm still not sure how the reasoning actually worked. But, of course, the correct answer is, sure, you cannot do XOR, you cannot do a linearly inseparable task with a single perceptron, but you can do it with a network of perceptrons, right? And the idea of a neural network, the idea of taking this kind of neurons and putting them together in layers and computing the final result of a composition of several such neurons, it's also very old, and it actually goes back to the same Alan Turing. He was a smart guy, and he already, in 1948, before the Turing test, he already had a paper, which I don't recommend to read, it's very hard to read today, but he already had a paper where he suggested actually deep neural networks, like real deep neural networks, compositions of layers of neurons. And the question was, how do we train it? The answer was pretty straightforward, I think we'll discuss it in detail tomorrow, along with all of the gradient descent variations that we have today. But the answer is, of course, well, you learn by gradient descent, and to do gradient descent, the only thing you need to be able to do is to take the gradients, take the derivatives, and how do you take the derivatives through the computational graph? Well, by backpropagation. I think you've heard about it. Probably you should already know it. Maybe we'll cut through it quickly tomorrow. So it's not a very deep idea. Backpropagation is just the chain rule for computing probabilities. And therefore, it's hard to say who discovered it because it was kind of discovered independently a lot of times. But by the 1970s, it was already kind of well known and understood that you can use backpropagation to go through the layers and to update the weights of a composition of simple functions. And already in the late 1970s, in the first half of the 1980s, you already had the idea of deep neural networks. And they already started to appear. And by the second half of the 1980s, you already had convolutional networks. You already had recurrent networks. You didn't have transformers yet that had to wait. But you already had a lot of architectural ideas that are actually still relevant, and that if you could just scale them up, they would work quite amazingly well, actually. So if you take a network, say a convolutional network, a CNN, from the early 1990s to late 1980s, and you just mechanically scale it up, and you train it on modern hardware and modern datasets, it's going to work pretty well. So of course it will be worse than the networks we have today, of course. But if people had this kind of results back in 1990, they would never be discouraged from neural networks. That would definitely be state-of-the-art back in the time. But unfortunately, neural networks require a certain scale to work, so to speak, right? So if you have a very small neural network and a small dataset, then probably the result will be worse than if you actually just think about the problem and do some more specialized model for this problem. So by the early 1990s, since people did not have the ability to scale up, they did not have the compute, they did not have the data, basically the consensus in the research community was like this: neural networks are the second best way of doing just about anything. So the place of neural networks was that they are very universal, you can do anything with a neural network, indeed, but it will be worse than if you just think about the specific problem you have and create a model for this specific problem. So in the 1990s and early 2000s, neural networks were kind of forgotten again. It was the heyday of probabilistic models, of graphical probabilistic models, etc., etc. Very interesting, still relevant, very important, but out of scope for us. And there were just a few groups who pushed and pushed on neural networks. There was Jan LeCun who was doing image processing with CNNs. There were Jeffrey Hinton's group and Joshua Bench's group. And they continued working, they continued believing in the neural networks. And finally, they were proved to be right. Okay, so the deep learning revolution happened in the middle of the 2000s, 2006, 2007. And I won't discuss in detail what exactly was their innovation because it's irrelevant by now. It's absolute. But the technical innovation, which is still, of course, relevant, was that they moved from CPUs to GPUs. So, again, it's not much of an idea to notice that the stuff we do in neural networks is easy to parallelize. Of course, it's easy to parallelize. It's a huge number of neurons and not very deep computation, just like in the brain. But only in our century, only in the early 2000s, there was actually hardware widely available on the market, gaming GPUs, that would actually implement this parallel process. So before that, CPUs were still the best we had, right? And as soon as GPUs became good enough, people, specifically the guys at Hinton's group, moved computations to GPUs. That gave a boost of about another 10x, 20x inefficiency. And that was enough. That was enough to put neural networks from not working to working. And starting from the late 2000s, neural networks have been kind of revolutionizing one field of machine learning after another. Actually, the first field was speech recognition, speech processing. Deep neural networks served as some very good feature extractors in about 2010. So basically, it was these original deep neural networks by Hinton and Benji that made Siri possible. Siri appeared in 2011, I think, the first version. And it was, of course, would be impossible on classical speech recognition. I mean, it wouldn't work well enough to be useful. And then, so we will not talk about speech recognition in this class, but we will talk definitely about image processing and image recognition and computer vision. So there the revolution happened around 2011, 2012 with AlexNet. We will discuss AlexNet in detail when we come to it. And then everywhere. Then with recurrent networks, deep learning got into natural language processing. So by 2014, 15, people were doing machine translation with neural networks and stuff like that with neural networks. And then in 2017, everything changed again. In 2017, we had the transformer and that transformed literally the whole industry again. We are still living in the age of transformers, so to speak. So I think I don't have time to go to BecProv right now. This was a quick historical overview and we'll do the optimization part tomorrow. Any questions? I'm sorry. I think I skipped one of the parts you were explaining about logistic regression and you put some neural network, you put logistic regression at the end. I think I just didn't capture what was going on there. Yeah, sure, no problem. So suppose that I'm doing a neural network that is supposed to do classification. So at the output, I want to have a loss function like this. And I want to have like a vector of probabilities for classes. Where do I get a vector of probabilities? Well, if I just do some neural layers, some elementary functions, some big compositions, I will not get a vector of neat numbers from zero to one that sum up to one, right? What I will get is a vector of scores that then will need to be converted to probabilities by the softmax function. That's part one. But also, I mean, for some networks, this will be the actual output and this may not happen, but usually, of course, it still happens. So usually after the main part of the neural network, what it does is it extracts some kind of features from the input. And these features are a vector or a higher dimensional tensor, it doesn't matter at this point, but it's a set of numbers, let's say, of size d, right? Okay, I got it. And we want to convert it to a set of numbers of size k. That's the only point that I was making here. So how can you do it well, for example, with just a linear transformation? So very often when neural networks do classification, very often the last layer is actually just logistic regression. This is literally straightforwardly logistic regression. But not on the input, but on the features extracted by all the rest of the neural network. And that's the very important difference. If that would be not logistic regression, but linear regression, everything would be the same except for softmax part. And probably, I mean, in linear regression it's kind of uncommon to have many outputs. So probably k would be equal to 1. But not necessarily, you could have several outputs, of course. Yes, you explained that before. And I also want to say thank you for the lecture. It was very interesting. It was very unobvious to see the prior Bayesian theory, imagining that regularization is a bias. Because I read a lot of information, I was preparing for an interview, and I literally couldn't find it. I haven't seen it before. Maybe I haven't read it properly. If you looked for it, you should be able to find it. Of course, it's like in the foundations of all the machine learning, but I'm really happy that you find it interesting. I'm always a little bit worried about this introductory part because some people just want to get to programming in PyTorch. But I think that foundations are important, and I'm really happy that you feel that way too. Thank you. Thank you. All right. Thanks a lot, guys. Sure. In the first part of the bus, we discussed the problem of overfitting, right? Mm-hmm. So, like, in general, you can... Okay, previously in statistics, you would use, like, measures like R-squared-adjusted, or, like, criteria, I don't remember, like, Kaike information criteria and some other measures that punish adding extra variables to the model. Which is basically what rich regression and lasso do, I guess. Not quite. So, yeah, there is a difference here that is a little bit... that is a little bit made unclear by my example. And I apologize for that, but it's still a very instructive example, so I still give it. But yes, that is a great question, and there is an important difference. So when we talk of regularization, we kind of have already fixed the model. So in the case of linear regression, I can have an L2 regularizer, I can have an L1 regularizer, I can have any kind of prior over here, but the likelihood is already fixed. And what it means that the likelihood is fixed in particular, it means that the size of this vector is also fixed. So when I change regularizers, I don't change the model structure, I don't change the number of parameters. It might look like that in my example, because as I went from between degrees of the polynomials, I was changing the number of parameters. You're right, it was a little bit confusing in this regard. But regularization usually does not do that. Regularization deals with the values of these parameters. And the stuff that you mentioned, and these are great keywords that I also talk about in classes when I have time, but not in this class where we go to deep learning, but things like Akaiki information criterion, the Bayesian information criterion, and stuff like that, they pertain to what is called model selection. And model selection basically means I can model my data set in several different ways. I can have linear regression, I have quadratic regression, cubic regression, local Gaussian regression, whatever. And then I need to choose between them. How do I choose between them? Well, what is this choice? What am I trying to estimate? It's deceptively simple. I want to estimate what is the likelihood, what is the probability of having model number k for my data set. And where do I get this probability from? Well, of course I get it from the bias rule. So of course I get it from something like this, p of mk times p of d given mk. And notice that here m is not a specific set of weights. Here m is the whole model. So like one m could be like linear regression and another m could be like quadratic regression. So it's the whole model, not specific weights. But still, the bias rule is the same. And it still tells you, well, okay, if I don't have any reasons to prefer one model to another, then let's assume this is uniform. And I just compare p of d given mk. Where is that p of d given mk in our formulas? Well, let's go back to our bias rule, p of theta. Put more space here because I need this. p of theta, p of d given theta, sorry, p of d given theta divided by p of d and here p of theta given d. This formula, as I wrote it, we didn't have, you know, the context and the chance to go this one meta level up. But you can go one meta level up. The formula, as I wrote it, was about one model. Like we are talking about linear regression and we are dealing with the parameters that obey this base rule and do inference for the parameters. So like everything happens in a model. Sorry, not the bar, right? You can add the model here, doesn't change the formula, it still works. So what do you compare the models by? How do you choose between quadratic and cubic features or between different versions of the model, et cetera? Well, by this guy over here. The denominator, so this is exactly this quantity. The denominator in the base rule, the normalizing constant. And everything that these information criteria do, they are basically approximations to compute this. And then there is a lot of methods, it's a very beautiful and interesting approximation. Lots to say about it, but basically it's an approximation to compute this. So model selection is about trying to estimate this normalizing constant and choose the model with the largest normalizing constant. But inside the model, then, we will have a whole distribution of parameters, blah, blah, blah, and so on. So there are two levels. There is the level of selecting the model, and then inside the model there is the level of actually learning the parameters. Did I answer the question? Thank you. Okay. Thanks, guys. And see you tomorrow, finally, for some actual neural networks. Bye-bye.
