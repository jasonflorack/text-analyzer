import os
import re
import sys

class Analyzer:

    def __init__(self):
        self.input_words = []
        self.filtered_words = []
        self.root_words = []

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
    
    # def stem_words(self):
    #     pass

a = Analyzer()
a.remove_stop_words()

print(a.filtered_words)
