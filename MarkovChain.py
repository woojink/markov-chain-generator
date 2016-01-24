import random

class MarkovChain(object):
    
    """
    Markov chain-based sentence/paragraph generator.
    
    Takes a text file with sentences separated by periods to form a corpus.
    It randomly picks out first words of the sentences from the corpus to 
    start the sentences according to the frequency of occurrence. The first 
    words are tied to the indices where they occurred, so the second words 
    are also selected according to their probability of occurrence.
    
    A dictionary of third words based on the preceding two words is used to
    determine the next word in the sentence. If any of the words ends with
    a period, then the sentence is terminated. Paragraphs are made using 
    a specified numbner of these sentences.
    
    Attributes:
        file_name (str): Name of the txt file with the corpus.
        dictionary (list of str): List of all the words in the corpus.
        start_list (list of int): Indices of all the words that start sentences.
        end_list (list of int): Indices of all the words that end sentences.
        pair_dict (dict of lists of int): Dictionary with 2-tuple key that stores possible third words.
    """
    
    def __init__(self, file_name):
        """
        Args:
            file_name (str): Name of the txt file with the corpus.
        """
        self.file_name = file_name
        self.dictionary = self.read_words()
        (self.start_list, self.end_list) = self.find_start_end()
        self.pair_dict = self.make_pair_dict()
        
    def read_words(self):
        """
        Separates words in the text file with space.
        """
        file = open(self.file_name)
        dictionary = file.read().split()
        
        return dictionary

    def find_start_end(self):
        """
        Finds the indices of the beginning and end of sentences.
        """
        end_list = []
        start_list = []
        for i in range(0,len(self.dictionary)):
            if self.dictionary[i].endswith("."):
                end_list.append(i)
                
                # If not at the end of the corpus, add the next word as a start word.
                if i+1 != len(self.dictionary):
                    start_list.append(i+1)
                    
        return start_list, end_list
    
    def make_pair_dict(self):
        """
        Creates a dictionary of list of 'next words' based on two previous words.
        """
        pair_dict = {}
        for i in range(0, len(self.dictionary)-2):
            pair = (self.dictionary[i], self.dictionary[i+1])
            if (i not in self.end_list) and (i+1 not in self.end_list):
                if pair not in pair_dict:
                    pair_dict[pair] = []
                pair_dict[pair].append(i+2)
                
        return pair_dict
    
    def find_next_word(self, pair):
        """
        Picks a random next word from the possible choices given the previous two words.
        
        See 'make_pair_dict()'
        """
        next_word_index = random.choice(self.pair_dict[pair])
        
        return self.dictionary[next_word_index]
        
    def make_sentence(self):
        """
        Provides a sentence made with next words until a period is encountered.
        """
        start_index = random.choice(self.start_list)
        pair = (self.dictionary[start_index], self.dictionary[start_index + 1])
        
        # Check if either word of the pair ends the sentence before selecting the third word.
        if pair[0].endswith("."):
            sentence = pair[0]
            return sentence
        else:
            sentence = pair[0] + " " + pair[1]
            if not pair[1].endswith("."):
                while True:                
                    next_word = self.find_next_word(pair)
                    sentence = sentence + " " + next_word

                    if next_word.endswith("."):
                        break
                    else:
                        pair = (pair[1], next_word)
        sentence = sentence[0].upper() + sentence[1:]
        
        return sentence
    
    def make_paragraph(self, number_of_sentences):
        """
        Provides a paragraph with a specified number of sentences.
        
        Args:
            number_of_sentences (int): Number of sentences desired
        """
        paragraph = ""
        for i in range(0,number_of_sentences):
            sentence = self.make_sentence()
            if i != 0:
                paragraph += " "
            paragraph += sentence
            
        return paragraph