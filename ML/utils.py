from ML.class_prediction import ESTIMATOR_PATH as CLASS_DETECTOR_PATH
from ML.preprocessing import series2vec, word2vec
from sklearn.externals import joblib
from pandas import Series


CLASS_DETECTOR = joblib.load(CLASS_DETECTOR_PATH)


def predict_class(input_data):
    """
    Predict class of object
    :param input_data: pandas Series or str
    :return: numpy array or string
    """
    if isinstance(input_data, Series):
        X = series2vec(input_data)
        return CLASS_DETECTOR.predict(X)

    else:
        X = word2vec(input_data)
        X = X.reshape(1, -1)
        return CLASS_DETECTOR.predict(X)[0]
