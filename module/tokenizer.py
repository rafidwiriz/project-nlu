from .token import Token
from .training_data import TrainingData
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def tokenize(sent_data):
    """TrainingData -> [Token]"""
    tokens = []
    words, slot = change_to_entity(sent_data)
    for word in words:
        token = Token(word)
        tokens.append(token)
    sent_data.set("text", words)
    return tokens

def stem(token):
    """Token* -> ??"""
    stemmer = StemmerFactory().create_stemmer()
    if (token.entity == '_'):
        stem_word = stemmer.stem(token.word)
        token.set(stem=stem_word)

def change_to_entity(sent_data):
    """TrainingData -> [str], Dict"""
    slot = {}
    entities = sent_data.get("entities")
    text = sent_data.get("text")
    for entity in entities:
        slot[entity["entity"]] = entity["value"]
        if not("end" in entity):
            entity["end"] = entity["start"]
        for i in range(entity["start"], (entity["end"] + 1)):
            text[i] = "({})".format(entity["entity"]) if (i == entity["start"]) else 'del'
    if 'del' in text: text.remove('del')
    return text, slot