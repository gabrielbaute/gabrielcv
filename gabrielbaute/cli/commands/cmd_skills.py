import json
from gabrielbaute.gabrielcv import GabrielBaute

profile = GabrielBaute()

def cmd_skills(args):
    print("\n🛠️ Habilidades Técnicas:")
    for skill in profile.skills:
        print(f" - {skill}")

def register_skills_parser(subparsers):
    parser = subparsers.add_parser("skills", help="Muestra las habilidades del desarrollador")
    parser.set_defaults(func=cmd_skills)