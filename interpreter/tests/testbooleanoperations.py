from unittest import TestCase

from interpreter.lexer import lexer


class TestLexerVariables(TestCase):
    def test_tokenize_eq(self):
        # FOR INTEGERS
        input_text = '1 == 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER EQ INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR FLOATS
        input_text = '1.5 == 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT EQ FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH INTEGER AND FLOAT
        input_text = '1.5 == 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT EQ INTEGER'

        self.assertEqual(tokens_result, result)

    def test_tokenize_neq(self):
        # FOR INTEGERS
        input_text = '1 != 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER NEQ INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR FLOATS
        input_text = '1.5 != 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT NEQ FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH INTEGER AND FLOAT
        input_text = '1.5 != 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT NEQ INTEGER'

        self.assertEqual(tokens_result, result)

    def test_tokenize_lt(self):
        # FOR INTEGERS
        input_text = '1 < 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER LT INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR FLOATS
        input_text = '1.5 < 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT LT FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH INTEGER AND FLOAT
        input_text = '1.5 < 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT LT INTEGER'

        self.assertEqual(tokens_result, result)

    def test_tokenize_lteq(self):
        # FOR INTEGERS
        input_text = '1 <= 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER LTEQ INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR FLOATS
        input_text = '1.5 <= 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT LTEQ FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH INTEGER AND FLOAT
        input_text = '1.5 <= 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT LTEQ INTEGER'

        self.assertEqual(tokens_result, result)

    def test_tokenize_gt(self):
        # FOR INTEGERS
        input_text = '1 > 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER GT INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR FLOATS
        input_text = '1.5 > 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT GT FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH INTEGER AND FLOAT
        input_text = '1.5 > 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT GT INTEGER'

        self.assertEqual(tokens_result, result)

    def test_tokenize_gteq(self):
        # FOR INTEGERS
        input_text = '1 >= 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'INTEGER GTEQ INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR FLOATS
        input_text = '1.5 >= 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT GTEQ FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR BOTH INTEGER AND FLOAT
        input_text = '1.5 >= 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FLOAT GTEQ INTEGER'

        self.assertEqual(tokens_result, result)
