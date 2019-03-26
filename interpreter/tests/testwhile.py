from unittest import TestCase

from interpreter.lexer import lexer


class TestLexerWhile(TestCase):
    def test_tokenize_while_asc(self):
        input_text = 'i = 0 ' \
                     'while i < 10 { ' \
                     'print i ' \
                     'i = i + 1' \
                     '}'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'IDENTIFIER ASSIGNMENT INTEGER ' \
                 'WHILE IDENTIFIER LT INTEGER LBRACE ' \
                 'PRINT IDENTIFIER ' \
                 'IDENTIFIER ASSIGNMENT IDENTIFIER PLUS INTEGER ' \
                 'RBRACE'

        self.assertEqual(tokens_result, result)

    def test_tokenize_while_desc(self):
        input_text = 'i = 10' \
                     'while i > 0 { ' \
                     'print i ' \
                     'i = i - 1' \
                     '}'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'IDENTIFIER ASSIGNMENT INTEGER ' \
                 'WHILE IDENTIFIER GT INTEGER LBRACE ' \
                 'PRINT IDENTIFIER ' \
                 'IDENTIFIER ASSIGNMENT IDENTIFIER MINUS INTEGER ' \
                 'RBRACE'

        self.assertEqual(tokens_result, result)
