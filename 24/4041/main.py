with open('24.txt') as file:
    lines = [i.rstrip() for i in file.readlines()]


maxRG = 0
for line in lines:
    if line.count('G') < 15:
        maxR = 0
        for cr in set(line):
            #print(line, cr, line.find(cr),  line.rfind(cr))
            maxR = max(maxR, abs(line.find(cr) - line.rfind(cr)))
        #print(maxR, line)
        maxRG = max(maxRG, maxR)

print(maxRG)
