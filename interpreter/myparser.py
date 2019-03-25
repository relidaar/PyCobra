from rply import ParserGenerator

from interpreter.data import ast
from interpreter.data.tokens import token_dict

pg = ParserGenerator(
    token_dict.keys(),
    precedence=[
        ('left', ['PRINTLN', 'PRINT']),
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV'])
    ]
)


@pg.production('program : statements')
def program(p):
    return ast.Program(p[0])


@pg.production('statements : statement')
def get_statement(p):
    return [p[0]]


@pg.production('statements : statements statement')
def add_statement(p):
    return p[0] + [p[1]]


@pg.production('statement : PRINTLN expression')
@pg.production('statement : PRINT expression')
def print_statement(p):
    value = p[1]
    operator = p[0].gettokentype()
    return ast.Print(value, True if operator == 'PRINTLN' else False)


@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MUL expression')
@pg.production('expression : expression DIV expression')
@pg.production('expression : expression MOD expression')
def calculate(p):
    operator = p[1].gettokentype()
    left = p[0]
    right = p[2]

    mapping = {
        'PLUS': ast.Add,
        'MINUS': ast.Subtract,
        'MUL': ast.Multiply,
        'DIV': ast.Divide,
        'MOD': ast.Modulo,
    }

    return mapping[operator](left, right)


@pg.production('expression : INTEGER')
def get_integer(p):
    return ast.Integer(p[0].value)


@pg.production('expression : FLOAT')
def get_float(p):
    return ast.Float(p[0].value)


@pg.production('expression : STRING')
def get_string(p):
    return ast.String(p[0].value)


@pg.production('expression : BOOLEAN')
def get_boolean(p):
    return ast.Boolean(p[0].value)


parser = pg.build()
