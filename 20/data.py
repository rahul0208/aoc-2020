import sys
from math import sqrt

f = open("sample.txt", "r")
#f = open("sample2.txt", "r")
#f = open("data.txt", "r")
data = []
tileMap ={}
id = None
for d in f :
    dstr = d.rstrip()
    if 'Tile' in dstr :
        id = int(dstr.replace('Tile ','').replace(":",''))
    elif len(dstr) > 0 :
        data.append(dstr)
    else :
        tileMap[id] = data
        data = []
        id = None
tileMap[id] = data
print(tileMap)
edgeMap ={}
for k in tileMap.keys():
    edges = []
    tm = tileMap.get(k)
    edges.append(tm[0])
    edges.append(tm[len(tm)-1])
    edges.append("")
    edges.append("")
    for e in tm :
        edges[2] += e[0]
        edges[3] += e[len(e)-1]
    reverse = []
    for re in edges:
        reverse.append(re[::-1])
    edgeMap[k] = edges + reverse
    # print(k, tileMap.get(k))
    # print(edgeMap[k])

def matchingCount(srck, srcEdge) :
    cnt =[]
    for k in edgeMap:
        if k != srck :
            elist = edgeMap.get(k)
            for e in elist:
                 if srcEdge in e :
                     cnt.append(k)
    return cnt;

edgeid = {}
middleid = {}
sideid = {}
for k in edgeMap :
    elist  = edgeMap.get(k)
    ecntlist= []
    for e in elist :
        cnt = matchingCount(k,e)
        ecntlist.append(cnt)
    # print(k, ecntlist)
    ecnt = 0
    for i in range(0,4) :
        if len(ecntlist[i]) == len(ecntlist[i+4]) and len(ecntlist[i]) == 0 :
            ecnt += 1
    # print(ecnt)
    if ecnt == 2 :
        # print("edge")
        edgeid[k]=ecntlist
    if ecnt == 1 :
        # print("side")
        sideid[k]=ecntlist
    if ecnt == 0 :
        # print("middle")
        middleid[k]=ecntlist

# val = 1
# for i in edgeid :
#     val= val*i
# print(val)


print("edge",edgeid)
print("middleid",middleid)
for e in middleid.keys() :
    print(e, middleid.get(e))

print("sideid",sideid)

def connectIds(e1,e2, p) :
    # e1neig = edgeid.get(e1)
    # e2neig = edgeid.get(e2)
    cids = []
    for i in sideid.keys() :
        negh = sideid.get(i)
        # print(e1,i,negh,p)
        if i not in p and [e1] in negh:
            # print(i, negh)
            if [e2] in negh :
                return [i]
            else :
                val= connectIds(i, e2, p + [e1])
                cids = cids + val
                if val :
                    cids = [i] + cids
    return cids

rows = {}
isize= int(sqrt(len(edgeMap)))

imtiles = []
for i in range(0,isize):
    imtiles.append([0]*isize)

for e1 in edgeid.keys() :
    for e2 in edgeid.keys() :
        if e1 != e2 :
            if (e1, e2 ) not in rows and (e2, e1) not in rows :
                ids = connectIds(e1,e2,[])
                if(len(ids) > 0) :
                    t = (e1, e2)
                    print(t,ids)
                    # for i in ids :
                    #     rid = rid+i
                    #rid.append(e2)
                    # print("pair",e1,e2,set(rid))
                    rows[t] = ids
print("rows",rows)

used = []
def fill(x,y):
    id = imtiles[x][y]
    dx = isize - 1 if x == 0 else 0
    dy = isize - 1 if y == 0 else 0
    # print(x,y, dx, dy)
    for p1,p2 in rows.keys() :
        if id ==0 :
            id=p1
            imtiles[x][y] = p1
            # print(imtiles)
        if id == p1 :
            # print("p2", p2)
            if imtiles[dx][y] == 0 and imtiles[x][dy] != p2:
                imtiles[dx][y] = p2
            elif imtiles[x][dy] == 0 and imtiles[dx][y] != p2:
                imtiles[x][dy] = p2
        if id == p2 :
            # print("p1", p1)
            if imtiles[dx][y] == 0 and imtiles[x][dy]!= p1:
                imtiles[dx][y] = p1
            elif imtiles[x][dy] ==0 and imtiles[dx][y] != p1:
                imtiles[x][dy] = p1

fill(0,0)
fill(isize-1,0)
 # fill(0,isize-1)
