
import os
import sys
import datetime
import shutil
import subprocess
import glob
from CPCReady import common as cm
from CPCReady import func_screen as screens
from CPCReady import func_sprite as sprites
from CPCReady import func_info as info
from CPCReady import func_about as my
from CPCReady import __version__ as version

module_path = os.path.dirname(os.path.abspath(__file__))

def create(scope):
    
    my.show(False)
    cm.showInfoTask(f"Build project in progress...")
    cm.validateYaml(cm.CFG_PROJECT)

    PROJECT_NAME     = cm.getNameProject()
    PROJECT_83_FILES = cm.get83Files()
    PROJECT_CDT      = f"{PROJECT_NAME}.CDT"
    PROJECT_DSK      = f"{PROJECT_NAME}.DSK"
    PROJECT_CPR_NAME = f"{PROJECT_NAME}.CPR"


    

    PROJECT_CDT_NAME       = f"{cm.PATH_DSK}/{PROJECT_CDT}"
    PROJECT_DSK_NAME       = f"{cm.PATH_DSK}/{PROJECT_DSK}"
    PROJECT_CDT_FILES      = cm.getCdtFiles()
    DESTINATION_MERGE_FILE = cm.getMergeDestinationFile()
    MERGE_FILES            = cm.getMergeFiles()

    

    if PROJECT_83_FILES:
        check_subfolders = ["src", "lib", "img", "spr","assets"]
        for carpeta in check_subfolders:
            if not check_nomenclature83(carpeta):
                cm.msgError(f"Folder '{carpeta}' contains files with names longer than 8 characters.")
                cm.showFoodDataProject("Build failure disc image", 1)

    cm.removeContentDirectory(cm.PATH_DISC)

    for folder in cm.subfolders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    cm.msgCustom("CHECK", "Folders Project.", "green")

    createImageDisc(PROJECT_DSK_NAME)

    ########################################
    # PROCESING MERGE FILES
    ########################################
    if DESTINATION_MERGE_FILE:
        for file_to_merge in MERGE_FILES:
            if cm.fileExist(cm.PATH_SRC + "/" + file_to_merge):
                addContenToFile(cm.PATH_DISC + "/" + DESTINATION_MERGE_FILE, readContentFile(cm.PATH_SRC + "/" + file_to_merge))
                cm.msgCustom("MERGE", f"{cm.getFileExt(file_to_merge)} ==> {cm.getFileExt(DESTINATION_MERGE_FILE)}", "green")
        convert2Dos(cm.PATH_DISC + "/" + DESTINATION_MERGE_FILE, cm.PATH_DISC + "/" + DESTINATION_MERGE_FILE)
        if not removeComments(cm.PATH_DISC + "/" + DESTINATION_MERGE_FILE,cm.PATH_DISC + "/" + DESTINATION_MERGE_FILE):
            cm.showFoodDataProject("Build failure disc image", 1)
        if not addBas2ImageDisc(PROJECT_DSK_NAME, cm.PATH_DISC + "/" + DESTINATION_MERGE_FILE):
            cm.showFoodDataProject("Build failure disc image", 1)
        addamsdos(cm.PATH_DISC + "/" + DESTINATION_MERGE_FILE)    
            

    ########################################
    # PROCESING BAS FILES
    ########################################
    
    allBasFiles = glob.glob(os.path.join(cm.PATH_SRC, '*.[bB][aA][sS]'))
    for basfile in allBasFiles:
        if not basInMergeFiles(MERGE_FILES,cm.getFileExt(basfile)):
            convert2Dos(basfile, cm.PATH_DISC + "/" + cm.getFileExt(basfile))
            if not removeComments(basfile,cm.PATH_DISC + "/" + cm.getFileExt(basfile)):
                cm.showFoodDataProject("Build failure disc image", 1)
            if not addBas2ImageDisc(PROJECT_DSK_NAME, cm.PATH_DISC + "/" + cm.getFileExt(basfile)):
                cm.showFoodDataProject("Build failure disc image", 1)
            addamsdos(cm.PATH_DISC + "/" + cm.getFileExt(basfile))    

    ########################################
    # PROCESING ASCII FILES
    ########################################                            

    for ascii in glob.glob(os.path.join(cm.PATH_SRC, '*.[tT][xX][tT]')):
        shutil.copyfile(ascii, f"{cm.PATH_DISC}/{cm.getFileExt(ascii)}")
        if not addBas2ImageDisc(PROJECT_DSK_NAME, f"{cm.PATH_DISC}/{cm.getFileExt(ascii)}"):
            cm.showFoodDataProject("Build failure disc image", 1)

    ########################################
    # PROCESING IMAGES FILES
    ########################################

    PROJECT_IMAGES = cm.getImages()
    for asset in PROJECT_IMAGES:
        if cm.fileExist(cm.PATH_ASSETS + "/" + asset):
            if not screens.create(cm.PATH_ASSETS + "/" + asset, cm.getImageMode(asset), cm.PATH_DISC, False, True):
                cm.showFoodDataProject("Build failure disc image", 1)
            NEW_FILE = cm.getFile(asset).upper()
            if not addBin2ImageDisc(f"{PROJECT_DSK_NAME}", f"{cm.PATH_DISC}/{NEW_FILE}.SCR"):
                cm.showFoodDataProject("Build failure disc image", 1)
            if cm.getImagePal(asset):
                if not addBin2ImageDisc(f"{PROJECT_DSK_NAME}", f"{cm.PATH_DISC}/{NEW_FILE}.PAL"):
                    cm.showFoodDataProject("Build failure disc image", 1)
                else:
                    os.remove(f"{cm.PATH_DISC}/{NEW_FILE}.PAL")         
                    
                

    ########################################
    # PROCESING SPRITES FILES
    ########################################

    PROJECT_SPRITES = cm.getSprites()
    for asset in PROJECT_SPRITES:
        if cm.fileExist(cm.PATH_ASSETS + "/" + asset):
            if not sprites.create(cm.PATH_ASSETS + "/" + asset, cm.getSpriteMode(asset), cm.PATH_CODE, cm.getSpriteWidth(asset), cm.getSpriteHeight(asset), True):
                cm.showFoodDataProject("Build failure disc image", 1)
            
            
    # for sprite in glob.glob(os.path.join(cm.PATH_SPR, '*.[pP][nN][gG]')):
    #     SPRITE_NAME = cm.getFileExt(sprite)
    #     SPRITE_MODE = DATA_SPRITES.get(SPRITE_NAME, "mode", fallback="NULL")
    #     SPRITE_HEIGHT = DATA_SPRITES.get(SPRITE_NAME, "height", fallback="NULL")
    #     SPRITE_WIDTH = DATA_SPRITES.get(SPRITE_NAME, "width", fallback="NULL")
    #     if SPRITE_MODE == "NULL":
    #         cm.msgWarning(f"No configuration {SPRITE_NAME} in sprites.cfg, not process file.")
    #     else:
    #         if not sprites.create(sprite, SPRITE_MODE, cm.PATH_DISC, SPRITE_WIDTH, SPRITE_HEIGHT, True):
    #             cm.showFoodDataProject("Build failure disc image", 1)

    ########################################
    # PROCESSING UGBASIC FILES
    ########################################

    # DATA_UGBASIC = cm.getData(cm.PATH_SRC)
    # # if sys.platform != 'darwin':
    # for ugbfile in glob.glob(os.path.join(cm.PATH_SRC, '*.[uU][gG][bB]')):
    #     UGBASIC_NAME = cm.getFileExt(ugbfile)
    #     if not compileUGBasic(ugbfile, cm.PATH_DISC + "/UGBTEMP.DSK"):
    #         cm.showFoodDataProject("Build failure disc image", 1)
    #     if not addBin2ImageDisc(PROJECT_DSK_NAME, f"{cm.PATH_DISC}/" + cm.getFile(UGBASIC_NAME) + ".BIN"):
    #         cm.showFoodDataProject("Build failure disc image", 1)
    # # else:
    #     cm.msgWarning("Mac OSX operating system does not support ugBasic")

    ########################################
    # PROCESSING DSK FILES (LIB)
    ########################################

    # for dskfile in glob.glob(os.path.join(cm.PATH_LIB, '*.[dD][sS][kK]')):
    #     if not extract2ImageDisc(dskfile, cm.PATH_DISC + "/" + cm.getFile(dskfile) + ".bin"):
    #         cm.showFoodDataProject("Build failure disc image", 1)
    #     if not addBin2ImageDisc(PROJECT_DSK_NAME, cm.PATH_DISC + "/" + cm.getFile(dskfile) + ".bin"):
    #         cm.showFoodDataProject("Build failure disc image", 1)

    ########################################
    # PROCESSING BIN FILES (LIB)
    ########################################

    # for binfile in glob.glob(os.path.join(cm.PATH_LIB, '*.[bB][iI][nN]')):
    #     outputbinfile = f"{cm.PATH_DISC}/{cm.getFileExt(binfile)}"
    #     shutil.copy2(binfile, outputbinfile)
    #     if not addBin2ImageDisc(PROJECT_DSK_NAME, outputbinfile):
    #         cm.showFoodDataProject("Build failure disc image", 1)

    ########################################
    # ADD FILES TO CDT
    ########################################

    if os.path.isfile(PROJECT_CDT_NAME):
        os.remove(PROJECT_CDT_NAME)
    createImageCDT(PROJECT_CDT_NAME)
    cdtfiles = PROJECT_CDT_FILES

    for cdtfile in cdtfiles:
        file = cm.PATH_DISC + "/" + cdtfile.strip()
        if not cm.fileExist(file):
            cm.showFoodDataProject("Build failure disc image", 1)
            sys.exit(1)

        addFile2CDTImage(file, PROJECT_CDT_NAME)

    # ########################################
    # # GENERATE CPR
    # ########################################

    # dsk2cpr(PROJECT_DSK_NAME,cm.PATH_DISC + "/" + PROJECT_CPR_NAME,PROJECT_CPR_RUN)
    
    cm.showFoodDataProject("Successfully create disc image", 0)

    print()


