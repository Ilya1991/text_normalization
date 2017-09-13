import numpy as np
# from transformers.utils import MORPH


# ANALYZERS = [
#     'PunctuationAnalyzer',
#     'AbbreviatedFirstNameAnalyzer',
#     'KnownSuffixAnalyzer',
#     'LatinAnalyzer',
#     'HyphenSeparatedParticleAnalyzer',
#     'HyphenatedWordsAnalyzer',
#     'AbbreviatedPatronymicAnalyzer',
#     'HyphenAdverbAnalyzer',
#     'DictionaryAnalyzer',
#     'KnownPrefixAnalyzer',
#     'UnknAnalyzer',
#     'RomanNumberAnalyzer',
#     'UnknownPrefixAnalyzer',
#     'NumberAnalyzer'
# ]


def word2vec(word, n_features=30):
    """
    Convert word to numpy array
    :param word: input word
    :param n_features: number features
    :return: numpy array
    """
    # perform morphological analysis
    word = str(word)
    # p = MORPH.parse(word)[0]
    #
    # tag_predictors = []
    #
    # analyzer = p.methods_stack[0][0].__class__.__name__
    #
    # tag_values = (
    #     (p.tag.POS, p.tag.PARTS_OF_SPEECH),
    #     (p.tag.animacy, p.tag.ANIMACY),
    #     (p.tag.gender, p.tag.GENDERS),
    #     (p.tag.case, p.tag.CASES),
    #     (p.tag.number, p.tag.NUMBERS),
    #     (analyzer, ANALYZERS)
    # )
    #
    # for row in tag_values:
    #     tag, tag_catalog = row
    #     cur_pred = [int(tag == t) for t in tag_catalog]
    #     tag_predictors += cur_pred

    # tag_predictors = np.array(tag_predictors)
    x_row = np.zeros(n_features, dtype=int)

    for n, letter in enumerate(word[:n_features]):
        x_row[n] = ord(letter)

    # return tag_predictors
    return x_row
    # return np.concatenate([x_row, tag_predictors])


def series2vec(series, n_features=30):
    """
    Convert word to numpy array
    :param series: input series of words
    :param n_features: number features
    :return: numpy array
    """
    data = []

    for word in series.values:
        data.append(word2vec(word, n_features=n_features))

    return np.array(data)
