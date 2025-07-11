import json
from rich.console import Console
from rich.table import Table
from gabrielbaute.gabrielcv import GabrielBaute

def cmd_studies(args):
    console = Console()
    profile = GabrielBaute()

    # Aplica filtro si se pidió solo estudios concluidos
    studies = profile.studies
    if args.only_concluded:
        studies = [s for s in studies if s["concluded"]]

    # Si el formato es JSON, mostrar como diccionario serializado
    if args.format == "json":
        console.print(json.dumps(studies, indent=2, ensure_ascii=False))
        return

    # En formato tabla
    table = Table(title="[bold blue]Formación Académica[/bold blue]", border_style="cyan")
    table.add_column("Título", style="bold yellow")
    table.add_column("Universidad", style="green")
    table.add_column("Año", justify="center")
    table.add_column("Estado", style="magenta")

    for study in studies:
        estado = "✅ Concluido" if study["concluded"] else "⏳ En curso / no concluido"
        table.add_row(
            study["title"],
            study["university"],
            str(study["year"]),
            estado
        )

    console.print(table)

def register_studies_parser(subparsers):
    parser = subparsers.add_parser("studies", help="Mostrar formación académica")
    parser.add_argument("--only-concluded", action="store_true", help="Mostrar solo estudios concluidos")
    parser.add_argument("--format", choices=["table", "json"], default="table", help="Formato de salida")
    parser.set_defaults(func=cmd_studies)