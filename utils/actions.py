from models import *
from pathlib import Path
import common
import PATHS

class Scope(ScopeData):
    pass

class Command(CommandData):
    pass

class Variable(VariableData):
    pass

class Project(ProjectData):
    pass

class Finding(FindingData):
    pass

class Host(HostData):
    pass

comando = Command(title="title",command="command",description="descripion",tags=["tags"],scope=Scope.GLOBAL)
findings = common.json_to_model(Path("/home/luciano/github/personal/LazyAudit/data/projects/audit_test/findings.json"), Finding)

print(findings[0].severity)