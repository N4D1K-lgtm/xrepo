import tomli
import tomli_w

from typing import List, Optional
from pathlib import Path

import typer
from rich import print


def get_workspace_dictionary(
    conf_path: Path, workspaces: Optional[List[str]], all=False
):
    """
    Accepts config path and a list of groups as parameters
    Parses through TOML config and appends the groups with the associated repositories to a dictionary and returns it.
    """

    with open(conf_path, "rb") as f:
        toml_dict = tomli.load(f).get("workspaces")
        dict = {}
        if all:
            workspaces = list(toml_dict)

        for workspace in workspaces:
            if workspace in toml_dict:
                dict[workspace] = toml_dict.get(workspace)
            else:
                print(
                    f"  [red bold]Error:[/red bold] The group [green bold]'{workspace}'[/green bold] does not exist! Did you mean one of these? {get_workspace_names}"
                )
                raise typer.Exit(code=1)

        return dict


# def get_repository_information(dict: dict, workspace: str, repository: str):
#     print(workspace, repository)

#     result = []
#     for property in dict.values():
#         result.append(str(property))
#     return result


def get_workspace_names(conf_path: Path):
    names = []
    with open(conf_path, "rb") as f:
        toml_dict = tomli.load(f).get("workspaces")

        for workspace in toml_dict:
            names.append(workspace)
    return names
