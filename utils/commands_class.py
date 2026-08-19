import json

class Command:
    def __init__(self, title, command, tags, description):
        self.title = title
        self.command = command
        self.tags = tags
        self.description = description

    # Muestra el comando matcheado, función interna
    def show(self):
        return f"Title: {self.title}\nCommand: {self.command}\nTags: {self.tags}\nDecription: {self.description}\n"

    def add(self, title, command, tags, description):
        Command.commands.append(Command(title, command, tags, description))

    def search(query):
        query = query.lower() # query = lo que se busca
        found = False

        for i in Command.commands: # Recorre todos los command
            for value in vars(i).values(): # Muestra los valores de command
                if isinstance(value, list):
                    if any(query in str(item).lower() for item in value): # Si query está en algún valor de la lista 
                        found = True
                        return i.show()
                        break
                else:
                    if query in str(value).lower():
                        found = True
                        return i.show()
                        break  

        if found == False:
            print("Not found")

# Command.commands = [
#     Command("Nmap", "nmap -p- -sCSV <IP> -vvv", ["nmap", "ports"], "Basic nmap"),
#     Command("Nmap1", "nmap -sV -O <IP>", ["nmap", "os"], "OS detection"),
#    Command("Nikto", "nikto -h <IP>", ["web", "scanner"], "Web vuln. scan"),
# ]

# Command.add(_, "test", "test", ["test", "test"], "test")
# print(Command.search("test"))


# Command.show("")

with open(r"global_commands.json", 'r', encoding='utf-8') as a:
    json_dict = json.load(a)
    for command in json_dict:
        Command.title = command["title"]
        Command.command = command["command"]
        Command.tags = command["tags"]
        Command.description = command["description"]
        print(Command.title)
        print(Command.command)
        print(Command.description)
        print(Command.tags)

