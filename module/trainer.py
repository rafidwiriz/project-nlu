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