G = {
'А': 'БГ',
'Б': 'Д',
'В': 'АБГДЖ',
'Г': 'Ж',
'Д': 'ЕИ',
'Ж': 'Е',
'И': 'ЕЛ',
'К': 'Ж',
'Л': 'К',
'Е': 'ВКЛ'
}


count = 0
def genWay(way, end):
    global count
    lastTown = way[-1]
    if lastTown == end and len(way) > 2:
        count += 1
        print(way)
        return None
    
    for town in G[lastTown]:
        if town not in way or town == end:
            genWay(way+town, end)


genWay("Е", "Е")
print(count)
