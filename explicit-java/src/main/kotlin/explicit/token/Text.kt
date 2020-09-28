package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*

/**
 * Token implementation which represents a simple text.
 */
data class Text(val text: String): IToken {
    override fun toString() = text

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        return ExplicitRuleEvaluation(toString() == navigator.getCurr(), HashMap(), listOf(navigator.getIndex() - 1))
    }
}
