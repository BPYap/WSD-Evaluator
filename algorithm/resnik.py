""" Word Sense Disambiguation using Resnik Method """
from nltk.corpus import wordnet as wn
from pywsd.similarity import max_similarity


def get_sensekey(sentence, word, lemma, pos):
    wordnet_pos = {'VERB': wn.VERB, 'NOUN': wn.NOUN, 'ADJ': wn.ADJ, 'ADV': wn.ADV}
    try:
        synsets = max_similarity(sentence, word, option="resnik", pos=wordnet_pos[pos], best=False)
        for _, synset in synsets:
            for lemma_ in synset.lemmas():
                if lemma_.name().lower() == lemma.lower():
                    return lemma_.key()
    except:
        return None

    return None
