from models import *
import PATHS
import common

class Scope(ScopeData):
    pass

class Command(CommandData, common.CommonActions):
    file_path = PATHS.COMMANDS_FILE
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
    file_path = PATHS.PROJECT_FILE
    pass

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