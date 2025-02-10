import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_upper_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("ABC", "ABC,<EOF>", 102))

    def test_mixed_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("aBc123", "aBc123,<EOF>", 103))

    def test_identifier_with_underscore(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_abc", "_abc,<EOF>", 104))

    def test_identifier_start_with_underscore(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_abc123", "_abc123,<EOF>", 105))

    def test_identifier_with_digit(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc123", "abc123,<EOF>", 106))

    def test_identifier_with_digit_and_underscore(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc_123", "abc_123,<EOF>", 107))

    def test_invalid_identifier_start_with_digit(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("123abc", "123,abc,<EOF>", 108))

    def test_invalid_identifier_with_hyphen(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc-123", "abc,-,123,<EOF>", 109))

    def test_invalid_identifier_with_special_char(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc@123", "abc,ErrorToken(@),123,<EOF>", 110))

    def test_keyword_if(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 111))

    def test_keyword_else(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("else", "else,<EOF>", 112))

    def test_keyword_for(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("for", "for,<EOF>", 113))

    def test_keyword_return(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("return", "return,<EOF>", 114))

    def test_keyword_func(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("func", "func,<EOF>", 115))

    def test_keyword_type(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("type", "type,<EOF>", 116))

    def test_keyword_const(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("const", "const,<EOF>", 117))

    def test_keyword_var(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("var", "var,<EOF>", 118))

    def test_keyword_true(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 119))

    def test_keyword_false(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 120))

    def test_keyword_continue(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("continue", "continue,<EOF>", 121))

    def test_keyword_break(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("break", "break,<EOF>", 122))

    def test_keyword_range(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("range", "range,<EOF>", 123))

    def test_keyword_nil(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 124))

    def test_keyword_struct(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("struct", "struct,<EOF>", 125))

    def test_keyword_interface(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("interface", "interface,<EOF>", 126))

    def test_keyword_string(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("string", "string,<EOF>", 127))

    def test_keyword_int(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("int", "int,<EOF>", 128))

    def test_keyword_float(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("float", "float,<EOF>", 129))

    def test_keyword_boolean(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("boolean", "boolean,<EOF>", 130))

    def test_integer_literal_decimal(self):
        """test integer literals"""
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 131))

    def test_integer_literal_binary(self):
        """test integer literals"""
        self.assertTrue(TestLexer.checkLexeme("0b101", "0b101,<EOF>", 132))

    def test_integer_literal_octal(self):
        """test integer literals"""
        self.assertTrue(TestLexer.checkLexeme("0o12", "0o12,<EOF>", 133))

    def test_integer_literal_hexadecimal(self):
        """test integer literals"""
        self.assertTrue(TestLexer.checkLexeme("0x1A", "0x1A,<EOF>", 134))

    def test_integer_literal_invalid_binary(self):
        """test integer literals"""
        self.assertTrue(TestLexer.checkLexeme("0b102", "0b10,2,<EOF>", 135))

    def test_integer_literal_invalid_octal(self):
        """test integer literals"""
        self.assertTrue(TestLexer.checkLexeme("0o19", "0o1,9,<EOF>", 136))

    def test_integer_literal_invalid_hexadecimal(self):
        """test integer literals"""
        self.assertTrue(TestLexer.checkLexeme("0x1G", "0x1,ErrorToken(G),<EOF>", 137))

    def test_float_literal(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("3.14", "3.14,<EOF>", 138))

    def test_float_literal_with_exponent(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("2.0e10", "2.0e10,<EOF>", 139))

    def test_float_literal_with_negative_exponent(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("2.0e-10", "2.0e-10,<EOF>", 140))

    def test_float_literal_without_fraction(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("2e10", "2e10,<EOF>", 141))

    def test_float_literal_invalid(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("2.0e", "2.0,e,<EOF>", 142))

    def test_string_literal(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"hello"', '"hello",<EOF>', 143))

    def test_string_literal_with_escape(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"hello\\nworld"', '"hello\\nworld",<EOF>', 144))

    def test_string_literal_with_double_quote(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"hello\\"world"', '"hello\\"world",<EOF>', 145))

    def test_string_literal_with_backslash(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"hello\\\\world"', '"hello\\\\world",<EOF>', 146))

    def test_string_literal_unclosed(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"hello', 'UnclosedString("hello)', 147))

    def test_string_literal_illegal_escape(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"hello\\xworld"', 'IllegalEscapeInString("hello\\x)', 148))

    def test_boolean_literal_true(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 149))

    def test_boolean_literal_false(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 150))

    def test_nil_literal(self):
        """test nil literals"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 151))

    def test_operator_plus(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("+", "+,<EOF>", 152))

    def test_operator_minus(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("-", "-,<EOF>", 153))

    def test_operator_multiply(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("*", "*,<EOF>", 154))

    def test_operator_divide(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("/", "/,<EOF>", 155))

    def test_operator_modulo(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("%", "%,<EOF>", 156))

    def test_operator_equal(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("==", "==,<EOF>", 157))

    def test_operator_not_equal(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("!=", "!=,<EOF>", 158))

    def test_operator_less_than(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("<", "<,<EOF>", 159))

    def test_operator_less_equal(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("<=", "<=,<EOF>", 160))

    def test_operator_greater_than(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(">", ">,<EOF>", 161))

    def test_operator_greater_equal(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(">=", ">=,<EOF>", 162))

    def test_operator_and(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("&&", "&&,<EOF>", 163))

    def test_operator_or(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("||", "||,<EOF>", 164))

    def test_operator_not(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("!", "!,<EOF>", 165))

    def test_operator_assign(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("=", "=,<EOF>", 166))

    def test_operator_short_assign(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(":=", ":=,<EOF>", 167))

    def test_operator_dot(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(".", ".,<EOF>", 168))

    def test_separator_parenthesis(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme("(", "(,<EOF>", 169))

    def test_separator_curly_brace(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme("{", "{,<EOF>", 170))

    def test_separator_square_bracket(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme("[", "[,<EOF>", 171))

    def test_separator_comma(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme(",", ",,<EOF>", 172))

    def test_separator_semicolon(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme(";", ";,<EOF>", 173))

    def test_comment_single_line(self):
        """test comments"""
        self.assertTrue(TestLexer.checkLexeme("// this is a comment", "<EOF>", 174))

    def test_comment_multi_line(self):
        """test comments"""
        self.assertTrue(TestLexer.checkLexeme("/* this is a \n multi-line comment */", "<EOF>", 175))

    def test_comment_nested_multi_line(self):
        """test comments"""
        self.assertTrue(TestLexer.checkLexeme("/* this is a /* nested */ comment */", "<EOF>", 176))

    def test_comment_unclosed_multi_line(self):
        """test comments"""
        self.assertTrue(TestLexer.checkLexeme("/* this is an unclosed comment", "UnclosedComment(/* this is an unclosed comment)", 177))

    def test_whitespace(self):
        """test whitespace"""
        self.assertTrue(TestLexer.checkLexeme(" \t\r\n", "<EOF>", 178))

    def test_mixed_tokens(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("int x = 10;", "int,x,=,10,;,<EOF>", 179))

    def test_mixed_tokens_with_comments(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("int x = 10; // assign 10 to x", "int,x,=,10,;,<EOF>", 180))

    def test_mixed_tokens_with_string(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme('string s = "hello";', "string,s,=,\"hello\",;,<EOF>", 181))

    def test_mixed_tokens_with_float(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("float f = 3.14;", "float,f,=,3.14,;,<EOF>", 182))

    def test_mixed_tokens_with_boolean(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("boolean b = true;", "boolean,b,=,true,;,<EOF>", 183))

    def test_mixed_tokens_with_array(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("int[] arr = {1, 2, 3};", "int,[,],arr,=,{,1,,,2,,,3,},;,<EOF>", 184))

    def test_mixed_tokens_with_struct(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("struct Point { int x; int y; };", "struct,Point,{,int,x,;,int,y,;,},;,<EOF>", 185))

    def test_mixed_tokens_with_function(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("func add(int x, int y) int { return x + y; }", "func,add,(,int,x,,,int,y,),int,{,return,x,+,y,;,},<EOF>", 186))

    def test_mixed_tokens_with_method(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("func (p Point) move(int dx, int dy) { p.x += dx; p.y += dy; }", "func,(,p,Point,),move,(,int,dx,,,int,dy,),{,p,.,x,+,=,dx,;,p,.,y,+,=,dy,;,},<EOF>", 187))

    def test_mixed_tokens_with_interface(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("type Shape interface { area() float; }", "type,Shape,interface,{,area,(,),float,;,},<EOF>", 188))

    def test_mixed_tokens_with_for_loop(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("for i := 0; i < 10; i++ { println(i); }", "for,i,:=,0,;,i,<,10,;,i,+,+,{,println,(,i,),;,},<EOF>", 189))

    def test_mixed_tokens_with_if_statement(self):
        """test mixed tokens"""
        self.assertTrue(TestLexer.checkLexeme("if x > 10 { println('x is greater than 10'); }", "if,x,>,10,{,println,(,ErrorToken('),x,is,greater,than,10,ErrorToken('),),;,},<EOF>", 190))

    def test_invalid_identifier_with_dollar(self):
        """test identifiers with unrecognized character '$'"""
        self.assertTrue(TestLexer.checkLexeme("a$b", "a,ErrorToken($),b,<EOF>", 191))

    def test_operator_triple_plus(self):
        """test operator triple plus"""
        self.assertTrue(TestLexer.checkLexeme("+++", "+,+,+,<EOF>", 192))

    def test_integer_literal_with_leading_zero(self):
        """test integer literal with leading zero"""
        self.assertTrue(TestLexer.checkLexeme("0123", "0123,<EOF>", 193))

    def test_float_literal_with_trailing_dot(self):
        """test float literal with trailing dot"""
        self.assertTrue(TestLexer.checkLexeme("3.", "3,ErrorToken(.),<EOF>", 194))

    def test_empty_input(self):
        """test empty input returns <EOF> only"""
        self.assertTrue(TestLexer.checkLexeme("", "<EOF>", 195))

    def test_complex_arithmetic_expression(self):
        """test mixed tokens in a complex arithmetic expression"""
        self.assertTrue(TestLexer.checkLexeme("a = b + c - d * e / f % g ;", "a,=,b,+,c,-,d,*,e,/,f,%,g,;,<EOF>", 196))

    def test_operator_combination_equal_not_equal(self):
        """test combination of operators '==' and '!='"""
        self.assertTrue(TestLexer.checkLexeme("==!=", "==,!=,<EOF>", 197))

    def test_invalid_character_hash(self):
        """test identifiers with unrecognized character '#'"""
        self.assertTrue(TestLexer.checkLexeme("a#b", "a,ErrorToken(#),b,<EOF>", 198))

    def test_array_of_identifiers(self):
        """test mixed tokens with an array containing identifiers"""
        self.assertTrue(TestLexer.checkLexeme("var arr = { abc, DEF, ghi_123 };", "var,arr,=,{,abc,,,DEF,,,ghi_123,},;,<EOF>", 199))

    def test_struct_with_nested_function(self):
        """test mixed tokens with struct containing a nested function"""
        self.assertTrue(TestLexer.checkLexeme("struct S { func f() int { return 0; } }", "struct,S,{,func,f,(,),int,{,return,0,;,},},<EOF>", 200))