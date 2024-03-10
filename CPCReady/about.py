
from rich.console import Console
from rich.logging import RichHandler
from rich.text import Text
from rich.console import Console
from rich import inspect
from rich.table import Table
from rich import print
from rich.columns import Columns
from CPCReady import common as cm
from CPCReady import upgrade as update

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
def show(description=True):
    print()
    LOGOCPCREADY2 = f"""[bold white]╔═╗╔═╗╔═╗   
[bold white]║  ╠═╝║    
[bold white]╚═╝╩  ╚═╝
[bold yellow]Ready[/]"""

    BANNER = Table(show_header=False)
    check_version_local = update.check_version()
    if not check_version_local == "99.99.99":
        TEXT = f"[bold white]👋 New version {check_version_local} found. Please Upgrade.!!![/]"
        new_version = True
    else:
        TEXT = f"[bold white]Version: {version}"
        new_version = False


    if description:
        print(LOGOCPCREADY2)
        print()
        if new_version:
            BANNER.add_row(TEXT)
            console.print(BANNER)
        else:
            print(TEXT)
        print("[bold white]Github : [/]https://github.com/CPCReady/sdk")
        print("[bold white]Docs   : [/]https://cpcready.github.io/doc/")
        print()
        print("[bold yellow]Ready[/]")
        print("[bold yellow]█[/]")
    else:
        if new_version:
            BANNER.add_row(TEXT)
            console.print(BANNER)        
    # if not description:
    #     BANNER.add_row(TEXT)
    #     console.print(BANNER)   
    #     print()         
    #     return
    print()
