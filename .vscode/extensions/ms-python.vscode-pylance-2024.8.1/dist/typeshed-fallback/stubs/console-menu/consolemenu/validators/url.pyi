from consolemenu.validators.base import BaseValidator as BaseValidator

class UrlValidator(BaseValidator):
    def __init__(self) -> None: ...
    def validate(self, input_string: str) -> bool: ...
