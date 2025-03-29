#!/bin/bash

JMENO=$1
TEMA=$2
CAS=$(date)

# Barvy
ZELENA="\033[32m"
MODRA="\033[34m"
RESET="\033[0m"

if [ -z "$JMENO" ] || [ -z "$TEMA" ]; then
  echo -e "\033[31mPoužití: ./pozdrav_barvy.sh [jméno] [téma]${RESET}"
  exit 1
fi

echo -e "${ZELENA}Nazdar ${JMENO}!${RESET}"
echo -e "${MODRA}Tak co, připraven na ${TEMA}?${RESET}"
echo "Dnes je: $CAS"
alias pozdrav="~/DevOps/scripts/pozdrav_barvy.sh Lukáš Bash"
