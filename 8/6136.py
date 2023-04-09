from itertools import permutations as p

def ch(s):
    if ('ОО' not in s) and ('АА' not in s) and ('ОА' not in s) and ('АО' not in s):
        return True
    else:
        return False
    
c = 0
for s in set(p('ВОДОПАД')):
    if ch(''.join(s)):
        c += 1
print(c)
