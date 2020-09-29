from abc import ABC, abstractmethod
from typing import Callable, List, Any


class IConversionBinding(ABC):

    @abstractmethod
    def register_variable(self, name: str, value):
        pass

    @abstractmethod
    def register_function(self, name:str, function: Callable[[List[Any]], Any]):
        pass

    @abstractmethod
    def get_variable(self, name: str) -> Any:
        pass

    @abstractmethod
    def get_function(self, name: str) -> Any:
        pass
