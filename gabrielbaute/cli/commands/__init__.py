from gabrielbaute.cli.commands.version import cmd_version
from gabrielbaute.cli.commands.cmd_summary import cmd_summary
from gabrielbaute.cli.commands.cmd_profile import cmd_skills, cmd_json, cmd_projects
from gabrielbaute.cli.commands.cmd_about import cmd_about
from gabrielbaute.cli.commands.cmd_highlight import cmd_highlight
from gabrielbaute.cli.commands.cmd_studies import cmd_studies

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