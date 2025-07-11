from gabrielbaute.cli.commands.cmd_version import cmd_version
from gabrielbaute.cli.commands.cmd_summary import cmd_summary
from gabrielbaute.cli.commands.cmd_skills import cmd_skills
from gabrielbaute.cli.commands.cmd_json import cmd_json
from gabrielbaute.cli.commands.cmd_projects import cmd_projects
from gabrielbaute.cli.commands.cmd_about import cmd_about
from gabrielbaute.cli.commands.cmd_highlight import cmd_highlight
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