from itertools import product
k=0
for x in product('АКРУ',repeat=5):
    s=''.join(x)
    if 'РУКАА'<= s <='УКАРА':
        k+=1
print(k)
