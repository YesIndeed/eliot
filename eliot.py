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

class EliotBot:
    def __init__(self):
        self._heat = 0 # 0-100. 100 triggers MELTDOWN state.
        self._state = 'default'
        self.defaultBag = BagOfPhrases(30, 'default.txt')

    def run(self):
        while(1):
            s = raw_input(">> ")
            self._heat += 10
            print(self.defaultBag.get(self._heat))

def main():
    e = EliotBot()
    e.run()

if __name__ == "__main__": main()