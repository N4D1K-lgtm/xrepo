import tomli
import tomli_w

from typing import List, Optional
from pathlib import Path

import typer
from rich import print
from rich.table import Table, box
from rich.console import Console
from rich.panel import Panel

import utils

# names = utils.get_workspace_names("test.toml")
# print(names)

dictionary = utils.get_workspace_dictionary("test.toml", None, all=True)
print(dictionary)

# new_dictionary = utils.get_workspace_dictionary("test.toml", ["Default"])
# print(new_dictionary)

result = utils.get_repository_information("test.toml", "Default", "currently-web")

console = Console()

table = Table(title=None, box=box.MINIMAL)

table.add_column("Repository Name", justify="left", style="cyan", no_wrap=True)
table.add_column("Description", justify="left", style="cyan")
table.add_column("Path", style="magenta")
table.add_column("Docker Compose", style="cyan", justify="center")

panel = Panel(
    table,
    title=f"[yellow bold]Workspace: Default",
    expand=False,
    box=box.ROUNDED,
)

table.add_row(*result)
console.print(result)
console.print(panel)
