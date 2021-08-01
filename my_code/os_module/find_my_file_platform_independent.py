import os,platform,sys,string

""" platform independent script to find given file is there in the system or not
 if it is there print the path found """

os_type = platform.system()
root_path = None
vaild_drive = list()

if(os_type == "Windows"):
    print("windows os")
    
    for find_drive in string.ascii_uppercase:
        
        
        if(os.path.exists(f"{find_drive}:\\".format())):
            print(f"the valid drive is {find_drive} ".format())
            root_path = find_drive+":\\"
            vaild_drive.append(root_path)
            print(root_path)
            
            
      
else:
    print("linux os")
    root_path = "/"
    
print(vaild_drive) 

    
key_path = None

for root_path in vaild_drive:
    temp_list = list(os.walk(root_path))
    file_name= input("enter file name : ")
    for p,d,f in temp_list:
        for file in f:
            if(file_name == file):
                key_path = os.path.join(p,file)
                break;
        
if (key_path != None):
    print("file found in the system and file path is:")
    print(key_path)
else:
    print("file not found in the system")
    
            

