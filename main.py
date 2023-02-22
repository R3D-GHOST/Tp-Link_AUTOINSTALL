import os
import time
#varibles
def tplink():
    print("1 --> TP-LINK WN722N V3")
    print("2 --> TP-LINK WN725N V3")
    kali = input(">>>> ")
    if kali == "1":
        os.system('sudo apt install git linux-headers-generic build-essential dkms bc')
        os.system('sudo apt-get update ; sudo apt-get install -y bc linux-headers-$(uname -r)')
        os.system('git clone https://github.com/aircrack-ng/rtl8188eus.git ; cd rtl8188eus')
        os.system('cd rtl8188eus ; cp realtek_blacklist.conf /etc/modprobe.d ; make ; make install')
    elif kali == "2":
        os.system('sudo apt install git linux-headers-generic build-essential dkms bc')
        os.system('git clone https://github.com/aircrack-ng/rtl8188eus.git ; cd rtl8188eus')
        os.system("cd rtl8188eus ; echo 'blacklist r8188eu'|sudo tee -a '/etc/modprobe.d/realtek.conf' ")
        os.system('cd rtl8188eus ; make && sudo make install')
def menu():
    print("1 --> Kali")
    print("2 --> Parrot OS")
    menu = input(">>>> ")
    if menu == "1":
        tplink()
    elif menu == "2":
        tplink()
#banner
banner = """
 _____ ____    _     ___ _   _ _  __     _   _   _ _____ ___  
|_   _|  _ \  | |   |_ _| \ | | |/ /    / \ | | | |_   _/ _ \ 
  | | | |_) | | |    | ||  \| | ' /    / _ \| | | | | || | | |
  | | |  __/  | |___ | || |\  | . \   / ___ \ |_| | | || |_| |
  |_| |_|     |_____|___|_| \_|_|\_\ /_/   \_\___/  |_| \___/ 
                                                              

"""
#menu
print(banner)
print("1 --> INSTALAR TP LINK")
print("2 --> Salir")
opt_menu = input(">>>> ") 
if opt_menu == "1":
    menu()
elif opt_menu == "2":
    exit()
else:
    print("Error Opcion no encontrada")