# WSD Evaluator
Provides an interface for [Unified Word Sense Disambiguation (WSD) evaluation framework](http://lcl.uniroma1.it/wsdeval/home)

# System Requirements
* Windows 10 operating system
* Python 3.0 and above
* WordNet 3.0+ corpora

# Dataset
The dataset included in this repository is retrieved from http://lcl.uniroma1.it/wsdeval/evaluation-data

Available dataset:
* Senseval2
* Senseval3
* SemEval2007
* SemEval2013
* SemEval2015
* ALL (concatenation of previous dataset)

# Usage
### Preparation
1. Wrap the codes/algorithm to be evaluated inside the function `get_sensekey` with the following signatures:
```
    def get_sensekey(sentence, word, lemma, pos):
        """
        Return the most likely sense key of `word` given `sentence` as context.

       :param str sentence: Context of `word`
       :param str word: Word to be disambiguate
       :param str lemma: lemma of `word`
       :param str pos: part-of-speech tag of `word`
       :return: sense key of disambiguated lemma
       :rtype: str
        """
```
Example:
```
#  algorithm/example.py

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
```

2. Put the `.py` file inside the `algorithm/` directory.

### Evaluation
##### Using Command line argument
1. (Optional step) Activate virtual environment.
2. In command prompt/powershell, change directory (`cd`) to `Evaluation/` then type and execute the following command:
<br/>```evaluate [your .py filename] [dataset name]``` (e.g. ```evaluate example semeval2015```)

3. The evaluation result will be displayed in the console. In addition, you can also view the evaluation result output under `evaluation_result/[dataset name]/[your .py filename]/` directory.

##### Using Interactive command prompt
1. Run `evaluate_interactive.bat` (by double clicking the `.bat` file or type `evaluate_interactive` in console), then follow the instruction on screen.


# References
 * Michael Lesk. 
 Automatic sense disambiguation using machine readable dictionaries: how to tell a pine cone from an ice cream cone. 
SIGDOC '86 Proceedings of the 5th annual international conference on Systems documentation

 * Alessandro Raganato, Jose Camacho-Collados and Roberto Navigli.
Word Sense Disambiguation: A Unified Evaluation Framework and Empirical Comparison.
Proceedings of EACL 2017, Valencia, Spain
