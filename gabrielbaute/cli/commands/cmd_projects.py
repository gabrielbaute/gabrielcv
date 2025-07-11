import json
from gabrielbaute.gabrielcv import GabrielBaute

profile = GabrielBaute()

def cmd_projects(args):
    print("\n🚀 Proyectos Destacados:")
    print(profile.get_featured_projects())

def register_projects_parser(subparsers):
    parser = subparsers.add_parser("projects", help="Una lista con los principales proyectos realizados")
    parser.set_defaults(func=cmd_projects)