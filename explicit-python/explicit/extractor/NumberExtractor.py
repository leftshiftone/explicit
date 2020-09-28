from dataclasses import dataclass
from typing import Any

from explicit.api import IConversion, IConversionBinding


@dataclass
class NumberExtractor(IConversion):
    result: float

    def extract(self, binding: IConversionBinding) -> Any:
        return self.result
