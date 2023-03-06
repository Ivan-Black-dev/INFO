G = {
    'А':'БДЕ',
    'Б':'ВЗ',
    'В':'ЖЗ',
    'Г':'АБ',
    'Д':'И',
    'Е':'ЗД',
    'Ж':'ЛЗ',
    'И':'ЕЗК',
    'К':'З',
    'Л':'К',
    'З':'ГЛ'
    }


count = 0
def f(way, end):
    global count
    lastTown = way[-1]
    if lastTown == end and len(way) > 1:
        print(way)
        count += 1
        return None

    for town in G[lastTown]:
        if town not in way or town == end or town != 'Д':
            f(way+town, end)

f('З', 'З')
print(count)
