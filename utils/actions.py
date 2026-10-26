from models import *
from pathlib import Path
import common
import PATHS
import json
import common

class Scope(ScopeData):
    pass

class Command(CommandData):
    def add(project_commands : Path, command):
        common.save(project_commands, command)

    def remove(project_commands : Path, command):
        pass

    def change_scope(command):
        if command.scope == Scope.PRIVATE:
            command.scope = Scope.GLOBAL
        else:
            command.scope = Scope.PRIVATE
        #print(command)

class Variable(VariableData):
    pass

class Project(ProjectData):
    pass

class Finding(FindingData):
    pass

class Host(HostData):
    pass

comando = Command(title="titulo1",command="ejecutar tal script",description="ejecuta el script tanto",tags=["ejecucion"],scope=Scope.GLOBAL)
print(comando.description)
#Command.add(comando)




#comando = [d for d in common.read_all(PATHS.get_project_commands("audit_test"), Command) if d.title == "prueba0"]
#Command.change_scope(comando[0])