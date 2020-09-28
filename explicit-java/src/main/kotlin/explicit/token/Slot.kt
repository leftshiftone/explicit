package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.api.extension.isNumeric
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*

/**
 * Token implementation which represents a ner slot.
 */
data class Slot(val slot: String): IToken {
    override fun toString() = "{$slot}"
    override fun asText() = slot

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        val expr1 = toString().equals(navigator.getCurr(), true)
        val expr2 = asText() == "number" && navigator.getCurr().isNumeric()
        val expr3 = evaluatePattern(rulez, navigator.getCurr())
        val expr4 = evaluateMapping(rulez, navigator.getCurr())

        val evaluation = expr1 || expr2 || expr3 || expr4
        return ExplicitRuleEvaluation(evaluation, HashMap(), listOf(navigator.getIndex() - 1))
    }

    private fun evaluatePattern(rulez: ExplicitRules, atomic: String): Boolean {
        if (rulez.patterns.containsKey(asText())) {
            val matcher = rulez.patterns[asText()]!!.matcher(atomic)
            if (matcher.find()) {
                return atomic.length == matcher.end()
            }
        }
        return false
    }

    private fun evaluateMapping(rulez: ExplicitRules, atomic: String): Boolean {
        if (rulez.mappings.containsKey(atomic)) {
            when (asText()) {
                "number" -> return rulez.mappings[atomic]?.isNumeric() ?: false
            }
        }
        return false
    }
}
