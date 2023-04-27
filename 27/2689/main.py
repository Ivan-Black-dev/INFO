f = open('27_B.txt')

n = int(f.readline())

s = [0]

for i in range(n):
    tr = [int(j) for j in f.readline().split()]
    tr = [tr[0] + tr[1], tr[1] + tr[2], tr[0] + tr[2]]
    s = [a+b for a in s for b in tr]
    s = {x%5:x for x in sorted(s)}.values()

print(max([x for x in s if x % 5 != 0]))
