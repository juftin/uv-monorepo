"""
uv-release helper

This Python script is meant to be used as a release helper for this monorepo.
The scenario here is that we have a monorepo with multiple projects, and we
only want to release the projects that have had their __version__ updated.
This script will help us to identify which projects have had their versions
updated and which projects have not. The output of the `diff` command can be
used to build a Github Action Matrix to only release the projects that have
had their versions updated.

This release method hasn't been implemented in this monorepo and instead a
`semantic-release` implementation has been done.
"""

# /// script
# dependencies = [
#   "click==8.1.7",
#   "packaging==24.1",
# ]
# ///

from __future__ import annotations

import dataclasses
import json
import logging
import os
import pathlib
import subprocess

import click
from packaging.version import Version

__version__ = "0.1.0"
__application__ = "uv-release"
monorepo_root = pathlib.Path(__file__).parent.parent

logger = logging.getLogger(__application__)


@dataclasses.dataclass
class UvPipList:
    """
    Output From `uv pip list --editable --format json`
    """

    name: str
    version: Version
    path: pathlib.Path

    def __post_init__(self):
        """
        Post Initialization Validation
        """
        self.version = Version(str(self.version))
        self.path = pathlib.Path(self.path)

    @classmethod
    def from_json(cls, data: str) -> dict[str, UvPipList]:
        """
        Create UvPipList from JSON Data
        """
        items: list[dict[str, str]] = json.loads(data)
        return {
            item["name"]: cls(
                name=item["name"],
                version=Version(item["version"]),
                path=pathlib.Path(item["path"]),
            )
            for item in items
        }

    def as_safe_dict(self) -> dict[str, str]:
        """
        Convert to Dictionary
        """
        return {
            "name": self.name,
            "version": str(self.version),
            "path": str(self.path),
        }


@click.group
def cli():
    """
    UV Release CLI
    """
    pass


@cli.command()
def versions() -> None:
    """
    Show the versions of all UV Projects
    """
    all_pyproject_files = list((monorepo_root / "src").rglob("**/pyproject.toml"))
    versions: list[UvPipList] = []
    os.environ.pop("VIRTUAL_ENV", None)
    for pyproject_filepath in all_pyproject_files:
        version = (
            subprocess.run(
                "uv run --no-sync --with hatch hatch project metadata version",
                shell=True,
                check=True,
                cwd=pyproject_filepath.parent,
                stdout=subprocess.PIPE,
            )
            .stdout.decode()
            .strip()
        )
        name = (
            subprocess.run(
                "uv run --no-sync --with hatch hatch project metadata name",
                shell=True,
                check=True,
                cwd=pyproject_filepath.parent,
                stdout=subprocess.PIPE,
            )
            .stdout.decode()
            .strip()
        )
        versions.append(
            UvPipList(
                name=name,
                version=Version(version),
                path=pyproject_filepath.parent.relative_to(monorepo_root),
            )
        )
    json_safe_versions = [package.as_safe_dict() for package in versions]
    click.echo(json.dumps(json_safe_versions))


@cli.command()
@click.option(
    "-o", "--old", help="Old UV Environment", required=True, envvar="OLD_VERSIONS"
)
@click.option(
    "-n", "--new", help="New UV Environment", required=True, envvar="NEW_VERSIONS"
)
def diff(old: str, new: str) -> list[UvPipList]:
    """
    Show the difference between two UV Environments
    """
    new_packages: list[UvPipList] = []
    former_versions = UvPipList.from_json(data=old)
    new_versions = UvPipList.from_json(data=new)
    for package_name, new_item in new_versions.items():
        former_item = former_versions.get(package_name)
        if former_item is None:
            logger.info("New Package: %s %s", new_item.name, new_item.version)
            new_packages.append(new_item)
        elif former_item.version < new_item.version:
            logger.info(
                "Upgrade: %s %s -> %s",
                new_item.name,
                former_item.version,
                new_item.version,
            )
            new_packages.append(new_item)
        elif former_item.version > new_item.version:
            logger.error(
                "Downgrade: %s %s -> %s",
                new_item.name,
                former_item.version,
                new_item.version,
            )
        elif former_item.version == new_item.version:
            logger.info("No Change: %s %s", new_item.name, new_item.version)
        else:
            logger.error(
                "Invalid Version Comparison: %s %s %s",
                new_item.name,
                former_item.version,
                new_item.version,
            )
            raise ValueError("Incompatible Version Change")
    json_safe_diff = [package.as_safe_dict() for package in new_packages]
    click.echo(json.dumps(json_safe_diff, indent=2))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s [%(levelname)8s]: %(message)s"
    )
    cli()
