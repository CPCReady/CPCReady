
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
source bin/lib/library.sh

## show version
show_version

while true; do
    echo
    read -p "Are you sure you want to install CPCReady on your system? (y/n): " respuesta
    echo
    case $respuesta in
        [Yy]* ) break;;
        [Nn]* ) echo "Bye....";exit;;
        * ) echo "Please respond with 'y' or 'n'.";;
    esac
done

VERSION=$(cat VERSION)

PRINT TITLE "Install CPCReady $VERSION in your system"

PRINT TAG "Dependencies"

## Chequeamos versiones previas instaladas
if [[ -f "$HOME/.bashrc" ]]; then
    if previus_version "$HOME/.bashrc"; then
        PRINT ERROR "There is a previous version of CPCReady installed on the system. ($HOME/.bashrc) "
    else
        PRINT OK "There is no previous version installed ($HOME/.bashrc)"
    fi
fi

if [[ -f "$HOME/.zshrc" ]]; then
    if previus_version "$HOME/.zshrc"; then
        PRINT ERROR "There is a previous version of CPCReady installed on the system. ($HOME/.zshrc)"
    else
        PRINT OK "There is no previous version installed ($HOME/.zshrc)"
    fi
fi

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    BIN_PATH="$PWD/bin:$PWD/bin/tools"
    PRINT OK "$OSTYPE Supported operating system."
elif [[ "$OSTYPE" == "darwin"* ]]; then
    BIN_PATH="$PWD/bin:$PWD/bin/tools"
    PRINT OK "$OSTYPE Supported operating system."
else
    PRINT ERROR "$OSTYPE Operating system NOT supported."
fi

if which unix2dos >/dev/null; then
    PRINT OK "unix2dos installed on your system"
else
    PRINT ERROR_NO_EXIT "unix2dos is not installed on your system."
    PRINT WARNING "Please install unix2dos on your system to continue."
fi

# Si la version de python es correcta instalamos la consola
# Obtener la versión de Python instalada
python_version=$(python3 -V 2>&1)

# Extraer la versión principal y secundaria
version_major=$(echo "$python_version" | cut -d ' ' -f 2 | cut -d '.' -f 1)
version_minor=$(echo "$python_version" | cut -d ' ' -f 2 | cut -d '.' -f 2)

# Verificar si la versión es 3.10 o superior
if [ "$version_major" -eq 3 ] && [ "$version_minor" -ge 10 ]; then
    if [[ "$OSTYPE" == "linux-gnu" ]]; then
        pip3 install bin/lib/console-$VERSION-py3-none-any.whl --force-reinstall
        PRINT OK "Install console amstrad for Visual Studio Code."
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        pip3 install bin/lib/console-$VERSION-py3-none-any.whl --break-system-packages --force-reinstall
        PRINT OK "Install console amstrad for Visual Studio Code."
    else
        PRINT ERROR "$OSTYPE Operating system NOT supported."
    fi
else
    PRINT WARNING "Python 3.10 or higher is not installed. No install console amstrad for Visual Studio Code."
fi

PRINT TAG "Installation"

echo -e "\nexport CPCREADY=$PWD" >> "$HOME/.bashrc"
echo -e "export PATH=\$PATH:$BIN_PATH" >> "$HOME/.bashrc"
PRINT OK "Install in Bash Shell."
echo -e "\nexport CPCREADY=$PWD" >> "$HOME/.zshrc"
echo -e "export PATH=\$PATH:$BIN_PATH" >> "$HOME/.zshrc"
PRINT OK "Install in Zsh Shell."

PRINT TITLE "Successful installation of CPCReady on your system."