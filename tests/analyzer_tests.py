import os
import sys
from .context import analyzer
from analyzer import analyzer


def test_remove_stop_words():
    a = analyzer.Analyzer()
    input_words = ['a', 'fantastic', 'test']
    stopwords = ['a', 'test']
    result = a.remove_stop_words(input_words, stopwords)

    assert result == ['fantastic']

def test_remove_no_stop_words():
    a = analyzer.Analyzer()
    input_words = ['a', 'fantastic', 'test']
    stopwords = ['foo']
    result = a.remove_stop_words(input_words, stopwords)

    assert result == input_words

def test_stem():
    a = analyzer.Analyzer()
    words = ['jumping', 'jumps', 'jumped', 'jump']
    result = a.stem(words)

    assert result == ['jump', 'jump', 'jump', 'jump']

def test_compute_term_frequency():
    a = analyzer.Analyzer()
    words = ['a', 'man', 'a', 'plan', 'a', 'canal', 'Panama']
    result = a.compute_term_frequency(words)

    assert result['a'] == 3
    assert result['man'] == 1
    assert result['plan'] == 1
    assert result['canal'] == 1
    assert result['Panama'] == 1

def test_sort_top_terms():
    a = analyzer.Analyzer()
    words = {'came': 1, 'saw': 1, 'conquered': 1, 'I': 3}
    result1 = a.sort_top_terms(words, 1)
    # result2 = a.sort_top_terms(words, 2)

    assert result1 == [('I', 3)]
    # assert result2 == [('I', 3), ('came', 1)]
