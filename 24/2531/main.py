with open('24.txt') as file:
    s = file.readline().replace('\n', '')

#s = "ZABCZ"

maxLen = (0, 0)
Len = 1
for i in range(1, len(s)):
    c1, c2 = s[i-1], s[i]
    if (ord(c2) - ord(c1)) > 0:
        Len += 1
    else:
        Len = 0
    if maxLen[0] < Len:
        maxLen = (Len, i-Len+1)

print(maxLen)
