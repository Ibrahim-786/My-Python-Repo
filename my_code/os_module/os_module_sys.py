""" this file is all about sys commonds like instead of using python os.getcwd or
    os.listdir() we can use directly os dependent commonds like
    ls pwd in linux
    dir cwd in windows   """


import os


x= os.system("dir")

y= os.system("cls")

x= os.system("dir")

if (not (x or y)):
    print("givin commonds found in os")
else:
    print("givin commonds not found")
