import sys
import os
import datetime
import subprocess
import shutil
import json
from jinja2 import Template
import CPCReady.common as common

##
# Create SCR image
#
# @param project: Project name
# @param model: CPC model
##

def create(filename, mode, fileout, dsk):

    if common.TEMP_PATH is not None:
        IMAGE_TEMP_PATH = common.TEMP_PATH + "." + os.path.basename(filename)
    else:
        IMAGE_TEMP_PATH = common.PWD + "." + os.path.basename(filename)
        
    IMAGE_TMP_FILE = os.path.basename(os.path.splitext(filename)[0])
    IMAGE_TMP_JSON = IMAGE_TEMP_PATH + "/" + IMAGE_TMP_FILE+".json"
    
    if os.path.exists(IMAGE_TEMP_PATH) and os.path.isdir(IMAGE_TEMP_PATH):
        shutil.rmtree(IMAGE_TEMP_PATH)
        
    if dsk:
        cmd = [common.MARTINE, '-in', filename, '-mode', str(mode), '-out', IMAGE_TEMP_PATH, '-json','-dsk']
    else:
        cmd = [common.MARTINE, '-in', filename, '-mode', str(mode), '-out', IMAGE_TEMP_PATH, '-json']
    
    try:
        if fileout:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            if not os.path.exists(fileout):
                os.makedirs(fileout)
            if not dsk:
                shutil.copy2(os.path.join(IMAGE_TEMP_PATH, IMAGE_TMP_FILE.upper() + '.PAL'), fileout)
                shutil.copy2(os.path.join(IMAGE_TEMP_PATH, IMAGE_TMP_FILE.upper() + '.SCR'), fileout)
                common.msgInfo(f"Create SCREEN File: {fileout}/{IMAGE_TMP_FILE.upper()}.SCR")
        else:
            subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        common.msgError(f'Error ' + common.getFileExt(filename) + f' executing command: {e.output.decode()}')
        return False

    # Open JSON file
    with open(IMAGE_TMP_JSON) as f:
        data = json.load(f)

    sw_palette = str(data['palette'])
    hw_palette = str(data['hardwarepalette'])
    
#     # Remove single quotes and brackets
    


    if dsk:
        if not os.path.exists(fileout):
            os.makedirs(fileout)
        shutil.copy2(os.path.join(IMAGE_TEMP_PATH, IMAGE_TMP_FILE.upper() + '.DSK'), fileout + '/' + IMAGE_TMP_FILE.upper() + '.DSK')
        common.msgInfo(f"Create IMAGE File: {fileout}/{IMAGE_TMP_FILE.upper()}.DSK")
        
    common.msgInfo(f"       SW PALETTE : {sw_palette}")
    common.msgInfo(f"       HW PALETTE : {hw_palette}")
    
    # Delete temporal file
    shutil.rmtree(IMAGE_TEMP_PATH)
    return True


# def create(project,model,testing):

#     if sys.platform == "win64" or sys.platform == "win32":
#         user = os.getenv('USERNAME')
#     else:
#         user = os.getenv('USER') or os.getenv('LOGNAME')

#     folder_project = f"{project}"
    
#     current_datetime = datetime.datetime.now()
#     APP_PATH = os.path.dirname(os.path.abspath(__file__))

#     common.banner(model)
#     common.showHeadDataProject(project)

#     if os.path.exists(folder_project) and os.path.isdir(folder_project):
#         common.msgError(f"The {folder_project} project name exists on this path.")
#         common.showFoodDataProject("The project could not be created.",1)
#         sys.exit(1)
#         # common.endCreteProject("ERROR")
#     else:
#         os.makedirs(f"{folder_project}")
#         common.msgInfo(f"Create Project: {folder_project}")

#     common.msgInfo("CPC Model: " + str(model))

#     ########################################
#     # CREATE TEMPLATE TESTING RVM WEB
#     ########################################
#     if testing == "web":
#         context = {
#             'name': project,
#             'cpc': model,
#             'dsk': f"dsk/{project}.dsk",
#             'run': 'run"MAIN.BAS"'
#         }

#         with open(APP_PATH + "/templates/cpc.j2", 'r') as file:
#             template_string = file.read()
#         template = Template(template_string)
#         rendered_template = template.render(context)
#         with open(folder_project + "/cpc.html", 'w') as file:
#             file.write(rendered_template)

#         common.msgInfo(f"Testing Project: Retro Virtual Machine Web")

#     ########################################
#     # CREATE PROJECT FOLDERS
#     ########################################
#     for folders in common.subfolders:
#         os.makedirs(f"{folder_project}/{folders}")
#         common.msgInfo(f"Create folder: {folder_project}/{folders}")

#     current_datetime = datetime.datetime.now()
    
#     ########################################
#     # CREATE TEMPLATE PROJECT CONFIGURATIONS
#     ########################################
#     context_CFG = {
#         'name': project,
#         'user': user,
#         'testing': testing,
#         'rvm_path': ""
#     }

#     with open(APP_PATH + "/templates/cpc_yaml.j2", 'r') as file:
#         template_string = file.read()
#     template = Template(template_string)
#     rendered_template = template.render(context_CFG)
#     with open(folder_project + common.CFG_PROJECT, 'w') as file:
#         file.write(rendered_template)

#     common.msgInfo(f"Configuration Project: {folder_project}" + common.CFG_PROJECT)

#     context = {
#         'name': project,
#         'user': user,
#         'fecha': current_datetime
#     }

#     with open(APP_PATH + "/templates/MAIN.BAS.j2", 'r') as file:
#         template_string = file.read()
#     template = Template(template_string)
#     rendered_template = template.render(context)
#     with open(folder_project + "/src/MAIN.BAS", 'w') as file:
#         file.write(rendered_template)

#     common.msgInfo(f"Create BASIC template: {folder_project}/src/MAIN.BAS")

#     shutil.copyfile(f"{folder_project}/src/MAIN.BAS", f"{folder_project}/src/MAIN.ugbasic")

#     common.msgInfo(f"Create ugBASIC template: {folder_project}/src/MAIN.ugbasic")

#     if sys.platform != "win64" or sys.platform != "win32":
#         shutil.copyfile(APP_PATH + "/templates/Makefile", f"{folder_project}/Makefile")
#         common.msgInfo(f"Create Makefile: {folder_project}/Makefile")

#     common.showFoodDataProject(f"{project} PROJECT SUCCESSFULLY CREATED.",0)