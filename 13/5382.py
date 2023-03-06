G = {
    'А': 'БЖ',
    'Б': 'ВЗ',
    'В': 'Г',
    'Г': 'ДЕЖЗ',
    'Д': 'Е',
    'Ж': 'З',
    'З': 'АВ',
    'Е': 'АЖ'
    }

count = 0
def genWay(way, end):
    global count
    lastPoint = way[-1]
    if lastPoint == end and len(way) > 1:
        count += 1
        print(way)
        return None
    for point in G[lastPoint]:
        if point not in way or point == end:
            genWay(way+point, end)

genWay('З', 'З')
print(count)
