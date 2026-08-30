from pathlib import Path
import PATHS

for path in Path(PATHS.PROJECTS_DIR).rglob("*"):
    if path.is_file():
        print(f"Archivo: {path}")
    elif path.is_dir():
        print(f"Carpeta: {path}")