import sys

""" sys.argv
commond line arguments passed to python script   """

if(len(sys.argv) != 3):
    print("wrong inputs this script require 2 commond arguments")
    sys.exit()

print(sys.argv)

print(sys.argv[0])


""" program to take two inputs from commond line
    first input is : string
    second input is : upper or lower
"""


enter_string = sys.argv[1]

enter_type = sys.argv[2]

if(enter_type == "lower"):
    print(enter_string.lower())
elif(enter_type == "upper"):
    print(enter_string.upper())
else:
    print(enter_string)

