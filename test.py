import typer
from typing import Optional
from typing_extensions import Annotated

app = typer.Typer(help="CLI Software Developer Kit for programming in Amstrad Basic and Ugbasic. ")


@app.command()
def run(file: str = typer.Option(default="fff",help="dfasdfasdfasdfa"),setting:str = typer.Option(default="fff",help="dfasdfasdfasdfa")):
    """
    Execute DSK/CDT in emulator.
    """
    print(f"Creating user: {file} {setting}")

@app.command()
def pepe(
    # file: Optional[str]=typer.Argument(default="fff",help="dfasdfasdfasdfa"),
    # name: Annotated[Optional[str], typer.Argument()] = None,
    name: str, ### ARGUMENTO
    # formal: bool = False, # DE TRUE O FALSE
    lastname: Annotated[str, typer.Option(default=...)],
    last_name: str = typer.Option(...,help="dfasdfasdfasdfa"),
    # age: Optional[str] = typer.Argument(None),
):

# @app.command()
# def pepe(
#     file: Optional[str]=typer.Argument(default="fff",help="dfasdfasdfasdfa"),
#     last_name: str = typer.Option(default="<unknown>"),
#     age: Optional[str] = typer.Argument(None),
# ):
    print(f"Creating user: ")
# @app.command()
# def pepe(
#     file: str,
#     last_name: str = typer.Option(default="<unknown>"),
#     age: Optional[str] = typer.Argument(None),
# ):
#     print(f"Creating user: ")    
    
@app.command()
def delete(
    username: str,
    force: bool = typer.Option(
        ...,
        prompt="Are you sure you want to delete the user?",
        help="Force deletion without confirmation.",
    ),
):
    """
    Delete a user with USERNAME.

    If --force is not used, will ask for confirmation.
    """
    if force:
        print(f"Deleting user: {username}")
    else:
        print("Operation cancelled")


@app.command()
def delete_all(
    force: bool = typer.Option(
        ...,
        prompt="Are you sure you want to delete ALL users?",
        help="Force deletion without confirmation.",
    )
):
    """
    Delete ALL users in the database.

    If --force is not used, will ask for confirmation.
    """
    if force:
        print("Deleting all users")
    else:
        print("Operation cancelled")


@app.command()
def init():
    """
    Initialize the users database.
    """
    print("Initializing user database")


if __name__ == "__main__":
    app()