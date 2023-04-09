with open('24.txt') as file:
    s = file.readline()

s = "XY"+ "X"*8 + 'YXY'
c = 1
maxLen = (1, s[0])
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        c += 1
        if c > maxLen[0]:
            maxLen = (c, s[i-1])
    else:
        c = 1
print(maxLen)
