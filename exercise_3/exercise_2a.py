"""
Use this file to implement your solution for exercise 3-2 a.
"""

# RE_GRAMMAR_EXPANDED = {
#     '<start>': ['<alternative>', '^<alternative-1>', '<alternative-2>$', '^<alternative-3>$'],
#     '<alternative>': ['<concat>', '<concat>|<alternative>'],
#     '<alternative-1>': ['<concat-1>', '<concat-1>|<alternative-1>'],
#     '<alternative-2>': ['<concat-2>', '<concat-2>|<alternative-2>'],
#     '<alternative-3>': ['<concat-3>', '<concat-3>|<alternative-3>'],
#     '<concat>': ['', '<concat><regex>'],
#     '<concat-1>': ['', '<concat-1><regex-1>'],
#     '<concat-2>': ['', '<concat-2><regex>'],
#     '<concat-3>': ['', '<concat-3><regex>'],

#     '<regex>': ['<symbol>', '<symbol>*', '<symbol>+', '<symbol>?', '<symbol>{<range>}'],
#     '<symbol>': ['.', '<char>', '(<alternative>)'],
#     '<char>': ['a', 'b', 'c'],
#     '<range>': ['<num>', ',<num>'],
#     '<num>': ['1', '2'],
# }
RE_GRAMMAR_EXPANDED = {
    "<start>": [
        "<alternative-1>",
        "^<alternative-2>",
        "<alternative-3>$",
        "^<alternative-4>$"
    ],
    "<alternative-1>": [
        "<concat-1>",
        "<concat-2>|<alternative-1>"
    ],
    "<concat-1>": [
        "",
        "<concat-1><regex-1>"
    ],
    "<regex-1>": [
        "<symbol-1>",
        "<symbol-2>*",
        "<symbol-3>+",
        "<symbol-4>?",
        "<symbol-5>{<range-1>}"
    ],
    "<symbol-1>": [
        ".",
        "<char-1>",
        "(<alternative-1>)"
    ],
    "<char-1>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-2>": [
        ".",
        "<char-2>",
        "(<alternative-1>)"
    ],
    "<char-2>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-3>": [
        ".",
        "<char-3>",
        "(<alternative-1>)"
    ],
    "<char-3>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-4>": [
        ".",
        "<char-4>",
        "(<alternative-1>)"
    ],
    "<char-4>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-5>": [
        ".",
        "<char-5>",
        "(<alternative-1>)"
    ],
    "<char-5>": [
        "a",
        "b",
        "c"
    ],
    "<range-1>": [
        "<num-1>",
        ",<num-2>"
    ],
    "<num-1>": [
        "1",
        "2"
    ],
    "<num-2>": [
        "1",
        "2"
    ],
    "<concat-2>": [
        "",
        "<concat-2><regex-2>"
    ],
    "<regex-2>": [
        "<symbol-6>",
        "<symbol-7>*",
        "<symbol-8>+",
        "<symbol-9>?",
        "<symbol-10>{<range-2>}"
    ],
    "<symbol-6>": [
        ".",
        "<char-6>",
        "(<alternative-1>)"
    ],
    "<char-6>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-7>": [
        ".",
        "<char-7>",
        "(<alternative-1>)"
    ],
    "<char-7>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-8>": [
        ".",
        "<char-8>",
        "(<alternative-1>)"
    ],
    "<char-8>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-9>": [
        ".",
        "<char-9>",
        "(<alternative-1>)"
    ],
    "<char-9>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-10>": [
        ".",
        "<char-10>",
        "(<alternative-1>)"
    ],
    "<char-10>": [
        "a",
        "b",
        "c"
    ],
    "<range-2>": [
        "<num-3>",
        ",<num-4>"
    ],
    "<num-3>": [
        "1",
        "2"
    ],
    "<num-4>": [
        "1",
        "2"
    ],
    "<alternative-2>": [
        "<concat-3>",
        "<concat-4>|<alternative-2>"
    ],
    "<concat-3>": [
        "",
        "<concat-3><regex-3>"
    ],
    "<regex-3>": [
        "<symbol-11>",
        "<symbol-12>*",
        "<symbol-13>+",
        "<symbol-14>?",
        "<symbol-15>{<range-3>}"
    ],
    "<symbol-11>": [
        ".",
        "<char-11>",
        "(<alternative-2>)"
    ],
    "<char-11>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-12>": [
        ".",
        "<char-12>",
        "(<alternative-2>)"
    ],
    "<char-12>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-13>": [
        ".",
        "<char-13>",
        "(<alternative-2>)"
    ],
    "<char-13>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-14>": [
        ".",
        "<char-14>",
        "(<alternative-2>)"
    ],
    "<char-14>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-15>": [
        ".",
        "<char-15>",
        "(<alternative-2>)"
    ],
    "<char-15>": [
        "a",
        "b",
        "c"
    ],
    "<range-3>": [
        "<num-5>",
        ",<num-6>"
    ],
    "<num-5>": [
        "1",
        "2"
    ],
    "<num-6>": [
        "1",
        "2"
    ],
    "<concat-4>": [
        "",
        "<concat-4><regex-4>"
    ],
    "<regex-4>": [
        "<symbol-16>",
        "<symbol-17>*",
        "<symbol-18>+",
        "<symbol-19>?",
        "<symbol-20>{<range-4>}"
    ],
    "<symbol-16>": [
        ".",
        "<char-16>",
        "(<alternative-2>)"
    ],
    "<char-16>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-17>": [
        ".",
        "<char-17>",
        "(<alternative-2>)"
    ],
    "<char-17>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-18>": [
        ".",
        "<char-18>",
        "(<alternative-2>)"
    ],
    "<char-18>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-19>": [
        ".",
        "<char-19>",
        "(<alternative-2>)"
    ],
    "<char-19>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-20>": [
        ".",
        "<char-20>",
        "(<alternative-2>)"
    ],
    "<char-20>": [
        "a",
        "b",
        "c"
    ],
    "<range-4>": [
        "<num-7>",
        ",<num-8>"
    ],
    "<num-7>": [
        "1",
        "2"
    ],
    "<num-8>": [
        "1",
        "2"
    ],
    "<alternative-3>": [
        "<concat-5>",
        "<concat-6>|<alternative-3>"
    ],
    "<concat-5>": [
        "",
        "<concat-5><regex-5>"
    ],
    "<regex-5>": [
        "<symbol-21>",
        "<symbol-22>*",
        "<symbol-23>+",
        "<symbol-24>?",
        "<symbol-25>{<range-5>}"
    ],
    "<symbol-21>": [
        ".",
        "<char-21>",
        "(<alternative-3>)"
    ],
    "<char-21>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-22>": [
        ".",
        "<char-22>",
        "(<alternative-3>)"
    ],
    "<char-22>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-23>": [
        ".",
        "<char-23>",
        "(<alternative-3>)"
    ],
    "<char-23>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-24>": [
        ".",
        "<char-24>",
        "(<alternative-3>)"
    ],
    "<char-24>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-25>": [
        ".",
        "<char-25>",
        "(<alternative-3>)"
    ],
    "<char-25>": [
        "a",
        "b",
        "c"
    ],
    "<range-5>": [
        "<num-9>",
        ",<num-10>"
    ],
    "<num-9>": [
        "1",
        "2"
    ],
    "<num-10>": [
        "1",
        "2"
    ],
    "<concat-6>": [
        "",
        "<concat-6><regex-6>"
    ],
    "<regex-6>": [
        "<symbol-26>",
        "<symbol-27>*",
        "<symbol-28>+",
        "<symbol-29>?",
        "<symbol-30>{<range-6>}"
    ],
    "<symbol-26>": [
        ".",
        "<char-26>",
        "(<alternative-3>)"
    ],
    "<char-26>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-27>": [
        ".",
        "<char-27>",
        "(<alternative-3>)"
    ],
    "<char-27>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-28>": [
        ".",
        "<char-28>",
        "(<alternative-3>)"
    ],
    "<char-28>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-29>": [
        ".",
        "<char-29>",
        "(<alternative-3>)"
    ],
    "<char-29>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-30>": [
        ".",
        "<char-30>",
        "(<alternative-3>)"
    ],
    "<char-30>": [
        "a",
        "b",
        "c"
    ],
    "<range-6>": [
        "<num-11>",
        ",<num-12>"
    ],
    "<num-11>": [
        "1",
        "2"
    ],
    "<num-12>": [
        "1",
        "2"
    ],
    "<alternative-4>": [
        "<concat-7>",
        "<concat-8>|<alternative-4>"
    ],
    "<concat-7>": [
        "",
        "<concat-7><regex-7>"
    ],
    "<regex-7>": [
        "<symbol-31>",
        "<symbol-32>*",
        "<symbol-33>+",
        "<symbol-34>?",
        "<symbol-35>{<range-7>}"
    ],
    "<symbol-31>": [
        ".",
        "<char-31>",
        "(<alternative-4>)"
    ],
    "<char-31>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-32>": [
        ".",
        "<char-32>",
        "(<alternative-4>)"
    ],
    "<char-32>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-33>": [
        ".",
        "<char-33>",
        "(<alternative-4>)"
    ],
    "<char-33>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-34>": [
        ".",
        "<char-34>",
        "(<alternative-4>)"
    ],
    "<char-34>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-35>": [
        ".",
        "<char-35>",
        "(<alternative-4>)"
    ],
    "<char-35>": [
        "a",
        "b",
        "c"
    ],
    "<range-7>": [
        "<num-13>",
        ",<num-14>"
    ],
    "<num-13>": [
        "1",
        "2"
    ],
    "<num-14>": [
        "1",
        "2"
    ],
    "<concat-8>": [
        "",
        "<concat-8><regex-8>"
    ],
    "<regex-8>": [
        "<symbol-36>",
        "<symbol-37>*",
        "<symbol-38>+",
        "<symbol-39>?",
        "<symbol-40>{<range-8>}"
    ],
    "<symbol-36>": [
        ".",
        "<char-36>",
        "(<alternative-4>)"
    ],
    "<char-36>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-37>": [
        ".",
        "<char-37>",
        "(<alternative-4>)"
    ],
    "<char-37>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-38>": [
        ".",
        "<char-38>",
        "(<alternative-4>)"
    ],
    "<char-38>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-39>": [
        ".",
        "<char-39>",
        "(<alternative-4>)"
    ],
    "<char-39>": [
        "a",
        "b",
        "c"
    ],
    "<symbol-40>": [
        ".",
        "<char-40>",
        "(<alternative-4>)"
    ],
    "<char-40>": [
        "a",
        "b",
        "c"
    ],
    "<range-8>": [
        "<num-15>",
        ",<num-16>"
    ],
    "<num-15>": [
        "1",
        "2"
    ],
    "<num-16>": [
        "1",
        "2"
    ]
}