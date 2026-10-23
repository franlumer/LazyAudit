from rapidfuzz import fuzz
from pathlib import Path
import json
from dataclasses import asdict

def json_to_model(file_path: Path, model_type) -> list: # Lista de Command
    # Lee un JSON y devuelve una lista de objetos

    # Si el archivo no existe o pesa 0 retorna la lisat vacía
    if not file_path.exists() or file_path.stat().st_size == 0:
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [model_type(**item) for item in data]
    except json.JSONDecodeError:
        return []

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

def fuzzy_matches(query: str, text_fields: list[str], threshold: int = 86) -> bool:
    # Evalúa si query coincide exacta o a medias con alguno de los campos
    query = query.lower()
    for field_val in text_fields:
        text_field = (field_val or "").lower()
        if query in text_field:
            return True
        if fuzz.partial_ratio(query, text_field) >= threshold:
            return True
    return False

def search_in_file(file_path: Path, query: str, model_type=None, threshold: int = 86) -> list:
        """Lee el JSON en file_path y devuelve los elementos que coincidan con query."""
        if not file_path.exists() or file_path.stat().st_size == 0:
            return []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = [data]  # Por si es project.json que tiene un solo objeto {...}
        except json.JSONDecodeError:
            return []

        resultados = []
        for item in data:
            # Junta todos los valores de texto del objeto (incluso si adentro tiene listas como 'tags' o 'vulns')
            campos = []
            for valor in item.values():
                if isinstance(valor, list):
                    campos.extend([str(v) for v in valor])
                else:
                    campos.append(str(valor))

            # Si coincide con fuzzy_matches, lo guarda
            if fuzzy_matches(query, campos, threshold):
                if model_type:
                    resultados.append(model_type(**item))
                else:
                    resultados.append(item)

        return resultados