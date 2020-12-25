

f = open("sample.txt", "r")
# f = open("sample2.txt", "r")
# f = open("data.txt", "r")
data = []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

head = None
prev = None
for d in f :
    dstr = d.rstrip()
    for e in list(dstr):
        data.append(int(e))
        node = Node(int(e))
        if head == None :
            head = node
        if prev :
            prev.next = node
        prev = node



for i in range(max(data)+1,1000001):
    data.append(i)
    node = Node(i)
    if prev:
        prev.next = node
    prev = node

maxNos = 1000000
move = 0
selectedPos = 0
totalCups = len(data)
movelist = data.copy()
# print(datakeys)

while move < 10000000 :
    move += 1

    selectedCup = movelist[selectedPos]
    pickup = []
    if(move % 1000) == 0 :
        print(f'-- move {move} --')
    # print(f'movelist : {movelist}')
    # print(f'selected : {selectedCup}')
    minos = [1, 2, 3, 4, 5]
    manos = [maxNos, maxNos - 1, maxNos - 2, maxNos - 3, maxNos - 4]

    remIdx = []
    for i in range(selectedPos+1, selectedPos+4):
         pickup.append(movelist [i % totalCups])
         remIdx.append(i % totalCups)

    remIdx.sort(reverse=True)
    # print(remIdx)
    for i in remIdx :
        del movelist[i]

    # print(f'movelist : {movelist}')
    # print(f'pickup : {pickup}')

    if selectedCup in minos:
        minos.remove(selectedCup)
    if selectedCup in manos:
        manos.remove(selectedCup)

    for e in pickup :
        # movelist.remove(e)
        if e in minos :
            minos.remove(e)
        if e in manos :
            manos.remove(e)

    dest = None
    d =  selectedCup
    dmin = min(minos)
    dmax = max(manos)

    while dest == None :
        d = d-1
        if d > 0 and d != selectedCup and d not in pickup :
            dest = d
        if d < dmin:
            d = dmax+1
    # print(f'destinnation : {dest}')
    p = (movelist.index(selectedCup) + 1) % len(movelist)
    nxt = movelist[p]
    l = movelist.index(dest)
    for i in range(1, 4):
        pos =(l + i) % totalCups
        movelist.insert(pos, pickup[i-1])

    # print(f'next : {movelist[p]}, {movelist}')
    selectedPos = movelist.index(nxt)

startPos = movelist.index(1)
print(movelist[startPos+1])
print(movelist[startPos+2])

clocklist = []
for i in range(0, 10) :
    clocklist.append(str(movelist[(startPos+i)%totalCups]))

print(clocklist)
# print("".join(clocklist))