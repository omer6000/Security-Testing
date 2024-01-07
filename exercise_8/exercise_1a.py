from fuzzingbook.Fuzzer import RandomFuzzer
from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from fuzzingbook.MutationFuzzer import MutationFuzzer
from fuzzingbook.GreyboxFuzzer import GreyboxFuzzer, PowerSchedule, Mutator
from fuzzingbook.GreyboxGrammarFuzzer import LangFuzzer, GreyboxGrammarFuzzer, FragmentMutator, AFLSmartSchedule, RegionMutator
from fuzzingbook.Parser import EarleyParser


def get_random_fuzzer() -> RandomFuzzer:
    return RandomFuzzer()


def get_grammar_fuzzer(grammar) -> GrammarFuzzer:
    return GrammarFuzzer(grammar)


def get_mutation_fuzzer(seeds) -> MutationFuzzer:
    return MutationFuzzer(seed=seeds)


def get_greybox_fuzzer(seeds) -> GreyboxFuzzer:
    return GreyboxFuzzer(seeds=seeds,mutator=Mutator(),schedule=PowerSchedule())


def get_lang_fuzzer(seeds, grammar) -> LangFuzzer:
    mutator = FragmentMutator(EarleyParser(grammar))
    schedule = PowerSchedule()
    return LangFuzzer(seeds, mutator, schedule)



def get_greybox_grammar_fuzzer(seeds, grammar) -> GreyboxGrammarFuzzer:
    parser = EarleyParser(grammar)
    byte_mutator = Mutator()
    tree_mutator = RegionMutator(parser)
    schedule = AFLSmartSchedule(parser)
    return GreyboxGrammarFuzzer(seeds, byte_mutator, tree_mutator, schedule)
