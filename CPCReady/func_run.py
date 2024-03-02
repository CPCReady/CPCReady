
import os
import sys
import datetime
import shutil
from jinja2 import Template
import subprocess
from CPCReady import common as cm
from CPCReady import func_info as info
import io
import platform


def ping_ok(sHost) -> bool:
    try:
        subprocess.check_output(
            "ping -{} 1 {}".format("n" if platform.system().lower() == "windows" else "c", sHost), shell=True
        )
    except Exception:
        return False

    return True


def executeFileM4BOARD(ip, file):
    FNULL = open(os.devnull, 'w')
    cmd = [cm.M4BOARD, "-x", ip, file]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgInfo("Execute " + cm.getFileExt(file) + " ==> M4 Board")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(file) + f' executing command: {e.output.decode()}')
        return False


def uploadFileM4BOARD(ip, file, folder):
    FNULL = open(os.devnull, 'w')
    cmd = [cm.M4BOARD, "-u", str(ip), str(file), str(folder), "0"]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgInfo("Upload " + cm.getFileExt(file) + " ==> M4 Board")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(file) + f' executing command: {e.output.decode()}')
        return False


def launch(emulador):
    
    print()
    if not cm.fileExist(cm.CFG_PROJECT):
        sys.exit(1)

    DATA_EMULATORS = cm.getEmulators()

    if not validateSettingEmulator(emulador,DATA_EMULATORS):
        cm.msgError(f"Config Emulator {emulador} not exist in settings project.")

    cm.showInfoTask(f"Launch DSK in progress...")
    run   = cm.getSEmulatorRun(emulador)
    model = cm.getSEmulatorModel(emulador)
    image = cm.getNameProject() + ".DSK"
    cm.msgInfo(f"Emulator settings ==> {emulador}")
    cm.msgInfo(f"Emulator model ==> {model}")
    cm.msgInfo(f"Emulator run ==> {run}")

    rvmDesktop("RetroVirtualMachine", cm.PATH_OUT + "/" + image, model, run)
    cm.showFoodDataProject("Successfully launch disc image", 0)
    print()
    return
    

    # RVM_EMULATOR_TYPE = DATA_EMULATORS.get(emulator, 'type', fallback="NONE")
    # RVM_CPC_MODEL = DATA_EMULATORS.get(emulator, 'model', fallback="NONE")
    # RVM_CPC_RUN = DATA_EMULATORS.get(emulator, 'run', fallback="NONE")
    # RVM_CPC_IMAGE = DATA_EMULATORS.get(emulator, 'image', fallback="NONE")
    # # RVM_CPC_PATH       = DATA_EMULATORS.get(emulator,'path',fallback="NONE")

    # if RVM_EMULATOR_TYPE not in cm.EMULATORS_TYPES:
    #     cm.msgError(f"The {RVM_EMULATOR_TYPE} emulator type is not supported.")
    #     sys.exit(1)
    # if RVM_CPC_MODEL not in cm.CPC_MODELS:
    #     cm.msgError(f"CPC Model {RVM_CPC_MODEL} not supported.")
    #     sys.exit(1)
    # if not cm.fileExist(RVM_CPC_IMAGE):
    #     sys.exit(1)

    #     # info.show("👉 DSK FILE: " + RVM_CPC_IMAGE)

    # print()
    # cm.showInfoTask(f"Launch disc image " + RVM_CPC_IMAGE + " in progress...")

    # cm.msgInfo(f"Emulator type ==> {RVM_EMULATOR_TYPE}")
    # cm.msgInfo(f"CPC Model     ==> {RVM_CPC_MODEL}")
    # cm.msgInfo(f"CPC Image     ==> {RVM_CPC_IMAGE}")

    # if RVM_EMULATOR_TYPE.upper() == "DESKTOP" and os.getenv("ENVIRONMENT") == "DOCKER":
    #     cm.msgError(f"It is not possible to run RetroVirtualMachine Desktop in a container environment..")
    #     cm.showFoodDataProject("Failure launch disc image", 1)
    #     sys.exit(1)

    # if RVM_EMULATOR_TYPE.upper() == "DESKTOP":

    #     rvmDesktop("RetroVirtualMachine", RVM_CPC_IMAGE, RVM_CPC_MODEL, RVM_CPC_RUN)
    #     cm.showFoodDataProject("Successfully launch disc image", 0)
    #     print()
        
    # elif RVM_EMULATOR_TYPE.upper() == "WEB":
    #     module_path = os.path.dirname(os.path.abspath(__file__))
    #     cfg_path = os.path.join(module_path, 'cfg') + "/monitor.png"
            
    #     context = {
    #         'name': "RETRO VIRTUAL MACHINE WEB",
    #         'model': RVM_CPC_MODEL,
    #         'dsk': f"{RVM_CPC_IMAGE}",
    #         'run': f'{RVM_CPC_RUN}'
    #     }

    #     cm.createTemplate("rvm-web.html", context, "cfg/" + emulator + ".html")
    #     cm.showFoodDataProject("Template RVM Web Create successfully", 0)
    #     print()
        
    # elif RVM_EMULATOR_TYPE.upper() == "M4BOARD":

    #     PROJECT_M4_EXECUTE = DATA_EMULATORS.get(emulator, 'execute', fallback="")
    #     PROJECT_M4_FOLDER = DATA_EMULATORS.get(emulator, 'folder', fallback="CPCReady")
    #     PROJECT_M4BOARD_IP = DATA_EMULATORS.get(emulator, 'ip', fallback="NONE")
    #     cm.msgInfo(f"Emulator type ==> M4 Board")
    #     cm.msgInfo(f"CPC Image     ==> {RVM_CPC_IMAGE}")
    #     cm.msgInfo(f"Files         ==> {PROJECT_M4_FOLDER}")
    #     if PROJECT_M4BOARD_IP == "NONE":
    #         cm.msgError(f"No ip found in {cm.CFG_EMULATORS} for M4 Board")
    #     if not cm.validateIP(PROJECT_M4BOARD_IP):
    #         sys.exit(1)
    #     if not ping_ok(PROJECT_M4BOARD_IP):
    #         cm.msgError(f"No connect    ==> {PROJECT_M4BOARD_IP}")
    #         cm.msgInfo(f"Connect OK    ==> {PROJECT_M4BOARD_IP}")
    #         sys.exit(1)
    #     else:
    #         cm.msgInfo(f"Connect OK    ==> {PROJECT_M4BOARD_IP}")

    #     count = 0

    #     archivos = os.listdir(cm.PATH_DISC)
    #     for archivo in archivos:
    #         if os.path.isfile(os.path.join(cm.PATH_DISC, archivo)):
    #             if not uploadFileM4BOARD(PROJECT_M4BOARD_IP, cm.PATH_DISC + "/" + archivo, PROJECT_M4_FOLDER):
    #                 sys.exit(1)
    #         count = count + 1

    #     if count > 0:
    #         if cm.fileExist(cm.PATH_DISC + "/" + PROJECT_M4_EXECUTE):
    #             if not executeFileM4BOARD(PROJECT_M4BOARD_IP, PROJECT_M4_FOLDER + "/" + PROJECT_M4_EXECUTE):
    #                 sys.exit(1)

    #             cm.msgInfo(f"Files upload and execute in M4 Board.")
    #     else:
    #         cm.msgWarning("No upload files in " + cm.PATH_DISC)

    #     cm.showFoodDataProject("Successfully send files to M4 Board", 0)
    #     print()

def rvmDesktop(RVM_CPC_PATH, RVM_CPC_IMAGE, RVM_CPC_MODEL, RVM_CPC_RUN):
    FNULL = open(os.devnull, 'w')
    try:
        retcode = subprocess.Popen(
            [RVM_CPC_PATH, "-i", RVM_CPC_IMAGE, "-b=cpc" + str(RVM_CPC_MODEL), "-c=" + RVM_CPC_RUN + "\n"],
            stdout=FNULL, stderr=subprocess.STDOUT)
        cm.msgInfo(f"Disk image launched successfully")
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Failed to launch {cm.getFileExt(RVM_CPC_IMAGE)} image on RVM Desktop: {e.output.decode()}')
        sys.exit(1)

def validateSettingEmulator(emulator,listEmulators):
    for modelos in listEmulators:
        if str(modelos) == str(emulator):
            return True
    return False   
    