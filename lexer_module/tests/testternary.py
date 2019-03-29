from unittest import TestCase

from interpreter_module.lexer import lexer


class TestLexerTernary(TestCase):
    def test_tokenize_ternary(self):
        input_text = 'a = True if 1 < 2 else False'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'IDENTIFIER ASSIGNMENT BOOLEAN IF INTEGER LT INTEGER ELSE BOOLEAN'

        self.assertEqual(tokens_result, result)
