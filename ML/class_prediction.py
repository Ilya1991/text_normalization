from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.externals import joblib
from ML.preprocessing import series2vec
import os


ESTIMATOR_PATH = os.path.join(os.path.dirname(__file__), 'estimators', 'class_predictor')


def make_estimator(word_series, y):
    """
    Learn estimator for class detection
    :param word_series: series of words
    :param y: word classes
    """
    X = series2vec(word_series)
    estimator = GradientBoostingClassifier(verbose=5)

    cv_score = cross_val_score(estimator, X, y, scoring='accuracy')
    print(cv_score)

    estimator.fit(X, y)
    joblib.dump(estimator, ESTIMATOR_PATH, compress=9)
    return estimator



