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
