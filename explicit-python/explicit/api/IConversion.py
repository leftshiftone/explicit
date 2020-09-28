from abc import ABC
from typing import Any

from explicit.api import IConversionBinding


class IConversion(ABC):

    def extract(self, binding: IConversionBinding) -> Any:
        pass
