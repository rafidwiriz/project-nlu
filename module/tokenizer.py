from token import Token
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def tokenize(str):
    words = str.split()
    tokens = []
    for word in words:
        token = Token(word)
        tokens.append(token)
    return tokens

def stem(token):
    stemmer = StemmerFactory().create_stemmer()
    if (token.entity == '_'):
        stem_word = stemmer.stem(token.word)
        token.set(stem=stem_word)
