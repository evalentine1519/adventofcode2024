f = open('day1input.txt', 'r')
data = f.read().splitlines()
firstlist = []
secondlist = []
resultlist = []
difference = 0


#Part 1
for item in data:
    temp = item.split('   ')
    firstlist.append(temp[0])
    secondlist.append(temp[1])

firstlist.sort()
secondlist.sort()

for (first, second) in zip(firstlist, secondlist):
    resultlist.append(abs(int(first)-int(second)))

for item in resultlist:
    difference += int(item)

print("Difference is: " + str(difference))

#Part 2
simlist = []
similarity = 0

for item in firstlist:
    simlist.append(secondlist.count(item))

for (item, freq) in zip(firstlist, simlist):
     similarity += (int(item) * int(freq))

print("Similarity is: " + str(similarity))