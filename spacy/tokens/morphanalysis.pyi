from typing import Any, Dict, Iterator, List, Optional, Union
from ..vocab import Vocab

class MorphAnalysis:
    def __init__(
        self, vocab: Vocab, features: Union[Dict[str, str], str] = ...
    ) -> None: ...
    @classmethod
    def from_id(cls, vocab: Vocab, key: Any) -> MorphAnalysis: ...
    def __contains__(self, feature: str) -> bool: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: MorphAnalysis) -> bool: ...  # type: ignore[override]
    def __ne__(self, other: MorphAnalysis) -> bool: ...  # type: ignore[override]
    def get(self, field: Any, default: Optional[List[str]]) -> List[str]: ...
    def to_json(self) -> str: ...
    def to_dict(self) -> Dict[str, str]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...