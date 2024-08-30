from _typeshed import Incomplete
from re import Pattern
from typing import Final

class TranslatorError(Exception): ...

class Translator:
    tokenizer: Incomplete
    def __init__(self, formula, origin) -> None: ...
    def get_tokens(self): ...
    ROW_RANGE_RE: Final[Pattern[str]]
    COL_RANGE_RE: Final[Pattern[str]]
    CELL_REF_RE: Final[Pattern[str]]
    @staticmethod
    def translate_row(row_str, rdelta): ...
    @staticmethod
    def translate_col(col_str, cdelta): ...
    @staticmethod
    def strip_ws_name(range_str): ...
    @classmethod
    def translate_range(cls, range_str, rdelta, cdelta): ...
    def translate_formula(self, dest: Incomplete | None = None, row_delta: int = 0, col_delta: int = 0): ...
