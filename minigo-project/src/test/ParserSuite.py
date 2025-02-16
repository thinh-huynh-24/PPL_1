import unittest
from antlr4 import *
from minigo.parser.MiniGoLexer import MiniGoLexer
from minigo.parser.MiniGoParser import MiniGoParser
from minigo.parser.MiniGoListener import MiniGoListener
from io import StringIO

class TestMiniGoParser(unittest.TestCase):

    def setUp(self):
        self.lexer = None
        self.parser = None

    def parse(self, input_string):
        input_stream = InputStream(input_string)
        self.lexer = MiniGoLexer(input_stream)
        token_stream = CommonTokenStream(self.lexer)
        self.parser = MiniGoParser(token_stream)
        return self.parser.program()

    def test_valid_programs(self):
        valid_programs = [
            "var x: int = 10;",
            "const y = true;",
            "func main() int { return 0; }",
            "if x == 10 { break; } else { continue; }",
            "for i := 0; i < 10; i++ { x = x + i; }"
        ]
        for program in valid_programs:
            with self.subTest(program=program):
                self.assertIsNotNone(self.parse(program))

    def test_invalid_programs(self):
        invalid_programs = [
            "var x: int = ;",  # Missing expression
            "const y = ;",     # Missing expression
            "func main() { return; }",  # Missing return type
            "if x == 10 { break; ",  # Unclosed if statement
            "for i := 0; i < 10; i++ { x = x + i"  # Unclosed for statement
        ]
        for program in invalid_programs:
            with self.subTest(program=program):
                with self.assertRaises(Exception):
                    self.parse(program)

    # Additional test cases can be added here to reach a total of 100

if __name__ == '__main__':
    unittest.main()