import os
import sys
import datetime
import time
import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.text import Text
from rich.console import Console
from rich import inspect
from rich.table import Table
from rich import print
from rich.columns import Columns

console = Console()

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)


log = logging.getLogger("rich")


CPC464= """
[grey]█▀▀█ █▀▄▀█ █▀▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄                                     ╔═╗╔═╗╔═╗ ┏┓┏┓┏┓ ┌─────────────┐  ON 🟢
[grey]█▄▄█ █ █ █ ▀▀▀▄▄   █   █▄▄▀ █▄▄█ █  █                                     ║  ╠═╝║   ┃┃┣┓┃┃ │[red] ███ [green]███ [blue]███ [white]│
[grey]█  █ █   █ █▄▄▄█   █   █  █ █  █ █▄▄▀     64K COLOUR PERSONAL COMPUTER[white]    ╚═╝╩  ╚═╝ ┗╋┗┛┗╋ └─────────────┘ COLOR
"""
CPC6128 = """[grey]█▀▀█ █▀▄▀█ █▀▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄                                                      ┌─────────────┐  ENC.
[grey]█▄▄█ █ █ █ ▀▀▀▄▄   █   █▄▄▀ █▄▄█ █  █                                                      │[red] ███ [green]███ [blue]███ [white]│  [green]▄▄▄[/green]
[grey]█  █ █   █ █▄▄▄█   █   █  █ █  █ █▄▄▀     128K ORDENADOR PERSONAL[white]                          └─────────────┘"""
CPC664 = """
[grey]█▀▀█ █▀▄▀█ █▀▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄                                     ╔═╗╔═╗╔═╗ ┏┓┏┓┏┓ ┌─────────────┐  ON 🟡
[grey]█▄▄█ █ █ █ ▀▀▀▄▄   █   █▄▄▀ █▄▄█ █  █                                     ║  ╠═╝║   ┣┓┣┓┃┃ │[red] ███ [green]███ [blue]███ [white]│
[grey]█  █ █   █ █▄▄▄█   █   █  █ █  █ █▄▄▀     64K COLOUR PERSONAL COMPUTER[white]    ╚═╝╩  ╚═╝ ┗┛┗┛┗╋ └─────────────┘ COLOR
"""

def banner(cpc):
    
    BANNER = Table(show_header=False)

    if cpc == 6128:
        BANNER.add_row(CPC6128)
    elif cpc == 464:
        BANNER.add_row(CPC6128)
    elif cpc == 665:
        BANNER.add_row(CPC6128)
    else:
        msgError("Model CPC not supported")
        sys.exit (1)
    
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
    log.debug(message)


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
# Remove comment lines
#
# @param source: source filename
# @param output: output filename
##
def removeComments(source, output):
    global file
    if not os.path.exists(source):
        msgError(f"The " + getFileExt(source) +" file does not exist")
        return False

    with open(source, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if not line.startswith("1'") and not line.startswith("1 '")]

    with open(output, 'w') as file:
        file.writelines(filtered_lines)
    file = getFileExt(source)
    msgInfo(file +"[green] ==> [/green]File Comments Removed")
    return True

    
def convert2Dos(source, output):
    if not os.path.exists(source):
        msgError(f"The " + getFileExt(source) +" file does not exist")
        return False
    with open(source, 'r') as file:
        unix_lines = file.readlines()

    dos_lines = [line.rstrip('\n') + '\r\n' for line in unix_lines]

    with open(output, 'w') as file:
        file.writelines(dos_lines)

    files = getFileExt(source)
    msgInfo(files +"[green] ==> [/green]Convert unix to dos")
    return True

##
# Concatenate Bas file
#
# @param source: source file name
# @param output: output file name
##
def concatFile(source, output):
    with open(source, 'r') as origen_file:
        contenido_origen = origen_file.read()
    with open(output, 'a') as destino_file:
        destino_file.write(contenido_origen)
    os.remove(source)
    # messageInfo(getFileExt(source), f"Concatenate in {getFileExt(output)}.")
    msgInfo(getFileExt(source) + f" ==> {getFileExt(output)}")
    return True

