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
        self.__add_sentense_bocchan()
        self.assertTrue(len(self.markov.starts) > 0)
        self.assertTrue(len(self.markov.dic) > 0)

    def test_generate(self):
        self.__add_sentense_bocchan()
        input_texts = [
            '初めまして、坊ちゃん',
            'あら、ご病気ですか',
            'あらあら、大変ですね',
            'いたずらして病気になっちゃったんですか？',
            'そんな威張らなくてもいいでしょう',
            'はあ、そんなもんですか',
            '遅刻しちゃだめですね',
            'よく覚えてないんですか？',
            'ターナー？',
            'どなたですか？'
        ]
        
        for input_text in input_texts:
            with self.subTest():
                tokens = Morph.analyze(input_text)
                keyword = 'N/A'
                for token in tokens:
                    if Morph.is_keyword(token):
                        keyword = token.surface
                generated = self.markov.generate(keyword)
                print('you > ' + input_text)
                print('generated > ' + generated)
                print('************')
                self.assertTrue(len(generated) > 0)

    # private method
    def __add_sentense_bocchan(self):
        sample_file = '../KOISURU_PROGRAM/sample/google/bocchan.txt'
        content = ''
        
        original_content = codecs.open(sample_file, 'r', 'shift_jis')
        for row in original_content:
            content += row.rstrip()
        original_content.close()
        texts = re.split(r'[。?？!！ 　]+', content)

        for text in texts:
            if text == '':
                continue
            tokens = Morph.analyze(text)
            self.markov.add_sentence(tokens)
            print('.', end='')
        print('')


if __name__ == "__main__":
    unittest.main()
