# -*- coding: utf-8 -*-

import copy
import random
import pickle


class Markov:
    end_mark = '%END%'
    chain_max = 30
    
    def __init__(self):
        self.dic = {}
        self.starts = {}
    
    def add_sentence(self, parts):
        if len(parts) < 3:
            return
        
        parts = copy.deepcopy(parts)
        point = 0
        for part in parts:
            if part.surface == '' or part.surface is None:
                continue
            parts[point] = part.surface
            point += 1
        
        prefix1 = parts.pop(0)
        prefix2 = parts.pop(0)
        self.__add_start(prefix1)
        
        for suffix in parts:
            self.__add_suffix(prefix1, prefix2, suffix)
            prefix1 = prefix2
            prefix2 = suffix
        
        self.__add_suffix(prefix1, prefix2, self.end_mark)
    
    def generate(self, keyword):
        if len(self.dic) == 0:
            return None
        words = []
        
        prefix1 = keyword if (keyword in self.dic.keys()) else self.__select_start()
        prefix2 = random.choice(list(self.dic[prefix1].keys()))
        words.extend([prefix1, prefix2])
        
        for x in range(self.chain_max):
            suffix = random.choice(self.dic[prefix1][prefix2])
            if suffix == self.end_mark:
                break
            words.append(suffix)
            prefix1 = prefix2
            prefix2 = suffix
        
        return ''.join(words)
    
    # TODO: filenameが同じなのは不自然?
    def load(self, f):
        # f = open(filename,'rb')
        self.dic = pickle.load(f)
        self.starts = pickle.load(f)
        # f.close()

    # TODO: filenameが同じなのは不自然?
    def save(self, f):
        # f = open(filename,'wb')
        pickle.dump(self.dic, f)
        pickle.dump(self.starts, f)
        # f.close

    # private method
    def __add_suffix(self, prefix1, prefix2, suffix):
        if prefix1 not in self.dic.keys():
            self.dic[prefix1] = {}
        if prefix2 not in self.dic[prefix1].keys():
            self.dic[prefix1][prefix2] = []
        self.dic[prefix1][prefix2].append(suffix)

    def __add_start(self, prefix1):
        if prefix1 not in self.starts.keys():
            self.starts[prefix1] = 0
        self.starts[prefix1] += 1

    def __select_start(self):
        return random.choice(list(self.starts.keys()))
