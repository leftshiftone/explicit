from dataclasses import dataclass
from typing import List, Dict

from explicit_nlu.parser.ExplicitRule import ExplicitRule


@dataclass
class ExplicitRules:
    name: str
    rulez: List[ExplicitRule]
    labels: Dict[str, str]
    tokens: List['Token']
    mappings: Dict[str, str]
    patterns: Dict[str, str]
    features: Dict[str, str]

    def __len__(self):
        return len(self.rulez)

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < (self.__len__() - 1):
            rule = self.rulez[self.counter]
            self.counter += 1
            return rule
        else:
            raise StopIteration


@dataclass
class Token:
    pattern: str
    replacement: str
    boundary: bool
    regex: bool
