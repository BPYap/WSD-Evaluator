""" Word Sense Disambiguation using Lesk Algorithm """
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.wsd import lesk


def get_sensekey(sentence, word, lemma, pos):
    wordnet_pos = {'VERB': wn.VERB, 'NOUN': wn.NOUN, 'ADJ': wn.ADJ, 'ADV': wn.ADV}
    synset = lesk(word_tokenize(sentence), word, pos=wordnet_pos[pos])
    if synset is not None:
        for lemma_ in synset.lemmas():
            if lemma_.name().lower() == lemma.lower():
                return lemma_.key()
    else:
        return None
