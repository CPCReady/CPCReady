import os
import sys
import datetime
import time
import logging
import shutil
from rich.console import Console
from rich.logging import RichHandler
from rich.text import Text
from rich.console import Console
from rich import inspect
from rich.table import Table
from rich import print
from rich.columns import Columns

console = Console()
log = logging.getLogger("rich")

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

CPC464 = """[grey]█▀▀█ █▀▄▀█ █▀▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄                                     ╔═╗╔═╗╔═╗ ┏┓┏┓┏┓ ┌─────────────┐  ON 🟢
[grey]█▄▄█ █ █ █ ▀▀▀▄▄   █   █▄▄▀ █▄▄█ █  █                                     ║  ╠═╝║   ┃┃┣┓┃┃ │[red] ███ [green]███ [blue]███ [white]│
[grey]█  █ █   █ █▄▄▄█   █   █  █ █  █ █▄▄▀     64K COLOUR PERSONAL COMPUTER[white]    ╚═╝╩  ╚═╝ ┗╋┗┛┗╋ └─────────────┘ COLOR"""

CPC6128 = """[grey]█▀▀█ █▀▄▀█ █▀▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄                                                      ┌─────────────┐  ENC.
[grey]█▄▄█ █ █ █ ▀▀▀▄▄   █   █▄▄▀ █▄▄█ █  █                                                      │[red] ███ [green]███ [blue]███ [white]│  [green]▄▄▄[/green]
[grey]█  █ █   █ █▄▄▄█   █   █  █ █  █ █▄▄▀     128K ORDENADOR PERSONAL[white]                          └─────────────┘"""

CPC664 = """[grey]█▀▀█ █▀▄▀█ █▀▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄                                     ╔═╗╔═╗╔═╗ ┏┓┏┓┏┓ ┌─────────────┐  ON 🟢
[grey]█▄▄█ █ █ █ ▀▀▀▄▄   █   █▄▄▀ █▄▄█ █  █                                     ║  ╠═╝║   ┣┓┣┓┃┃ │[red] ███ [green]███ [blue]███ [white]│
[grey]█  █ █   █ █▄▄▄█   █   █  █ █  █ █▄▄▀     64K COLOUR PERSONAL COMPUTER[white]    ╚═╝╩  ╚═╝ ┗┛┗┛┗╋ └─────────────┘ COLOR"""

## Common Variables
#
##

subfolders = ["assets", "out", "dsk", "src", "cfg"]

CFG_PROJECT      = "cfg/cpcready.cfg"
TEMPLATE_RVM_WEB = "rvm-web.html"
PATH_DISC        = "out"
PATH_OBJ         = "obj"
PATH_SRC         = "src"
PATH_DSK         = "dsk"
PATH_ASSETS      = "assets"

if sys.platform == "win32":
    cm.msgError(f"WIN32 Platform not supported")
    sys.exit(1)   

if sys.platform == "win64":
    TEMP_PATH = os.getenv('TEM')
    MARTINE = os.path.dirname(os.path.abspath(__file__)) + "/tools/win/martine.exe"
    DSK = os.path.dirname(os.path.abspath(__file__)) + "/bin/win64/iDSK.exe"
    UGBASIC = os.path.dirname(os.path.abspath(__file__)) + "/bin/win64/ugb.exe"
if sys.platform == 'darwin':
    TEMP_PATH = os.getenv('TMPDIR')
    MARTINE = os.path.dirname(os.path.abspath(__file__)) + "/tools/" + sys.platform + "/martine"
    IDSK = os.path.dirname(os.path.abspath(__file__)) + "/tools/darwin/iDSK"
if sys.platform.startswith('linux'):
    TEMP_PATH = os.getenv('TMP')
    MARTINE = os.path.dirname(os.path.abspath(__file__)) + "/tools/" + sys.platform + "/martine"
    IDSK = os.path.dirname(os.path.abspath(__file__)) + "/tools/linux/iDSK"
    UGBASIC = os.path.dirname(os.path.abspath(__file__)) + "/bin/linux/ugb"
    
PWD = os.getcwd() + "/"

##
# Delete folder
#
# @param directory: directory to remove
##

def rmFolder(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)


##
# Show banner dependencie model cpc
#
# @param cpc: Model CPC
##
def banner(cpc):
    BANNER = Table(show_header=False)

    if cpc == 6128:
        BANNER.add_row(CPC6128)
    elif cpc == 464:
        BANNER.add_row(CPC464)
    elif cpc == 664:
        BANNER.add_row(CPC664)
    else:
        msgError("Model CPC not supported")
        sys.exit(1)

    console.print(BANNER)


##
# Print message warning
#
# @param file: File to which the message refers
# @param message: message to display
##
def msgWarning(message):
    log.warning(message)


##
# Print message eror
#
# @param file: File to which the message refers
# @param message: message to display
##
def msgError(message):
    log.error(message)


##
# Print message info
#
# @param file: File to which the message refers
# @param message: message to display
##
def msgInfo(message):
    log.info(message)


##
# Print message debug
#
# @param file: File to which the message refers
# @param message: message to display
##
def msgInfo(message):
    log.info(message)


##
# Get Get file without extension
#
# @param source: source filename
##
def getFile(source):
    file_name = os.path.basename(source)
    file_name = os.path.splitext(file_name)[0]
    return file_name


##
# Get file and extension
#
# @param source: source filename
##
def getFileExt(source):
    file_name = os.path.basename(source)
    return file_name


##
# Get extension file
#
# @param source: source filename
##
def getFileExtension(source):
    file_extension = os.path.splitext(source)[1]
    return file_extension


##
# Show head data proyect
#
# @param project: project name
##

def showHeadDataProject(project):
    description = f"*** {project} ***"
    center_text = description.center(80)
    console.print(
        "[bold yellow]\n==================================================================================== [/bold yellow]")
    console.print("[bold yellow]" + center_text.upper() + "[/bold yellow]")
    console.print(
        "[bold yellow]====================================================================================\n [/bold yellow]")


##
# Show food data proyect
#
# @param description: description to show
# @param out: 1 is error, 0 is ok
##

def showFoodDataProject(description, out):
    description = f"*** {description} ***"
    center_text = description.center(80)
    console.print(
        "[bold yellow]\n==================================================================================== [/bold yellow]")
    if out == 0:
        console.print("[bold green]" + center_text.upper() + "[/bold green]")
        console.print("[bold yellow]====================================================================================\n [/bold yellow]")
    if out == 1:
        console.print("[bold red]" + center_text.upper() + "[/bold red]")
        console.print("[bold yellow]====================================================================================\n [/bold yellow]")
        sys.exit(1)


##
# verify file exist
#
# @param source: source file name
##
def fileExist(source):
    if not os.path.isfile(source):
        msgError(f"File {source} does not exist.")
        return False
    return True


##
# Remove directory
#
# @param directory: directory name
##
def removeContentDirectory (directory):

    if os.path.exists(directory) and os.path.isdir(directory):
        archivos = os.listdir(directory)
        for archivo in archivos:
            ruta_completa = os.path.join(directory, archivo)
            if os.path.isfile(ruta_completa):
                os.remove(ruta_completa)
    msgInfo(f"Clean temporal directory.")            
                
##
# compilation image
#
# @param project: image name
##
def imageCompilation(image):
    console.print(
        "\n[bold white]------------------------------------------------------------------------------------- [/bold white]")
    console.print("[bold blue] IMAGE: [/bold blue][bold white]" + image + "[/bold white]")
    console.print(
        "[bold white]------------------------------------------------------------------------------------- [/bold white]\n")
