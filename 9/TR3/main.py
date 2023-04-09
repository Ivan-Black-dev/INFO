from collections import Counter as cn


def f(num):
    cnum = cn(num)
    p = []
    np = []
    for i in cnum:
        if cnum[i] == 1:
            np.append(i)
        else:
            p.append(i)
    return (p, np)

    
with open('9.txt') as file:
    d = file.readlines()

nums = []
for i in d:
    nums.append([int(j) for j in i.split('\t')])

count = 0
for num in nums:
    p, np = f(num)
    if len(p) > 0 and len(np) > 0:
        sp = sum(p)/len(p)
        snp = sum(np)/len(p)
        if snp > sp:
            count += 1

print(count)
