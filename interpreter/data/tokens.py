token_dict = {
    # OPERATORS
    'PRINTLN': r'println',
    'PRINT': r'print',
    'IF': r'if',
    'ELSE': r'else',
    'WHILE': r'while',
    'FOR': r'for',

    # TYPES
    'FLOAT': r'\d+\.\d+|\-\d+\.\d+',
    'INTEGER': r'\d+|-\d+',
    'BOOLEAN': r'True|False',
    'STRING': r'\".*?\"',

    # CALCULATION
    'PLUS': r'\+',
    'MINUS': r'\-',
    'MUL': r'\*',
    'DIV': r'\/',
    'MOD': r'\%',

    # BOOLEAN OPERATIONS
    'EQ': r'==',
    'LTEQ': r'<=',
    'GTEQ': r'>=',
    'LT': r'<',
    'GT': r'>',
    'NOT': r'not',
    'AND': r'and',
    'OR': r'or',

    # VARIABLES
    'ASSIGNMENT': r'=',
    'IDENTIFIER': r'\w+',

    # BRACKETS
    'LBRACE': r'\{',
    'RBRACE': r'\}',
    'LPAREN': r'\(',
    'RPAREN': r'\)',

    # SYMBOLS
    'SEMICOLON': r';',
}

if __name__ == '__main__':
    for key, value in token_dict.items():
        print('{}: {}'.format(key, value))
