from itertools import product as p

# CFE FCE


with open('24.txt') as file:
    s = file.read().replace('\n', '')

s = s.replace('CFE', '*')
s = s.replace('FCE', '*')

count = 0
while '*' * count in s:
    count += 1
print(count-1)
