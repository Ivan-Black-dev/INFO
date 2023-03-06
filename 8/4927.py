from itertools import product as p

count = 0
a = [str(i)*3 for i in range(0,9)]
for i in p('012345678', repeat=7):
    if i[0] != '0':
        s = ''.join(i)
        if (all([(j not in s) for j in a] )) and s[-1] not in {'3', '4', '7'}:
            count += 1
print(count)
        
