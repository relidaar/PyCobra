from unittest import TestCase

from interpreter_module.lexer import lexer


class TestLexerVariables(TestCase):
    def test_tokenize_variable(self):
        # FOR INTEGER
        input_text = 'num1 = 1'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'IDENTIFIER ASSIGNMENT INTEGER'

        self.assertEqual(tokens_result, result)

        # FOR FLOAT
        input_text = 'num1 = 1.5'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'IDENTIFIER ASSIGNMENT FLOAT'

        self.assertEqual(tokens_result, result)

        # FOR STRING
        input_text = 'num1 = "text"'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'IDENTIFIER ASSIGNMENT STRING'

        self.assertEqual(tokens_result, result)

        # FOR BOOLEAN
        input_text = 'num1 = True'
        tokens = list(lexer.lex(input_text))

        tokens_result = ' '.join(token.gettokentype() for token in tokens)
        result = 'IDENTIFIER ASSIGNMENT BOOLEAN'

        self.assertEqual(tokens_result, result)
