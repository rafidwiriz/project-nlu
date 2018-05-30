class Token(object):
    def __init__(self, word, stem=None, entity=None, pos=None):
        self.word = word
        self.stem = stem if stem else '_'
        self.entity = entity if entity else '_'
        self.pos = pos if pos else '_'

    def set(self, stem=None, entity=None, pos=None):
        self.stem = stem if stem else self.stem
        self.entity = entity if entity else self.entity
        self.pos = pos if pos else self.pos

    def delete(self, type_attr):
        if (type_attr == 'stem'):
            self.stem = '_'
        elif (type_attr == 'entity'):
            self.entity = '_'
        elif (type_attr == 'pos'):
            self.pos = '_'
        else:
            print("Atribut tidak diketahui. Pilih antara 'stem', 'entity', atau 'pos'.")