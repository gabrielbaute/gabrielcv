import json
from gabrielbaute.gabrielcv import GabrielBaute

profile = GabrielBaute()

def cmd_skills(args):
    print("\n🛠️ Habilidades Técnicas:")
    for skill in profile.skills:
        print(f" - {skill}")