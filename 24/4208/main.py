def p(s):
    countPos = 0
    maxPos = 0
    for c in set(s):
        r = s.split(c)[1:-1]
        for i in r:
            if i:
                countPos += 1
                maxPos = max(maxPos, len(max(r, key=len)))
    return maxPos, countPos

with open('24.txt') as file:
    lines = [i.replace('\n', '') for i in file.readlines()]


maxPosGlobal = 0
countPos = 0
for line in lines:
    if line.count('R') < 30:
        maxPos, count = p(line)
        maxPosGlobal = max(maxPosGlobal, maxPos)
        countPos += count
print(maxPosGlobal+2, countPos)
