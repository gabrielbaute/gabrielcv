import json
from gabrielbaute.gabrielcv import GabrielBaute

profile = GabrielBaute()

def cmd_json(args):
    print(json.dumps(profile.__dict__, indent=2))

def register_json_parser(subparsers):
    parser = subparsers.add_parser("json", help="Devuelve toda la información en formato json")
    parser.set_defaults(func=cmd_json)