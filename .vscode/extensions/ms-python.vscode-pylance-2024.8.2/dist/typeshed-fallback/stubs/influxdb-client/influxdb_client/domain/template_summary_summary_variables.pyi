from _typeshed import Incomplete

class TemplateSummarySummaryVariables:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        kind: Incomplete | None = None,
        template_meta_name: Incomplete | None = None,
        id: Incomplete | None = None,
        org_id: Incomplete | None = None,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        arguments: Incomplete | None = None,
        label_associations: Incomplete | None = None,
        env_references: Incomplete | None = None,
    ) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def template_meta_name(self): ...
    @template_meta_name.setter
    def template_meta_name(self, template_meta_name) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def org_id(self): ...
    @org_id.setter
    def org_id(self, org_id) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    @property
    def arguments(self): ...
    @arguments.setter
    def arguments(self, arguments) -> None: ...
    @property
    def label_associations(self): ...
    @label_associations.setter
    def label_associations(self, label_associations) -> None: ...
    @property
    def env_references(self): ...
    @env_references.setter
    def env_references(self, env_references) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
