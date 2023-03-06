from itertools import product as p

counter = 0
for i in p('ОБЩЕСТВ', repeat=5):
    s = ''.join(i)
    if ( s[0] not in {'Щ', 'Б'} ): # Первое условие
        if ( s[3:] == 'ВВ' ):
            if('ЕВ' not in s) and ('ВЕ' not in s):
                if 'ТБ' in s:
                    counter += 1
print(counter)
