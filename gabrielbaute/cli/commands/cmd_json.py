import json
from gabrielbaute.gabrielcv import GabrielBaute

profile = GabrielBaute()

def cmd_json(args):
    print(json.dumps(profile.__dict__, indent=2))
