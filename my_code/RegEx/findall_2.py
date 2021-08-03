#^           only find in start of the string (start of line in multiline string)
#$           only find in end of the string (new line in multiline string)
#\b          empty string at begining or end of word
#\B          empty string not at the beginning or end of word
#\t \n \r    tab newline return

import re

text = "it is a python and it is easy to learn"

pattern = "i[st]"

print(re.findall(pattern,text))
#=================================================================

pattern = "^i[st]"  # only find in start of the string (start of line in multiline string)

print(re.findall(pattern,text))
#================================================================

text = "is a python and it is easy to learn"

pattern = "^i[st]"

print(re.findall(pattern,text))
#================================================================

text = "is learn a python and it is easy to learn"

pattern = "learn$" # only find in end of the string (new line in multiline string)

print(re.findall(pattern,text))

#================================================================

text = "is learn a python and it is easy to learn"

pattern = "learn$" # only find in end of the string (new line in multiline string)

print(re.findall(pattern,text))
text = "is learn a python and it is easy to learning"

pattern = "learn$" # only find in end of the string (new line in multiline string)

print(re.findall(pattern,text))

#===============================================================

text = "learning python is learn python and it is learn to learn"

pattern = "\b" # empty string at begining or end of word
#\b is for backspace 

print(re.findall(pattern,text))

pattern = "\\blearn" # empty string at begining or end of word
#\\b is for escape that backspace 

print(re.findall(pattern,text))

pattern = "learn\\b" # empty string at begining or end of word
#\\b is for escape that backspace 

print(re.findall(pattern,text))


pattern = "\\blearn\\b" # empty string at begining or end of word
#\\b is for escape that backspace 

print(re.findall(pattern,text))


#===============================================================
#\b using r not \\b


text = "learning python is learn python and it is learn to learn"

pattern = r"\b" # empty string at begining or end of word
#r is for backspace 

print(re.findall(pattern,text))
print(len(re.findall(pattern,text)))

pattern = r"\blearn" # empty string at begining or end of word
#r is for escape that backspace 

print(re.findall(pattern,text))

pattern = r"learn\b" # empty string at begining or end of word
#r is for escape that backspace 

print(re.findall(pattern,text))


pattern = r"\blearn\b" # empty string at begining or end of word
#r  is for escape that backspace 

print(re.findall(pattern,text))

#=====================================================================
#\B  empty string not at the beginning or end of word


text = "learning python is learn python and it is learn to learn"

pattern = r"learn\B" #  empty string not at the beginning or end of word
#r is for backspace 

print(re.findall(pattern,text))
print(len(re.findall(pattern,text)))

text = "learning python is learn python and it is learn to inlearn"

pattern = r"\Blearn" #  empty string not at the beginning or end of word
#r is for backspace 

print(re.findall(pattern,text))
print(len(re.findall(pattern,text)))


text = "iamlearning python is learn python and it is learn to learn"

pattern = r"\Blearn\B" #  empty string not at the beginning or end of word
#r is for backspace 

print(re.findall(pattern,text))
print(len(re.findall(pattern,text)))

#=====================================================================
#\t \n \r  tab newline return       

text = "simple_regex_1.py    \n \n    is learn python and it is learn to  \n   learn"

pattern = r"\n" #  newline
#r is for backspace 

print(re.findall(pattern,text))
print(len(re.findall(pattern,text)))

text = "    simple_regex_1.py          \n \n    is learn pyt    hon and it   is learn to  \n   learn"

pattern = r"\t" #  tab
#r is for backspace 

print(re.findall(pattern,text))
print(len(re.findall(pattern,text)))


#=====================================================================


