import re

my_string = "This is python we also have python2 version and Python3 version"

pattern = r"\bpython[23]?\b"

print(re.search(pattern,my_string))

my_obj = re.search(pattern,my_string)

print(my_obj.group())

print(re.findall(pattern,my_string,flags=re.I))


pattern_obj = re.compile(pattern,flags= re.I)

print(pattern_obj)

print(pattern_obj.findall(my_string))

print(pattern_obj.search(my_string).group())
