
f = open("sample.txt", "r")
# f = open("sample2.txt", "r")
#f = open("data.txt", "r")
data = []

for d in f :
    data.append(d.rstrip())


def move(x, y, d) :
    print("s", x,y, d)
    if(d.startswith('E')):
        v=int(d[1:])
        x=x+v
    if (d.startswith('W')):
        v = int(d[1:])
        x = x - v
    if (d.startswith('N')):
        v = int(d[1:])
        y = y + v
    if (d.startswith('S')):
        v = int(d[1:])
        y = y - v
   # print("E",x, y, d)
    return x,y

def move2(x, y, d) :
    print("moce2")

x=10
y=1
F='E'
pos=0
px = 0
py = 0
for d in data :
    if (d.startswith('R')):
        v = int(d[1:])
        pos = pos+v/90
        pos = pos%4
        tx, ty = x, y
        print("shift by", pos)
        while(pos > 0) :
            tx,ty = ty, -tx
            pos = pos - 1
        x, y = tx, ty
    elif (d.startswith('L')):
        v = int(d[1:])
        pos = pos + v / 90
        pos = pos % 4
        tx, ty = x, y
        print("shift by", pos)
        while (pos > 0):
            tx, ty = -ty, tx
            pos = pos - 1
        x, y = tx, ty
    elif (d.startswith('F')):
        v = int(d[1:])
        px = px+v*x
        py = py+v*y
        print("F",px, py)
    else :
        (x, y) = move(x, y, d)
    print(x,y)
print(x, y, abs(px)+abs(py))