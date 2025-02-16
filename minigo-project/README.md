# MiniGo Project

## Overview
MiniGo is a programming language designed for educational purposes, focusing on simplicity and ease of understanding. This project includes a lexer and parser defined in ANTLR, allowing for the detection of tokens and grammar rules specific to MiniGo programs.

## Files
- **src/main/minigo/parser/MiniGo.g4**: This file defines the grammar and lexer rules for the MiniGo programming language. It includes token definitions for keywords, literals, identifiers, and error handling for unrecognized characters, unclosed strings, and illegal escape sequences.

- **test/LexerSuite.py**: This file contains 100 test cases designed to test the lexer rules defined in MiniGo.g4. It implements specific exception handling for lexical errors, throwing `ErrorToken` for unrecognized characters, `UnclosedString` for unterminated strings, and `IllegalEscapeInString` for illegal escape sequences.

- **test/ParserSuite.py**: This file contains 100 test cases to test the grammar rules defined in MiniGo.g4. Each test case is designed to check the parsing of valid and invalid MiniGo programs, assuming that there is at most one error in each test case.

- **requirements.txt**: This file lists the dependencies required for the project, including any libraries needed for testing and parsing.

## Running Tests
To run the tests for the MiniGo project, follow these steps:

1. Ensure you have Python installed on your machine.
2. Install the required dependencies listed in `requirements.txt` by running:
   ```
   pip install -r requirements.txt
   ```
3. Navigate to the `test` directory and run the test suites:
   ```
   python LexerSuite.py
   python ParserSuite.py
   ```

## Conclusion
This project serves as a foundation for understanding the principles of language design and implementation. The MiniGo language, along with its lexer and parser, provides a practical example of how programming languages can be constructed and tested.