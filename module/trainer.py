import numpy as np

def intent_separate(data):
    """DataFrame -> DataFrame, DataFrame"""
    return data.drop("intent", axis=1), data.intent

def train_grid_search_svara(data):
    from sklearn.model_selection import GridSearchCV
    from sklearn.svm import SVC

    X, y = intent_separate(data)

    params = [{"C": [1, 2, 5, 10, 20, 100], "kernel": ["linear"]}]
    #cv_splits = max(2, min(5, np.min(np.bincount(y)) // 5))

    clf = GridSearchCV(SVC(C=1, probability=True, class_weight='balanced'),
                            param_grid=params, scoring='f1_weighted', verbose=1)

    clf.fit(X, y)

    return clf

"""
def train_random_search(data):
    from sklearn.model_selection import RandomizedSearchCV
    from sklearn.svm import SVC
    from scipy.stats import randint as sp_randint

    X, y = intent_separate(data)

    params = {"C": sp_randint(1, 100), "kernel": ["linear"]}

    clf = RandomizedSearchCV(SVC(C=1, probability=True, class_weight='balanced'),
                                param_distributions=params, scoring='f1_weighted', verbose=1, n_iter=20)

    clf.fit(X, y)

    return clf
"""

def train_entities(train_set, valid_set, dicts):
    from keras.models import Sequential
    from keras.layers.embeddings import Embedding
    from keras.layers.core import Dense, Dropout
    from keras.layers.wrappers import TimeDistributed
    from keras.layers import Convolution1D, GRU

    w2idx, labels2idx = dicts['words2idx'], dicts['labels2idx']

    train_x, _, train_label = train_set
    val_x, _, val_label = valid_set

    # Create index to word/label dicts
    idx2w  = {w2idx[k]:k for k in w2idx}
    idx2la = {labels2idx[k]:k for k in labels2idx}

    # For conlleval script
    words_train = [ list(map(lambda x: idx2w[x], w)) for w in train_x]
    labels_train = [ list(map(lambda x: idx2la[x], y)) for y in train_label]
    words_val = [ list(map(lambda x: idx2w[x], w)) for w in val_x]
    labels_val = [ list(map(lambda x: idx2la[x], y)) for y in val_label]

    n_classes = len(idx2la)
    n_vocab = len(idx2w)

    model = Sequential()
    model.add(Embedding(n_vocab,100))
    model.add(Convolution1D(128, 5, padding='same', activation='relu'))
    model.add(Dropout(0.25))
    model.add(GRU(100,return_sequences=True))
    model.add(TimeDistributed(Dense(n_classes, activation='softmax')))
    model.compile('rmsprop', 'categorical_crossentropy')

    import progressbar
    n_epochs = 30

    for i in range(n_epochs):
        print("Training epoch {}".format(i))
    
    bar = progressbar.ProgressBar(maxval=len(train_x))
    for n_batch, sent in bar(enumerate(train_x)):
        label = train_label[n_batch]
        # Make labels one hot
        label = np.eye(n_classes)[label][np.newaxis,:] 
        # View each sentence as a batch
        sent = sent[np.newaxis,:]

        if sent.shape[1] > 1: #ignore 1 word sentences
            model.train_on_batch(sent, label)

    return model