"""
Use this file to implement your solution for exercise 5-1 b.
"""
from fuzzingbook.Fuzzer import RandomFuzzer
from exercise_2a import FunctionCoverageRunner
import html


class RandomCoverageFuzzer(RandomFuzzer):
    
    def runs(self, runner: FunctionCoverageRunner):
        iterations = 0
        coverage_set = set()
        results = []
        while iterations < 10:
            iter_res = self.run(runner)
            coverage =  runner.coverage
            results.append(iter_res)
            if coverage_set.intersection(coverage) == coverage: # No change
                iterations += 1
            else: # New coverage
                coverage_set.update(coverage)
                iterations = 0
        return results


if __name__ == '__main__':
    fuzzer = RandomCoverageFuzzer()
    print(fuzzer.runs(FunctionCoverageRunner(html.escape)))
