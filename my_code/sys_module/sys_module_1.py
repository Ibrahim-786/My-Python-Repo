#demonstration of sys modules
""" not about operating system it's about to get python run time environment
 in your system"""

import sys


print(dir(sys))

print(sys.__doc__)

print(sys.platform)

print(sys.version)
print(sys.version_info)
sys.exit()

print(sys.modules)
print(sys.path)
