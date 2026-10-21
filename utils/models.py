from dataclasses import dataclass, field
from enum import Enum

class Scope:
    GLOBAL = 'global'
    PRIVATE = 'private'

@dataclass
class Command:
    title : str
    command : str
    description : str
    tags : list[str] = field(default_factory=list) # Para evitar que se compartan listas.
    scope : Scope = Scope.PRIVATE

@dataclass
class Variable:
    key : str
    value : str
    scope : Scope = Scope.PRIVATE
    description : str = ""

@dataclass
class Project:
    name : str
    description : str
    status : str
    created : str

@dataclass
class Finding: 
    host : str
    description : str
    vulns : list[str] = field(default_factory=list)
    severity : str = "low"

@dataclass
class Host: 
    ip : str
    hostname : str
    ports : list[str] = field(default_factory=list)
    services : list[str] = field(default_factory=list)

