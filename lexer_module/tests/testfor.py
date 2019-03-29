from unittest import TestCase

from interpreter_module.lexer import lexer


class TestLexerFor(TestCase):
    def test_tokenize_for_asc(self):
        input_text = 'for i = 0; i < 10; i = i + 1 { ' \
                     'print i ' \
                     '}'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FOR IDENTIFIER ASSIGNMENT INTEGER SEMICOLON ' \
                 'IDENTIFIER LT INTEGER SEMICOLON ' \
                 'IDENTIFIER ASSIGNMENT IDENTIFIER PLUS INTEGER LBRACE ' \
                 'PRINT IDENTIFIER ' \
                 'RBRACE'

        self.assertEqual(tokens_result, result)

    def test_tokenize_for_desc(self):
        input_text = 'for i = 10; i > 0; i = i - 1 { ' \
                     'print i ' \
                     '}'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'FOR IDENTIFIER ASSIGNMENT INTEGER SEMICOLON ' \
                 'IDENTIFIER GT INTEGER SEMICOLON ' \
                 'IDENTIFIER ASSIGNMENT IDENTIFIER MINUS INTEGER LBRACE ' \
                 'PRINT IDENTIFIER ' \
                 'RBRACE'

        self.assertEqual(tokens_result, result)
