import num2words
import pymorphy2


MORPH = pymorphy2.MorphAnalyzer()


def _is_plural(word):
    """
    Define if word is plural (for thousands and millions)
    :param word: string
    :return: bool
    """
    for w in ('тысяч', 'миллионов', 'тысячи', 'миллиона'):
        if word.endswith(w):
            return 'plur'
    return 'sing'


def _num2text(s, ordinal=False, case_type='nomn'):
    words = num2words.num2words(s, ordinal=False, lang='ru')
    words = words.split(' ')

    if words[0] in ('одна', 'один'):
        words = words[1:]

    result_word = []

    # parse words
    for n, word in enumerate(words):
        parsed = MORPH.parse(word)
        cur_tag = parsed[0].tag

        # for numeric words
        if 'NUMR' in cur_tag or 'ADJF' in cur_tag:
            inflected = parsed[0].inflect({case_type})

        # for nouns
        else:
            cur_numb = _is_plural(word)
            cur_case_type = case_type

            if cur_case_type != 'nomn':
                inflected = parsed[0].inflect({cur_case_type, cur_numb})
            else:
                inflected = parsed[0]
        try:
            result_word.append(inflected.word)
        except AttributeError:
            result_word.append(parsed[0].word)

    return ' '.join(result_word)


def to_cardinal(s, ordinal=False, case_type='nomn'):
    """
    Convert numeric representation to text
    :param s: string
    :param ordinal: if ordinal
    :param case_type: case type
    :return: converted number
    """
    try:
        return _num2text(s, ordinal=ordinal, case_type=case_type)
    except:
        return s


def to_ordinal(num, case_type='nomn'):
    """
    Convert to
    :param num: number
    :param case_type: case
    :return: text representation of number
    """
    try:
        word = num2words.num2words(num, lang='ru')
        words = word.split(' ')
        if words[0] in ('один', 'одна') and len(words) > 1:
            words = words[1:]

        word_to_change = words[-1]

        parsed = MORPH.parse(word_to_change)
        inflected = parsed[0].inflect({case_type, 'Anum'})

        if hasattr(inflected, 'word'):
            words[-1] = inflected.word

        return ' '.join(words)
    except ValueError:
        return num
