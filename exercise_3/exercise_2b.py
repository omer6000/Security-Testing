"""
Use this file to implement your solution for exercise 3-2 a.
"""

from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from fuzzingbook.GrammarCoverageFuzzer import GrammarCoverageFuzzer
from re_coverage import get_coverage

from exercise_2 import RE_GRAMMAR
from exercise_2a import RE_GRAMMAR_EXPANDED

import random

random.seed()

steps = 25
c1 = 0
c2 = 0
c3 = 0

for i in range(steps):
    # run the experiment for GrammarFuzzer with RE_GRAMMAR
    gf1 = GrammarFuzzer(RE_GRAMMAR,min_nonterminals=3,max_nonterminals=20)
    c1 += get_coverage(gf1)

    # run the experiment for GrammarCoverageFuzzer with RE_GRAMMAR
    gf2 = GrammarCoverageFuzzer(RE_GRAMMAR,min_nonterminals=3,max_nonterminals=20)
    c2 += get_coverage(gf2)

    # run the experiment for GrammarCoverageFuzzer with RE_GRAMMAR_EXPANDED
    gf3 = GrammarCoverageFuzzer(RE_GRAMMAR_EXPANDED,min_nonterminals=3, max_nonterminals=20)
    c3 += get_coverage(gf3)

print('GrammarFuzzer: {}'.format(c1/steps)) # print the average code coverage for GrammarFuzzer + RE_GRAMMAR
print('GrammarCoverageFuzzer: {}'.format(c2/steps)) # print the average code coverage for GrammarCoverageFuzzer + RE_GRAMMAR
print('GrammarCoverageFuzzer+: {}'.format(c3/steps)) # print the average code coverage for GrammarCoverageFuzzer + RE_GRAMMAR_EXPANDED
