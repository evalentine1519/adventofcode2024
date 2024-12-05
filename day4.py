f = open('day4input.txt', 'r')
data = f.read().splitlines()

movements = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
diagmovements = [[(-1,1),(1,-1)],[(-1,-1),(1,1)]]
xmascount = 0
mascount = 0

#part 1
#search the rows
for i, row in enumerate(data):
    #search the letters in the rows
    for j, char in enumerate(row):
        if char == 'X':
            #if 'X' found, start searching each direction
            for move in movements:
                newi = i + move[0]
                newj = j + move[1]
                #if moving won't take us out of bounds and letter 2 is M
                if 0 <= newi < 140 and 0 <= newj < 140 and data[newi][newj] == 'M':

                    newi += move[0]
                    newj += move[1]
                    #if moving won't take us out of bounds and letter 3 is A
                    if 0 <= newi < 140 and 0 <= newj < 140 and data[newi][newj] == 'A':

                        newi += move[0]
                        newj += move[1]
                        #if moving won't take us out of bounds and letter 4 is S
                        if 0 <= newi < 140 and 0 <= newj < 140 and data[newi][newj] == 'S':

                            xmascount += 1
                        else:
                            continue
                    else:
                        continue
                else:
                    continue

print(xmascount)

#part 2
for i, row in enumerate(data):
    for j, char in enumerate(row):
        chars = []
        if char == 'A':
            for move in diagmovements:
                newi = i + move[0][0]
                newj = j + move[0][1]
                newii = i + move[1][0]
                newjj = j + move[1][1]

                inboundij = False
                inboundiijj = False
                if 0 <= newi < 140 and 0 <= newj < 140:
                    inboundij = True
                
                if 0 <= newii < 140 and 0 <= newjj < 140:
                    inboundiijj = True

                if inboundij and data[newi][newj] == 'M':
                    if inboundiijj and data[newii][newjj] == 'S':
                        chars.append(data[newi][newj])
                        chars.append(data[newii][newjj])
                    else:
                        break
                elif inboundij and data[newi][newj] == 'S':
                    if inboundiijj and data[newii][newjj] == 'M':
                        chars.append(data[newi][newj])
                        chars.append(data[newii][newjj])
                    else:
                        break
                else:
                    break

            if len(chars) == 4 and chars.count('S') == 2 and chars.count('M') == 2:
                mascount += 1

print(mascount)