import os
import sys
import datetime
import shutil

from CPCReady import common as cm



##
# Create project
#
# @param project: Project name
# @param model: CPC model
##

def create(project):

    folder_project = f"{project}"
    cm.showHeadDataProject(project)

    if os.path.exists(folder_project) and os.path.isdir(folder_project):
        cm.msgError(f"The {folder_project} project name exists on this path.")
        sys.exit(1)
        # cm.endCreteProject("ERROR")
    else:
        os.makedirs(f"{folder_project}")
        cm.msgInfo(f"Project Name: {folder_project}")

    # cm.msgInfo("CPC Model: " + str(model))

    ########################################
    # CREATE PROJECT FOLDERS
    ########################################
    for folders in cm.subfolders:
        os.makedirs(f"{folder_project}/{folders}")
        cm.msgInfo(f"     - {folders}")

    ########################################
    # CREATE TEMPLATES PROJECT
    ########################################
    
    ## PROJECT
    DATA = {'name': project}
    cm.createTemplate("project.cfg",   DATA, f"{folder_project}/{cm.PATH_CFG}/project.cfg")
    cm.createTemplate("emulators.cfg", DATA, f"{folder_project}/{cm.PATH_CFG}/emulators.cfg")
    cm.createTemplate("images.cfg",    DATA, f"{folder_project}/{cm.PATH_CFG}/images.cfg")
    cm.createTemplate("sprites.cfg",   DATA, f"{folder_project}/{cm.PATH_CFG}/sprites.cfg")
    cm.createTemplate("MAIN.BAS",      DATA, f"{folder_project}/{cm.PATH_SRC}/MAIN.BAS")
    cm.createTemplate("MAIN.UGB",      DATA, f"{folder_project}/{cm.PATH_SRC}/MAIN.UGB")

    cm.msgInfo(f"Create Templates.")

    if sys.platform != "win64" or sys.platform != "win32":
        cm.createTemplate("Makefile", DATA, f"{folder_project}/Makefile")
        cm.msgInfo(f"Create Makefile.")

    cm.showFoodDataProject(f"{project} PROJECT SUCCESSFULLY CREATED.", 0)
