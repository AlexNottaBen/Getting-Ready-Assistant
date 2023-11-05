#! /usr/bin/python3
# -*- coding: utf-8 -*-

from distro import id as os_id
from os import system as execute
from getpass import getpass as input_password

# from distro import linux_distribution as get_os_infomation


def wait():
    input("Press any key to continue... ")


def apt_install(root_password, package_name):
    execute(
        "echo %s|sudo -S %s"
        % (root_password, "sudo apt install " + package_name + " --yes")
    )


def execute_as_root(root_password, Command):
    execute("echo %s|sudo -S %s" % (root_password, Command))


def what_it_is(About):
    print("==================== " + About + " ====================")


def update_packages(root_password):
    print("==================== Update ====================")
    execute("echo %s|sudo -S %s" % (root_password, "sudo apt update"))


def upgrade_packages(root_password):
    print("==================== Upgrade ====================")
    execute("echo %s|sudo -S %s" % (root_password, "sudo apt upgrade --yes"))


def apt_purge(root_password, package_name):
    execute(
        "echo %s|sudo -S %s"
        % (root_password, "sudo apt purge " + package_name + " --yes")
    )


def logo():
    print("######################################")
    print("#       Getting Ready Assistant      #")
    print("######################################")
    print("By AlexNottaBen")


def clear():
    execute("clear")


# begin

clear()
logo()
root_password = input_password("Input Root Password > ")
clear()
logo()

what_it_is("Сheck Update,Upgrade...")
update_packages(root_password)
upgrade_packages(root_password)
execute_as_root(
    root_password,
    "sudo apt update -y && sudo apt upgrade -y && sudo apt dist-upgrade -y &&  sudo apt-get autoremove -y; sudo apt-get autoclean -y",
)

what_it_is("Сheck SUDO,WGET...")
apt_install(root_password, "sudo")
apt_install(root_password, "wget")
apt_install(root_password, "gdebi")
apt_install(root_password, "git")
apt_install(root_password, "menulibre")

distro = os_id()
if distro == "debian":
    what_it_is("Deleting Superfluous Packages")
    execute_as_root(
        root_password,
        "sudo apt purge gnome-2048 gnome-chess gnome-klotski gnome-sudoku gnome-mahjongg gnome-robots gnome-mines gnome-nibbles gnome-taquin gnome-tetravex five-or-more four-in-a-row lightsoff quadrapassel swell-foop tali aisleriot hitori iagno -y;sudo apt purge yelp transmission-gtk totem evolution gnome-weather gnome-sound-recorder gnome-music gnome-contacts seahorse rhythmbox xterm mlterm-common kasumi mlterm-common -y;sudo apt-get purge xiterm+thai ibus uim mozc-utils-gui -y;sudo apt autoremove -y;sudo apt autoclean -y;sudo apt clean -y;",
    )

    what_it_is("Patch Connection Android-Devices...")
    apt_install(root_password, "mtp-tools")
    apt_install(root_password, "gvfs-backends")
    apt_install(root_password, "libmtp-common")
    apt_install(root_password, "libmtp-runtime")
    apt_install(root_password, "libmtp9")

    what_it_is("Check apt-add-repository...")
    apt_install(root_password, "software-properties-common")
    apt_install(root_password, "dirmngr")
    apt_install(root_password, "apt-transport-https")
    apt_install(root_password, "lsb-release ca-certificates")

    # print('GTK_MODULES="appmenu-gtk-module"')
    # execute_as_root(root_password,"sudo mousepad /etc/environment")

else:
    what_it_is("Deleting Superfluous Packages")
    apt_purge(root_password, "update-notifier")
    execute_as_root(
        root_password,
        "sudo apt purge popularity-contest --yes && sudo apt-mark hold popularity-contest",
    )
    apt_purge(root_password, "popularity-contest")

    what_it_is("Fix the time error")
    execute_as_root(root_password, "timedatectl set-local-rtc 1 --adjust-system-clock")
    execute("timedatectl set-local-rtc 1 --adjust-system-clock")

    answer = input(
        "\nSwitch FireFox -> FireFox ESR? Type 'yes' if you want to do it! > "
    )
    if answer == "yes" or answer == "Yes":
        what_it_is("Switching FireFox -> FireFox ESR")
        apt_purge(root_password, "firefox")
        execute_as_root(
            root_password, "sudo add-apt-repository ppa:mozillateam/ppa"
        )  # TO DO
        update_packages(root_password)
        apt_install(root_password, "firefox-esr")
        execute_as_root(root_password, "sudo snap remove firefox")
        execute_as_root(
            root_password, "sudo apt-get autoremove -y; sudo apt-get autoclean -y"
        )

    answer = input("\nDelete All FireFox Browsers? Type 'yes' if you want to do it! > ")
    if answer == "yes" or answer == "Yes":
        what_it_is("Delete All FireFox Browsers")
        apt_purge(root_password, "firefox")
        apt_purge(root_password, "firefox-esr")
        execute_as_root(root_password, "sudo snap remove firefox")
        execute_as_root(
            root_password, "sudo apt-get autoremove -y; sudo apt-get autoclean -y"
        )

    answer = input("\nDelete snap? Type 'yes' if you want to do it! > ")
    if answer == "yes" or answer == "Yes":
        what_it_is("Delete snap")
        execute_as_root(root_password, "sudo snap remove firefox")
        execute_as_root(root_password, "sudo snap remove snap-store")
        execute_as_root(root_password, "sudo snap remove gtk-common-themes")
        execute_as_root(root_password, "sudo snap remove snapd")
        execute_as_root(root_password, "sudo umount /var/snap")
        apt_purge(root_password, "snapd")
        execute_as_root(root_password, "sudo rm -rf ~/snap")
        execute_as_root(root_password, "sudo rm -rf /snap")
        execute_as_root(root_password, "sudo rm -rf /var/snap")
        execute_as_root(root_password, "sudo rm -rf /var/lib/snapd")
        apt_purge(root_password, "gnome-software")
        execute_as_root(
            root_password, "sudo apt-get autoremove -y; sudo apt-get autoclean -y"
        )

what_it_is("Install Grub Customizer")
apt_install(root_password, "grub-customizer")
execute_as_root(root_password, "grub-customizer")

wait()
