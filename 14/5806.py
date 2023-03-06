for x in range(0, 10):
    p1 = int(f'123{str(x)}5')
    p2 = int(f'1{str(x)}233')
    n1 = p1 + 5
    n2 = p2 + 5
    s = n1 + n2
    if s % 14 == 0:
        print(s//14)
