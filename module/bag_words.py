from collections import Counter

class BagOfWords(object):
    """Bertanggungjawab dalam pembuatan bag-of-words tiap kalimat."""

    def __init__(self, vocab=None):
        self.vocab = {0: "UNK"} if vocab == None else vocab # dict
        self.index = 1 if vocab == None else len(vocab) # int
    
    def add_word(self, word):
        """str -> None"""
        if word not in self.vocab.values():
            self.vocab[self.index] = word
            self.index += 1

    def create_bow(self, tokens):
        """[str] -> [str]"""
        bow = []
        count = Counter(tokens)
        for i in range(self.index):
            x = 1 if self.vocab[i] in count else 0
            bow.append(x)
            '''
            if self.vocab[i] in count:
                bow.append(count[self.vocab[i]])
            else:
                bow.append(0)'''
        return bow

    def create_bow_keys(self, tokens):
        """[str] -> [str]"""
        keys = self.create_labels()
        bow_keys = []
        for word in tokens:
            bow_keys.append(keys.index(word))
        return bow_keys

    def create_labels(self):
        """None -> [str]"""
        labels = list(self.vocab.values())
        return labels

    def create_keys(self):
        """None -> [str]"""
        keys = list(self.vocab.keys())
        return keys