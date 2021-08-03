#patter is sequence of characters, which represent multiple strings

import re

text = "This333@ is. py4thon, python.3 python4 python2 an5d it is __ easy to @@__learn 0 123&&"

my_text = "is"

print(re.findall(my_text,text))

print(re.findall("is","is not is ok is to be is"))

print(re.findall(my_text,"isis ok all ok"))

my_pattern = "i[st]"


print(re.findall(my_pattern,text))


print(re.findall("[a-b]",text))
print(re.findall("[a-z]",text))
print(re.findall("[A-Z]",text))
print(re.findall("[0-9]",text))
print(re.findall("1[0-9]",text))
print(re.findall("[a-zA-Z0-9]",text))


print(re.findall("\w",text))

print(re.findall("\w\w",text))

print(re.findall("\w\w\w",text))

print(re.findall("\w\w\w\w",text))

print(re.findall("\W",text))

print(re.findall("\d",text))

print(re.findall("python\d",text))

print(re.findall("\d\d",text))

print(re.findall(".",text))  # get all character except \n new line
print(re.findall("..",text))
print(re.findall("...",text))

print(re.findall("\.",text)) #for dot only \ help to find only dot

