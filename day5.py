def ruleCheck(update, rules):
    isGood = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) < update.index(rule[1]):
                continue
            else:
                isGood = False
                break

    return isGood

def orderFixer(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) < update.index(rule[1]):
                continue
            else:
                indexOne = update.index(rule[0])
                indexTwo = update.index(rule[1])
                update.pop(indexOne)
                update.pop(indexTwo)
                update.insert(indexOne, rule[1])
                update.insert(indexTwo, rule[0])

f = open('day5input.txt', 'r')
data = f.read().splitlines()

splitpoint = data.index('')

rules = data[:splitpoint]
updates = data[splitpoint+1:]
updatesClean = []
rulesClean = []
correctOrder = []
wrongOrder = []
middlePagesCorrect = 0
middlePagesWrong = 0

for rule in rules:
    rulesClean.append(rule.split('|'))

for update in updates:
    updatesClean.append(update.split(','))


for update in updatesClean:
    if ruleCheck(update, rulesClean):
        correctOrder.append(update)
    else:
        wrongOrder.append(update)

for update in wrongOrder:
    while ruleCheck(update, rulesClean) is False:
        orderFixer(update, rulesClean)

for update in wrongOrder:
    middlePagesWrong += int(update[len(update)//2])

for update in correctOrder:
    middlePagesCorrect += int(update[len(update)//2])

print(middlePagesCorrect)
print(middlePagesWrong)