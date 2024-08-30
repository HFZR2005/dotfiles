from typing import Any, Literal
from typing_extensions import LiteralString

class GaloisGroupException(Exception): ...
class ResolventException(GaloisGroupException): ...

class Resolvent:
    def __init__(self, F, X, s) -> None: ...
    def get_prec(self, M, target=...) -> int | Any: ...
    def approximate_roots_of_poly(self, T, target=...) -> list[Any]: ...
    @staticmethod
    def round_mpf(a) -> int | Any: ...
    def round_roots_to_integers_for_poly(self, T) -> dict[int, int | Any]: ...
    def eval_for_poly(self, T, find_integer_root=...) -> tuple[list[Any], int | Any | None, int | None]: ...

def wrap(text, width=...) -> LiteralString | Literal[""]: ...
def s_vars(n) -> Any: ...
def sparse_symmetrize_resolvent_coeffs(F, X, s, verbose=...) -> tuple[list[Any], list[Any]]: ...
def define_resolvents() -> dict[
    tuple[Literal[4], Literal[0]]
    | tuple[Literal[4], Literal[1]]
    | tuple[Literal[5], Literal[1]]
    | tuple[Literal[6], Literal[1]]
    | tuple[Literal[6], Literal[2]],
    Any,
]: ...
def generate_lambda_lookup(verbose=..., trial_run=...) -> str: ...
def get_resolvent_by_lookup(T, number) -> list[Any]: ...

if __name__ == "__main__":
    verbose = ...
    trial_run = ...
    table = ...
