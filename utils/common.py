from rapidfuzz import fuzz
from pathlib import Path
import json
from dataclasses import asdict
import PATHS

# Recibe una lista de objetos, los convierte en diccionarios y los escribe en JSON
# [Model(), Model()] -> { } -> JSON
# 1. Path. 2. Lista de modelos.
def _save(file_path: Path, data : list) -> None:

    if not isinstance(data, list): 
        data = [data]
        
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([asdict(item) for item in data], f, indent=4, ensure_ascii=False)

def _save_dual(model, file_path : Path, data : list) -> None:
    from models import ScopeData
    global_list = []
    private_list = []

    for i in data:
        if i.scope == ScopeData.GLOBAL:
            global_list.append(i)
        if i.scope == ScopeData.PRIVATE:
            private_list.append(i)

    _save(file_path, private_list)

    if model.__name__ == "Command":
        _save(PATHS.GLOBAL_COMMANDS_FILE, global_list)
    else:
        _save(PATHS.GLOBAL_VARS_FILE, global_list)
    
def _extract_data(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            return data
    except json.JSONDecodeError:
        return []

# Acciones generales de los modelos (read, add, remove, modify, delete)
class CommonActions():
    # Lee el json y devuelve una lista de objetos
    # JSON -> [Model(), Model()]
    # ej: print(read_all(PATHS.PROJECT_FILE))
    @classmethod
    def read_all(cls) -> list:
        project_file : Path = cls.file_path
        global_file = None
        data = []

        if project_file.name == "commands.json":
            global_file = PATHS.GLOBAL_COMMANDS_FILE
        if project_file.name == "variables.json":
            global_file = PATHS.GLOBAL_VARS_FILE

        # Si el archivo no existe o pesa 0 retorna la lista vacía
        if project_file.exists() and project_file.stat().st_size != 0:
            data.extend(_extract_data(project_file))

        if global_file and global_file.exists() and global_file.stat().st_size != 0:
            data.extend(_extract_data(global_file))

        return [cls(**item) for item in data]


    # Recibe la lista de modelos para modificar, el dato viejo y el dato nuevo
    # [Model(), Model()], OldModel(), NewModel()
    # La idea por ahora que no hay TUI es sacarlo de ahí, mediante selección
    # se busca en la lista completa y se lo modifica
    @classmethod
    def modify(cls, old_model, new_model) -> None:
        project_file: Path = cls.file_path
        data = cls.read_all()

        for model in data:
            if model == old_model:
                index = data.index(model)
                data[index] = new_model
                break

        if cls.__name__ == "Command" or cls.__name__ == "Variable":
            _save_dual(cls, project_file, data)
        else:
            _save(project_file, data)

    @classmethod
    def add(cls, command):
        project_command_file : Path = cls.file_path

        data = cls.read_all()
        data.append(command)

        if cls.__name__ == "Command" or cls.__name__ == "Variable":
            _save_dual(cls, project_command_file, data)
        else:
            _save(project_command_file, data)

    @classmethod
    def remove(cls, model_to_remove) -> None:
        project_file: Path = cls.file_path
        data = cls.read_all()

        if model_to_remove in data:
            data.remove(model_to_remove)

        if cls.__name__ == "Command" or cls.__name__ == "Variable":
            _save_dual(cls, project_file, data)
        else:
            _save(project_file, data)

        
        