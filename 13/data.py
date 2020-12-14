
f = open("sample.txt", "r")
# f = open("sample2.txt", "r")
f = open("data.txt", "r")
data = []

for d in f :
    data.append(d.rstrip().split(","))

print(data)
arr = int(data[0][0])

nos =[]
for i in range(0, len(data[1])) :
    if(data[1][i]!='x') :
        nos.append(int(data[1][i]))
    else :
        nos.append((data[1][i]))
print(nos)
#print(nos.sort())
print(nos)


def findMinX(num, rem, k):
    x = 100000000000000;  # Initialize result

    # As per the Chinise remainder
    # theorem, this loop will
    # always break.
    while (True):

        # Check if remainder of
        # x % num[j] is rem[j]
        # or not (for all j from
        # 0 to k-1)
        j = 0;
        while (j < k):
            if (x % num[j] != rem[j]):
                break;
            j += 1;

            # If all remainders
        # matched, we found x
        if (j == k):
            return x;

            # Else try next numner
        x += 1;

n = []
r = []
idx = []
for i in range(0, len(nos)) :
    if(nos[i]!='x') :
        n.append(int(nos[i]))
        idx.append(i)
        if(i> 0) :
            r.append(abs(nos[i]-i))
        else :
            r.append(i)
print(n)
print(idx)
print(r)

#print("x is", findMinX(n, r, len(r)));

busid = None
ts = 1
#chk =[False]*len(nos)
inc = 1
i = 0
while i < len(n):
   # ts = ts + inc
  #  if nos[i]=='x'
    while ts % n[i] != 0 :
        ts = ts + inc + r[i]
    inc = inc * n[i]
    print(ts, inc, i, n[i])
    i = i+1



print(ts,inc)



