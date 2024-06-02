#!/bin/bash
##------------------------------------------------------------------------------
##
##        ██████╗██████╗  ██████╗██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗
##       ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
##       ██║     ██████╔╝██║     ██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝ 
##       ██║     ██╔═══╝ ██║     ██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝  
##       ╚██████╗██║     ╚██████╗██║  ██║███████╗██║  ██║██████╔╝   ██║   
##        ╚═════╝╚═╝      ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   
##
##-----------------------------LICENSE NOTICE------------------------------------
##  This file is part of CPCReady Basic programation.
##  Copyright (C) 2024 Destroyer
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU Lesser General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU Lesser General Public License for more details.
##
##  You should have received a copy of the GNU Lesser General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##------------------------------------------------------------------------------


## VARIABLES SDK CPCREADY

PATH_VERSION_FILE="$HOMEBREW_PREFIX/share/VERSION"

if [[ "$OSTYPE" == "linux-gnu" ]]; then
   TEMPLATE_CPCEMU="$HOMEBREW_PREFIX/share/cpcemu/cpcemu0.cfg"
elif [[ "$OSTYPE" == "darwin"* ]]; then
   TEMPLATE_CPCEMU="$HOMEBREW_PREFIX/share/CPCemuMacOS.app/Contents/Resources/cpcemu0.cfg"
else
   PRINT ERROR "$OSTYPE Operating system NOT supported."
fi

## VARIABLES COLORES

RED=$'\033[0;31;49m'
GREEN=$'\033[38;5;040m'
BG_BLUE=$'\033[44m'
MAGENTA=$'\033[0;35;49m'
BLUE=$'\033[38;5;033m'
CYAN=$'\033[0;36;49m'
YELLOW=$'\033[0;33;49m'
WHITE=$'\033[0;37;49m'
NORMAL=$'\033[0;39;49m'
BOLD="$(tput bold)"

## VARIABLES PROYECTOS

IN_BAS="src"
OUT="out/M4Board"
OUT_DISC="out/disc"
OUT_TAPE="out/tape"
PATH_CONFIG_PROJECT="cfg"
CONFIG_CPCREADY="CPCReady.cfg"
CONFIG_CPCEMU="CPCEmu.cfg"


function show_version {
   CPCREADY
}

## Funcion que pinta Ready de amstrad
function ready {
   echo
   echo "Ready" >&2
   echo "█" >&2
   # echo "${YELLOW}Ready" >&2
   # echo "${YELLOW}█" >&2
   echo
}

## Función para verificar si existe el archivo
## .CPCReady en el directorio actual
function check_env_file {
   if [ ! -f "$PATH_CONFIG_PROJECT/$CONFIG_CPCREADY" ]; then
      echo
      PRINT "ERROR" "El archivo $PATH_CONFIG_PROJECT/$CONFIG_CPCREADY no existe en este directorio."
   fi
}

# ## informacion finalizacion tarea ok
# ## $1 : descripcion tarea
# message_success(){
#    echo
#    echo "${GREEN}→ $1"
# }

## informacion finalizacion tarea ok
## $1 : descripcion tarea
# message_build_ok(){
#    echo "${WHITE}    → ${GREEN}$1${NORMAL}"
# }

## informacion finalizacion tarea ok
## $1 : descripcion tarea
# message_build_error(){
#    echo "${WHITE}    → ${RED}$1"
# }

## informacion finalizacion tarea error
## $1 : descripcion tarea
# message_error(){
#    echo
#    echo "${RED}${BOLD}$1${NORMAL}"
# }

## informacion finalizacion tarea error
## $1 : descripcion tarea
# message_info(){
#    echo
#    echo "${BLUE}${BOLD}$1${NORMAL}"
# }

## informacion inicio tarea
## $1 : descripcion tarea
# message_progress(){
#    echo
#    echo "${YELLOW}👉 $1 in progress...🍺"
#    echo
# }

## cambios en el archivo .CPCReady valor MODE
## $1 : value mode
# function change_mode {
#    sed -i.bak "s/^MODE=.*$/MODE=$1/" "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCREADY"
#    rm "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCREADY.bak"
# }

# ## cambios en el archivo .CPCReady valor DISC
# ## $1 : value disc
# function change_disc {
#    sed -i.bak "s/^DISC=.*$/DISC=$1/" "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCREADY"
#    rm "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCREADY.bak"
# }

