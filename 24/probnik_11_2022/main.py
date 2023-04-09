with open('24.txt') as file:
    s = file.readline()

#s = 'DDDACFEADDDMK'


while 'DD' in s:
    s = s.replace('DD', "D D")
r = s.split()
maxLen = 0
for i in r:
    if 'FE' in i:
        maxLen = max(maxLen, len(i))

print(maxLen)
