from itertools import product as p

counter = 0
for n in p('012345678', repeat=7):
    if n[0] not in {'0', '3', '7'}:
        fl = True
        g = ''.join(n)
        for i in range(0, 9):
            if str(i)*2 in g:
                fl = False
                break
        if fl:
            counter += 1
print(counter)
        
