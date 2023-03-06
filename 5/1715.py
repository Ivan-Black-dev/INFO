from itertools import *


def alg(n):
    a = list(permutations([int(i) for i in str(n)], 2))
    a = [ i[0] * 10 + i[1] for i in a ]
    minN, maxN = 100, 0
    for i in a:
        if len(str(i)) > 1:
            minN = min(minN, i)
            maxN = max(maxN, i)
    return maxN - minN
    
counter = 0
for n in range(800, 901):
    print(n)
    if alg(n) == 30:
        counter += 1
print(counter)
