from typing import Any

from django.apps import apps as apps
from django.core.management.base import BaseCommand as BaseCommand
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS
from django.db import connections as connections
from django.db.migrations.loader import MigrationLoader as MigrationLoader

class Command(BaseCommand):
    verbosity: int = ...
    def show_list(self, connection: Any, app_names: list[str] | None = ...) -> None: ...
    def show_plan(self, connection: Any, app_names: list[str] | None = ...) -> None: ...
