with open('26.txt') as file:
    d = file.readlines()

dots = []
for i in d:
    dots.append([int(j)-1 for j in i.split(' ')])

mtr = []
for i in range(0, 100_000):
    mtr.append([0 for i in range(0, 100_000)])

print(len(mtr), len(mtr[0]))
