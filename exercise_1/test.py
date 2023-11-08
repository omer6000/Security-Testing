from fuzzingbook.Fuzzer import Runner
from fuzzingbook.Fuzzer import RandomFuzzer
from fuzzingbook.Fuzzer import ProgramRunner
from fuzzingbook.Fuzzer import ProgramRunner
from fuzzingbook.Fuzzer import PrintRunner
import subprocess

randomfuzzer = RandomFuzzer()
runner = Runner()
print(runner.run("hello"))
# runner.run
# outcome = randomfuzzer.run(runner)
# print(outcome)
# for _ in range(100):
# runner = PrintRunner.__bases__
# print(runner)
    # programrunner = ProgramRunner(['a','v'])
    # randomfuzzer.run(programrunner)