with open('24.txt') as file:
    s = file.read()

# A, B, C, D, O
for c in ["A", "O"]:
    s = s.replace(c, 'G')
for c in ["B", "C", "D"]:
    s = s.replace(c, 'S')


#s = 'SGSGGGSG'
count = 0
while 'SG' * count in s:
    count += 1

print(count-1)
