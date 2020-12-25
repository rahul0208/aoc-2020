

f = open("sample.txt", "r")
# f = open("sample2.txt", "r")
f = open("data.txt", "r")
data = []


for d in f :
    dstr = d.rstrip()
    data.append(int(dstr))

print(data)

cnt = 1

val = 1
tmp = {}
while True:
    val = val * 7
    val = val % 20201227
    # print(val)
    if val in data :
        tmp[val] = cnt
    if len(tmp.keys()) == len(data):
        break
    cnt += 1


print(tmp)

val = 1
maxloop =  tmp.get(data[0])
cnt = 1
while cnt < maxloop+1 :
    val = val * data[1]
    val = val % 20201227
    cnt += 1
print(val)