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
    
   ########################################
   # VARIABLES
   ########################################
   
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
        
   ########################################
   # EXECUTE MARTINE
   ########################################
    
    common.showHeadDataProject(filename)
   
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

   ########################################
   # READ JSON PALETTE
   ########################################
   
    with open(IMAGE_TMP_JSON) as f:
        data = json.load(f)

    sw_palette = str(data['palette'])
    hw_palette = str(data['hardwarepalette'])
    
   ########################################
   # IF PARAM DSK IS TRUE
   ########################################

    if dsk:
        if not os.path.exists(fileout):
            os.makedirs(fileout)
        shutil.copy2(os.path.join(IMAGE_TEMP_PATH, IMAGE_TMP_FILE.upper() + '.DSK'), fileout + '/' + IMAGE_TMP_FILE.upper() + '.DSK')
        common.msgInfo(f"Create IMAGE File: {fileout}/{IMAGE_TMP_FILE.upper()}.DSK")
        
    common.msgInfo(f"       SW PALETTE : {sw_palette}")
    common.msgInfo(f"       HW PALETTE : {hw_palette}")
    
   ########################################
   # DELETE TEMPORAL FILES
   ########################################
   
    shutil.rmtree(IMAGE_TEMP_PATH)
    if dsk:
        common.showFoodDataProject(IMAGE_TMP_FILE.upper() + ".DSK SUCCESSFULLY CREATED.",0)
    else:
        common.showFoodDataProject(f"{fileout}/{IMAGE_TMP_FILE.upper()}.SCR SUCCESSFULLY CREATED.",0)
    return True
