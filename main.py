from lexer import lexer
from myparser import parser


def main():
    filename = 'test.cb'
    with open(filename) as f:
        text_input = f.read()

    tokens = lexer.lex(text_input)
    parser.parse(tokens).eval()


if __name__ == '__main__':
    main()
