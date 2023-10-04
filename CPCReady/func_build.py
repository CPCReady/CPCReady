import os
import sys
import datetime
import shutil
import subprocess
import yaml
from CPCReady import common as cm

def create():

    # Check is cfg project exist
    if not cm.fileExist(cm.CFG_PROJECT):
        cm.msgError(f"The project configuration file does not exist ({cm.CFG_PROJECT})")
        # cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
        sys.exit(1)

    # load data cfg project
    with open(cm.CFG_PROJECT, 'r') as file:
        data = yaml.safe_load(file)


    NUMBER_CONCAT_FILES  = sum(1 for item in data['spec']['files'] if item.get('kind') == 'bas' and item.get('concat') == True)
    COUNT                = 0
    PATH_DISC            = "out"
    PATH_SRC             = "src"
    PATH_DSK             = "dsk"
    PATH_ASSETS          = "assets"
    PROJECT_NOT_SECTIONS = ["PROJECT", "CONCATENATE", "RVM"]
    PROJECT_NAME         = data['project']['data'].get('name', 'No project mame')
    PROJECT_AUTHOR       = data['project']['data'].get('author', 'No author mame')
    PROJECT_RVM_SYSTEM   = data['project']['rvm'].get('system')
    PROJECT_RVM_DESKTOP  = data['project']['rvm'].get('rvm_path')
    PROJECT_RVM_MODEL    = data['project']['rvm'].get('model')
    PROJECT_RVM_RUN      = data['project']['rvm'].get('run')
    PROJECT_CONCAT_OUT   = PATH_DISC + "/" + data['project']['concatenate'].get('out', 'PROJECT.BAS')
    PROJECT_DSK_FILE     = f"{PATH_DSK}/{PROJECT_NAME}.DSK"
    RVM_WEB              = "RVM.HTML"

    cm.showHeadDataProject("BUILD " + PROJECT_NAME)
    
    cm.removeContentDirectory(PATH_DISC)
    
    for folder in cm.subfolders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    cm.msgInfo("Check folders project: OK")
    
    createImageDisc(PROJECT_DSK_FILE)

    for file_data in data['spec']['files']:
        
        if file_data['kind'].upper() == 'BAS':
            COUNT = COUNT + 1
            if not cm.fileExist(f"{PATH_SRC}/{file_data['name']}"):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
            
            if not removeComments(f"{PATH_SRC}/{file_data['name']}", f"{PATH_DISC}/{file_data['name']}"):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
                
            if not convert2Dos(f"{PATH_DISC}/{file_data['name']}", f"{PATH_DISC}/{file_data['name']}"): 
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)

            if file_data['concat'] == True:
                if not concatFile(f"{PATH_DISC}/{file_data['name']}", PROJECT_CONCAT_OUT):
                    cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
                    if COUNT == NUMBER_CONCAT_FILES:
                       if not convert2Dos(PROJECT_CONCAT_OUT, PROJECT_CONCAT_OUT):
                           cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
                       if not addBas2ImageDisc(PROJECT_DSK_FILE, f"{PATH_DISC}/{file_data['name']}"):
                           cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
                    else:
                        if not addBas2ImageDisc(PROJECT_DSK_FILE, f"{PATH_DISC}/{file_data['name']}"): 
                            cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
                            
        elif file_data['kind'].upper() == 'ASCII':
            if not cm.fileExist(f"{PATH_SRC}/{file_data['name']}"):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
            if not addBas2ImageDisc(PROJECT_DSK_FILE, f"{PATH_SRC}/{file_data['name']}"):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
        #     ##
        #     # Processing C files
        #     ## 
        #     elif file_data['kind'].upper() == 'C':
        #         if not fileExist(f"{PATH_SRC}/{file_data['name']}"): endCompilation("ERROR",start_time)
        #         if not compile(f"{PATH_SRC}/{file_data['name']}", f"{PATH_DISC}/", f"{file_data['address']}",
        #                 f"{file_data['include']}"): endCompilation("ERROR",start_time)
                
        #         if not addBinaryFileDsk(f"{PROJECT_DSK_FILE}", f"{PATH_DISC}/" + getFile(f"{PATH_DISC}/{file_data['name']}") + ".bin"): endCompilation("ERROR",start_time)

        #     ##
        #     # Processing images files
        #     ## 
        #     elif file_data['kind'].upper() == 'IMAGE':
        #         if not fileExist(f"{PATH_ASSETS}/{file_data['name']}"): endCompilation("ERROR",start_time)
        #         if not img2scr(f"{PATH_ASSETS}/{file_data['name']}", f"{file_data['mode']}", "assets", ""): endCompilation("ERROR",start_time)
        #         NEW_FILE = getFile(f"{PATH_ASSETS}/{file_data['name']}").upper()
        #         if not addBinaryFileDsk(f"{PROJECT_DSK_FILE}", f"{PATH_DISC}/{NEW_FILE}.SCR"): endCompilation("ERROR",start_time)
        #         if not file_data['pal']:
        #             remove(f"{PATH_DISC}/{NEW_FILE}.PAL")
        #     ##
        #     # Processing sprites files
        #     ## 
        #     elif file_data['kind'].upper() == 'SPRITE':
        #         if not fileExist(f"{PATH_ASSETS}/{file_data['name']}"): endCompilation("ERROR",start_time)
        #         if not img2spr(f"{PATH_ASSETS}/{file_data['name']}",f"{file_data['mode']}",f"{file_data['width']}",f"{file_data['height']}","assets"): endCompilation("ERROR",start_time)

        # if PROJECT_RVM_SYSTEM == "web":
        #     rvm_web(PROJECT_RVM_MODEL,f"dsk/{PROJECT_NAME}.DSK",PROJECT_RVM_RUN,PROJECT_NAME,RVM_WEB)
        # elif PROJECT_RVM_SYSTEM == "desktop":
        #     if PROJECT_RVM_DESKTOP == "":
        #         messageError("There is no path to Retro virtual machine")
        #         endCompilation("ERROR",start_time)
        #     if not os.path.isfile(PROJECT_RVM_DESKTOP):
        #         messageError(PROJECT_RVM_DESKTOP +"[red] ==> FILE DOES NOT EXIST")
        #         endCompilation("ERROR",start_time)
        #     if not rvm_desktop(PROJECT_RVM_MODEL,f"{PWD}/dsk/{PROJECT_NAME}.DSK",PROJECT_RVM_RUN,PROJECT_NAME,PROJECT_RVM_DESKTOP):endCompilation("ERROR",start_time)

        # ##
        # # Show end compilation
        # ##  

        # endCompilation("OK",start_time)


