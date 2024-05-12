import random

class learn:
    def __init__(self):
        self.responses = ["Sure", "Okay", "Yes", "Absolutely", "Definitely", "Of course", "Done"]

    def repeat_word(self, word):
        return random.choice(self.responses) + ", " + word

if __name__ == "__main__":
    ai = learn()
    word = input("Enter a word: ")
    print(ai.repeat_word(word))
