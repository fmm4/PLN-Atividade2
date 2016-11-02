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

 	pcfg_productions = []
 	for item in pcfg_set:
 		for tree in item:
	 		tree.collapse_unary(collapsePOS=False)
	 		tree.chomsky_normal_form(horzMarkov=2)
	 		pcfg_productions += tree.productions()

 	pcfg_tbank_grammar = grammar.induce_pcfg(grammar.Nonterminal('S'), pcfg_productions)
 	print(pcfg_tbank_grammar)



if __name__ == "__main__":
    main()