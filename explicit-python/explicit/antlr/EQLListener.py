# Generated from EQL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EQLParser import EQLParser
else:
    from EQLParser import EQLParser

# This class defines a complete listener for a parse tree produced by EQLParser.
class EQLListener(ParseTreeListener):

    # Enter a parse tree produced by EQLParser#token.
    def enterToken(self, ctx:EQLParser.TokenContext):
        pass

    # Exit a parse tree produced by EQLParser#token.
    def exitToken(self, ctx:EQLParser.TokenContext):
        pass


    # Enter a parse tree produced by EQLParser#escaped.
    def enterEscaped(self, ctx:EQLParser.EscapedContext):
        pass

    # Exit a parse tree produced by EQLParser#escaped.
    def exitEscaped(self, ctx:EQLParser.EscapedContext):
        pass


    # Enter a parse tree produced by EQLParser#group.
    def enterGroup(self, ctx:EQLParser.GroupContext):
        pass

    # Exit a parse tree produced by EQLParser#group.
    def exitGroup(self, ctx:EQLParser.GroupContext):
        pass


    # Enter a parse tree produced by EQLParser#like.
    def enterLike(self, ctx:EQLParser.LikeContext):
        pass

    # Exit a parse tree produced by EQLParser#like.
    def exitLike(self, ctx:EQLParser.LikeContext):
        pass


    # Enter a parse tree produced by EQLParser#text.
    def enterText(self, ctx:EQLParser.TextContext):
        pass

    # Exit a parse tree produced by EQLParser#text.
    def exitText(self, ctx:EQLParser.TextContext):
        pass


    # Enter a parse tree produced by EQLParser#not_.
    def enterNot_(self, ctx:EQLParser.Not_Context):
        pass

    # Exit a parse tree produced by EQLParser#not_.
    def exitNot_(self, ctx:EQLParser.Not_Context):
        pass


    # Enter a parse tree produced by EQLParser#wildcard.
    def enterWildcard(self, ctx:EQLParser.WildcardContext):
        pass

    # Exit a parse tree produced by EQLParser#wildcard.
    def exitWildcard(self, ctx:EQLParser.WildcardContext):
        pass


    # Enter a parse tree produced by EQLParser#optional.
    def enterOptional(self, ctx:EQLParser.OptionalContext):
        pass

    # Exit a parse tree produced by EQLParser#optional.
    def exitOptional(self, ctx:EQLParser.OptionalContext):
        pass


    # Enter a parse tree produced by EQLParser#alias.
    def enterAlias(self, ctx:EQLParser.AliasContext):
        pass

    # Exit a parse tree produced by EQLParser#alias.
    def exitAlias(self, ctx:EQLParser.AliasContext):
        pass


    # Enter a parse tree produced by EQLParser#label.
    def enterLabel(self, ctx:EQLParser.LabelContext):
        pass

    # Exit a parse tree produced by EQLParser#label.
    def exitLabel(self, ctx:EQLParser.LabelContext):
        pass


    # Enter a parse tree produced by EQLParser#slot.
    def enterSlot(self, ctx:EQLParser.SlotContext):
        pass

    # Exit a parse tree produced by EQLParser#slot.
    def exitSlot(self, ctx:EQLParser.SlotContext):
        pass


    # Enter a parse tree produced by EQLParser#atomic.
    def enterAtomic(self, ctx:EQLParser.AtomicContext):
        pass

    # Exit a parse tree produced by EQLParser#atomic.
    def exitAtomic(self, ctx:EQLParser.AtomicContext):
        pass


    # Enter a parse tree produced by EQLParser#regex.
    def enterRegex(self, ctx:EQLParser.RegexContext):
        pass

    # Exit a parse tree produced by EQLParser#regex.
    def exitRegex(self, ctx:EQLParser.RegexContext):
        pass



del EQLParser