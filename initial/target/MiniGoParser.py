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
        buf.write("\u01e7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\6\2n\n\2\r\2\16\2o\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\u0092\n\3\3\4\3\4\3\4\5\4\u0097\n\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\5\6\u00ad\n\6\3\7\3\7\3\7\3\7\5")
        buf.write("\7\u00b3\n\7\3\b\3\b\3\b\3\b\5\b\u00b9\n\b\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\5\n\u00c1\n\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\5\13\u00ca\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00de\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u00f2\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u00f9\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0104")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u0113\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\5\27\u011d\n\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0125\n\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u0138\n\32\3\33\3\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\5\34\u0141\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u0148")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u014f\n\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\5\37\u0156\n\37\3 \3 \3 \3 \3 \5 \u015d")
        buf.write("\n \3!\3!\3!\5!\u0162\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\5\"\u016e\n\"\3#\3#\3#\5#\u0173\n#\3#\3#\3")
        buf.write("#\3#\5#\u0179\n#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\5%\u0185")
        buf.write("\n%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\5(\u0190\n(\3)\3)\3")
        buf.write(")\3)\5)\u0196\n)\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write(",\3,\5,\u01a6\n,\3-\3-\3-\3-\3.\3.\3.\3.\3.\5.\u01b1\n")
        buf.write(".\3/\3/\3/\3/\3\60\3\60\5\60\u01b9\n\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\5\62")
        buf.write("\u01c8\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\5\63\u01d3\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\5\65\u01e2\n\65\3\66\3")
        buf.write("\66\3\66\3\66\2\2\67\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("j\2\t\3\2%*\4\2\5\5\25\25\3\2\33 \3\2\26\27\3\2\30\32")
        buf.write("\4\2\27\27##\6\2\61\61\66\6689?@\2\u01ec\2m\3\2\2\2\4")
        buf.write("\u0091\3\2\2\2\6\u0096\3\2\2\2\b\u009b\3\2\2\2\n\u00ac")
        buf.write("\3\2\2\2\f\u00b2\3\2\2\2\16\u00b4\3\2\2\2\20\u00bc\3\2")
        buf.write("\2\2\22\u00c0\3\2\2\2\24\u00c9\3\2\2\2\26\u00d1\3\2\2")
        buf.write("\2\30\u00d4\3\2\2\2\32\u00dd\3\2\2\2\34\u00df\3\2\2\2")
        buf.write("\36\u00e1\3\2\2\2 \u00e3\3\2\2\2\"\u00f1\3\2\2\2$\u00f8")
        buf.write("\3\2\2\2&\u0103\3\2\2\2(\u0105\3\2\2\2*\u0112\3\2\2\2")
        buf.write(",\u011c\3\2\2\2.\u0124\3\2\2\2\60\u0126\3\2\2\2\62\u0137")
        buf.write("\3\2\2\2\64\u0139\3\2\2\2\66\u0140\3\2\2\28\u0147\3\2")
        buf.write("\2\2:\u014e\3\2\2\2<\u0155\3\2\2\2>\u015c\3\2\2\2@\u0161")
        buf.write("\3\2\2\2B\u016d\3\2\2\2D\u0178\3\2\2\2F\u017a\3\2\2\2")
        buf.write("H\u0184\3\2\2\2J\u0186\3\2\2\2L\u0188\3\2\2\2N\u018f\3")
        buf.write("\2\2\2P\u0195\3\2\2\2R\u0197\3\2\2\2T\u019b\3\2\2\2V\u01a5")
        buf.write("\3\2\2\2X\u01a7\3\2\2\2Z\u01b0\3\2\2\2\\\u01b2\3\2\2\2")
        buf.write("^\u01b8\3\2\2\2`\u01ba\3\2\2\2b\u01c7\3\2\2\2d\u01d2\3")
        buf.write("\2\2\2f\u01d4\3\2\2\2h\u01e1\3\2\2\2j\u01e3\3\2\2\2ln")
        buf.write("\5\4\3\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2pq\3\2")
        buf.write("\2\2qr\7\2\2\3r\3\3\2\2\2st\5\62\32\2tu\5\36\20\2u\u0092")
        buf.write("\3\2\2\2vw\5\60\31\2wx\5\36\20\2x\u0092\3\2\2\2yz\5(\25")
        buf.write("\2z{\5\36\20\2{\u0092\3\2\2\2|}\5\6\4\2}~\5\36\20\2~\u0092")
        buf.write("\3\2\2\2\177\u0080\5\n\6\2\u0080\u0081\5\36\20\2\u0081")
        buf.write("\u0092\3\2\2\2\u0082\u0083\5\16\b\2\u0083\u0084\5\36\20")
        buf.write("\2\u0084\u0092\3\2\2\2\u0085\u0086\5\26\f\2\u0086\u0087")
        buf.write("\5\36\20\2\u0087\u0092\3\2\2\2\u0088\u0089\5\30\r\2\u0089")
        buf.write("\u008a\5\36\20\2\u008a\u0092\3\2\2\2\u008b\u008c\5\32")
        buf.write("\16\2\u008c\u008d\5\36\20\2\u008d\u0092\3\2\2\2\u008e")
        buf.write("\u008f\5\34\17\2\u008f\u0090\5\36\20\2\u0090\u0092\3\2")
        buf.write("\2\2\u0091s\3\2\2\2\u0091v\3\2\2\2\u0091y\3\2\2\2\u0091")
        buf.write("|\3\2\2\2\u0091\177\3\2\2\2\u0091\u0082\3\2\2\2\u0091")
        buf.write("\u0085\3\2\2\2\u0091\u0088\3\2\2\2\u0091\u008b\3\2\2\2")
        buf.write("\u0091\u008e\3\2\2\2\u0092\5\3\2\2\2\u0093\u0097\5D#\2")
        buf.write("\u0094\u0097\5L\'\2\u0095\u0097\5T+\2\u0096\u0093\3\2")
        buf.write("\2\2\u0096\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0099\5\b\5\2\u0099\u009a\5\64\33\2\u009a")
        buf.write("\7\3\2\2\2\u009b\u009c\t\2\2\2\u009c\t\3\2\2\2\u009d\u009e")
        buf.write("\7,\2\2\u009e\u009f\5\64\33\2\u009f\u00a0\5*\26\2\u00a0")
        buf.write("\u00ad\3\2\2\2\u00a1\u00a2\7,\2\2\u00a2\u00a3\5\64\33")
        buf.write("\2\u00a3\u00a4\5*\26\2\u00a4\u00a5\5\f\7\2\u00a5\u00ad")
        buf.write("\3\2\2\2\u00a6\u00a7\7,\2\2\u00a7\u00a8\5\64\33\2\u00a8")
        buf.write("\u00a9\7\20\2\2\u00a9\u00aa\5\n\6\2\u00aa\u00ab\7\21\2")
        buf.write("\2\u00ab\u00ad\3\2\2\2\u00ac\u009d\3\2\2\2\u00ac\u00a1")
        buf.write("\3\2\2\2\u00ac\u00a6\3\2\2\2\u00ad\13\3\2\2\2\u00ae\u00af")
        buf.write("\7-\2\2\u00af\u00b3\5*\26\2\u00b0\u00b1\7-\2\2\u00b1\u00b3")
        buf.write("\5\n\6\2\u00b2\u00ae\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3")
        buf.write("\r\3\2\2\2\u00b4\u00b8\7.\2\2\u00b5\u00b9\5\20\t\2\u00b6")
        buf.write("\u00b9\5\22\n\2\u00b7\u00b9\5\24\13\2\u00b8\u00b5\3\2")
        buf.write("\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bb\5*\26\2\u00bb\17\3\2\2\2\u00bc\u00bd")
        buf.write("\5\64\33\2\u00bd\21\3\2\2\2\u00be\u00c1\5\6\4\2\u00bf")
        buf.write("\u00c1\5\62\32\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2")
        buf.write("\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\7\25\2\2\u00c3\u00c4")
        buf.write("\5\64\33\2\u00c4\u00c5\7\25\2\2\u00c5\u00c6\5\6\4\2\u00c6")
        buf.write("\23\3\2\2\2\u00c7\u00ca\7@\2\2\u00c8\u00ca\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\u00cc\7\24\2\2\u00cc\u00cd\7@\2\2\u00cd\u00ce\7")
        buf.write("%\2\2\u00ce\u00cf\7<\2\2\u00cf\u00d0\5D#\2\u00d0\25\3")
        buf.write("\2\2\2\u00d1\u00d2\7;\2\2\u00d2\u00d3\7\25\2\2\u00d3\27")
        buf.write("\3\2\2\2\u00d4\u00d5\7:\2\2\u00d5\u00d6\7\25\2\2\u00d6")
        buf.write("\31\3\2\2\2\u00d7\u00d8\7\64\2\2\u00d8\u00d9\5\64\33\2")
        buf.write("\u00d9\u00da\7\25\2\2\u00da\u00de\3\2\2\2\u00db\u00dc")
        buf.write("\7\64\2\2\u00dc\u00de\7\25\2\2\u00dd\u00d7\3\2\2\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00de\33\3\2\2\2\u00df\u00e0\5V,\2\u00e0")
        buf.write("\35\3\2\2\2\u00e1\u00e2\t\3\2\2\u00e2\37\3\2\2\2\u00e3")
        buf.write("\u00e4\7\65\2\2\u00e4\u00e5\7\16\2\2\u00e5\u00e6\7@\2")
        buf.write("\2\u00e6\u00e7\5N(\2\u00e7\u00e8\7\17\2\2\u00e8\u00e9")
        buf.write("\7@\2\2\u00e9\u00ea\5&\24\2\u00ea\u00eb\5*\26\2\u00eb")
        buf.write("!\3\2\2\2\u00ec\u00ed\7@\2\2\u00ed\u00f2\5N(\2\u00ee\u00f2")
        buf.write("\7@\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00f2\5\64\33\2\u00f1")
        buf.write("\u00ec\3\2\2\2\u00f1\u00ee\3\2\2\2\u00f1\u00ef\3\2\2\2")
        buf.write("\u00f1\u00f0\3\2\2\2\u00f2#\3\2\2\2\u00f3\u00f4\5\"\22")
        buf.write("\2\u00f4\u00f5\7\24\2\2\u00f5\u00f6\5$\23\2\u00f6\u00f9")
        buf.write("\3\2\2\2\u00f7\u00f9\5\"\22\2\u00f8\u00f3\3\2\2\2\u00f8")
        buf.write("\u00f7\3\2\2\2\u00f9%\3\2\2\2\u00fa\u00fb\7\16\2\2\u00fb")
        buf.write("\u00fc\5$\23\2\u00fc\u00fd\7\17\2\2\u00fd\u0104\3\2\2")
        buf.write("\2\u00fe\u00ff\7\16\2\2\u00ff\u0100\5$\23\2\u0100\u0101")
        buf.write("\7\17\2\2\u0101\u0102\5N(\2\u0102\u0104\3\2\2\2\u0103")
        buf.write("\u00fa\3\2\2\2\u0103\u00fe\3\2\2\2\u0104\'\3\2\2\2\u0105")
        buf.write("\u0106\7\65\2\2\u0106\u0107\7@\2\2\u0107\u0108\5&\24\2")
        buf.write("\u0108\u0109\5*\26\2\u0109)\3\2\2\2\u010a\u010b\7\20\2")
        buf.write("\2\u010b\u010c\5,\27\2\u010c\u010d\7\21\2\2\u010d\u0113")
        buf.write("\3\2\2\2\u010e\u010f\7\20\2\2\u010f\u0110\5.\30\2\u0110")
        buf.write("\u0111\7\21\2\2\u0111\u0113\3\2\2\2\u0112\u010a\3\2\2")
        buf.write("\2\u0112\u010e\3\2\2\2\u0113+\3\2\2\2\u0114\u0115\5\64")
        buf.write("\33\2\u0115\u0116\5\36\20\2\u0116\u0117\5,\27\2\u0117")
        buf.write("\u011d\3\2\2\2\u0118\u0119\5\64\33\2\u0119\u011a\5\36")
        buf.write("\20\2\u011a\u011d\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u0114")
        buf.write("\3\2\2\2\u011c\u0118\3\2\2\2\u011c\u011b\3\2\2\2\u011d")
        buf.write("-\3\2\2\2\u011e\u011f\5\4\3\2\u011f\u0120\5\36\20\2\u0120")
        buf.write("\u0121\5.\30\2\u0121\u0125\3\2\2\2\u0122\u0125\5\4\3\2")
        buf.write("\u0123\u0125\3\2\2\2\u0124\u011e\3\2\2\2\u0124\u0122\3")
        buf.write("\2\2\2\u0124\u0123\3\2\2\2\u0125/\3\2\2\2\u0126\u0127")
        buf.write("\7\62\2\2\u0127\u0128\7@\2\2\u0128\u0129\7$\2\2\u0129")
        buf.write("\u012a\5\64\33\2\u012a\u012b\5\36\20\2\u012b\61\3\2\2")
        buf.write("\2\u012c\u012d\7\63\2\2\u012d\u0138\7@\2\2\u012e\u012f")
        buf.write("\7\63\2\2\u012f\u0130\7@\2\2\u0130\u0138\5N(\2\u0131\u0132")
        buf.write("\7\63\2\2\u0132\u0133\7@\2\2\u0133\u0134\5N(\2\u0134\u0135")
        buf.write("\7$\2\2\u0135\u0136\5\64\33\2\u0136\u0138\3\2\2\2\u0137")
        buf.write("\u012c\3\2\2\2\u0137\u012e\3\2\2\2\u0137\u0131\3\2\2\2")
        buf.write("\u0138\63\3\2\2\2\u0139\u013a\5\66\34\2\u013a\65\3\2\2")
        buf.write("\2\u013b\u013c\58\35\2\u013c\u013d\7\"\2\2\u013d\u013e")
        buf.write("\5\64\33\2\u013e\u0141\3\2\2\2\u013f\u0141\58\35\2\u0140")
        buf.write("\u013b\3\2\2\2\u0140\u013f\3\2\2\2\u0141\67\3\2\2\2\u0142")
        buf.write("\u0143\5:\36\2\u0143\u0144\7!\2\2\u0144\u0145\5\64\33")
        buf.write("\2\u0145\u0148\3\2\2\2\u0146\u0148\5:\36\2\u0147\u0142")
        buf.write("\3\2\2\2\u0147\u0146\3\2\2\2\u01489\3\2\2\2\u0149\u014a")
        buf.write("\5<\37\2\u014a\u014b\t\4\2\2\u014b\u014c\5\64\33\2\u014c")
        buf.write("\u014f\3\2\2\2\u014d\u014f\5<\37\2\u014e\u0149\3\2\2\2")
        buf.write("\u014e\u014d\3\2\2\2\u014f;\3\2\2\2\u0150\u0151\5> \2")
        buf.write("\u0151\u0152\t\5\2\2\u0152\u0153\5\64\33\2\u0153\u0156")
        buf.write("\3\2\2\2\u0154\u0156\5> \2\u0155\u0150\3\2\2\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156=\3\2\2\2\u0157\u0158\5@!\2\u0158\u0159")
        buf.write("\t\6\2\2\u0159\u015a\5\64\33\2\u015a\u015d\3\2\2\2\u015b")
        buf.write("\u015d\5@!\2\u015c\u0157\3\2\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("?\3\2\2\2\u015e\u015f\t\7\2\2\u015f\u0162\5B\"\2\u0160")
        buf.write("\u0162\5B\"\2\u0161\u015e\3\2\2\2\u0161\u0160\3\2\2\2")
        buf.write("\u0162A\3\2\2\2\u0163\u016e\5D#\2\u0164\u016e\5L\'\2\u0165")
        buf.write("\u016e\5T+\2\u0166\u016e\5F$\2\u0167\u016e\5X-\2\u0168")
        buf.write("\u0169\7\16\2\2\u0169\u016a\5\64\33\2\u016a\u016b\7\17")
        buf.write("\2\2\u016b\u016e\3\2\2\2\u016c\u016e\5V,\2\u016d\u0163")
        buf.write("\3\2\2\2\u016d\u0164\3\2\2\2\u016d\u0165\3\2\2\2\u016d")
        buf.write("\u0166\3\2\2\2\u016d\u0167\3\2\2\2\u016d\u0168\3\2\2\2")
        buf.write("\u016d\u016c\3\2\2\2\u016eC\3\2\2\2\u016f\u0179\7\t\2")
        buf.write("\2\u0170\u0179\7\n\2\2\u0171\u0173\7\f\2\2\u0172\u0171")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0179\7\13\2\2\u0175\u0179\7\b\2\2\u0176\u0179\7\7\2")
        buf.write("\2\u0177\u0179\7@\2\2\u0178\u016f\3\2\2\2\u0178\u0170")
        buf.write("\3\2\2\2\u0178\u0172\3\2\2\2\u0178\u0175\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179E\3\2\2\2\u017a")
        buf.write("\u017b\5N(\2\u017b\u017c\7\20\2\2\u017c\u017d\5H%\2\u017d")
        buf.write("\u017e\7\21\2\2\u017eG\3\2\2\2\u017f\u0180\5J&\2\u0180")
        buf.write("\u0181\7\24\2\2\u0181\u0182\5H%\2\u0182\u0185\3\2\2\2")
        buf.write("\u0183\u0185\5J&\2\u0184\u017f\3\2\2\2\u0184\u0183\3\2")
        buf.write("\2\2\u0185I\3\2\2\2\u0186\u0187\5D#\2\u0187K\3\2\2\2\u0188")
        buf.write("\u0189\7@\2\2\u0189\u018a\5P)\2\u018aM\3\2\2\2\u018b\u0190")
        buf.write("\t\b\2\2\u018c\u018d\5R*\2\u018d\u018e\t\b\2\2\u018e\u0190")
        buf.write("\3\2\2\2\u018f\u018b\3\2\2\2\u018f\u018c\3\2\2\2\u0190")
        buf.write("O\3\2\2\2\u0191\u0192\5R*\2\u0192\u0193\5P)\2\u0193\u0196")
        buf.write("\3\2\2\2\u0194\u0196\5R*\2\u0195\u0191\3\2\2\2\u0195\u0194")
        buf.write("\3\2\2\2\u0196Q\3\2\2\2\u0197\u0198\7\22\2\2\u0198\u0199")
        buf.write("\7\13\2\2\u0199\u019a\7\23\2\2\u019aS\3\2\2\2\u019b\u019c")
        buf.write("\5N(\2\u019c\u019d\7+\2\2\u019d\u019e\7@\2\2\u019eU\3")
        buf.write("\2\2\2\u019f\u01a0\7@\2\2\u01a0\u01a6\5&\24\2\u01a1\u01a2")
        buf.write("\7@\2\2\u01a2\u01a3\7+\2\2\u01a3\u01a4\7@\2\2\u01a4\u01a6")
        buf.write("\5&\24\2\u01a5\u019f\3\2\2\2\u01a5\u01a1\3\2\2\2\u01a6")
        buf.write("W\3\2\2\2\u01a7\u01a8\7@\2\2\u01a8\u01a9\7\20\2\2\u01a9")
        buf.write("\u01aa\7\21\2\2\u01aaY\3\2\2\2\u01ab\u01ac\5\\/\2\u01ac")
        buf.write("\u01ad\7\24\2\2\u01ad\u01ae\5Z.\2\u01ae\u01b1\3\2\2\2")
        buf.write("\u01af\u01b1\5\\/\2\u01b0\u01ab\3\2\2\2\u01b0\u01af\3")
        buf.write("\2\2\2\u01b1[\3\2\2\2\u01b2\u01b3\7@\2\2\u01b3\u01b4\7")
        buf.write("\r\2\2\u01b4\u01b5\5\64\33\2\u01b5]\3\2\2\2\u01b6\u01b9")
        buf.write("\5`\61\2\u01b7\u01b9\5f\64\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b7\3\2\2\2\u01b9_\3\2\2\2\u01ba\u01bb\7\67\2\2\u01bb")
        buf.write("\u01bc\7@\2\2\u01bc\u01bd\7\60\2\2\u01bd\u01be\7\20\2")
        buf.write("\2\u01be\u01bf\5b\62\2\u01bf\u01c0\7\21\2\2\u01c0\u01c1")
        buf.write("\5\36\20\2\u01c1a\3\2\2\2\u01c2\u01c3\5d\63\2\u01c3\u01c4")
        buf.write("\5\36\20\2\u01c4\u01c5\5b\62\2\u01c5\u01c8\3\2\2\2\u01c6")
        buf.write("\u01c8\5d\63\2\u01c7\u01c2\3\2\2\2\u01c7\u01c6\3\2\2\2")
        buf.write("\u01c8c\3\2\2\2\u01c9\u01ca\7@\2\2\u01ca\u01cb\5&\24\2")
        buf.write("\u01cb\u01cc\5N(\2\u01cc\u01cd\5\36\20\2\u01cd\u01d3\3")
        buf.write("\2\2\2\u01ce\u01cf\7@\2\2\u01cf\u01d0\5&\24\2\u01d0\u01d1")
        buf.write("\5\36\20\2\u01d1\u01d3\3\2\2\2\u01d2\u01c9\3\2\2\2\u01d2")
        buf.write("\u01ce\3\2\2\2\u01d3e\3\2\2\2\u01d4\u01d5\7\67\2\2\u01d5")
        buf.write("\u01d6\7@\2\2\u01d6\u01d7\7/\2\2\u01d7\u01d8\7\21\2\2")
        buf.write("\u01d8\u01d9\5j\66\2\u01d9\u01da\7\20\2\2\u01da\u01db")
        buf.write("\5\36\20\2\u01dbg\3\2\2\2\u01dc\u01dd\5j\66\2\u01dd\u01de")
        buf.write("\5\36\20\2\u01de\u01df\5h\65\2\u01df\u01e2\3\2\2\2\u01e0")
        buf.write("\u01e2\5j\66\2\u01e1\u01dc\3\2\2\2\u01e1\u01e0\3\2\2\2")
        buf.write("\u01e2i\3\2\2\2\u01e3\u01e4\7@\2\2\u01e4\u01e5\5N(\2\u01e5")
        buf.write("k\3\2\2\2$o\u0091\u0096\u00ac\u00b2\u00b8\u00c0\u00c9")
        buf.write("\u00dd\u00f1\u00f8\u0103\u0112\u011c\u0124\u0137\u0140")
        buf.write("\u0147\u014e\u0155\u015c\u0161\u016d\u0172\u0178\u0184")
        buf.write("\u018f\u0195\u01a5\u01b0\u01b8\u01c7\u01d2\u01e1")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'\n'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "','", "';'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'&&'", "'||'", "'!'", "'='", "':='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'.'", "'if'", "'else'", 
                     "'for'", "'struct'", "'interface'", "'string'", "'const'", 
                     "'var'", "'return'", "'func'", "'int'", "'type'", "'float'", 
                     "'boolean'", "'continue'", "'break'", "'range'", "'true'", 
                     "'false'", "'nil'" ]

    symbolicNames = [ "<INVALID>", "ML_COMMENT", "SL_COMMENT", "NL", "WS", 
                      "NIL_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
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
    RULE_else_stmt = 5
    RULE_for_stmt = 6
    RULE_basic_for = 7
    RULE_with_init_con_upd = 8
    RULE_range_for = 9
    RULE_break_stmt = 10
    RULE_continue_stmt = 11
    RULE_return_stmt = 12
    RULE_call_stmt = 13
    RULE_end_stmt = 14
    RULE_menthod_decl = 15
    RULE_parameter = 16
    RULE_parameterlist = 17
    RULE_signature = 18
    RULE_func_decl = 19
    RULE_block = 20
    RULE_list_expression = 21
    RULE_list_statement = 22
    RULE_const_decl_stmt = 23
    RULE_var_decl_stmt = 24
    RULE_expression = 25
    RULE_term_1 = 26
    RULE_term_2 = 27
    RULE_term_3 = 28
    RULE_term_4 = 29
    RULE_term_5 = 30
    RULE_term_6 = 31
    RULE_term_7 = 32
    RULE_primitive_type = 33
    RULE_array_lit = 34
    RULE_list_array_elements = 35
    RULE_array_element = 36
    RULE_array_access = 37
    RULE_type_ = 38
    RULE_list_dimention = 39
    RULE_dimention = 40
    RULE_struct_access = 41
    RULE_func_call = 42
    RULE_struct_lit = 43
    RULE_list_struct_elements = 44
    RULE_struct_elements = 45
    RULE_type_decl = 46
    RULE_interface_decl = 47
    RULE_list_menthod = 48
    RULE_menthod = 49
    RULE_struck_decl = 50
    RULE_list_field_decl = 51
    RULE_field_decl = 52

    ruleNames =  [ "program", "statement", "assignment_stmt", "ass_op", 
                   "if_stmt", "else_stmt", "for_stmt", "basic_for", "with_init_con_upd", 
                   "range_for", "break_stmt", "continue_stmt", "return_stmt", 
                   "call_stmt", "end_stmt", "menthod_decl", "parameter", 
                   "parameterlist", "signature", "func_decl", "block", "list_expression", 
                   "list_statement", "const_decl_stmt", "var_decl_stmt", 
                   "expression", "term_1", "term_2", "term_3", "term_4", 
                   "term_5", "term_6", "term_7", "primitive_type", "array_lit", 
                   "list_array_elements", "array_element", "array_access", 
                   "type_", "list_dimention", "dimention", "struct_access", 
                   "func_call", "struct_lit", "list_struct_elements", "struct_elements", 
                   "type_decl", "interface_decl", "list_menthod", "menthod", 
                   "struck_decl", "list_field_decl", "field_decl" ]

    EOF = Token.EOF
    ML_COMMENT=1
    SL_COMMENT=2
    NL=3
    WS=4
    NIL_LITERAL=5
    BOOLEAN_LITERAL=6
    STRING_LITERAL=7
    FLOAT_LITERAL=8
    INTERGER_LITERAL=9
    SIGN=10
    COLON=11
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
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.statement()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.INTERGER_LITERAL) | (1 << MiniGoParser.SIGN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 111
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

        def var_decl_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_stmtContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def const_decl_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Const_decl_stmtContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.var_decl_stmt()
                self.state = 114
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.const_decl_stmt()
                self.state = 117
                self.end_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.func_decl()
                self.state = 120
                self.end_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 122
                self.assignment_stmt()
                self.state = 123
                self.end_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 125
                self.if_stmt()
                self.state = 126
                self.end_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 128
                self.for_stmt()
                self.state = 129
                self.end_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 131
                self.break_stmt()
                self.state = 132
                self.end_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 134
                self.continue_stmt()
                self.state = 135
                self.end_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 137
                self.return_stmt()
                self.state = 138
                self.end_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 140
                self.call_stmt()
                self.state = 141
                self.end_stmt()
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
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 145
                self.primitive_type()
                pass

            elif la_ == 2:
                self.state = 146
                self.array_access()
                pass

            elif la_ == 3:
                self.state = 147
                self.struct_access()
                pass


            self.state = 150
            self.ass_op()
            self.state = 151
            self.expression()
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
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.COLON_ASSIGN) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmtContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(MiniGoParser.IF)
                self.state = 156
                self.expression()
                self.state = 157
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(MiniGoParser.IF)
                self.state = 160
                self.expression()
                self.state = 161
                self.block()
                self.state = 162
                self.else_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(MiniGoParser.IF)
                self.state = 165
                self.expression()
                self.state = 166
                self.match(MiniGoParser.LBRACE)
                self.state = 167
                self.if_stmt()
                self.state = 168
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = MiniGoParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_else_stmt)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(MiniGoParser.ELSE)
                self.state = 173
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(MiniGoParser.ELSE)
                self.state = 175
                self.if_stmt()
                pass


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


        def basic_for(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_forContext,0)


        def with_init_con_upd(self):
            return self.getTypedRuleContext(MiniGoParser.With_init_con_updContext,0)


        def range_for(self):
            return self.getTypedRuleContext(MiniGoParser.Range_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MiniGoParser.FOR)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 179
                self.basic_for()
                pass

            elif la_ == 2:
                self.state = 180
                self.with_init_con_upd()
                pass

            elif la_ == 3:
                self.state = 181
                self.range_for()
                pass


            self.state = 184
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for" ):
                return visitor.visitBasic_for(self)
            else:
                return visitor.visitChildren(self)




    def basic_for(self):

        localctx = MiniGoParser.Basic_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_basic_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.expression()
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

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def assignment_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_stmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_stmtContext,i)


        def var_decl_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_with_init_con_upd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWith_init_con_upd" ):
                return visitor.visitWith_init_con_upd(self)
            else:
                return visitor.visitChildren(self)




    def with_init_con_upd(self):

        localctx = MiniGoParser.With_init_con_updContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_with_init_con_upd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.INTERGER_LITERAL, MiniGoParser.SIGN, MiniGoParser.LBRACK, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL, MiniGoParser.IDENTIFIER]:
                self.state = 188
                self.assignment_stmt()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 189
                self.var_decl_stmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 192
            self.match(MiniGoParser.SEMI)
            self.state = 193
            self.expression()
            self.state = 194
            self.match(MiniGoParser.SEMI)
            self.state = 195
            self.assignment_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_forContext(ParserRuleContext):
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

        def COLON_ASSIGN(self):
            return self.getToken(MiniGoParser.COLON_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_for" ):
                return visitor.visitRange_for(self)
            else:
                return visitor.visitChildren(self)




    def range_for(self):

        localctx = MiniGoParser.Range_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_range_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.state = 197
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.COMMA]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 201
            self.match(MiniGoParser.COMMA)
            self.state = 202
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 203
            self.match(MiniGoParser.COLON_ASSIGN)
            self.state = 204
            self.match(MiniGoParser.RANGE)
            self.state = 205
            self.primitive_type()
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
        self.enterRule(localctx, 20, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(MiniGoParser.BREAK)
            self.state = 208
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
        self.enterRule(localctx, 22, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(MiniGoParser.CONTINUE)
            self.state = 211
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

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_return_stmt)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(MiniGoParser.RETURN)
                self.state = 214
                self.expression()
                self.state = 215
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(MiniGoParser.RETURN)
                self.state = 218
                self.match(MiniGoParser.SEMI)
                pass


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

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.func_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_end_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_stmt" ):
                return visitor.visitEnd_stmt(self)
            else:
                return visitor.visitChildren(self)




    def end_stmt(self):

        localctx = MiniGoParser.End_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_end_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
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


    class Menthod_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_menthod_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenthod_decl" ):
                return visitor.visitMenthod_decl(self)
            else:
                return visitor.visitChildren(self)




    def menthod_decl(self):

        localctx = MiniGoParser.Menthod_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_menthod_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MiniGoParser.FUNC)
            self.state = 226
            self.match(MiniGoParser.LPAREN)
            self.state = 227
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 228
            self.type_()
            self.state = 229
            self.match(MiniGoParser.RPAREN)
            self.state = 230
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 231
            self.signature()
            self.state = 232
            self.block()
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


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameter)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 235
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameterlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlist" ):
                return visitor.visitParameterlist(self)
            else:
                return visitor.visitChildren(self)




    def parameterlist(self):

        localctx = MiniGoParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameterlist)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.parameter()
                self.state = 242
                self.match(MiniGoParser.COMMA)
                self.state = 243
                self.parameterlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.parameter()
                pass


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

        def parameterlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterlistContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

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
        self.enterRule(localctx, 36, self.RULE_signature)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(MiniGoParser.LPAREN)
                self.state = 249
                self.parameterlist()
                self.state = 250
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.match(MiniGoParser.LPAREN)
                self.state = 253
                self.parameterlist()
                self.state = 254
                self.match(MiniGoParser.RPAREN)
                self.state = 255
                self.type_()
                pass


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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MiniGoParser.FUNC)
            self.state = 260
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 261
            self.signature()
            self.state = 262
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

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_block)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(MiniGoParser.LBRACE)
                self.state = 265
                self.list_expression()
                self.state = 266
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(MiniGoParser.LBRACE)
                self.state = 269
                self.list_statement()
                self.state = 270
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_expression)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.expression()
                self.state = 275
                self.end_stmt()
                self.state = 276
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.expression()
                self.state = 279
                self.end_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_statement)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.statement()
                self.state = 285
                self.end_stmt()
                self.state = 286
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_decl_stmtContext(ParserRuleContext):
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


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl_stmt" ):
                return visitor.visitConst_decl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def const_decl_stmt(self):

        localctx = MiniGoParser.Const_decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_const_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(MiniGoParser.CONST)
            self.state = 293
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 294
            self.match(MiniGoParser.ASSIGN)
            self.state = 295
            self.expression()
            self.state = 296
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_stmt" ):
                return visitor.visitVar_decl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_stmt(self):

        localctx = MiniGoParser.Var_decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_var_decl_stmt)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(MiniGoParser.VAR)
                self.state = 299
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(MiniGoParser.VAR)
                self.state = 301
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 302
                self.type_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(MiniGoParser.VAR)
                self.state = 304
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 305
                self.type_()
                self.state = 306
                self.match(MiniGoParser.ASSIGN)
                self.state = 307
                self.expression()
                pass


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

        def term_1(self):
            return self.getTypedRuleContext(MiniGoParser.Term_1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniGoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.term_1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term_2(self):
            return self.getTypedRuleContext(MiniGoParser.Term_2Context,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_term_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_1" ):
                return visitor.visitTerm_1(self)
            else:
                return visitor.visitChildren(self)




    def term_1(self):

        localctx = MiniGoParser.Term_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_term_1)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.term_2()
                self.state = 314
                self.match(MiniGoParser.OR)
                self.state = 315
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.term_2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term_3(self):
            return self.getTypedRuleContext(MiniGoParser.Term_3Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_term_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_2" ):
                return visitor.visitTerm_2(self)
            else:
                return visitor.visitChildren(self)




    def term_2(self):

        localctx = MiniGoParser.Term_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_term_2)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.term_3()
                self.state = 321
                self.match(MiniGoParser.AND)
                self.state = 322
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.term_3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term_4(self):
            return self.getTypedRuleContext(MiniGoParser.Term_4Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


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

        def getRuleIndex(self):
            return MiniGoParser.RULE_term_3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_3" ):
                return visitor.visitTerm_3(self)
            else:
                return visitor.visitChildren(self)




    def term_3(self):

        localctx = MiniGoParser.Term_3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_term_3)
        self._la = 0 # Token type
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.term_4()
                self.state = 328
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 329
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.term_4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term_5(self):
            return self.getTypedRuleContext(MiniGoParser.Term_5Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term_4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_4" ):
                return visitor.visitTerm_4(self)
            else:
                return visitor.visitChildren(self)




    def term_4(self):

        localctx = MiniGoParser.Term_4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_term_4)
        self._la = 0 # Token type
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.term_5()
                self.state = 335
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 336
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.term_5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term_6(self):
            return self.getTypedRuleContext(MiniGoParser.Term_6Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term_5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_5" ):
                return visitor.visitTerm_5(self)
            else:
                return visitor.visitChildren(self)




    def term_5(self):

        localctx = MiniGoParser.Term_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_term_5)
        self._la = 0 # Token type
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.term_6()
                self.state = 342
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 343
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.term_6()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term_7(self):
            return self.getTypedRuleContext(MiniGoParser.Term_7Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term_6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_6" ):
                return visitor.visitTerm_6(self)
            else:
                return visitor.visitChildren(self)




    def term_6(self):

        localctx = MiniGoParser.Term_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_term_6)
        self._la = 0 # Token type
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 349
                self.term_7()
                pass
            elif token in [MiniGoParser.NIL_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.INTERGER_LITERAL, MiniGoParser.SIGN, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.term_7()
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


    class Term_7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


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

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_term_7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_7" ):
                return visitor.visitTerm_7(self)
            else:
                return visitor.visitChildren(self)




    def term_7(self):

        localctx = MiniGoParser.Term_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_term_7)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.struct_access()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 356
                self.array_lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 357
                self.struct_lit()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 358
                self.match(MiniGoParser.LPAREN)
                self.state = 359
                self.expression()
                self.state = 360
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 362
                self.func_call()
                pass


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
        self.enterRule(localctx, 66, self.RULE_primitive_type)
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


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_array_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = MiniGoParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.type_()
            self.state = 377
            self.match(MiniGoParser.LBRACE)
            self.state = 378
            self.list_array_elements()
            self.state = 379
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_array_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_elements" ):
                return visitor.visitList_array_elements(self)
            else:
                return visitor.visitChildren(self)




    def list_array_elements(self):

        localctx = MiniGoParser.List_array_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_list_array_elements)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.array_element()
                self.state = 382
                self.match(MiniGoParser.COMMA)
                self.state = 383
                self.list_array_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_array_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.primitive_type()
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

        def list_dimention(self):
            return self.getTypedRuleContext(MiniGoParser.List_dimentionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 391
            self.list_dimention()
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

        def dimention(self):
            return self.getTypedRuleContext(MiniGoParser.DimentionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniGoParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_type_)
        self._la = 0 # Token type
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.dimention()
                self.state = 395
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
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


    class List_dimentionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimention(self):
            return self.getTypedRuleContext(MiniGoParser.DimentionContext,0)


        def list_dimention(self):
            return self.getTypedRuleContext(MiniGoParser.List_dimentionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_dimention

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_dimention" ):
                return visitor.visitList_dimention(self)
            else:
                return visitor.visitChildren(self)




    def list_dimention(self):

        localctx = MiniGoParser.List_dimentionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_list_dimention)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.dimention()
                self.state = 400
                self.list_dimention()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.dimention()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimentionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def INTERGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTERGER_LITERAL, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimention

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimention" ):
                return visitor.visitDimention(self)
            else:
                return visitor.visitChildren(self)




    def dimention(self):

        localctx = MiniGoParser.DimentionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_dimention)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(MiniGoParser.LBRACK)
            self.state = 406
            self.match(MiniGoParser.INTERGER_LITERAL)
            self.state = 407
            self.match(MiniGoParser.RBRACK)
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

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_access" ):
                return visitor.visitStruct_access(self)
            else:
                return visitor.visitChildren(self)




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.type_()
            self.state = 410
            self.match(MiniGoParser.DOT)
            self.state = 411
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

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_func_call)
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 414
                self.signature()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 416
                self.match(MiniGoParser.DOT)
                self.state = 417
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 418
                self.signature()
                pass


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

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 422
            self.match(MiniGoParser.LBRACE)
            self.state = 423
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_struct_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementsContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_struct_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_struct_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_struct_elements" ):
                return visitor.visitList_struct_elements(self)
            else:
                return visitor.visitChildren(self)




    def list_struct_elements(self):

        localctx = MiniGoParser.List_struct_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_list_struct_elements)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.struct_elements()
                self.state = 426
                self.match(MiniGoParser.COMMA)
                self.state = 427
                self.list_struct_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.struct_elements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elementsContext(ParserRuleContext):
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
            return MiniGoParser.RULE_struct_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_elements" ):
                return visitor.visitStruct_elements(self)
            else:
                return visitor.visitChildren(self)




    def struct_elements(self):

        localctx = MiniGoParser.Struct_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_struct_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 433
            self.match(MiniGoParser.COLON)
            self.state = 434
            self.expression()
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

        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def struck_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struck_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl" ):
                return visitor.visitType_decl(self)
            else:
                return visitor.visitChildren(self)




    def type_decl(self):

        localctx = MiniGoParser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_type_decl)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.interface_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.struck_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
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

        def list_menthod(self):
            return self.getTypedRuleContext(MiniGoParser.List_menthodContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(MiniGoParser.TYPE)
            self.state = 441
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 442
            self.match(MiniGoParser.INTERFACE)
            self.state = 443
            self.match(MiniGoParser.LBRACE)
            self.state = 444
            self.list_menthod()
            self.state = 445
            self.match(MiniGoParser.RBRACE)
            self.state = 446
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_menthodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def menthod(self):
            return self.getTypedRuleContext(MiniGoParser.MenthodContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def list_menthod(self):
            return self.getTypedRuleContext(MiniGoParser.List_menthodContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_menthod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_menthod" ):
                return visitor.visitList_menthod(self)
            else:
                return visitor.visitChildren(self)




    def list_menthod(self):

        localctx = MiniGoParser.List_menthodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_list_menthod)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.menthod()
                self.state = 449
                self.end_stmt()
                self.state = 450
                self.list_menthod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.menthod()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MenthodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_menthod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenthod" ):
                return visitor.visitMenthod(self)
            else:
                return visitor.visitChildren(self)




    def menthod(self):

        localctx = MiniGoParser.MenthodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_menthod)
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 456
                self.signature()
                self.state = 457
                self.type_()
                self.state = 458
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 461
                self.signature()
                self.state = 462
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struck_declContext(ParserRuleContext):
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

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def field_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Field_declContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struck_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruck_decl" ):
                return visitor.visitStruck_decl(self)
            else:
                return visitor.visitChildren(self)




    def struck_decl(self):

        localctx = MiniGoParser.Struck_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_struck_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(MiniGoParser.TYPE)
            self.state = 467
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 468
            self.match(MiniGoParser.STRUCT)
            self.state = 469
            self.match(MiniGoParser.RBRACE)
            self.state = 470
            self.field_decl()
            self.state = 471
            self.match(MiniGoParser.LBRACE)
            self.state = 472
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Field_declContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def list_field_decl(self):
            return self.getTypedRuleContext(MiniGoParser.List_field_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_field_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_field_decl" ):
                return visitor.visitList_field_decl(self)
            else:
                return visitor.visitChildren(self)




    def list_field_decl(self):

        localctx = MiniGoParser.List_field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_list_field_decl)
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.field_decl()
                self.state = 475
                self.end_stmt()
                self.state = 476
                self.list_field_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.field_decl()
                pass


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
        self.enterRule(localctx, 104, self.RULE_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 482
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





