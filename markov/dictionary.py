# -*- coding: utf-8 -*-

import codecs
import re
import os
import shutil
import random
from singleton import SingletonType
from markov import Markov


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

    original_directory = '../KOISURU_PROGRAM/sample/markov/dics/'
    random_file = './random.txt'
    pattern_file = './pattern.txt'
    template_file = './template.txt'
    markov_files = [
        './markov_dic.pkl',
        './markov_starts.pkl'
    ]

    def __init__(self):
        self.__load_random()
        self.__load_pattern()
        self.__load_template()
        self.__load_markov()
    
    def __load_file(self, original_file, use_file):
        if not os.path.isfile(use_file):
            shutil.copyfile(original_file, use_file)

    def __load_random(self):
        self.__load_file(self.original_directory + 'random.txt', self.random_file)
        self.random = messages(self.random_file)

    def __load_pattern(self):
        self.__load_file(self.original_directory + 'pattern.txt', self.pattern_file)
        self.pattern = []
        rows = messages(self.pattern_file)
        for row in rows:
            divided = row.split('\t')
            item = PatternItem(divided[0], divided[1])
            self.pattern.append(item)

    def __load_template(self):
        self.__load_file(self.original_directory + 'template.txt', self.template_file)
        self.template = {}
        rows = messages(self.template_file)
        for row in rows:
            divided = row.split('\t')
            if divided[0] == None:
                continue
            count = int(divided[0])
            if not count in self.template.keys():
                self.template[count] = []
            self.template[count].append(divided[1])

    def __load_markov(self):
        self.markov = Markov()
        self.markov.load(markov_files[0], markov_files[1])

    def study(self, input_text, tokens):
        self.study_random(input_text)
        self.study_pattern(input_text, tokens)
        self.study_template(tokens)
        self.study_markov(tokens)

    def study_random(self, input_text):
        if not input_text in self.random:
            self.random.append(input_text)

    def find_pattern(self, word, input_text):
        for item in self.pattern:
            if re.match(word, item.pattern) == None:
                continue
            for phrase in item.phrases:
                if phrase['phrase'] == input_text:
                    break
                if phrase == item.phrases[-1]:
                    return item
        return None

    def study_pattern(self, input_text, tokens):
        for token in tokens:
            if not Morph.is_keyword(token):
                continue
            word = token.surface
            duped = self.find_pattern(word, input_text)
            if duped != None:
                duped.phrases.append({'need': 0, 'phrase': input_text})
            else:
                self.pattern.append(PatternItem(word, '0##' + input_text))

    def study_template(self, tokens):
        template = ''
        count = 0
        for token in tokens:
            word = token.surface
            if Morph.is_keyword(token):
                word = '%noun%'
                count += 1
            template += word
        if count == 0:
            return
        if not count in self.template.keys():
            self.template[count] = []
        if not template in self.template[count]:
            self.template[count].append(template)

    def study_markov(self, tokens):
        self.markov.add_sentence(tokens)

    def save(self):
        # random
        content = codecs.open(self.random_file, 'w', 'shift_jis')
        for x in self.random:
            content.write(x + "\n")
        content.close()

        # pattern
        content = codecs.open(self.pattern_file, 'w', 'shift_jis')
        for x in self.pattern:
            phrase = ''
            for y in x.phrases:
                phrase = phrase + str(y['need']) + '##' + y['phrase'] + '|'
            phrase = phrase[:-1]
            content.write(str(x.modify) + '##' + x.pattern + '\t' + phrase + '\n')
        content.close()

        # template
        content = codecs.open(self.template_file, 'w', 'shift_jis')
        for count in self.template.keys():
            for template in self.template[count]:
                content.write(str(count) + '\t' + template + "\n")
        content.close()
        
        self.markov.save(markov_files[0], markov_files[1])
