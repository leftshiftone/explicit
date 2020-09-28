package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*

/**
 * Token implementation which represents a token with an escaped text.
 */
data class Escaped(val str: String) : IToken {
    override fun toString() = str

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        return ExplicitRuleEvaluation(toString() == navigator.getCurr(), HashMap(), listOf(navigator.getIndex() - 1))
    }
}
