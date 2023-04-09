G = {
'А':'В',
'Б':'АГ',
'В':'ГЕ',
'Г':'ДЕ',
'Д':'БЖЗ',
'Ж':'ГИ',
'З':'ЖК',
'И':'Г',
'К':'ЖИ',
'Е':'Ж'
    }


def genWay(way, end):
    lt = way[-1]
    if lt == end and len(way) > 2:
        print(way, len(way)-1)
        return None
    for t in G[lt]:
        if t not in way or t == end:
            genWay(way+t, end)
            
genWay('Г', 'Г')
