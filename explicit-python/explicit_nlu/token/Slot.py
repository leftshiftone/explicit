import logging
import re
from dataclasses import dataclass

from explicit_nlu.api import IToken, Navigator
from explicit_nlu.api.support import Strings
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules


#
# Token implementation which represents a ner slot.
#
@dataclass
class Slot(IToken):
    slot: str

    def __str__(self):
        return "{" + self.slot + "}"

    def __repr__(self):
        return self.__str__()

    def as_text(self):
        return self.slot

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate slot")

        expr1 = self.__str__() == navigator.get_curr()
        expr2 = self.as_text() == "number" and Strings.is_numeric(navigator.get_curr())
        expr3 = self.evaluate_pattern(rulez, navigator.get_curr())
        expr4 = self.evaluate_mapping(rulez, navigator.get_curr())

        evaluation = expr1 or expr2 or expr3 or expr4
        return ExplicitEvaluation(evaluation, dict(), [navigator.get_absolute_index() - 1])

    def evaluate_pattern(self, rulez: ExplicitRules, atomic: str) -> bool:
        if self.as_text() in rulez.patterns:
            match = re.match(rulez.patterns[self.as_text()] + "$", atomic)
            return match is not None
        return False

    def evaluate_mapping(self, rulez: ExplicitRules, atomic: str) -> bool:
        if atomic in rulez.mappings:
            if self.as_text() == "number":
                return rulez.mappings[atomic].isdigit()
        return False
