from unittest import TestCase
from interpreter.lexer import lexer
from interpreter.myparser import parser


class TestLexerCalculation(TestCase):
    def test_tokenize_plus(self):
        # FOR TWO INTEGERS
        text_input = '1 + 1'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER PLUS INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR TWO FLOATS
        text_input = '1.5 + 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT PLUS FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH FLOAT AND INTEGER
        text_input = '1 + 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER PLUS FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR TWO STRINGS
        text_input = '"Some text " + "and another text"'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'STRING PLUS STRING'

        self.assertEqual(tokens_result, result)

        # FOR BOTH STRING AND INTEGER
        text_input = '"Some text " + 1'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'STRING PLUS INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR BOTH STRING AND FLOAT
        text_input = '"Some text " + 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'STRING PLUS FLOAT'

        self.assertEqual(tokens_result, result)

    def test_tokenize_minus(self):
        # FOR TWO INTEGERS
        text_input = '1 - 1'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MINUS INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR TWO FLOATS
        text_input = '1.5 - 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT MINUS FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH FLOAT AND INTEGER
        text_input = '1 - 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MINUS FLOAT'

        self.assertEqual(tokens_result, result)

    def test_tokenize_mul(self):
        # FOR TWO INTEGERS
        text_input = '1 * 1'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MUL INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR TWO FLOATS
        text_input = '1.5 * 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT MUL FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH FLOAT AND INTEGER
        text_input = '1 * 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MUL FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH STRING AND INTEGER
        text_input = '"Some text" * 1'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'STRING MUL INTEGER'

        self.assertEqual(tokens_result, result)

    def test_tokenize_div(self):
        # FOR TWO INTEGERS
        text_input = '1 / 1'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER DIV INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR TWO FLOATS
        text_input = '1.5 / 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT DIV FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH FLOAT AND INTEGER
        text_input = '1 / 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER DIV FLOAT'

        self.assertEqual(tokens_result, result)

    def test_tokenize_mod(self):
        # FOR TWO INTEGERS
        text_input = '1 % 1'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MOD INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR TWO FLOATS
        text_input = '1.5 % 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT MOD FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH FLOAT AND INTEGER
        text_input = '1 % 1.5'
        tokens = list(lexer.lex(text_input))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER MOD FLOAT'

        self.assertEqual(tokens_result, result)