import logging
from dataclasses import dataclass

from explicit.api import IToken, Navigator
from explicit.evaluator import ExplicitEvaluation
from explicit.parser import ExplicitRules


#
# Token implementation which represents a simple text.
#
@dataclass
class Text(IToken):
    text: str

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.__str__()

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate text")

        result = self.text == navigator.get_curr()
        return ExplicitEvaluation(result, dict(), [navigator.get_absolute_index() - 1])
