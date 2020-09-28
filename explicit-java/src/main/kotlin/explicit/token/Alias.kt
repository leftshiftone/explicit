package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*

/**
 * Token implementation which represents a token with an explicit alias.
 */
data class Alias(val alias: String, val token: IToken) : IToken {
    override fun asText() = alias
    override fun toString() = "$token:$alias"

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        val evaluation = token.evaluate(rulez, navigator)
        val entries = HashMap<String, String>()
        if (evaluation.result)
            entries[alias] = rulez.mappings[navigator.getCurr()] ?: navigator.getCurr()
        return ExplicitRuleEvaluation(evaluation.result, entries, listOf(navigator.getIndex() - 1))
    }

}
