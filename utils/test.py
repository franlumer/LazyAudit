from models import Variable, Command, Project, Finding, Host, Scope

var = Variable(key="test", value="test", scope=Scope.PRIVATE, description="test")

print(var.key)