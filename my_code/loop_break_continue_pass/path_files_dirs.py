""" Read a dir path and identify all files and directorys """


import os,sys,platform

path = input("please enter your directory ")
print(os.listdir(path))
for d in os.listdir(path):
    print(d)

print("===============================================")
for d in os.listdir(path):
    if(os.path.isdir(d)):
        print(d)
