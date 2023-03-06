def alg(n):
    nBin = bin(n)[2:]
    endNum = nBin[len(nBin)-1]
    countOne = nBin.count('1')
    nBin += endNum
    if countOne % 2 == 0:
        nBin += '0'
    else:
        nBin += '1'
    if nBin.count('1') % 2 == 0:
        nBin += '0'
    else:
        nBin += '1'
    return int(nBin, 2)



    
for i in range(0, 100):
    res = alg(i)
    if res > 80:
        print(res)
        break
