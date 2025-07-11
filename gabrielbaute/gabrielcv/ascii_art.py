from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel

def get_banner(name: str) -> Panel:
    figlet = Figlet(font="ansi_shadow")
    ascii_art = figlet.renderText(name)
    return Panel.fit(
        ascii_art,
        title="GabrielCV",
        subtitle="Python Jr. Developer",
        border_style="bold magenta",
        padding=(1, 4)
    )
