from dataclasses import dataclass
from typing import Dict, List

from explicit_nlu.api import IToken
from explicit_nlu.api.Navigator import Navigator
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules, ExplicitRule
from explicit_nlu.token import Wildcard, Not, Alias, Optional
from explicit_nlu.token.tokenizer import CharacterCaseTokenizer


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
        wildcard_collection = False

        rule_nav = Navigator(self.rule.rule)
        text_nav = Navigator(CharacterCaseTokenizer().tokenize(text, self.rulez.tokens))

        entries:Dict[str, str] = dict()
        negations:List[IToken] = []
        indices:List[int] = []
        wildcard_collector: Dict[str, List[str]] = {}

        while rule_nav.has_next():
            token = rule_nav.__next__()
            is_optional = isinstance(token, Optional) or (isinstance(token, Alias) and isinstance(token.token, Optional))

            if isinstance(token, Wildcard):
                wildcard = True
                continue

            if isinstance(token, Alias) and isinstance(token.token, Wildcard):
                if not rule_nav.has_next():
                    collector = []
                    while text_nav.has_next():
                        text_nav.__next__()
                        collector.append(text_nav.get_curr())
                        indices.append(text_nav.get_index())
                    entries[token.alias] = " ".join(collector)
                wildcard = True
                wildcard_collection = True
                continue

            if isinstance(token, Not):
                negations.append(token.token)
                continue

            if not text_nav.has_next():
                if is_optional:
                    continue
                return ExplicitEvaluation(False, entries, list())

            while text_nav.has_next():
                text_nav.__next__()

                is_negated = len(list(filter(lambda x: x.evaluate(self.rulez, text_nav).result, negations))) > 0

                if is_negated:
                    return ExplicitEvaluation(False, entries, list())

                evaluation = token.evaluate(self.rulez, text_nav)

                # navigate optionals during wildcard search
                if wildcard_collection and is_optional and not evaluation.result:
                    curr_index = rule_nav.index
                    stop_wildcard_collection = False
                    _token = token
                    while isinstance(_token, Optional):
                        _token = rule_nav.__next__()
                        _evaluation = _token.evaluate(self.rulez, text_nav)

                        if _evaluation.result:
                            token = _token
                            evaluation = _evaluation
                            stop_wildcard_collection = True

                    # reset index if the wildcard matches the token
                    if not stop_wildcard_collection:
                        rule_nav.index = curr_index

                if self.contains_any(excludes, evaluation.indices):
                    candidate = False
                    rule_nav.reset()
                    break

                entries.update(evaluation.entries)
                (result, _, indices1) = evaluation
                candidate = candidate or result

                if result:
                    wildcard = False
                    wildcard_collection = False

                    for key in wildcard_collector:
                        entries[key] = " ".join(wildcard_collector[key])

                    if len(self.rule.idx) == 0 or (rule_nav.get_index() - 1) in self.rule.idx:
                        indices.extend(indices1)
                    break

                if not result and is_optional and not wildcard_collection:
                    text_nav.prev()
                    break

                if not result and not wildcard:
                    # check how much words are remaining and reset the first navigator
                    if text_nav.get_remaining() >= rule_nav.get_remaining() and not is_negated:
                        candidate = False
                        rule_nav.reset()
                        indices.clear()
                        entries.clear()
                        break
                    return ExplicitEvaluation(False, entries, list())

                if not result and wildcard_collection:
                    # noinspection PyUnresolvedReferences
                    prev = rule_nav.get_prev()
                    if isinstance(prev, Alias):
                        alias = prev.alias
                        if alias not in wildcard_collector:
                            wildcard_collector[alias] = []
                        wildcard_collector[alias].append(text_nav.get_curr())

        return ExplicitEvaluation(candidate, entries, indices)

    def contains_any(self, list1:List[List[int]], list2:List[int]):
        for element1 in list1:
            for element2 in list2:
                if element2 in element1:
                    return True
        return False