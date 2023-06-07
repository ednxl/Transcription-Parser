from typing import Callable, Protocol, Iterator, Optional, Union, Tuple, Any, overload
from thinc.types import Floats1d, Ints2d, FloatsXd
from .doc import Doc
from .token import Token
from .underscore import Underscore
from ..lexeme import Lexeme
from ..vocab import Vocab

class SpanMethod(Protocol):
    def __call__(self: Span, *args: Any, **kwargs: Any) -> Any: ...  # type: ignore[misc]

class Span:
    @classmethod
    def set_extension(
        cls,
        name: str,
        default: Optional[Any] = ...,
        getter: Optional[Callable[[Span], Any]] = ...,
        setter: Optional[Callable[[Span, Any], None]] = ...,
        method: Optional[SpanMethod] = ...,
        force: bool = ...,
    ) -> None: ...
    @classmethod
    def get_extension(
        cls, name: str
    ) -> Tuple[
        Optional[Any],
        Optional[SpanMethod],
        Optional[Callable[[Span], Any]],
        Optional[Callable[[Span, Any], None]],
    ]: ...
    @classmethod
    def has_extension(cls, name: str) -> bool: ...
    @classmethod
    def remove_extension(
        cls, name: str
    ) -> Tuple[
        Optional[Any],
        Optional[SpanMethod],
        Optional[Callable[[Span], Any]],
        Optional[Callable[[Span, Any], None]],
    ]: ...
    def __init__(
        self,
        doc: Doc,
        start: int,
        end: int,
        label: Union[str, int] = ...,
        vector: Optional[Floats1d] = ...,
        vector_norm: Optional[float] = ...,
        kb_id: Union[str, int] = ...,
        span_id: Union[str, int] = ...,
    ) -> None: ...
    def __richcmp__(self, other: Span, op: int) -> bool: ...
    def __hash__(self) -> int: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    @overload
    def __getitem__(self, i: int) -> Token: ...
    @overload
    def __getitem__(self, i: slice) -> Span: ...
    def __iter__(self) -> Iterator[Token]: ...
    @property
    def _(self) -> Underscore: ...
    def as_doc(self, *, copy_user_data: bool = ...) -> Doc: ...
    def get_lca_matrix(self) -> Ints2d: ...
    def similarity(self, other: Union[Doc, Span, Token, Lexeme]) -> float: ...
    @property
    def doc(self) -> Doc: ...
    @property
    def vocab(self) -> Vocab: ...
    @property
    def sent(self) -> Span: ...
    @property
    def ents(self) -> Tuple[Span]: ...
    @property
    def has_vector(self) -> bool: ...
    @property
    def vector(self) -> Floats1d: ...
    @property
    def vector_norm(self) -> float: ...
    @property
    def tensor(self) -> FloatsXd: ...
    @property
    def sentiment(self) -> float: ...
    @property
    def text(self) -> str: ...
    @property
    def text_with_ws(self) -> str: ...
    @property
    def noun_chunks(self) -> Iterator[Span]: ...
    @property
    def root(self) -> Token: ...
    def char_span(
        self,
        start_idx: int,
        end_idx: int,
        label: Union[int, str] = ...,
        kb_id: Union[int, str] = ...,
        vector: Optional[Floats1d] = ...,
        id: Union[int, str] = ...,
        alignment_mode: str = ...,
        span_id: Union[int, str] = ...,
    ) -> Span: ...
    @property
    def conjuncts(self) -> Tuple[Token]: ...
    @property
    def lefts(self) -> Iterator[Token]: ...
    @property
    def rights(self) -> Iterator[Token]: ...
    @property
    def n_lefts(self) -> int: ...
    @property
    def n_rights(self) -> int: ...
    @property
    def subtree(self) -> Iterator[Token]: ...
    start: int
    end: int
    start_char: int
    end_char: int
    label: int
    kb_id: int
    id: int
    ent_id: int
    ent_id_: str
    @property
    def orth_(self) -> str: ...
    @property
    def lemma_(self) -> str: ...
    label_: str
    kb_id_: str
    id_: str