# ## cambios en el archivo .cpcemu.cfg valor DRIVE_A
# ## $1 : value disc
# function change_disc_cpcemu {
#    PATH_DISCO="$PWD/$OUT_DISC"
#    sed -i.bak "s/^DRIVE_A=.*$/DRIVE_A=\"$(printf '%s\n' "$PATH_DISCO" | sed 's/[\/&]/\\&/g')\/$(printf '%s\n' "$1" | sed 's/[\/&]/\\&/g')\"/" "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCEMU"
#    rm "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCEMU.bak"
# }

# function change_disc_in_config_files {
#    PATH_ESCAPED=$(printf '%s\n' "$1" | sed 's/[\&/]/\\&/g')
#    project=$(basename "$PATH_ESCAPED")
#    PATH_DSK="$PATH_ESCAPED/$OUT_DISC/$project.dsk"
#    sed -i.bak 's/^DRIVE_A=.*$/DRIVE_A='"\"$PATH_DSK\""'/' "$PATH_ESCAPED/$PATH_CONFIG_PROJECT/$CONFIG_CPCEMU"
#    rm "$PATH_ESCAPED/$PATH_CONFIG_PROJECT/$CONFIG_CPCEMU.bak"
# }




# ## cambios en el archivo .cpcemu.cfg valor M4_SD_PATH
# ## $1 : path
# function change_m4_path_in_config_files {
#    PATH_M4="$1/$OUT"
#    PATH_M4_escaped=$(printf '%s\n' "$PATH_M4" | sed 's/[\&/]/\\&/g')
#    sed -i.bak 's/^M4_SD_PATH=.*$/M4_SD_PATH='"\"$PATH_M4_escaped\""'/' "$1/$PATH_CONFIG_PROJECT/$CONFIG_CPCEMU"
#    rm "$1/$PATH_CONFIG_PROJECT/$CONFIG_CPCEMU.bak"
# }

# ## cambios en el archivo CONFIG_CPCREADY y CONFIG_CPCEMU valor MODEL
# ## $1 : value _model
# function change_model_in_config_files {

#    case $1 in
#       "464")
#          MODEL="0"
#          ;;
#       "664")
#          MODEL="1"
#          ;;
#       "6128")
#          MODEL="2"
#          ;;
#       *)
#          PRINT ERROR "CPC model $1 is not supported."
#          ;;
#    esac

#    sed -i.bak "s/^CPC_TYPE=.*$/CPC_TYPE=$MODEL/" "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCEMU"
#    sed -i.bak "s/^MODEL=.*$/MODEL=$1/" "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCREADY"
#    rm "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCEMU.bak"
#    rm "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCREADY.bak"

# }





# ## cambios en el archivo .CPCReady valor MODEL
# ## $1 : value disc
# function change_model {
#    sed -i.bak "s/^MODEL=.*$/MODEL=$1/" "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCREADY"
#    rm "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCREADY.bak"
# }

# ## cambios en el archivo .cpcemu valor CPC_TYPE
# ## $1 : value disc
# function change_model_cpcemu {
#    case $1 in
#       "464")
#          MODEL="0"
#          ;;
#       "664")
#          MODEL="1"
#          ;;
#       "6128")
#          MODEL="2"
#          ;;
#       *)
#          PRINT ERROR "CPC model $1 is not supported."
#          ;;
#    esac

#    sed -i.bak "s/^CPC_TYPE=.*$/CPC_TYPE=$MODEL/" "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCEMU"
#    rm "$2/$PATH_CONFIG_PROJECT/$CONFIG_CPCEMU.bak"
# }

