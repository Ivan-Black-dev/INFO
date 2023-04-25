with open('24.txt') as file:
    line = file.readline()


line = '**D*A***A'
maxLen = 0
maxChr = ''

for i in set(line):
    r = line.split(i)[1:-1]
    if r:
        maxC = len(max(r))
        if maxC > maxLen:
            maxLen = maxC
            maxChr = i
print(i, maxLen)