from unittest import TestCase

from interpreter_module.lexer import lexer


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
