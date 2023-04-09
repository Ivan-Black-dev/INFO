with open('24.txt') as file:
    s = file.readline()

#s = 'NPOPPPPPNONPO'

s = s.replace("NPO", 'p')
s = s.replace("PNO", 'p')

c = 0
while 'p'*c in s:
    c += 1
print(c-1)
