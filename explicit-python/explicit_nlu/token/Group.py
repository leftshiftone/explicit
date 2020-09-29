import logging
from dataclasses import dataclass
from typing import List

from explicit_nlu.api import IToken, Navigator
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules
#
# Token implementation which represents a group of tokens.
#
from explicit_nlu.token import Not, Like


@dataclass
class Group(IToken):
    tokens: List[IToken]

    def __str__(self):
        return "[" + (" ".join(list(map(IToken.as_text, self.tokens)))) + "]"

    def __repr__(self):
        return self.__str__()

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate group")

        whitelist = False

        for token in self.tokens:
            if token is not Not:
                whitelist = True

            if token.as_text() == navigator.get_curr():
                result = token is not Not
                return ExplicitEvaluation(result, dict(), [navigator.get_absolute_index() - 1])

            if token is Like:
                if self.levenshtein(token.as_text(), navigator.get_curr()) <= 1:
                    return ExplicitEvaluation(True, dict(), [navigator.get_absolute_index() - 1])

        return ExplicitEvaluation(not whitelist, dict(), [navigator.get_absolute_index() - 1])

    # TODO: use library
    def levenshtein(self, a: str, b: str):
        a = a.lower()
        b = b.lower()
        if not a: return len(b)
        if not b: return len(a)
        return min(self.levenshtein(a[1:], b[1:]) + (a[0] != b[0]),
                   self.levenshtein(a[1:], b) + 1,
                   self.levenshtein(a, b[1:]) + 1)
