from module.training_data import TrainingData
from module.load_data import load_data
from module.tokenizer import tokenize, stem

train = load_data('data/training_data.json')
tokens = []
for i, sent in enumerate(train):
    token_sent = tokenize(sent)
    tokens.append(token_sent)
for i, sent in enumerate(tokens):
    for j, token in enumerate(sent):
        print(token.word)