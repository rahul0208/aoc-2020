
f = open("sample.txt", "r")
f = open("data.txt", "r")
data = []

for d in f :
    data.append(int(d.rstrip()))

def fuc1(v, d) :
    for inc in range(1,4) :
        if v+inc in d :
            return v+inc
    return v

start = 0
diff1 =0
diff3 =0
all = []
all1 = []
all3 = []
for i in range(0, len(data)) :
    v = fuc1(start,data)
    all.append(v)
    if v-start ==1 :
        diff1 = diff1+1
        all1.append(v)
    if v-start ==3 :
        diff3 = diff3+1
        all3.append(v)
        all3.append(start)
    start = v
all3.append(all[len(all)-1])
#all.append(all[len(all)-1]+3)

print(diff1, diff3+1, diff1*(diff3+1))

#print(all1)
print(set(all3))
print(all)

combi=[0]*len(all)

for i in range(0,len(all)):
    if all[i] in all3 :
        combi[i] = 1

print(combi)

zeroct =0
val = 1
for i in range(0,len(combi)):
    if combi[i] == 0 :
        zeroct = zeroct + 1;
    if combi[i] == 1 :
        if zeroct == 3 :
            val = val*7
        if zeroct == 2 :
            val = val *4
        if zeroct == 1 :
            val = val *2
        zeroct =0

print("val",val)

# start = 0
# com=[[0]]
# i =0
#
# end=all[len(all)-1]
# idx=0
# while i < len(com) :
#     if i < 0 :
#         print(i)
#     f = com[i]
#     start = f[len(f)-1]
#     idx =0
#     if start  in all :
#         idx= all.index(start)
#     trnc=all[idx:idx+6]
#     for inc in range(1,4) :
#         v = start + inc
#         vcheck= (v+1 in trnc or v+2 in trnc or v+3 in trnc) or v==end
#         if v in trnc and vcheck:
#            # print(v, vcheck)
#             v= start+inc
#             d = [v]
#           #  print(start, f, v,d)
#             com.append(d)
# #    print(i)
#     i=i+1
#
# print(len(com))
#
# inc =0
# for i in range(0,len(com)) :
#     f = com[i]
#     start = f[len(f) - 1]
#     if(start==all[len(all)-1]):
#        # print("valid",f)
#         inc = inc+1
# print(inc)