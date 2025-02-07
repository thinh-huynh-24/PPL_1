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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0202\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\7\2\u0099\n\2\f\2\16\2\u009c\13\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\7\3\u00a7\n\3\f\3\16\3\u00aa\13\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\5\6\5\u00b3\n\5\r\5\16\5\u00b4")
        buf.write("\3\5\3\5\3\6\6\6\u00ba\n\6\r\6\16\6\u00bb\3\7\3\7\3\b")
        buf.write("\3\b\5\b\u00c2\n\b\3\t\3\t\3\t\7\t\u00c7\n\t\f\t\16\t")
        buf.write("\u00ca\13\t\3\t\3\t\3\n\3\n\3\n\3\13\6\13\u00d2\n\13\r")
        buf.write("\13\16\13\u00d3\3\13\3\13\7\13\u00d8\n\13\f\13\16\13\u00db")
        buf.write("\13\13\3\13\7\13\u00de\n\13\f\13\16\13\u00e1\13\13\3\13")
        buf.write("\7\13\u00e4\n\13\f\13\16\13\u00e7\13\13\3\f\3\f\7\f\u00eb")
        buf.write("\n\f\f\f\16\f\u00ee\13\f\3\r\3\r\3\r\3\r\5\r\u00f4\n\r")
        buf.write("\3\16\3\16\3\16\7\16\u00f9\n\16\f\16\16\16\u00fc\13\16")
        buf.write("\5\16\u00fe\n\16\3\17\3\17\3\17\3\17\5\17\u0104\n\17\3")
        buf.write("\17\6\17\u0107\n\17\r\17\16\17\u0108\3\20\3\20\3\20\3")
        buf.write("\20\5\20\u010f\n\20\3\20\6\20\u0112\n\20\r\20\16\20\u0113")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u011a\n\21\3\21\6\21\u011d\n")
        buf.write("\21\r\21\16\21\u011e\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&")
        buf.write("\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\3")
        buf.write("9\39\39\39\3:\3:\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3<\3")
        buf.write("=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3B\3")
        buf.write("B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3D\3D\3D\3D\3E\3E\7E\u01e2")
        buf.write("\nE\fE\16E\u01e5\13E\3F\3F\3F\3G\3G\3G\3H\3H\3H\7H\u01f0")
        buf.write("\nH\fH\16H\u01f3\13H\3H\3H\3I\3I\3I\7I\u01fa\nI\fI\16")
        buf.write("I\u01fd\13I\3I\3I\3I\3I\3\u009a\2J\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\2\25\13\27\2\31\f\33\2\35\2\37\2!")
        buf.write("\2#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\27")
        buf.write("9\30;\31=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([")
        buf.write(")]*_+a,c-e.g/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177")
        buf.write(";\u0081<\u0083=\u0085>\u0087?\u0089@\u008b\2\u008dA\u008f")
        buf.write("B\u0091C\3\2\22\4\2\f\f\17\17\5\2\13\13\16\17\"\"\3\2")
        buf.write("c|\4\2$$^^\7\2$$^^ppttvv\3\2\62;\4\2GGgg\4\2--//\3\2\63")
        buf.write(";\3\2\62\63\3\2\629\5\2\62;CHch\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\n\2$$))^^ddhhppttvv\6\2\f\f\17\17$$^^\2\u0217\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u00a2\3\2\2")
        buf.write("\2\7\u00ad\3\2\2\2\t\u00b2\3\2\2\2\13\u00b9\3\2\2\2\r")
        buf.write("\u00bd\3\2\2\2\17\u00c1\3\2\2\2\21\u00c3\3\2\2\2\23\u00cd")
        buf.write("\3\2\2\2\25\u00d1\3\2\2\2\27\u00e8\3\2\2\2\31\u00f3\3")
        buf.write("\2\2\2\33\u00fd\3\2\2\2\35\u0103\3\2\2\2\37\u010e\3\2")
        buf.write("\2\2!\u0119\3\2\2\2#\u0120\3\2\2\2%\u0122\3\2\2\2\'\u0124")
        buf.write("\3\2\2\2)\u0126\3\2\2\2+\u0128\3\2\2\2-\u012a\3\2\2\2")
        buf.write("/\u012c\3\2\2\2\61\u012e\3\2\2\2\63\u0130\3\2\2\2\65\u0132")
        buf.write("\3\2\2\2\67\u0134\3\2\2\29\u0136\3\2\2\2;\u0138\3\2\2")
        buf.write("\2=\u013a\3\2\2\2?\u013c\3\2\2\2A\u013f\3\2\2\2C\u0142")
        buf.write("\3\2\2\2E\u0144\3\2\2\2G\u0147\3\2\2\2I\u0149\3\2\2\2")
        buf.write("K\u014c\3\2\2\2M\u014f\3\2\2\2O\u0152\3\2\2\2Q\u0154\3")
        buf.write("\2\2\2S\u0156\3\2\2\2U\u0159\3\2\2\2W\u015c\3\2\2\2Y\u015f")
        buf.write("\3\2\2\2[\u0162\3\2\2\2]\u0165\3\2\2\2_\u0168\3\2\2\2")
        buf.write("a\u016a\3\2\2\2c\u016d\3\2\2\2e\u0172\3\2\2\2g\u0176\3")
        buf.write("\2\2\2i\u017d\3\2\2\2k\u0187\3\2\2\2m\u018e\3\2\2\2o\u0194")
        buf.write("\3\2\2\2q\u0198\3\2\2\2s\u019f\3\2\2\2u\u01a4\3\2\2\2")
        buf.write("w\u01a8\3\2\2\2y\u01ad\3\2\2\2{\u01b3\3\2\2\2}\u01bb\3")
        buf.write("\2\2\2\177\u01c4\3\2\2\2\u0081\u01ca\3\2\2\2\u0083\u01d0")
        buf.write("\3\2\2\2\u0085\u01d5\3\2\2\2\u0087\u01db\3\2\2\2\u0089")
        buf.write("\u01df\3\2\2\2\u008b\u01e6\3\2\2\2\u008d\u01e9\3\2\2\2")
        buf.write("\u008f\u01ec\3\2\2\2\u0091\u01f6\3\2\2\2\u0093\u0094\7")
        buf.write("\61\2\2\u0094\u0095\7,\2\2\u0095\u009a\3\2\2\2\u0096\u0099")
        buf.write("\5\3\2\2\u0097\u0099\13\2\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009a\3")
        buf.write("\2\2\2\u009d\u009e\7,\2\2\u009e\u009f\7\61\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\u00a1\b\2\2\2\u00a1\4\3\2\2\2\u00a2\u00a3")
        buf.write("\7\61\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a8\3\2\2\2\u00a5")
        buf.write("\u00a7\n\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2")
        buf.write("\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab\3")
        buf.write("\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ac\b\3\2\2\u00ac\6")
        buf.write("\3\2\2\2\u00ad\u00ae\7\f\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00b0\b\4\2\2\u00b0\b\3\2\2\2\u00b1\u00b3\t\3\2\2\u00b2")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2")
        buf.write("\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\b")
        buf.write("\5\2\2\u00b7\n\3\2\2\2\u00b8\u00ba\t\4\2\2\u00b9\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb")
        buf.write("\u00bc\3\2\2\2\u00bc\f\3\2\2\2\u00bd\u00be\5\u0087D\2")
        buf.write("\u00be\16\3\2\2\2\u00bf\u00c2\5\u0083B\2\u00c0\u00c2\5")
        buf.write("\u0085C\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2")
        buf.write("\20\3\2\2\2\u00c3\u00c8\7$\2\2\u00c4\u00c7\5\u008bF\2")
        buf.write("\u00c5\u00c7\n\5\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3")
        buf.write("\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9")
        buf.write("\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb")
        buf.write("\u00cc\7$\2\2\u00cc\22\3\2\2\2\u00cd\u00ce\7^\2\2\u00ce")
        buf.write("\u00cf\t\6\2\2\u00cf\24\3\2\2\2\u00d0\u00d2\t\7\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d9\7")
        buf.write("\60\2\2\u00d6\u00d8\t\7\2\2\u00d7\u00d6\3\2\2\2\u00d8")
        buf.write("\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\u00df\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00de\5")
        buf.write("\27\f\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e5\3\2\2\2")
        buf.write("\u00e1\u00df\3\2\2\2\u00e2\u00e4\t\7\2\2\u00e3\u00e2\3")
        buf.write("\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6\26\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00ec")
        buf.write("\t\b\2\2\u00e9\u00eb\t\t\2\2\u00ea\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\30\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f4\5\33")
        buf.write("\16\2\u00f0\u00f4\5\35\17\2\u00f1\u00f4\5\37\20\2\u00f2")
        buf.write("\u00f4\5!\21\2\u00f3\u00ef\3\2\2\2\u00f3\u00f0\3\2\2\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4\32\3\2")
        buf.write("\2\2\u00f5\u00fe\7\62\2\2\u00f6\u00fa\t\n\2\2\u00f7\u00f9")
        buf.write("\t\7\2\2\u00f8\u00f7\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fe\3\2\2\2")
        buf.write("\u00fc\u00fa\3\2\2\2\u00fd\u00f5\3\2\2\2\u00fd\u00f6\3")
        buf.write("\2\2\2\u00fe\34\3\2\2\2\u00ff\u0100\7\62\2\2\u0100\u0104")
        buf.write("\7d\2\2\u0101\u0102\7\62\2\2\u0102\u0104\7D\2\2\u0103")
        buf.write("\u00ff\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0106\3\2\2\2")
        buf.write("\u0105\u0107\t\13\2\2\u0106\u0105\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("\36\3\2\2\2\u010a\u010b\7\62\2\2\u010b\u010f\7q\2\2\u010c")
        buf.write("\u010d\7\62\2\2\u010d\u010f\7Q\2\2\u010e\u010a\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u0112\t")
        buf.write("\f\2\2\u0111\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0111")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114 \3\2\2\2\u0115\u0116")
        buf.write("\7\62\2\2\u0116\u011a\7z\2\2\u0117\u0118\7\62\2\2\u0118")
        buf.write("\u011a\7Z\2\2\u0119\u0115\3\2\2\2\u0119\u0117\3\2\2\2")
        buf.write("\u011a\u011c\3\2\2\2\u011b\u011d\t\r\2\2\u011c\u011b\3")
        buf.write("\2\2\2\u011d\u011e\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f")
        buf.write("\3\2\2\2\u011f\"\3\2\2\2\u0120\u0121\t\t\2\2\u0121$\3")
        buf.write("\2\2\2\u0122\u0123\7*\2\2\u0123&\3\2\2\2\u0124\u0125\7")
        buf.write("+\2\2\u0125(\3\2\2\2\u0126\u0127\7}\2\2\u0127*\3\2\2\2")
        buf.write("\u0128\u0129\7\177\2\2\u0129,\3\2\2\2\u012a\u012b\7]\2")
        buf.write("\2\u012b.\3\2\2\2\u012c\u012d\7_\2\2\u012d\60\3\2\2\2")
        buf.write("\u012e\u012f\7.\2\2\u012f\62\3\2\2\2\u0130\u0131\7=\2")
        buf.write("\2\u0131\64\3\2\2\2\u0132\u0133\7-\2\2\u0133\66\3\2\2")
        buf.write("\2\u0134\u0135\7/\2\2\u01358\3\2\2\2\u0136\u0137\7,\2")
        buf.write("\2\u0137:\3\2\2\2\u0138\u0139\7\61\2\2\u0139<\3\2\2\2")
        buf.write("\u013a\u013b\7\'\2\2\u013b>\3\2\2\2\u013c\u013d\7?\2\2")
        buf.write("\u013d\u013e\7?\2\2\u013e@\3\2\2\2\u013f\u0140\7#\2\2")
        buf.write("\u0140\u0141\7?\2\2\u0141B\3\2\2\2\u0142\u0143\7>\2\2")
        buf.write("\u0143D\3\2\2\2\u0144\u0145\7>\2\2\u0145\u0146\7?\2\2")
        buf.write("\u0146F\3\2\2\2\u0147\u0148\7@\2\2\u0148H\3\2\2\2\u0149")
        buf.write("\u014a\7@\2\2\u014a\u014b\7?\2\2\u014bJ\3\2\2\2\u014c")
        buf.write("\u014d\7(\2\2\u014d\u014e\7(\2\2\u014eL\3\2\2\2\u014f")
        buf.write("\u0150\7~\2\2\u0150\u0151\7~\2\2\u0151N\3\2\2\2\u0152")
        buf.write("\u0153\7#\2\2\u0153P\3\2\2\2\u0154\u0155\7?\2\2\u0155")
        buf.write("R\3\2\2\2\u0156\u0157\7<\2\2\u0157\u0158\7?\2\2\u0158")
        buf.write("T\3\2\2\2\u0159\u015a\7-\2\2\u015a\u015b\7?\2\2\u015b")
        buf.write("V\3\2\2\2\u015c\u015d\7/\2\2\u015d\u015e\7?\2\2\u015e")
        buf.write("X\3\2\2\2\u015f\u0160\7,\2\2\u0160\u0161\7?\2\2\u0161")
        buf.write("Z\3\2\2\2\u0162\u0163\7\61\2\2\u0163\u0164\7?\2\2\u0164")
        buf.write("\\\3\2\2\2\u0165\u0166\7\'\2\2\u0166\u0167\7?\2\2\u0167")
        buf.write("^\3\2\2\2\u0168\u0169\7\60\2\2\u0169`\3\2\2\2\u016a\u016b")
        buf.write("\7k\2\2\u016b\u016c\7h\2\2\u016cb\3\2\2\2\u016d\u016e")
        buf.write("\7g\2\2\u016e\u016f\7n\2\2\u016f\u0170\7u\2\2\u0170\u0171")
        buf.write("\7g\2\2\u0171d\3\2\2\2\u0172\u0173\7h\2\2\u0173\u0174")
        buf.write("\7q\2\2\u0174\u0175\7t\2\2\u0175f\3\2\2\2\u0176\u0177")
        buf.write("\7u\2\2\u0177\u0178\7v\2\2\u0178\u0179\7t\2\2\u0179\u017a")
        buf.write("\7w\2\2\u017a\u017b\7e\2\2\u017b\u017c\7v\2\2\u017ch\3")
        buf.write("\2\2\2\u017d\u017e\7k\2\2\u017e\u017f\7p\2\2\u017f\u0180")
        buf.write("\7v\2\2\u0180\u0181\7g\2\2\u0181\u0182\7t\2\2\u0182\u0183")
        buf.write("\7h\2\2\u0183\u0184\7c\2\2\u0184\u0185\7e\2\2\u0185\u0186")
        buf.write("\7g\2\2\u0186j\3\2\2\2\u0187\u0188\7u\2\2\u0188\u0189")
        buf.write("\7v\2\2\u0189\u018a\7t\2\2\u018a\u018b\7k\2\2\u018b\u018c")
        buf.write("\7p\2\2\u018c\u018d\7i\2\2\u018dl\3\2\2\2\u018e\u018f")
        buf.write("\7e\2\2\u018f\u0190\7q\2\2\u0190\u0191\7p\2\2\u0191\u0192")
        buf.write("\7u\2\2\u0192\u0193\7v\2\2\u0193n\3\2\2\2\u0194\u0195")
        buf.write("\7x\2\2\u0195\u0196\7c\2\2\u0196\u0197\7t\2\2\u0197p\3")
        buf.write("\2\2\2\u0198\u0199\7t\2\2\u0199\u019a\7g\2\2\u019a\u019b")
        buf.write("\7v\2\2\u019b\u019c\7w\2\2\u019c\u019d\7t\2\2\u019d\u019e")
        buf.write("\7p\2\2\u019er\3\2\2\2\u019f\u01a0\7h\2\2\u01a0\u01a1")
        buf.write("\7w\2\2\u01a1\u01a2\7p\2\2\u01a2\u01a3\7e\2\2\u01a3t\3")
        buf.write("\2\2\2\u01a4\u01a5\7k\2\2\u01a5\u01a6\7p\2\2\u01a6\u01a7")
        buf.write("\7v\2\2\u01a7v\3\2\2\2\u01a8\u01a9\7v\2\2\u01a9\u01aa")
        buf.write("\7{\2\2\u01aa\u01ab\7r\2\2\u01ab\u01ac\7g\2\2\u01acx\3")
        buf.write("\2\2\2\u01ad\u01ae\7h\2\2\u01ae\u01af\7n\2\2\u01af\u01b0")
        buf.write("\7q\2\2\u01b0\u01b1\7c\2\2\u01b1\u01b2\7v\2\2\u01b2z\3")
        buf.write("\2\2\2\u01b3\u01b4\7d\2\2\u01b4\u01b5\7q\2\2\u01b5\u01b6")
        buf.write("\7q\2\2\u01b6\u01b7\7n\2\2\u01b7\u01b8\7g\2\2\u01b8\u01b9")
        buf.write("\7c\2\2\u01b9\u01ba\7p\2\2\u01ba|\3\2\2\2\u01bb\u01bc")
        buf.write("\7e\2\2\u01bc\u01bd\7q\2\2\u01bd\u01be\7p\2\2\u01be\u01bf")
        buf.write("\7v\2\2\u01bf\u01c0\7k\2\2\u01c0\u01c1\7p\2\2\u01c1\u01c2")
        buf.write("\7w\2\2\u01c2\u01c3\7g\2\2\u01c3~\3\2\2\2\u01c4\u01c5")
        buf.write("\7d\2\2\u01c5\u01c6\7t\2\2\u01c6\u01c7\7g\2\2\u01c7\u01c8")
        buf.write("\7c\2\2\u01c8\u01c9\7m\2\2\u01c9\u0080\3\2\2\2\u01ca\u01cb")
        buf.write("\7t\2\2\u01cb\u01cc\7c\2\2\u01cc\u01cd\7p\2\2\u01cd\u01ce")
        buf.write("\7i\2\2\u01ce\u01cf\7g\2\2\u01cf\u0082\3\2\2\2\u01d0\u01d1")
        buf.write("\7v\2\2\u01d1\u01d2\7t\2\2\u01d2\u01d3\7w\2\2\u01d3\u01d4")
        buf.write("\7g\2\2\u01d4\u0084\3\2\2\2\u01d5\u01d6\7h\2\2\u01d6\u01d7")
        buf.write("\7c\2\2\u01d7\u01d8\7n\2\2\u01d8\u01d9\7u\2\2\u01d9\u01da")
        buf.write("\7g\2\2\u01da\u0086\3\2\2\2\u01db\u01dc\7p\2\2\u01dc\u01dd")
        buf.write("\7k\2\2\u01dd\u01de\7n\2\2\u01de\u0088\3\2\2\2\u01df\u01e3")
        buf.write("\t\16\2\2\u01e0\u01e2\t\17\2\2\u01e1\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e4\u008a\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7\7")
        buf.write("^\2\2\u01e7\u01e8\t\20\2\2\u01e8\u008c\3\2\2\2\u01e9\u01ea")
        buf.write("\13\2\2\2\u01ea\u01eb\bG\3\2\u01eb\u008e\3\2\2\2\u01ec")
        buf.write("\u01f1\7$\2\2\u01ed\u01f0\5\u008bF\2\u01ee\u01f0\n\21")
        buf.write("\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f3")
        buf.write("\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2")
        buf.write("\u01f4\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f5\bH\4\2")
        buf.write("\u01f5\u0090\3\2\2\2\u01f6\u01fb\7$\2\2\u01f7\u01fa\5")
        buf.write("\u008bF\2\u01f8\u01fa\n\21\2\2\u01f9\u01f7\3\2\2\2\u01f9")
        buf.write("\u01f8\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2")
        buf.write("\u01fb\u01fc\3\2\2\2\u01fc\u01fe\3\2\2\2\u01fd\u01fb\3")
        buf.write("\2\2\2\u01fe\u01ff\7^\2\2\u01ff\u0200\n\20\2\2\u0200\u0201")
        buf.write("\bI\5\2\u0201\u0092\3\2\2\2\36\2\u0098\u009a\u00a8\u00b4")
        buf.write("\u00bb\u00c1\u00c6\u00c8\u00d3\u00d9\u00df\u00e5\u00ec")
        buf.write("\u00f3\u00fa\u00fd\u0103\u0108\u010e\u0113\u0119\u011e")
        buf.write("\u01e3\u01ef\u01f1\u01f9\u01fb\6\b\2\2\3G\2\3H\3\3I\4")
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
    SIGN = 11
    LPAREN = 12
    RPAREN = 13
    LBRACE = 14
    RBRACE = 15
    LBRACK = 16
    RBRACK = 17
    COMMA = 18
    SEMI = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    MOD = 24
    EQ = 25
    NEQ = 26
    LT = 27
    LE = 28
    GT = 29
    GE = 30
    AND = 31
    OR = 32
    NOT = 33
    ASSIGN = 34
    COLON_ASSIGN = 35
    ADD_ASSIGN = 36
    SUB_ASSIGN = 37
    MUL_ASSIGN = 38
    DIV_ASSIGN = 39
    MOD_ASSIGN = 40
    DOT = 41
    IF = 42
    ELSE = 43
    FOR = 44
    STRUCT = 45
    INTERFACE = 46
    STRING = 47
    CONST = 48
    VAR = 49
    RETURN = 50
    FUNC = 51
    INT = 52
    TYPE = 53
    FLOAT = 54
    BOOLEAN = 55
    CONTINUE = 56
    BREAK = 57
    RANGE = 58
    TRUE = 59
    FALSE = 60
    NIL = 61
    IDENTIFIER = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65

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
            "SIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
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
                  "SIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                  "RBRACK", "COMMA", "SEMI", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR", 
                  "NOT", "ASSIGN", "COLON_ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "IF", 
                  "ELSE", "FOR", "STRUCT", "INTERFACE", "STRING", "CONST", 
                  "VAR", "RETURN", "FUNC", "INT", "TYPE", "FLOAT", "BOOLEAN", 
                  "CONTINUE", "BREAK", "RANGE", "TRUE", "FALSE", "NIL", 
                  "IDENTIFIER", "ESC", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
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
     


