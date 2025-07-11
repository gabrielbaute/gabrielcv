"""Este módulo contiene la clase del perfil"""

class GabrielBaute:
    def __init__(self):
        self.name = "Gabriel Baute"
        self.title = "Python Jr. Developer"
        self.country = "Venezuela"
        self.skills = [
            "Python", "Flask", "Docker", "Linux", "Argparse", "Click", "Sass/SCSS",
            "Web Scraping", "ffmpeg", "LVM", "ASCII art", "Pillow", "Fitz"
        ]
        self.projects = {
            "Web Apps": [
                "Octopus-CMS: un CMS basado en Flask y Bulma (CSS)",
                "SamanPhotos: App tipo Google Photos self-hosted, basada en Flask",
                "OctopusIcon: Generador de assets para PWA (basado en Flask y pillow)"
            ],
            "CLI Tools": [
                "Conversor PDF a CBZ para Kavita",
                "Conversor MP3 a M4B para Audiobookshelf",
                "anime-light: compresor de video CLI (PyPI)",
                "SpotifySaver: CLI y API de descagra de música Spotify → YouTube Music (PyPI)"
            ],
            "Frontend": [
                "Framework CSS en Sass/SCSS",
                "Telegrma bot para AudiobookShelf",
                "Diversos bot de telegram para scraping en actividades de docencia"],
            "Colaboraciones": [
                "Gestión del repositorio y desarrollo colaborativo (v0.5.1)"
            ]
        }
        self.contact = {
            "GitHub": "https://github.com/gabrielbaute",
            "Telegram": "@gabrielfernando",
            "LinkedIn": "https://www.linkedin.com/in/gabriel-f-baute-s-96a8b4158/",
            "Correo": "gabrielbaute@gmail.com"
        }
        self.studies = [
            {
                "title": "Ingeniero de Telecomunicaciones",
                "year": 2014,
                "university": "UNEFA",
                "concluded": True
            },
            {
                "title": "Licenciado en Matemáticas",
                "year": 2016,
                "university": "UC",
                "concluded": False
            },
            {
                "title": "Técnico Superior Universitario en producción de medios audiovisuales",
                "year": 2018,
                "university": "UBV",
                "concluded": True
            },
            {
                "title": "Licenciado en Comunicación Social",
                "year": 2019,
                "university": "UBV",
                "concluded": True
            },
        ]
    
    def summary_dict(self) -> dict:
        return {
            "Nombre": self.name,
            "Título": self.title,
            "Skills": ", ".join(self.skills[:5]) + "..." if len(self.skills) > 5 else ", ".join(self.skills),
            "Proyectos": f"{len(self.projects['CLI Tools']) + len(self.projects['Web Apps'])} principales",
            "Formación": self.get_studies_summary(),
            "Filosofía": "Autodidacta, DIY, self-hosted",
            "Contacto": ", ".join(f"{k}: {v}" for k, v in self.contact.items())
        }
    
    def get_summary(self) -> str:
        return f"{self.name} - {self.title}\nSkills: {', '.join(self.skills)}"

    def get_studies_summary(self):
        total = len(self.studies)
        concluded = sum(1 for s in self.studies if s["concluded"])
        return f"{total} carreras ({concluded} concluidas)"

    def get_featured_projects(self) -> str:
        featured = []
        for category, items in self.projects.items():
            featured.append(f"\n📁 {category}:")
            featured.extend([f"  - {project}" for project in items])
        return "\n".join(featured)

    def show_skills(self) -> str:
        return self.skills

    def show_projects(self) -> str:
        return self.projects
