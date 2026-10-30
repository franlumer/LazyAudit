from rapidfuzz import fuzz
from pathlib import Path
import json
from dataclasses import asdict

# Lee una lista de objetos, los convierte a json y los escribe
def save(file_path: Path, data : list) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([asdict(item) for item in data], f, indent=4, ensure_ascii=False)


class CommonActions():
    # Lee el json y devuelve una lista de objetos: [Model(), Model(), Model()] 
# print(read_all(PATHS.PROJECT_FILE))
    @classmethod
    def read_all(cls) -> list: # Lista de Command
        file_path : Path = cls.file_path

        # Si el archivo no existe o pesa 0 retorna la lisat vacía
        if not file_path.exists() or file_path.stat().st_size == 0:
            return []

        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [cls(**item) for item in data]
        except json.JSONDecodeError:
            return []

    
    # Recibe la [Model(), Model()] a modificar, el dato viejo (sacado de la tui) y el dato nuevo (armado)
    def modify(data, old_model, new_model) -> None:
        for model in data:
            if model == old_model:
                index = data.index(model)
                data[index] = new_model

    def add(project_commands : Path, command):
        save(project_commands, command)

    def remove(project_commands : Path, command):
        pass

