from itertools import permutations as p

counter = 1
for i in p('СПОРТЛОТО'):
    if i[0] != 'О' and i[-1] != 'О':
        counter += 1
print(counter)
