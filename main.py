from gabrielbaute.gabrielcv.profile import GabrielBaute
from gabrielbaute.gabrielcv.banner_ascii import get_banner

def main():
    profile = GabrielBaute()
    
    # Comandos como:
    banner = get_banner()
    print(banner)
    print(profile.get_featured_projects())

if __name__ == "__main__":
    main()