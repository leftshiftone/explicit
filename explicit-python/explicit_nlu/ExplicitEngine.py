from dataclasses import dataclass
from typing import Dict, Any, List

from explicit_nlu.api.Navigator import Navigator
from explicit_nlu.evaluator.ExplicitEvaluator import ExplicitEvaluator
from explicit_nlu.extractor.binding.ExplicitConversionBinding import ExplicitConversionBinding
from explicit_nlu.parser import ExplicitRules
from explicit_nlu.parser.AntlrParser import AntlrParser


@dataclass
class ExplicitEngine:
    rules: ExplicitRules

    def execute(self, text: str) -> List[Dict[str, Any]]:
        result:List[Dict[str, Any]] = []
        navigator = Navigator(self.rules.rulez)

        index_set: List[List[int]] = []

        for rule in navigator:
            evaluator = ExplicitEvaluator(self.rules, rule)
            evaluation = evaluator.evaluate(text, index_set)

            if evaluation.result:
                # print("rule")
                # print(rule)

                # prevent duplicated results
                def contains_index():
                    for indices in index_set:
                        for pos in indices:
                            if pos in evaluation.indices:
                                return True
                    return False

                if contains_index():
                    continue

                index_set.append(evaluation.indices)
                local_results:List[Dict[str, Any]] = []

                for entity in rule.ner:
                    local_result: Dict[str, Any] = {}

                    for k in entity:
                        extractor = AntlrParser().get_converters(entity[k])[0]
                        variables: Dict[str, Any] = dict(self.rules.features)

                        variables.update(evaluation.entries)
                        # variables.update(local_result)

                        local_result[k] = extractor.extract(ExplicitConversionBinding(variables))
                    local_results.append(local_result)
                result.extend(local_results)
                navigator.reset()
        return result
