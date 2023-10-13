import os
import sys
import datetime
import shutil
from jinja2 import Template
import subprocess
import yaml
from CPCReady import common as cm
import io
from ping3 import ping, verbose_ping


def executeFileM4BOARD(ip,file):
    FNULL = open(os.devnull, 'w')
    cmd = [cm.M4BOARD, "-x",ip,file]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgInfo("Execute " + cm.getFileExt(file) + " ==> M4 Board")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(file) + f' executing command: {e.output.decode()}')
        return False

def uploadFileM4BOARD(ip,file,folder):
    FNULL = open(os.devnull, 'w')
    cmd = [cm.M4BOARD, "-u",ip,file, folder, 0]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgInfo("Upload " + cm.getFileExt(file) + " ==> M4 Board")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(file) + f' executing command: {e.output.decode()}')
        return False

def execute(project,emulator):

    cm.validate_cfg(cm.CFG_PROJECT,cm.SECTIONS_PROJECT)
    cm.validate_cfg(cm.CFG_EMULATORS,cm.SECTIONS_EMULATOR)
    
    DATA_PROJECT   = cm.getData(cm.CFG_PROJECT)
    DATA_EMULATORS = cm.getData(cm.CFG_EMULATORS)

    PROJECT_NAME         = DATA_PROJECT.get('general','name',fallback="NONE")
    PROJECT_AUTHOR       = DATA_PROJECT.get('general','author',fallback="NONE")
    PROJECT_CDT          = DATA_PROJECT.get('CDT','name',fallback="NONE")
    PROJECT_DSK          = DATA_PROJECT.get('DSK','name',fallback="NONE")
    
    if PROJECT_NAME == "NONE":
        cm.msgError(f"project name in {cm.CFG_PROJECT} does not exist or is empty")
        sys.exit(1)
            
    if PROJECT_CDT == "NONE":
        cm.msgError(f"CDT name in {cm.CFG_PROJECT} does not exist or is empty")
        sys.exit(1)  
  
    if PROJECT_DSK == "NONE":
        cm.msgError(f"DSK name in {cm.CFG_PROJECT} does not exist or is empty")
        sys.exit(1)
    
    PROJECT_CDT_NAME     = f"{cm.PATH_DSK}/{PROJECT_CDT}"
    PROJECT_DSK_NAME     = f"{cm.PATH_DSK}/{PROJECT_DSK}"

    cm.showHeadDataProject(cm.getFileExt(PROJECT_DSK_NAME))
    
    if emulator == "rvm-web":   
        
        PROJECT_RVM_MODEL    = DATA_EMULATORS.get(emulator,'model',fallback="NONE")
        if PROJECT_RVM_MODEL == "NONE":
            cm.msgError(f"CPC model has not been selected in rvm-web from the {cm.CFG_EMULATORS} file")
            cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
        if not cm.validateCPCModel(PROJECT_RVM_MODEL):
            cm.msgError(f"CPC model {PROJECT_RVM_MODEL} not supported")
            cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)         
        PROJECT_RVM_RUN      = DATA_EMULATORS.get(emulator,'run',fallback="")
        EMULATOR             = f"Retro Virtual Machine WEB ({cm.TEMPLATE_RVM_WEB})"
        context = {
            'name': PROJECT_NAME,
            'model': PROJECT_RVM_MODEL,
            'dsk': f"{PROJECT_DSK_NAME}",
            'run': f'{PROJECT_RVM_RUN}'
        }
        cm.createTemplate("rvm-web.html", context, cm.PATH_CFG)
        cm.msgInfo(f"CPC Model  : {PROJECT_RVM_MODEL}")
        cm.msgInfo(f"RUN Command: {PROJECT_RVM_RUN}")
        cm.msgInfo(f"Emulator   : RVM Web ({cm.TEMPLATE_RVM_WEB})") 
           
    elif emulator == "rvm-desktop":   
        
        PROJECT_RVM_MODEL    = DATA_EMULATORS.get(emulator,'model',fallback="NONE")
        if PROJECT_RVM_MODEL == "NONE":
            cm.msgError(f"CPC model has not been selected in rvm-web from the {cm.CFG_EMULATORS} file")
            cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
        if not cm.validateCPCModel(PROJECT_RVM_MODEL):
            cm.msgError(f"CPC model {PROJECT_RVM_MODEL} not supported")
            cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)                
        PROJECT_RVM_RUN      = DATA_EMULATORS.get(emulator,'run',fallback="")
        PROJECT_RVM_PATH     = DATA_EMULATORS.get(emulator,'path',fallback="")
        
        if PROJECT_RVM_PATH != "":
            if cm.fileExist(PROJECT_RVM_PATH):
                cm.msgInfo(f"CPC Model  : {PROJECT_RVM_MODEL}")
                cm.msgInfo(f"RUN Command: {PROJECT_RVM_RUN}")
                cm.msgInfo(f"Emulator   : RVM Desktop ({PROJECT_RVM_PATH})")
                FNULL = open(os.devnull, 'w')
                try:
                    retcode = subprocess.Popen([PROJECT_RVM_PATH,"-i", PROJECT_DSK_NAME,"-b=cpc"+str(PROJECT_RVM_MODEL),"-c="+PROJECT_RVM_RUN + "\n"], stdout=FNULL, stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                    cm.msgError(f'{cm.getFileExt(PROJECT_DSK_NAME)} RELEASED WITH ERROR: {e.output.decode()}')
                    return False
            else:
                cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
        else:
            cm.msgError(f"RVM Desktop path does not exist in {cm.CFG_PROJECT}")
            cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
        
    elif emulator == "m4board":   
        
        PROJECT_M4_EXECUTE = DATA_EMULATORS.get(emulator,'execute',fallback="")
        PROJECT_M4_FOLDER  = DATA_EMULATORS.get(emulator,'folder',fallback="CPCReady")
        PROJECT_M4BOARD_IP = DATA_EMULATORS.get(emulator,'ip',fallback="NONE")
        
        if PROJECT_M4BOARD_IP == "NONE":
            cm.msgError(f"No ip found in {cm.CFG_EMULATORS} for M4 Board")
            cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
        if not cm.validateIP(PROJECT_M4BOARD_IP):
            cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
        if not ping(PROJECT_M4BOARD_IP):
            cm.msgError(f"No connect ==> {PROJECT_M4BOARD_IP}")
            cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
        else:
             cm.msgInfo(f"Connect OK ==> {PROJECT_M4BOARD_IP}")          
        EMULATOR             = "M4 Board"
        
        count = 0

        archivos = os.listdir(cm.PATH_DISC)
        for archivo in archivos:
            if os.path.isfile(os.path.join(cm.PATH_DISC, archivo)):
                cm.msgInfo("Upload " + cm.getFileExt(archivo) + " ==> M4 Board")  
                if not uploadFileM4BOARD(PROJECT_M4BOARD_IP,cm.PATH_DISC + "/" + archivo,PROJECT_M4_FOLDER):
                    cm.showFoodDataProject("NO FILES UPLOAD M4 BOARD", 1)
            count = count + 1     
        
        if count > 0:
            if cm.fileExist(cm.PATH_DISC + "/" + PROJECT_M4_EXECUTE):
                if not executeFileM4BOARD(PROJECT_M4BOARD_IP,):
                    cm.showFoodDataProject("NO FILES UPLOAD M4 BOARD", 1)
                cm.msgInfo(f"Execute file: {PROJECT_M4_EXECUTE}")
                cm.msgInfo(f"Emulator    : {EMULATOR}")
                cm.showFoodDataProject("FILES UPLOAD AND EXECUTE M4 BOARD", 0)
        else:
            cm.msgWarning("No upload files in " + cm.PATH_DISC)    
            cm.showFoodDataProject("NO FILE EXECUTED M4 BOARD", 1)
                  

        
