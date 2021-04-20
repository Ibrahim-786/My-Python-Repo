""" python script 2 for to find file path if exit """
import os,platform, sys

root_path = "C:\\Users\\ipasha\\Desktop"

temp_list = list(os.walk(root_path))
file_name= input("enter file name : ")
count =0
for p,d,f in temp_list:
    for file in f:
        if(file_name == file):
            count = 1
            print(os.path.join(root_path,file))
            break
    if (count == 1):
        exit()
print("file not found")

        
