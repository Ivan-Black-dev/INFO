with open('24.txt') as file:
    s = file.read()

maxLen = 0
for cr in range(ord('A'), ord('Z')+1):
    c = 0
    while chr(cr)*c in s:
        c += 1
    c -= 1

    if maxLen < c:
        maxLen = c

r = []
for cr in range(ord('A'), ord('Z')+1):
    if chr(cr)*maxLen in s:
        r.append(chr(cr))

with open('24.txt') as file:
    lines = [i.replace('\n', '') for i in  file.readlines()]

minC = 10**100
for line in lines:
    for cr in r:
        if cr*maxLen in line:
            minC = min(minC, line.count(cr))
print(minC)




