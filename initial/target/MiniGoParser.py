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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u01fd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0098\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00b5")
        buf.write("\n\6\3\7\3\7\3\7\3\7\5\7\u00bb\n\7\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u00c1\n\b\3\b\3\b\3\t\3\t\3\n\3\n\5\n\u00c9\n\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\5\13\u00d2\n\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\5\16\u00e1")
        buf.write("\n\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00f8\n\20\3\21\3\21\3\21\3\21\5\21\u00fe\n\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u0105\n\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u010d\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u011a\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u0123\n\26\3\26\3")
        buf.write("\26\7\26\u0127\n\26\f\26\16\26\u012a\13\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0140\n\30\3")
        buf.write("\31\3\31\3\31\5\31\u0145\n\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u014e\n\33\3\34\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u0155\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u015c\n\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\5\36\u0163\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u016a\n\37\3 \3 \3 \5 \u016f\n \3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\5!\u0179\n!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0183\n\"\3#\3#\3#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\5$\u0190\n$\3%\3%\5%\u0194\n%\3&\3&\3&\3&\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01a6\n(\3)\3)\3")
        buf.write(")\3)\5)\u01ac\n)\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write(",\3,\5,\u01bc\n,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\5.\u01c8")
        buf.write("\n.\3/\3/\3/\3/\3\60\3\60\5\60\u01d0\n\60\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\5\62")
        buf.write("\u01de\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\5\63\u01e9\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\5\65\u01f7\n\65\3\66\3\66\3")
        buf.write("\66\3\66\3\66\2\3*\67\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("j\2\b\3\2$)\3\2\32\37\3\2\25\26\3\2\27\31\4\2\26\26\"")
        buf.write("\"\6\2\60\60\65\65\678>?\2\u020b\2m\3\2\2\2\4\u0097\3")
        buf.write("\2\2\2\6\u0099\3\2\2\2\b\u009d\3\2\2\2\n\u00b4\3\2\2\2")
        buf.write("\f\u00ba\3\2\2\2\16\u00bc\3\2\2\2\20\u00c4\3\2\2\2\22")
        buf.write("\u00c8\3\2\2\2\24\u00d1\3\2\2\2\26\u00d9\3\2\2\2\30\u00db")
        buf.write("\3\2\2\2\32\u00e0\3\2\2\2\34\u00e2\3\2\2\2\36\u00f7\3")
        buf.write("\2\2\2 \u00fd\3\2\2\2\"\u0104\3\2\2\2$\u010c\3\2\2\2&")
        buf.write("\u0119\3\2\2\2(\u011b\3\2\2\2*\u0122\3\2\2\2,\u012b\3")
        buf.write("\2\2\2.\u013f\3\2\2\2\60\u0144\3\2\2\2\62\u0146\3\2\2")
        buf.write("\2\64\u014d\3\2\2\2\66\u0154\3\2\2\28\u015b\3\2\2\2:\u0162")
        buf.write("\3\2\2\2<\u0169\3\2\2\2>\u016e\3\2\2\2@\u0178\3\2\2\2")
        buf.write("B\u0182\3\2\2\2D\u0184\3\2\2\2F\u018f\3\2\2\2H\u0193\3")
        buf.write("\2\2\2J\u0195\3\2\2\2L\u0199\3\2\2\2N\u01a5\3\2\2\2P\u01ab")
        buf.write("\3\2\2\2R\u01ad\3\2\2\2T\u01b1\3\2\2\2V\u01bb\3\2\2\2")
        buf.write("X\u01bd\3\2\2\2Z\u01c7\3\2\2\2\\\u01c9\3\2\2\2^\u01cf")
        buf.write("\3\2\2\2`\u01d1\3\2\2\2b\u01dd\3\2\2\2d\u01e8\3\2\2\2")
        buf.write("f\u01ea\3\2\2\2h\u01f6\3\2\2\2j\u01f8\3\2\2\2ln\5\4\3")
        buf.write("\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2pq\3\2\2\2q")
        buf.write("r\7\2\2\3r\3\3\2\2\2st\5.\30\2tu\5\60\31\2u\u0098\3\2")
        buf.write("\2\2vw\5,\27\2wx\5\60\31\2x\u0098\3\2\2\2yz\5&\24\2z{")
        buf.write("\5\60\31\2{\u0098\3\2\2\2|}\5\36\20\2}~\5\60\31\2~\u0098")
        buf.write("\3\2\2\2\177\u0080\5\6\4\2\u0080\u0081\5\60\31\2\u0081")
        buf.write("\u0098\3\2\2\2\u0082\u0083\5\n\6\2\u0083\u0084\5\60\31")
        buf.write("\2\u0084\u0098\3\2\2\2\u0085\u0086\5\16\b\2\u0086\u0087")
        buf.write("\5\60\31\2\u0087\u0098\3\2\2\2\u0088\u0089\5\26\f\2\u0089")
        buf.write("\u008a\5\60\31\2\u008a\u0098\3\2\2\2\u008b\u008c\5\30")
        buf.write("\r\2\u008c\u008d\5\60\31\2\u008d\u0098\3\2\2\2\u008e\u008f")
        buf.write("\5\32\16\2\u008f\u0090\5\60\31\2\u0090\u0098\3\2\2\2\u0091")
        buf.write("\u0092\5\34\17\2\u0092\u0093\5\60\31\2\u0093\u0098\3\2")
        buf.write("\2\2\u0094\u0095\5^\60\2\u0095\u0096\5\60\31\2\u0096\u0098")
        buf.write("\3\2\2\2\u0097s\3\2\2\2\u0097v\3\2\2\2\u0097y\3\2\2\2")
        buf.write("\u0097|\3\2\2\2\u0097\177\3\2\2\2\u0097\u0082\3\2\2\2")
        buf.write("\u0097\u0085\3\2\2\2\u0097\u0088\3\2\2\2\u0097\u008b\3")
        buf.write("\2\2\2\u0097\u008e\3\2\2\2\u0097\u0091\3\2\2\2\u0097\u0094")
        buf.write("\3\2\2\2\u0098\5\3\2\2\2\u0099\u009a\5B\"\2\u009a\u009b")
        buf.write("\5\b\5\2\u009b\u009c\5\62\32\2\u009c\7\3\2\2\2\u009d\u009e")
        buf.write("\t\2\2\2\u009e\t\3\2\2\2\u009f\u00a0\7+\2\2\u00a0\u00a1")
        buf.write("\7\r\2\2\u00a1\u00a2\5\62\32\2\u00a2\u00a3\7\16\2\2\u00a3")
        buf.write("\u00a4\5(\25\2\u00a4\u00b5\3\2\2\2\u00a5\u00a6\7+\2\2")
        buf.write("\u00a6\u00a7\7\r\2\2\u00a7\u00a8\5\62\32\2\u00a8\u00a9")
        buf.write("\7\16\2\2\u00a9\u00aa\5(\25\2\u00aa\u00ab\5\f\7\2\u00ab")
        buf.write("\u00b5\3\2\2\2\u00ac\u00ad\7+\2\2\u00ad\u00ae\7\r\2\2")
        buf.write("\u00ae\u00af\5\62\32\2\u00af\u00b0\7\16\2\2\u00b0\u00b1")
        buf.write("\7\17\2\2\u00b1\u00b2\5\n\6\2\u00b2\u00b3\7\20\2\2\u00b3")
        buf.write("\u00b5\3\2\2\2\u00b4\u009f\3\2\2\2\u00b4\u00a5\3\2\2\2")
        buf.write("\u00b4\u00ac\3\2\2\2\u00b5\13\3\2\2\2\u00b6\u00b7\7,\2")
        buf.write("\2\u00b7\u00bb\5(\25\2\u00b8\u00b9\7,\2\2\u00b9\u00bb")
        buf.write("\5\n\6\2\u00ba\u00b6\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb")
        buf.write("\r\3\2\2\2\u00bc\u00c0\7-\2\2\u00bd\u00c1\5\20\t\2\u00be")
        buf.write("\u00c1\5\22\n\2\u00bf\u00c1\5\24\13\2\u00c0\u00bd\3\2")
        buf.write("\2\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00c3\5(\25\2\u00c3\17\3\2\2\2\u00c4\u00c5")
        buf.write("\5\62\32\2\u00c5\21\3\2\2\2\u00c6\u00c9\5\6\4\2\u00c7")
        buf.write("\u00c9\5.\30\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00ca\u00cb\7\24\2\2\u00cb\u00cc")
        buf.write("\5\62\32\2\u00cc\u00cd\7\24\2\2\u00cd\u00ce\5\6\4\2\u00ce")
        buf.write("\23\3\2\2\2\u00cf\u00d2\7?\2\2\u00d0\u00d2\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2")
        buf.write("\u00d3\u00d4\7\23\2\2\u00d4\u00d5\7?\2\2\u00d5\u00d6\7")
        buf.write("$\2\2\u00d6\u00d7\7;\2\2\u00d7\u00d8\5B\"\2\u00d8\25\3")
        buf.write("\2\2\2\u00d9\u00da\7:\2\2\u00da\27\3\2\2\2\u00db\u00dc")
        buf.write("\79\2\2\u00dc\31\3\2\2\2\u00dd\u00de\7\63\2\2\u00de\u00e1")
        buf.write("\5\62\32\2\u00df\u00e1\7\63\2\2\u00e0\u00dd\3\2\2\2\u00e0")
        buf.write("\u00df\3\2\2\2\u00e1\33\3\2\2\2\u00e2\u00e3\5V,\2\u00e3")
        buf.write("\35\3\2\2\2\u00e4\u00e5\7\64\2\2\u00e5\u00e6\7\r\2\2\u00e6")
        buf.write("\u00e7\7?\2\2\u00e7\u00e8\5N(\2\u00e8\u00e9\7\16\2\2\u00e9")
        buf.write("\u00ea\7?\2\2\u00ea\u00eb\5$\23\2\u00eb\u00ec\5(\25\2")
        buf.write("\u00ec\u00f8\3\2\2\2\u00ed\u00ee\7\64\2\2\u00ee\u00ef")
        buf.write("\7\r\2\2\u00ef\u00f0\7?\2\2\u00f0\u00f1\5N(\2\u00f1\u00f2")
        buf.write("\7\16\2\2\u00f2\u00f3\7?\2\2\u00f3\u00f4\5$\23\2\u00f4")
        buf.write("\u00f5\5N(\2\u00f5\u00f6\5(\25\2\u00f6\u00f8\3\2\2\2\u00f7")
        buf.write("\u00e4\3\2\2\2\u00f7\u00ed\3\2\2\2\u00f8\37\3\2\2\2\u00f9")
        buf.write("\u00fa\7?\2\2\u00fa\u00fe\5N(\2\u00fb\u00fe\7?\2\2\u00fc")
        buf.write("\u00fe\5\62\32\2\u00fd\u00f9\3\2\2\2\u00fd\u00fb\3\2\2")
        buf.write("\2\u00fd\u00fc\3\2\2\2\u00fe!\3\2\2\2\u00ff\u0100\5 \21")
        buf.write("\2\u0100\u0101\7\23\2\2\u0101\u0102\5\"\22\2\u0102\u0105")
        buf.write("\3\2\2\2\u0103\u0105\5 \21\2\u0104\u00ff\3\2\2\2\u0104")
        buf.write("\u0103\3\2\2\2\u0105#\3\2\2\2\u0106\u0107\7\r\2\2\u0107")
        buf.write("\u0108\5\"\22\2\u0108\u0109\7\16\2\2\u0109\u010d\3\2\2")
        buf.write("\2\u010a\u010b\7\r\2\2\u010b\u010d\7\16\2\2\u010c\u0106")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010d%\3\2\2\2\u010e\u010f")
        buf.write("\7\64\2\2\u010f\u0110\7?\2\2\u0110\u0111\5$\23\2\u0111")
        buf.write("\u0112\5(\25\2\u0112\u011a\3\2\2\2\u0113\u0114\7\64\2")
        buf.write("\2\u0114\u0115\7?\2\2\u0115\u0116\5$\23\2\u0116\u0117")
        buf.write("\5N(\2\u0117\u0118\5(\25\2\u0118\u011a\3\2\2\2\u0119\u010e")
        buf.write("\3\2\2\2\u0119\u0113\3\2\2\2\u011a\'\3\2\2\2\u011b\u011c")
        buf.write("\7\17\2\2\u011c\u011d\5*\26\2\u011d\u011e\7\20\2\2\u011e")
        buf.write(")\3\2\2\2\u011f\u0120\b\26\1\2\u0120\u0123\5\4\3\2\u0121")
        buf.write("\u0123\3\2\2\2\u0122\u011f\3\2\2\2\u0122\u0121\3\2\2\2")
        buf.write("\u0123\u0128\3\2\2\2\u0124\u0125\f\5\2\2\u0125\u0127\5")
        buf.write("\4\3\2\u0126\u0124\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126")
        buf.write("\3\2\2\2\u0128\u0129\3\2\2\2\u0129+\3\2\2\2\u012a\u0128")
        buf.write("\3\2\2\2\u012b\u012c\7\61\2\2\u012c\u012d\7?\2\2\u012d")
        buf.write("\u012e\7#\2\2\u012e\u012f\5\62\32\2\u012f-\3\2\2\2\u0130")
        buf.write("\u0131\7\62\2\2\u0131\u0140\7?\2\2\u0132\u0133\7\62\2")
        buf.write("\2\u0133\u0134\7?\2\2\u0134\u0140\5N(\2\u0135\u0136\7")
        buf.write("\62\2\2\u0136\u0137\7?\2\2\u0137\u0138\5N(\2\u0138\u0139")
        buf.write("\7#\2\2\u0139\u013a\5\62\32\2\u013a\u0140\3\2\2\2\u013b")
        buf.write("\u013c\7\62\2\2\u013c\u013d\7?\2\2\u013d\u013e\7#\2\2")
        buf.write("\u013e\u0140\5\62\32\2\u013f\u0130\3\2\2\2\u013f\u0132")
        buf.write("\3\2\2\2\u013f\u0135\3\2\2\2\u013f\u013b\3\2\2\2\u0140")
        buf.write("/\3\2\2\2\u0141\u0145\7\24\2\2\u0142\u0145\7\6\2\2\u0143")
        buf.write("\u0145\3\2\2\2\u0144\u0141\3\2\2\2\u0144\u0142\3\2\2\2")
        buf.write("\u0144\u0143\3\2\2\2\u0145\61\3\2\2\2\u0146\u0147\5\64")
        buf.write("\33\2\u0147\63\3\2\2\2\u0148\u0149\5\66\34\2\u0149\u014a")
        buf.write("\7!\2\2\u014a\u014b\5\62\32\2\u014b\u014e\3\2\2\2\u014c")
        buf.write("\u014e\5\66\34\2\u014d\u0148\3\2\2\2\u014d\u014c\3\2\2")
        buf.write("\2\u014e\65\3\2\2\2\u014f\u0150\58\35\2\u0150\u0151\7")
        buf.write(" \2\2\u0151\u0152\5\62\32\2\u0152\u0155\3\2\2\2\u0153")
        buf.write("\u0155\58\35\2\u0154\u014f\3\2\2\2\u0154\u0153\3\2\2\2")
        buf.write("\u0155\67\3\2\2\2\u0156\u0157\5:\36\2\u0157\u0158\t\3")
        buf.write("\2\2\u0158\u0159\5\62\32\2\u0159\u015c\3\2\2\2\u015a\u015c")
        buf.write("\5:\36\2\u015b\u0156\3\2\2\2\u015b\u015a\3\2\2\2\u015c")
        buf.write("9\3\2\2\2\u015d\u015e\5<\37\2\u015e\u015f\t\4\2\2\u015f")
        buf.write("\u0160\5\62\32\2\u0160\u0163\3\2\2\2\u0161\u0163\5<\37")
        buf.write("\2\u0162\u015d\3\2\2\2\u0162\u0161\3\2\2\2\u0163;\3\2")
        buf.write("\2\2\u0164\u0165\5> \2\u0165\u0166\t\5\2\2\u0166\u0167")
        buf.write("\5\62\32\2\u0167\u016a\3\2\2\2\u0168\u016a\5> \2\u0169")
        buf.write("\u0164\3\2\2\2\u0169\u0168\3\2\2\2\u016a=\3\2\2\2\u016b")
        buf.write("\u016c\t\6\2\2\u016c\u016f\5\62\32\2\u016d\u016f\5@!\2")
        buf.write("\u016e\u016b\3\2\2\2\u016e\u016d\3\2\2\2\u016f?\3\2\2")
        buf.write("\2\u0170\u0179\5B\"\2\u0171\u0179\5D#\2\u0172\u0179\5")
        buf.write("X-\2\u0173\u0174\7\r\2\2\u0174\u0175\5\62\32\2\u0175\u0176")
        buf.write("\7\16\2\2\u0176\u0179\3\2\2\2\u0177\u0179\5V,\2\u0178")
        buf.write("\u0170\3\2\2\2\u0178\u0171\3\2\2\2\u0178\u0172\3\2\2\2")
        buf.write("\u0178\u0173\3\2\2\2\u0178\u0177\3\2\2\2\u0179A\3\2\2")
        buf.write("\2\u017a\u0183\5T+\2\u017b\u0183\5L\'\2\u017c\u0183\7")
        buf.write("\t\2\2\u017d\u0183\7\n\2\2\u017e\u0183\7\13\2\2\u017f")
        buf.write("\u0183\7\b\2\2\u0180\u0183\7\7\2\2\u0181\u0183\7?\2\2")
        buf.write("\u0182\u017a\3\2\2\2\u0182\u017b\3\2\2\2\u0182\u017c\3")
        buf.write("\2\2\2\u0182\u017d\3\2\2\2\u0182\u017e\3\2\2\2\u0182\u017f")
        buf.write("\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183")
        buf.write("C\3\2\2\2\u0184\u0185\5N(\2\u0185\u0186\7\17\2\2\u0186")
        buf.write("\u0187\5F$\2\u0187\u0188\7\20\2\2\u0188E\3\2\2\2\u0189")
        buf.write("\u018a\5H%\2\u018a\u018b\7\23\2\2\u018b\u018c\5F$\2\u018c")
        buf.write("\u0190\3\2\2\2\u018d\u0190\5H%\2\u018e\u0190\3\2\2\2\u018f")
        buf.write("\u0189\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u018e\3\2\2\2")
        buf.write("\u0190G\3\2\2\2\u0191\u0194\5B\"\2\u0192\u0194\5J&\2\u0193")
        buf.write("\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194I\3\2\2\2\u0195")
        buf.write("\u0196\7\17\2\2\u0196\u0197\5F$\2\u0197\u0198\7\20\2\2")
        buf.write("\u0198K\3\2\2\2\u0199\u019a\7?\2\2\u019a\u019b\5P)\2\u019b")
        buf.write("M\3\2\2\2\u019c\u01a6\7\65\2\2\u019d\u01a6\7\67\2\2\u019e")
        buf.write("\u01a6\7\60\2\2\u019f\u01a6\78\2\2\u01a0\u01a6\7>\2\2")
        buf.write("\u01a1\u01a6\7?\2\2\u01a2\u01a3\5P)\2\u01a3\u01a4\t\7")
        buf.write("\2\2\u01a4\u01a6\3\2\2\2\u01a5\u019c\3\2\2\2\u01a5\u019d")
        buf.write("\3\2\2\2\u01a5\u019e\3\2\2\2\u01a5\u019f\3\2\2\2\u01a5")
        buf.write("\u01a0\3\2\2\2\u01a5\u01a1\3\2\2\2\u01a5\u01a2\3\2\2\2")
        buf.write("\u01a6O\3\2\2\2\u01a7\u01a8\5R*\2\u01a8\u01a9\5P)\2\u01a9")
        buf.write("\u01ac\3\2\2\2\u01aa\u01ac\5R*\2\u01ab\u01a7\3\2\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01acQ\3\2\2\2\u01ad\u01ae\7\21\2\2\u01ae")
        buf.write("\u01af\7\13\2\2\u01af\u01b0\7\22\2\2\u01b0S\3\2\2\2\u01b1")
        buf.write("\u01b2\5N(\2\u01b2\u01b3\7*\2\2\u01b3\u01b4\7?\2\2\u01b4")
        buf.write("U\3\2\2\2\u01b5\u01b6\7?\2\2\u01b6\u01bc\5$\23\2\u01b7")
        buf.write("\u01b8\7?\2\2\u01b8\u01b9\7*\2\2\u01b9\u01ba\7?\2\2\u01ba")
        buf.write("\u01bc\5$\23\2\u01bb\u01b5\3\2\2\2\u01bb\u01b7\3\2\2\2")
        buf.write("\u01bcW\3\2\2\2\u01bd\u01be\5N(\2\u01be\u01bf\7\17\2\2")
        buf.write("\u01bf\u01c0\5Z.\2\u01c0\u01c1\7\20\2\2\u01c1Y\3\2\2\2")
        buf.write("\u01c2\u01c3\5\\/\2\u01c3\u01c4\7\23\2\2\u01c4\u01c5\5")
        buf.write("Z.\2\u01c5\u01c8\3\2\2\2\u01c6\u01c8\5\\/\2\u01c7\u01c2")
        buf.write("\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8[\3\2\2\2\u01c9\u01ca")
        buf.write("\7?\2\2\u01ca\u01cb\7\f\2\2\u01cb\u01cc\5\62\32\2\u01cc")
        buf.write("]\3\2\2\2\u01cd\u01d0\5`\61\2\u01ce\u01d0\5f\64\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0_\3\2\2\2\u01d1")
        buf.write("\u01d2\7\66\2\2\u01d2\u01d3\7?\2\2\u01d3\u01d4\7/\2\2")
        buf.write("\u01d4\u01d5\7\17\2\2\u01d5\u01d6\5b\62\2\u01d6\u01d7")
        buf.write("\7\20\2\2\u01d7a\3\2\2\2\u01d8\u01d9\5d\63\2\u01d9\u01da")
        buf.write("\5b\62\2\u01da\u01de\3\2\2\2\u01db\u01de\5d\63\2\u01dc")
        buf.write("\u01de\3\2\2\2\u01dd\u01d8\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01dd\u01dc\3\2\2\2\u01dec\3\2\2\2\u01df\u01e0\7?\2\2")
        buf.write("\u01e0\u01e1\5$\23\2\u01e1\u01e2\5\60\31\2\u01e2\u01e9")
        buf.write("\3\2\2\2\u01e3\u01e4\7?\2\2\u01e4\u01e5\5$\23\2\u01e5")
        buf.write("\u01e6\5N(\2\u01e6\u01e7\5\60\31\2\u01e7\u01e9\3\2\2\2")
        buf.write("\u01e8\u01df\3\2\2\2\u01e8\u01e3\3\2\2\2\u01e9e\3\2\2")
        buf.write("\2\u01ea\u01eb\7\66\2\2\u01eb\u01ec\7?\2\2\u01ec\u01ed")
        buf.write("\7.\2\2\u01ed\u01ee\7\17\2\2\u01ee\u01ef\5h\65\2\u01ef")
        buf.write("\u01f0\7\20\2\2\u01f0g\3\2\2\2\u01f1\u01f2\5j\66\2\u01f2")
        buf.write("\u01f3\5h\65\2\u01f3\u01f7\3\2\2\2\u01f4\u01f7\5j\66\2")
        buf.write("\u01f5\u01f7\3\2\2\2\u01f6\u01f1\3\2\2\2\u01f6\u01f4\3")
        buf.write("\2\2\2\u01f6\u01f5\3\2\2\2\u01f7i\3\2\2\2\u01f8\u01f9")
        buf.write("\7?\2\2\u01f9\u01fa\5N(\2\u01fa\u01fb\5\60\31\2\u01fb")
        buf.write("k\3\2\2\2%o\u0097\u00b4\u00ba\u00c0\u00c8\u00d1\u00e0")
        buf.write("\u00f7\u00fd\u0104\u010c\u0119\u0122\u0128\u013f\u0144")
        buf.write("\u014d\u0154\u015b\u0162\u0169\u016e\u0178\u0182\u018f")
        buf.write("\u0193\u01a5\u01ab\u01bb\u01c7\u01cf\u01dd\u01e8\u01f6")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\n'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "':'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", 
                     "'||'", "'!'", "'='", "':='", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "'.'", "'if'", "'else'", "'for'", "'struct'", 
                     "'interface'", "'string'", "'const'", "'var'", "'return'", 
                     "'func'", "'int'", "'type'", "'float'", "'boolean'", 
                     "'continue'", "'break'", "'range'", "'true'", "'false'", 
                     "'nil'" ]

    symbolicNames = [ "<INVALID>", "ML_COMMENT", "SL_COMMENT", "WS", "NL", 
                      "NIL_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                      "FLOAT_LITERAL", "INTERGER_LITERAL", "COLON", "LPAREN", 
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
    RULE_menthod_decl = 14
    RULE_parameter = 15
    RULE_parameterlist = 16
    RULE_signature = 17
    RULE_func_decl = 18
    RULE_block = 19
    RULE_list_statement = 20
    RULE_const_decl_stmt = 21
    RULE_var_decl_stmt = 22
    RULE_end_stmt = 23
    RULE_expression = 24
    RULE_term_1 = 25
    RULE_term_2 = 26
    RULE_term_3 = 27
    RULE_term_4 = 28
    RULE_term_5 = 29
    RULE_term_6 = 30
    RULE_term_7 = 31
    RULE_primitive_type = 32
    RULE_array_lit = 33
    RULE_list_array_elements = 34
    RULE_array_element = 35
    RULE_nested_array = 36
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
    RULE_struct_decl = 50
    RULE_list_field_decl = 51
    RULE_field_decl = 52

    ruleNames =  [ "program", "statement", "assignment_stmt", "ass_op", 
                   "if_stmt", "else_stmt", "for_stmt", "basic_for", "with_init_con_upd", 
                   "range_for", "break_stmt", "continue_stmt", "return_stmt", 
                   "call_stmt", "menthod_decl", "parameter", "parameterlist", 
                   "signature", "func_decl", "block", "list_statement", 
                   "const_decl_stmt", "var_decl_stmt", "end_stmt", "expression", 
                   "term_1", "term_2", "term_3", "term_4", "term_5", "term_6", 
                   "term_7", "primitive_type", "array_lit", "list_array_elements", 
                   "array_element", "nested_array", "array_access", "type_", 
                   "list_dimention", "dimention", "struct_access", "func_call", 
                   "struct_lit", "list_struct_elements", "struct_elements", 
                   "type_decl", "interface_decl", "list_menthod", "menthod", 
                   "struct_decl", "list_field_decl", "field_decl" ]

    EOF = Token.EOF
    ML_COMMENT=1
    SL_COMMENT=2
    WS=3
    NL=4
    NIL_LITERAL=5
    BOOLEAN_LITERAL=6
    STRING_LITERAL=7
    FLOAT_LITERAL=8
    INTERGER_LITERAL=9
    COLON=10
    LPAREN=11
    RPAREN=12
    LBRACE=13
    RBRACE=14
    LBRACK=15
    RBRACK=16
    COMMA=17
    SEMI=18
    ADD=19
    SUB=20
    MUL=21
    DIV=22
    MOD=23
    EQ=24
    NEQ=25
    LT=26
    LE=27
    GT=28
    GE=29
    AND=30
    OR=31
    NOT=32
    ASSIGN=33
    COLON_ASSIGN=34
    ADD_ASSIGN=35
    SUB_ASSIGN=36
    MUL_ASSIGN=37
    DIV_ASSIGN=38
    MOD_ASSIGN=39
    DOT=40
    IF=41
    ELSE=42
    FOR=43
    STRUCT=44
    INTERFACE=45
    STRING=46
    CONST=47
    VAR=48
    RETURN=49
    FUNC=50
    INT=51
    TYPE=52
    FLOAT=53
    BOOLEAN=54
    CONTINUE=55
    BREAK=56
    RANGE=57
    TRUE=58
    FALSE=59
    NIL=60
    IDENTIFIER=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.INTERGER_LITERAL) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
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


        def menthod_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Menthod_declContext,0)


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


        def type_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Type_declContext,0)


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
            self.state = 149
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
                self.menthod_decl()
                self.state = 123
                self.end_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 125
                self.assignment_stmt()
                self.state = 126
                self.end_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 128
                self.if_stmt()
                self.state = 129
                self.end_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 131
                self.for_stmt()
                self.state = 132
                self.end_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 134
                self.break_stmt()
                self.state = 135
                self.end_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 137
                self.continue_stmt()
                self.state = 138
                self.end_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 140
                self.return_stmt()
                self.state = 141
                self.end_stmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 143
                self.call_stmt()
                self.state = 144
                self.end_stmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 146
                self.type_decl()
                self.state = 147
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

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def ass_op(self):
            return self.getTypedRuleContext(MiniGoParser.Ass_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


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
            self.state = 151
            self.primitive_type()
            self.state = 152
            self.ass_op()
            self.state = 153
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
            self.state = 155
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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

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
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(MiniGoParser.IF)
                self.state = 158
                self.match(MiniGoParser.LPAREN)
                self.state = 159
                self.expression()
                self.state = 160
                self.match(MiniGoParser.RPAREN)
                self.state = 161
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(MiniGoParser.IF)
                self.state = 164
                self.match(MiniGoParser.LPAREN)
                self.state = 165
                self.expression()
                self.state = 166
                self.match(MiniGoParser.RPAREN)
                self.state = 167
                self.block()
                self.state = 168
                self.else_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.match(MiniGoParser.IF)
                self.state = 171
                self.match(MiniGoParser.LPAREN)
                self.state = 172
                self.expression()
                self.state = 173
                self.match(MiniGoParser.RPAREN)
                self.state = 174
                self.match(MiniGoParser.LBRACE)
                self.state = 175
                self.if_stmt()
                self.state = 176
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
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(MiniGoParser.ELSE)
                self.state = 181
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(MiniGoParser.ELSE)
                self.state = 183
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
            self.state = 186
            self.match(MiniGoParser.FOR)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 187
                self.basic_for()
                pass

            elif la_ == 2:
                self.state = 188
                self.with_init_con_upd()
                pass

            elif la_ == 3:
                self.state = 189
                self.range_for()
                pass


            self.state = 192
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
            self.state = 194
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
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.INTERGER_LITERAL, MiniGoParser.LBRACK, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL, MiniGoParser.IDENTIFIER]:
                self.state = 196
                self.assignment_stmt()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 197
                self.var_decl_stmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 200
            self.match(MiniGoParser.SEMI)
            self.state = 201
            self.expression()
            self.state = 202
            self.match(MiniGoParser.SEMI)
            self.state = 203
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
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.state = 205
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.COMMA]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 209
            self.match(MiniGoParser.COMMA)
            self.state = 210
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 211
            self.match(MiniGoParser.COLON_ASSIGN)
            self.state = 212
            self.match(MiniGoParser.RANGE)
            self.state = 213
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
            self.state = 215
            self.match(MiniGoParser.BREAK)
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
            self.state = 217
            self.match(MiniGoParser.CONTINUE)
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
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(MiniGoParser.RETURN)
                self.state = 220
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(MiniGoParser.RETURN)
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
            self.state = 224
            self.func_call()
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

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Type_Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Type_Context,i)


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
        self.enterRule(localctx, 28, self.RULE_menthod_decl)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(MiniGoParser.FUNC)
                self.state = 227
                self.match(MiniGoParser.LPAREN)
                self.state = 228
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 229
                self.type_()
                self.state = 230
                self.match(MiniGoParser.RPAREN)
                self.state = 231
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 232
                self.signature()
                self.state = 233
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(MiniGoParser.FUNC)
                self.state = 236
                self.match(MiniGoParser.LPAREN)
                self.state = 237
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 238
                self.type_()
                self.state = 239
                self.match(MiniGoParser.RPAREN)
                self.state = 240
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 241
                self.signature()
                self.state = 242
                self.type_()
                self.state = 243
                self.block()
                pass


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
        self.enterRule(localctx, 30, self.RULE_parameter)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 248
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
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
        self.enterRule(localctx, 32, self.RULE_parameterlist)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.parameter()
                self.state = 254
                self.match(MiniGoParser.COMMA)
                self.state = 255
                self.parameterlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_signature

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignature" ):
                return visitor.visitSignature(self)
            else:
                return visitor.visitChildren(self)




    def signature(self):

        localctx = MiniGoParser.SignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_signature)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(MiniGoParser.LPAREN)
                self.state = 261
                self.parameterlist()
                self.state = 262
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(MiniGoParser.LPAREN)
                self.state = 265
                self.match(MiniGoParser.RPAREN)
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


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_func_decl)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(MiniGoParser.FUNC)
                self.state = 269
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 270
                self.signature()
                self.state = 271
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(MiniGoParser.FUNC)
                self.state = 274
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 275
                self.signature()
                self.state = 276
                self.type_()
                self.state = 277
                self.block()
                pass


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

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(MiniGoParser.LBRACE)
            self.state = 282
            self.list_statement(0)
            self.state = 283
            self.match(MiniGoParser.RBRACE)
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


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)



    def list_statement(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.List_statementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_list_statement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 286
                self.statement()
                pass

            elif la_ == 2:
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.List_statementContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_list_statement)
                    self.state = 290
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 291
                    self.statement() 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl_stmt" ):
                return visitor.visitConst_decl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def const_decl_stmt(self):

        localctx = MiniGoParser.Const_decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_const_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MiniGoParser.CONST)
            self.state = 298
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 299
            self.match(MiniGoParser.ASSIGN)
            self.state = 300
            self.expression()
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
        self.enterRule(localctx, 44, self.RULE_var_decl_stmt)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(MiniGoParser.VAR)
                self.state = 303
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.match(MiniGoParser.VAR)
                self.state = 305
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 306
                self.type_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.match(MiniGoParser.VAR)
                self.state = 308
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 309
                self.type_()
                self.state = 310
                self.match(MiniGoParser.ASSIGN)
                self.state = 311
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.match(MiniGoParser.VAR)
                self.state = 314
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 315
                self.match(MiniGoParser.ASSIGN)
                self.state = 316
                self.expression()
                pass


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
        self.enterRule(localctx, 46, self.RULE_end_stmt)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(MiniGoParser.NL)
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
        self.enterRule(localctx, 48, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
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
        self.enterRule(localctx, 50, self.RULE_term_1)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.term_2()
                self.state = 327
                self.match(MiniGoParser.OR)
                self.state = 328
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
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
        self.enterRule(localctx, 52, self.RULE_term_2)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.term_3()
                self.state = 334
                self.match(MiniGoParser.AND)
                self.state = 335
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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
        self.enterRule(localctx, 54, self.RULE_term_3)
        self._la = 0 # Token type
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.term_4()
                self.state = 341
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 342
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
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
        self.enterRule(localctx, 56, self.RULE_term_4)
        self._la = 0 # Token type
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.term_5()
                self.state = 348
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 349
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
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
        self.enterRule(localctx, 58, self.RULE_term_5)
        self._la = 0 # Token type
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.term_6()
                self.state = 355
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 356
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
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

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def term_7(self):
            return self.getTypedRuleContext(MiniGoParser.Term_7Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_term_6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_6" ):
                return visitor.visitTerm_6(self)
            else:
                return visitor.visitChildren(self)




    def term_6(self):

        localctx = MiniGoParser.Term_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_term_6)
        self._la = 0 # Token type
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 362
                self.expression()
                pass
            elif token in [MiniGoParser.NIL_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.INTERGER_LITERAL, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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
        self.enterRule(localctx, 62, self.RULE_term_7)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.array_lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
                self.struct_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 369
                self.match(MiniGoParser.LPAREN)
                self.state = 370
                self.expression()
                self.state = 371
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 373
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

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def INTERGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTERGER_LITERAL, 0)

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
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.struct_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.match(MiniGoParser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 379
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 380
                self.match(MiniGoParser.INTERGER_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 381
                self.match(MiniGoParser.BOOLEAN_LITERAL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 382
                self.match(MiniGoParser.NIL_LITERAL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 383
                self.match(MiniGoParser.IDENTIFIER)
                pass


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
        self.enterRule(localctx, 66, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.type_()
            self.state = 387
            self.match(MiniGoParser.LBRACE)
            self.state = 388
            self.list_array_elements()
            self.state = 389
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
        self.enterRule(localctx, 68, self.RULE_list_array_elements)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.array_element()
                self.state = 392
                self.match(MiniGoParser.COMMA)
                self.state = 393
                self.list_array_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.array_element()
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


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def nested_array(self):
            return self.getTypedRuleContext(MiniGoParser.Nested_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_array_element)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.INTERGER_LITERAL, MiniGoParser.LBRACK, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.nested_array()
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


    class Nested_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_array_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_nested_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNested_array" ):
                return visitor.visitNested_array(self)
            else:
                return visitor.visitChildren(self)




    def nested_array(self):

        localctx = MiniGoParser.Nested_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_nested_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MiniGoParser.LBRACE)
            self.state = 404
            self.list_array_elements()
            self.state = 405
            self.match(MiniGoParser.RBRACE)
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
            self.state = 407
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 408
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

        def list_dimention(self):
            return self.getTypedRuleContext(MiniGoParser.List_dimentionContext,0)


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
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 412
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 413
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 414
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 415
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 7)
                self.state = 416
                self.list_dimention()
                self.state = 417
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
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.dimention()
                self.state = 422
                self.list_dimention()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
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
            self.state = 427
            self.match(MiniGoParser.LBRACK)
            self.state = 428
            self.match(MiniGoParser.INTERGER_LITERAL)
            self.state = 429
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
            self.state = 431
            self.type_()
            self.state = 432
            self.match(MiniGoParser.DOT)
            self.state = 433
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
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 436
                self.signature()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 438
                self.match(MiniGoParser.DOT)
                self.state = 439
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 440
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

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_struct_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elementsContext,0)


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
            self.state = 443
            self.type_()
            self.state = 444
            self.match(MiniGoParser.LBRACE)
            self.state = 445
            self.list_struct_elements()
            self.state = 446
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
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.struct_elements()
                self.state = 449
                self.match(MiniGoParser.COMMA)
                self.state = 450
                self.list_struct_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
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
            self.state = 455
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 456
            self.match(MiniGoParser.COLON)
            self.state = 457
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


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


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
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.interface_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.struct_decl()
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
            self.state = 463
            self.match(MiniGoParser.TYPE)
            self.state = 464
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 465
            self.match(MiniGoParser.INTERFACE)
            self.state = 466
            self.match(MiniGoParser.LBRACE)
            self.state = 467
            self.list_menthod()
            self.state = 468
            self.match(MiniGoParser.RBRACE)
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
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.menthod()
                self.state = 471
                self.list_menthod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.menthod()
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


    class MenthodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


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
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 478
                self.signature()
                self.state = 479
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 482
                self.signature()
                self.state = 483
                self.type_()
                self.state = 484
                self.end_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
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

        def list_field_decl(self):
            return self.getTypedRuleContext(MiniGoParser.List_field_declContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(MiniGoParser.TYPE)
            self.state = 489
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 490
            self.match(MiniGoParser.STRUCT)
            self.state = 491
            self.match(MiniGoParser.LBRACE)
            self.state = 492
            self.list_field_decl()
            self.state = 493
            self.match(MiniGoParser.RBRACE)
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
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.field_decl()
                self.state = 496
                self.list_field_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.field_decl()
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


    class Field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


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
            self.state = 502
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 503
            self.type_()
            self.state = 504
            self.end_stmt()
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
        self._predicates[20] = self.list_statement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def list_statement_sempred(self, localctx:List_statementContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




