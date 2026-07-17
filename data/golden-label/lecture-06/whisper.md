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