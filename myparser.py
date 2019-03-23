from rply import ParserGenerator

from ast import Program, Integer, Float, String, Boolean
from lexer import lexer
from tokens import token_dict

pg = ParserGenerator(
    token_dict.keys()
)


@pg.production('program : expressions')
def program(p):
    return Program(p[0])


@pg.production('expressions : expression')
def get_expression(p):
    return [p[0]]


@pg.production('expressions : expressions expression')
def add_expression(p):
    return p[0] + [p[1]]


@pg.production('expression : INTEGER')
def integer(p):
    return Integer(p[0].value)


@pg.production('expression : FLOAT')
def integer(p):
    return Float(p[0].value)


@pg.production('expression : STRING')
def integer(p):
    return String(p[0].value)


@pg.production('expression : BOOLEAN')
def integer(p):
    return Boolean(p[0].value)


parser = pg.build()

if __name__ == '__main__':
    filename = 'test.cb'
    with open(filename) as f:
        text_input = f.read()

    tokens = lexer.lex(text_input)
    parser.parse(tokens).eval()
