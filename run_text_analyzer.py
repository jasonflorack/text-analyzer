from analyzer import analyzer

a = analyzer.Analyzer()
a.clear_screen()
a.greeting()

input_words = []
stopwords = []
while input_words == []:
    input_words = a.get_input_words()
while stopwords == []:
    stopwords = a.get_stopwords()

filtered_words = a.remove_stop_words(input_words, stopwords)
root_words = a.stem(filtered_words)
frequency = a.compute_term_frequency(root_words)
common_terms = a.sort_top_terms(frequency, 20)
a.print_top_terms(common_terms)
