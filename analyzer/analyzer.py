import os
import re
import sys

from . import porter_stemmer


class Analyzer:
    """Reads text from a given input_file, removes stop words from another file (stopwords.txt),
    removes all non-alphabetical text, stems words into their root form, computes the frequency
    of each term, and prints out the 20 most commonly occurring terms (not including stop words)
    in descending order of frequency.
    """

    def __init__(self):
        self.input_file = None
        self.input_words = []
        self.stopwords = []
        self.__get_input_file()
        self.__remove_punctuation_from_input_file()
        self.__get_stopwords_file()

    def __get_input_file(self):
        """Read and store data from the input file (provided in command-line arguments)"""
        try:
            input_file = str(sys.argv[1])
        except IndexError:
            raise Exception('No input file given!')

        if os.path.exists(input_file):
            self.input_file = open(input_file, 'r').read()
        else:
            raise Exception('Input file does not exist!')

    def __remove_punctuation_from_input_file(self):
        """Remove punctuation from input file; create list of each word in file"""
        self.input_words = re.sub(r'[^\w\s]', '', self.input_file).split()

    def __get_stopwords_file(self):
        """Read and store data from the stopwords file"""
        stopwords_file = "input/stopwords.txt"

        if os.path.exists(stopwords_file):
            # Create list of stopwords from file
            self.stopwords = open(stopwords_file, 'r').read().split()
        else:
            raise Exception('Stopwords file does not exist!')

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
