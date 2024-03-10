
import os
import sys
import datetime
import shutil
from rich import print
from rich.console import Console
from CPCReady import common as cm

from pprint import pprint
import inquirer

console = Console()

##
# Create project
#
# @param project: Project name
# @param model: CPC model
##

def project_validation(answers, current):
    if not current:
        raise inquirer.errors.ValidationError("", reason="The project name cannot be blank.")
    
    if os.path.exists(current):
        raise inquirer.errors.ValidationError("", reason="The project name already exists in this path.")
    
    if answers and answers.get("nomenclature83") and current is not None:
        if len(current) <= 8:
            return True
        else:
            raise inquirer.errors.ValidationError("", reason="Error: Project name cannot be more than 8 characters.")
    return True


def new():
    
    print()

    cm.showInfoTask(f"Create project...")

    questions = [
        inquirer.Confirm("nomenclature83", message="You want to activate the nomenclature 8:3?", default=True),
        inquirer.Text("project", message="Project name?", validate=project_validation),
    ]

    answers = inquirer.prompt(questions)



    project_name = answers.get("project")
    if not os.path.isabs(project_name):
        project_path = os.path.join(os.getcwd(), project_name)
    else:
        project_path = project_name

    os.makedirs(project_path, exist_ok=True)

    folder_project = project_name

    nomenclature63 = answers.get("nomenclature83")
    project = folder_project
        
    
    print()
    cm.msgCustom("CREATE", f"{folder_project}", "green")

    ########################################
    # CREATE PROJECT FOLDERS
    ########################################
    
    for folders in cm.subfolders:
        os.makedirs(f"{folder_project}/{folders}")
        cm.msgCustom("CREATE", f"{folder_project}/{folders}", "green")

    ########################################
    # CREATE TEMPLATES PROJECT
    ########################################
    
    ## PROJECT
    DATA = {'name': project,'nomenclature63': nomenclature63}
    cm.createTemplate("project.yml",   DATA, f"{folder_project}/{cm.PATH_CFG}/project.yml")
    cm.createTemplate("MAIN.BAS",      DATA, f"{folder_project}/{cm.PATH_SRC}/MAIN.BAS")


    print()
    console.print(f"🚀  Successfully creeated project [green]{project}[/]")
    print()
    console.print(f"👉  [yellow]Thank you for using CPCReady[/]")
    print()
