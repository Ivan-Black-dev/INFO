f = open('27_B.txt')

n = int(f.readline())

s = [0]
for i in range(n):
    tr = [int(i) for i in f.readline().split()]
    s = [a+b for a in s for b in tr]
    s = {x%7:x for x in sorted(s)[::-1]}.values()

print(min([x for x in s if x % 7 != 0]))
