G = {
'А': 'Б',
'Б': 'В',
'В': 'ГЖЕ',
'Г': 'И',
'Д': 'А',
'Е': 'АД',
'Ж': 'ЕГ',
'И': 'МН',
'К': 'ДЖ',
'Л': 'КЖ',
'М': 'ЖЛ',
'Н': 'М',
}


def genWay(way, end):
    global count
    lT = way[-1]
    if len(way) > 2 and lT == end:
        print(way)
        count += 1
        return None

    for i in G[lT]:
        if i not in way or i == end:
            genWay(way+i, end)

count = 0
genWay('Е', 'Е')
print(count)
