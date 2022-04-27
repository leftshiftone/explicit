# Generated from ECL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\7\7*\n\7\f\7\16\7-\13\7\5\7/\n\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\5\b8\n\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2=")
        buf.write("\2\25\3\2\2\2\4\33\3\2\2\2\6\35\3\2\2\2\b\37\3\2\2\2\n")
        buf.write("!\3\2\2\2\f$\3\2\2\2\16\67\3\2\2\2\20\26\5\4\3\2\21\26")
        buf.write("\5\6\4\2\22\26\5\b\5\2\23\26\5\n\6\2\24\26\5\f\7\2\25")
        buf.write("\20\3\2\2\2\25\21\3\2\2\2\25\22\3\2\2\2\25\23\3\2\2\2")
        buf.write("\25\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2")
        buf.write("\2\30\31\3\2\2\2\31\32\7\2\2\3\32\3\3\2\2\2\33\34\7\7")
        buf.write("\2\2\34\5\3\2\2\2\35\36\7\b\2\2\36\7\3\2\2\2\37 \7\5\2")
        buf.write("\2 \t\3\2\2\2!\"\7\t\2\2\"#\7\n\2\2#\13\3\2\2\2$%\7\n")
        buf.write("\2\2%.\7\3\2\2&+\5\16\b\2\'(\7\6\2\2(*\5\16\b\2)\'\3\2")
        buf.write("\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,/\3\2\2\2-+\3\2\2\2")
        buf.write(".&\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60\61\7\4\2\2\61\r\3")
        buf.write("\2\2\2\628\5\4\3\2\638\5\6\4\2\648\5\b\5\2\658\5\n\6\2")
        buf.write("\668\5\f\7\2\67\62\3\2\2\2\67\63\3\2\2\2\67\64\3\2\2\2")
        buf.write("\67\65\3\2\2\2\67\66\3\2\2\28\17\3\2\2\2\7\25\27+.\67")
        return buf.getvalue()


class ECLParser ( Parser ):

    grammarFileName = "ECL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "','", "<INVALID>", 
                     "<INVALID>", "'$'" ]

    symbolicNames = [ "<INVALID>", "ROUND_LEFT", "ROUND_RIGHT", "BOOLEAN", 
                      "COMMA", "STRING", "NUMBER", "DOLLAR", "IDENTIFIER", 
                      "WHITESPACE" ]

    RULE_extractor = 0
    RULE_string = 1
    RULE_number = 2
    RULE_bool_ = 3
    RULE_variable = 4
    RULE_function = 5
    RULE_argument = 6

    ruleNames =  [ "extractor", "string", "number", "bool_", "variable", 
                   "function", "argument" ]

    EOF = Token.EOF
    ROUND_LEFT=1
    ROUND_RIGHT=2
    BOOLEAN=3
    COMMA=4
    STRING=5
    NUMBER=6
    DOLLAR=7
    IDENTIFIER=8
    WHITESPACE=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExtractorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ECLParser.EOF, 0)

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.StringContext)
            else:
                return self.getTypedRuleContext(ECLParser.StringContext,i)


        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.NumberContext)
            else:
                return self.getTypedRuleContext(ECLParser.NumberContext,i)


        def bool_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.Bool_Context)
            else:
                return self.getTypedRuleContext(ECLParser.Bool_Context,i)


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.VariableContext)
            else:
                return self.getTypedRuleContext(ECLParser.VariableContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.FunctionContext)
            else:
                return self.getTypedRuleContext(ECLParser.FunctionContext,i)


        def getRuleIndex(self):
            return ECLParser.RULE_extractor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtractor" ):
                listener.enterExtractor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtractor" ):
                listener.exitExtractor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtractor" ):
                return visitor.visitExtractor(self)
            else:
                return visitor.visitChildren(self)




    def extractor(self):

        localctx = ECLParser.ExtractorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_extractor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ECLParser.STRING]:
                    self.state = 14
                    self.string()
                    pass
                elif token in [ECLParser.NUMBER]:
                    self.state = 15
                    self.number()
                    pass
                elif token in [ECLParser.BOOLEAN]:
                    self.state = 16
                    self.bool_()
                    pass
                elif token in [ECLParser.DOLLAR]:
                    self.state = 17
                    self.variable()
                    pass
                elif token in [ECLParser.IDENTIFIER]:
                    self.state = 18
                    self.function()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECLParser.BOOLEAN) | (1 << ECLParser.STRING) | (1 << ECLParser.NUMBER) | (1 << ECLParser.DOLLAR) | (1 << ECLParser.IDENTIFIER))) != 0)):
                    break

            self.state = 23
            self.match(ECLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ECLParser.STRING, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = ECLParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(ECLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ECLParser.NUMBER, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = ECLParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(ECLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(ECLParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_bool_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_" ):
                listener.enterBool_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_" ):
                listener.exitBool_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_" ):
                return visitor.visitBool_(self)
            else:
                return visitor.visitChildren(self)




    def bool_(self):

        localctx = ECLParser.Bool_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bool_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(ECLParser.BOOLEAN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(ECLParser.DOLLAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ECLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = ECLParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ECLParser.DOLLAR)
            self.state = 32
            self.match(ECLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ECLParser.IDENTIFIER, 0)

        def ROUND_LEFT(self):
            return self.getToken(ECLParser.ROUND_LEFT, 0)

        def ROUND_RIGHT(self):
            return self.getToken(ECLParser.ROUND_RIGHT, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ECLParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ECLParser.COMMA)
            else:
                return self.getToken(ECLParser.COMMA, i)

        def getRuleIndex(self):
            return ECLParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ECLParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ECLParser.IDENTIFIER)
            self.state = 35
            self.match(ECLParser.ROUND_LEFT)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECLParser.BOOLEAN) | (1 << ECLParser.STRING) | (1 << ECLParser.NUMBER) | (1 << ECLParser.DOLLAR) | (1 << ECLParser.IDENTIFIER))) != 0):
                self.state = 36
                self.argument()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ECLParser.COMMA:
                    self.state = 37
                    self.match(ECLParser.COMMA)
                    self.state = 38
                    self.argument()
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 46
            self.match(ECLParser.ROUND_RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(ECLParser.StringContext,0)


        def number(self):
            return self.getTypedRuleContext(ECLParser.NumberContext,0)


        def bool_(self):
            return self.getTypedRuleContext(ECLParser.Bool_Context,0)


        def variable(self):
            return self.getTypedRuleContext(ECLParser.VariableContext,0)


        def function(self):
            return self.getTypedRuleContext(ECLParser.FunctionContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ECLParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ECLParser.STRING]:
                self.state = 48
                self.string()
                pass
            elif token in [ECLParser.NUMBER]:
                self.state = 49
                self.number()
                pass
            elif token in [ECLParser.BOOLEAN]:
                self.state = 50
                self.bool_()
                pass
            elif token in [ECLParser.DOLLAR]:
                self.state = 51
                self.variable()
                pass
            elif token in [ECLParser.IDENTIFIER]:
                self.state = 52
                self.function()
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





