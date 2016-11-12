from nltk.corpus import treebank
from nltk.tree import *
from nltk.draw import tree
from nltk import grammar as g
import numpy as np
import random

def cky_parsing(words,grammar):
	nonterminals = list(set([a._lhs for a in grammar.productions()]))
	scores = [[dict() for word in words] for word in words]
	back = [[dict() for word in words] for word in words]


	for i in range(0,len(words)-1):
		lh_nonterminals = grammar.productions(None,words[i],False)
		for production in lh_nonterminals:
			a = production._lhs.unicode_repr()
			scores[i][i+1][a] = production.prob()
		added = True
		while added:
			added = False
			for A in nonterminals:
				if (A in scores[i][i+1].keys()):
					if (scores[i][i+1][A] > 0):
						for B in nonterminals:
							for k in grammar.productions(g.Nonterminal(B), g.Nonterminal(A), False):
								if(k._rhs[1]==""):
									probability = k.prob()*scores[i][i+1][A]
									if probability > score[i][i+1][B]:
										score[i][i+1][B] = probability
										back[i][i+1][B] = A
										added = True
										print("wewlad")
	for span in range(2,len(words)-1):
		print("wewmeme")
		for begin in range(0,len(words)-1-span):
			end = begin + span
			for split in range(begin+1,end-1):
				for A in nonterminals:
					for B in nonterminals:
						a_prod = grammar.productions(g.Nonterminal(A),g.Nonterminal(B), False)
						for p in a_prod:
							C = p._rhs[1].unicode_repr()
							prob = score[begin][split][B]*score[split][end][C]*a_prod.prob()
							if (prob > score[begin][end][A]):
								score[begin][end][A] = prob
								back[begin][end][A] = (split,B,C)
	return scores, back






def prepare_databases(database,pct):
	dataset_size = len(database)
	pcfg = random.sample(list(database), int(dataset_size*pct))
	cky = [x for x in database if x not in pcfg]
	return pcfg, cky


def main():
 	pcfg_set,cky_set = prepare_databases(treebank.parsed_sents(),0.75)

 	# pcfg_productions = []
 	# for item in pcfg_set:
 	# 	for tree in item:
	 # 		tree.collapse_unary(collapsePOS=False)
	 # 		tree.chomsky_normal_form(horzMarkov=2)
	 # 		pcfg_productions += tree.productions()

 	# pcfg_tbank_grammar = grammar.induce_pcfg(g.Nonterminal('S'), pcfg_productions)

 	cky_productions = []
 	for item in cky_set:
 		for tree in item:
	 		tree.collapse_unary(collapsePOS=False)
	 		tree.chomsky_normal_form(horzMarkov=2)
	 		cky_productions += tree.productions()

 	cky_tbank_grammar = g.induce_pcfg(g.Nonterminal('S'),cky_productions)

 	for item in cky_set:
 		scrs,back = cky_parsing(item.leaves(),cky_tbank_grammar)
 		print(scrs)
 		print(back)



if __name__ == "__main__":
    main()