# -*- coding: utf-8 -*-

import random
import re
from dictionary import Dictionary


dictionary = Dictionary()


class Responder:
    def __init__(self, name):
        self.name = name
    
    def response(self, input_text, mood):
        return ''


class WhatResponder(Responder):
    def response(self, input_text, mood):
            return f"{input_text}ってなに？"


class RandomResponder(Responder):
    def response(self, input_text, mood):
        return random.choice(dictionary.random)


class PatternResponder(Responder):
    def response(self, input_text, mood):
        for item in dictionary.pattern:
            m = item.match(input_text)
            if m:
                resp = item.choise(mood)
                if resp != None:
                    return resp.replace('%match%', m.group(0))
        return random.choice(dictionary.random)
