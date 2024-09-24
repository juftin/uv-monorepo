"""
Generate the code reference pages and navigation.
"""

import logging
from pathlib import Path

import mkdocs_gen_files

logger = logging.getLogger(__name__)

project_dir = Path(__file__).resolve().parent.parent

readme_file = project_dir / "README.md"
readme_content = readme_file.read_text(encoding="utf-8")
readme_content = readme_content.replace("](docs/", "](")
# Exclude parts that are between two exact `<!--skip-->` lines
readme_content = "\n".join(readme_content.split("\n<!--skip-->\n")[::2])
with mkdocs_gen_files.open("index.md", "w") as index_file:
    index_file.write(readme_content)
