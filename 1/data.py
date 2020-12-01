f = open("data.txt", "r")
data = []
for d in f :
    data.append(int(d))

print(data)

for i in range(len(data)) :
    for j in range(len(data)):
        if i!=j :
           val = data[i]+data[j]
           print (data[i]*data[j]) if val == 2020 else ""

for i in range(len(data)) :
    for j in range(len(data)):
        for k in range(len(data)):
            if i!=j and  j!=k and k!=i :
               val = data[i]+data[j]+data[k]
               print (data[i]*data[j]*data[k]) if val == 2020 else ""