# ===================== IMPORTS =====================
from dataclasses import dataclass, field, asdict
import json
import os
import PATHS
from rapidfuzz import fuzz
# ===================== CLASES ======================
PROJECT = ""
PROJECT_COMMANDS_FILE = PATHS.PROJECTS_DIR + PROJECT

@dataclass
class Command:
    title: str
    command: str
    tags: list = field(default_factory=list)
    description: str = ""

    @staticmethod
    def _read_all(PROJECT_COMMANDS_FILE) -> list["Command"]:
        # Lee el JSON y devuelve una lista de instancias de Command
        # Si el json no existe devuelve una lista vacía
        if not os.path.exists(PROJECT_COMMANDS_FILE):
            return []
        with open(PATHS.GLOBAL_COMMANDS_FILE ,'r', encoding='utf-8') as json_file:
            global_json_dict = []
            try: global_json_dict = json.load(json_file)
            except json.JSONDecodeError:
                global_json_dict = []

        with open(PROJECT_COMMANDS_FILE, 'r', encoding='utf-8') as json_file:
            project_json_dict = []
            try: project_json_dict = json.load(json_file)
            except json.JSONDecodeError:
                project_json_dict = []

        if global_json_dict or project_json_dict:
            global_json_dict.extend(project_json_dict)
            print(global_json_dict)
        return [Command(**item) for item in global_json_dict]

    @staticmethod
    def _write_all(commands: list["Command"]) -> None:
        #Recibe objetos Command y los escribe en JSON
        json_data = [asdict(c) for c in commands]
        with open(PROJECT_COMMANDS_FILE, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

    def matches(self, query: str, threshold: int = 70) -> bool:
        query = query.lower()
        text_fields = [self.title, self.command, self.description] + self.tags

        for text_field in text_fields:
            text_field = (text_field or "").lower()
            
            if query in text_field:
                return True
            
            score = fuzz.partial_ratio(query, text_field)
            if score >= threshold:
                return True

        return False

    @staticmethod
    # Para debug
    def show_all(PROJECT_COMMANDS_FILE):
        for comm in Command._read_all(PROJECT_COMMANDS_FILE):
            print(comm)

    @staticmethod
    def search(query: str) -> list["Command"]:
        commands = Command._read_all()
        result = [comm for comm in commands if comm.matches(query)]
        if result: 
            for i in result:
                print(i)
        else:
            print("[!] Not Found")

    @staticmethod
    def add(comm: "Command"):
        commands = Command._read_all()
        if any(c.title == comm.title for c in commands):
            print("[!] Existing command")
            return
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

    @staticmethod
    def _search_by_title(title: str) -> "Command | None":
        commands = Command._read_all()
        for command in commands:
            if command.title == title:
                return command
        return None

    # Busca según el título por lo que hay que extraerlo 
    # del campo en la TUI y hay que cargarlo ahí
    @staticmethod
    # modify(titulo_a_buscar, Command(completo))
    def modify(title: str, new_command: "Command"):
        old_command = Command._search_by_title(title) #Command()

        if old_command is None:
            print("[!] Not Found")
            return
        else:
            old_command_id = Command._find_index_by_title(title)
            commands_list = Command._read_all()

            left_commands_list, right_commands_list = commands_list[:old_command_id], commands_list[old_command_id+1:]
            left_commands_list.append(new_command)
            left_commands_list.extend(right_commands_list)

            Command._write_all(left_commands_list)

    # en teoría ya funciona, hay que usarlo para modify. que parta la lista en dos, donde hay que modificar el comando, 
    # agregue el comando a la primer mitad y agregue la segunda mitad
    @staticmethod
    def _find_index_by_title(title: str) -> int | None:
        commands = Command._read_all()
        for i, c in enumerate(commands):
            if c.title == title:
                return i 
        return None
        
#Command.modify("Nmap UDP top ports", Command(title="test", description="test", tags=["test", "test"], command="test"))
#Command.search("nnap todo")
#Command._find_index_by_title("Nmap scripts default")

#print(Command._read_all())
