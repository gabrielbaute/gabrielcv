from rich.console import Console
from rich.table import Table
from gabrielbaute.gabrielcv import GabrielBaute

def cmd_studies(args):
    console = Console()
    profile = GabrielBaute()

    table = Table(title="[bold blue]Formación Académica[/bold blue]", border_style="cyan")
    table.add_column("Título", style="bold yellow")
    table.add_column("Universidad", style="green")
    table.add_column("Año", justify="center")
    table.add_column("Estado", style="magenta")

    for study in profile.studies:
        estado = "✅ Concluido" if study["concluded"] else "⏳ En curso / no concluido"
        table.add_row(
            study["title"],
            study["university"],
            str(study["year"]),
            estado
        )

    console.print(table)
