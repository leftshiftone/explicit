package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*

/**
 * Token implementation which represents a negated token.
 */
data class Not(val token: IToken): IToken {
    override fun toString() = "!$token"
    override fun asText() = token.asText()

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        val evaluation = token.evaluate(rulez, navigator)
        return ExplicitRuleEvaluation(!evaluation.result, HashMap(), listOf(navigator.getIndex() - 1))
    }
}
