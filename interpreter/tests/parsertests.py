from unittest import TestCase
from interpreter.lexer import lexer
from interpreter.myparser import parser


class TestParserDataTypes(TestCase):
    def test_parse_integer(self):
        positive_integer = '5'
        positive_integer_result = lexer.lex(positive_integer)
        self.assertEqual(parser.parse(positive_integer_result).eval_test(), 5)

        negative_integer = '-5'
        negative_integer_result = lexer.lex(negative_integer)
        self.assertEqual(parser.parse(negative_integer_result).eval_test(), -5)

        zero = '0'
        zero_result = lexer.lex(zero)
        self.assertEqual(parser.parse(zero_result).eval_test(), 0)

    def test_parse_float(self):
        positive_float = '5.5'
        positive_float_result = lexer.lex(positive_float)
        self.assertEqual(parser.parse(positive_float_result).eval_test(), 5.5)

        negative_float = '-5.5'
        negative_float_result = lexer.lex(negative_float)
        self.assertEqual(parser.parse(negative_float_result).eval_test(), -5.5)

    def test_parse_string(self):
        empty_string = '""'
        empty_string_result = lexer.lex(empty_string)
        self.assertEqual(parser.parse(empty_string_result).eval_test(), '')

        full_string = '"Full string"'
        full_string_result = lexer.lex(full_string)
        self.assertEqual(parser.parse(full_string_result).eval_test(), 'Full string')

    def test_parse_boolean(self):
        false_boolean = 'False'
        false_boolean_result = lexer.lex(false_boolean)
        self.assertEqual(parser.parse(false_boolean_result).eval_test(), False)

        true_boolean = 'True'
        true_boolean_result = lexer.lex(true_boolean)
        self.assertEqual(parser.parse(true_boolean_result).eval_test(), True)
