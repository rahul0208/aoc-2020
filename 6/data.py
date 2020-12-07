import re

f = open("data.txt", "r")
data = []
memData = []

ans = ""
mem = 0
for d in f :
    if len(d.strip()) != 0:
        ans = ans + d.rstrip()
        mem = mem +1
    else :
        data.append(ans)
        memData.append(mem)
        ans = ""
        mem = 0
data.append(ans)
memData.append(mem)

az="abcdefghijklmnopqrstuvwxyz"
total = 0
print(data)
for p in range(0,len(data)):
    count = 0
    for i in range(0,len(az)):
        c = data[p].count(az[i])
        count= count+1 if memData[p]==c else count
 #       count= count+1 if az[i] in g else count
#    print(count)
    total = total + count
print (total)