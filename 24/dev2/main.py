with open('24.txt') as file:
    s = file.readline().replace('\n', '')
'''
#s = 'SGSSSSGGGSGS'
for c in ['A', 'E', 'U']:
    s = s.replace(c, "G")
for c in ['B', 'C', 'D', 'F']:
    s = s.replace(c, "S")

sSplit = s.split('SGS')
print(len(max(sSplit, key=len))+6)
'''
#s = 'ABABAAABABABAAABABBABABBB'
gl = 'AEU'
sgl = 'BCDF'
m = 0
last = 0
q = []  # очередь
for i in range(len(s)-2):
    #print(i, m, q)
    if s[i] in sgl and s[i+1] in gl and s[i+2] in sgl:
        #print(i, m, q)
        if i - last +2 > m:
            m = i - last + 2
        if len(q) > 1:
            last = q.pop(0)
        q.append(i+1)
print(m)  
# ответы: пример = 15; задача = 108
# см разбор
