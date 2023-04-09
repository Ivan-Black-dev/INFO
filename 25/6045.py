from fnmatch import *

for i in range(7181, 10**10, 7181):
    if fnmatch(str(i), '12?345*9'):
        print(i, i//7181)
