n = ( 2**345 + 8**65 - 4**130 ) * ( 8**123 - 2**89 + 4**45 )
summ = 0 
while n:
    summ += n%8
    n //= 8
print(summ)
