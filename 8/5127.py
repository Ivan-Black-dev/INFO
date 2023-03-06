counter = 0

for i in range(1, 100000):
    if i % 2 == 0:
        o = oct(i)[2:]
        if len(o) == 5 and o[0] == '7' and (('65' in o) ^ ('56' in o)):
            counter += 1
print(counter)
