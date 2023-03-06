def alg(n):
    return bin(n)[2:][:-2]

a = set()
for i in range(20, 601):
    a.add(alg(i))
print(len(a))
