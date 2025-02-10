grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

fragment NESTED_COMMENT: '/*' (NESTED_COMMENT | ~'*/')* '*/';
ML_COMMENT: NESTED_COMMENT -> skip;
SL_COMMENT: '//' ~[\r\n]* -> skip;

NL: '\n' -> skip; //skip newlines

WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs 



program  : statement+ EOF ;

statement: vardecl
        | const_decl
        | func_decl
        | assignment_stmt
        | if_stmt
        | for_stmt
        | range_stmt
        | break_stmt
        | continue_stmt
        | return_stmt
        | call_stmt
        ;

assignment_stmt: (primitive_type | array_access | struct_access) ass_op expression SEMI;
ass_op: (ASSIGN|COLON_ASSIGN|ADD_ASSIGN|SUB_ASSIGN|MUL_ASSIGN|DIV_ASSIGN|MOD_ASSIGN);
if_stmt: IF expression block (ELSE IF expression block )* (ELSE block)?;
for_stmt: FOR (basic|with_init_con_upd|range_stmt) block;
basic: expression;
with_init_con_upd: (assignment_stmt | vardecl) SEMI expression? SEMI assignment_stmt;
range_stmt: (IDENTIFIER | '_') COMMA IDENTIFIER ass_op RANGE IDENTIFIER;
break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI;
return_stmt: RETURN expression? SEMI;
call_stmt: (IDENTIFIER DOT)? IDENTIFIER signature (SEMI|NL);

expression
    : operands
    | array_access
    | struct_access
    | func_call
    | (NOT | SUB) expression                 
    | expression (MUL | DIV | MOD) expression               
    | expression (ADD | SUB) expression                    
    | expression (EQ | NEQ | LT | LE | GT | GE) expression 
    | expression AND expression                             
    | expression OR expression                              
    ;

operands
    : primitive_type
    | array_lit
    | struct_lit
    | LPAREN expression RPAREN
    ;


array_access: IDENTIFIER (LBRACK INTERGER_LITERAL RBRACK)+;
struct_access: IDENTIFIER DOT IDENTIFIER;
func_call: IDENTIFIER DOT IDENTIFIER signature;
array_lit: type_ LBRACK  ( expression (COMMA expression)* | (LBRACK (expression (COMMA expression)*) RBRACK)+) RBRACK;
struct_lit: IDENTIFIER LBRACE (fieldInit (COMMA fieldInit)*)? RBRACE;
fieldInit: IDENTIFIER COLON expression;

//func (ten kieu)? ten chu ki khoi
func_decl: FUNC (LPAREN IDENTIFIER type_ RPAREN)? IDENTIFIER signature block;
//{ bieu thuc* }
block: LBRACE expression* RBRACE;
//const ten gan bieu thuc;
const_decl: CONST IDENTIFIER ASSIGN expression SEMI;

// var ten kieu? (gan bieu thuc)? ;
vardecl: VAR IDENTIFIER type_? (ASSIGN expression)? SEMI ;

type_decl: TYPE IDENTIFIER (STRUCT LBRACE (field_decl SEMI)* RBRACE | INTERFACE LBRACE (method_spec SEMI)* RBRACE) SEMI;
//ten kieu
field_decl: IDENTIFIER type_;
//ten chu ki?
method_spec: IDENTIFIER signature;
// ( tham so? ) kieu?
signature: LPAREN (parameterList)? RPAREN type_?;
//danh sach tham so 
parameterList: parameter (COMMA parameter)*;
// ten kieu
parameter: IDENTIFIER type_;
//kieu chu
type_: (LBRACK INTERGER_LITERAL RBRACK)* ( INT | FLOAT | STRING | BOOLEAN | NIL | IDENTIFIER );
//kieu lit
primitive_type: STRING_LITERAL | FLOAT_LITERAL | SIGN? INTERGER_LITERAL | BOOLEAN_LITERAL | NIL_LITERAL | IDENTIFIER;


//LITERAL

NIL_LITERAL: NIL;

BOOLEAN_LITERAL: (TRUE | FALSE);

STRING_LITERAL: '"' (ESC | ~[\\"])* '"';
fragment ESC_SEQ: '\\' ('n' | 't' | 'r' | '"' | '\\');

FLOAT_LITERAL: [0-9]+ '.' [0-9]* EXP?; 
fragment EXP: ('e'|'E') [+-]? [0-9]+;

INTERGER_LITERAL: DEC | BIN | OCT | HEX;
fragment DEC: '0' | [1-9] [0-9]*;
fragment BIN: ('0b'|'0B') [01]+;
fragment OCT: ('0o'|'0O') [0-7]+;
fragment HEX: ('0x'|'0X') [0-9a-fA-F]+;
SIGN: [+-];



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