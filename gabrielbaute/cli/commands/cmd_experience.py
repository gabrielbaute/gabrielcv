from rich.console import Console
from rich.table import Table
import json
from gabrielbaute.gabrielcv import GabrielBaute

def cmd_experience(args):
    console = Console()
    profile = GabrielBaute()

    # Aplicar filtros
    experience = profile.experience
    if args.only_active:
        experience = [e for e in experience if e["active"]]
    if args.only_remote:
        experience = [e for e in experience if e["remote"]]

    # Salida en JSON
    if args.format == "json":
        console.print(json.dumps(experience, indent=2, ensure_ascii=False))
        return

    # Tabla con Rich
    table = Table(title="[bold cyan]Experiencia Laboral[/bold cyan]", border_style="blue")
    table.add_column("Empresa", style="bold yellow")
    table.add_column("Cargo(s)", style="green")
    table.add_column("Duración", justify="center")
    table.add_column("Tipo", style="magenta")

    for job in experience:
        cargos = "\n".join(f"• {c['name']}" for c in job["charges"])
        start = job["start"]
        end = job["until"]
        tipo = "🌐 Remoto" if job["remote"] else "🏢 Presencial"
        table.add_row(job["name"], cargos, f"{start} → {end}", tipo)

    console.print(table)

def register_experience_parser(subparsers):
    parser = subparsers.add_parser("experience", help="Mostrar experiencia laboral")
    parser.add_argument("--only-active", action="store_true", help="Mostrar solo trabajos activos")
    parser.add_argument("--only-remote", action="store_true", help="Mostrar solo trabajos remotos")
    parser.add_argument("--format", choices=["table", "json"], default="table", help="Formato de salida")
    parser.set_defaults(func=cmd_experience)
