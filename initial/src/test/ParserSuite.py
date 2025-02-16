import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_if_statement(self):
        """Test if statement with else and else if clauses."""
        input = """
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset();
            SayHello(name string);
        };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))
    