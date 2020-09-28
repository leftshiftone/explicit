/*
 * Copyright (c) 2016-2018, Leftshift One
 * __________________
 * [2018] Leftshift One
 * All Rights Reserved.
 * NOTICE:  All information contained herein is, and remains
 * the property of Leftshift One and its suppliers,
 * if any.  The intellectual and technical concepts contained
 * herein are proprietary to Leftshift One
 * and its suppliers and may be covered by Patents,
 * patents in process, and are protected by trade secret or copyright law.
 * Dissemination of this information or reproduction of this material
 * is strictly forbidden unless prior written permission is obtained
 * from Leftshift One.
 */

package explicit.evaluator

import explicit.api.IToken
import explicit.api.Navigator
import explicit.parser.ExplicitRule
import explicit.parser.ExplicitRules
import explicit.token.Alias
import explicit.token.Not
import explicit.token.Optional
import explicit.token.Wildcard
import explicit.token.tokenizer.CharacterCaseTokenizer
import java.util.*
import java.util.concurrent.atomic.AtomicBoolean
import kotlin.collections.HashMap

class ExplicitRuleEvaluator(val rulez: ExplicitRules, val rule: ExplicitRule) {

    fun evaluate(text: String, excludes: Set<List<Int>>): ExplicitRuleEvaluation {
        if (rule.rule.all { e -> e is Wildcard })
            return ExplicitRuleEvaluation(true, HashMap(), ArrayList(HashSet()))

        // val index = excludes.map { it.last() }.max() ?: 0

        val tokenCount = rule.rule.filter { e -> e !is Wildcard && e !is Not }.count()

        val wildcard = AtomicBoolean(false)
        val candidate = AtomicBoolean(false)

        val textNav = Navigator(rule.rule)
        val ruleNav = Navigator(CharacterCaseTokenizer().tokenize(text, rulez.tokens))
        // if (index > 0)
        //     ruleNav.setIndex(index + 1)
        val entries = HashMap<String, String>()
        val negations = ArrayList<IToken>()
        val indices = ArrayList<Int>()

        while (textNav.hasNext()) {
            val token = textNav.next()
            val isOptional = token is Optional || token is Alias && token.token is Optional

            if (token is Wildcard) {
                wildcard.set(true)
                continue
            }
            if (token is Not) {
                negations.add(token.token)
                continue
            }
            if (!ruleNav.hasNext()) {
                if (isOptional)
                    continue
                return ExplicitRuleEvaluation(false, entries, ArrayList())
            }
            while (ruleNav.hasNext()) {
                ruleNav.next()
                val isNegated = negations.any { n -> n.evaluate(rulez, ruleNav).result }
                if (isNegated)
                    return ExplicitRuleEvaluation(false, entries, ArrayList())

                val evaluation = token.evaluate(rulez, ruleNav)

                if (containsAny(excludes, evaluation.indices)) {
                    candidate.set(false)
                    textNav.reset()
                    break
                }

                entries.putAll(evaluation.entries)
                val (result, _, indices1) = evaluation
                candidate.compareAndSet(false, result)

                if (result) {
                    wildcard.set(false)
                    if (rule.idx.isEmpty() || rule.idx.contains(textNav.getIndex() - 1)) {
                        indices.addAll(indices1)
                    }
                    break
                }
                if (!result && isOptional) {
                    ruleNav.prev()
                    break
                }
                if (!result && !wildcard.get()) {
                    // check how much words are remaining and reset the first navigator
                    if (ruleNav.getRemaining() >= tokenCount - 1 && !isNegated) {
                        candidate.set(false)
                        textNav.reset()
                        break
                    }
                    return ExplicitRuleEvaluation(false, entries, ArrayList())
                }
            }
        }
        return ExplicitRuleEvaluation(candidate.get(), entries, ArrayList(HashSet(indices)))
    }

    private fun containsAny(set: Set<List<Int>>, list: List<Int>): Boolean {
        for (exclude in set) {
            for (index in list) {
                if (exclude.contains(index)) {
                    return true
                }
            }
        }
        return false
    }

}
