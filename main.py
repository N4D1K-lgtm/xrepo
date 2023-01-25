import typer
import logging
import click
import pathlib

from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table, box
from rich.logging import RichHandler
from dotenv import load_dotenv

from typing import List

import group, repo, utils

load_dotenv()

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])],
)

log = logging.getLogger("rich")

err_console = Console(stderr=True, style="bold red")
console = Console()

app = typer.Typer(
    rich_markup_mode="rich",
    help="xrepo is a Python CLI tool for more efficiently developing across multiple git repositories simultaneously. \
If you have any issues or suggestions, please submit them [blue underline][link=https://github.com/N4D1K-lgtm/xrepo/issues]here[/link][/blue underline].",
    epilog="Kidan was here",
    add_completion=False,
)

####################################################################
####################  Setup and Configuration ######################
####################################################################

app.add_typer(
    group.app,
    name="group",
    help="Manage repository groups",
    rich_help_panel="Setup and Configuration",
)
app.add_typer(
    repo.app,
    name="repo",
    help="Manage tracked repositories",
    rich_help_panel="Setup and Configuration",
)


@app.command(
    rich_help_panel="Setup and Configuration",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def show(
    path: str = typer.Option(
        "./conf.toml",
        "--config-file",
        "-c",
        help="path to TOML configuration file [green]Ex: ~/Documents/GitHub/conf.toml[/green]",
    ),
    all: bool = typer.Option(
        False, "--all", "-a", help="Display all repository groups"
    ),
    workspace: List[str] = typer.Argument(
        None,
        help="List of which workspaces to display configuration information about.[green]Ex: default my-web-app sample-repository-group[/green] [dim]\[default: default][/dim]",
        show_default=False,
        envvar="ACTIVE_REPOSITORY_WORKSPACE",
    ),
):
    """
    Print tracked repositories from a list of repository workspaces.
    """
    if not workspace:
        workspace = ["Default"]

    workspace_dict = utils.get_workspace_dictionary(path, workspace, all=all)
    for ws in workspace_dict:

        table = Table(title=None, box=box.MINIMAL)

        table.add_column("Repository Name", justify="left", no_wrap=True)
        table.add_column("Description", justify="left", style="dim")
        table.add_column("Path", style="magenta")
        table.add_column("Docker Compose", style="yellow dim", justify="center")
        table.add_column("Active Git Branch", style="cyan", justify="center")

        panel = Panel(
            table,
            title=f"[yellow bold]Workspace: {ws}",
            expand=False,
            box=box.ROUNDED,
        )

        for repository in workspace_dict.get(ws):

            table.add_row(*workspace_dict.get(ws).get(repository).values())

        console.print(panel)


@app.command(rich_help_panel="Setup and Configuration")
def configure():
    """
    Run auto configuration script
    """
    return


#########################################################
####################  GIT COMMANDS  #####################
#########################################################


@app.command(rich_help_panel="Git Commands")
def fetch():
    """
    Fetch remote commits on the active branch across all tracked repositories.
    """
    return


@app.command(rich_help_panel="Git Commands")
def pull():
    """
    Pull remote commits on the active branch across all tracked repositories, overwriting local changes.
    """
    return


@app.command(rich_help_panel="Git Commands")
def push():
    """
    Push local commits to remote on the active branch.
    """
    return


@app.command(rich_help_panel="Git Commands")
def checkout():
    """
    Create a new branch or switch to it if it already exists.
    """
    return


############################################################
####################  Docker Commands  #####################
############################################################


@app.command(rich_help_panel="Docker Commands")
def up():
    """
    Runs docker-compose up -d if a docker-compose.yml file exists in the repository.
    """
    return


@app.command(rich_help_panel="Docker Commands")
def down():
    return


@app.command(rich_help_panel="Docker Commands")
def detect():
    return


if __name__ == "__main__":
    app()
