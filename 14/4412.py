n = 7**(160+90) - (14**150 + 2**13)
s = 0

while n:
    r = n%7
    if r != 6:
        s += r
    n //= 7

print(s)
