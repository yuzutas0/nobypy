# -*- coding: utf-8 -*-

from numpy.random import *
from responder import WhatResponder, RandomResponder, PatternResponder, TemplateResponder, MarkovResponder, SearchResponder
from morph import Morph
import re
from dictionary import Dictionary


class Emotion:
    mood_min = -15
    mood_max = 15
    mood_recovery = 0.5
    dictionary = Dictionary()
    
    def __init__(self):
        self.mood = 0
    
    def clear(self):
        self.mood = 0

    def adjust_mood(self, value):
        self.mood += value
        if self.mood > self.mood_max:
            self.mood = self.mood_max
        elif self.mood < self.mood_min:
            self.mood = self.mood_min
    
    def update(self, input_text):
        for item in self.dictionary.pattern:
            if item.match(input_text):
                self.adjust_mood(item.modify)
                break
        
        if self.mood < 0:
            self.mood += self.mood_recovery
        elif self.mood > 0:
            self.mood -= self.mood_recovery


class Unmo:
    def __init__(self, name):
        self.name = name
        self.emotion = Emotion()
        self.responders = {
            'what': WhatResponder('What'),
            'random': RandomResponder('Random'),
            'pattern': PatternResponder('Pattern'),
            'template': TemplateResponder('Template'),
            'markov': MarkovResponder('Markov'),
            'search': SearchResponder('Search')
        }
        self.responder = self.responders['pattern']

    def dialogue(self, input_text):
        self.emotion.update(input_text)
        tokens = Morph.analyze(input_text)

        number = randint(20)
        if number == 0:
            self.responder = self.responders['what']
        elif number <= 5:
            self.responder = self.responders['pattern']
        elif number <= 9:
            self.responder = self.responders['template']
        elif number <= 13:
            self.responder = self.responders['markov']
        elif number <= 17:
            self.responder = self.responders['search']
        else:
            self.responder = self.responders['random']
        response = self.responder.response(input_text, tokens, self.emotion.mood)

        RandomResponder.dictionary.study(input_text, tokens)
        return response

    def save(self):
        RandomResponder.dictionary.save()
