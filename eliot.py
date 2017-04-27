from phrasemanager import PhraseManager
import os
import random
from nltk.sentiment.vader import SentimentIntensityAnalyzer

'''
Eliot is an aspiring politician. Though a friend to many, he has many
pain points and anger management issues that he hasn't quite worked
through yet. He alternates between intense arrogance and crushing
insecurity. But still, he'd like to hear what you think*.

*   Unless it happens to be about his potential connection to the mafia**.
**  Or if you're talking about the media***.
*** Or the word "give," the 97th most common English word. We're not
    sure why either.
'''

CULT_WORDS = ['cult', 'demon', 'devil', 'dark ones', ]

class EliotBot:
    def __init__(self):
        self._heat = 0 # 0-100. 100 triggers MELTDOWN state.
        self._interest = 70
        self._state = 'intro'
        self.sia = SentimentIntensityAnalyzer()
        with open('states.txt', 'r') as content_file:
            content = content_file.read()
            # Extract individual severity bags
            self.states = list(filter(None, content.split('\n')))
            # Instantiate a phrase manager for each state.
            self.phraseManagers = {state:PhraseManager('dialog/%s.tp' % state) for state in self.states}

    def handle_state(self, s):
        if 'goodbye' in s.lower():
            return 'end'
        # enter and then don't leave the meltdown state
        if self._state == 'meltdown' or self._heat >= 50:
            return 'meltdown'
        elif self._state == 'cult':
            ss = self.sia.polarity_scores(s)
            interest = 100
            # If you're positive enough and don't mention cults, return to smalltalk.
            if ss['pos'] > 0.5 and ss['pos'] > ss['neg'] and not any(word in s.lower() for word in CULT_WORDS):
                heat -= 10
                return 'smalltalk'

        # loop over all the states
        # if there is a tag that coincides, switch to that state.
        for state in self.states:
            manager = self.phraseManagers[state]
            if any(tag in s for tag in manager.tags):
               self._interest = 70
               return state
        self._interest -= 5

        # If Eliot gets bored of conversation, he might default to making small talk.
        if self._state == 'intro' or self._interest < 40 and random.random() > .8:
            return 'smalltalk'
        return self._state

    def handle_heat(self, s):
        # analyze the sentiment of a sentence
        ss = self.sia.polarity_scores(s)
        self._heat += 10 * ss['neg']
        if any(word in s for word in CULT_WORDS):
            self._heat += 10
            self._state = 'defensive'
        print('heat: %i' % self._heat) # debug

    def get_phrase(self, state, s):
        return self.phraseManagers[state].get(s)

    def run(self):
        print(self.get_phrase(self._state,'debug'))
        while(self._state != 'meltdown' and self._state != 'end'):
            s = input(">> ")
            # Update internal state according to input.
            self.handle_heat(s)
            self._state = self.handle_state(s)
            if self._state == 'meltdown' or self._state == 'end':
                continue
            print(self.get_phrase(self._state,s))

        if self._state == 'end':
            if self._heat < 30:
                print('I\'m glad that we could have this conversation.')
                return
            else:
                print('I\'ve had enough of this. Good day.')
                return

        with open('dialog/meltdown.convo') as f:
            for line in f:
                print(line,end='')
                s = input(">> ")
            print('<A horrifying monster bursts from Eliot\'s chest and begins to devour you.>')
            print('GAME OVER.')


def main():
    e = EliotBot()
    e.run()

if __name__ == "__main__": main()
