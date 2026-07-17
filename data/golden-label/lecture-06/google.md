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