grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
    def __init__(self, input=None, output=sys.stdout):
        super().__init__(input, output)
        self.prev_token = None

    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit()
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit()
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            result = super().emit()
            raise ErrorToken(result.text)
        else:
            result = super().emit()
            self.prev_token = result.type
            return result

}

options {
    language=Python3;
}



program  : statement+ EOF ;

statement: var_decl_stmt end_stmt
        | const_decl_stmt end_stmt
        | func_decl end_stmt
        | menthod_decl end_stmt
        | assignment_stmt end_stmt
        | if_stmt end_stmt
        | for_stmt end_stmt
        | break_stmt end_stmt 
        | continue_stmt end_stmt
        | return_stmt end_stmt
        | call_stmt end_stmt
        | type_decl end_stmt
        ;

assignment_stmt: primitive_type ass_op expression;
ass_op: (COLON_ASSIGN|ADD_ASSIGN|SUB_ASSIGN|MUL_ASSIGN|DIV_ASSIGN|MOD_ASSIGN);

if_stmt: IF LPAREN expression RPAREN block  | IF LPAREN expression RPAREN block else_stmt | IF LPAREN expression RPAREN LBRACE if_stmt RBRACE;
else_stmt: ELSE block | ELSE if_stmt;

for_stmt: FOR (basic_for|with_init_con_upd|range_for) block;
basic_for: expression;
with_init_con_upd: (assignment_stmt | var_decl_stmt) SEMI expression SEMI assignment_stmt;
range_for: (IDENTIFIER | ) COMMA IDENTIFIER COLON_ASSIGN RANGE primitive_type;

break_stmt: BREAK;

continue_stmt: CONTINUE ;

return_stmt: RETURN expression | RETURN ;

call_stmt: func_call ;
 
menthod_decl: FUNC LPAREN IDENTIFIER type_ RPAREN IDENTIFIER signature block | FUNC LPAREN IDENTIFIER type_ RPAREN IDENTIFIER signature type_ block;

parameter: IDENTIFIER type_ | IDENTIFIER | expression;

parameterlist: parameter COMMA parameterlist | parameter;

signature: LPAREN parameterlist RPAREN | LPAREN  RPAREN;

func_decl: FUNC IDENTIFIER signature block | FUNC IDENTIFIER signature type_ block;

block: LBRACE list_statement RBRACE ;
list_statement: list_statement statement  | statement | ;
const_decl_stmt: CONST IDENTIFIER ASSIGN expression;

var_decl_stmt: VAR IDENTIFIER | VAR IDENTIFIER type_ | VAR IDENTIFIER type_ ASSIGN expression | VAR IDENTIFIER  ASSIGN expression;

end_stmt: SEMI;

expression: term_1;
term_1: term_2 OR expression | term_2;
term_2: term_3 AND expression | term_3;
term_3: term_4 (EQ | NEQ | LT | LE | GT | GE) expression | term_4;
term_4: term_5 (ADD | SUB) expression | term_5;
term_5: term_6 (MUL | DIV | MOD) expression | term_6;
term_6: (NOT | SUB) expression | term_7;
term_7: primitive_type | array_lit | struct_lit | LPAREN expression RPAREN | func_call ;

primitive_type: struct_access | array_access| STRING_LITERAL | FLOAT_LITERAL | INTERGER_LITERAL | BOOLEAN_LITERAL | NIL_LITERAL | IDENTIFIER;

array_lit: type_ LBRACE list_array_elements RBRACE;
list_array_elements: array_element COMMA list_array_elements | array_element |;
array_element: primitive_type | nested_array;
nested_array: LBRACE list_array_elements RBRACE;

array_access: IDENTIFIER list_dimention;

type_: INT | FLOAT | STRING | BOOLEAN | NIL | IDENTIFIER | list_dimention ( INT | FLOAT | STRING | BOOLEAN | NIL | IDENTIFIER );

list_dimention: dimention list_dimention | dimention;
dimention: LBRACK INTERGER_LITERAL RBRACK;

struct_access: type_ DOT IDENTIFIER;

func_call: IDENTIFIER signature | IDENTIFIER DOT IDENTIFIER signature;

