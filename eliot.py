from phrasemanager import PhraseManager
import os

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

CULT_WORDS = ['cult', 'demon', 'devil', 'dark ones']

class EliotBot:
    def __init__(self):
        self._heat = 0 # 0-100. 100 triggers MELTDOWN state.
        self._state = 'intro'
        with open(filepath, 'r') as content_file:
            content = content_file.read()
            # Extract individual severity bags
            states = list(filter(None, content.split(' ')))
            # Instantiate a phrase manager for each state.
            self.phraseManagers = {state:PhraseManager('dialog/%s.tp' % state) for state in states}

    def handle_state(self, s):
        # loop over all the states
        # if there is a tag that coincides, switch to that state.

    def get_phrase(self, state, s):
        # get the phrase from an associated state
        # return
        # if no such phrase exists, return empty string(?)
        return ''

    def run(self):
        loop = 'continue'
        while(loop == 'continue'):
            s = raw_input(">> ")
            # Update internal state according to input.
            self.handle_state(s)
            self.get_phrase(s)

            if loop == 'exit':
                if self._state == 'cult':
                    print('<A horrifying monster bursts from Eliot\'s chest and begins to devour you.>')
                elif self._state == 'convo':
                    print('I do belive this conversation is over.')
                print('GAME OVER.')

def main():
    e = EliotBot()
    e.run()

if __name__ == "__main__": main()
