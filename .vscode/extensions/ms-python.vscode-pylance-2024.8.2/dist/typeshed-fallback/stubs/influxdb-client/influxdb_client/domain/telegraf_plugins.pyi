from _typeshed import Incomplete

class TelegrafPlugins:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, version: Incomplete | None = None, os: Incomplete | None = None, plugins: Incomplete | None = None
    ) -> None: ...
    @property
    def version(self): ...
    @version.setter
    def version(self, version) -> None: ...
    @property
    def os(self): ...
    @os.setter
    def os(self, os) -> None: ...
    @property
    def plugins(self): ...
    @plugins.setter
    def plugins(self, plugins) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
