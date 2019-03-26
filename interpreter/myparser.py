from rply import ParserGenerator

from interpreter.data import ast
from interpreter.data.tokens import token_dict

pg = ParserGenerator(
    token_dict.keys(),
    precedence=[
        ('left', ['PRINTLN', 'PRINT']),
        ('left', ['AND', 'OR']),
        ('left', ['EQ', 'NOT']),
        ('left', ['GT', 'GTEQ']),
        ('left', ['LT', 'LTEQ']),
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV', 'MOD'])
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


@pg.production('statement : IDENTIFIER ASSIGNMENT expression')
def assignment(p):
    return ast.Assignment(p[0].value, p[2])


@pg.production('expression : IDENTIFIER')
def get_variable(p):
    return ast.Variable(p[0].value)


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
        'PLUS': ast.Addition,
        'MINUS': ast.Subtraction,
        'MUL': ast.Multiplication,
        'DIV': ast.Division,
        'MOD': ast.Modulo,
    }

    return mapping[operator](left, right)


@pg.production('expression : expression EQ expression')
@pg.production('expression : expression LT expression')
@pg.production('expression : expression LTEQ expression')
@pg.production('expression : expression GT expression')
@pg.production('expression : expression GTEQ expression')
@pg.production('expression : expression NOT expression')
@pg.production('expression : expression AND expression')
@pg.production('expression : expression OR expression')
def calculate(p):
    operator = p[1].gettokentype()
    left = p[0]
    right = p[2]

    mapping = {
        'EQ': ast.Equals,
        'LT': ast.LessThan,
        'LTEQ': ast.LessThanOrEquals,
        'GT': ast.GreaterThan,
        'GTEQ': ast.GreaterThanOrEquals,
        'NOT': ast.NotEqual,
        'AND': ast.And,
        'OR': ast.Or,
    }

    return mapping[operator](left, right)


@pg.production('expression : INTEGER')
def get_integer(p):
    return ast.Integer(p[0].value)


@pg.production('expression : FLOAT')
def get_integer(p):
    return ast.Float(p[0].value)


@pg.production('expression : STRING')
def get_integer(p):
    return ast.String(p[0].value)


@pg.production('expression : BOOLEAN')
def get_integer(p):
    return ast.Boolean(p[0].value)


parser = pg.build()
