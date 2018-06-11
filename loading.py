from module.sentence_data import SentenceData
from module.entity_extractor import extract_entity
from module.load_data import load_data
from module.tokenizer import tokenize, stem
from module.bag_words import BagOfWords
from module.trainer import train_grid_search_svara
import pandas as pd

train, intents = load_data('data/svara_training.json')
slots = []
vocab_data = BagOfWords()
intent_data = BagOfWords()
for sent, intent in zip(train, intents):
    tokenize(sent)
    slot = extract_entity(sent)
    stem(sent)
    slots.append(slot)
    intent_data.add_word(intent)
for sent in train:
    for token in sent.token_to_ent():
        vocab_data.add_word(token)
'''for sent, slot in zip(train, slots):
    print(vocab_data.create_bow(sent.get("tokens")))
    print(slot)'''
labels = vocab_data.create_labels()
labels.append("intent")
bow_tuples = []
for i, sent in enumerate(train):
    bow_tuple = tuple(vocab_data.create_bow(sent.token_to_ent()) + intent_data.create_bow_keys([intents[i]]))
    bow_tuples.append(bow_tuple)
df = pd.DataFrame.from_records(bow_tuples, columns=labels)
clf = train_grid_search_svara(df)