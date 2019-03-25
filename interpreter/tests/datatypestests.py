from unittest import TestCase
from interpreter.lexer import lexer
from interpreter.myparser import parser


class TestLexerDataTypes(TestCase):
    def test_tokenize_integer(self):
        tokens = lexer.lex('1 -1 0')
        for token in tokens:
            self.assertEqual(token.gettokentype(), 'INTEGER')

    def test_tokenize_float(self):
        tokens = lexer.lex('1.5 -1.5')
        for token in tokens:
            self.assertEqual(token.gettokentype(), 'FLOAT')

    def test_tokenize_string(self):
        tokens = lexer.lex('"" "Full string"')
        for token in tokens:
            self.assertEqual(token.gettokentype(), 'STRING')

    def test_tokenize_boolean(self):
        tokens = lexer.lex('True False')
        for token in tokens:
            self.assertEqual(token.gettokentype(), 'BOOLEAN')


class TestParserDataTypes(TestCase):
    def test_parse_integer(self):
        tokens = lexer.lex('1')
        self.assertEqual(parser.parse(tokens).eval_test(), 1)

        tokens = lexer.lex('-1')
        self.assertEqual(parser.parse(tokens).eval_test(), -1)

        tokens = lexer.lex('0')
        self.assertEqual(parser.parse(tokens).eval_test(), 0)

    def test_parse_float(self):
        tokens = lexer.lex('1.5')
        self.assertEqual(parser.parse(tokens).eval_test(), 1.5)

        tokens = lexer.lex('-1.5')
        self.assertEqual(parser.parse(tokens).eval_test(), -1.5)

    def test_parse_string(self):
        tokens = lexer.lex('""')
        self.assertEqual(parser.parse(tokens).eval_test(), '')

        tokens = lexer.lex('"Full string"')
        self.assertEqual(parser.parse(tokens).eval_test(), 'Full string')

    def test_parse_boolean(self):
        tokens = lexer.lex('True')
        self.assertEqual(parser.parse(tokens).eval_test(), True)

        tokens = lexer.lex('False')
        self.assertEqual(parser.parse(tokens).eval_test(), False)
