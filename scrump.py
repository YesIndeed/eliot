from enum import Enum
from bagofphrases import BagOfPhrases

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

class EState(Enum):
    DEFAULT = 0
    MAFIA = 1
    MEDIA = 2
    GIVE = 3
    MELTDOWN = 4

class ScrumpBot:
    def __init__(self):
        self._heat = 0 # 0-100. 100 triggers MELTDOWN state.
        self._state = EState.DEFAULT
        self.defaultBag = BagOfPhrases([['I don\'t understand the question.',
                                         'All of the women on The Apprentice flirted with me -- consciously or unconsciously. That\'s to be expected.',
                                         'You have to think anyway, so why not think big?',
                                         'Anyone who thinks my story is anywhere near over is sadly mistaken.'],
                                         ['Perhaps it\'s time America was run like a business.',
                                         'Part of the beauty of me is that I am very rich.',
                                         'When I think I\'m right, nothing bothers me.'],
                                         ['Every time you walk down the street people are screaming, \"You\'re fired!\"',
                                         'I had some beautiful pictures taken in which I had a big smile on my face.  I looked happy, I looked content, I looked like a very nice person, which in theory I am.',
                                         'Well, someone\'s doing the raping, Don! I mean, somebody\'s doing it. Who\'s doing the raping? Who\'s doing the raping?!']
                                       ])

    def run(self):
        while(1):
            s = raw_input(">> ")
            self._heat += 10
            print(self.defaultBag.get(self._heat))

def main():
    scrump = ScrumpBot()
    scrump.run()

if __name__ == "__main__": main()