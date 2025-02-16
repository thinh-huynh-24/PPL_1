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
        buf.write("\u01fa\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\2\3\2\3\2\7\2\u009b\n\2\f\2\16\2\u009e\13\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00ab\n\4\f\4")
        buf.write("\16\4\u00ae\13\4\3\4\3\4\3\5\6\5\u00b3\n\5\r\5\16\5\u00b4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\5\b\u00c1\n\b")
        buf.write("\3\t\3\t\3\t\7\t\u00c6\n\t\f\t\16\t\u00c9\13\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\6\13\u00d1\n\13\r\13\16\13\u00d2\3\13")
        buf.write("\3\13\7\13\u00d7\n\13\f\13\16\13\u00da\13\13\3\13\5\13")
        buf.write("\u00dd\n\13\3\f\3\f\5\f\u00e1\n\f\3\f\6\f\u00e4\n\f\r")
        buf.write("\f\16\f\u00e5\3\r\3\r\3\r\3\r\5\r\u00ec\n\r\3\16\3\16")
        buf.write("\3\16\7\16\u00f1\n\16\f\16\16\16\u00f4\13\16\5\16\u00f6")
        buf.write("\n\16\3\17\3\17\3\17\3\17\5\17\u00fc\n\17\3\17\6\17\u00ff")
        buf.write("\n\17\r\17\16\17\u0100\3\20\3\20\3\20\3\20\5\20\u0107")
        buf.write("\n\20\3\20\6\20\u010a\n\20\r\20\16\20\u010b\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u0112\n\21\3\21\6\21\u0115\n\21\r\21\16")
        buf.write("\21\u0116\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\39\39\39\39")
        buf.write("\3:\3:\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3<\3=\3=\3=\3")
        buf.write("=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3")
        buf.write("B\3C\3C\3C\3C\3C\3C\3D\3D\3D\3D\3E\3E\7E\u01da\nE\fE\16")
        buf.write("E\u01dd\13E\3F\3F\3F\3G\3G\3G\3H\3H\3H\7H\u01e8\nH\fH")
        buf.write("\16H\u01eb\13H\3H\3H\3I\3I\3I\7I\u01f2\nI\fI\16I\u01f5")
        buf.write("\13I\3I\3I\3I\3I\2\2J\3\2\5\3\7\4\t\5\13\6\r\7\17\b\21")
        buf.write("\t\23\2\25\n\27\2\31\13\33\2\35\2\37\2!\2#\f%\r\'\16)")
        buf.write("\17+\20-\21/\22\61\23\63\24\65\25\67\269\27;\30=\31?\32")
        buf.write("A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a+c,e-g.i")
        buf.write("/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177:\u0081;\u0083")
        buf.write("<\u0085=\u0087>\u0089?\u008b\2\u008d@\u008fA\u0091B\3")
        buf.write("\2\23\4\2,,\61\61\3\2\61\61\4\2\f\f\17\17\5\2\n\13\16")
        buf.write("\17\"\"\4\2$$^^\7\2$$^^ppttvv\3\2\62;\4\2GGgg\4\2--//")
        buf.write("\3\2\63;\3\2\62\63\3\2\629\5\2\62;CHch\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\n\2$$))^^ddhhppttvv\6\2\f\f\17\17$$^^\2\u020e")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\25\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2")
        buf.write("+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2")
        buf.write("\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2")
        buf.write("=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2")
        buf.write("\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2")
        buf.write("\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2")
        buf.write("\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3")
        buf.write("\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m")
        buf.write("\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2")
        buf.write("w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u00a2\3\2\2\2\7\u00a6")
        buf.write("\3\2\2\2\t\u00b2\3\2\2\2\13\u00b8\3\2\2\2\r\u00bc\3\2")
        buf.write("\2\2\17\u00c0\3\2\2\2\21\u00c2\3\2\2\2\23\u00cc\3\2\2")
        buf.write("\2\25\u00d0\3\2\2\2\27\u00de\3\2\2\2\31\u00eb\3\2\2\2")
        buf.write("\33\u00f5\3\2\2\2\35\u00fb\3\2\2\2\37\u0106\3\2\2\2!\u0111")
        buf.write("\3\2\2\2#\u0118\3\2\2\2%\u011a\3\2\2\2\'\u011c\3\2\2\2")
        buf.write(")\u011e\3\2\2\2+\u0120\3\2\2\2-\u0122\3\2\2\2/\u0124\3")
        buf.write("\2\2\2\61\u0126\3\2\2\2\63\u0128\3\2\2\2\65\u012a\3\2")
        buf.write("\2\2\67\u012c\3\2\2\29\u012e\3\2\2\2;\u0130\3\2\2\2=\u0132")
        buf.write("\3\2\2\2?\u0134\3\2\2\2A\u0137\3\2\2\2C\u013a\3\2\2\2")
        buf.write("E\u013c\3\2\2\2G\u013f\3\2\2\2I\u0141\3\2\2\2K\u0144\3")
        buf.write("\2\2\2M\u0147\3\2\2\2O\u014a\3\2\2\2Q\u014c\3\2\2\2S\u014e")
        buf.write("\3\2\2\2U\u0151\3\2\2\2W\u0154\3\2\2\2Y\u0157\3\2\2\2")
        buf.write("[\u015a\3\2\2\2]\u015d\3\2\2\2_\u0160\3\2\2\2a\u0162\3")
        buf.write("\2\2\2c\u0165\3\2\2\2e\u016a\3\2\2\2g\u016e\3\2\2\2i\u0175")
        buf.write("\3\2\2\2k\u017f\3\2\2\2m\u0186\3\2\2\2o\u018c\3\2\2\2")
        buf.write("q\u0190\3\2\2\2s\u0197\3\2\2\2u\u019c\3\2\2\2w\u01a0\3")
        buf.write("\2\2\2y\u01a5\3\2\2\2{\u01ab\3\2\2\2}\u01b3\3\2\2\2\177")
        buf.write("\u01bc\3\2\2\2\u0081\u01c2\3\2\2\2\u0083\u01c8\3\2\2\2")
        buf.write("\u0085\u01cd\3\2\2\2\u0087\u01d3\3\2\2\2\u0089\u01d7\3")
        buf.write("\2\2\2\u008b\u01de\3\2\2\2\u008d\u01e1\3\2\2\2\u008f\u01e4")
        buf.write("\3\2\2\2\u0091\u01ee\3\2\2\2\u0093\u0094\7\61\2\2\u0094")
        buf.write("\u0095\7,\2\2\u0095\u009c\3\2\2\2\u0096\u009b\5\3\2\2")
        buf.write("\u0097\u009b\n\2\2\2\u0098\u0099\7,\2\2\u0099\u009b\n")
        buf.write("\3\2\2\u009a\u0096\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0098")
        buf.write("\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009f\u00a0\7,\2\2\u00a0\u00a1\7\61\2\2\u00a1\4\3\2\2")
        buf.write("\2\u00a2\u00a3\5\3\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5")
        buf.write("\b\3\2\2\u00a5\6\3\2\2\2\u00a6\u00a7\7\61\2\2\u00a7\u00a8")
        buf.write("\7\61\2\2\u00a8\u00ac\3\2\2\2\u00a9\u00ab\n\4\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00ac\3")
        buf.write("\2\2\2\u00af\u00b0\b\4\2\2\u00b0\b\3\2\2\2\u00b1\u00b3")
        buf.write("\t\5\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\u00b7\b\5\2\2\u00b7\n\3\2\2\2\u00b8\u00b9\7\f\2")
        buf.write("\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\b\6\2\2\u00bb\f\3\2")
        buf.write("\2\2\u00bc\u00bd\5\u0087D\2\u00bd\16\3\2\2\2\u00be\u00c1")
        buf.write("\5\u0083B\2\u00bf\u00c1\5\u0085C\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c0\u00bf\3\2\2\2\u00c1\20\3\2\2\2\u00c2\u00c7\7$\2")
        buf.write("\2\u00c3\u00c6\5\23\n\2\u00c4\u00c6\n\6\2\2\u00c5\u00c3")
        buf.write("\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca\3\2\2\2")
        buf.write("\u00c9\u00c7\3\2\2\2\u00ca\u00cb\7$\2\2\u00cb\22\3\2\2")
        buf.write("\2\u00cc\u00cd\7^\2\2\u00cd\u00ce\t\7\2\2\u00ce\24\3\2")
        buf.write("\2\2\u00cf\u00d1\t\b\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2")
        buf.write("\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d8\7\60\2\2\u00d5\u00d7\t\b\2")
        buf.write("\2\u00d6\u00d5\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00db\u00dd\5\27\f\2\u00dc\u00db\3\2\2")
        buf.write("\2\u00dc\u00dd\3\2\2\2\u00dd\26\3\2\2\2\u00de\u00e0\t")
        buf.write("\t\2\2\u00df\u00e1\t\n\2\2\u00e0\u00df\3\2\2\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00e4\t\b\2\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\30\3\2\2\2\u00e7\u00ec\5\33")
        buf.write("\16\2\u00e8\u00ec\5\35\17\2\u00e9\u00ec\5\37\20\2\u00ea")
        buf.write("\u00ec\5!\21\2\u00eb\u00e7\3\2\2\2\u00eb\u00e8\3\2\2\2")
        buf.write("\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\32\3\2")
        buf.write("\2\2\u00ed\u00f6\7\62\2\2\u00ee\u00f2\t\13\2\2\u00ef\u00f1")
        buf.write("\t\b\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f6\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f5\u00ed\3\2\2\2\u00f5\u00ee\3")
        buf.write("\2\2\2\u00f6\34\3\2\2\2\u00f7\u00f8\7\62\2\2\u00f8\u00fc")
        buf.write("\7d\2\2\u00f9\u00fa\7\62\2\2\u00fa\u00fc\7D\2\2\u00fb")
        buf.write("\u00f7\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fe\3\2\2\2")
        buf.write("\u00fd\u00ff\t\f\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0100\3")
        buf.write("\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\36")
        buf.write("\3\2\2\2\u0102\u0103\7\62\2\2\u0103\u0107\7q\2\2\u0104")
        buf.write("\u0105\7\62\2\2\u0105\u0107\7Q\2\2\u0106\u0102\3\2\2\2")
        buf.write("\u0106\u0104\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u010a\t")
        buf.write("\r\2\2\u0109\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c \3\2\2\2\u010d\u010e")
        buf.write("\7\62\2\2\u010e\u0112\7z\2\2\u010f\u0110\7\62\2\2\u0110")
        buf.write("\u0112\7Z\2\2\u0111\u010d\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0112\u0114\3\2\2\2\u0113\u0115\t\16\2\2\u0114\u0113")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0114\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117\"\3\2\2\2\u0118\u0119\7<\2\2\u0119")
        buf.write("$\3\2\2\2\u011a\u011b\7*\2\2\u011b&\3\2\2\2\u011c\u011d")
        buf.write("\7+\2\2\u011d(\3\2\2\2\u011e\u011f\7}\2\2\u011f*\3\2\2")
        buf.write("\2\u0120\u0121\7\177\2\2\u0121,\3\2\2\2\u0122\u0123\7")
        buf.write("]\2\2\u0123.\3\2\2\2\u0124\u0125\7_\2\2\u0125\60\3\2\2")
        buf.write("\2\u0126\u0127\7.\2\2\u0127\62\3\2\2\2\u0128\u0129\7=")
        buf.write("\2\2\u0129\64\3\2\2\2\u012a\u012b\7-\2\2\u012b\66\3\2")
        buf.write("\2\2\u012c\u012d\7/\2\2\u012d8\3\2\2\2\u012e\u012f\7,")
        buf.write("\2\2\u012f:\3\2\2\2\u0130\u0131\7\61\2\2\u0131<\3\2\2")
        buf.write("\2\u0132\u0133\7\'\2\2\u0133>\3\2\2\2\u0134\u0135\7?\2")
        buf.write("\2\u0135\u0136\7?\2\2\u0136@\3\2\2\2\u0137\u0138\7#\2")
        buf.write("\2\u0138\u0139\7?\2\2\u0139B\3\2\2\2\u013a\u013b\7>\2")
        buf.write("\2\u013bD\3\2\2\2\u013c\u013d\7>\2\2\u013d\u013e\7?\2")
        buf.write("\2\u013eF\3\2\2\2\u013f\u0140\7@\2\2\u0140H\3\2\2\2\u0141")
        buf.write("\u0142\7@\2\2\u0142\u0143\7?\2\2\u0143J\3\2\2\2\u0144")
        buf.write("\u0145\7(\2\2\u0145\u0146\7(\2\2\u0146L\3\2\2\2\u0147")
        buf.write("\u0148\7~\2\2\u0148\u0149\7~\2\2\u0149N\3\2\2\2\u014a")
        buf.write("\u014b\7#\2\2\u014bP\3\2\2\2\u014c\u014d\7?\2\2\u014d")
        buf.write("R\3\2\2\2\u014e\u014f\7<\2\2\u014f\u0150\7?\2\2\u0150")
        buf.write("T\3\2\2\2\u0151\u0152\7-\2\2\u0152\u0153\7?\2\2\u0153")
        buf.write("V\3\2\2\2\u0154\u0155\7/\2\2\u0155\u0156\7?\2\2\u0156")
        buf.write("X\3\2\2\2\u0157\u0158\7,\2\2\u0158\u0159\7?\2\2\u0159")
        buf.write("Z\3\2\2\2\u015a\u015b\7\61\2\2\u015b\u015c\7?\2\2\u015c")
        buf.write("\\\3\2\2\2\u015d\u015e\7\'\2\2\u015e\u015f\7?\2\2\u015f")
        buf.write("^\3\2\2\2\u0160\u0161\7\60\2\2\u0161`\3\2\2\2\u0162\u0163")
        buf.write("\7k\2\2\u0163\u0164\7h\2\2\u0164b\3\2\2\2\u0165\u0166")
        buf.write("\7g\2\2\u0166\u0167\7n\2\2\u0167\u0168\7u\2\2\u0168\u0169")
        buf.write("\7g\2\2\u0169d\3\2\2\2\u016a\u016b\7h\2\2\u016b\u016c")
        buf.write("\7q\2\2\u016c\u016d\7t\2\2\u016df\3\2\2\2\u016e\u016f")
        buf.write("\7u\2\2\u016f\u0170\7v\2\2\u0170\u0171\7t\2\2\u0171\u0172")
        buf.write("\7w\2\2\u0172\u0173\7e\2\2\u0173\u0174\7v\2\2\u0174h\3")
        buf.write("\2\2\2\u0175\u0176\7k\2\2\u0176\u0177\7p\2\2\u0177\u0178")
        buf.write("\7v\2\2\u0178\u0179\7g\2\2\u0179\u017a\7t\2\2\u017a\u017b")
        buf.write("\7h\2\2\u017b\u017c\7c\2\2\u017c\u017d\7e\2\2\u017d\u017e")
        buf.write("\7g\2\2\u017ej\3\2\2\2\u017f\u0180\7u\2\2\u0180\u0181")
        buf.write("\7v\2\2\u0181\u0182\7t\2\2\u0182\u0183\7k\2\2\u0183\u0184")
        buf.write("\7p\2\2\u0184\u0185\7i\2\2\u0185l\3\2\2\2\u0186\u0187")
        buf.write("\7e\2\2\u0187\u0188\7q\2\2\u0188\u0189\7p\2\2\u0189\u018a")
        buf.write("\7u\2\2\u018a\u018b\7v\2\2\u018bn\3\2\2\2\u018c\u018d")
        buf.write("\7x\2\2\u018d\u018e\7c\2\2\u018e\u018f\7t\2\2\u018fp\3")
        buf.write("\2\2\2\u0190\u0191\7t\2\2\u0191\u0192\7g\2\2\u0192\u0193")
        buf.write("\7v\2\2\u0193\u0194\7w\2\2\u0194\u0195\7t\2\2\u0195\u0196")
        buf.write("\7p\2\2\u0196r\3\2\2\2\u0197\u0198\7h\2\2\u0198\u0199")
        buf.write("\7w\2\2\u0199\u019a\7p\2\2\u019a\u019b\7e\2\2\u019bt\3")
        buf.write("\2\2\2\u019c\u019d\7k\2\2\u019d\u019e\7p\2\2\u019e\u019f")
        buf.write("\7v\2\2\u019fv\3\2\2\2\u01a0\u01a1\7v\2\2\u01a1\u01a2")
        buf.write("\7{\2\2\u01a2\u01a3\7r\2\2\u01a3\u01a4\7g\2\2\u01a4x\3")
        buf.write("\2\2\2\u01a5\u01a6\7h\2\2\u01a6\u01a7\7n\2\2\u01a7\u01a8")
        buf.write("\7q\2\2\u01a8\u01a9\7c\2\2\u01a9\u01aa\7v\2\2\u01aaz\3")
        buf.write("\2\2\2\u01ab\u01ac\7d\2\2\u01ac\u01ad\7q\2\2\u01ad\u01ae")
        buf.write("\7q\2\2\u01ae\u01af\7n\2\2\u01af\u01b0\7g\2\2\u01b0\u01b1")
        buf.write("\7c\2\2\u01b1\u01b2\7p\2\2\u01b2|\3\2\2\2\u01b3\u01b4")
        buf.write("\7e\2\2\u01b4\u01b5\7q\2\2\u01b5\u01b6\7p\2\2\u01b6\u01b7")
        buf.write("\7v\2\2\u01b7\u01b8\7k\2\2\u01b8\u01b9\7p\2\2\u01b9\u01ba")
        buf.write("\7w\2\2\u01ba\u01bb\7g\2\2\u01bb~\3\2\2\2\u01bc\u01bd")
        buf.write("\7d\2\2\u01bd\u01be\7t\2\2\u01be\u01bf\7g\2\2\u01bf\u01c0")
        buf.write("\7c\2\2\u01c0\u01c1\7m\2\2\u01c1\u0080\3\2\2\2\u01c2\u01c3")
        buf.write("\7t\2\2\u01c3\u01c4\7c\2\2\u01c4\u01c5\7p\2\2\u01c5\u01c6")
        buf.write("\7i\2\2\u01c6\u01c7\7g\2\2\u01c7\u0082\3\2\2\2\u01c8\u01c9")
        buf.write("\7v\2\2\u01c9\u01ca\7t\2\2\u01ca\u01cb\7w\2\2\u01cb\u01cc")
        buf.write("\7g\2\2\u01cc\u0084\3\2\2\2\u01cd\u01ce\7h\2\2\u01ce\u01cf")
        buf.write("\7c\2\2\u01cf\u01d0\7n\2\2\u01d0\u01d1\7u\2\2\u01d1\u01d2")
        buf.write("\7g\2\2\u01d2\u0086\3\2\2\2\u01d3\u01d4\7p\2\2\u01d4\u01d5")
        buf.write("\7k\2\2\u01d5\u01d6\7n\2\2\u01d6\u0088\3\2\2\2\u01d7\u01db")
        buf.write("\t\17\2\2\u01d8\u01da\t\20\2\2\u01d9\u01d8\3\2\2\2\u01da")
        buf.write("\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2")
        buf.write("\u01dc\u008a\3\2\2\2\u01dd\u01db\3\2\2\2\u01de\u01df\7")
        buf.write("^\2\2\u01df\u01e0\t\21\2\2\u01e0\u008c\3\2\2\2\u01e1\u01e2")
        buf.write("\13\2\2\2\u01e2\u01e3\bG\3\2\u01e3\u008e\3\2\2\2\u01e4")
        buf.write("\u01e9\7$\2\2\u01e5\u01e8\5\u008bF\2\u01e6\u01e8\n\22")
        buf.write("\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb")
        buf.write("\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write("\u01ec\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec\u01ed\bH\4\2")
        buf.write("\u01ed\u0090\3\2\2\2\u01ee\u01f3\7$\2\2\u01ef\u01f2\5")
        buf.write("\u008bF\2\u01f0\u01f2\n\22\2\2\u01f1\u01ef\3\2\2\2\u01f1")
        buf.write("\u01f0\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2")
        buf.write("\u01f3\u01f4\3\2\2\2\u01f4\u01f6\3\2\2\2\u01f5\u01f3\3")
        buf.write("\2\2\2\u01f6\u01f7\7^\2\2\u01f7\u01f8\n\21\2\2\u01f8\u01f9")
        buf.write("\bI\5\2\u01f9\u0092\3\2\2\2\35\2\u009a\u009c\u00ac\u00b4")
        buf.write("\u00c0\u00c5\u00c7\u00d2\u00d8\u00dc\u00e0\u00e5\u00eb")
        buf.write("\u00f2\u00f5\u00fb\u0100\u0106\u010b\u0111\u0116\u01db")
        buf.write("\u01e7\u01e9\u01f1\u01f3\6\b\2\2\3G\2\3H\3\3I\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ML_COMMENT = 1
    SL_COMMENT = 2
    WS = 3
    NL = 4
    NIL_LITERAL = 5
    BOOLEAN_LITERAL = 6
    STRING_LITERAL = 7
    FLOAT_LITERAL = 8
    INTERGER_LITERAL = 9
    COLON = 10
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
            "'\n'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
            "';'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", "':='", 
            "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "'if'", "'else'", 
            "'for'", "'struct'", "'interface'", "'string'", "'const'", "'var'", 
            "'return'", "'func'", "'int'", "'type'", "'float'", "'boolean'", 
            "'continue'", "'break'", "'range'", "'true'", "'false'", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "ML_COMMENT", "SL_COMMENT", "WS", "NL", "NIL_LITERAL", "BOOLEAN_LITERAL", 
            "STRING_LITERAL", "FLOAT_LITERAL", "INTERGER_LITERAL", "COLON", 
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "COMMA", "SEMI", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", 
            "LT", "LE", "GT", "GE", "AND", "OR", "NOT", "ASSIGN", "COLON_ASSIGN", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "IF", "ELSE", "FOR", "STRUCT", "INTERFACE", "STRING", 
            "CONST", "VAR", "RETURN", "FUNC", "INT", "TYPE", "FLOAT", "BOOLEAN", 
            "CONTINUE", "BREAK", "RANGE", "TRUE", "FALSE", "NIL", "IDENTIFIER", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NESTED_COMMENT", "ML_COMMENT", "SL_COMMENT", "WS", "NL", 
                  "NIL_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", "ESC_SEQ", 
                  "FLOAT_LITERAL", "EXP", "INTERGER_LITERAL", "DEC", "BIN", 
                  "OCT", "HEX", "COLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LBRACK", "RBRACK", "COMMA", "SEMI", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", 
                  "OR", "NOT", "ASSIGN", "COLON_ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
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


        def __init__(self, input):
            super().__init__(input)
            self.previous_token = Token.EOF  # �?ặt giá trị mặc định tránh lỗi None

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
            elif tk == self.NL:
        if self.previous_token in {
            MiniGoLexer.IDENTIFIER, MiniGoLexer.INTERGER_LITERAL, MiniGoLexer.FLOAT_LITERAL,
            MiniGoLexer.BOOLEAN_LITERAL, MiniGoLexer.STRING_LITERAL, MiniGoLexer.RETURN,
            MiniGoLexer.CONTINUE, MiniGoLexer.BREAK, MiniGoLexer.RPAREN, MiniGoLexer.RBRACK,
            MiniGoLexer.RBRACE
        }:
            self.type = MiniGoLexer.SEMI
            token = super().emit()
            self.previous_token = token
            return token
        else:
            self.skip()
            # Không reset previous_token v�? EOF ở đây
            return None


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
     


