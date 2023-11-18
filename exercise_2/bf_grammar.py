from fuzzingbook.Grammars import simple_grammar_fuzzer, US_PHONE_GRAMMAR, Grammar
# import random

BFGRAMMAR = {
    "<start>":  ["<expr>"],
    "<expr>": ["<expr> <expr2>  <expr> ","<expr2>  <expr>  <expr>","<expr> <expr> <expr2>", "<expr2>"],
    "<expr2>": ["[<expr> <command> <expr>]","<command>"],
    "<command>": [">","<","+","-",".",","]
}

# random.seed(20)
# a = simple_grammar_fuzzer(BFGRAMMAR)
# print(a)
# count = {}
# for c in a:
#     if c == " ":
#         continue
#     elif c in count:
#         count[c] += 1
#     else:
#         count[c] = 1
# print(count)
