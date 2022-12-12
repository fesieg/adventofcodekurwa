import utils.fileReader as fr

global forest
forest = fr.getTextFileContentAsListOfLines('data/day8.md', trim=True)

def isVisible(line, index, direction: str):
    if direction == "left" or direction == "top":
        return not max(line[:index]) >= line[index]

    elif direction == "right" or direction == "bottom":
        return not max(line[index + 1:]) >= line[index]


def getScenicScore(line, index, direction: str):
    distance = 0
    if direction == "right" or direction == "bottom":
        for step in range(index, len(line) - 1):
            distance = distance + 1
            if step != index and line[step] >= line[index]:
                break

    elif direction == "top" or direction == "left":
        for step in range(index, 0, -1):
            if step != index and line[step] >= line[index]:
                break
            distance = distance + 1


    return distance



def getResultPart1():
    visibleCount = 0

    for nLine in range(1, len(forest) - 1):
        for nTree in range(1, len(forest[nLine]) - 1):
            horizontalLine = [int(n) for n in forest[nLine]]
            verticalLine = [int(line[nTree]) for line in forest]

            if True in [isVisible(horizontalLine, nTree, "left"),
                isVisible(horizontalLine, nTree, "right"),
                isVisible(verticalLine, nLine, "top"),
                isVisible(verticalLine, nLine, "bottom")]: visibleCount += 1


    visibleCount += len(forest) * 2
    visibleCount += len(forest[0]) * 2
    visibleCount -= 4
    return visibleCount

def getResultPart2():
    highestScenicScore = 0

    for nLine in range(0, len(forest)):
        for nTree in range(0, len(forest[nLine])):
            totalScenicScore = 0

            horizontalLine = [int(n) for n in forest[nLine]]
            verticalLine = [int(line[nTree]) for line in forest]

            treesVisible = [getScenicScore(horizontalLine, nTree, "left"),
                getScenicScore(horizontalLine, nTree, "right"),
                getScenicScore(verticalLine, nLine, "top"),
                getScenicScore(verticalLine, nLine, "bottom")]

            totalScenicScore = treesVisible[0] * treesVisible[1] * treesVisible[2] * treesVisible[3]

            if totalScenicScore > highestScenicScore:
                highestScenicScore = totalScenicScore

    return highestScenicScore 

print(getResultPart2())