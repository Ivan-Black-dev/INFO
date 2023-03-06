from fnmatch import *
for x in range(20167, 10**7+1):
    if fnmatch(str(x), '2?1*67'):
        if x%159 == 0:
            print(x, x//159)
