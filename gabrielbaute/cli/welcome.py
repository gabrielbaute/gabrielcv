from rich.console import Console
from rich.table import Table

from gabrielbaute.cli.commands import get_available_commands
from gabrielcv.ascii_art import get_banner

def show_welcome():
    console = Console()
    console.print(get_banner("Gabriel Baute"))

    console.print("[bold cyan]Comandos disponibles:[/bold cyan]\n")
    table = Table(border_style="cyan", title="📘 Índice de comandos")

    table.add_column("Comando", style="magenta", justify="right")
    table.add_column("Descripción", style="green")

    for cmd, desc in get_available_commands().items():
        table.add_row(f"`{cmd}`", desc)

    console.print(table)
    console.print("\nUsa [yellow]gabrielcv <comando> --help[/yellow] para más detalles.")