##
# Compile ugbasic
#
# @param source: source file name
# @param out: output file name
##
# def compileUGBasic(source, out):
#     module_path = os.path.dirname(os.path.abspath(__file__))
#     binary_path = os.path.join(module_path, 'z88dk', 'bin')
#     os.environ['PATH'] = f"{binary_path}:{os.environ['PATH']}"
#     try:
#         cmd = [cm.UGBASIC, "-O", "dsk", "-o", out, source]
#         output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
#         if not os.path.isfile(cm.PATH_DISC + "/UGBTEMP.DSK"):
#             cm.msgError("Create bin: MAIN.BIN")
#             sys.exit(1)
#         else:
#             os.remove(os.getcwd() + "/main.bin")

#         name = cm.getFile(source)
#         if extractUGBC2ImageDisc(out):
#             shutil.move(cm.PATH_LIB + "/MAIN.BIN", cm.PATH_DISC + "/" + name.upper() + ".BIN")
#             cm.msgCustom("BUILD", f"{cm.getFileExt(source)} ==> " + name.upper() + ".BIN", "green")
#             os.remove(out)
#         else:
#             cm.showFoodDataProject("Build failure disc image", 1)
#         return True

#     except subprocess.CalledProcessError as e:
#         cm.msgError(cm.getFileExt(source) + f' ==> Error executing command: {e.output.decode()}')
#         return False


