from unittest import TestCase

from interpreter.lexer import lexer


class TestLexerPrint(TestCase):
    def test_tokenize_print_integer(self):
        input_list = [
            'print 1',
            'print -1',
            'print 0',
        ]

        for input_text in input_list:
            tokens = list(lexer.lex(input_text))
            self.assertEqual(tokens[0].gettokentype(), 'PRINT')
            self.assertEqual(tokens[1].gettokentype(), 'INTEGER')

        input_list = [
            'println 1',
            'println -1',
            'println 0',
        ]

        for input_text in input_list:
            tokens = list(lexer.lex(input_text))
            self.assertEqual(tokens[0].gettokentype(), 'PRINTLN')
            self.assertEqual(tokens[1].gettokentype(), 'INTEGER')

    def test_tokenize_print_float(self):
        input_list = [
            'print 1.5',
            'print -1.5',
        ]

        for input_text in input_list:
            tokens = list(lexer.lex(input_text))
            self.assertEqual(tokens[0].gettokentype(), 'PRINT')
            self.assertEqual(tokens[1].gettokentype(), 'FLOAT')

        input_list = [
            'println 1.5',
            'println -1.5',
        ]

        for input_text in input_list:
            tokens = list(lexer.lex(input_text))
            self.assertEqual(tokens[0].gettokentype(), 'PRINTLN')
            self.assertEqual(tokens[1].gettokentype(), 'FLOAT')

    def test_tokenize_print_string(self):
        input_list = [
            'print ""',
            'print "Text"',
        ]

        for input_text in input_list:
            tokens = list(lexer.lex(input_text))
            self.assertEqual(tokens[0].gettokentype(), 'PRINT')
            self.assertEqual(tokens[1].gettokentype(), 'STRING')

        input_list = [
            'println ""',
            'println "Text"',
        ]

        for input_text in input_list:
            tokens = list(lexer.lex(input_text))
            self.assertEqual(tokens[0].gettokentype(), 'PRINTLN')
            self.assertEqual(tokens[1].gettokentype(), 'STRING')

    def test_tokenize_print_boolean(self):
        input_list = [
            'print True',
            'print False',
        ]

        for input_text in input_list:
            tokens = list(lexer.lex(input_text))
            self.assertEqual(tokens[0].gettokentype(), 'PRINT')
            self.assertEqual(tokens[1].gettokentype(), 'BOOLEAN')

        input_list = [
            'println True',
            'println False',
        ]

        for input_text in input_list:
            tokens = list(lexer.lex(input_text))
            self.assertEqual(tokens[0].gettokentype(), 'PRINTLN')
            self.assertEqual(tokens[1].gettokentype(), 'BOOLEAN')
