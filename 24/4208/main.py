with open('24.txt') as file:
    lines = [i.replace('\n', '') for i in file.readlines()]

def proc(s):
    cCp = 0
    maxLen = 0
    for cr in set(s):
        line = s
        for i in set(s):
            if cr != i:
                line = line.replace(i, '*')
        line = line.strip('*')
        cCp += int(line.count(cr)/2)
        lenn = 0
        while '*'*lenn in line:
            lenn += 1
        maxLen = max(maxLen, lenn+1)
    return (maxLen, cCp)


maxLen = 0
c = 0
for i in lines:
    Len, cCp = proc(i)
    maxLen = max(maxLen, Len)
    c += cCp
print(maxLen, c)
