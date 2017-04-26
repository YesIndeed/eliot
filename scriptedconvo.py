import random
import math

HEAT_VAL = 30

'''
A ScriptedConvo iterates over a scripted conversation line-by-line.
There can be multiple scripted conversations depending on severity.
'''
class ScriptedConvo:
    def __init__(self, heat, filepath):
        # self.max_heat = len(words)*HEAT_VAL
        with open(filepath, 'r') as content_file:
            content = content_file.read()
            # Extract individual severity bags
            content = content.split('---')
            # Populate the phrases matrix indexed by [severity level][phrase idx]
            self.phrases = [filter(None, bag.split('\n')) for bag in content]
            # Store current indices for progress made in each script.
            self.indices = [0 for bag in content]
            self.max_heat_level = len(self.phrases)-1

    '''
    Return if we have reached the end of a conversation for a given severity.
    '''
    def end_of_convo(self, heat=0):
        heat_level = int(min(heat/HEAT_VAL, self.max_heat_level))
        curr_idx = self.indices[heat_level]
        return curr_idx >= len(self.phrases[heat_level])

    '''
    Find the appropriate script and return the next line in that conversation.
    By default, if the end of a script has been reached, return an empty string.
    '''
    def get(self, heat=0):
        out = ''

        # Check which severity level we are using.
        heat_level = int(min(heat/HEAT_VAL, self.max_heat_level))
        # Current index within appropriate conversation.
        curr_idx = self.indices[heat_level]
        # If we have not exhausted this conversation, get the next phrase
        # and increment the index.
        if not self.end_of_convo(heat):
            out = self.phrases[heat_level][curr_idx]
            self.indices[heat_level] += 1
        return out

    '''
    Reset the current index.
    '''
    def reset(self, heat=0, val=0):
        heat_level = int(min(heat/HEAT_VAL, self.max_heat_level))
        curr_idx = self.indices[heat_level]
        self.indices[heat_level] = val
