from nltk.corpus import treebank
from nltk.tree import *
from nltk.draw import tree
from nltk import grammar
import random

def prepare_databases(database,pct):
	dataset_size = len(database)
	pcfg = random.sample(list(database), int(dataset_size*pct))
	cky = [x for x in database if x not in pcfg]
	return pcfg, cky


def main():
 	pcfg_set,cky_set = prepare_databases(treebank.parsed_sents(),0.75)

 	pcfg_tbank_productions = []
 	for sent in pcfg_set:
 		for production in sent.productions():
 			pcfg_tbank_productions.append(production)

 	for word,tag in treebank.tagged_words():
 		t = Tree.fromstring("("+tag+" "+word+")")
 		for production in t.productions():
 			pcfg_tbank_productions.append(production)

 	pcfg_tbank_grammar = grammar.induce_pcfg(grammar.Nonterminal('S'), pcfg_tbank_productions)

 	print(pcfg_tbank_grammar)


if __name__ == "__main__":
    main()