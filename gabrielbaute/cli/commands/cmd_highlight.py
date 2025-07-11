from rich.console import Console
from rich.table import Table

def cmd_highlight(args):
    console = Console()
    table = Table(
        title="[bold green]🌟 Proyecto Destacado[/bold green]",
        show_header=False,
        border_style="bright_magenta",
        padding=(0, 2),
    )

    table.add_column("Campo", style="cyan", justify="right")
    table.add_column("Detalle", style="bold yellow")

    table.add_row("Nombre", "Descargador de música Spotify → YouTube Music")
    table.add_row("Tipo", "CLI Tool para Jellyfin")
    table.add_row("Versión", "0.5.1")
    table.add_row("Publicado en", "[link=https://pypi.org/project/spotify-downloader]PyPI[/link]")
    table.add_row("Colaboración", "Con desarrollador @rafnigx, python developer")
    table.add_row("Estrellas en GitHub", "⭐ 57")
    table.add_row("Repositorio", "[link=https://github.com/gabrielbaute/spotify-downloader]GitHub[/link]")

    console.print(table)
