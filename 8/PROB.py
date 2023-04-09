from itertools import product as p

c = 0
for n in p(sorted("СОЙКА"), repeat=5):
    s = ''.join(n)
    c += 1
    if s.count('О') <= 1 and all('С' * i not in s for i in range(2, 6)):
        print(c, s)
    
