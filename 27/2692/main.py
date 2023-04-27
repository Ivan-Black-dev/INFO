f = open('27_B.txt')

n = int(f.readline())

s = [0]
for i in range(n):
    tr = [int(j) for j in f.readline().split()]
    s = [a+b for a in tr for b in s]
    s = {x%11:x for x in sorted(s)[::-1]}.values()

print(min([x for x in s if x % 11 == 0]))
