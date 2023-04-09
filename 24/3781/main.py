from collections import Counter as cnt

with open('24.txt') as file:
    lines = [i.replace('\n', '') for i in file.readlines()]

minA = ''
minCA = 10**100
for line in lines:
    if minCA > line.count('A'):
        minA = line
        minCA = line.count('A')

# V

with open('24.txt') as file:
    print(file.read().count('V'))