compare_versions() {
  if [ "$1" == "$2" ]; then
    return 0
  fi

  local IFS=.
  local i ver1=($1) ver2=($2)

  # Comparar cada parte de la versión
  for ((i=${#ver1[@]}; i<${#ver2[@]}; i++)); do
    ver1[i]=0
  done

  for ((i=0; i<${#ver1[@]}; i++)); do
    if [[ -z ${ver2[i]} ]]; then
      ver2[i]=0
    fi
    if ((10#${ver1[i]} > 10#${ver2[i]})); then
      return 1
    fi
    if ((10#${ver1[i]} < 10#${ver2[i]})); then
      return 2
    fi
  done

  return 0
}

function create_dsk {
    local DSK_IMAGE="$1"
    TAG=$(basename "$1")
   #  PRINT "TAG" "$TAG"
    if iDSK "$DSK_IMAGE" -n > /dev/null 2>&1; then
      IMAGE=$(basename "$DSK_IMAGE")
      PRINT OK "Drive A: $IMAGE"
      #   echo -e "Drive A: $DISC"
    else
      #   echo -e "Drive A: $DISC"
        PRINT "ERROR" "There was an error creating the disk image."
    fi
}

function add_ascii_dsk {
   local DSK_IMAGE="$1"
   local ASCII_FILE="$2"
   if iDSK "$DSK_IMAGE" -i "$ASCII_FILE" -t 0 > /dev/null 2>&1; then
      PRINT "OK" "File added to the disk image."
   else
      PRINT "ERROR" "There was an error adding the file to the disk image."
   fi
}

function rm_comments {
    local archivo_origen="$1"
    local archivo_destino="$2"

    if [[ "$(uname)" == "Darwin" ]]; then
        # macOS
        sed -E '/^1'\''/d' "$archivo_origen" > "$archivo_destino"
        PRINT "OK" "Comments removed from the file."
    else
        # Linux u otros sistemas
        sed '/^1'\''/d' "$archivo_origen" > "$archivo_destino"
        PRINT "OK" "Comments removed from the file."
    fi
}

# banner(){
#    texto="$1"
#    texto=$(echo "$texto" | tr '[:lower:]' '[:upper:]')
#    longitud_texto=${#texto}
#    espacios=$(( (40 - longitud_texto) / 2 ))
#    echo
#    echo "${RED}════════════════════════════════════════"
#    echo "%*s%s%*s\n" $espacios '' "${YELLOW}${BOLD}$texto" $espacios ''
#    echo "${RED}════════════════════════════════════════"
#    echo
# }█

function model_cpc {
case $1 in
    6128)
echo """ 
 Amstrad 128K Microcomputer    (v3)
 ©1985 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.1${NORMAL}"""
        ;;
    664)
echo """ 
 Amstrad 64K Microcomputer    (v2)
 ©1984 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.1${NORMAL}"""
        ;;
    464)
echo """ 
 Amstrad 64K Microcomputer    (v1)
 ©1984 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.0${NORMAL}"""
        ;;
    m46128)
echo """ 
 Amstrad 128K Microcomputer    (v3)
 ©1985 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.1

 M4 Board v2.0.6${NORMAL}"""
;;
    m4664)
echo """ 
 Amstrad 64K Microcomputer    (v2)
 ©1984 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.1

 M4 Board v2.0.6"""
        ;;
    m4464)
echo """ 
 Amstrad 64K Microcomputer    (v1)
 ©1984 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.0

 M4 Board v2.0.6${NORMAL}"""
        ;;
esac
}

function CPCREADY {
   echo
   VERSION=$(cat $PATH_VERSION_FILE)
   echo "${WHITE}Software Developer Kit    (v$VERSION)"
   echo "${WHITE}╔═╗╔═╗╔═╗  ┌──────────┐"
   echo "${WHITE}║  ╠═╝║    │ ${NORMAL}${RED}██ ${GREEN}██ ${BLUE}██${NORMAL} │"
   echo "${WHITE}╚═╝╩  ╚═╝  └──────────┘"

   echo "Ready" >&2
   echo "█" >&2
   echo "${NORMAL}"
}
#→
function PRINT {

   exit_type="$1"
   case "$exit_type" in
      "OK")
         echo "${WHITE}${BOLD}* ${GREEN}${BOLD}$2${NORMAL}"
         ;;
      "ERROR")
         echo "${WHITE}${BOLD}* ${RED}${BOLD}ERROR: $2${NORMAL}"
         exit 1
         ;;
      "ERROR_NO_EXIT")
         echo "${WHITE}${BOLD}* ${RED}${BOLD}ERROR: $2${NORMAL}"
         ;;
      "INFO")
         echo "${WHITE}${BOLD}* ${BLUE}${BOLD}$2${NORMAL}"
         ;;
      "WARNING")
         echo "${WHITE}${BOLD}* ${YELLOW}${BOLD}$2${NORMAL}"
         ;;
      "TAG")
         echo
         echo "${WHITE}${BOLD}[$2]${NORMAL}"
         echo
         ;;
      "TITLE")
         echo
         echo "${BLUE}${BOLD}[${YELLOW}${BOLD}$2${BLUE}${BOLD}] -----------------------${NORMAL}"
         ;;
   esac   
}

# function print_general_tag {
#    echo
#    echo "${BLUE}${BOLD}-- [${YELLOW}${BOLD}$1${BLUE}${BOLD}] -----------------------"
# }

