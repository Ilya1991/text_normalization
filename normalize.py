from ML.utils import predict_class
from transformers.plain import TranslitDictionary
from transformers import *


class TextNormalizer:

    # transliteration dictionary
    TRANSLIT_DICT = TranslitDictionary()

    # dictionary of transformers
    ALL_TRANSFORMERS = dict(
        PLAIN=Plain(TRANSLIT_DICT),
        PUNCT=Punct(),
        CARDINAL=Cardinal(),
        LETTERS=Letters(),
        DATE=Date(),
        VERBATIM=BaseTransformer(),
        ORDINAL=BaseTransformer(),
        MEASURE=BaseTransformer(),
        TELEPHONE=BaseTransformer(),
        DECIMAL=BaseTransformer(),
        ELECTRONIC=BaseTransformer(),
        MONEY=BaseTransformer(),
        FRACTION=BaseTransformer(),
        DIGIT=BaseTransformer(),
        TIME=BaseTransformer()
    )

    def transform_word(self, word):
        """
        Normalize single word
        :param word: input word
        :return: normalized word
        """
        predicted_class = predict_class(word)
        transformer = self.ALL_TRANSFORMERS[predicted_class]
        return transformer.transform(word)

    def transform_series(self, series):
        """
        Normalize text
        :param series: pandas Series
        :return: normalized pandas series
        """
        return series.apply(self.transform_word)



