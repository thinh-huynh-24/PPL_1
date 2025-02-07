# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0088\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\6\2 \n\2\r\2\16\2!\3\2\3\2\3\3\3\3")
        buf.write("\5\3(\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6>\n\6\3\7\3\7")
        buf.write("\3\7\3\7\5\7D\n\7\3\b\3\b\3\b\5\bI\n\b\3\b\3\b\5\bM\n")
        buf.write("\b\3\b\3\b\3\t\3\t\5\tS\n\t\3\t\3\t\3\t\3\t\5\tY\n\t\5")
        buf.write("\t[\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nd\n\n\3\13\3\13")
        buf.write("\3\13\3\13\5\13j\n\13\3\f\3\f\3\f\5\fo\n\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\5\rv\n\r\3\16\3\16\3\16\3\16\3\16\5\16}\n\16")
        buf.write("\3\17\3\17\3\17\5\17\u0082\n\17\3\17\3\17\5\17\u0086\n")
        buf.write("\17\3\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2")
        buf.write("\4\4\2\5\5\25\25\4\2\f\f@@\2\u008b\2\37\3\2\2\2\4\'\3")
        buf.write("\2\2\2\6)\3\2\2\2\b.\3\2\2\2\n\66\3\2\2\2\fC\3\2\2\2\16")
        buf.write("E\3\2\2\2\20Z\3\2\2\2\22\\\3\2\2\2\24i\3\2\2\2\26k\3\2")
        buf.write("\2\2\30r\3\2\2\2\32|\3\2\2\2\34\u0085\3\2\2\2\36 \5\4")
        buf.write("\3\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"")
        buf.write("#\3\2\2\2#$\7\2\2\3$\3\3\2\2\2%(\5\b\5\2&(\5\6\4\2\'%")
        buf.write("\3\2\2\2\'&\3\2\2\2(\5\3\2\2\2)*\7\63\2\2*+\7\7\2\2+,")
        buf.write("\7\66\2\2,-\7\25\2\2-\7\3\2\2\2./\7\65\2\2/\60\7\7\2\2")
        buf.write("\60\61\7\16\2\2\61\62\7\17\2\2\62\63\7\20\2\2\63\64\7")
        buf.write("\21\2\2\64\65\7\25\2\2\65\t\3\2\2\2\66\67\7\67\2\2\67")
        buf.write("8\7@\2\289\7\60\2\29:\7\20\2\2:;\5\f\7\2;=\7\21\2\2<>")
        buf.write("\t\2\2\2=<\3\2\2\2=>\3\2\2\2>\13\3\2\2\2?@\5\16\b\2@A")
        buf.write("\5\f\7\2AD\3\2\2\2BD\5\16\b\2C?\3\2\2\2CB\3\2\2\2D\r\3")
        buf.write("\2\2\2EF\7@\2\2FH\7\16\2\2GI\5\20\t\2HG\3\2\2\2HI\3\2")
        buf.write("\2\2IJ\3\2\2\2JL\7\17\2\2KM\5\34\17\2LK\3\2\2\2LM\3\2")
        buf.write("\2\2MN\3\2\2\2NO\t\2\2\2O\17\3\2\2\2PR\7@\2\2QS\5\34\17")
        buf.write("\2RQ\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\7\24\2\2U[\5\20\t\2")
        buf.write("VX\7@\2\2WY\5\34\17\2XW\3\2\2\2XY\3\2\2\2Y[\3\2\2\2ZP")
        buf.write("\3\2\2\2ZV\3\2\2\2[\21\3\2\2\2\\]\7\67\2\2]^\7@\2\2^_")
        buf.write("\7/\2\2_`\7\20\2\2`a\5\24\13\2ac\7\21\2\2bd\t\2\2\2cb")
        buf.write("\3\2\2\2cd\3\2\2\2d\23\3\2\2\2ef\5\26\f\2fg\5\24\13\2")
        buf.write("gj\3\2\2\2hj\5\26\f\2ie\3\2\2\2ih\3\2\2\2j\25\3\2\2\2")
        buf.write("kn\7@\2\2lo\5\34\17\2mo\7@\2\2nl\3\2\2\2nm\3\2\2\2op\3")
        buf.write("\2\2\2pq\t\2\2\2q\27\3\2\2\2ru\5\32\16\2sv\5\34\17\2t")
        buf.write("v\5\22\n\2us\3\2\2\2ut\3\2\2\2v\31\3\2\2\2wx\7\22\2\2")
        buf.write("xy\t\3\2\2yz\7\23\2\2z}\5\32\16\2{}\t\3\2\2|w\3\2\2\2")
        buf.write("|{\3\2\2\2}\33\3\2\2\2~\u0086\7\n\2\2\177\u0086\7\13\2")
        buf.write("\2\u0080\u0082\7\r\2\2\u0081\u0080\3\2\2\2\u0081\u0082")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0086\7\f\2\2\u0084")
        buf.write("\u0086\7\t\2\2\u0085~\3\2\2\2\u0085\177\3\2\2\2\u0085")
        buf.write("\u0081\3\2\2\2\u0085\u0084\3\2\2\2\u0086\35\3\2\2\2\22")
        buf.write("!\'=CHLRXZcinu|\u0081\u0085")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'\n'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "';'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", "':='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "'if'", 
                     "'else'", "'for'", "'struct'", "'interface'", "'string'", 
                     "'const'", "'var'", "'return'", "'func'", "'int'", 
                     "'type'", "'float'", "'boolean'", "'continue'", "'break'", 
                     "'range'", "'true'", "'false'", "'nil'" ]

    symbolicNames = [ "<INVALID>", "ML_COMMENT", "SL_COMMENT", "NL", "WS", 
                      "ID", "NIL_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                      "FLOAT_LITERAL", "INTERGER_LITERAL", "SIGN", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "COMMA", "SEMI", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR", 
                      "NOT", "ASSIGN", "COLON_ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "IF", 
                      "ELSE", "FOR", "STRUCT", "INTERFACE", "STRING", "CONST", 
                      "VAR", "RETURN", "FUNC", "INT", "TYPE", "FLOAT", "BOOLEAN", 
                      "CONTINUE", "BREAK", "RANGE", "TRUE", "FALSE", "NIL", 
                      "IDENTIFIER", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_funcdecl = 3
    RULE_interface_type = 4
    RULE_interface_field = 5
    RULE_method = 6
    RULE_parameter = 7
    RULE_struct_type = 8
    RULE_struct_field = 9
    RULE_property_struct = 10
    RULE_array = 11
    RULE_dimension = 12
    RULE_primitive_type = 13

    ruleNames =  [ "program", "decl", "vardecl", "funcdecl", "interface_type", 
                   "interface_field", "method", "parameter", "struct_type", 
                   "struct_field", "property_struct", "array", "dimension", 
                   "primitive_type" ]

    EOF = Token.EOF
    ML_COMMENT=1
    SL_COMMENT=2
    NL=3
    WS=4
    ID=5
    NIL_LITERAL=6
    BOOLEAN_LITERAL=7
    STRING_LITERAL=8
    FLOAT_LITERAL=9
    INTERGER_LITERAL=10
    SIGN=11
    LPAREN=12
    RPAREN=13
    LBRACE=14
    RBRACE=15
    LBRACK=16
    RBRACK=17
    COMMA=18
    SEMI=19
    ADD=20
    SUB=21
    MUL=22
    DIV=23
    MOD=24
    EQ=25
    NEQ=26
    LT=27
    LE=28
    GT=29
    GE=30
    AND=31
    OR=32
    NOT=33
    ASSIGN=34
    COLON_ASSIGN=35
    ADD_ASSIGN=36
    SUB_ASSIGN=37
    MUL_ASSIGN=38
    DIV_ASSIGN=39
    MOD_ASSIGN=40
    DOT=41
    IF=42
    ELSE=43
    FOR=44
    STRUCT=45
    INTERFACE=46
    STRING=47
    CONST=48
    VAR=49
    RETURN=50
    FUNC=51
    INT=52
    TYPE=53
    FLOAT=54
    BOOLEAN=55
    CONTINUE=56
    BREAK=57
    RANGE=58
    TRUE=59
    FALSE=60
    NIL=61
    IDENTIFIER=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.decl()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.VAR or _la==MiniGoParser.FUNC):
                    break

            self.state = 33
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.funcdecl()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(MiniGoParser.VAR)
            self.state = 40
            self.match(MiniGoParser.ID)
            self.state = 41
            self.match(MiniGoParser.INT)
            self.state = 42
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(MiniGoParser.FUNC)
            self.state = 45
            self.match(MiniGoParser.ID)
            self.state = 46
            self.match(MiniGoParser.LPAREN)
            self.state = 47
            self.match(MiniGoParser.RPAREN)
            self.state = 48
            self.match(MiniGoParser.LBRACE)
            self.state = 49
            self.match(MiniGoParser.RBRACE)
            self.state = 50
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def interface_field(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_fieldContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_interface_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MiniGoParser.TYPE)
            self.state = 53
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 54
            self.match(MiniGoParser.INTERFACE)
            self.state = 55
            self.match(MiniGoParser.LBRACE)
            self.state = 56
            self.interface_field()
            self.state = 57
            self.match(MiniGoParser.RBRACE)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NL or _la==MiniGoParser.SEMI:
                self.state = 58
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMI):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def interface_field(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_field" ):
                return visitor.visitInterface_field(self)
            else:
                return visitor.visitChildren(self)




    def interface_field(self):

        localctx = MiniGoParser.Interface_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_interface_field)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.method()
                self.state = 62
                self.interface_field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 68
            self.match(MiniGoParser.LPAREN)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 69
                self.parameter()


            self.state = 72
            self.match(MiniGoParser.RPAREN)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.INTERGER_LITERAL) | (1 << MiniGoParser.SIGN))) != 0):
                self.state = 73
                self.primitive_type()


            self.state = 76
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMI):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.INTERGER_LITERAL) | (1 << MiniGoParser.SIGN))) != 0):
                    self.state = 79
                    self.primitive_type()


                self.state = 82
                self.match(MiniGoParser.COMMA)
                self.state = 83
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.INTERGER_LITERAL) | (1 << MiniGoParser.SIGN))) != 0):
                    self.state = 85
                    self.primitive_type()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_struct_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MiniGoParser.TYPE)
            self.state = 91
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 92
            self.match(MiniGoParser.STRUCT)
            self.state = 93
            self.match(MiniGoParser.LBRACE)
            self.state = 94
            self.struct_field()
            self.state = 95
            self.match(MiniGoParser.RBRACE)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NL or _la==MiniGoParser.SEMI:
                self.state = 96
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMI):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def property_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Property_structContext,0)


        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_struct_field)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.property_struct()
                self.state = 100
                self.struct_field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.property_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Property_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_property_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProperty_struct" ):
                return visitor.visitProperty_struct(self)
            else:
                return visitor.visitChildren(self)




    def property_struct(self):

        localctx = MiniGoParser.Property_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_property_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.INTERGER_LITERAL, MiniGoParser.SIGN]:
                self.state = 106
                self.primitive_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.state = 107
                self.match(MiniGoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 110
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMI):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MiniGoParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.dimension()
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.INTERGER_LITERAL, MiniGoParser.SIGN]:
                self.state = 113
                self.primitive_type()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.state = 114
                self.struct_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def dimension(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionContext,0)


        def INTERGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTERGER_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = MiniGoParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dimension)
        self._la = 0 # Token type
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(MiniGoParser.LBRACK)
                self.state = 118
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.INTERGER_LITERAL or _la==MiniGoParser.IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.match(MiniGoParser.RBRACK)
                self.state = 120
                self.dimension()
                pass
            elif token in [MiniGoParser.INTERGER_LITERAL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.INTERGER_LITERAL or _la==MiniGoParser.IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def INTERGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTERGER_LITERAL, 0)

        def SIGN(self):
            return self.getToken(MiniGoParser.SIGN, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MiniGoParser.BOOLEAN_LITERAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(MiniGoParser.STRING_LITERAL)
                pass
            elif token in [MiniGoParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass
            elif token in [MiniGoParser.INTERGER_LITERAL, MiniGoParser.SIGN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SIGN:
                    self.state = 126
                    self.match(MiniGoParser.SIGN)


                self.state = 129
                self.match(MiniGoParser.INTERGER_LITERAL)
                pass
            elif token in [MiniGoParser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.match(MiniGoParser.BOOLEAN_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





