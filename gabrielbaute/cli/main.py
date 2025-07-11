from gabrielbaute.cli.parser import create_parser
from gabrielbaute.cli.commands import COMMANDS

def main():
    """Función principal de la CLI"""   
    
    parser = create_parser()
    args = parser.parse_args()

    COMMANDS[args.command](args)
