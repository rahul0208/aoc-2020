
f = open("sample.txt", "r")
# f = open("sample2.txt", "r")
f = open("data.txt", "r")
data = []

for d in f :
    data.append(list(d.rstrip()))


def occupy(i, j, mi, mj, d):
    o = 0;

    if i > 0:
        if j > 0:
            o = o + 1 if d[i - 1][j - 1] == '#' else o
        if j < mj:
            o = o + 1 if d[i - 1][j + 1] == '#' else o
        o = o + 1 if d[i - 1][j] == '#' else o
    if i < mi:
        if j > 0:
            o = o + 1 if d[i + 1][j - 1] == '#' else o
        if j < mj:
            o = o + 1 if d[i + 1][j + 1] == '#' else o
        o = o + 1 if d[i + 1][j] == '#' else o

    if j < mj:
        o = o + 1 if d[i][j + 1] == '#' else o
    if j > 0:
        o = o + 1 if d[i][j - 1] == '#' else o
    # print (i, j, o, d[i])
    if (d[i][j] == 'L') and o == 0:
        return True
    if (d[i][j] == '#') and o > 3:
        return True
    return False

def occupy2(i,j,mi,mj, d) :
    o = 0;

    pi = i -1
    pj = j -1
    loc = []
    while pi >= 0 and pj >= 0 and d[pi][pj] == '.':
        pi = pi - 1
        pj = pj - 1
    o = o + 1 if  pi >= 0 and pj >= 0 and d[pi][pj] == '#'else o
    loc.append([o,pi, pj])

    pi = i -1
    while pi >= 0  and d[pi][j] == '.':
        pi = pi - 1

    o = o + 1 if pi >= 0 and d[pi][j] == '#' else o
    loc.append([o, pi, j])

    pj = j-1
    while pj >= 0 and d[i][pj] == '.' :
        pj = pj - 1
    o = o + 1 if pj >= 0 and d[i][pj] == '#' else o

    pi = i -1
    pj = j +1
    while pi >= 0 and pj <= mj and d[pi][pj] == '.':
        pi = pi - 1
        pj = pj + 1
    o = o + 1 if pi >= 0 and pj <= mj and d[pi][pj] == '#' else o

    pi = i +1
    pj = j -1
    while pi <=mi and pj >= 0 and d[pi][pj] == '.':
        pi = pi + 1
        pj = pj - 1
    o = o + 1 if pi <=mi and pj >= 0 and d[pi][pj] == '#' else o

    pi = i + 1
    while pi <= mi and d[pi][j] == '.':
        pi = pi + 1
    o = o + 1 if pi <= mi and d[pi][j] == '#' else o


    pj = j + 1
    while pj <= mj and d[i][pj] == '.':
        pj = pj + 1
    o = o + 1 if pj <= mj and d[i][pj] == '#' else o

    pi = i +1
    pj = j +1
    while pi <=mi and pj <= mj and d[pi][pj] == '.':
        pi = pi + 1
        pj = pj + 1
    o = o + 1 if pi <=mi and pj <= mj and d[pi][pj] == '#' else o




    if(d[i][j]=='L')  and o == 0:
        return  True
    if (d[i][j] == '#') and o > 4:
        return True
    return False

mi =len(data)-1
change = True
countpass =1
while change  and countpass < 300:
    change = False
   # print(countpass)
    countpass = countpass+1
    passdata =[]
    # for k in range(0, len(data)):
    #     print("b ", data[k])
    for i in range(0, len(data)) :
        passdata.append(data[i].copy())
        mj = len(data[i])-1
        for j in range(0, len(data[i])):
            v = occupy2(i, j,mi, mj, data)
           # print(i,j,v)
            if v :
              change = True
              if (data[i][j] == 'L') :
                  passdata[i][j] ="#"
              else :
                  if (data[i][j] == '#') :
                     passdata[i][j] ="L"
    data = passdata
print(countpass)

occ = 0
for i in range(0, len(data)):
    occ= occ + data[i].count("#")
print(occ)



