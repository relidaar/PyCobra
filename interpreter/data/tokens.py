token_dict = {
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
    'NEQ': r'!=',
    'LTEQ': r'<=',
    'GTEQ': r'>=',
    'LT': r'<',
    'GT': r'>',

    # OPERATORS
    'PRINTLN': r'println',
    'PRINT': r'print',

    # VARIABLES
    'ASSIGNMENT': r'=',
    'IDENTIFIER': r'\w+',
}

if __name__ == '__main__':
    for key, value in token_dict.items():
        print('{}: {}'.format(key, value))
