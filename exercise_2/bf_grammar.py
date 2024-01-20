from fuzzingbook.GrammarFuzzer import GrammarFuzzer
BFGRAMMAR = {
    "<start>":  ["<expr>"],
    "<expr>": ["<expr><expr2><expr>","<expr2><expr><expr>","<expr><expr><expr2>","<expr2>"],
    "<expr2>": ["<left_bracket><expr><command><expr><right_bracket>","<command>"],
    "<command>": ["<left_angle>","<right_angle>","<plus>","<minus>","<dot>","<comma>"],
    "<left_angle>": ["<"],
    "<right_angle>": [">"],
    "<comma>": [","],
    "<dot>":["."],
    "<plus>": ["+"],
    "<minus>": ["-"],
    "<left_bracket>": ["["],
    "<right_bracket>": ["]"]

}
a = GrammarFuzzer()
print(a)