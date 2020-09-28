from dataclasses import dataclass
from typing import Dict, List

from explicit.api import IToken
from explicit.api.Navigator import Navigator
from explicit.evaluator import ExplicitEvaluation
from explicit.parser import ExplicitRules, ExplicitRule
from explicit.token import Wildcard, Not, Alias, Optional
from explicit.token.tokenizer import CharacterCaseTokenizer


@dataclass
class ExplicitEvaluator:
    rulez: ExplicitRules
    rule: ExplicitRule

    def evaluate(self, text: str, excludes: List[List[int]] = []) -> ExplicitEvaluation:
        if len(list(filter(lambda x: not isinstance(x, Wildcard), self.rule.rule))) is 0:
            return ExplicitEvaluation(True, dict(), list())

        token_count = len(list(filter(lambda x: not isinstance(x, Wildcard) and not isinstance(x, Not), self.rule.rule)))
        wildcard = False
        candidate = False

        text_nav = Navigator(self.rule.rule)
        rule_nav = Navigator(CharacterCaseTokenizer().tokenize(text, self.rulez.tokens))

        entries:Dict[str, str] = dict()
        negations:List[IToken] = []
        indices:List[int] = []

        while text_nav.has_next():
            token = text_nav.__next__()
            is_optional = isinstance(token, Optional) or (isinstance(token, Alias) and isinstance(token.token, Optional))

            if isinstance(token, Wildcard):
                wildcard = True
                continue

            if isinstance(token, Not):
                negations.append(token.token)
                continue

            if not rule_nav.has_next():
                if is_optional:
                    continue
                return ExplicitEvaluation(False, entries, list())

            while rule_nav.has_next():
                rule_nav.__next__()

                is_negated = len(list(filter(lambda x: x.evaluate(self.rulez, rule_nav).result, negations))) > 0

                if is_negated:
                    return ExplicitEvaluation(False, entries, list())

                evaluation = token.evaluate(self.rulez, rule_nav)

                if self.contains_any(excludes, evaluation.indices):
                    candidate = False
                    text_nav.reset()
                    break

                entries.update(evaluation.entries)
                (result, _, indices1) = evaluation
                candidate = candidate or result

                if result:
                    wildcard = False
                    if len(self.rule.idx) == 0 or (text_nav.get_index() - 1) in self.rule.idx:
                        indices.extend(indices1)
                    break

                if not result and is_optional:
                    rule_nav.prev()
                    break

                if not result and not wildcard:
                    #check how much words are remaining and reset the first navigator
                    if rule_nav.get_remaining() >= token_count - 1 and not is_negated:
                        candidate = False
                        text_nav.reset()
                        break
                    return ExplicitEvaluation(False, entries, list())

        return ExplicitEvaluation(candidate, entries, indices)

    def contains_any(self, list1:List[List[int]], list2:List[int]):
        for element1 in list1:
            for element2 in list2:
                if element2 in element1:
                    return True
        return False