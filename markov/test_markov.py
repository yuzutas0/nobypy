# -*- coding: utf-8 -*-

import unittest
import codecs
import re
from markov import Markov
from morph import Morph


class TestMarkov(unittest.TestCase):
    """test class of markov.py"""
    
    def setUp(self):
        print('*** setup ***')
        self.markov = Markov()

    def test_add_sentense(self):
        sample_file = '../KOISURU_PROGRAM/sample/markov/bocchan.txt'
        content = ''
        
        original_content = codecs.open(sample_file, 'r', 'shift_jis')
        for row in original_content:
            content += row.rstrip()
        original_content.close()
        texts = re.split(r'[。?？!！ 　]+', content)

        for text in texts:
            if text == '':
                continue
            tokens = Morph.analyze(input_text)
            self.markov.add_sentence(tokens)
            print('.')

        self.assertTrue(len(self.markov.starts) > 0)
        self.assertTrue(len(self.markov.dic) > 0)

if __name__ == "__main__":
    unittest.main()
