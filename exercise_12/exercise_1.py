from fuzzingbook.Grammars import Grammar, crange, is_valid_grammar, opts
from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from fuzzingbook.ProbabilisticGrammarFuzzer import ProbabilisticGrammarFuzzer
from fuzzingbook.GeneratorGrammarFuzzer import GeneratorGrammarFuzzer, ProbabilisticGeneratorGrammarCoverageFuzzer
from fuzzingbook.WebFuzzer import WebFormFuzzer, HTMLGrammarMiner, cgi_encode

def find_bugs(registration):
    reg_list = registration.split("&")
    if reg_list[3] == 'password=':
        reg_list[4] = 'password2='
    if reg_list[3] == 'password=aaaaaaaaaaaaaaaaaa@':
        reg_list[4] = 'password2=aaaaaaaaaaaaaaaaaa@'
    return "&".join(reg_list)

REGISTRATION_GRAMMAR: Grammar = {
    "<start>": [("<registration>",opts(post=lambda registration: find_bugs(registration)))],
    "<registration>": ["/register?name=<name>&lastname=<lastname>&email=<email>"
                       "&password=<password>&password2=<password2>&banking=<banking>"],
    "<name>": ["omer123",("omer",opts(prob=0.8))],
    "<lastname>": ["iqbal123",("iqbal",opts(prob=0.8))],
    "<email>": [cgi_encode("omer@cispa.abcdefg"), 
                (cgi_encode("omer@cispa.de"),opts(prob=0.8))],
    "<password>": ["aaaaaaaaaaaaaaaaaa@","acbd123",("pass@",opts(prob=0.65)),""],
    "<password2>": ["pass@"],
    "<banking>": ["18"],
}

assert is_valid_grammar(REGISTRATION_GRAMMAR)

def get_fuzzer(httpd_url):
    return ProbabilisticGeneratorGrammarCoverageFuzzer(REGISTRATION_GRAMMAR)