from exercise_1 import levenshtein_distance
from fuzzingbook import Fuzzer

class FunctionRunner(Fuzzer.ProgramRunner):
    def __init__(self, program):
        super().__init__(program)
        self.outcome = ""
    
    def run_process(self,a,b):
        try:
            res = a(b)
            self.outcome = self.PASS
            return res
        except LookupError:
            self.outcome = self.FAIL
            return None
        except:
            self.outcome = self.UNRESOLVED
            return None
    def run(self,inp):
        return ((inp,self.run_process(self.program,inp)),self.outcome)



def ld_wrapper(inp):
    pass


def run():
    random_fuzzer = Fuzzer.RandomFuzzer()
    return random_fuzzer.runs(runner=FunctionRunner(ld_wrapper), trials=10)


if __name__ == '__main__':
    for result in run():
        print(result)    