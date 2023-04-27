f = open('27_B.txt')

n = int(f.readline())

s = [0]
for i in range(n):
    par = [int(j) for j in f.readline().split()]
    s = [a+b for a in s for b in par]
    s = {x%10:x for x in sorted(s)}.values()

print(max([x for x in s if x%10 != 5]))
