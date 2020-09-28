package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules

/**
 * Token implementation which represents an optional token.
 */
data class Optional(val token: IToken): IToken {
    override fun toString() = "$token?"
    override fun asText() = token.asText()

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        return token.evaluate(rulez, navigator)
    }
}
