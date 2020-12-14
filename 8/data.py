
f = open("sample.txt", "r")
f = open("data.txt", "r")
data = []

for d in f :
    data.append(d.rstrip())

idx = [False]*len(data)
print(data)

acc = 0
i=0
b = 3
accJmp = []
prevJmp = []
#print(len(data))
while i < len(data):
    cmd = data[i]
    idx[i] = True
    if cmd.startswith("acc") :
       if '+' in cmd :
           acc = acc + int(cmd.split('+')[1])
       else:
           acc = acc - int(cmd.split('-')[1])

    if cmd.startswith("jmp"):
        accJmp.append(acc)
        prevJmp.append(i)
        if '+' in cmd:
            i = i + int(cmd.split('+')[1])
        else:
            i = i - int(cmd.split('-')[1])
    else :
        i = i+1

    if i < len(idx) and idx[i] :
         if ( b ==0 ) :
             print("loop", acc, i)
             break
         while b > 0 :
            i = prevJmp.pop() + 1
            acc = accJmp.pop()
            b = b -1

 #        print("update", acc, i)

print("final", acc)