from ML.class_prediction import make_estimator, ESTIMATOR_PATH
from transformers.plain import TranslitDictionary, TRANSLIT_DICTIONARY
import os
import pandas as pd


# class        id      change  prc         change_prc
# PLAIN       7360439  544102  69.61        7.39
# PUNCT       2288640       0  21.64        0.00
# CARDINAL     272442  271934   2.58       99.81
# LETTERS      189528  189481   1.79       99.98
# DATE         185959  185859   1.76       99.95
# VERBATIM     157912   12944   1.49        8.20
# ORDINAL       46738   46535   0.44       99.57
# MEASURE       40534   39920   0.38       98.49
# TELEPHONE     10088   10088   0.10      100.00
# DECIMAL        7297    7193   0.07       98.57
# ELECTRONIC     5832    5677   0.06       97.34
# MONEY          2690    2623   0.03       97.51
# FRACTION       2460    2435   0.02       98.98
# DIGIT          2012    2012   0.02      100.00
# TIME           1945    1895   0.02       97.43


def make_transliteration_dictionary(train):
    """
    Create transliteration dictionary
    """
    X = pd.read_csv(train, usecols=['before', 'after', 'class'])
    X = X[(X['class'] == 'PLAIN') & (X['before'] != X['after'])]

    # preprocess data
    X['after'] = X['after'].str.replace('_trans', '')
    X['after'] = X['after'].str.replace('_latin', '')
    X['after'] = X['after'].str.replace(' ', '')
    X['after'] = X['after'].str.strip()
    X['before'] = X['before'].str.lower()
    X['before'] = X['before'].str.strip()

    latin = X['before'].tolist()
    cyrillic = X['after'].tolist()

    dictionary = TranslitDictionary()
    dictionary.add(latin, cyrillic)


def make_class_detection_classifier(train):
    """
    Create class detection classifier
    """
    X = pd.read_csv(train, usecols=['before', 'class'])
    X = X.sample(n=500000)
    words = X['before']
    classes = X['class']
    make_estimator(words, classes)


if __name__ == '__main__':

    FOLDER = os.path.dirname(os.path.dirname(__file__))
    TRAIN = os.path.join(FOLDER, 'ru_train.csv')
    TEST = os.path.join(FOLDER, 'ru_test.csv')

    # learn estimator if not exists
    if not os.path.isfile(ESTIMATOR_PATH):
        make_class_detection_classifier(TRAIN)

    # make transliteration dictionary if not exists
    if not os.path.isfile(TRANSLIT_DICTIONARY):
        make_transliteration_dictionary(TRAIN)


