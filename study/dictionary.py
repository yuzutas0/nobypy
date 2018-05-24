# -*- coding: utf-8 -*-

import codecs
import re
import os
import shutil
import random
from singleton import SingletonType


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

    dictionary_file = './random.txt'

    def __init__(self):
        # random
        directory = '../KOISURU_PROGRAM/sample/study/dics/'
        if not os.path.isfile(self.dictionary_file):
            shutil.copyfile(directory + 'random.txt', self.dictionary_file)
        self.random = messages(self.dictionary_file)
        # pattern
        self.pattern = []
        rows = messages(directory + 'pattern.txt')
        for row in rows:
            divided = row.split('\t')
            item = PatternItem(divided[0], divided[1])
            self.pattern.append(item)

    def study(self, input_text):
        if not input_text in self.random:
            self.random.append(input_text)

    def save(self):
        content = codecs.open(self.dictionary_file, 'w', 'shift_jis')
        for x in self.random:
            content.write(x + "\n")
        content.close()
