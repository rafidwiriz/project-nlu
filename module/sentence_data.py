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

    def token_to_ent(self):
        """None -> [str]"""
        token2ent = []
        ent_before = ""
        for token, ent in zip(self.tokens, self.entities):
            if (ent == 'O'):
                token2ent.append(token)
            else:
                if (ent != ent_before):
                    token2ent.append(ent)
            ent_before = ent
        return token2ent