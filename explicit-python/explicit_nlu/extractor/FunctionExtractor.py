from dataclasses import dataclass
from typing import Any, List

from explicit_nlu.api import IConversion, IConversionBinding


@dataclass
class FunctionExtractor(IConversion):
    name: str
    args: List[IConversion]

    def extract(self, binding: IConversionBinding) -> Any:
        return binding.get_function(self.name)(list(map(lambda x: x.extract(binding), self.args)))
