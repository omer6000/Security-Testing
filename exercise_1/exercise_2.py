from exercise_1 import levenshtein_distance
from fuzzingbook import Fuzzer

class FunctionRunner(Fuzzer.ProgramRunner):
    pass


def ld_wrapper(inp):
    pass


def run():
    random_fuzzer = Fuzzer.RandomFuzzer()
    return random_fuzzer.runs(runner=FunctionRunner(ld_wrapper), trials=10)


if __name__ == '__main__':
    for result in run():
        print(result)
    