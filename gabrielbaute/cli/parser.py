import argparse
from gabrielbaute.cli.commands import COMMANDS, register_subparsers


def create_parser():
    """Configura los argumentos de la CLI"""

    parser = argparse.ArgumentParser(
        prog="gabrielcv",
        description="CLI interactiva del CV de Gabriel Baute",
        epilog="Ejemplo: gabrielcv studies --only-concluded"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    register_subparsers(subparsers)

    return parser