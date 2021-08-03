#finding ip address pattern in given string


import re


my_string = "Theip address of my IPv4 Address. . . . . is. . . . . . : 192.168.1.100  123488484859359"


pattern = "\d\d\d.\d\d\d.\d.\d\d\d"


print(re.findall(pattern,my_string))

pattern = "\d\d\d\.\d\d\d\.\d\.\d\d\d"



print(re.findall(pattern,my_string))
