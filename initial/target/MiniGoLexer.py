# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01fe\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\2\7")
        buf.write("\2\u0097\n\2\f\2\16\2\u009a\13\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\7\3\u00a5\n\3\f\3\16\3\u00a8\13\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\5\6\5\u00b1\n\5\r\5\16\5\u00b2\3")
        buf.write("\5\3\5\3\6\6\6\u00b8\n\6\r\6\16\6\u00b9\3\7\3\7\3\b\3")
        buf.write("\b\5\b\u00c0\n\b\3\t\3\t\3\t\7\t\u00c5\n\t\f\t\16\t\u00c8")
        buf.write("\13\t\3\t\3\t\3\n\3\n\3\n\3\13\6\13\u00d0\n\13\r\13\16")
        buf.write("\13\u00d1\3\13\3\13\7\13\u00d6\n\13\f\13\16\13\u00d9\13")
        buf.write("\13\3\13\7\13\u00dc\n\13\f\13\16\13\u00df\13\13\3\13\7")
        buf.write("\13\u00e2\n\13\f\13\16\13\u00e5\13\13\3\f\3\f\7\f\u00e9")
        buf.write("\n\f\f\f\16\f\u00ec\13\f\3\r\3\r\3\r\3\r\5\r\u00f2\n\r")
        buf.write("\3\16\3\16\3\16\7\16\u00f7\n\16\f\16\16\16\u00fa\13\16")
        buf.write("\5\16\u00fc\n\16\3\17\3\17\3\17\3\17\5\17\u0102\n\17\3")
        buf.write("\17\6\17\u0105\n\17\r\17\16\17\u0106\3\20\3\20\3\20\3")
        buf.write("\20\5\20\u010d\n\20\3\20\6\20\u0110\n\20\r\20\16\20\u0111")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u0118\n\21\3\21\6\21\u011b\n")
        buf.write("\21\r\21\16\21\u011c\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3")
        buf.write("&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\38\3")
        buf.write("8\38\38\39\39\39\39\39\3:\3:\3:\3:\3;\3;\3;\3;\3;\3<\3")
        buf.write("<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3")
        buf.write("A\3A\3A\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3D\3D\7D\u01de\n")
        buf.write("D\fD\16D\u01e1\13D\3E\3E\3E\3F\3F\3F\3G\3G\3G\7G\u01ec")
        buf.write("\nG\fG\16G\u01ef\13G\3G\3G\3H\3H\3H\7H\u01f6\nH\fH\16")
        buf.write("H\u01f9\13H\3H\3H\3H\3H\3\u0098\2I\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\2\25\13\27\2\31\f\33\2\35\2\37\2!")
        buf.write("\2#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\27")
        buf.write("9\30;\31=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([")
        buf.write(")]*_+a,c-e.g/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177")
        buf.write(";\u0081<\u0083=\u0085>\u0087?\u0089\2\u008b@\u008dA\u008f")
        buf.write("B\3\2\22\4\2\f\f\17\17\5\2\13\13\16\17\"\"\3\2c|\4\2$")
        buf.write("$^^\7\2$$^^ppttvv\3\2\62;\4\2GGgg\4\2--//\3\2\63;\3\2")
        buf.write("\62\63\3\2\629\5\2\62;CHch\5\2C\\aac|\6\2\62;C\\aac|\n")
        buf.write("\2$$))^^ddhhppttvv\6\2\f\f\17\17$$^^\2\u0213\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\25\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\3\u0091\3\2\2\2\5\u00a0\3\2\2\2\7\u00ab\3\2\2")
        buf.write("\2\t\u00b0\3\2\2\2\13\u00b7\3\2\2\2\r\u00bb\3\2\2\2\17")
        buf.write("\u00bf\3\2\2\2\21\u00c1\3\2\2\2\23\u00cb\3\2\2\2\25\u00cf")
        buf.write("\3\2\2\2\27\u00e6\3\2\2\2\31\u00f1\3\2\2\2\33\u00fb\3")
        buf.write("\2\2\2\35\u0101\3\2\2\2\37\u010c\3\2\2\2!\u0117\3\2\2")
        buf.write("\2#\u011e\3\2\2\2%\u0120\3\2\2\2\'\u0122\3\2\2\2)\u0124")
        buf.write("\3\2\2\2+\u0126\3\2\2\2-\u0128\3\2\2\2/\u012a\3\2\2\2")
        buf.write("\61\u012c\3\2\2\2\63\u012e\3\2\2\2\65\u0130\3\2\2\2\67")
        buf.write("\u0132\3\2\2\29\u0134\3\2\2\2;\u0136\3\2\2\2=\u0138\3")
        buf.write("\2\2\2?\u013b\3\2\2\2A\u013e\3\2\2\2C\u0140\3\2\2\2E\u0143")
        buf.write("\3\2\2\2G\u0145\3\2\2\2I\u0148\3\2\2\2K\u014b\3\2\2\2")
        buf.write("M\u014e\3\2\2\2O\u0150\3\2\2\2Q\u0152\3\2\2\2S\u0155\3")
        buf.write("\2\2\2U\u0158\3\2\2\2W\u015b\3\2\2\2Y\u015e\3\2\2\2[\u0161")
        buf.write("\3\2\2\2]\u0164\3\2\2\2_\u0166\3\2\2\2a\u0169\3\2\2\2")
        buf.write("c\u016e\3\2\2\2e\u0172\3\2\2\2g\u0179\3\2\2\2i\u0183\3")
        buf.write("\2\2\2k\u018a\3\2\2\2m\u0190\3\2\2\2o\u0194\3\2\2\2q\u019b")
        buf.write("\3\2\2\2s\u01a0\3\2\2\2u\u01a4\3\2\2\2w\u01a9\3\2\2\2")
        buf.write("y\u01af\3\2\2\2{\u01b7\3\2\2\2}\u01c0\3\2\2\2\177\u01c6")
        buf.write("\3\2\2\2\u0081\u01cc\3\2\2\2\u0083\u01d1\3\2\2\2\u0085")
        buf.write("\u01d7\3\2\2\2\u0087\u01db\3\2\2\2\u0089\u01e2\3\2\2\2")
        buf.write("\u008b\u01e5\3\2\2\2\u008d\u01e8\3\2\2\2\u008f\u01f2\3")
        buf.write("\2\2\2\u0091\u0092\7\61\2\2\u0092\u0093\7,\2\2\u0093\u0098")
        buf.write("\3\2\2\2\u0094\u0097\5\3\2\2\u0095\u0097\13\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2")
        buf.write("\u0098\u0099\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009b\3")
        buf.write("\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\7,\2\2\u009c\u009d")
        buf.write("\7\61\2\2\u009d\u009e\3\2\2\2\u009e\u009f\b\2\2\2\u009f")
        buf.write("\4\3\2\2\2\u00a0\u00a1\7\61\2\2\u00a1\u00a2\7\61\2\2\u00a2")
        buf.write("\u00a6\3\2\2\2\u00a3\u00a5\n\2\2\2\u00a4\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3")
        buf.write("\2\2\2\u00a7\u00a9\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00aa")
        buf.write("\b\3\2\2\u00aa\6\3\2\2\2\u00ab\u00ac\7\f\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\u00ae\b\4\2\2\u00ae\b\3\2\2\2\u00af\u00b1")
        buf.write("\t\3\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b5\b\5\2\2\u00b5\n\3\2\2\2\u00b6\u00b8\t\4\2")
        buf.write("\2\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00b7")
        buf.write("\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\f\3\2\2\2\u00bb\u00bc")
        buf.write("\5\u0085C\2\u00bc\16\3\2\2\2\u00bd\u00c0\5\u0081A\2\u00be")
        buf.write("\u00c0\5\u0083B\2\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2")
        buf.write("\2\2\u00c0\20\3\2\2\2\u00c1\u00c6\7$\2\2\u00c2\u00c5\5")
        buf.write("\u0089E\2\u00c3\u00c5\n\5\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c6\3")
        buf.write("\2\2\2\u00c9\u00ca\7$\2\2\u00ca\22\3\2\2\2\u00cb\u00cc")
        buf.write("\7^\2\2\u00cc\u00cd\t\6\2\2\u00cd\24\3\2\2\2\u00ce\u00d0")
        buf.write("\t\7\2\2\u00cf\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\3\2\2\2")
        buf.write("\u00d3\u00d7\7\60\2\2\u00d4\u00d6\t\7\2\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00dd\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00da\u00dc\5\27\f\2\u00db\u00da\3\2\2\2\u00dc\u00df")
        buf.write("\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00e3\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e2\t\7\2\2")
        buf.write("\u00e1\u00e0\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3")
        buf.write("\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\26\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e6\u00ea\t\b\2\2\u00e7\u00e9\t\t\2\2\u00e8")
        buf.write("\u00e7\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb\30\3\2\2\2\u00ec\u00ea\3\2")
        buf.write("\2\2\u00ed\u00f2\5\33\16\2\u00ee\u00f2\5\35\17\2\u00ef")
        buf.write("\u00f2\5\37\20\2\u00f0\u00f2\5!\21\2\u00f1\u00ed\3\2\2")
        buf.write("\2\u00f1\u00ee\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f2\32\3\2\2\2\u00f3\u00fc\7\62\2\2\u00f4\u00f8")
        buf.write("\t\n\2\2\u00f5\u00f7\t\7\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00f3\3")
        buf.write("\2\2\2\u00fb\u00f4\3\2\2\2\u00fc\34\3\2\2\2\u00fd\u00fe")
        buf.write("\7\62\2\2\u00fe\u0102\7d\2\2\u00ff\u0100\7\62\2\2\u0100")
        buf.write("\u0102\7D\2\2\u0101\u00fd\3\2\2\2\u0101\u00ff\3\2\2\2")
        buf.write("\u0102\u0104\3\2\2\2\u0103\u0105\t\13\2\2\u0104\u0103")
        buf.write("\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\36\3\2\2\2\u0108\u0109\7\62\2\2\u0109")
        buf.write("\u010d\7q\2\2\u010a\u010b\7\62\2\2\u010b\u010d\7Q\2\2")
        buf.write("\u010c\u0108\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010f\3")
        buf.write("\2\2\2\u010e\u0110\t\f\2\2\u010f\u010e\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write(" \3\2\2\2\u0113\u0114\7\62\2\2\u0114\u0118\7z\2\2\u0115")
        buf.write("\u0116\7\62\2\2\u0116\u0118\7Z\2\2\u0117\u0113\3\2\2\2")
        buf.write("\u0117\u0115\3\2\2\2\u0118\u011a\3\2\2\2\u0119\u011b\t")
        buf.write("\r\2\2\u011a\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011d\"\3\2\2\2\u011e\u011f")
        buf.write("\7*\2\2\u011f$\3\2\2\2\u0120\u0121\7+\2\2\u0121&\3\2\2")
        buf.write("\2\u0122\u0123\7}\2\2\u0123(\3\2\2\2\u0124\u0125\7\177")
        buf.write("\2\2\u0125*\3\2\2\2\u0126\u0127\7]\2\2\u0127,\3\2\2\2")
        buf.write("\u0128\u0129\7_\2\2\u0129.\3\2\2\2\u012a\u012b\7.\2\2")
        buf.write("\u012b\60\3\2\2\2\u012c\u012d\7=\2\2\u012d\62\3\2\2\2")
        buf.write("\u012e\u012f\7-\2\2\u012f\64\3\2\2\2\u0130\u0131\7/\2")
        buf.write("\2\u0131\66\3\2\2\2\u0132\u0133\7,\2\2\u01338\3\2\2\2")
        buf.write("\u0134\u0135\7\61\2\2\u0135:\3\2\2\2\u0136\u0137\7\'\2")
        buf.write("\2\u0137<\3\2\2\2\u0138\u0139\7?\2\2\u0139\u013a\7?\2")
        buf.write("\2\u013a>\3\2\2\2\u013b\u013c\7#\2\2\u013c\u013d\7?\2")
        buf.write("\2\u013d@\3\2\2\2\u013e\u013f\7>\2\2\u013fB\3\2\2\2\u0140")
        buf.write("\u0141\7>\2\2\u0141\u0142\7?\2\2\u0142D\3\2\2\2\u0143")
        buf.write("\u0144\7@\2\2\u0144F\3\2\2\2\u0145\u0146\7@\2\2\u0146")
        buf.write("\u0147\7?\2\2\u0147H\3\2\2\2\u0148\u0149\7(\2\2\u0149")
        buf.write("\u014a\7(\2\2\u014aJ\3\2\2\2\u014b\u014c\7~\2\2\u014c")
        buf.write("\u014d\7~\2\2\u014dL\3\2\2\2\u014e\u014f\7#\2\2\u014f")
        buf.write("N\3\2\2\2\u0150\u0151\7?\2\2\u0151P\3\2\2\2\u0152\u0153")
        buf.write("\7<\2\2\u0153\u0154\7?\2\2\u0154R\3\2\2\2\u0155\u0156")
        buf.write("\7-\2\2\u0156\u0157\7?\2\2\u0157T\3\2\2\2\u0158\u0159")
        buf.write("\7/\2\2\u0159\u015a\7?\2\2\u015aV\3\2\2\2\u015b\u015c")
        buf.write("\7,\2\2\u015c\u015d\7?\2\2\u015dX\3\2\2\2\u015e\u015f")
        buf.write("\7\61\2\2\u015f\u0160\7?\2\2\u0160Z\3\2\2\2\u0161\u0162")
        buf.write("\7\'\2\2\u0162\u0163\7?\2\2\u0163\\\3\2\2\2\u0164\u0165")
        buf.write("\7\60\2\2\u0165^\3\2\2\2\u0166\u0167\7k\2\2\u0167\u0168")
        buf.write("\7h\2\2\u0168`\3\2\2\2\u0169\u016a\7g\2\2\u016a\u016b")
        buf.write("\7n\2\2\u016b\u016c\7u\2\2\u016c\u016d\7g\2\2\u016db\3")
        buf.write("\2\2\2\u016e\u016f\7h\2\2\u016f\u0170\7q\2\2\u0170\u0171")
        buf.write("\7t\2\2\u0171d\3\2\2\2\u0172\u0173\7u\2\2\u0173\u0174")
        buf.write("\7v\2\2\u0174\u0175\7t\2\2\u0175\u0176\7w\2\2\u0176\u0177")
        buf.write("\7e\2\2\u0177\u0178\7v\2\2\u0178f\3\2\2\2\u0179\u017a")
        buf.write("\7k\2\2\u017a\u017b\7p\2\2\u017b\u017c\7v\2\2\u017c\u017d")
        buf.write("\7g\2\2\u017d\u017e\7t\2\2\u017e\u017f\7h\2\2\u017f\u0180")
        buf.write("\7c\2\2\u0180\u0181\7e\2\2\u0181\u0182\7g\2\2\u0182h\3")
        buf.write("\2\2\2\u0183\u0184\7u\2\2\u0184\u0185\7v\2\2\u0185\u0186")
        buf.write("\7t\2\2\u0186\u0187\7k\2\2\u0187\u0188\7p\2\2\u0188\u0189")
        buf.write("\7i\2\2\u0189j\3\2\2\2\u018a\u018b\7e\2\2\u018b\u018c")
        buf.write("\7q\2\2\u018c\u018d\7p\2\2\u018d\u018e\7u\2\2\u018e\u018f")
        buf.write("\7v\2\2\u018fl\3\2\2\2\u0190\u0191\7x\2\2\u0191\u0192")
        buf.write("\7c\2\2\u0192\u0193\7t\2\2\u0193n\3\2\2\2\u0194\u0195")
        buf.write("\7t\2\2\u0195\u0196\7g\2\2\u0196\u0197\7v\2\2\u0197\u0198")
        buf.write("\7w\2\2\u0198\u0199\7t\2\2\u0199\u019a\7p\2\2\u019ap\3")
        buf.write("\2\2\2\u019b\u019c\7h\2\2\u019c\u019d\7w\2\2\u019d\u019e")
        buf.write("\7p\2\2\u019e\u019f\7e\2\2\u019fr\3\2\2\2\u01a0\u01a1")
        buf.write("\7k\2\2\u01a1\u01a2\7p\2\2\u01a2\u01a3\7v\2\2\u01a3t\3")
        buf.write("\2\2\2\u01a4\u01a5\7v\2\2\u01a5\u01a6\7{\2\2\u01a6\u01a7")
        buf.write("\7r\2\2\u01a7\u01a8\7g\2\2\u01a8v\3\2\2\2\u01a9\u01aa")
        buf.write("\7h\2\2\u01aa\u01ab\7n\2\2\u01ab\u01ac\7q\2\2\u01ac\u01ad")
        buf.write("\7c\2\2\u01ad\u01ae\7v\2\2\u01aex\3\2\2\2\u01af\u01b0")
        buf.write("\7d\2\2\u01b0\u01b1\7q\2\2\u01b1\u01b2\7q\2\2\u01b2\u01b3")
        buf.write("\7n\2\2\u01b3\u01b4\7g\2\2\u01b4\u01b5\7c\2\2\u01b5\u01b6")
        buf.write("\7p\2\2\u01b6z\3\2\2\2\u01b7\u01b8\7e\2\2\u01b8\u01b9")
        buf.write("\7q\2\2\u01b9\u01ba\7p\2\2\u01ba\u01bb\7v\2\2\u01bb\u01bc")
        buf.write("\7k\2\2\u01bc\u01bd\7p\2\2\u01bd\u01be\7w\2\2\u01be\u01bf")
        buf.write("\7g\2\2\u01bf|\3\2\2\2\u01c0\u01c1\7d\2\2\u01c1\u01c2")
        buf.write("\7t\2\2\u01c2\u01c3\7g\2\2\u01c3\u01c4\7c\2\2\u01c4\u01c5")
        buf.write("\7m\2\2\u01c5~\3\2\2\2\u01c6\u01c7\7t\2\2\u01c7\u01c8")
        buf.write("\7c\2\2\u01c8\u01c9\7p\2\2\u01c9\u01ca\7i\2\2\u01ca\u01cb")
        buf.write("\7g\2\2\u01cb\u0080\3\2\2\2\u01cc\u01cd\7v\2\2\u01cd\u01ce")
        buf.write("\7t\2\2\u01ce\u01cf\7w\2\2\u01cf\u01d0\7g\2\2\u01d0\u0082")
        buf.write("\3\2\2\2\u01d1\u01d2\7h\2\2\u01d2\u01d3\7c\2\2\u01d3\u01d4")
        buf.write("\7n\2\2\u01d4\u01d5\7u\2\2\u01d5\u01d6\7g\2\2\u01d6\u0084")
        buf.write("\3\2\2\2\u01d7\u01d8\7p\2\2\u01d8\u01d9\7k\2\2\u01d9\u01da")
        buf.write("\7n\2\2\u01da\u0086\3\2\2\2\u01db\u01df\t\16\2\2\u01dc")
        buf.write("\u01de\t\17\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e1\3\2\2")
        buf.write("\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u0088")
        buf.write("\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e3\7^\2\2\u01e3")
        buf.write("\u01e4\t\20\2\2\u01e4\u008a\3\2\2\2\u01e5\u01e6\13\2\2")
        buf.write("\2\u01e6\u01e7\bF\3\2\u01e7\u008c\3\2\2\2\u01e8\u01ed")
        buf.write("\7$\2\2\u01e9\u01ec\5\u0089E\2\u01ea\u01ec\n\21\2\2\u01eb")
        buf.write("\u01e9\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2")
        buf.write("\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f0\3")
        buf.write("\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f1\bG\4\2\u01f1\u008e")
        buf.write("\3\2\2\2\u01f2\u01f7\7$\2\2\u01f3\u01f6\5\u0089E\2\u01f4")
        buf.write("\u01f6\n\21\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f4\3\2\2")
        buf.write("\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8")
        buf.write("\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa")
        buf.write("\u01fb\7^\2\2\u01fb\u01fc\n\20\2\2\u01fc\u01fd\bH\5\2")
        buf.write("\u01fd\u0090\3\2\2\2\36\2\u0096\u0098\u00a6\u00b2\u00b9")
        buf.write("\u00bf\u00c4\u00c6\u00d1\u00d7\u00dd\u00e3\u00ea\u00f1")
        buf.write("\u00f8\u00fb\u0101\u0106\u010c\u0111\u0117\u011c\u01df")
        buf.write("\u01eb\u01ed\u01f5\u01f7\6\b\2\2\3F\2\3G\3\3H\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ML_COMMENT = 1
    SL_COMMENT = 2
    NL = 3
    WS = 4
    ID = 5
    NIL_LITERAL = 6
    BOOLEAN_LITERAL = 7
    STRING_LITERAL = 8
    FLOAT_LITERAL = 9
    INTERGER_LITERAL = 10
    LPAREN = 11
    RPAREN = 12
    LBRACE = 13
    RBRACE = 14
    LBRACK = 15
    RBRACK = 16
    COMMA = 17
    SEMI = 18
    ADD = 19
    SUB = 20
    MUL = 21
    DIV = 22
    MOD = 23
    EQ = 24
    NEQ = 25
    LT = 26
    LE = 27
    GT = 28
    GE = 29
    AND = 30
    OR = 31
    NOT = 32
    ASSIGN = 33
    COLON_ASSIGN = 34
    ADD_ASSIGN = 35
    SUB_ASSIGN = 36
    MUL_ASSIGN = 37
    DIV_ASSIGN = 38
    MOD_ASSIGN = 39
    DOT = 40
    IF = 41
    ELSE = 42
    FOR = 43
    STRUCT = 44
    INTERFACE = 45
    STRING = 46
    CONST = 47
    VAR = 48
    RETURN = 49
    FUNC = 50
    INT = 51
    TYPE = 52
    FLOAT = 53
    BOOLEAN = 54
    CONTINUE = 55
    BREAK = 56
    RANGE = 57
    TRUE = 58
    FALSE = 59
    NIL = 60
    IDENTIFIER = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", "':='", "'+='", 
            "'-='", "'*='", "'/='", "'%='", "'.'", "'if'", "'else'", "'for'", 
            "'struct'", "'interface'", "'string'", "'const'", "'var'", "'return'", 
            "'func'", "'int'", "'type'", "'float'", "'boolean'", "'continue'", 
            "'break'", "'range'", "'true'", "'false'", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "ML_COMMENT", "SL_COMMENT", "NL", "WS", "ID", "NIL_LITERAL", 
            "BOOLEAN_LITERAL", "STRING_LITERAL", "FLOAT_LITERAL", "INTERGER_LITERAL", 
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "COMMA", "SEMI", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", 
            "LT", "LE", "GT", "GE", "AND", "OR", "NOT", "ASSIGN", "COLON_ASSIGN", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "IF", "ELSE", "FOR", "STRUCT", "INTERFACE", "STRING", 
            "CONST", "VAR", "RETURN", "FUNC", "INT", "TYPE", "FLOAT", "BOOLEAN", 
            "CONTINUE", "BREAK", "RANGE", "TRUE", "FALSE", "NIL", "IDENTIFIER", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ML_COMMENT", "SL_COMMENT", "NL", "WS", "ID", "NIL_LITERAL", 
                  "BOOLEAN_LITERAL", "STRING_LITERAL", "ESC_SEQ", "FLOAT_LITERAL", 
                  "EXP", "INTERGER_LITERAL", "DEC", "BIN", "OCT", "HEX", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                  "COMMA", "SEMI", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
                  "NEQ", "LT", "LE", "GT", "GE", "AND", "OR", "NOT", "ASSIGN", 
                  "COLON_ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                  "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "IF", "ELSE", "FOR", 
                  "STRUCT", "INTERFACE", "STRING", "CONST", "VAR", "RETURN", 
                  "FUNC", "INT", "TYPE", "FLOAT", "BOOLEAN", "CONTINUE", 
                  "BREAK", "RANGE", "TRUE", "FALSE", "NIL", "IDENTIFIER", 
                  "ESC", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[68] = self.ERROR_CHAR_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             raise ErrorToken(self.text) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             raise UncloseString(self.text[1:]) 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise IllegalEscape(self.text[1:]) 
     


