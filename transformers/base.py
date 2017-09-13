class BaseTransformer:
    @staticmethod
    def transform(s, **kwargs):
        return s

    def __str__(self):
        return self.__class__.__name__
