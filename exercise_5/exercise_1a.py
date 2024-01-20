"""
Use this file to implement your solution for exercise 5-1 a.
"""
from fuzzingbook.Coverage import Location


def lcsaj(trace: list[Location]) -> set[tuple[Location, ...]]:
    output = set()
    cov_element = []
    input_len = len(trace)
    for i in range(1,input_len):
        prev = trace[i-1]
        current = trace[i]
        if cov_element == []:
            cov_element.append(prev)
        if current[1] == prev[1] + 1 and current[0] == prev[0] and i != input_len - 1:
            cov_element.append(current)
        elif i == input_len - 1: #end of program
            cov_element.append(current)
            output.add(tuple(cov_element))
            output.add(tuple([current]))
        else:
            cov_element.append(current)
            output.add(tuple(cov_element))
            cov_element = [current]
    return output

# input = a = [('f', 2),('f', 3),('f', 5),('f', 6),('f', 8),]
# print(lcsaj(a))