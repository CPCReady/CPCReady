import os
import sys
import datetime
import shutil
from jinja2 import Template
import subprocess
import yaml
from CPCReady import common as cm
from CPCReady import func_screen as screens
from CPCReady import func_sprite as sprites

def execute(project,emulator):

    if not cm.fileExist(cm.CFG_PROJECT):
        cm.msgError(f"The project configuration file does not exist ({cm.CFG_PROJECT})")
        sys.exit(1)

    with open(cm.CFG_PROJECT, 'r') as file:
        data = yaml.safe_load(file)

    PROJECT_NAME         = data['project']['data'].get('name', 'No project mame')
    PROJECT_AUTHOR       = data['project']['data'].get('author', 'No author mame')
    PROJECT_DSK_FILE     = f"{cm.PATH_DSK}/{PROJECT_NAME}.DSK"

    APP_PATH = os.path.dirname(os.path.abspath(__file__))
    
    cm.showHeadDataProject(cm.getFileExt(PROJECT_DSK_FILE))
    
    if emulator == "rvm-web":   
        PROJECT_RVM_MODEL    = data['project']['emulators'][emulator].get('model')
        PROJECT_RVM_RUN      = data['project']['emulators'][emulator].get('run')
        EMULATOR             = f"Retro Virtual Machine WEB ({cm.TEMPLATE_RVM_WEB})"
        context = {
            'name': PROJECT_NAME,
            'cpc': PROJECT_RVM_MODEL,
            'dsk': f"{PROJECT_DSK_FILE}",
            'run': f'{PROJECT_RVM_RUN}'
        }

        with open(APP_PATH + "/templates/cpc.j2", 'r') as file:
            template_string = file.read()
        template = Template(template_string)
        rendered_template = template.render(context)
        with open(cm.TEMPLATE_RVM_WEB, 'w') as file:
            file.write(rendered_template)
            
        cm.msgInfo(f"CPC Model: {PROJECT_RVM_MODEL}")
        cm.msgInfo(f"RUN Command: {PROJECT_RVM_RUN}")
        cm.msgInfo(f"Emulator: RVM Web ({cm.TEMPLATE_RVM_WEB})") 
           
    elif emulator == "rvm-desktop":   
        PROJECT_RVM_MODEL    = data['project']['emulators'][emulator].get('model')
        PROJECT_RVM_RUN      = data['project']['emulators'][emulator].get('run')
        PROJECT_RVM_PATH     = data['project']['emulators'][emulator].get('path')
        
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
        PROJECT_RVM_RUN      = data['project']['emulators'][emulator].get('run')
        PROJECT_M4BOARD_IP   = data['project']['emulators'][emulator].get('ip')
        EMULATOR             = "M4 Board"
        cm.msgInfo(f"CPC Model: {PROJECT_RVM_MODEL}")
        cm.msgInfo(f"RUN Command: {PROJECT_RVM_RUN}")
        cm.msgInfo(f"Emulator: {EMULATOR}")

    cm.showFoodDataProject("DISC IMAGE SUCCESSFULLY RELEASED", 0)