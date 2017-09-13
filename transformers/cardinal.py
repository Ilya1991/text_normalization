from transformers.utils import to_cardinal
from transformers.base import BaseTransformer


class Cardinal(BaseTransformer):
    @staticmethod
    def transform(s, **kwargs):
        case_type = kwargs.pop('case_type', 'nomn')
        return to_cardinal(s, case_type=case_type)

