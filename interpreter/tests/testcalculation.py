from unittest import TestCase

from interpreter.lexer import lexer


class TestLexerCalculation(TestCase):
    def test_tokenize_plus(self):
        # FOR TWO INTEGERS
        input_text = '1 + 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER PLUS INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR TWO FLOATS
        input_text = '1.5 + 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT PLUS FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH FLOAT AND INTEGER
        input_text = '1 + 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER PLUS FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR TWO STRINGS
        input_text = '"Some text " + "and another text"'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'STRING PLUS STRING'

        self.assertEqual(tokens_result, result)

        # FOR BOTH STRING AND INTEGER
        input_text = '"Some text " + 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'STRING PLUS INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR BOTH STRING AND FLOAT
        input_text = '"Some text " + 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'STRING PLUS FLOAT'

        self.assertEqual(tokens_result, result)

    def test_tokenize_minus(self):
        # FOR TWO INTEGERS
        input_text = '1 - 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MINUS INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR TWO FLOATS
        input_text = '1.5 - 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT MINUS FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH FLOAT AND INTEGER
        input_text = '1 - 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MINUS FLOAT'

        self.assertEqual(tokens_result, result)

    def test_tokenize_mul(self):
        # FOR TWO INTEGERS
        input_text = '1 * 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MUL INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR TWO FLOATS
        input_text = '1.5 * 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT MUL FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH FLOAT AND INTEGER
        input_text = '1 * 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MUL FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH STRING AND INTEGER
        input_text = '"Some text" * 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'STRING MUL INTEGER'

        self.assertEqual(tokens_result, result)

    def test_tokenize_div(self):
        # FOR TWO INTEGERS
        input_text = '1 / 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER DIV INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR TWO FLOATS
        input_text = '1.5 / 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT DIV FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH FLOAT AND INTEGER
        input_text = '1 / 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER DIV FLOAT'

        self.assertEqual(tokens_result, result)

    def test_tokenize_mod(self):
        # FOR TWO INTEGERS
        input_text = '1 % 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MOD INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR TWO FLOATS
        input_text = '1.5 % 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT MOD FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH FLOAT AND INTEGER
        input_text = '1 % 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MOD FLOAT'

        self.assertEqual(tokens_result, result)
