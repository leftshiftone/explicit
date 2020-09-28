package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*

/**
 * Token implementation which represents a wildcard.
 */
class Wildcard: IToken {
    override fun toString() = "*"

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        return ExplicitRuleEvaluation(false, HashMap(), ArrayList())
    }
}
