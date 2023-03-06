#3075_40 Решение с any(), all()

from functools import *
def m(h): #Возвращает варианты следующего хода
    return h + 1, h * 2

#print (m(6))   #проверка m
@lru_cache(None)
def g(h):
    if 45 <= h <= 65: return 'w'# конец игре (рекурсии)
    if h > 65: return p1
    
    if any(g(i) == 'w' for i in m(h)): return 'p1'  # выигрышв один ход
    if all(g(i) == 'p1' for i in m(h)): return 'v1' # проигрыш в один ход
    
    if any(g(i) == 'v1' for i in m(h)): return 'p2' # выигрыш в два хода
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(h)): return 'v2' # проигрыш в два хода
    
    if any(g(i) == 'v2' for i in m(h)): return 'p3' # выигрыш в три хода
    if all((g(i) == 'p1' or g(i) == 'p2' or g(i) == 'p3') for i in m(h)): return 'v3' # проигрыш в три хода
#k = 0
for s in range(1, 165+1):
    
    
    
    #if g(s) == 'v1':
        #print('№ 19:', s, g(s))
    if g(s) == 'v2':
        print(s)
        #print('№ 20:', s, g(s))    
    #if g(s) == 'v2':
        #print('№ 21:', s, g(s))    
#print(k)

# 82
# 41 81
# 80

