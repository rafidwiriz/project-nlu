import json

class TrainingData(object):
    """Bertanggung jawab dalam memuat dan memproses data training."""

    def __init__(self, text, intent, entities):
        self.intent = intent
        self.text = text
        self.entities = entities

    def get(self, prop):
        return getattr(self, prop)

    def set(self, prop, value):
        setattr(self, prop, value)