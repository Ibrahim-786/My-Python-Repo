""" script to clear terminal or cmd single code will work ion both
    linux based and windows based os """

import os, platform


if (platform.system() == "Windows"):
    os.system("cls")
    print("Windows")
elif(platform.system() == "Linux"):
    os.system("clear")
    print("Linux")
else:
    print("the os is other then linux and windows")
