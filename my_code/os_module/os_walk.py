"""working with os.walk module  """
""" os.walk is generater object it will generate a list of
 tuple followed by list
 
 eg [("path given ",[list of directory in given path ],[list of files]),
      ("path",[dir],[file]),
      ("path",[dir],[file]), (nth tuple) ]  """

""" vvv important script """ 


import os

path_1 = "C:\\Users\\ipasha\\Desktop\\ibrahim\\Resume_data"

lists_tuple_list = list (os.walk(path_1,topdown = True))

""" by default topdown = True  """

#print(lists_tuple_list)
print("-------topdown ---------------------------------------------")

for path_2,directory,files in lists_tuple_list:
    print(path_2)
    for d in directory:
        print(d)
    for file in files:
        print(file)
    print("-------------------one level printing done ---------------")




lists_tuple_list = list (os.walk(path_1,topdown = False))

"""  topdown = False  """
print("-------bottomdown ----------------------------------------\n\n")


#print(lists_tuple_list)

for path_2,directory,files in lists_tuple_list:
    print(path_2)
    for d in directory:
        print(d)
    for file in files:
        print(file)
    print("-------------------one level printing done ---------------")


print("-------topdown comp dir and file path using string ---------------------------------------------")

for path_2,directory,files in lists_tuple_list:
    print(path_2)
    for d in directory:
        print(path_2+"\\"+d)
    for file in files:
        print(path_2+"\\"+file)
    print("-------------------one level printing done ---------------")
        
           
print("-------topdown comp dir and file path using python os.path module ---------------------------------------------")

for path_2,directory,files in lists_tuple_list:
    print(path_2)
    for d in directory:
        print(os.path.join(path_2,d))
    for file in files:
        print(os.path.join(path_2,file))
    print("-------------------one level printing done ---------------")
        
           
    


    


