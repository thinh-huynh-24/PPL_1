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
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\7\2\u009d\n\2\f\2\16\2\u00a0\13\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00ad\n")
        buf.write("\4\f\4\16\4\u00b0\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\6\6")
        buf.write("\u00b9\n\6\r\6\16\6\u00ba\3\6\3\6\3\7\3\7\3\b\3\b\5\b")
        buf.write("\u00c3\n\b\3\t\3\t\3\t\7\t\u00c8\n\t\f\t\16\t\u00cb\13")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\13\6\13\u00d3\n\13\r\13\16\13")
        buf.write("\u00d4\3\13\3\13\7\13\u00d9\n\13\f\13\16\13\u00dc\13\13")
        buf.write("\3\13\5\13\u00df\n\13\3\f\3\f\5\f\u00e3\n\f\3\f\6\f\u00e6")
        buf.write("\n\f\r\f\16\f\u00e7\3\r\3\r\3\r\3\r\5\r\u00ee\n\r\3\16")
        buf.write("\3\16\3\16\7\16\u00f3\n\16\f\16\16\16\u00f6\13\16\5\16")
        buf.write("\u00f8\n\16\3\17\3\17\3\17\3\17\5\17\u00fe\n\17\3\17\6")
        buf.write("\17\u0101\n\17\r\17\16\17\u0102\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u0109\n\20\3\20\6\20\u010c\n\20\r\20\16\20\u010d\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u0114\n\21\3\21\6\21\u0117\n\21")
        buf.write("\r\21\16\21\u0118\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3")
        buf.write("\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\38\38\39\39\39\39\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3;\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3=\3>\3")
        buf.write(">\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3C\3C\3")
        buf.write("C\3C\3C\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3F\3F\7F\u01de\n")
        buf.write("F\fF\16F\u01e1\13F\3G\3G\3G\3H\3H\3H\3I\3I\3I\7I\u01ec")
        buf.write("\nI\fI\16I\u01ef\13I\3I\3I\3J\3J\3J\7J\u01f6\nJ\fJ\16")
        buf.write("J\u01f9\13J\3J\3J\3J\3J\2\2K\3\2\5\3\7\4\t\5\13\6\r\7")
        buf.write("\17\b\21\t\23\2\25\n\27\2\31\13\33\2\35\2\37\2!\2#\f%")
        buf.write("\r\'\16)\17+\20-\21/\22\61\23\63\24\65\25\67\269\27;\30")
        buf.write("=\31?\32A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a")
        buf.write("+c,e-g.i/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177:\u0081")
        buf.write(";\u0083<\u0085=\u0087>\u0089?\u008b@\u008d\2\u008fA\u0091")
        buf.write("B\u0093C\3\2\23\4\2,,\61\61\3\2\61\61\4\2\f\f\17\17\5")
        buf.write("\2\13\13\16\17\"\"\4\2$$^^\7\2$$^^ppttvv\3\2\62;\4\2G")
        buf.write("Ggg\4\2--//\3\2\63;\3\2\62\63\3\2\629\5\2\62;CHch\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\n\2$$))^^ddhhppttvv\6\2\f\f\17")
        buf.write("\17$$^^\2\u0212\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2")
        buf.write("\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0095")
        buf.write("\3\2\2\2\5\u00a4\3\2\2\2\7\u00a8\3\2\2\2\t\u00b3\3\2\2")
        buf.write("\2\13\u00b8\3\2\2\2\r\u00be\3\2\2\2\17\u00c2\3\2\2\2\21")
        buf.write("\u00c4\3\2\2\2\23\u00ce\3\2\2\2\25\u00d2\3\2\2\2\27\u00e0")
        buf.write("\3\2\2\2\31\u00ed\3\2\2\2\33\u00f7\3\2\2\2\35\u00fd\3")
        buf.write("\2\2\2\37\u0108\3\2\2\2!\u0113\3\2\2\2#\u011a\3\2\2\2")
        buf.write("%\u011c\3\2\2\2\'\u011e\3\2\2\2)\u0120\3\2\2\2+\u0122")
        buf.write("\3\2\2\2-\u0124\3\2\2\2/\u0126\3\2\2\2\61\u0128\3\2\2")
        buf.write("\2\63\u012a\3\2\2\2\65\u012c\3\2\2\2\67\u012e\3\2\2\2")
        buf.write("9\u0130\3\2\2\2;\u0132\3\2\2\2=\u0134\3\2\2\2?\u0136\3")
        buf.write("\2\2\2A\u0138\3\2\2\2C\u013b\3\2\2\2E\u013e\3\2\2\2G\u0140")
        buf.write("\3\2\2\2I\u0143\3\2\2\2K\u0145\3\2\2\2M\u0148\3\2\2\2")
        buf.write("O\u014b\3\2\2\2Q\u014e\3\2\2\2S\u0150\3\2\2\2U\u0152\3")
        buf.write("\2\2\2W\u0155\3\2\2\2Y\u0158\3\2\2\2[\u015b\3\2\2\2]\u015e")
        buf.write("\3\2\2\2_\u0161\3\2\2\2a\u0164\3\2\2\2c\u0166\3\2\2\2")
        buf.write("e\u0169\3\2\2\2g\u016e\3\2\2\2i\u0172\3\2\2\2k\u0179\3")
        buf.write("\2\2\2m\u0183\3\2\2\2o\u018a\3\2\2\2q\u0190\3\2\2\2s\u0194")
        buf.write("\3\2\2\2u\u019b\3\2\2\2w\u01a0\3\2\2\2y\u01a4\3\2\2\2")
        buf.write("{\u01a9\3\2\2\2}\u01af\3\2\2\2\177\u01b7\3\2\2\2\u0081")
        buf.write("\u01c0\3\2\2\2\u0083\u01c6\3\2\2\2\u0085\u01cc\3\2\2\2")
        buf.write("\u0087\u01d1\3\2\2\2\u0089\u01d7\3\2\2\2\u008b\u01db\3")
        buf.write("\2\2\2\u008d\u01e2\3\2\2\2\u008f\u01e5\3\2\2\2\u0091\u01e8")
        buf.write("\3\2\2\2\u0093\u01f2\3\2\2\2\u0095\u0096\7\61\2\2\u0096")
        buf.write("\u0097\7,\2\2\u0097\u009e\3\2\2\2\u0098\u009d\5\3\2\2")
        buf.write("\u0099\u009d\n\2\2\2\u009a\u009b\7,\2\2\u009b\u009d\n")
        buf.write("\3\2\2\u009c\u0098\3\2\2\2\u009c\u0099\3\2\2\2\u009c\u009a")
        buf.write("\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a1\u00a2\7,\2\2\u00a2\u00a3\7\61\2\2\u00a3\4\3\2\2")
        buf.write("\2\u00a4\u00a5\5\3\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7")
        buf.write("\b\3\2\2\u00a7\6\3\2\2\2\u00a8\u00a9\7\61\2\2\u00a9\u00aa")
        buf.write("\7\61\2\2\u00aa\u00ae\3\2\2\2\u00ab\u00ad\n\4\2\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00ae\3")
        buf.write("\2\2\2\u00b1\u00b2\b\4\2\2\u00b2\b\3\2\2\2\u00b3\u00b4")
        buf.write("\7\f\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\b\5\2\2\u00b6")
        buf.write("\n\3\2\2\2\u00b7\u00b9\t\5\2\2\u00b8\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bc\3\2\2\2\u00bc\u00bd\b\6\2\2\u00bd\f\3\2\2")
        buf.write("\2\u00be\u00bf\5\u0089E\2\u00bf\16\3\2\2\2\u00c0\u00c3")
        buf.write("\5\u0085C\2\u00c1\u00c3\5\u0087D\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c1\3\2\2\2\u00c3\20\3\2\2\2\u00c4\u00c9\7$\2")
        buf.write("\2\u00c5\u00c8\5\u008dG\2\u00c6\u00c8\n\6\2\2\u00c7\u00c5")
        buf.write("\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2")
        buf.write("\u00cb\u00c9\3\2\2\2\u00cc\u00cd\7$\2\2\u00cd\22\3\2\2")
        buf.write("\2\u00ce\u00cf\7^\2\2\u00cf\u00d0\t\7\2\2\u00d0\24\3\2")
        buf.write("\2\2\u00d1\u00d3\t\b\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\u00d6\3\2\2\2\u00d6\u00da\7\60\2\2\u00d7\u00d9\t\b\2")
        buf.write("\2\u00d8\u00d7\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8")
        buf.write("\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00de\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dd\u00df\5\27\f\2\u00de\u00dd\3\2\2")
        buf.write("\2\u00de\u00df\3\2\2\2\u00df\26\3\2\2\2\u00e0\u00e2\t")
        buf.write("\t\2\2\u00e1\u00e3\t\n\2\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e6\t\b\2\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e5\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\30\3\2\2\2\u00e9\u00ee\5\33")
        buf.write("\16\2\u00ea\u00ee\5\35\17\2\u00eb\u00ee\5\37\20\2\u00ec")
        buf.write("\u00ee\5!\21\2\u00ed\u00e9\3\2\2\2\u00ed\u00ea\3\2\2\2")
        buf.write("\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee\32\3\2")
        buf.write("\2\2\u00ef\u00f8\7\62\2\2\u00f0\u00f4\t\13\2\2\u00f1\u00f3")
        buf.write("\t\b\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f8\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f7\u00ef\3\2\2\2\u00f7\u00f0\3")
        buf.write("\2\2\2\u00f8\34\3\2\2\2\u00f9\u00fa\7\62\2\2\u00fa\u00fe")
        buf.write("\7d\2\2\u00fb\u00fc\7\62\2\2\u00fc\u00fe\7D\2\2\u00fd")
        buf.write("\u00f9\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u0100\3\2\2\2")
        buf.write("\u00ff\u0101\t\f\2\2\u0100\u00ff\3\2\2\2\u0101\u0102\3")
        buf.write("\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\36")
        buf.write("\3\2\2\2\u0104\u0105\7\62\2\2\u0105\u0109\7q\2\2\u0106")
        buf.write("\u0107\7\62\2\2\u0107\u0109\7Q\2\2\u0108\u0104\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u010c\t")
        buf.write("\r\2\2\u010b\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010b")
        buf.write("\3\2\2\2\u010d\u010e\3\2\2\2\u010e \3\2\2\2\u010f\u0110")
        buf.write("\7\62\2\2\u0110\u0114\7z\2\2\u0111\u0112\7\62\2\2\u0112")
        buf.write("\u0114\7Z\2\2\u0113\u010f\3\2\2\2\u0113\u0111\3\2\2\2")
        buf.write("\u0114\u0116\3\2\2\2\u0115\u0117\t\16\2\2\u0116\u0115")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0116\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\"\3\2\2\2\u011a\u011b\t\n\2\2\u011b")
        buf.write("$\3\2\2\2\u011c\u011d\7<\2\2\u011d&\3\2\2\2\u011e\u011f")
        buf.write("\7*\2\2\u011f(\3\2\2\2\u0120\u0121\7+\2\2\u0121*\3\2\2")
        buf.write("\2\u0122\u0123\7}\2\2\u0123,\3\2\2\2\u0124\u0125\7\177")
        buf.write("\2\2\u0125.\3\2\2\2\u0126\u0127\7]\2\2\u0127\60\3\2\2")
        buf.write("\2\u0128\u0129\7_\2\2\u0129\62\3\2\2\2\u012a\u012b\7.")
        buf.write("\2\2\u012b\64\3\2\2\2\u012c\u012d\7=\2\2\u012d\66\3\2")
        buf.write("\2\2\u012e\u012f\7-\2\2\u012f8\3\2\2\2\u0130\u0131\7/")
        buf.write("\2\2\u0131:\3\2\2\2\u0132\u0133\7,\2\2\u0133<\3\2\2\2")
        buf.write("\u0134\u0135\7\61\2\2\u0135>\3\2\2\2\u0136\u0137\7\'\2")
        buf.write("\2\u0137@\3\2\2\2\u0138\u0139\7?\2\2\u0139\u013a\7?\2")
        buf.write("\2\u013aB\3\2\2\2\u013b\u013c\7#\2\2\u013c\u013d\7?\2")
        buf.write("\2\u013dD\3\2\2\2\u013e\u013f\7>\2\2\u013fF\3\2\2\2\u0140")
        buf.write("\u0141\7>\2\2\u0141\u0142\7?\2\2\u0142H\3\2\2\2\u0143")
        buf.write("\u0144\7@\2\2\u0144J\3\2\2\2\u0145\u0146\7@\2\2\u0146")
        buf.write("\u0147\7?\2\2\u0147L\3\2\2\2\u0148\u0149\7(\2\2\u0149")
        buf.write("\u014a\7(\2\2\u014aN\3\2\2\2\u014b\u014c\7~\2\2\u014c")
        buf.write("\u014d\7~\2\2\u014dP\3\2\2\2\u014e\u014f\7#\2\2\u014f")
        buf.write("R\3\2\2\2\u0150\u0151\7?\2\2\u0151T\3\2\2\2\u0152\u0153")
        buf.write("\7<\2\2\u0153\u0154\7?\2\2\u0154V\3\2\2\2\u0155\u0156")
        buf.write("\7-\2\2\u0156\u0157\7?\2\2\u0157X\3\2\2\2\u0158\u0159")
        buf.write("\7/\2\2\u0159\u015a\7?\2\2\u015aZ\3\2\2\2\u015b\u015c")
        buf.write("\7,\2\2\u015c\u015d\7?\2\2\u015d\\\3\2\2\2\u015e\u015f")
        buf.write("\7\61\2\2\u015f\u0160\7?\2\2\u0160^\3\2\2\2\u0161\u0162")
        buf.write("\7\'\2\2\u0162\u0163\7?\2\2\u0163`\3\2\2\2\u0164\u0165")
        buf.write("\7\60\2\2\u0165b\3\2\2\2\u0166\u0167\7k\2\2\u0167\u0168")
        buf.write("\7h\2\2\u0168d\3\2\2\2\u0169\u016a\7g\2\2\u016a\u016b")
        buf.write("\7n\2\2\u016b\u016c\7u\2\2\u016c\u016d\7g\2\2\u016df\3")
        buf.write("\2\2\2\u016e\u016f\7h\2\2\u016f\u0170\7q\2\2\u0170\u0171")
        buf.write("\7t\2\2\u0171h\3\2\2\2\u0172\u0173\7u\2\2\u0173\u0174")
        buf.write("\7v\2\2\u0174\u0175\7t\2\2\u0175\u0176\7w\2\2\u0176\u0177")
        buf.write("\7e\2\2\u0177\u0178\7v\2\2\u0178j\3\2\2\2\u0179\u017a")
        buf.write("\7k\2\2\u017a\u017b\7p\2\2\u017b\u017c\7v\2\2\u017c\u017d")
        buf.write("\7g\2\2\u017d\u017e\7t\2\2\u017e\u017f\7h\2\2\u017f\u0180")
        buf.write("\7c\2\2\u0180\u0181\7e\2\2\u0181\u0182\7g\2\2\u0182l\3")
        buf.write("\2\2\2\u0183\u0184\7u\2\2\u0184\u0185\7v\2\2\u0185\u0186")
        buf.write("\7t\2\2\u0186\u0187\7k\2\2\u0187\u0188\7p\2\2\u0188\u0189")
        buf.write("\7i\2\2\u0189n\3\2\2\2\u018a\u018b\7e\2\2\u018b\u018c")
        buf.write("\7q\2\2\u018c\u018d\7p\2\2\u018d\u018e\7u\2\2\u018e\u018f")
        buf.write("\7v\2\2\u018fp\3\2\2\2\u0190\u0191\7x\2\2\u0191\u0192")
        buf.write("\7c\2\2\u0192\u0193\7t\2\2\u0193r\3\2\2\2\u0194\u0195")
        buf.write("\7t\2\2\u0195\u0196\7g\2\2\u0196\u0197\7v\2\2\u0197\u0198")
        buf.write("\7w\2\2\u0198\u0199\7t\2\2\u0199\u019a\7p\2\2\u019at\3")
        buf.write("\2\2\2\u019b\u019c\7h\2\2\u019c\u019d\7w\2\2\u019d\u019e")
        buf.write("\7p\2\2\u019e\u019f\7e\2\2\u019fv\3\2\2\2\u01a0\u01a1")
        buf.write("\7k\2\2\u01a1\u01a2\7p\2\2\u01a2\u01a3\7v\2\2\u01a3x\3")
        buf.write("\2\2\2\u01a4\u01a5\7v\2\2\u01a5\u01a6\7{\2\2\u01a6\u01a7")
        buf.write("\7r\2\2\u01a7\u01a8\7g\2\2\u01a8z\3\2\2\2\u01a9\u01aa")
        buf.write("\7h\2\2\u01aa\u01ab\7n\2\2\u01ab\u01ac\7q\2\2\u01ac\u01ad")
        buf.write("\7c\2\2\u01ad\u01ae\7v\2\2\u01ae|\3\2\2\2\u01af\u01b0")
        buf.write("\7d\2\2\u01b0\u01b1\7q\2\2\u01b1\u01b2\7q\2\2\u01b2\u01b3")
        buf.write("\7n\2\2\u01b3\u01b4\7g\2\2\u01b4\u01b5\7c\2\2\u01b5\u01b6")
        buf.write("\7p\2\2\u01b6~\3\2\2\2\u01b7\u01b8\7e\2\2\u01b8\u01b9")
        buf.write("\7q\2\2\u01b9\u01ba\7p\2\2\u01ba\u01bb\7v\2\2\u01bb\u01bc")
        buf.write("\7k\2\2\u01bc\u01bd\7p\2\2\u01bd\u01be\7w\2\2\u01be\u01bf")
        buf.write("\7g\2\2\u01bf\u0080\3\2\2\2\u01c0\u01c1\7d\2\2\u01c1\u01c2")
        buf.write("\7t\2\2\u01c2\u01c3\7g\2\2\u01c3\u01c4\7c\2\2\u01c4\u01c5")
        buf.write("\7m\2\2\u01c5\u0082\3\2\2\2\u01c6\u01c7\7t\2\2\u01c7\u01c8")
        buf.write("\7c\2\2\u01c8\u01c9\7p\2\2\u01c9\u01ca\7i\2\2\u01ca\u01cb")
        buf.write("\7g\2\2\u01cb\u0084\3\2\2\2\u01cc\u01cd\7v\2\2\u01cd\u01ce")
        buf.write("\7t\2\2\u01ce\u01cf\7w\2\2\u01cf\u01d0\7g\2\2\u01d0\u0086")
        buf.write("\3\2\2\2\u01d1\u01d2\7h\2\2\u01d2\u01d3\7c\2\2\u01d3\u01d4")
        buf.write("\7n\2\2\u01d4\u01d5\7u\2\2\u01d5\u01d6\7g\2\2\u01d6\u0088")
        buf.write("\3\2\2\2\u01d7\u01d8\7p\2\2\u01d8\u01d9\7k\2\2\u01d9\u01da")
        buf.write("\7n\2\2\u01da\u008a\3\2\2\2\u01db\u01df\t\17\2\2\u01dc")
        buf.write("\u01de\t\20\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e1\3\2\2")
        buf.write("\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u008c")
        buf.write("\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e3\7^\2\2\u01e3")
        buf.write("\u01e4\t\21\2\2\u01e4\u008e\3\2\2\2\u01e5\u01e6\13\2\2")
        buf.write("\2\u01e6\u01e7\bH\3\2\u01e7\u0090\3\2\2\2\u01e8\u01ed")
        buf.write("\7$\2\2\u01e9\u01ec\5\u008dG\2\u01ea\u01ec\n\22\2\2\u01eb")
        buf.write("\u01e9\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2")
        buf.write("\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f0\3")
        buf.write("\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f1\bI\4\2\u01f1\u0092")
        buf.write("\3\2\2\2\u01f2\u01f7\7$\2\2\u01f3\u01f6\5\u008dG\2\u01f4")
        buf.write("\u01f6\n\22\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f4\3\2\2")
        buf.write("\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8")
        buf.write("\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa")
        buf.write("\u01fb\7^\2\2\u01fb\u01fc\n\21\2\2\u01fc\u01fd\bJ\5\2")
        buf.write("\u01fd\u0094\3\2\2\2\35\2\u009c\u009e\u00ae\u00ba\u00c2")
        buf.write("\u00c7\u00c9\u00d4\u00da\u00de\u00e2\u00e7\u00ed\u00f4")
        buf.write("\u00f7\u00fd\u0102\u0108\u010d\u0113\u0118\u01df\u01eb")
        buf.write("\u01ed\u01f5\u01f7\6\b\2\2\3H\2\3I\3\3J\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ML_COMMENT = 1
    SL_COMMENT = 2
    NL = 3
    WS = 4
    NIL_LITERAL = 5
    BOOLEAN_LITERAL = 6
    STRING_LITERAL = 7
    FLOAT_LITERAL = 8
    INTERGER_LITERAL = 9
    SIGN = 10
    COLON = 11
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
            "'\n'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
            "';'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", "':='", 
            "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "'if'", "'else'", 
            "'for'", "'struct'", "'interface'", "'string'", "'const'", "'var'", 
            "'return'", "'func'", "'int'", "'type'", "'float'", "'boolean'", 
            "'continue'", "'break'", "'range'", "'true'", "'false'", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "ML_COMMENT", "SL_COMMENT", "NL", "WS", "NIL_LITERAL", "BOOLEAN_LITERAL", 
            "STRING_LITERAL", "FLOAT_LITERAL", "INTERGER_LITERAL", "SIGN", 
            "COLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "COMMA", "SEMI", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", 
            "LT", "LE", "GT", "GE", "AND", "OR", "NOT", "ASSIGN", "COLON_ASSIGN", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "IF", "ELSE", "FOR", "STRUCT", "INTERFACE", "STRING", 
            "CONST", "VAR", "RETURN", "FUNC", "INT", "TYPE", "FLOAT", "BOOLEAN", 
            "CONTINUE", "BREAK", "RANGE", "TRUE", "FALSE", "NIL", "IDENTIFIER", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NESTED_COMMENT", "ML_COMMENT", "SL_COMMENT", "NL", "WS", 
                  "NIL_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", "ESC_SEQ", 
                  "FLOAT_LITERAL", "EXP", "INTERGER_LITERAL", "DEC", "BIN", 
                  "OCT", "HEX", "SIGN", "COLON", "LPAREN", "RPAREN", "LBRACE", 
                  "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMI", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "LE", "GT", 
                  "GE", "AND", "OR", "NOT", "ASSIGN", "COLON_ASSIGN", "ADD_ASSIGN", 
                  "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "DOT", "IF", "ELSE", "FOR", "STRUCT", "INTERFACE", "STRING", 
                  "CONST", "VAR", "RETURN", "FUNC", "INT", "TYPE", "FLOAT", 
                  "BOOLEAN", "CONTINUE", "BREAK", "RANGE", "TRUE", "FALSE", 
                  "NIL", "IDENTIFIER", "ESC", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
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
     


