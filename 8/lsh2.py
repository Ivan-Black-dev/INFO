from itertools import product as p


def pal(s):
    c = len(s)//2
    return s[:c+1][::-1] ==  s[c:]


alb = [chr(i) for i in range(ord('A'), ord('Z')+1)]

c = 0
for n in p(alb, repeat=11):
    if pal(n):
        c += 1
print(c)
