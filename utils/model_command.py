# ===================== IMPORTS =====================
from dataclasses import dataclass, field, asdict
import json
import os
import PATHS
# ===================== CLASES ======================
@dataclass
class Command:
    title: str
    command: str
    tags: list = field(default_factory=list)
    description: str = ""

    @staticmethod
    def _read_all() -> list["Command"]:
        #Lee el JSON y devuelve objetos Command
        with open(PATHS.global_commands_file, 'r', encoding='utf-8') as json_file:
            json_dict = json.load(json_file)
        return [Command(**item) for item in json_dict]

    @staticmethod
    def _write_all(commands: list["Command"]) -> None:
        #Recibe objetos Command y los escribe en JSON
        json_data = [asdict(c) for c in commands]
        with open(PATHS.global_commands_file, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

    def matches(self, query: str) -> bool:
        query = query.lower()
        text_fields = [self.title, self.command, self.description]
        if any(query in (field or "").lower() for field in text_fields):
            return True
        if any(query in tag.lower() for tag in self.tags):
            return True
        return False

    @staticmethod
    def show_all():
        for comm in Command._read_all():
            print(comm)

    @staticmethod
    def search(query: str) -> list["Command"]:
        commands = Command._read_all()
        return [comm for comm in commands if comm.matches(query)]

    @staticmethod
    def add(comm: "Command"):
        commands = Command._read_all()
        commands.append(comm)
        Command._write_all(commands)

    @staticmethod
    def remove(title: str):
        commands = Command._read_all()
        filtered = [c for c in commands if c.title != title]

        if len(filtered) == len(commands):
            print("Not found")
            return

        Command._write_all(filtered)

    # Busca según el título por lo que hay que extraerlo 
    # del campo en la TUI y hay que cargarlo ahí
    @staticmethod
    def modify(title: str, new_command):
        old_command = Command.search(title) # Command()
        if old_command.title != new_command.title:
            pass
        if old_command.command != new_command.command:
            pass
        if old_command.description != new_command.description:
            pass
        if old_command.tags != new_command.tags:
            pass

print(Command.search("Nmap todos los puertos"))