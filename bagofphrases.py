import random
import math

HEAT_VAL = 30

'''
A bag of phrases is a wrapper around multiple lists of strings.
For the dialog system, it stores state about which list was last
accessed.
'''
class BagOfPhrases:
    def __init__(self, words):
        self.words = words
        self.max_heat = len(words)*HEAT_VAL

    def get(self, heat=0):
        idx = int(math.ceil(heat%self.max_heat/HEAT_VAL))
        return random.choice(self.words[idx])
