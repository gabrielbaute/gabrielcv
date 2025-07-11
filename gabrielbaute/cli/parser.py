import argparse
from gabrielbaute.cli.commands import COMMANDS

def create_parser():
    """Configura los argumentos de la CLI"""
    
    parser = argparse.ArgumentParser(
        prog="gabrielcv",
        description="CLI interactiva del CV de Gabriel Baute",
        epilog="Ejemplo: gabrielcv sumarry"
    )
    parser.add_argument("command", choices=COMMANDS.keys(), help="Comando a ejecutar")
    return parser
