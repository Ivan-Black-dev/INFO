from itertools import product as p


def main(): 
    counter = 0
    for i in p('012345678', repeat=5):
        if i[0] != '0':
            nCh = '1357'
            s = ''.join(i)
            if (s[0] not in nCh) and ( s[-1] not in '18') and s.count('3') <= 1:
                counter += 1
    print(counter)

if __name__ == "__main__":
    main()
