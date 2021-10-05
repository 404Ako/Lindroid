import os
from colorama import Fore
import time
from pyfiglet import figlet_format

green = Fore.GREEN
blue = Fore.BLUE
white = Fore.WHITE
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
def menu():
		
	print(Fore.RED+"     Welcome To Android Linux Installer")
	time.sleep(1)
	print(Fore.BLUE+(figlet_format("Lindroid", font = "slant")))
	time.sleep(1)
	print("Type help to check all installable systems!")
def main():
	time.sleep(1)
	inp = input(f"""
{green}┌──{green}(\{blue}u0_a173㉿localhost{green}){green}-[{white}~{green}]
└─${white} """)
	if inp == "help":
 		print(Fore.BLUE+"""
| ====================================== |
| 1 - Kali Linux           2 - Arch      |
| 3 - Ubuntu               4 - Debian    |
| 5 - Manjaro              6 - Fedora    |
| 7 - Void                 8 - Alpine    |
|            9 - Parrot OS               |
| ====================================== |""")
 		main()
	elif inp == "1":
		os.system("pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-xfce.sh -O kali-xfce.sh && chmod +x kali-xfce.sh && bash kali-xfce.sh")
	elif inp == "2":
		os.system("pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-lxde.sh -O arch-lxde.sh && chmod +x arch-lxde.sh && bash arch-lxde.sh")
	elif inp == "3":
		os.system("pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-xfce.sh -O ubuntu20-xfce.sh && chmod +x ubuntu20-xfce.sh && bash ubuntu20-xfce.sh")
	elif inp == "4":
		os.system("pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-xfce.sh -O debian-xfce.sh && chmod +x debian-xfce.sh &&  bash debian-xfce.sh")
	elif inp == "5":
		os.system("pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-xfce.sh -O manjaro-xfce.sh && chmod +x manjaro-xfce.sh && bash manjaro-xfce.sh")
	elif inp == "6":
		os.system("pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-xfce.sh -O fedora-xfce.sh && chmod +x fedora-xfce.sh && bash fedora-xfce.sh")
	elif inp == "7":
		os.system("pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-xfce.sh && chmod +x void-xfce.sh && bash void-xfce.sh")
	elif inp == "8":
		os.system("pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpinexfce.sh -O alpinexfce.sh && chmod +x alpinexfce.sh && bash alpinexfce.sh")
	elif inp == "9":
		os.system("pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/risecid/parrot-in-termux/main/parrot.sh -O parrotinstall.sh && chmod +x parrotinstall.sh && bash parrotinstall.sh")
	else:
		print(Fore.RED+"Incorrect command")
		main()
menu()
main()
