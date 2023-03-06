with open('9.txt') as f:
    s = [i.replace('\t', ' ').replace('\n', '') for i in f.readlines()]
d = []

for n in s:
    d.append(sorted([int(i) for i in n.split(' ')]))


c = 0
for n in d:
    sr = sum(n)/len(n)
    if n[-1] > sr and n[-2] > sr and n[-3] > sr:
        c += 1
print(c, len(d))

