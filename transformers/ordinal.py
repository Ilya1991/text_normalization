from transformers.utils import to_ordinal
from transformers.base import BaseTransformer


class Ordinal(BaseTransformer):
    @staticmethod
    def transform(s, **kwargs):
        case_type = kwargs.pop('case_type', 'nomn')
        return to_ordinal(s, case_type=case_type)


