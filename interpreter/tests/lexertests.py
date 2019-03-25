from unittest import TestCase
from interpreter.lexer import lexer


class TestLexerDataTypes(TestCase):
    def test_tokenize_integer(self):
        positive_integer = '5'
        positive_integer_result = list(lexer.lex(positive_integer))[0]
        self.assertEqual(positive_integer_result.gettokentype(), 'INTEGER')

        negative_integer = '-5'
        negative_integer_result = list(lexer.lex(negative_integer))[0]
        self.assertEqual(negative_integer_result.gettokentype(), 'INTEGER')

        zero = '0'
        zero_result = list(lexer.lex(zero))[0]
        self.assertEqual(zero_result.gettokentype(), 'INTEGER')

    def test_tokenize_float(self):
        positive_float = '5.5'
        positive_float_result = list(lexer.lex(positive_float))[0]
        self.assertEqual(positive_float_result.gettokentype(), 'FLOAT')

        negative_float = '-5.5'
        negative_float_result = list(lexer.lex(negative_float))[0]
        self.assertEqual(negative_float_result.gettokentype(), 'FLOAT')

    def test_tokenize_string(self):
        empty_string = '""'
        empty_string_result = list(lexer.lex(empty_string))[0]
        self.assertEqual(empty_string_result.gettokentype(), 'STRING')

        full_string = '"Full string"'
        full_string_result = list(lexer.lex(full_string))[0]
        self.assertEqual(full_string_result.gettokentype(), 'STRING')

    def test_tokenize_boolean(self):
        false_boolean = 'False'
        false_boolean_result = list(lexer.lex(false_boolean))[0]
        self.assertEqual(false_boolean_result.gettokentype(), 'BOOLEAN')

        true_boolean = 'True'
        true_boolean_result = list(lexer.lex(true_boolean))[0]
        self.assertEqual(true_boolean_result.gettokentype(), 'BOOLEAN')


class TestLexerCalculation(TestCase):
    pass
