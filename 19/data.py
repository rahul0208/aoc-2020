import sys

f = open("sample.txt", "r")
f = open("sample2.txt", "r")
f = open("data.txt", "r")
rule = [""]*1000
data = []
dataFlag = False


# print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
# print(sys.getrecursionlimit())

for d in f :
    dstr = d.rstrip()
    if dataFlag :
        data.append(dstr)
    else:
        if len(dstr) > 0 :
            v = dstr.split(':')
            idx = int(v[0].strip())
            # print(idx)
            rule[idx] = v[1].strip()
        else :
            dataFlag = True

print(rule[8])
print(rule[11])

def validateOrClaues(strval,rstr) :
    orValues= rstr.split("|") if "|" in rstr else [rstr]
    allMatch = 0
    for cl in orValues :
        match = validate(strval, cl.strip())
        if match > 0 :
            allMatch = match
            break;

    return allMatch

def validate(strval,rstr) :
    # print("check ",strval, rstr)
    match = 0
    if '"' in rstr:
        rval = rstr.replace('"','')
        reval = ''.join(strval).startswith(rval)
        # print("rval", rstr, rval, reval)
        return len(rval) if reval else match
    else :
        rexp=rstr.split(' ')
        for r in rexp :
            rpos = validateOrClaues(strval[match:], rule[int(r)])
            # print("idx", rstr, r, rpos)
            if rpos == 0 :
                match = 0
                break
            match += rpos
    return match


max_rec = 15

cntvals= 0
for i in range(1, max_rec):
    rule[8] = '|'.join(['42 ' * i])
    for j in range(1, max_rec):
        rule[11] = '|'.join(['42 ' * j + '31 ' * j])
        print(rule[8])
        print(rule[11])
        cnt = 0
        for d in data :
            vld = False
            # for rval in r0 :
            m = validateOrClaues(list(d), rule[0])
            vld = m == len(d)
            print(d,vld)
            cnt = cnt+1 if vld else cnt
        cntvals += cnt

print(cntvals)