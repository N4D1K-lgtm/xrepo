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
    group: List[str] = typer.Argument(
        None,
        help="List of desired groups to display [green]Ex: default my-web-app sample-repository-group[/green] [dim]\[default: default][/dim]",
        show_default=False,
        envvar="ACTIVE_REPOSITORY_GROUP",
    ),
):
    """
    Print tracked repositories from a list of repository groups.
    """
    if not group:
        group = ["default"]

    repo_dict = utils.fetch_repositories_in_groups(path, group, all=all)
    for g in repo_dict:

        table = Table(title=None, box=box.MINIMAL)

        table.add_column("Repository Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Path", style="magenta")
        table.add_column("Docker Compose", style="cyan", justify="center")
        table.add_column("Git Branch", style="magenta", justify="center")
        panel = Panel(
            table,
            title=f"[yellow bold]Repository Group: {g}",
            expand=False,
            box=box.ROUNDED,
        )

        for repo in repo_dict.get(g):
            table.add_row(str(pathlib.PurePath(repo).name), repo)

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
