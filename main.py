import typer
from rich import print
from rich.console import Console
from rich.table import Table
from typing import List
import tomli

err_console = Console(stderr=True)
console = Console()

app = typer.Typer(
    rich_markup_mode="rich",
    help="xrepo is a Python CLI tool for more efficiently developing across multiple git repositories simultaneously. If you have any issues or suggestions, please submit them here: [blue]https://github.com/N4D1K-lgtm/xrepo/issues",
)


# @app.command()
# def pull(repositories: List[str] = typer.Argument(envvar="repos")):
#     print(f"Hello ")


@app.command()
def print_config(
    path: str = typer.Argument(
        "./conf.toml",
        help="path to TOML configuration file [green]Ex: ~/Documents/GitHub/conf.toml[/green]",
    ),
    group: str = typer.Option(
        "default",
        help="group name as defined in TOML configuration file [green]Ex: myproject-web[/green]",
    ),
):
    """
    Print the PATHS of currently configured repositories
    """
    with open(path, "rb") as f:
        toml_dict = tomli.load(f)
        repos = toml_dict.get(group).get("repos")
        for repo in repos:
            console.print(repo)


@app.command()
def configure():

    return


if __name__ == "__main__":
    app()
