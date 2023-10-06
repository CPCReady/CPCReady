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
    CPC_MODEL            = DATA_PROJECT.get('project','model')
    PROJECT_AUTHOR       = DATA_PROJECT.get('project','author')
    PROJECT_CONCAT_OUT   = DATA_PROJECT.get('project','concatenate')        
    PROJECT_DSK_FILE     = f"{cm.PATH_DSK}/{DATA_PROJECT.get('project','dsk')}"

    cm.banner(CPC_MODEL)
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
        IMAGE_MODE = DATA_IMAGES.get(IMAGE_NAME,"mode",fallback="NULL")
        outputbinfile = f"{cm.PATH_DISC}/{cm.getFileExt(image)}"
        if IMAGE_MODE == "NULL":
            cm.msgWarning(f"No configuration {IMAGE_NAME} in images.cfg, not process files")
        else:
            IMAGE_PAL = DATA_IMAGES.get(IMAGE_NAME,"include_pal",fallback="FALSE")
            if not screens.create(image, IMAGE_MODE, cm.PATH_DISC, False, True):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
            NEW_FILE = cm.getFile(image).upper()
            if not addBin2ImageDisc(f"{PROJECT_DSK_FILE}", f"{cm.PATH_DISC}/{NEW_FILE}.SCR"):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)            
            if IMAGE_PAL.upper() == "FALSE":
                os.remove(f"{cm.PATH_DISC}/{NEW_FILE}.PAL")
            else:
                if not addBin2ImageDisc(f"{PROJECT_DSK_FILE}", f"{cm.PATH_DISC}/{NEW_FILE}.PAL"):
                    cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)    
                                   
    ########################################
    # PROCESING ASCII FILES
    ########################################                            

    for ascii in glob.glob(os.path.join(cm.PATH_SRC, '*.[tT][xX][tT]')):
        shutil.copyfile(ascii,f"{cm.PATH_DISC}/{cm.getFileExt(ascii)}")
        if not addBas2ImageDisc(PROJECT_DSK_FILE, f"{cm.PATH_DISC}/{cm.getFileExt(ascii)}"):
            cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)

    ########################################
    # PROCESING SPRITES FILES
    ########################################
                             
    DATA_SPRITES = cm.getData(cm.CFG_SPRITES)
    
    for sprite in glob.glob(os.path.join(cm.PATH_SPR, '*.[pP][nN][gG]')):
        SPRITE_NAME   = cm.getFileExt(sprite)
        SPRITE_MODE   = DATA_SPRITES.get(SPRITE_NAME,"mode",fallback="NULL")
        SPRITE_HEIGHT = DATA_SPRITES.get(SPRITE_NAME,"height",fallback="NULL")
        SPRITE_WIDTH  = DATA_SPRITES.get(SPRITE_NAME,"width",fallback="NULL")
        if SPRITE_MODE == "NULL":
            cm.msgWarning(f"No configuration {SPRITE_NAME} in sprites.cfg, not process file.")
        else:
            if not sprites.create(sprite,SPRITE_MODE,cm.PATH_DISC,SPRITE_WIDTH,SPRITE_HEIGHT,True):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)

    ########################################
    # PROCESING UGBASIC FILES
    ########################################
                             
    DATA_UGBASIC = cm.getData(cm.PATH_SRC)
    if sys.platform != 'darwin':
        for ugbfile in glob.glob(os.path.join(cm.PATH_SPR, '*.[uU][gG][bB]')):
            UGBASIC_NAME   = cm.getFileExt(ugbfile)
            if not compile(UGBASIC_NAME, cm.PATH_DISC):
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
            if not cm.addBin2ImageDisc(PROJECT_DSK_FILE, f"{cm.PATH_DISC}/" + UGBASIC_NAME + ".bin"): 
                cm.showFoodDataProject("BUILD FAILURE DISC IMAGE", 1)
    else:
        cm.msgWarning("Mac OSX operating system does not support ugBasic")
                    
    cm.showFoodDataProject("CREATE DISC IMAGE SUCCESSFULLY", 0)

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