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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0203\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\3\3\3\3\3\3\3\3\7\3\u009d\n\3\f\3\16\3\u00a0\13\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00ab\n\4\f\4\16")
        buf.write("\4\u00ae\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\6\6\u00b7\n")
        buf.write("\6\r\6\16\6\u00b8\3\6\3\6\3\7\3\7\3\b\3\b\5\b\u00c1\n")
        buf.write("\b\3\t\3\t\3\t\7\t\u00c6\n\t\f\t\16\t\u00c9\13\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\13\6\13\u00d1\n\13\r\13\16\13\u00d2\3")
        buf.write("\13\3\13\7\13\u00d7\n\13\f\13\16\13\u00da\13\13\3\13\7")
        buf.write("\13\u00dd\n\13\f\13\16\13\u00e0\13\13\3\13\7\13\u00e3")
        buf.write("\n\13\f\13\16\13\u00e6\13\13\3\f\3\f\7\f\u00ea\n\f\f\f")
        buf.write("\16\f\u00ed\13\f\3\r\3\r\3\r\3\r\5\r\u00f3\n\r\3\16\3")
        buf.write("\16\3\16\7\16\u00f8\n\16\f\16\16\16\u00fb\13\16\5\16\u00fd")
        buf.write("\n\16\3\17\3\17\3\17\3\17\5\17\u0103\n\17\3\17\6\17\u0106")
        buf.write("\n\17\r\17\16\17\u0107\3\20\3\20\3\20\3\20\5\20\u010e")
        buf.write("\n\20\3\20\6\20\u0111\n\20\r\20\16\20\u0112\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u0119\n\21\3\21\6\21\u011c\n\21\r\21\16")
        buf.write("\21\u011d\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
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
        buf.write("D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3F\3F\7F\u01e3\nF\fF\16F")
        buf.write("\u01e6\13F\3G\3G\3G\3H\3H\3H\3I\3I\3I\7I\u01f1\nI\fI\16")
        buf.write("I\u01f4\13I\3I\3I\3J\3J\3J\7J\u01fb\nJ\fJ\16J\u01fe\13")
        buf.write("J\3J\3J\3J\3J\3\u009e\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\2\25\13\27\2\31\f\33\2\35\2\37\2!\2#\r%\16\'")
        buf.write("\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31=\32")
        buf.write("?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g")
        buf.write("/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083")
        buf.write("=\u0085>\u0087?\u0089@\u008bA\u008d\2\u008fB\u0091C\u0093")
        buf.write("D\3\2\21\4\2\f\f\17\17\5\2\13\13\16\17\"\"\4\2$$^^\7\2")
        buf.write("$$^^ppttvv\3\2\62;\4\2GGgg\4\2--//\3\2\63;\3\2\62\63\3")
        buf.write("\2\629\5\2\62;CHch\5\2C\\aac|\6\2\62;C\\aac|\n\2$$))^")
        buf.write("^ddhhppttvv\6\2\f\f\17\17$$^^\2\u0217\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\25\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u0097")
        buf.write("\3\2\2\2\7\u00a6\3\2\2\2\t\u00b1\3\2\2\2\13\u00b6\3\2")
        buf.write("\2\2\r\u00bc\3\2\2\2\17\u00c0\3\2\2\2\21\u00c2\3\2\2\2")
        buf.write("\23\u00cc\3\2\2\2\25\u00d0\3\2\2\2\27\u00e7\3\2\2\2\31")
        buf.write("\u00f2\3\2\2\2\33\u00fc\3\2\2\2\35\u0102\3\2\2\2\37\u010d")
        buf.write("\3\2\2\2!\u0118\3\2\2\2#\u011f\3\2\2\2%\u0121\3\2\2\2")
        buf.write("\'\u0123\3\2\2\2)\u0125\3\2\2\2+\u0127\3\2\2\2-\u0129")
        buf.write("\3\2\2\2/\u012b\3\2\2\2\61\u012d\3\2\2\2\63\u012f\3\2")
        buf.write("\2\2\65\u0131\3\2\2\2\67\u0133\3\2\2\29\u0135\3\2\2\2")
        buf.write(";\u0137\3\2\2\2=\u0139\3\2\2\2?\u013b\3\2\2\2A\u013d\3")
        buf.write("\2\2\2C\u0140\3\2\2\2E\u0143\3\2\2\2G\u0145\3\2\2\2I\u0148")
        buf.write("\3\2\2\2K\u014a\3\2\2\2M\u014d\3\2\2\2O\u0150\3\2\2\2")
        buf.write("Q\u0153\3\2\2\2S\u0155\3\2\2\2U\u0157\3\2\2\2W\u015a\3")
        buf.write("\2\2\2Y\u015d\3\2\2\2[\u0160\3\2\2\2]\u0163\3\2\2\2_\u0166")
        buf.write("\3\2\2\2a\u0169\3\2\2\2c\u016b\3\2\2\2e\u016e\3\2\2\2")
        buf.write("g\u0173\3\2\2\2i\u0177\3\2\2\2k\u017e\3\2\2\2m\u0188\3")
        buf.write("\2\2\2o\u018f\3\2\2\2q\u0195\3\2\2\2s\u0199\3\2\2\2u\u01a0")
        buf.write("\3\2\2\2w\u01a5\3\2\2\2y\u01a9\3\2\2\2{\u01ae\3\2\2\2")
        buf.write("}\u01b4\3\2\2\2\177\u01bc\3\2\2\2\u0081\u01c5\3\2\2\2")
        buf.write("\u0083\u01cb\3\2\2\2\u0085\u01d1\3\2\2\2\u0087\u01d6\3")
        buf.write("\2\2\2\u0089\u01dc\3\2\2\2\u008b\u01e0\3\2\2\2\u008d\u01e7")
        buf.write("\3\2\2\2\u008f\u01ea\3\2\2\2\u0091\u01ed\3\2\2\2\u0093")
        buf.write("\u01f7\3\2\2\2\u0095\u0096\7a\2\2\u0096\4\3\2\2\2\u0097")
        buf.write("\u0098\7\61\2\2\u0098\u0099\7,\2\2\u0099\u009e\3\2\2\2")
        buf.write("\u009a\u009d\5\5\3\2\u009b\u009d\13\2\2\2\u009c\u009a")
        buf.write("\3\2\2\2\u009c\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a1\3\2\2\2")
        buf.write("\u00a0\u009e\3\2\2\2\u00a1\u00a2\7,\2\2\u00a2\u00a3\7")
        buf.write("\61\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\b\3\2\2\u00a5")
        buf.write("\6\3\2\2\2\u00a6\u00a7\7\61\2\2\u00a7\u00a8\7\61\2\2\u00a8")
        buf.write("\u00ac\3\2\2\2\u00a9\u00ab\n\2\2\2\u00aa\u00a9\3\2\2\2")
        buf.write("\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3")
        buf.write("\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0")
        buf.write("\b\4\2\2\u00b0\b\3\2\2\2\u00b1\u00b2\7\f\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\u00b4\b\5\2\2\u00b4\n\3\2\2\2\u00b5\u00b7")
        buf.write("\t\3\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2")
        buf.write("\u00ba\u00bb\b\6\2\2\u00bb\f\3\2\2\2\u00bc\u00bd\5\u0089")
        buf.write("E\2\u00bd\16\3\2\2\2\u00be\u00c1\5\u0085C\2\u00bf\u00c1")
        buf.write("\5\u0087D\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1")
        buf.write("\20\3\2\2\2\u00c2\u00c7\7$\2\2\u00c3\u00c6\5\u008dG\2")
        buf.write("\u00c4\u00c6\n\4\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3")
        buf.write("\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca")
        buf.write("\u00cb\7$\2\2\u00cb\22\3\2\2\2\u00cc\u00cd\7^\2\2\u00cd")
        buf.write("\u00ce\t\5\2\2\u00ce\24\3\2\2\2\u00cf\u00d1\t\6\2\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d8\7")
        buf.write("\60\2\2\u00d5\u00d7\t\6\2\2\u00d6\u00d5\3\2\2\2\u00d7")
        buf.write("\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00de\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dd\5")
        buf.write("\27\f\2\u00dc\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e4\3\2\2\2")
        buf.write("\u00e0\u00de\3\2\2\2\u00e1\u00e3\t\6\2\2\u00e2\u00e1\3")
        buf.write("\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\26\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00eb")
        buf.write("\t\7\2\2\u00e8\u00ea\t\b\2\2\u00e9\u00e8\3\2\2\2\u00ea")
        buf.write("\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\30\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f3\5\33")
        buf.write("\16\2\u00ef\u00f3\5\35\17\2\u00f0\u00f3\5\37\20\2\u00f1")
        buf.write("\u00f3\5!\21\2\u00f2\u00ee\3\2\2\2\u00f2\u00ef\3\2\2\2")
        buf.write("\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\32\3\2")
        buf.write("\2\2\u00f4\u00fd\7\62\2\2\u00f5\u00f9\t\t\2\2\u00f6\u00f8")
        buf.write("\t\6\2\2\u00f7\u00f6\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fd\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fc\u00f4\3\2\2\2\u00fc\u00f5\3")
        buf.write("\2\2\2\u00fd\34\3\2\2\2\u00fe\u00ff\7\62\2\2\u00ff\u0103")
        buf.write("\7d\2\2\u0100\u0101\7\62\2\2\u0101\u0103\7D\2\2\u0102")
        buf.write("\u00fe\3\2\2\2\u0102\u0100\3\2\2\2\u0103\u0105\3\2\2\2")
        buf.write("\u0104\u0106\t\n\2\2\u0105\u0104\3\2\2\2\u0106\u0107\3")
        buf.write("\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\36")
        buf.write("\3\2\2\2\u0109\u010a\7\62\2\2\u010a\u010e\7q\2\2\u010b")
        buf.write("\u010c\7\62\2\2\u010c\u010e\7Q\2\2\u010d\u0109\3\2\2\2")
        buf.write("\u010d\u010b\3\2\2\2\u010e\u0110\3\2\2\2\u010f\u0111\t")
        buf.write("\13\2\2\u0110\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113 \3\2\2\2\u0114")
        buf.write("\u0115\7\62\2\2\u0115\u0119\7z\2\2\u0116\u0117\7\62\2")
        buf.write("\2\u0117\u0119\7Z\2\2\u0118\u0114\3\2\2\2\u0118\u0116")
        buf.write("\3\2\2\2\u0119\u011b\3\2\2\2\u011a\u011c\t\f\2\2\u011b")
        buf.write("\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011b\3\2\2\2")
        buf.write("\u011d\u011e\3\2\2\2\u011e\"\3\2\2\2\u011f\u0120\t\b\2")
        buf.write("\2\u0120$\3\2\2\2\u0121\u0122\7<\2\2\u0122&\3\2\2\2\u0123")
        buf.write("\u0124\7*\2\2\u0124(\3\2\2\2\u0125\u0126\7+\2\2\u0126")
        buf.write("*\3\2\2\2\u0127\u0128\7}\2\2\u0128,\3\2\2\2\u0129\u012a")
        buf.write("\7\177\2\2\u012a.\3\2\2\2\u012b\u012c\7]\2\2\u012c\60")
        buf.write("\3\2\2\2\u012d\u012e\7_\2\2\u012e\62\3\2\2\2\u012f\u0130")
        buf.write("\7.\2\2\u0130\64\3\2\2\2\u0131\u0132\7=\2\2\u0132\66\3")
        buf.write("\2\2\2\u0133\u0134\7-\2\2\u01348\3\2\2\2\u0135\u0136\7")
        buf.write("/\2\2\u0136:\3\2\2\2\u0137\u0138\7,\2\2\u0138<\3\2\2\2")
        buf.write("\u0139\u013a\7\61\2\2\u013a>\3\2\2\2\u013b\u013c\7\'\2")
        buf.write("\2\u013c@\3\2\2\2\u013d\u013e\7?\2\2\u013e\u013f\7?\2")
        buf.write("\2\u013fB\3\2\2\2\u0140\u0141\7#\2\2\u0141\u0142\7?\2")
        buf.write("\2\u0142D\3\2\2\2\u0143\u0144\7>\2\2\u0144F\3\2\2\2\u0145")
        buf.write("\u0146\7>\2\2\u0146\u0147\7?\2\2\u0147H\3\2\2\2\u0148")
        buf.write("\u0149\7@\2\2\u0149J\3\2\2\2\u014a\u014b\7@\2\2\u014b")
        buf.write("\u014c\7?\2\2\u014cL\3\2\2\2\u014d\u014e\7(\2\2\u014e")
        buf.write("\u014f\7(\2\2\u014fN\3\2\2\2\u0150\u0151\7~\2\2\u0151")
        buf.write("\u0152\7~\2\2\u0152P\3\2\2\2\u0153\u0154\7#\2\2\u0154")
        buf.write("R\3\2\2\2\u0155\u0156\7?\2\2\u0156T\3\2\2\2\u0157\u0158")
        buf.write("\7<\2\2\u0158\u0159\7?\2\2\u0159V\3\2\2\2\u015a\u015b")
        buf.write("\7-\2\2\u015b\u015c\7?\2\2\u015cX\3\2\2\2\u015d\u015e")
        buf.write("\7/\2\2\u015e\u015f\7?\2\2\u015fZ\3\2\2\2\u0160\u0161")
        buf.write("\7,\2\2\u0161\u0162\7?\2\2\u0162\\\3\2\2\2\u0163\u0164")
        buf.write("\7\61\2\2\u0164\u0165\7?\2\2\u0165^\3\2\2\2\u0166\u0167")
        buf.write("\7\'\2\2\u0167\u0168\7?\2\2\u0168`\3\2\2\2\u0169\u016a")
        buf.write("\7\60\2\2\u016ab\3\2\2\2\u016b\u016c\7k\2\2\u016c\u016d")
        buf.write("\7h\2\2\u016dd\3\2\2\2\u016e\u016f\7g\2\2\u016f\u0170")
        buf.write("\7n\2\2\u0170\u0171\7u\2\2\u0171\u0172\7g\2\2\u0172f\3")
        buf.write("\2\2\2\u0173\u0174\7h\2\2\u0174\u0175\7q\2\2\u0175\u0176")
        buf.write("\7t\2\2\u0176h\3\2\2\2\u0177\u0178\7u\2\2\u0178\u0179")
        buf.write("\7v\2\2\u0179\u017a\7t\2\2\u017a\u017b\7w\2\2\u017b\u017c")
        buf.write("\7e\2\2\u017c\u017d\7v\2\2\u017dj\3\2\2\2\u017e\u017f")
        buf.write("\7k\2\2\u017f\u0180\7p\2\2\u0180\u0181\7v\2\2\u0181\u0182")
        buf.write("\7g\2\2\u0182\u0183\7t\2\2\u0183\u0184\7h\2\2\u0184\u0185")
        buf.write("\7c\2\2\u0185\u0186\7e\2\2\u0186\u0187\7g\2\2\u0187l\3")
        buf.write("\2\2\2\u0188\u0189\7u\2\2\u0189\u018a\7v\2\2\u018a\u018b")
        buf.write("\7t\2\2\u018b\u018c\7k\2\2\u018c\u018d\7p\2\2\u018d\u018e")
        buf.write("\7i\2\2\u018en\3\2\2\2\u018f\u0190\7e\2\2\u0190\u0191")
        buf.write("\7q\2\2\u0191\u0192\7p\2\2\u0192\u0193\7u\2\2\u0193\u0194")
        buf.write("\7v\2\2\u0194p\3\2\2\2\u0195\u0196\7x\2\2\u0196\u0197")
        buf.write("\7c\2\2\u0197\u0198\7t\2\2\u0198r\3\2\2\2\u0199\u019a")
        buf.write("\7t\2\2\u019a\u019b\7g\2\2\u019b\u019c\7v\2\2\u019c\u019d")
        buf.write("\7w\2\2\u019d\u019e\7t\2\2\u019e\u019f\7p\2\2\u019ft\3")
        buf.write("\2\2\2\u01a0\u01a1\7h\2\2\u01a1\u01a2\7w\2\2\u01a2\u01a3")
        buf.write("\7p\2\2\u01a3\u01a4\7e\2\2\u01a4v\3\2\2\2\u01a5\u01a6")
        buf.write("\7k\2\2\u01a6\u01a7\7p\2\2\u01a7\u01a8\7v\2\2\u01a8x\3")
        buf.write("\2\2\2\u01a9\u01aa\7v\2\2\u01aa\u01ab\7{\2\2\u01ab\u01ac")
        buf.write("\7r\2\2\u01ac\u01ad\7g\2\2\u01adz\3\2\2\2\u01ae\u01af")
        buf.write("\7h\2\2\u01af\u01b0\7n\2\2\u01b0\u01b1\7q\2\2\u01b1\u01b2")
        buf.write("\7c\2\2\u01b2\u01b3\7v\2\2\u01b3|\3\2\2\2\u01b4\u01b5")
        buf.write("\7d\2\2\u01b5\u01b6\7q\2\2\u01b6\u01b7\7q\2\2\u01b7\u01b8")
        buf.write("\7n\2\2\u01b8\u01b9\7g\2\2\u01b9\u01ba\7c\2\2\u01ba\u01bb")
        buf.write("\7p\2\2\u01bb~\3\2\2\2\u01bc\u01bd\7e\2\2\u01bd\u01be")
        buf.write("\7q\2\2\u01be\u01bf\7p\2\2\u01bf\u01c0\7v\2\2\u01c0\u01c1")
        buf.write("\7k\2\2\u01c1\u01c2\7p\2\2\u01c2\u01c3\7w\2\2\u01c3\u01c4")
        buf.write("\7g\2\2\u01c4\u0080\3\2\2\2\u01c5\u01c6\7d\2\2\u01c6\u01c7")
        buf.write("\7t\2\2\u01c7\u01c8\7g\2\2\u01c8\u01c9\7c\2\2\u01c9\u01ca")
        buf.write("\7m\2\2\u01ca\u0082\3\2\2\2\u01cb\u01cc\7t\2\2\u01cc\u01cd")
        buf.write("\7c\2\2\u01cd\u01ce\7p\2\2\u01ce\u01cf\7i\2\2\u01cf\u01d0")
        buf.write("\7g\2\2\u01d0\u0084\3\2\2\2\u01d1\u01d2\7v\2\2\u01d2\u01d3")
        buf.write("\7t\2\2\u01d3\u01d4\7w\2\2\u01d4\u01d5\7g\2\2\u01d5\u0086")
        buf.write("\3\2\2\2\u01d6\u01d7\7h\2\2\u01d7\u01d8\7c\2\2\u01d8\u01d9")
        buf.write("\7n\2\2\u01d9\u01da\7u\2\2\u01da\u01db\7g\2\2\u01db\u0088")
        buf.write("\3\2\2\2\u01dc\u01dd\7p\2\2\u01dd\u01de\7k\2\2\u01de\u01df")
        buf.write("\7n\2\2\u01df\u008a\3\2\2\2\u01e0\u01e4\t\r\2\2\u01e1")
        buf.write("\u01e3\t\16\2\2\u01e2\u01e1\3\2\2\2\u01e3\u01e6\3\2\2")
        buf.write("\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u008c")
        buf.write("\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8\7^\2\2\u01e8")
        buf.write("\u01e9\t\17\2\2\u01e9\u008e\3\2\2\2\u01ea\u01eb\13\2\2")
        buf.write("\2\u01eb\u01ec\bH\3\2\u01ec\u0090\3\2\2\2\u01ed\u01f2")
        buf.write("\7$\2\2\u01ee\u01f1\5\u008dG\2\u01ef\u01f1\n\20\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1\u01f4\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f5\3")
        buf.write("\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f6\bI\4\2\u01f6\u0092")
        buf.write("\3\2\2\2\u01f7\u01fc\7$\2\2\u01f8\u01fb\5\u008dG\2\u01f9")
        buf.write("\u01fb\n\20\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01f9\3\2\2")
        buf.write("\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd")
        buf.write("\3\2\2\2\u01fd\u01ff\3\2\2\2\u01fe\u01fc\3\2\2\2\u01ff")
        buf.write("\u0200\7^\2\2\u0200\u0201\n\17\2\2\u0201\u0202\bJ\5\2")
        buf.write("\u0202\u0094\3\2\2\2\35\2\u009c\u009e\u00ac\u00b8\u00c0")
        buf.write("\u00c5\u00c7\u00d2\u00d8\u00de\u00e4\u00eb\u00f2\u00f9")
        buf.write("\u00fc\u0102\u0107\u010d\u0112\u0118\u011d\u01e4\u01f0")
        buf.write("\u01f2\u01fa\u01fc\6\b\2\2\3H\2\3I\3\3J\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ML_COMMENT = 2
    SL_COMMENT = 3
    NL = 4
    WS = 5
    NIL_LITERAL = 6
    BOOLEAN_LITERAL = 7
    STRING_LITERAL = 8
    FLOAT_LITERAL = 9
    INTERGER_LITERAL = 10
    SIGN = 11
    COLON = 12
    LPAREN = 13
    RPAREN = 14
    LBRACE = 15
    RBRACE = 16
    LBRACK = 17
    RBRACK = 18
    COMMA = 19
    SEMI = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQ = 26
    NEQ = 27
    LT = 28
    LE = 29
    GT = 30
    GE = 31
    AND = 32
    OR = 33
    NOT = 34
    ASSIGN = 35
    COLON_ASSIGN = 36
    ADD_ASSIGN = 37
    SUB_ASSIGN = 38
    MUL_ASSIGN = 39
    DIV_ASSIGN = 40
    MOD_ASSIGN = 41
    DOT = 42
    IF = 43
    ELSE = 44
    FOR = 45
    STRUCT = 46
    INTERFACE = 47
    STRING = 48
    CONST = 49
    VAR = 50
    RETURN = 51
    FUNC = 52
    INT = 53
    TYPE = 54
    FLOAT = 55
    BOOLEAN = 56
    CONTINUE = 57
    BREAK = 58
    RANGE = 59
    TRUE = 60
    FALSE = 61
    NIL = 62
    IDENTIFIER = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'_'", "'\n'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "','", "';'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", 
            "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "'if'", 
            "'else'", "'for'", "'struct'", "'interface'", "'string'", "'const'", 
            "'var'", "'return'", "'func'", "'int'", "'type'", "'float'", 
            "'boolean'", "'continue'", "'break'", "'range'", "'true'", "'false'", 
            "'nil'" ]

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

    ruleNames = [ "T__0", "ML_COMMENT", "SL_COMMENT", "NL", "WS", "NIL_LITERAL", 
                  "BOOLEAN_LITERAL", "STRING_LITERAL", "ESC_SEQ", "FLOAT_LITERAL", 
                  "EXP", "INTERGER_LITERAL", "DEC", "BIN", "OCT", "HEX", 
                  "SIGN", "COLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
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
     


