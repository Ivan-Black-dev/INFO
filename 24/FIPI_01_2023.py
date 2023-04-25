with open('24.txt') as file:
    s = file.readline().rsplit()

#s = 'ACDFOCOOCACDFAAAAC'
    
s = s.replace('A', 'G')
s = s.replace('O', 'G')
s = s.replace('C', 'S')
s = s.replace('D', 'S')
s = s.replace('F', 'S')

lenn = 0
maxLen = 0
for i in range(3, len(s)):
    if s[i-3] + s[i-2] + s[i-1] + s[i] == 'SGGS':
        maxLen = max(lenn+3, maxLen)
        lenn = 0
    else:
        lenn += 1
maxLen = max(lenn+3, maxLen)
print(maxLen)
