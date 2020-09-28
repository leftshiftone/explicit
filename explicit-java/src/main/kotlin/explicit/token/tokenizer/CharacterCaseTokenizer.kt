package explicit.token.tokenizer

import explicit.api.extension.getAndReset
import explicit.parser.ExplicitRules
import java.io.CharArrayWriter
import java.util.concurrent.atomic.AtomicReference

class CharacterCaseTokenizer {

    fun tokenize(str: String, tokens: List<ExplicitRules.Token> = emptyList()): List<String> {
        return str.toLowerCase().split(" ").flatMap { e ->
            for (token in tokens) {
                if (!token.regex && token.pattern == e) {
                    return@flatMap (token.replacement ?: e).split(" ")
                }
                if (token.regex) {
                    val regex = token.pattern.toRegex()
                    val result = regex.find(e)
                    val isBoundary = str.endsWith(e)

                    if (result != null && (token.boundary || !isBoundary)) {
                        val list = ArrayList<String>()
                        if (result.range.first > 0) list.addAll(tokenize(e.substring(0, result.range.first), tokens))
                        if (result.groupValues.size > 1)
                            list.addAll(result.groupValues.takeLast(result.groupValues.size - 1))
                        else
                            list.addAll(listOf(result.groupValues[0]))

                        if (e.length > (result.range.last + 1)) {
                            list.add(e.substring(result.range.last + 1))
                        }
                        return@flatMap list
                    }
                }
            }
            map(e)
        }
    }

    private fun map(str: String): List<String> {
        val result = ArrayList<String>()
        val writer = CharArrayWriter()

        val type = AtomicReference<TokenType>()
        str.toCharArray().map { it.toInt() }.forEach { c ->
            when (type.get()) {
                null -> writer.write(c)
                TokenType.toType(c) -> when (type.get()) {
                    TokenType.SPECIAL -> result.add(writer.getAndReset(c))
                    else -> writer.write(c)
                }
                else -> result.add(writer.getAndReset(c))
            }
            type.set(TokenType.toType(c))
        }
        if (writer.size() > 0) result.add(writer.toString())
        return result
    }

    private enum class TokenType {
        TEXT, NUMBER, SPECIAL;

        companion object {
            fun toType(char: Int): TokenType {
                return when {
                    Character.isAlphabetic(char) -> TEXT
                    Character.isDigit(char) -> NUMBER
                    else -> SPECIAL
                }
            }
        }
    }

}
