import re

f = open("sample.txt", "r")
#f = open("data.txt", "r")
data = []

for d in f :
    data.append(d.rstrip())

def checkcolor(color, data) :
    selected_color = []
    for i in range(0,len(data)):
        d = data[i]
        if color in d and not d.startswith(color):
            selected_color.append(d.split("bags contain")[0].strip())
    print(color, selected_color)
    return selected_color

colors = ["shiny gold"]

i=0
while i < len(colors):
    selected = checkcolor(colors[i],data)
    colors = colors + selected
    i = i+1

print(len(set(colors))-1)