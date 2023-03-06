from itertools import permutations as pr

def main():
    c = list(pr('КЛН', 2)) + list(pr('ОУ', 2))
    c = [''.join(i) for i in c]
    print(c)
    counter = 0
    for i in pr('КОЛУН', 5):
        s = ''.join(i)
        if all(b not in s for b in c):
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
