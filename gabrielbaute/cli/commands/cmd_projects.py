import json
from gabrielbaute.gabrielcv import GabrielBaute

profile = GabrielBaute()

def cmd_projects(args):
    print("\n🚀 Proyectos Destacados:")
    print(profile.get_featured_projects())