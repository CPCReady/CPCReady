import os
import sys
import datetime
import shutil
from jinja2 import Template
import subprocess
import yaml
from CPCReady import common as cm
import io


def execute(project,emulator):

    if not cm.fileExist(cm.CFG_EMULATORS):
        sys.exit(1)

    DATA_PROJECT   = cm.getData(cm.CFG_PROJECT)
    DATA_EMULATORS = cm.getData(cm.CFG_EMULATORS)

    PROJECT_NAME         = DATA_PROJECT.get('project','name')
    PROJECT_AUTHOR       = DATA_PROJECT.get('project','author')
    PROJECT_DSK_FILE     = f"{cm.PATH_DSK}/{DATA_PROJECT.get('project','dsk')}"
    
    cm.showHeadDataProject(cm.getFileExt(PROJECT_DSK_FILE))
    
    if emulator == "rvm-web":   
        PROJECT_RVM_MODEL    = DATA_EMULATORS.get(emulator,'model')
        PROJECT_RVM_RUN      = DATA_EMULATORS.get(emulator,'run')
        EMULATOR             = f"Retro Virtual Machine WEB ({cm.TEMPLATE_RVM_WEB})"
        context = {
            'name': PROJECT_NAME,
            'model': PROJECT_RVM_MODEL,
            'dsk': f"{PROJECT_DSK_FILE}",
            'run': f'{PROJECT_RVM_RUN}'
        }
        
        cm.createTemplate("rvm-web.html", context, cm.PATH_CFG)
        cm.msgInfo(f"CPC Model: {PROJECT_RVM_MODEL}")
        cm.msgInfo(f"RUN Command: {PROJECT_RVM_RUN}")
        cm.msgInfo(f"Emulator: RVM Web ({cm.TEMPLATE_RVM_WEB})") 
           
    elif emulator == "rvm-desktop":   
        PROJECT_RVM_MODEL    = DATA_EMULATORS.get(emulator,'model')
        PROJECT_RVM_RUN      = DATA_EMULATORS.get(emulator,'run')
        PROJECT_RVM_PATH     = DATA_EMULATORS.get(emulator,'path')
        
        if PROJECT_RVM_PATH != "":
            if cm.fileExist(PROJECT_RVM_PATH):
                cm.msgInfo(f"CPC Model: {PROJECT_RVM_MODEL}")
                cm.msgInfo(f"RUN Command: {PROJECT_RVM_RUN}")
                cm.msgInfo(f"Emulator: RVM Desktop ({PROJECT_RVM_PATH})")
                FNULL = open(os.devnull, 'w')
                try:
                    retcode = subprocess.Popen([PROJECT_RVM_PATH,"-i", PROJECT_DSK_FILE,"-b=cpc"+str(PROJECT_RVM_MODEL),"-c="+PROJECT_RVM_RUN + "\n"], stdout=FNULL, stderr=subprocess.STDOUT)
                    return True
                except subprocess.CalledProcessError as e:
                    cm.msgError(f'{cm.getFileExt(PROJECT_DSK_FILE)} RELEASED WITH ERROR: {e.output.decode()}')
                    return False
            else:
                cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
        else:
            cm.msgError(f"RVM Desktop path does not exist in {cm.CFG_PROJECT}")
            cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
        
    elif emulator == "m4board":   
        PROJECT_RVM_RUN      = DATA_EMULATORS.get(emulator,'run')
        PROJECT_M4BOARD_IP   = DATA_EMULATORS.get(emulator,'ip')
        EMULATOR             = "M4 Board"
        cm.msgInfo(f"CPC Model: {PROJECT_RVM_MODEL}")
        cm.msgInfo(f"RUN Command: {PROJECT_RVM_RUN}")
        cm.msgInfo(f"Emulator: {EMULATOR}")

    cm.showFoodDataProject("DISC IMAGE SUCCESSFULLY RELEASED", 0)