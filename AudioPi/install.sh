#!/bin/bash
LRED='\033[1;31m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

clear

echo -e "${CYAN}Welcome to the ${LRED}Audio${WHITE}Pi ${CYAN}installer!"
echo -e "${CYAN}Do you want to continue?"

select yn in "Yes" "No"; do
    case $yn in
        Yes ) break;;
        No ) clear; echo -e "${CYAN}Exiting${NC}"; exit;;
    esac
done

clear

# echo -e "${CYAN}Installation continues here${NC}"

