from itertools import product as p

def main():
    counter = 0
    for i in p("ВЕСНА", repeat=3):
        s = ''.join(i)
        if s.count('А') >= 1:
            counter += 1
    print(counter)
    

if __name__ == "__main__":
    main()
