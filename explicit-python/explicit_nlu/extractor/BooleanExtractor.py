from dataclasses import dataclass
from typing import Any

from explicit_nlu.api import IConversion, IConversionBinding


@dataclass
class BooleanExtractor(IConversion):
    result: bool

    def extract(self, binding: IConversionBinding) -> Any:
        return self.result
