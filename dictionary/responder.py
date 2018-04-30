# -*- coding: utf-8 -*-

import random
import codecs


class Responder:
    def __init__(self, name):
        self.name = name
    
    def response(self, input_text):
        return ''


class WhatResponder(Responder):
    def response(self, input_text):
            return f"{input_text}ってなに？"


class RandomResponder(Responder):
    def __init__(self, name):
        super().__init__(name)
        self.responses = []
        path = '../KOISURU_PROGRAM/sample/dictionary/dics/random.txt'
        content = codecs.open(path, "r", "shift_jis")
        for row in content:
            if row.rstrip() == '':
                continue
            self.responses.append(row.rstrip())
        content.close()
    
    def response(self, input_text):
        return random.choice(self.responses)
