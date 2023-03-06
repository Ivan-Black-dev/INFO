n = (64**25 + 4**10) - (16**20 + 32**3)
s = ''
while n:
    s += str(n%4)
    n //= 4
print(s.find('2'))
