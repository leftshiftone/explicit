# Generated from ECL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ECLParser import ECLParser
else:
    from ECLParser import ECLParser

# This class defines a complete listener for a parse tree produced by ECLParser.
class ECLListener(ParseTreeListener):

    # Enter a parse tree produced by ECLParser#extractor.
    def enterExtractor(self, ctx:ECLParser.ExtractorContext):
        pass

    # Exit a parse tree produced by ECLParser#extractor.
    def exitExtractor(self, ctx:ECLParser.ExtractorContext):
        pass


    # Enter a parse tree produced by ECLParser#string.
    def enterString(self, ctx:ECLParser.StringContext):
        pass

    # Exit a parse tree produced by ECLParser#string.
    def exitString(self, ctx:ECLParser.StringContext):
        pass


    # Enter a parse tree produced by ECLParser#number.
    def enterNumber(self, ctx:ECLParser.NumberContext):
        pass

    # Exit a parse tree produced by ECLParser#number.
    def exitNumber(self, ctx:ECLParser.NumberContext):
        pass


    # Enter a parse tree produced by ECLParser#bool_.
    def enterBool_(self, ctx:ECLParser.Bool_Context):
        pass

    # Exit a parse tree produced by ECLParser#bool_.
    def exitBool_(self, ctx:ECLParser.Bool_Context):
        pass


    # Enter a parse tree produced by ECLParser#variable.
    def enterVariable(self, ctx:ECLParser.VariableContext):
        pass

    # Exit a parse tree produced by ECLParser#variable.
    def exitVariable(self, ctx:ECLParser.VariableContext):
        pass


    # Enter a parse tree produced by ECLParser#function.
    def enterFunction(self, ctx:ECLParser.FunctionContext):
        pass

    # Exit a parse tree produced by ECLParser#function.
    def exitFunction(self, ctx:ECLParser.FunctionContext):
        pass


    # Enter a parse tree produced by ECLParser#argument.
    def enterArgument(self, ctx:ECLParser.ArgumentContext):
        pass

    # Exit a parse tree produced by ECLParser#argument.
    def exitArgument(self, ctx:ECLParser.ArgumentContext):
        pass



del ECLParser