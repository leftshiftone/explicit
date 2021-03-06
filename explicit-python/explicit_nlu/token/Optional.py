import logging
from dataclasses import dataclass

from explicit_nlu.api import IToken, Navigator
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules


#
# Token implementation which represents an optional token.
#
@dataclass
class Optional(IToken):
    token: IToken

    def __str__(self):
        return str(self.token) + "?"

    def __repr__(self):
        return self.__str__()

    def as_text(self):
        return self.token.as_text()

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate optional")
        return self.token.evaluate(rulez, navigator)
