# -*- coding: utf-8 -*-

import random
from responder import WhatResponder, RandomResponder


class Unmo:
    def __init__(self, name):
        self.name = name
        self.responders = [
            WhatResponder('What'),
            RandomResponder('Random')
        ]
        self.responder = self.responders[0]
    
    def dialogue(self, input_text):
        self.responder = random.choice(self.responders)
        return self.responder.response(input_text)
