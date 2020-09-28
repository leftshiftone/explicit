package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.api.extension.getLevenshteinDistance
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*

/**
 * Token implementation which represents a fuzzy text.
 */
data class Like(val token: String): IToken {
    override fun toString() = "~$token"
    override fun asText() = token

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        return ExplicitRuleEvaluation(asText().toLowerCase().getLevenshteinDistance(navigator.getCurr().toLowerCase()) <= 1, HashMap(), listOf(navigator.getIndex() - 1))
    }
}
