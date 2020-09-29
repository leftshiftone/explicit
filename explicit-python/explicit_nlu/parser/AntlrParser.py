from typing import List

from antlr4 import *

from explicit_nlu.antlr.ECLLexer import ECLLexer
from explicit_nlu.antlr.ECLParser import ECLParser
from explicit_nlu.antlr.EQLLexer import EQLLexer
from explicit_nlu.antlr.EQLParser import EQLParser
from explicit_nlu.api import IToken, IConversion
from explicit_nlu.listener.ExplicitRulesErrorListener import ExplicitRulesErrorListener
from explicit_nlu.visitor.ECLVisitorImpl import ECLVisitorImpl
from explicit_nlu.visitor.EQLVisitorImpl import EQLVisitorImpl


class AntlrParser:

    @staticmethod
    def get_tokens(script: str) -> List[IToken]:
        error_listener = ExplicitRulesErrorListener()

        lexer = EQLLexer(AntlrParser.stream(script))
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        stream = CommonTokenStream(lexer)
        parser = EQLParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        visitor = EQLVisitorImpl()
        tokens = visitor.visit(parser.token())

        if error_listener.error is not None:
            raise ValueError(script + ": " + error_listener.error)

        return tokens

    @staticmethod
    def get_converters(script: str) -> List[IConversion]:
        errorListener = ExplicitRulesErrorListener()

        lexer = ECLLexer(AntlrParser.stream(script))
        lexer.removeErrorListeners()
        lexer.addErrorListener(errorListener)

        stream = CommonTokenStream(lexer)
        parser = ECLParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(errorListener)

        visitor = ECLVisitorImpl()
        tokens = visitor.visit(parser.extractor())

        if errorListener.error is not None:
            raise ValueError(script + ": " + errorListener.error)

        return tokens

    @staticmethod
    def stream(obj):
        if isinstance(obj, InputStream):
            return obj
        if isinstance(obj, str):
            return InputStream(str(obj))
        if isinstance(obj, bytes):
            return InputStream(obj.decode("utf-8"))
        if isinstance(obj, bytearray):
            return InputStream(obj.decode("utf-8"))
        raise ValueError(str(obj) + " cannot be converted to input stream")
