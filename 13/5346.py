# 5346 ege13
G = {'А':'БГ',
     'Б':'Д',
     'В':'АБГД',
     'Г':'ЕЖ',
     'Д':'ЗЕК',
     'Е':'КВ',
     'Ж':'Е',
     'З':'К',
     'И':'Ж',
     'К':'ИЖ',}
count = 0
def f(way, end):
    global count
    lastTown = way[-1]
    if lastTown == end and len(way) > 1:
        count+=1
        print(way)
        return None
    for town in G[lastTown]:
        if town not in way or town == end:
            f(way+town, end)
              
f('Е', 'Е')
print(count)
