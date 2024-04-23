#!/usr/bin/env bash

clear

__size_files() {
  local SIZE=$(du -sh . | awk '{print $1}')
  echo "${SIZE}"
}


__prompt() {
  local EXIT="$?"
  local BLUE="\\[\\e[38;5;21m\\]"
  local WHITE="\\[\\e[38;5;231m\\]"
  local RED="\[\033[00;31m\]"
  local YELLOW="\[\033[00;33m\]"
  local GREEN="\[\033[00;32m\]"
  local RESET="\[\033[00;00m\]"
  local NADA="\[\033[01;00m\]"
  local BOLD="\\[$(tput bold)\\]"
  local BG_WHITE="\\[\\e[48;5;231m\\]"
  local BG_CYAN="\\[\\e[48;5;51m\\]"
  local BG_DARK_BLUE="\\[\\e[48;5;18m\\]"
  local BG_CUSTOM_BLUE="\\[\\e[48;5;62m\\]"
  local expand_bg="\e[K"
local blue_bg="\e[0;104m${expand_bg}"
local red_bg="\e[0;101m${expand_bg}"
local green_bg="\e[0;102m${expand_bg}"

  if [[ -z "${DISC}" ]]; then
    DISC="${RED}${BOLD}EMPTY${RESET}"
  else
    DISC="${GREEN}${BOLD}${DISC}${RESET}"
  fi

  local HOST="${RED}${BOLD}\h${RESET}"
  local USER="\[\033[00;32m\]\u${RESET}"

  local SYMBOL="${RESET}${BOLD}${RED}»${RESET}"
  local DATA_CPC="${green_bg}${WHITE}${BOLD}AMSTRAD CPC: ${GREEN}${BOLD}${MODEL} ${WHITE}${BOLD}SCREEN MODE: ${GREEN}${BOLD}${MODE} ${WHITE}${BOLD}DISC: ${DISC}${RESET}"
  local CPC="${WHITE}${BOLD}AMSTRAD CPC: ${GREEN}${BOLD}${MODEL}${RESET}"
  local SCREEN="${WHITE}${BOLD}SCREEN MODE: ${GREEN}${BOLD}${MODE}${RESET}"

  local PATH="${RED}${BOLD}${BG_WHITE}  ${BG_CUSTOM_BLUE}\w ${RESET}"

  local DISC="${WHITE}${BOLD}DISC: ${DISC}${RESET}"
  local PROMPT="${YELLOW}${BOLD}Ready\n${RESET}"
  local DT="\[\033[02;37m\]$(/bin/date "+%Y-%m-%d %H:%M:%S")${RESET}"
  local USER_PROMP="${HOST}:${PATH}"
  local UP="¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"
  local DOWN="‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗"
  local STATUS=
  [[ ${EXIT} != 0 ]] &&
    STATUS="${RED}${BOLD}\nReady\n█\n${RESET}" ||
    STATUS="${GREEN}${BOLD}\nReady\n█\n${RESET}"

  PS1="${STATUS}\n${PATH}\n \n${DATA_CPCd}\n${PROMPT}"
}

PROMPT_COMMAND=__prompt