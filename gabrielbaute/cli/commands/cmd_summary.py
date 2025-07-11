from rich.console import Console
from rich.table import Table
from gabrielbaute.gabrielcv import GabrielBaute, get_banner

def cmd_summary(args):
    console = Console()
    profile = GabrielBaute()

    console.print(get_banner(profile.name))

    data = profile.summary_dict()
    table = Table(title="[bold cyan]Resumen[/bold cyan]", border_style="green")
    table.add_column("Campo", style="magenta", justify="right")
    table.add_column("Valor", style="bold yellow")

    for key, value in data.items():
        table.add_row(key, value)

    console.print(table)

def register_summary_parser(subparsers):
    parser = subparsers.add_parser("summary", help="Muestra un resumen, en forma de tabla, del desarrollador.")
    parser.set_defaults(func=cmd_summary)