package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*
import java.util.regex.Pattern

/**
 * Token implementation which represents a regex.
 */
data class Regex(val pattern: String): IToken {
    override fun toString() = "`$pattern`"
    override fun asText() = pattern

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        val pattern = Pattern.compile(asText())

        val tuples = ArrayList<Pair<Int, String>>()
        tuples.add(Pair(navigator.getIndex() - 1, navigator.getCurr()))

        val entries = HashMap<String, String>()

        var matcher = pattern!!.matcher(tuples.map { it.second }.joinToString(""))
        if (matcher.find()) {
            entries["group"] = matcher.group()
            return ExplicitRuleEvaluation(true, HashMap(), listOf(navigator.getIndex() - 1))
        }
        while (navigator.hasNext()) {
            navigator.next()
            tuples.add(Pair(navigator.getIndex() - 1, navigator.getCurr()))

            matcher = pattern.matcher(tuples.map { it.second }.joinToString(""))
            if (matcher.find()) {
                for (i in tuples.indices.reversed()) {
                    val substr = tuples.subList(i, tuples.size)
                            .map { it.second }.joinToString("")

                    matcher = pattern.matcher(substr)
                    if (matcher.find()) {
                        if (matcher.start() == 0 || substr[matcher.start() - 1] == ' ') {
                            entries["group"] = matcher.group()
                            return ExplicitRuleEvaluation(true, entries, tuples.subList(i, tuples.size)
                                    .map { it.first })
                        }
                    }
                }
            }
        }
        return ExplicitRuleEvaluation(false, entries, ArrayList())
    }
}
