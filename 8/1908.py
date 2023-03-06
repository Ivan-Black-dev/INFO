from itertools import product as p

def main():
    counter = 0
    for i in p(set("РАДУГА"), repeat=6):
        s = ''.join(i)
        if (s.count('Р') + s.count('Д') + s.count('Г')) >= 3:
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
