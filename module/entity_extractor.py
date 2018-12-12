import io
import json
from pathlib import Path
import numpy as np

def create_vocab(*args):
    vocab = {"UNK": 0}
    index = 1
    for arg in args:
        for item in arg:
            for comp in item:
                if comp not in vocab:
                    vocab[comp] = index
                    index += 1
    return vocab

def extract_entity(sent_datas):

    words_train = []
    ne_train = []
    groundtruth_train = []
    words_val = []
    ne_val = []
    groundtruth_val = []

    for sent_data in sent_datas:
        words_train.append(sent_data.get("text").split())
        groundtruth_train.append(sent_data.get("entities"))

    w2idx = create_vocab(words_train, words_val)
    ne2idx = {}
    la2idx = create_vocab(groundtruth_train, groundtruth_val)

    train_x = [np.array(list(map(lambda x: w2idx[x], w))) for w in words_train]
    train_ne = ne_train
    train_label = [np.array(list(map(lambda x: la2idx[x], y))) for y in groundtruth_train]
    val_x = [np.array(list(map(lambda x: w2idx[x], w))) for w in words_val]
    val_ne = ne_val
    val_label = [np.array(list(map(lambda x: la2idx[x], y))) for y in groundtruth_val]

    train_set = (train_x, train_ne, train_label)
    val_set = (val_x, val_ne, val_label)

    dicts = {"words2idx": w2idx, "ne2idx": ne2idx, "labels2idx": la2idx}

    return (train_set, val_set, dicts)