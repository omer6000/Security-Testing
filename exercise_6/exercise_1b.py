"""
Use this file to implement your solution for exercise 6-1 b.
"""

from exercise_1a import *
from fuzzingbook.Grammars import simple_grammar_fuzzer

def generalize(g: dict, cnt_inputs: int) -> dict:
    for key in g:
        rule_set = set(g[key]) #distinct rules
        if len(rule_set) < cnt_inputs/2:
            continue
		
		# Checking if a non terminal is present. 
        # Also checking if all rules defined produce digits
        # Also checking if all rules defined produce letters
        
        non_terminal = False
        isdigit = True
        ischar = True
        for rule in g[key]:
            if rule.find("<") != -1 and rule.find(">") != -1:
                non_terminal = True
            if rule.isdigit() == False:
                isdigit = False
            if rule.isalpha() == False:
                ischar = False
        if non_terminal:
            continue
        if isdigit:
            g[key] = [key+'<digit>','<digit>']
        if ischar:
            g[key] = [key+'<letter>','<letter>']

    g['<digit>'] = [str(i) for i in range(10)]
    g['<letter>'] = [chr(i) for i in range(ord('A'),ord('Z')+1)] + [chr(i) for i in range(ord('a'),ord('z')+1)]
    return g



# g = generalize(mine_student_grammar(),len(INPS))
# for _ in range(10):
# 	print(simple_grammar_fuzzer(g))