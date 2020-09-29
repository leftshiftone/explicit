import logging

from explicit_nlu.api import IToken, Navigator
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules


#
# Token implementation which represents a wildcard.
#
class Wildcard(IToken):

    def __str__(self):
        return "*"

    def __repr__(self):
        return self.__str__()

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate wildcard")
        return ExplicitEvaluation(False, dict(), [navigator.get_absolute_index() - 1])
