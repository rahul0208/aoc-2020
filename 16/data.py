
f = open("sample.txt", "r")
#f = open("sample2.txt", "r")
f = open("data.txt", "r")
fields = []
tickets = []
fieldChk = True

for d in f :
    str = d.rstrip()
    if fieldChk and len(str) > 0:
        fld = []
        fldDetail = str.split(": ")
        fld.append(fldDetail[0])
        fldVal = fldDetail[1].split('or')
        for chk in fldVal:
            vals = chk.split('-')
            fld.append([int(i) for i in vals])
        fields.append(fld)
    elif ',' in str :
        tickets.append([int(i) for i in str.split(",")])
    else :
        fieldChk = False


print(fields)
print(tickets)

cntMap = {}
for e in fields :
    cntMap[e[0]] = [0]*len(tickets[0])

def tktcnt(fname,idx) :
    fcount = cntMap[fname]
    fcount[idx] += 1
 #   print(fname)

def findInvalid(f, t) :
    idx = 0
    mappig = []
    for a in t :
        r = False
        for c in f:
            vls = c[1:]
            for crange in vls:
                if a>=crange[0] and a<=crange[1]:
                    r= True
                    mappig.append([c[0],idx])
        if not r :
#            print(a)
            return a
        idx += 1
    for m in mappig :
        tktcnt(m[0],m[1])
    return 0

error = 0


for t in tickets :
    error += findInvalid(fields,t)

print(error)
print(cntMap)
fldnames = [''] *len(tickets[0])
fillPos = True
while fillPos :
    fillPos = False
    for k in cntMap.keys() :
        kdata = cntMap.get(k)
        for i in range(0, len(fldnames)) :
            if len(fldnames[i]) > 0 :
                kdata[i] = 0
        mval = max(kdata)
        if kdata.count(mval) == 1 :
            p = kdata.index(mval)
            if(len(fldnames[p]) > 0) :
                print("some error found")
            else :
                fldnames[p] = k
                fillPos = True

    for i in range(0, len(fldnames)) :
        if len(fldnames[i]) > 0 and fldnames[i] in cntMap:
            cntMap.pop(fldnames[i])

print(fldnames)

departureval =1
for i in range(0, len(fldnames)) :
    print(fldnames[i], tickets[0][i])
    if fldnames[i].startswith('departure') :
        departureval = departureval*tickets[0][i]
print(departureval)
