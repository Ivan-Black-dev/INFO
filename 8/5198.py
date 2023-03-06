from itertools import product as p

counter = 0
for i in zip(range(1, 1000000), p('СТЕПУХА', repeat=4)):
    n, s = i
    s = ''.join(s)
    if n > 1000:
        fl = True
        for j in 'СТЕПУХА':
            if s.count(j*2) < 0:
                fl = False
                break
        if fl:
            counter += 1
            
print(counter)
