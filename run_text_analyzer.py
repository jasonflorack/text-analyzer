from analyzer import analyzer

a = analyzer.Analyzer()
filtered_words = a.remove_stop_words(a.input_words, a.stopwords)
root_words = a.stem(filtered_words)
frequency = a.compute_term_frequency(root_words)
common_terms = a.sort_top_terms(frequency, 20)
a.print_top_terms(common_terms)
