# -*- coding: utf-8 -*-

import random
import re
from dictionary import Dictionary
from morph import Morph


class Responder:
    dictionary = Dictionary()

    def __init__(self, name):
        self.name = name
    
    def response(self, input_text='', tokens=[], mood=0):
        return ''


class WhatResponder(Responder):
    def response(self, input_text='', tokens=[], mood=0):
            return f"{input_text}ってなに？"


class RandomResponder(Responder):
    def response(self, input_text='', tokens=[], mood=0):
        return random.choice(self.dictionary.random)


class PatternResponder(Responder):
    def response(self, input_text='', tokens=[], mood=0):
        for item in self.dictionary.pattern:
            m = item.match(input_text)
            if m:
                resp = item.choise(mood)
                if resp != None:
                    return resp.replace('%match%', m.group(0))
        return random.choice(self.dictionary.random)


class TemplateResponder(Responder):
    def response(self, input_text='', tokens=[], mood=0):
        keywords = []
        for token in tokens:
            if Morph.is_keyword(token):
                keywords.append(token.surface)
        count = len(keywords)
        if count > 0 and count in self.dictionary.template.keys():
            template = random.choice(self.dictionary.template[count])
            for keyword in keywords:
                template = template.replace('%noun%', keyword, 1)
            return template
        return random.choice(self.dictionary.random)


class MarkovResponder(Responder):
    def response(self, input_text='', tokens=[], mood=0):
        keyword = ''
        for token in tokens:
            if Morph.is_keyword(token):
                keyword = token.surface
        generated = self.dictionary.markov.generate(keyword)
        return generated if ((generated is not None) and (len(generated) > 0)) else random.choice(self.dictionary.random)
