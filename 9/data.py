
f = open("sample.txt", "r")
f = open("data.txt", "r")
data = []

for d in f :
    data.append(int(d.rstrip()))

pos=25

def checkSum(total,arr) :
 #   print(total,arr)
    for i in range(0, len(arr)):
        diff = total - arr[i]
        check= arr.copy()
        check[i] =0
#        print(check)
        if diff in check :
            return True;
    return False

def smallarry(arr) :
    val = arr[0]
    for i in range(0, len(arr)):
        if (val < arr[i] ):
            val=arr[i]
    return  val

def large(arr) :
    val = arr[0]
    for i in range(0, len(arr)):
        if (val > arr[i] ):
            val=arr[i]
    return  val

def findtotal (total,arr) :
    print("find",total, len(arr))
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
             e = len(arr)-(j-i)
             dataarr = arr[i:e]
             d = sum(dataarr)
             if (d == total) :
                 print("sum is",smallarry(dataarr)+large(dataarr))

for i in range(pos, len(data)):
    val = checkSum(data[i],data[i-pos:i] )
    print(val, data[i])
    if not val :
        findtotal(data[i],data[0:i])
        break