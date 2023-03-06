with open('17.txt') as file:
    lines = [ int(i.replace('\n', '')) for i in file.readlines()]


sr = sum(lines)/len(lines)

c = 0
mS = -100000000
for i in range(2, len(lines)):
    n1, n2, n3 = lines[i-2], lines[i-1], lines[i]
    if (n1 < sr or n2 < sr or n3 < sr) and  (( n1 % 3 == 0 ) or ( n2 % 3 == 0 ) or ( n3 % 3 == 0 )):
        mS = max(mS, n1+n2+n3)
        c += 1

print(c, mS)
