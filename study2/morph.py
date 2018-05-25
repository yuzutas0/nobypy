# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer


class Morph:
    t = Tokenizer()

    @classmethod
    def analyze(cls, input_text):
        return cls.t.tokenize(input_text)

    @staticmethod
    def is_keyword(token):
        black_list = ['？', '?']
        if token.surface in black_list:
            return False
        return token.part_of_speech.split(',')[1] in ['一般', '固有名詞', 'サ変接続', '形容動詞語幹']
