
f = open("sample.txt", "r")
#f = open("sample2.txt", "r")
f = open("data.txt", "r")

cpos = {}
cx = 0
for d in f :
    cubes = []
    str = d.rstrip()
    for i in  list(str) :
        if i == '.' :
            cubes.append(False)
        else :
            cubes.append(True)


    for y in range(0, len(cubes)):
        cpos[(cx, y, 0, 0)] = cubes[y]

    cx += 1

def cposval(x, y, z, w):
    return cpos[(x, y, z, w)] if (x, y, z, w) in cpos else False

for x in range(-35, 35):
    for y in range(-35, 35):
        for z in range(-35, 35):
            for w in range(-35, 35):
                cpos[(x, y, z, w)] = cposval(x, y, z, w)
                if cpos[(x, y, z, w)] :
                    print ("Initial True",(x, y, z, w))

def countEnabled():
    cnt = []
    for w in range(-35, 35):
        for z in range(-35, 35):
            #print("z", z)
            for x in range(-35, 35):
                val = []
                for y in range(-35, 35):
                    state = cposval(x, y, z, w)
                    if state :
                        cnt.append((x, y, z, w))
                    val.append(str)
    print(len(cnt),cnt)


def printMatrix():
    for z in range(-1, 2):
        print("z", z)
        for x in range(0, 5):
            val = []
            for y in range(0, 5):
                state = cposval(x, y, z)
                str = '#' if state else "."
                val.append(str)
            print(val)


#printMatrix()

def neighbourStateCount(x, y, z, w) :
    mapping = []
    for nx in range(x-1, x+2):
        for ny in range(y-1, y+2):
            for nz in range(z-1, z+2):
                for nw in range(w - 1, w + 2):
                    #print((x, y,z),"chk",(nx, ny, nz),cposval(nx,ny,nz))
                    mapping.append(cposval(nx,ny,nz,nw))
    return mapping


for loop in range(0,6) :
    countEnabled()
    updatepos = {}
    print("execute pass")
    for x in range(-15, 15):
        for y in range(-15, 15):
            for z in range(-15, 15):
                for w in range(-15, 15):
                    state = cposval(x,y,z,w)
                    mapping = neighbourStateCount(x,y,z,w)
                    tcount=mapping.count(True)
                    fcount = mapping.count(False)
                   # print(state, (x, y, z), tcount,fcount)
                    # print((x,y,z),mapping,tcount,fcount)
                    if state :
                        tcount = tcount-1
                        if tcount==2 or tcount==3 :
                            updatepos[(x, y, z, w)] = True
                        else :
                            updatepos[(x, y, z, w)] = False
                    else:
                        if tcount==3 :
                            updatepos[(x, y, z, w)] = True
                        else :
                            updatepos[(x, y, z, w)] = False

    for k in updatepos.keys() :
        cpos[k] = updatepos[k]


#printMatrix()
countEnabled()
