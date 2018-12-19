from flask import Flask, request, make_response, jsonify, redirect
from module.sentence_data import SentenceData
from module.bag_words import BagOfWords
from sklearn.externals import joblib
from keras.models import load_model
from json import load
import pandas as pd
import numpy as np
import nltk
import requests
import datetime

app = Flask(__name__)
WIT_TOKEN = 'RUU3F6BNDSDLL7RO6ZLL6V6IKN3Z5T4W'

@app.route('/wit-sound', methods=['POST'])
def witSound():
    params = {'v': get_string_date()}
    headers = {'Authorization': 'Bearer ' + WIT_TOKEN, 'Content-Type': 'audio/mpeg3'}
    res = requests.post("https://api.wit.ai/speech", params=params, headers=headers, data=request.get_data())
    res = res.json()

    r = slu(res['text'])

    if r:
        r = make_response(jsonify(r))
        r = (r, 200)
    else:
        r = make_response(jsonify({"text": "Oops. Something went wrong!"}))
        r = (r, 404)

    return r

def slu(txt):
    text = SentenceData(txt)

    text_predict = np.array(list(map(lambda x: toIndex(x, w2idx), text.get("text").split())))
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

    return response

def toIndex(txt, dict):
    if dict.get(txt, None):
        return dict[txt]
    else:
        minVal = len(txt)
        idx = 0
        for word, i in dict.items():
            val = nltk.edit_distance(txt, word)
            if val < minVal:
                minVal = val
                idx = i
        if minVal < 3:
            return idx
        else:
            return 0

if __name__ == "__main__":
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
    
    app.run()