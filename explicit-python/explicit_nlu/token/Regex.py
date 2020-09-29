import logging
import re
from dataclasses import dataclass
from typing import List, Dict

from explicit_nlu.api import IToken, Navigator
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules


@dataclass
class RegexUnit:
    index: int
    token: str


@dataclass
class Regex(IToken):
    pattern: str

    def __str__(self):
        return "`" + self.pattern + "`"

    def __repr__(self):
        return self.__str__()

    def as_text(self):
        return self.pattern

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate regex")

        tuples: List[RegexUnit] = [RegexUnit(navigator.get_absolute_index() - 1, navigator.get_curr())]

        pattern = re.compile(self.pattern)
        entries: Dict[str, str] = dict()

        text = "".join(map(lambda x: x.token, tuples))
        result = re.search(pattern, text)

        if result:
            entries["group"] = result.group()
            return ExplicitEvaluation(True, entries, [navigator.get_absolute_index() - 1])

        while navigator.has_next():
            navigator.__next__()
            tuples.append(RegexUnit(navigator.get_absolute_index() - 1, navigator.get_curr()))

            text = "".join(map(lambda x: x.token, tuples))
            result = re.search(pattern, text)

            if result:
                for i in reversed(range(len(tuples))):
                    substr = "".join(map(lambda x: x.token, tuples[i:]))
                    result = re.search(pattern, text)

                    if result:
                        if result.pos == 0 and substr[result.pos - 1] == ' ':
                            entries["group"] = result.group()
                            return ExplicitEvaluation(True, entries, list(map(lambda x: x.index, tuples[i:])))

        return ExplicitEvaluation(False, entries, [])
