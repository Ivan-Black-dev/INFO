'''with open('24.txt') as file:
    s = file.readline()


#s = 'ABCD'
for i in range(65, 91):
    c = chr(i)
    if c in ['A', 'E', 'I', 'O', 'U', 'Y']:
        s = s.replace(c, "g")
    else:
        s = s.replace(c, 's')

'''

s = 'sgggggs'
mlen = 0
lenS = 1
cgls = 0
for i in s:
    if i == 'g':
        cgls += 1
    if cgls > 5:
        mlen = max(lenS, mlen)
        lenS = 0
        cgls = 0
    lenS += 1
print(mlen)
