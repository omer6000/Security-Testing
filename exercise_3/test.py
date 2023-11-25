from fuzzingbook.GrammarFuzzer import display_tree, GrammarFuzzer
from fuzzingbook.Grammars import US_PHONE_GRAMMAR

area_fuzzer = GrammarFuzzer(US_PHONE_GRAMMAR, start_symbol='<area>')