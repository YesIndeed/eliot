import random
import math

HEAT_VAL = 30

class Phrase:
    def __init__(self, phrase):
        s = list(filter(None, phrase.split('\n')))
        self.tags = self.getTags(s[0])
        self.phrase = s[1]

    def getTags(self, tags):
        out = []
        for tag in tags.split('|'):
            out.append(tag.lower())
        return out

'''
A bag of phrases is a wrapper around multiple lists of strings.
For the dialog system, it stores state about which list was last
accessed.
'''
class PhraseManager:
    def __init__(self, filepath):
        # self.max_heat = len(words)*HEAT_VAL
        with open(filepath, 'r') as content_file:
            content = content_file.read()
            # Extract individual severity bags
            content = list(filter(None, content.split('---')))
            # Create a phrase object for each phrase.
            self.phrases = [Phrase(phrase) for phrase in content]
            # All tags associated with phrases in this manager.
            self.tags = set()
            # Populate all tags.
            for phrase in self.phrases:
                for t in phrase.tags:
                    self.tags.add(tags)

    def get(self, s=''):
        # candidate output phrases
        candidates = set()
        for p in self.phrases:
            if self.isPhraseRelevant(p, s):
                candidates.add(p)
        if candidates:
            return random.sample(candidates, 1)[0].phrase
        return random.sample(self.phrases, 1)[0].phrase

    def isPhraseRelevant(self, p, s):
        for tag in p.tags:
            if tag in s:
                return True
        return False
