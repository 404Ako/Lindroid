License = """
MIT License

Copyright (c) 2021 404Ako

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os
os.system("pip install colorama")
from colorama import Fore
import time
os.system("title Lindroid | | Linux In Android")
green = Fore.GREEN
blue = Fore.BLUE
white = Fore.WHITE
if os.name == "nt":
        os.system("cls")
else:
        os.system("clear")
def menu():
        print(Fore.BLUE+"""
                          W E L C O M E
                 ╦    ╦  ╔╗╔  ╔╦╗  ╦═╗  ╔═╗  ╦  ╔╦╗
                 ║    ║  ║║║   ║║  ╠╦╝  ║ ║  ║   ║║
                 ╩═╝  ╩  ╝╚╝  ═╩╝  ╩╚═  ╚═╝  ╩  ═╩╝
              ————————————————————————————————————————
                 Type "help" To Check All Commands!
""")
def main():
        inp = input(f"""
{green}┌──{green}({blue}u0_a173㉿localhost{green}){green}-[{white}~{green}]
└─${white} """)
        if inp == "help":
                print(Fore.BLUE+"""
        ╔════════════════════════════════════════════╗
        ║                 LinDroid                   ║
        ║════════════════════════════════════════════║
        ║ help - Shows this command                  ║
        ║                                            ║
        ║ clear - Clears the screen                  ║
        ║                                            ║
        ║ distros - Shows all installable systems    ║
        ║                                            ║
        ║ credit - Sends the credit screen           ║
        ║                                            ║
        ║ support - Sends the Discord Server link    ║
        ║                                            ║
        ║ exit - Exits out of the script             ║
        ╚════════════════════════════════════════════╝""")
                main()
        elif inp == "exit":
                print(Fore.YELLOW+"thanks for using lindroid :)")
                exit()
        elif inp == "support":
                print("https://discord.gg/9tX23eYb")
                main()
        elif inp == "clear":
                if os.name == "nt":
                        os.system("cls")
                        main()
                else:
                        os.system("clear")
                        main()
        elif inp == "credit":
                print(Fore.BLUE+"""
        ╔════════════════════════════════════════════╗
        ║                 Credits                    ║
        ║════════════════════════════════════════════║
        ║                Lindroid                    ║
        ║              —————————————                 ║
        ║ This script has been made by Ahmad Aka     ║
        ║ 404Ako                                     ║
        ║                                            ║
        ║ Instagram: ahmadthebean                    ║
        ║ GitHub: 404Ako                             ║
        ║ YouTube: Black Magic                       ║
        ║ Discord: 404Ako#8272                       ║
        ╚════════════════════════════════════════════╝""")
                main()
        elif inp == "distros":
                print(Fore.BLUE+"""
        ╔══════════════════════════════════════════════════════╗
        ║                    Distributions                     ║
        ║══════════════════════════════════════════════════════║
        ║ 1 - Kali Linux                     2 - Arch Linux    ║
        ║                                                      ║
        ║ 3 - Ubuntu                         4 - Debian        ║
        ║                                                      ║
        ║ 5 - Manjaro                        6 - Fedora        ║
        ║                                                      ║
        ║ 7 - Void                           8 - Alpine        ║
        ║                                                      ║
        ║                  9 - Parrot OS                       ║
        ╚══════════════════════════════════════════════════════╝""")
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
