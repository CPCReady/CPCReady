import os
import sys
import datetime
import shutil
from jinja2 import Template
from CPCReady import common as cm

##
# Create project
#
# @param project: Project name
# @param model: CPC model
##

def create(project, model):
    if sys.platform == "win64" or sys.platform == "win32":
        user = os.getenv('USERNAME')
    else:
        user = os.getenv('USER') or os.getenv('LOGNAME')

    folder_project = f"{project}"

    current_datetime = datetime.datetime.now()
    APP_PATH = os.path.dirname(os.path.abspath(__file__))

    cm.banner(model)
    cm.showHeadDataProject(project)

    if os.path.exists(folder_project) and os.path.isdir(folder_project):
        cm.msgError(f"The {folder_project} project name exists on this path.")
        cm.showFoodDataProject("The project could not be created.", 1)
        sys.exit(1)
        # cm.endCreteProject("ERROR")
    else:
        os.makedirs(f"{folder_project}")
        cm.msgInfo(f"Create Project: {folder_project}")

    cm.msgInfo("CPC Model: " + str(model))

    # ########################################
    # # CREATE TEMPLATE TESTING RVM WEB
    # ########################################
    # if testing == "rvm-web":
    #     context = {
    #         'name': project,
    #         'cpc': model,
    #         'dsk': f"dsk/{project}.dsk",
    #         'run': 'run"MAIN.BAS"'
    #     }

    #     with open(APP_PATH + "/templates/cpc.j2", 'r') as file:
    #         template_string = file.read()
    #     template = Template(template_string)
    #     rendered_template = template.render(context)
    #     with open(folder_project + "/cpc.html", 'w') as file:
    #         file.write(rendered_template)

    #     cm.msgInfo(f"Testing Project: Retro Virtual Machine Web")

    ########################################
    # CREATE PROJECT FOLDERS
    ########################################
    for folders in cm.subfolders:
        os.makedirs(f"{folder_project}/{folders}")
        cm.msgInfo(f"Create folder: {folder_project}/{folders}")

    current_datetime = datetime.datetime.now()

    ########################################
    # CREATE TEMPLATE PROJECT CONFIGURATIONS
    ########################################
    context_CFG = {
        'name': project,
        'user': user,
        'rvm_path': ""
    }

    with open(APP_PATH + "/templates/cpc_yaml.j2", 'r') as file:
        template_string = file.read()
    template = Template(template_string)
    rendered_template = template.render(context_CFG)
    with open(folder_project + cm.CFG_PROJECT, 'w') as file:
        file.write(rendered_template)

    cm.msgInfo(f"Configuration Project: {folder_project}" + cm.CFG_PROJECT)

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

    cm.msgInfo(f"Create BASIC template: {folder_project}/src/MAIN.BAS")

    shutil.copyfile(f"{folder_project}/src/MAIN.BAS", f"{folder_project}/src/MAIN.ugbasic")

    cm.msgInfo(f"Create ugBASIC template: {folder_project}/src/MAIN.ugbasic")

    if sys.platform != "win64" or sys.platform != "win32":
        shutil.copyfile(APP_PATH + "/templates/Makefile", f"{folder_project}/Makefile")
        cm.msgInfo(f"Create Makefile: {folder_project}/Makefile")

    cm.showFoodDataProject(f"{project} PROJECT SUCCESSFULLY CREATED.", 0)
