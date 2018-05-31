import json

class TrainingData(object):
    """Bertanggung jawab dalam memuat dan memproses data training."""

    def __init__(self, text, intent, entities):
        self.intent = intent # str
        self.text = text.split() # [str]
        self.entities = entities # str

    def get(self, prop):
        return getattr(self, prop)

    def set(self, prop, value):
        setattr(self, prop, value)