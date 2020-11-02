import os
import re
import sys
from porter_stemmer import PorterStemmer


class Analyzer:

    def __init__(self):
        self.input_words = []
        self.filtered_words = []
        self.root_words = []
        self.frequency = dict()
        self.common_terms = []

        self.stopwords_file = "stopwords.txt"
        if os.path.exists(self.stopwords_file):
            # Create list of stopwords from file
            self.stopwords = open(self.stopwords_file, 'r').read().split()
        else:
            raise Exception('Stopwords file does not exist!')

        self.__get_input_file()

    def __get_input_file(self):
        try:
            self.input_file = str(sys.argv[1])
        except IndexError:
            raise Exception('No input file given!')

        if os.path.exists(self.input_file):
            self.input_file = open(self.input_file, 'r').read()
            # Remove punctuation from input file; create list of each word in file
            self.input_words = re.sub(r'[^\w\s]', '', self.input_file).split()
        else:
            raise Exception('Input file does not exist!')

    def remove_stop_words(self):
        for word in self.input_words:
            if not word.lower() in self.stopwords:
                self.filtered_words.append(word)

    def compute_frequency(self):
        for word in self.root_words:
            if word not in self.frequency.keys():
                self.frequency[word] = 1
            else:
                self.frequency[word] += 1

    def display_common_terms(self):
        self.common_terms = sorted(self.frequency.items(), key=lambda x: x[1], reverse=True)
        for i in range (20):
            print (self.common_terms[i])

    def stem_words(self, words):
        p = PorterStemmer()
        stemmed_words = []
        for word in words:
            stemmed_words.append(p.stem(word, 0, len(word)-1))
        return stemmed_words

a = Analyzer()
a.remove_stop_words()
a.root_words = a.stem_words(a.filtered_words)
a.compute_frequency()
a.display_common_terms()
