from model_command import Command
import utils.model_projects as model_projects
import PATHS

PROJECT = "/audit1/commands.json"
PROJECT_COMMANDS_FILE = PATHS.PROJECTS_DIR + PROJECT

while True:
    a = input()
    if a == "show all":
        Command.show_all(PROJECT_COMMANDS_FILE)
    elif a == "1":
        PROJECT = "/audit1/commands.json"
        PROJECT_COMMANDS_FILE = PATHS.PROJECTS_DIR + PROJECT

    elif a == "2":
        PROJECT = "/audit2/commands.json"
        PROJECT_COMMANDS_FILE = PATHS.PROJECTS_DIR + PROJECT