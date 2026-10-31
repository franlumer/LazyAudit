from models import *
import PATHS
import common
import json
from pathlib import Path

# Los modelos heredan common.CommonActions que es donde está add, modify, delete y remove
# permite que se los llame directamente con la acción y se evita pasar el Path. 
# Command.reead_all(), Variable.add(), etc.

class Scope(ScopeData):
    pass

class Command(CommandData, common.CommonActions):
    file_path = PATHS.COMMANDS_FILE
    @classmethod
    def change_scope(command):
        if command.scope == Scope.PRIVATE:
            command.scope = Scope.GLOBAL
        else:
            command.scope = Scope.PRIVATE
        #print(command)

class Variable(VariableData, common.CommonActions):
    file_path = PATHS.VARIABLES_FILE
    pass

class Project(ProjectData, common.CommonActions):

    @classmethod
    def modify(cls, new_project):
        old_project = cls.read_all()
        print(old_project)
        print(new_project)
        print(cls.file_path)

        if old_project[0] != new_project:
            common._save(cls.file_path, new_project)

        if cls.file_path.parent.name != new_project.name:
            project_dir = cls.file_path.parent
            project_dir.rename(project_dir.parent/new_project.name)
            cls.change(new_project.name)

        

    @classmethod
    def add(cls, new_project : "Project") -> None:
        base_files = ["commands.json", "findings.json", "hosts.json", "variables.json"]
        project_dir = Path(PATHS.PROJECTS_DIR/new_project.name)
        project_dir.mkdir(parents=True, exist_ok=True)
        for path in base_files: 
            Path(project_dir/path).touch()
        common._save(project_dir/"project.json", new_project)

    @classmethod
    def show(cls):
        print("[+] Proyecos disponibles")
        for i in PATHS.PROJECTS_DIR.iterdir():
            print(i.name)

    @classmethod
    def change(cls, new_project : str) -> None:
        with open(PATHS.CONFIG_FILE, "r") as f:
            data = json.load(f)
            active_project = data["project"]
        if active_project == new_project:
            print(f"[+] {new_project} activo")
            
        # Verifica que el pryecto al que se quiere cambiar realmente exista
        elif (PATHS.PROJECTS_DIR / new_project).exists():
            with open(PATHS.CONFIG_FILE, "w") as f:
                json.dump( {"project": new_project}, f, indent=4, ensure_ascii=False)
                print(f"[+] Proyecto cambiado a: {new_project}")
        else: 
            print(f"[!] Proyecto no existente")

    file_path = PATHS.PROJECT_FILE # No borrar


class Finding(FindingData, common.CommonActions):
    file_path = PATHS.FINDINGS_FILE
    pass

class Host(HostData, common.CommonActions):
    file_path = PATHS.HOSTS_FILE
    pass




#comando = Command(title="titulo1",command="ejecutar tal script",description="ejecuta el script tanto",tags=["ejecucion"],scope=Scope.GLOBAL)
#print(comando.description)
#Command.add(comando)

#comando = [d for d in common.read_all(PATHS.get_project_commands("audit_test"), Command) if d.title == "prueba0"]
#Command.change_scope(comando[0])