#f = open("sample.txt", "r")
f = open("data.txt", "r")
data = []
colors = []

for d in f :
    data.append(d.rstrip())
    colors.append(d.split("bags contain")[0].strip())

def combo(colors, d) :
    count = []

    for i in range(0,len(colors)):
        color = colors[i]
        if color in d and not d.startswith(color):
            numstr=d.split(color)[0].strip()
            parts=numstr.split(" ");
            count.append(int(parts[len(parts)-1].strip()))
        else :
            count.append(0)

    return count

i=0
matrix=[]
while i < len(data):
    numbers = combo(colors,data[i])
    matrix.append(numbers)
    i = i+1

print(matrix)

i=0;

def count(color,colors, matrix) :
    indexof = colors.index(color)
    val =1
    for j in range(0,len(matrix[indexof])) :
        if(matrix[indexof][j] > 0) :
            val= val + matrix[indexof][j]*count(colors[j], colors, matrix)
    return val


def bags(color,colors, matrix) :
    indexof = colors.index(color)
    val = set([color])
    for j in range(0,len(matrix[indexof])) :
        if(matrix[j][indexof] > 0) :
            val.update(bags(colors[j], colors, matrix))
    return val

print(count("shiny gold",colors,matrix)-1)
print(len(bags("shiny gold",colors,matrix))-1)