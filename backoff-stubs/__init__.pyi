import logging
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    Iterable,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
)

_FuncT = TypeVar("_FuncT", bound=Callable[..., Any])
_HandlerFunction = Callable[[Dict], None]
_EventHandler = Union[_HandlerFunction, Iterable[_HandlerFunction]]

def on_predicate(
    wait_gen: Callable[..., Generator[float, None, None]],
    predicate: Callable[[Any], bool] = ...,
    max_tries: Optional[int] = ...,
    max_time: Optional[int] = ...,
    jitter: Callable[[float], float] = ...,
    on_success: Optional[_EventHandler] = ...,
    on_backoff: Optional[_EventHandler] = ...,
    on_giveup: Optional[_EventHandler] = ...,
    logger: Union[str, logging.Logger, None] = ...,
    **wait_gen_kwargs: Any
) -> Callable[[_FuncT], _FuncT]: ...
def on_exception(
    wait_gen: Callable[..., Generator[float, None, None]],
    exception: Union[Type[Exception], Tuple[Type[Exception], ...]],
    max_tries: Optional[int] = ...,
    max_time: Optional[int] = ...,
    jitter: Callable[[float], float] = ...,
    giveup: Callable[[Exception], bool] = ...,
    on_success: Optional[_EventHandler] = ...,
    on_backoff: Optional[_EventHandler] = ...,
    on_giveup: Optional[_EventHandler] = ...,
    logger: Union[str, logging.Logger, None] = ...,
    **wait_gen_kwargs: Any
) -> Callable[[_FuncT], _FuncT]: ...
def expo(
    base: float = ..., factor: float = ..., max_value: Optional[float] = ...
) -> Generator[float, None, None]: ...
def fibo(max_value: Optional[float] = ...) -> Generator[float, None, None]: ...
def constant(
    interval: Union[float, Iterable[float], Sequence[float]] = ...
) -> Generator[float, None, None]: ...
def full_jitter(value: float) -> float: ...
def random_jitter(value: float) -> float: ...
