from .token import Token
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def tokenize(sent_data):
    """SentenceData -> [Token]"""
    sent_data.set("token", sent_data.get("text").split())

'''def stem(token):
    """Token* -> ??"""
    stemmer = StemmerFactory().create_stemmer()
    if (token.entity == '_'):
        stem_word = stemmer.stem(token.word)
        token.set(stem=stem_word)'''
