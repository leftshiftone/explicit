from dataclasses import dataclass
from typing import Any

from explicit_nlu.api import IConversion, IConversionBinding


@dataclass
class StringExtractor(IConversion):
    result: str

    def extract(self, binding: IConversionBinding) -> Any:
        return self.result[1:-1]
