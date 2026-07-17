# Slides (extracted) — slides.pdf

## Slide 1

CONVOLUTIONAL NEURAL NETWORKS
Sergey Nikolenko
Harbour Space University
June 12, 2026
Random facts:
• on June 12, 1550, King Gustav I of Sweden founded Helsinki as a rival trading town to Reval
(now Tallinn) across the gulf; it stayed a small fishing village for centuries and only became
a real capital after Russia took Finland in 1809
• on June 12, 1817, Karl von Drais first rode his Laufmaschine, the ``dandy horse'' ancestor of
the bicycle; he had been spurred on by a mass die-off of horses after the 1815 eruption of
Mount Tambora caused the "Year Without a Summer"
• on June 12, 1898, General Emilio Aguinaldo proclaimed Philippine independence from Spain;
the Philippines would not actually become independent until 1946, after Spanish, then
American, then Japanese, then again American rule
• on June 12, 1939, the Baseball Hall of Fame opened in Cooperstown, New York, on the
strength of a charming myth that Abner Doubleday had invented baseball there in 1839 (he
had not)
• on June 12, 1979, Bryan Allen pedalled the Gossamer Albatross across the English Channel in
2 hours 49 minutes, the first human-powered flight across it, winning the second Kremer
prize
1

## Slide 2

CONVOLUTIONAL NEURAL NETWORKS

## Slide 3

VISUAL CORTEX
• Convolutional neural networks – an important part of the deep
learning revolution.
• CNNs are partly motivated by the visual cortex.
• Hubel and Wiesel: the famous studies of the visual cortex.
3

## Slide 4

VISUAL CORTEX
• Hubel and Wiesel showed that first-level neurons activate for
simple shapes, second-level neurons activate for combinations
of these simple shapes, third-level... nope, they wisely didn’t go
there.
3

## Slide 5

VISUAL CORTEX
• Information from the retina goes to the lateral geniculate
nucleus (LGN), then to visual cortex.
• And it’s neatly organized into layers, from V1 to V4 and then
either to V5 or to V6.
3

## Slide 6

VISUAL CORTEX
• Well, kinda. The brain is complicated.
3

## Slide 7

VISUAL CORTEX
• Very complicated.
3

## Slide 8

VISUAL CORTEX
• But some kind of layers are indeed there:
• V1 – local features;
• V2 – more local features, binocular vision;
• V3 – color, texture, first results of segmentation;
• V4 – geometric shapes, silhouettes; the most important layer for
attention;
• V5 – recognizes motion of objects segmented in V4;
• V6 – generalizes data from the whole image; wide-field
stimulation; processes changes due to our own movement;
• V7 (controversial) – recognition of complex objects, e.g., human
faces.
• What pathway: V2 to V4, recognition of shapes and objects.
• Where pathway: V2 to V5 and V6, motion recognition, control
over eyes and hands.
3

## Slide 9

CONVOLUTIONAL NEURAL NETWORKS: IDEA
• These ideas were reflected in ANNs in the form of convolutional
networks.
• Convolutions appeared in Neocognitron (Fukushima, 1979; 1980).
• In modern form – in LeCunn’s group in late 1980s.
• Main idea: we would like to apply the same operation to every
part of the image.
4

## Slide 10

CONVOLUTIONAL NEURAL NETWORKS: IDEA
• Break the picture into windows:
4

## Slide 11

CONVOLUTIONAL NEURAL NETWORKS: IDEA
• Break the picture into windows:
4

## Slide 12

CONVOLUTIONAL NEURAL NETWORKS: IDEA
• Apply a small neural network to every window:
4

## Slide 13

CONVOLUTIONAL NEURAL NETWORKS: IDEA
• Then compress the image by max-pooling over small windows:
4

## Slide 14

CONVOLUTIONAL NEURAL NETWORKS: IDEA
• And then predict with a fully connected network:
• Adding new layers improves generalization:
4

## Slide 15

CONVOLUTIONAL NEURAL NETWORKS: IDEA
• Moreover, we can see where exactly are the parts of the picture
that cause activation of individual neurons:
4

## Slide 16

CNNS FORMALLY
• Formally speaking, we have a single small matrix and apply it to
every window:
• If x𝑙is the feature map in layer 𝑙, then two-dimensional
convolution of size 2𝑑+ 1 and weight matrix 𝑊of size
(2𝑑+ 1) × (2𝑑+ 1) is
𝑦𝑙
𝑖,𝑗=
∑
−𝑑<=𝑎,𝑏<=𝑑
𝑊𝑎,𝑏𝑥𝑙
𝑖+𝑎,𝑗+𝑏.
5

## Slide 17

CNNS FORMALLY
• If x𝑙is the feature map in layer 𝑙, then two-dimensional
convolution of size 2𝑑+ 1 and weight matrix 𝑊of size
(2𝑑+ 1) × (2𝑑+ 1) is
𝑦𝑙
𝑖,𝑗=
∑
−𝑑<=𝑎,𝑏<=𝑑
𝑊𝑎,𝑏𝑥𝑙
𝑖+𝑎,𝑗+𝑏.
• It is usually followed by a nonlinearity:
𝑧𝑙
𝑖,𝑗= ℎ(𝑦𝑙
𝑖,𝑗).
• Almost always ReLU in modern networks.
5

## Slide 18

CNNS FORMALLY
• And then max-pooling (sometimes average-pooling, but usually
max):
𝑥𝑙+1
𝑖,𝑗=
max
−𝑑<=𝑎,𝑏<=𝑑𝑧𝑙
𝑖+𝑎,𝑗+𝑏.
5

## Slide 19

CNNS FORMALLY
• And this is the overall scheme of a single convolutional layer.
5

## Slide 20

CNNS FORMALLY
• Classical LeNet architecture:
• Modern CNNs can get very deep due to a number of
architectural tricks and advances.
5

## Slide 21

THANK YOU!
Thank you for your attention!
6
