f = open("data.txt", "r")
data = []
for d in f :
    val=d.split(' ')
    o=val[0].split('-')
    data.append([
        int(o[0]),int(o[1]),
        val[1],val[2]]
    )
print(data)
valid =0
valid2 =0
for i in range(len(data)) :
    mi = data[i][0]
    ma = data[i][1]
    c = data[i][2][0]
    str = data[i][3]
    count = str.count(c)
    print (mi, ma, c , str,count )
    valid = valid+1  if (mi <=count and count<=ma) else valid
    mincheck = len(str)>= mi and str[mi - 1] == c
    maxcheck = len(str) >= ma and str[ma - 1] == c
    valid2 = valid2+ 1 if (mincheck and not maxcheck) else valid2
    valid2 = valid2 + 1 if (not mincheck and maxcheck) else valid2

print(valid)
print(valid2)
