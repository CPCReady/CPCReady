
import os
from dotenv import load_dotenv
from CPCReady import common as cm

from rich.logging import RichHandler
from rich.console import Console
from rich.table import Table
from rich import print

home_dir = os.path.expanduser("~")
cpc_file_path = os.path.join(home_dir, ".cpcready")

def loadYaml(path):

    if not path or path == "None":
        path = os.getcwd() + "/"
        
    if os.path.exists(cpc_file_path):
        os.remove(cpc_file_path)

    with open(cpc_file_path, 'w') as file:
        file.write(f"PATH_PROJECT={path}\n")
    if readEnvironmentVariable():
        print("[bold yellow]Ready[/]")
        print("[bold yellow]█[/]")

def readEnvironmentVariable():
    load_dotenv(cpc_file_path)
    if os.path.exists(cm.PATH_CFG) + "/" + cm.FILE_PROJECT:
        return True

