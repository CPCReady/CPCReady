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

## Bash Include files
source $(dirname $0)/lib/library.sh

## Chequeamos si existe el archivo de variables.
## si no existe salimos con error
check_env_file

## Cargamos archivo de variables
source .cpc


while :
    do
        #Menu
        clear
        echo
        CPCREADY
        # echo " MENU OPTIONS"
        echo "   1. Create new project disk"
        echo "   2. Check new version"
        echo "   3. Mostrar dato"
        echo "   4. Exit"
        echo ""

        echo -n "${BOLD}Choose option: "
        read opcion

        case $opcion in
        1)  echo;echo "${WHITE}${BOLD}[Create new project disk]${NORMAL}"
            project_name=""
            echo
            # while [[ -z "$project_name" ]]; do
            #     read -p "${GREEN}→${BLUE}${BOLD} Project's name: ${NORMAL}" project_name
            #     project_name=${project_name// /_}
            #         if [[ -e "$project_name" ]]; then
            #             echo "La ruta $ruta existe."
            #         else
            #             mkdir -p "$project_name"
            #         fi
            #     if [[ -z "$project_name" ]]; then
            #         echo
            #         message_build_error "The project name cannot be empty."
            #         echo

            #     fi

            # done
while true; do
    read -p "Project's name: " project_name

    # Reemplazar espacios por guiones bajos
    project_name=${project_name// /_}

    if [[ -z "$project_name" ]]; then
        message_build_error "The project name cannot be empty."
    elif [[ -d "./$project_name" ]]; then
        message_build_error "A directory with the name '$project_name' already exists. Please choose another name."
    else
        break
    fi
done
            echo
            echo "Press enter to continue."
            read foo
        ;;
        2)  echo "Mostrando calendario"
            cal
            read foo
        ;;
        3)  echo "Mostrando datos"
            date
            read foo
        ;;
        4)exit 0;;
        #Alerta
        *)echo "Opcion invalida..."
            sleep 1
        esac
done