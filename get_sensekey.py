import argparse
import importlib
import os
import string
from xml.etree import ElementTree

# arguments parsing
argparser = argparse.ArgumentParser()
argparser.add_argument('-a', '--algorithm')
argparser.add_argument('-d', '--dataset')
args = argparser.parse_args()

dataset_path = "dataset/{dataset_name}/{dataset_name}.data.xml".format(dataset_name=args.dataset)
output_dir = "evaluation_result/{}/{}".format(args.dataset, args.algorithm)
output_path = output_dir + "/{}.predicted.key.txt".format(args.dataset)

# `get_sensekey` function must be defined in the imported package
get_sensekey = importlib.import_module("algorithm." + args.algorithm).get_sensekey

OPEN_BRACKETS = "([{"
if __name__ == '__main__':
    tree = ElementTree.parse(dataset_path)
    corpus = tree.getroot()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'a') as f:
        for text in corpus:
            for sentence in text:
                sent_txt = ""
                # reconstruct sentence
                for child in sentence:
                    if child.text in string.punctuation and child.text not in OPEN_BRACKETS:
                        sent_txt = sent_txt.rstrip()
                    sent_txt += child.text
                    if child.text not in OPEN_BRACKETS:
                        sent_txt += " "
                # disambiguate word
                print(sent_txt)
                for child in sentence:
                    if child.tag == 'instance':
                        word = child.text
                        pos = child.attrib['pos']
                        lemma = child.attrib['lemma']
                        id = child.attrib['id']
                        sense_key = get_sensekey(sent_txt.strip(), word, lemma, pos)
                        if not sense_key:
                            continue
                        else:
                            print(word, "====>", sense_key)
                            print(id, sense_key, file=f)
                print('=' * 100)
