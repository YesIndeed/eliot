from bagofphrases import BagOfPhrases
from scriptedconvo import ScriptedConvo
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
        self._state = 'convo'
        self.defaultBag = BagOfPhrases(30, 'dialog/default.txt')
        self.defaultConvo = ScriptedConvo(30, 'dialog/convo.txt')
        self.cultConvo = ScriptedConvo(30, 'dialog/cult.txt')

    '''
    Handle state transitions. Currently hardcoded.
    Transitions should have a notion of precedence.
    '''
    def handle_state(self, s):
        if any(word in s for word in CULT_WORDS):
            print '(state transition to cult)'
            self._state = 'cult'
        elif 'conversation' in s or 'convo' in s:
            print '(state transition to convo)'
            self._state = 'convo'
        elif 'default' in s:
            print '(state transition to default)'

    def handle_heat(self, s):
        if any(word in s for word in CULT_WORDS):
            self._heat += 20
        elif self._state == 'cult':
            self._heat += 10
        elif self._state == 'default':
            # For debug purposes.
            self._heat += 5

    def run(self):
        while(1):
            if self._state == 'convo':
                print(self.defaultConvo.next(self._heat))
            elif self._state == 'cult':
                print(self.cultConvo.next(self._heat))
            else:
                print(self.defaultBag.get(self._heat))
            s = raw_input(">> ")
            # Update internal state according to input.
            self.handle_state(s)
            self.handle_heat(s)

def main():
    e = EliotBot()
    e.run()

if __name__ == "__main__": main()
