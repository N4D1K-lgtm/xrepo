import tomli
import tomli_w

from typing import List, Optional
from pathlib import Path

import typer
from rich import print


def fetch_repositories_in_groups(
    conf_path: Path, groups: Optional[List[str]], all=False
):
    """
    Accepts config path and a list of groups as parameters
    Parses through TOML config and appends the groups with the associated repositories to a dictionary and returns it.
    """

    with open(conf_path, "rb") as f:
        toml_dict = tomli.load(f)
        repo_dict = {}
        if all:
            groups = list(toml_dict.keys())

        for group in groups:
            if group in toml_dict:
                repo_dict[group] = toml_dict.get(group).get("repos")
            else:
                group_names = list(toml_dict.keys())
                print(
                    f"  [red bold]Error:[/red bold] The group [green bold]'{group}'[/green bold] does not exist! Did you mean one of these? {group_names}"
                )
                raise typer.Exit(code=1)

        return repo_dict
