with open('24.txt') as file:
    s = file.readline()

#s = 'ABDCCBAD'

r = []
for i in s.split('D'):
    r += i.split('E')

maxLen = 0
for i in r:
    maxLen = max(maxLen, len(i))
print(maxLen)
