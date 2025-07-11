import sys

from gabrielbaute.cli.parser import create_parser
from gabrielbaute.cli.welcome import show_welcome

def main():
    """Función principal de la CLI"""   
    
    parser = create_parser()

    # Si no se pasa ningún argumento, mostrar bienvenida
    if len(sys.argv) == 1:
        show_welcome()
        return
    
    args = parser.parse_args()

    args.func(args)
