class Token(object):
    """Bertanggungjawab dalam pembuatan dan penyimpanan token."""
    
    def __init__(self, word, stem=None, entity=None, pos=None):
        self.word = word # str
        self.stem = stem if stem else '_' # str
        self.entity = entity if entity else '_' # str
        self.pos = pos if pos else '_' # str

    def get(self, prop):
        return getattr(self, prop)
    
    def set(self, prop, value):
        setattr(self, prop, value)

    def delete(self, prop):
        setattr(self, prop, '_')