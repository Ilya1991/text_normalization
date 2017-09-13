from transformers.base import BaseTransformer
from transformers.utils import to_ordinal
from transformers.utils import MORPH


YEAR = MORPH.parse('год')[0]


class Date(BaseTransformer):
    """
    Date to string converter
    """
    @staticmethod
    def transform(s, **kwargs):

        string = s.split(' ')

        # get case_type
        parsed = [MORPH.parse(s) for s in string]
        cases = [p[0].tag.case for p in parsed]
        cases = [c for c in cases if c]
        try:
            case = cases[0]
        except IndexError:
            case = 'nomn'

        # analyze last word
        last_word = string[-1]
        last_word_parse = MORPH.parse(last_word)[0]

        if hasattr(last_word_parse, 'normal_form'):
            if last_word_parse.normal_form != YEAR.word and len(string) > 2:
                string.append(YEAR.inflect({case}).word)

        # convert numbers to string
        result_str = [to_ordinal(s, case_type=case) for s in string]
        result_str = ' '.join(result_str)
        return result_str


