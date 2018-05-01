# -*- coding: utf-8 -*-

import random
from numpy.random import *
from responder import WhatResponder, RandomResponder, PatternResponder


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
