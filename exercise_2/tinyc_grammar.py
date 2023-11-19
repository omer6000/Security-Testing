TINYCGRAMMAR = {
    "<start>":  ["<statement>"],
    "<statement>" : ["if <paren_expr> <statement>",
                     "if <paren_expr> <statement> else <statement>",
                     "while <paren_expr> <statement>","do <statement> while <paren_expr> <semicolon>",
                     "<curlybracket_left> <statement><asterisk> <curlybracket_right>",
                     "<expr> <semicolon>",
                     "<semicolon>"],
    "<paren_expr>" : ["( <expr> )"],
    "<expr>" : ["<test>","<id> <equal> <expr>"],
    "<test>" : ["<sum>","<sum> <less> <sum>"],
    "<sum>" : ["<term>","<sum> + <term>", "<sum> - <term>"],
    "<term>": ["<id>","<int>","<paren_expr>"],
    "<id>": ["/[a-z]+/"],
    "<int>": ["/[-+]?(\d*\.\d+|\d+\.\d*)([eE][-+]?\d+)?/"],
    "<semicolon>" : [";"],
    "<asterisk>": ["*"],
    "<curlybracket_left>": "{",
    "<curlybracket_right>": "}",
    "<less>" : "<",
    "<equal>": "="

    
}

from fuzzingbook.Grammars import simple_grammar_fuzzer

a = simple_grammar_fuzzer(TINYCGRAMMAR)
print(a)

#                 "{" <statement>* "}" |
#                 <expr> ";" |
#                 ";"
# <paren_expr> ::= "(" <expr> ")"
# <expr> ::= <test> | <id> "=" <expr>
# <test> ::= <sum> | <sum> "<" <sum>
# <sum> ::= <term> | <sum> "+" <term> | <sum> "-" <term>
# <term> ::= <id> | <int> | <paren_expr>
# <id> ::= "a" | "b" | "c" | "d" | ... | "z"
# <int> ::= <an_unsigned_decimal_integer>