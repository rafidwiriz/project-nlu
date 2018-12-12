from module.sentence_data import SentenceData
from module.load_data import load_data
from module.tokenizer import tokenize, stem
from module.bag_words import BagOfWords
from module.entity_extractor import extract_entity
from module import trainer
from sklearn.externals import joblib
import pandas as pd
import json

train, intents = load_data('data/svara_training.json')

vocab_data = BagOfWords()
intent_data = BagOfWords()

for sent, intent in zip(train, intents):
    tokenize(sent)
    # stem(sent)
    intent_data.add_word(intent)
    for token in sent.token_to_ent():
        vocab_data.add_word(token)

train_set, valid_set, dicts = extract_entity(train)

labels = vocab_data.create_labels()
labels.append("intent")

bow_tuples = []

for i, sent in enumerate(train):
    bow_tuple = tuple(vocab_data.create_bow(sent.token_to_ent()) + intent_data.create_bow_keys([intents[i]]))
    bow_tuples.append(bow_tuple)
    
df = pd.DataFrame.from_records(bow_tuples, columns=labels)

model = trainer.train_entities(train_set, valid_set, dicts)
clf2 = trainer.train_grid_search_svara(df)

model.save('model/model.h5')
joblib.dump(clf2, 'model/clf2.pkl')
with open('model/dicts.json', 'w') as fp:
    json.dump(dicts, fp)