# -*- coding: utf-8 -*-

import random
from numpy.random import *
from responder import WhatResponder, RandomResponder, PatternResponder
import re
from dictionary import Dictionary


dictionary = Dictionary()

class Unmo:
    def __init__(self, name):
        self.name = name
        self.responders = [
            WhatResponder('What'),
            RandomResponder('Random'),
            PatternResponder('Pattern')
        ]
        self.responder = self.responders[0]
    
    def dialogue(self, input_text):
        number = randint(9)
        if number == 0:
            self.responder = self.responders[0]
        elif number >= 5:
            self.responder = self.responders[2]
        else:
            self.responder = self.responders[1]
        return self.responder.response(input_text)


class Emotion:
    mood_min = -15
    mood_max = 15
    mood_recovery = 0.5
    
    def __init__(self):
        self.mood = 0
    
    def adjust_mood(self, value):
        self.mood += value
        if self.mood > mood_max:
            self.mood = mood_max
        elif self.mood < mood_min:
            self.mood = mood_min
    
    def update(self, input_text):
        for item in dictionary.pattern:
            if re.search(item, input_text):
                adjust_mood(item.modify)
                break
        
        if self.mood < 0:
            self.mood += mood_recovery
        elif self.mood > 0:
            self.mood -= mood_recovery
