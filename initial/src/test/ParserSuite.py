import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_if_statement(self):
        """Test if statement with else and else if clauses."""
        input = """
        func main() {
            if (x > 10) {
                println("x is greater than 10");
            } else if (x == 10) {
                println("x is equal to 10");
            } else {
                println("x is less than 10");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))
    