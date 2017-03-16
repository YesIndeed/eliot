import random
import math

HEAT_VAL = 30

'''
A bag of phrases is a wrapper around multiple lists of strings.
For the dialog system, it stores state about which list was last
accessed.
'''
class BagOfPhrases:
    def __init__(self, heat, filepath):
        # self.max_heat = len(words)*HEAT_VAL
        with open(filepath, 'r') as content_file:
            content = content_file.read()
            # Extract individual severity bags
            content = content.split('---')
            # Populate the phrases matrix indexed by [severity level][phrase idx]
            self.phrases = [filter(None, bag.split('\n')) for bag in content]
            self.max_heat = len(phrases)*heat

    def get(self, heat=0):
        idx = int(math.ceil(heat%self.max_heat/HEAT_VAL))
        return random.choice(self.phrases[idx])
