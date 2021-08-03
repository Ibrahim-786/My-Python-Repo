import re

text = "This is python there are two major versions python2 and python3 in feature python4"

pattern = r"\bpython\b"

print(re.findall(pattern,text))
print(re.search(pattern,text))

pattern = r"\bpython[23]\b"

print(re.findall(pattern,text))
print(re.search(pattern,text))

pattern = r"\bpython[23]?\b"

print(re.findall(pattern,text))
print(re.search(pattern,text))

pattern = r"\bpython\d?\b"

print(re.findall(pattern,text))
print(re.search(pattern,text))

match = re.search(pattern,text)
print(match)

print("math from ur pattern",match.group())

print("staring index",match.start())
print("ending index",match.end())

print("length of the text is ", match.end()- match.start())
#======================================================================
# need to check if match is present otherwise it is error
match = re.search(pattern,text)
print(match)

if match:
    print("math from ur pattern",match.group())

    print("staring index",match.start())
    print("ending index",match.end())

    print("length of the text is ", match.end()- match.start())

    
pattern = r"\bpythonnn\d?\b"
match = re.search(pattern,text)
print(match)

if match:
    print("math from ur pattern",match.group())

    print("staring index",match.start())
    print("ending index",match.end())

    print("length of the text is ", match.end()- match.start())
else:
    print("no match found")
#=====================================================================
#by default search is for multiline

text = """This is python there
are two major versions
python2 and python3
in feature python4"""

pattern = r"\bpython[234]?\b"
match = re.search(pattern,text)
print(match)

if match:
    print("match from ur pattern",match.group())

    print("staring index",match.start())
    print("ending index",match.end())

    print("length of the text is ", match.end()- match.start())


#=========================================================================
# match is same as search but only diff is it only look at first line


text = """This is python there
are two major versions
python2 and python3
in feature python4"""

pattern = r"\bpython[234]?\b"
print(re.match(pattern,text))

text = """python2 is python there
are two major versions
python2 and python3
in feature python4"""

pattern = r"\bpython[234]?\b"
print(re.match(pattern,text))
match = re.match(pattern,text)
print(match)

if match:
    print("match from ur pattern",match.group())

    print("staring index",match.start())
    print("ending index",match.end())

    print("length of the text is ", match.end()- match.start())