##
# verify file exist
#
# @param source: source file name
##
def fileExist(source):
    if not os.path.isfile(source):
        msgError(getFileExt(source) +"[red] ==> FILE DOES NOT EXIST")
        return False
    return True

##
# Concatenate Bas files
#
# @param files: list files separate with ","
# @param output: output filename
##
def concatBasFiles(files, output, folder):
    if files != "":
        ficheros = files.split(',')
        folder = folder + "/"
        if os.path.exists(folder + output):
            os.remove(folder + output)
        with open(folder + output, 'a') as salida:
            for fichero in ficheros:
                nombre_fichero = fichero.strip()
                if os.path.exists(folder + nombre_fichero):
                    with open(folder + nombre_fichero, 'r') as archivo:
                        contenido = archivo.read()
                        salida.write(contenido)
                    os.remove(folder + nombre_fichero)
                    msgInfo(nombre_fichero + f" ==> {getFileExt(output)}")
                else:
                    msgError(f"The " + getFileExt(nombre_fichero) +" file does not exist")
                    return False
    else:
        msgWarning("Warning Not concat files.")
        return True
    return True

##
# end compilation
#
# @param type: show final compilation values OK or ERROR
##
def endCompilation(type,start_time):
    end_time = time.time()  # Registrar el tiempo de finalización
    execution_time = end_time - start_time
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    console.print("\n[bold white]------------------------------------------------------------------------------------- [/bold white]")
    if type == "OK":
        console.print("[bold green]BUILD SUCCESSFULLY [/bold green]")
    if type == "ERROR":
        console.print("[bold red]BUILD FAILURE [/bold red]")
    console.print("[bold white]------------------------------------------------------------------------------------- [/bold white]")
    console.print(f"[white]Total time: {execution_time:.2f} seg [/white]")
    console.print(f"[white]Finished at: {formatted_datetime}[/white]")
    console.print("[bold white]------------------------------------------------------------------------------------- [/bold white]")
    if type == "ERROR":sys.exit(1)
    if type == "OK":sys.exit(0)
##
# begin compilation
#
# @param project: show project name in initial compilation
##
def beginCompilation(project,author,model):
    # console.print("\n[bold white]------------------------------------------------------------------------------------- [/bold white]")
    # console.print("[bold blue] PROJECT: [/bold blue][bold white]" + project + "[/bold white]")
    # console.print("[bold white]------------------------------------------------------------------------------------- [/bold white]\n")
    console.print("\n[bold white]------------------------------------------------------------------------------------- [/bold white]")
    console.print("[bold blue] PROJECT: [/bold blue][bold white]" + project + "[/bold white]")
    console.print("[bold blue] AUTHOR : [/bold blue][bold white]" + author + "[/bold white]")
    console.print("[bold blue] MODEL  : [/bold blue][bold white]CPC " + str(model) + "[/bold white]")
    console.print("[bold white]------------------------------------------------------------------------------------- [/bold white]\n")

##
# compilation image
#
# @param project: image name
##
def imageCompilation(image):
    console.print("\n[bold white]------------------------------------------------------------------------------------- [/bold white]")
    console.print("[bold blue] IMAGE: [/bold blue][bold white]" + image + "[/bold white]")
    console.print("[bold white]------------------------------------------------------------------------------------- [/bold white]\n")

##
# create project
#
# @param project: image name
##
def createProject(project):
    console.print("\n[bold white]------------------------------------------------------------------------------------- [/bold white]")
    console.print("[bold blue]CREATE PROJECT: [/bold blue][bold white]" + project + "[/bold white]")
    console.print("[bold white]------------------------------------------------------------------------------------- [/bold white]\n")

##
# end create project
#
# @param type: show final compilation values OK or ERROR
##
def endCreteProject(type):
    console.print("\n[bold white]------------------------------------------------------------------------------------- [/bold white]")
    if type == "OK":
        console.print("[bold green]CREATE PROJECT SUCCESSFULLY [/bold green]")
    if type == "ERROR":
        console.print("[bold red]CREATE PROJECT FAILURE [/bold red]")
    console.print("[bold white]------------------------------------------------------------------------------------- [/bold white]")
    if type == "ERROR":sys.exit(1)
    if type == "OK":sys.exit(0)