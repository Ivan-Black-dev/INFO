G = {
    'А': 'В',
    'Б': 'АД',
    'В': 'Е',
    'Г': '',
    'Д': 'З',
    'Е': 'Ж',
    'Ж': 'ГК',
    'З': 'Ж',
    'К': 'З'
    }


count = 0
def genWay(way, end):
    global count
    lastTown = way[-1]
    if lastTown == end and len(way) > 1:
        print(way)
        count += 1
        return None
    for town in G[lastTown]:
        if town not in way or town == end:
            genWay(way+town, end)


genWay('Ж', 'Ж')
print(count)
