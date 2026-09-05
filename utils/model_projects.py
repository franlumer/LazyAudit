from pathlib import Path
from PATHS import PROJECTS_DIR
from dataclasses import dataclass, asdict
import json
from datetime import date
from rapidfuzz import fuzz
import os
import PATHS

basic_project = ["commands.json", "findings.json", "project.json", "variables.json"]
project_name = "audit_test1"

@dataclass
class Project:
    name: str
    description: str
    status: str
    created: str

    def write(project_data : "Project", new_project_dir):
        json_data = asdict(project_data)
        with open(f"{new_project_dir}/project.json", "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

    @staticmethod
    def create(project_data : "Project"):
        new_project_dir = PROJECTS_DIR + "/" + project_name
        # Crea la carpeta
        Path(f"{new_project_dir}").mkdir(parents=True, exist_ok=True)

        # Crea los archivos básicos
        for i in basic_project:
            Path(f"{new_project_dir}/{i}").touch()

        #Recibe objetos Project y los escribe en JSON
        Project.write(project_data, new_project_dir)

    @staticmethod
    def search(query: str, threshold: int = 70) -> "dir":
        query = query.lower()

        best_match = None
        best_score = 0

        # Recorre las carpetas de los proyectos
        for path in Path(PROJECTS_DIR).iterdir():
            if not path.is_dir():
                continue
            name = path.name.lower()
            # Match exacto -> devuelve directo, no hace falta seguir buscando
            if name == query:
                return path

            # Match medio -> se queda con el mejor score
            score = fuzz.ratio(query, name)
            if score > best_score:
                best_score = score
                best_match = path

        if best_match and best_score >= threshold:
            return best_match
        return None

    @staticmethod
    def modify(query : "str", name : str = None, description : str = None, status : str = None, created : date = None):
        to_modify = str(Project.search(query))
        new_project_data = {"name": name, "description": description, "status": status, "created": created}

        with open(f"{to_modify}/project.json", 'r', encoding='utf-8') as json_file:
            project_json_dict = []
            try: project_json_dict = json.load(json_file)
            except json.JSONDecodeError:
                project_json_dict = []    

        for clave in project_json_dict:
            if project_json_dict[clave] != new_project_data[clave]:
                project_json_dict[clave] = new_project_data[clave]

        Project.write(Project(**project_json_dict), to_modify)


# No funciona con el 2 porque está vacío pero en teoría debería funcinar porque al crear no se crean vacíos
Project.modify("audit1", "project1", "asdasdasd", "open", "04-09-2026")
#Project.create(Project(name="test",description="test test test",status="test",created=date.today().isoformat()))
#Project.search("adassdasdas")