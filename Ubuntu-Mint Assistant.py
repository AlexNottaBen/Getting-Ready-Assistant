
#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

def Wait():
    input("Press any key to continue... ")

def SimpleInstall(RootPassword,ProgrammeName):
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt install " + ProgrammeName + " --yes"))

def DoThis(RootPassword,Command):
    os.system('echo %s|sudo -S %s' % (RootPassword,Command))

def WhatItIs(About):
    print("==================== " + About + " ====================")

def UpdatePackege(RootPassword):
    print("==================== Update ====================")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt update"))

def UpgradePackege(RootPassword):
    print("==================== Upgrade ====================")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt upgrade --yes"))

def SimpleUnInstall(RootPassword,ProgrammeName):
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt purge " + ProgrammeName + " --yes"))
    
def Logo():
    print("######################################")
    print("#     Ubuntu/Linux Mint Assistant    #")
    print("######################################")
    print("By AlexNottaBen")

def ClearScreen():
    os.system("clear")
    
#Begin

ClearScreen()
Logo()
RootPassword = input("Input Root Password > ")
ClearScreen()
Logo()

WhatItIs("1. Сheck Update,Upgrade...")
UpdatePackege(RootPassword)
UpgradePackege(RootPassword)
DoThis(RootPassword,"sudo apt update -y && sudo apt upgrade -y && sudo apt dist-upgrade -y &&  sudo apt-get autoremove -y; sudo apt-get autoclean -y")

WhatItIs("2. Сheck SUDO,WGET...")
SimpleInstall(RootPassword,"sudo")
SimpleInstall(RootPassword,"wget")
SimpleInstall(RootPassword,"gdebi")
SimpleInstall(RootPassword,"git")

WhatItIs("3. Deleting Superfluous Packages")
SimpleUnInstall(RootPassword,"update-notifier")
DoThis(RootPassword,"sudo apt purge popularity-contest whoopsie --yes && sudo apt-mark hold popularity-contest whoopsie")


WhatItIs("4. Fix the time error")
DoThis(RootPassword,"timedatectl set-local-rtc 1 --adjust-system-clock")
os.system("timedatectl set-local-rtc 1 --adjust-system-clock")

Answer = input("\nSwitch FireFox -> FireFox ESR? Type 'yes' if you want to do it! > ")
if Answer == "yes" or Answer == "Yes":
    WhatItIs("Switching FireFox -> FireFox ESR")
    SimpleUnInstall(RootPassword,"firefox")
    DoThis(RootPassword,"sudo add-apt-repository ppa:mozillateam/ppa") #TO DO
    UpdatePackege(RootPassword)
    SimpleInstall(RootPassword,"firefox-esr")
    DoThis(RootPassword,"sudo snap remove firefox")
    DoThis(RootPassword,"sudo apt-get autoremove -y; sudo apt-get autoclean -y")

Answer = input("\nDelete All FireFox Browsers? Type 'yes' if you want to do it! > ")
if Answer == "yes" or Answer == "Yes":
    WhatItIs("Delete All FireFox Browsers")
    SimpleUnInstall(RootPassword,"firefox")
    SimpleUnInstall(RootPassword,"firefox-esr")
    DoThis(RootPassword,"sudo snap remove firefox")
    DoThis(RootPassword,"sudo apt-get autoremove -y; sudo apt-get autoclean -y")

Answer = input("\nDelete snap? Type 'yes' if you want to do it! > ")
if Answer == "yes" or Answer == "Yes":
	WhatItIs("5. Delete snap")
	DoThis(RootPassword,"sudo snap remove firefox")
	DoThis(RootPassword,"sudo snap remove snap-store")
	DoThis(RootPassword,"sudo snap remove gtk-common-themes")
	DoThis(RootPassword,"sudo snap remove snapd")
	DoThis(RootPassword,"sudo umount /var/snap")
	DoThis(RootPassword,"sudo apt purge snapd -y")
	DoThis(RootPassword,"sudo rm -rf ~/snap")
	DoThis(RootPassword,"sudo rm -rf /snap")
	DoThis(RootPassword,"sudo rm -rf /var/snap")
	DoThis(RootPassword,"sudo rm -rf /var/lib/snapd")
	SimpleUnInstall(RootPassword,"gnome-software")
	DoThis(RootPassword,"sudo apt-get autoremove -y; sudo apt-get autoclean -y")

WhatItIs("6. Install Grub Customizer")
SimpleInstall(RootPassword,"grub-customizer")
DoThis(RootPassword,"grub-customizer")

Wait()
