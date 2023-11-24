
from rich.console import Console
from rich.logging import RichHandler
from rich.text import Text
from rich.console import Console
from rich import inspect
from rich.table import Table
from rich import print
from rich.columns import Columns
from CPCReady import common as cm
from CPCReady import func_update as update
import glob
import sys
import os
import random
from CPCReady import __version__ as version

console = Console()


##
# Show banner dependencie model cpc
# @
# param cpc: Model CPC
##
def projectInformation():
    print()

    # Check is cfg project exist
    if not cm.fileExist(cm.CFG_PROJECT):
        sys.exit(1)

    DATA_PROJECT = cm.getData(cm.CFG_PROJECT)
    PROJECT_NAME     = DATA_PROJECT.get('general', 'name', fallback="NONE")
    cm.showInfoTask(f"List of " + PROJECT_NAME + " files...")

    # table = Table(title="Images Files")
    # table.add_column("Folder", justify="left", style="cyan", no_wrap=True)
    # table.add_column("File", style="magenta")
    # table.add_column("Size", justify="right", style="green")
    # target_folders = ["out"]
    
    # for folder in target_folders:
    #     for basfile in glob.glob(os.path.join(folder, '*.*')):
    #             bytes = os.path.getsize(basfile)
    #             kb = cm.bytes_to_kilobytes(bytes)
    #             kb =f"{kb:.0f}"
    #             table.add_row(folder, cm.getFileExt(basfile), f"{kb} KB")            
    # print(table)
    
    table = Table(title="Project Files")
    table.add_column("Folder", justify="left", style="cyan", no_wrap=True)
    table.add_column("File", style="magenta")
    table.add_column("Size", justify="right", style="green")
    target_folders = ["src", "cfg", "docs", "lib", "spr", "scr","img"]
    
    for folder in target_folders:
        for basfile in glob.glob(os.path.join(folder, '*.*')):
                bytes = os.path.getsize(basfile)
                table.add_row(folder, cm.getFileExt(basfile), str(bytes) + " Bytes")            
    print(table)
    

    table = Table(title="Disc Files")
    table.add_column("Folder", justify="left", style="cyan", no_wrap=True)
    table.add_column("File", style="magenta")
    table.add_column("Size", justify="right", style="green")

    target_folders = [cm.PATH_DISC]
    TotalBytes = 0
    for folder in target_folders:
        for basfile in glob.glob(os.path.join(folder, '*.*')):
                bytes = os.path.getsize(basfile)
                TotalBytes = TotalBytes + bytes
                table.add_row(folder, cm.getFileExt(basfile), str(bytes) + " Bytes")      
    sizeDisc = cm.bytes_to_kilobytes(TotalBytes)
    table.add_row("--------", "--------", "---------")

    if sizeDisc > 174:
        table.add_row("", "[bold yellow]WARNING !!", f"[bold yellow]{sizeDisc:.0f} KB")
    else:
        table.add_row("", "", f"[bold green]{sizeDisc:.0f} KB")
    print(table)

    print()
    cm.showFoodDataProject("Successfully list files", 0)