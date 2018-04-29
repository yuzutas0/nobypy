# -*- coding: utf-8 -*-

from responder import RandomResponder


class Unmo:
    def __init__(self, name):
        self.name = name
        self.responder = RandomResponder('Random')
    
    def dialogue(self, input_text):
        return self.responder.response(input_text)
