# Markov Chain Generator
Create almost convincing sentences and paragraphs using Markov chains

## Overview
This project uses [Markov chains](https://en.wikipedia.org/wiki/Markov_chain) to generate almost convincing sentences. New words are selected based on two preceding words, so the grammatical structures are kept well for the most part. The start and end of sentences are preserved as well, so in general, sentences begin and end as they normally should. With vocabs and grammatical style of the authors and topics in the corpus, you should end up with strange sentences with the overall feeling and style still intact. Give it a try!

## Instructions
### Get started
1. Put a corpus file in the same directory, with sentences separated using periods.
2. Import the class and create a `MarkovChain` object with the following commands, substituting the corpus file name for `file_name`:
```
from MarkovChain import MarkovChain
mk = MarkovChain(file_name)
```
### Methods
```
mk.make_sentence()
mk.make_paragraph(number_of_sentences)
```
`make_sentence()` provides a random sentence generated with Markov Chain Generator. `mk.make_paragraph(number_of_sentences)` provides you with a number of random sentences, specified using `number_of_sentences`.

* Note: This was written for Python 3

## Examples
Feeding the generator with The Smiths' lyrics ([link here](http://www.cemetrygates.com/vault/smiths/lyricshandbook.txt)) plus some clean-up, here are some lines Morrissey definitely *did not* write:
> I'm truely sorry - but it sounds like a dulling wine. And people who don't care if I were you I wouldn't say no. I don't want to cry. 'Cause I will too. Please stay with your biology. Come out and find the one that you make feel so ashamed. Why are you on your sacred mind. Deep in the middle of the world. In my room and I think you know where you came from, you know it's over-still I cling.

An assortment of basketball articles from Grantland ended up with the following:
> How many teams are just so quick in the league; it’s time to teach winning by losing. Mozgov is nimble for his new team. That is a question I can’t believe I’m saying this, but I didn’t know Saunders well, but we talked now and then. Orlando has shown spunk of late with Glen Davis back, but it’s a tool to confirm what they already think and know. The immediacy of the floor from a Pacers-Raptors game this season: Two things happen here, and both are already out first-round picks to draft him, and Mozgov share the floor, than Real DeRozan as Chandler rolls to the back end of their advantages.
