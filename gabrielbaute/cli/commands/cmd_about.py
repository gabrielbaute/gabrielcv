
def cmd_about(args):
    print("Gabriel es un desarrollador autodidacta, fan del self-hosting y la cultura DIY...")

def register_about_parser(subparsers):
    parser = subparsers.add_parser("about", help="Acerca de...")
    parser.set_defaults(func=cmd_about)