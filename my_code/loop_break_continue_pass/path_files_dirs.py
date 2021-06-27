""" Read a dir path and identify all files and directorys """


import os,sys,platform

path = input("please enter your directory ")




for d in os.listdir(path):
    if(os.path.isfile(d)):
        print(d)
