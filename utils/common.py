from rapidfuzz import fuzz
from pathlib import Path
import json
from dataclasses import asdict
from models import CommandData, VariableData, ProjectData, FindingData, HostData 

# Lee el json y devuelve una lista de objetos: [Model(), Model(), Model()] 
def read_all(file_path : Path) -> list: # Lista de Command
    # Si el archivo no existe o pesa 0 retorna la lisat vacía
    if not file_path.exists() or file_path.stat().st_size == 0:
        return []

    match file_path.name:
        case "commands.json":
            model_type = CommandData
        case "variables.json":
            model_type = VariableData
        case "project.json":
            model_type = ProjectData
        case "findings.json":
            model_type = FindingData
        case "hosts.json":
            model_type = HostData
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [model_type(**item) for item in data]
    except json.JSONDecodeError:
        return []

# Lee una lista de objetos, los convierte a json y los escribe
def save(file_path: Path, data : list) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([asdict(item) for item in data], f, indent=4, ensure_ascii=False)

#print(read_all(PATHS.PROJECT_FILE, models.ProjectData))