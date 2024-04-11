import click
from common.safe import runs_safely
from api import runs_authentified, auth
from config import config
import sys
import os

USERNAME, PASSWORD, PROMPT = config.USERNAME, config.PASSWORD, config.PROMPT


@click.group()
def main():
    """
    Simple CLI for PROTEUS Worker utils
    """
    pass


@main.command()
@click.option("--user", prompt=PROMPT, default=USERNAME)
@click.option("--password", prompt=PROMPT, default=PASSWORD)
@runs_authentified
def login():
    """Will perfom a login to test current credentials"""
    click.echo(auth.access_token_parsed)


@main.command()
@click.option("--user", prompt=PROMPT, default=USERNAME)
@click.option("--password", prompt=PROMPT, default=PASSWORD)
@runs_authentified
@runs_safely
def run():
    """Will start worker lifecycle"""
    exit_code = os.EX_OK
    try:
        from private.lifecycle.main import Lifecycle

        lifecycle = Lifecycle()
        lifecycle.run()
    except Exception as error:
        print(error)
        exit_code = os.EX_SOFTWARE
    finally:
        sys.exit(exit_code)


if __name__ == "__main__":
    main()
