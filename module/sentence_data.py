import json

class SentenceData(object):
    """Bertanggungjawab dalam memuat dan memproses data kalimat."""

    def __init__(self, text):
        #self.intent = intent # str
        self.text = text # str
        self.entities = [] # [str]
        #self.entities_dict = entities # dict
        self.tokens = list(text.split()) # [str]
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
        for token, ent in zip(self.tokens, self.entities):
            if (ent == 'O'):
                token2ent.append(token)
            else:
                if (ent[0] == 'B') or (ent[0] == 'U'):
                    token2ent.append(ent)
        return token2ent

    def extract_entity(self):
        """None -> [dict]"""
        entities = []
        entity = ""
        sent = ""
        for token, ent in zip(self.tokens, self.entities):
            if (ent[0] == 'B'):
                if entity != ent[2:]:
                    if entity != "":
                        ent_dict = {"name": entity, "value": sent}
                        entity, sent = "", ""
                        entities.append(ent_dict)
                    entity = ent[2:]
                    sent += token
            elif (ent[0] == 'I'):
                sent = sent + ' ' + token
            elif (ent[0] == 'O'):
                if entity != "":
                    ent_dict = {"name": entity, "value": sent}
                    entity, sent = "", ""
                    entities.append(ent_dict)
        return entities
