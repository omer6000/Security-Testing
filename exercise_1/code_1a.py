from exercise_1 import levenshtein_distance
from fuzzingbook.Fuzzer import fuzzer
import random

while True:
    try:
        len1 = random.randrange(0,10)
        len2 = random.randrange(0,10)
        str1 = fuzzer(len1, ord('a'), 26)
        str2 = fuzzer(len2, ord('a'), 26)
        levenshtein_distance(str1,str2)
    except IndexError:
        with open('1a_inputs.txt','w') as f:
            f.write(f'str1: {str1}\nstr2: {str2}')
        break
    except: 
        continue