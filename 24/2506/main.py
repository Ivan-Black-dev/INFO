with open('24.txt') as file:
    s = file.readline()

n = 0
while 'C' * n in s:
    n += 1
print(n-1)
