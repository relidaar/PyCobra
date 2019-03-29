from unittest import TestCase

from interpreter_module.lexer import lexer


class TestLexerIfElse(TestCase):
    def test_tokenize_if(self):
        input_text = 'if a < b { print True }'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'IF IDENTIFIER LT IDENTIFIER LBRACE PRINT BOOLEAN RBRACE'

        self.assertEqual(tokens_result, result)

    def test_tokenize_if_else(self):
        input_text = 'if a < b { print True } else { print True }'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'IF IDENTIFIER LT IDENTIFIER LBRACE PRINT BOOLEAN RBRACE ELSE LBRACE PRINT BOOLEAN RBRACE'

        self.assertEqual(tokens_result, result)
