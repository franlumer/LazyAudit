from pathlib import Path
from PATHS import PROJECTS_DIR
from dataclasses import dataclass, asdict
import json
from datetime import date
from rapidfuzz import fuzz

basic_project = ["commands.json", "findings.json", "project.json", "variables.json"]
project_name = "audit_test"

@dataclass
class Project:
    name: str
    description: str
    status: str
    created: str
        
    @staticmethod
    def create(project_data: "Project"):
        new_project_dir = PROJECTS_DIR + "/" + project_name
        # Crea la carpeta
        Path(f"{new_project_dir}").mkdir(parents=True, exist_ok=True)

        # Crea los archivos básicos
        for i in basic_project:
            Path(f"{new_project_dir}/{i}").touch()

        #Recibe objetos Command y los escribe en JSON
        json_data = asdict(project_data)
        with open(f"{new_project_dir}/project.json", "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

    @staticmethod
    def search(query: str, threshold: int = 70):
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





#Project.create(Project(name="test",description="test test test",status="test",created=date.today().isoformat()))
#Project.search("adassdasdas")