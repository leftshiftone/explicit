from dataclasses import dataclass
from typing import Any

from explicit_nlu.api import IConversion, IConversionBinding


@dataclass
class VariableExtractor(IConversion):
    name:str

    def extract(self, binding: IConversionBinding) -> Any:
        return binding.get_variable(self.name)
