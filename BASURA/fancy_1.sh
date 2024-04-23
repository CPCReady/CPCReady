#!/usr/bin/env bash

clear
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

  local CPC="${WHITE}${BOLD}AMSTRAD CPC ${MODEL}${RESET}"
  local SCREEN="${GREEN}${BOLD}MODE ${MODE}${RESET}"
  local PATH="${YELLOW}${BOLD}\w${RESET}"
  local DISC="${BLUE}${BOLD}${DISC}${RESET}"
  local PROMPT="${YELLOW}${BOLD}Ready\n${RESET}${YELLOW}"
  local DT="\[\033[02;37m\]$(/bin/date "+%Y-%m-%d %H:%M:%S")${RESET}"

  local STATUS=
  [[ ${EXIT} != 0 ]] &&
    STATUS="${RED}${BOLD}\nx ERROR\n${RESET}" ||
    STATUS="${GREEN}${BOLD}\n✓ OK\n${RESET}"

  PS1="${STATUS}\n${BOLD}${CPC} ${SCREEN} ${DISC} ${PATH}\n${PROMPT}"
}

PROMPT_COMMAND=__prompt