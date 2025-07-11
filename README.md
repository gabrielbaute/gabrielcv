# 🧠 GabrielCV — CLI interactiva del perfil de Gabriel Baute

**GabrielCV** es un proyecto escrito en Python que convierte tu CV tradicional en una herramienta interactiva, modular, extensible y con estilo visual. Utiliza `argparse`, `rich`, y una arquitectura limpia para presentar tu formación, habilidades, experiencia y proyectos desarrollados como comandos tipo CLI.

### ✨ Características

- Presentación jerárquica con arte ASCII y tablas estilizadas
- Comandos personalizados con flags como `--format`, `--only-concluded`, `--only-remote`
- Visualización rica con `rich.table`, `rich.panel` y `rich.tree`
- Proyecto modular con arquitectura extensible
- Disponible como script vía `poetry`

### 🚀 Instalación

```bash
git clone https://github.com/gabrielbaute/gabrielcv.git
cd gabrielcv
poetry install
```

### 📦 Uso

```bash
poetry run gabrielcv              # Muestra el banner y los comandos disponibles
poetry run gabrielcv summary      # Muestra resumen general
poetry run gabrielcv skills       # Lista tus habilidades
poetry run gabrielcv projects     # Proyectos desarrollados
poetry run gabrielcv studies --only-concluded --format json
poetry run gabrielcv experience --only-remote
```

### 🛠️ Estructura del proyecto

```
gabrielcv/
├── gabrielcv/           # Datos del perfil y arte ASCII
├── cli/                 # Módulo CLI con comandos, parsers y main
│   ├── commands/        # Comandos divididos por lógica
│   └── parser.py        # Manejo de argumentos por subcomando
├── README.md            # Este archivo
└── pyproject.toml       # Configuración con poetry
```

### 💡 Filosofía

> Este CV interactivo refleja mi enfoque autodidacta, mi pasión por el desarrollo de herramientas prácticas y mi gusto por lo visual, lo modular y lo autoalojado.