import re


text = "this python and Python is fun PythoN is not available"


pattern = r"\bpython\b"

print(re.findall(pattern,text))

print(re.findall(pattern,text,re.I)) # ignore case sensitivity

print(re.findall(pattern,text,re.IGNORECASE)) # same as previous

#========================================

# multiline string operation


text = """This is ibrahim this
This is line one this
This is this line two
This is line this 3
this is line  this 4"""

pattern = r"^This"
print(re.findall(pattern,text))
print(re.findall(pattern,text,re.M))


print(re.findall(pattern,text,re.M|re.I))
#===============================================

text = """This is ibrahim end
This is line one this End
This is this line two end
This is line this 3 end
this is line  this 4 end"""

pattern = r"end$"
print(re.findall(pattern,text))
print(re.findall(pattern,text,re.M))
print(re.findall(pattern,text,re.M|re.I))
#=============================================


