def mask(v1, v2):
    return int(f'1{v1}34567{v2}9')

for v1 in range(0, 10):
    for v2 in range(0, 10):
        res = mask(v1, v2)
        if res % 17 == 0:
            print(res, res//17)
