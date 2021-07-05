import click
import pyperclip
import sys

# TODO -> Check into cx-freeze for distribution or be lazy and use pyinstaller again


@click.command()
@click.argument("input", type=click.File("r"), default=sys.stdin)
def cli(input):
    pyperclip.copy("".join(input.readlines()))
