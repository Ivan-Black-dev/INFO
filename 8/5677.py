from itertools import permutations as p


count = 0
for i in set(p('СПОРТЛОТО')):
    if i[0] == 'О' or i[-1] == 'О':
        count += 1
print(count)
