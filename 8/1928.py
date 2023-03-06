from itertools import permutations as pr

def main():
    counter = 0
    for i in pr('МАНОК', 5):
        s = ''.join(i)
        if s[0] != 'О' and 'АО' not in s:
            counter += 1
    print(counter)

if __name__ == '__main__':
    main()
