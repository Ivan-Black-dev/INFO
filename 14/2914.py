n = 2**51 + 2**40 + 2**35 + 2**17 - 2**5
res = set( hex(n)[2:] )
print(res, len(res))