struct_lit: type_ LBRACE list_struct_elements RBRACE;

list_struct_elements: struct_elements COMMA list_struct_elements | struct_elements;
struct_elements: IDENTIFIER COLON expression;

type_decl: interface_decl | struct_decl;
interface_decl: TYPE IDENTIFIER INTERFACE LBRACE list_menthod RBRACE ;
list_menthod: menthod list_menthod | menthod  |;
menthod: IDENTIFIER signature end_stmt | IDENTIFIER signature type_ end_stmt;

struct_decl: TYPE IDENTIFIER STRUCT LBRACE list_field_decl RBRACE ;
list_field_decl: field_decl list_field_decl | field_decl |;
field_decl: IDENTIFIER type_ end_stmt;

//LITERAL
fragment NESTED_COMMENT: '/*' ( NESTED_COMMENT | ~[*/] | '*' ~[/] )* '*/';
ML_COMMENT: NESTED_COMMENT -> skip;
SL_COMMENT: '//' ~[\r\n]* -> skip;

IMPLICIT_SEMI: (IDENTIFIER | INTERGER_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL 
              | INT | FLOAT | BOOLEAN | STRING | RETURN | CONTINUE | BREAK 
              | RPAREN | RBRACE | RBRACK) 
              NL -> type(SEMI);

WS : [ \f\b\t\r] -> skip ; // skip spaces, tabs, newlines

NL: '\n' -> skip;

NIL_LITERAL: NIL;

BOOLEAN_LITERAL: TRUE | FALSE;

STRING_LITERAL: '"' ( ESC_SEQ | ~[\\"])* '"';
fragment ESC_SEQ: '\\' ('n' | 't' | 'r' | '"' | '\\');

FLOAT_LITERAL: [0-9]+ '.' [0-9]* EXP?; 
fragment EXP: ('e'|'E') [+-]? [0-9]+;

INTERGER_LITERAL: DEC | BIN | OCT | HEX;
fragment DEC: '0' | [1-9] [0-9]*;
fragment BIN: ('0b'|'0B') [01]+;
fragment OCT: ('0o'|'0O') [0-7]+;
fragment HEX: ('0x'|'0X') [0-9a-fA-F]+;

COLON: ':';
//SEPARATORSEPARATOR
LPAREN   : '(';  
RPAREN   : ')';   
LBRACE   : '{';   
RBRACE   : '}';   
LBRACK   : '[';  
RBRACK   : ']';  
COMMA    : ',';   
SEMI     : ';';   

// OPERATOR
ADD         : '+';
SUB         : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%';

EQ          : '==';
NEQ         : '!=';
LT          : '<';
LE          : '<=';
GT          : '>';
GE          : '>=';

AND         : '&&';
OR          : '||';
NOT         : '!';

ASSIGN      : '=';
COLON_ASSIGN: ':=';
ADD_ASSIGN  : '+=';
SUB_ASSIGN  : '-=';
MUL_ASSIGN  : '*=';
DIV_ASSIGN  : '/=';
MOD_ASSIGN  : '%=';

DOT         : '.';

//KEYWORD
IF          : 'if';
ELSE        : 'else';
FOR         : 'for';
STRUCT      : 'struct';
INTERFACE   : 'interface';
STRING      : 'string';
CONST       : 'const';
VAR         : 'var';
RETURN      : 'return';
FUNC        : 'func';
INT         : 'int';
TYPE        : 'type';
FLOAT       : 'float';
BOOLEAN     : 'boolean';
CONTINUE    : 'continue';
BREAK       : 'break';
RANGE       : 'range';
TRUE        : 'true';
FALSE       : 'false';
NIL         : 'nil';

IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

fragment ESC: '\\' [btnfr"'\\] ;

ERROR_CHAR: . { raise ErrorToken(self.text) } ;

UNCLOSE_STRING: '"' (ESC | ~["\\\r\n])* { raise UncloseString(self.text[1:]) } ;

ILLEGAL_ESCAPE: '"' (ESC | ~["\\\r\n])* '\\' ~[btnfr"'\\] { raise IllegalEscape(self.text[1:]) } ;