# -*- coding: utf-8 -*-

import codecs
import re
import os
import shutil
import random
from singleton import SingletonType
from morph import Morph


def messages(path):
    results = []
    content = codecs.open(path, 'r', 'shift_jis')
    for row in content:
        if row.rstrip() != '':
            results.append(row.rstrip())
    content.close()
    return results

def covert_int(text):
    if text != None:
        return int(text)
    return 0

def is_suitable(need, mood):
    if need == 0:
        return True
    if need > 0:
        return mood > need
    else:
        return mood < need


class PatternItem:
    separator = re.compile('^((-?\d+)##)?(.*)$')

    def __init__(self, pattern, phrases):
        m = self.separator.search(pattern)
        self.modify = covert_int(m.group(2))
        self.pattern = m.group(3)
        self.phrases = []
        for phrase in phrases.split('|'):
            m = self.separator.search(phrase)
            self.phrases.append({
                'need': covert_int(m.group(2)),
                'phrase': m.group(3)
            })
    
    def match(self, text):
        return re.search(self.pattern, text)
    
    def choise(self, mood):
        choises = []
        for p in self.phrases:
            if is_suitable(p['need'], mood):
                choises.append(p['phrase'])
        if len(choises) == 0:
            return None
        return random.choice(choises)


class Dictionary:
    __metaclass__ = SingletonType

    original_directory = '../KOISURU_PROGRAM/sample/study2/dics/'
    random_file = './random.txt'
    pattern_file = './pattern.txt'

    def __init__(self):
        # random
        if not os.path.isfile(self.random_file):
            shutil.copyfile(self.original_directory + 'random.txt', self.random_file)
        self.random = messages(self.random_file)

        # pattern
        if not os.path.isfile(self.pattern_file):
            shutil.copyfile(self.original_directory + 'pattern.txt', self.pattern_file)
        self.pattern = []
        rows = messages(self.pattern_file)
        for row in rows:
            divided = row.split('\t')
            item = PatternItem(divided[0], divided[1])
            self.pattern.append(item)

    def study(self, input_text, tokens):
        self.study_random(input_text)
        self.study_pattern(input_text, tokens)

    def study_random(self, input_text):
        if not input_text in self.random:
            self.random.append(input_text)

    def find_pattern(self, word):
        for item in self.pattern:
            if word == item.pattern:
                return item
        return None

    def study_pattern(self, input_text, tokens):
        for token in tokens:
            if not Morph.is_keyword(token):
                next
            word = token.surface
            duped = self.find_pattern(word)
            if duped != None:
                duped.phrases.append({'need': 0, 'phrase': word})
            else:
                self.pattern.append(PatternItem(word, '0##' + input_text))

    def save(self):
        # random
        content = codecs.open(self.random_file, 'w', 'shift_jis')
        for x in self.random:
            content.write(x + "\n")
        content.close()
