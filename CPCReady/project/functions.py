import sys
import os
import datetime
from common import *


def create(project, model):

    if sys.platform == "win64" or sys.platform == "win32":
        user = os.getenv('USERNAME')
    else:
        user = os.getenv('USER') or os.getenv('LOGNAME')

    folder_project = f"{project}"
    subfolders = ["assets", "out", "dsk", "src"]
    current_datetime = datetime.datetime.now()

    banner(6128)

    # if os.path.exists(folder_project) and os.path.isdir(folder_project):
    #     msgError(f"The {folder_project} folder exist")
    #     endCreteProject("ERROR")
    # else:
    #     os.makedirs(f"{folder_project}")
    #     msgInfo(f"{folder_project}")

    # for folders in subfolders:
    #     os.makedirs(f"{folder_project}/{folders}")
    #     msgInfo(f"{folder_project}/{folders}")

    # cretateTemplateProject(folder_project, folder_project, user)
    # cretateTemplateBas(folder_project, folder_project, user, current_datetime)

    # endCreteProject("OK")


def cretateTemplateProject(project_folder, name, user):
    APP_PATH = os.path.dirname(os.path.abspath(__file__))
    context = {
        'name': name,
        'user': user
    }

    with open(APP_PATH + "/templates/cpc_yaml.j2", 'r') as file:
        template_string = file.read()
    template = Template(template_string)
    rendered_template = template.render(context)
    with open(project_folder + "/CPC.YAML", 'w') as file:
        file.write(rendered_template)

    msgInfo(f"{project_folder}/CPC.YAML")


def cretateTemplateBas(project_folder, name, user, fecha):
    APP_PATH = os.path.dirname(os.path.abspath(__file__))
    context = {
        'name': name,
        'user': user,
        'fecha': fecha
    }

    with open(APP_PATH + "/templates/MAIN.BAS.j2", 'r') as file:
        template_string = file.read()
    template = Template(template_string)
    rendered_template = template.render(context)
    with open(project_folder + "/src/MAIN.BAS", 'w') as file:
        file.write(rendered_template)

    msgInfo(f"{project_folder}/src/MAIN.BAS")
