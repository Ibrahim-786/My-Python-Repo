import re

my_string  = "This is python and we are having python2 python3 versions also"

pattern = r"\bpython[23]?\b"

print(re.match(pattern,my_string))

print(re.search(pattern,my_string))

print(re.findall(pattern,my_string))

print(len(re.findall(pattern,my_string)))

#Draw back of finall

#there is no information regarding index of matchings

print(re.finditer(pattern,my_string))

pattern = r"\bpyxthon[23]?\b"

print(re.finditer(pattern,my_string))

for iterator in re.finditer(pattern,my_string):
    print(iterator)

pattern = r"\bpython[23]?\b"

for iterator in re.finditer(pattern,my_string):
    print(iterator.group(), iterator.start(), iterator.end())
    
