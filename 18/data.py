
f = open("sample.txt", "r")
#f = open("sample2.txt", "r")
f = open("data.txt", "r")

data = []
for d in f :
    str = d.rstrip()
    data.append("( "+str+" )")

def processSimpleBrackest(exp) :
    items = list(exp)
    print(items)
    exp =[]
    for i in items :
        #print(exp)
        if i !='(' and i !=')' :
            t = exp.pop() + i
            exp.append(t)
        elif i =='(':
            exp.append("")
            pass
        elif i ==')':
            v=processv2(exp.pop())
          #  print(v)
            t = exp.pop()+ f'{v}' if len(exp) > 0 else f'{v}'
            exp.append(t)
#print('exp',exp)
    return exp.pop()


def procesAdd(exp) :
    items = list(exp)
    print(items)
    exp =[]
    for i in items :
        #print(exp)
        if i !='(' and i !=')' :
            t = exp.pop() + i
            exp.append(t)
        elif i =='(':
            exp.append("")
            pass
        elif i ==')':
            v=process(exp.pop())
          #  print(v)
            t = exp.pop()+ f'{v}' if len(exp) > 0 else f'{v}'
            exp.append(t)
#print('exp',exp)
    return exp.pop()


def processv2(exp) :
    items = exp.split(" ")
    d = []
    lastops = None
    for opr in items :
        if opr == '+' :
            lastops = opr
        elif opr.isdigit() :
            temp = int(opr)
            if lastops == "+" :
                temp = d.pop() + temp
            elif lastops == "*":
                temp = d.pop() * temp
            lastops = None
            d.append(temp)
    v = 1
    for i in d :
        v= v*i
    return v

def process(exp) :
    items = exp.split(" ")
    d = []
    lastops = None
    for opr in items :
        if opr == "+" or opr == "*" :
            lastops = opr
        elif opr.isdigit() :
            temp = int(opr)
            if lastops == "+" :
                temp = d.pop() + temp
            elif lastops == "*":
                temp = d.pop() * temp
            lastops = None
            d.append(temp)
    return d[0]

total = 0
for d in data :
    v=processSimpleBrackest(d)
    print(v)
    total += int(v)
print(total)

