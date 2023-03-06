from itertools import product as p

def main():
    counter = 0
    ch = {'0', '2', '4', '6'}
    for i in p('01234567', repeat=5):
        if i[0] != '0':
            s = ''.join(i)
            if s.count('6') == 1:
                i6 = s.index('6')
                if i6 == 0:
                    if s[i6+1] in ch:
                        counter += 1
                if i6 == len(s)-1:
                    if s[i6-1] in ch:
                        counter += 1
                else:
                    if s[i6-1] in ch and s[i6+1] in ch:
                        counter += 1               
    print(counter)
        


if __name__ == "__main__":
    main()
