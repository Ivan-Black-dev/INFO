with open('24.txt') as file:
    line = file.readline()

for i in 'ABC':
    line = line.replace(i, 'S')

for i in '123':
    line = line.replace(i, '*')

c = 0
while 'S*'*c in line:
    c += 1
print(c-1)