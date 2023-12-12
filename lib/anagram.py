# your code goes here!

class Anagram(str):
    def __init__(self, word):
        self.word = word

    def is_anagram(self, word):
        return (
            self.word.lower() != word.lower() and
            sorted(self.word.lower()) == sorted(word.lower())
        )

    def match(self, candidates):
        return [word for word in candidates if self.is_anagram(word)]