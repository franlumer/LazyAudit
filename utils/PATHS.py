from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
GLOBAL_COMMANDS_FILE = DATA_DIR / "global_commands.json"
GLOBAL_VARS_FILE = DATA_DIR / "global_vars.json"
PROJECTS_DIR = DATA_DIR / "projects"
CHECKLISTS_DIR = DATA_DIR / "checklists"
WORKFLOWS_DIR = DATA_DIR / "workflows"

def get_project_dir(project_name : str) -> str:
    return PROJECTS_DIR/project_name

def get_project_metafile(project_name : str) -> str:
    return PROJECTS_DIR/project_name/"project.json"

def get_project_commands(project_name : str) -> str:
    return PROJECTS_DIR/project_name/"commands.json" 
    
def get_project_vars(project_name : str) -> str:
    return PROJECTS_DIR/project_name/"variables.json"
    
