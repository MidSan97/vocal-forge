"""Module which defines functions used for managing various settings."""

from __future__ import annotations

from vocal_forge.common import TEMP_DIR
from vocal_forge.core.manage.common import delete_directory


def delete_temp_files() -> None:
    """Delete all temporary files."""
    delete_directory(TEMP_DIR)
