from explicit.antlr.ECLParser import ECLParser
from explicit.antlr.ECLVisitor import ECLVisitor
from explicit.extractor.BooleanExtractor import BooleanExtractor
from explicit.extractor.FunctionExtractor import FunctionExtractor
from explicit.extractor.NumberExtractor import NumberExtractor
from explicit.extractor.StringExtractor import StringExtractor
from explicit.extractor.VariableExtractor import VariableExtractor


class ECLVisitorImpl(ECLVisitor):

    def visitString(self, ctx: ECLParser.StringContext):
        return StringExtractor(ctx.getText())

    def visitNumber(self, ctx: ECLParser.NumberContext):
        return NumberExtractor(float(ctx.getText()))

    def visitBool_(self, ctx: ECLParser.Bool_Context):
        return BooleanExtractor(ctx.getText() == "true")

    def visitVariable(self, ctx: ECLParser.VariableContext):
        return VariableExtractor(ctx.getChild(1).getText())

    def visitFunction(self, ctx: ECLParser.FunctionContext):
        args = [item for sublist in super().visitFunction(ctx) for item in sublist]
        return FunctionExtractor(ctx.getChild(0).getText(), args)

    def aggregateResult(self, aggregate, nextResult):
        array = []
        if aggregate is not None:
            array += aggregate
        if nextResult is not None:
            array += [nextResult]
        return array
