from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ExplicitEvaluation:
    result: bool
    entries: Dict[str, str]
    indices: List[int]

    def __iter__(self):
        for i in [self.result, self.entries, self.indices]:
            yield i
