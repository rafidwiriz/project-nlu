from module.sentence_data import SentenceData
from module.entity_extractor import extract_entity
from module.load_data import load_data
from module.tokenizer import tokenize
from module.bag_words import BagOfWords

train, label = load_data('data/training_data.json')
slots = []
vocab_data = BagOfWords()
label_data = BagOfWords()
for intent in label:
    label_data.add_word(intent)
for sent in train:
    tokenize(sent)
    slot = extract_entity(sent)
    slots.append(slot)
for i, sent in enumerate(train):
    print(' '.join(sent.get("tokens")))
    for j, token in enumerate(sent.get("tokens")):
        vocab_data.add_word(token)
for sent, intent, slot in zip(train, label, slots):
    print(vocab_data.create_bow(sent.get("tokens")), label_data.create_bow([intent]))
    print(slot)