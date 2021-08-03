#regular expressions

import re


my_str = "python is easy to learn and it is very powerfull"

print(my_str)

print(my_str.split())

print(my_str.split("is"))

print(my_str.split("it"))

print(re.split("i[st]",my_str))

