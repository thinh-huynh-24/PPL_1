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
        buf.write("\u01df\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\6\2l\n\2\r\2\16\2m\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\u0082\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u009f\n\6\3\7\3\7\3\7\3\7\5\7\u00a5\n")
        buf.write("\7\3\b\3\b\3\b\3\b\5\b\u00ab\n\b\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\5\n\u00b3\n\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\5\13\u00bc")
        buf.write("\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\5\16\u00cd\n\16\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00e7\n\21\3\22\3\22\3\22\3\22\5\22\u00ed\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u00f4\n\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u00fc\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\5\25\u0109\n\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\5\27\u0112\n\27\3\27\3\27\7")
        buf.write("\27\u0116\n\27\f\27\16\27\u0119\13\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u012f\n\31\3\32\3")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\5\33\u0138\n\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u013f\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\5\35\u0146\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u014d")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u0154\n\37\3 \3 \3")
        buf.write(" \5 \u0159\n \3!\3!\3!\3!\3!\3!\3!\3!\5!\u0163\n!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u016d\n\"\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\5$\u0179\n$\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\5\'\u0184\n\'\3(\3(\3(\3(\5(\u018a\n(\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\5+\u019a\n+\3,\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\5-\u01a6\n-\3.\3.\3.\3.\3/\3/\5")
        buf.write("/\u01ae\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01c0\n\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\5\62\u01c8\n\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\5\64\u01da\n\64\3\65\3\65\3\65\3\65\2")
        buf.write("\3,\66\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh\2\b\3\2$)\3\2")
        buf.write("\32\37\3\2\25\26\3\2\27\31\4\2\26\26\"\"\6\2\60\60\65")
        buf.write("\65\678>?\2\u01e5\2k\3\2\2\2\4\u0081\3\2\2\2\6\u0083\3")
        buf.write("\2\2\2\b\u0087\3\2\2\2\n\u009e\3\2\2\2\f\u00a4\3\2\2\2")
        buf.write("\16\u00a6\3\2\2\2\20\u00ae\3\2\2\2\22\u00b2\3\2\2\2\24")
        buf.write("\u00bb\3\2\2\2\26\u00c3\3\2\2\2\30\u00c6\3\2\2\2\32\u00cc")
        buf.write("\3\2\2\2\34\u00ce\3\2\2\2\36\u00d1\3\2\2\2 \u00e6\3\2")
        buf.write("\2\2\"\u00ec\3\2\2\2$\u00f3\3\2\2\2&\u00fb\3\2\2\2(\u0108")
        buf.write("\3\2\2\2*\u010a\3\2\2\2,\u0111\3\2\2\2.\u011a\3\2\2\2")
        buf.write("\60\u012e\3\2\2\2\62\u0130\3\2\2\2\64\u0137\3\2\2\2\66")
        buf.write("\u013e\3\2\2\28\u0145\3\2\2\2:\u014c\3\2\2\2<\u0153\3")
        buf.write("\2\2\2>\u0158\3\2\2\2@\u0162\3\2\2\2B\u016c\3\2\2\2D\u016e")
        buf.write("\3\2\2\2F\u0178\3\2\2\2H\u017a\3\2\2\2J\u017c\3\2\2\2")
        buf.write("L\u0183\3\2\2\2N\u0189\3\2\2\2P\u018b\3\2\2\2R\u018f\3")
        buf.write("\2\2\2T\u0199\3\2\2\2V\u019b\3\2\2\2X\u01a5\3\2\2\2Z\u01a7")
        buf.write("\3\2\2\2\\\u01ad\3\2\2\2^\u01af\3\2\2\2`\u01bf\3\2\2\2")
        buf.write("b\u01c7\3\2\2\2d\u01c9\3\2\2\2f\u01d9\3\2\2\2h\u01db\3")
        buf.write("\2\2\2jl\5\4\3\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2")
        buf.write("\2no\3\2\2\2op\7\2\2\3p\3\3\2\2\2qr\5\60\31\2rs\5\36\20")
        buf.write("\2s\u0082\3\2\2\2tu\5.\30\2uv\5\36\20\2v\u0082\3\2\2\2")
        buf.write("w\u0082\5(\25\2x\u0082\5 \21\2y\u0082\5\6\4\2z\u0082\5")
        buf.write("\n\6\2{\u0082\5\16\b\2|\u0082\5\26\f\2}\u0082\5\30\r\2")
        buf.write("~\u0082\5\32\16\2\177\u0082\5\34\17\2\u0080\u0082\5\\")
        buf.write("/\2\u0081q\3\2\2\2\u0081t\3\2\2\2\u0081w\3\2\2\2\u0081")
        buf.write("x\3\2\2\2\u0081y\3\2\2\2\u0081z\3\2\2\2\u0081{\3\2\2\2")
        buf.write("\u0081|\3\2\2\2\u0081}\3\2\2\2\u0081~\3\2\2\2\u0081\177")
        buf.write("\3\2\2\2\u0081\u0080\3\2\2\2\u0082\5\3\2\2\2\u0083\u0084")
        buf.write("\5B\"\2\u0084\u0085\5\b\5\2\u0085\u0086\5\62\32\2\u0086")
        buf.write("\7\3\2\2\2\u0087\u0088\t\2\2\2\u0088\t\3\2\2\2\u0089\u008a")
        buf.write("\7+\2\2\u008a\u008b\7\r\2\2\u008b\u008c\5\62\32\2\u008c")
        buf.write("\u008d\7\16\2\2\u008d\u008e\5*\26\2\u008e\u009f\3\2\2")
        buf.write("\2\u008f\u0090\7+\2\2\u0090\u0091\7\r\2\2\u0091\u0092")
        buf.write("\5\62\32\2\u0092\u0093\7\16\2\2\u0093\u0094\5*\26\2\u0094")
        buf.write("\u0095\5\f\7\2\u0095\u009f\3\2\2\2\u0096\u0097\7+\2\2")
        buf.write("\u0097\u0098\7\r\2\2\u0098\u0099\5\62\32\2\u0099\u009a")
        buf.write("\7\16\2\2\u009a\u009b\7\17\2\2\u009b\u009c\5\n\6\2\u009c")
        buf.write("\u009d\7\20\2\2\u009d\u009f\3\2\2\2\u009e\u0089\3\2\2")
        buf.write("\2\u009e\u008f\3\2\2\2\u009e\u0096\3\2\2\2\u009f\13\3")
        buf.write("\2\2\2\u00a0\u00a1\7,\2\2\u00a1\u00a5\5*\26\2\u00a2\u00a3")
        buf.write("\7,\2\2\u00a3\u00a5\5\n\6\2\u00a4\u00a0\3\2\2\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a5\r\3\2\2\2\u00a6\u00aa\7-\2\2\u00a7")
        buf.write("\u00ab\5\20\t\2\u00a8\u00ab\5\22\n\2\u00a9\u00ab\5\24")
        buf.write("\13\2\u00aa\u00a7\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\5*\26\2\u00ad")
        buf.write("\17\3\2\2\2\u00ae\u00af\5\62\32\2\u00af\21\3\2\2\2\u00b0")
        buf.write("\u00b3\5\6\4\2\u00b1\u00b3\5\60\31\2\u00b2\u00b0\3\2\2")
        buf.write("\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5")
        buf.write("\7\24\2\2\u00b5\u00b6\5\62\32\2\u00b6\u00b7\7\24\2\2\u00b7")
        buf.write("\u00b8\5\6\4\2\u00b8\23\3\2\2\2\u00b9\u00bc\7?\2\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd\u00be\7\23\2\2\u00be\u00bf")
        buf.write("\7?\2\2\u00bf\u00c0\7$\2\2\u00c0\u00c1\7;\2\2\u00c1\u00c2")
        buf.write("\5B\"\2\u00c2\25\3\2\2\2\u00c3\u00c4\7:\2\2\u00c4\u00c5")
        buf.write("\7\24\2\2\u00c5\27\3\2\2\2\u00c6\u00c7\79\2\2\u00c7\u00c8")
        buf.write("\7\24\2\2\u00c8\31\3\2\2\2\u00c9\u00ca\7\63\2\2\u00ca")
        buf.write("\u00cd\5\62\32\2\u00cb\u00cd\7\63\2\2\u00cc\u00c9\3\2")
        buf.write("\2\2\u00cc\u00cb\3\2\2\2\u00cd\33\3\2\2\2\u00ce\u00cf")
        buf.write("\5T+\2\u00cf\u00d0\5\36\20\2\u00d0\35\3\2\2\2\u00d1\u00d2")
        buf.write("\7\24\2\2\u00d2\37\3\2\2\2\u00d3\u00d4\7\64\2\2\u00d4")
        buf.write("\u00d5\7\r\2\2\u00d5\u00d6\7?\2\2\u00d6\u00d7\5L\'\2\u00d7")
        buf.write("\u00d8\7\16\2\2\u00d8\u00d9\7?\2\2\u00d9\u00da\5&\24\2")
        buf.write("\u00da\u00db\5*\26\2\u00db\u00e7\3\2\2\2\u00dc\u00dd\7")
        buf.write("\64\2\2\u00dd\u00de\7\r\2\2\u00de\u00df\7?\2\2\u00df\u00e0")
        buf.write("\5L\'\2\u00e0\u00e1\7\16\2\2\u00e1\u00e2\7?\2\2\u00e2")
        buf.write("\u00e3\5&\24\2\u00e3\u00e4\5L\'\2\u00e4\u00e5\5*\26\2")
        buf.write("\u00e5\u00e7\3\2\2\2\u00e6\u00d3\3\2\2\2\u00e6\u00dc\3")
        buf.write("\2\2\2\u00e7!\3\2\2\2\u00e8\u00e9\7?\2\2\u00e9\u00ed\5")
        buf.write("L\'\2\u00ea\u00ed\7?\2\2\u00eb\u00ed\5\62\32\2\u00ec\u00e8")
        buf.write("\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed")
        buf.write("#\3\2\2\2\u00ee\u00ef\5\"\22\2\u00ef\u00f0\7\23\2\2\u00f0")
        buf.write("\u00f1\5$\23\2\u00f1\u00f4\3\2\2\2\u00f2\u00f4\5\"\22")
        buf.write("\2\u00f3\u00ee\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4%\3\2")
        buf.write("\2\2\u00f5\u00f6\7\r\2\2\u00f6\u00f7\5$\23\2\u00f7\u00f8")
        buf.write("\7\16\2\2\u00f8\u00fc\3\2\2\2\u00f9\u00fa\7\r\2\2\u00fa")
        buf.write("\u00fc\7\16\2\2\u00fb\u00f5\3\2\2\2\u00fb\u00f9\3\2\2")
        buf.write("\2\u00fc\'\3\2\2\2\u00fd\u00fe\7\64\2\2\u00fe\u00ff\7")
        buf.write("?\2\2\u00ff\u0100\5&\24\2\u0100\u0101\5*\26\2\u0101\u0109")
        buf.write("\3\2\2\2\u0102\u0103\7\64\2\2\u0103\u0104\7?\2\2\u0104")
        buf.write("\u0105\5&\24\2\u0105\u0106\5L\'\2\u0106\u0107\5*\26\2")
        buf.write("\u0107\u0109\3\2\2\2\u0108\u00fd\3\2\2\2\u0108\u0102\3")
        buf.write("\2\2\2\u0109)\3\2\2\2\u010a\u010b\7\17\2\2\u010b\u010c")
        buf.write("\5,\27\2\u010c\u010d\7\20\2\2\u010d+\3\2\2\2\u010e\u010f")
        buf.write("\b\27\1\2\u010f\u0112\5\4\3\2\u0110\u0112\3\2\2\2\u0111")
        buf.write("\u010e\3\2\2\2\u0111\u0110\3\2\2\2\u0112\u0117\3\2\2\2")
        buf.write("\u0113\u0114\f\5\2\2\u0114\u0116\5\4\3\2\u0115\u0113\3")
        buf.write("\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118-\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b")
        buf.write("\7\61\2\2\u011b\u011c\7?\2\2\u011c\u011d\7#\2\2\u011d")
        buf.write("\u011e\5\62\32\2\u011e/\3\2\2\2\u011f\u0120\7\62\2\2\u0120")
        buf.write("\u012f\7?\2\2\u0121\u0122\7\62\2\2\u0122\u0123\7?\2\2")
        buf.write("\u0123\u012f\5L\'\2\u0124\u0125\7\62\2\2\u0125\u0126\7")
        buf.write("?\2\2\u0126\u0127\5L\'\2\u0127\u0128\7#\2\2\u0128\u0129")
        buf.write("\5\62\32\2\u0129\u012f\3\2\2\2\u012a\u012b\7\62\2\2\u012b")
        buf.write("\u012c\7?\2\2\u012c\u012d\7#\2\2\u012d\u012f\5\62\32\2")
        buf.write("\u012e\u011f\3\2\2\2\u012e\u0121\3\2\2\2\u012e\u0124\3")
        buf.write("\2\2\2\u012e\u012a\3\2\2\2\u012f\61\3\2\2\2\u0130\u0131")
        buf.write("\5\64\33\2\u0131\63\3\2\2\2\u0132\u0133\5\66\34\2\u0133")
        buf.write("\u0134\7!\2\2\u0134\u0135\5\62\32\2\u0135\u0138\3\2\2")
        buf.write("\2\u0136\u0138\5\66\34\2\u0137\u0132\3\2\2\2\u0137\u0136")
        buf.write("\3\2\2\2\u0138\65\3\2\2\2\u0139\u013a\58\35\2\u013a\u013b")
        buf.write("\7 \2\2\u013b\u013c\5\62\32\2\u013c\u013f\3\2\2\2\u013d")
        buf.write("\u013f\58\35\2\u013e\u0139\3\2\2\2\u013e\u013d\3\2\2\2")
        buf.write("\u013f\67\3\2\2\2\u0140\u0141\5:\36\2\u0141\u0142\t\3")
        buf.write("\2\2\u0142\u0143\5\62\32\2\u0143\u0146\3\2\2\2\u0144\u0146")
        buf.write("\5:\36\2\u0145\u0140\3\2\2\2\u0145\u0144\3\2\2\2\u0146")
        buf.write("9\3\2\2\2\u0147\u0148\5<\37\2\u0148\u0149\t\4\2\2\u0149")
        buf.write("\u014a\5\62\32\2\u014a\u014d\3\2\2\2\u014b\u014d\5<\37")
        buf.write("\2\u014c\u0147\3\2\2\2\u014c\u014b\3\2\2\2\u014d;\3\2")
        buf.write("\2\2\u014e\u014f\5> \2\u014f\u0150\t\5\2\2\u0150\u0151")
        buf.write("\5\62\32\2\u0151\u0154\3\2\2\2\u0152\u0154\5> \2\u0153")
        buf.write("\u014e\3\2\2\2\u0153\u0152\3\2\2\2\u0154=\3\2\2\2\u0155")
        buf.write("\u0156\t\6\2\2\u0156\u0159\5\62\32\2\u0157\u0159\5@!\2")
        buf.write("\u0158\u0155\3\2\2\2\u0158\u0157\3\2\2\2\u0159?\3\2\2")
        buf.write("\2\u015a\u0163\5B\"\2\u015b\u0163\5D#\2\u015c\u0163\5")
        buf.write("V,\2\u015d\u015e\7\r\2\2\u015e\u015f\5\62\32\2\u015f\u0160")
        buf.write("\7\16\2\2\u0160\u0163\3\2\2\2\u0161\u0163\5T+\2\u0162")
        buf.write("\u015a\3\2\2\2\u0162\u015b\3\2\2\2\u0162\u015c\3\2\2\2")
        buf.write("\u0162\u015d\3\2\2\2\u0162\u0161\3\2\2\2\u0163A\3\2\2")
        buf.write("\2\u0164\u016d\5R*\2\u0165\u016d\5J&\2\u0166\u016d\7\t")
        buf.write("\2\2\u0167\u016d\7\n\2\2\u0168\u016d\7\13\2\2\u0169\u016d")
        buf.write("\7\b\2\2\u016a\u016d\7\7\2\2\u016b\u016d\7?\2\2\u016c")
        buf.write("\u0164\3\2\2\2\u016c\u0165\3\2\2\2\u016c\u0166\3\2\2\2")
        buf.write("\u016c\u0167\3\2\2\2\u016c\u0168\3\2\2\2\u016c\u0169\3")
        buf.write("\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016dC")
        buf.write("\3\2\2\2\u016e\u016f\5L\'\2\u016f\u0170\7\17\2\2\u0170")
        buf.write("\u0171\5F$\2\u0171\u0172\7\20\2\2\u0172E\3\2\2\2\u0173")
        buf.write("\u0174\5H%\2\u0174\u0175\7\23\2\2\u0175\u0176\5F$\2\u0176")
        buf.write("\u0179\3\2\2\2\u0177\u0179\5H%\2\u0178\u0173\3\2\2\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179G\3\2\2\2\u017a\u017b\5B\"\2\u017b")
        buf.write("I\3\2\2\2\u017c\u017d\7?\2\2\u017d\u017e\5N(\2\u017eK")
        buf.write("\3\2\2\2\u017f\u0184\t\7\2\2\u0180\u0181\5N(\2\u0181\u0182")
        buf.write("\t\7\2\2\u0182\u0184\3\2\2\2\u0183\u017f\3\2\2\2\u0183")
        buf.write("\u0180\3\2\2\2\u0184M\3\2\2\2\u0185\u0186\5P)\2\u0186")
        buf.write("\u0187\5N(\2\u0187\u018a\3\2\2\2\u0188\u018a\5P)\2\u0189")
        buf.write("\u0185\3\2\2\2\u0189\u0188\3\2\2\2\u018aO\3\2\2\2\u018b")
        buf.write("\u018c\7\21\2\2\u018c\u018d\7\13\2\2\u018d\u018e\7\22")
        buf.write("\2\2\u018eQ\3\2\2\2\u018f\u0190\5L\'\2\u0190\u0191\7*")
        buf.write("\2\2\u0191\u0192\7?\2\2\u0192S\3\2\2\2\u0193\u0194\7?")
        buf.write("\2\2\u0194\u019a\5&\24\2\u0195\u0196\7?\2\2\u0196\u0197")
        buf.write("\7*\2\2\u0197\u0198\7?\2\2\u0198\u019a\5&\24\2\u0199\u0193")
        buf.write("\3\2\2\2\u0199\u0195\3\2\2\2\u019aU\3\2\2\2\u019b\u019c")
        buf.write("\7?\2\2\u019c\u019d\7\17\2\2\u019d\u019e\5X-\2\u019e\u019f")
        buf.write("\7\20\2\2\u019fW\3\2\2\2\u01a0\u01a1\5Z.\2\u01a1\u01a2")
        buf.write("\7\23\2\2\u01a2\u01a3\5X-\2\u01a3\u01a6\3\2\2\2\u01a4")
        buf.write("\u01a6\5Z.\2\u01a5\u01a0\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6")
        buf.write("Y\3\2\2\2\u01a7\u01a8\7?\2\2\u01a8\u01a9\7\f\2\2\u01a9")
        buf.write("\u01aa\5\62\32\2\u01aa[\3\2\2\2\u01ab\u01ae\5^\60\2\u01ac")
        buf.write("\u01ae\5d\63\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2")
        buf.write("\u01ae]\3\2\2\2\u01af\u01b0\7\66\2\2\u01b0\u01b1\7?\2")
        buf.write("\2\u01b1\u01b2\7/\2\2\u01b2\u01b3\7\17\2\2\u01b3\u01b4")
        buf.write("\5`\61\2\u01b4\u01b5\7\20\2\2\u01b5\u01b6\5\36\20\2\u01b6")
        buf.write("_\3\2\2\2\u01b7\u01b8\5b\62\2\u01b8\u01b9\5\36\20\2\u01b9")
        buf.write("\u01ba\5`\61\2\u01ba\u01c0\3\2\2\2\u01bb\u01bc\5b\62\2")
        buf.write("\u01bc\u01bd\5\36\20\2\u01bd\u01c0\3\2\2\2\u01be\u01c0")
        buf.write("\3\2\2\2\u01bf\u01b7\3\2\2\2\u01bf\u01bb\3\2\2\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01c0a\3\2\2\2\u01c1\u01c2\7?\2\2\u01c2")
        buf.write("\u01c8\5&\24\2\u01c3\u01c4\7?\2\2\u01c4\u01c5\5&\24\2")
        buf.write("\u01c5\u01c6\5L\'\2\u01c6\u01c8\3\2\2\2\u01c7\u01c1\3")
        buf.write("\2\2\2\u01c7\u01c3\3\2\2\2\u01c8c\3\2\2\2\u01c9\u01ca")
        buf.write("\7\66\2\2\u01ca\u01cb\7?\2\2\u01cb\u01cc\7.\2\2\u01cc")
        buf.write("\u01cd\7\17\2\2\u01cd\u01ce\5f\64\2\u01ce\u01cf\7\20\2")
        buf.write("\2\u01cf\u01d0\5\36\20\2\u01d0e\3\2\2\2\u01d1\u01d2\5")
        buf.write("h\65\2\u01d2\u01d3\5\36\20\2\u01d3\u01d4\5f\64\2\u01d4")
        buf.write("\u01da\3\2\2\2\u01d5\u01d6\5h\65\2\u01d6\u01d7\5\36\20")
        buf.write("\2\u01d7\u01da\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01d1")
        buf.write("\3\2\2\2\u01d9\u01d5\3\2\2\2\u01d9\u01d8\3\2\2\2\u01da")
        buf.write("g\3\2\2\2\u01db\u01dc\7?\2\2\u01dc\u01dd\5L\'\2\u01dd")
        buf.write("i\3\2\2\2#m\u0081\u009e\u00a4\u00aa\u00b2\u00bb\u00cc")
        buf.write("\u00e6\u00ec\u00f3\u00fb\u0108\u0111\u0117\u012e\u0137")
        buf.write("\u013e\u0145\u014c\u0153\u0158\u0162\u016c\u0178\u0183")
        buf.write("\u0189\u0199\u01a5\u01ad\u01bf\u01c7\u01d9")
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
    RULE_end_stmt = 14
    RULE_menthod_decl = 15
    RULE_parameter = 16
    RULE_parameterlist = 17
    RULE_signature = 18
    RULE_func_decl = 19
    RULE_block = 20
    RULE_list_statement = 21
    RULE_const_decl_stmt = 22
    RULE_var_decl_stmt = 23
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
    RULE_array_access = 36
    RULE_type_ = 37
    RULE_list_dimention = 38
    RULE_dimention = 39
    RULE_struct_access = 40
    RULE_func_call = 41
    RULE_struct_lit = 42
    RULE_list_struct_elements = 43
    RULE_struct_elements = 44
    RULE_type_decl = 45
    RULE_interface_decl = 46
    RULE_list_menthod = 47
    RULE_menthod = 48
    RULE_struck_decl = 49
    RULE_list_field_decl = 50
    RULE_field_decl = 51

    ruleNames =  [ "program", "statement", "assignment_stmt", "ass_op", 
                   "if_stmt", "else_stmt", "for_stmt", "basic_for", "with_init_con_upd", 
                   "range_for", "break_stmt", "continue_stmt", "return_stmt", 
                   "call_stmt", "end_stmt", "menthod_decl", "parameter", 
                   "parameterlist", "signature", "func_decl", "block", "list_statement", 
                   "const_decl_stmt", "var_decl_stmt", "expression", "term_1", 
                   "term_2", "term_3", "term_4", "term_5", "term_6", "term_7", 
                   "primitive_type", "array_lit", "list_array_elements", 
                   "array_element", "array_access", "type_", "list_dimention", 
                   "dimention", "struct_access", "func_call", "struct_lit", 
                   "list_struct_elements", "struct_elements", "type_decl", 
                   "interface_decl", "list_menthod", "menthod", "struck_decl", 
                   "list_field_decl", "field_decl" ]

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
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.statement()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.INTERGER_LITERAL) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 109
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.var_decl_stmt()
                self.state = 112
                self.end_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.const_decl_stmt()
                self.state = 115
                self.end_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.menthod_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 119
                self.assignment_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 120
                self.if_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 121
                self.for_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 122
                self.break_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 123
                self.continue_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 124
                self.return_stmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 125
                self.call_stmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 126
                self.type_decl()
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
            self.state = 129
            self.primitive_type()
            self.state = 130
            self.ass_op()
            self.state = 131
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
            self.state = 133
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
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(MiniGoParser.IF)
                self.state = 136
                self.match(MiniGoParser.LPAREN)
                self.state = 137
                self.expression()
                self.state = 138
                self.match(MiniGoParser.RPAREN)
                self.state = 139
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(MiniGoParser.IF)
                self.state = 142
                self.match(MiniGoParser.LPAREN)
                self.state = 143
                self.expression()
                self.state = 144
                self.match(MiniGoParser.RPAREN)
                self.state = 145
                self.block()
                self.state = 146
                self.else_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.match(MiniGoParser.IF)
                self.state = 149
                self.match(MiniGoParser.LPAREN)
                self.state = 150
                self.expression()
                self.state = 151
                self.match(MiniGoParser.RPAREN)
                self.state = 152
                self.match(MiniGoParser.LBRACE)
                self.state = 153
                self.if_stmt()
                self.state = 154
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
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(MiniGoParser.ELSE)
                self.state = 159
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(MiniGoParser.ELSE)
                self.state = 161
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
            self.state = 164
            self.match(MiniGoParser.FOR)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 165
                self.basic_for()
                pass

            elif la_ == 2:
                self.state = 166
                self.with_init_con_upd()
                pass

            elif la_ == 3:
                self.state = 167
                self.range_for()
                pass


            self.state = 170
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
            self.state = 172
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
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.INTERGER_LITERAL, MiniGoParser.LBRACK, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL, MiniGoParser.IDENTIFIER]:
                self.state = 174
                self.assignment_stmt()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 175
                self.var_decl_stmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 178
            self.match(MiniGoParser.SEMI)
            self.state = 179
            self.expression()
            self.state = 180
            self.match(MiniGoParser.SEMI)
            self.state = 181
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
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.state = 183
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.COMMA]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 187
            self.match(MiniGoParser.COMMA)
            self.state = 188
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 189
            self.match(MiniGoParser.COLON_ASSIGN)
            self.state = 190
            self.match(MiniGoParser.RANGE)
            self.state = 191
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
            self.state = 193
            self.match(MiniGoParser.BREAK)
            self.state = 194
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
            self.state = 196
            self.match(MiniGoParser.CONTINUE)
            self.state = 197
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
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(MiniGoParser.RETURN)
                self.state = 200
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
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


        def end_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmtContext,0)


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
            self.state = 204
            self.func_call()
            self.state = 205
            self.end_stmt()
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(MiniGoParser.SEMI)
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
        self.enterRule(localctx, 30, self.RULE_menthod_decl)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(MiniGoParser.FUNC)
                self.state = 210
                self.match(MiniGoParser.LPAREN)
                self.state = 211
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 212
                self.type_()
                self.state = 213
                self.match(MiniGoParser.RPAREN)
                self.state = 214
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 215
                self.signature()
                self.state = 216
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(MiniGoParser.FUNC)
                self.state = 219
                self.match(MiniGoParser.LPAREN)
                self.state = 220
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 221
                self.type_()
                self.state = 222
                self.match(MiniGoParser.RPAREN)
                self.state = 223
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 224
                self.signature()
                self.state = 225
                self.type_()
                self.state = 226
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
        self.enterRule(localctx, 32, self.RULE_parameter)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 231
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
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
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.parameter()
                self.state = 237
                self.match(MiniGoParser.COMMA)
                self.state = 238
                self.parameterlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
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
        self.enterRule(localctx, 36, self.RULE_signature)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(MiniGoParser.LPAREN)
                self.state = 244
                self.parameterlist()
                self.state = 245
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(MiniGoParser.LPAREN)
                self.state = 248
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
        self.enterRule(localctx, 38, self.RULE_func_decl)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(MiniGoParser.FUNC)
                self.state = 252
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 253
                self.signature()
                self.state = 254
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(MiniGoParser.FUNC)
                self.state = 257
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 258
                self.signature()
                self.state = 259
                self.type_()
                self.state = 260
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
        self.enterRule(localctx, 40, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(MiniGoParser.LBRACE)
            self.state = 265
            self.list_statement(0)
            self.state = 266
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_list_statement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 269
                self.statement()
                pass

            elif la_ == 2:
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.List_statementContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_list_statement)
                    self.state = 273
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 274
                    self.statement() 
                self.state = 279
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
        self.enterRule(localctx, 44, self.RULE_const_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniGoParser.CONST)
            self.state = 281
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 282
            self.match(MiniGoParser.ASSIGN)
            self.state = 283
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
        self.enterRule(localctx, 46, self.RULE_var_decl_stmt)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(MiniGoParser.VAR)
                self.state = 286
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(MiniGoParser.VAR)
                self.state = 288
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 289
                self.type_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                self.match(MiniGoParser.VAR)
                self.state = 291
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 292
                self.type_()
                self.state = 293
                self.match(MiniGoParser.ASSIGN)
                self.state = 294
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 296
                self.match(MiniGoParser.VAR)
                self.state = 297
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 298
                self.match(MiniGoParser.ASSIGN)
                self.state = 299
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
        self.enterRule(localctx, 48, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
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
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.term_2()
                self.state = 305
                self.match(MiniGoParser.OR)
                self.state = 306
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
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
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.term_3()
                self.state = 312
                self.match(MiniGoParser.AND)
                self.state = 313
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
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
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.term_4()
                self.state = 319
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 320
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
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
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.term_5()
                self.state = 326
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 327
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
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
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.term_6()
                self.state = 333
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 334
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
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
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 340
                self.expression()
                pass
            elif token in [MiniGoParser.NIL_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.INTERGER_LITERAL, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
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
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.array_lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 346
                self.struct_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 347
                self.match(MiniGoParser.LPAREN)
                self.state = 348
                self.expression()
                self.state = 349
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 351
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
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.struct_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.match(MiniGoParser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 357
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 358
                self.match(MiniGoParser.INTERGER_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 359
                self.match(MiniGoParser.BOOLEAN_LITERAL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 360
                self.match(MiniGoParser.NIL_LITERAL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 361
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
            self.state = 364
            self.type_()
            self.state = 365
            self.match(MiniGoParser.LBRACE)
            self.state = 366
            self.list_array_elements()
            self.state = 367
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
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.array_element()
                self.state = 370
                self.match(MiniGoParser.COMMA)
                self.state = 371
                self.list_array_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
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
        self.enterRule(localctx, 70, self.RULE_array_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
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
        self.enterRule(localctx, 72, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 379
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
        self.enterRule(localctx, 74, self.RULE_type_)
        self._la = 0 # Token type
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.list_dimention()
                self.state = 383
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
        self.enterRule(localctx, 76, self.RULE_list_dimention)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.dimention()
                self.state = 388
                self.list_dimention()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
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
        self.enterRule(localctx, 78, self.RULE_dimention)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MiniGoParser.LBRACK)
            self.state = 394
            self.match(MiniGoParser.INTERGER_LITERAL)
            self.state = 395
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
        self.enterRule(localctx, 80, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.type_()
            self.state = 398
            self.match(MiniGoParser.DOT)
            self.state = 399
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
        self.enterRule(localctx, 82, self.RULE_func_call)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 402
                self.signature()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 404
                self.match(MiniGoParser.DOT)
                self.state = 405
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 406
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
        self.enterRule(localctx, 84, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 410
            self.match(MiniGoParser.LBRACE)
            self.state = 411
            self.list_struct_elements()
            self.state = 412
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
        self.enterRule(localctx, 86, self.RULE_list_struct_elements)
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.struct_elements()
                self.state = 415
                self.match(MiniGoParser.COMMA)
                self.state = 416
                self.list_struct_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
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
        self.enterRule(localctx, 88, self.RULE_struct_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 422
            self.match(MiniGoParser.COLON)
            self.state = 423
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
        self.enterRule(localctx, 90, self.RULE_type_decl)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.interface_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
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
        self.enterRule(localctx, 92, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.TYPE)
            self.state = 430
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 431
            self.match(MiniGoParser.INTERFACE)
            self.state = 432
            self.match(MiniGoParser.LBRACE)
            self.state = 433
            self.list_menthod()
            self.state = 434
            self.match(MiniGoParser.RBRACE)
            self.state = 435
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
        self.enterRule(localctx, 94, self.RULE_list_menthod)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.menthod()
                self.state = 438
                self.end_stmt()
                self.state = 439
                self.list_menthod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.menthod()
                self.state = 442
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_menthod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenthod" ):
                return visitor.visitMenthod(self)
            else:
                return visitor.visitChildren(self)




    def menthod(self):

        localctx = MiniGoParser.MenthodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_menthod)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 448
                self.signature()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 450
                self.signature()
                self.state = 451
                self.type_()
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_field_decl(self):
            return self.getTypedRuleContext(MiniGoParser.List_field_declContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 98, self.RULE_struck_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(MiniGoParser.TYPE)
            self.state = 456
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 457
            self.match(MiniGoParser.STRUCT)
            self.state = 458
            self.match(MiniGoParser.LBRACE)
            self.state = 459
            self.list_field_decl()
            self.state = 460
            self.match(MiniGoParser.RBRACE)
            self.state = 461
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
        self.enterRule(localctx, 100, self.RULE_list_field_decl)
        try:
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.field_decl()
                self.state = 464
                self.end_stmt()
                self.state = 465
                self.list_field_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.field_decl()
                self.state = 468
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
        self.enterRule(localctx, 102, self.RULE_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 474
            self.type_()
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
        self._predicates[21] = self.list_statement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def list_statement_sempred(self, localctx:List_statementContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




