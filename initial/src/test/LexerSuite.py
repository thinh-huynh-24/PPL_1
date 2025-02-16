import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abcabc", "abcabc,<EOF>", 101))

    def test_multi_line_comment(self):
        """test multi-line comments"""
        input = """/* This is a 
        multi-line comment
        /* with nested comment */
        testing */"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 102))

    def test_single_line_comment(self):
        """test single-line comments"""
        input = """// This is a single line comment
        abc"""
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 103))

    def test_mixed_comments(self):
        """test mixing both comment types"""
        input = """// Single line comment
        /* Multi-line
        comment */
        identifier"""
        expect = "identifier,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 104))

    def test_lowercase_identifier(self):
        """test lowercase identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 105))

    def test_uppercase_identifier(self):
        """test uppercase identifiers"""
        self.assertTrue(TestLexer.checkLexeme("ABC", "ABC,<EOF>", 106))

    def test_mixed_case_identifier(self):
        """test mixed case identifiers"""
        self.assertTrue(TestLexer.checkLexeme("aBcDeF", "aBcDeF,<EOF>", 107))

    def test_identifier_with_underscore(self):
        """test identifiers with underscore"""
        self.assertTrue(TestLexer.checkLexeme("_abc_123", "_abc_123,<EOF>", 108))

    def test_identifier_with_numbers(self):
        """test identifiers with numbers"""
        self.assertTrue(TestLexer.checkLexeme("abc123", "abc123,<EOF>", 109))

    def test_invalid_identifier_start_number(self):
        """test invalid identifier starting with number"""
        self.assertTrue(TestLexer.checkLexeme("123abc", "123,abc,<EOF>", 110))

    def test_identifier_with_special_char(self):
        """test identifier with special character"""
        self.assertTrue(TestLexer.checkLexeme("abc@def", "abc,Error Token @", 111))

    def test_multiple_identifiers(self):
        """test multiple identifiers separated by space"""
        self.assertTrue(TestLexer.checkLexeme("abc def ghi", "abc,def,ghi,<EOF>", 112))

    def test_single_keyword(self):
        """test single keyword"""
        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 113))

    def test_multiple_keywords(self):
        """test multiple keywords"""
        self.assertTrue(TestLexer.checkLexeme("if else for", "if,else,for,<EOF>", 114))

    def test_keywords_with_identifier(self):
        """test keywords mixed with identifiers"""
        self.assertTrue(TestLexer.checkLexeme("if abc else xyz", "if,abc,else,xyz,<EOF>", 115))

    def test_type_keywords(self):
        """test type keywords"""
        self.assertTrue(TestLexer.checkLexeme("int float boolean string", "int,float,boolean,string,<EOF>", 116))

    def test_declaration_keywords(self):
        """test declaration keywords"""
        self.assertTrue(TestLexer.checkLexeme("var const func", "var,const,func,<EOF>", 117))

    def test_control_flow_keywords(self):
        """test control flow keywords"""
        self.assertTrue(TestLexer.checkLexeme("break continue return", "break,continue,return,<EOF>", 118))

    def test_struct_interface_keywords(self):
        """test struct and interface keywords"""
        self.assertTrue(TestLexer.checkLexeme("struct interface type", "struct,interface,type,<EOF>", 119))

    def test_bool_nil_keywords(self):
        """test boolean and nil literals as keywords"""
        self.assertTrue(TestLexer.checkLexeme("true false nil", "true,false,nil,<EOF>", 120))

    def test_keyword_as_part_identifier(self):
        """test keyword as part of identifier"""
        self.assertTrue(TestLexer.checkLexeme("ifabc", "ifabc,<EOF>", 121))

    def test_case_sensitive_keywords(self):
        """test case sensitivity of keywords"""
        self.assertTrue(TestLexer.checkLexeme("IF If if", "IF,If,if,<EOF>", 122))

    def test_arithmetic_operators(self):
        """test arithmetic operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / %", "+,-,*,/,%,<EOF>", 123))

    def test_comparison_operators(self):
        """test comparison operators"""
        self.assertTrue(TestLexer.checkLexeme("== != < <= > >=", "==,!=,<,<=,>,>=,<EOF>", 124))

    def test_logical_operators(self):
        """test logical operators"""
        self.assertTrue(TestLexer.checkLexeme("&& || !", "&&,||,!,<EOF>", 125))

    def test_assignment_operators(self):
        """test assignment operators"""
        self.assertTrue(TestLexer.checkLexeme("= := += -= *= /= %=", "=,:=,+=,-=,*=,/=,%=,<EOF>", 126))

    def test_mixed_operators(self):
        """test mixed operators with identifiers"""
        self.assertTrue(TestLexer.checkLexeme("a + b * c", "a,+,b,*,c,<EOF>", 127))

    def test_operator_precedence(self):
        """test operator precedence with parentheses"""
        self.assertTrue(TestLexer.checkLexeme("(a + b) * c", "(,a,+,b,),*,c,<EOF>", 128))

    def test_invalid_operator_combination(self):
        """test invalid operator combinations"""
        self.assertTrue(TestLexer.checkLexeme("a +* b", "a,+,*,b,<EOF>", 129))

    def test_dot_operator(self):
        """test dot operator for member access"""
        self.assertTrue(TestLexer.checkLexeme("a.b", "a,.,b,<EOF>", 130))

    def test_operators_with_whitespace(self):
        """test operators with different whitespace"""
        self.assertTrue(TestLexer.checkLexeme("a  +  b", "a,+,b,<EOF>", 131))

    def test_operator_with_error_char(self):
        """test operator with invalid character"""
        self.assertTrue(TestLexer.checkLexeme("a @ b", "a,Error Token @", 132))

    def test_parentheses(self):
        """test parentheses separators"""
        self.assertTrue(TestLexer.checkLexeme("()", "(,),<EOF>", 133))

    def test_braces(self):
        """test curly braces separators"""
        self.assertTrue(TestLexer.checkLexeme("{}", "{,},<EOF>", 134))

    def test_brackets(self):
        """test square brackets separators"""
        self.assertTrue(TestLexer.checkLexeme("[]", "[,],<EOF>", 135))

    def test_comma(self):
        """test comma separator"""
        self.assertTrue(TestLexer.checkLexeme("a,b,c", "a,,,b,,,c,<EOF>", 136))

    def test_semicolon(self):
        """test semicolon separator"""
        self.assertTrue(TestLexer.checkLexeme("a;b;c", "a,;,b,;,c,<EOF>", 137))

    def test_mixed_separators(self):
        """test mixed separators"""
        self.assertTrue(TestLexer.checkLexeme("(a,b);[c]", "(,a,,,b,),[,c,],<EOF>", 138))

    def test_nested_separators(self):
        """test nested separators"""
        self.assertTrue(TestLexer.checkLexeme("{[()]}", "{,[,(,),],},<EOF>", 139))

    def test_separators_with_whitespace(self):
        """test separators with whitespace"""
        self.assertTrue(TestLexer.checkLexeme("( a , b )", "(,a,,,b,),<EOF>", 140))

    def test_separators_in_array(self):
        """test separators in array declaration"""
        self.assertTrue(TestLexer.checkLexeme("int[3]", "int,[,3,],<EOF>", 141))

    def test_separator_with_error(self):
        """test separator with error character"""
        self.assertTrue(TestLexer.checkLexeme("(a@b)", "(,a,Error Token @", 142))

    def test_string_literal(self):
        """test basic string literal"""
        self.assertTrue(TestLexer.checkLexeme('"Hello World"', 'Hello World,<EOF>', 143))

    def test_string_with_escape(self):
        """test string with escape sequences"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\nWorld"', 'Hello\\nWorld,<EOF>', 144))

    def test_unclosed_string(self):
        """test unclosed string literal"""
        self.assertTrue(TestLexer.checkLexeme('"Hello World', 'Unclosed String: Hello World', 145))

    def test_illegal_escape(self):
        """test string with illegal escape"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\kWorld"', 'Illegal Escape In String: Hello\\k', 146))

    def test_integer_literal(self):
        """test integer literals in different bases"""
        self.assertTrue(TestLexer.checkLexeme("123 0xFF 0o77 0b11", "123,0xFF,0o77,0b11,<EOF>", 147))

    def test_float_literal(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("123.456 1.2e-10 1.2E+10", "123.456,1.2e-10,1.2E+10,<EOF>", 148))

    def test_boolean_literal(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("true false", "true,false,<EOF>", 149))

    def test_nil_literal(self):
        """test nil literal"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 150))

    def test_mixed_literals(self):
        """test mixing different types of literals"""
        self.assertTrue(TestLexer.checkLexeme('123 3.14 "abc" true nil', '123,3.14,abc,true,nil,<EOF>', 151))

    def test_literal_with_error(self):
        """test literal with error character"""
        self.assertTrue(TestLexer.checkLexeme('123@456', '123,Error Token @', 152))

    def test_complex_expression(self):
        """test complex expression"""
        self.assertTrue(TestLexer.checkLexeme("a + b * (c - d)", "a,+,b,*,(,c,-,d,),<EOF>", 153))

    def test_array_declaration(self):
        """test array declaration"""
        self.assertTrue(TestLexer.checkLexeme("int[5] arr", "int,[,5,],arr,<EOF>", 154))

    def test_function_declaration(self):
        """test function declaration"""
        self.assertTrue(TestLexer.checkLexeme("func main() { }", "func,main,(,),{,},<EOF>", 155))

    def test_string_with_special_chars(self):
        """test string with special characters"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\t\\n\\r"', 'Hello\\t\\n\\r,<EOF>', 156))

    def test_multi_dimensional_array(self):
        """test multi-dimensional array access"""
        self.assertTrue(TestLexer.checkLexeme("arr[1][2]", "arr,[,1,],[,2,],<EOF>", 157))

    def test_struct_member_access(self):
        """test struct member access"""
        self.assertTrue(TestLexer.checkLexeme("person.name", "person,.,name,<EOF>", 158))

    def test_complex_float(self):
        """test complex float literal"""
        self.assertTrue(TestLexer.checkLexeme("1.234e-5", "1.234e-5,<EOF>", 159))

    def test_nested_block(self):
        """test nested block"""
        self.assertTrue(TestLexer.checkLexeme("{ { { } } }", "{,{,{,},},},<EOF>", 160))

    def test_mixed_expression(self):
        """test mixed expression with different operators"""
        self.assertTrue(TestLexer.checkLexeme("a + b * c / d", "a,+,b,*,c,/,d,<EOF>", 161))

    def test_function_call(self):
        """test function call"""
        self.assertTrue(TestLexer.checkLexeme("print(x)", "print,(,x,),<EOF>", 162))

    def test_string_concat(self):
        """test string concatenation"""
        self.assertTrue(TestLexer.checkLexeme('"Hello" + "World"', 'Hello,+,World,<EOF>', 163))

    def test_array_literal(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme("[1,2,3]", "[,1,,,2,,,3,],<EOF>", 164))

    def test_complex_identifier(self):
        """test complex identifier"""
        self.assertTrue(TestLexer.checkLexeme("_complex_id_123", "_complex_id_123,<EOF>", 165))

    def test_nested_comment(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("/* outer /* inner */ */", "<EOF>", 166))

    def test_multiple_statements(self):
        """test multiple statements"""
        self.assertTrue(TestLexer.checkLexeme("x=1;y=2;", "x,=,1,;,y,=,2,;,<EOF>", 167))

    def test_complex_string(self):
        """test complex string with multiple escapes"""
        self.assertTrue(TestLexer.checkLexeme('"String\\nwith\\tmultiple\\rescapes"', 'String\\nwith\\tmultiple\\rescapes,<EOF>', 168))

    def test_mixed_operators_complex(self):
        """test complex mixed operators"""
        self.assertTrue(TestLexer.checkLexeme("a += b *= c /= d", "a,+=,b,*=,c,/=,d,<EOF>", 169))

    def test_complex_separators(self):
        """test complex separator combinations"""
        self.assertTrue(TestLexer.checkLexeme("{[a,b];(c,d)}", "{,[,a,,,b,],;,(,c,,,d,),},<EOF>", 170))

    def test_error_string(self):
        """test error in string"""
        self.assertTrue(TestLexer.checkLexeme('"String with \p"', 'Illegal Escape In String: String with \p', 171))

    def test_unclosed_comment(self):
        """test unclosed comment"""
        self.assertTrue(TestLexer.checkLexeme("/* Unclosed comment", "Unclosed Comment", 172))

    def test_mixed_number_formats(self):
        """test different number formats together"""
        self.assertTrue(TestLexer.checkLexeme("123 0xFF 1.23e-4", "123,0xFF,1.23e-4,<EOF>", 173))

    def test_string_with_quotes(self):
        """test string with escaped quotes"""
        self.assertTrue(TestLexer.checkLexeme('"String with \\"quotes\\""', 'String with \\"quotes\\",<EOF>', 174))

    def test_complex_function_call(self):
        """test complex function call with parameters"""
        self.assertTrue(TestLexer.checkLexeme("calc(x+y, z*w)", "calc,(,x,+,y,,,z,*,w,),<EOF>", 175))

    def test_struct_definition(self):
        """test struct definition"""
        self.assertTrue(TestLexer.checkLexeme("type Person struct {}", "type,Person,struct,{,},<EOF>", 176))

    def test_interface_definition(self):
        """test interface definition"""
        self.assertTrue(TestLexer.checkLexeme("type Shape interface {}", "type,Shape,interface,{,},<EOF>", 177))

    def test_multiple_declarations(self):
        """test multiple variable declarations"""
        self.assertTrue(TestLexer.checkLexeme("var x,y,z int", "var,x,,,y,,,z,int,<EOF>", 178))

    def test_array_initialization(self):
        """test array initialization"""
        self.assertTrue(TestLexer.checkLexeme("arr := []int{1,2,3}", "arr,:=,[,],int,{,1,,,2,,,3,},<EOF>", 179))

    def test_complex_type_declaration(self):
        """test complex type declaration"""
        self.assertTrue(TestLexer.checkLexeme("[][]int", "[,],[,],int,<EOF>", 180))

    def test_string_with_tabs(self):
        """test string with tab characters"""
        self.assertTrue(TestLexer.checkLexeme('"Col1\\tCol2\\tCol3"', 'Col1\\tCol2\\tCol3,<EOF>', 181))

    def test_nested_array_access(self):
        """test nested array access"""
        self.assertTrue(TestLexer.checkLexeme("matrix[i][j][k]", "matrix,[,i,],[,j,],[,k,],<EOF>", 182))

    def test_complex_method_call(self):
        """test complex method call"""
        self.assertTrue(TestLexer.checkLexeme("obj.method().field", "obj,.,method,(,),.,field,<EOF>", 183))

    def test_multiple_escape_sequence(self):
        """test multiple escape sequences"""
        self.assertTrue(TestLexer.checkLexeme('"\\n\\t\\r\\"\\\\"', '\\n\\t\\r\\"\\\\,<EOF>', 184))

    def test_nested_block_with_statement(self):
        """test nested block with statement"""
        self.assertTrue(TestLexer.checkLexeme("if(x){if(y){}}", "if,(,x,),{,if,(,y,),{,},},<EOF>", 185))

    def test_complex_for_loop(self):
        """test complex for loop"""
        self.assertTrue(TestLexer.checkLexeme("for i:=0;i<n;i+=1", "for,i,:=,0,;,i,<,n,;,i,+=,1,<EOF>", 186))

    def test_multiline_string_error(self):
        """test multiline string error"""
        self.assertTrue(TestLexer.checkLexeme('"string\nwith\nlinebreaks"', 'Unclosed String: string', 187))

    def test_complex_operator_chain(self):
        """test chain of operators"""
        self.assertTrue(TestLexer.checkLexeme("a += b -= c *= d", "a,+=,b,-=,c,*=,d,<EOF>", 188))

    def test_multiple_dot_access(self):
        """test multiple dot access"""
        self.assertTrue(TestLexer.checkLexeme("a.b.c.d", "a,.,b,.,c,.,d,<EOF>", 189))

    def test_mixed_bracket_types(self):
        """test mixed bracket types"""
        self.assertTrue(TestLexer.checkLexeme("func({[]})", "func,(,{,[,],},),<EOF>", 190))

    def test_complex_expression_with_literals(self):
        """test complex expression with different literals"""
        self.assertTrue(TestLexer.checkLexeme('x = 1 + 2.0 + "3"', 'x,=,1,+,2.0,+,3,<EOF>', 191))

    def test_invalid_hex_number(self):
        """test invalid hexadecimal number"""
        self.assertTrue(TestLexer.checkLexeme("0xGH", "0,x,GH,<EOF>", 192))

    def test_invalid_binary_number(self):
        """test invalid binary number"""
        self.assertTrue(TestLexer.checkLexeme("0b102", "0b10,2,<EOF>", 193))

    def test_complex_identifier_sequence(self):
        """test sequence of complex identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_a1 _b2_ __c3", "_a1,_b2_,__c3,<EOF>", 194))

    def test_mixed_comment_string(self):
        """test mixing comments and strings"""
        self.assertTrue(TestLexer.checkLexeme('/*comment*/"string"//comment', 'string,<EOF>', 195))

    def test_complex_escape_error(self):
        """test complex escape sequence error"""
        self.assertTrue(TestLexer.checkLexeme('"\\n\\t\\k"', 'Illegal Escape In String: \\n\\t\\k', 196))

    def test_nested_function_calls(self):
        """test nested function calls"""
        self.assertTrue(TestLexer.checkLexeme("f1(f2(f3()))", "f1,(,f2,(,f3,(,),),),<EOF>", 197))

    def test_complex_array_declaration(self):
        """test complex array declaration"""
        self.assertTrue(TestLexer.checkLexeme("var arr [3][4]int", "var,arr,[,3,],[,4,],int,<EOF>", 198))

    def test_unicode_string_error(self):
        """test string with unicode error"""
        self.assertTrue(TestLexer.checkLexeme('"Hello \u0123"', 'Illegal Escape In String: Hello \\u', 199))

    def test_mixed_declaration_types(self):
        """test mixed declaration types"""
        self.assertTrue(TestLexer.checkLexeme("var x int; const y = 5", "var,x,int,;,const,y,=,5,<EOF>", 200))

    def test_complex_package_access(self):
        """test complex package access"""
        self.assertTrue(TestLexer.checkLexeme("pkg.sub.func()", "pkg,.,sub,.,func,(,),<EOF>", 201))

