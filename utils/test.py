import json
from models import CommandData, ScopeData
from dataclasses import asdict
from pathlib import Path

class Scope(ScopeData):
    pass

class Command(CommandData):
    pass

comando = Command(title="title",command="command",description="descripion",tags=["tags","tags"],scope=Scope.GLOBAL)

def model_to_json(file_path: Path, model_obj) -> None:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                #Lee el archivo actual y si no es lista (no existe) crea una lista vacía
                lista_actual = json.load(f)
                if not isinstance(lista_actual, list):
                    lista_actual = []
        except (FileNotFoundError, json.JSONDecodeError):
            lista_actual = []

        # Exend = Lista + Lista
        # Append = Lista + Objeto
        if isinstance(model_obj, list):
            lista_actual.extend([asdict(item) for item in model_obj])
        else:
            lista_actual.append(asdict(model_obj))

        # Crea la carpeta si no existe, sino no hace nada
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(lista_actual, f, indent=4, ensure_ascii=False)

model_to_json(Path("test.json"), comando)