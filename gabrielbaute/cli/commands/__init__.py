from gabrielbaute.cli.commands.cmd_version import cmd_version, register_version_parser
from gabrielbaute.cli.commands.cmd_summary import cmd_summary, register_summary_parser
from gabrielbaute.cli.commands.cmd_skills import cmd_skills, register_skills_parser
from gabrielbaute.cli.commands.cmd_json import cmd_json, register_json_parser
from gabrielbaute.cli.commands.cmd_projects import cmd_projects, register_projects_parser
from gabrielbaute.cli.commands.cmd_about import cmd_about, register_about_parser
from gabrielbaute.cli.commands.cmd_highlight import cmd_highlight, register_highlight_parser
from gabrielbaute.cli.commands.cmd_studies import cmd_studies, register_studies_parser

# Mapeo de comandos
COMMANDS = {
    "summary": cmd_summary,
    "skills": cmd_skills,
    "projects": cmd_projects,
    "highlight": cmd_highlight,
    "about": cmd_about,
    "version": cmd_version,
    "json": cmd_json,
    "studies": cmd_studies,
}

def register_subparsers(subparsers):
    register_studies_parser(subparsers)
    register_skills_parser(subparsers)
    register_projects_parser(subparsers)
    register_summary_parser(subparsers)
    register_json_parser(subparsers)
    register_highlight_parser(subparsers)
    register_about_parser(subparsers)
    register_version_parser(subparsers)

def get_available_commands() -> dict:
    return {
        "summary": "Mostrar resumen general con banner",
        "skills": "Listar habilidades técnicas",
        "projects": "Ver proyectos desarrollados por categoría",
        "highlight": "Proyecto más exitoso",
        "about": "Filosofía del desarrollador",
        "version": "Información de versión y autor",
        "json": "CV como diccionario serializable",
        "studies": "Formación académica con filtros",
    }