##
# Concatenate Bas file
#
# @param source: source file name
# @param output: output file name
##
def concatFile(source, output):
    with open(source, 'r') as origen_file:
        contenido_origen = origen_file.read()
    with open(output, 'a') as destino_file:
        destino_file.write(contenido_origen)
    os.remove(source)
    cm.msgInfo(f"Concat file {cm.getFileExt(source)} ==> {cm.getFileExt(output)}")
    return True

def convert2Dos(source, output):
    if not os.path.exists(source):
        cm.msgError(f"File {source} does not exist.")
        return False
    with open(source, 'r') as file:
        unix_lines = file.readlines()

    dos_lines = [line.rstrip('\n') + '\r\n' for line in unix_lines]

    with open(output, 'w') as file:
        file.writelines(dos_lines)

    files = cm.getFileExt(source)
    cm.msgInfo(f"Convert unix to dos: {source}")
    return True

##
# Remove comment lines
#
# @param source: source filename
# @param output: output filename
##
def removeComments(source, output):

    if not os.path.exists(source):
        cm.msgError(f"File {source} does not exist.")
        return False

    with open(source, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if not line.startswith("1'") and not line.startswith("1 '")]

    with open(output, 'w') as file:
        file.writelines(filtered_lines)
    file = cm.getFileExt(source)
    cm.msgInfo(f"Comments Removed: {file}")
    return True

def createImageDisc(imagefile):
    cm.rmFolder(imagefile)
    cmd = [cm.IDSK, imagefile, "-n"]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        if not os.path.isfile(imagefile):
            cm.msgError('Error generating disk image ' + cm.getFileExt(imagefile))
            cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)

def addBas2ImageDisc(imagefile, file):
    cmd = [cm.IDSK, imagefile, "-i", file, '-t', '0']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgInfo("Add file : " + cm.getFileExt(file) + " ==> " + cm.getFileExt(imagefile))
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        return False

def addBin2ImageDisc(imagefile, file):
    cmd = [cm.IDSK, imagefile, "-i", file, '-t', '1']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgInfo(cm.getFileExt(file)  + " ==> " +  cm.getFileExt(imagefile))
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        return False


# def addBinFileDsk(imagefile, file, laddress):
#     cmd = [cm.IDSK, f"{imagefile}", '-i', file, '-c', laddress, '-t', '1']
#     try:
#         output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
#         cm.msgInfo(cm.getFileExt(file)  + " ==> " +  cm.getFileExt(imagefile))
#         return True
#     except subprocess.CalledProcessError as e:
#         cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
#         return False

def extract2ImageDisc(imagefile, file):
    FNULL = open(os.devnull, 'w')
    cmd = [cm.IDSK, imagefile, "-g", file]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        return False