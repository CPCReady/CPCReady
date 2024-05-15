import os
import configparser
from pathlib import Path
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.styles import Style

dialog_style = Style.from_dict({
    'dialog':             'bg:#000080',
    'dialog frame.label': 'bg:#000080 #ffffff',
    'dialog.body':        'bg:#000080 #ffffff',
    'dialog shadow':      'bg:#000080',
    'dialog button':      'bg:green red',
})

def about():
    message_dialog(
        title=HTML('<style fg="white">About CPCReady</style> '),
        text=HTML(
            '<style fg="white">       Software Developer Kit    (v1.0.0)</style>\n'
            '<style fg="white">       ╔═╗╔═╗╔═╗  ┌──────────┐</style>\n'
            '<style fg="white">       ║  ╠═╝║    │ </style>'
            '<style fg="ansired">██</style> '  # Primer ██ en rojo
            '<style fg="ansigreen">██</style> '  # Segundo ██ en verde
            '<style fg="ansiblue">██</style> '  # Tercer ██ en azul
            '<style fg="ansiwhite">│</style>\n'  # Tercer ██ en azul
            '<style fg="white">       ╚═╝╩  ╚═╝  └──────────┘</style>\n'
            '<style fg="white">       Ready</style>\n'
            '<style fg="white">       █</style>\n'
        ),
        style=dialog_style
    ).run()
    
def readKey(File, key, default="Key not found"):
    config = configparser.ConfigParser()
    archivo = Path(File)
    with open(archivo, "r") as f:
        contenido = f.read()
    if not contenido.strip().startswith("["):
        contenido = "[DEFAULT]\n" + contenido
    config.read_string(contenido)
    readkey = config.get("DEFAULT", key, fallback=default)
    return readkey

def executeCommand(command):
    # Ejecutar el comando y capturar la salida
    with os.popen(command) as resultado:
        salida = resultado.read()
        print(salida)

def cpcModels(model,emulator):
    
    if model == "6128" and emulator == "rvm":
        print("""
 Amstrad 128K Microcomputer    (v3)
 ©1985 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.1

Ready""")
    elif model =="464" and emulator == "rvm":
        print ("""
 Amstrad 64K Microcomputer    (v1)
 ©1984 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.0

Ready""") 

    elif model =="664" and emulator == "rvm":
        print ("""
 Amstrad 64K Microcomputer    (v2)
 ©1984 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.1

Ready""")
    elif model =="6128" and emulator == "m4":
        print("""
 Amstrad 128K Microcomputer    (v3)
 ©1985 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.1

 M4 Board v2.0.6
 
Ready""")
    elif model =="464" and emulator == "m4":
        print("""
 Amstrad 64K Microcomputer    (v1)
 ©1984 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.0

 M4 Board v2.0.6
 
Ready""")
    elif model =="664" and emulator == "m4":
        print("""
 Amstrad 64K Microcomputer    (v2)
 ©1984 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.1

 M4 Board v2.0.6
 
Ready""")
