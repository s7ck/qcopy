import click
import pyperclip

# TODO -> Check into cx-freeze for distribution or be lazy and use pyinstaller again


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def cli(filename):
    with open(filename, "r") as file:
        pyperclip.copy("".join(file.readlines()))

    print(f"The contents of {filename} are now on your clipboard.")
