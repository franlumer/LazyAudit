from dataclasses import dataclass, field
from enum import Enum

class ScopeData:
    GLOBAL = 'global'
    PRIVATE = 'private'

@dataclass
class CommandData:
    title : str
    command : str
    description : str
    tags : list[str] = field(default_factory=list) # Para evitar que se compartan listas.
    scope : ScopeData = ScopeData.PRIVATE

@dataclass
class VariableData:
    key : str
    value : str
    scope : ScopeData = ScopeData.PRIVATE
    description : str = ""

@dataclass
class ProjectData:
    name : str
    description : str
    status : str
    created : str

@dataclass
class FindingData: 
    host : str
    description : str
    vulns : list[str] = field(default_factory=list)
    severity : str = "low"

@dataclass
class HostData: 
    ip : str
    hostname : str
    ports : list[str] = field(default_factory=list)
    services : list[str] = field(default_factory=list)

