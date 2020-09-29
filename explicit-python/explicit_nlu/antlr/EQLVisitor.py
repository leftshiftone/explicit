# Generated from EQL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EQLParser import EQLParser
else:
    from EQLParser import EQLParser

# This class defines a complete generic visitor for a parse tree produced by EQLParser.

class EQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EQLParser#token.
    def visitToken(self, ctx:EQLParser.TokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#escaped.
    def visitEscaped(self, ctx:EQLParser.EscapedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#group.
    def visitGroup(self, ctx:EQLParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#like.
    def visitLike(self, ctx:EQLParser.LikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#text.
    def visitText(self, ctx:EQLParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#not_.
    def visitNot_(self, ctx:EQLParser.Not_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#wildcard.
    def visitWildcard(self, ctx:EQLParser.WildcardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#optional.
    def visitOptional(self, ctx:EQLParser.OptionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#alias.
    def visitAlias(self, ctx:EQLParser.AliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#label.
    def visitLabel(self, ctx:EQLParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#slot.
    def visitSlot(self, ctx:EQLParser.SlotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#atomic.
    def visitAtomic(self, ctx:EQLParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EQLParser#regex.
    def visitRegex(self, ctx:EQLParser.RegexContext):
        return self.visitChildren(ctx)



del EQLParser