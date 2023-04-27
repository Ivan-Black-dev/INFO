f = open('27_B.txt')

n = int(f.readline())

s = [0]
for i in range(n):
    p = [int(i) for i in f.readline().split()]
    s = [a + b for a in s for b in p]
    s = sorted(s)[::-1]
    s = {x%10:x for x in s}.values()
print(min([x for x in s if x % 10 == 4]))
