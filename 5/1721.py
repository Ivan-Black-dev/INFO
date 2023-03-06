from itertools import permutations as pr

def alg(n):
    a = [int(i) for i in str(n)]
    a = list(pr(a, 2))
    a = [ i[0]*10 + i[1] for i in a]
    minN, maxN = 100, 0
    for i in a:
        if len(str(i)) > 1:
            minN = min(i, minN)
            maxN = max(i, maxN)
    return maxN - minN

count = 0
for i in range(100, 1000):
    print(i)
    if alg(i) == 58:
        count += 1
print(count)
