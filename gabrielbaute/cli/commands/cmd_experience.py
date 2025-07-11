from rich.console import Console
from rich.table import Table
from rich.tree import Tree
import json
from gabrielbaute.gabrielcv import GabrielBaute

def cmd_experience(args):
    console = Console()
    profile = GabrielBaute()

    experience = profile.experience
    
    # Filtros
    if args.only_active:
        experience = [e for e in experience if e["active"]]
    if args.only_remote:
        experience = [e for e in experience if e["remote"]]

    # Salida en JSON
    if args.format == "json":
        console.print(json.dumps(experience, indent=2, ensure_ascii=False))
        return

    tree = Tree("[bold blue]🌳 Experiencia Laboral[/bold blue]")

    for job in experience:
        empresa_str = f"📁 [bold yellow]{job['name']}[/bold yellow] ({job['start']} → {job['until']})"
        empresa_node = tree.add(empresa_str)

        for charge in job["charges"]:
            cargo_str = f"👔 [green]{charge['name']}[/green]"
            cargo_node = empresa_node.add(cargo_str)

            descripcion = f"📝 {charge['description']}"
            cargo_node.add(descripcion)

        tipo_str = "🌐 Remoto" if job["remote"] else "🏢 Presencial"
        empresa_node.add(f"Tipo: {tipo_str}")

    console.print(tree)

def register_experience_parser(subparsers):
    parser = subparsers.add_parser("experience", help="Mostrar experiencia laboral en árbol jerárquico")
    parser.add_argument("--only-active", action="store_true", help="Mostrar solo trabajos activos")
    parser.add_argument("--only-remote", action="store_true", help="Mostrar solo trabajos remotos")
    parser.add_argument("--format", choices=["table", "json"], default="table", help="Formato de salida")
    parser.set_defaults(func=cmd_experience)
