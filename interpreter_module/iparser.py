from rply import ParserGenerator

from interpreter_module import ast
from lexer_module.tokens import token_dict

pg = ParserGenerator(
    token_dict.keys(),
    precedence=[
        ('left', ['ASSIGNMENT']),
        ('left', ['WHILE', 'FOR']),
        ('left', ['IF', 'ELSE']),
        ('left', ['AND', 'OR']),
        ('left', ['EQ', 'NOT']),
        ('left', ['GT', 'GTEQ']),
        ('left', ['LT', 'LTEQ']),
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV', 'MOD']),
        ('left', ['LPAREN', 'RPAREN']),
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


@pg.production('statement : IF expression LBRACE statements RBRACE')
def if_statement(p):
    return ast.IfStatement(p[1], p[3], None)


@pg.production('statement : IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACE')
def if_else_statement(p):
    return ast.IfStatement(p[1], p[3], p[7])


@pg.production('statement : IDENTIFIER ASSIGNMENT expression IF expression ELSE expression')
def if_else_statement(p):
    return ast.Assignment(p[0].value, ast.TernaryStatement(p[2], p[4], p[6]))


@pg.production('statement : WHILE expression LBRACE statements RBRACE')
def if_statement(p):
    return ast.WhileStatement(p[1], p[3])


@pg.production('statement : FOR statement SEMICOLON expression SEMICOLON statement LBRACE statements RBRACE')
def if_statement(p):
    return ast.ForStatement(p[1], p[3], p[5], p[7])


@pg.production('expression : LPAREN expression RPAREN')
def factor_parens(p):
    return p[1]


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
