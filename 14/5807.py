for x in range(0, 10):
    p1 = int(f'12{x}34')
    p2 = int(f'1{x}234')
    n1 = 1 * p1 + 9
    n2 = 2 * p2 + 1
    s = n1 + n2
    if s % 11 == 0:
        print(s/11)
