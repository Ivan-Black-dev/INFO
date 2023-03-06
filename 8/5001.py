from itertools import permutations as p


n = {'АО', 'ОА', 'ВТ', 'ТВ', 'ВР', 'РВ', 'ТР', 'РТ', 'АА', 'ОО', 'ТТ'}

counter = 0
for i in set(p('АВТОРОТА')):
    f = True
    s = ''.join(i)
    for j in n:
        if j in s:
            f= False
    if f:
        counter += 1
print(counter)