def basInMergeFiles(lista, elemento):
    """
    Comprueba si el bas existe para merge

    Args:
        lista (_type_): _description_
        elemento (_type_): _description_

    Returns:
        _type_: _description_
    """
    return elemento in lista


def readContentFile( source):
    """Read content file to merge

    Args:
        source (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(source, 'r') as origen_file:
        contenfile = origen_file.read()
    return contenfile

def addContenToFile(source, text):
    """Añade el contenido del fichero a otro

    Args:
        source (_type_): _description_
        text (_type_): _description_
    """
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
    cm.msgCustom("CONVERT", f"{cm.getFileExt(source)} ==> Dos Format File", "green")
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
    cm.msgCustom("REMOVE", f"Comments Remove ==> {file}", "green")
    return True

def dsk2cpr(imagefile,imagecpr, file):
    name = cm.getFile(imagefile)
    cmd = [cm.IMAGE2CPR, imagefile, imagecpr, "-c",'RUN"'+ file]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        if not os.path.isfile(imagefile):
            cm.msgError('Error generating CPR image ' + cm.getFileExt(imagefile) + ".cpr")
            cm.showFoodDataProject("Build failure disc image", 1)
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        cm.showFoodDataProject("Build failure disc image", 1)

def createImageDisc(imagefile):
    
    cm.rmFolder(imagefile)
    
    if cm.fileExist(cm.PATH_8BP + "/dsk/8BP.dsk"):
        shutil.copy2(cm.PATH_8BP + "/dsk/8BP.dsk", imagefile)
        cm.msgCustom("MOVE", "8BP.dsk ==> " + imagefile, "green")
    else:
    
        cmd = [cm.IDSK, imagefile, "-n"]
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            if not os.path.isfile(imagefile):
                cm.msgError('Error generating disk image ' + cm.getFileExt(imagefile))
                cm.showFoodDataProject("Build failure disc image", 1)
            return True
        except subprocess.CalledProcessError as e:
            cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
            cm.showFoodDataProject("Build failure disc image", 1)


def addBas2ImageDisc(imagefile, file):
    cmd = [cm.IDSK, imagefile, "-i", file, '-t', '0']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgCustom("ADD", cm.getFileExt(file) + " ==> " + cm.getFileExt(imagefile), "green")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        return False


def addBin2ImageDisc(imagefile, file):
    cmd = [cm.IDSK, imagefile, "-i", file, '-t', '1']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgCustom("ADD", cm.getFileExt(file) + " ==> " + cm.getFileExt(imagefile), "green")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        return False


def extract2ImageDisc(imagefile, file):
    FNULL = open(os.devnull, 'w')
    cmd = [cm.IDSK, imagefile, "-g", file.upper()]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgCustom("EXTRAC", f"library " + cm.getFileExt(imagefile) + " ==> " + cm.getFile(imagefile) + ".bin",
                     "green")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        return False


# def extractUGBC2ImageDisc(imagefile):
#     FNULL = open(os.devnull, 'w')
#     cmd = [cm.IDSK, imagefile, "-g", cm.PATH_LIB + "/MAIN"]
#     try:
#         output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
#         shutil.move(cm.PATH_LIB + "/MAIN", cm.PATH_LIB + "/MAIN.BIN")
#         return True
#     except subprocess.CalledProcessError as e:
#         cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
#         return False


def addamsdos(file):
    FNULL = open(os.devnull, 'w')
    cmd = [cm.AMSDOS, file]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgCustom("ADD", "Amsdos header ==> " + cm.getFileExt(file), "green")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(file) + f' executing command: {e.output.decode()}')
        return False


def addFile2CDTImage(file, cdtimg):
    extension = cm.getFileExtension(file)
    if extension.upper() != ".BIN" or extension.upper() != ".SRC":
        typefile = "cpctxt"
    else:
        typefile = "cpc"
    name = cm.getFile(file)
    FNULL = open(os.devnull, 'w')

    cmd = [cm.CPC2CDT, "-t", "-m", typefile, "-r", name.upper(), file, cdtimg]
    try:
        output = subprocess.check_output(cmd)
        cm.msgCustom("ADD", cm.getFileExt(file) + " ==> " + cm.getFileExt(cdtimg), "green")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(file) + f' executing command: {e.output.decode()}')
        return False


def createImageCDT(imagefile):
    cm.rmFolder(imagefile)
    cmd = [cm.CDT, "-n", ".", imagefile]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        if not os.path.isfile(imagefile):
            cm.msgError('Error generating CDT image ' + cm.getFileExt(imagefile))
            cm.showFoodDataProject("BUILD FAILURE CDT IMAGE", 1)
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(imagefile) + f' executing command: {e.output.decode()}')
        cm.showFoodDataProject("BUILD FAILURE CDT IMAGE", 1)


def check_nomenclature83(path):
    try:
        archivos = os.listdir(path)
        for archivo in archivos:
            if len(cm.getFile(archivo)) > 8:
                return False
        return True
    except FileNotFoundError:

        return True
