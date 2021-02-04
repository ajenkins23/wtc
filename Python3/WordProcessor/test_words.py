import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import word_processor

class TestWord(unittest.TestCase):
    def test_ConvertToList(self):
        output = word_processor.convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?')
        correct = ['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you']
        self.assertEqual(output,correct)

    def test_WordsLongerThan(self):
        output = word_processor.words_longer_than(10, 'These are indeed interesting, an obvious understatement, times. What say you?')
        correct = ['interesting','understatement']
        self.assertEqual(output,correct)
    
    def test_WordLengthMap(self):
        output = word_processor.words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?')
        correct = {2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1}
        self.assertEqual(output,correct)
    
    def test_LettersCountMap(self):
        output = word_processor.letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?')
        correct = {'a':5, 'b': 1, 'c':0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}
        self.assertEqual(output,correct)

    def test_MostUsedCharacter(self):
        output = word_processor.most_used_character('These are indeed interesting, an obvious understatement, times. What say you?')
        correct = 'e'
        self.assertEqual(output,correct)