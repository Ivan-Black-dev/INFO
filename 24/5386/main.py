with open('24.txt') as file:
    s = file.readline().replace('\n', '')

#s = "APAAPAOAOBOCOOOO"
for c in ['A', 'O']:
    s = s.replace(c, 'G')
for c in ['B', 'C', 'D']:
    s = s.replace(c, 'S')

c = 0
while 'GS'*c in s:
    c += 1
print(c-1)
