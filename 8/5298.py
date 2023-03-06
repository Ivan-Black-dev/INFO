from itertools import product as p

a = "АЕЖЙМУ"
counter = 0
for c in zip(p(a, repeat=5), range(1, 1000000)):
    s, i = c
    x = ''.join(s)
    if i % 2 == 0:
        fl = True
        for i in range(len(x)-1):
            if s[i] == s[i+1]:
                fl = False
                break
        if fl:
            counter += 1
print(counter)
        
