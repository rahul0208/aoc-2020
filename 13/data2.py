with open('sample.txt') as f:
    inputs = [line.rstrip('\n') for line in f]


bus_time_offsets = []
for i, t in enumerate(inputs[1].split(',')):
    if t == 'x':
        continue
    bus_time_offsets.append((int(t), i))

position = 0
increment = bus_time_offsets[0][0]

print(bus_time_offsets, increment)

for bus_time, bus_offset in bus_time_offsets[1:]:
    print(position,bus_time, bus_offset, increment)
    while True:
        position += increment
        if (position + bus_offset) % bus_time == 0:
            break
    increment = increment * bus_time
print(position)