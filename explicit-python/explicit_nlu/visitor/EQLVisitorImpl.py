from explicit_nlu.antlr.EQLParser import EQLParser
from explicit_nlu.antlr.EQLVisitor import EQLVisitor
from explicit_nlu.token import Group, Text, Atomic, Like, Not, Wildcard, Slot, Optional, Label, Alias, Regex


class EQLVisitorImpl(EQLVisitor):

    def visitGroup(self, ctx: EQLParser.GroupContext):
        return Group(super().visitGroup(ctx))

    def visitLike(self, ctx: EQLParser.LikeContext):
        return Like(ctx.getText()[1:])

    def visitText(self, ctx: EQLParser.TextContext):
        return Text(ctx.getText())

    def visitNot_(self, ctx: EQLParser.Not_Context):
        return Not(super().visitNot_(ctx)[0])

    def visitWildcard(self, ctx: EQLParser.WildcardContext):
        return Wildcard()

    def visitOptional(self, ctx: EQLParser.OptionalContext):
        return Optional(super().visit(ctx.getChild(0)))

    def visitAlias(self, ctx: EQLParser.AliasContext):
        return Alias(ctx.getChild(2).getText(), super().visit(ctx.getChild(0)))

    def visitLabel(self, ctx: EQLParser.LabelContext):
        return Label(super().visit(ctx.getChild(1)))

    def visitSlot(self, ctx: EQLParser.SlotContext):
        return Slot(ctx.getChild(1).getText())

    def visitAtomic(self, ctx: EQLParser.AtomicContext):
        return Atomic(super().visitAtomic(ctx))

    def visitRegex(self, ctx: EQLParser.RegexContext):
        sublist = ctx.children[1:-1]
        regex = "".join(map(lambda x: x.getText(), sublist))
        return Regex(regex)

    def aggregateResult(self, aggregate, nextResult):
        array = []
        if aggregate is not None:
            array += aggregate
        if nextResult is not None:
            array += [nextResult]
        return array
