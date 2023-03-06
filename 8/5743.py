from itertools import product as p

counter = 0
for n in p('012345678', repeat=6):
    if n[0] != '0':
        s = ''.join(n)

        cN = 0
        for c in {'1', '3', '5', '7'}:
            cN += s.count(c)

        summ = sum([int(i) for i in n])
        if cN <= 2 and (summ % 6 == 0) and (summ % 4 != 0):
            counter += 1
print(counter)
