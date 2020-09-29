import logging
from dataclasses import dataclass

from explicit_nlu.api import IToken, Navigator
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules


#
# Token implementation which represents a label. A label can be used
# to reference a result of the ner parsing process.
#
@dataclass
class Label(IToken):
    token: IToken

    def __str__(self):
        return "#" + str(self.token)

    def __repr__(self):
        return self.__str__()

    def as_text(self):
        return str(self.token)

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate label")

        if navigator.get_curr() not in rulez.labels:
            return ExplicitEvaluation(False, dict(), [navigator.get_absolute_index() - 1])

        result = self.as_text() == rulez.labels[navigator.get_curr()]
        return ExplicitEvaluation(result, dict(), [navigator.get_absolute_index() - 1])