# fill(isize-1,isize-1)

def fillVerical(y):
    p1 = imtiles[0][y]
    p2 = imtiles[isize-1][y]
    if (p1, p2) in rows :
        v = rows.get((p1,p2))
        # print("u",v)
        for i in range (1,isize-1) :
            imtiles[i][y] = v[i-1]
    else :
        v = rows.get((p2, p1))
        # print("d",v)
        for i in range(1, isize - 1):
            imtiles[isize-i-1][y] = v[i - 1]

def fillhorizontal(x):
    p1 = imtiles[x][0]
    p2 = imtiles[x][isize-1]
    if (p1, p2) in rows :
        v = rows.get((p1,p2))
        for i in range (1,isize-1) :
            imtiles[x][i] = v[i-1]
    else :
        v = rows.get((p2, p1))
        for i in range(1, isize - 1):
            imtiles[x][isize-i-1] = v[i - 1]

fillVerical(0)
fillVerical(isize-1)
fillhorizontal(0)
fillhorizontal(isize-1)

def fillhorizontalV2(p):
    for i in range(1,isize-1):
        x1 = imtiles[p-1][i]
        y1 = imtiles[p][i-1]
        for e in middleid.keys():
            enghs = middleid.get(e)
            # print("chk", x1, y1, enghs)
            if [x1] in enghs and [y1] in enghs :
                imtiles[p][i]=e

for i in range (1,isize-1) :
     fillhorizontalV2(i)

for e in imtiles :
    print(e)

printImtiles = []
for i in range(0,isize):
    printImtiles.append([0]*isize)

for i in range(0,isize-1):
    for j in range(0, isize-1):
        n = imtiles[i][j]
        dn = imtiles[i+1][j]
        sn = imtiles[i][j+1]
        exp = tileMap.get(n)
        # print(n,dn,sn,exp)
        if n in edgeid.keys()  :
            nlist = edgeid.get(n)
        elif n in middleid.keys() :
            nlist = middleid.get(n)
        else :
            nlist = sideid.get(n)
        if nlist[0] == [dn]:
            exp.reverse()
            # print("exp1",exp)
        if nlist[1] == [dn]:
            exp = exp
        if nlist[2] == [sn]:
            texp = []
            for e in exp:
                texp.append(e[::-1])
            exp = texp
            # print("exp2", exp)
        if nlist[3] == [sn]:
            exp = exp
        # print(n,dn,sn,exp)
        printImtiles[i][j] = exp



for i in range(0,isize-1):
    n = imtiles[i][isize-1]
    dn = imtiles[i+1][isize-1]
    sn = imtiles[i][isize-2]
    exp = tileMap.get(n)
    if n in edgeid.keys():
        nlist = edgeid.get(n)
    elif n in middleid.keys() :
        nlist = middleid.get(n)
    else :
        nlist = sideid.get(n)

    print(n, dn, sn, nlist, exp)
    if nlist[0] == [dn]:
        print("revese x")
        exp.reverse()
    if nlist[1] == [dn]:
        print("do not revese x")
        exp = exp
    if nlist[2] == [sn]:
        print("do not revese y")
        exp = exp
    if nlist[3] == [sn]:
        print("revese y")
        texp = []
        for e in exp:
            texp.append(e[::-1])
        exp = texp
    printImtiles[i][isize-1] = exp


# for i in range(0,isize-1):
#     n = imtiles[isize-1][i]
#     un = imtiles[isize-2][i]
#     sn = imtiles[isize-1][i+1]
#     exp = tileMap.get(n)
#     print(n,dn,sn,len(exp))
#     if n in edgeid.keys()  :
#         nlist = edgeid.get(n)
#     elif n in middleid.keys() :
#         nlist = middleid.get(n)
#     else :
#         nlist = sideid.get(n)
#     if nlist[0] == [un]:
#         exp = exp
#     if nlist[1] == [un]:
#         exp.reverse()
#     if nlist[3] == [sn]:
#         exp = exp
#     if nlist[2] == [sn]:
#         texp = []
#         for e in exp:
#             texp.append(e[::-1])
#         exp = texp
#     printImtiles[isize-1][i] = exp

patlen = len(printImtiles[0][0])
for i in range(0,isize-1):
    print(" ")
    for k in range(0, patlen):
        ptext = ""
        for j in range(0, isize):
            ptext += " "+printImtiles[i][j][k]
        print(ptext)
