# ===================== IMPORTS =====================
from dataclasses import dataclass, field
import json
import os
# ==================== CONSTANTS ====================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
global_commands_file = os.path.join(BASE_DIR,"global_commands.json")
# ===================== CLASES ======================
@dataclass
class Command:
    title: str
    command: str
    tags: list = field(default_factory=list)
    description: str = ""

with open(global_commands_file, 'r', encoding='utf-8') as json_file:
    json_dict = json.load(json_file)

commands = [Command(**i) for i in json_dict]

for i in commands:
    if i.title == "Nmap básico2":
        print(i)
        break
