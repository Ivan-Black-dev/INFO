with open('24.txt') as file:
    s = file.readline().replace('\n', '')

sm = dict()
#s = 'ABCAABADDD'
for i in range(1, len(s)):
    c1, c2 = s[i-1], s[i]
    if c1 == 'A':
        if sm.get(c2):
            sm[c2] += 1
        else:
            sm[c2] = 1
print(sm)

mV = 0
for i in sm.keys():
    if sm[i] > mV:
        print(i, sm[i])
        mV = sm[i]
