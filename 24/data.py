

f = open("sample.txt", "r")
# f = open("sample2.txt", "r")
f = open("data.txt", "r")
data = []

for d in f :
    dstr = d.rstrip()
    inst = []
    move = ""
    for i in list(dstr) :
        if i =='e' or i == 'w' :
            move += i
            inst.append(move)
            move = ""
        else :
            move = ""+i
    data.append(inst)

# print(data)

tilepos=[]
for instList in data :
    tx = 0
    ty = 0
    incx = 0
    incy = 0
    # print(instList)
    for e in instList :
        if e == "e" :
            incx = 2
            incy = 0
        if e == "se":
            incx = 1
            incy = -1
        if e=="ne" :
            incx = 1
            incy = 1
        if e=="w":
            incx = -2
            incy = 0
        if e=="sw" :
            incx = -1
            incy = -1
        if e =="nw":
            incx = -1
            incy = 1
        tx += incx
        ty += incy
        # print((tx,ty))

    tilepos.append((tx,ty))

# print(tilepos)

tilecolor =[[],[]]
for e in tilepos :
    c = tilepos.count(e)
    tilecolor[c % 2].append(e)

tileGrid = {}
for i in range(-70,70) :
    x = i
    y = -70 if abs(x) % 2 == 0 else -69
    rowGrid =[]
    while y < 70 :
        tileGrid[(x,y)] = 1 if (x,y) in tilecolor[1] else 0
        y += 2


cnt = 1
while cnt < 101:
     temp = {}

     sbcount = 0
     for e in tileGrid.keys():
         colo = tileGrid.get(e)
         if colo == 1:
             sbcount = sbcount + 1

     for (kx,ky) in tileGrid.keys() :
          c = tileGrid.get((kx,ky))
          neigh=[(kx + 2, ky), (kx-2, ky),(kx + 1, ky + 1),(kx + 1, ky - 1),(kx - 1, ky + 1), (kx - 1, ky - 1)]
          neighcolors = []

          for n in neigh :
                nc = 0
                if n in tileGrid.keys() :
                    nc = tileGrid.get(n)
                else :
                    temp[n] =  0
                neighcolors.append(nc)

          neighb = sum(neighcolors)


          if c == 1 and (neighb == 0 or neighb > 2) :
              # print(f'--- flip  white--')
              temp[(kx, ky)] = 0
          if c == 0 and neighb == 2:
              # print(f'--- flip  black--')
              temp[(kx, ky)] = 1

     tcount = 0
     for e in temp.keys() :
         tileGrid[e] = temp[e]
         if temp[e] == 1 :
             tcount = tcount + 1

     bcount = 0
     pos =[]
     for e in tileGrid.keys():
         colo = tileGrid.get(e)
         if colo == 1 :
             bcount = bcount + 1
             pos.append(e)
     if (cnt% 10 == 0 or cnt < 10):
        print(f' End Day {cnt} {bcount}')
     cnt +=1