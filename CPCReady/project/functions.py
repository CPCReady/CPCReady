import sys
import os
import datetime
import shutil
from jinja2 import Template
import CPCReady.common as common

##
# Create project
#
# @param project: Project name
# @param model: CPC model
##

def create(project,model,testing):

    if sys.platform == "win64" or sys.platform == "win32":
        user = os.getenv('USERNAME')
    else:
        user = os.getenv('USER') or os.getenv('LOGNAME')

    folder_project = f"{project}"
    
    current_datetime = datetime.datetime.now()
    APP_PATH = os.path.dirname(os.path.abspath(__file__))

    common.banner(model)
    common.showHeadDataProject(project)

    if os.path.exists(folder_project) and os.path.isdir(folder_project):
        common.msgError(f"The {folder_project} project name exists on this path.")
        common.showFoodDataProject("The project could not be created.",1)
        sys.exit(1)
        # common.endCreteProject("ERROR")
    else:
        os.makedirs(f"{folder_project}")
        common.msgInfo(f"Create Project: {folder_project}")

    common.msgInfo("CPC Model: " + str(model))

    ########################################
    # CREATE TEMPLATE TESTING RVM WEB
    ########################################
    if testing == "web":
        context = {
            'name': project,
            'cpc': model,
            'dsk': f"dsk/{project}.dsk",
            'run': 'run"MAIN.BAS"'
        }

        with open(APP_PATH + "/templates/cpc.j2", 'r') as file:
            template_string = file.read()
        template = Template(template_string)
        rendered_template = template.render(context)
        with open(folder_project + "/cpc.html", 'w') as file:
            file.write(rendered_template)

        common.msgInfo(f"Testing Project: Retro Virtual Machine Web")

    ########################################
    # CREATE PROJECT FOLDERS
    ########################################
    for folders in common.subfolders:
        os.makedirs(f"{folder_project}/{folders}")
        common.msgInfo(f"Create folder: {folder_project}/{folders}")

    current_datetime = datetime.datetime.now()
    
    ########################################
    # CREATE TEMPLATE PROJECT CONFIGURATIONS
    ########################################
    context_CFG = {
        'name': project,
        'user': user,
        'testing': testing,
        'rvm_path': ""
    }

    with open(APP_PATH + "/templates/cpc_yaml.j2", 'r') as file:
        template_string = file.read()
    template = Template(template_string)
    rendered_template = template.render(context_CFG)
    with open(folder_project + common.CFG_PROJECT, 'w') as file:
        file.write(rendered_template)

    common.msgInfo(f"Configuration Project: {folder_project}" + common.CFG_PROJECT)

    context = {
        'name': project,
        'user': user,
        'fecha': current_datetime
    }

    with open(APP_PATH + "/templates/MAIN.BAS.j2", 'r') as file:
        template_string = file.read()
    template = Template(template_string)
    rendered_template = template.render(context)
    with open(folder_project + "/src/MAIN.BAS", 'w') as file:
        file.write(rendered_template)

    common.msgInfo(f"Create BASIC template: {folder_project}/src/MAIN.BAS")

    shutil.copyfile(f"{folder_project}/src/MAIN.BAS", f"{folder_project}/src/MAIN.ugbasic")

    common.msgInfo(f"Create ugBASIC template: {folder_project}/src/MAIN.ugbasic")

    if sys.platform != "win64" or sys.platform != "win32":
        shutil.copyfile(APP_PATH + "/templates/Makefile", f"{folder_project}/Makefile")
        common.msgInfo(f"Create Makefile: {folder_project}/Makefile")

    common.showFoodDataProject(f"{project} PROJECT SUCCESSFULLY CREATED.",0)