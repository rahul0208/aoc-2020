f = open("data.txt", "r")
data = []

idx=1
count = 0
pos =0
for d in f :
    pos = pos +1
    str = d.rstrip()*100
    print (pos, idx, count, str )
    if pos % 2 == 1 : ## run without this check for part 1
        count = count + 1 if (str[idx-1] == '#')  else count
        idx = idx+1 ## inc as 1 ,3,5,7
print(count)
