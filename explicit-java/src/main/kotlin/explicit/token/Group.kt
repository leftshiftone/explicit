package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.api.extension.getLevenshteinDistance
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*
import java.util.concurrent.atomic.AtomicBoolean

/**
 * Token implementation which represents a group of tokens.
 */
data class Group(val tokens: List<IToken>): IToken {
    override fun toString() = "[${tokens.map(IToken::asText).joinToString(" ")}]"

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        val whitelist = AtomicBoolean(false)
        for (groupToken in tokens) {
            if (groupToken !is Not) {
                whitelist.set(true)
            }
            if (groupToken.asText().equals(navigator.getCurr(), ignoreCase = true)) {
                val evaluation = groupToken !is Not
                return ExplicitRuleEvaluation(evaluation, HashMap(), listOf(navigator.getIndex() - 1))
            }
            if (groupToken is Like) {
                if (groupToken.asText().toLowerCase().getLevenshteinDistance(navigator.getCurr().toLowerCase()) <= 1) {
                    return ExplicitRuleEvaluation(true, HashMap(), listOf(navigator.getIndex() - 1))
                }
            }
        }
        return ExplicitRuleEvaluation(!whitelist.get(), HashMap(), listOf(navigator.getIndex() - 1))
    }
}
