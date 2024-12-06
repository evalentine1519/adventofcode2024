f = open('day6input.txt', 'r')
data = f.read().splitlines()

movements = [(-1,0), (0,1), (1,0), (0,-1)]
direction = 0

print(type(data))
print(type(data[0]))
print(data[0])

rowsCleaned = []
inBound = True


for row in data:
    rowsCleaned.append(list(row))

print(type(rowsCleaned))
print(type(rowsCleaned[0]))
print(rowsCleaned[0:2])

#get initial position of guard
for i, row in enumerate(rowsCleaned):
    for j, position in enumerate(row):
        if position == "^":
            initialPos = (i, j)

guardPos = [initialPos[0], initialPos[1]]

#walk guard through map until they leave boundary
while inBound:
    guardPos[0] += movements[direction][0]
    guardPos[1] += movements[direction][1]
