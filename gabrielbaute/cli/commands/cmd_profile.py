import json
from gabrielbaute.gabrielcv import get_banner, GabrielBaute

profile = GabrielBaute()

def cmd_skills(args):
    print("\n🛠️ Habilidades Técnicas:")
    for skill in profile.skills:
        print(f" - {skill}")

def cmd_projects(args):
    print("\n🚀 Proyectos Destacados:")
    print(profile.get_featured_projects())

def cmd_json(args):
    print(json.dumps(profile.__dict__, indent=2))
