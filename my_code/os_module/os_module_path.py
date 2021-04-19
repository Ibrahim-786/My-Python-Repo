import os
#OR
#from os import path


""" os.path is sub module of os """


print(os.path.sep)


print(os.path.basename("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo"))

os.chdir("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo\\my_code")

print(os.listdir())


print(os.path.basename(os.getcwd()))

print(os.path.dirname("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo"))

path1 = "C:\\Users\\ipasha\\Desktop"

path2 = "My_first_Python_Repo"


""" joining path without using python need to provide os path separater \\ """
print(path1+"\\"+path2)


""" joining path using python os.path modules """
print(os.path.join(path1,path2))

""" path split in to two head and tail """
print(os.path.split("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo"))

dup = os.path.split("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo")

print(type(dup))

for du in dup:
    print(du)

print(os.path.getsize("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo"))

print(os.path.exists("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo"))

print(os.path.isfile("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo"))

print(os.path.isfile("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo\\my_code\\filter.py"))

print(os.path.isdir("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo"))
