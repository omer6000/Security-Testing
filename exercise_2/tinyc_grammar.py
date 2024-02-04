TINYCGRAMMAR = {
    "<start>":  ["<statement>"],
    "<statement>" : ["if <paren_expr> <statement>",
                     "if <paren_expr> <statement> else <statement>",
                     "while <paren_expr> <statement>",
                     "do <statement> while <paren_expr> <semicolon>",
                     "<curlybracket_left> <curlybracket_left> <statement> <curlybracket_right> <curlybracket_right>",
                     "<expr> <semicolon>",
                     "<semicolon>"],
    "<paren_expr>" : ["<bracket_left> <expr> <bracket_right>"],
    "<expr>" : ["<test>","<id> <equal> <expr>"],
    "<test>" : ["<sum>","<sum> <less> <sum>"],
    "<sum>" : ["<term>","<sum> <plus> <term>", "<sum> <minus> <term>"],
    "<term>": ["<id>","<int>","<paren_expr>"],
    "<id>": [chr(i) for i in range(97, 123)],
    "<int>": ["<int><number>","<number>"],
    "<number>": [str(i) for i in range(10)],
    "<semicolon>" : [";"],
    "<curlybracket_left>": ["{"],
    "<curlybracket_right>": ["}"],
    "<less>" : ["<"],
    "<equal>": ["="],
    "<plus>": ["+"],
    "<minus>": ["-"],
    "<bracket_left>": ["("],
    "<bracket_right>": [")"]
}