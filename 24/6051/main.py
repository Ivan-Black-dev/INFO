with open('24.txt') as file:
    s = file.readline().replace('\n', '')

for c in ['A', 'E', 'O']:
    s = s.replace(c, 'G')
for c in ['B', 'C', 'D', 'F']:
    s = s.replace(c, 'S')

c = 0
while 'SSG'*c in s:
    c += 1
print(c-1)
