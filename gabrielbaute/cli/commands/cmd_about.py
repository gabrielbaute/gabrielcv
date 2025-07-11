
def cmd_about(args):
    print(
"""Gabriel es un desarrollador autodidacta, fan del self-hosting y la cultura DIY.
Se formó como Ingeniero en Telecomunicaciones y, posteriormente, como periodista.
Esta mezcla le permitió integrar tempranamente ramas diferentes del ejercicio profesional,
llevándolo a trabajos relacionados con el big data, la investigación y el desarrollo
de herramientas para cubrir las necesidades del proceso.

Esto se puso de manifiesto en su estancia en Infomigration (donde se trabajó con metodologías
como Lean Startup y el Business Canvas de Ostelwalder), y posteriormente, en su trabajo en
la docencia, donde se prefirió siempre el método del aprendizaje basado en proyectos
para motivar a los estudiantes y lograr ver la conexión entre los conocimientos adquiridos
en su formación académica y la aplicación inmediata con las necesidades del entorno.

En la actualidad, es un fiel entusiasta de la comunidad self-hosted, en la que procura
dar su aporte pensando en herramientas que ayuden al crecimiento y mantenimiento
del movimiento self-hosted.
"""
        )

def register_about_parser(subparsers):
    parser = subparsers.add_parser("about", help="Acerca de...")
    parser.set_defaults(func=cmd_about)