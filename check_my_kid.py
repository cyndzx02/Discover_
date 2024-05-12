import random

class Check_kid:
    def __init__(self):
        self.words = {}

    def teach_word(self, word, definition):
        self.words[word] = definition

    def get_definition(self, word):
        if word in self.words:
            return self.words[word]
        else:
            return "Sorry, but i do not know that word!"

    def test_word(self):
        if not self.words:
            return "No words have been taught yet."
        else:
            word = random.choice(list(self.words.keys()))
            definition = self.words[word]
            return f"What is the definition of '{word}'?\nDefinition: {definition}"

if __name__ == "__main__":
    ai = Check_kid()
    
    ai.teach_word("Sitdown", "sit")
    ai.teach_word("Mommy", "mother")
    ai.teach_word("Daddy", "Father")
    print(ai.test_word())
