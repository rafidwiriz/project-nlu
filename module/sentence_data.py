import json

class SentenceData(object):
    """Bertanggungjawab dalam memuat dan memproses data kalimat."""

    def __init__(self, text, entities):
        #self.intent = intent # str
        self.text = text # str
        self.entities = [] # [str]
        self.entities_dict = entities # dict
        self.tokens = [] # [str]
        self.pos = [] # [str]
        self.stem = [] # [str]

    def get(self, prop):
        """str -> attribute TrainingData"""
        return getattr(self, prop)

    def set(self, prop, value):
        setattr(self, prop, value)