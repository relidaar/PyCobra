token_dict = {
    # TYPES
    'FLOAT': r'\d+\.\d+',
    'INTEGER': r'\d+',
    'BOOLEAN': r'True|False',
    'STRING': r'\".*?\"',

    # CALCULATION
    'PLUS': r'\+',
    'MINUS': r'\-',
    'MUL': r'\*',
    'DIV': r'\/',
    'MOD': r'\%',
}

if __name__ == '__main__':
    for key, value in token_dict.items():
        print('{}: {}'.format(key, value))
