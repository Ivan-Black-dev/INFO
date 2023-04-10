with open('24.txt') as file:
    s = file.readline()

#s = 'PNNPOPNONPOPNONPOPNONP'

s = s.replace('NPO', '*')
s = s.replace('PNO', '*')

c = 0
while '*'*c in s:
    c += 1
print(c-1)