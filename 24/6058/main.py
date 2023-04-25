fileName = '24.txt'

with open(fileName) as file:
    s = file.read()

maxLen = 0
maxChr = ''
for i in range(ord('A'), ord('Z')+1):
    c = 0
    while chr(i)*c in s:
        c += 1
    c -= 1
    if c > maxLen:
        maxChr = chr(i)
        maxLen = c

with open(fileName) as file:
    lines = file.readlines()

maxCount = 0
for line in lines:
    if maxChr*maxLen in line:
        maxCount = max(maxCount, line.count(maxChr))

print(maxCount)
