f = open('day4input.txt', 'r')
data = f.read().splitlines()

movements = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
count = 0

#search the rows
for i, row in enumerate(data):
    #search the letters in the rows
    for j, char in enumerate(row):
        if char == 'X':
            #print("X found at: " + str(i) + ',' + str(j))
            #if 'X' found, start searching each direction
            for move in movements:
                newi = i + move[0]
                newj = j + move[1]
                #if moving won't take us out of bounds and letter 2 is M
                if 0 <= newi < 140 and 0 <= newj < 140 and data[newi][newj] == 'M':
                    #print("M found at: " + str(newi) + ',' + str(newj))
                    newi += move[0]
                    newj += move[1]
                    #if moving won't take us out of bounds and letter 3 is A
                    if 0 <= newi < 140 and 0 <= newj < 140 and data[newi][newj] == 'A':
                        #print("A found at: " + str(newi) + ',' + str(newj))
                        newi += move[0]
                        newj += move[1]
                        #if moving won't take us out of bounds and letter 4 is S
                        if 0 <= newi < 140 and 0 <= newj < 140 and data[newi][newj] == 'S':
                            #print("S found at: " + str(newi) + ',' + str(newj))
                            count += 1
                        else:
                            continue
                    else:
                        continue
                else:
                    continue

print(count)