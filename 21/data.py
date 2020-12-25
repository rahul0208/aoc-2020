
f = open("sample.txt", "r")
# f = open("sample2.txt", "r")
f = open("data.txt", "r")
data = []

for d in f :
    dstr = d.rstrip()
    parts = [dstr]
    if 'contains' in dstr :
        dstr =dstr.replace("(",'')
        dstr = dstr.replace(")",'')
        dstr = dstr.replace(",", '')
        parts = dstr.split("contains")
    v = []
    for p in parts :
        vals = p.strip().split(" ")
        v.append(vals)
    if (len(parts)) ==1 :
        v.append([])

    data.append(v)

print(data)


alergen = []
ing = []
for i in range(0,len(data)) :
    ing += data[i][0]
    alergen += data[i][1]

alergen = list(set(alergen))
ing = list(set(ing))

print(ing)
print(alergen)

ingalerMap = [["ING"]+alergen]

for i in range(0,len(ing)) :
    ingalerMap.append([ing[i]]+[0]*len(alergen))

for i in range(0,len(data)) :
    for j in data[i][0] :
        for k in data[i][1] :
            if(j=='mxmxvkd') :
                print(k)
            algIdx =alergen.index(k)
            ingIdx = ing.index(j)
            ingalerMap[ingIdx+1][algIdx+1] += 1

for i in range(0,len(ingalerMap)) :
    print(ingalerMap[i])

nonAlgIng = ing.copy()
for i in range(0,len(alergen)) :
    v = []
    for j in range(1, len(ingalerMap)):
        v.append(ingalerMap[j][i+1])
    mv = max(v)
    for j in range(1, len(ingalerMap)):
        if(ingalerMap[j][i+1] ==mv) :
            if ingalerMap[j][0] in nonAlgIng :
                nonAlgIng.remove(ingalerMap[j][0])


print(nonAlgIng)

cnt =0
for n in nonAlgIng :
    for d in data:
        if n in d[0] :
            cnt+=1

print(cnt)

ingAlgMap = {}
while len(ingAlgMap) != len(alergen):
    for i in range(0,len(alergen)) :
        if alergen[i] not in ingAlgMap.keys() :
            v = []
            for j in range(1, len(ingalerMap)):
                v.append(ingalerMap[j][i+1])
            mv = max(v)
            cnt = 0
            prev = None
            for j in range(1, len(ingalerMap)):
                if(ingalerMap[j][i+1] ==mv) :
                    if ingalerMap[j][0] not in ingAlgMap.values() :
                        cnt += 1
                        prev = ingalerMap[j][0]
            if cnt == 1 :
                ingAlgMap[alergen[i]] = prev

print(ingAlgMap)

v= []
for k in sorted(ingAlgMap.keys()) :
    v.append(ingAlgMap.get(k))
print(",".join(v))

