from fnmatch import *


for i in range(9573, 10**10, 9573):
    if fnmatch(str(i), '202*47*6'):
        print(i, i//9573)
