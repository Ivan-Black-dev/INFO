from fnmatch import *

for i in range(5321, 10**10, 5321):
    if fnmatch(str(i), '12*135*9'):
        print(i, i//5321)
