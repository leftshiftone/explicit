import logging
from dataclasses import dataclass

from explicit_nlu.api import IToken, Navigator
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules


#
# Token implementation which represents a token with an escaped text.
#
@dataclass
class Escaped(IToken):
    text: str

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.__str__()

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate escaped")

        result = self.text == navigator.get_curr()
        return ExplicitEvaluation(result, dict(), [navigator.get_absolute_index() - 1])
