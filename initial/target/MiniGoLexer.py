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
        buf.write("\u020e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\4\f\4\16\4\u00b0\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00c3\n\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\5\t\u00d5\n\t\3\n\3\n\3\n\7\n\u00da\n\n\f\n\16")
        buf.write("\n\u00dd\13\n\3\n\3\n\3\13\3\13\3\13\3\f\6\f\u00e5\n\f")
        buf.write("\r\f\16\f\u00e6\3\f\3\f\7\f\u00eb\n\f\f\f\16\f\u00ee\13")
        buf.write("\f\3\f\5\f\u00f1\n\f\3\r\3\r\5\r\u00f5\n\r\3\r\6\r\u00f8")
        buf.write("\n\r\r\r\16\r\u00f9\3\16\3\16\3\16\3\16\5\16\u0100\n\16")
        buf.write("\3\17\3\17\3\17\7\17\u0105\n\17\f\17\16\17\u0108\13\17")
        buf.write("\5\17\u010a\n\17\3\20\3\20\3\20\3\20\5\20\u0110\n\20\3")
        buf.write("\20\6\20\u0113\n\20\r\20\16\20\u0114\3\21\3\21\3\21\3")
        buf.write("\21\5\21\u011b\n\21\3\21\6\21\u011e\n\21\r\21\16\21\u011f")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u0126\n\22\3\22\6\22\u0129\n")
        buf.write("\22\r\22\16\22\u012a\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.")
        buf.write("\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\38\38\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(";\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3=\3>\3>\3>\3>\3")
        buf.write(">\3>\3?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3")
        buf.write("D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3F\3F\7F\u01ee\nF\fF\16F")
        buf.write("\u01f1\13F\3G\3G\3G\3H\3H\3H\3I\3I\3I\7I\u01fc\nI\fI\16")
        buf.write("I\u01ff\13I\3I\3I\3J\3J\3J\7J\u0206\nJ\fJ\16J\u0209\13")
        buf.write("J\3J\3J\3J\3J\2\2K\3\2\5\3\7\4\t\2\13\5\r\6\17\7\21\b")
        buf.write("\23\t\25\2\27\n\31\2\33\13\35\2\37\2!\2#\2%\f\'\r)\16")
        buf.write("+\17-\20/\21\61\22\63\23\65\24\67\259\26;\27=\30?\31A")
        buf.write("\32C\33E\34G\35I\36K\37M O!Q\"S#U$W%Y&[\'](_)a*c+e,g-")
        buf.write("i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8\1779\u0081:\u0083")
        buf.write(";\u0085<\u0087=\u0089>\u008b?\u008d\2\u008f@\u0091A\u0093")
        buf.write("B\3\2\23\4\2,,\61\61\3\2\61\61\4\2\f\f\17\17\5\2\n\13")
        buf.write("\16\17\"\"\4\2$$^^\7\2$$^^ppttvv\3\2\62;\4\2GGgg\4\2-")
        buf.write("-//\3\2\63;\3\2\62\63\3\2\629\5\2\62;CHch\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\n\2$$))^^ddhhppttvv\6\2\f\f\17\17$$^^\2")
        buf.write("\u022f\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\33\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
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
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2")
        buf.write("\2\5\u00a4\3\2\2\2\7\u00a8\3\2\2\2\t\u00c2\3\2\2\2\13")
        buf.write("\u00c8\3\2\2\2\r\u00cc\3\2\2\2\17\u00d0\3\2\2\2\21\u00d4")
        buf.write("\3\2\2\2\23\u00d6\3\2\2\2\25\u00e0\3\2\2\2\27\u00e4\3")
        buf.write("\2\2\2\31\u00f2\3\2\2\2\33\u00ff\3\2\2\2\35\u0109\3\2")
        buf.write("\2\2\37\u010f\3\2\2\2!\u011a\3\2\2\2#\u0125\3\2\2\2%\u012c")
        buf.write("\3\2\2\2\'\u012e\3\2\2\2)\u0130\3\2\2\2+\u0132\3\2\2\2")
        buf.write("-\u0134\3\2\2\2/\u0136\3\2\2\2\61\u0138\3\2\2\2\63\u013a")
        buf.write("\3\2\2\2\65\u013c\3\2\2\2\67\u013e\3\2\2\29\u0140\3\2")
        buf.write("\2\2;\u0142\3\2\2\2=\u0144\3\2\2\2?\u0146\3\2\2\2A\u0148")
        buf.write("\3\2\2\2C\u014b\3\2\2\2E\u014e\3\2\2\2G\u0150\3\2\2\2")
        buf.write("I\u0153\3\2\2\2K\u0155\3\2\2\2M\u0158\3\2\2\2O\u015b\3")
        buf.write("\2\2\2Q\u015e\3\2\2\2S\u0160\3\2\2\2U\u0162\3\2\2\2W\u0165")
        buf.write("\3\2\2\2Y\u0168\3\2\2\2[\u016b\3\2\2\2]\u016e\3\2\2\2")
        buf.write("_\u0171\3\2\2\2a\u0174\3\2\2\2c\u0176\3\2\2\2e\u0179\3")
        buf.write("\2\2\2g\u017e\3\2\2\2i\u0182\3\2\2\2k\u0189\3\2\2\2m\u0193")
        buf.write("\3\2\2\2o\u019a\3\2\2\2q\u01a0\3\2\2\2s\u01a4\3\2\2\2")
        buf.write("u\u01ab\3\2\2\2w\u01b0\3\2\2\2y\u01b4\3\2\2\2{\u01b9\3")
        buf.write("\2\2\2}\u01bf\3\2\2\2\177\u01c7\3\2\2\2\u0081\u01d0\3")
        buf.write("\2\2\2\u0083\u01d6\3\2\2\2\u0085\u01dc\3\2\2\2\u0087\u01e1")
        buf.write("\3\2\2\2\u0089\u01e7\3\2\2\2\u008b\u01eb\3\2\2\2\u008d")
        buf.write("\u01f2\3\2\2\2\u008f\u01f5\3\2\2\2\u0091\u01f8\3\2\2\2")
        buf.write("\u0093\u0202\3\2\2\2\u0095\u0096\7\61\2\2\u0096\u0097")
        buf.write("\7,\2\2\u0097\u009e\3\2\2\2\u0098\u009d\5\3\2\2\u0099")
        buf.write("\u009d\n\2\2\2\u009a\u009b\7,\2\2\u009b\u009d\n\3\2\2")
        buf.write("\u009c\u0098\3\2\2\2\u009c\u0099\3\2\2\2\u009c\u009a\3")
        buf.write("\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1")
        buf.write("\u00a2\7,\2\2\u00a2\u00a3\7\61\2\2\u00a3\4\3\2\2\2\u00a4")
        buf.write("\u00a5\5\3\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\b\3\2\2")
        buf.write("\u00a7\6\3\2\2\2\u00a8\u00a9\7\61\2\2\u00a9\u00aa\7\61")
        buf.write("\2\2\u00aa\u00ae\3\2\2\2\u00ab\u00ad\n\4\2\2\u00ac\u00ab")
        buf.write("\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b1\u00b2\b\4\2\2\u00b2\b\3\2\2\2\u00b3\u00c3\5\u008b")
        buf.write("F\2\u00b4\u00c3\5\33\16\2\u00b5\u00c3\5\27\f\2\u00b6\u00c3")
        buf.write("\5\21\t\2\u00b7\u00c3\5\23\n\2\u00b8\u00c3\5w<\2\u00b9")
        buf.write("\u00c3\5{>\2\u00ba\u00c3\5}?\2\u00bb\u00c3\5m\67\2\u00bc")
        buf.write("\u00c3\5s:\2\u00bd\u00c3\5\177@\2\u00be\u00c3\5\u0081")
        buf.write("A\2\u00bf\u00c3\5)\25\2\u00c0\u00c3\5-\27\2\u00c1\u00c3")
        buf.write("\5\61\31\2\u00c2\u00b3\3\2\2\2\u00c2\u00b4\3\2\2\2\u00c2")
        buf.write("\u00b5\3\2\2\2\u00c2\u00b6\3\2\2\2\u00c2\u00b7\3\2\2\2")
        buf.write("\u00c2\u00b8\3\2\2\2\u00c2\u00b9\3\2\2\2\u00c2\u00ba\3")
        buf.write("\2\2\2\u00c2\u00bb\3\2\2\2\u00c2\u00bc\3\2\2\2\u00c2\u00bd")
        buf.write("\3\2\2\2\u00c2\u00be\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4\u00c5\5\r\7\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\b")
        buf.write("\5\3\2\u00c7\n\3\2\2\2\u00c8\u00c9\t\5\2\2\u00c9\u00ca")
        buf.write("\3\2\2\2\u00ca\u00cb\b\6\2\2\u00cb\f\3\2\2\2\u00cc\u00cd")
        buf.write("\7\f\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\b\7\2\2\u00cf")
        buf.write("\16\3\2\2\2\u00d0\u00d1\5\u0089E\2\u00d1\20\3\2\2\2\u00d2")
        buf.write("\u00d5\5\u0085C\2\u00d3\u00d5\5\u0087D\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\22\3\2\2\2\u00d6\u00db")
        buf.write("\7$\2\2\u00d7\u00da\5\25\13\2\u00d8\u00da\n\6\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da\u00dd\3\2\2\2")
        buf.write("\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00de\3")
        buf.write("\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\7$\2\2\u00df\24")
        buf.write("\3\2\2\2\u00e0\u00e1\7^\2\2\u00e1\u00e2\t\7\2\2\u00e2")
        buf.write("\26\3\2\2\2\u00e3\u00e5\t\b\2\2\u00e4\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e6\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\u00ec\7\60\2\2\u00e9\u00eb")
        buf.write("\t\b\2\2\u00ea\u00e9\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00f0\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ef\u00f1\5\31\r\2\u00f0\u00ef")
        buf.write("\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\30\3\2\2\2\u00f2\u00f4")
        buf.write("\t\t\2\2\u00f3\u00f5\t\n\2\2\u00f4\u00f3\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6\u00f8\t\b\2\2")
        buf.write("\u00f7\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00f7\3")
        buf.write("\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\32\3\2\2\2\u00fb\u0100")
        buf.write("\5\35\17\2\u00fc\u0100\5\37\20\2\u00fd\u0100\5!\21\2\u00fe")
        buf.write("\u0100\5#\22\2\u00ff\u00fb\3\2\2\2\u00ff\u00fc\3\2\2\2")
        buf.write("\u00ff\u00fd\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100\34\3\2")
        buf.write("\2\2\u0101\u010a\7\62\2\2\u0102\u0106\t\13\2\2\u0103\u0105")
        buf.write("\t\b\2\2\u0104\u0103\3\2\2\2\u0105\u0108\3\2\2\2\u0106")
        buf.write("\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u010a\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0109\u0101\3\2\2\2\u0109\u0102\3")
        buf.write("\2\2\2\u010a\36\3\2\2\2\u010b\u010c\7\62\2\2\u010c\u0110")
        buf.write("\7d\2\2\u010d\u010e\7\62\2\2\u010e\u0110\7D\2\2\u010f")
        buf.write("\u010b\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0112\3\2\2\2")
        buf.write("\u0111\u0113\t\f\2\2\u0112\u0111\3\2\2\2\u0113\u0114\3")
        buf.write("\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115 ")
        buf.write("\3\2\2\2\u0116\u0117\7\62\2\2\u0117\u011b\7q\2\2\u0118")
        buf.write("\u0119\7\62\2\2\u0119\u011b\7Q\2\2\u011a\u0116\3\2\2\2")
        buf.write("\u011a\u0118\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u011e\t")
        buf.write("\r\2\2\u011d\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u011d")
        buf.write("\3\2\2\2\u011f\u0120\3\2\2\2\u0120\"\3\2\2\2\u0121\u0122")
        buf.write("\7\62\2\2\u0122\u0126\7z\2\2\u0123\u0124\7\62\2\2\u0124")
        buf.write("\u0126\7Z\2\2\u0125\u0121\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0126\u0128\3\2\2\2\u0127\u0129\t\16\2\2\u0128\u0127")
        buf.write("\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u0128\3\2\2\2\u012a")
        buf.write("\u012b\3\2\2\2\u012b$\3\2\2\2\u012c\u012d\7<\2\2\u012d")
        buf.write("&\3\2\2\2\u012e\u012f\7*\2\2\u012f(\3\2\2\2\u0130\u0131")
        buf.write("\7+\2\2\u0131*\3\2\2\2\u0132\u0133\7}\2\2\u0133,\3\2\2")
        buf.write("\2\u0134\u0135\7\177\2\2\u0135.\3\2\2\2\u0136\u0137\7")
        buf.write("]\2\2\u0137\60\3\2\2\2\u0138\u0139\7_\2\2\u0139\62\3\2")
        buf.write("\2\2\u013a\u013b\7.\2\2\u013b\64\3\2\2\2\u013c\u013d\7")
        buf.write("=\2\2\u013d\66\3\2\2\2\u013e\u013f\7-\2\2\u013f8\3\2\2")
        buf.write("\2\u0140\u0141\7/\2\2\u0141:\3\2\2\2\u0142\u0143\7,\2")
        buf.write("\2\u0143<\3\2\2\2\u0144\u0145\7\61\2\2\u0145>\3\2\2\2")
        buf.write("\u0146\u0147\7\'\2\2\u0147@\3\2\2\2\u0148\u0149\7?\2\2")
        buf.write("\u0149\u014a\7?\2\2\u014aB\3\2\2\2\u014b\u014c\7#\2\2")
        buf.write("\u014c\u014d\7?\2\2\u014dD\3\2\2\2\u014e\u014f\7>\2\2")
        buf.write("\u014fF\3\2\2\2\u0150\u0151\7>\2\2\u0151\u0152\7?\2\2")
        buf.write("\u0152H\3\2\2\2\u0153\u0154\7@\2\2\u0154J\3\2\2\2\u0155")
        buf.write("\u0156\7@\2\2\u0156\u0157\7?\2\2\u0157L\3\2\2\2\u0158")
        buf.write("\u0159\7(\2\2\u0159\u015a\7(\2\2\u015aN\3\2\2\2\u015b")
        buf.write("\u015c\7~\2\2\u015c\u015d\7~\2\2\u015dP\3\2\2\2\u015e")
        buf.write("\u015f\7#\2\2\u015fR\3\2\2\2\u0160\u0161\7?\2\2\u0161")
        buf.write("T\3\2\2\2\u0162\u0163\7<\2\2\u0163\u0164\7?\2\2\u0164")
        buf.write("V\3\2\2\2\u0165\u0166\7-\2\2\u0166\u0167\7?\2\2\u0167")
        buf.write("X\3\2\2\2\u0168\u0169\7/\2\2\u0169\u016a\7?\2\2\u016a")
        buf.write("Z\3\2\2\2\u016b\u016c\7,\2\2\u016c\u016d\7?\2\2\u016d")
        buf.write("\\\3\2\2\2\u016e\u016f\7\61\2\2\u016f\u0170\7?\2\2\u0170")
        buf.write("^\3\2\2\2\u0171\u0172\7\'\2\2\u0172\u0173\7?\2\2\u0173")
        buf.write("`\3\2\2\2\u0174\u0175\7\60\2\2\u0175b\3\2\2\2\u0176\u0177")
        buf.write("\7k\2\2\u0177\u0178\7h\2\2\u0178d\3\2\2\2\u0179\u017a")
        buf.write("\7g\2\2\u017a\u017b\7n\2\2\u017b\u017c\7u\2\2\u017c\u017d")
        buf.write("\7g\2\2\u017df\3\2\2\2\u017e\u017f\7h\2\2\u017f\u0180")
        buf.write("\7q\2\2\u0180\u0181\7t\2\2\u0181h\3\2\2\2\u0182\u0183")
        buf.write("\7u\2\2\u0183\u0184\7v\2\2\u0184\u0185\7t\2\2\u0185\u0186")
        buf.write("\7w\2\2\u0186\u0187\7e\2\2\u0187\u0188\7v\2\2\u0188j\3")
        buf.write("\2\2\2\u0189\u018a\7k\2\2\u018a\u018b\7p\2\2\u018b\u018c")
        buf.write("\7v\2\2\u018c\u018d\7g\2\2\u018d\u018e\7t\2\2\u018e\u018f")
        buf.write("\7h\2\2\u018f\u0190\7c\2\2\u0190\u0191\7e\2\2\u0191\u0192")
        buf.write("\7g\2\2\u0192l\3\2\2\2\u0193\u0194\7u\2\2\u0194\u0195")
        buf.write("\7v\2\2\u0195\u0196\7t\2\2\u0196\u0197\7k\2\2\u0197\u0198")
        buf.write("\7p\2\2\u0198\u0199\7i\2\2\u0199n\3\2\2\2\u019a\u019b")
        buf.write("\7e\2\2\u019b\u019c\7q\2\2\u019c\u019d\7p\2\2\u019d\u019e")
        buf.write("\7u\2\2\u019e\u019f\7v\2\2\u019fp\3\2\2\2\u01a0\u01a1")
        buf.write("\7x\2\2\u01a1\u01a2\7c\2\2\u01a2\u01a3\7t\2\2\u01a3r\3")
        buf.write("\2\2\2\u01a4\u01a5\7t\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7")
        buf.write("\7v\2\2\u01a7\u01a8\7w\2\2\u01a8\u01a9\7t\2\2\u01a9\u01aa")
        buf.write("\7p\2\2\u01aat\3\2\2\2\u01ab\u01ac\7h\2\2\u01ac\u01ad")
        buf.write("\7w\2\2\u01ad\u01ae\7p\2\2\u01ae\u01af\7e\2\2\u01afv\3")
        buf.write("\2\2\2\u01b0\u01b1\7k\2\2\u01b1\u01b2\7p\2\2\u01b2\u01b3")
        buf.write("\7v\2\2\u01b3x\3\2\2\2\u01b4\u01b5\7v\2\2\u01b5\u01b6")
        buf.write("\7{\2\2\u01b6\u01b7\7r\2\2\u01b7\u01b8\7g\2\2\u01b8z\3")
        buf.write("\2\2\2\u01b9\u01ba\7h\2\2\u01ba\u01bb\7n\2\2\u01bb\u01bc")
        buf.write("\7q\2\2\u01bc\u01bd\7c\2\2\u01bd\u01be\7v\2\2\u01be|\3")
        buf.write("\2\2\2\u01bf\u01c0\7d\2\2\u01c0\u01c1\7q\2\2\u01c1\u01c2")
        buf.write("\7q\2\2\u01c2\u01c3\7n\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5")
        buf.write("\7c\2\2\u01c5\u01c6\7p\2\2\u01c6~\3\2\2\2\u01c7\u01c8")
        buf.write("\7e\2\2\u01c8\u01c9\7q\2\2\u01c9\u01ca\7p\2\2\u01ca\u01cb")
        buf.write("\7v\2\2\u01cb\u01cc\7k\2\2\u01cc\u01cd\7p\2\2\u01cd\u01ce")
        buf.write("\7w\2\2\u01ce\u01cf\7g\2\2\u01cf\u0080\3\2\2\2\u01d0\u01d1")
        buf.write("\7d\2\2\u01d1\u01d2\7t\2\2\u01d2\u01d3\7g\2\2\u01d3\u01d4")
        buf.write("\7c\2\2\u01d4\u01d5\7m\2\2\u01d5\u0082\3\2\2\2\u01d6\u01d7")
        buf.write("\7t\2\2\u01d7\u01d8\7c\2\2\u01d8\u01d9\7p\2\2\u01d9\u01da")
        buf.write("\7i\2\2\u01da\u01db\7g\2\2\u01db\u0084\3\2\2\2\u01dc\u01dd")
        buf.write("\7v\2\2\u01dd\u01de\7t\2\2\u01de\u01df\7w\2\2\u01df\u01e0")
        buf.write("\7g\2\2\u01e0\u0086\3\2\2\2\u01e1\u01e2\7h\2\2\u01e2\u01e3")
        buf.write("\7c\2\2\u01e3\u01e4\7n\2\2\u01e4\u01e5\7u\2\2\u01e5\u01e6")
        buf.write("\7g\2\2\u01e6\u0088\3\2\2\2\u01e7\u01e8\7p\2\2\u01e8\u01e9")
        buf.write("\7k\2\2\u01e9\u01ea\7n\2\2\u01ea\u008a\3\2\2\2\u01eb\u01ef")
        buf.write("\t\17\2\2\u01ec\u01ee\t\20\2\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write("\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u008c\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f3\7")
        buf.write("^\2\2\u01f3\u01f4\t\21\2\2\u01f4\u008e\3\2\2\2\u01f5\u01f6")
        buf.write("\13\2\2\2\u01f6\u01f7\bH\4\2\u01f7\u0090\3\2\2\2\u01f8")
        buf.write("\u01fd\7$\2\2\u01f9\u01fc\5\u008dG\2\u01fa\u01fc\n\22")
        buf.write("\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff")
        buf.write("\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u0200\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0201\bI\5\2")
        buf.write("\u0201\u0092\3\2\2\2\u0202\u0207\7$\2\2\u0203\u0206\5")
        buf.write("\u008dG\2\u0204\u0206\n\22\2\2\u0205\u0203\3\2\2\2\u0205")
        buf.write("\u0204\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\u020a\3\2\2\2\u0209\u0207\3")
        buf.write("\2\2\2\u020a\u020b\7^\2\2\u020b\u020c\n\21\2\2\u020c\u020d")
        buf.write("\bJ\6\2\u020d\u0094\3\2\2\2\35\2\u009c\u009e\u00ae\u00c2")
        buf.write("\u00d4\u00d9\u00db\u00e6\u00ec\u00f0\u00f4\u00f9\u00ff")
        buf.write("\u0106\u0109\u010f\u0114\u011a\u011f\u0125\u012a\u01ef")
        buf.write("\u01fb\u01fd\u0205\u0207\7\b\2\2\t\24\2\3H\2\3I\3\3J\4")
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

    ruleNames = [ "NESTED_COMMENT", "ML_COMMENT", "SL_COMMENT", "IMPLICIT_SEMI", 
                  "WS", "NL", "NIL_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                  "ESC_SEQ", "FLOAT_LITERAL", "EXP", "INTERGER_LITERAL", 
                  "DEC", "BIN", "OCT", "HEX", "COLON", "LPAREN", "RPAREN", 
                  "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMI", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", 
                  "LE", "GT", "GE", "AND", "OR", "NOT", "ASSIGN", "COLON_ASSIGN", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "DOT", "IF", "ELSE", "FOR", "STRUCT", "INTERFACE", 
                  "STRING", "CONST", "VAR", "RETURN", "FUNC", "INT", "TYPE", 
                  "FLOAT", "BOOLEAN", "CONTINUE", "BREAK", "RANGE", "TRUE", 
                  "FALSE", "NIL", "IDENTIFIER", "ESC", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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
     


