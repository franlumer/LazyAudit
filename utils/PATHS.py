from pathlib import Path

LAZYAUDIT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = LAZYAUDIT_DIR / "data"
#GLOBAL_COMMANDS_FILE = DATA_DIR / "global_commands.json"
#GLOBAL_VARS_FILE = DATA_DIR / "global_vars.json"
ACTUAL_PROJECT = "audit_test"
PROJECTS_DIR = DATA_DIR / "projects"
ACTUAL_PROJECT_DIR = DATA_DIR / "projects" / ACTUAL_PROJECT
GLOBALS = DATA_DIR / "globals"

#CHECKLISTS_DIR = DATA_DIR / "checklists"
#WORKFLOWS_DIR = DATA_DIR / "workflows"

print(LAZYAUDIT_DIR)
print(DATA_DIR)
print(ACTUAL_PROJECT)
print(PROJECTS_DIR)
print(ACTUAL_PROJECT_DIR)

