import json

class SentenceData(object):
    """Bertanggungjawab dalam memuat dan memproses data kalimat."""

    def __init__(self, text, intent, entities):
        self.intent = intent # str
        self.text = text # str
        self.entities = entities # str
        self.token = [] # [str]
        self.pos = [] # [str]
        self.stem = [] # [str]

    def get(self, prop):
        return getattr(self, prop)

    def set(self, prop, value):
        setattr(self, prop, value)