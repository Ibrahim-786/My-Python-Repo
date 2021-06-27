""" Read a path after reading check weather given path is dir or file  """


import os

path = input("enter your path: ")


if(os.path.exists(path)):
    print("the given path is valid and the path is :")
    if(os.path.isfile(path)):
        print(f"{path} and it is file")
    else:
        print(f"{path} and it is dir")
else:
    print("the given path is not valid")
