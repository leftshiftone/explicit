import logging
from dataclasses import dataclass

from explicit_nlu.api import IToken, Navigator
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules


#
# Token implementation which represents a fuzzy text.
#
@dataclass
class Like(IToken):
    text: str

    def __str__(self):
        return "~" + self.text

    def __repr__(self):
        return self.__str__()

    def as_text(self):
        return self.text

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate like")

        if abs(len(self.as_text()) - len(navigator.get_curr())) > 1:
            return ExplicitEvaluation(False, dict(), [navigator.get_absolute_index() - 1])

        result = self.levenshtein(self.as_text(), navigator.get_curr()) <= 1
        return ExplicitEvaluation(result, dict(), [navigator.get_absolute_index() - 1])

    # TODO: use library
    def levenshtein(self, a: str, b: str):
        a = a.lower()
        b = b.lower()
        if not a: return len(b)
        if not b: return len(a)
        return min(self.levenshtein(a[1:], b[1:]) + (a[0] != b[0]),
                   self.levenshtein(a[1:], b) + 1,
                   self.levenshtein(a, b[1:]) + 1)
