
f = open("sample.txt", "r")
#f = open("sample2.txt", "r")
#f = open("data.txt", "r")
data = []

nospos = {}
for d in f :
    str = d.rstrip()
    n = str.split(",")
    idx = 0
    for i in n :
        data.append(int(i))
        nospos[int(i)]= idx
        idx += 1


nospos = {}

i = 0
last = None
lastpos = None
while i < 30000000 :
    spoken = None
    if(i < len(data)):
        spoken = data[i]
    else :
        spoken = 0
        if last in nospos:
            pos = nospos[last]
            spoken = i - pos -1
    print(spoken)
    nospos[last] = lastpos
    last = spoken
    lastpos = i
    i =i +1


print(data)

