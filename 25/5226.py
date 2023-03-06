def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac

def f(x):
    return 19500000+x


a = []
for i in range(0, 100):
    mn = primfacs(f(i))
    if len(mn) < 3:
        a.append((i, mn))

for i in range(0, 5):
    print(a[i][0], max(a[i][1]))
