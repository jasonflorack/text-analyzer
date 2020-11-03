import os
import re
import sys
from sys import version_info

from . import porter_stemmer


class Analyzer:
    """Reads text from a given input_file, removes stop words from another file (stopwords.txt),
    removes all non-alphabetical text, stems words into their root form, computes the frequency
    of each term, and prints out the 20 most commonly occurring terms (not including stop words)
    in descending order of frequency.
    """

    def __init__(self):
        self.prompt = None
        self.establish_input_method()

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def greeting():
        print ('******************************************************************************************************')
        print ('                                      Text File Analyzer')
        print ('******************************************************************************************************')
        print ('This app collects all of the words in a text file (which you provide), removes any stop words found')
        print ('in another file (which you also provide), removes all non-alphabetical text, stems all remaining')
        print ('words into their root form, computes the frequency of each term, and prints out the 20 most commonly')
        print ('occurring terms in descending order of frequency.')
        print('')

    def establish_input_method(self):
        if version_info.major == 3:  # Python3 is being used, so use 'input' method
            self.prompt = input
        elif version_info.major == 2:  # Python2 is being used, so use 'raw_input' method
            try:
                self.prompt = raw_input
            except NameError:
                pass

    def get_input_words(self):
        """Prompt user for input file location, read the file, then return a list of the words
        it contains
        """
        filename = self.prompt("Please enter the path of the text file to be analyzed (e.g., input/Text1.txt): ")
        if os.path.isfile(filename):
            input_text = open(filename, 'r').read()
            return self.remove_punctuation(input_text)
        else:
            print("This file does not exist.  Please try again.")
            return []

    @staticmethod
    def remove_punctuation(text):
        """Remove punctuation from text; return list of each word in text"""
        return re.sub(r'[^\w\s]', '', text).split()

    def get_stopwords(self):
        """Prompt user for stopwords file location, read the file, then return a list of words
        it contains
        """
        stopwords_file = self.prompt("Please enter the path of the stopwords file (e.g., input/stopwords.txt): ")
        if os.path.isfile(stopwords_file):
            # Create list of stopwords from file
            return open(stopwords_file, 'r').read().split()
        else:
            print("This file does not exist.  Please try again.")
            return []

    @staticmethod
    def remove_stop_words(input_words, stopwords):
        """Return a list of 'filtered_words' from the provided list of 'input_words' by
        removing any words from the provided list of 'stopwords'
        """
        filtered_words = []
        for word in input_words:
            if not word.lower() in stopwords:
                filtered_words.append(word)
        return filtered_words

    @staticmethod
    def stem(words):
        """Return a list of 'stemmed_words' from the provided list of 'words' by
        using a Porter Stemming Algorithm to stem all words to their
        morphological root (e.g., jumping, jumps, jumped -> jump)
        """
        p = porter_stemmer.PorterStemmer()
        stemmed_words = []
        for word in words:
            stemmed_words.append(p.stem(word, 0, len(word)-1))
        return stemmed_words

    @staticmethod
    def compute_term_frequency(words):
        """Return a 'frequency' dict from the provided list of 'words' which contains
        each word (key) and the number of times it appears (value)
        """
        frequency = dict()
        for word in words:
            if word not in frequency.keys():
                frequency[word] = 1
            else:
                frequency[word] += 1
        return frequency

    @staticmethod
    def sort_top_terms(frequency, count):
        """Return a 'top_common_terms' list of tuples from the provided 'frequency' dict
        which contains the top 'count' number of key/value pairs, in descending order
        """
        top_common_terms = []
        all_common_terms = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        for i in range (count):
            top_common_terms.append(all_common_terms[i])
        return top_common_terms

    @staticmethod
    def print_top_terms(terms):
        """Print the provided 'terms' list of tuples"""
        print('')
        print('After filtering out stopwords, the provided text contains these 20 most commonly occurring root terms:')
        print('------------------------------------------------------------------------------------------------------')
        for term in terms:
            print(term[0] + ' : ' + str(term[1]) + ' occurrences')
        print('')
