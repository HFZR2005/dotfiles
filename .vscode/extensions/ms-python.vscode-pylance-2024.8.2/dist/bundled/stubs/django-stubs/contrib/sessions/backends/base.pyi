from datetime import datetime
from typing import Any

VALID_KEY_CHARS: Any

class CreateError(Exception): ...
class UpdateError(Exception): ...

class SessionBase(dict[str, Any]):
    TEST_COOKIE_NAME: str = ...
    TEST_COOKIE_VALUE: str = ...
    accessed: bool = ...
    modified: bool = ...
    serializer: Any = ...
    def __init__(self, session_key: str | None = ..., **kwargs: Any) -> None: ...
    def set_test_cookie(self) -> None: ...
    def test_cookie_worked(self) -> bool: ...
    def delete_test_cookie(self) -> None: ...
    def encode(self, session_dict: dict[str, Any]) -> str: ...
    def decode(self, session_data: bytes | str) -> dict[str, Any]: ...
    def has_key(self, key: Any) -> Any: ...
    def keys(self) -> Any: ...
    def values(self) -> Any: ...
    def items(self) -> Any: ...
    def clear(self) -> None: ...
    def is_empty(self) -> bool: ...
    session_key: Any = ...
    def get_expiry_age(self, **kwargs: Any) -> int: ...
    def get_expiry_date(self, **kwargs: Any) -> datetime: ...
    def set_expiry(self, value: datetime | int | None) -> None: ...
    def get_expire_at_browser_close(self) -> bool: ...
    def flush(self) -> None: ...
    def cycle_key(self) -> None: ...
    def exists(self, session_key: str) -> bool: ...
    def create(self) -> None: ...
    def save(self, must_create: bool = ...) -> None: ...
    def delete(self, session_key: Any | None = ...) -> None: ...
    def load(self) -> dict[str, Any]: ...
    @classmethod
    def clear_expired(cls) -> None: ...
