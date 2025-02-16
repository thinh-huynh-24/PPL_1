from lexererr import UncloseString, IllegalEscape, ErrorToken
import unittest
from antlr4 import *
from minigo.parser.MiniGoLexer import MiniGoLexer
from minigo.parser.MiniGoParser import MiniGoParser

class LexerSuite(unittest.TestCase):

    def setUp(self):
        self.lexer = None

    def runLexer(self, input_string):
        input_stream = InputStream(input_string)
        self.lexer = MiniGoLexer(input_stream)
        tokens = []
        while True:
            token = self.lexer.nextToken()
            if token.type == Token.EOF:
                break
            tokens.append(token)
        return tokens

    def test_valid_tokens(self):
        test_cases = [
            ("var x = 10;", [Token.VAR, Token.IDENTIFIER, Token.ASSIGN, Token.INTERGER_LITERAL, Token.SEMI]),
            ("if (x > 5) { return true; }", [Token.IF, Token.LPAREN, Token.IDENTIFIER, Token.GT, Token.INTERGER_LITERAL, Token.RBRACE, Token.RETURN, Token.TRUE, Token.SEMI, Token.RBRACE]),
            # Add more valid test cases here
        ]
        for input_string, expected_tokens in test_cases:
            with self.subTest(input_string=input_string):
                tokens = self.runLexer(input_string)
                self.assertEqual([token.type for token in tokens], expected_tokens)

    def test_unclosed_string(self):
        with self.assertRaises(UncloseString):
            self.runLexer('"This is an unclosed string')

    def test_illegal_escape(self):
        with self.assertRaises(IllegalEscape):
            self.runLexer('"This is an illegal escape: \\x"')

    def test_error_token(self):
        with self.assertRaises(ErrorToken):
            self.runLexer('var x = @;')  # Unrecognized character '@'

    # Add more tests for lexical errors and valid tokens

if __name__ == '__main__':
    unittest.main()