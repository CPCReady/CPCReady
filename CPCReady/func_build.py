import os
import sys
import datetime
import shutil
import subprocess
import glob
import yaml
from CPCReady import common as cm
from CPCReady import func_screen as screens
from CPCReady import func_sprite as sprites


def getBasFiles(path):
    archivos_bas = []
    for ruta, directorios, archivos in os.walk(path):
        for archivo in archivos:
            if archivo.lower().endswith((".bas", ".bAs", ".baS","BAS", "Bas")):
                archivos_bas.append(os.path.join(ruta, archivo))
    return archivos_bas

def getBinFiles(path):
    archivos_bin = []
    for ruta, directorios, archivos in os.walk(path):
        for archivo in archivos:
            if archivo.lower().endswith((".bin", ".bIn", ".biS","BIN", "Bin")):
                archivos_bin.append(os.path.join(ruta, archivo))
    return archivos_bin

def getAsciiFiles(path):
    archivos_ascii = []
    for ruta, directorios, archivos in os.walk(path):
        for archivo in archivos:
            if archivo.lower().endswith((".txt", ".tXt", ".txT","TXT", "Txt")):
                archivos_ascii.append(os.path.join(ruta, archivo))
    return archivos_ascii

def getImgFiles(path):
    archivos_ascii = []
    for ruta, directorios, archivos in os.walk(path):
        for archivo in archivos:
            if archivo.lower().endswith((".jpg", ".JPG", ".Jpg",".png", ".PNG", ".Png")):
                archivos_ascii.append(os.path.join(ruta, archivo))
    return archivos_ascii

