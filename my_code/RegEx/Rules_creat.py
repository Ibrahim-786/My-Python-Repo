import re

# {times}
# {1,manytimes}
# {1,10} 1 to 10 times
# {3,7} 3 to 7 times
# +
# r"\ba+b\b" a can be found as many times same as {1,manytimes}
# * 0 or many times
# ? 1 time or None time
#===================================================================================

text = "my python is easy to learn as pythonnnnn"

pattern = r"\bpython\b"

print(re.findall(pattern,text))
#===================================================================================
pattern = r"\bpythonnnnn\b"

print(re.findall(pattern,text))

pattern = r"\bpython{5}\b" # n is 5 times

print(re.findall(pattern,text))

#===================================================================================
text = "my python is easy to learn as pythonnnnn aaaaaa dkkdkdkd iooooo ibraaaaaaahim"

pattern = r"\ba{6}\b"

print(re.findall(pattern,text))

#===================================================================================
text = "my python is easy to learn as pythonnnnn aaaaaa dkkdkdkd iooooo ibraaaaaaahim"

pattern = r"\bibra{7}him\b"

print(re.findall(pattern,text))

#====================================================================================


text = "axxxz i am not human axxz  axz being axxxxxxxz"

pattern = r"\baxz\b"  #only axz

print(re.findall(pattern,text))

pattern = r"\bax{1,7}z\b"  #axz x is 1 to 7 times

print(re.findall(pattern,text))

pattern = r"\bax{1,}z\b"  #axz x is 1 to many times up to 

print(re.findall(pattern,text))

pattern = r"\bax{2,}z\b"  #axz x is minimum 2 times to many times up to 

print(re.findall(pattern,text))

pattern = r"\bax{1,}z\b"  #axz x is 1 or many times up to 

print(re.findall(pattern,text))


pattern = r"\bax+z\b"  #axz x is 1 or many times up to  same as above one

print(re.findall(pattern,text))

#=======================================================================
text = "axxxz i am not human axxz  axz being axxxxxxxz"

pattern = r"\bax*z\b"  #0 or many times

print(re.findall(pattern,text))


#====================================================================
text = "axxxz i   am not human axxz  az axz being axxxxxxxz"

pattern = r"\bax?z\b"  #only None or 1 time

print(re.findall(pattern,text))

