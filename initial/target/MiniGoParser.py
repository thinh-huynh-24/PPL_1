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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u017b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\6\2F\n\2\r\2\16\2G")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3W\n\3\3\4\3\4\3\4\5\4\\\n\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6l\n\6\f\6\16\6o\13")
        buf.write("\6\3\6\3\6\5\6s\n\6\3\7\3\7\3\7\3\7\5\7y\n\7\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\5\t\u0081\n\t\3\t\3\t\5\t\u0085\n\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\5\r\u0099\n\r\3\r\3\r\3\16\3\16\5\16")
        buf.write("\u009f\n\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u00ac\n\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17")
        buf.write("\u00bd\n\17\f\17\16\17\u00c0\13\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00c9\n\20\3\21\3\21\3\21\3\21\6")
        buf.write("\21\u00cf\n\21\r\21\16\21\u00d0\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\7\24")
        buf.write("\u00e1\n\24\f\24\16\24\u00e4\13\24\3\24\3\24\3\24\3\24")
        buf.write("\7\24\u00ea\n\24\f\24\16\24\u00ed\13\24\3\24\3\24\6\24")
        buf.write("\u00f1\n\24\r\24\16\24\u00f2\5\24\u00f5\n\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\7\25\u00fe\n\25\f\25\16\25\u0101")
        buf.write("\13\25\5\25\u0103\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\5\27\u0111\n\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\7\30\u0119\n\30\f\30\16\30\u011c")
        buf.write("\13\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\5\32\u0129\n\32\3\32\3\32\5\32\u012d\n\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0138\n")
        buf.write("\33\f\33\16\33\u013b\13\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\7\33\u0143\n\33\f\33\16\33\u0146\13\33\3\33\5\33\u0149")
        buf.write("\n\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\5\36\u0155\n\36\3\36\3\36\5\36\u0159\n\36\3\37\3\37\3")
        buf.write("\37\7\37\u015e\n\37\f\37\16\37\u0161\13\37\3 \3 \3 \3")
        buf.write("!\3!\3!\7!\u0169\n!\f!\16!\u016c\13!\3!\3!\3\"\3\"\3\"")
        buf.write("\5\"\u0173\n\"\3\"\3\"\3\"\3\"\5\"\u0179\n\"\3\"\2\3\34")
        buf.write("#\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@B\2\n\3\2%+\4\2\3\3AA\4\2\6\6\26\26\4\2\30")
        buf.write("\30$$\3\2\31\33\3\2\27\30\3\2\34!\6\2\62\62\67\679:@A")
        buf.write("\2\u0192\2E\3\2\2\2\4V\3\2\2\2\6[\3\2\2\2\ba\3\2\2\2\n")
        buf.write("c\3\2\2\2\ft\3\2\2\2\16|\3\2\2\2\20\u0080\3\2\2\2\22\u0089")
        buf.write("\3\2\2\2\24\u0090\3\2\2\2\26\u0093\3\2\2\2\30\u0096\3")
        buf.write("\2\2\2\32\u009e\3\2\2\2\34\u00ab\3\2\2\2\36\u00c8\3\2")
        buf.write("\2\2 \u00ca\3\2\2\2\"\u00d2\3\2\2\2$\u00d6\3\2\2\2&\u00db")
        buf.write("\3\2\2\2(\u00f8\3\2\2\2*\u0106\3\2\2\2,\u010a\3\2\2\2")
        buf.write(".\u0116\3\2\2\2\60\u011f\3\2\2\2\62\u0125\3\2\2\2\64\u0130")
        buf.write("\3\2\2\2\66\u014c\3\2\2\28\u014f\3\2\2\2:\u0152\3\2\2")
        buf.write("\2<\u015a\3\2\2\2>\u0162\3\2\2\2@\u016a\3\2\2\2B\u0178")
        buf.write("\3\2\2\2DF\5\4\3\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2")
        buf.write("\2\2HI\3\2\2\2IJ\7\2\2\3J\3\3\2\2\2KW\5\62\32\2LW\5\60")
        buf.write("\31\2MW\5,\27\2NW\5\6\4\2OW\5\n\6\2PW\5\f\7\2QW\5\22\n")
        buf.write("\2RW\5\24\13\2SW\5\26\f\2TW\5\30\r\2UW\5\32\16\2VK\3\2")
        buf.write("\2\2VL\3\2\2\2VM\3\2\2\2VN\3\2\2\2VO\3\2\2\2VP\3\2\2\2")
        buf.write("VQ\3\2\2\2VR\3\2\2\2VS\3\2\2\2VT\3\2\2\2VU\3\2\2\2W\5")
        buf.write("\3\2\2\2X\\\5B\"\2Y\\\5 \21\2Z\\\5\"\22\2[X\3\2\2\2[Y")
        buf.write("\3\2\2\2[Z\3\2\2\2\\]\3\2\2\2]^\5\b\5\2^_\5\34\17\2_`")
        buf.write("\7\26\2\2`\7\3\2\2\2ab\t\2\2\2b\t\3\2\2\2cd\7-\2\2de\5")
        buf.write("\34\17\2em\5.\30\2fg\7.\2\2gh\7-\2\2hi\5\34\17\2ij\5.")
        buf.write("\30\2jl\3\2\2\2kf\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2")
        buf.write("\2nr\3\2\2\2om\3\2\2\2pq\7.\2\2qs\5.\30\2rp\3\2\2\2rs")
        buf.write("\3\2\2\2s\13\3\2\2\2tx\7/\2\2uy\5\16\b\2vy\5\20\t\2wy")
        buf.write("\5\22\n\2xu\3\2\2\2xv\3\2\2\2xw\3\2\2\2yz\3\2\2\2z{\5")
        buf.write(".\30\2{\r\3\2\2\2|}\5\34\17\2}\17\3\2\2\2~\u0081\5\6\4")
        buf.write("\2\177\u0081\5\62\32\2\u0080~\3\2\2\2\u0080\177\3\2\2")
        buf.write("\2\u0081\u0082\3\2\2\2\u0082\u0084\7\26\2\2\u0083\u0085")
        buf.write("\5\34\17\2\u0084\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0087\7\26\2\2\u0087\u0088\5\6\4")
        buf.write("\2\u0088\21\3\2\2\2\u0089\u008a\t\3\2\2\u008a\u008b\7")
        buf.write("\25\2\2\u008b\u008c\7A\2\2\u008c\u008d\5\b\5\2\u008d\u008e")
        buf.write("\7=\2\2\u008e\u008f\7A\2\2\u008f\23\3\2\2\2\u0090\u0091")
        buf.write("\7<\2\2\u0091\u0092\7\26\2\2\u0092\25\3\2\2\2\u0093\u0094")
        buf.write("\7;\2\2\u0094\u0095\7\26\2\2\u0095\27\3\2\2\2\u0096\u0098")
        buf.write("\7\65\2\2\u0097\u0099\5\34\17\2\u0098\u0097\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\7\26\2")
        buf.write("\2\u009b\31\3\2\2\2\u009c\u009d\7A\2\2\u009d\u009f\7,")
        buf.write("\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\u00a1\7A\2\2\u00a1\u00a2\5:\36\2\u00a2")
        buf.write("\u00a3\t\4\2\2\u00a3\33\3\2\2\2\u00a4\u00a5\b\17\1\2\u00a5")
        buf.write("\u00ac\5\36\20\2\u00a6\u00ac\5 \21\2\u00a7\u00ac\5\"\22")
        buf.write("\2\u00a8\u00ac\5$\23\2\u00a9\u00aa\t\5\2\2\u00aa\u00ac")
        buf.write("\5\34\17\b\u00ab\u00a4\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab")
        buf.write("\u00a7\3\2\2\2\u00ab\u00a8\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ac\u00be\3\2\2\2\u00ad\u00ae\f\7\2\2\u00ae\u00af\t")
        buf.write("\6\2\2\u00af\u00bd\5\34\17\b\u00b0\u00b1\f\6\2\2\u00b1")
        buf.write("\u00b2\t\7\2\2\u00b2\u00bd\5\34\17\7\u00b3\u00b4\f\5\2")
        buf.write("\2\u00b4\u00b5\t\b\2\2\u00b5\u00bd\5\34\17\6\u00b6\u00b7")
        buf.write("\f\4\2\2\u00b7\u00b8\7\"\2\2\u00b8\u00bd\5\34\17\5\u00b9")
        buf.write("\u00ba\f\3\2\2\u00ba\u00bb\7#\2\2\u00bb\u00bd\5\34\17")
        buf.write("\4\u00bc\u00ad\3\2\2\2\u00bc\u00b0\3\2\2\2\u00bc\u00b3")
        buf.write("\3\2\2\2\u00bc\u00b6\3\2\2\2\u00bc\u00b9\3\2\2\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\35\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c9\5B\"")
        buf.write("\2\u00c2\u00c9\5&\24\2\u00c3\u00c9\5(\25\2\u00c4\u00c5")
        buf.write("\7\17\2\2\u00c5\u00c6\5\34\17\2\u00c6\u00c7\7\20\2\2\u00c7")
        buf.write("\u00c9\3\2\2\2\u00c8\u00c1\3\2\2\2\u00c8\u00c2\3\2\2\2")
        buf.write("\u00c8\u00c3\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c9\37\3\2")
        buf.write("\2\2\u00ca\u00ce\7A\2\2\u00cb\u00cc\7\23\2\2\u00cc\u00cd")
        buf.write("\7\f\2\2\u00cd\u00cf\7\24\2\2\u00ce\u00cb\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1!\3\2\2\2\u00d2\u00d3\7A\2\2\u00d3\u00d4\7,\2\2")
        buf.write("\u00d4\u00d5\7A\2\2\u00d5#\3\2\2\2\u00d6\u00d7\7A\2\2")
        buf.write("\u00d7\u00d8\7,\2\2\u00d8\u00d9\7A\2\2\u00d9\u00da\5:")
        buf.write("\36\2\u00da%\3\2\2\2\u00db\u00dc\5@!\2\u00dc\u00f4\7\23")
        buf.write("\2\2\u00dd\u00e2\5\34\17\2\u00de\u00df\7\25\2\2\u00df")
        buf.write("\u00e1\5\34\17\2\u00e0\u00de\3\2\2\2\u00e1\u00e4\3\2\2")
        buf.write("\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00f5")
        buf.write("\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6\7\23\2\2\u00e6")
        buf.write("\u00eb\5\34\17\2\u00e7\u00e8\7\25\2\2\u00e8\u00ea\5\34")
        buf.write("\17\2\u00e9\u00e7\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ee\u00ef\7\24\2\2\u00ef\u00f1\3\2\2")
        buf.write("\2\u00f0\u00e5\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4")
        buf.write("\u00dd\3\2\2\2\u00f4\u00f0\3\2\2\2\u00f5\u00f6\3\2\2\2")
        buf.write("\u00f6\u00f7\7\24\2\2\u00f7\'\3\2\2\2\u00f8\u00f9\7A\2")
        buf.write("\2\u00f9\u0102\7\21\2\2\u00fa\u00ff\5*\26\2\u00fb\u00fc")
        buf.write("\7\25\2\2\u00fc\u00fe\5*\26\2\u00fd\u00fb\3\2\2\2\u00fe")
        buf.write("\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u00fa\3")
        buf.write("\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105")
        buf.write("\7\22\2\2\u0105)\3\2\2\2\u0106\u0107\7A\2\2\u0107\u0108")
        buf.write("\7\16\2\2\u0108\u0109\5\34\17\2\u0109+\3\2\2\2\u010a\u0110")
        buf.write("\7\66\2\2\u010b\u010c\7\17\2\2\u010c\u010d\7A\2\2\u010d")
        buf.write("\u010e\5@!\2\u010e\u010f\7\20\2\2\u010f\u0111\3\2\2\2")
        buf.write("\u0110\u010b\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3")
        buf.write("\2\2\2\u0112\u0113\7A\2\2\u0113\u0114\5:\36\2\u0114\u0115")
        buf.write("\5.\30\2\u0115-\3\2\2\2\u0116\u011a\7\21\2\2\u0117\u0119")
        buf.write("\5\34\17\2\u0118\u0117\3\2\2\2\u0119\u011c\3\2\2\2\u011a")
        buf.write("\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d\3\2\2\2")
        buf.write("\u011c\u011a\3\2\2\2\u011d\u011e\7\22\2\2\u011e/\3\2\2")
        buf.write("\2\u011f\u0120\7\63\2\2\u0120\u0121\7A\2\2\u0121\u0122")
        buf.write("\7%\2\2\u0122\u0123\5\34\17\2\u0123\u0124\7\26\2\2\u0124")
        buf.write("\61\3\2\2\2\u0125\u0126\7\64\2\2\u0126\u0128\7A\2\2\u0127")
        buf.write("\u0129\5@!\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2\2\u0129")
        buf.write("\u012c\3\2\2\2\u012a\u012b\7%\2\2\u012b\u012d\5\34\17")
        buf.write("\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e")
        buf.write("\3\2\2\2\u012e\u012f\7\26\2\2\u012f\63\3\2\2\2\u0130\u0131")
        buf.write("\78\2\2\u0131\u0148\7A\2\2\u0132\u0133\7\60\2\2\u0133")
        buf.write("\u0139\7\21\2\2\u0134\u0135\5\66\34\2\u0135\u0136\7\26")
        buf.write("\2\2\u0136\u0138\3\2\2\2\u0137\u0134\3\2\2\2\u0138\u013b")
        buf.write("\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013c\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u0149\7\22\2")
        buf.write("\2\u013d\u013e\7\61\2\2\u013e\u0144\7\21\2\2\u013f\u0140")
        buf.write("\58\35\2\u0140\u0141\7\26\2\2\u0141\u0143\3\2\2\2\u0142")
        buf.write("\u013f\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2")
        buf.write("\u0144\u0145\3\2\2\2\u0145\u0147\3\2\2\2\u0146\u0144\3")
        buf.write("\2\2\2\u0147\u0149\7\22\2\2\u0148\u0132\3\2\2\2\u0148")
        buf.write("\u013d\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\7\26\2")
        buf.write("\2\u014b\65\3\2\2\2\u014c\u014d\7A\2\2\u014d\u014e\5@")
        buf.write("!\2\u014e\67\3\2\2\2\u014f\u0150\7A\2\2\u0150\u0151\5")
        buf.write(":\36\2\u01519\3\2\2\2\u0152\u0154\7\17\2\2\u0153\u0155")
        buf.write("\5<\37\2\u0154\u0153\3\2\2\2\u0154\u0155\3\2\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156\u0158\7\20\2\2\u0157\u0159\5@!\2")
        buf.write("\u0158\u0157\3\2\2\2\u0158\u0159\3\2\2\2\u0159;\3\2\2")
        buf.write("\2\u015a\u015f\5> \2\u015b\u015c\7\25\2\2\u015c\u015e")
        buf.write("\5> \2\u015d\u015b\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160=\3\2\2\2\u0161\u015f")
        buf.write("\3\2\2\2\u0162\u0163\7A\2\2\u0163\u0164\5@!\2\u0164?\3")
        buf.write("\2\2\2\u0165\u0166\7\23\2\2\u0166\u0167\7\f\2\2\u0167")
        buf.write("\u0169\7\24\2\2\u0168\u0165\3\2\2\2\u0169\u016c\3\2\2")
        buf.write("\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016d")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016e\t\t\2\2\u016e")
        buf.write("A\3\2\2\2\u016f\u0179\7\n\2\2\u0170\u0179\7\13\2\2\u0171")
        buf.write("\u0173\7\r\2\2\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0179\7\f\2\2\u0175\u0179\7")
        buf.write("\t\2\2\u0176\u0179\7\b\2\2\u0177\u0179\7A\2\2\u0178\u016f")
        buf.write("\3\2\2\2\u0178\u0170\3\2\2\2\u0178\u0172\3\2\2\2\u0178")
        buf.write("\u0175\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2")
        buf.write("\u0179C\3\2\2\2$GV[mrx\u0080\u0084\u0098\u009e\u00ab\u00bc")
        buf.write("\u00be\u00c8\u00d0\u00e2\u00eb\u00f2\u00f4\u00ff\u0102")
        buf.write("\u0110\u011a\u0128\u012c\u0139\u0144\u0148\u0154\u0158")
        buf.write("\u015f\u016a\u0172\u0178")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'", "<INVALID>", "<INVALID>", "'\n'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", 
                     "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
                     "'if'", "'else'", "'for'", "'struct'", "'interface'", 
                     "'string'", "'const'", "'var'", "'return'", "'func'", 
                     "'int'", "'type'", "'float'", "'boolean'", "'continue'", 
                     "'break'", "'range'", "'true'", "'false'", "'nil'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ML_COMMENT", "SL_COMMENT", 
                      "NL", "WS", "NIL_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                      "FLOAT_LITERAL", "INTERGER_LITERAL", "SIGN", "COLON", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "COMMA", "SEMI", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", 
                      "OR", "NOT", "ASSIGN", "COLON_ASSIGN", "ADD_ASSIGN", 
                      "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "IF", "ELSE", "FOR", "STRUCT", "INTERFACE", 
                      "STRING", "CONST", "VAR", "RETURN", "FUNC", "INT", 
                      "TYPE", "FLOAT", "BOOLEAN", "CONTINUE", "BREAK", "RANGE", 
                      "TRUE", "FALSE", "NIL", "IDENTIFIER", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment_stmt = 2
    RULE_ass_op = 3
    RULE_if_stmt = 4
    RULE_for_stmt = 5
    RULE_basic = 6
    RULE_with_init_con_upd = 7
    RULE_range_stmt = 8
    RULE_break_stmt = 9
    RULE_continue_stmt = 10
    RULE_return_stmt = 11
    RULE_call_stmt = 12
    RULE_expression = 13
    RULE_operands = 14
    RULE_array_access = 15
    RULE_struct_access = 16
    RULE_func_call = 17
    RULE_array_lit = 18
    RULE_struct_lit = 19
    RULE_fieldInit = 20
    RULE_func_decl = 21
    RULE_block = 22
    RULE_const_decl = 23
    RULE_vardecl = 24
    RULE_type_decl = 25
    RULE_field_decl = 26
    RULE_method_spec = 27
    RULE_signature = 28
    RULE_parameterList = 29
    RULE_parameter = 30
    RULE_type_ = 31
    RULE_primitive_type = 32

    ruleNames =  [ "program", "statement", "assignment_stmt", "ass_op", 
                   "if_stmt", "for_stmt", "basic", "with_init_con_upd", 
                   "range_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "call_stmt", "expression", "operands", "array_access", 
                   "struct_access", "func_call", "array_lit", "struct_lit", 
                   "fieldInit", "func_decl", "block", "const_decl", "vardecl", 
                   "type_decl", "field_decl", "method_spec", "signature", 
                   "parameterList", "parameter", "type_", "primitive_type" ]

    EOF = Token.EOF
    T__0=1
    ML_COMMENT=2
    SL_COMMENT=3
    NL=4
    WS=5
    NIL_LITERAL=6
    BOOLEAN_LITERAL=7
    STRING_LITERAL=8
    FLOAT_LITERAL=9
    INTERGER_LITERAL=10
    SIGN=11
    COLON=12
    LPAREN=13
    RPAREN=14
    LBRACE=15
    RBRACE=16
    LBRACK=17
    RBRACK=18
    COMMA=19
    SEMI=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQ=26
    NEQ=27
    LT=28
    LE=29
    GT=30
    GE=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    COLON_ASSIGN=36
    ADD_ASSIGN=37
    SUB_ASSIGN=38
    MUL_ASSIGN=39
    DIV_ASSIGN=40
    MOD_ASSIGN=41
    DOT=42
    IF=43
    ELSE=44
    FOR=45
    STRUCT=46
    INTERFACE=47
    STRING=48
    CONST=49
    VAR=50
    RETURN=51
    FUNC=52
    INT=53
    TYPE=54
    FLOAT=55
    BOOLEAN=56
    CONTINUE=57
    BREAK=58
    RANGE=59
    TRUE=60
    FALSE=61
    NIL=62
    IDENTIFIER=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


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
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.statement()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.INTERGER_LITERAL) | (1 << MiniGoParser.SIGN) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 71
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def range_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Range_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.assignment_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.if_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.for_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 79
                self.range_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 80
                self.break_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 81
                self.continue_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 82
                self.return_stmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 83
                self.call_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ass_op(self):
            return self.getTypedRuleContext(MiniGoParser.Ass_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = MiniGoParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 86
                self.primitive_type()
                pass

            elif la_ == 2:
                self.state = 87
                self.array_access()
                pass

            elif la_ == 3:
                self.state = 88
                self.struct_access()
                pass


            self.state = 91
            self.ass_op()
            self.state = 92
            self.expression(0)
            self.state = 93
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ass_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def COLON_ASSIGN(self):
            return self.getToken(MiniGoParser.COLON_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ass_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss_op" ):
                return visitor.visitAss_op(self)
            else:
                return visitor.visitChildren(self)




    def ass_op(self):

        localctx = MiniGoParser.Ass_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ass_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.COLON_ASSIGN) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IF)
            else:
                return self.getToken(MiniGoParser.IF, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(MiniGoParser.IF)
            self.state = 98
            self.expression(0)
            self.state = 99
            self.block()
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 100
                    self.match(MiniGoParser.ELSE)
                    self.state = 101
                    self.match(MiniGoParser.IF)
                    self.state = 102
                    self.expression(0)
                    self.state = 103
                    self.block() 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 110
                self.match(MiniGoParser.ELSE)
                self.state = 111
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def basic(self):
            return self.getTypedRuleContext(MiniGoParser.BasicContext,0)


        def with_init_con_upd(self):
            return self.getTypedRuleContext(MiniGoParser.With_init_con_updContext,0)


        def range_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Range_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MiniGoParser.FOR)
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 115
                self.basic()
                pass

            elif la_ == 2:
                self.state = 116
                self.with_init_con_upd()
                pass

            elif la_ == 3:
                self.state = 117
                self.range_stmt()
                pass


            self.state = 120
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic" ):
                return visitor.visitBasic(self)
            else:
                return visitor.visitChildren(self)




    def basic(self):

        localctx = MiniGoParser.BasicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class With_init_con_updContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def assignment_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_stmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_stmtContext,i)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_with_init_con_upd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWith_init_con_upd" ):
                return visitor.visitWith_init_con_upd(self)
            else:
                return visitor.visitChildren(self)




    def with_init_con_upd(self):

        localctx = MiniGoParser.With_init_con_updContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_with_init_con_upd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.INTERGER_LITERAL, MiniGoParser.SIGN, MiniGoParser.IDENTIFIER]:
                self.state = 124
                self.assignment_stmt()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 125
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 128
            self.match(MiniGoParser.SEMI)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.INTERGER_LITERAL) | (1 << MiniGoParser.SIGN) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 129
                self.expression(0)


            self.state = 132
            self.match(MiniGoParser.SEMI)
            self.state = 133
            self.assignment_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def ass_op(self):
            return self.getTypedRuleContext(MiniGoParser.Ass_opContext,0)


        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_range_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_stmt" ):
                return visitor.visitRange_stmt(self)
            else:
                return visitor.visitChildren(self)




    def range_stmt(self):

        localctx = MiniGoParser.Range_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_range_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__0 or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 136
            self.match(MiniGoParser.COMMA)
            self.state = 137
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 138
            self.ass_op()
            self.state = 139
            self.match(MiniGoParser.RANGE)
            self.state = 140
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(MiniGoParser.BREAK)
            self.state = 143
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(MiniGoParser.CONTINUE)
            self.state = 146
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(MiniGoParser.RETURN)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.INTERGER_LITERAL) | (1 << MiniGoParser.SIGN) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 149
                self.expression(0)


            self.state = 152
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 154
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 155
                self.match(MiniGoParser.DOT)


            self.state = 158
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 159
            self.signature()
            self.state = 160
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operands(self):
            return self.getTypedRuleContext(MiniGoParser.OperandsContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 163
                self.operands()
                pass

            elif la_ == 2:
                self.state = 164
                self.array_access()
                pass

            elif la_ == 3:
                self.state = 165
                self.struct_access()
                pass

            elif la_ == 4:
                self.state = 166
                self.func_call()
                pass

            elif la_ == 5:
                self.state = 167
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 168
                self.expression(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 186
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 171
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 172
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 173
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 174
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 175
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 176
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 177
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 178
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 179
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 180
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 181
                        self.match(MiniGoParser.AND)
                        self.state = 182
                        self.expression(3)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 183
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 184
                        self.match(MiniGoParser.OR)
                        self.state = 185
                        self.expression(2)
                        pass

             
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_litContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = MiniGoParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_operands)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.array_lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.struct_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.match(MiniGoParser.LPAREN)
                self.state = 195
                self.expression(0)
                self.state = 196
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACK)
            else:
                return self.getToken(MiniGoParser.LBRACK, i)

        def INTERGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INTERGER_LITERAL)
            else:
                return self.getToken(MiniGoParser.INTERGER_LITERAL, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACK)
            else:
                return self.getToken(MiniGoParser.RBRACK, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 204 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 201
                    self.match(MiniGoParser.LBRACK)
                    self.state = 202
                    self.match(MiniGoParser.INTERGER_LITERAL)
                    self.state = 203
                    self.match(MiniGoParser.RBRACK)

                else:
                    raise NoViableAltException(self)
                self.state = 206 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_access" ):
                return visitor.visitStruct_access(self)
            else:
                return visitor.visitChildren(self)




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 209
            self.match(MiniGoParser.DOT)
            self.state = 210
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 213
            self.match(MiniGoParser.DOT)
            self.state = 214
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 215
            self.signature()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACK)
            else:
                return self.getToken(MiniGoParser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACK)
            else:
                return self.getToken(MiniGoParser.RBRACK, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = MiniGoParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.type_()
            self.state = 218
            self.match(MiniGoParser.LBRACK)
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 219
                self.expression(0)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 220
                    self.match(MiniGoParser.COMMA)
                    self.state = 221
                    self.expression(0)
                    self.state = 226
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 238 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 227
                    self.match(MiniGoParser.LBRACK)

                    self.state = 228
                    self.expression(0)
                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==MiniGoParser.COMMA:
                        self.state = 229
                        self.match(MiniGoParser.COMMA)
                        self.state = 230
                        self.expression(0)
                        self.state = 235
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 236
                    self.match(MiniGoParser.RBRACK)
                    self.state = 240 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.LBRACK):
                        break

                pass


            self.state = 244
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def fieldInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FieldInitContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FieldInitContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_struct_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 247
            self.match(MiniGoParser.LBRACE)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 248
                self.fieldInit()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 249
                    self.match(MiniGoParser.COMMA)
                    self.state = 250
                    self.fieldInit()
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 258
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldInit" ):
                return visitor.visitFieldInit(self)
            else:
                return visitor.visitChildren(self)




    def fieldInit(self):

        localctx = MiniGoParser.FieldInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_fieldInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 261
            self.match(MiniGoParser.COLON)
            self.state = 262
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(MiniGoParser.FUNC)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPAREN:
                self.state = 265
                self.match(MiniGoParser.LPAREN)
                self.state = 266
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 267
                self.type_()
                self.state = 268
                self.match(MiniGoParser.RPAREN)


            self.state = 272
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 273
            self.signature()
            self.state = 274
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(MiniGoParser.LBRACE)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.INTERGER_LITERAL) | (1 << MiniGoParser.SIGN) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 277
                self.expression(0)
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 283
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(MiniGoParser.CONST)
            self.state = 286
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 287
            self.match(MiniGoParser.ASSIGN)
            self.state = 288
            self.expression(0)
            self.state = 289
            self.match(MiniGoParser.SEMI)
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(MiniGoParser.VAR)
            self.state = 292
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 293
                self.type_()


            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 296
                self.match(MiniGoParser.ASSIGN)
                self.state = 297
                self.expression(0)


            self.state = 300
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def field_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Field_declContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Field_declContext,i)


        def method_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Method_specContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Method_specContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl" ):
                return visitor.visitType_decl(self)
            else:
                return visitor.visitChildren(self)




    def type_decl(self):

        localctx = MiniGoParser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_type_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(MiniGoParser.TYPE)
            self.state = 303
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 304
                self.match(MiniGoParser.STRUCT)
                self.state = 305
                self.match(MiniGoParser.LBRACE)
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.IDENTIFIER:
                    self.state = 306
                    self.field_decl()
                    self.state = 307
                    self.match(MiniGoParser.SEMI)
                    self.state = 313
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 314
                self.match(MiniGoParser.RBRACE)
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 315
                self.match(MiniGoParser.INTERFACE)
                self.state = 316
                self.match(MiniGoParser.LBRACE)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.IDENTIFIER:
                    self.state = 317
                    self.method_spec()
                    self.state = 318
                    self.match(MiniGoParser.SEMI)
                    self.state = 324
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 325
                self.match(MiniGoParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 328
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_decl" ):
                return visitor.visitField_decl(self)
            else:
                return visitor.visitChildren(self)




    def field_decl(self):

        localctx = MiniGoParser.Field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 331
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_spec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_spec" ):
                return visitor.visitMethod_spec(self)
            else:
                return visitor.visitChildren(self)




    def method_spec(self):

        localctx = MiniGoParser.Method_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_method_spec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 334
            self.signature()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def parameterList(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterListContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_signature

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignature" ):
                return visitor.visitSignature(self)
            else:
                return visitor.visitChildren(self)




    def signature(self):

        localctx = MiniGoParser.SignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_signature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(MiniGoParser.LPAREN)
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 337
                self.parameterList()


            self.state = 340
            self.match(MiniGoParser.RPAREN)
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 341
                self.type_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParameterContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_parameterList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = MiniGoParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.parameter()
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 345
                self.match(MiniGoParser.COMMA)
                self.state = 346
                self.parameter()
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 353
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACK)
            else:
                return self.getToken(MiniGoParser.LBRACK, i)

        def INTERGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INTERGER_LITERAL)
            else:
                return self.getToken(MiniGoParser.INTERGER_LITERAL, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACK)
            else:
                return self.getToken(MiniGoParser.RBRACK, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniGoParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_type_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACK:
                self.state = 355
                self.match(MiniGoParser.LBRACK)
                self.state = 356
                self.match(MiniGoParser.INTERGER_LITERAL)
                self.state = 357
                self.match(MiniGoParser.RBRACK)
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 363
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
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

        def NIL_LITERAL(self):
            return self.getToken(MiniGoParser.NIL_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(MiniGoParser.STRING_LITERAL)
                pass
            elif token in [MiniGoParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass
            elif token in [MiniGoParser.INTERGER_LITERAL, MiniGoParser.SIGN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SIGN:
                    self.state = 367
                    self.match(MiniGoParser.SIGN)


                self.state = 370
                self.match(MiniGoParser.INTERGER_LITERAL)
                pass
            elif token in [MiniGoParser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 371
                self.match(MiniGoParser.BOOLEAN_LITERAL)
                pass
            elif token in [MiniGoParser.NIL_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 372
                self.match(MiniGoParser.NIL_LITERAL)
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 373
                self.match(MiniGoParser.IDENTIFIER)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




