"""script to find a file path in system """
""" should be platform independent """
""" if file is not present print file not present """

""" use sys platform and os.path os.system os.walk() os.path.join() """


import os,sys,platform

path = "C:\\Users\\ipasha\\Desktop\\my_walk"


path_that_has_to_found = None

file_name= input("----please enter your file name -------")

print(file_name)
print(f"i am searching your file name in this path {path}".format())

temp_list = list(os.walk(path))
file_name_found = None
for lit in temp_list:
    p,d,f =  lit
    print(p)
    for dirt in d:
        print(dirt)
    for file in f:
        if (file_name == file ):
            file_name_found =file
            path_that_has_to_found = p
        
            
if(path_that_has_to_found != None):
    print("file found in the system")
else:
    print("file not found in the system ")



print("-----------the file path is --------")
print(os.path.join(path,file_name_found))





