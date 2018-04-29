# -*- coding: utf-8 -*-

import random


class Responder:
    def __init__(self, name):
        self.name = name
    
    def response(self, input_text):
        return ''


class WhatResponder(Responder):
    def response(self, input_text):
            return f"{input_text}ってなに？"


class RandomResponder(Responder):
    def __init__(self, name):
        super().__init__(name)
        self.responses = [
            '今日はさむいね',
            'チョコたべたい',
            'きのう10円ひろった'
        ]
    
    def response(self, input_text):
        return random.choice(self.responses)
