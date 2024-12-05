import re

f = open('day3input.txt', 'r')
data = f.read()

cleaned = re.findall("mul\(\d+,\d+\)", data)
multis = []

for operation in cleaned:
    multis.append(list(map(int, operation[4:-1].split(','))))

sum = 0

for multi in multis:
    sum += multi[0]*multi[1]

print(sum)

cond = re.split('do\(\)', data)
condcleaned = []

for item in cond:
    condcleaned.append(re.split("don't\(\)", item)[0])

condcleaned = ''.join(condcleaned)

condcleanedresults = re.findall("mul\(\d+,\d+\)", condcleaned)

condmultis = []

for operation in condcleanedresults:
    condmultis.append(list(map(int, operation[4:-1].split(','))))

condsum = 0

for multi in condmultis:
    condsum += multi[0]*multi[1]

print(condsum)