# function print_tag {
#    echo
#    echo "   ${WHITE}${BOLD}[$1]"
#    echo
# }

# Función para verificar si una línea existe en un archivo
# function previus_version {
#     local line="export CPCREADY=\"$PWD\""
#     local file="$1"
#     grep -qF -- "$line" "$file"
# }

# Verificamos el valor de mode
function evaluaMode {
   # Lista de valores
   lista=("1" "2" "0")
   # Bucle para iterar sobre todos los elementos de la lista
   for elemento in "${lista[@]}"; do
      if [[ "$elemento" == "$1" ]]; then
         return
      fi
   done
   echo
   PRINT ERROR "Screen mode $1 not supported"
}

# Verificamos el valor de emulator
function evaluaEmulator {
   # Lista de valores
   lista=("rvm" "RVM" "m4" "M4")
   # Bucle para iterar sobre todos los elementos de la lista
   for elemento in "${lista[@]}"; do
      if [[ "$elemento" == "$1" ]]; then
         return
      fi
   done
   echo
   PRINT ERROR "Emulator Software $1 not supported"
}

# Verificamos el valor de Model
function evaluaCPCModel {
   # Lista de valores
   lista=("464" "664" "6128")
   # Bucle para iterar sobre todos los elementos de la lista
   for elemento in "${lista[@]}"; do
      if [[ "$elemento" == "$1" ]]; then
         return
      fi
   done
   echo
   PRINT ERROR "CPC Model $1 not supported"
}

check_83_files_path() {
    local path=$1

    # Find all files and directories
    find "$path" | while read -r entry; do
        # Get the base name of the entry
        base_name=$(basename "$entry")
        
        if [ -d "$entry" ]; then
            # Check directory name length
            if [ ${#base_name} -gt 8 ]; then
               PRINT ERROR "Directory name does not support more than 8 characters.: $entry"
            fi
        elif [ -f "$entry" ]; then
            # Check file name and extension length
            file_name="${base_name%.*}"
            extension="${base_name##*.}"
            
            if [ ${#file_name} -gt 8 ]; then
               PRINT ERROR "File name does not support more than 8 characters.: $entry"
            fi
            
            if [ "$file_name" != "$base_name" ] && [ ${#extension} -gt 3 ]; then
               PRINT ERROR "File extension name does not support more than 8 characters.: $entry"
            fi
        fi
    done
    
    return 0
}

function template_rvm {

    local DISC="$1"
    local MODEL="$2"
    local COMMAND="$3\n"

    # Definir la cadena de texto con la variable a sustituir
    read -r -d '' rvm << EOF

<html>
  <head>
    <script src='https://cdn.rvmplayer.org/rvmplayer.cpc$MODEL.0.1.0.min.js'></script>
    <style>
      body {
        background-color: rgb(7, 7, 7);
      }
      h1 {
        text-align: center;
        color: white;
      }
      .container {
        background-color: black;
        color: white;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 800px;
        height: 600px;
      }
    </style>
  </head>
  <body>
    <h1>$DISC</h1>
    <div class='container'></div>
    <script>
      const c=document.querySelector('.container')
      rvmPlayer_cpc$MODEL(c,{
        disk: {
          type: 'dsk',
          url: '$DISC',
        },
        command: '$COMMAND',
        warpFrames: 20*50,
        videoMode: 'hd'
      })
    </script>
  </body>
</html>
EOF

    # Escribir el contenido final en un archivo
    echo "%s\n" "$rvm" > rvm.html
}

function template_settings {
    local SYSTEM="$1"
    local SETTINGS_PATH="$2"
    read -r -d '' settings << EOF
{
  "workbench.colorCustomizations": {
    "terminal.foreground": "#d9ff00",
    "terminal.background": "#000080"
},
"terminal.integrated.profiles.$SYSTEM": {
  "amstrad": {
      "path": "console-amstrad",
      "args": [
          "${workspaceFolder}"
      ],
      "icon": "terminal-bash"
  }
},
"terminal.integrated.defaultProfile.$SYSTEM": "amstrad",
"terminal.integrated.fontSize": 13
}

EOF

    echo "$settings" > "$SETTINGS_PATH"
}

function template_bas {
    local BAS_PATH="$1"
    read -r -d '' BAS << EOF
1' AMSTRAD BASIC EXAMPLE CPCREADY
10 CLS
20 PRINT "HELLO WORLD WITH CPCREADY"
30 GOTO 20

EOF

    echo "$BAS" > "$BAS_PATH"
}