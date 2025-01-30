import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    
    def test_whitespace_characters(self):
        """test whitespace characters"""
        self.assertTrue(TestLexer.checkLexeme(" \t\f\r\n","<EOF>",105))
    
    def test_single_line_comment(self):
        """test single-line comment"""
        self.assertTrue(TestLexer.checkLexeme("// this is a comment\nabc","abc,<EOF>",106))
    
    def test_multi_line_comment(self):
        """test multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme("/* this is a \n multi-line \n comment */abc","abc,<EOF>",107))
    
    def test_nested_multi_line_comment(self):
        """test nested multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme("/* this is a /* nested */ comment */abc","abc,<EOF>",108))
   
    def test_valid_identifiers(self):
        """test valid identifiers"""
        self.assertTrue(TestLexer.checkLexeme("x userName tempVar count123","x,userName,tempVar,count123,<EOF>",109))
    def test_keyword_if(self):
        """test keyword if"""
        self.assertTrue(TestLexer.checkLexeme("if","if,<EOF>",110))

    def test_keyword_else(self):
            """test keyword else"""
            self.assertTrue(TestLexer.checkLexeme("else","else,<EOF>",111))

    def test_keyword_for(self):
            """test keyword for"""
            self.assertTrue(TestLexer.checkLexeme("for","for,<EOF>",112))

    def test_keyword_struct(self):
            """test keyword struct"""
            self.assertTrue(TestLexer.checkLexeme("struct","struct,<EOF>",113))

    def test_keyword_interface(self):
            """test keyword interface"""
            self.assertTrue(TestLexer.checkLexeme("interface","interface,<EOF>",114))

    def test_keyword_string(self):
            """test keyword string"""
            self.assertTrue(TestLexer.checkLexeme("string","string,<EOF>",115))

    def test_keyword_const(self):
            """test keyword const"""
            self.assertTrue(TestLexer.checkLexeme("const","const,<EOF>",116))

    def test_keyword_var(self):
            """test keyword var"""
            self.assertTrue(TestLexer.checkLexeme("var","var,<EOF>",117))

    def test_keyword_return(self):
            """test keyword return"""
            self.assertTrue(TestLexer.checkLexeme("return","return,<EOF>",118))

    def test_keyword_func(self):
            """test keyword func"""
            self.assertTrue(TestLexer.checkLexeme("func","func,<EOF>",119))

    def test_keyword_int(self):
            """test keyword int"""
            self.assertTrue(TestLexer.checkLexeme("int","int,<EOF>",120))

    def test_keyword_type(self):
            """test keyword type"""
            self.assertTrue(TestLexer.checkLexeme("type","type,<EOF>",121))

    def test_keyword_float(self):
            """test keyword float"""
            self.assertTrue(TestLexer.checkLexeme("float","float,<EOF>",122))

    def test_keyword_boolean(self):
            """test keyword boolean"""
            self.assertTrue(TestLexer.checkLexeme("boolean","boolean,<EOF>",123))

    def test_keyword_continue(self):
            """test keyword continue"""
            self.assertTrue(TestLexer.checkLexeme("continue","continue,<EOF>",124))

    def test_keyword_break(self):
            """test keyword break"""
            self.assertTrue(TestLexer.checkLexeme("break","break,<EOF>",125))

    def test_keyword_range(self):
            """test keyword range"""
            self.assertTrue(TestLexer.checkLexeme("range","range,<EOF>",126))

    def test_keyword_true(self):
            """test keyword true"""
            self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>",127))

    def test_keyword_false(self):
            """test keyword false"""
            self.assertTrue(TestLexer.checkLexeme("false","false,<EOF>",128))

    def test_keyword_nil(self):
            """test keyword nil"""
            self.assertTrue(TestLexer.checkLexeme("nil","nil,<EOF>",129))
    def test_decimal_integer_literals(self):
        """test decimal integer literals"""
        self.assertTrue(TestLexer.checkLexeme("0 42 12345","0,42,12345,<EOF>",130))

    def test_binary_integer_literals(self):
            """test binary integer literals"""
            self.assertTrue(TestLexer.checkLexeme("0b101 0B1101","0b101,0B1101,<EOF>",131))

    def test_octal_integer_literals(self):
            """test octal integer literals"""
            self.assertTrue(TestLexer.checkLexeme("0o12 0O77","0o12,0O77,<EOF>",132))

    def test_hexadecimal_integer_literals(self):
            """test hexadecimal integer literals"""
            self.assertTrue(TestLexer.checkLexeme("0x1A 0XFF","0x1A,0XFF,<EOF>",133))
    def test_floating_point_literal_1(self):
        """test floating-point literal 3.14"""
        self.assertTrue(TestLexer.checkLexeme("3.14","3.14,<EOF>",134))

    def test_floating_point_literal_2(self):
            """test floating-point literal 0."""
            self.assertTrue(TestLexer.checkLexeme("0.","0.,<EOF>",135))

    def test_floating_point_literal_3(self):
            """test floating-point literal 2.0e10"""
            self.assertTrue(TestLexer.checkLexeme("2.0e10","2.0e10,<EOF>",136))
    def test_floating_point_literal_4(self):
        """test floating-point literal 1.0"""
        self.assertTrue(TestLexer.checkLexeme("1.0","1.0,<EOF>",137))

    def test_floating_point_literal_6(self):
            """test floating-point literal 6.022e23"""
            self.assertTrue(TestLexer.checkLexeme("6.022e23","6.022e23,<EOF>",138))

    def test_floating_point_literal_7(self):
            """test floating-point literal 7.0E-10"""
            self.assertTrue(TestLexer.checkLexeme("7.0E-10","7.0E-10,<EOF>",139))

    def test_floating_point_literal_8(self):
            """test floating-point literal 8.0E+10"""
            self.assertTrue(TestLexer.checkLexeme("8.0E+10","8.0E+10,<EOF>",140))       
    def test_string_literal_1(self):
        """test string literal "hello" """
        self.assertTrue(TestLexer.checkLexeme('"hello"', '"hello",<EOF>',141))

    def test_string_literal_2(self):
            """test string literal "123" """
            self.assertTrue(TestLexer.checkLexeme('"123"', '"123",<EOF>',142))

    def test_string_literal_3(self):
            """test string literal with newline"""
            self.assertTrue(TestLexer.checkLexeme('"This is a string with a newline\\n"', '"This is a string with a newline\\n",<EOF>',143))

    def test_string_literal_4(self):
            """test string literal with tab"""
            self.assertTrue(TestLexer.checkLexeme('"This is a string with a tab\\t"', '"This is a string with a tab\\t",<EOF>',144))

    def test_string_literal_5(self):
            """test string literal with carriage return"""
            self.assertTrue(TestLexer.checkLexeme('"This is a string with a carriage return\\r"', '"This is a string with a carriage return\\r",<EOF>',145))

    def test_string_literal_6(self):
            """test string literal with double quote"""
            self.assertTrue(TestLexer.checkLexeme('"This is a string with a double quote\\""','"This is a string with a double quote\\"",<EOF>',146))

    def test_string_literal_7(self):
            """test string literal with backslash"""
            self.assertTrue(TestLexer.checkLexeme('"This is a string with a backslash\\\\"','"This is a string with a backslash\\\\",<EOF>',147))
    
    def test_boolean_literal_true(self):
        """test boolean literal true"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>",148))

    def test_boolean_literal_false(self):
            """test boolean literal false"""
            self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>",149))

    def test_nil_literal(self):
            """test nil literal"""
            self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>",150))