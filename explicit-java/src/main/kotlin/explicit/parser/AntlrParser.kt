package explicit.parser

import explicit.antlr.ECLLexer
import explicit.antlr.ECLParser
import explicit.antlr.EQLLexer
import explicit.antlr.EQLParser
import explicit.api.IConversion
import explicit.api.IToken
import explicit.listener.ExplicitRulesErrorListener
import explicit.visitor.ExplicitCodeVisitor
import explicit.visitor.ExplicitRuleVisitor
import org.antlr.v4.runtime.CharStreams
import org.antlr.v4.runtime.CommonTokenStream

class AntlrParser {

    fun getTokens(str:String):List<IToken> {
        val errorListener = ExplicitRulesErrorListener()

        val charStream = CharStreams.fromString(str)
        val lexer = EQLLexer(charStream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(errorListener)

        val commonTokenStream = CommonTokenStream(lexer)
        val parser = EQLParser(commonTokenStream)
        parser.removeErrorListeners()
        parser.addErrorListener(errorListener)

        val visitor = ExplicitRuleVisitor()
        val tokens = visitor.visit(parser.token())

        if (errorListener.get() != null) {
            throw RuntimeException(str + ": " + errorListener.get())
        }

        return tokens
    }

    fun getExtractors(str:String):List<IConversion> {
        val errorListener = ExplicitRulesErrorListener()

        val charStream = CharStreams.fromString(str)
        val lexer = ECLLexer(charStream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(errorListener)

        val commonTokenStream = CommonTokenStream(lexer)
        val parser = ECLParser(commonTokenStream)
        parser.removeErrorListeners()
        parser.addErrorListener(errorListener)

        val visitor = ExplicitCodeVisitor()
        val extractors = visitor.visit(parser.extractor())

        if (errorListener.get() != null) {
            throw RuntimeException(str + ": " + errorListener.get())
        }

        return extractors
    }

}
