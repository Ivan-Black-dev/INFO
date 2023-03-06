#4110 Решение с any(), all()
from functools import *
def m(h): #Возвращает варианты следующего хода
    return h + 2, h * 3
#print (moves(6))   #проверка moves
@lru_cache(None)
def g(h):
    if 50 <= h: return 'w'#конец игре (рекурсии)
    #if h > 80: return 'p1'
    if any(g(i) == 'w' for i in m(h)): return 'p1'  #выигрышв один ход
    #если неудачный ход Пети, то all меняем на any в следующей строке (19)
    if all(g(i) == 'p1' for i in m(h)): return 'v1' # проигрыш в один ход
    if any(g(i) == 'v1' for i in m(h)): return 'p2' # выигрыш в два хода
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(h)): return 'v2' # проигрыш в два хода

n19 = []
n20 = []
n21 = []
for s in range(1, 55+1):
    if g(s) == 'p2':
        n20.append(s)
    if g(s) == 'v1':
        n19.append(s)
    if g(s) == 'v2':
        n21.append(s)

print('19: ', min(n19))
print('20: ', len(n20))
print('21: ', n21)
