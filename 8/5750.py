from itertools import product as p

def f(s):
    if ('К' in s) and ('О' in s) and ('Т' in s):
        k = s.index('К')
        o = s.index('О')
        t = s.index('Т')
        if k < o < t:
            return True
        else:
            return False

s = "ОКОТРГ"
print(f(s))
"""
count = 0
for i in p('КОМПЬЮТЕР', repeat=6):
    if f(''.join(i)):
        count += 1
print(count)
"""
