from itertools import product as p

def chek(s):
    nc = '135'
    if s.count('2') != 1:
        return False
    else:
        i2 = s.index('2')
        if i2 == 0:
            return s[1] not in nc
        if i2 == 5:
            return s[4] not in nc
        else:
            return (s[i2-1] not in nc) and (s[i2+1] not in nc)
            


c = 0
for s in p('012345', repeat=6):
    if s[0] != '0':
        if chek(''.join(s)):
            c += 1
print(c)
