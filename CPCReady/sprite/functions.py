import sys
import os
import subprocess
import shutil
import json
import CPCReady.common as common

##
# Create SCR image

#
# @param project: image filename
# @param mode: CPC mode (0, 1, 2)
# @param fileout: folder out
# @param height: height size
# @param width: width size
# @param api; if funcion or not
##

def create(filename, mode, fileout, height, width, api=False):
    
   ########################################
   # VARIABLES
   ########################################
   
    if common.TEMP_PATH is not None:
        IMAGE_TEMP_PATH = common.TEMP_PATH + "." + os.path.basename(filename)
    else:
        IMAGE_TEMP_PATH = common.PWD + "." + os.path.basename(filename)
    
    IMAGE_TMP_FILE = os.path.basename(os.path.splitext(filename)[0])
    IMAGE_TMP_JSON = IMAGE_TEMP_PATH + "/" + IMAGE_TMP_FILE+".json"
    IMAGE_TMP_TXT  = IMAGE_TEMP_PATH + "/" + IMAGE_TMP_FILE+".TXT"
    IMAGE_TMP_CTXT = IMAGE_TEMP_PATH + "/" + IMAGE_TMP_FILE+"C.TXT"
    
    if os.path.exists(IMAGE_TEMP_PATH) and os.path.isdir(IMAGE_TEMP_PATH):
        shutil.rmtree(IMAGE_TEMP_PATH)
    
    cmd = [common.MARTINE, '-in', filename, '-width', str(width),'-height',str(height),'-mode', str(mode), '-out', IMAGE_TEMP_PATH, '-json','-noheader']
        
   ########################################
   # EXECUTE MARTINE
   ########################################
    if api == False:
        common.showHeadDataProject(common.getFileExt(filename))
   
    try:
        if fileout:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            if not os.path.exists(fileout):
                os.makedirs(fileout)
        else:
            subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        common.msgError(f'Error ' + common.getFileExt(filename) + f' executing command: {e.output.decode()}')
        if api == False:
            common.showFoodDataProject(IMAGE_TMP_FILE.upper() + ".DSK NOT CREATED.",1)
        else:
            common.showFoodDataProject(f"{fileout}/{IMAGE_TMP_FILE.upper()}.SCR NOT CREATED.",1)
            return False

   ########################################
   # READ JSON PALETTE
   ########################################
   
    with open(IMAGE_TMP_JSON) as f:
        data = json.load(f)

    sw_palette = str(data['palette'])
    hw_palette = str(data['hardwarepalette'])

   ########################################
   # GENERATE C FILE
   ########################################

    only=0
    copy = False
    with open(IMAGE_TMP_CTXT, 'r') as input_file:
        with open(fileout + "/" + IMAGE_TMP_FILE.upper() + ".C", 'w') as output_file:
            if only == 0:
                output_file.write("array byte " + IMAGE_TMP_FILE + " = {\n")
                only = 1
            for line in input_file:
                if line.startswith('; width'):
                    copy = True
                    continue
                elif line.startswith('; Palette'):
                    copy = False
                    continue
                if copy:
                    output_file.write(line.replace("db ", "   "))
            output_file.write("};\n")
            
    common.msgInfo(f"Create C File  : {fileout}/" + IMAGE_TMP_FILE.upper() + ".C")

   ########################################
   # GENERATE ASM FILE
   ########################################
    
    only=0
    with open(IMAGE_TMP_TXT, 'r') as input_file:
        with open(fileout + "/" + IMAGE_TMP_FILE.upper() + ".ASM", 'w') as output_file:
            if only == 0:
                output_file.write(";------ BEGIN SPRITE --------\n")
                output_file.write(IMAGE_TMP_FILE)
                output_file.write("\ndb " + str(width) + " ; ancho")
                output_file.write("\ndb " + str(height) + " ; alto\n")
                only = 1
            for line in input_file:
                if line.startswith('; width'):
                    copy = True
                    continue
                elif line.startswith('; Palette'):
                    copy = False
                    continue
                if copy:
                    output_file.write(line)
            output_file.write("\n;------ END SPRITE --------\n")
            
    common.msgInfo(f"Create ASM File: {fileout}/" + IMAGE_TMP_FILE.upper() + ".ASM") 
    common.msgInfo(f"       SW PALETTE : {sw_palette}")
    common.msgInfo(f"       HW PALETTE : {hw_palette}")   
    
    if api == False:
        common.showFoodDataProject("SPRITE FILES SUCCESSFULLY CREATED.",0)
    
    return True
