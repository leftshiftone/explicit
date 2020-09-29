import logging
from dataclasses import dataclass

from explicit_nlu.api import IToken, Navigator
from explicit_nlu.evaluator import ExplicitEvaluation
from explicit_nlu.parser import ExplicitRules


#
# Token implementation which represents a token with an explicit alias.
#
@dataclass
class Alias(IToken):
    alias: str
    token: IToken

    def __str__(self):
        return str(self.token) + ":" + self.alias

    def __repr__(self):
        return self.__str__()

    def as_text(self):
        return self.alias

    def evaluate(self, rulez: ExplicitRules, navigator: Navigator) -> ExplicitEvaluation:
        logging.debug("evaluate alias")

        evaluation = self.token.evaluate(rulez, navigator)
        entries = dict()

        if evaluation.result:
            curr = navigator.get_curr()
            entries[self.alias] = rulez.mappings[curr] if curr in rulez.mappings else curr

        return ExplicitEvaluation(evaluation.result, entries, [navigator.get_absolute_index() - 1])
