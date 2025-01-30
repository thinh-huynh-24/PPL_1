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

ML_COMMENT: '/*' (ML_COMMENT | .)*? '*/' -> skip;
SL_COMMENT: '//' ~[\r\n]* -> skip;

NL: '\n' -> skip; //skip newlines

WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs 



program  : decl+ EOF ;

decl: funcdecl | vardecl  ;

vardecl: 'var' ID 'int' ';' ;

funcdecl: 'func' ID '(' ')' '{' '}' ';' ;

ID: [a-z]+;


//LITERAL
NIL_LITERAL: NIL;

BOOLEAN_LITERAL: (TRUE | FALSE);

STRING_LITERAL: '"' (ESC | ~[\\"])* '"';
fragment ESC_SEQ: '\\' ('n' | 't' | 'r' | '"' | '\\');

FLOAT_LITERAL: [0-9]+ '.' [0-9]* EXP* [0-9]*; 
fragment EXP: ('e'|'E') [+-]*;

INTERGER_LITERAL: DEC | BIN | OCT | HEX;
fragment DEC: '0' | [1-9] [0-9]*;
fragment BIN: ('0b'|'0B') [01]+;
fragment OCT: ('0o'|'0O') [0-7]+;
fragment HEX: ('0x'|'0X') [0-9a-fA-F]+;


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



//STRING: '"' (ESC | ~["\\\r\n])* '"' ;
fragment ESC: '\\' [btnfr"'\\] ;

ERROR_CHAR: . { raise ErrorToken(self.text) } ;

UNCLOSE_STRING: '"' (ESC | ~["\\\r\n])* { raise UncloseString(self.text[1:]) } ;

ILLEGAL_ESCAPE: '"' (ESC | ~["\\\r\n])* '\\' ~[btnfr"'\\] { raise IllegalEscape(self.text[1:]) } ;