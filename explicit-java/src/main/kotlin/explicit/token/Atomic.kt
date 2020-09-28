package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*

/**
 * Token implementation which represents a group of tokens which build an atomic unit.
 */
data class Atomic(val tokens: List<IToken>): IToken {
    override fun toString() = "(${tokens.map(IToken::asText).joinToString(" ")})"

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        val iterator = tokens.iterator()
        while (iterator.hasNext()) {
            val result = iterator.next().evaluate(rulez, navigator)
            if (!result.result) {
                return ExplicitRuleEvaluation(false, HashMap(), listOf(navigator.getIndex() - 1))
            }
            if (iterator.hasNext()) {
                navigator.next()
            }
        }
        return ExplicitRuleEvaluation(true, HashMap(), listOf(navigator.getIndex() - 1))
    }
}
