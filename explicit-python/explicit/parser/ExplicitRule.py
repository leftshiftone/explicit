from dataclasses import dataclass
from typing import List, Dict

from explicit.api.IToken import IToken


@dataclass
class ExplicitRule:
    rule: List[IToken]
    ner: List[Dict[str, str]]
    idx: List[int]