def create():

    # Check is cfg project exist
    if not cm.fileExist(cm.CFG_PROJECT):
        sys.exit(1)

    # load data cfg project
    # with open(cm.CFG_PROJECT, 'r') as file:
    #     data = yaml.safe_load(file)
        
    DATA_PROJECT   = cm.getData(cm.CFG_PROJECT)
    DATA_EMULATORS = cm.getData(cm.CFG_EMULATORS)

    # NUMBER_CONCAT_FILES  = sum(1 for item in data['spec']['files'] if item.get('kind') == 'bas' and item.get('concat') == True)
    COUNT                = 0
    PROJECT_NAME         = DATA_PROJECT.get('project','name')
    PROJECT_AUTHOR       = DATA_PROJECT.get('project','author')
    PROJECT_CONCAT_OUT   = DATA_PROJECT.get('project','concatenate')        
    PROJECT_DSK_FILE     = f"{cm.PATH_DSK}/{DATA_PROJECT.get('project','dsk')}"

    cm.showHeadDataProject("BUILD " + PROJECT_NAME)
    
    cm.removeContentDirectory(cm.PATH_DISC)
    
    for folder in cm.subfolders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    cm.msgInfo("Check folders project OK")
    
    createImageDisc(PROJECT_DSK_FILE)
 
    ########################################
    # PROCESING BAS FILES
    ########################################

    if PROJECT_CONCAT_OUT:
        PROJECT_CONCAT_OUT   = cm.PATH_DISC + "/" + PROJECT_CONCAT_OUT
        concatAllFiles(cm.PATH_SRC,PROJECT_CONCAT_OUT)
        if not convert2Dos(PROJECT_CONCAT_OUT, PROJECT_CONCAT_OUT):
            cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
        if not addBas2ImageDisc(PROJECT_DSK_FILE, PROJECT_CONCAT_OUT):
            cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    else:          
        for basfile in glob.glob(os.path.join(cm.PATH_SRC, '*.[bB][aA][sS]')):
            outputbasfile = f"{cm.PATH_DISC}/{cm.getFileExt(basfile)}"
            if not removeComments(basfile, outputbasfile):
                    cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
            if not convert2Dos(outputbasfile, outputbasfile): 
                    cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
            if not addBas2ImageDisc(PROJECT_DSK_FILE, outputbasfile):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)   
                                             
    ########################################
    # PROCESING BIN FILES
    ########################################
    
    for binfile in glob.glob(os.path.join(cm.PATH_LIB, '*.[bB][iI][nN]')):
        outputbinfile = f"{cm.PATH_DISC}/{cm.getFileExt(binfile)}"
        shutil.copy2(binfile,outputbinfile)
        if not addBin2ImageDisc(PROJECT_DSK_FILE, outputbinfile):
            cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)    
      
    ########################################
    # PROCESING IMAGES FILES
    ########################################
    DATA_IMAGES = cm.getData(cm.CFG_IMAGES)
    for image in glob.glob(os.path.join(cm.PATH_ASSETS, '*.[pP][nN][gG]')):
        IMAGE_NAME  = cm.getFileExt(image)
        CONFIG_IMAGE = DATA_IMAGES.get('images',IMAGE_NAME,fallback="NULL")
        outputbinfile = f"{cm.PATH_DISC}/{cm.getFileExt(image)}"
        if CONFIG_IMAGE == "NULL":
            cm.msgWarning(f"No configuration {IMAGE_NAME} in images.cfg, not process files")
        else:
            CONFIG = CONFIG_IMAGE.split(',')
            MODE = CONFIG[0].strip()
            PAL  = CONFIG[1].strip()
            if not screens.create(image, MODE, cm.PATH_DISC, False, True):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
            NEW_FILE = cm.getFile(image).upper()
            if not addBin2ImageDisc(f"{PROJECT_DSK_FILE}", f"{cm.PATH_DISC}/{NEW_FILE}.SCR"):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)            
            if PAL.upper() != "TRUE":
                os.remove(f"{cm.PATH_DISC}/{NEW_FILE}.PAL")
            else:
                if not addBin2ImageDisc(f"{PROJECT_DSK_FILE}", f"{cm.PATH_DISC}/{NEW_FILE}.PAL"):
                    cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)                   
    ########################################
    # PROCESING ASCII FILES
    ########################################                            

            if not cm.fileExist(f"{cm.PATH_SRC}/{file_data['name']}"):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
            if not addBas2ImageDisc(PROJECT_DSK_FILE, f"{cm.PATH_SRC}/{file_data['name']}"):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
            
    # for file_data in data['spec']['files']:
    #     ########################################
    #     # PROCESING BAS FILES
    #     ########################################
    #     if file_data['kind'].upper() == 'BAS':
    #         COUNT = COUNT + 1
    #         if not cm.fileExist(f"{cm.PATH_SRC}/{file_data['name']}"):
    #             cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
            
    #         if not removeComments(f"{cm.PATH_SRC}/{file_data['name']}", f"{cm.PATH_DISC}/{file_data['name']}"):
    #             cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
                
    #         if not convert2Dos(f"{cm.PATH_DISC}/{file_data['name']}", f"{cm.PATH_DISC}/{file_data['name']}"): 
    #             cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #     ########################################
    #     # CONCAT FILES
    #     ########################################
    #         if file_data['concat'] == True:
    #             if not concatFile(f"{cm.PATH_DISC}/{file_data['name']}", PROJECT_CONCAT_OUT):
    #                 cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #                 if COUNT == NUMBER_CONCAT_FILES:
    #                    if not convert2Dos(PROJECT_CONCAT_OUT, PROJECT_CONCAT_OUT):
    #                        cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #                    if not addBas2ImageDisc(PROJECT_DSK_FILE, f"{cm.PATH_DISC}/{file_data['name']}"):
    #                        cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #                 else:
    #                     if not addBas2ImageDisc(PROJECT_DSK_FILE, f"{cm.PATH_DISC}/{file_data['name']}"): 
    #                         cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #     ########################################
    #     # PROCESING ASCII FILES
    #     ########################################                            
    #     elif file_data['kind'].upper() == 'ASCII':
    #         if not cm.fileExist(f"{cm.PATH_SRC}/{file_data['name']}"):
    #             cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #         if not addBas2ImageDisc(PROJECT_DSK_FILE, f"{cm.PATH_SRC}/{file_data['name']}"):
    #             cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #     ########################################
    #     # PROCESING UGBASIC FILES
    #     ########################################
    #     elif file_data['kind'].upper() == 'UGBASIC':
    #         if sys.platform != 'darwin':
    #             if not cm.fileExist(f"{cm.PATH_SRC}/{file_data['name']}"):
    #                 cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #             if not compile(f"{cm.PATH_SRC}/{file_data['name']}", f"{cm.PATH_DISC}/", f"{file_data['address']}",f"{file_data['include']}"):
    #                 cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #             if not cm.addBin2ImageDisc(f"{PROJECT_DSK_FILE}", f"{cm.PATH_DISC}/" + cm.getFile(f"{cm.PATH_DISC}/{file_data['name']}") + ".bin"): 
    #                 cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #         else:
    #             cm.msgWarning("Mac OSX operating system does not support ugBasic")
    #     ########################################
    #     # PROCESING IMAGES FILES
    #     ########################################
    #     elif file_data['kind'].upper() == 'IMAGE':
    #         if not cm.fileExist(f"{cm.PATH_ASSETS}/{file_data['name']}"):
    #             cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #         if not screens.create (f"{cm.PATH_ASSETS}/{file_data['name']}", f"{file_data['mode']}", cm.PATH_DISC, False, True):
    #             cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #         NEW_FILE = cm.getFile(f"{cm.PATH_ASSETS}/{file_data['name']}").upper()
    #         if not addBin2ImageDisc(f"{PROJECT_DSK_FILE}", f"{cm.PATH_DISC}/{NEW_FILE}.SCR"):
    #             cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #         if not file_data['pal']:
    #                 os.remove(f"{cm.PATH_DISC}/{NEW_FILE}.PAL")
    #     ########################################
    #     # PROCESING SPRITE FILES
    #     ########################################
    #     elif file_data['kind'].upper() == 'SPRITE':
    #             if not cm.fileExist(f"{cm.PATH_ASSETS}/{file_data['name']}"):
    #                 cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    #             if not sprites.create(f"{cm.PATH_ASSETS}/{file_data['name']}",f"{file_data['mode']}",cm.PATH_DISC,f"{file_data['width']}",f"{file_data['height']}",True):
    #                 cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
                    
    #     cm.showFoodDataProject("CREATE DISC IMAGE SUCCESSFULLY", 0)

