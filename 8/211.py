from itertools import product
k = 0
for i in product('МЕТРО', repeat = 4):
    s = ''.join(i)
    if s[0] in 'МТР' and s[-1] in 'ЕО':
        k += 1
print(k)
