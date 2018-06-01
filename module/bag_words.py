from collections import Counter

class BagOfWords(object):
    """Bertanggungjawab dalam pembuatan bag-of-words tiap kalimat."""

    def __init__(self):
        self.vocab = {} # dict
        self.index = 0 # int
    
    def add_word(self, word):
        """str -> None"""
        if word not in self.vocab.values():
            self.vocab[self.index] = word
            self.index += 1

    def create_bow(self, tokens):
        """[str] -> [int]"""
        bow = []
        count = Counter(tokens)
        for i in range(self.index):
            if self.vocab[i] in count:
                bow.append(count[self.vocab[i]])
            else:
                bow.append(0)
        return bow