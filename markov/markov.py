# -*- coding: utf-8 -*-

import copy
import random


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
        prefix1 = parts.pop(0)
        prefix2 = parts.pop(0)
        self.add_start(prefix1)
        
        for suffix in parts:
            self.add_suffix(prefix1, prefix2, suffix)
            prefix1 = prefix2
            prefix2 = suffix
        
        add_suffix(prefix1, prefix2, self.end_mark)
    
    def generate(self, keyword):
        if len(self.dic) == 0:
            return None
        
        words = []
        
        prefix1 = keyword if keyword in self.dic.keys() else self.select_start()
        prefix2 = random.choice(self.dic[prefix1].keys())
        words.extend([prefix1, prefix2])
        
        for x in range(self.chain_max):
            suffix = random.choice(self.dic[prefix1][prefix2])
            if suffix == self.end_mark:
                break
            words.append(suffix)
            prefix1 = prefix2
            prefix2 = suffix
        
        return ''.join(words)
