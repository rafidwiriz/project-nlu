from module.sentence_data import SentenceData
from module.entity_extractor import extract_entity
from module.load_data import load_data
from module.tokenizer import tokenize
from module.bag_words import BagOfWords

train = load_data('data/training_data.json')
slots = []
vocab_data = BagOfWords()
for sent in train:
    tokenize(sent)
    slot = extract_entity(sent)
    slots.append(slot)
for i, sent in enumerate(train):
    for j, token in enumerate(sent.get("tokens")):
        vocab_data.add_word(token)
print(vocab_data.vocab)
for slot in slots:
    print(slot)