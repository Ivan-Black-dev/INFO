from fnmatch import *


for i in range(10**8):
    if fnmatch(str(i), '2*5443?1') and i % 23 == 0:
        print(i, i//23)
