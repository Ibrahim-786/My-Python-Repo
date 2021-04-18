"""" os module programs """

""" very import to automate your task for server side
    using os module we can work or intract with os """

""" to make it clear dividing in to 4 part
    os
    os.path
    os.system
    os.walk """



import os


""" to which slash / for linux \ for windows """
print(os.sep)


#path = "C:\Users\ipasha\Desktop\My_first_Python_Repo\my_code\sys_module_2.py"    error \U is special character
path = "C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo\\my_code\\sys_module_2.py"
print(path)


""" get current working directry for both windows linux  """
print(os.getcwd())


""" change  working directry for both windows linux  """
os.chdir("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo")  #it will work fine


""" get current working directry for both windows linux  """
print(os.getcwd())
    
""" list working directry for bith windows and linux os """
#print(os.listdir())
list_dir_ls = os.listdir()
print("\n\n\n\n")
print("before creating any directory ")
print("\n")
for ls in list_dir_ls:
    print(ls)


""" create some directory and files through python script and delete them all at the end  """

os.mkdir("pasha_2")

""" create directories     mkdirs
    """
os.makedirs("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo/d1/d2/d3")


""" list working directry for bith windows and linux os """
#print(os.listdir())
list_dir_ls = os.listdir()
print("\n\n\n\n")
print("after creating  directory  and before  deleting ")
print("\n")
for ls in list_dir_ls:
    print(ls)

    
""" remove dir  and file that are created  """
os.chdir("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo\\d1\\d2")

os.rmdir("d3")

os.chdir("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo\\d1")
os.rmdir("d2")
os.chdir("C:\\Users\\ipasha\\Desktop\\My_first_Python_Repo")

os.rmdir("d1")

os.rmdir("pasha_2")



""" list working directry for bith windows and linux os """
#print(os.listdir())
list_dir_ls = os.listdir()
print("\n\n\n\n")
print("after deleting  directory ")
print("\n")
for ls in list_dir_ls:
    print(ls)


""" similar way we have os.remove(path) os.removedirs(path (remove recursivley))  """

print("\n the environment variables are \n:")
print(os.environ)
print(os.getpid())


