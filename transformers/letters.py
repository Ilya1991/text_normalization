from transformers.base import BaseTransformer


class Letters(BaseTransformer):
    @staticmethod
    def transform(s, **kwargs):
        string = str(s).lower()
        return ' '.join([char for char in string if char.isalpha()])

