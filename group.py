import typer
import tomli
import tomli_w
import rich

from typing import List, Optional

app = typer.Typer()


@app.command(
    hidden=True,
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def show():
    rich.print(
        "If you would like to display a repository group's information run [cyan]xrepo show GROUP... [OPTIONS][/cyan]."
    )
    return


@app.command()
def create():
    """
    create a repository group
    """
