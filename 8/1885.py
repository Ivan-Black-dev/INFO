from itertools import product as p

def main():
    counter = 0
    for i in p('АНДРЕЙ', repeat=7):
        s = ''.join(i)
        if s[0] != 'Й' and s.count('Й') == 1 and s.count('А') == 1:
            counter += 1
    print(counter)
    

if __name__ == '__main__':
    main()
