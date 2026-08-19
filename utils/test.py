import json 
import dataclasses
from dataclasses import dataclass, field
import PATHS


@dataclass
class Command:
    title: str
    command: str
    tags: list = field(default_factory=list)
    description: str = ""

#{
#    "title": "Nmap UDP top ports",
#    "command": "nmap -sU --top-ports 100 {RHOST}",
#    "tags": ["recon", "nmap", "udp"],
#   "description": "Escaneo de los 100 puertos UDP más comunes"
#}
    @staticmethod
    def read_json():
        with open(PATHS.global_commands_file, 'r', encoding='utf-8') as json_file:
            json_dict = json.load(json_file) 
            return json_dict
        
    def matches(self, query: str) -> bool:
        query = query.lower()

        # Campos de texto simple
        text_fields = [self.title, self.command, self.description]
        if any(query in (field or "").lower() for field in text_fields): # si query está en algún valor de los text_fields
            return True

        # Tags (lista de strings)
        if any(query in tag.lower() for tag in self.tags): # si query está en algún valor de la lista de tags
            return True

        return False

    @staticmethod
    def search(query: str):
        json_dict = Command.read_json()

        commands = [Command(**i) for i in json_dict]
        results = [comm for comm in commands if comm.matches(query)]

        return results

    @staticmethod
    def remove(comm):
        if Command.search(comm):
            with open("data/global_commands.json", "r", encoding="utf-8") as json_file:
                json_dict = json.load(json_file)
                json_data = [item for item in json_dict if item.get('title') != comm]

                with open("data/global_commands.json", "w", encoding="utf-8") as json_file:
                            json.dump(json_data, json_file, indent=4, ensure_ascii=False)
        else:
            print("Not found")

Command.remove("Nmap básico")