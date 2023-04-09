def obrS(S):
    lenn = 0
    mLenn = 0
    mC = ''
    for i in range(1, len(S)):
        if S[i-1] == S[i]:
            lenn += 1
        if S[i-1] != S[i]:
            if mLenn < lenn:
                mLenn = lenn
                mC = S[i-1]
            lenn = 0
    return S.count(mC)

with open('24.txt') as file:
    lines = file.readlines()

r = []
for line in lines:
    r.append(obrS(line))
print(max(r))
