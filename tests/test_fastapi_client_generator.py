import filecmp
import os

from pathlib import Path
from typing import Any, Dict

from python_client_generator.generate_apis import generate_apis
from python_client_generator.generate_base_client import generate_base_client
from python_client_generator.generate_models import generate_models
from python_client_generator.generate_pyproject import generate_pyproject


EXPECTED_PATH = Path(os.path.dirname(os.path.realpath(__file__))) / "expected/fastapi_app_client"


def test_models(fastapi_app_openapi: Dict[str, Any], tmp_path: Path) -> None:
    generate_models(fastapi_app_openapi, tmp_path / "models.py")
    assert filecmp.cmp(EXPECTED_PATH / "models.py", tmp_path / "models.py", shallow=False) is True


def test_base_client(tmp_path: Path) -> None:
    generate_base_client(tmp_path / "base_client.py", sync=False)
    assert (
        filecmp.cmp(EXPECTED_PATH / "base_client.py", tmp_path / "base_client.py", shallow=False)
        is True
    )


def test_apis(fastapi_app_openapi: Dict[str, Any], tmp_path: Path) -> None:
    generate_apis(fastapi_app_openapi, tmp_path / "apis.py", group_by_tags=False, sync=False)
    assert filecmp.cmp(EXPECTED_PATH / "apis.py", tmp_path / "apis.py", shallow=False) is True


def test_pyproject(fastapi_app_openapi: Dict[str, Any], tmp_path: Path) -> None:
    generate_pyproject(
        fastapi_app_openapi, tmp_path / "pyproject.toml", project_name="fastapi-project"
    )
    assert (
        filecmp.cmp(EXPECTED_PATH / "pyproject.toml", tmp_path / "pyproject.toml", shallow=False)
        is True
    )
