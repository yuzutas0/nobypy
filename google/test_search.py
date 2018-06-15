# -*- coding: utf-8 -*-

import unittest
from search import Search
from morph import Morph


class TestSearch(unittest.TestCase):
    """test class of markov.py"""
    
    def test_get_sentence(self):
        input_texts = [
            'こんにちは',
            'ジブリが好きです',
            'ディズニーが好きです',
            'ピクサーが好きです'
        ]
        
        for input_text in input_texts:
            with self.subTest():
                tokens = Morph.analyze(input_text)
                keyword = ''
                for token in tokens:
                    if Morph.is_keyword(token):
                        keyword += token.surface + ' '
                sentence = Search.get_sentence(keyword)
                print('you > ' + input_text)
                print('keyword > ' + keyword)
                print('sentence > ' + sentence)
                print('************')
                self.assertTrue(len(sentence) > 0)


if __name__ == "__main__":
    unittest.main()
