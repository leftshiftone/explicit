from abc import ABC, abstractmethod

from explicit.api import Navigator


class IToken(ABC):

    def as_text(self):
        return str(self)

    @abstractmethod
    def evaluate(self, rulez, navigator: Navigator):
        pass
