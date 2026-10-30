from pathlib import Path

# ========== LAZYAUDIT PATHS ==========
LAZYAUDIT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = LAZYAUDIT_DIR/"data"
GLOBAL_DIR = LAZYAUDIT_DIR/"globals"

# ========== PROJECTS PATHS ===========
PROJECTS_DIR = DATA_DIR / "projects"

PROJECT = "audit_test1"
ACTIVE_PROJECT_DIR = DATA_DIR/"projects"/PROJECT 
COMMANDS_FILE = ACTIVE_PROJECT_DIR/"commands.json"
VARIABLES_FILE = ACTIVE_PROJECT_DIR/"variables.json"
PROJECT_FILE = ACTIVE_PROJECT_DIR/"project.json"
FINDINGS_FILE = ACTIVE_PROJECT_DIR/"findings.json"
HOSTS_FILE = ACTIVE_PROJECT_DIR/"hosts.json"
#CHECKLISTS_DIR = ACTIVE_PROJECT_DIR/"checklists"
#WORKFLOWS_DIR = ACTIVE_PROJECT_DIR/"workflows"

# ========== GLOBAL PATHS ==========
GLOBAL_COMMANDS_FILE = DATA_DIR/"global_commands.json"
GLOBAL_VARS_FILE = DATA_DIR/"global_vars.json"
#GLOBAL_CHECKLISTS_DIR = DATA_DIR / "checklists"
#GLOBAL_WORKFLOWS_DIR = DATA_DIR / "workflows"



