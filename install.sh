#!/bin/bash
LRED='\033[1;31m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

clear

echo -e "${CYAN}Welcome to the ${LRED}Audio${WHITE}Pi ${CYAN}installer!"
echo -e "${CYAN}This operation overwrites Samba configs, do you want to continue?"

select yn in "Yes" "No"; do
    case $yn in
        Yes ) break;;
        No ) clear; echo -e "${CYAN}Exiting${NC}"; exit;;
    esac
done

clear

echo -e "${CYAN}Installing dependencies...${NC}"
sudo apt -y install python3 python3-pip samba wget &>/dev/null

echo -e "${CYAN}Installing Python modules...${NC}"
sudo pip3 install RPi.GPIO datetime &>/dev/null

echo -e "${CYAN}Configuring Samba...${NC}"
wget https://raw.githubusercontent.com/TheRasPiGuy/AudioPi/master/AudioPi/smb.conf &>/dev/null
sudo cp -f smb.conf /etc/samba/smb.conf &>/dev/null
sudo service smbd restart &>/dev/null

echo -e "${CYAN}In the following prompts, enter a password for Samba${NC}"
sudo smbpasswd -a pi

echo -e "${CYAN}Cleaning up...${NC}"
rm smb.conf &>/dev/null

echo -e "${CYAN}Done!${NC}"
