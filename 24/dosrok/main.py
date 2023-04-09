with open('24.txt') as file:
    s = file.readline()

for c in 'QRS':
    s = s.replace(c, '*')

maxLen = 0
for st in s.split('*'):
    maxLen = max(len(st), maxLen)


print(maxLen+2)
