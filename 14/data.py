
f = open("sample.txt", "r")
f = open("sample2.txt", "r")
f = open("data.txt", "r")
data = []

mask =""
for d in f :
    str = d.rstrip()
    val= str.split("=")
    if "mask"== val[0].strip() :
        mask = val[1].strip()
        # print(len(mask))
    else :
        val2=int(val[1].strip())
        idx=int(val[0].split("[")[1].split("]")[0])
        data.append([mask, val[0].strip(), int(val[1].strip()),'{0:b}'.format(idx)])

print(data)

for d in data :
    pro = list(d[0])
    i = 1
    start = list(d[3])
    while i  <= len(pro) :
        if pro[len(pro) - i] == 'X':
            # if ( i > len(start)) :
            #     pro[len(pro) - i] = 0
            # else :
            pro[len(pro) - i] = 'X'
        elif pro[len(pro) - i] == '0':
            if (i > len(start)):
                pro[len(pro) - i] = 0
            else :
                pro[len(pro) - i] = int(start[len(start) - i])
        else :
            pro[len(pro) - i] = int(pro[len(pro) - i])
        i = i+1
    d.append(pro)
    # print(pro)

# print(data)

def computeval(arr):
    i = 0
    s = 0
    while i < len(arr):
        v = pow(2,i)
        s= s+ v* arr[len(arr)-i-1]
        i = i+1
    return s

def computeloc(arr):
    i = 0
    s = [[0]*len(arr)]
    cx =0
    # print(s)
    while i < len(arr):
        c = arr[len(arr) - i - 1]
        if c!='X' :
            for j in range(0,len(s)):
                s[j][len(arr) - i - 1]=c
        else :
            cx += 1
            cls = []
            for j in range(0,len(s)):
                cl = s[j].copy()
                # print(s[j])
                s[j][len(arr) - i - 1]=0
                cl[len(arr) - i - 1]=1
                cls.append(cl)
            s = s+cls
        i = i+1
    sval=[]
    print(arr, cx, len(s), len(arr))
    for j in range(0,len(s)):
        sval.append(computeval(s[j]))
    return sval

key = {}
for d in data :
    val  = computeloc(d[4])
    print(val,d[2])
    for j in range(0, len(val)):
        key[val[j]]=d[2]

v = 0
for e in key.keys() :
    v += key.get(e)

print(key)
print(v)
