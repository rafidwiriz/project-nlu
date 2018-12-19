from module.sentence_data import SentenceData
from module.bag_words import BagOfWords
from sklearn.externals import joblib
from keras.models import load_model
from json import load
import pandas as pd
import numpy as np

clf2 = joblib.load('model/clf2.pkl')
model = load_model('model/model.h5')

with open('model/dicts.json', 'r') as fp:
    dicts = load(fp)
    
with open('model/vocab.json', 'r') as fp:
    vocab = load(fp)
    vocab = {int(k):vocab[k] for k in vocab}
    vocab_data = BagOfWords(vocab)
    
with open('model/intent.json', 'r') as fp:
    intent = load(fp)
    intent = {int(k):intent[k] for k in intent}

w2idx, labels2idx = dicts['words2idx'], dicts['labels2idx']
idx2w  = {w2idx[k]:k for k in w2idx}
idx2la = {labels2idx[k]:k for k in labels2idx}

text = "tolong putarkan lagu separuh aku dari noah terima kasih"
text = SentenceData(text)

text_predict = np.array(list(map(lambda x: w2idx[x], text.get("text").split())))
text_predict = text_predict[np.newaxis,:]
pred = model.predict_on_batch(np.array(text_predict))
pred = np.argmax(pred,-1)[0]

predword_val = []
for label in pred:
    x = idx2la[label]
    predword_val.append(x)
text.set("entities", predword_val)

labels = vocab_data.create_labels()
bow_tuple = [tuple(vocab_data.create_bow(text.token_to_ent()))]

df = pd.DataFrame.from_records(bow_tuple, columns=labels)

idxIntent = clf2.predict(df)
idxIntent = idxIntent[0]

response = {}
response["text"] = text.get("text")
response["intent"] = intent[idxIntent]
response["entities"] = text.extract_entity()
print(response)