from main import FOLDER, TEST
import pandas as pd
from normalize import TextNormalizer
from datetime import datetime as dt
import os
import csv


def make_submission():
    """ Make submission to Kaggle """
    text_normalizer = TextNormalizer()
    X = pd.read_csv(TEST)
    id = X['sentence_id'].astype(str) + '_' + X['token_id'].astype(str)
    after = text_normalizer.transform_series(X['before'])

    X_norm = pd.concat([id, after], axis=1)
    X_norm.columns = ['id', 'after']

    submission_filename = os.path.join(FOLDER, 'submission_{}.csv'.format(str(dt.now())))
    X_norm.to_csv(submission_filename, sep=',', header=True, index=False, quoting=csv.QUOTE_ALL)


if __name__ == '__main__':
    make_submission()