##
# Compile ugbasic
#
# @param source: source file name
# @param out: output file name
##
def compileUGBasic(source, out):

    try:
        cmd = [cm.UGBASIC, source, "-o", out]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        name = cm.getFile(source)
        extract2ImageDisc(name,out)
        shutil.move("src/" + name, name+".bin")
        cm.msgInfo(f"Compile: {source} ==> + {name}.bin")
        os.remove(out)
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(cm.getFileExt(source) + f' ==> Error executing command: {e.output.decode()}')
        return False

def concatAllFiles(path, inFile):
    allBasFiles = glob.glob(os.path.join(path, '*.[bB][aA][sS]'))
    for basfile in allBasFiles:
        addContenToFile(inFile,readContentFile(basfile))
        cm.msgInfo(f"Concat file {cm.getFileExt(basfile)} ==> {cm.getFileExt(inFile)}")
    return

def readContentFile (source):
    with open(source, 'r') as origen_file:
        contenfile = origen_file.read()
    return contenfile

def addContenToFile (source, text):
    with open(source, 'a') as destino_file:
        destino_file.write(text)


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
    cm.msgInfo(f"Convert unix to dos ==> {cm.getFileExt(source)}")
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
    cm.msgInfo(f"Comments Remove ==> {file}")
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
        cm.msgInfo("Add file " + cm.getFileExt(file) + " ==> " + cm.getFileExt(imagefile))
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        return False

def addBin2ImageDisc(imagefile, file):
    cmd = [cm.IDSK, imagefile, "-i", file, '-t', '1']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgInfo("Add file " + cm.getFileExt(file) + " ==> " + cm.getFileExt(imagefile))
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        return False

def extract2ImageDisc(imagefile, file):
    FNULL = open(os.devnull, 'w')
    cmd = [cm.IDSK, imagefile, "-g", file]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        return False