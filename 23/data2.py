

f = open("sample.txt", "r")
# f = open("sample2.txt", "r")
f = open("data.txt", "r")
data = []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

nodeMap = {}

head = None
prev = None
for d in f :
    dstr = d.rstrip()
    for e in list(dstr):
        data.append(int(e))
        node = Node(int(e))
        nodeMap[node.data] = node
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
    nodeMap[node.data] = node

maxNos = max(data) #1000000
move = 0
selectedPos = 0
# print(datakeys)
selectedNode = None
def getNodes():
    printNode = head
    arr =[]
    while printNode != None :
        arr.append(printNode.data)
        printNode = printNode.next
    return arr

while move < 10000000 :
    move += 1
    if selectedNode == None :
        selectedNode =head

    selectedCup = selectedNode.data

    pickup = []

    print(f'-- move {move} --')
    # print(getNodes())
    # print(f'movelist : {movelist}')
    # print(f'selected : {selectedCup}')
    minos = [1, 2, 3, 4, 5]
    manos = [maxNos, maxNos - 1, maxNos - 2, maxNos - 3, maxNos - 4]

    remIdx = []
    pickNode = selectedNode.next

    prevPickNode = None
    for i in range(0, 3):
        if pickNode== None:
            pickNode=head
        pickup.append(pickNode.data)
        prevPickNode = pickNode
        pickNode = pickNode.next
    pickNode =prevPickNode


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

    # print(f'destination : {dest}')

    # p = (movelist.index(selectedCup) + 1) % len(movelist)
    # nxt = movelist[p]
    statPickNode = selectedNode.next
    selectedNode.next = pickNode.next
    pickNode.next = None
    # print(getNodes())

    destNode = nodeMap.get(dest)
    pickNode.next = destNode.next
    destNode.next = statPickNode
    # nextNode = pickNode.next

    selectedNode = selectedNode.next


printNode = head
f = False
arr =[]
while printNode != None and len(arr) < 5:
    if(printNode.data ==1):
        f = True
    if f:
        arr.append(printNode.data)
    printNode = printNode.next

print(arr)
print(arr[1]*arr[2])

# print("".join(clocklist))