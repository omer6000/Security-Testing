"""
Use this file to implement your solution for exercise 5-1 b.
"""

from exercise_1a import *
from fuzzingbook.Coverage import Location

def lcsaj_n(trace: list[Location], n: int) -> set[tuple[Location, ...]]:
    lcsaj_seq = sorted(list(lcsaj(trace)))
    # print(lcsaj_seq)
    # print(lcsaj_seq)
    length = len(lcsaj_seq)
    # print(length)
    output = set()
    if n > length:
        return output
    elif n == 1:
        for i in range(length):
            output.add(tuple([lcsaj_seq[i]]))
    else:
        seq = []
        for i in range(length):
            seq.append(lcsaj_seq[i])
            if len(seq) == n:
                output.add(tuple(seq))
                seq = [lcsaj_seq[i]]
    return output

# input = a = [('f', 2),('f', 3),('f', 5),('f', 6),('f', 8),]
# {((('f', 5), ('f', 6), ('f', 8)), (('f', 8),)), ((('f', 2), ('f', 3), ('f', 5)), (('f', 5), ('f', 6), ('f', 8)))}
# print(lcsaj_n(a,3))
# {
#    ((('f', 2), ('f', 3), ('f', 5)),),
#    ((('f', 5), ('f', 6), ('f', 8)),),
#    ((('f', 8),),)
# }
# {
#     ((('f', 5), ('f', 6), ('f', 8)),),
#     ((('f', 8),),),
#     ((('f', 2), ('f', 3), ('f', 5)),)}

# {((('f', 2), ('f', 3), ('f', 5)), (('f', 5), ('f', 6), ('f', 8)), (('f', 8),))}