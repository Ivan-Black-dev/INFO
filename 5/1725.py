from itertools import permutations as pr

def alg(n):
    ls = []
    
    for x in pr(str(n), 2):
        s = ''.join(x)
        if s[0] != '0':
            ls.append(int(s))
    return max(ls) - min(ls)

for n in range(999, 100-1, -1):
    if alg(n) == 50:
        print(n)
        break
