from itertools import product as p

def ch(s):
    if (s[0] <= s[2] <= s[4]) and (s[1] <= s[3] <= s[5]):
        return True
    else:
        return False

c = 0
for s in p('ДРЕВО', repeat=6):
    r = ''.join(s)
    if ch(r):
        c += 1
print(c)
