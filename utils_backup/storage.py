import json
import re
from dataclasses import asdict
from pathlib import Path
from rapidfuzz import fuzz

def load_models(file_path: Path, model_type) -> list: # Lista de Command
    # Lee un JSON de lista ([...]) y devuelve una lista de objetos model_type

    # Si el archivo no existe o pesa 0 retorna la lisat vacía
    if not file_path.exists() or file_path.stat().st_size == 0:
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [model_type(**item) for item in data]
    except json.JSONDecodeError:
        return []

def save_models(file_path: Path, items: list, model_type) -> None:
        # Recibe una lista de objetos dataclass y los escribe en el JSON
        old_commands = load_models(file_path, model_type)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        old_commands.extend(items)
        data = [asdict(item) for item in old_commands]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

def load_single_model(file_path: Path, model_type):
    # Lee un JSON de un único objeto ({...}) y devuelve una instancia de model_type
    if not file_path.exists() or file_path.stat().st_size == 0:
        return None
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return model_type(**data)
    except json.JSONDecodeError:
        return None

def save_single_model(file_path: Path, item) -> None:
    # Guarda un único objeto dataclass en un archivo JSON
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(asdict(item), f, indent=4, ensure_ascii=False)

def interpolate_text(text: str, variables: list) -> str:
        # Convierte la lista de objetos Variable en un dict {key: value}
        vars_dict = {v.key: v.value for v in variables}

        def replace(match):
            var_name = match.group(1)
            return str(vars_dict.get(var_name, match.group(0)))
        return re.sub(r"\{(\w+)\}", replace, text)

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

if __name__ == "__main__":
    import PATHS
    from models import Command, Variable, Project, Scope

    # --- 1. Prueba de save_single_model (Objeto único -> project.json) ---
    #ruta_proyecto_test = PATHS.get_project_metafile("audit_test")
    #nuevo_proyecto = Project(
    #    name="audit_test",
    #    description="Proyecto de prueba para save",
    #    status="active",
    #    created="21-10-2026"
    #)
    #save_single_model(ruta_proyecto_test, nuevo_proyecto)
    #print("Proyecto guardado y vuelto a leer:", load_single_model(ruta_proyecto_test, Project))

    # --- 2. Prueba de save_models (JSON -> Modelo -> Agregar -> JSON) ---
    ruta_commands_test = PATHS.get_project_commands("audit_test")
    
    # Paso 1: Leemos los que ya estaban en el archivo
    #comandos_actuales = load_models(ruta_commands_test, Command)
    
    # Paso 2: Agregamos los nuevos a la lista en Python
    nuevos_commands = [
        Command(title="prueba0", command="prueba {prueba} prueba", description="prueba", tags=["prueba", "prueba"], scope=Scope.PRIVATE),
        Command(title="prueba0", command="prueba {prueba} prueba", description="prueba", tags=["prueba", "prueba"], scope=Scope.GLOBAL)
    ]
    #comandos_actuales.extend(nuevos_commands)
    
    # Paso 3: Guardamos la lista unificada
    save_models(ruta_commands_test, nuevos_commands, Command)
    #print("Comandos guardados y vueltos a leer:", load_models(ruta_commands_test, Command))

    #print("1. Comandos globales:", load_models(PATHS.GLOBAL_COMMANDS_FILE, Command))
    #Command.title/command/description/tags/scope

    #print("2. Variables audit1:", load_models(PATHS.get_project_vars("audit1"), Variable))
    #var.key/value (Lista de Variable)

    #print("3. Proyecto audit1:", load_single_model(PATHS.get_project_metafile("audit1"), Project))
    #Project.name/description/status/created (Lista de Project)

    #Con textos directos
    #campos = ["Gobuster directorios", "gobuster dir -u http://{RHOST}", "web", "fuzzing"]
    #print(fuzzy_matches("gobustre", campos))
    #print(fuzzy_matches("wireshark", campos)) # False

    # Busqueda básica sobre comandos 
    #comandos = load_models(PATHS.GLOBAL_COMMANDS_FILE, Command)
    #query = "nmap"
    #resultados = [
    #    c.title for c in comandos
    #    if fuzzy_matches(query, [c.title, c.command, c.description] + c.tags)
    #]
    #print(f"Comandos encontrados para '{query}':", resultados)

    #variables_dict = PATHS.get_project_vars("audit1")
    #variables_model = load_models(variables_dict, Variable)
    #print(variables_model)
    #print(interpolate_text("Prueba {RHOST} prueba", variables_model))