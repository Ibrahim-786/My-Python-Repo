import shutil

#'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'



print(help(shutil))

print(dir(shutil))

source = "C:\\Users\\ipasha\\Desktop\\ibrahim\\Mission_Nvidia\\new.txt"


destination = "C:\\Users\\ipasha\\Desktop\\ibrahim\\new\\new.txt"

shutil.copy(source,destination)

source = "C:\\Users\\ipasha\\Desktop\\ibrahim\\Mission_Nvidia\\new.txt"


destination = "C:\\Users\\ipasha\\Desktop\\ibrahim\\Mission_Nvidia\\new.txt_backup"

shutil.copy(source,destination)

shutil.copyfile(source,destination)

shutil.copy2(source,destination)

shutil.copymode(source,destination)

shutil.copystat(source,destination)

