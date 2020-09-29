/*
 * Copyright (c) 2016-2020, Leftshift One
 * __________________
 * [2020] Leftshift One
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

package explicit

import explicit.api.Navigator
import explicit.conversion.binding.ExplicitConversionBinding
import explicit.evaluator.ExplicitRuleEvaluator
import explicit.parser.AntlrParser
import explicit.parser.ExplicitRules

class ExplicitEngine(private val rulez: ExplicitRules) {

    fun execute(text: String): List<Map<String, Any>> {
        val result = ArrayList<Map<String, Any>>()
        val navigator = Navigator(rulez.toList())

        val indexSet = HashSet<List<Int>>()
        while (navigator.hasNext()) {
            val rule = navigator.next()
            val evaluator = ExplicitRuleEvaluator(rulez, rule)
            val evaluation = evaluator.evaluate(text, indexSet)

            if (evaluation.result) {
                // prevent duplicated results
                if (indexSet.any { a -> a.any { b -> evaluation.indices.contains(b) } }) continue
                indexSet.add(evaluation.indices)

                val localResults = ArrayList<Map<String, Any>>()
                rule.ner.forEach { entity ->
                    val localResult = HashMap<String, Any>()
                    entity.forEach { k, v ->
                        val extractor = AntlrParser().getExtractors(v)[0]
                        val variables = HashMap<String, Any>(rulez.features)
                        variables.putAll(evaluation.entries)
                        // variables.putAll(localResult)
                        localResult[k] = extractor.extract(ExplicitConversionBinding(variables))
                    }
                    localResults.add(localResult)
                }
                result.addAll(localResults)
                navigator.reset()
            }
        }
        return result
    }

}
