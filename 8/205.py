from itertools import product
k = 0
for i in product('ЕГЭ', repeat = 5):
    s = ''.join(i)
    if s[0] in 'ЕЭ':
        k += 1
print(k)
