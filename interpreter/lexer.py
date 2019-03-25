from rply import LexerGenerator

from interpreter.data.tokens import token_dict

lg = LexerGenerator()

for key, value in token_dict.items():
    lg.add(key, value)

lg.ignore(r'\s+')
lg.ignore(r'\n')
lg.ignore(r'\#.*?\n')

lexer = lg.build()
