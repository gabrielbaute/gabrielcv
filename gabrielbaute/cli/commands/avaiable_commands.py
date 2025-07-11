"""Diccionario con los comandos disponibles"""

def get_available_commands() -> dict:
    return {
        "summary": {"desc": "Mostrar resumen general con banner", "tag": "[INFO]"},
        "skills": {"desc": "Listar habilidades técnicas", "tag": "[DATA]"},
        "projects": {"desc": "Ver proyectos desarrollados por categoría", "tag": "[DATA]"},
        "highlight": {"desc": "Proyecto más exitoso", "tag": "[CLI]"},
        "about": {"desc": "Filosofía del desarrollador", "tag": "[INFO]"},
        "version": {"desc": "Información de versión y autor", "tag": "[META]"},
        "json": {"desc": "CV como diccionario serializable", "tag": "[DEV]"},
        "studies": {"desc": "Formación académica con filtros", "tag": "[DATA]"},
    }
