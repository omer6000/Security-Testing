from exercise_1 import levenshtein_distance
from fuzzingbook import Fuzzer

class FunctionRunner(Fuzzer.ProgramRunner): 
    def run_process(self,a,b):
        try:
            return (a(b),self.PASS)
        except LookupError:
            return (None, self.FAIL)
        except:
            return (None,self.UNRESOLVED)
    def run(self,inp):
        proc_outcome = self.run_process(self.program,inp)
        result = (inp,proc_outcome[0])
        outcome = proc_outcome[1]
        return (result,outcome)

def ld_wrapper(inp):
    split_inp = inp.split('+')
    n = len(split_inp)
    if n < 2:
        raise ValueError
    return levenshtein_distance(split_inp[0],split_inp[1])

def run():
    random_fuzzer = Fuzzer.RandomFuzzer(max_length=20)
    return random_fuzzer.runs(runner=FunctionRunner(ld_wrapper), trials=10)


if __name__ == '__main__':
    for result in run():
        print(result)    