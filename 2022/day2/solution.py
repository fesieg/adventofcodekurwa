import utils.fileReader as fr

# bonus = language agnostic

textInput = fr.getTextFileContentAsList('data/day2.md', trim=True)

pointValues = { 'A': 1,'X': 1,'B': 2,'Y': 2, 'C': 3, 'Z': 3 }

def isWin(opp, me):
    # opps value - our value = 2 is a loss if they chose the 3-value option
    if pointValues[opp] == 3:
        return (pointValues[opp] - pointValues[me]) == 2
    else:
        # otherwise, losing means not getting -1 as the result of opp value - our value
        return (pointValues[opp] - pointValues[me]) == -1


def isDraw(opp, me):
    return pointValues[opp] - pointValues[me] == 0


def resolveMatch(opp, me):
    if isDraw(opp, me):
        return pointValues[me] + 3
    elif isWin(opp, me):
        return pointValues[me] + 6
    else:
        return pointValues[me]


def resolveMatchWithFixedSolution(opp, solution):
    if pointValues[solution] == 1:
        # we need to lose
        for option in ['X', 'Y', 'Z']:
            if not isWin(opp, option) and not isDraw(opp, option):
                return resolveMatch(opp, option)
        
    elif pointValues[solution] == 2:
        # we need to draw
        for option in ['X', 'Y', 'Z']:
            if isDraw(opp, option):
                return resolveMatch(opp, option)

    if pointValues[solution] == 3:
        # we need to win
        for option in ['X', 'Y', 'Z']:
            if isWin(opp, option):
                return resolveMatch(opp, option)

        

def part1():
    total = 0
    for r in [[line[0], line[2]] for line in textInput]:
        total += resolveMatch(r[0], r[1])
    return total

def part2():
    total = 0
    for r in [[line[0], line[2]] for line in textInput]:
        total += resolveMatchWithFixedSolution(r[0], r[1])
    return total

print(part1())
print(part2())
