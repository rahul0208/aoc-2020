import re

f = open("data.txt", "r")
data = []

def seatId(val) :
    fbPos = range(0, 127)
    fbStart = 0
    fbEnd = len(fbPos)
#    print(fbEnd)
    for i in range(7):
        delta = (fbEnd - fbStart) / 2
        if val[i]=='F' :
            fbEnd = int(fbEnd - delta - 0.5)
        else :
            fbStart = int(fbStart + delta + 0.5)
        print(fbStart, fbEnd)

    lrPos= range(0,7)
    lrStart = 0
    lrEnd = len(lrPos)

    for i in range(3):
        delta = (lrEnd - lrStart) / 2
        if val[7+i]=='L' :
            lrEnd = int(lrEnd - delta - 0.5)
        else :
            lrStart = int(lrStart + delta + 0.5)
        print(lrStart, lrEnd)

    if(fbStart!=fbEnd) :
        raise AssertionError("FB")
    if (lrStart != lrEnd):
        raise AssertionError("LR")
    return  fbStart * 8 + lrStart

seatIndex = [False]*1000

maxid = 0
for d in f :
    s = seatId(d.rstrip())
    seatIndex[s-1] = True
    if(s > maxid) :
        maxid = s
    print(s)

print (maxid)

for i in range(0,len(seatIndex)) :
    if seatIndex[i] == False :
        print(i+1, seatIndex[i])