from transformers.base import BaseTransformer
from pymorphy2.shapes import is_latin
# from transliterate import translit
from sklearn.externals import joblib
import os


TRANSLIT_DICTIONARY = os.path.join(os.path.dirname(__file__), 'dictionaries', 'eng2rus_translit')


class TranslitDictionary:
    def __init__(self):
        self.path = TRANSLIT_DICTIONARY

        if os.path.isfile(self.path):
            self.dict = joblib.load(self.path)
        else:
            self.dict = dict()

    def add(self, latin, cyrillic):
        for lat, cyr in zip(latin, cyrillic):
            if lat in self.dict:
                continue
            self.dict[lat] = cyr
        self._dump()

    def _dump(self):
        joblib.dump(self.dict, self.path, compress=9)

    def get(self, word):
        try:
            return self.dict[word]
        except KeyError:
            return word

    def transform(self, word):
        word = str(word).lower()
        result_word = self.get(word)

        if any(elem in word for elem in ('-', '—')):
            return result_word

        if any(elem in result_word for elem in ('-', '—')):
            return result_word

        if word == result_word and len(word) == 1:
            return result_word + '_latin'

        return ' '.join([letter + '_trans' for letter in result_word])


class Plain(BaseTransformer):
    def __init__(self, translit_dict):
        self.translit_dict = TranslitDictionary()

    def transform(self, s, **kwargs):
        s = str(s)
        if not is_latin(s):
            return s.replace('ё', 'е')
        return self.translit_dict.transform(s)
        # TODO: additional translitaration
        # return translit(s, 'ru')


