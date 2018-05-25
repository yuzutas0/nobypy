# -*- coding: utf-8 -*-

import random
import re
from dictionary import Dictionary


class Responder:
    dictionary = Dictionary()

    def __init__(self, name):
        self.name = name
    
    def response(self, input_text, mood):
        return ''


class WhatResponder(Responder):
    def response(self, input_text, mood):
            return f"{input_text}ってなに？"


class RandomResponder(Responder):
    def response(self, input_text, mood):
        return random.choice(self.dictionary.random)


class PatternResponder(Responder):
    def response(self, input_text, mood):
        for item in self.dictionary.pattern:
            m = item.match(input_text)
            if m:
                resp = item.choise(mood)
                if resp != None:
                    return resp.replace('%match%', m.group(0))
        return random.choice(self.dictionary.random)
