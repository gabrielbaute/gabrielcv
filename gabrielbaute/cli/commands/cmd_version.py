from rich.console import Console
from rich.table import Table

console = Console()
__version__ = "0.1.2"

def show_version():
    """Muestra la versión en una tabla estilo Rich."""
    console = Console()
    table = Table(
        title="[bold magenta]Gabriel Baute CV CLI[/bold magenta]",
        show_header=False,
        border_style="blue",
        padding=(0, 2),
    )
    table.add_column("Key", style="cyan", justify="right")
    table.add_column("Value", style="green")
    
    table.add_row("[yellow]Build[/yellow]", "[bold]stable[/bold]")
    table.add_row("Versión", f"[bold]{__version__}[/bold]")
    table.add_row("Autor", "Gabriel Baute")
    table.add_row("Licencia", "MIT")
    table.add_row("Repo", "https://github.com/gabrielbaute/gabrielcv")

    console.print(table)

def cmd_version(args):
    show_version()

def register_version_parser(subparsers):
    parser = subparsers.add_parser("version", help="Devuelve una tabla con la versión de la CLI")
    parser.set_defaults(func=cmd_version)