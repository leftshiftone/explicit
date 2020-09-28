package explicit.parser

import java.util.regex.Pattern

data class ExplicitRules(val name: String,
                         val rulez: List<ExplicitRule>,
                         val labels: Map<String, String>,
                         val tokens: List<Token>,
                         val mappings: Map<String, String>,
                         val patterns: Map<String, Pattern>,
                         val features: Map<String, String>) : Iterable<ExplicitRule> {
    override fun iterator() = rulez.iterator()

    data class Token(val pattern: String, val replacement: String?, val boundary: Boolean, val regex: Boolean)
}
