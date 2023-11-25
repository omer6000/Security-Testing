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

# run the experiment for GrammarFuzzer with RE_GRAMMAR
# run the experiment for GrammarCoverageFuzzer with RE_GRAMMAR
# run the experiment for GrammarCoverageFuzzer with RE_GRAMMAR_EXPANDED

print('GrammarFuzzer: {}'.format(0)) # print the average code coverage for GrammarFuzzer + RE_GRAMMAR
print('GrammarCoverageFuzzer: {}'.format(0)) # print the average code coverage for GrammarCoverageFuzzer + RE_GRAMMAR
print('GrammarCoverageFuzzer+: {}'.format(0)) # print the average code coverage for GrammarCoverageFuzzer + RE_GRAMMAR_EXPANDED
