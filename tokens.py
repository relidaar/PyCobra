token_dict = {
    # TYPES
    'FLOAT': r'\d+\.\d+',
    'INTEGER': r'\d+',
    'BOOLEAN': r'True|False',
    'STRING': r'\".*?\"',
}

if __name__ == '__main__':
    for key, value in token_dict.items():
        print('{}: {}'.format(key, value))
