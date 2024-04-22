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

## Colors for ANSI terminal

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
IN_BAS="src"
OUT="out/M4Board"

show_version(){
   CPCREADY
   VERSION=$(cat $CPCREADY/VERSION)
   echo "${BOLD}v$VERSION${NORMAL}"
}

## Funcion que pinta Ready de amstrad
ready() {
   echo
   echo "${YELLOW}Ready" >&2
   echo "${YELLOW}█" >&2
   echo
}

## Función para verificar si existe el archivo
## .cpc en el directorio actual
check_env_file() {
   if [ ! -f .cpc ]; then
      echo
      PRINT "ERROR" "El archivo .cpc no existe en este directorio."
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

## cambios en el archivo .cpc valor MODE
## $1 : value mode
change_mode(){
   sed -i.bak "s/^MODE=.*$/MODE=$1/" "$2/.cpc"
   rm "$2/.cpc.bak"
}

## cambios en el archivo .cpc valor DISC
## $1 : value disc
change_disc(){
   sed -i.bak "s/^DISC=.*$/DISC=$1/" "$2/.cpc"
   rm "$2/.cpc.bak"
}

## cambios en el archivo .cpc valor MODEL
## $1 : value disc
change_model(){
   sed -i.bak "s/^MODEL=.*$/MODEL=$1/" "$2/.cpc"
   rm "$2/.cpc.bak"
}

create_dsk() {
    local DSK_IMAGE="$1"
    TAG=$(basename "$1")
    PRINT "TAG" "$TAG"
    if iDSK "$DSK_IMAGE" -n > /dev/null 2>&1; then
        PRINT "OK" "Disk image created successfully."
    else
        PRINT "ERROR" "There was an error creating the disk image."
    fi
}

add_ascii_dsk(){
   local DSK_IMAGE="$1"
   local ASCII_FILE="$2"
   if iDSK "$DSK_IMAGE" -i "$ASCII_FILE" -t 0 > /dev/null 2>&1; then
      PRINT "OK" "File added to the disk image."
   else
      PRINT "ERROR" "There was an error adding the file to the disk image."
   fi
}

rm_comments() {
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
#    printf "%*s%s%*s\n" $espacios '' "${YELLOW}${BOLD}$texto" $espacios ''
#    echo "${RED}════════════════════════════════════════"
#    echo
# }

model_cpc(){
case $1 in
    6128)
echo """ 
Amstrad 128K Microcomputer    (v3)
©1985 Amstrad Consumer Electronics plc
        and Locomotive Software Ltd.

BASIC 1.1

Ready
█${NORMAL}"""
        ;;
    664)
echo """ 
Amstrad 64K Microcomputer    (v2)
©1984 Amstrad Consumer Electronics plc
        and Locomotive Software Ltd.

BASIC 1.1

Ready
█${NORMAL}"""
        ;;
    464)
echo """ 
Amstrad 64K Microcomputer    (v1)
©1984 Amstrad Consumer Electronics plc
        and Locomotive Software Ltd.

BASIC 1.0

Ready
█${NORMAL}"""
        ;;
esac
}

CPCREADY(){
   echo
   # echo " ██████╗██████╗  ██████╗██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗"
   # echo "██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝"
   # echo "██║     ██████╔╝██║     ██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝" 
   # echo "██║     ██╔═══╝ ██║     ██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝ " 
   # echo "╚██████╗██║     ╚██████╗██║  ██║███████╗██║  ██║██████╔╝   ██║  "
   # echo " ╚═════╝╚═╝      ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝  "
   # echo "${RED}════════════════════════════════════════"
   echo "${YELLOW}░█▀▀░█▀█░█▀▀░█▀▄░█▀▀░█▀█░█▀▄░█░█░"
   echo "${YELLOW}░█░░░█▀▀░█░░░█▀▄░█▀▀░█▀█░█░█░░█░░"
   echo "${YELLOW}░▀▀▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀░░░▀░░"
   echo
   # echo "${RED}════════════════════════════════════════"
   # echo "${GREEN}════════════════════════════════════════"
   # echo "${YELLOW}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
   # echo "${YELLOW}░░░░░█▀▀░█▀█░█▀▀░█▀▄░█▀▀░█▀█░█▀▄░█░█░░░░"
   # echo "${YELLOW}░░░░░█░░░█▀▀░█░░░█▀▄░█▀▀░█▀█░█░█░░█░░░░░"
   # echo "${YELLOW}░░░░░▀▀▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀░░░▀░░░░░"
   # echo "${YELLOW}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
   # echo "${GREEN}════════════════════════════════════════"
   # echo ${NORMAL}
}

PRINT(){

   exit_type="$1"
   case "$exit_type" in
      "OK")
         echo "${WHITE}${BOLD}  → ${GREEN}${BOLD}$2${NORMAL}"
         ;;
      "ERROR")
         echo "${WHITE}${BOLD}  → ${RED}${BOLD}$2${NORMAL}"
         exit 1
         ;;
      "ERROR_NO_EXIT")
         echo "${WHITE}${BOLD}  → ${RED}${BOLD}$2${NORMAL}"
         ;;
      "INFO")
         echo "${WHITE}${BOLD}  → ${BLUE}${BOLD}$2${NORMAL}"
         ;;
      "WARNING")
         echo "${WHITE}${BOLD}  → ${YELLOW}${BOLD}$2${NORMAL}"
         ;;
      "TAG")
         echo
         echo " ${WHITE}${BOLD}[$2]"
         echo
         ;;
      "TITLE")
         echo
         echo "${BLUE}${BOLD} [${YELLOW}${BOLD}$2${BLUE}${BOLD}] -----------------------"
         ;;
   esac   
}

print_general_tag(){
   echo
   echo "${BLUE}${BOLD}-- [${YELLOW}${BOLD}$1${BLUE}${BOLD}] -----------------------"
}

print_tag(){
   echo
   echo "   ${WHITE}${BOLD}[$1]"
   echo
}