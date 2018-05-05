# -*- coding: utf-8 -*-

import random
from numpy.random import *
from responder import WhatResponder, RandomResponder, PatternResponder
import re
from dictionary import Dictionary


dictionary = Dictionary()


class Emotion:
    mood_min = -15
    mood_max = 15
    mood_recovery = 0.5
    
    def __init__(self):
        self.mood = 0
    
    def adjust_mood(self, value):
        self.mood += value
        if self.mood > self.mood_max:
            self.mood = self.mood_max
        elif self.mood < self.mood_min:
            self.mood = self.mood_min
    
    def update(self, input_text):
        for item in dictionary.pattern:
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
            'pattern': PatternResponder('Pattern')
        }
        self.responder = self.responders['pattern']
    
    def dialogue(self, input_text):
        self.emotion.update(input_text)
        number = randint(9)
        if number == 0:
            self.responder = self.responders['what']
        elif number >= 5:
            self.responder = self.responders['pattern']
        else:
            self.responder = self.responders['random']
        return self.responder.response(input_text, self.emotion.mood)

