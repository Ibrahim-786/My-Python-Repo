''' different ways of importing python modules '''

from math_funs import *
print(__name__)
if (__name__ == "__main__"):
    print(add(1,2))

    print(sub(2,1))


    print(mul(8,2))

    print(div(18,2))


    print(__name__)


import math_funs as simple_math
print(__name__)
if (__name__ == "__main__"):
    print(simple_math.add(1,2))

    print(simple_math.sub(2,1))


    print(simple_math.mul(8,2))

    print(simple_math.div(18,2))


    print(__name__)

   

from math_funs import add,sub,mul,div
print(__name__)
if (__name__ == "__main__"):
    print(add(1,2))

    print(sub(2,1))


    print(mul(8,2))

    print(div(18,2))


    print(__name__)
