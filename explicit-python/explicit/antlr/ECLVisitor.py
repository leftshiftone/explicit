# Generated from ECL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ECLParser import ECLParser
else:
    from ECLParser import ECLParser

# This class defines a complete generic visitor for a parse tree produced by ECLParser.

class ECLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ECLParser#extractor.
    def visitExtractor(self, ctx:ECLParser.ExtractorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#string.
    def visitString(self, ctx:ECLParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#number.
    def visitNumber(self, ctx:ECLParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#bool_.
    def visitBool_(self, ctx:ECLParser.Bool_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#variable.
    def visitVariable(self, ctx:ECLParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#function.
    def visitFunction(self, ctx:ECLParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#argument.
    def visitArgument(self, ctx:ECLParser.ArgumentContext):
        return self.visitChildren(ctx)



del ECLParser