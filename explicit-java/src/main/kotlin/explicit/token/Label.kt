package explicit.token

import explicit.api.IToken
import explicit.api.Navigator
import explicit.evaluator.ExplicitRuleEvaluation
import explicit.parser.ExplicitRules
import java.util.*

/**
 * Token implementation which represents a label. A label can be used
 * to reference a result of the ner parsing process.
 */
data class Label(val token: IToken): IToken {
    override fun toString() = "#$token"
    override fun asText() = token.asText()

    override fun evaluate(rulez: ExplicitRules, navigator: Navigator<String>): ExplicitRuleEvaluation {
        return ExplicitRuleEvaluation(asText() == rulez.labels[navigator.getCurr()], HashMap(), listOf(navigator.getIndex() - 1))
    }
}
