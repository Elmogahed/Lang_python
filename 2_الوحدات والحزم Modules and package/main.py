import utils
import pkg.module1 , pkg.module2
# import requests

pkg.module1.mod1()
pkg.module2.mod2()

print(pkg.numbers)


print(utils.__file__)

def greet(): 
    print('This is greet function from the main file')

utils.greet("Ahmed")
greet()

import sys
print(sys.path)

print()
print(dir())

