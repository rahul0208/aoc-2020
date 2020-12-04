import re

f = open("data.txt", "r")
data = []

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

pas =[]
data ={}
for d in f :
    if len(d.strip()) != 0:
        d = d.rstrip()
        res = dict(item.split(":") for item in d.split(" "))
        data.update(res)
    else :
         pas.append(data)
         data = {}
pas.append(data)
#print(len(pas))
count = 0

def  checkByr(d) :
 #   print('checkByr')
    try:
        val = int(d)
        return val >= 1920 and val <= 2002
    except ValueError:
        return False

def  checkiyr(d) :
#    print('checkiyr')
    try:
        val = int(d)
        return val >= 2010 and val <= 2020
    except ValueError:
        return False

def  checkeyr(d) :
#    print('checkeyr')
    try:
        val = int(d)
        return val >= 2020 and val <= 2030
    except ValueError:
        return False

def  checkhgt(d) :
#    print('checkhgt')
    if d.endswith('in'):
        d = d.replace('in','')
        try:
            inval = int(d)
            return inval >= 59 and inval <= 76
        except ValueError:
            return False

    if d.endswith('cm'):
        d = d.replace('cm','')
        try:
            cmval = int(d)
            return cmval >= 150 and cmval <= 193
        except ValueError:
            return False

    return False

def  checkecl(d) :
#    print('checkecl')
    vals=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return d.rstrip() in vals

def  checkhcl(d) :
#    print("checkhcl")
    d = d.rstrip()
    if d.startswith('#') and len(d) == 7 :
        test_string= d.replace('#','')
        str="abcdef0987654321"
        val = 0
        for i in range(len(test_string)) :
            if test_string[i] in str :
                val = val+1
        return  val==6
    return False

def  checkpid(d) :
    d = d.rstrip()
    if len(d) == 9 :
        return d.isdigit()
    return False

for p in pas :
    keys = p.keys()
    if fields[0] in keys and checkByr(p[fields[0]])\
            and fields[1] in keys and checkiyr(p[fields[1]])\
            and fields[2] in keys and checkeyr(p[fields[2]])\
            and fields[3] in keys and checkhgt(p[fields[3]])\
            and fields[4] in keys and checkhcl(p[fields[4]])\
            and fields[5] in keys and checkecl(p[fields[5]])\
            and fields[6] in keys and checkpid(p[fields[6]]):
        count = count+1
    else :
        print(p)
print(count)