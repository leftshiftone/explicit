# Generated from ECL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("W\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4+\n\4\3\5\3\5\3\6\3\6\7\6\61\n\6\f\6\16\6\64\13")
        buf.write("\6\3\6\3\6\3\7\6\79\n\7\r\7\16\7:\3\b\3\b\3\t\3\t\7\t")
        buf.write("A\n\t\f\t\16\tD\13\t\3\n\5\nG\n\n\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\6\16R\n\16\r\16\16\16S\3\16\3\16\2")
        buf.write("\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\2\25\2\27")
        buf.write("\2\31\2\33\13\3\2\7\3\2\62;\4\2C\\c|\6\2\62;C\\aac|\3")
        buf.write("\2$$\5\2\13\f\16\17\"\"\2X\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2")
        buf.write("\2\7*\3\2\2\2\t,\3\2\2\2\13.\3\2\2\2\r8\3\2\2\2\17<\3")
        buf.write("\2\2\2\21>\3\2\2\2\23F\3\2\2\2\25J\3\2\2\2\27L\3\2\2\2")
        buf.write("\31N\3\2\2\2\33Q\3\2\2\2\35\36\7*\2\2\36\4\3\2\2\2\37")
        buf.write(" \7+\2\2 \6\3\2\2\2!\"\7v\2\2\"#\7t\2\2#$\7w\2\2$+\7g")
        buf.write("\2\2%&\7h\2\2&\'\7c\2\2\'(\7n\2\2()\7u\2\2)+\7g\2\2*!")
        buf.write("\3\2\2\2*%\3\2\2\2+\b\3\2\2\2,-\7.\2\2-\n\3\2\2\2.\62")
        buf.write("\7$\2\2/\61\5\31\r\2\60/\3\2\2\2\61\64\3\2\2\2\62\60\3")
        buf.write("\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64\62\3\2\2\2\65\66")
        buf.write("\7$\2\2\66\f\3\2\2\2\679\t\2\2\28\67\3\2\2\29:\3\2\2\2")
        buf.write(":8\3\2\2\2:;\3\2\2\2;\16\3\2\2\2<=\7&\2\2=\20\3\2\2\2")
        buf.write(">B\5\25\13\2?A\5\27\f\2@?\3\2\2\2AD\3\2\2\2B@\3\2\2\2")
        buf.write("BC\3\2\2\2C\22\3\2\2\2DB\3\2\2\2EG\7/\2\2FE\3\2\2\2FG")
        buf.write("\3\2\2\2GH\3\2\2\2HI\t\2\2\2I\24\3\2\2\2JK\t\3\2\2K\26")
        buf.write("\3\2\2\2LM\t\4\2\2M\30\3\2\2\2NO\n\5\2\2O\32\3\2\2\2P")
        buf.write("R\t\6\2\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TU\3")
        buf.write("\2\2\2UV\b\16\2\2V\34\3\2\2\2\t\2*\62:BFS\3\b\2\2")
        return buf.getvalue()


class ECLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ROUND_LEFT = 1
    ROUND_RIGHT = 2
    BOOLEAN = 3
    COMMA = 4
    STRING = 5
    NUMBER = 6
    DOLLAR = 7
    IDENTIFIER = 8
    WHITESPACE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "'$'" ]

    symbolicNames = [ "<INVALID>",
            "ROUND_LEFT", "ROUND_RIGHT", "BOOLEAN", "COMMA", "STRING", "NUMBER", 
            "DOLLAR", "IDENTIFIER", "WHITESPACE" ]

    ruleNames = [ "ROUND_LEFT", "ROUND_RIGHT", "BOOLEAN", "COMMA", "STRING", 
                  "NUMBER", "DOLLAR", "IDENTIFIER", "Digit", "Letter", "LetterOrDigit", 
                  "StringCharacter", "WHITESPACE" ]

    grammarFileName = "ECL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


