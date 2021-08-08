#split subtitute

import re

my_string = "This is about python and also have python2 version and Python3 also"

pattern =  r"python[23]?"

print(re.split(pattern,my_string, flags= re.I))
print(re.split(pattern,my_string,maxsplit = 0, flags= re.I))
print(re.split(pattern,my_string,maxsplit = 1, flags= re.I))
print(re.split(pattern,my_string,maxsplit = 2, flags= re.I))

print(re.split(pattern,my_string,maxsplit = 3, flags= re.I))


#sub(pattern, repl, string, count=0, flags=0)
print(help(re.sub))

print(re.sub(pattern,"cpython",my_string))
print(re.sub(pattern,"cpython",my_string,flags = re.I))

print(re.sub(pattern,"cpython",my_string,count = 0,flags = re.I))
print(re.sub(pattern,"cpython",my_string,count = 1,flags = re.I))
print(re.sub(pattern,"cpython",my_string,count = 2,flags = re.I))
print(re.sub(pattern,"cpython",my_string,count = 3,flags = re.I))


#subn(pattern, repl, string, count=0, flags=0)
#    Return a 2-tuple containing (new_string, number).

print("\n\n\n \n\n")

print("subn")

print(help(re.sub))
print("it will return dictionary")

print(re.subn(pattern,"cpython",my_string))
print(re.subn(pattern,"cpython",my_string,flags = re.I))

print(re.subn(pattern,"cpython",my_string,count = 0,flags = re.I))
print(re.subn(pattern,"cpython",my_string,count = 1,flags = re.I))
print(re.subn(pattern,"cpython",my_string,count = 2,flags = re.I))
print(re.subn(pattern,"cpython",my_string,count = 3,flags = re.I))
