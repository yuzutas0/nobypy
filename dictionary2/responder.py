# -*- coding: utf-8 -*-

import random
import re
from dictionary import Dictionary


dictionary = Dictionary()


class Responder:
    def __init__(self, name):
        self.name = name
    
    def response(self, input_text):
        return ''


class WhatResponder(Responder):
    def response(self, input_text):
            return f"{input_text}ってなに？"


class RandomResponder(Responder):
    def response(self, input_text):
        return random.choice(dictionary.random)


class PatternResponder(Responder):
    def response(self, input_text):
        for k, v in dictionary.patterns.items():
            m = re.search(k, input_text)
            if m:
                return random.choice(v.split('|')).replace('%match%', m.group(0))
        return random.choice(dictionary.random)
