#!/usr/bin/env bash

clear

__prompt() {
  local EXIT="$?"
  local RED="\e[91m"
  local YELLOW="\e[93m"
  local GREEN="\e[92m"
  local RESET="\[\033[00;00m\]"
  local BG_DARK_BLUE="\\[\\e[48;5;18m\\]"
  local expand_bg="\e[K"
  local blue_bg="\e[0;104m"

  if [[ -z "${DISC}" ]]; then
    DISC="${RED}${BOLD}EMPTY"
  else
    DISC="${DISC}"
  fi

  [ -f .cpc ] && source .cpc

  local BLACK_LINE="${BG_DARK_BLUE}${expand_bg}${RESET}"
  local DATA_CPC="${BG_DARK_BLUE}${YELLOW} AMSTRAD » MODEL: ${MODEL} » SCREEN MODE: ${MODE} » DISC: ${DISC} » PROJECT: \w ${expand_bg}${RESET}"
  local PROMPT="${YELLOW}${BOLD}Ready\n${RESET}"
  local STATUS=
  [[ ${EXIT} != 0 ]] &&
    STATUS="${RED}${BOLD}\nReady\n█\n${RESET}" ||
    STATUS="${YELLOW}\nReady\n█\n${RESET}"
  PS1="${STATUS}\n \n${BLACK_LINE}\n${DATA_CPC}\n${BLACK_LINE}\n\n${PROMPT}${YELLOW}"
}

PROMPT_COMMAND=__prompt