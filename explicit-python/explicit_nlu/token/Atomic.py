import logging
from dataclasses import dataclass
from typing import List

from explicit_nlu.api import IToken, Navigator
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules


#
# Token implementation which represents a group of tokens which build an atomic unit.
#
@dataclass
class Atomic(IToken):
    tokens: List[IToken]

    def __str__(self):
        return " ".join(list(map(IToken.as_text, self.tokens)))

    def __repr__(self):
        return self.__str__()

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate atomic")

        for i, entry in enumerate(self.tokens):
            result = entry.evaluate(rulez, navigator)

            if not result.result:
                return ExplicitEvaluation(False, dict(), [navigator.get_absolute_index() - 1])

            if i < len(self.tokens) - 1:
                navigator.__next__()

        return ExplicitEvaluation(True, dict(), [navigator.get_absolute_index() - 1])
