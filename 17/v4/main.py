with open('17.txt') as file:
    data = [int(i) for i in file.readlines()]

def end9(n):
    return str(n)[-1] == '9'

max9 = -10**10
for n in data:
    if end9(n):
        max9 = max(max9, n)


count = 0
minSq = 10**10
for i in range(1, len(data)):
    n1, n2 = data[i-1], data[i]
    if (end9(n1) ^ end9(n2)) and (n1**2 + n2**2) < max9**2:
        count += 1
        minSq = min(minSq, (n1**2 + n2**2))
print(count, minSq)
